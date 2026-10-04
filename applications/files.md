# Files and folders

Hornero supports a graphical file manager and a terminal file browser. They
serve different tasks and share the same files on disk.

## Thunar for visual file management

Press **Super + F** to open the host's XDG `FileManager` association through
`exo-open`. Thunar is the curated graphical file manager in the current
dotfiles setup and has Hornero Config defaults for accelerators and bulk
rename. Its configuration is under `~/.config/Thunar/`; packaged system
defaults are under `/etc/xdg/Thunar/`. The personal dotfiles setup adds two
Thunar custom actions. The `hornero-config` package omits `uca.xml` because
the Thunar package already owns that system path.

When Thunar is installed, the session starts its daemon to make later windows
open faster. The dotfiles context menu includes **Open in Yazi** and **Open
Terminal Here**. Those actions require the corresponding program and a
working terminal association.

Upstream: [Thunar documentation](https://docs.xfce.org/xfce/thunar/start).

## Yazi for keyboard-driven browsing

Press **Super + E** to open Yazi in a Kitty popup. The current shortcut calls
`horneroctl apps terminal-file --last-dir`; the CLI can also open a directory
or selected file directly:

```sh
horneroctl apps terminal-file --help
horneroctl apps terminal-file --cheatsheet
horneroctl apps terminal-file --path ~/Downloads
```

The Hornero Config package lists Kitty as an optional package and does not
declare Yazi. Both must be present for the keybinding. The personal dotfiles
setup installs Yazi and its preview helpers, but those optional packages
are not part of the HorneroOS release profile.

Yazi keybindings can be queried from the CLI cheatsheet. Preview support
depends on optional host tools such as `ffmpegthumbnailer`, `poppler`, and
ImageMagick. A missing preview does not mean the file is missing. Yazi
upstream: [Yazi documentation](https://yazi-rs.github.io/docs/).

## File opening and archives

`exo-open` launches the default file manager and terminal. `handlr` and
`xdg-mime` resolve MIME associations, such as which app opens a PDF or image.
Thunar delegates archive operations to compatible archive utilities and
plugins installed on the host. Yazi has its own archive actions when the
required tools are installed.

Inspect the current directory handler with:

```sh
horneroctl apps files --info
horneroctl config default-apps list
```

Change a file association using the instructions in
[Default applications](default-apps.md). Hornero does not install or silently
download archive or preview dependencies.
