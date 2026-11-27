# RFC 0001 — Hornero Signal

- **Status** — Accepted (2026-11-16); **superseded in part** by
  [RFC 0002 — Hornero Chromatic](rfc-0002-hornero-chromatic.md) (2026-11-17,
  optional dynamic colour; §1, §3.1 and §9 below are annotated where it
  applies); amended 2026-11-27 (amendment 3: Hornero Signal Design Renaissance
  — Cool Ceramic Day, Blue-Hour Graphite Night, `inkFaint` discipline and
  curated Argentine Light originals, see the end of this document); amended
  2026-11-17 (amendment 4: Cozy Hackerpunk atmosphere, see the end of this
  document); amended 2026-11-16 (amendment 2: contrast-driven palette tweaks,
  optional `glow` role, Signal Bezel direction; amendment 1: WOW + WORK
  ambition, motion springs, layout catalogue, experience modes,
  instrumentation, integration contracts)
- **Implementation** — In progress; nothing is validated on a physical
  host yet. See [Implementation status](#implementation-status).
- **Scope** — Every first-party HorneroOS surface: shell, PluginKit and
  extensions, config (GTK/Qt/terminal/compositor), horneroctl, greeter,
  installer, website, docs, brand
- **Supersedes** — The Material 3–derived token system (`M3Palette`, `m3*`
  roles, Material Symbols, Material wallpaper synthesis) and the "Hornero
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

RFC 0002: removing the Material machinery does not remove dynamic colour.
[RFC 0002 — Hornero Chromatic](rfc-0002-hornero-chromatic.md) restores
wallpaper-derived palettes and variants as an **option**, with a native
engine that produces the Signal roles of §3.1 directly. The curated palettes
of §3.2 remain the default and the fallback.

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
in [Signal Visual Language](signal-visual-language.md). Amendment 2: the
chosen direction is **Signal Bezel** (matte instrument modules, sunken
readout wells, oscilloscope telemetry, trigger notches), selected over
*Carta* and *Transmisión* after a documented comparison; it borrows
dimension lines from Carta and channel strips / on-air chips from
Transmisión. The `signal` experience mode must be visibly richer than
`everyday` (framed instrument compositions, live luminous traces, larger
telemetry) — not the same desktop with more widgets. It must look exceptional with
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
- `inkFaint` — Disabled controls and decorative marks only (ticks, dimension
  rules, `/` separators) — **never** essential or readable text (use
  `inkMuted` for readable secondary text, labels, captions and hints)
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
- `glow` — Optional luminous accent for live telemetry (amendment 2)
- `focus` — Keyboard focus ring (defaults to `cue`)
- `term0`…`term15` — Terminal ANSI palette

Removed with no replacement: all `*Fixed*`, `*_paletteKeyColor`,
`surfaceTint`, `surfaceVariant`, `onBackground` and the external Material
colour library. The Material scheme types and Material "follow wallpaper"
synthesis are removed; RFC 0002 replaces the capability (not the roles or
the algorithm) with Hornero Chromatic variants and an optional wallpaper
follow policy, specified in [RFC 0002](rfc-0002-hornero-chromatic.md).

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

`hornero-signal-night` is the factory default: cool blue-hour graphite
instrument panels with crisp off-white ink, amber live signal and celeste
focus cue. `hornero-signal-day` is luminous white ceramic and pale aluminum
instrument panels with dark slate ink, deep amber signal and deep celeste cue.

| Role             | Signal Night | Signal Day |
| ---------------- | ------------ | ---------- |
| `ground`         | `#0C1016`    | `#E8EDF4`  |
| `sunken`         | `#10151C`    | `#E0E6EF`  |
| `base`           | `#141B24`    | `#EEF2F7`  |
| `panel`          | `#1B2430`    | `#F5F8FC`  |
| `raised`         | `#24303D`    | `#FCFCFE`  |
| `lifted`         | `#2C3947`    | `#FFFFFF`  |
| `ink`            | `#E6EBF1`    | `#283344`  |
| `inkMuted`       | `#A9B7C6`    | `#505E70`  |
| `inkFaint`       | `#8999AB`    | `#606D80`  |
| `rule`           | `#2D3B4B`    | `#D2DAE6`  |
| `ruleStrong`     | `#8393A6`    | `#7A8798`  |
| `focus`          | `#8BCEF0`    | `#145D86`  |
| `signal`         | `#F2AC52`    | `#864700`  |
| `onSignal`       | `#1E1304`    | `#FFFFFF`  |
| `signalWell`     | `#3D2B12`    | `#FCE9C8`  |
| `onSignalWell`   | `#FFE0B0`    | `#432300`  |
| `cue`            | `#8BCEF0`    | `#145D86`  |
| `onCue`          | `#071A26`    | `#FFFFFF`  |
| `cueWell`        | `#163345`    | `#D8EEF9`  |
| `onCueWell`      | `#D6EFFC`    | `#0B334B`  |
| `phosphor`       | `#8DDBAF`    | `#1E6448`  |
| `onPhosphor`     | `#071D12`    | `#FFFFFF`  |
| `phosphorWell`   | `#153425`    | `#D6F4E8`  |
| `onPhosphorWell` | `#D1F5E0`    | `#0E3425`  |
| `alert`          | `#FF8494`    | `#9C293E`  |
| `onAlert`        | `#24070C`    | `#FFFFFF`  |
| `alertWell`      | `#421922`    | `#FADDE4`  |
| `onAlertWell`    | `#FFD6DC`    | `#4E111E`  |
| `inverse`        | `#E6EBF1`    | `#283344`  |
| `onInverse`      | `#1B2430`    | `#F5F8FC`  |
| `inverseSignal`  | `#864700`    | `#F2AC52`  |
| `scrim`          | `#000000`    | `#000000`  |
| `shadow`         | `#000000`    | `#000000`  |
| `glow`           | `#FFC06B`    | `#864700`  |

**Signal High Contrast** keeps the roles, uses `#000000` ground, `#FFFFFF`
ink, `#FFC247` signal, `#8FD3FF` cue and pure white `ruleStrong`.

Other catalogue themes (regional Argentina photo themes, community ports)
remain valid **if** they provide a complete schema-v2 role set that passes the
contrast tests. Themes that only existed as M3 seeds are removed or ported.

Amendment 2 tightened contrast on `sunken` readout wells and `lifted` tooltips
and added the optional `glow` role (default: `signal`) for luminous accents:
only on live telemetry traces and, in the `signal` experience mode, the active
on-air bar and on-air chips; blur ≤ 4 px, alpha ≤ 40 %, at most three glowing
items on screen, never animated, disabled in day themes, high contrast,
`focus` and `gaming` modes and on Cockpit Clear bars. Amendment 3 (see below)
later refined the Night and Day flagship hexes to blue-hour graphite and white
ceramic / pale aluminum.

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
| `settleFast` | `0.34, 1.3, 0.5, 1`   | Quick controls, chips        |

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
   with the `horneroctl mode` command group (list, get, set, reset, status) as
   the system interface.
3. **Layout preset** — bar composition (Cockpit, Hornero Left, …).
4. **Theme** — Signal roles and wallpaper.

Rules: modes are switched explicitly by the user (launcher, Control Center,
IPC, CLI); optional automatic switching (e.g. fullscreen game → `gaming`) is
off by default, local-only, shown in the UI and reversible with one action.
User customisations per mode are preserved; the `horneroctl mode reset` verb
and a Control Center action return to the factory `everyday` + Cockpit + Signal
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
  `schemaVersion: 2`, `id`, `name`, `mode` (`dark` | `light`), `palette`
  (exactly the §3.1 roles; `glow` optional, absent → `signal`), `terminal`
  (array of 16 hex colours), `gtkTheme`, `iconTheme`, `defaultWallpaper`,
  `wallpaperDir`; optional `description`, `tags`, `collection`,
  `collectionOrder`, `colorOnly`, `version`, `$schema`. Removed with no
  replacement: M3 seeds, `schemeType`, variants, flavours, `darkMode`,
  `gtkPreferDark`, `family`, `tokensVersion`, `components`.
- **Live scheme** —
  `${XDG_STATE_HOME:-~/.local/state}/hornero/signal/scheme.json` =
  `{"schemaVersion":2,"id":…,"mode":…,"palette":{role:"#RRGGBB"},"terminal":[16]}`
  (`glow` only when the theme defines it), written atomically by
  horneroctl's theme apply path (or the shell for built-ins) and watched by
  the shell. With a curated theme, wallpapers never change the palette (only
  Cockpit Clear's per-region choice between the theme's night and day inks
  follows the wallpaper).
  RFC 0002: the reserved theme id `hornero-chromatic` selects Hornero
  Chromatic; horneroctl then writes a generated scheme with the optional,
  additive `chromatic`, `minSurfaceAlpha` and `clearInk` blocks
  ([RFC 0002](rfc-0002-hornero-chromatic.md) §8).
- **Built-in ids** — `hornero-signal-night` (default), `hornero-signal-day`,
  `hornero-signal-contrast`; `hornero-dark/light/199x` selections migrate
  once to night/day/night. The retired `neon-city`, `vapor-dreams`,
  `soft-morning` and `warm-sunset` have no Signal equivalent and migrate to
  night or day by their mode. This is a one-shot data migration, not an
  alias layer.
- **Fonts and glyphs** — families `IBM Plex Sans`, `IBM Plex Mono`,
  `IBM Plex Sans Condensed` from `ttf-ibm-plex`;
  `assets/fonts/hornero-glyphs.ttf` loaded by the shell through
  `Glyph { name }`, with no system icon-font dependency.
- **Default preset** — `cockpit`; default mode — `everyday`.

## Implementation status

*As of 2026-11-17, from the `main` branches of each repository. This section
records what is merged and where it was checked. It is not a claim that the
design is accepted visually: no part of this RFC has been validated on a
physical host, and only one smoke scenario has run in the QA virtual
machine.* The mission checklist and discussion live in
[HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28).

### Where each workstream stands

| Workstream (section 6) | Repository | Merged on `main` |
| --- | --- | --- |
| W1 Tokens, theme schema v2, themes, generators, Cockpit default | config | [128](https://github.com/HorneroOS/config/pull/128), [133](https://github.com/HorneroOS/config/pull/133), [134](https://github.com/HorneroOS/config/pull/134), [135](https://github.com/HorneroOS/config/pull/135), [136](https://github.com/HorneroOS/config/pull/136) (the last four resync the shell defaults) |
| W2 Shell foundation, motion tokens, M3 removal | shell | [475](https://github.com/HorneroOS/shell/pull/475) |
| Anchored-surface solver and popouts (section 4) | shell | [477](https://github.com/HorneroOS/shell/pull/477), [482](https://github.com/HorneroOS/shell/pull/482) |
| W3 Appearance backend | hornero | [421](https://github.com/HorneroOS/hornero/pull/421), [424](https://github.com/HorneroOS/hornero/pull/424) |
| W4 Controls, bar, Cockpit default, workspace cells | shell | [483](https://github.com/HorneroOS/shell/pull/483), [484](https://github.com/HorneroOS/shell/pull/484), [494](https://github.com/HorneroOS/shell/pull/494) |
| W4 Cockpit Clear with adaptive ink | shell | [490](https://github.com/HorneroOS/shell/pull/490) |
| W4 Launcher, notifications, OSD, session, toasts | shell | [481](https://github.com/HorneroOS/shell/pull/481) |
| W4 Dashboard, lock, Welcome, sidebar, utilities, background | shell | [492](https://github.com/HorneroOS/shell/pull/492), [493](https://github.com/HorneroOS/shell/pull/493), [497](https://github.com/HorneroOS/shell/pull/497), [499](https://github.com/HorneroOS/shell/pull/499), [500](https://github.com/HorneroOS/shell/pull/500) |
| W4 Control Center recomposition (in progress) | shell | [488](https://github.com/HorneroOS/shell/pull/488), [489](https://github.com/HorneroOS/shell/pull/489), [491](https://github.com/HorneroOS/shell/pull/491), [495](https://github.com/HorneroOS/shell/pull/495), [501](https://github.com/HorneroOS/shell/pull/501), [504](https://github.com/HorneroOS/shell/pull/504), [506](https://github.com/HorneroOS/shell/pull/506), [508](https://github.com/HorneroOS/shell/pull/508) |
| W4 Companion and area picker | shell | [496](https://github.com/HorneroOS/shell/pull/496) |
| Experience modes (section 5a) | shell | [479](https://github.com/HorneroOS/shell/pull/479), [487](https://github.com/HorneroOS/shell/pull/487) |
| Signal instrument deck (section 5b) | shell | [503](https://github.com/HorneroOS/shell/pull/503), [505](https://github.com/HorneroOS/shell/pull/505), [507](https://github.com/HorneroOS/shell/pull/507) |
| W5 PluginKit 3 host | shell | [486](https://github.com/HorneroOS/shell/pull/486) |
| W5 First-party extensions on PluginKit 3 | plugins | [63](https://github.com/HorneroOS/plugins/pull/63), [64](https://github.com/HorneroOS/plugins/pull/64), [65](https://github.com/HorneroOS/plugins/pull/65), [66](https://github.com/HorneroOS/plugins/pull/66), [67](https://github.com/HorneroOS/plugins/pull/67), [68](https://github.com/HorneroOS/plugins/pull/68), [69](https://github.com/HorneroOS/plugins/pull/69) |
| W6 Greeter | greeter | [44](https://github.com/HorneroOS/greeter/pull/44) |
| W6 Installer branding | installer | [98](https://github.com/HorneroOS/installer/pull/98), [100](https://github.com/HorneroOS/installer/pull/100) |
| W7 Website | website | [224](https://github.com/HorneroOS/website/pull/224), [225](https://github.com/HorneroOS/website/pull/225), [226](https://github.com/HorneroOS/website/pull/226), [227](https://github.com/HorneroOS/website/pull/227), [229](https://github.com/HorneroOS/website/pull/229), [230](https://github.com/HorneroOS/website/pull/230) |
| W8 Docs | docs | [107](https://github.com/HorneroOS/docs/pull/107), [108](https://github.com/HorneroOS/docs/pull/108), [110](https://github.com/HorneroOS/docs/pull/110), [111](https://github.com/HorneroOS/docs/pull/111), [113](https://github.com/HorneroOS/docs/pull/113) and the phase 2 pages |
| W9 QA tooling | qa | [85](https://github.com/HorneroOS/qa/pull/85), [86](https://github.com/HorneroOS/qa/pull/86) |

Not done, by design or not yet reached:

- The rest of the Control Center panes and a few surfaces (layout picker,
  window info, polkit, and the companion UI), tracked in
  [shell#485](https://github.com/HorneroOS/shell/issues/485), and the
  remaining experience-mode evidence in
  [shell#478](https://github.com/HorneroOS/shell/issues/478).
- The website product-data refresh and a fresh QA image minted from the
  merged mains.
- Every item in section 7.1 that needs the real host.

### Where each part was validated

"Offscreen / CI" means automated tests, schema and contrast checks, static
scans and offscreen QML renders that ran in CI or on a developer machine
without a compositor. "QA VM" means the disposable guest in
[HorneroOS/qa](https://github.com/HorneroOS/qa). "Host" means a real desktop
session on physical hardware.

| Area | Offscreen / CI | QA VM | Host |
| --- | --- | --- | --- |
| Theme schema, palettes and contrast | Yes | No | No |
| Shell foundation, glyphs, static M3 scan | Yes | No | No |
| Placement solver | Yes | No | No |
| Popout geometry, motion timing, perf | Offscreen tests | No | No |
| Bar, Cockpit, Cockpit Clear | Offscreen renders | No | No |
| Launcher, OSD, session, lock, Welcome | Offscreen renders | No | No |
| Control Center panes | Offscreen renders | No | No |
| Experience profiles, state and deck solver | Yes | No | No |
| Experience page and Signal deck visuals | Offscreen tests | No | No |
| Per-mode idle processor cost | No | No | No |
| PluginKit 3 host and 36 extensions | Validators, offscreen | No | No |
| `horneroctl` appearance backend | Unit tests | No | No |
| Greeter and installer branding | CI | No | No |
| Website | Build, a11y gate, browser captures | No | No |
| Desktop reaches ready on a Signal image | n/a | Smoke only | No |

The one QA VM result is the `smoke/desktop-ready` scenario, which passed on
an image built from earlier Signal mains (it loaded the live Signal scheme
and a desktop capture was inspected by a person). It does not cover the
surfaces merged since. Cockpit Clear has not been checked over real
wallpapers, the anchored popouts have not been timed on a compositor, and
no preset has been captured at the resolutions and scales listed in
section 7.1. Until that evidence exists, treat the visual claims in the
user pages as intent, not result.

### Definition of done (section 7)

| Criterion | State |
| --- | --- |
| No Material references in first-party code | Gated in shell and plugins |
| Contrast tests for every shipped theme | In config (`test_contrast.sh`) |
| Solver edge, scale, multi-monitor tests | In shell tests |
| Cockpit and presets captured on the host | Not done |
| VM install reaches first boot in Cockpit | Not done |

The Material scan is gated in the shell and plugins repositories only; the
other repositories are not yet gated by a static scan.

## Amendment 4 — Cozy Hackerpunk (2026-11-17)

Direction: **Cozy Hackerpunk, Argentine retrofuturism, personal computing**
([study](signal-cozy-hackerpunk-study.md)). Signal Bezel remains the
structure; this amendment changes atmosphere, not contracts.

- **Roles unchanged.** §3.1 gains no roles. Warmth comes from a curated
  palette and from atmosphere values derived from the active palette.
- **New flagship palette.** `hornero-signal-dusk` (collection `hornero-signal`,
  order 4): warm charcoal-aubergine surfaces, cream ink `#F1E6D2`, copper
  signal `#F29A4A`, cyan cue, phosphor, `glow` `#FFB070`. Same gates as
  Night; Night, Day and High Contrast keep their values.
- **Atmosphere** (lamp wash, soft inner light, vignette, grain) is allowed as
  a low-alpha layer under text with hard ceilings, user-tunable, disabled in
  High Contrast and by low power, and never counted as glow. The glow budget
  of Amendment 2 is unchanged.
- **Typography.** IBM Plex remains the family. Adds a *plate* label style
  (Plex Sans Condensed SemiBold, uppercase, +14 % tracking) for enum states,
  at most four type treatments per screen, tabular figures for every changing
  value.
- **Rose/violet** are rare accents (terminal, tags, special moments), never
  the sole carrier of meaning.
- **Voice.** Warm microcopy in the user's language (voseo in Spanish) with a
  plain voice always one switch away.
- **Originality.** The reference series informs principles only; no
  third-party character, artwork, logo or prop is used (study §2).

## Amendment 3 — Hornero Signal Design Renaissance (2026-11-27)

Direction: **Cool Ceramic Day, Blue-Hour Graphite Night and Curated Argentine
Light Originals**. Role names (§3.1), typography (§3.3), glyphs (§3.4),
geometry (§3.5) and motion (§3.6) are unchanged; this amendment refines the
flagship Night and Day palettes, clarifies Light catalogue roles and enforces
`inkFaint` discipline.

- **Design rationale for Signal Day (`hornero-signal-day`).** Earlier Signal
  Day (`#F2EEE5`, OKLCH `C = 0.013, h = 86.8°`) carried a warm yellowish
  technical-drawing paper cast and sat close to the warm Light originals.
  Amendment 3 replaces that cast with luminous white ceramic and pale
  aluminum instrument panels (`#E8EDF4` `ground` through `#FFFFFF` `lifted`,
  `C ≤ 0.004`), dark slate ink (`#283344` / `#505E70`), deep amber
  (`#864700`), deep celeste (`#145D86`), mint (`#1E6448`) and rose-crimson
  (`#9C293E`).
- **Blue-hour refinement for Signal Night (`hornero-signal-night`).** Deepens
  Night to cool blue-hour graphite (`#0C1016`..`#2C3947`) with crisp
  off-white ink (`#E6EBF1` / `#A9B7C6`), amber (`#F2AC52`), celeste
  (`#8BCEF0`), mint (`#8DDBAF`), rose-coral (`#FF8494`) and `glow`
  (`#FFC06B`), sharpening separation from neutral-slate community themes.
- **Dusk and High Contrast preserved.** `hornero-signal-dusk` remains the
  warm workshop copper/charcoal dark flagship; `hornero-signal-contrast`
  remains the protected AAA-passing high-contrast palette (`#000000` ground,
  `#FFFFFF` ink, `#FFC247` signal, `#8FD3FF` cue, `#FFFFFF` `ruleStrong`).
- **Warm paper preserved explicitly.** The warm drafting and highland paper
  aesthetic is preserved intentionally in `sierras` (`#F3EDDD`, warm
  dry-grass paper) and `quebrada` (rose-terracotta stone paper) instead of
  tinting the flagship Day palette.
- **Curated Argentine Light originals.** Three Light originals join
  `hornero-originals`:
  - `jacaranda` (**Jacarandá**, order 10) — Buenos Aires spring in bloom: cool
    porcelain-lavender ceramic panels (`#EAE7F3`..`#FFFFFF`), deep indigo-slate
    ink (`#2B2640`), lavender-violet `signal` (`#6538A6`) and celeste `cue`
    (`#185E8A`).
  - `glaciar` (**Glaciar**, order 11) — Patagonian glacier ice: cool
    ice-white ceramic panels (`#E3EFF5`..`#FFFFFF`), deep fjord-slate ink
    (`#1F3240`), celeste `signal` (`#0E5D7E`) and turquoise-mint `cue`
    (`#0F6466`).
  - `ceibo` (**Ceibo**, order 12) — National blossom in daylight: neutral
    porcelain surfaces (`#ECE9EE`..`#FFFFFF`), deep plum-slate ink
    (`#2E2630`), coral-rose `signal` (`#9E2A48`) and botanical mint
    `phosphor` (`#1F6644`).
- **`inkFaint` discipline.** Reaffirms §3.1: `inkFaint` is reserved strictly
  for disabled controls and decorative hairlines, tick marks, dimension rules
  and `/` separators. Essential or readable text (timestamps, captions,
  metadata, placeholders, validation copy and hints) must use `inkMuted` or
  `ink`.
- **Single-source built-in sync.** Built-in fallbacks (`Signal.qml`,
  `cover.js`, `Signal.js`, `global.css`) and brand assets must match the
  canonical `hornero-signal-{night,day,contrast}/theme.json` definitions.
