# System and command-line utilities

This guide distinguishes Hornero's system configuration from applications in
the broader personal Arch workstation profile. A file under `/etc/xdg` is a
system default; a file under `~/.config` belongs to the user and can override
it. The exact installed packages still depend on the host and selected
composition.

## Tools configured by Hornero Config

The `hornero-config` package requires Bash, Git, Python, and
`python-materialyoucolor` for its appearance operations. Its optional package
metadata names tools for which it can provide defaults:

### Terminal and developer tools

- **Git** — shared defaults and ignore rules in `/etc/xdg/git/`. Add your
  own `user.name` and `user.email`; Hornero deliberately ships no identity.
- **Fastfetch** — terminal system summary. Defaults live in
  `/etc/xdg/fastfetch/`; the personal workstation adds a Hornero text mark.
- **btop** — interactive CPU, memory, process, and device monitor. Defaults
  live in `/etc/xdg/btop/`.

### Appearance and desktop integration

- **Fontconfig** — font selection defaults under `/etc/xdg/fontconfig/`;
  font files are separate packages.
- **GTK 3/4** — theme, icon, and dark/light preferences under XDG config
  paths. Hornero also ships Hornero Dark, Light, and Pampa GTK theme assets.
- **`qt6ct`** — optional Qt 6 theme and palette under `/etc/xdg/qt6ct/`.
  Applications use it only when the host selects qt6ct as its platform theme.
- **Papirus icons** — optional external icon package referenced by factory
  defaults. The host fallback remains available when it is absent.
- **Kitty**, **Thunar**, **CopyQ**, and **`handlr`** — optional application
  defaults under `/etc/xdg/kitty/`, `/etc/xdg/Thunar/`, `/etc/xdg/copyq/`,
  and `/etc/xdg/handlr/`. See [Terminal](terminal.md), [Files](files.md),
  [Clipboard](clipboard.md), and [Default applications](default-apps.md).

### Media

- **Cava** — optional terminal audio visualizer configuration under
  `/etc/xdg/cava/`. It does not start the Shell visualizer, which is off by
  default. See [Media and audio](media-audio.md).

These are defaults and integrations. Programs marked optional are not
installed merely because their config file exists. Inspect the package's
[dependency metadata](https://github.com/HorneroOS/config/blob/main/packaging/PKGBUILD)
for the current required and optional package names.

## Tools in the personal workstation configuration

The public [dotfiles repository](https://github.com/ulises-jeremias/dotfiles)
describes one broader workstation; it is not the Hornero release manifest.
Its public Arch profile can install tools such as:

**Shell helpers:** `bat`, `exa`, `fzf`, `fd`, `ripgrep`, `zoxide`, `direnv`,
and `jq` support listing, search, navigation, JSON inspection, and project
environments.

**Source and package tools:** Git, `github-cli`, Python, `uv`,
`pacman-contrib`, and ShellCheck support development and system maintenance.

**Device utilities:** `acpi`, `upower`, `brightnessctl`, and
`power-profiles-daemon` report or change device state.

**Wayland capture:** `grim`, `slurp`, `sss`, and GPU Screen Recorder provide
optional capture backends. See [Screenshots and recording](capture.md).

**Session integration:** `gnome-keyring`, `dex`, and `polkit-gnome` provide
secret storage, XDG autostart, and privilege prompts.

**Media and sound:** PipeWire, `pamixer`, `playerctl`, `pavucontrol`, Cava,
and mpv support audio routing, media control, visualization, and playback.

**Files and previews:** Yazi, Thunar, Xarchiver, `ffmpegthumbnailer`,
Poppler, and ImageMagick support browsing, archives, and previews. See
[Files](files.md).

**Optional desktop apps:** Zen Browser, Neovim, sxiv, Discord, Lutris, Docker,
and Safe Eyes cover browsing, editing, images, collaboration, gaming,
development, and eye rest.

These groups support source management, hardware, capture, sessions, media,
archives, and optional desktop workflows. For launch and troubleshooting,
follow the relevant linked guide above.

The personal profile may vary by machine mode and available hardware. Optional
tools in that repository do not imply that a fresh Hornero release installs
them.

## Troubleshoot from the capability outward

When a button or key does not work, first inspect the Hornero capability and
then its host dependency:

```sh
horneroctl doctor
horneroctl apps launch --list
horneroctl config default-apps list
```

For example, the Shell can show a media control while the host has no MPRIS
player; a theme can select Papirus while its icon package is missing; and a
screenshot command can exist while its Wayland backend is absent. The status
message should identify the missing capability. Hornero does not silently
install optional programs.

## Internal implementation tools

Implementation libraries, build tools, test fixtures, and generated metadata
are documented with their owning repository rather than listed as user apps.
They are not a second package catalogue. The [architecture guide](../architecture/README.md)
describes which layer owns each product capability.
