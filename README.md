# Hornero OS documentation

Find a guide by the task you are trying to complete. This repository is the
user and contributor handbook; implementation contracts stay with the
[Shell](https://github.com/HorneroOS/shell), [CLI](https://github.com/HorneroOS/hornero),
and [configuration](https://github.com/HorneroOS/config) repositories.

> Hornero OS is an Arch-based desktop project in development. There is no
> installable ISO or supported system installer yet. The
> [release page](https://horneroos.org/releases) and
> [installation status](https://github.com/HorneroOS/website/blob/main/src/pages/install.astro)
> are the current
> source for what can be installed.

## Choose a path

| If you want to… | Start here |
| --- | --- |
| Understand release and installation status | [Getting started](getting-started/README.md) |
| Use the desktop, apps, and Control Center | [Desktop](desktop/README.md) |
| Change themes, colors, or wallpaper | [Appearance](desktop/appearance.md) · [Wallpapers](desktop/wallpapers.md) |
| Choose a bar arrangement | [Layouts](desktop/layouts.md) |
| Find a keyboard shortcut | [Shortcuts](desktop/shortcuts.md) |
| Automate or inspect the system from a terminal | [horneroctl](desktop/horneroctl.md) |
| Diagnose graphics or device problems | [Hardware](hardware/README.md) · [Troubleshooting](troubleshooting/README.md) |
| Understand system boundaries | [Architecture](architecture/README.md) |
| Build, test, or contribute | [Development](development/README.md) |

## How these docs stay accurate

Steps describe behavior available in the released product unless they are
labelled **Development** or **Preview**. Package, installer, and release
availability can change; check the live release and installation pages before
following older notes. Commands are taken from `horneroctl` help and current
product configuration. Personal machine examples from the former dotfiles
wiki are not system requirements.

The website imports these Markdown pages at a reviewed commit and adds its own
navigation, search, and responsive presentation. This repository owns the
content; the website does not maintain a second copy.

## Areas

- [Getting started](getting-started/README.md) — release status and a safe
  first look.
- [Desktop](desktop/README.md) — appearance, wallpaper, layouts, and shortcuts.
- [horneroctl](desktop/horneroctl.md) — supported command-line entry points.
- [Hardware](hardware/README.md) — device diagnostics and graphics guidance.
- [Troubleshooting](troubleshooting/README.md) — recover from common failures.
- [Architecture](architecture/README.md) — ownership and data flow.
- [Development](development/README.md) — code, QA, and contribution paths.

## License

[MIT](LICENSE).
