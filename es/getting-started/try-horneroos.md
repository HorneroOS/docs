# Probá HorneroOS sin instalar

Podés probar el escritorio real de HorneroOS —Hyprland, Hornero Shell, temas,
layouts de barra, Hornero Welcome y `horneroctl`— sin borrar tu disco ni
reparticionar tu computadora. Cada camino en
[`horneroos.com/try`](https://www.horneroos.com/try) corre software real de
HorneroOS, nunca una simulación armada en el navegador.

> **Estado honesto hoy:** HorneroOS se usa a diario en producción en múltiples
> estaciones de trabajo físicas y está validado en KVM con UEFI y Legacy BIOS.
> La release firmada actual es **`v0.2.0-preview42`** (`x86_64`), que incluye
> **Hornero Signal**, **Hornero Apps**, **Signal Flight Welcome (`v1.6.0`)**,
> **Chromatic v3** y **Calamares `3.4.3`**. **Desktop**, **Studio** y
> **Gaming** son ediciones **Soportadas**; **Hyprland** (por defecto) y
> **Niri** son compositores Wayland **Soportados**; **Server**, **Agents**,
> **Labwc** y el rollback completo de raíz del SO siguen **Planificados**. Ver
> [Ediciones y composición de paquetes](../architecture/editions.md) y
> [Actualizaciones y recuperación](../desktop/updates-and-rollback.md).

## Elegí tu camino

| Camino | Mejor para | Fidelidad | Límite |
| --- | --- | --- | --- |
| **1. Navegador** | Vista rápida | WebRTC (alta) / `noVNC` (baja) | 15 min |
| **2. VM local** | Escritorio fluido a 60 FPS | VirGL local (KVM) | Ilimitado |
| **3. Live USB** | Probar GPU, Wi-Fi y audio | Velocidad nativa | Ilimitado |

---

## 1. Probar en el navegador

### HorneroOS Browser Playground

HorneroOS Browser Playground (`HorneroOS/playground`) levanta una máquina
virtual KVM descartable por visitante y transmite el escritorio Wayland real
junto con el audio de PipeWire directo a tu navegador por WebRTC.

- **Efímero por diseño:** Tu sesión corre en un disco temporal copy-on-write
  con un **límite estricto de 15 minutos** (y corte por inactividad). Al cerrar
  la pestaña o cumplirse el tiempo, la máquina virtual y todo lo que hiciste
  adentro se borran para siempre.
- **Nunca ingreses secretos reales:** No inicies sesión en correo personal,
  GitHub ni cuentas en la nube, ni pegues claves SSH o tokens dentro de una
  sesión pública en el navegador.
- **Disponibilidad honesta:** El clúster alojado está en despliegue bajo
  `HorneroOS/playground#1` con cupos limitados. Si los turnos públicos están
  llenos o en mantenimiento, usá el **Camino 2 (VM preinstalada)** o alojá el
  stack vos mismo en cualquier Linux con `/dev/kvm`.

### Autoalojar el stack de navegador

Si tenés un servidor o workstation Linux con KVM (`/dev/kvm`), podés levantar
el orquestador y el streamer WebRTC de `HorneroOS/playground` en tu propia red
para demos o talleres. Revisá la
[arquitectura de Hornero Playground (en inglés)](../../architecture/adr-hornero-playground.md)
y su
[modelo de amenazas (en inglés)](../../architecture/hornero-playground-threat-model.md)
antes de exponerlo a internet.

### DistroSea (canal secundario de descubrimiento)

HorneroOS también apunta a **DistroSea** (`distrosea.com`) como vidriera sin
costo de infraestructura. Tené presente la diferencia: DistroSea transmite por
`noVNC` **sin aceleración GPU 3D y sin audio**, así que el blur de Hyprland,
las transiciones Chromatic y las animaciones se ven entrecortadas frente a una
VM local o el Playground por WebRTC.

---

## 2. Descargar una máquina virtual preinstalada

Correr HorneroOS en una máquina virtual local te da tiempo ilimitado, control
total del teclado y fluidez real sin tocar tu sistema anfitrión. Para
`v0.2.0-preview42`, HorneroOS publica **ambos** artefactos firmados: una
imagen QCOW2 preinstalada de Desktop lista para VM y la ISO live e instalable
completa:

- **QCOW2 oficial preinstalada de Desktop (`2.61 GiB`, validada punta a punta
  en KVM UEFI):**
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/vm/horneroos-0.2.0-preview42-desktop-qemu-x86_64.qcow2.zst`
  - SHA-256:
    `c1012413227f407d0a312fad7d7a34f789922303db13c752a9a9ed1a324e13c2`
- **ISO oficial Live e instalable (`3.3 GiB`, UEFI + Legacy BIOS, validada en
  hardware físico y KVM):**
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/iso/horneroos-2026.11-preview42-x86_64.iso`
  - SHA-256:
    `9e494ab5f9783df6a5986385421ec0816b0033d3558d3323248a03e07f2e76a2`

Descomprimí la imagen `.qcow2.zst` con `unzstd` (o `zstd -d`) antes de
conectarla a QEMU/KVM, Quickemu o `libvirt`.

### Verificá antes de arrancar

Toda imagen oficial de HorneroOS incluye `SHA256SUMS` (o `.sha256`) y una
firma GPG desacoplada `.sig` de la clave de releases de HorneroOS
(`FCFBEE43925AB5429362278AE59EAB44AA2498DC`). Seguí los comandos de
verificación en [Primeros pasos](README.md) antes de iniciar cualquier disco
o ISO descargada.

### Recursos recomendados para la VM

- **RAM:** 4 GiB mínimo (6–8 GiB recomendados si abrís Studio o navegadores)
- **CPU:** 4 vCPU
- **Disco:** 32 GiB QCOW2/VDI dinámico (si instalás dentro de la VM)
- **Firmware:** UEFI (OVMF)

### QEMU / KVM en Linux (el más rápido, lanzador en 1 comando)

En Linux con `/dev/kvm` y `qemu-system-x86_64`, VirGL (`virtio-vga-gl`) acelera
Hyprland, Niri y Quickshell directo sobre la GPU de tu host.
`HorneroOS/playground` incluye el lanzador `hornero-vm-run.sh`, o podés
arrancar a mano con UEFI OVMF y VirGL:

```sh
./hornero-vm-run.sh horneroos-0.2.0-preview42-desktop-qemu-x86_64.qcow2
```

Si lanzás QEMU manualmente con una ISO o QCOW2, activá KVM, máquina `q35`,
UEFI OVMF y `-device virtio-vga-gl` con `-display gtk,gl=on`.

### Quickemu (`horneroos.conf`)

Si usás [Quickemu](https://github.com/quickemu-project/quickemu), creá un
archivo `horneroos.conf` junto a tu imagen y arrancá con un solo comando:

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

*(Si arrancás la ISO live en vez de la QCOW2 preinstalada, agregá la línea
`iso="horneroos/horneroos-2026.11-preview42-x86_64.iso"`.)*

### libvirt / `virt-manager` / GNOME Boxes

1. Creá una VM nueva desde un disco existente (`.qcow2`) o desde la ISO
   verificada.
2. Elegí firmware **UEFI** (`OVMF_CODE.4m.fd`) en lugar de BIOS heredado.
3. Asigná al menos **4096 MiB de RAM** y **4 vCPU**.
4. Usá **VirtIO** para disco y red, y elegí Video **Virtio** con **aceleración
   3D** activada (pantalla Spice/GTK OpenGL).

### VMware Workstation / Fusion (Linux, Windows, Mac Intel)

VMware Workstation Pro y Fusion son gratuitos para uso personal y exponen el
driver upstream `vmwgfx` (`SVGA3D`), que maneja compositores Wayland con mucha
más estabilidad que VirtualBox:

1. Importá el appliance `.ova` (o creá una VM Arch Linux 64-bit con UEFI desde
   la ISO).
2. Asigná **4 GiB de RAM**, **4 núcleos de CPU** y activá **Accelerate 3D
   graphics**.
3. Si Quickshell alguna vez muestra pantalla negra con el driver de tu host,
   probá `QSG_RHI_BACKEND=opengl` o `QSG_RHI_BACKEND=software` en la sesión
   invitada.

### Oracle VirtualBox (requiere modo software)

La aceleración 3D `VMSVGA` de VirtualBox hoy provoca pantallas negras o cierres
inmediatos en Hyprland y Niri. Si VirtualBox es tu única opción:

1. Creá una VM **Arch Linux (64-bit)** con **UEFI activado**, **4 GiB de RAM**
   y **4 CPUs**.
2. **Desmarcá "Habilitar aceleración 3D"** en Pantalla y subí la memoria de
   video a **128 MB**.
3. Si instalás dentro de la VM, instalá `virtualbox-guest-utils` (y habilitá
   `vboxservice.service`) y usá el fallback por software:
   `LIBGL_ALWAYS_SOFTWARE=1` y `QT_QUICK_BACKEND=software`.

Tené en cuenta que en este modo las animaciones van a ser mucho más lentas y
el uso de CPU más alto.

### macOS UTM (advertencia honesta para Apple Silicon)

HorneroOS hoy compila imágenes **únicamente para `x86_64`**. Como las Mac con
Apple Silicon (`M1`–`M4`) no pueden virtualizar `x86_64` por hardware mediante
`Hypervisor.framework`, **UTM cae en emulación de CPU por software (QEMU
TCG)**. Incluso con el renderizador VirGL de UTM (`virtio-gpu-gl`), Hyprland,
Niri y Quickshell se sienten **muy lentos** en Apple Silicon bajo UTM.

Para evaluar la velocidad real de HorneroOS, usá un equipo x86_64 con Live USB
o una sesión del Playground en el navegador cuando esté disponible.

---

## 3. Probar en tu propio hardware (Live USB)

Arrancar la ISO oficial firmada desde un pendrive USB te deja probar Wi-Fi,
audio, pantallas y periféricos reales en memoria sin tocar tus discos:

1. **Descargá y verificá** `horneroos-2026.11-preview42-x86_64.iso` (`.sig` +
   `.sha256`) siguiendo los comandos de [Primeros pasos](README.md).
2. **Grabá el pendrive** con un grabador gráfico de confianza o con `dd`
   después de confirmar el dispositivo correcto con `lsblk`:

   ```sh
   sudo dd if=horneroos-2026.11-preview42-x86_64.iso of=/dev/sdX bs=4M \
     status=progress conv=fsync
   ```

3. **Arrancá desde el USB:** Desactivá Secure Boot en el firmware si bloquea
   el arranque. Si tu GPU da pantalla negra en el arranque normal, elegí la
   opción **Safe Graphics** del menú de arranque
   (`nomodeset WLR_RENDERER=pixman`).
4. **Explorá sin riesgo:** La sesión live entra automático a Hyprland como
   `hornero-live` con el bloqueo por inactividad desactivado. Probá **Hornero
   Welcome**, cambiá temas y layouts, recorré el escritorio y chequeá la salud
   del sistema con:

   ```sh
   horneroctl doctor
   horneroctl version
   ```

5. **Instalá solo si decidís hacerlo:** Nada modifica tu disco interno hasta
   que abrís el instalador Calamares y confirmás las particiones. Seguí
   [Instalar HorneroOS paso a paso](install-step-by-step.md) (o
   [Instalar sobre un Arch Linux existente](install-on-arch.md) si ya usás
   Arch Linux).

---

## 4. Modo presentador y grabación

Cuando grabás demos, capturas o recorridos en vivo dentro de HorneroOS, podés
silenciar notificaciones y mantener la pantalla despejada sin cambiar tus
ajustes permanentes:

- **Overlay presentador (`HorneroOS/playground`):** En imágenes Playground o
  sesiones con el asistente de presentación instalado, activá o desactivá el
  modo limpio de demo con:

  ```sh
  hornero-presenter on
  hornero-presenter off
  ```

- **IPC nativo de No Molestar en Hornero Shell:** En cualquier escritorio
  HorneroOS (incluidas instalaciones existentes), controlá el modo No Molestar
  de notificaciones directo por IPC de Quickshell y pasá a modo Focus:

  ```sh
  qs ipc call notifs enableDnd
  qs ipc call notifs isDndEnabled
  horneroctl mode set focus
  ```

  Cuando termines, restaurá las notificaciones normales y el modo Signal:

  ```sh
  qs ipc call notifs disableDnd
  horneroctl mode set signal
  ```

- **Comandos integrados de captura:** Sacá capturas o grabaciones directo con:

  ```sh
  horneroctl capture screenshot
  horneroctl capture record
  ```

- **Consejos para grabaciones limpias:**
  - Usá **1920×1080** (1080p) o **1280×800** a 60 FPS para una escala clara y
    legible de la interfaz.
  - Corré `qs ipc call notifs clear` antes de empezar a grabar para limpiar
    avisos viejos.
  - Quitá nombres de usuario, rutas privadas, nombres de red y tokens antes
    de publicar videos o logs (ver
    [Seguridad y privacidad](../security/README.md)).

## Guías relacionadas

- [Primeros pasos](README.md) — descarga de ISO, verificación GPG y límites
- [Instalar HorneroOS paso a paso](install-step-by-step.md) — guía de
  Calamares
- [Instalar HorneroOS sobre un Arch Linux existente](install-on-arch.md)
- [Hornero Welcome](../desktop/hornero-welcome.md) y
  [Hornero Apps](../desktop/hornero-apps.md)
- [ADR: arquitectura de Hornero Playground (en inglés)](../../architecture/adr-hornero-playground.md)
- [Modelo de amenazas de Hornero Playground (en inglés)](../../architecture/hornero-playground-threat-model.md)
