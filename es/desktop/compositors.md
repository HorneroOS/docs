# Compositores Wayland

HorneroOS Desktop es un escritorio Wayland-first impulsado por Hornero Shell.
Un compositor gestiona las ventanas, los espacios de trabajo, las salidas, la
entrada y la sesión Wayland. Hornero Shell provee las barras compartidas, el
lanzador, el Dashboard, el Centro de control, las notificaciones, el OSD y las
demás superficies del escritorio.

El compositor es una elección de backend, no la identidad del producto. Los
backends disponibles tienen distintos límites de madurez y capacidades:

- **Hyprland — Soportado.** Compositor por defecto para HorneroOS Desktop.
- **Niri — Soportado.** Opción de compositor Wayland de columnas desplazables
  con backend real en Hornero Shell; sus límites específicos de capacidades se
  detallan abajo.
- **Labwc — Planificado.** No es una opción de instalación; no hay un backend
  de Hornero implementado.

HorneroOS Desktop es una edición **Soportada** de uso diario. Las diferencias
entre backends se documentan con claridad en lugar de simular funciones
exclusivas de Hyprland donde no aplican.

## Hyprland

Hyprland es el compositor por defecto y la sesión más validada de HorneroOS
Desktop. Su semántica de gestor de ventanas, el comportamiento de espacios de
trabajo, los layouts multibarra, el foco de teclado y los controles específicos
de Hyprland son parte del camino soportado del escritorio. El producto sigue
siendo Wayland-first; Hyprland es su backend actual, no la definición de
HorneroOS.

Mirá [atajos del escritorio](shortcuts.md) y [layouts](layouts.md) para los
flujos compartidos de la Shell.

### Módulos de fábrica y overrides de usuario

La entrada de Hyprland de Hornero (`~/.config/hypr/hyprland.lua`) separa los
módulos inmutables empaquetados de las personalizaciones del usuario:

- **Módulos de fábrica (`load_factory`):** módulos como `monitors.lua`,
  `autostart.lua`, `environment.lua`, `input.lua`, `gestures.lua`,
  `layout.lua`, `keybindings-overlay.lua`, `helpers.lua`, `keybindings.lua`,
  `window-rules.lua`, `animations.lua`, `smart-colors.lua`, `plugins.lua` y
  `static.lua` se cargan desde `/etc/xdg/hypr/hyprland.lua.d/` cuando están
  empaquetados ahí (se puede pisar con `HORNERO_HYPR_FACTORY_DIR`), con
  respaldo por archivo a `~/.config/hypr/hyprland.lua.d/` para instalaciones
  sin paquete. Como `/etc/xdg/hypr/hyprland.lua.d/` tiene prioridad, las
  actualizaciones de `pacman` llegan a cuentas existentes aunque queden copias
  viejas de `/etc/skel` en `~/.config/hypr/`.
- **Hooks de override (`load_user`):** `monitors-user.lua`,
  `keybindings-user.lua` y `window-rules-user.lua` cargan primero desde tu
  `~/.config/hypr/hyprland.lua.d/` local, y recurren a `factory_dir` si faltan.
- **Fijar un módulo de fábrica:** para usar una copia local modificada de un
  módulo de fábrica, reemplazá su llamada `load_factory("...")` por
  `load_user("...")` en `~/.config/hypr/hyprland.lua`.
- **Refrescar una entrada anterior:** `horneroctl config refresh-hypr --dry-run`
  previsualiza de forma aditiva las líneas de módulos de fábrica faltantes
  (soporta tanto `load_factory`/`load_user` como entradas `dofile` legadas)
  conservando tus líneas existentes y archivos `*-user.lua`; `--yes` escribe
  con respaldo `.pre-refresh`.

## Niri

Niri es una opción soportada de compositor Wayland de desplazamiento
horizontal en HorneroOS. HorneroOS provee una configuración de Niri y un
backend de Shell que consume el flujo de eventos de Niri para espacios de
trabajo, ventanas, foco y distribuciones de teclado. El backend usa las
acciones de ventana y el selector de capturas propios de Niri donde difieren
de Hyprland.

La configuración actual de Niri parte de los valores por defecto de Niri 26.04
upstream y rutea los atajos de Hornero hacia la Shell y `horneroctl`:

| Atajo | Acción |
| --- | --- |
| `Super+D` | Abrir el Lanzador de Hornero |
| `Super+Shift+D` | Abrir el Dashboard |
| `Super+Shift+B` | Abrir el Selector de layouts |
| `Super+X` | Abrir el menú de sesión |
| `Super+,` | Abrir Apariencia en el Centro de control |
| `Super+E` | Abrir Yazi en la terminal configurada |
| `Super+V` | Abrir el historial del portapapeles |
| `Super+L` | Bloquear la sesión |
| `Print` | Abrir la UI de selección de captura de Niri |
| `Ctrl+Print` | Capturar la pantalla con Niri |
| `Alt+Print` | Capturar la ventana con foco con Niri |

El Selector de layouts cambia las superficies y barras de Hornero Shell. No
cambia el layout nativo de columnas deslizantes de Niri. Niri no expone los
espacios de trabajo especiales propios de Hyprland, los metadatos de salida,
las miniaturas nativas de ventanas, la creación o renombrado de espacios de
trabajo ni los atajos globales a través del protocolo exclusivo de Hyprland.
Hornero oculta o desactiva controles que dependen de esas capacidades en vez de
simular paridad.

### Portales y captura de pantalla

Con `hornero-config` 0.3.1 o posterior, la preferencia empaquetada de portales
de Niri elige GTK como portal de respaldo y selector de archivos, y GNOME para
screencast. El screencast en Niri usa el soporte nativo del compositor mediante
PipeWire. La sesión de Niri también usa `xwayland-satellite` para aplicaciones
X11. Son dependencias de la sesión de Niri; el conjunto de paquetes de Hyprland
no arrastra los backends GTK ni GNOME de portales de Niri.

OBS y la grabación de pantalla de punta a punta todavía no pasaron aceptación
gráfica bajo Niri. Un archivo de configuración de portales y paquetes
instalados por sí solos no prueban un flujo de captura funcionando.

### Comportamiento verificado y límites de capacidades

Se probó un invitado QEMU corriendo Niri 26.04 en 1280×800 con entrada real de
teclado y puntero. El recorrido verificado cubre el arranque de la Shell, el
Lanzador, el Dashboard, el Centro de control, Apariencia, cambio de tema,
Selector de layouts/Hornero Left, cambio de espacios de trabajo y la selección
de capturas de Niri. Es un chequeo de sesión gráfica real, no solo un test del
parser de configuración.

Algunos flujos siguen difiriendo respecto de Hyprland o están sin certificar
bajo Niri: foco y escalado multimonitor, OBS/screencast a través de los
portales elegidos, consistencia de temas entre apps GTK y Qt y controles
exclusivos de Hyprland (espacios especiales, detección de pantalla completa en
Gaming). Hyprland sigue siendo el valor por defecto cuando dependés de esas
funciones.

La configuración de Niri se instala como respaldo en `/etc/niri/config.kdl` y
se materializa bajo el directorio de configuración XDG del usuario. El paquete
no sobrescribe una configuración de usuario existente durante una sesión
activa. Revisá el
[estado actual de releases e instalación](https://horneroos.com/install) antes
de seguir pasos específicos de paquetes. La ISO firmada `v0.2.0-preview42`
instala mediante el instalador gráfico Calamares (`3.4.3`).

Para diagnósticos, `horneroctl doctor` identifica una sesión Niri reconocida.
Usá la [guía de configuración de Niri](https://niri-wm.github.io/niri/Configuration%3A-Introduction.html),
los [atajos de teclado](https://niri-wm.github.io/niri/Configuration%3A-Key-Bindings.html)
y la [referencia IPC](https://niri-wm.github.io/niri/IPC.html) para ajustes del
compositor más allá de los valores por defecto de Hornero.

## Otros compositores

Labwc está planificado. Hoy Hornero no empaqueta ni valida un backend de Labwc.
El límite del compositor se basa en capacidades: cualquier soporte futuro debe
usar las APIs reales del compositor y exponer sus límites con honestidad en vez
de copiar supuestos de Hyprland a otra sesión.
