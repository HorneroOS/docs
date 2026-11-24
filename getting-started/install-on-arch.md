# Installing HorneroOS on an existing Arch Linux system

This guide installs the HorneroOS desktop as packages on an Arch
Linux system you already use. Nothing is reinstalled, no disk is
touched, and no file you own is overwritten. For a from-scratch
install with edition provisioning, use the ISO path in
[Getting started](README.md) instead.

## What you get, and what you do not

You get the packaged desktop: Hornero Shell, the curated defaults,
the greeter theme if you ask for it, and `horneroctl`. Experience
modes are part of the desktop. Edition applications are not
provisioned for you: the Studio creative stack, Steam and friends
install with pacman/yay like on any Arch system. The ISO remains
the only path that provisions a whole edition at once.

Arch derivatives (CachyOS, EndeavourOS and others) use the same
packages but are not officially verified; treat this path as
experimental there.

## Requirements

Required:

- Arch Linux x86_64, fully updated (`pacman -Syu`).
- `git` and `base-devel` to build AUR packages, and an AUR helper
  such as yay (below).
- For the full experience, a Wayland session with Hyprland. If you
  have no compositor yet, step 2 installs one.

Recommended: PipeWire + WirePlumber, and a backup of your current
configuration. First-time setup never overwrites your files, but a
backup is still free:

```sh
tar -czf ~/hornero-pre-adopt-$(date +%F).tar.gz \
  ~/.config/hypr ~/.config/ghostty ~/.config/environment.d 2>/dev/null
```

GPU drivers stay your responsibility, exactly as on plain Arch:
follow the Arch wiki for your hardware (on NVIDIA that includes the
proprietary driver and its modeset configuration). HorneroOS
packages do not install or configure GPU drivers on this path.

## 1. Install yay (if you do not have an AUR helper)

The AUR is community-maintained: read every PKGBUILD before
building, and never run `makepkg` as root.

```sh
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

## 2. Install the packages

`hornero-shell` pulls in `hornero-config` (curated defaults) and
`horneroctl-bin` (the signed system CLI). The second line is
session support; skip anything you already have.

```sh
yay -Syu hornero-shell
yay -S --needed hyprland xdg-desktop-portal-hyprland \
  xdg-desktop-portal-gtk kitty dex hypridle cliphist wl-clipboard
```

The greeter is optional and only for current SDDM users — it
installs the HorneroOS theme and does not switch or enable your
display manager:

```sh
yay -S hornero-greeter
```

## 3. Seed your user configuration (missing files only)

Your account predates the packages, so the factory skeleton in
`/etc/skel` never reached it. The packaged seed copies only what
you are missing — Hyprland modules, terminal, session environment,
helper symlinks — and reports every file it would create first:

```sh
/usr/share/hornero/seed-user.sh --dest "$HOME" --dry-run
/usr/share/hornero/seed-user.sh --dest "$HOME"
horneroctl doctor
```

On current `horneroctl` releases the same backend also answers to
`horneroctl config materialize --dest "$HOME"`. Seeding is
idempotent: re-running it after a package update only adds newly
shipped files. It refuses system destinations and symlinked
destination roots.

What seeding never does:

- It never overwrites an existing file. Your own `hyprland.lua`,
  terminal config and login shell win over every factory default.
- It never disables another desktop, bar or notification daemon.
  If one is already autostarting, both will run until you turn
  one off.
- It never changes your display manager, bootloader or partitions.

If your Hyprland entrypoint is the factory one (seeded above or
from an account created after installing the packages),
`horneroctl config refresh-hypr` keeps its module list current
additively; your `hyprland.lua.d/*-user.lua` overrides stay yours.

## 4. Start the desktop

There is no new session to pick: HorneroOS lives inside Hyprland.

- **No Hyprland config of your own:** just log into the Hyprland
  session from your usual display manager (or start `Hyprland`
  from a TTY). Seeded/factory defaults autostart the shell.
- **Existing Hyprland config:** your entrypoint keeps control. To
  try only the shell inside your current session, run
  `horneroctl shell start --yes`. To adopt the factory entrypoint,
  move your `hyprland.lua` aside, seed again, and carry your
  customizations over into `hyprland.lua.d/*-user.lua`.
- **Another desktop installed:** nothing to do. KDE, GNOME or any
  other session stays installed and selectable in your display
  manager; HorneroOS does not replace it.

## 5. Make it yours

Open Control Center for layouts, themes, Hornero Chromatic,
experience modes and PluginKit extensions from the catalogue.
Companions install from the same catalogue as data packages.
Then read [Post-install: your first
session](../applications/post-install-first-steps.md).

## Updating

Updating is the usual `yay -Syu`. Take a Hornero settings snapshot
first if you want one:

```sh
horneroctl config snapshot create --yes
yay -Syu
```

The packaged desktop can be newer than the published ISO; that is
expected. Follow release notes for per-release changes.

## Rolling back and uninstalling

Removing the packages leaves your configuration and data in
place, and your previous session keeps starting as before:

```sh
yay -Rns hornero-shell hornero-config horneroctl-bin
```

The only files seeding created are the ones it listed when it
ran; deleting them is optional and safe if you never edited them.
Your own files were never touched, so there is nothing to restore.

## Troubleshooting

- **The shell does not start with your session:** your Hyprland
  entrypoint is your own and does not autostart it. Start it once
  with `horneroctl shell start --yes` to confirm it works, then
  either adopt the factory entrypoint (step 3) or add that command
  to your own autostart.
- **`horneroctl doctor` reports missing tools:** install the named
  package and re-run; doctor distinguishes hard requirements from
  optional creative tooling.
- **Two notification daemons or bars at once:**expected when
  another desktop component autostarts alongside Hornero Shell.
  Disable the autostart of the one you do not want; HorneroOS does
  not stop foreign processes for you.
- **Anything else:** see
  [Troubleshooting by symptom](../troubleshooting/by-symptom.md).
