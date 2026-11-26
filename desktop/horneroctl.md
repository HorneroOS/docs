# `horneroctl`

`horneroctl` is Hornero's command-line interface for system capabilities,
desktop settings, diagnostics, and scripts. Use it when you want repeatable
commands or need to inspect state without opening a settings page.

Start with the help for the command you need:

```sh
horneroctl --help
horneroctl appearance --help
horneroctl appearance theme --help
```

Use `--json` for machine-readable output. Read-only commands do not need
confirmation. For a change, inspect the dry run and then pass `--yes`:

```sh
horneroctl shell preset apply cockpit --dry-run
horneroctl shell preset apply cockpit --yes
```

## Command groups

`horneroctl` organizes its subcommands into 27 top-level groups:

- `agent` — manage local AI coding agents, defaults, config, and usage
  (`horneroctl agent list`).
- `appearance` — themes, Chromatic palettes, GTK/Qt sync, night mode, and
  colors (`horneroctl appearance status --json`).
- `apps` — app launcher, switcher, git-status watcher, toggles, and
  performance (`horneroctl apps toggle launcher`).
- `assistant` — Hornero assistant gateway, sessions, tools, policy, and
  prompts (`horneroctl assistant status`).
- `backup` — create, list, restore, and schedule user backups
  (`horneroctl backup list`).
- `bluetooth` — inspect and control Bluetooth state
  (`horneroctl bluetooth`).
- `capture` — screenshots, screen recording, and clipboard capture
  (`horneroctl capture status`).
- `completion` — generate shell completion scripts for `bash`, `fish`, and
  `zsh` (`horneroctl completion bash`).
- `config` — Control Center GUI, paths, validation, snapshots, and default
  apps (`horneroctl config validate`).
- `doctor` — run system and session health checks (`horneroctl doctor`).
- `gaming` — Gaming edition diagnostics, launch options, and selections
  (`horneroctl gaming doctor`).
- `github` — GitHub inbox, status, stats, and export
  (`horneroctl github status`).
- `hardware` — battery, brightness, keyboard, microphone, and network
  controls (`horneroctl hardware battery status`).
- `help` — print CLI help for any command group (`horneroctl help`).
- `hypr` — Hyprland animations, cursor, input, layouts, monitors, and
  plugins (`horneroctl hypr monitors list`).
- `lock` — lock screen control and status (`horneroctl lock status`).
- `mode` — switch or inspect desktop experience modes
  (`horneroctl mode list`).
- `package` — query repository/AUR updates, dependencies, and upgrades
  (`horneroctl package check`).
- `plugin` — browse PluginKit catalog, enable/disable, or scaffold plugins
  (`horneroctl plugin catalog`).
- `power` — lock, logout, suspend, reboot, shutdown, and power status
  (`horneroctl power status`).
- `recovery` — read-only snapshot and recovery readiness diagnostics
  (`horneroctl recovery doctor`).
- `shell` — start, stop, restart, inspect logs, IPC, and bar presets
  (`horneroctl shell status`).
- `studio` — Studio audio profiles, jobs, modes, apps, and diagnostics
  (`horneroctl studio doctor`).
- `system` — installed edition profile and active compositor info
  (`horneroctl system info`).
- `version` — print the `horneroctl` version (`horneroctl version`).
- `wallpaper` — inspect or change the active wallpaper
  (`horneroctl wallpaper current`).
- `welcome` — open, reset, or configure the Welcome Center on login
  (`horneroctl welcome status`).

Run `horneroctl <group> --help` to inspect every subcommand and flag in a
group.

## Open a Settings page

The CLI can open Control Center directly to a pane:

```sh
horneroctl config gui
horneroctl config gui --pane appearance
horneroctl config gui --pane network
```

Pane IDs come from the Shell's
[pane registry](https://github.com/HorneroOS/shell/blob/main/modules/controlcenter/PaneRegistry.qml);
examples above use `appearance` and `network`. If a destination cannot open,
run the corresponding CLI command directly; see `horneroctl <command> --help`.

## Useful commands

| Need | Command |
| --- | --- |
| Check the runtime environment | `horneroctl doctor` |
| See resolved config and state paths | `horneroctl config paths` |
| Validate the shell configuration | `horneroctl config validate` |
| See active theme and appearance | `horneroctl appearance status --json` |
| Check theme consistency | `horneroctl appearance doctor` |
| List installed themes | `horneroctl appearance theme list` |
| Find the current wallpaper | `horneroctl wallpaper current` |
| List and inspect shell presets | `horneroctl shell preset list --full` |
| Read Shell logs | `horneroctl shell logs --lines 100` |
| Read current key bindings | `horneroctl hardware keyboard keys` |

![A terminal showing doctor output: fourteen checks listed with OK
marks, covering the Wayland session, the selected terminal, the shell
configuration paths and the Qt themes, ending with "all 14 checks
passed".](https://www.horneroos.com/captures/cap-term-04.png)

*Example `doctor` output on the maintainer's machine — the paths shown
are that machine's home directory; yours will differ. Capture,
19 November 2026.*

## Check for updates

AUR-aware update checks report repository packages through `checkupdates` and
AUR packages through `yay -Qua` or `paru -Qua` when one of those helpers is
installed. These checks only query package state; they do not install or
upgrade packages. The AUR query has a 30-second limit.

```sh
horneroctl package check
horneroctl package updates --json
horneroctl package check --dry-run
```

`package check` lists each source separately. `package updates` includes a
combined `count`, plus `repository_count`, `aur_count`, and `aur_status` in
JSON output. If neither `yay` nor `paru` is available, repository results
remain available and the AUR lane is explicitly marked as unchecked. A dry run
shows which commands would run without invoking either query. A full system
upgrade is a separate, explicit operation: `horneroctl package upgrade`.

## Edition and compositor information

`horneroctl system info` reports the installed composition separately from
the compositor active in the current session:

```sh
horneroctl system info
horneroctl system info --json
```

The command reads the profile record installed by a HorneroOS composition. It
reports the edition, package sets, configured compositor, maturity, and source
revision, alongside the compositor detected in the running session. It does
not infer an edition from packages that happen to be installed. Systems
without the profile record are reported as **unrecorded**.

## Updates and recovery readiness

There is no HorneroOS system rollback today, and no command creates
or restores an operating-system snapshot. `horneroctl package
upgrade --yes` is a full system upgrade with no snapshot step. The
only recovery subcommand is read-only:

```sh
horneroctl recovery doctor
horneroctl recovery doctor --json
```

It probes the shipped snapshot backend (currently `none`), the root
filesystem, the `/.snapshots` store, snapper and its timers.
Readiness is not proof that a restore works. See
[Updates and recovery: no system rollback yet](updates-and-rollback.md).

## Configuration recovery

`horneroctl config snapshot list` shows saved snapshots. Create or restore a
snapshot only after reviewing its dry run and selecting the intended target.
`horneroctl config show <key>` reads one materialized value; `config paths`
shows which files are active. A configuration snapshot archives
Hornero settings only; it is never a system snapshot or an OS
rollback.

The CLI does not rewrite data from another product or a retired path
namespace. To recover a broken Hornero configuration, inspect
`horneroctl config paths`, use a reviewed snapshot, or reset the specific
user-owned file described by the relevant settings page.

## Scripting

Prefer structured output and explicit checks over parsing display text:

```sh
horneroctl appearance status --json
horneroctl shell preset current --json
```

Treat non-zero exit status as failure. The CLI verifies live state for
multi-part appearance changes; a partial apply is reported as an error so a
script can stop and recover. The
[HorneroOS/hornero repository](https://github.com/HorneroOS/hornero) owns the
command implementation and detailed contracts.
