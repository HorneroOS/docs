# Browsing, editing, and documents

Hornero does not require a particular browser, graphical editor, image viewer,
or PDF reader. It asks the desktop's XDG application registry to open a web
link or file, so you can choose the tools that suit your work.

## Browsing

Press **Super + W** to open the host's `WebBrowser` handler. The browser is
selected by the desktop environment; Hornero Config does not install or set a
universal browser. The public [dotfiles repository](https://github.com/ulises-jeremias/dotfiles)
can install Zen Browser on a personal Arch workstation, but that is an
optional personal choice.

If a link does nothing, check that a browser package is installed, that it
provides a desktop entry under `/usr/share/applications/`, and that an XDG
`WebBrowser` handler is selected. `horneroctl config default-apps list`
reports the currently visible desktop handlers. Browser privacy, sync, and
profile settings belong to the browser you choose.

Upstream examples: [Firefox](https://support.mozilla.org/products/firefox),
[Zen Browser](https://docs.zen-browser.app/).

## Editors

There is no Hornero-wide graphical editor. Install the editor you prefer and
select its desktop entry for `text/plain`. Shell programs use `$EDITOR` or
`$VISUAL` only when those environment variables are set. The personal dotfiles
Zsh profile sets both to `nvim`; Hornero does not set that value globally.

Check an editor's desktop entry before changing the association:

```sh
horneroctl config default-apps list
horneroctl config default-apps set text/plain org.example.Editor.desktop --dry-run
horneroctl config default-apps set text/plain org.example.Editor.desktop --yes
```

Replace `org.example.Editor.desktop` with an installed desktop-file ID. The
command updates that MIME association; it does not set a terminal editor for
every shell or application. See the
[Neovim user manual](https://neovim.io/doc/user/) if using the personal
workstation profile.

## PDFs, images, and media files

Double-clicking a PDF, image, audio file, or video uses its MIME association.
The file opener is independent of the Shell's media controls. A host may use
different programs for image formats or media types; Hornero does not assume
one package. `poppler` and ImageMagick can support file previews, but neither
is a graphical PDF or image viewer.

When a type opens in the wrong program, inspect the association rather than
changing the media controls:

```sh
xdg-mime query default application/pdf
xdg-mime query default image/png
xdg-mime query default video/mp4
xdg-mime query default audio/mpeg
```

If the result names an application that is not installed, install or choose a
valid desktop entry, then set the relevant MIME type with
[`horneroctl config default-apps`](default-apps.md). Yazi's personal workflow
can open video in `mpv` when it is installed; this does not define the system
default player.

For archive handling and file previews, see [Files](files.md). For active
playback controls and audio routing, see [Media and audio](media-audio.md).
The [XDG MIME Applications specification](https://specifications.freedesktop.org/mime-apps-spec/latest/)
describes the desktop association model.
