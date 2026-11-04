# Getting started

## Know what is available

HorneroOS publishes a signed Preview ISO: **v0.2.0-preview32**, one x86_64
image that installs HorneroOS Desktop, Studio or Gaming Preview
with selectable creative specializations. It is a preview, not a stable or
supported release.

- Download: [horneroos.com/install](https://www.horneroos.com/install) or the
  [v0.2.0-preview32 release](https://github.com/HorneroOS/hornero/releases/tag/v0.2.0-preview32).
- ISO: `horneroos-2026.10-preview32-x86_64.iso` (2.8 GB, hosted on Vercel
  Blob because it exceeds GitHub's 2 GB asset limit).
- SHA-256: `b8cd0f8604bc69f7d2112fb8bccd97115d32d197e9c92c62e02faf5de6345aec`
- Signature: detached GPG signature from the HorneroOS releases key
  `FCFBEE43925AB5429362278AE59EAB44AA2498DC`. The public key is
  `packaging/keys/hornero-release.pub.asc` in HorneroOS/hornero.

Verify every copy before writing it to media:

The public key comes straight from the release tag, no checkout needed:

```sh
key_base="https://raw.githubusercontent.com/HorneroOS/hornero"
curl -fsSL \
  "$key_base/v0.2.0-preview32/packaging/keys/hornero-release.pub.asc" \
  | gpg --import
gpg --verify horneroos-2026.10-preview32-x86_64.iso.sig \
  horneroos-2026.10-preview32-x86_64.iso
sha256sum -c horneroos-2026.10-preview32-x86_64.iso.sha256
```

## Requirements and limits

- x86_64 machine or VM; UEFI or legacy BIOS firmware.
- The ISO installs with the provisional Calamares installer. Disk layout
  and encryption (LUKS) are chosen during installation; nothing is
  preselected, and confirming a partition operation can erase data.
- Validated scope: Desktop, Studio and Gaming UEFI unencrypted
  installs passed on the preview32 ISO in disposable virtual machines.
  LUKS-encrypted installs, legacy BIOS, Niri sessions and copytoram
  were not run on this artifact and are not carried forward as passed
  for preview32. Preview32 itself has no physical-hardware validation.
- Physical-hardware acceptance for one ASUS ROG Strix G16 workstation
  is recorded as USER-VERIFIED on preview24 plus post-install fixes
  (see HorneroOS/qa `docs/PELICANO-PARITY.md`); specialized checks
  such as NVENC, Vulkan correctness and HDMI capture remain
  NOT SPECIFICALLY TESTED. Studio, Desktop and Gaming are Preview,
  not Supported. Server and Agents are planned editions with no
  installable image. Niri is experimental.
- Panda Foss is developing the future official installer; the Calamares
  path in this ISO is a provisional bridge.

Write the ISO to a USB stick with a graphical writer you trust, or with
`dd`. With `dd`, first confirm the whole-disk device with `lsblk` (writing
to the wrong device destroys its data), then run it with privileges:

```sh
sudo dd if=horneroos-2026.10-preview32-x86_64.iso of=/dev/sdX bs=4M \
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

Systems installed from v0.2.0-preview24 need a one-time manual
migration before normal updates work; follow
[Upgrading an existing preview24 installation](upgrading-from-preview24.md).
Follow the release notes for changes to package availability. Use the
[HorneroOS/installer issue chooser](https://github.com/HorneroOS/installer/issues/new/choose)
for installation failures and the owning repository's tracker for
post-install problems.
