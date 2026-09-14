# Appearance: themes and switching

Switch between Hornero Dark and Hornero Light, or author
your own theme pack. Fresh installs boot into Hornero Dark
with no setup and no network fetch.

How it all fits together is mapped in
[Appearance system](../architecture/appearance-system.md).

## Switching themes

```text
horneroctl appearance theme list
horneroctl appearance theme show hornero-light
horneroctl appearance theme get
horneroctl appearance theme set hornero-light --yes
```

- `list`, `show <id>`, and `get` are read-only.
- `set <id>` switches between the official pair
  (`hornero-dark`, `hornero-light`).
- `apply <id>` applies any installed pack.
- Mutations need `--yes`; `--dry-run` only previews.
- After apply, the CLI reads live state back (mode plus
  GTK). A half-applied switch is reported as a failure,
  never as success.

Related verbs:

```text
horneroctl appearance status
horneroctl appearance sync --dry-run
horneroctl appearance scheme status
dots-appearance theme list
dots-gtk-theme theme vapor-dreams
dots-gtk-theme color-scheme follow
```

`sync` re-applies the pending color scheme.
`color-scheme` sets the Libadwaita policy (`follow`,
`default`, `prefer-light`, `prefer-dark`) without
changing the theme name. Run any verb with `--help`
for the full contract.

## Authoring a theme pack

A theme is one folder,
`profiles/themes/<id>/theme.json`, in
[HorneroOS/config][config]. Copy an existing pack
(`hornero-dark` for dark, `hornero-light` for light),
keep the `id` lowercase alphanumeric with dashes, and
fill in every required field:

- `name`, `family`, `mode`, `version`: display name,
  family, `dark`/`light`, semver.
- `darkMode`, `schemeType`: legacy mode flag plus the M3
  generator hint.
- `gtkTheme`, `iconTheme`, `gtkPreferDark`: upstream
  GTK and icon pins plus the dark preference.
- `defaultWallpaper`, `wallpaperDir`: wallpaper ref
  (see below).
- `palette`: semantic ramp (`background`, `surface`,
  `text`, `primary`/`secondary`/`accent` with `on*`
  mates, `border`, `error`, `success`).
- `components`: named `background`/`foreground` pairs
  (`window`, `panel`, `card`, `buttonPrimary`, `input`,
  `tooltip`, and more).

Rules that CI enforces:

- Every color is `#RRGGBB`.
- `mode` and `darkMode` must agree.
- Text pairs must hold WCAG AA contrast; the flagship
  gate (`scripts/check-contrast.py`) fails the build on
  violation, and terminal palettes additionally hold ANSI
  floors plus red/green/yellow distinguishability.
- `schemeType` is one of `tonal-spot`, `vibrant`,
  `expressive`, `fidelity`, `content`, `neutral`,
  `monochrome`.
- Validate with `scripts/validate.sh` before opening a PR.

The full field contract is
[tokens.schema.json][schema] (`schemaVersion: 1`); the
`$schema` pointer at the top of each `theme.json` keeps
editors in sync.

## Wallpapers for theme packs

Do not vendor binaries. Add one row to
`profiles/themes/wallpapers.manifest.json` with the
pack's `defaultWallpaper` / `wallpaperDir` and where to
fetch the pack; users drop packs into
`~/.local/share/dots/wallpapers/<wallpaperDir>/` or
`~/Pictures/Wallpapers/<id>/`. An explicit path always
wins; otherwise the last-applied pointer resolves. The
flagship dark/light wallpapers are procedural SVGs
rendered on-device (see the architecture map).

## GTK, icon, and font pins

Prefer installed upstream themes: the flagships pin
`Orchis-Dark-Compact` / `Orchis-Light-Compact` for GTK
and `Papirus-Dark` for icons. The shell font stack is
sans `Rubik`, mono `CaskaydiaCove NF`, icons
`Material Symbols Rounded`; only the last two words of
that sentence ship in Arch extra (Material Symbols and
Papirus packages), so Rubik and CaskaydiaCove stay
recorded preferences with AUR-side provisioning. Do not
invent package names: check Arch extra first, as the
factory record documents.

## Troubleshooting

```text
dots-appearance doctor
dots-appearance status --json
horneroctl appearance status
```

`doctor` reports backend health; `status --json` shows
the live mode, GTK theme, icon theme, color-scheme
policy, and wallpaper the system actually resolved.

[config]: https://github.com/HorneroOS/config
[schema]: https://github.com/HorneroOS/config/blob/feat/p2-desktop-integration/profiles/themes/tokens.schema.json
