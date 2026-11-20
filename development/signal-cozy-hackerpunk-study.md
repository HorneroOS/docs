# Signal: Cozy Hackerpunk study

<!-- markdownlint-disable MD013 -->

- **Status** — Accepted direction (2026-11-17) for
  [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md), amendment 4
- **Tracking** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)
  (requirements L1, L2, K4)
- **Audience** — shell, PluginKit, config, website, brand and QA contributors

Direction in one line: **Cozy Hackerpunk, Argentine retrofuturism, personal
computing.** Signal Bezel stays the structure; it gets a warm lamp, lived-in
detail and a sharper typographic voice. This is an evolution of
[Signal Visual Language](signal-visual-language.md), not a restart.

> **Every image here is an original concept render** (HTML/CSS specimens
> rendered headlessly at 1920×1080, sources in
> `assets/signal-cozy-hackerpunk/sources/`), labelled "CONCEPT RENDER", with
> sample values and no live telemetry. No third-party artwork was downloaded,
> traced or reused.

## 1. Evidence, and its limits

The creative reference is the Argentine animated series *Electro Andes*
(Bellolandia Studio). Studied for **principles only**.

What the public sources actually say:

- The studio page describes a family-oriented 2D fantasy series set in
  "Arcadia Iruyana", a future of technology, environmental collapse and Andean
  heritage ([Bellolandia](https://www.bellolandia.com/work/electro-andes)).
  It gives synopsis and credits, **not** palette, lighting or type.
- Press frames it as "a cyberpunk ethno mythological action adventure horror
  story" ([80.lv](https://80.lv/articles/electro-andes-cyberpunk-ethno-mythological-horror-animated-show)),
  with a look compared to *Cyberpunk: Edgerunners* and a hip-hop / neon feel
  ([Cultura Geek](https://culturageek.com.ar/electro-andes-como-sera-el-anime-argentino-con-estetica-cyberpunk-que-promete-romperla-toda/)).
- The setting is inspired by Iruya (Salta) and the Peruvian mining town La
  Rinconada; the director compares the approach to a fictional version of a
  culture "without making a literal representation"; references include a
  "trashy future" and neon; the soundtrack is northern *electro-folklore*;
  Kiwi, the hacker, is called "the most likable character"
  ([421.news](https://www.421.news/en/electro-andes-animated-series/)).

I did not inspect the artwork itself, and no source describes its colour or
lighting. Where this study talks about warmth, lamps and lived-in gear, that is
**the product owner's brief (2026-11-17)** and our own judgement, not a claim
about the series. The transferable principles that the evidence does support:

1. **Ground the future in a real place.** Technology is read through a
   specific region, not a generic city. For us: Buenos Aires broadcast and
   industrial graphic culture, regional Argentine palettes, Spanish microcopy
   in voseo.
2. **Stylise, never transcribe.** A culture is borrowed as a fictional
   version, not copied literally. For us: no folklore or Andean motifs
   lifted into UI; our own symbols only.
3. **Likeable hackers.** Technical people are warm and approachable. For us: a
   desktop that greets you, with instruments you can read.
4. **Sound and image share one culture** (electro-folklore). For us: sound
   themes and palettes are authored as a pair later (not in this slice).
5. **Cyberpunk without sterility.** "Trashy future" implies wear and
   improvisation: handwritten labels, mismatched lamps, taped notes.

## 2. What we must not copy

- Kiwi's design, likeness, silhouettes, outfits, props, colour scripts, logo
  or any frame, and any compositions of the series.
- Series names and places as branding (Arcadia Iruyana, Black Mountain),
  Andean sacred imagery (Killa/Inti figures, gestures), engraved motifs.
- Edgerunners-style neon-on-black as our default.
- Anything downloaded from the studio or press. Our mascot is Javi el Hornero
  (an original hornero bird character); his states are specified in
  requirement L8, not here.

## 3. Delta versus current Signal

| Axis       | Signal (RFC 0001 + amendments)    | Cozy Hackerpunk                                                       |
| ---------- | --------------------------------- | --------------------------------------------------------------------- |
| Mood       | Precise instrument faceplate      | Same precision, in a lit room: someone works here                      |
| Neutrals   | Cool graphite (Night), paper (Day) | Add a warm charcoal-aubergine night (Dusk); keep Night/Day/Contrast   |
| Light      | Amber is *live*; glow budgeted    | Plus a lamp wash and soft inner top light (atmosphere), tiny alphas    |
| Texture    | None (flat, hairline)             | Optional fine grain and vignette, off in High Contrast and for a11y   |
| Labels     | Mono eyebrows                     | Adds engraved "plate" labels, paper-note microcopy accents            |
| Voice      | Neutral                           | Warm, rioplatense, short; a plain voice remains one switch away       |
| Colour use | amber / cyan / green              | Adds occasional rose/violet as a *rare* accent (terminal 5, tags)     |

## 4. Three coherent directions compared

*Concept render removed (2026-11-20): Concept render: three directions. Real captures: [Showroom](https://horneroos.com/showroom/).*

| Criterion                          | A Bezel Cálido | B Taller | C Noche Norteña |
| ---------------------------------- | -------------- | -------- | --------------- |
| Fits Signal, extends instead of replaces | 5        | 3        | 1               |
| All-day comfort                    | 5              | 3        | 2               |
| Distinct from generic cyberpunk    | 4              | 4        | 2               |
| GlowBudget and perf cost           | 5              | 3        | 1               |
| Works with wallpaper-derived palettes | 5           | 3        | 3               |
| Day / High Contrast variants       | 5              | 3        | 2               |
| Charm on first sight               | 4              | 5        | 4               |

- **A. Bezel Cálido (lamp on the bench)** — Signal Bezel unchanged in
  structure; warm neutrals, a lamp wash, soft inner light, grain, cream ink,
  copper-amber signal. Light is an instrument signal, never ambient glow.
- **B. Taller (ham-radio workshop)** — painted olive sheet metal, paper
  labels, screws, double bezels. Charming, but skeuomorphic texture per
  surface, heavy for long sessions and fights wallpaper-derived palettes.
- **C. Noche Norteña (electro-folk neon)** — saturated violet/magenta/cyan
  with glow as language. Closest to the generic neon look the brief rejects
  and incompatible with the glow budget.

**Chosen: A, borrowing from B and C** what is cheap: from B, the cream paper
note and the engraved plate label (typography, not texture); from C, a rare
rose/violet accent for tags, terminal magenta and special moments, never a
default surface colour.

## 5. The chosen direction

*Concept render removed (2026-11-20): Concept render: Signal Dusk desktop. Real captures: [Showroom](https://horneroos.com/showroom/).*

### 5.1 Emotional atmosphere

Late evening at the workbench: a desk lamp on one side, a cyan glow from the
monitor on the other, instruments that tell the truth quietly, a note taped to
the bezel saying hello. Warm but exact; charming but not childish. Kawaii is
carried by the mascot and a few soft touches, never by the structure.

### 5.2 Colour (art direction, not a new system)

- Same RFC §3.1 roles and the same contrast gates (`contrast-gates.json`).
  **No new schema roles** are added: warmth is delivered by (a) a new curated
  palette and (b) atmosphere values derived from whichever palette is active
  (shell `services/atmosphere.js` derives lamp and blush chips from the
  palette, so custom and Chromatic palettes warm up too).
- **Signal Dusk** (`hornero-signal-dusk`, config): charcoal-aubergine
  surfaces `#14100F → #3B312E`, cream ink `#F1E6D2`, copper-amber signal
  `#F29A4A`, cyan cue `#74C6E8`, phosphor `#93D79B`, rose in the terminal.
  Passes the shared gates (weakest text pair 4.98:1). Night, Day and High
  Contrast are unchanged.
- Chromatic still derives palettes from wallpapers (RFC 0002); warm bias is a
  Chromatic policy item for the palettes owner, not a fork.

*Concept render removed (2026-11-20): Concept render: Dusk palette, contrast and type roles. Real captures: [Showroom](https://horneroos.com/showroom/).*

Measured on Dusk: `ink` ≥ 10.2:1 and `inkMuted` ≥ 6.2:1 on every surface,
`signal` ≥ 5.7:1, `ruleStrong` ≥ 3.3:1 on `lifted`. `alert` is 4.36:1 on
`lifted` (the gate checks it on sunken to raised): do not put alert text on
tooltips.

### 5.3 Typography as a premium asset

Plex stays, because it is OFL-1.1, packaged in Arch (`ttf-ibm-plex`) and has
the weights, a condensed cut and true tabular figures. Alternatives with an
open licence (Space Grotesk, JetBrains Mono, Big Shoulders) were weighed and
rejected: each adds a second superfamily to ship and test for a marginal gain.
Roles:

| Role     | Face                              | Use                                       |
| -------- | --------------------------------- | ----------------------------------------- |
| UI       | IBM Plex Sans 13                  | Everyday text                             |
| Readout  | IBM Plex Mono, `tnum`             | Numbers, code, timers                     |
| Eyebrow  | IBM Plex Mono 11, caps, +8 %      | Section and channel labels (exists)       |
| Plate    | IBM Plex Sans Condensed SemiBold, caps, +14 % | Engraved mode and status plates (new) |
| Display  | IBM Plex Sans Condensed Light, −2 % tracking | Clock, lock, greeter             |

Rules: at most four treatments per screen, tabular figures wherever a value
changes, display sizes a hair tighter, plates only on enums (mode, state),
never on sentences.

### 5.4 Material and light

- Surfaces stay flat, hairline-ruled, small radius (RFC: no giant pills).
  The existing "Cozy" look scales rounding to 1.6; recommend capping the
  effective radius at `small × 2` on bars and cards so soft does not become
  pill (see §8).
- Warm light = three small alphas (lamp wash, soft inner top highlight,
  vignette) plus optional grain, all with hard ceilings and user sliders.
- Indicators: one small LED per live thing, real data only. Glow stays inside
  the RFC §3.2 budget (≤ 3 glowing items, blur ≤ 4 px, alpha ≤ 40 %), off in
  Day, High Contrast, Gaming and on Cockpit Clear.

### 5.5 Motion

Unchanged choreography (RFC §3.6, visual language §11). Additions: mode
changes fade the lamp over 400–600 ms; nothing loops except real activity;
**reduced motion** swaps every fade for an instant state and disables grain
shimmer (grain is static anyway); **low power** drops grain, vignette and
glow first.

### 5.6 Accessibility and performance constraints

- Text contrast gates unchanged; atmosphere layers sit under text and may not
  reduce measured text contrast (vignette ceiling 0.30, lamp 0.20).
- Grain and vignette are single textures or one gradient, not shaders; off in
  High Contrast; user-disableable (AGENT-RULES §6).
- Microcopy never carries information that a tooltip or label does not.
- Rose/violet is never the only carrier of meaning.

## 6. Plugin customisation opportunities

- Plugins read the atmosphere through the same tokens (lamp, soft light,
  grain) so widgets match the room; they may not set their own glow outside
  the budget (shell#600 already routes plugin glows through intensity).
- A **Look pack** manifest (palette + atmosphere + font scale + mascot skin +
  microcopy voice) installable as one extension, previewable before applying.
- Instrument widgets (clock plate, VU, scope) declare `tabular` readouts and
  the plate style through typed settings.
- Sound themes paired with Look packs (later).

## 7. Website storytelling

Lead with the room, not the feature list: a warm hero (the Dusk desktop in a
real capture once available), the line "Pasá, sentate.", then the instrument
story (real data, nothing faked), then customisation as "arrange your own
workbench". Released / experimental / planned labels stay. Use original
renders marked CONCEPT until host captures exist. Fonts self-hosted (Plex),
no third-party requests, images with explicit sizes, dark and light.

## 8. Decisions and open items

- Implemented now: `hornero-signal-dusk` in config; this study;
  RFC 0001 amendment 4; specimens. The shell atmosphere layer (lamp, soft
  light, vignette, grain, Look presets, microcopy) is already in a separate
  shell branch (`feat/cozy-atmosphere`) and is intentionally not duplicated
  here.
- Recommended retunes for that layer: cap the "Cozy" look rounding (§5.4);
  disable grain and vignette automatically in High Contrast and low power;
  add the Plate label style (§5.3) as a small `Plate` component with a
  tracking control.
- Not decided here: Javi states (L8), lock/greeter/installer art direction,
  Chromatic warm-bias policy, sound pairing.
