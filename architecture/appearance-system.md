# Appearance architecture

This page describes ownership and data flow for contributors. For the user
model, start with [Appearance](../desktop/appearance.md) and
[Wallpapers](../desktop/wallpapers.md).

## Ownership

- **`HorneroOS/config`** owns theme pack data, semantic brand tokens,
  defaults, wallpaper manifests, GTK assets, package contents, and the
  generated theme catalogue.
- **`HorneroOS/shell`** owns live desktop presentation, wallpaper analysis,
  M3 color roles, preview UI, and coordination of session-level appearance
  changes.
- **`HorneroOS/hornero`** owns stable `horneroctl` operations: catalogue
  resolution, apply and verification, error reporting, and prior-state
  restoration where supported.
- **User data** owns explicit overrides and generated state in the user's
  config/cache/data directories. System catalogues under `/usr/share` are
  read-only.

The theme catalogue is generated from installed packs; it is not a second
hand-maintained list. User themes take precedence over system themes when the
user deliberately installs an override. Reads and writes use the Hornero
user catalogue followed by the read-only system catalogue; no retired path
namespace is part of the lookup contract.

## Two kinds of theme pack

The catalogue supports two levels of description. Flagship themes use the
semantic model: named color roles, component surfaces, mode, versioned token
metadata, and coordinated GTK/icon/wallpaper information. Recipe-style packs
describe an appearance choice using a scheme generator and optional GTK, icon,
and wallpaper references. A recipe is not required to claim ownership of a
complete semantic palette. Both are resolved through the same catalogue and
application path; richer metadata is optional enrichment, not a separate
runtime.

Do not infer a product guarantee from a pack name. Dependency availability,
media presence, and fallback behavior come from the pack metadata and the
installed package set. The UI and CLI must report unavailable pieces instead
of claiming that an incomplete appearance was fully applied.

## Color flow

```text
theme pack or selected wallpaper
          │
          ├── semantic brand/component tokens (when provided by the pack)
          └── wallpaper analysis → selected generation mode → M3 roles
                                      │
                                      └── Shell palette and supported consumers
```

Brand tokens and generated Material roles have different purposes. Brand
tokens express Hornero's curated identity; M3 roles map a source color to
roles appropriate for controls and surfaces. They should remain related but
must not be forced into identical hex values. Wallpaper-derived colors are
user-selected appearance state, not a replacement for the pack's authored
brand palette.

The Shell's `Colours`, `WallpaperAnalysis`, and `ThemePipeline` services
coordinate rendering and previews. `horneroctl` remains usable without the
Control Center and owns the stable system-facing operations. Keep display
logic in QML, live session coordination in Shell services, OS capabilities in
the CLI, and defaults in config packs.

## Applying and recovering

Applying a pack can touch Shell colors, mode, wallpaper, GTK theme and color
policy, icons, and generated state. Each consumer has different runtime
capabilities, so this is a verified best-effort transaction rather than one
filesystem atomic rename. The operation must validate inputs before writing,
check resulting state, report partial failure accurately, and restore the
previous state where the command supports rollback. Never display success
based only on a process starting.

The official command and behavior contract is documented in
[horneroctl](../desktop/horneroctl.md). Component implementation and tests
live in the linked repositories, not in this handbook.

## Wallpaper media

Wallpaper binaries are distributed separately from pack metadata. Config
manifests identify expected media and its source. A missing default must
produce a deliberate fallback or an unavailable state; it must not make the
whole theme look malformed. Never download arbitrary images as an implicit
side effect of selecting a theme.

## Change checklist

When changing appearance data or behavior, update the owning source and its
tests, then check the downstream consumers:

- Config pack and generated catalogue.
- CLI resolution, apply verification, and error reporting.
- Shell preview and live rendering.
- GTK, icon, and Qt behavior when relevant.
- QA evidence for user-visible transitions.
- Website product data and screenshots only after the behavior is shipped.

Useful implementation references: [config](https://github.com/HorneroOS/config),
[shell](https://github.com/HorneroOS/shell), and
[hornero](https://github.com/HorneroOS/hornero).
