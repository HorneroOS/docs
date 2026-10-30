# Upgrading an existing preview24 installation

This guide migrates a system installed from **HorneroOS
v0.2.0-preview24** to the package composition shipped in
**v0.2.0-preview28**, without reinstalling the operating system.

It was validated end to end in a disposable UEFI VM (Studio — Hyprland,
LUKS-encrypted Btrfs, no swap): user files, an OBS profile, and a custom
`.zshrc` line survived the upgrade and a reboot, and
`horneroctl studio doctor` passed all checks afterwards.

> `horneroctl package upgrade` only runs `pacman -Syu`. It does **not**
> perform this migration: it does not repair the preview24 repository
> configuration, update AUR packages, install factory packages added
> after preview24 (zsh, nano), or change your login shell. Follow the
> steps below instead.

## Before you start

- Make a backup of anything you cannot afford to lose. This procedure
  has no snapshot or rollback mechanism; recovery from a failed system
  upgrade uses standard Arch tools (pacman cache, `downgrade`, chroot
  from live media).
- Read every step first. Step 1 is mandatory on preview24: its package
  manager configuration is broken and `pacman -Syu` fails until it is
  repaired.

## 1. Repair the pacman repository configuration (preview24 bug)

Preview24 installations ship with two defects:

- The `[multilib]` section of `/etc/pacman.conf` has no `Include` line.
- `/etc/pacman.d/mirrorlist` contains no active `Server` lines.

Together they cause
`error: failed to synchronize all databases (no servers configured for repository)`.

Repair both, then verify that every enabled repository has servers:

```bash
sudo sed -i '/^\[multilib\]/a Include = /etc/pacman.d/mirrorlist' /etc/pacman.conf
sudo sed -i '1i Server = https://geo.mirror.pkgbuild.com/$repo/os/$arch' /etc/pacman.d/mirrorlist
grep -A1 '^\[multilib\]' /etc/pacman.conf
grep -c '^Server' /etc/pacman.d/mirrorlist
```

Expected: the `Include` line is present under `[multilib]`, and the
mirror count is at least 1 (add more mirrors if you prefer).

## 2. Upgrade the Arch packages

```bash
sudo pacman -Syu
```

Do not use a bare `pacman -Sy` followed by installing individual
packages; that leaves the system in a partial-upgrade state.

## 3. Install the factory packages added after preview24

Preview28 makes zsh the factory login shell for new users and ships
nano as the default editor. Existing installations get neither
automatically:

```bash
sudo pacman -S --needed zsh nano base-devel
```

`base-devel` is only needed for the next step (building the AUR
package); skip it if you do not want build tools installed.

## 4. Update the HorneroOS AUR packages

HorneroOS components such as `hornero-config` are distributed through
the AUR and are not touched by `pacman -Syu`. There is no bundled AUR
helper; build the package manually:

```bash
git clone https://aur.archlinux.org/hornero-config.git
cd hornero-config
makepkg -si
pacman -Q hornero-config   # expect 0.3.14-1 or newer
```

Repeat the equivalent update for any other HorneroOS AUR packages you
have installed (for example `horneroctl-bin`).

## 5. Adopt the factory editor default (existing users)

The `EDITOR=nano` / `VISUAL=nano` default ships in
`/etc/skel/.config/environment.d/10-hornero-editor.conf`, which only
applies to newly created users. Adopt it for your existing account
without overwriting anything:

```bash
mkdir -p ~/.config/environment.d
cp -n /etc/skel/.config/environment.d/10-hornero-editor.conf ~/.config/environment.d/
```

Log out and back in for the variables to take effect. The factory
`/etc/skel/.zshrc` is intentionally not copied over your `~/.zshrc`;
merge anything you want from it manually.

## 6. Optionally switch your login shell to zsh

Existing users are never switched automatically. If you want the
preview28 factory shell:

```bash
chsh -s /usr/bin/zsh
```

Log out and back in, then confirm with `echo $SHELL`.

## 7. Verify

```bash
horneroctl studio doctor        # Studio systems; expect all checks passed
systemctl --user status pipewire wireplumber
pacman -Q hornero-config zsh nano
```

Reboot once and confirm the machine still unlocks (LUKS), reaches the
greeter, and logs in normally. Your files, OBS profiles, and personal
configuration are not touched by any step above.

## Known limitations

- **OS identity does not change.** `/etc/os-release` keeps `ID=arch` on
  migrated systems. The `ID=horneroos` identity is written by the
  installer at install time (preview28 and later) and does not
  propagate through package upgrades. Tooling that detects HorneroOS
  through os-release (for example chezmoi's `osRelease.id`) will not
  recognize a migrated preview24 system; use the documented
  `HORNERO_NATIVE=1` override where supported.
- **No edition reconciliation.** If a future release changes the
  edition composition, installed systems do not gain or lose edition
  packages automatically. Install or remove them explicitly.
- **No rollback.** There is no snapshot integration yet. Btrfs
  subvolumes exist, but no snapshot tool is installed by default.
- **Graphics drivers are out of scope.** NVIDIA and hybrid-GPU systems
  keep their existing driver stack; this guide was validated on VM
  graphics only, not on physical GPU hardware.
