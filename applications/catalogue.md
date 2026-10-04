# Application catalogue

This catalogue describes the boundaries between the Hornero product, host
services, and the separately maintained personal workstation profile. A
program listed as optional is not silently installed by Hornero Config.
Package availability depends on the selected host and release.

Search the page for either the application name or the task name. For example,
**kitty**, **terminal**, **Thunar**, **files**, **Yazi**, **clipboard**, **CopyQ**,
**PDF**, **browser**, **video**, and **screenshot** are indexed together with
their workflows.

## Hornero product and session

| Component | Role in Hornero | Where to learn more |
| --- | --- | --- |
| Hornero Shell (Quickshell) | Owns bars, Launcher, Dashboard, Control Center, notifications, OSD, and media presentation. | [Desktop](../desktop/README.md), [Shell source and docs](https://github.com/HorneroOS/shell) |
| `horneroctl` | Supported CLI for appearance, config, hardware, capture, and application actions. It also offers shell-independent diagnostics. | [CLI reference](../desktop/horneroctl.md), [upstream repository](https://github.com/HorneroOS/hornero) |
| Hyprland | Wayland compositor and session integration used by the current reference environment. | [Shortcuts](../desktop/shortcuts.md), [upstream documentation](https://wiki.hypr.land/) |
| `hornero-config` | Declarative defaults, theme packs, application snippets, and package integration; does not provide a whole installed OS. | [Appearance](../desktop/appearance.md), [Config repository](https://github.com/HorneroOS/config) |
| Bash, Git, Python, `python-materialyoucolor` | Required package dependencies for the current Config CLI and palette pipeline. | [CLI reference](../desktop/horneroctl.md), [Themes](../desktop/appearance.md) |

## Terminal and command line

| App or tool | Status and Hornero behavior | Config / workflow |
| --- | --- | --- |
| Kitty | Optional host package with Hornero terminal colors and font defaults. The curated **Super + E** action opens Yazi in Kitty when available. | [`~/.config/kitty/kitty.conf`](terminal.md#kitty), [Terminal guide](terminal.md), [Kitty manual](https://sw.kovidgoyal.net/kitty/) |
| Bash | Required by `hornero-config`; used by package scripts and shell helpers. | [Terminal guide](terminal.md#shell-and-command-workflow), [Bash manual](https://www.gnu.org/software/bash/manual/) |
| Zsh | Personal workstation choice, not a Hornero Config dependency. The dotfiles profile configures its prompt and startup files. | [Terminal guide](terminal.md#shell-and-command-workflow), [Zsh documentation](https://zsh.sourceforge.io/Doc/) |
| tmux | Optional personal terminal multiplexer with a dotfiles-managed config and session helpers. | [Terminal guide](terminal.md#shell-and-command-workflow), [tmux manual](https://github.com/tmux/tmux/wiki) |
| Git | Required by Config and receives shared aliases, ignore rules, and defaults where the dotfiles profile is used. Hornero does not set a personal commit identity. | [Terminal guide](terminal.md#shell-and-command-workflow), [Git book](https://git-scm.com/book/en/v2) |
| `bat`, `exa`, `fzf`, `direnv`, `jq`, `uv`, `shellcheck` | Optional command-line tools from the personal workstation profile. These are not Hornero Shell requirements. | [Terminal guide](terminal.md#shell-and-command-workflow), [dotfiles repository](https://github.com/ulises-jeremias/dotfiles) |
| Fastfetch, btop, Cava | Optional configured terminal summary, resource monitor, and audio visualizer. The Shell visualizer is separately opt-in. | [System utilities](system-utilities.md), [Fastfetch](https://github.com/fastfetch-cli/fastfetch), [btop](https://github.com/aristocratos/btop), [Cava](https://github.com/karlstav/cava) |

## Files, browsing, and documents

| App or tool | Status and Hornero behavior | Config / workflow |
| --- | --- | --- |
| Thunar | Optional file manager. Config adds useful keyboard actions and context integrations; **Super + F** follows the host FileManager association. | [Files](files.md#thunar-for-visual-file-management), [Thunar documentation](https://docs.xfce.org/xfce/thunar/start) |
| Yazi | Personal-profile file manager, not a Hornero Config dependency. **Super + E** opens it in Kitty when installed; preview tools are optional. | [Files](files.md#yazi-for-keyboard-driven-browsing), [Yazi documentation](https://yazi-rs.github.io/docs/) |
| `xdg-mime`, `exo-open`, desktop files | Host mechanisms that choose the default app for a URL or MIME type. Hornero requests these handlers instead of embedding a browser or file manager. | [Default applications](default-apps.md), [freedesktop MIME applications](https://specifications.freedesktop.org/mime-apps-spec/latest/) |
| Zen Browser | Optional personal-profile browser. It is not the required browser and is not a Hornero package dependency. | [Browsing, editing, and documents](browsing-documents.md#browsers), [Zen](https://zen-browser.app/) |
| Neovim, VS Code, other editors | Chosen by the host. The personal profile contains editor configuration; Hornero does not require one editor. | [Browsing, editing, and documents](browsing-documents.md#editors), [Default applications](default-apps.md) |
| Zathura, Evince, other PDF viewers | Host MIME choice; none is required by Hornero Config. | [Browsing, editing, and documents](browsing-documents.md#pdfs-images-and-media-files), [Default applications](default-apps.md) |
| sxiv, other image viewers | Optional personal-profile image viewer; file opening follows the host image MIME association. | [Browsing, editing, and documents](browsing-documents.md#pdfs-images-and-media-files), [Default applications](default-apps.md) |
| mpv, other media players | Optional playback apps. Shell controls connect to active MPRIS players; file opening still follows MIME defaults. | [Media and audio](media-audio.md#media-players), [mpv manual](https://mpv.io/manual/stable/) |
| Xarchiver, archive helpers | Optional host tools used by file-manager actions; archive support is not implied by installing the Shell. | [Files](files.md#file-opening-and-archives), [Xarchiver](https://github.com/ib/xarchiver) |

## Clipboard, capture, audio, and connectivity

| App or service | Role and availability | Guide |
| --- | --- | --- |
| CopyQ | Optional clipboard-history interface with Hornero configuration and theme colors. | [Clipboard](clipboard.md), [CopyQ manual](https://copyq.readthedocs.io/en/latest/) |
| `wl-clipboard`, `cliphist` | Separate Wayland clipboard tools; the personal session profile can run `wl-paste --watch` to collect history. Clipboard data is sensitive. | [Clipboard](clipboard.md), [wl-clipboard](https://github.com/bugaevc/wl-clipboard), [cliphist](https://github.com/sentriz/cliphist) |
| `grim`, `slurp`, `swappy`, `sss`, GPU Screen Recorder | Optional screenshot, region-selection, annotation, and recording backends. `horneroctl capture` reports or invokes available tools. | [Screenshots and recording](capture.md) |
| PipeWire, WirePlumber, `pamixer`, `pavucontrol`, `playerctl` | Host-owned sound server, mixer, and MPRIS controls. Exact installation varies; Hornero does not replace the audio stack. | [Media and audio](media-audio.md), [PipeWire](https://pipewire.org/), [playerctl](https://github.com/altdesktop/playerctl) |
| NetworkManager, BlueZ, VPN plugins | Host-owned networking, Bluetooth, and VPN providers. Control Center operates only where a compatible service/provider exists. | [Connectivity](connectivity.md), [NetworkManager](https://networkmanager.dev/), [BlueZ](http://www.bluez.org/) |
| `brightnessctl`, `acpi`, `upower`, `power-profiles-daemon` | Optional host utilities for brightness, battery, and power profile state. Device support determines which controls appear. | [System utilities](system-utilities.md#tools-in-the-personal-workstation-configuration) |

## Appearance, login, and desktop support

| App or component | Role and availability | Guide |
| --- | --- | --- |
| GTK, Fontconfig, `qt6ct` | Optional host appearance components. Hornero can configure them; external GTK themes and icon packages must be installed separately. | [Appearance](../desktop/appearance.md) |
| Papirus, Numix Circle, Orchis | Optional icon and GTK theme packages used by the personal profile and theme packs. Missing packages produce a documented fallback/degraded state. | [Appearance](../desktop/appearance.md#theme-packs-and-wallpaper-availability) |
| Rubik, Cascadia Code Nerd Font, Material Symbols | Fonts used by the configured workstation and Shell. Other fonts remain available as user choices. | [Appearance](../desktop/appearance.md) |
| Hyprlock, Hypridle | Optional lock and idle-session tools, separate from Shell notifications and Controls. | [Lock and login](login-lock.md#lock-the-session) |
| SDDM and Hornero Greeter | Separate display-manager and login-screen components. They are not part of the Preview composition. | [Lock and login](login-lock.md#hornero-greeter) |
| Portals, `polkit-gnome`, `libnotify`, `dex` | Session services and helpers used for file dialogs, privilege prompts, notification compatibility, and desktop autostart. They are integration components rather than end-user apps. | [System utilities](system-utilities.md#internal-implementation-tools) |

## Apps that are not user-facing

Build-only libraries, `hornero-config` materialization helpers, Quickshell
services, theme generators, screenshot QA tools, and package hooks implement
the desktop but are not presented as applications. Their developer contracts
belong in the Config, Shell, CLI, and QA repositories. Hardware-specific
utilities and optional profiles may vary by machine.

The [Apps and workflows guide](README.md) links the complete user journeys.
For default handlers, start with [Default applications](default-apps.md); for
the public workstation source, see
[ulises-jeremias/dotfiles](https://github.com/ulises-jeremias/dotfiles).
