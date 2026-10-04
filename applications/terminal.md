# Terminal and shell

The terminal is the entry point for commands and text-based workflows. The
current Shell config names `foot` as its terminal app preference, while the
Hyprland shortcuts ask `exo-open` for the desktop's `TerminalEmulator`
association. Kitty defaults are also supplied by Hornero Config as an
optional package payload. Your installed desktop association decides what
opens from **Super + T** or **Super + Enter**.

## Open a terminal

- Press **Super + T** or **Super + Enter** to launch the XDG
  `TerminalEmulator` handler through `exo-open`.
- Open the application launcher with **Ctrl + Space** and search for a
  terminal installed on the host.
- **Super + E** opens the Yazi file manager in a Kitty popup. This shortcut
  directly invokes Kitty, so installing only a different terminal does not
  satisfy that particular shortcut.

See [default applications](default-apps.md) to inspect terminal and MIME
associations. Hornero Config supplies Kitty's base config and dark palette as
an optional package payload. Theme application can select a matching Kitty
palette when Kitty is installed.

The configured Xfce helper file is `~/.config/xfce4/helpers.rc`. Use the
desktop's preferred-applications tool to change the terminal target. The
`horneroctl config default-apps set` command changes MIME associations, not
the `TerminalEmulator` helper.

## Kitty configuration

Kitty reads `~/.config/kitty/kitty.conf`. Hornero Config materializes system
defaults under `/etc/xdg/kitty`; user files override those defaults. The
configuration includes the current Hornero Dark palette, copy/paste and
scrollback bindings, font settings, and window padding. Theme-specific files
include the Hornero Light and Pampa palettes.

The optional generated-color overlay lives under
`~/.cache/hornero/smart-colors/`. If Kitty warns that the include is missing,
the base palette still works; generate colors from Appearance or remove the
include from your user override if you do not use generated palettes.

Kitty's upstream manual has the complete option reference:
[kitty documentation](https://sw.kovidgoyal.net/kitty/).

## Interactive shell

Hornero Config does not define a user-wide interactive Zsh environment.
Zsh, prompt themes, aliases, plugin managers, and shell startup files are
personal choices. The
[dotfiles repository](https://github.com/ulises-jeremias/dotfiles) has
historically provisioned Zsh, but that does not make its prompt or aliases a
Hornero default.

Use the shell already configured for your account. A terminal emulator
launches that account shell unless its application command overrides it.
For shared command-line desktop operations, use [horneroctl](../desktop/horneroctl.md)
and inspect `horneroctl --help` for the installed version.

Useful links: [Zsh manual](https://zsh.sourceforge.io/Doc/Release/),
[Kitty shortcuts](../desktop/shortcuts.md), [themes and appearance](../desktop/appearance.md).
