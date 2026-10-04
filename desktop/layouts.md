# Bar layouts

Layouts change where desktop bars, rails, and docks sit. They do not change
the window arrangement: that is controlled by the compositor's window-layout
profile. This keeps two useful choices separate — **where shell controls
live** and **how windows are arranged**.

Open the Layout Picker with **Super + Shift + B**. Its topology previews show
whether a preset uses a side rail, one or two horizontal bars, clear surfaces,
separate islands, or a dock. Select a preview to apply it; use Escape to leave
without applying.

## Presets

Hornero currently ships fifteen presets:

| Family | Presets |
| --- | --- |
| Rails | Hornero Left, Hornero Right, Minimal Left |
| Horizontal bars | Minimal Top, Classic Top, Classic Bottom, Productivity |
| Multi-surface | Cockpit, Cockpit Clear, Horizon, Islands, Cozy Minimal |
| Floating and docked | Floating Island, Dock Bottom, Gaming |

The current [Layouts page](https://github.com/HorneroOS/website/blob/main/src/pages/layouts.astro)
shows real captures and short descriptions. Polybar and Waybar influenced
some topologies; the current shell uses one Quickshell layout system rather
than separate historical bar implementations.

## Apply from a terminal

Use the CLI to list the available presets and inspect the current choice:

```sh
horneroctl shell preset list --full
horneroctl shell preset current
horneroctl shell preset apply cockpit-clear --dry-run
horneroctl shell preset apply cockpit-clear --yes
```

Applying a preset replaces the settings that the preset owns. It keeps
unrelated shell preferences. Keep personal edits in the user configuration,
not inside a package-owned preset.

## When a bar covers a window

Attached bars and docks reserve edge space. Floating surfaces normally
overlay the desktop; some presets explicitly reserve space to preserve
readability. Try another preset before editing geometry. For the schema,
edge behavior, entry options, per-monitor settings, and compatibility rules,
see the [layout contract in the Shell repository](https://github.com/HorneroOS/shell/blob/main/docs/LAYOUTS.md).
