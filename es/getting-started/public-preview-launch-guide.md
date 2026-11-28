# Guía de lanzamiento de vista previa pública

Esta guía ofrece a quienes visitan HorneroOS por primera vez un único punto de
entrada honesto para probar, instalar, resolver problemas y reportar hallazgos,
sin asumir conocimientos previos de Arch Linux ni Hyprland.

> **Estado real hoy:** HorneroOS es software en prelanzamiento bajo desarrollo
> activo. La ISO firmada publicada hoy es **`v0.2.0-preview32`** (`x86_64`),
> mientras que los componentes más recientes (**Hornero Signal**, **Hornero
> Apps**, mejoras de **Hornero Welcome** y **Chromatic v3**) ya se distribuyen
> mediante paquetes AUR en `main` antes del próximo corte de ISO. **Desktop**,
> **Studio** y **Gaming** son ediciones **Preview** validadas en máquinas
> virtuales; **Hyprland** es el compositor validado por defecto; **Niri** es
> experimental; **Server** y **Agents** están planificadas; y todavía no
> existe rollback completo del sistema operativo.

## 1. Elegí tu punto de partida

| Tu equipo | Camino seguro | Tiempo | Advertencia clave |
| --- | --- | --- | --- |
| **Windows 10/11** | VM (ISO) o USB | 20m | Sin 3D VirtualBox; Rufus DD |
| **macOS (M1–M4)** | PC x86_64 o KVM | — | Emulación x86_64 muy lenta |
| **macOS (Intel)** | VMware o USB | 20m | Verificá con `shasum -a 256` |
| **Arch Linux** | Paquetes AUR | 10m | Nunca pisa tus dotfiles |

### Windows: probá sin tocar tu instalación de Windows

No necesitás redimensionar particiones ni borrar Windows para evaluar
HorneroOS.

#### Opción A — Máquina virtual en Windows (arranque desde ISO)

Hoy solo la ISO firmada tiene descarga directa publicada (las imágenes `.ova` y
`.qcow2` automatizadas forman parte del pipeline de VM). Arrancá la ISO
verificada `v0.2.0-preview32` directamente:

1. Descargá `horneroos-2026.10-preview32-x86_64.iso` (2.7 GB) y su archivo
   `.sha256` desde [horneroos.com/install](https://www.horneroos.com/install).
2. Verificá la descarga en PowerShell o Símbolo del sistema antes de montarla:

   ```powershell
   CertUtil -hashfile horneroos-2026.10-preview32-x86_64.iso SHA256
   ```

   Compará el hash obtenido contra el archivo `.sha256` descargado.
3. **Recomendado en Windows — VMware Workstation Pro** (gratuito para uso
   personal): creá una VM **Linux → Other Linux 6.x kernel 64-bit** con
   firmware **UEFI**, **4 GiB+ de RAM**, **4 núcleos de CPU**, disco virtual de
   **32 GiB** y **Accelerate 3D graphics** activado.
4. **Alternativa VirtualBox:** creá una VM **Arch Linux 64-bit** con **Enable
   EFI** marcado, **4 GiB+ de RAM**, **4 CPU**, **128 MB de memoria de video** y
   **desmarcá "Enable 3D Acceleration"** (VMSVGA 3D produce pantallas negras en
   Hyprland). Dentro de la sesión invitada, exportá:

   ```sh
   export LIBGL_ALWAYS_SOFTWARE=1
   export QT_QUICK_BACKEND=software
   ```

#### Opción B — Live USB desde Windows

1. Guardá una copia de tu **clave de recuperación de BitLocker** y desactivá el
   **Inicio rápido de Windows** si pensás probar arranque dual más adelante.
2. Desactivá **Secure Boot** en el firmware UEFI (HorneroOS todavía no incluye
   shims firmados para Secure Boot).
3. Grabá la ISO verificada con **Rufus** (cuando pregunte, elegí **Escribir en
   modo imagen DD**, no modo ISO) o con **balenaEtcher**.
4. Arrancá desde el pendrive. Nada toca tu disco de Windows hasta que abras
   Calamares y confirmes particiones. Si tu GPU da pantalla negra, elegí
   **Safe Graphics** en el menú de arranque (`nomodeset WLR_RENDERER=pixman`).

### macOS: advertencia honesta para Apple Silicon (M1–M4)

Leé esto **antes** de descargar la ISO de 2.7 GB en una Mac:

- **Macs con Apple Silicon (`M1`–`M4`):** HorneroOS publica **únicamente
  imágenes `x86_64`**. `Hypervisor.framework` no puede virtualizar `x86_64` por
  hardware en ARM64, así que UTM recurre a **emulación de CPU por software QEMU
  TCG** y se vuelve extremadamente lento. ARM64 nativo y Parallels FEX no
  están soportados.
- **Qué hacer en Apple Silicon:** Probá en una PC `x86_64` con Live USB,
  autoalojá `HorneroOS/playground` en cualquier servidor Linux con `/dev/kvm`, o
  esperá a que haya un clúster público del Browser Playground activo.
- **Macs Intel:** VMware Fusion (gratuito para uso personal) arranca la ISO
  `x86_64` con UEFI y aceleración 3D activada.
- **Crear un Live USB desde macOS** (para una PC `x86_64`): verificá el hash
  con el comando nativo `shasum`:

  ```sh
  shasum -a 256 horneroos-2026.10-preview32-x86_64.iso
  ```

### Arch Linux existente: paquetes AUR e inspección

Si ya usás Arch Linux `x86_64` actualizado, podés evaluar Hornero Signal,
Hornero Apps, Hornero Welcome y `horneroctl` sin reinstalar. Mirá los pasos
completos en [Instalar en Arch](install-on-arch.md).

1. **Inspeccioná antes de compilar:** Revisá cada receta del AUR:
   - [`hornero-shell`](https://aur.archlinux.org/packages/hornero-shell)
   - [`hornero-config`](https://aur.archlinux.org/packages/hornero-config)
   - [`horneroctl-bin`](https://aur.archlinux.org/packages/horneroctl-bin)
     (verifica firmas de release con la clave GPG
     `FCFBEE43925AB5429362278AE59EAB44AA2498DC`)
   - [`hornero-greeter`](https://aur.archlinux.org/packages/hornero-greeter)
     (tema SDDM) o
     [`hornero-greeter-greetd`](https://aur.archlinux.org/packages/hornero-greeter-greetd)
     (para quienes usan `greetd`; elegí el que coincida con tu gestor)
2. **Respaldá e instalá:**

   ```sh
   tar -czf ~/hornero-pre-adopt-$(date +%F).tar.gz \
     ~/.config/hypr ~/.config/kitty ~/.config/ghostty \
     ~/.config/environment.d 2>/dev/null
   yay -Syu hornero-shell
   ```

3. **Simulá el sembrado y verificá:**

   ```sh
   /usr/share/hornero/seed-user.sh --dest "$HOME" --dry-run
   /usr/share/hornero/seed-user.sh --dest "$HOME"
   horneroctl doctor
   ```

4. **Probá solo la shell en tu sesión Hyprland actual** sin adoptar defaults:

   ```sh
   horneroctl shell start --yes
   ```

## 2. Problemas conocidos y limitaciones honestas

Revisá estos límites frente a tu caso de uso antes de adoptar el sistema:

- **ISO validada en VM, sin matriz física todavía:** `v0.2.0-preview32` aprobó
  instalaciones UEFI sin cifrado en VMs para Desktop, Studio y Gaming. LUKS,
  BIOS heredado, `copytoram` y sesiones Niri de ISO no se ejecutaron sobre
  `preview32`. Solo una laptop física (ASUS ROG Strix G16 sobre `preview24` más
  ajustes manuales) figura como `USER-VERIFIED`. Ver
  [Probado y no probado](../hardware/tested-and-untested.md).
- **Todavía no hay rollback del sistema:** Toda compilación actual reporta
  backend de snapshots `none`. `horneroctl recovery doctor` es diagnóstico de
  solo lectura, y `horneroctl config snapshot` archiva solo ajustes de
  Hornero—nunca `/`, el kernel ni transacciones de `pacman`. Ver
  [Actualizaciones y recuperación](../desktop/updates-and-rollback.md).
- **Diferencia entre la ISO y el AUR:** La ISO `v0.2.0-preview32` es anterior al
  trabajo reciente de Signal Enmienda 3, Chromatic v3, Hornero Apps y Welcome
  Signal Flight en `main`/AUR hasta que se firme el próximo corte de ISO.
  Actualizar con `yay -Syu` tras instalar trae los últimos paquetes.
- **Browser Playground público en espera:** `HorneroOS/playground` queda en
  `standby-awaiting-provider` (compromiso cloud de $0/mes) hasta seleccionar y
  financiar un proveedor público. El autoalojamiento ya funciona en cualquier
  Linux con `/dev/kvm`.
- **Límites en VirtualBox 3D e Hyper-V:** VirtualBox `VMSVGA` 3D causa
  pantallas negras en Hyprland/Niri; las VMs Linux en Hyper-V carecen de VirGL
  nativo y caen a renderizado por software `llvmpipe`.
- **Lentitud `x86_64` en Apple Silicon:** Todavía no existe compilación ARM64;
  UTM cae a emulación de CPU QEMU TCG.
- **Alcance experimental o planificado:** **Niri** es experimental (VM de una
  sola salida); **Server**, **Agents** y **Labwc** están planificados sin
  imágenes booteables; **Secure Boot** requiere desactivarse en firmware o
  enrolar claves propias.

## 3. Solución práctica de problemas

Empezá cualquier diagnóstico con chequeos de solo lectura y guardá el primer
error:

```sh
horneroctl doctor
horneroctl config validate
```

### Pantalla negra al arrancar o fallo del instalador

- Elegí la entrada **Safe Graphics** en el menú de arranque de la ISO live
  (`nomodeset WLR_RENDERER=pixman`).
- Luego de instalar, si una actualización de kernel falla al iniciar, elegí el
  kernel de respaldo en las opciones avanzadas de GRUB (`kernel-and-fallback`) e
  inspeccioná el arranque anterior:

  ```sh
  journalctl -b -1 --no-pager
  ```

- Si un SSD NVMe interno no aparece en Calamares en una laptop Intel, cambiá
  Intel VMD / RST a modo AHCI en el firmware UEFI (respaldá Windows antes si
  hacés arranque dual).

### Wayland, NVIDIA y cursor o pantalla negra en VMs

- **Cursor invisible o pantalla negra en VM (QEMU/VMware/VirtualBox):**
  - En **VirtualBox**, desmarcá **Enable 3D Acceleration** y exportá
    `LIBGL_ALWAYS_SOFTWARE=1` + `QT_QUICK_BACKEND=software`.
  - En **VMware**, habilitá `Accelerate 3D graphics`; si Quickshell abre en
    blanco, probá `QSG_RHI_BACKEND=opengl` o `QSG_RHI_BACKEND=software`.
  - En **QEMU/KVM**, usá UEFI OVMF + `-device virtio-vga-gl` (`VirGL`).
- **Laptops NVIDIA / híbridas:** HorneroOS no incluye instalador propio de
  drivers NVIDIA. Seguí
  [Gráficos híbridos y NVIDIA](../hardware/hybrid-graphics-nvidia.md) para
  verificar `nvidia-dkms` / `nvidia-open-dkms` y `nvidia_drm.modeset=1`.
- **Shell o panel de Control Center en blanco:**

  ```sh
  horneroctl shell status --json
  horneroctl shell logs --lines 120
  ```

### Configuración de Flatpak y Flathub (`Hornero Apps`)

Verificá la salud del store, las fuentes activas y la conexión a Flathub:

```sh
horneroctl store doctor
horneroctl store sources
```

Si falta Flathub en una instalación Arch personalizada, agregalo:

```sh
flatpak remote-add --if-not-exists flathub \
  https://dl.flathub.org/repo/flathub.flatpakrepo
```

Consultá [Hornero Apps](../desktop/hornero-apps.md) para entender las insignias
de procedencia (`Official`, `Verified`, `Community`, `Web App`) y
`horneroctl store policy`.

### Recuperación de audio PipeWire

Revisá los servicios de audio y el enrutamiento Studio antes de editar archivos:

```sh
horneroctl studio doctor
horneroctl studio routing status
systemctl --user status pipewire pipewire-pulse wireplumber
```

Si activaste un kit de ruteo en vivo de Studio y querés volver al audio normal:

```sh
horneroctl studio routing disable live-call
systemctl --user restart pipewire pipewire-pulse wireplumber
```

## 4. Bugs, reportes de hardware, seguridad y adopción en equipos

### Reportar un bug

Abrí un issue en el repositorio dueño del componente (`shell`, `config`,
`hornero`, `installer`, `docs`, `website`) desde su selector de issues,
adjuntando la salida sanitizada de `horneroctl doctor` y las primeras líneas de
error. Nunca publiques usuarios, IPs locales, tokens ni logs personales. Mirá
[Reportá un bug](../development/README.md#reportá-un-bug).

### Enviar un reporte de compatibilidad de hardware

Los reportes en hardware real son la evidencia que permite validar más allá de
las VMs. Usá la plantilla **Hardware Compatibility Report** (disponible en los
repositorios de HorneroOS vía `HorneroOS/.github`) y adjuntá la salida
sanitizada de:

```sh
horneroctl doctor
lspci -nnk
journalctl -b -k -p warning --no-pager
```

Indicá la versión exacta de ISO o paquetes AUR, firmware (UEFI/BIOS), uso de
LUKS, edición y compositor.

### Reportar una vulnerabilidad de seguridad

**Nunca abras un issue o PR público para un fallo de seguridad.** Seguí
[`SECURITY.md`](https://github.com/HorneroOS/.github/blob/main/SECURITY.md): usá
**Security → Report a vulnerability** en el repositorio afectado o pedí un canal
privado a las personas mantenedoras de la organización.

### Adoptar HorneroOS upstream en equipos (sin forks privados)

Equipos de ingeniería y laboratorios pueden estandarizar estaciones de trabajo
manteniéndose en los paquetes upstream:

- **Bloqueá la procedencia de software:** Aplicá `verified-only` o reglas
  curadas con `horneroctl store policy` y exportá listas reproducibles con
  `horneroctl store manifest` ([Hornero Apps](../desktop/hornero-apps.md)).
- **Separá overrides del equipo:** Dejá `/etc/xdg/hypr/hyprland.lua.d/` bajo
  control de paquetes y ubicá las reglas propias en `*-user.lua`
  ([Instalar en Arch](install-on-arch.md)).
- **Compartí perfiles reproducibles:** Capturá y aplicá experiencia, ruteo de
  audio, energía y extensiones con `horneroctl profile`
  ([Perfiles y Snapshots](../desktop/profiles-snapshots.md)).
- **Autoalojá Playground:** Desplegá `HorneroOS/playground` en hardware KVM
  interno para evaluaciones aisladas
  ([Infraestructura](../infrastructure/README.md)).

> **Expectativa de soporte:** HorneroOS es un proyecto open-source en
> prelanzamiento **sin SLAs comerciales ni tiempos de respuesta garantizados**.
