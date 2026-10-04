# Apps and workflows

This guide describes the applications and system tools that Hornero
configures or calls. It separates three different things: packages supplied
by a release, configuration files supplied by `hornero-config`, and
applications available only when the host or personal dotfiles install
them.

## What an installed Hornero release includes

The current edition profiles compose Hornero Shell, Hornero Config, and
`horneroctl`. Hornero does not yet publish a supported ISO or end-user
installer. The `hornero-config` package has a small required dependency set;
desktop application packages such as Kitty, Thunar, CopyQ, `handlr`, and
`qt6ct` are optional dependencies. Their defaults are installed only when
the related application is installed.

The current `~/.dotfiles` checkout provisions a broader personal Arch
workstation. Its package scripts install programs such as Kitty, Thunar,
Yazi, CopyQ, Zen Browser, Zsh, PipeWire tools, screenshot tools, and studio
software. That provisioning is useful source material, but it is not the
Hornero release package set. Do not treat a personal `chezmoi apply` as a
Hornero installer.

## Application and integration catalogue

| App or tool | Hornero relationship | Where to learn more |
| --- | --- | --- |
| Hyprland | Compositor configuration and shortcuts come from Hornero Config. | [Desktop](../desktop/README.md), [shortcuts](../desktop/shortcuts.md) |
| Quickshell / Hornero Shell | Owns bars, launcher, Dashboard, notifications, OSD, and Control Center. | [Desktop](../desktop/README.md), [Shell docs](https://github.com/HorneroOS/shell/tree/main/docs) |
| `horneroctl` | Opens Shell surfaces and provides system, app, capture, and configuration commands. | [`horneroctl`](../desktop/horneroctl.md) |
| Kitty | Optional `hornero-config` dependency with a Hornero palette. The current Super+E Yazi shortcut launches Kitty directly. | [Terminal](terminal.md) |
| Yazi | Terminal file manager launched by the Hornero Super+E shortcut. The personal dotfiles setup also adds a Thunar context-menu action. | [Files](files.md) |
| `exo` / `exo-open` | Launches the default TerminalEmulator, FileManager, and WebBrowser from Hyprland shortcuts. | [Default applications](default-apps.md) |
| `handlr-regex` / `handlr` | Optional config dependency for reading MIME defaults; `horneroctl` uses `xdg-mime` to set them. | [Default applications](default-apps.md) |
| CopyQ | Optional config dependency with a base config and generated theme support. Used by the clipboard shortcut when installed. | [Clipboard](clipboard.md) |
| `cliphist` and `wl-clipboard` | Wayland clipboard history collection and fallback integration in the configured session. | [Clipboard](clipboard.md) |
| GTK 3/4 and Hornero GTK packs | Configured by Hornero Config; GTK packs are applied by the appearance pipeline. | [Appearance](../desktop/appearance.md) |
| `qt6ct` | Optional Qt 6 platform-theme configuration. Hornero supplies Fusion, font, icon, and generated palette settings. | [Appearance](../desktop/appearance.md) |
| Papirus and Orchis | Optional icon and GTK packages referenced by factory appearance defaults. Other theme packs may request other third-party assets. | [Themes](https://horneroos.org/themes) |
| Fontconfig and Material Symbols | Font rendering defaults and the Shell's symbol font integration. | [Appearance](../desktop/appearance.md) |
| Fastfetch, btop, Cava | Optional applications with configuration files supplied by Hornero Config. | [System utilities](system-utilities.md) |
| PipeWire, `pavucontrol`, `pamixer` | Host audio services and mixer utilities used by controls and media workflows; not installed by the Hornero Config package. | [Media and audio](media-audio.md) |
| MPRIS players, `playerctl`, mpv | The Shell observes MPRIS players. Media keys use `playerctl`; mpv is a host playback option, not a required release dependency. | [Media and audio](media-audio.md) |
| NetworkManager / `nmcli` | Host network service used by the Shell's connection controls. | [Connectivity](connectivity.md) |
| BlueZ | Host Bluetooth service used by the Shell's device controls. | [Connectivity](connectivity.md) |
| `sss`, `grim`, `slurp` | Screenshot capture integrations in the personal dotfiles workflow. `horneroctl capture screenshot` resolves the `sss` helper when present. | [Screenshots and recording](capture.md) |
| GPU Screen Recorder | Optional recording backend called by `horneroctl capture record`. | [Screenshots and recording](capture.md) |
| Hyprlock and Hypridle | Lock screen and idle behavior configured in the compositor defaults; packages belong to the host composition. | [Lock and login](login-lock.md), [troubleshooting](../troubleshooting/README.md) |
| Hornero Greeter / SDDM | Optional login-screen component maintained in its own repository. It is not installed by the current release profile. | [Lock and login](login-lock.md) |
| `xdg-user-dirs`, `xdg-autostart`, `dex` | Host helpers for standard user folders and launching desktop autostart entries. | [System utilities](system-utilities.md) |
| Archive tools and preview helpers | Optional host programs such as `p7zip`, `poppler`, `ffmpegthumbnailer`, ImageMagick, `fd`, `fzf`, and `ripgrep` support Yazi workflows. | [Files](files.md) |
| Editors, image viewers, and PDF readers | Host-selected applications. Personal dotfiles have included `sxiv`; that is not the Hornero default. | [Default applications](default-apps.md) |
| Zsh and tmux | Interactive shell and multiplexer provisioned by personal dotfiles; Hornero Config does not define their user setup. | [Terminal](terminal.md) |
| Git | Required package dependency with Hornero defaults that deliberately omit user identity. | [System utilities](system-utilities.md) |
| Browser, editor, image viewer, PDF viewer | Chosen from host-installed desktop applications. Hornero does not require one particular product in these roles. | [Default applications](default-apps.md) |

This catalogue describes roles, not a fixed Arch package transaction. Check
the current release notes and your package manager before installing optional
software.

## User workflows

- [Terminal](terminal.md) explains Kitty, terminal launch, and shell scope.
- [Files](files.md) connects Thunar, Yazi, file associations, and previews.
- [Clipboard](clipboard.md) explains CopyQ, `cliphist`, and session history.
- [Default applications](default-apps.md) covers browser, editor, media, PDF,
  image, file-manager, and terminal associations.
- [Media and audio](media-audio.md) connects MPRIS, PipeWire, volume controls,
  players, and the Shell.
- [Screenshots and recording](capture.md) covers `horneroctl capture` and
  its optional backends.
- [Connectivity](connectivity.md) covers network and Bluetooth services.
- [System utilities](system-utilities.md) covers the configured monitoring
  and information tools.

## Historical source review

The former dotfiles wiki supplied workflow ideas, not current product
contracts. Its migration status is recorded in
[Historical wiki disposition](../development/dotfiles-wiki-disposition.md).
Old package lists, `dots-*` commands, paths under `~/.cache/dots`, private
hardware results, and chezmoi-only procedures are not current Hornero
instructions.
