# Terminal and shell

Hornero separates the terminal window, the interactive shell inside it, and
the command-line tools that manage the desktop. Kitty is the selected default
terminal when installed; Alacritty and Ghostty are optional alternatives with
their own Hornero defaults. The terminal applications are separate host
packages, not dependencies of the Shell. **Super + E** opens Yazi in the
host's configured terminal, while regular terminal launches follow that same
association.

## Open a terminal

- Press **Super + T** or **Super + Enter** to open the host's XDG
  `TerminalEmulator` association through `exo-open`.
- Open the Launcher with **Ctrl + Space** and search for an installed
  terminal.
- Press **Super + E** for Yazi in a separate window from the configured
  terminal. Hornero selects Kitty by default; Alacritty and Ghostty are also
  supported. This workflow needs the selected terminal and Yazi.

Choose an installed terminal in **Settings → Terminal**. Hornero keeps the
selection aligned across the host's Xfce helper, XDG preference, and Shell
launch actions. You can inspect it with `horneroctl config default-apps list`
or change it from the CLI. Preview the change first:

```sh
horneroctl config default-apps set terminal ghostty --dry-run
horneroctl config default-apps set terminal ghostty --yes
```

Supported targets are Kitty, Alacritty, and Ghostty. The command updates the user's
`$XDG_CONFIG_HOME/xfce4/helpers.rc` and generic
`$XDG_CONFIG_HOME/xdg-terminals.list` (or the equivalent paths under
`~/.config`), while leaving MIME defaults and other helper entries alone. It
also removes a fallback exclusion for the selected terminal. When installed,
`xdg-terminal-exec` reads the generic list; a
desktop-specific preference file can take precedence. See
[Default applications](default-apps.md) and
[keyboard shortcuts](../desktop/shortcuts.md).

## Kitty

Kitty is a GPU-accelerated terminal emulator. Hornero Config provides its
system defaults under `/etc/xdg/kitty`; your user configuration at
`~/.config/kitty/kitty.conf` can override them. The defaults include a Hornero
Dark palette, font and window spacing, scrollback, and copy/paste bindings:

| Key | Action |
| --- | --- |
| `Ctrl + Shift + C` | Copy selection |
| `Ctrl + Shift + V` | Paste |
| `Ctrl + Shift + Page Up/Down` | Scroll one line |
| `Ctrl + Shift + Home/End` | Scroll to top / bottom |
| `Ctrl + L` | Clear the visible screen |

The screenshot shows Kitty running `horneroctl` appearance commands with the
current host configuration. Theme IDs shown by a specific machine can differ
from a later catalogue pin.

![Kitty displays Hornero theme IDs and wallpaper-derived color information in a styled terminal window.](/images/apps/kitty-appearance.webp)

Theme packs provide Hornero Dark, Light, and Pampa palettes. Wallpaper-derived
colors can also write a user overlay under
`~/.cache/hornero/smart-colors/colors-kitty.conf`. If Kitty reports that the
optional overlay is absent, the packaged palette still works; generate colors
from Appearance or remove only the stale include in a user override.

The public [dotfiles repository](https://github.com/ulises-jeremias/dotfiles)
adds a personal Kitty setup with an 80×24 initial window, 12-point font, and
80% background opacity. Those are workstation preferences, not a Hornero
release requirement. Edit the active `kitty.conf` to customize Kitty. See the
[Kitty manual](https://sw.kovidgoyal.net/kitty/).

## Alacritty

Alacritty is an optional terminal for users who prefer a compact TOML
configuration. When Alacritty is installed, Hornero Config supplies a system
fallback at `/etc/alacritty/alacritty.toml`. It imports the static Hornero
Dark palette and an optional generated palette, and enables live config
reload. Hornero writes the active wallpaper-derived colors to
`~/.config/alacritty/hornero-colors.toml`; applying an appearance updates this
file. If you maintain a user config at
`~/.config/alacritty/alacritty.toml`, include the Hornero palette imports there
to keep generated colors active.

The installed default uses 12-pixel window padding, 88% opacity, a 2,500-line
scrollback, and a non-blinking block cursor. The [Alacritty configuration
reference](https://alacritty.org/config-alacritty.html) documents TOML imports
and other settings.

## Ghostty

Ghostty is another optional terminal. Hornero Config provides a
`Hornero Dynamic` fallback theme under `/usr/share/ghostty/themes/` and seeds
`/etc/skel/.config/ghostty/config.ghostty` for newly created accounts. That
config selects the Hornero theme and sets 88% background opacity. Existing
accounts are not overwritten by the skeleton; add `theme = Hornero Dynamic`
to your own `~/.config/ghostty/config.ghostty` to opt in.

When an appearance is applied, Hornero writes the wallpaper-derived theme to
`~/.config/ghostty/themes/Hornero Dynamic`, which takes precedence over the
system fallback, and signals a running Ghostty instance to reload. Keep the
theme name stable in your config so subsequent appearances update it. See
Ghostty's [configuration guide](https://ghostty.org/docs/config) and
[color-theme guide](https://ghostty.org/docs/features/theme).

## Shared appearance behavior

Applying an appearance in Hornero updates the generated palette files for
Kitty, Alacritty, and Ghostty from the active wallpaper. Each emulator reads
its native format. Kitty and Alacritty have static Hornero Dark / Light
fallbacks; Ghostty has a static `Hornero Dynamic` theme fallback. These keep
the terminals usable before palette generation, while user-level files remain
yours to customize.
To inspect the generated scheme, run `horneroctl appearance colors status`.
See [Appearance](../desktop/appearance.md) for theme and palette controls.

## Shell and command workflow

Your account's configured shell runs inside the terminal. Hornero Config
does not make Zsh, a prompt, shell plugins, or aliases a system dependency.
The public dotfiles configuration optionally installs Zsh and defines a
personal profile in `~/.zshrc`, `~/.zsh/config.d/`, and related prompt files.
It enables vi-style command-line editing, reverse history search with
`Ctrl + R`, and prompt/alias loading. These personal choices do not affect
Hornero's CLI contract.

That profile also sets `$EDITOR` and `$VISUAL` to Neovim for command-line
programs. Hornero itself has no universal graphical editor default; see
[Default applications](default-apps.md). To run desktop tasks from a shell,
use [`horneroctl`](../desktop/horneroctl.md) and its installed
`--help` output.

## Optional tmux setup

The personal workstation configuration includes tmux and plugins; neither is
required by Hornero. Its configuration uses `Ctrl + A` as the primary prefix,
`Ctrl + B` as an alternate prefix, mouse support, vi-style copy-mode, and a
large scrollback history. Plugin installation depends on the optional TPM
checkout. See the [tmux manual](https://github.com/tmux/tmux/wiki) before
copying those preferences to another machine.

## When something does not open

- Run `horneroctl apps launch --list` to see which launch backends are
  available.
- Run `horneroctl apps terminal-file --help` to inspect the Yazi workflow.
- Check that the selected terminal is installed and that the
  `TerminalEmulator` helper in `~/.config/xfce4/helpers.rc` matches it.
- If a terminal's colors are stale, apply the desired appearance again in
  **Settings → Appearance** and check `horneroctl appearance colors status`.
- Check whether a user-level config overrides the Hornero system fallback.
  For Ghostty, confirm `theme = Hornero Dynamic` is present in the active
  `config.ghostty` file.

Useful references: [Kitty](https://sw.kovidgoyal.net/kitty/),
[Alacritty](https://alacritty.org/config-alacritty.html),
[Ghostty](https://ghostty.org/docs),
[Zsh manual](https://zsh.sourceforge.io/Doc/Release/),
[tmux wiki](https://github.com/tmux/tmux/wiki),
[Appearance](../desktop/appearance.md), and
[shortcuts](../desktop/shortcuts.md).
