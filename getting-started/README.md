# Getting started

## Know what is available

HorneroOS is used daily in production across physical workstations and
validated in full UEFI and Legacy BIOS KVM. The current signed release is
**`v0.2.0-preview42`** (`x86_64`), which ships two official signed artifacts
from [horneroos.com/install](https://www.horneroos.com/install) and the
[v0.2.0-preview42 release](https://github.com/HorneroOS/hornero/releases/tag/v0.2.0-preview42)
*(note: `v0.2.0-preview42` is kept as the published git tag and artifact
identifier)*:

- **Official Live & Installable ISO (`3.3 GiB`, UEFI + Legacy BIOS, validated
  on physical hardware & KVM):** Installs HorneroOS **Desktop**, **Studio**, or
  **Gaming** with selectable creative specializations, **Hornero Signal**,
  **Hornero Apps**, **Signal Flight Welcome (`v1.6.0`)**, and **Calamares
  `3.4.3`** (Signal Night chrome).
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/iso/horneroos-2026.11-preview42-x86_64.iso`
  - SHA-256:
    `9e494ab5f9783df6a5986385421ec0816b0033d3558d3323248a03e07f2e76a2`
- **Official Preinstalled Desktop QCOW2 (`2.61 GiB`):** Clean-room built,
  scrubbed, and E2E-validated in UEFI KVM for immediate local VM booting.
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/vm/horneroos-0.2.0-preview42-desktop-qemu-x86_64.qcow2.zst`
  - SHA-256:
    `c1012413227f407d0a312fad7d7a34f789922303db13c752a9a9ed1a324e13c2`
- **Signature:** Detached GPG signature (`.sig`) and `.sha256` from the
  HorneroOS releases key `FCFBEE43925AB5429362278AE59EAB44AA2498DC`. The
  public key is `packaging/keys/hornero-release.pub.asc` in
  `HorneroOS/hornero`.

Verify every copy before writing it to media or booting a VM:

The public key comes straight from the release tag, no checkout needed:

```sh
key_base="https://raw.githubusercontent.com/HorneroOS/hornero"
curl -fsSL \
  "$key_base/v0.2.0-preview42/packaging/keys/hornero-release.pub.asc" \
  | gpg --import
gpg --verify horneroos-2026.11-preview42-x86_64.iso.sig \
  horneroos-2026.11-preview42-x86_64.iso
sha256sum -c horneroos-2026.11-preview42-x86_64.iso.sha256
```

## Requirements and limits

- `x86_64` machine or VM; UEFI or Legacy BIOS firmware.
- The ISO installs with **Calamares 3.4.3** (Signal Night chrome). Disk
  layout and encryption (LUKS) are chosen during installation; nothing is
  preselected, and confirming a partition operation can erase data.
- **Supported editions and compositors:** **Desktop**, **Studio**, and
  **Gaming** are **Supported** daily-driven editions. **Hyprland** is the
  default compositor and **Niri** is supported as a scrolling Wayland
  compositor option (see [Wayland compositors](../desktop/compositors.md) for
  compositor-specific capability differences). **Server**, **Agents**, and
  **Labwc** remain **Planned** with no bootable images.
- **Validation scope:** HorneroOS runs daily in production across multiple
  physical workstations, and `v0.2.0-preview42` passed both UEFI and Legacy
  BIOS KVM validation plus physical-hardware verification. Specialized
  per-hardware checks (individual GPU/audio/handheld rigs) are tracked in
  [Tested and untested](../hardware/tested-and-untested.md); full OS root
  rollback remains **Planned**
  ([Updates and recovery](../desktop/updates-and-rollback.md)).

Write the ISO to a USB stick with a graphical writer you trust, or with
`dd`. With `dd`, first confirm the whole-disk device with `lsblk` (writing
to the wrong device destroys its data), then run it with privileges:

```sh
sudo dd if=horneroos-2026.11-preview42-x86_64.iso of=/dev/sdX bs=4M \
  status=progress conv=fsync
```

Boot from the stick and follow the Calamares steps. Report installation
problems in the [HorneroOS/installer issue
chooser](https://github.com/HorneroOS/installer/issues/new/choose) with
the ISO name, your firmware (UEFI or BIOS), whether the disk is
encrypted, and the step where it failed.

Individual components are also packaged for people already running Arch
Linux and Hyprland. That AUR path is a supported alternative for an
existing Arch system — follow [Installing HorneroOS on an existing Arch
Linux system](install-on-arch.md) for the packages, the missing-only
first-time setup and the rollback path. Do not treat a bare package
list, a dotfiles checkout, or an old wiki page as an installer.

## Explore before installing

- Start with the [Public launch guide](public-preview-launch-guide.md)
  for Windows, macOS (Apple Silicon caveats), and Arch Linux paths, known
  limitations, practical troubleshooting, and hardware/security reporting.
- Follow [Try HorneroOS without installing](try-horneroos.md) for browser
  Playground sessions, local virtual machines, Live USB, and Presenter Mode.
- Review the [v0.2.0-preview42 release announcement](../releases/v0.2.0-preview42-announcement-draft.md)
  for launch highlights and the YouTube demonstration checklist.
- See real product captures in the [Showroom](https://horneroos.com/showroom/).
- Compare the available [themes](https://horneroos.com/themes/)
  and [bar layouts](https://horneroos.com/layouts/).
- Read [desktop basics](../desktop/README.md), [shortcuts](../desktop/shortcuts.md),
  and [appearance](../desktop/appearance.md).

## After installing

Work through [Installing HorneroOS step by step](install-step-by-step.md)
for the installer choices in order, then
[Post-install: your first session](../applications/post-install-first-steps.md).

Systems installed from v0.2.0-preview24 need a one-time manual
migration before normal updates work; follow
[Upgrading an existing preview24 installation](upgrading-from-preview24.md).
Follow the release notes for changes to package availability. Use the
[HorneroOS/installer issue chooser](https://github.com/HorneroOS/installer/issues/new/choose)
for installation failures and the owning repository's tracker for
post-install problems.
