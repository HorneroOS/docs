# Hermes assistant architecture

Design contract for the first Hermes-backed Hornero Assistant vertical slice.
Implementation follows this document; where code and this document disagree,
code wins and this document must be fixed.

## Decision summary

- **Backend**: [Hermes Agent](https://github.com/NousResearch/hermes-agent)
  (Nous Research, MIT), studied at `f14699a1379838862d3020b97785796aa555d36d`.
  Hermes is the reasoning, tool-use, skills, and memory engine. HorneroOS
  does not reimplement an agent loop and does not fork Hermes.
- **Transport**: Hermes gateway API server — OpenAI-compatible HTTP/SSE on
  `127.0.0.1:8642` with a Bearer `API_SERVER_KEY`
  (`gateway/platforms/api_server.py`). Chosen over the TUI JSON-RPC stdio
  gateway (fragile process lifecycle, host auto-approve behavior) and ACP
  (version-skew errors, sessions not owned by the API surface).
- **Process model**: a user-level Hornero assistant service (never root)
  owns the Hermes lifecycle: start on enable, stop on disable, recovery on
  crash. The shell never orchestrates models.
- **UI**: Hornero Companion (Quickshell/QML) is presentation only, per
  ADR 002 in the shell repository. Existing reserved states
  `listening / thinking / acting / success / warning / error` map to
  assistant activity; existing Companion IPC remains the presentation
  boundary.

## Transport contract (from Hermes source)

| Operation | Endpoint | Notes |
|---|---|---|
| Capabilities | `GET /v1/capabilities` | Feature negotiation before any run; pin expectations per Hermes version |
| Start run | `POST /v1/runs` | Send `Idempotency-Key`; API-owned session only (foreign CLI/TUI/ACP sessions return 409 — the assistant must create and keep its own sessions) |
| Stream events | `GET /v1/runs/{id}/events` | SSE: tokens, tool activity, approval requests |
| Cancel | `POST /v1/runs/{id}/stop` | Must be wired to the UI cancel action and Companion error/success states |
| Approval | `POST /v1/runs/{id}/approval` | Hermes asks; the user decides in native UI. Never auto-approve |
| Clarify | `POST /v1/runs/{id}/clarify` | Structured follow-up questions |

Authentication: Bearer key generated per user, stored with restrictive
permissions in the user config dir, never committed, never logged. Loopback
only; no listener leaves `127.0.0.1`.

## First vertical slice (scope)

1. User explicitly enables the assistant (Settings/Companion surface +
   `horneroctl` parity). Default: **disabled**. Normal desktop must be
   complete with Hermes absent.
2. Service initializes Hermes; health = `GET /v1/capabilities` success.
3. Companion opens a conversation; user sends a message; Hermes streams a
   real response; Companion shows thinking/speaking states.
4. Read-only native tools (below) callable by Hermes; tool activity visible
   in the UI; user can cancel mid-run.
5. “Why is my system using memory / what updates exist” class questions
   answered from real `horneroctl` output, not hardcoded replies.
6. Failure paths: Hermes missing, wrong version, port conflict, provider
   unconfigured — each yields a human recovery message, never a stack trace.
7. Disable stops the integration and the daemon; zero idle cost when off.

## Native tool catalogue (slice 1: read-only only)

Exposed as literal argv through the existing `hornero_core` exec boundary
(no shell interpolation). All return the uniform `--json` envelope.

| Tool | Command | Class |
|---|---|---|
| System information | `horneroctl system info --json` | Safe read |
| Appearance status | `horneroctl appearance status --json` (as implemented today) | Safe read |
| Theme catalogue | `horneroctl appearance theme list --json`, `show <id>` | Safe read; ids validated (`/`, `..`, empty rejected) |
| GTK state | `horneroctl appearance gtk list/current --json` | Safe read |
| Update check | `horneroctl package updates --json` / `check` | Safe read (note the ~30 s AUR lane in UX copy) |
| Companion state | `qs ipc call companion status` | Safe read |

Mutations (theme apply, package install, settings changes) are **out of
slice 1**. Slice 2 adds them only behind Hermes approval surfaced in native
UI, one capability at a time, each with dry-run where `horneroctl` supports
it.

## Security model

- Disabled by default; enabling is an explicit, reversible user action.
- User-level service; no root, no polkit broadening in slice 1.
- Hermes approval model is never weakened or auto-answered.
- No screenshots, clipboard, microphone, files, or window contents are
  exposed in slice 1. Each is a separate future capability with its own
  consent.
- Secrets: provider keys belong to Hermes' own configuration; Hornero
  stores only its local Bearer key, `0600`, user-owned.
- Prompt-injection posture: tool results are data, not instructions; the
  tool allowlist above is exhaustive for slice 1.
- Auditability: run/tool history stays in Hermes' session plus a local,
  user-readable assistant log of tool invocations (command + result status,
  no secret material).

## Packaging and versions

- Hermes installed through a reproducible, version-pinned, auditable path
  (Arch package or managed isolated runtime). Never `curl | bash`.
- The supported Hermes version range is recorded with the implementation;
  `capabilities` negotiation fails closed with an upgrade message.
- Install, upgrade, disable, and uninstall are separate, tested operations;
  uninstall never removes user configuration without explicit consent.

## Performance gates

- Assistant disabled: zero processes, zero idle cost.
- Enabled but idle: measure daemon RSS/CPU and record it; no local model
  loads or weight downloads without explicit user action.
- Shell overhead: streaming UI must not regress launcher/frame baselines
  (shell performance tooling owns the measurement).

## Acceptance tests (slice 1)

- Protocol compatibility against the pinned Hermes version (mock + real).
- Streaming, cancellation, reconnection after daemon restart.
- Approval denial path (slice-2 preview: denial must block the action).
- Tool allowlist enforcement: a prompt asking for an unlisted action gets
  no execution.
- Disable/uninstall leaves the ordinary desktop fully functional.
- Resource report for disabled, idle, and streaming states.

## Non-goals for slice 1

Voice input/output, proactive suggestions, arbitrary command execution,
package mutations, file access, multi-provider Hornero-side key management,
and any claim of offline operation.
