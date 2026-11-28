# Cloud provider decision kit for Hornero Playground

- **Last verified:** `2026-11-28`
- **Tracking:** `HorneroOS/playground#1`, `HorneroOS/docs`
- **Cost model helper:** `HorneroOS/playground/tools/cost_calculator.py`

This decision kit compares every evaluated hosting and sponsorship path for
running the **HorneroOS Browser Playground** (`x86_64` Arch Linux + Hyprland /
Niri + Quickshell + PipeWire over WebRTC). Every interactive slot requires
**2–4 vCPU threads**, **4096 MiB guest RAM** (plus **1200 MiB** host VirGL
cgroup overhead, zero swap), and hardware `/dev/kvm`.

---

## Zero-spending commitment

**HorneroOS makes no recurring cloud spending commitment by default.**

1. **Phase 1 ships at $0/month** using downloadable signed `.qcow2.zst` VMs,
   Quickemu (`horneroos.conf`), `hornero-vm-run.sh`, and a DistroSea discovery
   listing (`distrosea.com/contact/`).
2. **Hosted WebRTC slots remain behind a feature flag** on
   `https://www.horneroos.com/try` until maintainers explicitly authorize a
   budget tier or receive approved open-source hosting/credits.
3. **Self-hosting stays portable:** any Linux host with `/dev/kvm` can run the
   same `HorneroOS/playground` orchestrator and Terraform modules without
   vendor lock-in.

---

## Verified provider comparison matrix (2026-11-28)

### Hardware, virtualization, GPU, and bandwidth

| Provider | KVM | Nested | GPU / VirGL | Specs & Bandwidth |
| --- | --- | --- | --- | --- |
| **DistroSea** | `noVNC` | N/A | **None** | Shared ISO queue; no audio |
| **AWS Credits** | `.metal` | N/A | None (`c7i`) | Per-EC2; AWS egress |
| **OSUOSL** | OpenStack | Policy | **None** (VM) | Project VM; academic net |
| **GCP `n2-std`** | L1 KVM | **Yes** | **None** | 16c/64G; $0.12/G egress |
| **AWS `.metal`** | L0 KVM | L0 | **None** | 96c/192G; AWS egress |
| **OVH `KS-1/2/A`** | L0 KVM | L0 | **None** | 4–8c/32–64G; 100–500M |
| **OVH `RISE-1`** | L0 KVM | L0 | Intel UHD | 6c/12t/32G+; 1G unlim |
| **Hetzner `AX42`** | L0 KVM | L0 | **Radeon** | 8c/16t/64G; 1G unlim |
| **Hetzner `EX44`** | L0 KVM | L0 | Intel UHD | 14c/20t/64G; 1G unlim |
| **Hetzner `AX52`** | L0 KVM | L0 | Ryzen iGPU | 8c/16t/64G; 1G unlim |

### Pricing, contracts, regions, AUP, and sponsorship

| Provider | Price (excl. VAT) | Term | Region | AUP & Eligibility |
| --- | --- | --- | --- | --- |
| **DistroSea** | **$0** | None | EU/US | ISO via contact |
| **AWS Credits** | Promo credits | Expiry | `sa`/`us-e1` | OSI + paid acct |
| **OSUOSL** | **$0** (grant) | Review | US-West | OSI + FOSS impact |
| **GCP `n2-std`** | ~$567–$900/m | On-dem | `sa`/`us-e1` | No IMDS/SMTP |
| **AWS `.metal`** | **$4.284/hr** | On-dem | `sa`/`us-e1` | Credits ok; $3.1k |
| **OVH `KS-1/2/A`** | ~$19–$55 + 1m | Month | EU/CA/AP | Anti-spam; low stock |
| **OVH `RISE-1`** | ~$64–$67/mo | 1m/12m | CA/FR | 12m waives setup |
| **Hetzner `AX42`** | **€46–€99**+€49 | Month | `FSN1`/`HEL1` | Zero abuse |
| **Hetzner `EX44`** | **€59/m**, **€0** | Month | `FSN1`/`HEL1` | Zero abuse |
| **Hetzner `AX52`** | ~€59–€83.7/m | Month | `FSN1`/`NBG1` | Zero abuse AUP |

### Provider verification notes and official URLs (`2026-11-28`)

- **DistroSea** ([distrosea.com](https://distrosea.com/),
  [distrosea.com/contact/](https://distrosea.com/contact/)): Free managed
  `noVNC` discovery queue; lacks 3D VirGL acceleration and audio.
- **AWS Cloud Credits for Open Source**
  ([aws.amazon.com/government-education/open-source/](https://aws.amazon.com/government-education/open-source/)):
  Requires an OSI-approved license, active maintenance and community, non-vendor
  dominance, and an active AWS account with a valid payment method (credits are
  non-retroactive). Submit the application form to
  `awsopensourcecredits@amazon.com`; monthly review pauses issuance in December.
  Even if awarded, AWS `.metal` (`c7i.metal-24xl` at `$4.284/hr`,
  `~$3,127/mo`, [c7i specs](https://aws.amazon.com/ec2/instance-types/c7i/))
  exhausts modest credit grants quickly.
- **OSU Open Source Lab (OSUOSL)**
  ([osuosl.org/services/hosting/](https://osuosl.org/services/hosting/)):
  Sponsored FOSS hosting for OSI-licensed, open-development projects with
  strong community impact. The `x86_64` OpenStack/KVM cluster targets
  production services (while AArch64 and OpenPOWER target cross-arch CI).
  Shared OpenStack VMs expose no physical GPU for VirGL, making OSUOSL better
  suited for control-plane, mirrors, or CI unless dedicated hardware is granted.
- **Google Cloud (`n2-standard-16`)**
  ([nested virtualization](https://cloud.google.com/compute/docs/instances/nested-virtualization/overview)):
  16 vCPU, 64 GiB RAM with nested KVM enabled at `$0` extra surcharge (incurs
  `>=10%` L1->L2 CPU/IO overhead and no physical iGPU). On-demand rates are
  `~$0.777/hr` (`~$567/mo`) in `us-east1` vs `~$1.233/hr` (`~$900/mo`) in
  `southamerica-east1`; Spot drops to `~$0.08–$0.31/hr`. Premium internet egress
  is `$0.12/GiB` (first 1 TB) and SA<->US inter-region is `$0.14/GiB`.
- **OVHcloud Eco / Kimsufi & Rise**
  ([eco.ovhcloud.com](https://eco.ovhcloud.com/)): `KS-1` (Xeon-D 1520, 4c/8t,
  32 GB, `~$18.80/mo`), `KS-2` (Xeon-D 1540, 8c/16t, 32–64 GB, `~$21.10/mo`),
  and `KS-A` (i7-6700K, 32 GB, `~€/$54.99/mo`, APAC/Singapore with 100 Mbps /
  5 TB cap) carry a 1-month setup fee and depend heavily on live stock.
  `RISE-1` (Xeon-E 2386G, 6c/12t, 32–128 GB ECC, 2x512 GB NVMe, `~$64–$67/mo`,
  1 Gbps unmetered + 1 Gbps vRack) waives setup on a 12-month commitment.
- **Hetzner Dedicated (`AX42`, `EX44`, `AX52`)**
  ([hetzner.com/dedicated-rootserver](https://www.hetzner.com/dedicated-rootserver/)):
  Bare-metal L0 KVM with a 1 Gbit/s unlimited standard uplink (10 Gbit/s
  upgrades cap at 20 TB) and monthly billing. `AX42` (Ryzen 7 PRO 8700GE +
  Radeon iGPU, 64 GB DDR5 ECC, 2x512 GB NVMe, `€46–€99/mo` + `€49` setup) backs
  VirGL directly on the host iGPU; `EX44` (Core i5-13500, 14c/20t, 64 GB DDR4,
  `€59/mo`, `€0` setup) maximizes thread density; `AX52` (`~€59–€83.70/mo`)
  adds 2x1 TB NVMe in `FSN1`/`NBG1`/`HEL1`.

---

## Latency from Argentina (Buenos Aires)

HorneroOS maintainers work from Argentina, so interactive WebRTC RTT from
Buenos Aires directly affects evaluation UX:

| Region / Hub | RTT (Buenos Aires) | WebRTC UX |
| --- | --- | --- |
| **São Paulo** (`sa-east-1`) | **~25–35 ms** | Near-local feel |
| **US-East** (`us-east-1`) | **~130–150 ms** | Responsive demos |
| **EU West** (Paris / Gravelines) | **~220–235 ms** | Slight drag lag |
| **EU Central** (Falkenstein `FSN1`) | **~225–240 ms** | Best cost/FPS |
| **EU North** (Helsinki `HEL1`) | **~245–260 ms** | Higher RTT (EU fit) |

For **zero-latency (0 ms)** evaluation of 60 FPS Hyprland/Niri animations,
prefer local VirGL VMs via Quickemu or `hornero-vm-run.sh` (see
[Try HorneroOS without installing](../getting-started/try-horneroos.md)).

---

## Budget scenario analysis

Use `HorneroOS/playground/tools/cost_calculator.py` to model slot count, egress,
and monthly cost against your target concurrency. Each active slot reserves
**4 GiB RAM + 2–4 threads**.

| Budget | Setup | Slots | Unviable / Rejected |
| --- | --- | --- | --- |
| **$0** | Local QCOW2 + R2 + DistroSea | 0 | AWS `.metal`; GCP |
| **~$25/mo** | OVH `KS-1/2` control/cpu | ~4–6 | AWS `.metal`; no VirGL |
| **~$50/mo** | **Hetzner `AX42`** (€46+€49) | **8–12** | AWS `.metal`; GCP |
| **~$100/mo** | **Hetzner `EX44`** (€59)+R2 | **10–14** | AWS `.metal` (>30×) |
| **~$200/mo** | 2–3× Hetzner + `coturn` | **20–36** | AWS `.metal` (>15×) |
| **Burst** | **GCP `n2-std-16` Spot** | 8–12 | Fixed GCP or `.metal` |

### Why AWS `.metal` is unviable for $25–$200/mo budgets

AWS EC2 does **not** offer small bare-metal instances with `/dev/kvm`. Standard
EC2 Nitro instances (`t3`, `c7i.large`, etc.) block nested KVM, forcing
operators onto `c7i.metal-24xl` (96 vCPU, 192 GiB RAM) at **$4.284/hr
(~$3,127/month)** on-demand before EBS storage and WebRTC egress. Even with a
72% Savings Plan, one `.metal` node remains **4×–40× over** a $25–$200/month
community budget.

---

## Ready-to-send DistroSea submission summary

The full maintainer-ready dossier lives in
[`HorneroOS/playground/distributions/distrosea-submission.md`](https://github.com/HorneroOS/playground/blob/main/distributions/distrosea-submission.md).
Submit through [distrosea.com/contact/](https://distrosea.com/contact/) with:

- **Distribution:** HorneroOS (`x86_64`, Arch Linux base, Hyprland, Quickshell,
  and SDDM `hornero-greeter`).
- **Release:** `v0.2.0-preview32` (`horneroos-2026.10-preview32-x86_64.iso`,
  2.7 GB / `2,931,294,208` bytes).
- **Direct ISO URL:**
  `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/iso/horneroos-2026.10-preview32-x86_64.iso`
- **SHA-256:**
  `b8cd0f8604bc69f7d2112fb8bccd97115d32d197e9c92c62e02faf5de6345aec` (with
  `.sha256` and `.sig` signed by `FCFBEE43925AB5429362278AE59EAB44AA2498DC`).
- **Boot & graphics note for DistroSea operators:** Supports UEFI
  (`systemd-boot`) and BIOS (`syslinux`), auto-logs into `hornero-live`
  (`Session=hyprland.desktop`). Without VirGL, pick the built-in **"HorneroOS
  (Safe Graphics)"** entry (`nomodeset WLR_RENDERER=pixman`) with >= 4096 MiB
  RAM and 2–4 vCPUs.
- **Role:** Zero-cost organic discovery listing linking visitors to WebRTC
  Playground and Quickemu/QCOW2 downloads, with upfront disclosure that `noVNC`
  has no audio and no 3D GPU acceleration.

## Related guides

- [Playground deployment runbook](playground-deployment-runbook.md)
- [ADR: Hornero Playground architecture](../architecture/adr-hornero-playground.md)
- [Hornero Playground threat model](../architecture/hornero-playground-threat-model.md)
- [Try HorneroOS without installing](../getting-started/try-horneroos.md)
