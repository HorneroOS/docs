# Primeros pasos

Guía de instalación en orden:
[Instalar HorneroOS paso a paso](install-step-by-step.md), y después
[Primeros pasos después de instalar](../applications/post-install-first-steps.md).

## Sabé qué hay disponible

HorneroOS se usa a diario en producción en múltiples estaciones de trabajo
físicas y está validado en KVM con UEFI y Legacy BIOS. La release firmada actual
es **`v0.2.0-preview42`** (`x86_64`), que publica dos artefactos oficiales
firmados en [horneroos.com/install](https://www.horneroos.com/install) y en la
[release v0.2.0-preview42](https://github.com/HorneroOS/hornero/releases/tag/v0.2.0-preview42)
*(nota: `v0.2.0-preview42` se mantiene como tag de git y nombre publicado del
artefacto)*:

- **ISO oficial Live e instalable (`3.3 GiB`, UEFI + Legacy BIOS, validada en
  hardware físico y KVM):** Instala HorneroOS **Desktop**, **Studio** o
  **Gaming** con especializaciones creativas a elección, **Hornero Signal**,
  **Hornero Apps**, **Signal Flight Welcome (`v1.6.0`)** y **Calamares
  `3.4.3`** (estética Signal Night).
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/iso/horneroos-2026.11-preview42-x86_64.iso`
  - SHA-256:
    `9e494ab5f9783df6a5986385421ec0816b0033d3558d3323248a03e07f2e76a2`
- **QCOW2 oficial preinstalada de Desktop (`2.61 GiB`):** Compilada en
  entorno limpio, saneada y validada punta a punta en KVM UEFI para arranque
  inmediato en VM local.
  - URL:
    `https://apvhgc6x8t0o0dzm.public.blob.vercel-storage.com/vm/horneroos-0.2.0-preview42-desktop-qemu-x86_64.qcow2.zst`
  - SHA-256:
    `c1012413227f407d0a312fad7d7a34f789922303db13c752a9a9ed1a324e13c2`
- **Firma:** Firma GPG desacoplada (`.sig`) y `.sha256` de la clave de
  releases de HorneroOS `FCFBEE43925AB5429362278AE59EAB44AA2498DC`. La clave
  pública está en `packaging/keys/hornero-release.pub.asc` dentro de
  `HorneroOS/hornero`.

Verificá cada copia antes de escribirla en un medio o arrancar una VM:

La clave pública viene directo del tag de la release, sin checkout:

```sh
key_base="https://raw.githubusercontent.com/HorneroOS/hornero"
curl -fsSL \
  "$key_base/v0.2.0-preview42/packaging/keys/hornero-release.pub.asc" \
  | gpg --import
gpg --verify horneroos-2026.11-preview42-x86_64.iso.sig \
  horneroos-2026.11-preview42-x86_64.iso
sha256sum -c horneroos-2026.11-preview42-x86_64.iso.sha256
```

## Requisitos y límites

- Máquina o VM `x86_64`; firmware UEFI o Legacy BIOS.
- La ISO instala con **Calamares 3.4.3** (estética Signal Night). El esquema de
  disco y el cifrado (LUKS) se eligen durante la instalación; nada viene
  preseleccionado, y confirmar una operación de particiones puede borrar datos.
- **Ediciones y compositores soportados:** **Desktop**, **Studio** y **Gaming**
  son ediciones **Soportadas** de uso diario. **Hyprland** es el compositor por
  defecto y **Niri** está soportado como opción de compositor Wayland con
  columnas desplazables (mirá [Compositores Wayland](../desktop/compositors.md)
  para las diferencias puntuales de capacidades). **Server**, **Agents** y
  **Labwc** siguen **Planificados** sin imágenes booteables.
- **Alcance validado:** HorneroOS corre a diario en producción en múltiples
  estaciones físicas, y `v0.2.0-preview42` aprobó validación en KVM UEFI y
  Legacy BIOS además de verificación en hardware físico. Las pruebas
  específicas por dispositivo (GPU/audio/handheld puntuales) se siguen en
  [Probado y no probado](../hardware/tested-and-untested.md); el rollback
  completo de raíz del SO sigue **Planificado**
  ([Actualizaciones y recuperación](../desktop/updates-and-rollback.md)).

Escribí la ISO en un pendrive USB con un escritor gráfico de confianza, o
con `dd`. Con `dd`, primero confirmá el dispositivo de disco completo
con `lsblk` (escribir al dispositivo equivocado destruye sus datos) y
después ejecutalo con privilegios:

```sh
sudo dd if=horneroos-2026.11-preview42-x86_64.iso of=/dev/sdX bs=4M \
  status=progress conv=fsync
```

Arrancá desde el pendrive y seguí los pasos de Calamares. Reportá los
problemas de instalación en el
[selector de issues de HorneroOS/installer](https://github.com/HorneroOS/installer/issues/new/choose)
con el nombre de la ISO, tu firmware (UEFI o BIOS), si el disco está
cifrado y el paso donde falló.

Los componentes individuales también están empaquetados para quien ya
usa Arch Linux y Hyprland. Ese camino AUR es una alternativa soportada
para un sistema Arch existente: seguí [Instalar HorneroOS sobre un Arch
Linux existente](install-on-arch.md) para los paquetes, la
configuración inicial que nunca sobrescribe y el camino de vuelta. No
trates una lista pelada de paquetes, un checkout de dotfiles ni una
página vieja de wiki como si fueran un instalador.

## Explorá antes de instalar

- Empezá por la
  [Guía de lanzamiento público](public-preview-launch-guide.md)
  para caminos en Windows, macOS (advertencias de Apple Silicon) y Arch Linux,
  limitaciones honestas, diagnóstico práctico y reportes de hardware/seguridad.
- Seguí [Probá HorneroOS sin instalar](try-horneroos.md) para sesiones en el
  navegador, máquinas virtuales locales, Live USB y modo presentador.
- Revisá el
  [Anuncio de lanzamiento v0.2.0-preview42](../releases/v0.2.0-preview42-announcement-draft.md)
  con lo más destacado del lanzamiento y el checklist de video para YouTube.
- Mirá capturas reales del producto en el [Showroom](https://horneroos.com/showroom/).
- Compará los [temas](https://horneroos.com/themes/)
  y los [layouts de barra](https://horneroos.com/layouts/)
  disponibles.
- Leé los [fundamentos del escritorio](../desktop/README.md), los
  [atajos](../desktop/shortcuts.md) y la
  [apariencia](../desktop/appearance.md).

## Después de instalar

Los sistemas instalados desde v0.2.0-preview24 necesitan una migración
manual única antes de que las actualizaciones normales funcionen; seguí
[Actualizar una instalación preview24 existente](upgrading-from-preview24.md).
Seguí las notas de release para los cambios en la disponibilidad de
paquetes. Usá el
[selector de issues de HorneroOS/installer](https://github.com/HorneroOS/installer/issues/new/choose)
para fallos de instalación y el tracker del repositorio dueño para
problemas post-instalación.
