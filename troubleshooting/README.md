# Troubleshooting

Start with read-only diagnostics. Record the exact error and the steps that
reproduce it before changing configuration or reinstalling packages.

```sh
horneroctl doctor
horneroctl config validate
horneroctl shell status --json
horneroctl appearance doctor
```

## The shell is missing or not responding

Check whether Quickshell is reachable, then read its recent log:

```sh
horneroctl shell status --json
horneroctl shell logs --lines 120
```

If the log reports a missing QML module or plugin, record the package versions
and the first import/load error. Do not repeatedly restart the graphical
session. See the [Shell troubleshooting notes](https://github.com/HorneroOS/shell/blob/main/README.md#troubleshooting)
and [report a reproducible issue](../development/README.md#report-a-bug).

## Settings or a pane appears empty

Validate the materialized configuration, read the Shell log, and reopen the
specific pane from the Control Center. Include the pane name and whether it
was opened through the sidebar or a deep link. Avoid deleting user settings:

```sh
horneroctl config validate
horneroctl shell logs --lines 120
horneroctl config gui --pane appearance
```

If another pane works but one is blank, report it as a pane-load failure.

## Theme and wallpaper do not agree

Read live state before applying another look:

```sh
horneroctl appearance status --json
horneroctl appearance theme get
horneroctl appearance gtk current
horneroctl appearance gtk current-icon
horneroctl wallpaper current
horneroctl appearance doctor
```

An image named by a theme manifest may not be installed locally. Choose a
local wallpaper and check installed GTK and icon themes before treating an
external dependency as a shell failure. See [Appearance](../desktop/appearance.md)
and [Wallpapers](../desktop/wallpapers.md).

## Network and Bluetooth

Check that the adapter is visible to the operating system, then open the
matching Control Center pane. A missing adapter is below the shell layer;
collect `lspci -nnk`, `lsusb`, and the relevant kernel log lines before
reporting it. These commands only inspect devices.

## Display and graphics

Check the monitor list and loaded kernel driver:

```sh
hyprctl monitors -j
lspci -nnk
journalctl -b -k -p warning
```

For NVIDIA or hybrid graphics, follow the device-specific
[hardware guidance](../hardware/README.md#nvidia-and-hybrid-graphics). A
black screen or failed session before the shell starts is not a Control
Center problem.

## Login screen

For an SDDM login-screen failure, gather the installed package and selected
theme plus the current boot log:

```sh
pacman -Q sddm hornero-greeter
journalctl -b -u sddm --no-pager
```

The [Hornero greeter repository](https://github.com/HorneroOS/greeter) owns
the theme and packaging contract. Do not restart SDDM during a graphical
session merely to test a theme.

## Include this in a bug report

- Relevant repo and component version.
- What you expected and what happened.
- The smallest repeatable sequence of actions.
- The first relevant error lines, with personal identifiers removed.
- A screenshot only when it contains no private windows or notifications.

See [how to report a bug](../development/README.md#report-a-bug) for the
repository issue links and information to include.
