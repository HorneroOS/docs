# System utilities

This page separates tools with Hornero-supplied defaults from personal
workstation packages and implementation dependencies.

## Tools with configuration defaults

`hornero-config` supplies optional configuration for:

- **Fastfetch**, a terminal system summary, including Hornero's text mark.
- **btop**, a terminal resource monitor.
- **Cava**, an audio visualizer configuration. The desktop visualizer stays
  off by default.
- **Git**, a safe base configuration and ignore rules, with no user name or
  email. Set your identity in your own Git configuration before committing.
- **Kitty**, **Thunar**, **CopyQ**, `handlr`, `qt6ct`, GTK, and Fontconfig.
  See their workflow pages and [Appearance](../desktop/appearance.md).

The package lists these desktop programs as optional dependencies. Its
required dependencies support Hornero appearance and theme operations, not
general web browsing or document editing.

## Session and hardware helpers

The curated configuration calls or expects common host tools such as
`exo-open`, `xdg-utils`, `wl-clipboard`, `cliphist`, `playerctl`, `pamixer`,
`brightnessctl`, NetworkManager, BlueZ, Hyprlock, and Hypridle. The exact
set comes from the selected host composition. These helpers provide desktop
services; most do not need a separate user-facing app page.

The Shell owns notifications, on-screen display, lock coordination, and its
own settings panels. Hornero Config masks common competing notification
services in its curated session defaults. Do not start another notification
daemon unless you deliberately replace that ownership.

## Personal dotfiles additions

The [dotfiles repository](https://github.com/ulises-jeremias/dotfiles) can
provision optional tools including Zen Browser, Zsh, tmux, Yazi preview
utilities, Discord, Lutris, Docker, Safe Eyes, ClamTk, PipeWire studio
software, and GPU Screen Recorder. Those choices belong to that personal
workstation profile, not the Hornero release catalogue. Check hardware-specific
GPU and audio instructions against the actual machine and current Arch
documentation.

Hornero's Git defaults do not contain a user name or email. Set your own
identity before creating commits.

Useful references: [Git](https://git-scm.com/doc),
[Fastfetch](https://github.com/fastfetch-cli/fastfetch),
[btop](https://github.com/aristocratos/btop),
[Hyprland](https://wiki.hyprland.org/),
[Arch Wiki](https://wiki.archlinux.org/).
