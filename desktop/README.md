# Use the desktop

Hornero's desktop is built around the Quickshell session. A bar or rail gives
quick access to workspaces and shell actions; the launcher opens apps and
commands; the Dashboard brings together desktop summaries; and the Control
Center contains persistent system and shell settings.

## Find a task

| Task | Guide |
| --- | --- |
| Pick a coordinated look | [Themes and appearance](appearance.md) |
| Change or understand a wallpaper | [Wallpapers and color](wallpapers.md) |
| Move between rails, bars, islands, or docks | [Layouts](layouts.md) |
| Use the keyboard efficiently | [Shortcuts](shortcuts.md) |
| Open files or launch applications | [Everyday apps](everyday-apps.md) |
| Learn how the configured applications fit together | [Apps and workflows](../applications/README.md) |
| Open a Settings page or automate a change | [horneroctl](horneroctl.md) |

## Desktop surfaces

- **Launcher** searches applications and offers shell actions.
- **Dashboard** collects useful desktop information without replacing
  dedicated applications.
- **Control Center** groups connectivity, media, appearance, shell, and system
  controls.
- **Layout Picker** previews bar topology before a layout is selected.
- **Notifications, OSD, and session menu** have different jobs: notifications
  keep actionable events, the OSD echoes short-lived hardware changes, and the
  session menu contains lock and power actions.
- **Companion** is a small shell character, not a source of system activity.

These surfaces are part of the shell package. Their implementation and
keyboard focus contracts live in the [Shell repository](https://github.com/HorneroOS/shell/tree/main/docs).

## Configuration boundaries

Use Control Center for supported interactive settings and `horneroctl` for
scripts and diagnostics. `horneroctl config paths` reports which user files
are active; `horneroctl config validate` checks the materialized shell config.
The [configuration repository](https://github.com/HorneroOS/config) owns
factory defaults. Keep personal changes under your user configuration rather
than editing packaged files.
