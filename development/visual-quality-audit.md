# Visual quality audit — Hornero Signal

- **Status** — Independent audit, 2026-11-17
- **Tracking** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28) and the
  visual-audit tracking issue linked from it
- **Design authority** — [RFC 0001](rfc-0001-hornero-signal.md) with its
  amendments and [Signal Visual Language](signal-visual-language.md)
- **Audience** — maintainers deciding what blocks the Signal release,
  contributors picking up visual work

This is a critic's audit, not a status report. It judges what exists in the
evidence, as if for a curated r/unixporn showcase (WOW) and for a workstation
used eight hours a day (WORK). Every finding is filed as a `visual-audit` issue
in the repository that owns the fix. Nothing in this document was checked
against a live session: the auditor worked only from existing evidence and asks
for the captures listed in [What was not verified](#what-was-not-verified).

## 1. Method and evidence classes

Images were opened and read, not trusted from reports. Evidence classes, from
strongest to weakest:

- **H, real host** — the maintainer's Hyprland session: dashboard, launcher,
  Control Center Appearance, Cockpit, lock and 64 px strips of every preset and
  edge. Used for bars, dashboard, launcher, lock and Appearance.
- **V, QA VM** — `qa` `docs/evidence/signal-vm-20261117/` and the run bundles
  `20261117T02*` to `T03*` (1280x800). Used for layouts, popouts, Clear ink and
  the installer gate.
- **O, offscreen** — `shell` `.github/evidence/**` (Qt offscreen, stand-in
  wallpaper). Used for every shell surface in Night, Day and High Contrast.
- **W, web and greeter** — `greeter` `screens/signal/`, `website`
  `.github/evidence/signal-*` and `public/og/`. Used for the greeter, website
  and social cards.
- **C, concept** — `docs` `development/assets/signal-visual-language/`. Not
  product evidence; not used to rate anything.

Host captures contain fragments of the maintainer's terminal and browser. They
are cited by name in words and were not copied into any repository.

Two cautions apply to every rating:

1. **Staleness.** Host captures from 00:2x to 01:33 and the VM runs up to 03:2x
   were taken on images and checkouts older than shell main (`f47f323`). The VM
   galleries show 52 px and 46 px bars; main now ships 28 px and 24 px
   (#517-#520). Where a finding was likely fixed by a later merge it says so and
   asks for a re-capture instead of claiming a defect.
2. **Empty stage.** The VM captures show a blueprint-grid wallpaper with no
   window, so they cannot show how bars relate to content (finding VA-24).

## 2. Verdict

**The design language is strong and the product is close behind it, but the bar
is not yet a showcase and one shipped artefact blocks the release.**

What is genuinely excellent, and should be protected:

- The Performance dashboard on the host: channel-numbered eyebrows, graticule
  scopes, segment meters, a dimension line under the memory bar. It is the one
  place that looks like nothing else on r/unixporn.
- The greeter: a 24 h daypart ribbon, readout wells and corner brackets over
  credited Argentine stills. Distinct, legible and coherent.
- The lock clock, the website typography and the notification popup anatomy.
- Thin bars. The host strips at 28 px with 3 px radii are the first time the
  bars look like instruments and not tablets.
- Honest empty states (em dash, segments off) where the data is missing.

What keeps it from a showcase:

- **Colour discipline in the bar.** Six hues in a 28 px strip (VA-04) and the
  distro's logo in green where the one permanent amber mark belongs (VA-03).
- **Two grammars.** Popup notifications versus history (VA-08), Signal panes
  versus older sub-pages (VA-18), eyebrow headers versus a generic titlebar
  (VA-07).
- **The marquee interactions have no proof.** No real-host popout, no motion
  capture, no glow capture anywhere (VA-11, VA-06).
- **Plugins at scale.** Bar items overprint core segments and widgets overlap
  (VA-05, VA-06).
- **First impressions outside the shell.** The ISO's live session is pre-Signal
  and visibly broken (VA-01), the website leads with the previous appearance
  (VA-20), the first-run Shortcuts page is empty (VA-09).

Release recommendation: **VA-01 is the only P0.** The P1 set below should land
before the Signal preview is announced; VA-11 (popout proof) is a P1 that
becomes a P0 if the release notes advertise the anchored-popout interaction.

## 3. Scorecard

Ratings run from 1 (failing) to 5 (exemplary); `-` means no evidence exists for
that gate, not a good score. Gates: **VE** visual excellence, **OR** originality
versus Material/Caelestia derivatives, **CO** consistency of tokens across
surfaces, **US** usability, **DI** discoverability, **AC** accessibility, **PF**
performance, **TQ** technical quality of the rendering, **CP** completeness.
Evidence classes as in section 1. `PF` is `-` everywhere: no frame-time or
idle-CPU figure exists for any surface (RFC 0001 section 7.1 and visual language
11.4 require them).

| Surface | Ev | VE OR CO US DI AC PF TQ CP |
| ------- | -- | ----------------------- |
| Cockpit (factory default) | HVO | 3  4  3  4  3  3  -  4  3 |
| Cockpit Clear | VO | 2  4  3  3  3  3  -  3  2 |
| Horizon | HV | 4  3  3  4  3  3  -  4  3 |
| Islands | HV | 3  4  3  4  3  3  -  3  3 |
| Minimal Float (cozy-minimal) | HV | 4  3  4  4  3  3  -  4  3 |
| Dock | HV | 3  3  3  4  4  3  -  3  3 |
| Classic top / bottom | HV | 3  2  3  4  4  3  -  4  3 |
| Minimal Top | HV | 4  3  4  4  3  3  -  4  3 |
| Minimal Left rail | V | 3  4  3  3  2  3  -  3  2 |
| Studio | HV | 3  3  3  4  3  3  -  3  2 |
| Gaming | HV | 3  3  3  3  3  3  -  3  2 |
| Hornero Left / Right | HV | 3  2  3  4  3  3  -  3  3 |
| Workspace and window indicators | HVO | 4  4  4  4  3  4  -  4  3 |
| Launcher | HO | 4  3  4  4  4  3  -  4  4 |
| Dashboard (all four tabs) | HO | 4  4  4  3  3  3  -  3  3 |
| Control Center window frame | HV | 2  2  2  3  3  3  -  3  3 |
| Appearance, themes, wallpapers | HVO | 2  2  2  2  3  3  -  3  3 |
| Audio, Displays, Power, A11y, Input | O | 4  3  4  4  3  3  -  4  3 |
| Network, Bluetooth, VPN | O | 2  2  2  3  3  3  -  3  2 |
| Bars, Layout, Windows, Keybinds panes | O | 3  3  3  2  2  3  -  3  3 |
| Layout Picker | O | 2  2  3  2  2  3  -  3  3 |
| Quick settings (utilities drawer) | O | 3  2  3  4  4  3  -  3  3 |
| Notification popups and toasts | O | 4  4  4  4  3  3  -  4  4 |
| Notification history (sidebar) | O | 2  2  2  3  3  3  -  3  3 |
| OSD | O | 3  3  3  3  3  3  -  3  3 |
| Session / power menu | O | 3  2  3  4  3  3  -  4  3 |
| Anchored popouts and tooltips | V | 3  4  3  -  3  -  -  3  1 |
| Telemetry, scopes, meters, instrument deck | HVO | 4  5  4  3  3  3  -  3  3 |
| Companion (Javi) | O | 3  3  2  3  3  3  -  3  1 |
| Plugin bar items | V | 2  3  2  2  2  3  -  2  3 |
| Plugin desktop and dashboard widgets | OV | 4  4  4  3  3  3  -  3  3 |
| Plugin popovers | - | -  -  -  -  -  -  -  -  - |
| Marketplace (Extensions pane) | O | 3  3  3  3  3  3  -  3  2 |
| Lock | HO | 3  4  4  3  -  3  -  4  3 |
| Greeter | W | 4  5  4  3  3  3  -  4  3 |
| Installer (Calamares and slides) | VW | 2  2  2  3  3  2  -  2  1 |
| Welcome | O | 3  3  3  2  3  3  -  3  2 |
| Website pages | W | 4  4  4  4  4  -  -  4  3 |
| Social cards | W | 3  3  4  -  -  -  -  3  2 |
| Docs site | - | -  -  -  -  -  -  -  -  - |

Findings and notes per surface:

- Cockpit (factory default): VA-03, 04, 11, 12
- Cockpit Clear: VA-10
- Horizon: VA-04, 12
- Islands: VA-04; VM pills predate #517
- Minimal Float (cozy-minimal): VA-04
- Dock: full-colour app icons inside a mono bar
- Classic top / bottom: VA-04
- Minimal Top: VA-12
- Minimal Left rail: numerals only; no capture with a window
- Studio: meters per spec 14.12 not seen
- Gaming: hide-under-fullscreen unverified
- Hornero Left / Right: VA-04; Caelestia-inspired by design, attributed
- Workspace and window indicators: VA-12; active numeral missing in one
  offscreen render
- Launcher: strongest daily surface
- Dashboard (all four tabs): VA-13
- Control Center window frame: VA-07
- Appearance, themes, wallpapers: VA-07, shell#514
- Audio, Displays, Power, A11y, Input: VA-16
- Network, Bluetooth, VPN: VA-18; VPN pane not captured
- Bars, Layout, Windows, Keybinds panes: VA-17, 18
- Layout Picker: VA-17
- Quick settings (utilities drawer): VA-16
- Notification popups and toasts: VA-15
- Notification history (sidebar): VA-08
- OSD: VA-15
- Session / power menu: large generic icon list
- Anchored popouts and tooltips: VA-11
- Telemetry, scopes, meters, instrument deck: VA-06, 13
- Companion (Javi): VA-18; chat UI not captured
- Plugin bar items: VA-05
- Plugin desktop and dashboard widgets: VA-06, 22
- Plugin popovers: no capture
- Marketplace (Extensions pane): catalogue shows 0 installed everywhere
- Lock: VA-14
- Greeter: VA-19
- Installer (Calamares and slides): VA-01, 02
- Welcome: VA-09
- Website pages: VA-20, 21
- Social cards: VA-20
- Docs site: VA-21; no capture

Accessibility is rated 3 where contrast and roles are plausible but not measured
(only Clear ink has numbers); nothing was rated above 3 without numbers, nothing
below without a specific defect.

## 4. Cross-cutting critique

### Type scale

The RFC defines steps (`small 11`, `body 13/14`, `title 18`, `display 28`).
Observed sizes across surfaces: ~9 (greeter and lock error), 10 (Companion
descriptions), 11, 12, 13, 14, 16, 18, 22, 24 and ~34 (Appearance `Preview`).
Eyebrows alone appear at ~11, ~14 (deck widgets) and ~16-18 (notification
history). The two ends are the worst offenders: errors and status lines under 11
px (VA-14, VA-19) and display-size headings on trivial labels (VA-07).
Marathon's "fontslop" warning, cited in the visual language itself, applies.

### Spacing rhythm and alignment

Bars are on the 4 px grid and read well, but several alignments fail: the `ST`
token sits ~3 px below the baseline of its neighbours (VA-12); dashboard columns
end at different heights (VA-13); Control Center rows range from visibly under
32 px (Bars) to ~44 px (Audio) against a 32 px minimum (VA-18); plugin bar items
use three baselines (VA-05).

### Colour

The language promises amber as a rationed signal. In practice amber is on every
slider thumb, every selected chip, the mark's neighbours and several tiles,
while green (clock, mark) and cyan (status) fill the bar (VA-04). The Control
Center selection grammar changes between amber-fill rows, brown wells and
dark-blue chips (VA-16).

### Shape

Radius discipline is mostly good (3 px). Exceptions: Clear slider capsules
(VA-10), the VM Islands pills (pre-#517, re-capture), windows rounded 10-12 px
on the host under the old Hyprland config (config#138 and #139 fixed this on
main; not re-captured), and the Control Center titlebar. The user's rule "no
oversized pills" is met in the strips from 01:33 and unproven elsewhere.

### Originality

Not Material, not Caelestia-derived, with two deliberate exceptions (Hornero
Left/Right, attributed). The scopes, wells, channel eyebrows and daypart ribbon
are original. Risk: wherever the shell falls back to generic rows (sidebar
history, Bluetooth/Network sub-pages, session menu) it reads as a competent dark
settings app. Originality is a property of the weakest surface that a screenshot
catches.

### Motion

No motion has been evidenced on any real compositor. The storyboard is a concept
render. Every motion statement in the spec is unverified (see coverage).

### Performance

No numbers. The 60 fps and 4 ms budget in visual language 11.4 cannot be
confirmed; shell#47 and #228 are the existing baseline issues.

### WOW versus WORK

- **WOW:** the Cockpit bars plus the dashboard are screenshot-worthy only once
  VA-03/04 land and a popout is shown; Signal mode is not visibly different from
  Everyday (shell#511); the lock is restrained to the point of being forgettable
  (VA-14); the website shows the previous appearance (VA-20).
- **WORK:** thin bars, workspace cells and the launcher are good daily-driver
  UI. The toast noise (VA-15), empty first-run pages (VA-09) and dense Control
  Center panes (VA-18) cost daily comfort.

## 5. Findings and prioritised backlog

P0 blocks the release. P1 should land before the Signal preview is announced. P2
is polish. Issues carry the label `visual-audit` and the `[Pn]` title prefix in
the owning repository.

### P0

- **VA-01** [installer#101](https://github.com/HorneroOS/installer/issues/101):
  Live ISO first run shows a broken pre-Signal desktop: icon ligature names as
  text, clipped Calamares banner

### P1

- **VA-02** [installer#102](https://github.com/HorneroOS/installer/issues/102):
  No capture of the Signal-themed Calamares pages; slideshow is Signal but the
  installer chrome is unverified
- **VA-03** [shell#529](https://github.com/HorneroOS/shell/issues/529): Bar mark
  is the distro logo in phosphor green, not the Hornero mark in signal amber
- **VA-04** [shell#530](https://github.com/HorneroOS/shell/issues/530): Bar
  chromatic discipline: green mark and clock, cyan status icons, amber sliders,
  red power, full-colour tray
- **VA-05** [shell#531](https://github.com/HorneroOS/shell/issues/531): Plugin
  bar items overlap core segments and ignore bar type scale and overflow
- **VA-06** [shell#532](https://github.com/HorneroOS/shell/issues/532): Desktop
  instrument deck: widgets overlap and clip their own content
- **VA-07** [shell#533](https://github.com/HorneroOS/shell/issues/533): Control
  Center Appearance: oversized Preview heading, raw wallpaper IDs, generic
  titlebar, ambiguous header control
- **VA-08** [shell#534](https://github.com/HorneroOS/shell/issues/534): Sidebar
  notification history is not Signal: icon tiles, run-on title and body,
  oversized controls
- **VA-09** [shell#535](https://github.com/HorneroOS/shell/issues/535): Welcome
  opens with an empty Shortcuts page and developer wording in the first-run flow
- **VA-10** [shell#536](https://github.com/HorneroOS/shell/issues/536): Cockpit
  Clear: solid outline fixes legibility but makes the clear bar heavy and
  sticker-like
- **VA-11** [shell#537](https://github.com/HorneroOS/shell/issues/537): Anchored
  popouts, the headline Signal interaction, have no real-host or populated-VM
  capture
- **VA-19** [greeter#45](https://github.com/HorneroOS/greeter/issues/45):
  Greeter login failure message and session default undermine an otherwise
  strong first impression
- **VA-20** [website#233](https://github.com/HorneroOS/website/issues/233): Site
  and social cards still show the pre-Signal desktop; no real Signal screenshot
  above the fold
- **VA-24** [qa#88](https://github.com/HorneroOS/qa/issues/88): Visual scenarios
  capture an empty wallpaper at 1280x800; real content, popouts, resolutions and
  numbers are missing

### P2

- **VA-12** [shell#538](https://github.com/HorneroOS/shell/issues/538): Bar end
  cluster polish: unlabeled `ST` token below the baseline, glyph-only bottom
  meters, cramped icon rhythm
- **VA-13** [shell#539](https://github.com/HorneroOS/shell/issues/539):
  Dashboard Performance tab: empty scopes on open, truncated CPU name, ragged
  column bottoms
- **VA-14** [shell#540](https://github.com/HorneroOS/shell/issues/540): Lock
  screen: small authentication card, hairline through the clock, little WOW for
  a flagship surface
- **VA-15** [shell#541](https://github.com/HorneroOS/shell/issues/541): OSD and
  routine toasts: oversized dual-channel OSD, `Config loaded` and `Num lock
  enabled` noise
- **VA-16** [shell#542](https://github.com/HorneroOS/shell/issues/542): Switch
  control is a two-cell rocker whose off state looks selected
- **VA-17** [shell#543](https://github.com/HorneroOS/shell/issues/543): Layout
  Picker thumbnails are near-identical wireframes and descriptions truncate
- **VA-18** [shell#544](https://github.com/HorneroOS/shell/issues/544): Control
  Center panes mix generations: sub-page headers, tiny labels and chip styles
  differ between panes
- **VA-21** [website#234](https://github.com/HorneroOS/website/issues/234): Docs
  site and long-tail pages have no visual evidence
- **VA-22** [plugins#71](https://github.com/HorneroOS/plugins/issues/71):
  First-party widget copy leaks implementation detail; fixtures and empty
  regions in evidence
- **VA-23** [docs#124](https://github.com/HorneroOS/docs/issues/124): Visual
  language still specifies 36/30 px bars and 3 px radius examples; shipped thin
  bars are 28/24 px with a density factor

Existing issues this audit builds on instead of duplicating: shell#511 (Signal
mode indistinguishable), #512 (stray 6 px notch mark), #513 (Power popout
clipped), #514 (theme card names and chips), #515 (Signal Contrast bar
edge), #516 (debug dump second output), #485 and #478 (surface recomposition and
deck), plugins#21 (Extension Quality Gate), qa#81 (Premium Acceptance Matrix),
qa#17 and #19, website#222 (held regeneration), hornero#427 (Signal release).

## 6. Finding detail

### VA-01 (P0)

Defect: Live ISO first run shows a broken pre-Signal desktop: icon ligature
names as text, clipped Calamares banner

- **Surface** — Installer (Calamares) + live-session shell + Welcome
- **Gates** — Visual excellence, Consistency, Completeness, Technical quality
- **Issue** — [installer#101](https://github.com/HorneroOS/installer/issues/101)
- **Evidence**
  - `HorneroOS/qa`
    `docs/evidence/signal-vm-20261117/installer-preview32-live-3gib-ram-gate.png`
    (VM, signed preview32 ISO, 1280x800).

The only capture of the shipped installer path shows four release-blocking
visual faults at once. (1) The live session's Hornero Welcome renders icon
ligature names as literal text (`waving_hand`, `explore`, `terminal`,
`chevron_right`, `apps`): the icon font is not resolving, so every row has a 20
px raw word where a glyph belongs and the page title reads `waving_hand`. (2)
The shell in the ISO is the pre-Signal one: workspace indicator is a cream
rounded pill with clipped text (`rmin`/`rmin` fragments), the left rail is
clipped mid-word (`p_wi`, `ndar_m`, `_setting`), accents are terracotta and
pink, not Signal amber. (3) Calamares is stock light grey (default Qt body and
buttons) with a dark terracotta banner that is clipped at the right edge (the
`PREVIEW` chip is cut to `PRE`) because the banner is wider than the 1280 px
slide area. (4) The error state (`does not have enough working memory`) is a
pink block with 14 px black text on a grey page: no Signal treatment, no
eyebrow, no hierarchy. A first-time user meets this before any Signal surface.

**Fix direction.** Rebuild the ISO from Signal mains and add a live-session
smoke scenario that fails if any visible string matches `^[a-z_]{4,}$` inside an
icon slot or if `fc-match 'Hornero Glyphs'` falls back. Ship the glyph and IBM
Plex fonts in the live package set. Re-cut the Calamares banner at 1024 px
maximum width and theme `stylesheet.qss` (installer repo
`image/calamares/branding/hornero/`) with the Signal tokens; reuse the website
eyebrow/hairline language already used by the slideshow.

**Not verified.** Real Calamares pages other than the welcome gate have no
Signal-era capture. The slideshow frames are web renders, not the running
installer.

### VA-02 (P1)

Defect: No capture of the Signal-themed Calamares pages; slideshow is Signal but
the installer chrome is unverified

- **Surface** — Installer (Calamares pages, slideshow)
- **Gates** — Completeness, Consistency, Accessibility
- **Issue** — [installer#102](https://github.com/HorneroOS/installer/issues/102)
- **Evidence**
  - `HorneroOS/installer` `.github/evidence/signal-installer-2026-11/` (banner,
    slideshow-00..04, niri-card): web/Qt renders of the slides only.
  - `HorneroOS/installer`
    `.github/evidence/provisional-installer-2026-10/live-boot-20261023/` shows
    the stock grey chrome.

The slideshow is the strongest installer asset (large `00`/`02`/`04` index
numerals in `inkFaint`, hairline rules, eyebrow labels, chip rows). But the
slide body text is small relative to the canvas, and the very large index
numeral is the loudest element on the slide while carrying no information.
Nothing proves the surrounding Calamares chrome follows: the October evidence is
stock. No scale (1.25x/1.5x) or HiDPI capture exists, and no Day variant.

**Fix direction.** Add `install/signal-pages` scenarios to qa (see qa#19),
extend the evidence README with a per-page checklist, and tighten the slideshow
type scale to the RFC steps (display 28, title 18, body 14 -> 16 for slides).

**Not verified.** All Calamares pages besides welcome; Day theme; scale > 1;
Spanish strings (the site is ES-first).

### VA-03 (P1)

Defect: Bar mark is the distro logo in phosphor green, not the Hornero mark in
signal amber

- **Surface** — Bars (Cockpit, Classic, Horizon, Studio, rails), launcher
  trigger
- **Gates** — Visual excellence, Originality, Consistency
- **Issue** — [shell#529](https://github.com/HorneroOS/shell/issues/529)
- **Evidence**
  - Host captures (maintainer-local, not committed): `host/04-cockpit.png`,
    `host/layouts/cockpit-top.png`, `host/layouts/horizon-top.png`; green
    chevron `A` at the bar start in every layout.
  - VM: `docs/evidence/signal-vm-20261117/shell-night-reference.png` and all
    `layouts-gallery-*` runs show the same glyph on a HorneroOS image.
  - Code: `modules/bar/components/OsIcon.qml` draws `SysInfo.osLogo` with
    `Signal.palette.phosphor`.
  - Spec: `signal-visual-language.md` section 4.1 ("Mark ... in `signal`. It is
    the launcher trigger and the only permanently amber item"); RFC 0001 section
    5.

The single brand element in the bar is the Arch Linux logo, tinted green. On a
HorneroOS install the first thing in the Cockpit bar is another distribution's
logo, and it carries the `phosphor` (data/level) colour instead of the one
permanent amber accent the language reserves for the mark. The dashboard Station
card also reads "Arch Linux".

**Fix direction.** Ship the mark as a symbolic glyph in Hornero Glyphs (or a
monochrome SVG), make `osLogo` an option (`bar.mark = hornero|distro|custom`),
default hornero, colour with `Signal.palette.signal`.

**Not verified.** Behaviour on a real HorneroOS install via the package set
(os-release content).

### VA-04 (P1)

Defect: Bar chromatic discipline: green mark and clock, cyan status icons, amber
sliders, red power, full-colour tray

- **Surface** — Bars (Cockpit, Horizon, Studio, Classic, rails)
- **Gates** — Visual excellence, Originality, Consistency
- **Issue** — [shell#530](https://github.com/HorneroOS/shell/issues/530)
- **Evidence**
  - Host (maintainer-local): `host/04-cockpit.png`,
    `host/layouts/cockpit-top.png`, `horizon-top.png`, `studio-top.png`;
    `host/layouts/sheet-1.png` to `sheet-3.png`.
  - VM: `layouts-gallery-cockpit-1`,
    `signal-vm-20261117/shell-night-reference.png`.
  - Spec: `signal-visual-language.md` section 4.1 (glyphs `ink`, secondary
    clusters `inkMuted`, amber only for live), RFC section 2 ("Amber marks only
    what is live").

A single 28 px strip shows at least six hues: green calendar glyph and green
minutes in the clock (`04 : 22`), a green mark, cyan status glyphs (volume,
wifi, bluetooth, mode), amber slider thumbs and amber `SIG`, red power, and
white/red full-colour tray icons (scissors, red monitor). The spec's discipline
(ink, inkMuted, one amber) is what would separate this from a rainbow Polybar;
currently it reads as a themed dashboard. The clock's split colouring makes the
hour and minute look like two readouts. Amber is also spent on every slider
thumb (permanently on at 43 %), so it no longer marks what is live.

**Fix direction.** Introduce `Segment.tone` (`ink`, `muted`, `live`, `alert`)
and route every bar component through it; remove per-component `phosphor`/`cue`
colours; reuse the ClearInk recolour path for tray icons.

**Not verified.** Day theme bar on host; High Contrast on host.

### VA-05 (P1)

Defect: Plugin bar items overlap core segments and ignore bar type scale and
overflow

- **Surface** — Plugin widgets (bar slots), Extensions island
- **Gates** — Visual excellence, Consistency, Usability, Technical quality
- **Issue** — [shell#531](https://github.com/HorneroOS/shell/issues/531)
- **Evidence**
  - Mission-local VM evidence `evidence/plugin-e2e/shots/dash-ext-12.png` and
    `bar-18-top.png` (36 plugins enabled, 1280x800).

With all 36 catalogue plugins enabled the top bar is unusable: `96.00 BPM` is
drawn over the Hornero mark, the first glyphs of the quick-actions cluster are
overprinted, `No input device` and `No output device` are 14 px labels (bar text
is 11-12 px), `No player` has no segment padding, three different baselines
coexist (`Moon ~49%`, `Sun Card`, `Aa`), and nothing collapses into the
Extensions island. Placeholder strings (`No input device`, `No player`) occupy
permanent bar width when the right behaviour is to hide. 36 enabled plugins is
an extreme case, but 6 to 8 is a normal user and the overlap logic is the same.

**Fix direction.** Measure plugin implicit widths in the bar host, clamp to a
max width (e.g. 160 px) with ellipsis, apply `Density` text steps via an
injected `Theme.text`, and add the overflow collapse in `ExtensionsIsland`.

**Not verified.** Real host with plugins enabled (the user's host runs v3
plugins but no bar capture with them exists).

### VA-06 (P1)

Defect: Desktop instrument deck: widgets overlap and clip their own content

- **Surface** — Signal instrument deck / desktop widgets
- **Gates** — Visual excellence, Technical quality, Completeness
- **Issue** — [shell#532](https://github.com/HorneroOS/shell/issues/532)
- **Evidence**
  - Mission-local VM evidence `evidence/plugin-e2e/shots/all36-desktop.png`
    (1280x800).
  - `HorneroOS/shell` `.github/evidence/signal-deck/deck-layout.png` is a solver
    diagram, not a render.

The Moon Phase widget sits on top of the Now Playing widget (the `NO PLAYER`
eyebrow shows through at the right edge of Moon's header); System Insight is cut
mid-row (`CORES` clipped at its bottom edge, the card is shorter than its
content); Network Scope leaves a 70 px dead area under `SESSION DOWN/UP`. The
widgets' eyebrows are visibly larger than the 11-12 px eyebrow used on the
dashboard and panes. This is the surface that will be in every r/unixporn
screenshot of Signal mode.

**Fix direction.** Feed the real implicit sizes into `services/deck.js` and
render from it; add a QML geometry test that instantiates the deck with the 6
deck widgets and asserts non-overlap and `contentHeight <= height`.

**Not verified.** Glow/scanlines on the deck; idle CPU with the deck running
(RFC 7.1 asks for numbers).

### VA-07 (P1)

Defect: Control Center Appearance: oversized Preview heading, raw wallpaper IDs,
generic titlebar, ambiguous header control

- **Surface** — Control Center window, Appearance pane
- **Gates** — Visual excellence, Consistency, Usability
- **Issue** — [shell#533](https://github.com/HorneroOS/shell/issues/533)
- **Evidence**
  - Host (maintainer-local): `host/03-cc-appearance.png` (1920x1080).
  - VM:
    `docs/evidence/signal-vm-20261117/shell-appearance-pane-chips-overlap.png`.

Hierarchy is inverted: the right column opens with `Preview` in ~34 px bold Plex
Sans, the biggest text in the window, over a card whose actual content (theme
name 16 px, description 13 px, five 16 px swatches) is small; the pane title
`Appearance` (24 px) carries a sort-arrows icon at the right with no label or
tooltip evidence. The window titlebar is a generic centred `Hornero Settings -
Appearance` with a tiny app icon and an X, which does not use the
eyebrow/registration language of the panes below it (`14 · SOUND & ALERTS`).
Wallpaper thumbnails are captioned with raw file stems (`wallhaven 73v179`,
`wallhaven lqxdqy`). In the host capture ten accordion headers (THEMES ...
HEALTH & SYNC) are collapsed so the main content of an Appearance pane, the
theme cards, is not visible without a click (partly fixed by #519 for upgraded
configs; not re-captured).

**Fix direction.** Move titlebar into the Signal channel header; derive display
names in the wallpaper model (`displayName`); reduce Preview to the shared
`PaneHeader` eyebrow.

**Not verified.** Day and High Contrast Appearance on host; 1.25x/1.5x scale.

### VA-08 (P1)

Defect: Sidebar notification history is not Signal: icon tiles, run-on title and
body, oversized controls

- **Surface** — Sidebar / notification history
- **Gates** — Visual excellence, Consistency, Usability, Discoverability
- **Issue** — [shell#534](https://github.com/HorneroOS/shell/issues/534)
- **Evidence**
  - `HorneroOS/shell`
    `.github/evidence/sidebar/after-night-offscreen-notifications.png` (470x700)
    versus `.github/evidence/notifications/after-night-offscreen.png`.

Popup notifications use the Signal recipe: eyebrow (`BUILDS · NOW`), 16 px bold
title on its own line, 14 px body, 1 px state edge. The history list beside it
does not: every card has an outlined ~40 px square holding a generic
speech-bubble glyph (same glyph for Terminal, Mail and Files, so it carries no
information), the app name and `now` share a row with a boxed `1 v` expander,
and title and body run together on one wrapped line (`Build passed All 1,246
tests passed.`, with the title only distinguished by weight). `Clear all` is a
filled ~30 px button, the biggest control in the column, while the urgent card
is a full red-filled icon tile. The header `04 · NOTIFICATIONS` is ~16-18 px
mono, well above the 11 px eyebrow used elsewhere. Same data, two grammars.

**Fix direction.** Extract the popup card into a shared `NotificationCard` used
by popup and history, parametrised by `compact`.

**Not verified.** Long-body, many-action and image notifications in history;
keyboard navigation.

### VA-09 (P1)

Defect: Welcome opens with an empty Shortcuts page and developer wording in the
first-run flow

- **Surface** — Welcome
- **Gates** — Completeness, Usability, Discoverability
- **Issue** — [shell#535](https://github.com/HorneroOS/shell/issues/535)
- **Evidence**
  - `HorneroOS/shell`
    `.github/evidence/welcome/after-night-offscreen-shortcuts.png`,
    `after-night-offscreen-start.png`.

The Shortcuts page, the page a new user is told to open to learn the desktop,
shows a keyboard glyph and "No keybindings found. Regenerate the shortcuts
manifest." That is a build-system instruction shown to end users. The Start page
lists "Compositor tuning - Not available" and "Low-latency audio profile -
Checked on first use" in three tiny (11 px) ledger columns whose rows wrap at 60
characters, so the first screen is dense status text with no single call to
action (the three action rows below compete equally). The filter chip `All` is a
~46x27 px amber-bordered box with a single option.

**Fix direction.** Generate the shortcut manifest in `hornero-config` packaging
(or read binds via `hyprctl binds -j` at runtime) and gate the page on non-empty
data; simplify StartPage copy.

**Not verified.** Welcome in Spanish; Day; large text.

### VA-10 (P1)

Defect: Cockpit Clear: solid outline fixes legibility but makes the clear bar
heavy and sticker-like

- **Surface** — Bars (Cockpit Clear, Horizon lower strip)
- **Gates** — Visual excellence, Originality, Accessibility
- **Issue** — [shell#536](https://github.com/HorneroOS/shell/issues/536)
- **Evidence**
  - Mission-local offscreen `evidence/ink/v3/*.png` (glacier, water, leafy,
    city): 2 px light/dark outlines on every glyph; slider track drawn as a
    white pill outline.
  - VM before the fix: `signal-vm-20261117/shell-clear-ink-iguazu-detailed.png`,
    `...quebrada-vivid.png`, `...ibera-bright.png` (illegible), and runs
    `wallpapers-ink-cockpit-clear-*` (52 px/46 px bars, pre-thin).
  - Spec: `signal-visual-language.md` section 12 (1 px halo, soft 4 px shadow
    only on detailed regions, wells become a 1 px outline).

shell#524 fixed the P0 (Clear text was unreadable over water and foliage in the
VM captures). The current answer uses a solid outline wider than the spec's 1 px
halo: strokes are fat enough that the 11 px mono labels (`CPU`, `MEM`) clog, and
the volume and brightness slider tracks become full-radius white capsules, the
only pill shapes left on the bar. Clock digits are outlined while the calendar
glyph beside them is not, so the group looks mismatched. On the bright glacier
wallpaper worst-cluster p5 contrast is still 2.86 (target >= 4.5 median, >= 3
worst).

**Fix direction.** Tune ClearInk to 1 px halo + conditional shadow, switch track
drawing to `Rectangle` with `radius: Appearance.rounding.small`, and apply the
halo at the `Segment` level so mixed glyph/text groups match.

**Not verified.** Cockpit Clear with a video or slideshow wallpaper; on the host
after thin bars; at 2x.

### VA-11 (P1)

Defect: Anchored popouts, the headline Signal interaction, have no real-host or
populated-VM capture

- **Surface** — Popouts (audio, network, status, resources), tooltips, notch
- **Gates** — Completeness, Visual excellence, Technical quality
- **Issue** — [shell#537](https://github.com/HorneroOS/shell/issues/537)
- **Evidence**
  - Host (maintainer-local): `host/05-top-audio-popout.png`,
    `05b-top-network-popout.png`, `06-bottom-popout.png` all show no popout;
    only a `Settings` tooltip is visible.
  - VM: `docs/evidence/signal-vm-20261117/shell-power-popout-text-clipped.png`,
    `shell-closed-popout-notch-crop-10x.png`, `shell-scaled-output-popout.png`;
    runs `bars-popout-placement-*`.

Three host attempts to open popouts with synthetic cursor moves produced none
(hover-intent is 120 ms; the pointer is moved in 12 ms steps and the capture
waits 1.4 s). Either synthetic motion does not generate the hover events, or
hover popouts do not open on the host; the capture cannot tell. The VM popout
captures show an empty wallpaper behind a 285 px wide panel with truncated copy
(`Power profile: E`), and the amber 6 px notch mark persists when no popout is
open (shell#512). Nothing demonstrates the morph, the notch continuity or the
attached/floating variants on the real compositor.

**Fix direction.** Expose popout ids on the existing IPC target, add a qa step
action `popout.open`, and add the cases to the layouts-gallery scenarios.

**Not verified.** Everything about motion (morph timing, stagger) on any real
compositor; hover vs click behaviour on the host.

### VA-12 (P2)

Defect: Bar end cluster polish: unlabeled `ST` token below the baseline,
glyph-only bottom meters, cramped icon rhythm

- **Surface** — Bars (Cockpit end cluster, bottom strip)
- **Gates** — Visual excellence, Discoverability, Accessibility
- **Issue** — [shell#538](https://github.com/HorneroOS/shell/issues/538)
- **Evidence**
  - Host (maintainer-local): `host/layouts/cockpit-top.png`, `horizon-top.png`,
    `studio-top.png`, `host/04-cockpit.png` (bottom strip).

A two-letter `ST` token follows the status icons in every Cockpit-family strip,
sits about 3 px lower than its neighbours (centre at y 21 vs 18 in a 28 px
strip) and has no hover label in any capture, so a stranger cannot tell what it
is. The bottom strip on the host (`04-cockpit.png`) shows `US`, three glyph-only
percentages (`1%`, `43%`, `64%`) and a thermometer value with no labels (density
`values`), so `43%` is ambiguous between memory and CPU; the horizon strip does
show `CPU MEM DSK TMP`. Icon spacing inside the status cluster is 18 px but the
gap to the tray is 22 px and to the chevron 16 px: three rhythms in 140 px.

**Fix direction.** Audit with the bar debug dump (`qs ipc call debug bars`) for
baseline offsets; make Density choose `labels` by width.

**Not verified.** What `ST` represents in the running build.

### VA-13 (P2)

Defect: Dashboard Performance tab: empty scopes on open, truncated CPU name,
ragged column bottoms

- **Surface** — Dashboard (Performance, Media, Weather)
- **Gates** — Visual excellence, Usability, Completeness
- **Issue** — [shell#539](https://github.com/HorneroOS/shell/issues/539)
- **Evidence**
  - Host (maintainer-local): `host/02-dashboard.png` (Performance tab).
  - `HorneroOS/shell`
    `.github/evidence/dashboard/after-night-offscreen-media.png`,
    `...-weather.png`.

Good: eyebrows with channel numbers, graticule scopes, segment meters, dimension
line under the memory bar are the strongest Signal execution in the product.
Defects: (1) both 60 s scopes open on a graticule with a one-sample stub at the
right edge, so the first minute looks broken (no `COLLECTING` state); (2) the
CPU label truncates to `AMD RYZEN 9 5900X 12-`; (3) the left column ends at y
595 and the right at y 550 so the panel bottom is ragged and `GPU` is taller
than `NETWORK`; (4) the scope trace is thin and low-contrast on the host (spec
asks for a 1.5 px phosphor trace with persistence); (5) the Media tab with no
player draws a full-width empty segment well that reads like a broken seek bar;
(6) Weather with no location is a large empty panel.

**Fix direction.** Add a `samples < window` state to `ScopeTrace`; use `elide:
Text.ElideMiddle`; lay the Performance page with a 2-column Grid with row spans.

**Not verified.** Workspaces and Extensions tabs on host; dashboard at 1366x768.

### VA-14 (P2)

Defect: Lock screen: small authentication card, hairline through the clock,
little WOW for a flagship surface

- **Surface** — Lock
- **Gates** — Visual excellence, Originality, Accessibility
- **Issue** — [shell#540](https://github.com/HorneroOS/shell/issues/540)
- **Evidence**
  - Host (maintainer-local): `host/08-signal-mode.png` (actually the lock
    screen, 1920x1080).
  - `HorneroOS/shell` `.github/evidence/lock/after-night-offscreen-idle.png`,
    `...wrong-password.png`.

The 120 px condensed clock and amber 48 px rule are excellent. The
authentication card is 360x125 px at 1080p with 11 px text (`Num lock is ON.`,
`01 · LOCKED`), so the interactive element is the smallest thing on the screen,
the wrong-password message is roughly 9 px red on graphite (offscreen 1600x900
`wrong-password` frame), and the diagonal hairline from (975,105) to (0,1080)
crosses the leading `1` of the clock. `Num lock is ON.` is a status line that
should appear only when it is OFF. The surface is flat `ground` with two corner
cards: restrained, but for the lock screen, the screenshot most often posted, it
is the least memorable surface.

**Fix direction.** Parametrise the card by `Density` and screen height; move the
hairline behind a clip mask; add an optional `lock.instrument` slot fed by the
deck providers.

**Not verified.** Fingerprint state; multi-monitor lock; lock over the real
wallpaper.

### VA-15 (P2)

Defect: OSD and routine toasts: oversized dual-channel OSD, `Config loaded` and
`Num lock enabled` noise

- **Surface** — OSD, toasts
- **Gates** — Visual excellence, Usability, Performance
- **Issue** — [shell#541](https://github.com/HorneroOS/shell/issues/541)
- **Evidence**
  - `HorneroOS/shell` `.github/evidence/osd/after-night-offscreen.png`
    (300x330), `.github/evidence/toasts/after-night-offscreen.png`.
  - Host (maintainer-local): `host/01-first-boot.png`, `host/04-cockpit.png`
    (toast over the bottom strip).

The volume OSD is a free-floating ~130x230 px slab showing OUT and BRI together
even when only volume changed; BRI reads 0 on a machine without a backlight. The
meter is a dense ribbed column of very small segments, so it reads as a texture
rather than an instrument. On the host two toasts fire at routine events:
`Config loaded in 909ms` (every reload/boot) and `Num lock enabled`; both
overlap bottom-right content and the second stacks over the bottom bar. Toast
severities mix a left stripe (done, warning, note) with a full red border
(error), so error is a different shape not a stronger state.

**Fix direction.** Drive OSD content from the last-changed property; demote
config/numlock notices to the history without a popup; unify `Toast` borders.

**Not verified.** OSD motion timing (enter 90 ms, hold 1200 ms); toast stacking
with 4+ items on host.

### VA-16 (P2)

Defect: Switch control is a two-cell rocker whose off state looks selected

- **Surface** — Control Center and quick settings (every toggle)
- **Gates** — Usability, Accessibility, Consistency
- **Issue** — [shell#542](https://github.com/HorneroOS/shell/issues/542)
- **Evidence**
  - `HorneroOS/shell`
    `.github/evidence/controlcenter-settings-panes/accessibility-night-offscreen.png`
    (zoomed), `controlcenter-daily-panes/audio-night-offscreen.png`,
    `controlcenter-hubs/studio-hub-night-offscreen.png`.

The switch is a 42x25 px two-cell rocker: OFF lights the left cell (raised fill
and a filled rectangle), ON lights the right cell in amber with a thin `I`. A
lit left cell reads as selected/active to anyone not versed in I/O marks; a
filled block is not a recognised `O`; the thin `I` is 1 px wide on the dark
cell. The state is mostly carried by fill, with no text, and the control is
exactly 24 px tall (the WCAG 2.5.8 minimum). Next to it, chip groups (Bars pane
`Speakers`, `Microphone` ...) use amber fill for selected and dark-blue grey for
unselected, a third selection grammar.

**Fix direction.** Redraw `UiToggle`/`SwitchRow` thumb with a clear `O`/`I`
pair; migrate chip groups to `SegmentedControl`.

**Not verified.** Toggle at 1.5x scale; screen-reader announcements.

### VA-17 (P2)

Defect: Layout Picker thumbnails are near-identical wireframes and descriptions
truncate

- **Surface** — Layout Picker, Layout pane
- **Gates** — Discoverability, Visual excellence
- **Issue** — [shell#543](https://github.com/HorneroOS/shell/issues/543)
- **Evidence**
  - `HorneroOS/shell`
    `.github/evidence/controlcenter-hubs/layout-presets-night-offscreen.png`,
    `.github/evidence/layout-picker-mixed-label/`.

Sixteen cards use the same dark wireframe with a thin amber bar moved to a
different edge, so Cockpit, Classic Top, Studio and Productivity are
indistinguishable at a glance, which defeats a picker whose job is comparison.
Descriptions are cut after 28 characters (`After Polybar default +...`, `After
Waybar cozy-min...`), the attribution (an RFC requirement for Hornero
Left/Right) is the first thing truncated, and the evidence still lists `Floating
Island` and `Productivity`, which the language removes (section 14), so the
capture is stale or the data still contains them.

**Fix direction.** Generate thumbnails from the preset JSON (a QML
`PresetThumbnail` that draws the same segments at 1/8 scale).

**Not verified.** Layout Picker at 1366x768; the host picker.

### VA-18 (P2)

Defect: Control Center panes mix generations: sub-page headers, tiny labels and
chip styles differ between panes

- **Surface** — Control Center (Bluetooth, Network, Companion, Dashboard, Bars,
  Windows panes)
- **Gates** — Consistency, Discoverability
- **Issue** — [shell#544](https://github.com/HorneroOS/shell/issues/544)
- **Evidence**
  - `HorneroOS/shell`
    `.github/evidence/controlcenter-network-bt-bars/bluetooth-night-offscreen.png`,
    `wireless-night-offscreen.png`, `companion-night-offscreen.png`,
    `windows-night-offscreen.png`, `taskbar-night-offscreen.png`,
    `controlcenter-daily-panes/audio-night-offscreen.png`.

Audio, Displays, Extensions, Power, Accessibility open with `NN · SECTION`
eyebrow, 28 px title and subtitle. The Bluetooth and Network sub-pages open with
`Bluetooth Settings` / `Network settings` (a tiny glyph, 18 px title, no channel
eyebrow) and a row of four green/blue/amber icon chips at the top left;
Companion uses a 22 px title but 11 px labels and 10 px descriptions in a
3-column density; Bars is a six-panel mosaic with 20+ chips and every row is 11
px. Row heights range from clearly under 32 px (Bars) to ~44 px (Audio); label
sizes from 10 to 13 px. The spec asks for 32 px minimum rows.

**Fix direction.** Enforce `PaneHeader` via the pane registry (shell#460
pattern) and a lint test for pane roots; split Bars into Sections / Status /
Behaviour tabs.

**Not verified.** Day and High Contrast on real windows; all 30 panes at
1366x768.

### VA-19 (P1)

Defect: Greeter login failure message and session default undermine an otherwise
strong first impression

- **Surface** — Greeter (SDDM)
- **Gates** — Accessibility, Usability, Completeness
- **Issue** — [greeter#45](https://github.com/HorneroOS/greeter/issues/45)
- **Evidence**
  - `HorneroOS/greeter` `screens/signal/05-login-failed.jpg`,
    `01-signal-night-golden-hour.jpg`, `06-session-list-open.jpg`,
    `04-high-contrast-large-text.jpg`.

The greeter is the best-realised surface in the set (24 h daypart ribbon,
SEC/ZONE/DAYPART readout wells, hairline corner brackets, stills credited in the
footer). Defects: (1) the failed-login line (`Login failed`) is about 9 px red
on near-black at 1920x1080, below legible even though the field gets an alert
well; (2) every frame preselects `HorneroOS Gaming Session (Experimental)` while
the session list shows it above the other Hyprland sessions, so a default user
would land in the experimental session (test-mode ordering, unverified); (3) the
full-width amber `Login` button is the loudest block on the panel, louder than
the readouts and close to the clock in visual weight. Day fallback uses a sunset
photo with `STILL` chip but no Signal Day palette check.

**Fix direction.** Raise the status line to the `small` step; sort sessions by a
stable priority from `hornero-config`; adjust button state styling.

**Not verified.** Video playback and `LIVE` chip; real SDDM display manager
session on a VM; 4K; multi-user list.

### VA-20 (P1)

Defect: Site and social cards still show the pre-Signal desktop; no real Signal
screenshot above the fold

- **Surface** — Website home, OG/social cards, showroom
- **Gates** — Visual excellence, Originality, Completeness
- **Issue** — [website#233](https://github.com/HorneroOS/website/issues/233)
- **Evidence**
  - `HorneroOS/website` `.github/evidence/signal-homepage/home-night-1920.png`,
    `home-en-day-1280.png`, `home-experience-concepts-1280.png`;
    `public/og/default.png`, `editions.png`, `greeter.png`.

Typography, rhythm and the Signal chrome on the site are excellent (Plex Sans
Condensed headline, telemetry strip, bilingual, three-way theme switch). But the
only desktop picture on the home page and the default OG card is a `btop and
yazi` terminal capture dated 2026-10-25 labelled `PREVIEW · PREVIOUS
APPEARANCE`; there is no Cockpit, no popout, no dashboard and no deck anywhere
in a social card. At 1920x1080 the hero sits in the left 55 % and the right 45 %
is dead hairline space; the product image is below the fold. For a
r/unixporn-grade launch the site must lead with the desktop. OG cards: headline
and body are separated by ~120 px of empty space, the Hornero mark is about 20
px, and `Greeter` is a browser recreation labelled `NOT A SCREENSHOT`.

**Fix direction.** Use a scripted VM scene (qa scenario `showroom/signal-hero`)
to produce the hero and OG assets; regenerate product data from Signal mains
first.

**Not verified.** Live production site; all pages other than home, editions,
download, gaming, install; docs site; search; 404.

### VA-21 (P2)

Defect: Docs site and long-tail pages have no visual evidence

- **Surface** — Docs site, themes, wallpapers, layouts, showroom, extensions,
  companion, terminals, releases, search, 404
- **Gates** — Completeness, Accessibility, Performance
- **Issue** — [website#234](https://github.com/HorneroOS/website/issues/234)
- **Evidence**
  - `HorneroOS/website` `.github/evidence/` contains captures for home,
    editions, download, gaming, install and an older redesign; none for `/docs`,
    `/search`, `/layouts`, `/themes`, `/showroom`, `/companion`, `/terminals`,
    `/releases`.

The docs site is where contributors and unixporn readers land after the hero and
it has not been captured at all in the Signal era. Code blocks, tables, sidebar,
search results, admonitions, and the 16 layout cards are unverified at 360, 768,
1280 and 1920 in both colour modes.

**Fix direction.** Add a Playwright sweep script
(`scripts/capture-evidence.mjs`) that visits the sitemap and writes the set.

**Not verified.** Everything above.

### VA-22 (P2)

Defect: First-party widget copy leaks implementation detail; fixtures and empty
regions in evidence

- **Surface** — Plugin widgets, popovers, catalogue entries
- **Gates** — Visual excellence, Consistency, Usability
- **Issue** — [plugins#71](https://github.com/HorneroOS/plugins/issues/71)
- **Evidence**
  - Mission-local
    `evidence/plugins/batch3-time/hornero-calendar.desktop.night.png`,
    `hornero-quick-notes.dashboard.night.png`,
    `hornero-world-clock.dashboard.day.png`,
    `batch5-widgets/hornero-system-insight.desktop.day.png`,
    `hornero-audio-deck.desktop.night.png`,
    `hornero-weather.dashboard.night.png`.

The widgets share the Signal vocabulary well (channel eyebrows, wells, segment
meters), which is a real achievement. Remaining issues: Calendar says "No
calendar events source is available to extensions yet; this widget shows dates
only."; Quick Notes ends with a 4-line paragraph (`Saved automatically via
Settings; restored when this extension loads again. Disabling flushes any
pending edit ...`); World Clock ends with a DST disclaimer paragraph taller than
the data; Weather leaves 40 % of its card empty; calendar numerals are 22 px
bold while the dashboard calendar uses 14 px; System Insight's CPU trace in the
Day evidence is a sine wave (fixture data) which contradicts the real-data rule
and would mislead anyone using it as a reference; the audio deck evidence shows
`Fixture Artist · Fixture Album` and `Fixture Speakers`.

**Fix direction.** Move limitation notes to manifest `notes` shown in the
catalogue; add a `plugins` CI check that fails when `Fixture` appears in
screenshots' source data; trim paddings via a shared `Card` component.

**Not verified.** Popover/menu surfaces of extensions; marketplace pane with
live catalogue (shows 0 installed in all captures); orientation (rails).

### VA-23 (P2)

Defect: Visual language still specifies 36/30 px bars and 3 px radius examples;
shipped thin bars are 28/24 px with a density factor

- **Surface** — Docs (signal-visual-language.md sections 4, 7, 14; RFC
  amendment)
- **Gates** — Consistency, Completeness
- **Issue** — [docs#124](https://github.com/HorneroOS/docs/issues/124)
- **Evidence**
  - `HorneroOS/shell` `.github/evidence/thin-bars/README.md` and
    `after-cockpit-1080-offscreen.png` (top 28 px, bottom 24 px); `docs`
    `development/signal-visual-language.md` sections 4.1 and 14.1.

Implementation moved to thin bars (shell#517-#520) with `Density.screenHeight`;
the design authority still says 36 px rail and 30 px strip and open item 16
mentions 40/32. Reviewers using the doc as the contract will mis-flag the
shipped bars, and the new numbers (and the sizes at 720/768/960) have no home.

**Fix direction.** Docs-only PR after the visual-quality-audit merges; table of
preset x logical height.

### VA-24 (P1)

Defect: Visual scenarios capture an empty wallpaper at 1280x800; real content,
popouts, resolutions and numbers are missing

- **Surface** — QA VM scenarios and evidence
- **Gates** — Completeness, Performance, Accessibility
- **Issue** — [qa#88](https://github.com/HorneroOS/qa/issues/88)
- **Evidence**
  - Every run under `~/.local/share/hornero/qa/runs/20261117T02*`..`T03*`
    (`layouts-gallery-*`, `wallpapers-ink-*`, `experience-mode-*`): 1280x800, no
    windows, no popout, bars 52/46 px (pre-thin).
  - `docs/evidence/signal-vm-20261117/README.md` lists 14 frames; none shows a
    populated desktop.

The VM gallery judges bars against a blueprint-grid background with one bird,
with no window behind them, so alignment of content and bar, blur/transparency,
window borders and gaps, and the relation between bar and window radius cannot
be assessed. The resolution is one (1280x800) while the spec and thin-bar
evidence ask for 1366x768, 1920x1080, 2560x1440 at 1.25x, 3840x2160 at 2x. Only
one Day capture and no High Contrast. No frame-time or idle-CPU number is
recorded although the visual language (11.4) requires them. Runs before 01:31
are pre-thin-bar images; they are being read as current.

**Fix direction.** Extend scenario schema with `windows:` and `popout:`; reuse
qa#17's stale-evidence alarm.

**Not verified.** N/A (this issue is the coverage plan).

## What was not verified

No real capture exists for the following. Each is a rating gap, not a pass.

- **Motion**: popout morph, stagger, tooltip, launcher, dashboard sweep,
  notification reflow, workspace slide, layout change, lock reveal, reduced
  motion. Nothing animated was captured anywhere.
- **Anchored popouts on the host** (VA-11) and with real windows behind them.
- **Glow, scanlines and persistence** in Signal mode (shell#511, VA-06).
- **Day and High Contrast on real windows** for any surface except the Cockpit
  VM frame; large text and reduced-motion on the host.
- **Scale and resolution**: 1366x768 beyond Cockpit offscreen, 2560x1440 at
  1.25x, 3840x2160 at 2x, ultrawide; fractional scale popouts beyond the 1.5x VM
  frames.
- **Multi-monitor** with different scale and per-output bars on the host (VM
  runs exist for October images only).
- **Experience modes** Focus, Gaming and Studio on the current image: the runs
  exist but were not re-read against the spec after thin bars.
- **Chromatic** (RFC 0002) colours, previews and templates: in flight.
- **Companion chat UI**, voice, approvals.
- **Plugin popovers and context menus**; the Marketplace with a live catalogue.
- **Greeter on a real SDDM display** with video; **installer pages** other than
  the memory gate; **docs site and 8+ website routes**.
- **Wallpaper browser** with the shipped catalogue (only the host's own files
  were seen).
- **Performance**: idle CPU, frame time, input-to-first-frame for any surface.
- **VPN, Input, Keybinds and Capture panes** on real hardware.
- **The 'ST' token** and the bottom-strip glyph meanings on the running build.
- **Offscreen anomalies**: in `thin-bars/after-cockpit-1080-offscreen.png` the
  mark and the active workspace numeral are missing; the VM and host frames show
  both, so this is read as a harness gap, but it is not proven.

The full capture checklist is in the tracking issue.

## Strengths worth stating

Specific things that should survive any refactor: the per-surface channel
numbering (`01 · STATION`), the dimension lines under partitioned meters, the
`NOTE`/`WARNING`/`ERROR` eyebrow system, the daypart ribbon on the greeter, the
condensed lock clock with its amber rule, the sunken readout wells, honest
em-dash empty states, 1 px state edges on notifications and thin Bezel radii.
