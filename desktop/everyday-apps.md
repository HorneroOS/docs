# Everyday apps and file workflows

Hornero's factory configuration declares default applications for the file
manager, terminal, browser, editor, image viewer, media, and PDF roles. The
actual installed applications depend on the package composition of the Arch
system; Hornero does not yet provide a supported end-to-end installer.

Check the current associations with:

```sh
horneroctl config default-apps list
horneroctl apps launch --list
```

## Open files and folders

The default file manager opens from the desktop with **Super + F**. The
terminal file browser opens with **Super + E**. To open them without their
shortcuts:

```sh
horneroctl apps files
horneroctl apps terminal-file
```

The terminal file browser accepts an initial directory or file selection.
Read its options before scripting or opening a path:

```sh
horneroctl apps terminal-file --help
horneroctl apps terminal-file --cheatsheet
```

For the current terminal, browser, and editor associations, use the default
application list rather than assuming that a particular personal app is
installed.

## Launch apps

Open the application launcher with **Ctrl + Space**. The CLI can open it or
report the available launch backends:

```sh
horneroctl apps launch
horneroctl apps launch --list
```

Use the desktop shortcut table for window and workspace actions:
[Keyboard shortcuts](shortcuts.md).

## Change an association

Hornero currently exposes the factory associations as a read-only list.
Changing a desktop-file association through `horneroctl` is not implemented
yet. Use the desktop's standard file-association settings or the application
itself, and check the current CLI help before relying on a future management
command.
