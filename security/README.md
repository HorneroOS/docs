# Security and privacy

HorneroOS is a development-stage operating-system family built on Arch Linux.
A preview ISO or an AUR package is not a substitute for reviewing the software,
update sources, and threat model on a machine that holds important data.

## Disk encryption (LUKS)

Full-disk encryption is optional and chosen in the provisional Calamares
installer during partitioning. Nothing is preselected.

- **Status on v0.2.0-preview32:** Unencrypted UEFI installs passed in
  disposable VMs. LUKS-encrypted installs were not re-run on preview32 and
  are not carried forward as passed for that artifact.
- **Session lock is not disk encryption:** Locking the desktop with
  **Super + L** only protects an already-running session. Without LUKS, anyone
  with physical access to the drive can read your files offline.

## Secure Boot

HorneroOS does not currently ship signed Secure Boot shims or enroll
Microsoft/custom Secure Boot keys automatically.

- Booting the preview ISO requires disabling Secure Boot in firmware unless
  you sign and enroll your own keys (for example with `sbctl`, following the
  [ArchWiki Secure Boot guide](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot)).
- Do not assume Secure Boot is active after installation; verify with
  `bootctl status`.

## Firewall posture

HorneroOS does not silently install or enable an opinionated firewall profile
on top of Arch Linux defaults.

- Review listening sockets with `ss -tulpn` after installation.
- If you connect to untrusted networks, enable and configure a host firewall
  such as `nftables` or `ufw` (see the
  [ArchWiki Firewall guide](https://wiki.archlinux.org/title/Firewalls)).

## Release signing and verification

Official HorneroOS ISOs and release artifacts are signed with the HorneroOS
releases GPG key:

- **Fingerprint:** `FCFBEE43925AB5429362278AE59EAB44AA2498DC`
- **Public key:** `packaging/keys/hornero-release.pub.asc` in
  [`HorneroOS/hornero`](https://github.com/HorneroOS/hornero)

Always verify both the detached `.sig` signature and the `.sha256` checksum
before writing an ISO to USB media. See [Getting started](../getting-started/README.md)
for the exact verification commands.

## AUR trust boundaries

On Arch Linux, packages outside the official Arch repositories come from the
Arch User Repository (AUR), which is community-maintained.

- Read every `PKGBUILD` before building or upgrading with `yay` or `paru`.
- Never run `makepkg` as `root`.
- Official HorneroOS packages (`hornero-shell`, `hornero-config`,
  `horneroctl-bin`, `hornero-greeter`) are built from the repositories under
  `github.com/HorneroOS`. Third-party AUR packages are outside HorneroOS's
  trust boundary.

## Privilege escalation (polkit and sudo)

HorneroOS follows standard Arch Linux privilege boundaries:

- Interactive graphical elevation uses `polkit-gnome` (the polkit
  authentication agent).
- Terminal administration uses `sudo` with explicit user authentication.
- `horneroctl` separates read-only inspection from mutating actions. Mutating
  commands support `--dry-run` and require `--yes` (or interactive
  confirmation) rather than elevating silently.

## Extensions: unsandboxed QML vs PluginKit 6 companions

Hornero Shell supports two distinct extension models with different trust
boundaries:

- **QML shell extensions (unsandboxed):** QML extensions run inside the
  Quickshell / Hornero Shell process with the full permissions of your user
  session. Treat a QML extension with the same caution as any local
  executable code — inspect its source before installing it.
- **PluginKit 6 data-only companions:** Companions installed from the
  PluginKit catalogue are declarative data packages (manifests, metadata, and
  structured actions) rather than arbitrary executable QML. They cannot
  execute arbitrary code inside the shell process on their own.

See [Extensions 2.0 authoring guide](../development/extensions.md) and
[PluginKit platform](../development/pluginkit-platform.md) for the exact
contracts.

## AI agent confinement (bubblewrap)

When HorneroOS launches local AI coding agents or assistant tools through
`horneroctl agent` / `horneroctl assistant`, confinement relies on
`bubblewrap` (`bwrap`) namespaces where supported:

- Filesystem access is scoped to the declared workspace and explicit
  read-only system mounts rather than the entire home directory.
- Network and secret exposure should be treated as explicit opt-ins; never
  assume an agent sandbox protects against a host kernel vulnerability or
  overly broad bind mounts.
- Inspect agent policies and status with `horneroctl assistant policy` and
  `horneroctl agent status`.

## Location and weather

With no configured location, Weather makes no location request and does not
infer your location from your IP. Entering a city sends that city name to
Open-Meteo's geocoding service, then requests the forecast for its
coordinates. Entering coordinates requests the forecast and uses Nominatim
reverse geocoding to label the location. These requests use HTTPS. The
current provider behavior is implemented in
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

## Vulnerability disclosure

Do not report security vulnerabilities in public GitHub issues. Follow the
private reporting process in
[`SECURITY.md`](https://github.com/HorneroOS/.github/blob/main/SECURITY.md)
(or use GitHub Private Vulnerability Reporting on the affected repository
under `HorneroOS`).

For the former dotfiles wiki's machine-specific security-tool recipes, see
the [documentation disposition](../development/dotfiles-wiki-disposition.md).
