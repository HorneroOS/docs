# Catálogo de aplicaciones

Este catálogo describe los límites entre el producto Hornero, los servicios
del host y el perfil personal de estación de trabajo mantenido por separado.
Un programa listado como opcional no se instala en silencio mediante Hornero
Config. La disponibilidad de paquetes depende del host y la composición
elegida.

Buscá en la página tanto por el nombre de la aplicación como por el nombre de
la tarea. Por ejemplo, **Kitty**, **Alacritty**, **Ghostty**, **terminal**,
**Thunar**, **archivos**, **Yazi**, **portapapeles**, **CopyQ**, **PDF**,
**navegador**, **video** y **captura** están indexados junto con sus flujos.

## Producto Hornero y sesión

| Componente | Rol en Hornero | Dónde aprender más |
| --- | --- | --- |
| Hornero Shell (Quickshell) | Dueña de barras, Lanzador, Dashboard, Centro de control, notificaciones, OSD y presentación multimedia. | [Escritorio](../desktop/README.md), [código fuente y docs de la Shell](https://github.com/HorneroOS/shell) |
| `horneroctl` | CLI soportada para apariencia, configuración, hardware, captura y acciones de aplicaciones. También ofrece diagnósticos independientes de la shell. | [Referencia de la CLI](../desktop/horneroctl.md), [repositorio upstream](https://github.com/HorneroOS/hornero) |
| Hyprland | Compositor Wayland e integración de sesión usados por el entorno de referencia actual. | [Atajos](../desktop/shortcuts.md), [documentación upstream](https://wiki.hypr.land/) |
| `hornero-config` | Valores por defecto declarativos, paquetes de temas, fragmentos de aplicaciones e integración de paquetes; no provee un SO instalado completo. | [Apariencia](../desktop/appearance.md), [repositorio Config](https://github.com/HorneroOS/config) |
| Bash, Git, Python, `polkit-gnome`, `ttf-ibm-plex` | Dependencias obligatorias del paquete `hornero-config`: helpers, renderizadores de temas, avisos de privilegios y familias IBM Plex. | [Referencia de la CLI](../desktop/horneroctl.md), [Temas](../desktop/appearance.md) |

## Terminal y línea de comandos

| App o herramienta | Estado en Hornero | Configuración / flujo |
| --- | --- | --- |
| Kitty | Paquete opcional del host elegido como terminal por defecto de fábrica. Hornero provee valores de sistema; **Super + E** usa la terminal configurada, incluyendo Kitty, Alacritty o Ghostty. | [`~/.config/kitty/kitty.conf`](terminal.md#kitty), [Guía de terminal](terminal.md), [manual de Kitty](https://sw.kovidgoyal.net/kitty/) |
| Alacritty | Alternativa opcional con respaldo empaquetado `/etc/alacritty/alacritty.toml` e import de la paleta del tema aplicado. La configuración de usuario puede sobrescribir el respaldo. | [Guía de Alacritty](terminal.md#alacritty), [referencia de configuración](https://alacritty.org/config-alacritty.html) |
| Ghostty | Alternativa opcional con tema del sistema `Hornero Dynamic`, semilla de configuración para usuarios nuevos y paletas por usuario escritas desde el tema aplicado. Las configuraciones existentes no se sobrescriben. | [Guía de Ghostty](terminal.md#ghostty), [guía de configuración](https://ghostty.org/docs/config) |
| Bash | Requerido por `hornero-config`; usado por scripts de paquete y helpers de shell. | [Guía de terminal](terminal.md#shell-y-flujo-de-comandos), [manual de Bash](https://www.gnu.org/software/bash/manual/) |
| Zsh | Elección de estación de trabajo personal, no es dependencia de Hornero Config. El perfil de dotfiles configura su prompt y archivos de inicio. | [Guía de terminal](terminal.md#shell-y-flujo-de-comandos), [documentación de Zsh](https://zsh.sourceforge.io/Doc/) |
| tmux | Multiplexor de terminal opcional personal con configuración y helpers de sesión gestionados por dotfiles. | [Guía de terminal](terminal.md#shell-y-flujo-de-comandos), [manual de tmux](https://github.com/tmux/tmux/wiki) |
| Git | Requerido por Config; recibe alias compartidos, reglas de ignore y valores por defecto cuando se usa el perfil de dotfiles. Hornero no fija una identidad personal de commits. | [Guía de terminal](terminal.md#shell-y-flujo-de-comandos), [libro de Git](https://git-scm.com/book/en/v2) |
| `bat`, `exa`, `fzf`, `direnv`, `jq`, `uv`, `shellcheck` | Herramientas opcionales de línea de comandos del perfil personal de estación de trabajo. No son requisitos de Hornero Shell. | [Guía de terminal](terminal.md#shell-y-flujo-de-comandos), [repositorio de dotfiles](https://github.com/ulises-jeremias/dotfiles) |
| Fastfetch, btop, Cava | Resumen de terminal, monitor de recursos y visualizador de audio opcionales configurados. El visualizador de la Shell se activa por separado. | [Utilidades del sistema](system-utilities.md), [Fastfetch](https://github.com/fastfetch-cli/fastfetch), [btop](https://github.com/aristocratos/btop), [Cava](https://github.com/karlstav/cava) |

## Archivos, navegación y documentos

| App o herramienta | Estado en Hornero | Configuración / flujo |
| --- | --- | --- |
| Thunar | Gestor de archivos opcional. Config agrega acciones de teclado útiles e integraciones contextuales; **Super + F** sigue la asociación `FileManager` del host. | [Archivos](files.md#thunar-para-gestión-visual-de-archivos), [documentación de Thunar](https://docs.xfce.org/xfce/thunar/start) |
| Yazi | Gestor de archivos en terminal opcional, no es dependencia de Hornero Config. **Super + E** lo abre en la terminal configurada cuando está instalado; las herramientas de vista previa son opcionales. | [Archivos](files.md#yazi-para-navegar-desde-el-teclado), [documentación de Yazi](https://yazi-rs.github.io/docs/) |
| `xdg-mime`, `exo-open`, archivos `.desktop` | Mecanismos del host que eligen la app por defecto para una URL o tipo MIME. Hornero pide esos manejadores en vez de incrustar un navegador o gestor de archivos. | [Aplicaciones por defecto](default-apps.md), [aplicaciones MIME de freedesktop](https://specifications.freedesktop.org/mime-apps-spec/latest/) |
| Zen Browser | Navegador opcional del perfil personal. No es el navegador obligatorio ni dependencia de paquetes de Hornero. | [Navegación, edición y documentos](browsing-documents.md#navegación), [Zen](https://zen-browser.app/) |
| Neovim, VS Code y otros editores | Elegidos por el host. El perfil personal contiene configuración de editor; Hornero no exige un editor único. | [Navegación, edición y documentos](browsing-documents.md#editores), [Aplicaciones por defecto](default-apps.md) |
| Zathura, Evince y otros visores PDF | Elección MIME del host; ninguno es requerido por Hornero Config. | [Navegación, edición y documentos](browsing-documents.md#pdfs-imágenes-y-archivos-multimedia), [Aplicaciones por defecto](default-apps.md) |
| sxiv y otros visores de imágenes | Visor de imágenes opcional del perfil personal; abrir archivos sigue la asociación MIME de imágenes del host. | [Navegación, edición y documentos](browsing-documents.md#pdfs-imágenes-y-archivos-multimedia), [Aplicaciones por defecto](default-apps.md) |
| mpv y otros reproductores multimedia | Apps de reproducción opcionales. Los controles de la Shell se conectan a reproductores MPRIS activos; abrir archivos sigue los valores MIME por defecto. | [Medios y audio](media-audio.md#reproductores-de-medios), [manual de mpv](https://mpv.io/manual/stable/) |
| Xarchiver y helpers de archivos comprimidos | Herramientas opcionales del host usadas por acciones del gestor de archivos; instalar la Shell no implica soporte de compresión. | [Archivos](files.md#apertura-de-archivos-y-archivos-comprimidos), [Xarchiver](https://github.com/ib/xarchiver) |

## Portapapeles, captura, audio y conectividad

| App o servicio | Rol y disponibilidad | Guía |
| --- | --- | --- |
| CopyQ | Interfaz opcional de historial del portapapeles con configuración y colores de tema de Hornero. | [Portapapeles](clipboard.md), [manual de CopyQ](https://copyq.readthedocs.io/en/latest/) |
| `wl-clipboard`, `cliphist` | Herramientas separadas de portapapeles de Wayland; el perfil personal de sesión puede correr `wl-paste --watch` para recolectar historial. Los datos del portapapeles son sensibles. | [Portapapeles](clipboard.md), [wl-clipboard](https://github.com/bugaevc/wl-clipboard), [cliphist](https://github.com/sentriz/cliphist) |
| `grim`, `slurp`, `swappy`, `sss`, GPU Screen Recorder | Backends opcionales de captura de pantalla, selección de región, anotación y grabación. `horneroctl capture` informa o invoca las herramientas disponibles. | [Capturas y grabación](capture.md) |
| PipeWire, WirePlumber, `pamixer`, `pavucontrol`, `playerctl` | Servidor de sonido, mezclador y controles MPRIS propiedad del host. La instalación exacta varía; Hornero no reemplaza el stack de audio. | [Medios y audio](media-audio.md), [PipeWire](https://pipewire.org/), [playerctl](https://github.com/altdesktop/playerctl) |
| NetworkManager, BlueZ, plugins VPN | Proveedores de red, Bluetooth y VPN propiedad del host. El Centro de control opera solo cuando existe un servicio o proveedor compatible. | [Conectividad](connectivity.md), [NetworkManager](https://networkmanager.dev/), [BlueZ](http://www.bluez.org/) |
| `brightnessctl`, `acpi`, `upower`, `power-profiles-daemon` | Utilidades opcionales del host para brillo, batería y estado del perfil de energía. El soporte del dispositivo determina qué controles aparecen. | [Utilidades del sistema](system-utilities.md#herramientas-en-la-configuración-de-estación-de-trabajo-personal) |

## Apariencia, login y soporte del escritorio

| App o componente | Rol y disponibilidad | Guía |
| --- | --- | --- |
| GTK, Fontconfig, `qt6ct` | Componentes opcionales de apariencia del host. Hornero puede configurarlos; los temas GTK y paquetes de íconos externos se instalan por separado. | [Apariencia](../desktop/appearance.md) |
| Papirus, Numix Circle, Orchis | Paquetes opcionales de íconos y temas GTK usados por el perfil personal y paquetes de temas. Los paquetes faltantes producen un estado de respaldo o degradado documentado. | [Apariencia](../desktop/appearance.md#paquetes-de-temas) |
| IBM Plex Sans, Mono y Sans Condensed (`ttf-ibm-plex`) | Tipografías de Hornero Signal para la Shell, GTK, Qt y terminales; dependencia dura de `hornero-config`. Los íconos de la Shell son los Hornero Glyphs incluidos, así que no se requiere una fuente de íconos. Otras fuentes siguen disponibles a elección del usuario. | [Apariencia](../desktop/appearance.md) |
| Hyprlock, Hypridle | Herramientas opcionales de bloqueo y sesión en reposo, separadas de las notificaciones y controles de la Shell. | [Bloqueo y login](login-lock.md#bloquear-la-sesión) |
| SDDM y Hornero Greeter | Componentes separados de gestor de pantalla y pantalla de login. No forman parte de la composición Preview. | [Bloqueo y login](login-lock.md#hornero-greeter) |
| Portals, `polkit-gnome`, `libnotify`, `dex` | Servicios y helpers de sesión usados para diálogos de archivos, avisos de privilegios, compatibilidad de notificaciones y autoarranque de escritorio. Son componentes de integración, no apps de usuario final. | [Utilidades del sistema](system-utilities.md#herramientas-de-implementación-interna) |

## Apps que no son de cara al usuario

Las bibliotecas solo de compilación, los helpers de materialización de
`hornero-config`, los servicios de Quickshell, los generadores de temas, las
herramientas de QA de capturas y los hooks de paquetes implementan el
escritorio pero no se presentan como aplicaciones. Sus contratos de desarrollo
pertenecen a los repositorios Config, Shell, CLI y QA. Las utilidades
específicas de hardware y los perfiles opcionales pueden variar según la
máquina.

La [guía de Apps y flujos](README.md) enlaza los recorridos completos de
usuario. Para manejadores por defecto, empezá por
[Aplicaciones por defecto](default-apps.md); para la fuente pública de la
estación de trabajo, mirá
[ulises-jeremias/dotfiles](https://github.com/ulises-jeremias/dotfiles).
