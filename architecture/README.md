# Architecture

Hornero is a set of collaborating repositories with explicit ownership. The
full system is still in development; no single repository is an installable
operating system. The [release ledger](https://github.com/HorneroOS/hornero/releases)
records which component revisions were composed together.

## Where a change belongs

| Repository | Owns |
| --- | --- |
| [hornero](https://github.com/HorneroOS/hornero) | V-based system CLI, capability entry points, and release composition |
| [config](https://github.com/HorneroOS/config) | Factory defaults, package metadata, theme packs, and generated catalogues |
| [shell](https://github.com/HorneroOS/shell) | Quickshell UI and live session services: bars, launcher, Dashboard, Settings, notifications, lock, and appearance |
| [greeter](https://github.com/HorneroOS/greeter) | SDDM theme, Qt/QML assets, and package validation |
| [qa](https://github.com/HorneroOS/qa) | Isolated graphical acceptance runs and evidence |
| [docs](https://github.com/HorneroOS/docs) | This user and contributor handbook |
| [website](https://github.com/HorneroOS/website) | Public product presentation and the rendered view of this handbook |

## Guides

- [Editions and package composition](editions.md) — the shared catalogue,
  composition model, and honest maturity boundary.
- [Appearance system](appearance-system.md) — theme, wallpaper, palette, and
  toolkit responsibilities.
- [Updates and delivery](updates-delivery.md) — how source, packages, and
  tested compositions relate.
- [Power and performance](power-performance.md) — measurement and current
  reference data.

Detailed contracts stay close to their implementation: see the Shell
[architecture](https://github.com/HorneroOS/shell/blob/main/docs/ARCHITECTURE.md),
[layout](https://github.com/HorneroOS/shell/blob/main/docs/LAYOUTS.md), and
[focus](https://github.com/HorneroOS/shell/blob/main/docs/FOCUS.md) documents.
