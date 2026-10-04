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

The generation variant and accent seed are advanced controls. Settings offers
the visual controls; the CLI names are available for scripts and diagnostics:

```sh
horneroctl appearance accent show
horneroctl appearance scheme list
```

Saved palettes are available in Appearance for reusing a generated look.
They are useful when you want to keep a color result while trying another
wallpaper; they do not replace a theme pack.

## Theme packs and compatibility

Theme metadata and validation rules live in
[HorneroOS/config](https://github.com/HorneroOS/config/tree/main/profiles/themes).
The catalogue is generated from those packs. Wallpaper files are separate
media: packs may name an expected image without bundling that image in the
package. If the image is not present locally, choose an available wallpaper
or use a path on your own machine.

The architecture guide explains the boundaries between semantic tokens,
wallpaper analysis, shell colors, GTK, icons, and Qt:
[Appearance system](../architecture/appearance-system.md). For everyday
wallpaper selection, see [Wallpapers and color](wallpapers.md).
