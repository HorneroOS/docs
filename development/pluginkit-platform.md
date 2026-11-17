# PluginKit 4: the extension platform

**Development.** PluginKit 4 turns Hornero Shell extensions from "a widget in
a few places" into a platform: an extension contributes to named surfaces
through typed contracts, with settings the Control Center renders for it. The
design authority is [RFC 0003](rfc-0003-pluginkit-contribution-surfaces.md);
the normative contract is `docs/PLUGINS.md` in `HorneroOS/shell`. This page is
the author-facing tour. Status: the Shell changes are in review at the time of
writing; nothing here is on a released Shell until its pull requests merge.

## What a package can contribute

- **Desktop widget, bar item, dashboard card** — Declared in:
  `surfaces.desktop` / `bar` / `dashboard`; Where it shows up: the desktop
  layer, the bar, the dashboard
- **Several instances of one desktop widget** — Declared in:
  `surfaces.desktop.instances`; Where it shows up: the desktop; each instance
  has its own settings, position and size
- **Commands** — Declared in: `contributes.commands` + `surfaces.commands`;
  Where it shows up: the launcher (`>do`), `qs ipc call plugincommands`, key
  bindings you own
- **Quick-setting tile** — Declared in: `contributes.quickSettings` +
  `surfaces.quickSetting`; Where it shows up: the Utilities quick toggles,
  once the person adds it
- **Control Center panel** — Declared in: `contributes.panels` +
  `surfaces.panel`; Where it shows up: Control Center › Extensions, loaded
  only while open
- **Typed settings** — Declared in: `capabilities.settings`; Where it shows
  up: generated controls in Control Center, with a live preview

Everything that can be shown without running extension code (names, glyphs,
settings, command lists) is declared in `manifest.json`; code is loaded lazily,
per surface. A package that uses any PluginKit 4 feature declares
`"pluginKit": 4`; the validator refuses a package that under-declares, and an
older Shell refuses a package that needs more than it has.

## Settings that draw themselves

Besides boolean, integer, number, string and enum, PluginKit 4 adds `colour`,
`list` (multi-select), `strings` (free list), `text` (multi-line) and `path`
(a string the Shell never opens), and the display fields `title`, `group`,
`unit`, `step`, `visibleWhen` and `hidden` (state the extension persists
itself, never shown in the UI). Control Center renders them, validates every
write, offers Reset, and shows the extension itself above the controls so each
change is visible immediately.

## Per-instance configuration

An extension that reads `hostInstanceId` and binds it to `Settings.instanceId`
may declare `instances: true`. The person can then add, duplicate, rename and
remove instances; removing one deletes its settings, position and size.

## Trust

None of this is a sandbox. Extension QML runs in-process with your
permissions, exactly as before. PluginKit 4 adds consent and containment:
tiles are off until added, commands run only on a user gesture, each surface
has its own Loader so one failure stays local, and safe mode still loads
nothing. Read the source of any extension before enabling it.
