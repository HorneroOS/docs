# Virtual workstations, display profiles, and screenshot factory

- **Official visual baseline:** Full HD **`1920×1080` (`16:9`, scale `1.0`,
  `60 Hz`)**
- **Canonical VM builder:** `HorneroOS/installer/scripts/build-vm-image.sh`
- **Acceptance & capture engine:** `HorneroOS/qa` (`hornero-qa`)

This guide explains how HorneroOS contributors build reproducible preinstalled
QCOW2 virtual workstations, verify hypervisor compatibility across Linux,
Windows, and macOS, author Screenshot Factory and Demo Studio scenarios, and
navigate the six release automation CI tiers.

---

## 1. Visual baseline and 7 display profiles

All flagship captures, showroom assets, and YouTube masters standardize on
**Full HD `1920×1080`** at scale `1.0` so Hornero Signal typography (IBM Plex)
and bar proportions stay consistent across `HorneroOS/qa`, `HorneroOS/website`,
and `HorneroOS/playground`.

| # | Profile ID | Size | Scale | Primary Use |
| --- | --- | --- | --- | --- |
| 1 | `fhd-baseline` | `1920×1080` | `1.0` | Flagship captures, YouTube |
| 2 | `laptop-1280x800` | `1280×800` | `1.0` | Playground, fast QA smoke |
| 3 | `wxga-1366x768` | `1366×768` | `1.0` | Narrow-screen regression |
| 4 | `qhd-2560x1440` | `2560×1440` | `1.0` | Multi-window coding / DAW |
| 5 | `uhd-4k-scaled` | `3840×2160` | `1.5`/`2` | HiDPI scaling & 4K demos |
| 6 | `vertical-shorts` | `1080×1920` | `1.0` | YouTube Shorts & Reels |
| 7 | `dual-mixed-dpi` | `1080p`+`800p` | Mixed | Multi-monitor QA |

> **Lua monitor pin note (`HorneroOS/qa`):** Inside Hyprland Lua QA guests,
> `qa/guest/hyprland.lua` pins `Virtual-1` to `1280×800`. When authoring a
> `1920×1080` or `1366×768` scenario, update both `requires.resolution` and an
> explicit `hyprctl eval 'hl.monitor({ output = "Virtual-1", mode =
> "1920x1080@60", position = "0x0", scale = 1 })'` step in `setup.commands`.

---

## 2. Building official preinstalled QCOW2 VMs & 6 image profiles

HorneroOS builds preinstalled VM disks deterministically from
`HorneroOS/installer/installer.lock.yaml` and
`HorneroOS/hornero/editions/catalogue.yaml` using **`arch-install-scripts`
(`pacstrap`)** (the Arch `arch-boxes` pattern). It **never** uses fragile
Packer `boot_command` keystroke scripts and **never** clones a developer's
machine.

```sh
# Preview deterministic build plan and resolved package list without root
./scripts/build-vm-image.sh \
  --edition desktop \
  --compositor hyprland \
  --demo \
  --dry-run

# Build compressed Playground demo QCOW2 (.qcow2.zst + .sha256 + .manifest.json)
sudo ./scripts/build-vm-image.sh \
  --edition desktop \
  --compositor hyprland \
  --demo \
  --disk-size 24G \
  --output-dir ./output
```

Key flags in `HorneroOS/installer/scripts/build-vm-image.sh`:

- `--edition`: `desktop | studio | gaming`
- `--compositor`: `hyprland | niri`
- `--demo`: embeds `hornero-playground-demo` (`hornero` autologin, idle lock
  disabled, seeded `/home/hornero/Workspace`)
- `--disk-size`: e.g. `24G` or `32G`
- `--no-compress`: emits uncompressed `.qcow2` (faster local QEMU/QA iteration)
- `--dry-run`: prints JSON plan and package closure without root or disk writes

### Six official image profiles

| # | Profile | Edition | Comp. | Demo | Purpose |
| --- | --- | --- | --- | --- | --- |
| 1 | `desktop-hyprland` | `desktop` | `hypr` | No | Standard `.qcow2.zst` |
| 2 | `desktop-niri` | `desktop` | `niri` | No | Exp. Niri `.qcow2.zst` |
| 3 | `studio-hyprland` | `studio` | `hypr` | No | Studio disk |
| 4 | `gaming-hyprland` | `gaming` | `hypr` | No | Gaming (VM only) |
| 5 | `playground-demo` | `desktop` | `hypr` | **Yes** | Playground / Demo |
| 6 | `qa-uncompressed` | Any | Any | Opt. | Raw `.qcow2` |

Every published archive exceeding GitHub's 2 GiB asset cap ships via external
object storage (Vercel Blob / Cloudflare R2) with `SHA256SUMS` and detached GPG
`.sig` signed by `FCFBEE43925AB5429362278AE59EAB44AA2498DC`.

---

## 3. Cross-hypervisor compatibility matrix

HorneroOS's Wayland stack (`hyprland 0.57.2-1` on **Aquamarine**, experimental
`niri` on **Smithay**, and **Quickshell** on **Qt 6**) requires functional
DRM/EGL or an explicit software fallback (last verified `2026-11-28`):

| Tier | Hypervisor / Host | Driver | UX Summary |
| --- | --- | --- | --- |
| **Tested** | **QEMU/KVM** | `virtio-vga-gl` | Best 60 FPS (VirGL) |
| **Tested** | **libvirt / `virt-mgr`** | VirtIO 3D | 60 FPS via `virgl` |
| **Tested** | **Quickemu** | `gl="on"` EFI | 1-command 60 FPS |
| **Compat.** | **VMware WS / Fusion** | `vmwgfx` | Usable; RHI if blank |
| **Compat.** | **GNOME Boxes** | VirtIO GL | Usable; basic UI |
| **Exp./SW** | **Oracle VirtualBox** | `VMSVGA` | Slow CPU `llvmpipe` |
| **Exp./SW** | **macOS UTM** (ARM) | QEMU **TCG** | Slow `x86_64` emu |
| **Exp./SW** | **Microsoft Hyper-V** | `hyperv_fb` | Slow; no Mesa 3D |
| **Unsupp.** | **ARM64 hosts** | N/A | `x86_64` only |
| **Unsupp.** | **Parallels (ARM)** | FEX `x86_64` | Slow + breaks Wayland |

*(Tier key: **Tested** = Officially tested; **Compat.** = Compatible with
limitations; **Exp./SW** = Experimental / Software fallback; **Unsupp.** =
Unsupported.)*

### Detailed hypervisor requirements and caveats

- **QEMU/KVM (`hornero-vm-run.sh`), libvirt, and Quickemu *(Officially
  tested)*:** Requires `/dev/kvm` and `/dev/dri/renderD*` for VirGL
  (`virtio-vga-gl`, `AQ_NO_MODIFIERS=1`, `QSG_RHI_BACKEND=opengl` injected by
  `hornero-vm-gpu-detect`). Venus (`venus=true`) requires Linux `>= 6.13`,
  QEMU `>= 9.2`, and Mesa `>= 24.2`.
- **VMware Workstation / Fusion & GNOME Boxes *(Compatible with
  limitations)*:** VMware (free for personal use) requires `svga.enable3d =
  "TRUE"`; if Quickshell blanks on `vmwgfx` EGL/dmabuf, export
  `QSG_RHI_BACKEND=opengl` or `software`. GNOME Boxes reuses libvirt/VirGL but
  exposes fewer custom OVMF/Venus controls.
- **Oracle VirtualBox *(Experimental / Software fallback)*:** Enabling 3D
  crashes or blanks Hyprland and Niri. Uncheck **Enable 3D Acceleration**, set
  128 MB VRAM, install `virtualbox-guest-utils`, and export
  `LIBGL_ALWAYS_SOFTWARE=1` + `QT_QUICK_BACKEND=software`.
- **macOS UTM *(Experimental / Software fallback)*:** On Apple Silicon
  (`M1`–`M4`), `Hypervisor.framework` cannot virtualize `x86_64`, so UTM runs
  QEMU TCG software CPU emulation (very slow even with ANGLE/MoltenVK VirGL).
  Intel Macs run at near-native CPU speed.
- **Microsoft Hyper-V *(Experimental / Software fallback)*:** Standard Gen 2
  Linux VMs lack an upstream Mesa Gallium3D driver (`virtio_gpu`/`vmwgfx`)
  and fall back to `hyperv_fb` + `llvmpipe`. Consumer GPU-P is unsupported for
  Linux Wayland guests, and Microsoft's `d3d12` Mesa bridge is WSL2/WSLg-only.
- **ARM64 native & Parallels on Apple Silicon *(Unsupported)*:** HorneroOS
  publishes `x86_64` builds only. Parallels' FEX-derived `x86_64` emulation is
  significantly slower than native ARM64, and Parallels Tools (dynamic resize,
  clipboard, drag-and-drop) break under Linux Wayland sessions, requiring X11.

---

## 4. Adding Screenshot Factory and Demo Studio scenarios

Screenshot and video assets follow a single rule: **real running HorneroOS
captures only**, never mockups or unverified renders.

1. **Choose the right owner repository:**
   - **QA & Screenshot Factory scenarios:** `HorneroOS/qa` under
     `scenarios/visual/` or `scenarios/playground/`.
   - **Product capture slots & shot list:** `HorneroOS/website`
     (`src/data/capture-slots.json`, `docs/CAPTURES.md`).
   - **YouTube / Demo Studio scripts:** `HorneroOS/playground` (`demo/`) and
     [YouTube production workflow](../studio/youtube-production-workflow.md).
2. **Author the scenario YAML in `HorneroOS/qa`:**
   - Pin `requires.resolution` (prefer `1920x1080` for showcase captures) and
     `requires.compositor` (`hyprland` or `niri`).
   - Configure clean state in `setup.commands` (e.g. `horneroctl appearance
     theme apply hornero-signal-night --yes`, `qs ipc call notifs enableDnd`,
     and `hyprctl eval 'hl.monitor(...)'` when changing resolution on Lua).
   - Never include personal paths, tokens, or real user directories.
3. **Validate statically before booting KVM:**

   ```sh
   uv run hornero-qa validate
   uv run hornero-qa matrix --check
   ```

4. **Execute in an isolated KVM window (`flock` serialized):**

   ```sh
   flock ~/.local/share/hornero-signal-mission/vm.lock \
     uv run hornero-qa run visual/populated-hornero-right-1920x1080
   ```

   Open every captured PNG in the run evidence bundle (`runs/<run-id>/`) to
   visually inspect typography, margins, and Contrast before ingesting into
   `HorneroOS/website`.

---

## 5. Release automation CI tiers

GitHub-hosted runners lack `/dev/kvm`, so HorneroOS separates **fast static
verification** from **KVM graphical qualification** across six CI tiers:

| Tier | Trigger | Host | Gates & Outputs |
| --- | --- | --- | --- |
| **1. PR** | Pull request | GitHub | `ruff`, `mypy`, lint, `--dry-run` |
| **2. `main`** | Merge | GitHub | Lock, truth, captures, i18n |
| **3. Nightly** | Cron | GH + KVM | 45-day alarm; KVM refresh |
| **4. RC** | Freeze | KVM host | `build-iso.sh`, VM builds, QA |
| **5. Release** | Tag | GH + sign | GPG `.sig`, `SHA256SUMS`, AUR, R2 |
| **6. Manual** | Dispatch | Operator | Live ISO, hardware, release-bump |

### Exact checks per tier

- **PR:** `ruff`, `mypy --strict`, `pytest`, `shellcheck`, `markdownlint`,
  `check-horneroctl-refs.py`, `check-i18n-links.py`, `check-installer.py`,
  `hornero-qa validate`, `hornero-qa matrix --check`, and
  `build-vm-image.sh --dry-run`.
- **`main`:** Composition lock checks plus website `check-release-truth`,
  `check-captures`, and `check-i18n`.
- **Nightly / Weekly:** `evidence-staleness.yml` runs `hornero-qa matrix
  --stale-days 45`; scheduled KVM windows refresh stale graphical bundles.
- **RC:** Immutable `manifests/` freeze, candidate ISO/QCOW2 builds, and
  disposable-VM `install/*`, `smoke/*`, and `scenarios/playground/` suites.
- **Release:** Signed with `FCFBEE43925AB5429362278AE59EAB44AA2498DC`,
  published to GitHub Releases/AUR + external object storage (>2 GiB) with an
  immutable checklist under `HorneroOS/hornero/releases/`.
- **Manual:** Live ISO releases (`installer/docs/release-iso.md`), physical
  `PELICANO-PARITY` / `studio-gate` / `gaming-gate` runs, and website
  `release-bump` / `sync-product-data`.

---

## Related guides

- [YouTube and content production workflow](../studio/youtube-production-workflow.md)
- [Try HorneroOS without installing](../getting-started/try-horneroos.md)
- [Testing HorneroOS changes](../development/testing.md)
- [Quality assurance and release engineering](../development/quality-and-releases.md)
