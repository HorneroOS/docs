# Browsers, editors, and default applications

Hornero uses desktop-file and MIME associations so users can choose their
own browser, editor, PDF viewer, image viewer, video player, audio player,
and file manager. The current Hornero release does not require a specific
browser or editor package.

## How application launching works

Hyprland's default shortcuts ask `exo-open` for the XDG `TerminalEmulator`,
`FileManager`, or `WebBrowser` handler. File types such as `text/plain`,
`application/pdf`, and `image/png` use MIME associations. A missing
association or missing `.desktop` file can make a shortcut or file open fail.

The current config repository supplies an optional `handlr` configuration.
`horneroctl config default-apps list` reads the active terminal helper and
the current MIME defaults. It reports what is configured on this machine,
not what Hornero installs.

## Change a file association

Use a desktop Settings page or the CLI. First find the application's desktop
ID, usually a file under `/usr/share/applications/`, then preview and apply
the MIME change:

```sh
horneroctl config default-apps set application/pdf org.example.Reader.desktop --dry-run
horneroctl config default-apps set application/pdf org.example.Reader.desktop --yes
```

Replace the example ID with an installed `.desktop` file. The setter uses
`xdg-mime`; it only changes MIME associations. The terminal emulator is
configured separately by the desktop's `TerminalEmulator` helper, so this
command does not change **Super + T** or **Super + Enter**.

To check the selected application names and available launch backends, run:

```sh
horneroctl config default-apps list
horneroctl apps launch --list
```

## Browser and editor choices

**Super + W** launches the current `WebBrowser` handler. Hornero does not
select a universal browser. Zen Browser appears in the personal dotfiles
provisioning scripts, so it should be treated as an optional personal choice.

There is no Hornero-wide editor default. Install an editor, then set its
`.desktop` ID for `text/plain` if you want double-clicking text files to open
it. Command-line users can set `$EDITOR` in their own shell configuration;
Hornero Config does not ship a user shell startup file.

Other defaults are system choices too. Check and set the relevant MIME type
for images (`image/png`), video (`video/mp4`), audio (`audio/mpeg`), and PDF
(`application/pdf`). The Shell's MPRIS media controls are separate from the
file association used to open a media file.

For the current directory and file-manager workflow, see [Files](files.md).
For media playback controls, see [Media and audio](media-audio.md).
Upstream references: [XDG MIME applications](https://www.freedesktop.org/wiki/Specifications/mime-apps-spec/),
[exo](https://docs.xfce.org/xfce/exo/start),
[handlr-regex](https://github.com/chmln/handlr).
