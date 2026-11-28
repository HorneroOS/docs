# Desktop: build your world

The base edition: Hornero Shell on Wayland, Hyprland (default) and Niri as
supported compositor backends, Hornero Signal visuals, 14 bar layouts,
themes, experience modes and a plugin system. Studio and Gaming extend it;
they do not replace it.

**Maturity: Supported.** Daily-driven in production across multiple physical
workstations and validated in UEFI and Legacy BIOS KVM. Installs from the
signed `v0.2.0-preview42` ISO or preinstalled QCOW2 (see the
[releases page](https://horneroos.com/releases)).

## What you can build

- Pick a layout (Cockpit is the default), a theme (Signal Night/Day and the
  curated themes) and an experience mode (Focus, Everyday, Signal, Gaming,
  Studio) independently. Switching a mode never changes your layout or theme.
- Add desktop widgets and bar extensions through the Extensions pane.

See [Layouts](../desktop/layouts.md), [Appearance](../desktop/appearance.md),
[Experience modes](../desktop/experience-modes.md) and
[Control Center](../desktop/control-center.md).

## Verified

- **Shell unit and contract tests, QML lint, mode policy under fullscreen**:
  Where: CI + offscreen
- **Desktop boots to a ready session, mode switching, screenshots**: Where: QA
  VM (Hyprland)
- **Package composition for the edition**: Where: `scripts/resolve-edition.py`
  in CI

## Not validated

- Every third-party laptop, hybrid GPU wiring, or external dock beyond
  tested workstations.
- Niri capability parity with Hyprland-only protocols (see
  [Wayland compositors](../desktop/compositors.md)).
- Multi-monitor mixed-scale and ultrawide layouts (partly captured only).
- Performance budgets (frame time, input latency, idle CPU) are not measured
  for every layout.
