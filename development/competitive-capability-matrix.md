# Competitive capability matrix

Evidence-backed comparison of HorneroOS against the strongest
open-source Arch/Wayland desktop references. This document drives
engineering priorities; it is not marketing copy. A capability is
only "validated" when a user can discover, configure, use, and
recover it — never merely because code exists.

Maturity states: **Validated** · **Partial** · **Experimental** ·
**Planned** · **Absent**.

## Upstream references studied

Studied from source in an isolated research workspace (never in
product commits, never installed on a host). Pinned revisions:

| Project | Revision | Studied for |
| --- | --- | --- |
| Omarchy | `81fd2d23ca6e` | Cohesion, theme swap, migrations |
| Ryoku | `98a0368253d9` | Installer philosophy, Rashin |
| DankMaterialShell | `d6a362d6b36b` | Plugin loader, Go services |
| Noctalia Shell (v4) | `3aab45a2f34f` | Configurability, plugin API |
| Hermes Agent | `f14699a13798` | Gateway API, runs, approvals |

Full URLs: `github.com/omacom/omarchy`,
`github.com/Ryoku-dev/ryoku`,
`github.com/AvengeMedia/DankMaterialShell`,
`github.com/kozer/noctalia-shell` (canonical repo now
`noctalia-dev/noctalia`), `github.com/NousResearch/hermes-agent`
(MIT). Attribution class for every row below: *studied for
inspiration*. Any future code reuse requires license verification
and attribution in the owning repository.

## Matrix summary

| Capability | HorneroOS status | Owner |
| --- | --- | --- |
| Plugin/extension runtime | Partial | shell + hornero |
| Companion / AI assistant | Experimental | shell + hornero |
| Hermes transport | Experimental | hornero |
| Read-only agent tools | Partial (strong) | hornero |
| Launcher providers | Partial | shell |
| Control Center depth | Partial | shell |
| Theme system | Validated (core) | config + hornero |
| Updates and recovery | Partial | hornero + installer |
| Installer and first boot | Experimental | installer |
| Hardware and performance | Partial | hornero + qa |
| Optional profiles | Planned | hornero + config |
| Onboarding | Partial | shell |
| Dotfiles-only capabilities | Partial | config + shell |

## Evidence per capability

### Plugin/extension runtime

- DMS: `PluginService.qml` plus Go registries; in-process QML with
  full user privileges, experimental API, no signing.
- Noctalia v4: injected `pluginApi` plus entry points.
- HorneroOS: contract and static validator
  (`shell/docs/PLUGINS.md`, `shell/scripts/validate_plugin.py`,
  schema v1, allowed imports, exact file match). Lifecycle is
  implemented: `horneroctl plugin enable|disable` owns receipt
  state (fresh installs start disabled; enable re-validates and
  fails closed). `services/Plugins.qml` discovers enabled plugins
  and `modules/plugins/PluginHost.qml` loads each entrypoint in
  its own loader with per-plugin fault isolation. Manifest
  `placement` renders bar plugins in the bar end group
  (`background` stays headless) and dashboard plugins as cards
  in the dashboard Extensions tab. The Control Center Extensions
  pane lists installed state and can enable/disable by invoking
  the exact `horneroctl` lifecycle commands (horneroctl stays
  the single receipt writer; enable needs an inline confirmation
  mirroring the CLI `--yes` gate). Desktop placement renders
  widgets on the background layer (fixed bottom-right stack;
  positioning/persistence not configurable yet). Signing and a
  community registry are not done yet. Enabled QML runs
  with the logged-in user's permissions; it is not sandboxed.

### Companion / AI assistant

- Ryoku Rashin (`docs/rashin.md` in Ryoku): optional, off by
  default, loopback daemon, generated system-knowledge vault,
  one-click Hermes setup; no native chat UX in the shell.
- HorneroOS: Companion states, skins, IPC, and reserved assistant
  states (`listening/thinking/acting/success/warning/error`) are
  live. `horneroctl assistant` (status/enable/disable/tools/ask/
  stop/approve/clarify/events) talks to Hermes;
  `AssistantBridge.qml` routes Companion IPC `ask` through that
  CLI only, surfaces pending approvals in the bubble, and never
  auto-answers them; the launcher offers a `>ai` prompt entry.
  Disabled by default; read-only tools slice 1. `assistant ask`
  and `assistant events` accept `--stream` (human output only):
  SSE deltas print live as they arrive (incremental parser over
  the HTTP progress callback; buffered and `--json` paths are
  unchanged). A native chat panel shows the conversation with
  approval buttons; real-Hermes acceptance passed locally on
  2026-10-19 (real provider, approvals approve/deny executed,
  skill-driven tool use — see the architecture doc). Graphical
  Companion acceptance and managed Hermes lifecycle remain.

### Hermes transport

- Hermes `gateway/platforms/api_server.py`: `127.0.0.1:8642`,
  Bearer key, `POST /v1/runs`, SSE events, `/stop`, `/approval`,
  `/clarify`, `GET /v1/capabilities`, idempotency keys.
  API-owned sessions only.
- HorneroOS: implemented in `hornero_core/assistant.v` —
  loopback endpoint, local Bearer key file (0600), runs + SSE
  consumption, stop, approval/clarify answers, an `events`
  reader for pending requests, and a capabilities probe in
  `assistant status`. There is no gateway semver to pin, so
  status negotiates the protocol (platform plus the five
  feature flags the client calls) against the studied Hermes
  commit `f14699a13798…` and fails closed when incompatible.
  See
  [Hermes assistant architecture](hermes-assistant-architecture.md).

### Read-only agent tools

- HorneroOS substrate is strong: `horneroctl` read-only queries
  with a uniform `--json` envelope — system info, appearance,
  theme and GTK queries, package update check, hardware,
  Hyprland, shell, power, wallpaper, welcome.

### Launcher, Control Center, themes

- Launcher exists; plugin-defined providers are blocked on the
  plugin runtime.
- Control Center: 17 panes (network, bluetooth, VPN, appearance,
  taskbar, layout, launcher, dashboard, companion, audio,
  notifications, OSD, system, updates, terminal, power,
  extensions). Gaps are
  tracked per pane, not by mock UI.
- Themes: validated core. Mature packs, token schema, GTK, icon
  and wallpaper binding, CLI apply, 12 regional Hornero
  Originals. Omarchy's staged atomic swap with a generation
  token (`omarchy-theme-set`) is still to adopt.

### Updates, recovery, installer

- Omarchy: migration marker files and snapshot-before-update.
- HorneroOS updates exist for packages and components. There is
  no proven OS snapshot/rollback story; a chezmoi backup is
  config-only and must not be sold as OS rollback.
- Installer: Calamares provisional, no ISO install acceptance.
  Installer issue 11 is blocked on a builder disk guard
  (52 GiB required vs ~29 GiB free); the ISO was not rebuilt
  after the resolver fix. Official gates (issue 12) are not yet
  agreed with the installer owner.

### Hardware, profiles, onboarding, dotfiles

- Hardware queries exist; measured shell baselines exist
  (shell issue 47). No CachyOS-grade detection matrix yet.
- Profiles (developer/gaming/creator/agentic) must ride the
  canonical edition model with exact dependencies, footprint,
  uninstall behavior, and acceptance. They are not released
  editions.
- Welcome module plus `horneroctl welcome status` exist; Hermes
  setup joins onboarding only as an optional, skippable step.
- Dotfiles: Hyprland Lua migration staged and inert (dotfiles
  issue 179, 2 of 9 steps); tmux/yazi workflows are marked
  adopt-copy, not yet generalized. Personal preferences stay
  personal.

## Copy, adapt, avoid

- **Copy (ideas, not ABI)**: manifest, semver, and lockfile
  discipline for plugins (DMS/Noctalia); atomic theme swap with
  generation token (Omarchy); migration markers and
  snapshot-before-update (Omarchy); generated, fenced system
  knowledge for agents (Rashin), produced by `horneroctl`
  queries instead of a second indexer where possible.
- **Adapt**: Rashin's off-by-default, local-only posture, but
  with an authenticated transport and a native Companion chat
  UX instead of a web dashboard.
- **Avoid**: in-process third-party QML presented as sandboxed;
  unauthenticated local daemons; `curl | bash` agent installs;
  AI as a mandatory dependency; claiming ISO validation from a
  build alone.

## Priority order (dependency-based)

1. Installer/first-boot acceptance unblocked (installer issues
   11 and 12, owner-led).
2. Plugin runtime lifecycle on the existing manifest contract,
   with truthful trust labels: trusted QML runs with user
   privileges; no fake sandbox claims.
3. Hermes assistant vertical slice, per the architecture doc.
4. Settings and launcher gaps closed per pane, GUI/CLI parity.
5. Update/snapshot/recovery design with measured performance
   gates.

## Known evidence gaps

- Noctalia v5 (`noctalia-dev/noctalia`) not yet studied.
- DMS community registry repository not cloned; registry claims
  rest on the DMS tree only.
- QA graphical scenarios audited, not executed, in this pass.
- CachyOS and Garuda source-level study still pending.
