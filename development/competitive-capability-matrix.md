# Competitive capability matrix

Evidence-backed comparison of HorneroOS against the strongest open-source
Arch/Wayland desktop references. This document drives engineering priorities;
it is not marketing copy. A capability is only "validated" when a user can
discover, configure, use, and recover it — never merely because code exists.

Maturity states: **Validated** · **Partial** · **Experimental** · **Planned** ·
**Absent**.

## Upstream references studied

Studied from source in an isolated research workspace (never in product
commits, never installed on a host). Pinned revisions:

| Project | Revision | License | Studied for |
|---|---|---|---|
| [Omarchy](https://github.com/omacom/omarchy) | `81fd2d23ca6e3462183a4dc8360de3113fa8d80c` | MIT | Product cohesion, theme-set atomic swap, migration markers, snapshot-before-update |
| [Ryoku](https://github.com/Ryoku-dev/ryoku) | `98a0368253d9628be72b853985878a5db90e1547` | See repo | ISO/installer philosophy, Rashin agent subsystem, Hermes setup |
| [DankMaterialShell](https://github.com/AvengeMedia/DankMaterialShell) | `d6a362d6b36b9d4717b4ceb6a4a05a4c707515aa` | See repo | Plugin loader/registry, Go services, multi-compositor shell |
| [Noctalia Shell](https://github.com/kozer/noctalia-shell) | `3aab45a2f34fd47666b05892b95054952e788de1` (v4 tree; canonical repo now `noctalia-dev/noctalia`) | See repo | Configurability, injected plugin API, entry points |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | `f14699a1379838862d3020b97785796aa555d36d` | MIT | Official AI backend: gateway API, runs, approvals, skills, memory |

Attribution classes: *studied for inspiration* (all rows below unless noted).
No upstream code is copied by this document; any future reuse requires
license verification and attribution in the owning repository.

## Matrix

| Capability | Upstream reference (evidence) | HorneroOS today | Owner |
|---|---|---|---|
| Plugin/extension runtime | DMS `PluginService.qml` + Go registries: in-process QML, full user privileges, experimental API, no signing. Noctalia v4: injected `pluginApi` + entry points | **Absent (runtime)** / Partial (contract): `shell/docs/PLUGINS.md`, `shell/scripts/validate_plugin.py` (schema v1, allowed imports, exact file match), `hornero_core/community_plugins.v` installs *inert* packages — “Third-party QML is not loaded or sandboxed” | shell + hornero |
| Companion / AI assistant | Ryoku Rashin (`docs/rashin.md`): optional, off by default, loopback daemon, generated system-knowledge vault, one-click Hermes setup; no native chat UX in the shell | **Absent (backend)** / Partial (presentation): Companion states, skins, IPC and reserved assistant states (`listening/thinking/acting/success/warning/error`) live; ADR 002 keeps the assistant a separate future daemon; no LLM, sessions, or tool calling | shell + hornero |
| Hermes transport | Hermes `gateway/platforms/api_server.py`: `127.0.0.1:8642`, Bearer key, `POST /v1/runs`, SSE `GET /v1/runs/{id}/events`, `/stop`, `/approval`, `/clarify`, `GET /v1/capabilities`, idempotency keys; API-owned sessions only | **Planned**: no session discovery, credential store, versioning, or consent UX exists yet in Hornero code | hornero |
| Read-only system tools for agents | Rashin vault (generated markdown knowledge) | **Partial (strong substrate)**: `horneroctl` read-only queries with `--json` envelope — system info, appearance/theme/GTK queries, package update check, hardware, Hyprland, shell, power, wallpaper, welcome | hornero |
| Launcher providers/plugins | DMS launcher providers; Noctalia entry points | **Partial**: launcher exists; plugin-defined providers blocked on plugin runtime | shell |
| Control Center depth | DMS/Noctalia settings breadth | **Partial**: 16 panes (network, bluetooth, VPN, appearance, taskbar, layout, launcher, dashboard, companion, audio, notifications, OSD, system, updates, terminal, power); gaps tracked per-pane, not by mock UI | shell |
| Theme system | Omarchy `omarchy-theme-set`: staged atomic swap + generation token | **Validated (core)**: mature theme packs, token schema, GTK/icon/wallpaper binding, CLI apply; 12 regional Hornero Originals; atomicity lessons from Omarchy still to adopt | config + hornero |
| Updates & recovery | Omarchy migration markers + snapshot-before-update; Garuda/CachyOS snapshot models (to study) | **Partial**: package/component updates exist; no proven OS snapshot/rollback story; chezmoi backup is config-only and must not be sold as OS rollback | hornero + installer |
| Installer & first boot | Ryoku ISO philosophy; Omarchy post-base-install provisioning (its ISO entry point is not in-repo) | **Experimental**: Calamares provisional, no ISO install acceptance; installer #11 blocked on builder disk guard (52 GiB vs ~29 GiB free), ISO not rebuilt after resolver fix; official gates in #12 not yet agreed with the installer owner | installer |
| Hardware & performance | CachyOS hardware detection/performance methodology (to study in depth) | **Partial**: hardware queries exist; measured shell baselines exist (shell #47); no CachyOS-grade detection matrix yet | hornero + qa |
| Optional profiles (dev/gaming/creator/agentic) | Omarchy/Ryoku curated bundles | **Planned**: must ride the canonical edition model with exact deps, footprint, uninstall, and acceptance; not released editions | hornero + config |
| Onboarding | Omarchy first-run; Ryoku Settings gates | **Partial**: Welcome module + `horneroctl welcome status`; Hermes setup must join as an optional, skippable step | shell |
| Dotfiles-only mature capabilities | Hornero dotfiles (historical source) | **Partial**: Hyprland Lua migration staged/inert (dotfiles #179, 2/9); tmux/yazi workflows marked adopt-copy, not yet generalized; personal preferences stay personal | config + shell |

## What HorneroOS will copy, adapt, or avoid

- **Copy (ideas, not ABI)**: manifest + semver + lockfile discipline for
  plugins (DMS/Noctalia); atomic theme swap with generation token (Omarchy);
  migration marker files and snapshot-before-update (Omarchy); generated,
  fenced system-knowledge for agents (Rashin) — produced by `horneroctl`
  queries instead of a second indexer where possible.
- **Adapt**: Rashin's “off by default, local-only” posture, but with an
  authenticated transport (Bearer over loopback) and a native Companion chat
  UX instead of a web dashboard.
- **Avoid**: in-process third-party QML presented as sandboxed (DMS model);
  unauthenticated local daemons; `curl | bash` agent installation; AI as a
  mandatory dependency; claiming ISO validation from a build alone.

## Priority order (dependency-based)

1. Installer/first-boot acceptance unblocked (installer #11/#12, owner-led).
2. Plugin runtime lifecycle on the existing manifest contract, with truthful
   trust labels (trusted QML = user privileges; no fake sandbox claims).
3. Hermes assistant vertical slice — see
   [Hermes assistant architecture](hermes-assistant-architecture.md).
4. Settings/launcher gaps closed per-pane with GUI/CLI parity.
5. Update/snapshot/recovery design with measured performance gates.

## Known evidence gaps

- Noctalia v5 (`noctalia-dev/noctalia`) plugin system not yet studied.
- DMS community registry repository not cloned; registry claims rest on the
  DMS tree only.
- QA graphical scenarios audited, not executed, in this pass.
- CachyOS and Garuda source-level study still pending.
