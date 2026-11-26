# Hornero OS documentation

[![lint](https://github.com/HorneroOS/docs/actions/workflows/lint.yml/badge.svg)](https://github.com/HorneroOS/docs/actions/workflows/lint.yml)
[![License: MIT](https://img.shields.io/github/license/HorneroOS/docs)](LICENSE)

Find a guide by the task you are trying to complete. This repository is the
user and contributor handbook; implementation contracts stay with the
[Shell](https://github.com/HorneroOS/shell), [CLI](https://github.com/HorneroOS/hornero),
and [configuration](https://github.com/HorneroOS/config) repositories.

> HorneroOS is an Arch-based operating-system family in development. Its
> Desktop edition is Wayland-first, with Hyprland as the default validated
> compositor and Niri as an experimental backend. A signed preview ISO
> (Desktop, Studio and Gaming, v0.2.0-preview32) is published;
> it is not a
> stable or supported release, and v0.2.0-preview32 itself has no
> physical-hardware validation or acceptance yet. The
> [release page](https://horneroos.com/releases) and
> [installation status](https://horneroos.com/install) are the current source
> for what can be installed.

## Choose a path

| If you want to… | Start here |
| --- | --- |
| Understand release and installation status | [Getting started](getting-started/README.md) |
| Install and take the first steps | [Installing step by step](getting-started/install-step-by-step.md) · [Post-install](applications/post-install-first-steps.md) |
| Install on an existing Arch Linux system | [Install on Arch](getting-started/install-on-arch.md) |
| Boot a fallback kernel, fix NVIDIA, play, or record | [Kernel and fallback](desktop/kernel-and-fallback.md) · [Hybrid graphics](hardware/hybrid-graphics-nvidia.md) · [Gaming](applications/gaming-proton-gamemode.md) · [Studio audio](applications/studio-low-latency.md) |
| Know what is tested and what is not | [Tested and untested](hardware/tested-and-untested.md) · [Troubleshooting by symptom](troubleshooting/by-symptom.md) |
| Use the desktop, apps, and Control Center | [Desktop](desktop/README.md) · [Apps and workflows](applications/README.md) |
| Know what Desktop, Studio and Gaming really offer, verified and not | [Editions](editions/README.md) |
| Learn the Hornero Signal look: themes, type, accessibility | [Hornero Signal](desktop/hornero-signal.md) |
| Change themes, colors, or wallpaper | [Appearance](desktop/appearance.md) · [Wallpapers](desktop/wallpapers.md) |
| Choose a bar arrangement | [Layouts](desktop/layouts.md) |
| Lock, restart, or shut down the desktop session | [Session menu](desktop/session-menu.md) |
| Find a keyboard shortcut | [Shortcuts](desktop/shortcuts.md) |
| Automate or inspect the system from a terminal | [horneroctl](desktop/horneroctl.md) |
| Update the system and understand recovery limits | [Updates and recovery: no system rollback yet](desktop/updates-and-rollback.md) |
| Understand security, encryption, and trust boundaries | [Security and privacy](security/README.md) |
| Diagnose graphics or device problems | [Hardware](hardware/README.md) · [Troubleshooting](troubleshooting/README.md) |
| Understand editions and system boundaries | [Architecture](architecture/README.md) |
| Build, test, or contribute | [Development](development/README.md) |
| Write a shell extension | [Extensions 2.0 authoring guide](development/extensions.md) |
| Design an interface for HorneroOS | [Design language](development/design-language.md) |

![Keybindings overlay listing live Hyprland binds with search,
Essential Applications group expanded.](https://www.horneroos.com/captures/cap-shell-08.png)

*The keybindings overlay, read live from Hyprland — see
[Shortcuts](desktop/shortcuts.md). Real capture; the same capture is
reused intentionally from that guide, not a new copy.*

## How these docs stay accurate

Steps describe behavior available in the released product unless they are
labelled **Development** or **Preview**. Package, installer, and release
availability can change; check the live release and installation pages before
following older notes. Commands are taken from `horneroctl` help and current
product configuration. Personal machine examples from the former dotfiles
wiki are not system requirements.

The website imports these Markdown pages at a reviewed commit and adds its own
navigation, search, and responsive presentation. This repository owns the
content; the website does not maintain a second copy.

## Areas

- [Getting started](getting-started/README.md) — release status and a safe
  first look.
- [Desktop](desktop/README.md) — appearance, wallpaper, layouts, compositors,
  and shortcuts.
- [Hornero Signal](desktop/hornero-signal.md) — the HorneroOS visual
  language: themes, IBM Plex type, glyphs, high contrast, and reduced
  motion.
- [Apps and workflows](applications/README.md) — the configured application
  catalog and the paths that connect those tools to Hornero.
- [horneroctl](desktop/horneroctl.md) — supported command-line entry points.
- [Hardware](hardware/README.md) — device diagnostics and graphics guidance.
- [Security and privacy](security/README.md) — disk encryption, Secure Boot,
  firewall, release signing, and trust boundaries.
- [Troubleshooting](troubleshooting/README.md) — recover from common failures.
- [Architecture](architecture/README.md) — editions, ownership, and data flow.
- [Development](development/README.md) — code, QA, and contribution paths.
- [Design language](development/design-language.md) — product identity, UI
  principles, source-of-truth map, and guidance for installer contributors.
  The design authority is
  [RFC 0001 — Hornero Signal](development/rfc-0001-hornero-signal.md).

## Languages

English is the canonical text. Argentine Spanish translations live in
[`es/`](es/README.md), mirroring the English paths; the website serves
the Spanish page when a translation exists and falls back to English
(labelled as such) when it does not. When an English page changes, its
`es/` counterpart should change in the same pull request.

## License

[MIT](LICENSE).

---

[Website](https://www.horneroos.com) ·
[Docs](https://www.horneroos.com/docs) ·
[`HorneroOS/shell`](https://github.com/HorneroOS/shell) ·
[`HorneroOS/hornero`](https://github.com/HorneroOS/hornero) ·
[`HorneroOS/config`](https://github.com/HorneroOS/config) ·
[Issues](https://github.com/HorneroOS/docs/issues) ·
[License](LICENSE)
