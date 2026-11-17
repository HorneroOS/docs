# Appearance architecture

This page describes ownership and data flow for contributors. For the user
model, start with [Hornero Signal](../desktop/hornero-signal.md),
[Appearance](../desktop/appearance.md) and
[Wallpapers](../desktop/wallpapers.md). The design authority is
[RFC 0001 — Hornero Signal](../development/rfc-0001-hornero-signal.md);
token names, font families, the glyph API, motion names and the
anchored-surface contract change only by amending it.

## Ownership

- **`HorneroOS/config`** owns the token contract
  (`profiles/themes/tokens.schema.json`, schema version 2), every theme pack,
  the generated theme catalogue, wallpaper manifests and credits, brand
  assets, the GTK/Qt/terminal/compositor generators
  (`lib/hornero/signal_theme.py`, `lib/hornero/signal_render.py`) and factory
  defaults, including Cockpit and Signal Night.
- **`HorneroOS/shell`** owns live presentation: the `Signal` singleton
  (`Signal.palette.<role>`), IBM Plex type roles, Hornero Glyphs, motion
  tokens, theme previews, accessibility overrides and the anchored-surface
  solver.
- **`HorneroOS/hornero`** owns stable `horneroctl` operations: catalogue
  resolution, theme apply and verification, the one-shot migration of
  retired selections, diagnostics and error reporting.
- **User data** holds explicit overrides and generated state in the user's
  config, state and cache directories. System catalogues under `/usr/share`
  are read-only.

The theme catalogue is generated from installed packs; it is not a second
hand-maintained list. Reads use the user catalogue, then the read-only system
catalogue.

## One kind of theme pack

Every theme is `profiles/themes/<id>/theme.json` with `schemaVersion: 2`:
`id`, `name`, `mode` (`dark` or `light`), `palette` (exactly the RFC §3.1
roles, plus the optional `glow`), `terminal` (16 colours), `gtkTheme`,
`iconTheme`, `defaultWallpaper` and `wallpaperDir`; `description`, `tags`,
`collection` and `collectionOrder` are optional presentation metadata.
There are no seeds, scheme types, variants or partial "recipe" packs. A pack
that does not define the full role set is invalid, and Config's contrast
check runs on every shipped pack.

`collection` describes authorship and presentation only (`hornero-signal`,
`hornero-originals`, community ports); it never implies a different token
model.

## Colour flow

```text
config theme pack (schema v2)
          │  horneroctl appearance theme apply|set   (or the shell, for built-ins)
          ▼
$XDG_STATE_HOME/hornero/signal/scheme.json   ← written atomically
          │
          ├── Shell: watches the file → Signal.palette.<role>
          ├── Hyprland borders, hyprlock variables
          ├── Kitty include, Alacritty, Ghostty, btop, Cava palettes
          ├── GTK 3/4 + libadwaita recolour (pack's gtkTheme tree)
          └── Qt via qt6ct colour scheme
```

The live scheme is
`{"schemaVersion":2,"id":…,"mode":…,"palette":{role:"#RRGGBB"},"terminal":[16]}`.
For curated themes, wallpapers never feed this flow and the wallpaper
pointer is a separate file the shell watches for the image only. The
optional **Hornero Chromatic** theme (`hornero-chromatic`,
[RFC 0002](../development/rfc-0002-hornero-chromatic.md), not yet
implemented) adds one step in front of the same writer: horneroctl runs the
native `hornero-chromatic` helper (shipped with the shell) to synthesise the
Signal roles from the wallpaper, an image or a chosen colour, validates them
against config's gate table and then writes the live scheme and every output
exactly as for a curated theme. There is no Material step and no Python in
that path.

High contrast (`appearance.highContrast`) is a shell-only override: the shell
renders the `hornero-signal-contrast` table and disables translucency without
changing the persisted theme. Reduced motion (`appearance.reducedMotion` or
GNOME's `enable-animations`) sets durations to zero except short opacity
fades.

Keep display logic in QML, live session coordination in shell services, OS
operations in `horneroctl`, and data in Config packs. `horneroctl` stays
usable without the Control Center.

## Applying and recovering

Applying a theme writes the live scheme atomically, then the derived files,
then GTK, and persists the selection. Each consumer has different runtime
capabilities, so the whole apply is a verified best-effort transaction
rather than one atomic rename. It must validate the pack before writing,
check the resulting state, report partial failure accurately and, for
`appearance theme set`, roll back to the previous built-in theme on
failure. Never report success because a process started.

Retired ids (`hornero-dark`, `hornero-light`, `hornero-199x`, `neon-city`,
`vapor-dreams`, `soft-morning`, `warm-sunset`) are rejected by `apply` with
their replacement. A persisted selection naming one of them migrates once,
on shell load or through `horneroctl appearance sync --yes`. This is a data
migration, not an alias layer.

The command contract is documented in [horneroctl](../desktop/horneroctl.md)
and in `horneroctl appearance --help`.

## Wallpaper media

Wallpaper binaries are separate from pack metadata. Config manifests name
the expected media and its source; licensed photographs and their credits
ship with `hornero-config`, and the Signal wallpapers are rendered from SVG
on the target machine. A missing default produces an unavailable state, not
a malformed theme. Never download an image as a side effect of selecting a
theme.

## Change checklist

When changing appearance data or behaviour, update the owning source and its
tests, then check the downstream consumers:

- RFC 0001, if a role, family, glyph API or motion name changes.
- Config schema, packs, contrast check and generated catalogue.
- `horneroctl` apply, verification, migration and error reporting.
- Shell `Signal` roles, previews and live rendering.
- GTK, icon, Qt and terminal output.
- QA evidence for user-visible transitions, stating where it ran.
- Website product data and screenshots only after the behaviour ships.

Implementation references: [config](https://github.com/HorneroOS/config),
[shell `docs/NATIVE-APPEARANCE.md`](https://github.com/HorneroOS/shell/blob/main/docs/NATIVE-APPEARANCE.md)
and [hornero](https://github.com/HorneroOS/hornero).
