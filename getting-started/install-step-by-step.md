# Installing HorneroOS step by step

HorneroOS is an operating system for everyday use: used and
maintained daily, with concrete, declared limitations. This guide
installs the published ISO on a real machine or a virtual machine.
The ISO file keeps its published name; that name is an artifact
name, not a statement about how you may use the system day to day.

## Before you start

- Back up anything on the target disk you want to keep. Confirming
  a partition operation in the installer can erase data.
- Prefer UEFI firmware. Legacy BIOS, LUKS-encrypted installs, Niri
  sessions and copy-to-RAM were not run on the v0.2.0-preview32 ISO
  and are concrete limitations today, not steps this guide can
  promise. See [Hardware: tested and untested](../hardware/tested-and-untested.md).
- Validated scope for that ISO is Desktop, Studio and Gaming UEFI
  unencrypted installs in disposable virtual machines. There is no
  physical-hardware validation for that artifact yet.

## Download and verify

Follow [Getting started](README.md) for the download, SHA-256 and
GPG verification commands. Do not skip verification: write only an
image whose checksum and signature both pass.

## Write the USB stick and boot it

Use a graphical writer you trust, or `dd` as shown in
[Getting started](README.md). Confirm the whole-disk device with
`lsblk` first; writing to the wrong device destroys its data.

Boot from the stick, disable Secure Boot if your firmware blocks
the live system, and confirm the installer can see your target
disk. If an internal NVMe drive is missing on an Intel laptop, see
the VMD/RST note in [Troubleshooting](../troubleshooting/README.md).

## What to choose in the installer today

1. Language, keyboard and timezone: pick your real locale; you can
   change the keyboard later from the desktop.
2. Edition: Desktop for a general machine, Studio for audio and
   creative work, Gaming for a game-focused setup. All three are
   selectable from the same ISO.
3. Compositor: Hyprland is the validated default. Choose Niri only
   if you accept an experimental session with a smaller verified
   surface.
4. Disk: prefer a whole-disk or manual layout you understand over
   an alongside/resize option you have not backed up. LUKS
   encryption is offered by the installer, but encrypted installs
   were not validated on this ISO; choose it knowing that limit.
5. User: create your everyday account and a strong password. That
   account is the one you will update and configure from.

The installer is the provisional Calamares installer. If it fails,
reboot before retrying and report the failure in the
[installer issue chooser](https://github.com/HorneroOS/installer/issues/new/choose)
with the ISO name, firmware type, encryption choice and the exact
step that failed.

## First boot

Remove the USB stick and boot the installed system. Then work
through [Post-install: your first session](../applications/post-install-first-steps.md).
If the machine does not boot, see
[Troubleshooting by symptom](../troubleshooting/by-symptom.md).
