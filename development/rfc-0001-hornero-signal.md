# RFC 0001 — Hornero Signal

- **Status** — Accepted (2026-11-16); amended 2026-11-16 (amendment 1:
  WOW + WORK ambition, motion springs, layout catalogue, experience modes,
  instrumentation, integration contracts)
- **Scope** — Every first-party HorneroOS surface: shell, PluginKit and
  extensions, config (GTK/Qt/terminal/compositor), horneroctl, greeter,
  installer, website, docs, brand
- **Supersedes** — The Material 3–derived token system (`M3Palette`, `m3*`
  roles, Material Symbols, wallpaper tonal-spot synthesis) and the "Hornero
  199X" optional theme
- **Tracking** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)

## 1. Why

The shell inherited Caelestia's Material 3 architecture: every colour is an
`m3*` tonal role, icons are Material Symbols ligatures, motion uses M3
"expressive" springs, and themes are synthesised from the wallpaper with
`materialyoucolor`. That made HorneroOS look like a reskinned Caelestia and
tied the whole appearance stack (shell, horneroctl, config) to an external
design system. Hornero 199X proved that a retrofuturist Argentine direction is
right for the project, but it shipped only as one optional colour pack on top
of the M3 machinery.

Hornero Signal replaces the machinery, not only the colours. This is an
intentional breaking change. There is **no** Material compatibility layer and
no parallel legacy system.

## 2. Creative direction

> A contemporary engineering workstation from an alternate 1990s Argentina:
> broadcast control rooms, oscilloscope bezels, test cards, technical drawing
> sheets and the diagonal geometry of La Plata — executed with modern
> restraint.

Amendment 1 raises the ambition: HorneroOS should feel like an
extraordinary workstation from an alternate technological future —
retrofuturist and cyberpunk computing interpreted by a world-class designer —
inspired by the best Rainmeter/Conky desktops, purposeful Polybar/Waybar
configurations, Cyberpunk 2077-era interfaces and fictional operating systems.
Two experiences must coexist without compromising each other:

- **WOW** — unmistakably original, cinematic, delightful to discover.
- **WORK** — responsive, accessible, dependable for hours of coding, music
  production, creative work and gaming.

The concrete visual language (bar anatomy, meters, framing, luminous accents,
phosphor details, per-layout art direction, motion choreography) is specified
in [Signal Visual Language](signal-visual-language.md), chosen after a
documented comparison of three directions. It must look exceptional with
animations disabled.

Principles, in priority order:

1. **Work first.** Chrome is quiet and matte. The accent is a signal, not a
   decoration: amber means *live / active / primary*, celeste means *focus /
   selection / information*.
2. **Instrument, not toy.** Hairline rules, small radii, tabular numerals,
   segmented meters, labelled channels, restrained luminous signal accents.
   No pills-everywhere, no glass, no neon gradients, no random hex
   decoration, no glitch effects, no constant blinking, no pixel-art chrome.
3. **Legible at a glance.** Every text role passes WCAG AA on every surface it
   is used on; UI boundaries pass 3:1.
4. **One language everywhere.** Shell, extensions, GTK/Qt apps, greeter,
   installer and website use the same roles, type, glyphs and motion.

Signature details (use consistently, never as random ornament):

- **Eyebrows** — section labels in IBM Plex Mono, uppercase, +8 % tracking,
  `inkMuted`, optionally prefixed by a channel number (`01 · AUDIO`).
- **Registration tick** — the focused/active panel shows a 2×10 px `signal`
  tick on its leading top corner instead of a glow.
- **On-air bar** — active state on strips (workspaces, tabs, rail items) is a
  2–3 px `signal` bar on the edge facing the content, not a filled pill.
- **Segmented meters** — volume, brightness, battery, CPU and similar readouts
  render as discrete segments (VU-meter style) with tabular mono values.
- **Diagonal** — the La Plata 45° diagonal appears only in brand surfaces
  (lock, greeter, installer, website hero, wallpapers), never inside controls.

## 3. Tokens

The token contract is owned by **HorneroOS/config**
(`profiles/themes/tokens.schema.json`, schema version 2). The shell consumes
the same role names through the `Signal` singleton (`Signal.palette.<role>`).
GTK, Qt, terminal, Hyprland, hyprlock, greeter, installer and website
generators map from these roles only.

### 3.1 Colour roles

- `ground` — Desktop/back-most level, scrims over wallpaper, lock background
- `sunken` — Input wells, track backgrounds, inset areas
- `base` — Bars, window/dialog body
- `panel` — Cards, popouts, menus
- `raised` — Hovered/selected rows, nested cards
- `lifted` — Highest elevation, tooltips, pressed states
- `ink` — Primary text and glyphs
- `inkMuted` — Secondary text, eyebrows, inactive glyphs
- `inkFaint` — Disabled / decorative only — never essential text
- `rule` — Hairline separators inside a surface
- `ruleStrong` — Control boundaries, outlines that must pass 3:1
- `signal` / `onSignal` — Primary action, live/active state (amber)
- `signalWell` / `onSignalWell` — Low-emphasis primary fill (selected chip)
- `cue` / `onCue` — Focus ring, selection, information (celeste)
- `cueWell` / `onCueWell` — Low-emphasis informational fill
- `phosphor` / `onPhosphor` — Positive/healthy/connected (phosphor green)
- `phosphorWell` / `onPhosphorWell` — Low-emphasis positive fill
- `alert` / `onAlert` — Destructive/error
- `alertWell` / `onAlertWell` — Low-emphasis error fill
- `inverse` / `onInverse` / `inverseSignal` — Snackbars and inverted toasts
- `scrim`, `shadow` — Overlays and the single shadow colour
- `focus` — Keyboard focus ring (defaults to `cue`)
- `term0`…`term15` — Terminal ANSI palette

Removed with no replacement: all `*Fixed*`, `*_paletteKeyColor`,
`surfaceTint`, `surfaceVariant`, `onBackground`, tonal-spot "variants",
"follow wallpaper" synthesis and `materialyoucolor`.

Material → Signal mapping used **once** for the migration (not kept as an
alias table): `background/surfaceDim/surfaceContainerLowest → ground`,
`surfaceContainerLow → sunken`, `surface → base`,
`surfaceContainer → panel`, `surfaceContainerHigh → raised`,
`surfaceContainerHighest/surfaceBright → lifted`, `onSurface → ink`,
`onSurfaceVariant → inkMuted`, `outlineVariant → rule`,
`outline → ruleStrong`, `primary* → signal*`, `secondary* → cue*`,
`tertiary* → phosphor*`, `success* → phosphor*`, `error* → alert*`,
`*Container → *Well`.

### 3.2 Flagship palettes

`hornero-signal-night` is the factory default: cool graphite instrument
panels with warm phosphor-cream ink. `hornero-signal-day` is warm
technical-drawing paper with ink-black text.

| Role             | Signal Night | Signal Day |
| ---------------- | ------------ | ---------- |
| `ground`         | `#0C0F13`    | `#E6E1D5`  |
| `sunken`         | `#101419`    | `#DCD6C8`  |
| `base`           | `#13171D`    | `#F2EEE5`  |
| `panel`          | `#181D24`    | `#F7F4EE`  |
| `raised`         | `#1F252E`    | `#FBF9F5`  |
| `lifted`         | `#283039`    | `#FFFFFF`  |
| `ink`            | `#ECE6DA`    | `#1B1E22`  |
| `inkMuted`       | `#A8ABAD`    | `#4E545B`  |
| `inkFaint`       | `#737980`    | `#7A8086`  |
| `rule`           | `#2C333C`    | `#D3CCBD`  |
| `ruleStrong`     | `#66707B`    | `#857F73`  |
| `focus`          | `#7EC1EA`    | `#1D6894`  |
| `signal`         | `#F2A33A`    | `#9A5100`  |
| `onSignal`       | `#1A1205`    | `#FFFFFF`  |
| `signalWell`     | `#3A2A12`    | `#F6DDB8`  |
| `onSignalWell`   | `#FFD9A3`    | `#3D2200`  |
| `cue`            | `#7EC1EA`    | `#1D6894`  |
| `onCue`          | `#06151F`    | `#FFFFFF`  |
| `cueWell`        | `#16303F`    | `#D3E7F3`  |
| `onCueWell`      | `#CDE8F8`    | `#0B2E44`  |
| `phosphor`       | `#8BD49A`    | `#2A7341`  |
| `onPhosphor`     | `#07170C`    | `#FFFFFF`  |
| `phosphorWell`   | `#173222`    | `#D5EBD9`  |
| `onPhosphorWell` | `#CDEFD4`    | `#0E2E17`  |
| `alert`          | `#F0705A`    | `#B0371F`  |
| `onAlert`        | `#1E0905`    | `#FFFFFF`  |
| `alertWell`      | `#3D1A14`    | `#F7D7D0`  |
| `onAlertWell`    | `#FFD3CA`    | `#4A1209`  |
| `inverse`        | `#ECE6DA`    | `#1B1E22`  |
| `onInverse`      | `#181D24`    | `#F2EEE5`  |
| `inverseSignal`  | `#8A5200`    | `#F2A33A`  |
| `scrim`          | `#000000`    | `#000000`  |
| `shadow`         | `#000000`    | `#000000`  |

**Signal High Contrast** keeps the roles, uses `#000000` ground, `#FFFFFF`
ink, `#FFC247` signal, `#8FD3FF` cue and pure white `ruleStrong`.

Other catalogue themes (regional Argentina photo themes, community ports)
remain valid **if** they provide a complete schema-v2 role set that passes the
contrast tests. Themes that only existed as M3 seeds are removed or ported.

### 3.3 Typography

| Family    | Font                    | Use                                |
| --------- | ----------------------- | ---------------------------------- |
| `sans`    | IBM Plex Sans           | UI text                            |
| `mono`    | IBM Plex Mono           | Readouts, numerals, eyebrows, code |
| `display` | IBM Plex Sans Condensed | Clock, lock, large headings        |

Package: `ttf-ibm-plex` (Arch `extra`, OFL-1.1). Scale (px at scale 1):
`small 11`, `smaller 12`, `normal 13`, `larger 15`, `large 18`,
`extraLarge 28`, `display 56`. Numbers always use tabular figures.

### 3.4 Glyphs

**Hornero Glyphs** — a curated subset of Tabler Icons (outline, MIT) built
into `assets/fonts/hornero-glyphs.ttf` with `fonttools`, plus a generated
name→codepoint table. Components use `Glyph { name: "wifi" }`.
Material Symbols are removed from code, defaults and packaging. Stroke reads
as 1.5–2 px at 16–24 px, which matches the hairline language.

### 3.5 Geometry and spacing

4 px grid. Radius: `small 3`, `normal 5`, `large 8`, `full` only for
genuinely circular elements (avatars, radio dots). Spacing:
`small 4`, `smaller 8`, `normal 12`, `larger 16`, `large 24`. Padding:
`small 4`, `smaller 6`, `normal 8`, `larger 12`, `large 16`. Borders: 1 px
`rule` inside surfaces, 1 px `ruleStrong` on controls. Elevation is expressed
by surface role plus one restrained shadow (`shadow` at 35 %, 12 px blur, 4 px
offset away from the anchor edge). No blur-behind glass by default.

### 3.6 Motion

| Curve      | Bezier              | Use                            |
| ---------- | ------------------- | ------------------------------ |
| `standard` | `0.2, 0, 0, 1`      | State changes                  |
| `enter`    | `0.05, 0.7, 0.1, 1` | Things appearing               |
| `exit`     | `0.3, 0, 1, 1`      | Things leaving                 |
| `sweep`    | `0.65, 0, 0.35, 1`  | Reveal wipes, page transitions |

| `settle`     | `0.32, 1.24, 0.42, 1` | Small elegant overshoot      |
| `settleFast` | `0.34, 1.36, 0.5, 1`  | Quick controls, chips        |

Durations: `quick 90`, `short 160`, `medium 240`, `long 360`, `scan 480`,
`settleFast 220`, `settle 320` ms.

Amendment 1: physically inspired settling is part of the language. Overshoot
stays small (≤ 4 % of travel), is used for spatial motion only (position, size,
shape morph), never for opacity or colour, and every surface defines its
choreography (trigger-origin morph, size/shape morphing between adjacent
controls, stagger of content, layered depth) through shared primitives — no
layout-specific tricks. Motion must not add input latency: surfaces are
interactive from their first frame, budgets are measured (§7), and low-power
hardware can select a reduced motion level. **Scan-in**: anchored surfaces
reveal by a clip wipe from the anchor edge plus 6 px travel and a fade
(`enter`/`short` to `medium`); exit is a fade plus 4 px travel back toward the
anchor (`exit`/`quick`). Reduced motion (`appearance.reducedMotion` or the
system preference) sets durations to 0 except opacity cross-fades capped at 90
ms.

## 4. Interaction contract — anchored surfaces

Every popout, tooltip, drawer, menu, notification and extension popover is
positioned by one shared solver (`AnchoredSurface` + `Placement` in the shell,
re-exported to PluginKit). Inputs: the trigger's item, its owning bar
(edge, style, thickness, margin, reserve, floating/attached), the owning
screen (geometry, scale, reserved areas) and the surface's preferred size.

Rules:

1. Expansion direction is derived from the owning bar edge: top → down,
   bottom → up, left → right, right → left. Surfaces not owned by a bar use an
   explicit preferred edge.
2. Cross-axis alignment centres on the trigger, then clamps to the screen's
   usable rectangle minus the gutter (8 px × scale). If the preferred
   direction cannot fit, flip once; if neither fits, clamp and scroll the
   content.
3. The anchor is live: the surface tracks trigger geometry changes (bar
   reorder, island resize, monitor change) without a stale frame.
4. Motion originates at the trigger edge (scan-in) — never from screen centre.
5. Focus: hover popouts never take keyboard focus; click/keyboard-opened
   surfaces take focus and return it to the trigger on Escape. One Escape
   closes exactly one surface (existing escape cascade).
6. Hover popouts have a 120 ms open intent delay and a 240 ms close grace
   bridged across the trigger↔surface gap; no flicker when crossing.
7. Extensions receive the same contract; they cannot position themselves in
   absolute screen coordinates.

Correctness is verified by unit tests of the solver for all four edges,
mixed-scale multi-monitor rectangles and constrained space, plus host
screenshots (§7).

## 5. Cockpit — factory default desktop

**Top bar = act. Bottom bar = know. Centre = uninterrupted work.**

- **Top rail** (36 px, `base`, 1 px `rule` on the inner edge, inset 6 px):
  start — Hornero mark (launcher), quick actions; centre — clock and date in
  Plex Sans Condensed; end — status cluster (network, Bluetooth, audio),
  tray, extensions island, notifications, power.
- **Bottom strip** (30 px, attached): start — workspaces with on-air bar and
  occupancy ticks; centre — active window title and media transport; end —
  keyboard layout, resources (segmented mini-meters), battery when present.
- Cockpit is the default in `shell.default.json`, config defaults, horneroctl
  reset, installer first boot and every edition. Cockpit is the recognizable
  flagship and gets the most art direction.

### 5.1 Layout catalogue (amendment 1)

Every shipped preset is audited and art-directed; weak presets are improved,
merged or removed on merit, not kept to preserve a count. Survivors each have
a distinct visual and functional identity defined in the visual-language
spec.

- **Hornero Left / Hornero Right** are preserved as polished, supported
  layouts. Their descriptions acknowledge that they are inspired by
  Caelestia's layout, with attribution. They adopt Signal tokens, the shared
  interaction contract and motion primitives while keeping their recognizable
  composition. This does not reintroduce Material tokens or APIs.
- **Cockpit Clear** has a genuinely absent bar background: zero background
  opacity, no tint, slab, blur, edge scrim or backdrop shadow. Legibility
  comes from foreground-only treatments (adaptive ink chosen per wallpaper
  region, glyph/text outline or shadow on the foreground only, user-selectable
  foreground styles). Popouts opened from Clear bars remain fully opaque
  Signal surfaces. Validated against bright, dark, detailed and high-contrast
  wallpapers on the real host.

## 5a. Experience modes (amendment 1)

Four independent axes compose; none of them is a separate shell:

1. **Edition** (Desktop, Studio, Gaming) — installed capabilities and
   packages. Owned by HorneroOS/hornero.
2. **Experience mode** — how the system behaves right now: `focus`,
   `everyday` (default), `signal` (immersive), `gaming`, `studio`. A mode is a
   declarative profile of: motion level, instrumentation density, desktop
   widgets, notification policy (do-not-disturb, fullscreen suppression),
   preferred layout preset, idle/power hints, and edition hooks (GameMode,
   PipeWire quantum, Gamescope). Owned by the shell (`services/Experience`)
   with `horneroctl mode get|set|list|reset` as the system interface.
3. **Layout preset** — bar composition (Cockpit, Hornero Left, …).
4. **Theme** — Signal roles and wallpaper.

Rules: modes are switched explicitly by the user (launcher, Control Center,
IPC, CLI); optional automatic switching (e.g. fullscreen game → `gaming`) is
off by default, local-only, shown in the UI and reversible with one action.
User customisations per mode are preserved; `horneroctl mode reset` and a
Control Center action return to the factory `everyday` + Cockpit + Signal
Night. Modes only enable capabilities the installed edition has; a missing
capability is shown as unavailable, not faked. **Gaming** must never draw
over fullscreen applications, steal focus, or poll at a cost; **Focus**
maximises usable space and quiets motion and notifications; **Signal** is
where the richest telemetry and motion live.

## 5b. Instrumentation (amendment 1)

Rainmeter/Conky-class desktops are built on PluginKit, not a competing widget
engine: bar modules, desktop widgets (floating, layer-shell), and contextual
panels share one widget surface API, Signal tokens, motion primitives and the
anchored-surface contract. Data comes from native shell services
(SystemUsage, Network, Audio, Players, Battery, Hypr/Niri) and declared
providers with permissions; values are never invented — unavailable sensors
render as unavailable. Polling is shared and rate-limited per provider with
measured CPU cost. Instrumentation covers CPU/GPU load and temperature,
memory, storage, network, audio/playback, hardware health, workspaces, clocks
and calendars.

## 6. Ownership and integration order

- **W1 Tokens + theme schema v2 + flagship themes, GTK/Qt/kitty/Hyprland
  generators, Cockpit default** — config; *depends on:* RFC
- **W2 Shell foundation: `Signal` singleton, fonts, Hornero Glyphs, motion
  tokens, removal of M3 code** — shell; *depends on:* RFC
- **W3 Appearance backend: drop `materialyoucolor` synthesis, apply schema-v2
  themes** — hornero (horneroctl); *depends on:* W1
- **W4 Shell surfaces: components, bars, Cockpit, anchored surface solver,
  launcher, dashboard, Control Center, notifications, OSD, lock, session,
  welcome** — shell; *depends on:* W2
- **W5 PluginKit + first-party extensions on Signal** — shell, plugins; *depends
  on:* W2
- **W6 Greeter, installer branding, boot** — greeter, installer; *depends on:*
  RFC
- **W7 Website repositioning + brand assets** — website, config; *depends on:*
  RFC
- **W8 Docs, org profile, READMEs** — docs, .github, all; *depends on:* W1–W7
- **W9 QA: host matrix, VM install, evidence** — qa; *depends on:* W4–W6

Contracts between workstreams are the role names (§3.1), font families
(§3.3), glyph component API (§3.4), motion names (§3.6) and the anchored
surface API (§4). Changing any of them requires amending this RFC.

## 7. Validation and definition of done

The [mission issue](https://github.com/HorneroOS/.github/issues/28) holds the
checklist. In summary: no `m3`, `Material`, `materialyoucolor` or
Material Symbols references remain in first-party code or packaging (static
scan in CI); contrast tests pass for every shipped theme; the solver passes
edge/scale/multi-monitor tests; Cockpit and supported presets are captured on
the real host at the listed resolutions and scales; a disposable VM install
reaches first boot in Cockpit + Signal Night. Evidence states where it was
produced (host, VM or CI) and is never fabricated.

### 7.1 Visual validation (amendment 1)

Passing tests are not evidence of good design. Every surface change is run on
the real host (or a VM when the host cannot exercise it), captured, inspected
and compared before/after; weak results are iterated. Required coverage:
1280×720, 1366×768, 1920×1080, ultrawide; 100/125/150/200 % scale; single,
multi and mixed-scale monitors (virtual outputs where hardware is absent,
labelled as such); all four bar edges; every surviving preset; Cockpit Clear
over at least four wallpaper classes; light/dark, reduced motion; startup,
restart, persistence. Motion is measured (frame time, input-to-first-frame)
and recorded where possible. Concept renders are always labelled as concepts.

## 8. Attribution

Caelestia ancestry, licences and NOTICE files are kept, and the Hornero
Left/Right preset descriptions credit Caelestia's layout and remain accurate
(`shell/docs/PROVENANCE.md`). Tabler Icons (MIT) and IBM Plex (OFL-1.1) are
credited in NOTICE files where they ship.

## 9. Integration contracts

- **Theme file** — `config/profiles/themes/<id>/theme.json`, schema v2:
  `schemaVersion: 2`, `id`, `name`, `mode`, `palette` (exactly the §3.1
  roles), `terminal` (16 colours) and gtk/icon/wallpaper metadata.
- **Live scheme** —
  `${XDG_STATE_HOME:-~/.local/state}/hornero/signal/scheme.json` written
  atomically by `horneroctl theme apply` (or the shell for built-ins) and
  watched by the shell. Wallpapers never recolour the UI.
- **Built-in ids** — `hornero-signal-night` (default), `hornero-signal-day`,
  `hornero-signal-contrast`; `hornero-dark/light/199x` selections migrate
  once to night/day/night.
- **Default preset** — `cockpit`; default mode — `everyday`.
