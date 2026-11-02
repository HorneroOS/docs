# Troubleshooting

Start with read-only diagnostics. Record the exact error and the steps that
reproduce it before changing configuration or reinstalling packages.

```sh
horneroctl doctor
horneroctl config validate
horneroctl shell status --json
horneroctl appearance doctor
```

## The shell is missing or not responding

Check whether Quickshell is reachable, then read its recent log:

```sh
horneroctl shell status --json
horneroctl shell logs --lines 120
```

If the log reports a missing QML module or plugin, record the package versions
and the first import/load error. Do not repeatedly restart the graphical
session. See the [Shell troubleshooting notes](https://github.com/HorneroOS/shell/blob/main/README.md#troubleshooting)
and [report a reproducible issue](../development/README.md#report-a-bug).

## Settings or a pane appears empty

Validate the materialized configuration, read the Shell log, and reopen the
specific pane from the Control Center. Include the pane name and whether it
was opened through the sidebar or a deep link. Avoid deleting user settings:

```sh
horneroctl config validate
horneroctl shell logs --lines 120
horneroctl config gui --pane appearance
```

If another pane works but one is blank, report it as a pane-load failure.

## Theme and wallpaper do not agree

Read live state before applying another look:

```sh
horneroctl appearance status --json
horneroctl appearance theme get
horneroctl appearance gtk current
horneroctl appearance gtk current-icon
horneroctl wallpaper current
horneroctl appearance doctor
```

An image named by a theme manifest may not be installed locally. Choose a
local wallpaper and check installed GTK and icon themes before treating an
external dependency as a shell failure. See [Appearance](../desktop/appearance.md)
and [Wallpapers](../desktop/wallpapers.md).

## Network and Bluetooth

Check that the adapter is visible to the operating system, then open the
matching Control Center pane. A missing adapter is below the shell layer;
collect `lspci -nnk`, `lsusb`, and the relevant kernel log lines before
reporting it. These commands only inspect devices.

## Display and graphics

Check the monitor list and loaded kernel driver:

```sh
hyprctl monitors -j
lspci -nnk
journalctl -b -k -p warning
```

For NVIDIA or hybrid graphics, follow the device-specific
[hardware guidance](../hardware/README.md#nvidia-and-hybrid-graphics). A
black screen or failed session before the shell starts is not a Control
Center problem.

## Login screen

For an SDDM login-screen failure, gather the installed package and selected
theme plus the current boot log:

```sh
pacman -Q sddm hornero-greeter
journalctl -b -u sddm --no-pager
```

The [Hornero greeter repository](https://github.com/HorneroOS/greeter) owns
the theme and packaging contract. Do not restart SDDM during a graphical
session merely to test a theme.

## Installation failures

If the Preview ISO does not boot, the Calamares installer fails, or the
first boot of that ISO does not reach a login, report it in the
[HorneroOS/installer issue chooser](https://github.com/HorneroOS/installer/issues/new/choose)
with the ISO name, your firmware (UEFI or BIOS), whether the disk is
encrypted, and the step where it failed. Failures after that first
boot (greeter, shell, desktop hardware, applications) belong to the
owning component trackers below, not to the installer repository.

## Include this in a bug report

- Relevant repo and component version.
- What you expected and what happened.
- The smallest repeatable sequence of actions.
- The first relevant error lines, with personal identifiers removed.
- A screenshot only when it contains no private windows or notifications.

See [how to report a bug](../development/README.md#report-a-bug) for the
repository issue links and information to include.

## The installer does not see the internal NVMe drive (Intel VMD/RST)

On some Intel laptops (for example ASUS ROG models) the firmware exposes
the NVMe SSD through Intel VMD/RST ("PCIE RST Controlled Disk"). With VMD
enabled, the Live system may show no internal disk at all. This is a
controller-visibility problem, not a missing or damaged drive:

1. Do **not** delete partitions or reformat anything to "fix" it.
2. Reboot into the firmware setup and switch the storage controller from
   RST/VMD to the standard NVMe/AHCI mode, if your firmware offers it.
3. Boot the HorneroOS Live ISO again and confirm the drive appears in the
   installer's disk list before continuing.

Warnings: changing the controller mode can make an existing Windows
installation unbootable until its storage driver is prepared, and it can
affect BitLocker recovery (have the recovery key ready). HorneroOS never
changes firmware settings for you. Compatibility with VMD-managed drives
is not claimed; the standard-controller path above is the tested one.
Note also that a missing disk does not prove the SSD is healthy: if the
drive stays invisible in standard controller mode too, suspect a
hardware or seating problem and stop before installing anywhere else.

## Encrypted swap and the `openswap` initramfs error

Older installer builds could generate an `mkinitcpio` configuration with
an `openswap` hook (plus duplicate `encrypt` entries) for LUKS + separate
encrypted swap, failing with `ERROR: Hook 'openswap' cannot be found`.
HorneroOS does not ship an `openswap` hook, so that layout could never
produce a bootable initramfs. Current installers therefore offer
`No Swap` only (`userSwapChoices: [ none ]`) — a fail-closed boundary,
not a claim that encrypted swap is supported. If you need swap, add a
swapfile on the installed (already encrypted) Btrfs root after
installation instead of re-enabling the partition option.

## Copy-to-RAM and the missing `base.sqfs`

With large amounts of RAM, Archiso could copy the Live system to RAM and
unmount the installation payload, after which Calamares failed with
`The source filesystem "/run/archiso/bootmnt/hornero/x86_64/base.sqfs"
does not exist`. Current ISOs disable automatic copy-to-RAM and verify
the payload before any disk changes. If you hit this on an old ISO, boot
with `copytoram=n` as a workaround and prefer a current ISO.
