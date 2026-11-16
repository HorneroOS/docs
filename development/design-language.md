# HorneroOS design language

This guide is the shared starting point for people designing or implementing
a HorneroOS interface, including the provisional installer. It collects the
product-level direction and points to the repository that owns each concrete
rule. It does not replace those implementation contracts or create a second
copy of their changing token values.

## Status and authority

The concrete design system is [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md).
It defines the token roles, flagship palettes, typography, glyphs, motion,
anchored-surface contract and the Cockpit default. Where this guide and the
RFC disagree, the RFC wins.

HorneroOS is a product family in development. The design direction below is
the cross-component policy; the linked repositories remain authoritative for
their assets, tokens, interaction details, and tested capabilities. When this
guide and an implementation disagree, report the mismatch and verify the
current product before changing either one. Do not infer maturity from a
mockup, a package, or an experimental configuration.

For installer contributors, use this guide for product identity and
interaction principles, then use the Config brand files for official assets
and the edition catalogue for the options the installer may offer. The
current Calamares branding is provisional implementation detail, not a
separate brand source of truth.

## Product character

HorneroOS is an independent, carefully composed Arch-based operating-system
family. Its interfaces should feel considered, capable, warm, and direct.
Argentine identity belongs in the Hornero mark, the project's origins, and
real places and visual references; it should not depend on flags, clichés, or
an obligatory neon treatment.

The Hornero bird and oven-arch motif form the canonical visual signature.
The design language is **Hornero Signal**: a contemporary engineering
workstation from an alternate 1990s Argentina — broadcast control rooms,
oscilloscope bezels, test cards and technical drawing sheets — executed with
modern restraint. Chrome is quiet and matte; amber `signal` marks what is
live or primary and celeste `cue` marks focus and information. Regional
themes may have distinct palettes and moods, but every theme fills the same
Signal roles. It is not Material Design, not glass, and not generic neon.
The [Hornero Signal overview](../desktop/hornero-signal.md) explains it for
users; the [Signal Visual Language](signal-visual-language.md) spec gives
the concrete rules for bars, meters, panels and motion.

The interface should prioritize the task in front of the user. Ornament,
motion, transparency, and imagery must not reduce legibility, keyboard access,
system feedback, or confidence around consequential actions.

## Design rules

### 1. Use the shared Hornero identity

- Use the canonical logo, wordmark, app icon, and small-size favicon from
  [Config's brand assets](https://github.com/HorneroOS/config/tree/main/assets/brand).
- Follow [Config's brand direction](https://github.com/HorneroOS/config/blob/main/docs/BRAND.md)
  for mark variants, color intent, and placement. Do not redraw the bird or
  introduce a competing mascot or product mark.
- Keep the Hornero identity visible but subordinate to the user's current
  task. Installer screens should identify the product without turning every
  step into a promotional panel.

### 2. Compose from semantic appearance roles

- In the desktop, use the Signal roles (`ground` … `lifted` surfaces,
  `ink` tiers, `rule`/`ruleStrong`, `signal`, `cue`, `phosphor`, `alert`) for
  surfaces, text, outlines, focus and status. Do not hardcode hex values or a
  dark-only appearance, and never derive UI colours from the wallpaper.
- Config owns theme packs, the schema-v2 token contract, theme catalogues,
  and wallpaper references. Shell owns live palette presentation
  and runtime appearance behavior. Their boundary and fallback behavior are
  described in [the appearance architecture](../architecture/appearance-system.md).
- For a standalone installer or the greeter, map to the Signal Night and
  Signal Day role values and use canonical brand assets. Do not pretend the
  installer implements desktop theme switching.
- Preserve contrast for text, controls, focus indicators, warnings, and
  destructive steps in every supported mode. See Config's
  [theme token schema](https://github.com/HorneroOS/config/blob/main/profiles/themes/tokens.schema.json)
  and contrast checks before adding product theme tokens.

### 3. Keep hierarchy and language clear

- Make the current screen, next action, and recovery path easy to identify.
- Use plain labels for user tasks. Keep implementation names such as IPC
  verbs, package identifiers, and compositor dispatch strings out of primary
  user-facing copy unless the user must act on them.
- Explain consequences before formatting disks, replacing boot entries,
  changing partitions, or performing another hard-to-reverse action. Show a
  review step with the chosen target and edition before execution.
- Distinguish required choices from optional customization. Use progressive
  disclosure instead of crowding the first-run path with every advanced
  setting.
- Use the same product and edition names as the
  [edition catalogue](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml).
  Do not offer a backend, capability, or installation claim that the current
  catalogue and release status do not support.

### 4. Make interaction predictable and accessible

- Every essential action must work with a keyboard and have a visible focus
  state. Focus order follows the visual and task order; moving between steps
  must not strand focus.
- Use consistent Escape and Back behavior. Do not silently discard entered
  values or hide the only route to recover from an error.
- Give controls explicit names, state, and helpful validation messages. Never
  communicate meaning through color alone.
- Respect system text scaling and contrast settings where the framework
  allows. Use readable defaults, comfortable hit targets, and sufficient
  contrast; avoid relying on transparency over variable imagery for critical
  text.
- Motion is brief feedback, not a prerequisite for understanding. Avoid
  animated backgrounds and nonessential transitions in installation flows;
  honor reduced-motion preferences when supported.
- Follow the Shell's tested
  [focus contract](https://github.com/HorneroOS/shell/blob/main/docs/FOCUS.md)
  and [interaction contract](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md)
  when implementing Shell surfaces. These details do not automatically define
  the installer toolkit's behavior.

### 5. Be honest about system capabilities

- HorneroOS Desktop is Wayland-first. Hyprland and Niri have different
  support maturity; the system is not synonymous with either compositor.
- Show only installation choices that can be installed and validated. Label
  preview or experimental paths at the choice itself, not only in a footer.
- Degrade gracefully when optional devices, networks, portals, or services
  are unavailable. Explain the condition and provide a safe next step.
- Use real, reviewed product captures for product claims. Mark concept art,
  browser recreations, and provisional installer screens clearly.

## Type, icons, and imagery

Hornero Signal uses three IBM Plex families (Arch `ttf-ibm-plex`, OFL-1.1):
IBM Plex Sans for interface text, IBM Plex Mono for readouts, numerals,
eyebrows and code, and IBM Plex Sans Condensed for the clock, lock screen and
large headings. Numbers use tabular figures. Shell icons are Hornero Glyphs,
a curated Tabler Icons (MIT) subset used through `Glyph { name: "wifi" }`;
Material Symbols are not used anywhere. The roles and scale are defined in
RFC 0001 §3.3–3.4 and implemented in Shell's
[`AppearanceConfig.qml`](https://github.com/HorneroOS/shell/blob/main/config/AppearanceConfig.qml).
Independent tools that cannot load Plex should pick an available, licensed
face with similar clarity and density.

Use icons with a consistent, recognizable meaning; pair unfamiliar or
high-impact icons with text. Prefer genuine app icons for applications.
Photographs and wallpapers should be authentic, credited, and licensed for
their distribution context. Use the Config wallpaper manifest and credits as
the authority for shipped desktop wallpaper; do not copy website preview
files into a package as a shortcut.

## Composition and density

Prefer clear alignment, a small number of meaningful groups, and enough space
to separate unrelated tasks. A dense information view is appropriate when it
helps comparison or review; it should not make the primary action hard to
find. Use borders, elevation, and rounded corners to communicate grouping or
interaction, not as decoration on every element.

In the installer, keep the step navigation stable, the main content focused,
and the primary action in a predictable location. The product banner and
slideshow are supporting context; installation state, validation, target
selection, and recovery instructions take visual priority.

## Where the rules live

| Concern | Authoritative source | What it governs |
| --- | --- | --- |
| Product identity and logo | [Config `docs/BRAND.md`](https://github.com/HorneroOS/config/blob/main/docs/BRAND.md), [`assets/brand/`](https://github.com/HorneroOS/config/tree/main/assets/brand) | Hornero mark, logo variants, wordmark, app symbols, brand direction |
| Desktop themes and wallpaper | [Config appearance architecture](../architecture/appearance-system.md), [theme profiles](https://github.com/HorneroOS/config/tree/main/profiles/themes), [wallpaper policy](https://github.com/HorneroOS/config/blob/main/docs/WALLPAPERS.md) | Semantic theme packs, wallpaper selection, credits and application boundary |
| Design system | [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md), [Signal Visual Language](signal-visual-language.md) | Roles, palettes, type, glyphs, motion, anchored surfaces, per-layout art direction |
| Shell visual tokens and runtime behavior | [Shell `AppearanceConfig.qml`](https://github.com/HorneroOS/shell/blob/main/config/AppearanceConfig.qml), [`Signal.qml`](https://github.com/HorneroOS/shell/blob/main/services/Signal.qml), [`NATIVE-APPEARANCE.md`](https://github.com/HorneroOS/shell/blob/main/docs/NATIVE-APPEARANCE.md) | Spacing, typography, rounding, motion, `Signal.palette` roles |
| Shell interaction and compositor capabilities | [Focus](https://github.com/HorneroOS/shell/blob/main/docs/FOCUS.md), [Interaction](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md), [Compositors](https://github.com/HorneroOS/shell/blob/main/docs/COMPOSITORS.md), [Layouts](https://github.com/HorneroOS/shell/blob/main/docs/LAYOUTS.md) | Keyboard focus, dismissal, compositor-specific feature support, layout intent |
| Login and lock experience | [Greeter UX checklist](https://github.com/HorneroOS/greeter/blob/main/docs/UX_CHECKLIST.md) | Authentication-safe visual hierarchy, keyboard access, offline media and fallback behavior |
| Edition and installable capability truth | [Hornero edition catalogue](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml), [edition architecture](../architecture/editions.md) | Product names, profile composition, maturity and supported choices |
| Installer visuals | [Provisional Calamares branding](https://github.com/HorneroOS/installer/tree/main/image/calamares/branding/hornero) | Current provisional assets and Calamares-specific implementation only; not canonical identity policy |
| Website art direction | [Website styling guide](https://github.com/HorneroOS/website/blob/main/docs/COMPONENTS_AND_STYLING.md) | The website's own editorial composition, web palette, content imagery, accessibility and motion |
| Evidence and visual QA | [QA scenarios](https://github.com/HorneroOS/qa/blob/main/docs/SCENARIOS.md), [QA media policy](https://github.com/HorneroOS/qa/blob/main/docs/MEDIA.md) | Reproducible captures, provenance, and what test evidence can claim |

The website uses the same Hornero Signal roles and IBM Plex families as the
desktop, adapted for editorial layout. It does not define a separate palette
for the desktop or the installer.

## Applying this guide to the provisional installer

The installer should feel like HorneroOS through its mark, naming, language,
Signal colours and type, and care with consequential decisions. It remains an
installation utility, not a miniature desktop shell. A visitor should be
able to tell what edition is being installed, where it will go, what will
change, and whether a choice is experimental before confirming it.

Keep Calamares-specific work localized to its branding and module
configuration. Prefer a small adapter from the shared edition catalogue over
duplicating package or capability truth in installer UI. When a choice cannot
yet be performed or tested, label it as unavailable or provisional instead
of presenting it as complete. The provisional installer is a reference and
integration surface for the future custom installer; its current colors,
screenshots, and layout do not overrule this guide.

Before treating an installer design as ready, validate a complete install
flow in a disposable UEFI and BIOS environment, including both keyboard use
and failure/recovery paths. A branding preview or Calamares configuration
parse alone does not certify installation safety.

## Proposing a design change

1. Identify the owning repository from the table above.
2. Describe the user need, the relevant task, and any capability or maturity
   boundary the design depends on.
3. Reuse the canonical identity assets and the owning component's tokens.
   If a new shared rule or token is needed, update its source of truth and
   generator/schema/tests in the same change.
4. Include real screenshots or reproducible evidence for changes to visible
   product behavior. State which compositor, theme, viewport, and release
   revision the evidence represents.
5. Check keyboard operation, contrast, reduced motion, narrow layouts, and
   failure states. Do not claim a test that was not run.
6. Update this map only when repository ownership, product-level principles,
   or source links change. Keep detailed implementation rules beside the
   implementation.
