# Try HorneroOS without installing

You can test the real HorneroOS desktop—Hyprland, Hornero Shell, themes, bar
layouts, Hornero Welcome, and `horneroctl`—without wiping your disk or
repartitioning your computer. Every path on
[`horneroos.com/try`](https://www.horneroos.com/try) runs real HorneroOS
software, never a mocked browser simulation.

> **Honest status today:** HorneroOS is used daily in production across
> multiple physical workstations and validated in UEFI and Legacy BIOS KVM. The
> current signed release is **`v0.2.0-preview42`** (`x86_64`), bundling
> **Hornero Signal**, **Hornero Apps**, **Signal Flight Welcome (`v1.6.0`)**,
> **Chromatic v3**, and **Calamares `3.4.3`**. **Desktop**, **Studio**, and
> **Gaming** are **Supported** editions; **Hyprland** (default) and **Niri**
> are **Supported** Wayland compositors; **Server**, **Agents**, **Labwc**,
> and full OS root rollback remain **Planned**. See
> [Editions and package composition](../architecture/editions.md) and
> [Updates and recovery](../desktop/updates-and-rollback.md).

## Choose your path

| Path | Best for | Fidelity | Limit |
| --- | --- | --- | --- |
| **1. Browser** | Quick look | WebRTC (high) / `noVNC` (low) | 15 min |
| **2. Local VM** | Smooth 60 FPS desktop | Local VirGL (KVM) | Unlimited |
| **3. Live USB** | Real GPU, Wi-Fi, audio | Native hardware speed | Unlimited |

---

## 1. Try in your browser

### HorneroOS Browser Playground

The HorneroOS Browser Playground (`HorneroOS/playground`) spins up a fresh,
disposable Linux KVM virtual machine per visitor and streams the real Wayland
desktop and PipeWire audio straight to your browser over WebRTC.

- **Ephemeral by design:** Your session runs on a clean temporary copy-on-write
  disk with a **15-minute hard limit** (and an idle timeout). When you close
  the tab or time runs out, the virtual machine and everything inside it are
  deleted permanently.
- **Never enter real secrets:** Do not log into personal email, GitHub, cloud
  accounts, or paste private SSH/API keys inside a public browser session.
- **Honest availability note:** The hosted browser cluster is being rolled out
  under `HorneroOS/playground#1` with limited concurrent slots. If public
  slots are full or offline for maintenance, use **Path 2 (Preinstalled VM)**
  or self-host the stack on any Linux machine with `/dev/kvm`.

### Self-hosting the browser stack

If you run a Linux server or workstation with hardware KVM (`/dev/kvm`), you
can run the `HorneroOS/playground` orchestrator and WebRTC streamer locally for
team demos or workshops. See the
[Hornero Playground architecture](https://github.com/HorneroOS/playground) and
[security threat model](../architecture/hornero-playground-threat-model.md)
before exposing an instance on a public network.

### DistroSea (secondary discovery track)

HorneroOS also targets **DistroSea** (`distrosea.com`) as a zero-cost
discovery listing. Keep the difference in mind: DistroSea streams over
`noVNC` **without 3D GPU acceleration and without audio**, so Hyprland blur,
Chromatic transitions, and animations feel choppy compared to a local VM or
WebRTC Playground session.

---

## 2. Download a preinstalled virtual machine

Running HorneroOS in a local virtual machine gives you unlimited time, full
keyboard control, and smooth performance without touching your host system.
For `v0.2.0-preview42`, HorneroOS publishes **both** a clean-room preinstalled
Desktop QCOW2 image and a full live & installable ISO:

- **Official Preinstalled Desktop QCOW2 (`2.61 GiB`, E2E-validated in UEFI
  KVM):**
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/vm/horneroos-0.2.0-preview42-desktop-qemu-x86_64.qcow2.zst`
  - SHA-256:
    `c1012413227f407d0a312fad7d7a34f789922303db13c752a9a9ed1a324e13c2`
- **Official Live & Installable ISO (`3.3 GiB`, UEFI + Legacy BIOS, validated
  on physical hardware & KVM):**
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/iso/horneroos-2026.11-preview42-x86_64.iso`
  - SHA-256:
    `9e494ab5f9783df6a5986385421ec0816b0033d3558d3323248a03e07f2e76a2`

Decompress the `.qcow2.zst` image with `unzstd` (or `zstd -d`) before
attaching it to QEMU/KVM, Quickemu, or `libvirt`.

### Verify before booting

Every official HorneroOS image ships with `SHA256SUMS` (or `.sha256`) and a
detached GPG `.sig` signed by the HorneroOS releases key
(`FCFBEE43925AB5429362278AE59EAB44AA2498DC`). Follow the verification commands
in [Getting started](README.md) before launching any downloaded disk or ISO.

### Recommended VM sizing

- **RAM:** 4 GiB minimum (6–8 GiB recommended if opening Studio or browsers)
- **CPU:** 4 vCPUs
- **Disk:** 32 GiB dynamic QCOW2/VDI (when installing inside the VM)
- **Firmware:** UEFI (OVMF)

### QEMU / KVM on Linux (fastest, 1-command launcher)

On Linux with `/dev/kvm` and `qemu-system-x86_64`, VirGL (`virtio-vga-gl`)
accelerates Hyprland, Niri, and Quickshell directly on your host GPU.
`HorneroOS/playground` provides a one-command launcher (`hornero-vm-run.sh`),
or you can boot directly with OVMF UEFI and VirGL:

```sh
./hornero-vm-run.sh horneroos-0.2.0-preview42-desktop-qemu-x86_64.qcow2
```

If launching QEMU manually with an ISO or preinstalled QCOW2, enable KVM,
`q35`, OVMF UEFI, and `-device virtio-vga-gl` with `-display gtk,gl=on`.

### Quickemu (`horneroos.conf`)

If you use [Quickemu](https://github.com/quickemu-project/quickemu), drop a
`horneroos.conf` file next to your image and start it in one command:

```sh
cat <<'EOF' > horneroos.conf
guest_os="linux"
disk_img="horneroos/horneroos-0.2.0-preview42-desktop-qemu-x86_64.qcow2"
disk_size="32G"
ram="4G"
cpu_cores="4"
boot="efi"
gl="on"
preallocation="metadata"
EOF

quickemu --vm horneroos.conf
```

*(If booting the live ISO instead of the prebuilt Desktop QCOW2, add
`iso="horneroos/horneroos-2026.11-preview42-x86_64.iso"`.)*

### libvirt / `virt-manager` / GNOME Boxes

1. Create a new VM from an existing disk image (`.qcow2`) or the verified ISO.
2. Select **UEFI** firmware (`OVMF_CODE.4m.fd`) rather than legacy BIOS.
3. Allocate at least **4096 MiB RAM** and **4 vCPUs**.
4. Use **VirtIO** for disk and network, and set Video to **Virtio** with **3D
   acceleration** enabled (Spice/GTK OpenGL display).

### VMware Workstation / Fusion (Linux, Windows, Intel Mac)

VMware Workstation Pro and Fusion are free for personal use and expose the
upstream `vmwgfx` (`SVGA3D`) Linux driver, which handles Wayland compositors
much more reliably than VirtualBox:

1. Import the `.ova` appliance (or create a 64-bit Arch Linux UEFI VM from the
   ISO).
2. Give it **4 GiB RAM**, **4 CPU cores**, and enable **Accelerate 3D
   graphics**.
3. If Quickshell ever renders a blank screen on your host GPU driver, test
   `QSG_RHI_BACKEND=opengl` or `QSG_RHI_BACKEND=software` in your guest session.

### Oracle VirtualBox (software fallback required)

VirtualBox's `VMSVGA` 3D acceleration currently causes black screens or
immediate crashes under Hyprland and Niri. If VirtualBox is your only option:

1. Create a **64-bit Arch Linux** VM with **UEFI enabled**, **4 GiB RAM**, and
   **4 CPUs**.
2. **Uncheck "Enable 3D Acceleration"** in Display settings and set Video
   Memory to **128 MB**.
3. Install `virtualbox-guest-utils` (and enable `vboxservice.service`) if
   installing inside the VM, and use software rendering fallback:
   `LIBGL_ALWAYS_SOFTWARE=1` and `QT_QUICK_BACKEND=software`.

Expect noticeably slower animations and higher CPU usage in this mode.

### macOS UTM (honest Apple Silicon caveat)

HorneroOS currently builds **`x86_64` images only**. Because Apple Silicon
(`M1`–`M4`) Macs cannot hardware-virtualize `x86_64` through
`Hypervisor.framework`, **UTM falls back to QEMU TCG software CPU emulation**.
Even with UTM's VirGL renderer (`virtio-gpu-gl`), Hyprland, Niri, and Quickshell
will feel **painfully slow** on Apple Silicon UTM.

For a real impression of HorneroOS on a Mac, use an x86_64 machine with a
Live USB or a hosted browser Playground session when available.

---

## 3. Try on your own hardware (Live USB)

Booting the official signed ISO from a USB stick lets you test real Wi-Fi,
audio, displays, and input devices in memory without modifying your drives:

1. **Download and verify** `horneroos-2026.11-preview42-x86_64.iso` (`.sig` +
   `.sha256`) using the commands in [Getting started](README.md).
2. **Write to USB** with a trusted graphical writer or `dd` after confirming
   your stick's device name with `lsblk`:

   ```sh
   sudo dd if=horneroos-2026.11-preview42-x86_64.iso of=/dev/sdX bs=4M \
     status=progress conv=fsync
   ```

3. **Boot from USB:** Disable Secure Boot in your firmware if blocked. If your
   GPU hits a black screen on normal boot, pick the **Safe Graphics** entry in
   the boot menu (`nomodeset WLR_RENDERER=pixman`).
4. **Explore safely:** The live session auto-logs into Hyprland as
   `hornero-live` with idle screen lock disabled. Try **Hornero Welcome**,
   switch themes and layouts, inspect the desktop, and check system health with:

   ```sh
   horneroctl doctor
   horneroctl version
   ```

5. **Install only if you decide to:** Nothing touches your internal disk until
   you open the Calamares installer and confirm partitioning. Follow
   [Installing HorneroOS step by step](install-step-by-step.md) (or
   [Install on Arch](install-on-arch.md) if you already run Arch Linux).

---

## 4. Presenter and recording mode

When recording demos, screenshots, or live walkthroughs inside HorneroOS, hide
distracting notifications and keep the screen clean without permanently
altering your settings:

- **Presenter overlay (`HorneroOS/playground`):** Inside Playground images or
  sessions with the presenter helper installed, toggle clean demo mode on or
  off with:

  ```sh
  hornero-presenter on
  hornero-presenter off
  ```

- **Shipped Shell Do Not Disturb IPC:** On any HorneroOS desktop (including
  existing installs), toggle notification Do Not Disturb directly via
  Quickshell IPC and switch to Focus mode:

  ```sh
  qs ipc call notifs enableDnd
  qs ipc call notifs isDndEnabled
  horneroctl mode set focus
  ```

  Restore normal notifications and Signal mode when finished:

  ```sh
  qs ipc call notifs disableDnd
  horneroctl mode set signal
  ```

- **Built-in capture commands:** Take screenshots or recordings directly with:

  ```sh
  horneroctl capture screenshot
  horneroctl capture record
  ```

- **Clean capture tips:**
  - Use **1920×1080** (1080p) or **1280×800** at 60 FPS for crisp readable UI
    scaling.
  - Run `qs ipc call notifs clear` before recording to clear old banners.
  - Strip usernames, private paths, network names, and tokens before
    publishing clips or logs (see [Security and privacy](../security/README.md)).

## Related guides

- [Getting started](README.md) — ISO download, GPG verification, and limits
- [Installing HorneroOS step by step](install-step-by-step.md) — Calamares
  walkthrough
- [Installing HorneroOS on an existing Arch Linux system](install-on-arch.md)
- [Hornero Welcome](../desktop/hornero-welcome.md) and
  [Hornero Apps](../desktop/hornero-apps.md)
- [ADR: Hornero Playground architecture](../architecture/adr-hornero-playground.md)
- [Hornero Playground threat model](../architecture/hornero-playground-threat-model.md)
