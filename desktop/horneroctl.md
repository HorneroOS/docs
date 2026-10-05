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

## Edition and compositor information (Preview)

Development builds that include the edition-profile command can report the
installed composition separately from the compositor active in the current
session:

```sh
horneroctl system info
horneroctl system info --json
```

The command reads the profile record installed by a HorneroOS composition. It
reports the edition, package sets, configured compositor, maturity, and source
revision, alongside the compositor detected in the running session. It does
not infer an edition from packages that happen to be installed. Systems
without the profile record are reported as **unrecorded**. This capability is
in Preview and may not be present in the released `horneroctl` package yet.

## Configuration recovery

`horneroctl config snapshot list` shows saved snapshots. Create or restore a
snapshot only after reviewing its dry run and selecting the intended target.
`horneroctl config show <key>` reads one materialized value; `config paths`
shows which files are active.

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
