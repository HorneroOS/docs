# Appearance: themes, mode, and color

Start in **Settings → Appearance** when you want a coordinated change. A
theme is the simplest choice: it selects a visual direction and may also
choose a wallpaper, GTK theme, icon theme, and light or dark default. You do
not need to understand color-generation algorithms to pick a look.

## Pick a theme

The shipped catalogue contains three Hornero semantic themes — **Hornero
Dark**, **Hornero Light**, and **Pampa** — plus appearance recipes such as
Catppuccin, Everforest, Gruvbox, Neon City, and Vapor Dreams. Semantic themes
carry curated interface roles; recipes provide a starting look and may use
wallpaper-derived colors. Both are selected from the same theme list.

In Settings, preview a card and select it to apply. If a theme's external GTK
or icon theme is missing, the system cannot create that part of the look; use
the theme details and the [troubleshooting guide](../troubleshooting/README.md)
to check readiness. Hornero does not silently download third-party themes.

From a terminal, inspect before applying:

```sh
horneroctl appearance theme list
horneroctl appearance theme show neon-city
horneroctl appearance theme apply neon-city --dry-run
horneroctl appearance theme apply neon-city --yes
horneroctl appearance theme get
```

Use `apply` for any installed pack. `set` is the verified, atomic switch for
the Hornero semantic themes:

```sh
horneroctl appearance theme set hornero-light --dry-run
horneroctl appearance theme set hornero-light --yes
```

Mutating CLI commands require `--yes`; `--dry-run` shows the proposed action.
After a theme change, `horneroctl appearance doctor` checks whether live
appearance state is coherent.

## Light and dark

A theme supplies a default mode. The current mode can follow that default or
be overridden by the user. GTK's color-scheme preference is a separate
setting: changing it does not switch the shell between light and dark.
Settings indicates when the live mode differs from the theme's default.

For scripted workflows, inspect `horneroctl appearance scheme --help` before
using `set-mode`; use `horneroctl appearance gtk color-scheme` to inspect or
change GTK's policy. Avoid changing the shell mode and GTK policy together
unless that is intentional.

## Wallpaper-derived color

Some appearance recipes use the current wallpaper to generate shell colors.
The active wallpaper, theme, and mode are related, but they are not the same
setting: changing a wallpaper does not rename the theme, and a user mode
override remains independent of the theme default.

To see how a wallpaper will resolve without changing it:

```sh
horneroctl wallpaper current
horneroctl appearance scheme status
horneroctl appearance colors status
```

### Choose how the palette feels

When a recipe follows a wallpaper, Hornero samples its most representative
colors and builds coordinated colors for surfaces, text, and controls. The
variant changes the character of that generated palette; it does not change
the wallpaper or the theme name. Preview a few options against your current
desktop before applying one.

| Variant | What it tends to look like |
| --- | --- |
| Tonal spot | Balanced color with softly tinted surfaces; a good starting point. |
| Vibrant | Stronger, more colorful accents. |
| Expressive | A wider mix of related hues, with more distance from the source color. |
| Fidelity | Keeps the generated roles closer to the source color. |
| Content | Uses the source color's character more directly in key color roles. |
| Neutral | Quieter, less colorful surfaces and accents. |
| Monochrome | Near-grayscale roles with little color emphasis. |

These are generation styles, not seven separate Hornero themes. Light/dark
mode determines which tones are used; the chosen variant determines how the
source colors are arranged into a palette. The names are available for
scripts and diagnostics:

```sh
horneroctl appearance accent show
horneroctl appearance scheme list
```

Saved palettes let you keep a generated color result while trying a different
wallpaper or variant. They are reusable color choices, not another theme pack.
For the underlying Material Color Utilities scheme model, see the
[upstream color scheme guide](https://github.com/material-foundation/material-color-utilities/blob/main/dev_guide/creating_color_scheme.md).

## Theme packs and wallpaper availability

Theme metadata and validation rules live in
[HorneroOS/config](https://github.com/HorneroOS/config/tree/main/profiles/themes).
The catalogue is generated from those packs. Wallpaper files are separate
media: packs may name an expected image without bundling that image in the
package. If the image is not present locally, choose another available
wallpaper or use a path on your own machine. Theme selection remains
available and the Shell explains when referenced media is missing.

The architecture guide explains the boundaries between semantic tokens,
wallpaper analysis, shell colors, GTK, icons, and Qt:
[Appearance system](../architecture/appearance-system.md). For everyday
wallpaper selection, see [Wallpapers and color](wallpapers.md). For the
application-specific behavior of GTK, Qt, Kitty, and CopyQ, see
[Apps and workflows](../applications/README.md).
