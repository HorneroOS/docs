# Utilidades del sistema y línea de comandos

Esta guía distingue la configuración del sistema de Hornero de las
aplicaciones del perfil más amplio de estación de trabajo personal en Arch. Un
archivo bajo `/etc/xdg` es un valor por defecto del sistema; un archivo bajo
`~/.config` pertenece al usuario y puede sobrescribirlo. Los paquetes exactos
instalados siguen dependiendo del host y de la composición elegida.

## Herramientas configuradas por Hornero Config

El paquete `hornero-config` requiere Bash, Git, Python, `polkit-gnome` y
`ttf-ibm-plex` (las tipografías de Hornero Signal). Sus metadatos de paquetes
opcionales nombran herramientas para las que puede proveer valores por defecto:

### Herramientas de terminal y desarrollo

- **Git** — valores compartidos y reglas de ignore en `/etc/xdg/git/`. Sumá
  tus propios `user.name` y `user.email`; Hornero no incluye identidad a
  propósito.
- **Fastfetch** — resumen del sistema en terminal. Los valores por defecto
  viven en `/etc/xdg/fastfetch/`; la estación de trabajo personal agrega una
  marca de texto de Hornero.
- **btop** — monitor interactivo de CPU, memoria, procesos y dispositivos. Los
  valores por defecto viven en `/etc/xdg/btop/`. Hornero elige su tema
  `Hornero Dynamic`, que se reescribe desde la paleta Signal del tema
  aplicado. Mirá [Apariencia](../desktop/appearance.md).

### Apariencia e integración del escritorio

- **Fontconfig** — valores por defecto de selección de fuentes bajo
  `/etc/xdg/fontconfig/`; los archivos de fuentes son paquetes separados.
- **GTK 3/4** — preferencias de tema, íconos y modo claro/oscuro bajo rutas de
  configuración XDG. Hornero también trae un árbol de tema GTK para cada tema
  Signal (`Hornero-Signal`, `Hornero-Signal-Day`, `Hornero-Signal-Contrast` y
  uno por cada Hornero Original).
- **`qt6ct`** — tema y paleta opcionales de Qt 6 bajo `/etc/xdg/qt6ct/`. Las
  aplicaciones lo usan solo cuando el host elige `qt6ct` como tema de
  plataforma.
- **Íconos Papirus** — paquete externo opcional de íconos referenciado por los
  valores de fábrica. El respaldo del host sigue disponible cuando falta.
- **Kitty**, **Thunar**, **CopyQ** y **`handlr`** — valores por defecto
  opcionales de aplicaciones bajo `/etc/xdg/kitty/`, `/etc/xdg/Thunar/`,
  `/etc/xdg/copyq/` y `/etc/xdg/handlr/`. Mirá [Terminal](terminal.md),
  [Archivos](files.md), [Portapapeles](clipboard.md) y
  [Aplicaciones por defecto](default-apps.md).

### Medios

- **Cava** — configuración opcional del visualizador de audio en terminal bajo
  `/etc/xdg/cava/`. Su tema de colores `Hornero Dynamic` sigue al tema
  aplicado. No inicia el visualizador de la Shell, que viene desactivado por
  defecto. Mirá [Apariencia](../desktop/appearance.md) y
  [Medios y audio](media-audio.md).

Son valores por defecto e integraciones. Los programas marcados como opcionales
no se instalan solo porque exista su archivo de configuración. Inspeccioná los
[metadatos de dependencias](https://github.com/HorneroOS/config/blob/main/packaging/PKGBUILD)
del paquete para ver los nombres actuales de paquetes requeridos y opcionales.

## Herramientas en la configuración de estación de trabajo personal

El [repositorio público de dotfiles](https://github.com/ulises-jeremias/dotfiles)
describe una estación de trabajo más amplia; no es el manifiesto de release de
Hornero. Su perfil público de Arch puede instalar herramientas como:

**Helpers de shell:** `bat`, `exa`, `fzf`, `fd`, `ripgrep`, `zoxide`, `direnv`
y `jq` ayudan con listados, búsqueda, navegación, inspección de JSON y
entornos por proyecto.

**Herramientas de código fuente y paquetes:** Git, `github-cli`, Python, `uv`,
`pacman-contrib` y ShellCheck ayudan en desarrollo y mantenimiento del sistema.

**Utilidades de dispositivos:** `acpi`, `upower`, `brightnessctl` y
`power-profiles-daemon` informan o cambian el estado de dispositivos.

**Captura en Wayland:** `grim`, `slurp`, `sss` y GPU Screen Recorder proveen
backends opcionales de captura. Mirá [Capturas y grabación](capture.md).

**Integración de sesión:** `gnome-keyring`, `dex` y `polkit-gnome` proveen
almacenamiento de secretos, autoarranque XDG y avisos de privilegios.

**Medios y sonido:** PipeWire, `pamixer`, `playerctl`, `pavucontrol`, Cava y
mpv dan soporte de ruteo de audio, control multimedia, visualización y
reproducción.

**Archivos y vistas previas:** Yazi, Thunar, Xarchiver, `ffmpegthumbnailer`,
Poppler e ImageMagick dan soporte de navegación, archivos comprimidos y vistas
previas. Mirá [Archivos](files.md).

**Apps de escritorio opcionales:** Zen Browser, Neovim, sxiv, Discord, Lutris,
Docker y Safe Eyes cubren navegación, edición, imágenes, colaboración, gaming,
desarrollo y descanso visual.

Estos grupos cubren gestión de código, hardware, captura, sesiones, medios,
archivos comprimidos y flujos opcionales de escritorio. Para lanzamiento y
solución de problemas, seguí la guía enlazada correspondiente de arriba.

El perfil personal puede variar según el modo de máquina y el hardware
disponible. Las herramientas opcionales de ese repositorio no implican que un
release limpio de Hornero las instale.

## Solucionar problemas desde la capacidad hacia afuera

Cuando un botón o una tecla no funciona, inspeccioná primero la capacidad de
Hornero y después su dependencia del host:

```sh
horneroctl doctor
horneroctl apps launch --list
horneroctl config default-apps list
```

Por ejemplo, la Shell puede mostrar un control multimedia aunque el host no
tenga un reproductor MPRIS; un tema puede elegir Papirus aunque falte su
paquete de íconos; y un comando de captura puede existir aunque falte su
backend de Wayland. El mensaje de estado debería identificar la capacidad
faltante. Hornero no instala programas opcionales en silencio.

## Herramientas de implementación interna

Las bibliotecas de implementación, herramientas de compilación, fixtures de
test y metadatos generados se documentan en su repositorio dueño en vez de
listarse como apps de usuario. No son un segundo catálogo de paquetes. La
[guía de arquitectura](../architecture/README.md) describe qué capa es dueña de
cada capacidad del producto.
