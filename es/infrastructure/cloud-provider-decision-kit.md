# Kit de decisión de proveedores cloud para Hornero Playground

- **Última verificación:** `2026-11-28`
- **Seguimiento:** `HorneroOS/playground#1`, `HorneroOS/docs`
- **Calculadora de costos:** `HorneroOS/playground/tools/cost_calculator.py`

Este kit compara cada alternativa evaluada de hosting y patrocinio para correr
**HorneroOS Browser Playground** (`x86_64` Arch Linux + Hyprland / Niri +
Quickshell + PipeWire sobre WebRTC). Cada turno interactivo necesita **2–4
hilos de vCPU**, **4096 MiB de RAM invitada** (más **1200 MiB** de margen VirGL
en el cgroup del host, sin swap) y `/dev/kvm` por hardware.

---

## Compromiso de gasto cero

**HorneroOS no asume ningún compromiso de gasto recurrente en la nube por
defecto.**

1. **La Fase 1 sale a $0/mes** con VMs descargables firmadas `.qcow2.zst`,
   Quickemu (`horneroos.conf`), `hornero-vm-run.sh` y el listado orgánico en
   DistroSea (`distrosea.com/contact/`).
2. **Los turnos WebRTC alojados quedan detrás de un feature flag** en
   `https://www.horneroos.com/try` hasta que los maintainers autoricen un nivel
   de presupuesto o reciban créditos/hosting open source aprobados.
3. **El autoalojamiento sigue siendo portable:** cualquier servidor Linux con
   `/dev/kvm` puede correr el mismo orquestador y los módulos Terraform de
   `HorneroOS/playground` sin atarse a un proveedor.

---

## Matriz comparativa verificada de proveedores (2026-11-28)

### Hardware, virtualización, GPU y ancho de banda

| Proveedor | KVM | Anid. | GPU / VirGL | Specs y Red |
| --- | --- | --- | --- | --- |
| **DistroSea** | `noVNC` | N/A | **Sin 3D** | Cola ISO; sin audio |
| **AWS Credits** | `.metal` | N/A | Sin GPU | Según EC2; egreso AWS |
| **OSUOSL** | OpenStack | Polít. | **Sin GPU** | VM proyecto; red acad. |
| **GCP `n2-std`** | KVM L1 | **Sí** | **Sin GPU** | 16c/64G; $0.12/GiB |
| **AWS `.metal`** | L0 KVM | L0 | **Sin GPU** | 96c/192G; egreso AWS |
| **OVH `KS-1/2/A`** | L0 KVM | L0 | **Sin GPU** | 4–8c/32–64G; 100–500M |
| **OVH `RISE-1`** | L0 KVM | L0 | Intel UHD | 6c/12t/32G+; 1G ilim. |
| **Hetzner `AX42`** | L0 KVM | L0 | **Radeon** | 8c/16t/64G; 1G ilim. |
| **Hetzner `EX44`** | L0 KVM | L0 | Intel UHD | 14c/20t/64G; 1G ilim. |
| **Hetzner `AX52`** | L0 KVM | L0 | Ryzen iGPU | 8c/16t/64G; 1G ilim. |

### Costos, contratos, regiones, AUP y patrocinio

| Proveedor | Precio | Plazo | Región | AUP / Elegibilidad |
| --- | --- | --- | --- | --- |
| **DistroSea** | **$0** | N/A | EU/US | ISO pública vía form. |
| **AWS Credits** | Créditos | Vence | `sa`/`us-e1` | OSI + cuenta paga |
| **OSUOSL** | **$0** | Revis. | US-West | OSI + impacto FOSS |
| **GCP `n2-std`** | ~$567–900/m | On-dem | `sa`/`us-e1` | Bloquea IMDS/SMTP |
| **AWS `.metal`** | **$4.284/h** | On-dem | `sa`/`us-e1` | Elegible; $3.1k |
| **OVH `KS-1/2/A`** | ~$19–55+1m | Mes | EU/CA/AP | Sin spam; poco stock |
| **OVH `RISE-1`** | ~$64–67/m | 1m/12m | CA/FR | 12m bonifica alta |
| **Hetzner `AX42`** | **€46–99**+49 | Mes | `FSN1`/`HEL1` | Sin abuso AUP |
| **Hetzner `EX44`** | **€59**, **€0** | Mes | `FSN1`/`HEL1` | Sin abuso AUP |
| **Hetzner `AX52`** | ~€59–83.7/m | Mes | `FSN1`/`NBG1` | Sin abuso AUP |

### Notas de verificación y URLs oficiales (`2026-11-28`)

- **DistroSea** ([distrosea.com](https://distrosea.com/),
  [distrosea.com/contact/](https://distrosea.com/contact/)): cola web gratuita
  sobre `noVNC`; sin aceleración 3D VirGL y sin audio.
- **AWS Cloud Credits for Open Source**
  ([aws.amazon.com/government-education/open-source/](https://aws.amazon.com/government-education/open-source/)):
  exige licencia OSI, mantenimiento y comunidad activos, independencia de un
  único vendedor y cuenta AWS activa con medio de pago (no es retroactivo).
  Se envía el formulario a `awsopensourcecredits@amazon.com`; revisión mensual
  con pausa de emisión en diciembre. Aun con créditos, `c7i.metal-24xl`
  (`$4.284/h`, `~$3,127/mes`,
  [especificaciones c7i](https://aws.amazon.com/ec2/instance-types/c7i/))
  agota rápido créditos modestos.
- **OSU Open Source Lab (OSUOSL)**
  ([osuosl.org/services/hosting/](https://osuosl.org/services/hosting/)):
  hosting FOSS patrocinado para proyectos con licencia OSI, desarrollo abierto e
  impacto comunitario. Su clúster OpenStack/KVM `x86_64` apunta a servicios en
  producción (AArch64 y OpenPOWER son para CI multi-arquitectura). Las VMs
  compartidas no traen GPU física para VirGL, así que conviene más para plano
  de control, espejos o CI salvo hardware dedicado.
- **Google Cloud (`n2-standard-16`)**
  ([virtualización anidada](https://cloud.google.com/compute/docs/instances/nested-virtualization/overview)):
  16 vCPU, 64 GiB de RAM con KVM anidado a `$0` de recargo (con `>=10%` de
  impuesto CPU/IO L1->L2 y sin iGPU física). On-demand cuesta `~$0.777/h`
  (`~$567/mes`) en `us-east1` contra `~$1.233/h` (`~$900/mes`) en
  `southamerica-east1`; Spot baja a `~$0.08–$0.31/h`. El egreso Premium cuesta
  `$0.12/GiB` (primer TB) y `$0.14/GiB` entre Sudamérica y EE. UU.
- **OVHcloud Eco / Kimsufi y Rise**
  ([eco.ovhcloud.com](https://eco.ovhcloud.com/)): `KS-1` (Xeon-D 1520, 4c/8t,
  32 GB, `~$18.80/mes`), `KS-2` (Xeon-D 1540, 8c/16t, 32–64 GB, `~$21.10/mes`)
  y `KS-A` (i7-6700K, 32 GB, `~€/$54.99/mes`, APAC/Singapur con tope de 100
  Mbps / 5 TB) cobran alta de 1 mes y dependen del stock en vivo. `RISE-1`
  (Xeon-E 2386G, 6c/12t, 32–128 GB ECC, 2x512 GB NVMe, `~$64–$67/mes`, 1 Gbps
  ilimitado + 1 Gbps vRack) bonifica el alta con compromiso de 12 meses.
- **Hetzner Dedicated (`AX42`, `EX44`, `AX52`)**
  ([hetzner.com/dedicated-rootserver](https://www.hetzner.com/dedicated-rootserver/)):
  bare-metal L0 KVM con puerto de 1 Gbit/s ilimitado estándar (los upgrades de
  10 Gbit/s tienen tope de 20 TB) y contrato mensual. `AX42` (Ryzen 7 PRO
  8700GE + iGPU Radeon, 64 GB DDR5 ECC, 2x512 GB NVMe, `€46–€99/mes` + `€49`
  alta) acelera VirGL en la iGPU del host; `EX44` (Core i5-13500, 14c/20t, 64
  GB DDR4, `€59/mes`, `€0` alta) maximiza hilos; `AX52` (`~€59–€83.70/mes`)
  suma 2x1 TB NVMe en `FSN1`/`NBG1`/`HEL1`.

---

## Latencia desde Argentina (Buenos Aires)

Quienes mantienen HorneroOS trabajan desde Argentina, así que el RTT WebRTC
desde Buenos Aires impacta directo al probar el escritorio:

| Región / Hub | RTT (Buenos Aires) | UX WebRTC |
| --- | --- | --- |
| **São Paulo** (`sa-east-1`) | **~25–35 ms** | Casi local |
| **US-East** (`us-east-1`) | **~130–150 ms** | Ágil para demos |
| **EU Oeste** (París / Gravelines) | **~220–235 ms** | Leve demora |
| **EU Centro** (Falkenstein `FSN1`) | **~225–240 ms** | Mejor costo/FPS |
| **EU Norte** (Helsinki `HEL1`) | **~245–260 ms** | Mayor RTT (EU) |

Para evaluar animaciones de Hyprland y Niri a **60 FPS con latencia 0 ms**,
usá siempre VMs locales con VirGL mediante Quickemu o `hornero-vm-run.sh` (ver
[Probá HorneroOS sin instalar](../getting-started/try-horneroos.md)).

---

## Análisis por escenario de presupuesto

Usá `HorneroOS/playground/tools/cost_calculator.py` para modelar turnos
simultáneos, egreso y costo mensual según tu concurrencia objetivo. Cada turno
activo reserva **4 GiB de RAM + 2–4 hilos**.

| Presupuesto | Topología | Turnos | Inviables / Descartadas |
| --- | --- | --- | --- |
| **$0** | QCOW2 local + R2 + DistroSea | 0 | AWS `.metal`; GCP fijo |
| **~$25/mes** | OVH `KS-1/2` control/cpu | ~4–6 | AWS `.metal`; sin VirGL |
| **~$50/mes** | **Hetzner `AX42`** (€46+€49) | **8–12** | AWS `.metal`; GCP |
| **~$100/mes** | **Hetzner `EX44`** (€59)+R2 | **10–14** | `.metal` (>30×) |
| **~$200/mes** | 2–3× Hetzner+`coturn` | **20–36** | AWS `.metal` (>15×) |
| **Ráfagas** | **GCP `n2-std-16` Spot** | 8–12 | GCP fijo o AWS `.metal` |

### Por qué AWS `.metal` es inviable para presupuestos de $25–$200/mes

AWS EC2 **no** ofrece instancias bare-metal chicas con `/dev/kvm`. Las
instancias EC2 Nitro estándar (`t3`, `c7i.large`, etc.) bloquean KVM anidado,
lo que obliga a saltar a `c7i.metal-24xl` (96 vCPU, 192 GiB RAM) a
**$4.284/hora (~$3,127/mes)** on-demand antes de discos EBS y egreso WebRTC.
Incluso con un Savings Plan del 72%, un solo nodo `.metal` queda **4× a 40× por
encima** de un presupuesto comunitario de $25–$200/mes.

---

## Resumen listo para enviar a DistroSea

El dossier completo para maintainers está en
[`HorneroOS/playground/distributions/distrosea-submission.md`](https://github.com/HorneroOS/playground/blob/main/distributions/distrosea-submission.md).
Envialo por [distrosea.com/contact/](https://distrosea.com/contact/) con estos
datos:

- **Distribución:** HorneroOS (`x86_64`, base Arch Linux, Hyprland, Quickshell
  y SDDM `hornero-greeter`).
- **Release:** `v0.2.0-preview32` (`horneroos-2026.10-preview32-x86_64.iso`,
  2.7 GB / `2,931,294,208` bytes).
- **URL directa de la ISO:**
  `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/iso/horneroos-2026.10-preview32-x86_64.iso`
- **SHA-256:**
  `b8cd0f8604bc69f7d2112fb8bccd97115d32d197e9c92c62e02faf5de6345aec` (con
  `.sha256` y `.sig` firmados con `FCFBEE43925AB5429362278AE59EAB44AA2498DC`).
- **Nota de arranque y gráficos para operadores:** Soporta UEFI
  (`systemd-boot`) y BIOS (`syslinux`), entra automático como `hornero-live`
  (`Session=hyprland.desktop`). Sin VirGL, elegí la entrada **"HorneroOS (Safe
  Graphics)"** (`nomodeset WLR_RENDERER=pixman`) con >= 4096 MiB de RAM y 2–4
  vCPU.
- **Rol:** Vidriera orgánica sin costo que enlaza al Playground WebRTC y a las
  descargas Quickemu/QCOW2, aclarando de frente que `noVNC` no tiene audio ni
  aceleración 3D.

## Guías relacionadas

- [Runbook de despliegue de Playground](playground-deployment-runbook.md)
- [ADR: arquitectura de Hornero Playground (en inglés)](../../architecture/adr-hornero-playground.md)
- [Modelo de amenazas de Hornero Playground (en inglés)](../../architecture/hornero-playground-threat-model.md)
- [Probá HorneroOS sin instalar](../getting-started/try-horneroos.md)
