# Playground deployment runbook

- **Scope:** Production rollout of the hosted WebRTC **HorneroOS Browser
  Playground** (`HorneroOS/playground`)
- **Security baseline:** [Hornero Playground threat model](../architecture/hornero-playground-threat-model.md)
- **Provider selection:** [Cloud provider decision kit](cloud-provider-decision-kit.md)

This runbook defines what remains once maintainers choose a cloud or bare-metal
provider and documents the **19-step final cloud deployment sequence**,
including hardware validation and the emergency kill-switch.

---

## What remains after choosing a cloud provider?

Once a provider and budget tier are approved (defaulting to **$0/mo** until
maintainers authorize spend), six concrete tasks separate selection from launch:

1. **Confirm provider choice & budget authorization** (e.g. Hetzner Robot
   `AX42`/`EX44` primary or GCP Spot burst).
2. **Provision authorized infrastructure** via `HorneroOS/playground` Terraform
   modules and `cloud-init.yaml.tftpl`.
3. **Configure DNS & secrets outside git/Terraform state** (`playground.horneroos.com`,
   Turnstile, `coturn`, metrics bearer token, Cloudflare Tunnel).
4. **Deploy control plane and KVM worker nodes** with non-root QEMU, cgroups,
   and `nftables` egress isolation.
5. **Run hardware, KVM, VirGL, streaming, isolation, and Presenter smoke tests**
   using `HorneroOS/qa` `scenarios/playground/`.
6. **Flip the website feature flag** on `HorneroOS/website` (`/try`) and verify
   production end-to-end from an external browser.

---

## 19-step final cloud deployment runbook

### Phase A — Infrastructure, DNS, secrets, and TLS (Steps 1–5)

#### 1. Verify provider requirements

Confirm the target node provides `x86_64` CPU extensions (`vmx` or `svm`),
hardware `/dev/kvm`, >= 64 GiB RAM for 4–6 conservative VirGL slots (or 2–4
CPU-only `llvmpipe` slots; unbenchmarked), >= 1 Gbit/s uplink, and (for VirGL)
an accessible host GPU render node (`/dev/dri/renderD*`, such as Hetzner
`AX42` Ryzen 7 PRO 8700GE iGPU). Verify AUP rules allow public demo traffic
behind strict egress filtering.

#### 2. Provision infrastructure

Apply the matching module under `HorneroOS/playground/infra/terraform/`:

```sh
cd infra/terraform/hetzner
terraform init
terraform plan \
  -var="cloudflare_account_id=$CF_ACCOUNT_ID" \
  -var="cloudflare_zone_id=$CF_ZONE_ID" \
  -var='admin_cidrs=["<operator-ip>/32"]'
terraform apply
```

Keep SSH (`TCP/22`) restricted strictly to `admin_cidrs` or WireGuard CIDRs—never
`0.0.0.0/0`. For temporary bursts, use `infra/terraform/gcp-nested-kvm/` with
`use_spot = true` and `enable_nested_virtualization = true`.

#### 3. Configure DNS

Point the dedicated origin `playground.horneroos.com` via proxied Cloudflare
CNAME to the provisioned Cloudflare Tunnel (`cloudflare_record.playground_cname`).
Never host the streaming orchestrator on `horneroos.com`: keeping separate
origins preserves `HorneroOS/website`'s strict `vercel.json` CSP
(`default-src 'self'; connect-src 'self'; frame-ancestors 'none'`).

#### 4. Provision and verify secrets

Inject runtime secrets strictly via host environment files (`0600`, root-owned,
readable only by the orchestrator/`coturn` units) outside Terraform state and
git:

- `HORNERO_TURN_SHARED_SECRET` (HMAC shared secret for short-lived `coturn` leases)
- `HORNERO_TURNSTILE_SECRET` (Cloudflare Turnstile server validation secret)
- `HORNERO_METRICS_BEARER_TOKEN` (protects `/metrics`)
- Cloudflare Tunnel credentials and R2 bucket read tokens
- HorneroOS release GPG public key
  (`FCFBEE43925AB5429362278AE59EAB44AA2498DC`,
  `packaging/keys/hornero-release.pub.asc` in `HorneroOS/hornero`)

#### 5. Configure TLS and edge ingress

Verify HTTPS and signaling WebSocket (`WSS`) terminate with **TLS 1.3** at
Cloudflare Tunnel / edge reverse proxy, WebRTC media negotiates **DTLS-SRTP**,
and firewall rules allow **UDP/TCP `3478`** (plus configured `coturn` relay
port range) without exposing orchestrator port `8080` publicly.

### Phase B — Control plane, execution nodes, and signed images (Steps 6–8)

#### 6. Deploy control plane

Start the `hornero_playground` orchestrator and `coturn` container stack
(`browser/streaming/docker-compose.yml` or systemd unit), bound to `127.0.0.1:8080`
behind the edge tunnel, with `trust_proxy_headers` enabled only for
`127.0.0.1` / `::1` or explicit proxy IPs.

#### 7. Prepare KVM execution nodes

Configure every bare-metal worker node with:

- Dedicated unprivileged service user (never `root`) in the `kvm` and `render`
  groups.
- Systemd cgroup scope budget matching `HorneroOS/qa`: `MemoryMax` =
  `ram_mb + 1200M` (4096 MiB guest + 1200 MiB VirGL overhead),
  `MemorySwapMax=0`, `CPUQuota`, and `TasksMax`.
- OVMF split firmware (`/usr/share/OVMF/x64/OVMF_CODE.4m.fd` and per-VM
  copied `OVMF_VARS.4m.fd`).
- Host `nftables` egress rules dropping RFC1918 (`10.0.0.0/8`, `172.16.0.0/12`,
  `192.168.0.0/16`), link-local/IMDS (`169.254.0.0/16`, `169.254.169.254`),
  CGNAT (`100.64.0.0/10`), IPv6 `fe80::/10`/`fd00::/8`, and outbound SMTP
  (`25`, `465`, `587`).

#### 8. Import and verify signed golden images

Download the published `.qcow2.zst`, `.sha256`, and `.sig` from Cloudflare R2 /
object storage, verify cryptographic integrity before decompression, and lock
the base disk read-only (`0444`):

```sh
gpg --verify horneroos.qcow2.zst.sig horneroos.qcow2.zst
sha256sum -c horneroos.qcow2.zst.sha256
zstd -d horneroos.qcow2.zst -o /var/lib/hornero/horneroos.qcow2
chmod 0444 /var/lib/hornero/horneroos.qcow2
```

Never boot an unverified image or copy a maintainer's personal disk.

### Phase C — Hardware, streaming, isolation, and quotas (Steps 9–14)

#### 9. Validate KVM virtualization

Run a dry-run and a single live CoW overlay boot to verify `/dev/kvm`, `q35` +
OVMF boot, `qemu-img create -f qcow2 -F qcow2 -b` overlay creation, and nested
virtualization disabled inside the guest (`vmx=off` / `svm=off` so tenants
cannot spawn L2 guests):

```sh
python3 -m hornero_playground --host 127.0.0.1 --port 8080 --dry-run \
  --base-image /var/lib/hornero/horneroos.qcow2
```

#### 10. Validate GPU / VirGL acceleration

Verify `/dev/dri/renderD*` permissions and confirm a guest booted with
`-device virtio-vga-gl` (`-display egl-headless,gl=on` or `-display dbus`)
receives hardware-accelerated OpenGL (`AQ_NO_MODIFIERS=1`,
`QSG_RHI_BACKEND=opengl`, `LIBVA_DRIVER_NAME=virtio_gpu`) rather than falling
back to CPU `llvmpipe`. Confirm both **Hyprland** and **Niri** render without
DRM modifier negotiation errors.

#### 11. Validate WebRTC & PipeWire streaming

Verify `guest-stream-agent.sh` (or host DMA-BUF `webrtcbin` worker) delivers:

- Smooth 60 FPS video (`VP8` / `H.264`) and dynamic output resize.
- **PipeWire Opus audio** isolated to a per-session sink/node (zero cross-VM
  audio leakage).
- Working **Super / Alt** compositor keybinds for Hyprland and Niri.
- `coturn` relay traversal when symmetric NAT blocks direct P2P ICE.

#### 12. Validate public multi-tenant isolation

Run negative security checks on a live session:

- Confirm QEMU runs non-root with `-sandbox on,obsolete=deny,elevateprivileges=deny,spawn=deny,resourcecontrol=deny`
  and zero `virtio-fs`/`9p` host mounts.
- Confirm inside the guest that connections to `169.254.169.254`, RFC1918
  addresses, host orchestrator ports, and TCP `25`/`465`/`587` fail immediately
  (`restrict=on` default or `nftables` drops).
- Confirm host clipboard is isolated and consecutive sessions see zero leftover
  files (fresh CoW overlay deleted on exit).

#### 13. Validate Presenter Mode & demo overlay

Confirm images built with `build-vm-image.sh --demo` (or patched via
`demo/apply-demo-overlay.sh`) boot directly into `hornero` autologin with idle
screen-locking disabled, Hornero Welcome ready, and working presenter controls:

```sh
hornero-presenter --dry-run on
hornero-presenter --dry-run status
hornero-presenter --dry-run off
```

#### 14. Configure quotas, rate limits, and abuse gates

Lock production orchestrator settings before exposing ingress:

- `require_turnstile = true` (Cloudflare Turnstile managed challenge)
- `max_sessions <= 14` (sized to node RAM: `floor((HostRAM - 8GiB) / 5.2GiB)`)
- `rate_limit_per_ip_per_hour = 3` (sliding-window per IP / subnet)
- `session_ttl_seconds = 900` (15-minute hard reaper)
- `idle_timeout_seconds = 300` (5-minute inactivity reaper)
- `egress_mode = "restrict"` for anonymous visitors

### Phase D — Observability, verification, launch, and rollback (Steps 15–19)

#### 15. Enable monitoring and observability

Configure authenticated scraping of `/metrics` using
`HORNERO_METRICS_BEARER_TOKEN` plus host alerts for:

- Active systemd `hornero-pg-*.scope` count vs `max_sessions`
- Host RAM / VirGL RSS headroom and OOM events
- Overlay disk utilization under `/var/lib/hornero/overlays`
- `nftables` egress drop bursts and Turnstile HTTP 403/429 spikes
- Log scrubbing (never log visitor keystrokes, IP-linked PII, or secrets)

#### 16. Run end-to-end smoke tests

Execute the Playground test suite and `HorneroOS/qa` acceptance gates against
the deployed candidate image:

```sh
python3 -m pytest -q
uv run hornero-qa run scenarios/playground/vm-boot-ready \
  scenarios/playground/apps-and-welcome \
  scenarios/playground/presenter-dnd
```

All smoke checks (plus negative IMDS/SMTP egress checks) must pass before
enabling public links.

#### 17. Enable website feature flag

Update `HorneroOS/website` `/try` configuration to flip the hosted Playground
availability flag from local-only / waitlist to active `playground.horneroos.com`
routing, and verify `website`'s build checks (`check-release-truth`,
`check-i18n`, CSP headers) stay green.

#### 18. Verify production from external client

From an external residential/mobile network (outside `admin_cidrs`):

1. Visit `https://www.horneroos.com/try` and navigate to `playground.horneroos.com`.
2. Complete Turnstile, allocate a session, and confirm boot into Hornero Shell
   in under the expected startup budget.
3. Test `Super + Return`, Launcher (`Super + D`), `horneroctl doctor`, audio
   playback, and confirm the 15-minute reaper deletes the overlay on disconnect.

#### 19. Rollback and emergency kill-switch

If an operator observes active abuse, VirGL instability, CVE exposure, or
resource exhaustion, execute the **Emergency Kill-Switch** in order:

1. **Drain new allocations immediately:** Switch the orchestrator into
   maintenance drain (or disable Turnstile allocation endpoint / set
   `max_sessions = 0` and restart the orchestrator) and flip the
   `HorneroOS/website` `/try` flag back to Phase 1 local VMs.
2. **Terminate all active ephemeral VMs:**

   ```sh
   systemctl --user stop 'hornero-pg-*.scope'
   ```

3. **Apply emergency host egress drop-all** on the tenant bridge/VLAN if
   outbound abuse is suspected, while keeping `admin_cidrs` SSH intact.
4. **Preserve forensics and rotate secrets:** Keep host `journald`, `nftables`,
   and orchestrator allocation logs for incident triage; rotate
   `HORNERO_TURN_SHARED_SECRET`, Tunnel tokens, and cordon the node from DNS
   until patched and re-verified with `HorneroOS/qa`.

---

## Related guides

- [Cloud provider decision kit](cloud-provider-decision-kit.md)
- [Hornero Playground threat model](../architecture/hornero-playground-threat-model.md)
- [Try HorneroOS without installing](../getting-started/try-horneroos.md)
