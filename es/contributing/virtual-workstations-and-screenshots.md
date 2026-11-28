# Estaciones virtuales, perfiles de pantalla y fábrica de capturas

- **Base visual oficial:** Full HD **`1920×1080` (`16:9`, escala `1.0`,
  `60 Hz`)**
- **Constructor canónico de VMs:** `HorneroOS/installer/scripts/build-vm-image.sh`
- **Motor de aceptación y capturas:** `HorneroOS/qa` (`hornero-qa`)

Esta guía explica cómo quienes contribuyen a HorneroOS arman estaciones
virtuales QCOW2 reproducibles, verifican compatibilidad entre hipervisores en
Linux, Windows y macOS, crean escenarios para Screenshot Factory y Demo Studio,
y trabajan con los seis niveles de CI de releases.

---

## 1. Base visual y 7 perfiles de pantalla

Todas las capturas insignia, los recursos del showroom y los masters de YouTube
se estandarizan en **Full HD `1920×1080`** a escala `1.0` para que la
tipografía Hornero Signal (IBM Plex) y las barras conserven proporciones
idénticas entre `HorneroOS/qa`, `HorneroOS/website` y `HorneroOS/playground`.

| # | Perfil | Tamaño | Escala | Uso principal |
| --- | --- | --- | --- | --- |
| 1 | `fhd-baseline` | `1920×1080` | `1.0` | Capturas, YouTube, hero |
| 2 | `laptop-1280x800` | `1280×800` | `1.0` | Playground, smoke QA |
| 3 | `wxga-1366x768` | `1366×768` | `1.0` | Regresión angosta |
| 4 | `qhd-2560x1440` | `2560×1440` | `1.0` | Código / DAW multi-ventana |
| 5 | `uhd-4k-scaled` | `3840×2160` | `1.5`/`2` | Escala HiDPI y demos 4K |
| 6 | `vertical-shorts` | `1080×1920` | `1.0` | Shorts y clips 9:16 |
| 7 | `dual-mixed-dpi` | `1080p`+`800p` | Mixta | QA multi-monitor |

> **Nota sobre pines Lua (`HorneroOS/qa`):** Dentro de invitados Hyprland con
> Lua en QA, `qa/guest/hyprland.lua` fija `Virtual-1` a `1280×800`. Al crear un
> escenario `1920×1080` o `1366×768`, actualizá tanto `requires.resolution`
> como un paso explícito `hyprctl eval 'hl.monitor({ output = "Virtual-1",
> mode = "1920x1080@60", position = "0x0", scale = 1 })'` en `setup.commands`.

---

## 2. Compilar VMs QCOW2 oficiales y 6 perfiles de imagen

HorneroOS genera discos de VM preinstalados de forma determinista a partir de
`HorneroOS/installer/installer.lock.yaml` y
`HorneroOS/hornero/editions/catalogue.yaml` usando **`arch-install-scripts`
(`pacstrap`)** (el patrón `arch-boxes` de Arch). **Nunca** usa scripts
frágiles `boot_command` de Packer ni clona la máquina de un desarrollador.

```sh
# Previsualizar el plan determinista y cierre de paquetes sin root
./scripts/build-vm-image.sh \
  --edition desktop \
  --compositor hyprland \
  --demo \
  --dry-run

# Generar QCOW2 demo comprimido (.qcow2.zst + .sha256 + .manifest.json)
sudo ./scripts/build-vm-image.sh \
  --edition desktop \
  --compositor hyprland \
  --demo \
  --disk-size 24G \
  --output-dir ./output
```

Flags principales en `HorneroOS/installer/scripts/build-vm-image.sh`:

- `--edition`: `desktop | studio | gaming`
- `--compositor`: `hyprland | niri`
- `--demo`: embebe `hornero-playground-demo` (autologin `hornero`, bloqueo por
  inactividad desactivado, `/home/hornero/Workspace` precargado)
- `--disk-size`: por ejemplo `24G` o `32G`
- `--no-compress`: emite `.qcow2` sin comprimir (iteración local más ágil)
- `--dry-run`: imprime plan JSON y lista de paquetes sin root ni escrituras

### Seis perfiles oficiales de imagen

| # | Perfil | Edición | Comp. | Demo | Salida y uso |
| --- | --- | --- | --- | --- | --- |
| 1 | `desktop-hyprland` | `desktop` | `hypr` | No | `.qcow2.zst` estándar |
| 2 | `desktop-niri` | `desktop` | `niri` | No | `.qcow2.zst` Niri exp. |
| 3 | `studio-hyprland` | `studio` | `hypr` | No | Disco Studio |
| 4 | `gaming-hyprland` | `gaming` | `hypr` | No | Disco Gaming (solo VM) |
| 5 | `playground-demo` | `desktop` | `hypr` | **Sí** | Base Playground/Demo |
| 6 | `qa-uncompressed` | Cualq. | Cualq. | Opc. | `.qcow2` sin comprimir |

Cada archivo publicado que supere el tope de 2 GiB de GitHub se distribuye por
almacenamiento de objetos externo (Vercel Blob / Cloudflare R2) con
`SHA256SUMS` y `.sig` GPG firmado por
`FCFBEE43925AB5429362278AE59EAB44AA2498DC`.

---

## 3. Matriz de compatibilidad entre hipervisores

El stack Wayland de HorneroOS (`hyprland 0.57.2-1` sobre **Aquamarine**,
`niri` experimental sobre **Smithay** y **Quickshell** en **Qt 6**) exige
DRM/EGL funcional o un fallback explícito por software (verificado al
`2026-11-28`):

| Nivel | Hipervisor / Host | Driver | Resumen UX |
| --- | --- | --- | --- |
| **Probado** | **QEMU/KVM** | `virtio-vga-gl` | Mejor 60 FPS (VirGL) |
| **Probado** | **libvirt / `virt-mgr`** | VirtIO 3D | 60 FPS vía `virgl` |
| **Probado** | **Quickemu** | `gl="on"` EFI | 60 FPS en 1 comando |
| **Compat.** | **VMware WS / Fusion** | `vmwgfx` | Usable; RHI si negro |
| **Compat.** | **GNOME Boxes** | VirtIO GL | Usable; UI básica |
| **Exp./SW** | **Oracle VirtualBox** | `VMSVGA` | Lento `llvmpipe` |
| **Exp./SW** | **macOS UTM** (ARM) | QEMU **TCG** | Lento (`x86_64` emu) |
| **Exp./SW** | **Microsoft Hyper-V** | `hyperv_fb` | Lento; sin Mesa 3D |
| **No sop.** | **Hosts ARM64** | N/A | Solo `x86_64` |
| **No sop.** | **Parallels (ARM)** | FEX `x86_64` | Lento + rompe Wayland |

*(Leyenda: **Probado** = Probado oficialmente; **Compat.** = Compatible con
límites; **Exp./SW** = Experimental / Software; **No sop.** = No soportado.)*

### Detalles y advertencias honestas por hipervisor

- **QEMU/KVM (`hornero-vm-run.sh`), libvirt y Quickemu *(Probado
  oficialmente)*:** Requiere `/dev/kvm` y `/dev/dri/renderD*` para VirGL
  (`virtio-vga-gl`, `AQ_NO_MODIFIERS=1`, `QSG_RHI_BACKEND=opengl` inyectados
  por `hornero-vm-gpu-detect`). Venus (`venus=true`) exige Linux `>= 6.13`,
  QEMU `>= 9.2` y Mesa `>= 24.2`.
- **VMware Workstation / Fusion y GNOME Boxes *(Compatible con límites)*:**
  VMware (gratuito para uso personal) requiere `svga.enable3d = "TRUE"`; si
  Quickshell muestra pantalla negra sobre `vmwgfx` EGL/dmabuf, exportá
  `QSG_RHI_BACKEND=opengl` o `software`. GNOME Boxes reutiliza libvirt/VirGL
  pero expone menos controles de OVMF o Venus.
- **Oracle VirtualBox *(Experimental / Software)*:** Activar 3D cuelga o deja
  en negro Hyprland y Niri. Desmarcá **Habilitar aceleración 3D**, asigná 128
  MB de VRAM, instalá `virtualbox-guest-utils` y exportá
  `LIBGL_ALWAYS_SOFTWARE=1` + `QT_QUICK_BACKEND=software`.
- **macOS UTM *(Experimental / Software)*:** En Apple Silicon (`M1`–`M4`),
  `Hypervisor.framework` no virtualiza `x86_64`, así que UTM emula CPU por
  software vía QEMU TCG (muy lento aun con VirGL experimental ANGLE/MoltenVK).
  Las Mac Intel corren a velocidad cercana a nativa.
- **Microsoft Hyper-V *(Experimental / Software)*:** Las VMs Linux Gen 2
  estándar no tienen driver Mesa Gallium3D (`virtio_gpu`/`vmwgfx`) y caen en
  `hyperv_fb` + `llvmpipe`. GPU-P en GPUs de consumo no está soportado para
  Wayland en invitados Linux, y el puente Mesa `d3d12` es exclusivo de
  WSL2/WSLg.
- **ARM64 nativo y Parallels en Apple Silicon *(No soportado)*:** HorneroOS
  publica builds `x86_64` únicamente. La emulación `x86_64` de Parallels es
  mucho más lenta que ARM64 nativo, y Parallels Tools (redimensionado,
  portapapeles, arrastrar y soltar) falla en sesiones Wayland y exige X11.

---

## 4. Sumar escenarios a Screenshot Factory y Demo Studio

Las capturas y videos siguen una sola regla: **solo capturas reales de
HorneroOS en ejecución**, nunca maquetas ni renders sin verificar.

1. **Elegí el repositorio dueño correcto:**
   - **Escenarios QA y Screenshot Factory:** `HorneroOS/qa` bajo
     `scenarios/visual/` o `scenarios/playground/`.
   - **Slots de captura del producto y shot list:** `HorneroOS/website`
     (`src/data/capture-slots.json`, `docs/CAPTURES.md`).
   - **Guiones de YouTube / Demo Studio:** `HorneroOS/playground` (`demo/`) y
     [Flujo de producción para YouTube](../studio/youtube-production-workflow.md).
2. **Escribí el YAML del escenario en `HorneroOS/qa`:**
   - Fijá `requires.resolution` (preferí `1920x1080` para vitrina) y
     `requires.compositor` (`hyprland` o `niri`).
   - Prepará estado limpio en `setup.commands` (por ejemplo `horneroctl
     appearance theme apply hornero-signal-night --yes`, `qs ipc call notifs
     enableDnd` y `hyprctl eval 'hl.monitor(...)'` si cambiás resolución en
     Lua).
   - Nunca incluyas rutas personales, tokens ni directorios de usuario reales.
3. **Validá de forma estática antes de levantar KVM:**

   ```sh
   uv run hornero-qa validate
   uv run hornero-qa matrix --check
   ```

4. **Ejecutá en una ventana KVM aislada (serializada con `flock`):**

   ```sh
   flock ~/.local/share/hornero-signal-mission/vm.lock \
     uv run hornero-qa run visual/populated-hornero-right-1920x1080
   ```

   Abrí cada PNG del bundle de evidencia (`runs/<run-id>/`) para inspeccionar
   tipografía, márgenes y contraste antes de ingresarlo a `HorneroOS/website`.

---

## 5. Niveles de automatización CI de releases

Los runners alojados en GitHub no tienen `/dev/kvm`, por lo que HorneroOS
separa la **verificación estática rápida** de la **calificación gráfica en
KVM** en seis niveles:

| Nivel | Disparador | Entorno | Compuertas y salidas |
| --- | --- | --- | --- |
| **1. PR** | Pull request | GitHub | `ruff`, `mypy`, lint, `--dry-run` |
| **2. `main`** | Merge | GitHub | Locks, verdad, capturas, i18n |
| **3. Nightly** | Cron | GH + KVM | Alarma 45d; refresco KVM |
| **4. RC** | Freeze | Host KVM | `build-iso.sh`, VMs, QA |
| **5. Release** | Tag | GH + firma | `.sig` GPG, `SHA256SUMS`, AUR, R2 |
| **6. Manual** | Dispatch | Operador | ISO live, HW, `release-bump` |

### Detalle exacto por nivel

- **PR:** `ruff`, `mypy --strict`, `pytest`, `shellcheck`, `markdownlint`,
  `check-horneroctl-refs.py`, `check-i18n-links.py`, `check-installer.py`,
  `hornero-qa validate`, `hornero-qa matrix --check` y
  `build-vm-image.sh --dry-run`.
- **`main`:** Chequeos de lock de composición más `check-release-truth`,
  `check-captures` y `check-i18n` en `website`.
- **Nightly / Semanal:** `evidence-staleness.yml` corre `hornero-qa matrix
  --stale-days 45`; ventanas KVM programadas refrescan evidencia vencida.
- **RC:** Congelamiento inmutable de `manifests/`, compilación candidata
  ISO/QCOW2 y suites `install/*`, `smoke/*` y `scenarios/playground/` en VMs
  desechables.
- **Release:** Firma con `FCFBEE43925AB5429362278AE59EAB44AA2498DC`,
  publicación en GitHub Releases/AUR y almacenamiento externo (>2 GiB) junto a
  un checklist inmutable en `HorneroOS/hornero/releases/`.
- **Manual:** Lanzamientos de ISO live (`installer/docs/release-iso.md`),
  corridas físicas `PELICANO-PARITY` / `studio-gate` / `gaming-gate` y
  `release-bump` / `sync-product-data` en `website`.

---

## Guías relacionadas

- [Flujo de producción para YouTube y contenido](../studio/youtube-production-workflow.md)
- [Probá HorneroOS sin instalar](../getting-started/try-horneroos.md)
- [Pruebas](../development/testing.md)
- [Calidad y releases](../development/quality-and-releases.md)
