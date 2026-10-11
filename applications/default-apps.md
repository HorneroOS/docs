# Default applications

Hornero uses desktop-file and MIME associations so users can choose their
own browser, editor, PDF viewer, image viewer, video player, audio player,
and file manager. The current Hornero release does not require a specific
browser, editor, image viewer, PDF reader, or media player. See
[Browsing, editing, and documents](browsing-documents.md) for practical
examples and package distinctions.

## How application launching works

The active compositor's default shortcuts ask `exo-open` for the XDG
`TerminalEmulator`, `FileManager`, or `WebBrowser` handler. File types such as
`text/plain`, `application/pdf`, and `image/png` use MIME associations. A
missing association or missing `.desktop` file can make a shortcut or file
open fail.

The current config repository supplies an optional `handlr` configuration.
`horneroctl config default-apps list` reads the Exo terminal helper, the
generic XDG terminal preference, and the current MIME defaults. It reports
what is configured on this machine, not what Hornero installs. A
desktop-specific `<desktop>-xdg-terminals.list` can override the generic XDG
preference for a particular session.

## Change a file association

Use a desktop Settings page or the CLI. First find the application's desktop
ID, usually a file under `/usr/share/applications/`, then preview and apply
the MIME change:

```sh
horneroctl config default-apps set application/pdf org.example.Reader.desktop --dry-run
horneroctl config default-apps set application/pdf org.example.Reader.desktop --yes
```

Replace the example ID with an installed `.desktop` file. MIME changes use
`xdg-mime`. To change the terminal used by **Super + T** or **Super + Enter**,
set the terminal preference:

```sh
horneroctl config default-apps set terminal ghostty --dry-run
horneroctl config default-apps set terminal ghostty --yes
```

The terminal setter supports Kitty, Alacritty, and Ghostty, and requires the
chosen program to be installed. It keeps Exo's `TerminalEmulator` helper and
the generic `$XDG_CONFIG_HOME/xdg-terminals.list` preference (or
`~/.config/xdg-terminals.list`) aligned. Existing helper entries, comments,
directives, and other terminal choices remain in place; a fallback exclusion
for the selected terminal is removed so it can be selected. The selected
terminal takes first priority in the XDG list. When installed,
`xdg-terminal-exec` reads that preference. Desktop-specific preference files
can still take precedence. `--dry-run` reports both target paths without writing;
`--yes` is required to apply.

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

The MIME association applies to files opened from file managers and other
XDG-aware applications. It does not change which program the Shell's MPRIS
controls target or which terminal starts a shell.

For the current directory and file-manager workflow, see [Files](files.md).
For media playback controls, see [Media and audio](media-audio.md), and for
more application-specific guidance see
[Browsing, editing, and documents](browsing-documents.md).
Upstream references: [XDG MIME applications](https://www.freedesktop.org/wiki/Specifications/mime-apps-spec/),
[exo](https://docs.xfce.org/xfce/exo/start),
[XDG default terminal execution](https://github.com/Vladimir-csp/xdg-terminal-exec),
[handlr-regex](https://github.com/chmln/handlr).
