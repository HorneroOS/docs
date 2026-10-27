# Getting started

## Know what is available

HorneroOS publishes a signed Preview ISO: **v0.2.0-preview22**, one x86_64
image that installs HorneroOS Desktop Preview or HorneroOS Studio Preview
with selectable creative specializations. It is a preview, not a stable or
supported release.

- Download: [horneroos.com/install](https://www.horneroos.com/install) or the
  [v0.2.0-preview22 release](https://github.com/HorneroOS/hornero/releases/tag/v0.2.0-preview22).
- ISO: `horneroos-2026.10-preview22-x86_64.iso` (2.6 GB, hosted on Vercel
  Blob because it exceeds GitHub's 2 GB asset limit).
- SHA-256: `38ec76d7c9c10ea3e956b2c9f2d8d420e3d09b61899dc453a2858622d7e90bd2`
- Signature: detached GPG signature from the HorneroOS releases key
  `FCFBEE43925AB5429362278AE59EAB44AA2498DC`. The public key is
  `packaging/keys/hornero-release.pub.asc` in HorneroOS/hornero.

Verify every copy before writing it to media:

The public key comes straight from the release tag, no checkout needed:

```sh
key_base="https://raw.githubusercontent.com/HorneroOS/hornero"
curl -fsSL \
  "$key_base/v0.2.0-preview22/packaging/keys/hornero-release.pub.asc" \
  | gpg --import
gpg --verify horneroos-2026.10-preview22-x86_64.iso.sig \
  horneroos-2026.10-preview22-x86_64.iso
sha256sum -c horneroos-2026.10-preview22-x86_64.iso.sha256
```

## Requirements and limits

- x86_64 machine or VM; UEFI or legacy BIOS firmware.
- The ISO installs with the provisional Calamares installer. Disk layout
  and encryption (LUKS) are chosen during installation; nothing is
  preselected, and confirming a partition operation can erase data.
- Validated scope: the Desktop and Studio install matrix (UEFI/BIOS,
  encrypted/unencrypted) passed in disposable virtual machines, on the
  preview21 composition carried forward to preview22. UEFI first login
  remains pending in the installer's R11 record, and installed package
  parity is unverified.
- No physical-hardware validation exists yet. Studio hardware QA
  (`hornero-qa studio-gate`) is blocked on approved hardware fixtures,
  so Studio is Preview, not Supported. Server and Agents are planned
  editions with no installable image. Niri is experimental.
- Panda Foss is developing the future official installer; the Calamares
  path in this ISO is a provisional bridge.

Write the ISO to a USB stick with a graphical writer you trust, or with
`dd`. With `dd`, first confirm the whole-disk device with `lsblk` (writing
to the wrong device destroys its data), then run it with privileges:

```sh
sudo dd if=horneroos-2026.10-preview22-x86_64.iso of=/dev/sdX bs=4M \
  status=progress conv=fsync
```

Boot from the stick and follow the Calamares steps. Report installation
problems in the [HorneroOS/installer issue
chooser](https://github.com/HorneroOS/installer/issues/new/choose) with
the ISO name, your firmware (UEFI or BIOS), whether the disk is
encrypted, and the step where it failed.

Individual components are also packaged for people already running Arch
Linux and Hyprland. That AUR path is an alternative for an existing Arch
system; the ISO is the primary installation path. Do not treat a package
list, a dotfiles checkout, or an old wiki page as an installer.

## Explore before installing

- See real product captures in the [Showroom](https://github.com/HorneroOS/website/tree/main/src/content/showroom).
- Compare the available [themes](https://github.com/HorneroOS/website/blob/main/src/pages/themes.astro)
  and [bar layouts](https://github.com/HorneroOS/website/blob/main/src/pages/layouts.astro).
- Read [desktop basics](../desktop/README.md), [shortcuts](../desktop/shortcuts.md),
  and [appearance](../desktop/appearance.md).

## After installing

Follow the release notes for changes to package availability. Use the
[HorneroOS/installer issue chooser](https://github.com/HorneroOS/installer/issues/new/choose)
for installation failures and the owning repository's tracker for
post-install problems.
