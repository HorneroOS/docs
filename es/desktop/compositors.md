# Compositores Wayland

HorneroOS Desktop es un escritorio Wayland-first impulsado por Hornero Shell.
Un compositor gestiona las ventanas, los espacios de trabajo, las salidas, la
entrada y la sesión Wayland. Hornero Shell provee las barras compartidas, el
lanzador, el Dashboard, el Centro de control, las notificaciones, el OSD y las
demás superficies del escritorio.

El compositor es una elección de backend, no la identidad del producto. Los
backends disponibles tienen distintos límites de madurez y capacidades:

- **Hyprland — Soportado.** Valor por defecto validado para HorneroOS Desktop.
- **Niri — Experimental.** Una sesión real de la Shell funciona en una VM de
  una sola salida; quedan brechas específicas del compositor y flujos sin
  verificar.
- **Labwc — Planificado.** No es una opción de instalación; no hay un backend
  de Hornero implementado.

Desktop en su conjunto sigue en Preview. Un compositor experimental no es una
promesa de paridad de funciones con Hyprland.

## Hyprland

Hyprland es el compositor por defecto y la sesión más validada de HorneroOS
Desktop. Su semántica de gestor de ventanas, el comportamiento de espacios de
trabajo, los layouts multibarra, el foco de teclado y los controles específicos
de Hyprland son parte del camino soportado del escritorio. El producto sigue
siendo Wayland-first; Hyprland es su backend actual, no la definición de
HorneroOS.

Mirá [atajos del escritorio](shortcuts.md) y [layouts](layouts.md) para los
flujos compartidos de la Shell.

## Niri

Niri es un compositor Wayland experimental de desplazamiento horizontal.
HorneroOS provee una configuración de Niri y un backend de Shell que consume el
flujo de eventos de Niri para espacios de trabajo, ventanas, foco y
distribuciones de teclado. El backend usa las acciones de ventana y el selector
de capturas propios de Niri donde difieren de Hyprland.

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

### Comportamiento verificado y límites

Se probó un invitado QEMU corriendo Niri 26.04 en 1280×800 con entrada real de
teclado y puntero. El recorrido verificado cubre el arranque de la Shell, el
Lanzador, el Dashboard, el Centro de control, Apariencia, un cambio de tema
(Hornero Light, antes de que Hornero Signal lo reemplazara), Selector de
layouts/Hornero Left, cambio de espacios de trabajo y la selección de capturas
de Niri. Es un chequeo de sesión gráfica real, no solo un test del parser de
configuración.

Todavía falta aceptación gráfica en lo siguiente antes de que Niri deje de ser
experimental: foco y escalado multimonitor, bloqueo y recuperación de sesión,
OBS/screencast a través de los portales elegidos, consistencia de temas entre
apps GTK y Qt, y el resto de las superficies y flujos de la Shell. Hyprland
sigue siendo la opción más segura cuando esas brechas importan.

La configuración de Niri se instala como respaldo en `/etc/niri/config.kdl` y
se materializa bajo el directorio de configuración XDG del usuario. El paquete
no sobrescribe una configuración de usuario existente durante una sesión
activa. Revisá el
[estado actual de releases e instalación](https://horneroos.com/install) antes
de seguir pasos específicos de paquetes. La ISO firmada actual instala mediante
el camino provisional Calamares; todavía no hay un instalador soportado.

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
