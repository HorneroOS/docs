# Session menu

The session menu groups actions that lock or end the current desktop session.
It is part of Hornero Shell and is separate from the SDDM login screen.

## Open and navigate

Press **Super + X** to open the menu. Use **Up** and **Down** to move between
actions, **Tab** and **Shift + Tab** to move forward or backward, and
**Enter** to activate the focused action. The menu offers **Log out**,
**Shut down**, **Hibernate**, and **Restart**. The exact commands are supplied
by the active Hornero configuration, so a system may customize their behavior.

The default keyboard shortcut is configured for both the validated Hyprland
session and the experimental Niri session. User keybindings can differ; see
[Keyboard shortcuts](shortcuts.md) and
[compositor support](compositors.md) for the current support level.

## Confirm a power action

Each menu action uses a two-step confirmation. The first activation arms the
action and changes its label to **Confirm?**; activate it again while it stays
focused to run it. Moving focus away or clicking elsewhere clears the armed
state. Press **Escape** once to disarm a pending action; press it again to
close the menu. An outside click dismisses the menu where the compositor
supports that interaction.

This confirmation helps prevent an accidental key press from ending the
session. For a quick lock without opening the menu, press **Super + L**. The
[lock and login guide](../applications/login-lock.md) explains session locking
and the separate login screen.

## Configuration

The packaged configuration defines the menu's action commands, icons, and
optional session animation. Personal configuration may override these values.
Use the supported configuration paths rather than editing packaged files;
`horneroctl config paths` reports which files are active. The implementation
and interaction details live in
[Hornero Shell's session module](https://github.com/HorneroOS/shell/tree/main/modules/session)
and [interaction guide](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md).
