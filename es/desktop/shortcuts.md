# Atajos de teclado

`Super` es la tecla Windows/Meta. Los atajos pueden cambiar según la versión y
tu configuración; esta referencia sigue los valores de fábrica actuales de
Hornero en Hyprland. Apretá **Super + /** para abrir el panel de atajos, que
lista todos los atajos que tu sesión está usando ahora mismo (mirá
[Panel de atajos](#panel-de-atajos)). Desde una terminal, usá
`horneroctl hardware keyboard rebind list`.

Los nombres de grupos y botones se muestran en inglés, tal como aparecen en
pantalla.

## Shell y aplicaciones

| Atajo | Acción |
| --- | --- |
| `Ctrl + Space` | Abrir el lanzador de aplicaciones |
| `Super + D` | Abrir el Dashboard |
| `Super + Shift + B` | Abrir el selector de diseños (Layout Picker) |
| `Super + X` | Abrir el menú de sesión y energía |
| `Super + V` | Abrir el historial del portapapeles |
| `Super + E` | Abrir el gestor de archivos en la terminal |
| `Super + F` | Abrir el gestor de archivos gráfico |
| `Super + T` o `Super + Enter` | Abrir una terminal |
| `Super + W` | Abrir el navegador |
| `Super + L` | Bloquear la sesión |
| `Print` / `Shift + Print` | Capturar la pantalla / elegir un área |

## Ventanas y espacios de trabajo

| Atajo | Acción |
| --- | --- |
| `Super + H/J/K` o flechas | Pasar el foco a una ventana vecina |
| `Super + Shift + H/J/K/L` o flechas | Mover la ventana con foco |
| `Super + Space` | Alternar flotante en la ventana con foco |
| `Super + M` | Alternar pantalla completa |
| `Super + Shift + M` | Alternar maximizado |
| `Super + Shift + Q` | Cerrar la ventana con foco |
| `Super + R` | Modo de redimensionado: H/J/K/L o flechas, después Escape |
| `Super + 1…9, 0` | Ir al espacio de trabajo 1…10 |
| `Super + Shift + 1…9, 0` | Mover la ventana con foco al espacio 1…10 |
| `Super + Tab` / `Super + Shift + Tab` | Espacio siguiente / anterior |
| `Super + S` | Alternar el espacio auxiliar (scratch) |
| `Super + O` | Vista general de espacios (plugin opcional) |

`Super + L` bloquea la sesión, así que el foco va a la derecha con
`Super + →` (igual que en Niri).

En el diseño con desplazamiento, `Super + Alt + H/L` se mueve entre columnas y
`Super + Alt + -/=` cambia el ancho de la columna activa. La
[guía de interacción de Shell](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md)
tiene el detalle del movimiento.

## Teclas de hardware

Las teclas multimedia controlan la reproducción, las de volumen cambian el
volumen de salida y la de silenciar micrófono alterna la entrada por defecto.
Las teclas de brillo cambian la pantalla de a 10 %; con Shift, de a 1 %.
Dependen del hardware y del backend activo.

## Recuperación y cuidado

Apretá Escape para salir del modo de redimensionado o de un panel del shell.
`Super + Shift + R` recarga la configuración del compositor.
**`Super + Shift + E` cierra Hyprland**: no lo uses para cerrar ventanas.

Para ver la distribución de teclado activa:

```sh
horneroctl hardware keyboard layout --current
```

Para cambiar qué distribuciones ofrece la sesión, usá **Control Center ›
Input** o la terminal (se aplica al instante, se guarda y se restaura al
iniciar sesión):

```sh
horneroctl hardware keyboard layout --list
horneroctl hardware keyboard layout --set us,latam \
  --variant intl, --yes
```

## Panel de atajos

**Super + /** abre un panel con todos los atajos activos, leídos en vivo de
Hyprland y agrupados por propósito: aplicaciones, ventanas, foco, espacios de
trabajo, multimedia, capturas, sistema, mouse, tus atajos personales y
plugins. Escribí para filtrar. La búsqueda encuentra teclas, acciones y
nombres de grupo en inglés o en castellano ("foco", "ventanas", "capturas").

![El panel de atajos con el grupo Essential Applications: las
combinaciones de teclas a la izquierda, el comando que ejecuta cada
una a la derecha y un buscador arriba.](https://www.horneroos.com/captures/cap-shell-08.png)

*El panel de atajos, convocado con Super + / y leído en vivo de
Hyprland. Captura real del escritorio en el equipo del maintainer,
19 de noviembre de 2026.*

| Tecla | Acción |
| --- | --- |
| Arriba / Abajo | Mover la selección |
| Enter | Ejecutar el atajo seleccionado |
| Ctrl+E | Reasignarlo ahí mismo: apretá la combinación nueva |
| Ctrl+D | Desactivarlo |
| Ctrl+Z | Deshacer el último cambio |
| Escape | Borrar la búsqueda y, si ya está vacía, cerrar |

Al reasignar, el panel graba la próxima combinación que aprietes, aunque ya
esté ocupada. Si está ocupada, antes de guardar te dice qué atajo la usa y de
qué grupo es. Apretá **S** para intercambiar los dos atajos, **R** para
probar otra combinación o **Enter** para guardar una combinación libre. Los
cambios se aplican al instante y **Undo** deja todo exactamente como estaba.

La tecla que abre el panel es un atajo más. Si querés usar **Super + K** como
en Omarchy, reasigná la entrada "keyboard keys" a Super + K e intercambiala
con mover el foco hacia arriba. En **Control Center › Keybinds** están los
ajustes del panel (Enter ejecuta, cerrar después de ejecutar, mostrar atajos
de submapas y de mouse, filas compactas) y el mismo editor.

## Reasignar atajos

Usá el panel de atajos, **Control Center › Keybinds** o la terminal:

```sh
horneroctl hardware keyboard rebind list --json
horneroctl hardware keyboard rebind set \
  --old "SUPER + Return" --new "SUPER + F13" --yes
horneroctl hardware keyboard rebind set \
  --old "SUPER + K" --new "SUPER + J" --swap --yes
horneroctl hardware keyboard rebind set --old "SUPER + K" --new none --yes
horneroctl hardware keyboard rebind undo --yes
horneroctl hardware keyboard rebind reset --yes
```

En la configuración Lua de fábrica, `keybindings.lua` y
`keybindings-overlay.lua` cargan mediante `load_factory` desde
`/etc/xdg/hypr/hyprland.lua.d/`, mientras que `keybindings-user.lua` carga
mediante `load_user` desde `~/.config/hypr/hyprland.lua.d/`. Las
reasignaciones se guardan en el archivo generado
`~/.config/hypr/hornero-keybinds.lua`. Ese archivo solo contiene datos, y
`keybindings-overlay.lua` lo aplica antes de cargar cualquier atajo. No se
edita ni el `keybindings.lua` de fábrica ni tu `keybindings-user.lua`, y los
pares unbind/bind de tu archivo personal siguen a la reasignación. Las
instantáneas para deshacer quedan en `~/.local/state/hornero/keybinds/undo`
(las últimas 20). Las configuraciones hyprlang anteriores guardan pares
`unbind`/`bind` en `keybindings-user.conf`.

## Comportamiento de ventanas

**Control Center › Windows** reúne márgenes, borde, redondeo de esquinas y
foco que sigue al mouse, además de las reglas de ventana del usuario:

```sh
horneroctl hypr windows status
horneroctl hypr windows set --gaps-in 8 --follow-mouse 2 --yes
horneroctl hypr windows rules add --match class \
  --pattern kitty --effect float --yes
horneroctl hypr windows rules list
```

La geometría y el foco se aplican al instante y se restauran al iniciar
sesión. Las reglas se guardan en tu `window-rules-user.conf`, nunca en las de
fábrica, y se aplican al recargar Hyprland (**Super + Shift + R**) o al
reiniciarlo. Las ventanas que ya están abiertas no cambian.

## Accesibilidad

**Control Center › Accessibility** reúne tamaño de texto, transparencia,
movimiento y tamaño del cursor:

```sh
horneroctl hypr cursor status
horneroctl hypr cursor set --size 32 --yes
```

El tamaño del cursor se aplica al instante en Hyprland, se restaura al
iniciar sesión y las demás aplicaciones lo toman cuando arrancan. El comando
de estado dice de dónde sale el tamaño efectivo (ajuste guardado,
`XCURSOR_SIZE` o el valor por defecto), porque Hyprland no informa el tamaño
en uso.

Los atajos de fábrica están definidos en el
[archivo de atajos de HorneroOS/config](https://github.com/HorneroOS/config/blob/main/desktop/hypr/hyprland.lua.d/keybindings.lua).
Para ver cómo estos atajos abren los programas configurados, mirá
[Aplicaciones y flujos](../applications/README.md).
