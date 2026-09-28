# Updates and delivery

How a change in a HorneroOS repo reaches a running machine, and the
contract that keeps a user's install a mirror of the repos. Read this
before adding a config file, a `shell.json` key, or anything a user
must receive.

## Two lanes, and why

HorneroOS owns its own layer and nothing under it. Two update lanes,
deliberately separate:

| Lane | Command | What moves |
|---|---|---|
| **Hornero** | `horneroctl` verbs | presets, appearance, snapshots, backups |
| **Distro** | `sudo pacman -Syu` | base system and kernel, from Arch |

`horneroctl package upgrade` moves the Hornero set; it never decides
when your box changes kernel. Every lane reports what the other is
holding (`horneroctl package check`, `horneroctl doctor`), so a box
that cannot take a system upgrade today can still take a Hornero fix,
and the reverse.

## How a change reaches a machine

```text
repo (source of truth)
  |-- hornero:  tag -> release manifest -> AUR (horneroctl-bin) -> user box
  |-- config:   package -> /usr/share/hornero/* + /etc/xdg/* -> materialize -> ~/.config
  |-- shell:    package -> quickshell tree -> `horneroctl shell restart --yes`
  `-- greeter:  package -> SDDM theme dir
```

- A **dev box** runs checkouts: the shell from a clone, configs
  materialized from `config/scripts/materialize.sh`.
- A **user box** runs packages: `horneroctl` from AUR, defaults from
  `/usr/share/hornero` and `/etc/xdg`.
- They must converge: a change that lands on one but not the other is
  the bug this page exists to prevent.

## User edits survive updates

Shipped files are never the user's notepad:

- The shell user file (`~/.config/hornero/shell.json`) is created by
  the shell runtime, never shipped; a preset apply deep-merges into it
  and live-reloads.
- `horneroctl config snapshots` / `backup create` capture the user
  layer before risky changes; `backup restore` puts it back.
- Removing or renaming a shipped key needs a migration path, not a
  silent drop (see `horneroctl migrate`, `config/tests/test_migrate.sh`).

## Gates that enforce it

| Gate | Where | What it proves |
|---|---|---|
| `horneroctl doctor` | user box | read-only health: environment, paths, drift |
| `config validate` | CI + box | syntax, data guard, shortcuts |
| bind audit | dotfiles CI | every `horneroctl` call in configs resolves |
| delivery check | dotfiles CI | every repo file reaches the live box |

The implementing repos own the details: [HorneroOS/hornero][hornero]
(CLI, releases), [HorneroOS/config][config] (defaults, packaging).

[hornero]: https://github.com/HorneroOS/hornero
[config]: https://github.com/HorneroOS/config
