# Apps y flujos

Hornero es un producto de escritorio, no una colección fija de
aplicaciones de terceros. Su Shell es dueña de las superficies del
escritorio, Hornero Config provee los valores por defecto del sistema, y
el host decide qué aplicaciones y servicios opcionales están instalados.
Estas guías explican cómo se conectan esas partes y qué revisar cuando
falta una.

## ¿Qué es parte de Hornero?

La composición Preview actual se distribuye en la ISO firmada
v0.2.0-preview32 (Desktop, Studio y Gaming Preview, instalador
provisional Calamares). Reúne a Hornero Shell, `horneroctl` y el paquete
`hornero-config`. Config requiere Bash, Git, Python y
`python-materialyoucolor`; no instala una estación de trabajo completa
por sí solo.

### Valores por defecto de Hornero para aplicaciones opcionales

Estos programas siguen siendo paquetes separados del host. Si están
instalados, pueden usar los valores por defecto que provee Hornero
Config:

- **Kitty** — colores de terminal, tipografía y ajustes de teclas;
  seleccionado por defecto para el flujo Yazi con **Super + E**. Esa
  acción sigue a la terminal configurada, incluyendo Alacritty o Ghostty.
  Ver [Terminal](../../applications/terminal.md).
- **Alacritty** y **Ghostty** — alternativas opcionales de terminal con
  fallback nativo de Hornero e integración de paleta derivada del fondo.
  No los instala Hornero Config. Ver
  [Terminal](../../applications/terminal.md).
- **Thunar** — aceleradores del gestor de archivos, renombrado masivo y
  acciones de contexto. **Super + F** le pide al host que abra su
  FileManager. Ver [Archivos](../../applications/files.md).
- **CopyQ** — configuración de la UI del historial del portapapeles y
  colores de tema generados. Ver
  [Portapapeles](../../applications/clipboard.md).
- **Fastfetch**, **btop** y **Cava** — configuración del resumen de
  terminal, el monitor de recursos y el visualizador. Ver
  [Utilidades del sistema](../../applications/system-utilities.md).
- **Git** — valores compartidos y reglas de ignore, sin identidad de
  usuario. Sumá tu propio nombre y email antes de crear commits.
- **Fontconfig**, **GTK**, **qt6ct** y **Papirus** — valores por defecto
  de tipografías y apariencia de aplicaciones. Los temas GTK y los
  paquetes de íconos externos pueden faltar; Hornero no los descarga. Ver
  [Apariencia](../../desktop/appearance.md).
- **`handlr`** — integración opcional para inspeccionar manejadores de
  archivos y aplicaciones. [`horneroctl`](../../desktop/horneroctl.md)
  usa `xdg-mime` para actualizar las asociaciones MIME.

### Servicios y aplicaciones del host

- **Hyprland** ejecuta la sesión de escritorio configurada. Hornero
  Config provee sus valores por defecto; ver
  [atajos](../../desktop/shortcuts.md).
- **Quickshell / Hornero Shell** es dueña de las barras, el lanzador, el
  Dashboard, las notificaciones, el OSD y el Centro de control. Ver la
  [guía del escritorio](../desktop/README.md) y la
  [documentación de la Shell](https://github.com/HorneroOS/shell/tree/main/docs).
- **`exo-open` y los helpers XDG** inician la terminal, el gestor de
  archivos, el navegador y los manejadores MIME elegidos por el host. Ver
  [Aplicaciones por defecto](../../applications/default-apps.md).
- **Yazi** no es una dependencia del paquete Config, pero **Super + E**
  lo abre en la terminal configurada. El perfil de estación de trabajo
  personal puede instalar Yazi y helpers de vista previa. Ver
  [Archivos](../../applications/files.md).
- **`cliphist` y `wl-clipboard`** pueden recolectar el historial del
  portapapeles de Wayland; **PipeWire**, `pamixer`, `pavucontrol` y
  `playerctl` proveen la integración de audio y medios del host. Ver
  [Portapapeles](../../applications/clipboard.md) y
  [Medios y audio](../../applications/media-audio.md).
- **NetworkManager y BlueZ** proveen los servicios de red y Bluetooth del
  host. El Centro de control expone su estado; ver
  [Conectividad](../../applications/connectivity.md).
- **`sss`, `grim`, `slurp` y GPU Screen Recorder** proveen backends
  opcionales de captura. Ver
  [Capturas y grabación](../../applications/capture.md).
- **Hyprlock e Hypridle** soportan el bloqueo y el comportamiento en
  reposo. **SDDM y Hornero Greeter** son componentes de login separados,
  no parte de la composición Preview actual. Ver
  [Bloqueo y login](../../applications/login-lock.md).

### Aplicaciones opcionales de la estación de trabajo personal

El [repositorio público de dotfiles](https://github.com/ulises-jeremias/dotfiles)
configura una estación de trabajo Arch más amplia. Sus aplicaciones
opcionales incluyen Zen Browser, Zsh, tmux, mpv, sxiv, Xarchiver y
herramientas de audio o estudio. No son valores por defecto de las
releases de Hornero; las páginas de flujos relevantes explican su rol.

Los metadatos exactos de dependencias del paquete de release se mantienen
en [Hornero Config](https://github.com/HorneroOS/config/blob/main/packaging/PKGBUILD).
El [repositorio de dotfiles](https://github.com/ulises-jeremias/dotfiles)
es una configuración de estación de trabajo separada y más amplia. Sirve
para entender el setup de aplicaciones personal, pero el comportamiento
del producto Hornero no depende de ejecutar sus comandos de provisión.

## Seguí un flujo

- [Terminal](../../applications/terminal.md) — Kitty, Alacritty, Ghostty,
  la shell de la cuenta, Zsh y tmux.
- [Archivos](../../applications/files.md) — Thunar, Yazi, vistas previas,
  archivos compactados y asociaciones de archivos.
- [Portapapeles](../../applications/clipboard.md) — CopyQ, historial del
  portapapeles de Wayland y privacidad.
- [Aplicaciones por defecto](../../applications/default-apps.md) —
  manejadores de apps del host y tipos MIME.
- [Navegación, edición y documentos](../../applications/browsing-documents.md) —
  navegadores, editores, PDFs y asociaciones de imágenes/archivos.
- [Medios y audio](../../applications/media-audio.md) — PipeWire,
  controles de volumen, MPRIS y reproductores.
- [Aplicaciones de Studio](../../applications/studio.md) — matriz
  verificada de origen, licencia y soporte de la edición Studio Preview.
- [Primeros pasos en Studio](../../applications/studio-getting-started.md) —
  recorrido del primer proyecto para la edición Studio Preview.
- [Audio en Studio](../../applications/studio-audio.md) — configuración
  de modos, ruteo y recuperación para la edición Studio Preview.
- [Aplicaciones de Gaming](../../applications/gaming.md) — matriz
  verificada de origen, licencia y soporte de la edición Gaming Preview.
- [Capturas y grabación](../../applications/capture.md) — backends de
  captura de pantalla y grabación.
- [Conectividad](../../applications/connectivity.md) — NetworkManager,
  Bluetooth y proveedores de VPN.
- [Utilidades del sistema](../../applications/system-utilities.md) — Git,
  Fastfetch, btop, Cava y helpers del host.
- [Bloqueo y login](../../applications/login-lock.md) — bloqueo de sesión
  versus login de SDDM.

Estas guías describen primero el contrato actual de Hornero. Las
elecciones opcionales de la estación de trabajo personal están
etiquetadas como tales. Los procedimientos históricos de la wiki fueron
revisados y clasificados en
[la disposición de fuentes](../../development/dotfiles-wiki-disposition.md);
las rutas viejas y los comandos `dots-*` no son instrucciones actuales.

Para un inventario buscable y con estados etiquetados de aplicaciones y
servicios integrados, ver el
[catálogo de aplicaciones](../../applications/catalogue.md). Separa los
componentes de Hornero de las apps opcionales del host y del perfil
público de la estación de trabajo personal.

El catálogo se organiza alrededor del trabajo que hace la gente:
[terminal](../../applications/catalogue.md#terminal-and-command-line),
[archivos y documentos](../../applications/catalogue.md#files-browsing-and-documents),
[portapapeles, captura y medios](../../applications/catalogue.md#clipboard-capture-audio-and-connectivity),
y [apariencia y login](../../applications/catalogue.md#appearance-login-and-desktop-support).
