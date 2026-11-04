# Primeros pasos

## Sabé qué hay disponible

HorneroOS publica una ISO Preview firmada: **v0.2.0-preview32**, una sola
imagen x86_64 que instala HorneroOS Desktop, Studio o Gaming Preview con
especializaciones creativas a elección. Es una preview, no una release
estable ni soportada.

- Descarga: [horneroos.com/install](https://www.horneroos.com/install) o la
  [release v0.2.0-preview32](https://github.com/HorneroOS/hornero/releases/tag/v0.2.0-preview32).
- ISO: `horneroos-2026.10-preview32-x86_64.iso` (2.8 GB, alojada en Vercel
  Blob porque supera el límite de 2 GB por asset de GitHub).
- SHA-256: `b8cd0f8604bc69f7d2112fb8bccd97115d32d197e9c92c62e02faf5de6345aec`
- Firma: firma GPG desacoplada de la clave de releases de HorneroOS
  `FCFBEE43925AB5429362278AE59EAB44AA2498DC`. La clave pública es
  `packaging/keys/hornero-release.pub.asc` en HorneroOS/hornero.

Verificá cada copia antes de escribila en un medio:

La clave pública viene directo del tag de la release, sin checkout:

```sh
key_base="https://raw.githubusercontent.com/HorneroOS/hornero"
curl -fsSL \
  "$key_base/v0.2.0-preview32/packaging/keys/hornero-release.pub.asc" \
  | gpg --import
gpg --verify horneroos-2026.10-preview32-x86_64.iso.sig \
  horneroos-2026.10-preview32-x86_64.iso
sha256sum -c horneroos-2026.10-preview32-x86_64.iso.sha256
```

## Requisitos y límites

- Máquina o VM x86_64; firmware UEFI o BIOS heredado.
- La ISO instala con el instalador provisional Calamares. El esquema de
  disco y el cifrado (LUKS) se eligen durante la instalación; nada viene
  preseleccionado, y confirmar una operación de particiones puede borrar
  datos.
- Alcance validado: las instalaciones UEFI sin cifrar de Desktop, Studio
  y Gaming pasaron sobre la ISO preview32 en máquinas virtuales
  desechables. Las instalaciones con cifrado LUKS, el BIOS heredado, las
  sesiones Niri y copytoram no se ejecutaron sobre este artefacto y no
  se heredan como aprobadas para preview32. La propia preview32 todavía
  no tiene validación en hardware físico.
- La aceptación en hardware físico de una estación de trabajo ASUS ROG
  Strix G16 está registrada como USER-VERIFIED en preview24 más arreglos
  post-instalación (ver `docs/PELICANO-PARITY.md` en HorneroOS/qa); los
  chequeos especializados como NVENC, corrección Vulkan y captura HDMI
  siguen NOT SPECIFICALLY TESTED. Studio, Desktop y Gaming son Preview,
  no Supported. Server y Agents son ediciones planificadas sin imagen
  instalable. Niri es experimental.
- Panda Foss está desarrollando el instalador oficial futuro; el camino
  Calamares de esta ISO es un puente provisional.

Escribí la ISO en un pendrive USB con un escritor gráfico de confianza, o
con `dd`. Con `dd`, primero confirmá el dispositivo de disco completo
con `lsblk` (escribir al dispositivo equivocado destruye sus datos) y
después ejecutalo con privilegios:

```sh
sudo dd if=horneroos-2026.10-preview32-x86_64.iso of=/dev/sdX bs=4M \
  status=progress conv=fsync
```

Arrancá desde el pendrive y seguí los pasos de Calamares. Reportá los
problemas de instalación en el
[selector de issues de HorneroOS/installer](https://github.com/HorneroOS/installer/issues/new/choose)
con el nombre de la ISO, tu firmware (UEFI o BIOS), si el disco está
cifrado y el paso donde falló.

Los componentes individuales también están empaquetados para quien ya
usa Arch Linux y Hyprland. Ese camino AUR es una alternativa para un
sistema Arch existente; la ISO es el camino de instalación principal. No
trates una lista de paquetes, un checkout de dotfiles ni una página vieja
de wiki como si fueran un instalador.

## Explorá antes de instalar

- Mirá capturas reales del producto en el [Showroom](https://github.com/HorneroOS/website/tree/main/src/content/showroom).
- Compará los [temas](https://github.com/HorneroOS/website/blob/main/src/pages/themes.astro)
  y los [layouts de barra](https://github.com/HorneroOS/website/blob/main/src/pages/layouts.astro)
  disponibles.
- Leé los [fundamentos del escritorio](../desktop/README.md), los
  [atajos](../../desktop/shortcuts.md) y la
  [apariencia](../../desktop/appearance.md).

## Después de instalar

Los sistemas instalados desde v0.2.0-preview24 necesitan una migración
manual única antes de que las actualizaciones normales funcionen; seguí
[Actualizar una instalación preview24 existente](../../getting-started/upgrading-from-preview24.md).
Seguí las notas de release para los cambios en la disponibilidad de
paquetes. Usá el
[selector de issues de HorneroOS/installer](https://github.com/HorneroOS/installer/issues/new/choose)
para fallos de instalación y el tracker del repositorio dueño para
problemas post-instalación.
