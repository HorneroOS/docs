# HorneroOS design language

This guide is the shared starting point for people designing or implementing
a HorneroOS interface, including the provisional installer. It collects the
product-level direction and points to the repository that owns each concrete
rule. It does not replace those implementation contracts or create a second
copy of their changing token values.

## Status and authority

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

The Hornero bird and oven-arch motif form the canonical visual signature. The
desktop's flagship identity uses clay, adobe, cream, and sunset colors. Other
themes may have distinct palettes and moods while retaining clear Hornero
authorship. Cyberpunk and neon are valid creative directions for particular
themes or the website; they are not mandatory OS chrome.

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

- In the desktop, use the theme's semantic roles for surfaces, text, outlines,
  focus, and status. Do not hardcode a dark-only appearance or use wallpaper
  colors as the only source of UI contrast.
- Config owns product theme recipes, the semantic token contract, theme
  catalogues, and wallpaper references. Shell owns live palette presentation
  and runtime appearance behavior. Their boundary and fallback behavior are
  described in [the appearance architecture](../architecture/appearance-system.md).
- For a standalone installer, use canonical brand assets and a restrained
  brand-derived accent, while keeping the installer's surfaces and status
  colors independently readable. Do not copy the website's cyberpunk palette
  wholesale or pretend the installer implements desktop theme switching.
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

The desktop's current reference typefaces are Rubik for interface text,
CaskaydiaCove Nerd Font for technical values, and Material Symbols Rounded
for system icons; those values are implemented in Shell's
[`AppearanceConfig.qml`](https://github.com/HorneroOS/shell/blob/main/config/AppearanceConfig.qml).
Treat them as implementation references, not a requirement to bundle the
same font in every independent tool. A separate component should choose
available, licensed fonts that preserve the same clarity and density.

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
| Shell visual tokens and runtime behavior | [Shell `AppearanceConfig.qml`](https://github.com/HorneroOS/shell/blob/main/config/AppearanceConfig.qml), [`Colours.qml`](https://github.com/HorneroOS/shell/blob/main/services/Colours.qml) | Spacing, typography, rounding, motion defaults, semantic palette presentation |
| Shell interaction and compositor capabilities | [Focus](https://github.com/HorneroOS/shell/blob/main/docs/FOCUS.md), [Interaction](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md), [Compositors](https://github.com/HorneroOS/shell/blob/main/docs/COMPOSITORS.md), [Layouts](https://github.com/HorneroOS/shell/blob/main/docs/LAYOUTS.md) | Keyboard focus, dismissal, compositor-specific feature support, layout intent |
| Login and lock experience | [Greeter UX checklist](https://github.com/HorneroOS/greeter/blob/main/docs/UX_CHECKLIST.md) | Authentication-safe visual hierarchy, keyboard access, offline media and fallback behavior |
| Edition and installable capability truth | [Hornero edition catalogue](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml), [edition architecture](../architecture/editions.md) | Product names, profile composition, maturity and supported choices |
| Installer visuals | [Provisional Calamares branding](https://github.com/HorneroOS/installer/tree/main/image/calamares/branding/hornero) | Current provisional assets and Calamares-specific implementation only; not canonical identity policy |
| Website art direction | [Website styling guide](https://github.com/HorneroOS/website/blob/main/docs/COMPONENTS_AND_STYLING.md) | The website's own editorial composition, web palette, content imagery, accessibility and motion |
| Evidence and visual QA | [QA scenarios](https://github.com/HorneroOS/qa/blob/main/docs/SCENARIOS.md), [QA media policy](https://github.com/HorneroOS/qa/blob/main/docs/MEDIA.md) | Reproducible captures, provenance, and what test evidence can claim |

The website's Southern Signal palette is a web presentation layer. It may
interpret Buenos Aires and Argentine landscapes with night ink, river cyan,
signage magenta, and sodium amber. It does not replace the desktop's semantic
theme system or establish a mandatory installer palette.

## Applying this guide to the provisional installer

The installer should feel like HorneroOS through its mark, naming, language,
color accents, and care with consequential decisions. It remains an
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
