# Runbook de despliegue de Playground

- **Alcance:** Despliegue en producción de **HorneroOS Browser Playground**
  sobre WebRTC (`HorneroOS/playground`)
- **Base de seguridad:** [Modelo de amenazas de Hornero Playground (en inglés)](../../architecture/hornero-playground-threat-model.md)
- **Selección de proveedor:** [Kit de decisión de proveedores cloud](cloud-provider-decision-kit.md)

Este runbook detalla qué falta una vez elegido el proveedor cloud o bare-metal y
documenta la **secuencia final de 19 pasos**, incluyendo validación de hardware
y el kill-switch de emergencia.

---

## ¿Qué falta después de elegir un proveedor cloud?

Una vez aprobados el proveedor y el presupuesto (manteniendo **$0/mes** por
defecto hasta autorización explícita), seis pasos separan la elección de la
puesta en marcha:

1. **Confirmar la elección de proveedor y presupuesto** (por ejemplo Hetzner
   Robot `AX42`/`EX44` como primario o GCP Spot para ráfagas).
2. **Provisionar la infraestructura autorizada** con los módulos Terraform de
   `HorneroOS/playground` y `cloud-init.yaml.tftpl`.
3. **Configurar DNS y secretos fuera de git y del estado de Terraform**
   (`playground.horneroos.com`, Turnstile, `coturn`, token de métricas,
   Cloudflare Tunnel).
4. **Desplegar el plano de control y los nodos KVM** con QEMU sin privilegios,
   cgroups y aislamiento de egreso vía `nftables`.
5. **Correr validación de hardware, KVM, VirGL, streaming, aislamiento y modo
   presentador** con `HorneroOS/qa` `scenarios/playground/`.
6. **Activar el feature flag en el sitio web** (`HorneroOS/website` `/try`) y
   verificar producción desde un navegador externo.

---

## Runbook final de despliegue en 19 pasos

### Fase A — Infraestructura, DNS, secretos y TLS (Pasos 1–5)

#### 1. Verificar requisitos del proveedor

Confirmá que el nodo destino ofrece extensiones `x86_64` (`vmx` o `svm`),
`/dev/kvm` por hardware, >= 64 GiB de RAM para 4–6 turnos conservadores con
VirGL (o 2–4 con `llvmpipe` solo CPU; sin benchmark aún), enlace >= 1 Gbit/s
y (para VirGL) un nodo de renderizado GPU accesible en el host
(`/dev/dri/renderD*`, como la iGPU Ryzen 7 PRO 8700GE del Hetzner `AX42`).
Verificá que el AUP permita tráfico público de demos detrás de filtrado
estricto de salida.

#### 2. Provisionar la infraestructura

Aplicá el módulo correspondiente en `HorneroOS/playground/infra/terraform/`:

```sh
cd infra/terraform/hetzner
terraform init
terraform plan \
  -var="cloudflare_account_id=$CF_ACCOUNT_ID" \
  -var="cloudflare_zone_id=$CF_ZONE_ID" \
  -var='admin_cidrs=["<ip-operador>/32"]'
terraform apply
```

Mantené SSH (`TCP/22`) restringido estrictamente a `admin_cidrs` o CIDRs de
WireGuard—nunca `0.0.0.0/0`. Para picos puntuales, usá
`infra/terraform/gcp-nested-kvm/` con `use_spot = true` y
`enable_nested_virtualization = true`.

#### 3. Configurar DNS

Apuntá el origen dedicado `playground.horneroos.com` mediante CNAME proxied en
Cloudflare hacia el Cloudflare Tunnel provisionado
(`cloudflare_record.playground_cname`). Nunca alojes el orquestador en
`horneroos.com`: separar los orígenes mantiene intacta la CSP estricta de
`HorneroOS/website` en `vercel.json` (`default-src 'self'; connect-src 'self';
frame-ancestors 'none'`).

#### 4. Provisionar y verificar secretos

Cargá los secretos de ejecución únicamente en archivos de entorno del host
(`0600`, dueño root, legibles solo por las unidades del orquestador/`coturn`)
fuera del estado de Terraform y de git:

- `HORNERO_TURN_SHARED_SECRET` (secreto HMAC para credenciales temporales de
  `coturn`)
- `HORNERO_TURNSTILE_SECRET` (secreto de validación server-side de Cloudflare
  Turnstile)
- `HORNERO_METRICS_BEARER_TOKEN` (protege `/metrics`)
- Credenciales del Cloudflare Tunnel y tokens de lectura para R2
- Clave GPG pública de releases de HorneroOS
  (`FCFBEE43925AB5429362278AE59EAB44AA2498DC`,
  `packaging/keys/hornero-release.pub.asc` en `HorneroOS/hornero`)

#### 5. Configurar TLS e ingreso de borde

Verificá que HTTPS y el WebSocket de señalización (`WSS`) terminen con **TLS
1.3** en Cloudflare Tunnel / reverse proxy, que los medios WebRTC negocien
**DTLS-SRTP** y que el firewall habilite **UDP/TCP `3478`** (más el rango de
puertos relay de `coturn`) sin exponer el puerto `8080` del orquestador a
internet.

### Fase B — Plano de control, nodos de ejecución e imágenes firmadas (Pasos 6–8)

#### 6. Desplegar el plano de control

Iniciá el orquestador `hornero_playground` y el stack de `coturn`
(`browser/streaming/docker-compose.yml` o unidad systemd), escuchando en
`127.0.0.1:8080` detrás del túnel, con `trust_proxy_headers` habilitado solo
para `127.0.0.1` / `::1` o las IPs explícitas del proxy.

#### 7. Preparar nodos de ejecución KVM

Configurá cada nodo bare-metal con:

- Usuario de servicio dedicado sin privilegios (nunca `root`) en los grupos
  `kvm` y `render`.
- Presupuesto de cgroup en systemd equivalente a `HorneroOS/qa`: `MemoryMax` =
  `ram_mb + 1200M` (4096 MiB para el guest + 1200 MiB de margen VirGL),
  `MemorySwapMax=0`, `CPUQuota` y `TasksMax`.
- Firmware dividido OVMF (`/usr/share/OVMF/x64/OVMF_CODE.4m.fd` y copia por VM
  de `OVMF_VARS.4m.fd`).
- Reglas `nftables` de egreso en el host bloqueando RFC1918 (`10.0.0.0/8`,
  `172.16.0.0/12`, `192.168.0.0/16`), link-local/IMDS (`169.254.0.0/16`,
  `169.254.169.254`), CGNAT (`100.64.0.0/10`), IPv6 `fe80::/10`/`fd00::/8` y
  SMTP saliente (`25`, `465`, `587`).

#### 8. Importar y verificar imágenes doradas firmadas

Descargá el archivo `.qcow2.zst`, `.sha256` y `.sig` publicado en Cloudflare R2
/ object storage, verificá su integridad criptográfica antes de descomprimir y
dejá el disco base solo lectura (`0444`):

```sh
gpg --verify horneroos.qcow2.zst.sig horneroos.qcow2.zst
sha256sum -c horneroos.qcow2.zst.sha256
zstd -d horneroos.qcow2.zst -o /var/lib/hornero/horneroos.qcow2
chmod 0444 /var/lib/hornero/horneroos.qcow2
```

Nunca arranques una imagen sin verificar ni copies el disco personal de un
maintainer.

### Fase C — Hardware, streaming, aislamiento y cuotas (Pasos 9–14)

#### 9. Validar virtualización KVM

Corré un `dry-run` y un arranque real con overlay CoW para verificar
`/dev/kvm`, arranque `q35` + OVMF, creación de overlays con `qemu-img create
-f qcow2 -F qcow2 -b` y virtualización anidada deshabilitada dentro del guest
(`vmx=off` / `svm=off` para que nadie levante L2):

```sh
python3 -m hornero_playground --host 127.0.0.1 --port 8080 --dry-run \
  --base-image /var/lib/hornero/horneroos.qcow2
```

#### 10. Validar aceleración GPU / VirGL

Comprobá permisos de `/dev/dri/renderD*` y confirmá que una VM lanzada con
`-device virtio-vga-gl` (`-display egl-headless,gl=on` o `-display dbus`)
recibe OpenGL acelerado por hardware (`AQ_NO_MODIFIERS=1`,
`QSG_RHI_BACKEND=opengl`, `LIBVA_DRIVER_NAME=virtio_gpu`) en lugar de caer a
CPU `llvmpipe`. Verificá que tanto **Hyprland** como **Niri** rendericen sin
errores de negociación DRM.

#### 11. Validar streaming WebRTC y PipeWire

Confirmá que `guest-stream-agent.sh` (o el worker DMA-BUF `webrtcbin` del
host) entrega:

- Video fluido a 60 FPS (`VP8` / `H.264`) y redimensionado dinámico.
- **Audio Opus vía PipeWire** aislado por sesión en un sink dedicado (cero
  filtración de audio entre VMs).
- Atajos de teclado **Super / Alt** funcionando en Hyprland y Niri.
- Relay `coturn` operativo cuando un NAT simétrico bloquea ICE directo.

#### 12. Validar aislamiento multi-tenant público

Ejecutá chequeos negativos de seguridad sobre una sesión activa:

- Confirmá que QEMU corre sin `root` con `-sandbox
  on,obsolete=deny,elevateprivileges=deny,spawn=deny,resourcecontrol=deny` y
  sin montajes `virtio-fs`/`9p`.
- Confirmá desde adentro del guest que las conexiones a `169.254.169.254`,
  rangos RFC1918, puertos del orquestador y TCP `25`/`465`/`587` fallan de
  inmediato (`restrict=on` por defecto o drops `nftables`).
- Confirmá que el portapapeles del host está aislado y que sesiones
  consecutivas no ven archivos residuales (overlay CoW borrado al salir).

#### 13. Validar Modo Presentador y overlay de demo

Verificá que las imágenes armadas con `build-vm-image.sh --demo` (o
configuradas con `demo/apply-demo-overlay.sh`) inician sesión automática en
`hornero` con bloqueo por inactividad desactivado, Hornero Welcome listo y
controles de presentador operativos:

```sh
hornero-presenter --dry-run on
hornero-presenter --dry-run status
hornero-presenter --dry-run off
```

#### 14. Configurar cuotas, límites de tasa y controles anti-abuso

Fijá los parámetros de producción del orquestador antes de abrir el ingreso:

- `require_turnstile = true` (desafío gestionado de Cloudflare Turnstile)
- `max_sessions <= 14` (dimensionado según RAM del nodo: `floor((HostRAM -
  8GiB) / 5.2GiB)`)
- `rate_limit_per_ip_per_hour = 3` (ventana deslizante por IP / subred)
- `session_ttl_seconds = 900` (corte estricto a los 15 minutos)
- `idle_timeout_seconds = 300` (corte por inactividad a los 5 minutos)
- `egress_mode = "restrict"` para visitantes anónimos

### Fase D — Monitoreo, verificación, lanzamiento y rollback (Pasos 15–19)

#### 15. Habilitar monitoreo y observabilidad

Configurá recolección autenticada en `/metrics` usando
`HORNERO_METRICS_BEARER_TOKEN` junto con alertas de host para:

- Cantidad de scopes `hornero-pg-*.scope` activos frente a `max_sessions`
- Margen de RAM / RSS de VirGL y eventos OOM
- Uso de disco bajo `/var/lib/hornero/overlays`
- Picos de paquetes descartados en `nftables` y rechazos Turnstile HTTP 403/429
- Sanitización de logs (nunca registrar teclas, PII asociada a IP ni secretos)

#### 16. Correr smoke tests de punta a punta

Ejecutá la suite de pruebas de Playground y las compuertas de `HorneroOS/qa`
sobre la imagen candidata desplegada:

```sh
python3 -m pytest -q
uv run hornero-qa run scenarios/playground/vm-boot-ready \
  scenarios/playground/apps-and-welcome \
  scenarios/playground/presenter-dnd
```

Todos los smoke tests (más las pruebas negativas contra IMDS/SMTP) deben
aprobarse antes de habilitar enlaces públicos.

#### 17. Habilitar el feature flag del sitio web

Actualizá la configuración de `/try` en `HorneroOS/website` para pasar el flag
de Playground alojado a estado activo apuntando a `playground.horneroos.com`,
y confirmá que pasen todos los chequeos de build (`check-release-truth`,
`check-i18n`, headers CSP).

#### 18. Verificar producción desde un cliente externo

Desde una red residencial o móvil externa (fuera de `admin_cidrs`):

1. Entrá a `https://www.horneroos.com/try` y navegá a
   `playground.horneroos.com`.
2. Completá Turnstile, asigná un turno y confirmá el arranque en Hornero Shell
   dentro del tiempo esperado.
3. Probá `Super + Return`, el lanzador (`Super + D`), `horneroctl doctor`,
   reproducción de audio y confirmá que el reaper de 15 minutos borre el
   overlay al desconectar.

#### 19. Rollback y kill-switch de emergencia

Si detectás abuso activo, inestabilidad de VirGL, una vulnerabilidad crítica o
agotamiento de recursos, ejecutá el **Kill-Switch de Emergencia** en orden:

1. **Cortar nuevas asignaciones al instante:** Poné el orquestador en drenaje
   de mantenimiento (deshabilitá asignación / fijá `max_sessions = 0` y
   reiniciá el servicio) y devolvé el feature flag de `HorneroOS/website`
   `/try` a VMs locales de Fase 1.
2. **Terminar todas las VMs efímeras activas:**

   ```sh
   systemctl --user stop 'hornero-pg-*.scope'
   ```

3. **Aplicar bloqueo total de egreso** en el bridge o VLAN de tenants si se
   sospecha abuso saliente, manteniendo intacto el acceso SSH de `admin_cidrs`.
4. **Preservar forense y rotar secretos:** Guardá `journald`, contadores de
   `nftables` y logs del orquestador para análisis; rotá
   `HORNERO_TURN_SHARED_SECRET`, tokens del túnel y sacá el nodo de DNS hasta
   parchear y re-validar con `HorneroOS/qa`.

---

## Guías relacionadas

- [Kit de decisión de proveedores cloud](cloud-provider-decision-kit.md)
- [Modelo de amenazas de Hornero Playground (en inglés)](../../architecture/hornero-playground-threat-model.md)
- [Probá HorneroOS sin instalar](../getting-started/try-horneroos.md)
