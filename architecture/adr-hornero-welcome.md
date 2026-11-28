# ADR: Hornero Welcome Center architecture and motion specification

- **Status:** Accepted
- **Date:** 2026-11-28
- **Tracking:** `HorneroOS/docs#167`, `HorneroOS/shell#751`, `HorneroOS/hornero#506`

## Context

Hornero Welcome (`HorneroOS/shell/modules/welcome/` paired with
`HorneroOS/hornero/cli/modules/hornero_core/welcome.v`) is the first surface
many desktop users meet after logging in, and the permanent entry point for
discovering keyboard-first workflows, appearance customization, Experience
Modes, Javi, and system recovery limits.

An audit of the baseline Welcome module established four structural limits:

- **Monolithic flat layout:** `Welcome.qml` (71 lines) and `Window.qml`
  (397 lines) wrap 11 flat `pages/*.qml` files inside a permanent 232 px left
  `ListView` + `StackLayout`, repeating the exact same `PageHeader` and
  vertical `ActionCard` list on every screen.
- **Coupled state schema (`schemaVersion: 1`):** `State.qml` and
  `hornero_core/welcome.v` track `showOnLogin`, `contentRevision`, and
  `lastSeenContentRevision`, with no distinct `firstRunCompleted` or
  `lastSeenReleaseVersion` fields to separate first-run onboarding from a
  returning user's `What's New` summary.
- **Static tutorial claims without live detection:** `ShortcutHints.qml` and
  `ShortcutList.qml` read `$XDG_DATA_HOME/hornero/shortcuts.json` with a
  `hyprctl binds -j` fallback, yet onboarding lacked an interactive tutorial
  driven by real shell and compositor state transitions.
- **Unrestricted preview & media boundaries:** `HorneroOS/config` ships 2
  MIT procedural SVG wallpapers and 3 verified CC BY 2.0 Argentine
  photographs alongside 54 legacy collection files marked `license: unknown`.
  Welcome must showcase only the verified licensed tier and protect live
  theme/layout previews with explicit revert and crash recovery.

At the same time, existing static and contract tests
(`shell/tests/test_welcome_*.py`) enforce hard invariants that the redesign
must preserve: zero hardcoded hex colours (`Signal.*` and `Appearance.*` only),
zero `http://` or `https://` literals in QML, zero `dots-*` paths, `qsTr()` on
all UI strings, strict `Actions.*` allowlists, `horneroctl`-only writes in
`State.qml`, and IPC parity (`welcome open|close|status`).

### Competitive analysis

We benchmarked desktop onboarding flows and craft-led software tools to isolate
which patterns belong in a Wayland-first, zero-telemetry workstation:

| Reference | Adopted pattern | Avoided |
| --- | --- | --- |
| macOS Setup | Calm pacing, disclosure | Cloud ID, lock-in |
| GNOME Tour | Focused arrival, brevity | Static slides, no preview |
| KDE Welcome | Broad discovery links | Uniform card grids |
| COSMIC | Clean Wayland chrome | Incomplete onboarding |
| Steam Deck | First-boot readiness | Closed appliance model |
| Linear | Sharp type, keyboard UX | SaaS workspace terms |
| Raycast | Unified search, keycaps | Cloud sync / paywalls |
| Arc | Memorable live studio | Heavy visual chrome |
| Teenage Eng. | Instrument restraint | Decorative gimmicks |

## Options evaluated

### Creative direction

| Criterion | A: Signal Flight | B: Pampa Broadsheet | C: Cockpit Telemetry |
| --- | --- | --- | --- |
| Status | **Selected** | Rejected | Rejected |
| Metaphor | Editorial observatory | Print gazette | Avionics scope |
| Day Ceramic | Clean porcelain + cue | Heavy print rules | Clashes w/ light |
| Night Blue | Graphite + lamp | Harsh columns | Fatiguing for users |
| Scene layout | Bespoke per job | Multi-column text | Dashboard clones |
| Brand fit | Signal + Argentine art | Reads like docs | Excludes Everyday |

**Rejected Direction B (Pampa Broadsheet — Typographic Gazette):** Strong in
editorial print readability, but heavy tabular ink rules make interactive
personalization feel like reading a newspaper rather than operating a live
Wayland desktop.

**Rejected Direction C (Cockpit Telemetry — Avionics Console):** Fits dark
hardware monitoring, but perpetual instrument scopes clash with Signal Day's
white ceramic aesthetic and overwhelm non-technical Desktop and Studio users.

## Decision

HorneroOS adopts **Signal Flight — Editorial Observatory** as the architecture
for Hornero Welcome, structured around seven core contracts.

### 1. Visual identity, surface contrast, and licensed wallpapers

Welcome aligns with RFC 0001 Amendment 3 (*White Ceramic Signal Day* and
*Blue-Hour Graphite Signal Night*, `SIGNAL_TOKENS_CANONICAL.json`), Native C++
Chromatic Engine v3 (`SurfacePolicy`, `kAlgorithm = 3`), and `Appearance.font`:

- **Typography (`Appearance.font`):** `IBM Plex Sans Condensed` (`display`) for
  Scene 1 and Scene 9 anchors, `IBM Plex Sans` (`sans`, `58ch`–`64ch` measure)
  for editorial copy and controls, and `IBM Plex Mono` (`mono` with tabular
  figures) for keycaps, telemetry readouts, versions, and provenance credits.
- **Zero repetitive card grids:** Each scene in `First Flight` uses a distinct
  spatial composition rather than repeating `PageHeader` + `ActionCard` lists.
- **Anti-slop rules:** Flagship Light mode (`hornero-signal-day`) strictly
  forbids yellowish aged-paper surfaces (`#FDF3E8`, `#F7F4EE`), purple/indigo
  SaaS gradients, Material drop-shadows, and decorative non-interactive pills.
- **WCAG 2.2 AA & Signal palette binding:** Every surface binds strictly to
  `Signal.palette.*` (`ground`/`sunken`, `base`, `panel`, `raised`/`lifted`,
  `ink`/`inkMuted`, `rule`/`ruleStrong`, `signal`/`onSignal`, `cue`/`cueWell`,
  `phosphor`/`alert`). Weakest Day text maintains `>= 5.27:1` contrast,
  `ruleStrong` boundaries maintain `>= 3.0:1`, and Scene 1 full-bleed
  photography uses a directional gradient scrim anchored in
  `Signal.palette.ground` (`0.92` alpha behind text to `0.15` alpha over the
  focal subject) to guarantee `>= 7.0:1` text legibility.
- **Licensed Argentine wallpaper policy:** Welcome showcases and promotes
  **only** the 2 MIT procedural SVGs (`hornero-signal-day.svg`,
  `hornero-signal-night.svg`) and the 3 verified CC BY 2.0 Argentine
  photographs from `wallpaper-provenance.json` (`buenos-aires-nocturno` by
  Luis Argerich, `fin-del-mundo` / Beagle Channel by RAYANDBEE, and `sierras`
  / Quebrada del Condorito by Kevin Jones), each paired with a visible
  `AttributionChip` credit. The 54 legacy collection files carrying
  `license: unknown` are never promoted in Welcome.

### 2. Motion Design System tokens and power budget

Welcome extends `qs.components.motion` (`Choreography.qml`, `MotionAnim.qml`,
`Stagger.qml`) and `Appearance.anim`. No hardcoded durations or custom easing
curves are permitted inside `modules/welcome/`.

| Token | Standard | Reduced (`0.5x`) | Off / Reduced Motion | Welcome role |
| --- | --- | --- | --- | --- |
| `quick` | `90 ms` | `45 ms` | `0 ms` | Keycap press, hover tint |
| `brief` | `160 ms` | `80 ms` | `0 ms` | Focus ring, `Stagger` row |
| `medium` | `240 ms` | `120 ms` | `0 ms` | Scene crossfade, OKLab tween |
| `settleFast` | `220 ms` | `0 ms` | `0 ms` | Active `OnAirBar` travel |
| `settle` | `320 ms` | `0 ms` | `0 ms` | Tutorial check, `PreviewTxBar` |
| `extended` | `360 ms` | `180 ms` | `0 ms` | Scene 1 sprite entrance |
| `fade` | `90 ms` | `90 ms` | `90 ms` (cap) | Pure opacity crossfades |
| `staggerStart` | `60 ms` | `0 ms` | `0 ms` | Delay before row stagger |
| `staggerStep` | `24 ms` | `0 ms` | `0 ms` | Up to 8 revealed rows |

- **Curves (`Appearance.anim.curves`):** `standard` (`[0.2, 0, 0, 1]`),
  `enter` (`[0.05, 0.7, 0.1, 1]`), `exit` (`[0.3, 0, 1, 1]`), `sweep`
  (`[0.65, 0, 0.35, 1]`), and `settle`/`settleFast` (`[0.32, 1.24, 0.42, 1]`
  with `<= 1.9%` overshoot / `[0.34, 1.3, 0.5, 1]` with `<= 3.0%` overshoot in
  `smooth` style, restricted exclusively to position, size, and needle
  indicators—never opacity or colour).
- **Travel and continuity:** `SceneDeck.qml` uses `dx = ±16 px` when
  `Choreography.morph` is true, dropping to `Choreography.scanTravel` (`4 px`)
  in `reduced` mode. Scene 1 pointer parallax is capped at `±10 px` X /
  `±6 px` Y and disabled when `!Choreography.morph`. Content `scale`
  transforms are banned on text and cards. Top/bottom chrome rails and the
  `HorneroSprite` emblem persist outside `SceneDeck` for optical continuity.
- **Reduced Motion (`Appearance.anim.reduced` or `off`):** Disables `morph`,
  `stagger`, and `travel`; caps transitions to `<= 90 ms` `Choreography.fade`;
  sets `holdStill: Appearance.anim.reduced` on `CompanionFramePlayer` /
  `Player.qml` (frame `0`, zero timer); disables `HorneroSprite`'s 7 s blink
  timer; and skips `AtmosphereLayer` glow leases.
- **Pause-on-hidden budget:** Every ambient timer, sprite animation reel
  (`playing: win.visible && sceneActive`), `FrameAnimation`, and `ShaderEffect`
  in `modules/welcome/` binds `running`/`playing` to `win.visible &&
  Qt.application.state === Qt.ApplicationActive` (or `win.visible` for preview
  reels), guaranteeing 0% idle CPU/GPU wakeups when Welcome is hidden or
  closed.

### 3. Reversible Live Preview Transaction Model (`WelcomePreviewTx`)

Scene 2 (`Make It Yours`) uses a two-tier reversible transaction model so users
can experiment with themes, Chromatic accents, wallpapers, and bar layouts
without destructive side effects:

1. **Tier A — Zero-write in-memory preview:** Hovering or selecting themes,
   Chromatic modes, and wallpapers invokes `Signal.beginPreview(scheme)` (which
   snapshots `Signal._snapshot` in memory and animates via OKLab `<= 240 ms`),
   `ChromaticPreview`, and `Wallpapers.preview(path)` (`showPreview = true`)
   without writing `scheme.json`, `shell.json`, or `Paths.wallpaperPointer`.
2. **Tier B — Disk-mutating live preview & transaction file:** Before invoking
   disk-writing previews such as `PresetApply.apply(targetPreset, display,
   false)`, `WelcomePreviewTx.beginIfNeeded()` persists the user's exact
   pre-preview baseline (`themeId`, `themeMode`, `chromaticActive`,
   `chromaticRequest`, `wallpaperPath`, `shellPreset`, `experienceMode`) to
   `$XDG_STATE_HOME/hornero/welcome-preview-tx.json` (`schemaVersion: 1`,
   `active: true`, `txId`, `startedAt`, `baseline`) via atomic write (`temp` +
   `mv -f`) owned by `hornero_core/welcome.v` (matching the `horneroctl`
   single-writer contract), alongside `PresetApply`'s `shell.json` safety copy
   under `$XDG_STATE_HOME/hornero/shell/undo/<ms>/`.
3. **Explicit `Apply & Keep` (`commit()`) vs `Revert` (`revert()`):** While
   `WelcomePreviewTx.dirty` is true, a persistent non-blocking `PreviewTxBar`
   offers `Revert` and `Apply & Keep`. `commit()` persists staged choices via
   `ThemePipeline.applyTheme`, `Wallpapers.setWallpaper`, and `horneroctl
   appearance chromatic apply` when Chromatic is active, then clears the
   transaction file. `revert()` calls `Signal.cancelPreview()` and
   `Wallpapers.stopPreview()`, restores any mutated `shellPreset` or disk
   state from `baseline`, and removes `welcome-preview-tx.json`.
4. **Close and crash recovery:** `Escape` or unexpected window close
   auto-reverts unapplied previews; leaving Scene 2 via `Next` prompts inline
   to keep or revert. If the shell terminates unexpectedly (`SIGKILL`), the
   next `Startup.qml` boot detects `active === true` in
   `welcome-preview-tx.json`, restores `baseline`, and posts a calm
   `Toaster.toast(..., Toast.Info)` notice.

### 4. Interactive Real-Event Tutorial (`PracticeScene`)

Scene 5 (`Move & Fly`) never simulates completion with timers or synthetic
clicks. Each mission resolves the user's **effective live keybinding** via
`ShortcutHints.badge(id)` and `Keybinds.entries` (`dispatcher` + `args`),
falling back to `"Unbound — use action button or Bar"` if unbound:

| Mission | Binding ID | Event source | Completion condition |
| --- | --- | --- | --- |
| 1. Launcher | `exec-launcher` | `Visibilities` | `launcher` `false -> true` |
| 2. Dashboard | `ipc-dashboard-toggle` | `Visibilities` | `dashboard` opens |
| 3. Workspace | `workspace:1` | `Compositor` | `newWsId !== initialWsId` |
| 4. Settings | `Keybinds.entries` | `WindowFactory` | `windows.length > 0` |

- Mission 1 guards `!Compositor.hasFullscreenOnFocusedOutput()`.
- Mission 4 keeps Welcome open in the background during practice (unlike
  `Actions.openControlCenter`) so the user sees the completed `phosphor`
  checkmark upon returning.
- `Toggle Scratchpad` (`togglespecialworkspace:magic`) appears **only** when
  `Compositor.supports("specialWorkspaces") === true` (Hyprland) and stays
  hidden on Niri.

### 5. Three-mode Information Architecture and v2 state schema

Welcome moves from 11 uniform pages to three focused modes inside a
`1080×680` (minimum `960×600`) `FloatingWindow`:

- **Mode 1 — `First Flight` (`mode = "first-flight"`):** Nine sequential
  compositions (`arrival` → `studio` → `workstation` → `javi` → `practice` →
  `extensions` → `workloads` → `trust` → `ready`) with a minimal top
  telemetry bar and compact bottom flight rail (`Show on login`, `Skip tour`,
  `Back` / `Next`).
- **Mode 2 — `Explore Hornero` (`mode = "explore"`):** Permanent returning-user
  hub backed by `services/welcomeRegistry.js` (Feature Registry),
  `services/welcomeSearch.js` (unified instant search across features,
  `PaneRegistry` settings targets, and live shortcuts), and `ShortcutsView.qml`.
  Every registry item invokes strictly typed, allowlisted deep-link URIs:
  - `welcome://first-flight/<sceneId>`, `welcome://explore/<categoryId>`,
    `welcome://whats-new/<version>`
  - `controlCenter://<paneId>#<sectionId>` (validated by
    `PaneRegistry.resolveTarget()`)
  - `drawer://<drawerName>` (`launcher`, `dashboard`, `utilities`, `session`,
    `layoutPicker`)
  - `action://<actionName>` (validated against `Actions.qml` allowlist)
- **Mode 3 — `What's New` (`mode = "whats-new"`):** Declarative offline
  changelog sourced from `assets/welcome/releases.json` (`schemaVersion: 1`,
  `currentReleaseVersion`, ordered `releases[]` with typed `deepLink` and
  `availability` badges).

**Per-user v2 state schema (`$XDG_STATE_HOME/hornero/welcome/state.json`):**

```json
{
  "schemaVersion": 2,
  "showOnLogin": true,
  "firstRunCompleted": false,
  "firstRunCompletedAt": "",
  "lastVisitedScene": "arrival",
  "contentRevision": "p2",
  "lastSeenContentRevision": "",
  "currentReleaseVersion": "0.5.0",
  "lastSeenReleaseVersion": "",
  "firstOpenedAt": "",
  "lastOpenedAt": ""
}
```

Both `hornero_core/welcome.v` and `State.qml` preserve tolerant v1→v2 read
compatibility and enforce three startup invariants:

1. **Explicit opt-out always wins:** If `showOnLogin === false`, Welcome
   **never** auto-opens on login—neither for `First Flight` nor for
   `What's New`.
2. **Decoupled first-run vs upgrade flow:** If `firstRunCompleted === true` and
   `lastSeenReleaseVersion !== currentReleaseVersion`, `First Flight` **never**
   replays; when `showOnLogin === true && !Session.markerExists`, Welcome
   opens directly in **Mode 3 (`What's New`)** and updates
   `lastSeenReleaseVersion` once viewed.
3. **Returning manual open:** Opening Welcome manually (`horneroctl welcome
   open`, Launcher, or Settings) after `firstRunCompleted === true` defaults to
   **`Explore Hornero`** unless a deep link or unread `What's New` target is
   specified.

### 6. Honest feature availability classification

Welcome surfaces only verified capabilities and adapts to the active host:

- **Supported:** Lifecycle & state, Signal Day/Night/Contrast & Originals,
  Chromatic Engine v3, 16 shell layouts, 2 MIT + 3 CC BY 2.0 licensed
  wallpapers, Experience Modes, Hyprland integration, live Keybinds, visual
  Javi Companion, PluginKit v3 extensions (with privilege notice), Agent
  Center UI + CLI, and Hornero Config Snapshots.
- **Experimental / Preview / Edition-dependent:** Niri compositor
  (`Compositor.supports(...)` hides Hyprland-only features), Studio Audio &
  routing (`Experience.studioAudioAvailable`), Gaming (`auto.fullscreenGaming`),
  and OS Btrfs recovery (`hornero_core/os_snapshots.v` read-only probe,
  marked `Ready (Opt-in)` or `Not configured`, never claiming unproven
  restore).
- **Optional / Local-only:** Javi AI / Hermes Assistant (`AssistantRun.gateway`
  is off by default and never auto-started by Welcome).
- **Planned / Excluded:** `Labwc` compositor backend, `Server` edition, and
  `Agents` edition (`editions/catalogue.yaml` `maturity: planned`) are omitted
  from interactive Welcome paths.

### 7. Security and user agency guarantees

- **No arbitrary code or URL execution:** `welcomeRegistry.js` and
  `releases.json` store declarative data only. Deep links pass strict allowlist
  validation; zero shell strings, `eval`, or `http://`/`https://` literals run
  from QML or metadata.
- **Explicit consent everywhere:** Software profiles delegate to
  `horneroctl store` (showing provenance badges and requiring explicit
  confirmation for proprietary or AUR entries); Scene 6 displays an `alertWell`
  banner noting that Quickshell plugins run unsandboxed with user privileges
  and documenting `HORNERO_SAFE_MODE=1` recovery; Scene 4 documents
  `AssistantBridge`'s secret-attachment refusal (`.env`, keys) and
  `ApprovalCard`/`ClarifyCard` consent gates.
- **Zero mandatory accounts or telemetry:** Welcome runs completely offline
  using local JSON assets (`releases.json`, `wallpaper-provenance.json`,
  `ExtensionStore.catalogue` with graceful offline fallback).

## Consequences

### Positive

- First-time users receive a coherent, keyboard-accessible, visually varied
  9-scene onboarding flow with zero risk of losing their desktop look.
- Existing upgraded users are never forced back through first-run onboarding
  and see concise, actionable `What's New` release summaries instead.
- Pure JS logic modules (`welcomeModel.js`, `welcomeRegistry.js`,
  `welcomeSearch.js`, `welcomePreviewTx.js`, `welcomeTutorial.js`) enable fast
  headless unit testing (`node --test` / `pytest`) alongside QML static checks
  (`test_welcome_*.py`), keeping every QML file focused (`< 220` lines).

### Negative and honest boundaries

- Adding `schemaVersion: 2` and the atomic `preview-tx` transaction verb
  requires coordinated updates across `HorneroOS/hornero` (`welcome.v`) and
  `HorneroOS/shell` (`modules/welcome/`), plus updating `test_welcome_content.py`
  for the new `scenes/*Scene.qml` and `views/*View.qml` layout.
- Multi-compositor parity remains asymmetric: Niri users receive a verified
  capability-gated experience while Hyprland retains deeper keybind rebinding
  and special-workspace tutorials.

## References

- [Hornero Welcome user guide](../desktop/hornero-welcome.md)
- [ADR: Hornero Apps architecture](adr-hornero-apps.md)
- [Design language](../development/design-language.md)
- [RFC 0001 — Hornero Signal](../development/rfc-0001-hornero-signal.md)
- [Popups, focus and motion](../desktop/popups-and-motion.md)
- [Updates and recovery](../desktop/updates-and-rollback.md)
