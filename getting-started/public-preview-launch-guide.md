# Public launch guide

This guide gives first-time external visitors a single, honest entry point to
try, install, troubleshoot, and report findings on HorneroOS—without assuming
prior Arch Linux or Hyprland knowledge.

> **Product truth today:** HorneroOS is used daily in production across
> multiple physical workstations and validated in UEFI and Legacy BIOS KVM.
> The current signed release is **`v0.2.0-preview42`** (`x86_64`), bundling
> **Hornero Signal**, **Hornero Apps**, **Signal Flight Welcome (`v1.6.0`)**,
> **Chromatic v3**, **Experience Modes**, and **Calamares `3.4.3`** across
> two signed artifacts: a `3.3 GiB` live & installable ISO and a `2.61 GiB`
> preinstalled Desktop QCOW2. **Desktop**, **Studio**, and **Gaming** are
> **Supported** editions; **Hyprland** (default) and **Niri** are **Supported**
> compositors; **Server**, **Agents**, **Labwc**, and full OS root rollback
> remain **Planned**.

## 1. Pick your starting path

| Your setup | Safe path | Time | Key caveat |
| --- | --- | --- | --- |
| **Windows 10/11** | VM (ISO/QCOW2) or USB | 20m | No VirtualBox 3D; Rufus DD |
| **macOS (M1–M4)** | x86_64 PC or KVM | — | Slow x86_64 CPU emulation |
| **macOS (Intel)** | VMware or USB | 20m | Verify ISO via `shasum -a 256` |
| **Arch Linux** | AUR packages | 10m | Never overwrites dotfiles |

### Windows: try safely without touching Windows

You do **not** need to resize partitions or wipe Windows to test HorneroOS.

#### Option A — Virtual machine on Windows (ISO or QCOW2)

Both signed `v0.2.0-preview42` artifacts are available as direct downloads
from [horneroos.com/install](https://www.horneroos.com/install) and
[GitHub Releases](https://github.com/HorneroOS/hornero/releases/tag/v0.2.0-preview42)
(GPG key `FCFBEE43925AB5429362278AE59EAB44AA2498DC`):

- **Official Live & Installable ISO (`3.3 GiB`, UEFI + Legacy BIOS, validated
  on physical hardware & KVM):**
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/iso/horneroos-2026.11-preview42-x86_64.iso`
  - SHA-256:
    `9e494ab5f9783df6a5986385421ec0816b0033d3558d3323248a03e07f2e76a2`
- **Official Preinstalled Desktop QCOW2 (`2.61 GiB`, E2E-validated in UEFI
  KVM):**
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/vm/horneroos-0.2.0-preview42-desktop-qemu-x86_64.qcow2.zst`
  - SHA-256:
    `c1012413227f407d0a312fad7d7a34f789922303db13c752a9a9ed1a324e13c2`

1. Download the `3.3 GiB` ISO (`horneroos-2026.11-preview42-x86_64.iso`) and
   its `.sha256` file from [horneroos.com/install](https://www.horneroos.com/install)
   (or download the `2.61 GiB` `.qcow2.zst` for QEMU/KVM hosts).
2. Verify the download in PowerShell or Command Prompt before mounting it:

   ```powershell
   CertUtil -hashfile horneroos-2026.11-preview42-x86_64.iso SHA256
   ```

   Compare the output against the downloaded `.sha256` file (`9e494ab5...`).
3. **Recommended on Windows — VMware Workstation Pro** (free for personal use):
   create a new **Linux → Other Linux 6.x kernel 64-bit** VM with **UEFI**
   firmware, **4 GiB+ RAM**, **4 CPU cores**, **32 GiB** virtual disk, and
   **Accelerate 3D graphics** enabled.
4. **VirtualBox fallback:** create a **64-bit Arch Linux** VM with **Enable EFI**
   checked, **4 GiB+ RAM**, **4 CPUs**, **128 MB Video Memory**, and
   **uncheck "Enable 3D Acceleration"** (VMSVGA 3D causes black screens under
   Hyprland). Inside the guest session, export:

   ```sh
   export LIBGL_ALWAYS_SOFTWARE=1
   export QT_QUICK_BACKEND=software
   ```

#### Option B — Live USB from Windows

1. Confirm your **BitLocker recovery key** is backed up and disable **Windows
   Fast Startup** if you ever plan to dual-boot later.
2. Disable **Secure Boot** in UEFI firmware (HorneroOS does not ship signed
   Secure Boot shims yet).
3. Flash the verified ISO using **Rufus** (when prompted, pick **Write in DD
   Image mode**, not ISO Image mode) or **balenaEtcher**.
4. Boot from USB. Nothing touches your Windows drive unless you open Calamares
   and confirm partitioning. If your GPU shows a black screen, pick **Safe
   Graphics** in the boot menu (`nomodeset WLR_RENDERER=pixman`).

### macOS: honest Apple Silicon (M1–M4) guidance

Read this **before** downloading the `3.3 GiB` ISO on a Mac:

- **Apple Silicon (`M1`–`M4`) Macs:** HorneroOS publishes **`x86_64` images
  only**. `Hypervisor.framework` cannot hardware-virtualize `x86_64` on ARM64,
  so UTM falls back to **QEMU TCG software CPU emulation** and runs
  painfully slow. Native ARM64 and Parallels FEX are unsupported.
- **What to do on Apple Silicon instead:** Test on an `x86_64` PC via Live USB,
  self-host `HorneroOS/playground` on any Linux box with `/dev/kvm`, or wait for
  a hosted public Browser Playground cluster.
- **Intel Macs:** VMware Fusion (free for personal use) can boot the `x86_64`
  ISO with UEFI and 3D acceleration enabled.
- **Making a Live USB on macOS** (for an `x86_64` machine): verify with
  built-in `shasum`:

  ```sh
  shasum -a 256 horneroos-2026.11-preview42-x86_64.iso
  ```

### Existing Arch Linux: AUR packages & inspection

If you already run updated `x86_64` Arch Linux, you can evaluate Hornero
Signal, Hornero Apps, Hornero Welcome, and `horneroctl` without reinstalling.
See the full steps in [Install on Arch](install-on-arch.md).

1. **Inspect before building:** Review each AUR recipe directly:
   - [`hornero-shell`](https://aur.archlinux.org/packages/hornero-shell)
   - [`hornero-config`](https://aur.archlinux.org/packages/hornero-config)
   - [`horneroctl-bin`](https://aur.archlinux.org/packages/horneroctl-bin)
     (verifies upstream release signatures against GPG key
     `FCFBEE43925AB5429362278AE59EAB44AA2498DC`)
   - [`hornero-greeter`](https://aur.archlinux.org/packages/hornero-greeter)
     (SDDM theme) or
     [`hornero-greeter-greetd`](https://aur.archlinux.org/packages/hornero-greeter-greetd)
     (for `greetd` users; pick the one matching your display manager)
2. **Back up and install:**

   ```sh
   tar -czf ~/hornero-pre-adopt-$(date +%F).tar.gz \
     ~/.config/hypr ~/.config/kitty ~/.config/ghostty \
     ~/.config/environment.d 2>/dev/null
   yay -Syu hornero-shell
   ```

3. **Dry-run seeding and verify:**

   ```sh
   /usr/share/hornero/seed-user.sh --dest "$HOME" --dry-run
   /usr/share/hornero/seed-user.sh --dest "$HOME"
   horneroctl doctor
   ```

4. **Test inside your existing Hyprland session** without adopting defaults:

   ```sh
   horneroctl shell start --yes
   ```

## 2. Known issues & honest limitations

Verify these constraints against your workflow before adopting daily:

- **Physical-hardware + KVM validation & growing hardware matrix:**
  HorneroOS runs daily in production across multiple physical workstations,
  and `v0.2.0-preview42` passed both UEFI and Legacy BIOS KVM validation.
  Per-device combinations (specific NVIDIA hybrid laptops, handhelds, audio
  interfaces) are tracked openly in
  [Tested and untested](../hardware/tested-and-untested.md).
- **No OS root rollback yet:** Every current build reports snapshot backend
  `none`. `horneroctl recovery doctor` is read-only diagnostics, and
  `horneroctl config snapshot` archives Hornero settings only—never `/`, the
  kernel, or `pacman` transactions. See
  [Updates and recovery](../desktop/updates-and-rollback.md).
- **Public Browser Playground is on standby:** `HorneroOS/playground` defaults
  to `standby-awaiting-provider` ($0/month cloud commitment) until a public
  cluster provider is funded and configured. Self-hosting works today on any
  Linux host with `/dev/kvm`.
- **VirtualBox 3D & Hyper-V limitations:** VirtualBox `VMSVGA` 3D causes
  Hyprland/Niri black screens; Hyper-V Linux VMs lack native VirGL and fall back
  to `llvmpipe` software rendering.
- **Apple Silicon `x86_64` slowness:** No ARM64 build exists yet; UTM falls
  back to QEMU TCG CPU emulation.
- **Compositor boundaries & Planned items:** **Hyprland** is the default
  compositor and **Niri** is supported as a scrolling Wayland compositor
  (features that rely on Hyprland-only protocols such as fullscreen Gaming mode
  detection or Hyprland scratchpads are documented in
  [Wayland compositors](../desktop/compositors.md)); **Server**, **Agents**,
  and **Labwc** remain **Planned** with no bootable images; **Secure Boot**
  requires disabling in firmware or self-enrolling keys.

## 3. Practical troubleshooting

Start every triage session with read-only checks and keep the first error:

```sh
horneroctl doctor
horneroctl config validate
```

### Boot black screen or installer boot failure

- Choose the **Safe Graphics** entry on the live ISO boot menu
  (`nomodeset WLR_RENDERER=pixman`).
- After installing, if a kernel update fails to boot, pick the fallback kernel in
  GRUB advanced options (`kernel-and-fallback`) and inspect the previous boot:

  ```sh
  journalctl -b -1 --no-pager
  ```

- If an internal NVMe drive is invisible in Calamares on an Intel laptop, switch
  Intel VMD / RST to AHCI in UEFI firmware (back up Windows first if dual
  booting).

### Wayland, NVIDIA, and VM cursor or black-screen fixes

- **VM cursor invisible or black screen (QEMU/VMware/VirtualBox):**
  - On **VirtualBox**, uncheck **Enable 3D Acceleration** and set
    `LIBGL_ALWAYS_SOFTWARE=1` + `QT_QUICK_BACKEND=software`.
  - On **VMware**, ensure `Accelerate 3D graphics` is enabled; if Quickshell
    opens blank, test `QSG_RHI_BACKEND=opengl` or `QSG_RHI_BACKEND=software`.
  - On **QEMU/KVM**, use OVMF UEFI + `-device virtio-vga-gl` (`VirGL`).
- **NVIDIA / hybrid laptops:** HorneroOS does not ship a custom NVIDIA driver
  installer. Follow [Hybrid graphics and NVIDIA](../hardware/hybrid-graphics-nvidia.md)
  to confirm `nvidia-dkms` / `nvidia-open-dkms` and `nvidia_drm.modeset=1`.
- **Shell or Control Center pane blank:**

  ```sh
  horneroctl shell status --json
  horneroctl shell logs --lines 120
  ```

### Flatpak and Flathub setup (`Hornero Apps`)

Verify store health, active sources, and Flathub connectivity:

```sh
horneroctl store doctor
horneroctl store sources
```

If Flathub is missing on a custom Arch install, add it for your user or system:

```sh
flatpak remote-add --if-not-exists flathub \
  https://dl.flathub.org/repo/flathub.flatpakrepo
```

See [Hornero Apps](../desktop/hornero-apps.md) for provenance badges
(`Official`, `Verified`, `Community`, `Web App`) and `horneroctl store policy`.

### PipeWire audio recovery

Confirm audio services and Studio routing before editing config files:

```sh
horneroctl studio doctor
horneroctl studio routing status
systemctl --user status pipewire pipewire-pulse wireplumber
```

If you enabled a Studio live-routing kit and want clean desktop audio back:

```sh
horneroctl studio routing disable live-call
systemctl --user restart pipewire pipewire-pulse wireplumber
```

## 4. Reporting bugs, hardware, security, and team adoption

### Report a bug

Open an issue in the repository that owns the component (`shell`, `config`,
`hornero`, `installer`, `docs`, `website`) via its issue chooser, attaching
sanitized `horneroctl doctor` output and the first error lines. Never include
usernames, LAN IPs, tokens, or personal logs. See
[Report a bug](../development/README.md#report-a-bug).

### Submit a hardware compatibility report

Community bare-metal reports expand our compatibility matrix across diverse
laptops, desktops, and GPUs. Use the **Hardware Compatibility Report** issue
template (available across HorneroOS repositories via `HorneroOS/.github`) and
attach sanitized output from:

```sh
horneroctl doctor
lspci -nnk
journalctl -b -k -p warning --no-pager
```

Include your exact ISO or AUR package versions, firmware mode (UEFI/BIOS),
LUKS encryption choice, edition, and compositor.

### Report a security vulnerability

**Never open a public GitHub issue or PR for a security bug.** Follow
[`SECURITY.md`](https://github.com/HorneroOS/.github/blob/main/SECURITY.md): use
**Security → Report a vulnerability** on the affected repository, or request a
private channel through the organization owners.

### Adopt HorneroOS upstream in teams (without private forks)

Organizations and labs can standardize workstations while staying cleanly on
upstream packages:

- **Lock software provenance:** Enforce `verified-only` or curated rules via
  `horneroctl store policy` and export reproducible setups with
  `horneroctl store manifest` ([Hornero Apps](../desktop/hornero-apps.md)).
- **Layer user/team Hyprland overrides:** Keep `/etc/xdg/hypr/hyprland.lua.d/`
  package-managed and place team customizations in `*-user.lua`
  ([Install on Arch](install-on-arch.md)).
- **Share reproducible workstation profiles:** Capture and apply experience,
  audio routing, power, and extension profiles with `horneroctl profile`
  ([Profiles & Snapshots](../desktop/profiles-snapshots.md)).
- **Self-host Playground:** Run `HorneroOS/playground` on internal KVM hardware
  for isolated team onboarding ([Infrastructure](../infrastructure/README.md)).

> **Support expectation:** HorneroOS is an open-source community project with
> **no commercial SLAs or guaranteed response times**.
