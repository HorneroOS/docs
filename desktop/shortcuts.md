# Keyboard shortcuts

`Super` means the Windows/Meta key. The configured bindings can vary with the
release and user configuration; this quick reference follows the current
Hornero Hyprland defaults. Open the built-in help with **Super + /**, or ask
the CLI to show it with `horneroctl hardware keyboard keys`.

## Shell and applications

| Shortcut | Action |
| --- | --- |
| `Ctrl + Space` | Open the application launcher |
| `Super + D` | Open the Dashboard |
| `Super + Shift + B` | Open the Layout Picker |
| `Super + X` | Open the session and power menu |
| `Super + V` | Open clipboard history |
| `Super + E` | Open the terminal file manager |
| `Super + F` | Open the graphical file manager |
| `Super + T` or `Super + Enter` | Open a terminal |
| `Super + W` | Open the browser |
| `Super + L` | Lock the session |
| `Print` / `Shift + Print` | Capture the screen / choose an area |

## Windows and workspaces

| Shortcut | Action |
| --- | --- |
| `Super + H/J/K/L` or arrow keys | Focus a neighboring window |
| `Super + Shift + H/J/K/L` or arrow keys | Move the focused window |
| `Super + Space` | Toggle floating for the focused window |
| `Super + M` | Toggle fullscreen |
| `Super + Shift + M` | Toggle maximize |
| `Super + Shift + Q` | Close the focused window |
| `Super + R` | Enter resize mode; use H/J/K/L or arrows, then Escape |
| `Super + 1…9, 0` | Switch to workspace 1…10 |
| `Super + Shift + 1…9, 0` | Move the focused window to workspace 1…10 |
| `Super + Tab` / `Super + Shift + Tab` | Move to next / previous workspace |
| `Super + S` | Toggle the scratch workspace |
| `Super + O` | Workspace overview (optional plugin) |

In the scrolling window layout, `Super + Alt + H/L` moves across
columns;
`Super + Alt + -/=` changes the active column width. The
[Shell interaction guide](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md)
has the detailed movement contract.

## Hardware keys

Media keys control playback, volume keys change output volume, and microphone
mute toggles the default source. Brightness keys change the display by 10%;
hold Shift for 1% steps. These keys depend on hardware and the active backend.

## Recovery and caution

Press Escape to leave the resize mode or a shell overlay. `Super + Shift + R`
reloads the compositor configuration. **`Super + Shift + E` exits Hyprland**;
do not use it as a routine close-window shortcut.

For current bindings and keyboard-layout status:

```sh
horneroctl hardware keyboard keys
horneroctl hardware keyboard layout --current
```

The source of truth is
[HorneroOS/config's keybinding file](https://github.com/HorneroOS/config/blob/main/desktop/hypr/hyprland.conf.d/keybindings.conf).
