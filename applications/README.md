# Apps and workflows

Hornero is a desktop product, not a fixed collection of third-party apps. Its
Shell owns desktop surfaces, Hornero Config supplies system defaults, and the
host decides which optional applications and services are installed. These
guides explain how those parts connect and what to check when one is missing.

## What is part of Hornero?

The current Preview composition has no ISO or supported installer. It brings
together Hornero Shell, `horneroctl`, and the `hornero-config` package. Config
requires Bash, Git, Python, and `python-materialyoucolor`; it does not install
a complete workstation by itself.

### Hornero defaults for optional applications

These programs remain separate host packages. If installed, they can use
defaults supplied by Hornero Config:

- **Kitty** — terminal colors, typography, and key settings; used by the
  default **Super + E** Yazi workflow. See [Terminal](terminal.md).
- **Thunar** — file-manager accelerators, bulk rename, and context actions.
  **Super + F** asks the host to open its FileManager. See [Files](files.md).
- **CopyQ** — clipboard history UI configuration and generated theme colors.
  See [Clipboard](clipboard.md).
- **Fastfetch**, **btop**, and **Cava** — terminal summary, resource monitor,
  and visualizer configuration. See [System utilities](system-utilities.md).
- **Git** — shared defaults and ignore rules, with no user identity. Add your
  own name and email before creating commits.
- **Fontconfig**, **GTK**, **qt6ct**, and **Papirus** — font and application
  appearance defaults. GTK themes and external icon packages can be missing;
  Hornero does not download them. See [Appearance](../desktop/appearance.md).
- **`handlr`** — optional integration for inspecting file and app handlers.
  [`horneroctl`](../desktop/horneroctl.md) uses `xdg-mime` to update MIME
  associations.

### Host services and applications

- **Hyprland** runs the configured desktop session. Hornero Config supplies
  its defaults; see [shortcuts](../desktop/shortcuts.md).
- **Quickshell / Hornero Shell** owns bars, Launcher, Dashboard, notifications,
  OSD, and Control Center. See the [desktop guide](../desktop/README.md) and
  [Shell documentation](https://github.com/HorneroOS/shell/tree/main/docs).
- **`exo-open` and XDG helpers** start the host's selected terminal, file
  manager, browser, and MIME handlers. See [Default applications](default-apps.md).
- **Yazi** is not a Config package dependency, but **Super + E** invokes it
  inside Kitty. The personal workstation profile can install Yazi and preview
  helpers. See [Files](files.md).
- **`cliphist` and `wl-clipboard`** can collect Wayland clipboard history;
  **PipeWire**, `pamixer`, `pavucontrol`, and `playerctl` provide host audio
  and media integration. See [Clipboard](clipboard.md) and
  [Media and audio](media-audio.md).
- **NetworkManager and BlueZ** provide host network and Bluetooth services.
  Control Center exposes their state; see [Connectivity](connectivity.md).
- **`sss`, `grim`, `slurp`, and GPU Screen Recorder** provide optional capture
  backends. See [Screenshots and recording](capture.md).
- **Hyprlock and Hypridle** support lock and idle behavior. **SDDM and Hornero
  Greeter** are separate login components, not part of the current Preview
  composition. See [Lock and login](login-lock.md).

### Optional personal workstation applications

The public [dotfiles repository](https://github.com/ulises-jeremias/dotfiles)
configures a broader Arch workstation. Its optional applications include Zen
Browser, Zsh, tmux, mpv, sxiv, Xarchiver, and audio or studio tools. They are
not Hornero release defaults; the relevant workflow pages explain their role.

The release package's exact dependency metadata is maintained in
[Hornero Config](https://github.com/HorneroOS/config/blob/main/packaging/PKGBUILD).
The [dotfiles repository](https://github.com/ulises-jeremias/dotfiles) is a
separate, broader workstation configuration. It is useful to understand the
personal application setup, but Hornero's product behavior does not depend on
running its provisioning commands.

## Follow a workflow

- [Terminal](terminal.md) — Kitty, the account shell, Zsh, and tmux.
- [Files](files.md) — Thunar, Yazi, previews, archives, and file associations.
- [Clipboard](clipboard.md) — CopyQ, Wayland clipboard history, and privacy.
- [Default applications](default-apps.md) — host app handlers and MIME types.
- [Browsing, editing, and documents](browsing-documents.md) — browsers,
  editors, PDFs, and image/file associations.
- [Media and audio](media-audio.md) — PipeWire, volume controls, MPRIS, and players.
- [Screenshots and recording](capture.md) — screenshot and recording backends.
- [Connectivity](connectivity.md) — NetworkManager, Bluetooth, and VPN providers.
- [System utilities](system-utilities.md) — Git, Fastfetch, btop, Cava, and
  host helpers.
- [Lock and login](login-lock.md) — session lock versus SDDM login.

These guides describe the current Hornero contract first. Optional personal
workstation choices are labelled as such. Historical wiki procedures were
reviewed and classified in [the source disposition](../development/dotfiles-wiki-disposition.md);
old paths and `dots-*` commands are not current instructions.

For a searchable, status-labelled inventory of applications and integrated
services, see the [application catalogue](catalogue.md). It separates Hornero
components from optional host apps and the public personal workstation
profile.

The catalogue is organized around the work people do:
[terminal](catalogue.md#terminal-and-command-line),
[files and documents](catalogue.md#files-browsing-and-documents),
[clipboard, capture, and media](catalogue.md#clipboard-capture-audio-and-connectivity),
and [appearance and login](catalogue.md#appearance-login-and-desktop-support).
