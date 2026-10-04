# Security and privacy

Hornero is still a development-stage desktop project. An Arch package or a
preview release is not a substitute for reviewing the software and update
source on a machine that holds important data.

## Location and weather

With no configured location, Weather remains offline: it does not infer your
location from your IP. If you enter a city or coordinates, Weather sends that
location to Open-Meteo for geocoding and forecast data. The current provider
behavior is implemented in
[Weather.qml](https://github.com/HorneroOS/shell/blob/main/services/Weather.qml);
review it again before enabling any future location-detection feature.

## Lock your session

Use **Super + L** or the session menu to lock the current session. The lock
screen protects access to an already-running session; it does not encrypt a
disk, replace account security, or protect a machine whose session was left
unlocked.

## Themes and files

Hornero theme packs describe appearance. A theme card does not authorize an
unreviewed package or script. Hornero does not silently download arbitrary
wallpaper or icon assets. Use trusted package sources and review custom
configuration changes before applying them.

## Sharing diagnostics

Before publishing logs or screenshots, remove usernames, hostnames, serials,
network names, paths to private files, notification contents, and unrelated
terminal output. Share only the lines needed to reproduce the problem.

For the former dotfiles wiki's machine-specific security-tool recipes, see
the [documentation disposition](../development/dotfiles-wiki-disposition.md).
