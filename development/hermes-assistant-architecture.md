# Hermes assistant architecture

Design contract for the first Hermes-backed Hornero Assistant
vertical slice. Implementation follows this document; where code
and this document disagree, code wins and this document must be
fixed.

## Decision summary

- **Backend**: Hermes Agent (Nous Research, MIT), studied at
  `f14699a1379838862d3020b97785796aa555d36d`. Hermes is the
  reasoning, tool-use, skills, and memory engine. HorneroOS
  does not reimplement an agent loop and does not fork Hermes.
- **Transport**: Hermes gateway API server — OpenAI-compatible
  HTTP/SSE on `127.0.0.1:8642` with a Bearer `API_SERVER_KEY`
  (`gateway/platforms/api_server.py` in Hermes). Chosen over
  the TUI JSON-RPC stdio gateway (fragile process lifecycle,
  host auto-approve behavior) and ACP (version-skew errors;
  sessions not owned by the API surface).
- **Process model**: a user-level Hornero assistant service
  (never root) owns the Hermes lifecycle. As shipped
  (hornero#174), enabling the assistant never starts anything:
  `horneroctl assistant gateway start --yes` writes and starts
  the `hornero-hermes.service` systemd user unit, and
  `gateway stop --yes` stops only that unit. The shell never
  orchestrates models.
- **UI**: Hornero Companion (Quickshell/QML) is presentation
  only, per ADR 002 in the shell repository. Existing reserved
  states `listening / thinking / acting / success / warning /
  error` map to assistant activity; existing Companion IPC
  remains the presentation boundary.

## Gateway lifecycle (shipped, hornero#174)

`horneroctl assistant gateway` owns start/stop of the gateway:

- `gateway status` (default): reports the classified state —
  `disabled`, `not-installed`, `installed-not-running`,
  `running-incompatible` or `running-compatible` — plus the
  `hornero-hermes.service` user-unit state. The same
  classification appears as `state` in `assistant health`.
- `gateway start --yes`: requires the assistant enabled and
  Hermes on PATH (install guidance names a pinned, auditable
  package; this CLI never downloads Hermes). It writes
  `~/.config/systemd/user/hornero-hermes.service` only when the
  content changed, daemon-reloads, and starts the unit. If the
  gateway already answers, it reports that and starts no
  duplicate. Without a systemd user session it degrades to
  "run `hermes gateway run` manually" guidance.
- `gateway stop --yes`: stops only the unit Hornero manages. A
  gateway started elsewhere is reported, never killed: Hornero
  does not terminate processes it does not own.

Neither command needs root, enables anything at login, or
widens the loopback endpoint. Both require explicit `--yes`
(`--dry-run` previews), matching `assistant enable`.

`horneroctl assistant setup [--dry-run|--yes]` performs the
Hornero-owned half of standing Hermes up (hornero#191):
enablement with the 0600 key, the gateway unit, and the
Hornero skill installed into the Hermes home from an embedded
copy (refreshed only when changed). When Hermes is missing it
fails before changing anything and prints the pinned source
contract — NousResearch/hermes-agent at the studied commit,
user-local layout — because horneroctl never downloads Hermes
and never runs a remote install script. `setup --remove`
reverses only what setup wrote (a user-modified skill is kept
and reported); the Hermes installation itself is user-owned.
Shipping the Hermes binary as a package remains an installer
track decision.

`assistant knowledge` exports the live read-only catalogue as
a bounded Markdown snapshot (dated, provenance-stamped) for
agents that cannot execute commands; the live
`assistant tools --json` stays the truth.

## Transport contract (from Hermes source)

| Operation | Endpoint |
|---|---|
| Capabilities | `GET /v1/capabilities` |
| Start run | `POST /v1/runs` |
| Stream events | `GET /v1/runs/{id}/events` |
| Cancel | `POST /v1/runs/{id}/stop` |
| Approval | `POST /v1/runs/{id}/approval` |
| Clarify | `POST /v1/runs/{id}/clarify` |

Notes:

- Capabilities are negotiated before any run; expectations are
  pinned per supported Hermes version.
- Start sends an `Idempotency-Key`. Sessions are API-owned:
  foreign CLI/TUI/ACP sessions return 409, so the assistant
  creates and keeps its own sessions.
- Events stream over SSE: tokens, tool activity, and approval
  requests.
- Cancel must wire to the UI cancel action and to Companion
  success/error states.
- Hermes asks for approval; the user decides in native UI.
  Approvals are never auto-answered.

Authentication: a Bearer key generated per user, stored with
restrictive permissions (`0600`) in the user config directory,
never committed, never logged. Loopback only; no listener
leaves `127.0.0.1`.

## First vertical slice (scope)

1. The user explicitly enables the assistant (Settings and
   Companion surface, with `horneroctl` parity). Default:
   **disabled**. The normal desktop is complete with Hermes
   absent.
2. The service initializes Hermes. Health means a successful
   `GET /v1/capabilities`.
3. Companion opens a conversation; the user sends a message;
   Hermes streams a real response; Companion shows thinking
   and speaking states.
4. Read-only native tools (below) are callable by Hermes.
   Tool activity is visible in the UI. The user can cancel
   mid-run.
5. Questions like "why is my system using memory" or "what
   updates exist" are answered from real `horneroctl` output,
   never hardcoded replies.
6. Failure paths — Hermes missing, wrong version, port
   conflict, provider unconfigured — each yield a human
   recovery message, never a stack trace.
7. Disable stops the integration and the daemon. Zero idle
   cost when off.

## Native tool catalogue (slice 1: read-only only)

Exposed as literal argv through the existing `hornero_core`
exec boundary (no shell interpolation). All return the uniform
`--json` envelope. Class for every tool below: safe read.

- System information: `horneroctl system info --json`
- Appearance status: `horneroctl appearance status --json`
- Theme catalogue: `horneroctl appearance theme list --json`
  and `horneroctl appearance theme show <id> --json`
  (ids validated: `/`, `..`, and empty are rejected)
- GTK state: `horneroctl appearance gtk list --json` and
  `horneroctl appearance gtk current --json`
- Update check: `horneroctl package updates --json` and
  `horneroctl package check --json` (UX copy notes the ~30 s
  AUR lane)
- Companion state: `qs ipc call companion status`

Mutations (theme apply, package install, settings changes)
are **out of slice 1**. Slice 2 adds them only behind Hermes
approval surfaced in native UI, one capability at a time, each
with dry-run where `horneroctl` supports it.

## Security model

- Disabled by default; enabling is explicit and reversible.
- User-level service; no root, no polkit broadening in
  slice 1.
- Hermes' approval model is never weakened or auto-answered.
- No screenshots, clipboard, microphone, files, or window
  contents are exposed in slice 1. Each is a separate future
  capability with its own consent.
- Secrets: provider keys belong to Hermes' own configuration.
  Hornero stores only its local Bearer key, `0600`,
  user-owned.
- Prompt-injection posture: tool results are data, not
  instructions; the tool allowlist above is exhaustive for
  slice 1.
- Auditability: run and tool history stays in Hermes'
  session, plus a local, user-readable assistant log of tool
  invocations (command and result status, no secret material).

## Packaging and versions

- Hermes is installed through a reproducible, version-pinned,
  auditable path (Arch package or managed isolated runtime).
  Never `curl | bash`.
- The supported Hermes version range is recorded with the
  implementation; capability negotiation fails closed with an
  upgrade message. As implemented: Hermes exposes no gateway
  semver, so `horneroctl assistant status` negotiates the
  protocol — it requires platform `hermes-agent` plus the
  feature flags the client calls (`run_submission`,
  `run_events_sse`, `run_stop`, `run_approval_response`,
  `approval_events`) and reports the studied upstream commit
  (`f14699a13798…`) it was verified against. An incompatible
  gateway fails status with the exact missing capabilities.
- Install, upgrade, disable, and uninstall are separate,
  tested operations. Uninstall never removes user
  configuration without explicit consent.

## Performance gates

- Assistant disabled: zero processes, zero idle cost.
- Enabled but idle: daemon RSS/CPU is measured and recorded.
  No local model loads or weight downloads without explicit
  user action.
- Shell overhead: the streaming UI must not regress launcher
  or frame baselines (shell performance tooling owns the
  measurement).

## Acceptance tests (slice 1)

- Protocol compatibility against the pinned Hermes version
  (mock backend plus real Hermes).
- Streaming, cancellation, and reconnection after a daemon
  restart.
- Approval denial path: denial must block the action.
- Tool allowlist enforcement: a prompt asking for an unlisted
  action gets no execution.
- Disable and uninstall leave the ordinary desktop fully
  functional.
- Resource report for disabled, idle, and streaming states.

## Real-Hermes acceptance (executed 2026-10-19)

Against Hermes at the pinned commit running locally with a
real provider (OpenAI), user-level and loopback-only:

- `assistant status` negotiates the protocol as compatible;
  `assistant ask` returned a real model answer.
- Tool use from the shipped `hornero` skill: the agent answered
  installed GTK themes from `horneroctl appearance gtk list
  --json` (20 themes), not from generic knowledge.
- Approval flow with `approvals.mode: manual`: a `rm -rf` run
  parked in `waiting_for_approval`; `assistant approve`
  executed it (agent-verified), and a second run denied left
  the target untouched. This caught and fixed the approval
  wire protocol (hornero#168): the gateway authority path
  requires `{request_id, execution_generation, choice}` from
  `pending_controls`, with `approve` mapped to `once` only.
- Live streaming in the CLI (`--stream`) with timed deltas.

Still open: graphical Companion acceptance on a live desktop
session, resource report, and the managed lifecycle
(hornero#174). Hermes packaging for end users is **not**
decided; local acceptance used a pinned `uv sync --frozen`
source runtime, never an install script.

## Versus Ryoku Rashin (studied at `98a0368`)

Rashin (Ryoku `docs/rashin.md`, `ryoku/rashin/`) is a Go daemon
with a generated knowledge vault, an unauthenticated loopback
web dashboard (Origin-checked), ACP chat, a fast read-only
quick-ask lane, and one-click Hermes setup via the official
installer. HorneroOS deliberately differs where it is stricter:

| Axis | Rashin | HorneroOS |
| --- | --- | --- |
| Transport auth | none (Origin check) | Bearer auth, key file `0600` |
| Hermes install | official installer | pinned runtime, auditable |
| Protocol safety | ACP/stdio bridge | capability negotiation |
| Approvals | ACP prompts | authority protocol, live-verified |
| UI | web dashboard | native Companion chat panel |
| System knowledge | generated vault | live horneroctl + skill |
| Agent scope | any coding agent | Hermes as official backend |

Rashin's vault, quick-ask fast lane, and session history UX
remain worth studying; adopting any of them is separate,
evidence-first work, not imitation for its own sake.

## Non-goals for slice 1

Voice input/output, proactive suggestions, arbitrary command
execution, package mutations, file access, multi-provider
Hornero-side key management, and any claim of offline
operation.
