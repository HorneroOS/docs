# RFC 0002 — Hornero Chromatic

- **Status** — Accepted (2026-11-17)
- **Implementation** — Not started. Nothing in this RFC is implemented or
  validated yet; see [Rollout](#16-rollout-and-migration).
- **Amends** — [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md):
  supersedes in part §1 (the exclusion of wallpaper synthesis), the "removed
  with no replacement" list in §3.1 (variants, "follow wallpaper") and the
  "wallpapers never recolour the UI" clause of §9. Everything else in
  RFC 0001 stands: role names, curated palettes, typography, glyphs, motion,
  anchored surfaces, Cockpit.
- **Scope** — Shell (engine, preview, Control Center, PluginKit), horneroctl
  (apply, state, rollback, outputs), config (schema, gates, templates),
  plugins (extension templates), website (presentation once shipped)
- **Tracking** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)
  (mission), [docs#122](https://github.com/HorneroOS/docs/issues/122) (this
  RFC), [shell#525](https://github.com/HorneroOS/shell/issues/525) (engine),
  [shell#526](https://github.com/HorneroOS/shell/issues/526) (shell UI and
  PluginKit), [hornero#428](https://github.com/HorneroOS/hornero/issues/428)
  (horneroctl), [config#140](https://github.com/HorneroOS/config/issues/140)
  (schema, gates, templates),
  [plugins#70](https://github.com/HorneroOS/plugins/issues/70) (extensions),
  [website#232](https://github.com/HorneroOS/website/issues/232) (website)

## 1. Problem

RFC 0001 removed the Material 3 machinery the shell inherited from
Caelestia. That was right for the design language and wrong for one
capability users valued: a desktop whose colours come from the wallpaper,
with variants that change its character. Removing Material Design must not
mean losing dynamic colour.

Hornero Chromatic restores that capability as a first-party engine that
produces **Signal roles directly** — the RFC 0001 §3.1 role set, the
optional `glow` and the 16 terminal colours. It is an **option**. The
curated Signal Night, Signal Day and Signal High Contrast themes stay the
factory default and the fallback for every failure. Colour algorithms and
visual design are separate: Chromatic changes hue and chroma inside the
Signal structure; it does not change anatomy, type, glyphs, motion or
surfaces.

Non-negotiable constraints:

- No Material roles, no Material widgets or symbols, no compatibility layer,
  and no wrapping of an external Material colour library under new names.
- No Caelestia visual components. Caelestia is credited for the feature
  lineage; no Caelestia code is copied.
- Cockpit Clear bars stay at zero opacity. Chromatic may change their
  foreground ink, never add a backdrop, tint, scrim or blur.
- One owner per concern: horneroctl applies and writes state; config owns
  the theme schema, the gate table and the shipped templates; the shell owns
  presentation (`Signal`) and the interactive preview.
- A wallpaper must never make the interface unreadable.

## 2. What existed before, and what we keep

### 2.1 Caelestia (shell and cli)

Studied at `caelestia-dots/shell` and `caelestia-dots/cli` `main` (GPL-3.0):

- **Seed extraction** — Caelestia: Python: 128-colour Celebi quantiser on a 128
  px nearest-neighbour thumbnail, Material "score" (chroma 48 target,
  hue-proportion weighting), dislike fix; Assessment: Proven idea; RGB/HCT,
  nearest-neighbour thumbnail aliases; one seed only
- **Palette** — Caelestia: The external Material colour library's scheme classes
  (tonal spot, vibrant, expressive, fidelity, content, fruit salad, rainbow,
  neutral, monochrome); Assessment: Rich variants, but the output is Material
  roles
- **Flavours** — Caelestia: `default` / `hard` (hard darkens surfaces);
  Assessment: Useful "surface depth" knob
- **Smart inference** — Caelestia: Mode: 1×1 Lanczos average tone > 60 → light.
  Variant: Hasler–Süsstrunk colourfulness < 10 neutral, < 20 content, else tonal
  spot; Assessment: Cheap; the single-pixel mean is fooled by split images
- **Terminal / named colours** — Caelestia: Fixed Gruvbox and Catppuccin tables
  rotated toward the seed hue; Assessment: Good idea; no contrast check
- **Contrast** — Caelestia: Whatever the Material scheme yields; Assessment: No
  gate, no protection over translucent surfaces
- **Video / GIF** — Caelestia: `ffmpeg` first frame; GIF frame 0; Assessment:
  First frames are often black fades
- **Preview** — Caelestia: Shell spawns the Python CLI per preview (`wallpaper
  -p`), parses JSON, swaps a preview palette; Assessment: Correct model
  (in-memory preview), high latency
- **Apply** — Caelestia: One Python process writes scheme state, Hyprland, GTK,
  Qt, terminals (OSC to every `/dev/pts`), many app templates, user templates
  (`{{ $role }}`), then an arbitrary `postHook` shell command; Assessment: Broad
  coverage; writes terminals of other users' sessions it can open; shell hooks
  are unsafe
- **Caching** — Caelestia: Per image hash: thumbnail, score, smart options,
  scheme per variant/flavour/mode; Assessment: Good
- **Shell analyser** — Caelestia: C++ `ImageAnalyser` (dominant colour,
  luminance) used for transparency compensation; Assessment: Good native seed
  for our work

### 2.2 HorneroOS before Signal

Before shell#475, hornero#421 and config#128:

- The shell's `ThemePipeline.qml` chained several processes per change
  (`sh -c` pointer write, M3 generation through horneroctl, state sync,
  Hyprland regeneration, `hyprctl reload`, hyprlock, notifications). The
  native `ImageAnalyser` (in `plugin/src/Hornero`, still present) only fed a
  luminance hint (`WallpaperAnalysis.qml`).
- horneroctl `smartcolor.v` and `run_m3_synthesis` resolved a Python
  interpreter that had the external Material library installed and ran
  config's `generate-m3-colors.py` (scheme type, harmonised success and
  terminal colours, a terminal contrast check from `terminal_themes.py`).
  `appearance doctor` failed when no such Python existed.
- Outputs were Material role names, so every downstream generator carried a
  Material vocabulary.

### 2.3 Lost, weak, and better

- **Capability** — Kept from the lineage: Wallpaper seeds, variants, surface
  depth, smart mode/variant, terminal harmonisation, preview-before-apply, app
  templates, caching; Weak, not repeated: Python + external library dependency;
  Material roles; process chains; first-frame-only video; single-pixel mode
  inference; `postHook` shell commands; OSC writes to every pty; Chromatic does
  better: Native engine used in-process for previews and by a helper for apply;
  Signal roles produced directly; perceptual (OKLab) statistics; multi-seed;
  contrast solved by construction and re-validated before write; minimum surface
  opacity over the wallpaper; deterministic golden output; transactional apply
  with rollback

## 3. Architecture decision

### 3.1 Decision

**One engine, written once in C++, in the shell repository.**

- `libs/chromatic/` — a static library, C++20, depending only on Qt6 Core
  and Gui (`QImage`, `QImageReader`, `QColorSpace`). It owns decoding,
  analysis, inference, synthesis and the contrast solver.
- `plugin/src/Hornero/Chromatic/` — the QML module `Hornero.Chromatic`,
  linking the library, for instant in-process previews.
- `extras/chromatic/` — the `hornero-chromatic` helper, installed at
  `/usr/lib/hornero/hornero-chromatic`, linking the same library. horneroctl
  calls it for every generation that is going to be applied.
- **horneroctl** stays the only writer of the live scheme
  (`${XDG_STATE_HOME}/hornero/signal/scheme.json`), the downstream app
  outputs, the Chromatic state and the history used for rollback.
- **config** owns the schema extensions, the gate table and the shipped
  templates. **The shell** owns `Signal` presentation, the preview and the
  Control Center UI.

Video wallpapers are analysed from a single frame extracted once by
`ffmpeg` (optional dependency). Without `ffmpeg`, a video source reports
`chromatic.source-unreadable` and the current palette stays.

### 3.2 Alternatives considered

- **Engine in V inside horneroctl** — V has no first-class decoders for WebP,
  AVIF, JPEG XL, ICC profiles or animated frames; the shell would still need a
  second, native or JavaScript, implementation for 60 fps slider previews. Two
  implementations drift.
- **Engine in QML/JavaScript** — Too slow for 4K decode and clustering on the
  GUI thread; no use outside the shell.
- **Engine in Python (config)** — Reintroduces the dependency RFC 0001 removed;
  startup cost on every apply.
- **Link the engine into horneroctl through a C ABI** — Pulls Qt into
  `horneroctl-bin`; image decoders would run inside the process that owns state.
  A short-lived helper isolates crashes in decoders fed with untrusted files.
- **Shell computes, horneroctl just stores the shell's palette** — Breaks
  scripted and login-time use without a running shell, and makes the shell a
  second writer.
- **A separate `HorneroOS/chromatic` repository** — Clean versioning but a new
  package and release pipeline during a release freeze. The helper ships in
  `hornero-shell`, which already installs `/usr/lib/hornero` binaries.
  Extraction stays possible because the library has no QML dependency.

### 3.3 Consequences

- Preview and apply use the same decoder and the same library build, so a
  previewed palette and the applied one are byte-identical (§13); the
  result carries a `fingerprint` that the shell compares after apply.
- horneroctl works without the shell package for curated themes; Chromatic
  is unavailable (`chromatic.engine-missing`) when the helper is absent.
- Zero Python in the runtime path. New runtime dependencies: none.
  `ffmpeg` becomes an optional dependency of `hornero-shell`. Optional
  `qt6-imageformats` / `kimageformats` widen the decodable formats; they are
  not required.

## 4. Colour science

All arithmetic is IEEE double precision without fast-math. Colours are
analysed in **OKLab / OKLCH** (Björn Ottosson, 2020) and output as sRGB
`#RRGGBB`. Contrast uses WCAG 2.x relative luminance, exactly as config's
`signal_theme.py`; terminal separation uses CIE76 ΔE on CIELAB D65, also as
config does, so the engine and every validator agree.

### 4.1 Decode

1. Open with `QImageReader`; refuse sources above 100 megapixels or with
   unreadable headers (`source-unreadable`).
2. Use scaled decoding where the format supports it (JPEG) to a longest side
   of 512 px; otherwise decode and downscale.
3. Convert to sRGB through the embedded colour profile
   (`QImage::convertToColorSpace`), so Display P3 and Adobe RGB photos are
   read correctly.
4. Animated GIF/WebP/APNG: sample `n = min(8, frameCount)` frames at
   indices `floor(i × frameCount / n)` for `i = 0 … n−1`; pixels from every
   sampled frame are pooled with equal frame weight. The choice depends only
   on the file, never on elapsed time. A file whose frame count is unknown
   uses frame 0 only; a sampled frame that fails to decode fails the source
   (`source-unreadable`) rather than being skipped.
5. Video (`.mp4 .mkv .webm .mov .avi`): one frame at 1 s (or at 0 when the
   video is shorter), scaled to 512 px, extracted by one `ffmpeg` call into
   the cache (§15). Never more than once per file identity; never while the
   video plays.
6. Downscale to a longest side of **256 px** with a box filter in **linear
   light**. Pixels with alpha < 0.5 are ignored; premultiplied input is
   un-premultiplied first.

### 4.2 Statistics

Over the 256 px working image, area-weighted, with the top and bottom 8 %
bands (where bars live) weighted 2×:

- Lightness: mean `L̄`, `Lmin`, `Lmax`, percentiles `L5`, `L50`, `L95`,
  standard deviation.
- Chroma: mean, `C90`, `C95`; colourfulness `Cf = C90`.
- Hue histogram: 36 bins weighted by chroma; hue entropy (bits).
- Detail: mean absolute Laplacian of L (busy-ness).
- Band statistics for the top and bottom bands (mean L, deviation).
- A 96 × 54 luminance grid (mean and deviation per cell), cached for the
  Cockpit Clear sampler (signal-visual-language §12.5). Adoption by ClearInk
  is a follow-up, not a requirement of this RFC.

### 4.3 Quantisation

Deterministic, no randomness:

1. Build a histogram of the working pixels on a 5-bit-per-channel sRGB grid
   (≤ 32 768 bins), each bin storing population and mean OKLab.
2. Initialise 16 clusters by **median cut in OKLab** (split the box with the
   largest population-weighted variance along its longest axis; ties broken
   by axis order L, a, b).
3. Run 8 iterations of population-weighted Lloyd k-means in OKLab, in bin
   order. Drop empty clusters; merge clusters closer than ΔEOK 0.02.

Result: up to 16 clusters `{oklab, population share}`.

### 4.4 Seed scoring

For each cluster with OKLCH `(L, C, h)` and share `s`:

```text
score = 0.70 * sqrt(s) * 10
      + 0.30 * min(C, 0.20) / 0.20 * 10
      + 0.10 * hueNeighbourhood(h)          # share of chroma mass within ±15°
      - 4.0  if C < 0.02                    # near-neutral
      - 2.0  if L < 0.15 or L > 0.95        # crushed or blown out
      - 1.5  if 90° <= h <= 115° and L < 0.60 and C > 0.04   # muddy olive
```

- **Primary seed**: highest score with `s >= 0.005` (a small saturated
  object on a grey field still wins).
- **Secondary seed**: highest-scoring cluster whose hue differs from the
  primary by at least 50°.
- **Neutral hue**: the hue of the largest cluster with `C >= 0.01`, else the
  primary hue. Surfaces take this hue in the `faithful` variant.
- **Achromatic images** (`C90 < 0.025`): if the chroma-weighted mean hue of
  pixels with `C > 0.005` exists it becomes the seed hue with chroma 0.06;
  otherwise the **Signal house hues** are used (signal 69°, cue 236°) and
  `inference.reasons` says so.

Up to five ranked seeds are reported so the user can pick another one.

### 4.5 The Signal structure is fixed

The curated palettes are a lightness ladder with a split temperature: Signal
Night pairs cool graphite surfaces (hue ≈ 256°) with warm ink (≈ 85°);
Signal Day pairs warm paper (≈ 87°) with cool ink (≈ 252°). Chromatic keeps
the **ladder** (elevation, ink tiers, rule strength) and the **split
temperature**, and takes only **hue and chroma** from the image. The
reference model of these rules reproduces Signal Night from an amber seed
within a mean CIE76 ΔE of 3.3.

OKLCH lightness targets (before the solver):

| Role | Dark | Light |
| --- | --- | --- |
| `ground` | 0.167 | 0.910 |
| `sunken` | 0.189 | 0.877 |
| `base` | 0.203 | 0.950 |
| `panel` | 0.229 | 0.968 |
| `raised` | 0.263 | 0.983 |
| `lifted` | 0.305 | 0.995 |
| `rule` | 0.318 | 0.847 |
| `ruleStrong` | 0.575 | 0.537 |
| `ink` | 0.926 | 0.234 |
| `inkMuted` | 0.739 | 0.443 |
| `inkFaint` | 0.573 | 0.597 |
| `signal` / `cue` | 0.78 / 0.78 | 0.49 / 0.47 |
| `phosphor` / `alert` | 0.80 / 0.70 | 0.47 / 0.50 |
| `*Well` | 0.29 | 0.915 |
| `on*Well` | 0.91 | 0.28 |
| `on*` (on accent fills) | 0.18 | 0.995 |

`surfaceDepth: deep` (Caelestia's "hard" flavour, renamed) lowers the dark
surface ladder by 0.03 and raises the light one by 0.015 (capped at 1.0).

### 4.6 Role synthesis

With primary hue `hp`, chroma `cp`, secondary hue `hs` (optional), neutral
hue `hn` and the variant parameters of §6:

- **Surfaces** (`ground` … `lifted`, `rule`, `ruleStrong`): hue `hn`,
  chroma `sC × k` with `k` = 0.75, 0.85, 1.0, 1.1, 1.25, 1.3, 1.3, 1.4.
- **Ink tiers**: hue `hn + 180°`, chroma `iC` (`ink`) and `iC / 2`
  (`inkMuted`, `inkFaint`).
- **Status anchors** keep their meaning on every wallpaper: `alert` hue 29°
  and `phosphor` hue 150°, each rotated toward `hp` by a quarter of the hue
  difference, capped at the variant's `harm` (≤ 20°).
- **`signal`**: hue `hp`, chroma `clamp(cp × 1.15, aCmin, aCmax)` limited
  to the sRGB gamut at its lightness (`faithful`: `cp` unscaled).
- **`cue`**: the first candidate whose hue is ≥ 35° from both status
  anchors and ≥ 60° from `signal`, in order: `hs`, `hp + r`, `hp − r`,
  `hp + 180°`, the house cue 236° rotated ≤ 15° toward `hp`, `hp ± 120°`
  (`r` is the variant rotation). If none qualifies, the candidate farthest
  from the anchors.
- **Separation**: `signal` and `cue` are rotated to stay ≥ 30° from `alert`
  and `phosphor` (in `faithful`, `alert` moves instead, inside 10°–45°), so
  "live" never reads as "error" and "focus" never reads as "healthy".
- **Wells**: accent hue, chroma `min(C × 0.32, 0.055)`; **on-wells**: chroma
  `min(C × 0.5, 0.085)`; **on-fills**: accent hue, chroma 0.03 (dark) or
  neutral white (light).
- `inverse` = `ink`, `onInverse` = `panel`, `inverseSignal` = signal hue at
  0.49 (dark) / 0.776 (light). `focus` = `cue`. `scrim` and `shadow` stay
  `#000000`.
- **`glow`**: dark modes only (and never `monochrome`, `high-contrast`):
  signal hue, lightness `signal + 0.05`, chroma `signal × 1.1` in gamut.
  Light schemes omit it (it falls back to `signal`, and the glow budget
  already disables glow in day themes).
- **Gamut mapping**: keep L and h, reduce chroma by bisection (24 steps)
  until the colour is inside sRGB.

### 4.7 Contrast solver

Surfaces never move. Foregrounds move only in lightness, away from their
backgrounds, by bisection (30 steps) until every gated pair reaches its
minimum plus a **0.15 margin**:

1. `ink`, `inkMuted`, `signal`, `cue`, `phosphor`, `alert` on `sunken`,
   `base`, `panel`, `raised`.
2. `ruleStrong` on `base`, `panel`, `lifted` and the text surfaces; `focus`
   on every surface (stricter than config, which gates `focus` on `base`);
   `inkFaint` 3:1 on `base` and `panel`. `inkFaint` is decorative and never
   carries essential text (RFC 0001 §3.1), so it is not a text role at any
   level; the 3:1 floor keeps decorative marks visible.
3. Every `on*` on its fill; `onInverse` and `inverseSignal` on `inverse`.
4. Terminal: normals (1–6) 4.5:1 and brights (9–14) 3:1 on `base`; red,
   green and yellow separable (ΔE ≥ 10); each normal → bright step ΔE ≥ 6.

If a target is unreachable at the end of the range, chroma drops to 0 and
the colour goes to the extreme lightness, which always passes on the
ladder's surfaces. The minima come from config's gate table (§9.3) and the
contrast level (§5.3). The solver order is fixed, so output is
deterministic.

The reference model of §4.5–§4.7 was run over 360 seed hues × 5 chromas ×
2 secondary choices × 8 variants × 2 modes (11 520 palettes); every one
passed config's `signal_theme.py validate`. This was a scratch reference
model, not the shipped engine; the engine's own property test replaces it
(§15).

### 4.8 Terminal ANSI 16

- 1 red = `alert` hue, 2 green = `phosphor` hue; 3 yellow 85°, 4 blue 255°,
  5 magenta 325°, 6 cyan 190°, each rotated toward `hp` by at most the
  variant's `term` cap.
- Normals at L 0.77 (dark) / 0.48 (light); brights at 0.87 / 0.39 with
  0.85× the chroma; chroma 0.14 (0.09 `muted`, 0.06 `monochrome`; never
  below what the separation gate needs).
- 0 = surface hue at L 0.26 / 0.23; 7 and 15 = ink hue; 8 = surface hue at
  L 0.54 / 0.44.
- The solver step 4 then applies.

### 4.9 Over the wallpaper

Two outputs protect readability where the wallpaper shows through:

- **`minSurfaceAlpha`**: for each translucent surface role, the smallest
  opacity at which `ink` and `inkMuted` still pass their gate when the
  surface is composited over the wallpaper's darkest and lightest pixels
  (`Lmin`, `Lmax` of the working image, §4.2), so no patch of the wallpaper
  can lower contrast below the bound.
  `Signal` uses `max(user opacity, minSurfaceAlpha)`.
- **`clearInk`**: the Cockpit Clear foreground sets for both polarities
  (`ink`, `inkMuted`, `signal`, `alert`, `halo`) re-hued from the scheme and
  solved to 4.5:1 against the opposite polarity's halo. ClearInk keeps
  choosing polarity per region (signal-visual-language §12.1). This changes
  **foregrounds only**; a clear bar never gets a fill, tint, scrim or blur.

## 5. Smart inference

Every inferred value is a default the user can override; the result lists
`reasons` (human-readable) and a `confidence` in 0–1.

### 5.1 Mode

`L̄` is the band-weighted mean lightness (§4.2):

- `L̄ < 0.58` → dark; `L̄ > 0.68` → light.
- Between the two, keep the current mode (hysteresis, so a rotating
  wallpaper folder does not flip the desktop), or dark when there is none.
- If the top and bottom bands disagree with the whole image by more than
  0.25, the bands decide (the shell's surfaces sit there).

### 5.2 Variant

Automatic choice is limited to `balanced`, `vibrant`, `expressive` and
`muted`:

| Condition | Variant |
| --- | --- |
| `C90 < 0.025` | `muted` (house hues when the image has no hue) |
| `C90 < 0.06` | `balanced` |
| `C90 < 0.12` and two seeds ≥ 50° apart, each ≥ 10 % share | `expressive` |
| `C90 < 0.12` | `balanced` |
| `C90 >= 0.12` | `vibrant` |

`neon` is **suggested** (never auto-applied) when `L̄ < 0.30` and `C95 >
0.18` at `L > 0.6`. `faithful`, `monochrome` and `high-contrast` are never
suggested automatically.

### 5.3 Contrast level

`standard` (config gates), `boosted` and `maximum` (§11). Automatic: when
transparency is enabled and detail (§4.2) exceeds 0.08, recommend `boosted`;
the recommendation is shown, not applied, unless the user set contrast to
`auto`.

### 5.4 Personality

A short label for the UI built from the inference (for example "Dark ·
balanced · warm amber · calm"), plus chroma class (`grey`, `soft`, `rich`,
`intense`) and temperature (`warm` for seed hues 20°–110°, `cool` for
180°–300°, otherwise `neutral`).

## 6. Variants

Variants are parameter sets for §4.6–§4.8. `sC` surface chroma, `iC` ink
chroma, `aC` accent chroma range, `r` cue rotation, `harm`/`term` hue caps.

- `balanced` (default) — Lineage: tonal spot; `sC`: 0.016; `iC`: 0.014; `aC`:
  0.09–0.15; `r`: 165°; `harm` / `term`: 10° / 10°; Behaviour: Signal Night/Day
  character re-hued; quiet surfaces, one confident accent
- `vibrant` — Lineage: vibrant; `sC`: 0.028; `iC`: 0.014; `aC`: 0.14–gamut; `r`:
  165°; `harm` / `term`: 12° / 15°; Behaviour: Stronger accents and tinted
  chrome
- `expressive` — Lineage: expressive, fruit salad, rainbow; `sC`: 0.022; `iC`:
  0.016; `aC`: 0.11–0.17; `r`: 120°; `harm` / `term`: 20° / 20°; Behaviour:
  Triadic cue unless the image has a second hue; more harmonised status colours
- `faithful` — Lineage: fidelity, content; `sC`: 0.020; `iC`: 0.012; `aC`: seed
  chroma; `r`: 165°; `harm` / `term`: 8° / 8°; Behaviour: `signal` is the seed
  itself when it passes the gates; surfaces take the image's dominant hue
- `muted` — Lineage: neutral; `sC`: 0.008; `iC`: 0.008; `aC`: 0.05–0.08; `r`:
  165°; `harm` / `term`: 5° / 5°; Behaviour: Near-neutral chrome, soft accents
- `monochrome` — Lineage: monochrome; `sC`: 0; `iC`: 0; `aC`: 0.035; `r`: 165°;
  `harm` / `term`: 0 / 0; Behaviour: Neutral chrome and ink; accents whisper the
  seed hue; status colours keep their meaning; no `glow`
- `high-contrast` — `sC`: 0.006; `iC`: 0; `aC`: 0.12–0.17; `r`: 165°; `harm` /
  `term`: 5° / 5°; Behaviour: `maximum` gates, deeper ground, brighter ink; no
  `glow`; no translucency
- `neon` — `sC`: 0.030; `iC`: 0.020; `aC`: 0.16–gamut; `r`: 180°; `harm` /
  `term`: 0 / 0; Behaviour: Dark only (a light request returns dark with a
  reason); complementary cue, saturated terminal, `glow` at gamut; glow budget
  unchanged

Orthogonal knobs: `surfaceDepth` (`standard` / `deep`), `chroma` scale
(0.5–1.5, multiplies `sC`, `iC` and `aC`), `hueShift` (−180° to 180°,
applied to the seeds).

Fixed rules for every variant: the glow budget (RFC 0001 amendment 2), no
glow on Cockpit Clear bars, motion and anatomy untouched.

## 7. Sources

- `wallpaper` (default) — The current wallpaper pointer, per monitor 0
- `image:<path>` — Any image or video file
- `seed` — One or two manual colours (`#RRGGBB`); first → `signal`, second →
  `cue`
- `house` — Signal house hues; only the surface tint follows the wallpaper
  (`balanced` "Signal tinted")

Manual colours in `faithful` are kept exactly when they pass; otherwise the
result lists `adjustments` such as `signal #F2E200 → #C9BB00 (contrast on
panel)`.

## 8. Live scheme and theme extensions

All additions are optional and additive; schema version stays 2 and
existing readers ignore them.

### 8.1 Live scheme (`scheme.json`)

```json
{
  "schemaVersion": 2,
  "id": "hornero-chromatic",
  "mode": "dark",
  "palette": { "ground": "#0F1114", "…": "#……" },
  "terminal": ["#……", "… 16 colours"],
  "chromatic": {
    "version": 1,
    "engine": "1.0.0",
    "algorithm": 1,
    "fingerprint": "sha256:…",
    "request": {
      "source": "wallpaper",
      "variant": "balanced",
      "mode": "auto",
      "contrast": "standard",
      "surfaceDepth": "standard",
      "chroma": 1.0,
      "hueShift": 0
    },
    "resolved": { "mode": "dark", "variant": "balanced", "contrast": "standard" },
    "seeds": ["#D98A3A", "#3A7FD9"],
    "sourceKey": "sha256:…"
  },
  "minSurfaceAlpha": { "base": 0.82, "panel": 0.86 },
  "clearInk": {
    "light": {
      "ink": "#……", "inkMuted": "#……", "signal": "#……",
      "alert": "#……", "halo": "#……"
    },
    "dark": {
      "ink": "#……", "inkMuted": "#……", "signal": "#……",
      "alert": "#……", "halo": "#……"
    }
  }
}
```

`hornero-chromatic` is a reserved theme id with no catalogue directory.
Curated themes keep writing the document without the three optional blocks.

### 8.2 Theme files (`theme.json`)

A saved Chromatic palette is an ordinary schema-v2 theme in
`${XDG_DATA_HOME}/hornero/themes/<id>/theme.json` with `collection: "user"`
and an optional `chromatic` provenance object (`engine`, `algorithm`,
`request`, `seeds`, `createdAt`). It is listed, applied, exported and
validated like any catalogue theme. config's `tokens.schema.json` gains the
`chromatic` property and the `user` collection; a new
`scheme.schema.json` describes §8.1.

### 8.3 Preferences (`shell.json`)

User preferences live in `appearance.chromatic` (shell-owned schema, shipped
in `shell.default.json`, resynced into config):

```json
{
  "appearance": {
    "theme": "hornero-signal-night",
    "chromatic": {
      "source": "wallpaper",
      "seeds": [],
      "variant": "auto",
      "mode": "auto",
      "contrast": "standard",
      "surfaceDepth": "standard",
      "chroma": 1.0,
      "hueShift": 0,
      "follow": "auto",
      "perMode": {
        "dark": { "variant": "auto" },
        "light": { "variant": "auto" }
      },
      "fallback": {
        "dark": "hornero-signal-night",
        "light": "hornero-signal-day"
      },
      "transition": "smooth"
    }
  }
}
```

Chromatic is active only when `appearance.theme` is `hornero-chromatic`.
`follow` is `off`, `auto` (recolour when the wallpaper changes) or `ask`
(preview with a timed Apply / Keep current toast). The shell edits these
preferences; horneroctl reads them. A horneroctl `apply` always selects
Chromatic (it sets `appearance.theme` to `hornero-chromatic`); by default it
also stores its request in `appearance.chromatic`, and `--no-persist`
skips only that second write, so a one-off CLI request does not replace the
saved preferences.

## 9. Ownership

### 9.1 Files

- `$XDG_STATE_HOME/hornero/signal/scheme.json` — Owner: horneroctl; Writer:
  horneroctl (the shell still writes it for its built-ins, as today)
- `$XDG_STATE_HOME/hornero/chromatic/state.json` — Owner: horneroctl; Writer:
  horneroctl: last applied request, fingerprint, timestamps
- `$XDG_STATE_HOME/hornero/chromatic/history/NNNN.json` — Owner: horneroctl;
  Writer: horneroctl: ring of 10 snapshots for rollback
- `$XDG_CACHE_HOME/hornero/chromatic/` — Owner: engine; Writer: helper and shell
  plugin: analysis, frames, palettes (disposable)
- `$XDG_CONFIG_HOME/hornero/chromatic/templates.d/*.json` — Owner: user; Writer:
  user templates (§12.2)
- `/usr/share/hornero/chromatic/templates/` — Owner: config; Writer: shipped
  first-party templates
- `profiles/themes/contrast-gates.json` — Owner: config; Writer: gate table
  (§9.3)
- `shell.json` `appearance.chromatic` — Owner: shell; Writer: shell UI;
  horneroctl on `--persist`

### 9.2 Flow

```text
Control Center ──in-process──▶ Hornero.Chromatic (preview, no writes)
      │ Apply
      ▼
[horneroctl] appearance chromatic apply ──▶ hornero-chromatic generate (JSON)
      │ validate with the gate table ─ fail → write nothing, exit 1
      │ lock → snapshot (scheme, outputs, shell.json appearance keys)
      │ render scheme, outputs and shell.json to temp files
      │ rename scheme.json, outputs, then shell.json
      │ any failure → restore every renamed file from the snapshot
      ▼
Signal (FileView) adopts the scheme with a transition; apps reload natively
```

### 9.3 Gate table

`profiles/themes/contrast-gates.json` in config is the single source of the
contrast pairs and minima per level (`standard`, `boosted`, `maximum`),
including the terminal and separation rules. config's validator reads it;
the engine and horneroctl compile in a vendored copy, and each repository
has a sync test against the vendored file (the same pattern as
`shell.default.json`).

## 10. horneroctl contract

All verbs live under horneroctl `appearance chromatic`. Every verb accepts
`--json`; writing verbs accept `--dry-run` (writes nothing, prints the plan)
and require `--yes` when not interactive.

- `status` — Active or not, preferences, last applied request and fingerprint,
  helper and `ffmpeg` availability
- `analyze [--source …]` — Analysis and inference only
- `preview [request]` — Generate and validate without writing; prints the scheme
  and gate report
- `apply [request] [--no-persist]` — Generate, validate, snapshot, write scheme
  and outputs, select `hornero-chromatic` in `shell.json`; `--no-persist`
  leaves `appearance.chromatic` unchanged
- `follow` — Re-apply from the current wallpaper when Chromatic is active and
  `follow` is `auto`; otherwise a successful no-op reporting `skipped`
- `rollback [--steps N]` — Restore an earlier snapshot (curated or Chromatic)
  through the same write path
- `history` — List snapshots
- `save --id ID --name NAME` — Save the current (or requested) Chromatic scheme
  as a user theme
- `export [--output FILE]` — Write the current scheme as a schema-v2 theme file
- `import FILE` — Validate and install a theme file as a user theme
- `variants` — Variants with descriptions and parameters
- `off` — Leave Chromatic: apply the per-mode fallback theme
- `doctor` — Helper, `ffmpeg`, image formats, cache and state health
- `templates list` / `render` / `check` — Inspect, render and validate templates

Request flags: `--source wallpaper|image:PATH|seed|house`, `--seed HEX`
(repeatable, up to 2), `--variant NAME|auto`, `--mode auto|dark|light`,
`--contrast auto|standard|boosted|maximum`, `--depth standard|deep`,
`--chroma F`, `--hue-shift DEG`. Unspecified flags come from
`appearance.chromatic`.

Exit codes follow horneroctl: `0` success, `1` failure, `2` usage. Failures
carry a stable `error.code`: `chromatic.engine-missing`,
`chromatic.source-unreadable`, `chromatic.gates-failed`,
`chromatic.locked`, `chromatic.write-failed`, `chromatic.state-corrupt`,
`chromatic.template-invalid`.

Rules:

- `wallpaper set` (and the shell after a wallpaper change, debounced
  1.5 s) runs `follow`.
- A corrupt `state.json` or history entry is moved aside to `*.corrupt` and
  reported; the live scheme is never left partial.
- The apply lock is `$XDG_RUNTIME_DIR/hornero/appearance.lock`; a second
  apply fails fast with `chromatic.locked`.

### 10.1 Helper contract

`hornero-chromatic` is an internal helper (not on `PATH`); its interface is
versioned by `schemaVersion` in its output.

- `analyze --source PATH [--frames N]` — `{schemaVersion, engine, source,
  analysis, inference}`
- `generate (--source PATH | --seed HEX…) [request flags] [--current-mode M]` —
  `{schemaVersion, engine, request, analysis, inference, scheme, gates,
  adjustments, fingerprint}`
- `validate --scheme FILE [--level L]` — `{schemaVersion, passed, rows}`
- `variants` — `{schemaVersion, variants}`
- `version` — `{schemaVersion, engine, algorithm, qt, formats, ffmpeg}`

Common flags: `--cache-dir DIR` (default `$XDG_CACHE_HOME/hornero/chromatic`),
`--no-cache`. Exit codes: `0` ok, `2` usage, `3` source unreadable or
unsupported, `4` gates unreachable (a bug; reported, never written), `5`
internal error.

## 11. Accessibility

- Gate levels: **standard** = config's gates; **boosted** = `ink` 7:1,
  `inkMuted` 5.5:1, `ruleStrong` and `focus` 4.5:1; **maximum** = every
  text role and on-pair 7:1, boundaries 4.5:1.
- `focus` reaches 3:1 (standard) on **every** surface, not only `base`.
- Status meaning never depends on hue alone (RFC 0001 rules stand), and
  status hues are anchored (§4.6).
- The `appearance.highContrast` switch is **protected**: it always shows the
  curated `hornero-signal-contrast` table and disables translucency,
  whatever Chromatic produces. The `high-contrast` variant is a separate,
  optional look.
- Translucent surfaces honour `minSurfaceAlpha` (§4.9).
- Reduced motion disables palette transitions.
- horneroctl re-validates before writing; a palette that fails is never
  applied.

## 12. Theming outputs

### 12.1 Adapters

horneroctl renders every output from roles, for curated and Chromatic
schemes alike:

- **Hornero Shell and PluginKit** — Live scheme (`Signal`, `Theme.palette`)
- **Hyprland, hyprlock** — Existing horneroctl renderers
- **alacritty, ghostty, btop, cava** — Existing horneroctl renderers
- **kitty** — Template → `kitty/hornero-chromatic.conf`, include swap, reload
  through kitty's own config-reload signal
- **GTK 3 / GTK 4 (libadwaita)** — Templates → `@define-color` overrides and
  `gtk-4.0/gtk.css` recolour; GTK theme tree chosen by mode
- **Qt (qt5ct / qt6ct)** — Template → `qt6ct/colors/hornero-chromatic.conf`,
  existing qt6ct line edit
- **foot, fuzzel, neovim (`nvim` + `nvim-colorscheme`), helix, delta, zed** —
  Shipped templates (config; 23 first-party manifests including
  `:colorscheme hornero-chromatic` for Neovim, Helix themes, and
  `git-delta`)
- **User and extension apps** — Templates (§12.2)

New adapters for dynamic output are config-owned **templates** rendered by
horneroctl's template engine, so formats stay in config and no new
hand-written renderer is added to horneroctl.

### 12.2 Template mechanism

A template is a text file with placeholders; a manifest says where it goes.

```json
{
  "name": "waybar",
  "template": "waybar.css.tmpl",
  "output": "~/.config/waybar/hornero.css"
}
```

- Placeholders: `{{ ink }}` (`#RRGGBB`), `{{ ink.hex }}`, `{{ ink.bare }}`
  (no `#`), `{{ ink.rgb }}` (`r, g, b`), `{{ ink.rgba 0.8 }}`,
  `{{ ink.r }}` / `.g` / `.b`, `{{ term3 }}`, `{{ mode }}`, `{{ id }}`.
- Sections: `{{#dark}}…{{/dark}}`, `{{#light}}…{{/light}}`. Nothing else: no
  loops, no expressions, no includes, no command execution.
- Unknown placeholders fail the render; the output is not written.
- Outputs must resolve under `$XDG_CONFIG_HOME`, `$XDG_CACHE_HOME` or
  `$XDG_DATA_HOME` after symlink resolution; written atomically, mode 0644.
- No hooks. Reloads exist only in first-party adapters.
- Extensions declare `theme.templates` in manifest v3; their outputs go to
  `$XDG_CACHE_HOME/hornero/themes/ext/<extension-id>/` only, rendered by
  horneroctl, never by the extension.

## 13. Shell and PluginKit API

### 13.1 `Hornero.Chromatic` (QML module)

- `ChromaticEngine` (singleton): `available`, `engineVersion`,
  `analyse(source) → ChromaticJob`, `generate(request) → ChromaticJob`,
  `contrast(a, b) → real`, `ensureContrast(fg, bg, min) → color`.
- `ChromaticRequest` (value object): `source`, `seeds`, `variant`, `mode`,
  `contrast`, `surfaceDepth`, `chroma`, `hueShift`, `currentMode`.
- `ChromaticJob`: `running`, `cancel()`, signals `finished(result)` and
  `failed(code, message)`. A cancelled job never emits.
- `ChromaticResult`: `scheme` (JS object in §8.1 shape), `analysis`,
  `inference`, `gates`, `adjustments`, `fingerprint`.

Work runs on a thread pool; analysis results are cached in memory (LRU, 8
sources) and on disk (§15). A slider change re-synthesises from the
cached analysis.

### 13.2 `Signal`

- `beginPreview(scheme)`, `commitPreview()`, `cancelPreview()`,
  `previewing`. Preview changes the in-memory palette only. Cancel restores
  the previous palette; nothing is written.
- Transitions: palette changes interpolate in OKLab over at most 240 ms in
  at most 12 steps, one notification per step; instant under reduced
  motion, gaming mode, high contrast or `transition: "instant"`.
- `chromatic` (read-only): `active`, `variant`, `mode`, `seeds`,
  `fingerprint`; `minSurfaceAlpha` and `clearInk` are consumed internally.

### 13.3 Control Center

An Appearance → Chromatic section: source picker (wallpaper, image, colour,
Signal house), ranked seed chips, variant gallery, mode, contrast, surface
depth, chroma and hue sliders, per-mode preferences, follow policy, and a
specimen board (bar strip, popout, notification, launcher row, buttons,
terminal swatch, GTK button swatch, gate report). Actions: Apply, Cancel,
Save as theme, Export, Import, Rollback. Built from the existing Bezel
control kit; no new visual components.

### 13.4 PluginKit

`Theme.palette` already follows the live scheme. Additions:
`Theme.chromatic` (read-only status, no wallpaper path), `Theme.revision`
(increments on every palette change, for canvases), `Theme.contrast(a, b)`
and `Theme.ensureContrast(fg, bg, min)` for data-driven colours. Extensions
cannot run the engine on arbitrary images in this version.

## 14. Performance budgets

Measured on the CI runner by `chromatic-bench`; CI fails at 3× budget.

| Operation | Budget |
| --- | --- |
| Decode + analyse 4K JPEG | ≤ 60 ms |
| Decode + analyse 4K PNG | ≤ 150 ms |
| Synthesis + solver from cached analysis | ≤ 2 ms |
| Helper end-to-end on a cache hit | ≤ 20 ms |
| `apply` on a cache hit, excluding GTK and Hyprland reloads | ≤ 150 ms |
| Palette transition step (offscreen, full shell) | ≤ 2 ms binding work |
| Helper peak memory, 4K / 8K source | ≤ 96 MB / ≤ 220 MB |
| Idle cost | Zero: no timers, no watchers beyond the existing scheme watcher |

Never: continuous video analysis, analysis at shell startup (the shell
reads the last scheme), regeneration when the request and source identity
are unchanged.

## 15. Determinism, caching and tests

- **Determinism**: identical source bytes and request produce byte-identical
  JSON from the same build, across runs and thread counts. Cross-architecture
  results may differ by at most ΔEOK 0.005 per role (checked in CI when a
  second architecture is available).
- **Cache keys**: `sourceKey = sha256(content digest, algorithm)`, where the
  content digest is the SHA-256 of the file bytes (files above 64 MiB, in
  practice videos: of the size plus the first and last 4 MiB). Path, size
  and mtime are only a fast index to a stored digest and are never trusted
  alone; a changed file with the same size and mtime is detected because a
  hit re-hashes the file before reuse. Palette key =
  `sha256(analysis digest, canonical request, algorithm)`. Entries carry
  their own digest; a mismatch or parse failure deletes the entry and
  recomputes. Size cap 64 MB, LRU pruning on write.
  The cache is never required: `--no-cache` gives the same result.
- **Corpus**: generated by the test harness, no binary blobs — black, white,
  mid grey, noise, 50/50 complementary split, 0.3 % saturated dot on grey,
  neon on black, pastel high key, sepia, skin-dominant, muddy olive, hue
  gradient, red-dominant (alert collision), green-dominant (phosphor
  collision), half-transparent PNG, 16-bit PNG, CMYK JPEG, Display P3 JPEG,
  animated GIF with differing frames, 1×1, 16384×1 strip, truncated file,
  empty file, and a generated video when `ffmpeg` exists — plus the credited
  catalogue wallpapers from config.
- **Golden files**: `tests/chromatic/golden/<case>__<variant>__<mode>.json`;
  any change bumps `algorithm` and is reviewed.
- **Property tests**: corpus × 8 variants × 2 modes × 3 contrast levels ×
  64 deterministic manual seeds → every gate passes, separation holds, and
  config's `signal_theme.py validate` accepts every scheme.
- **horneroctl**: dispatch tests with a fake helper, fault injection on each
  rename (state restored), lock contention, corrupt state and cache,
  dry-run writes nothing, rollback round trips.
- **Shell**: preview and cancel write nothing (isolated XDG tree), reduced
  motion disables transitions, Cockpit Clear bar pixels equal the wallpaper
  pixels, `minSurfaceAlpha` honoured.
- **QA VM**: an apply scenario over four wallpaper classes (dark, bright,
  detailed, grey) with captures; no host claims without host evidence.

## 16. Rollout and migration

1. RFC (this document) and tracking issues.
2. Engine library, helper and golden corpus (shell#525).
3. horneroctl verbs, config schema, gate table and templates (hornero#428,
   config#140).
4. Shell preview, transitions, Control Center, PluginKit (shell#526), then
   extension templates (plugins#70).
5. QA-VM evidence; website copy only after release (website#232).

Migration: none required. Existing selections keep their theme ids and
keep working; Chromatic is off until a user picks it. Curated Signal
Night / Day / High Contrast stay the factory default. Selections migrated by
RFC 0001 are not turned back into dynamic colour automatically; Welcome and
Control Center offer Chromatic as an option.

## 17. Attribution

- The feature lineage — wallpaper seeds, variants, flavours, smart mode and
  variant, app templates — comes from
  [Caelestia](https://github.com/caelestia-dots) (GPL-3.0). Chromatic is a
  new implementation: no Caelestia code or tables are copied. The shell's
  `NOTICE` and `docs/PROVENANCE.md` keep their Caelestia attribution and
  record this lineage.
- OKLab and OKLCH: Björn Ottosson, "A perceptual color space for image
  processing" (2020); the published conversion matrices are used.
- WCAG 2.x relative luminance and contrast ratio (W3C).
- Median cut (Heckbert, 1982) and Lloyd's k-means are textbook algorithms.
