# Arquitectura de los modos de experiencia

Esta página explica cómo se construyen los modos de experiencia y quién es
dueño de cada pieza. Para saber qué hacen por una persona, leé
[Modos de experiencia](../desktop/experience-modes.md). La autoridad de
diseño es la
[RFC 0001](../../development/rfc-0001-hornero-signal.md) sección 5a y el
[Signal Visual Language](../../development/signal-visual-language.md)
sección 13 (ambos en inglés). El contrato a nivel código vive en el
repositorio Shell
([`docs/EXPERIENCE.md`](https://github.com/HorneroOS/shell/blob/main/docs/EXPERIENCE.md)
y [`docs/IPC.md`](https://github.com/HorneroOS/shell/blob/main/docs/IPC.md));
esta página no lo repite.

> **Development.** Esto describe la rama `main` de Shell (noviembre de
> 2026). El modelo, el solver del deck y la página Experience están
> cubiertos por pruebas sin pantalla que corren en CI. Nada de esto se
> validó todavía en una imagen de máquina virtual ni en un escritorio
> físico. `horneroctl` todavía no tiene un grupo de comandos para modos; la RFC
> prevé uno, y hasta que exista la interfaz propia de la shell es la forma
> soportada de cambiar de modo.

## Cuatro ejes, cuatro dueños

Un modo es uno de cuatro ejes independientes. Ningún eje es una shell aparte.

| Eje | Dueño | Notas |
| --- | --- | --- |
| Edición | [hornero](https://github.com/HorneroOS/hornero) | Capacidades y paquetes instalados |
| Modo de experiencia | [shell](https://github.com/HorneroOS/shell) | `services/Experience.qml` y `services/experience.js` |
| Preset de layout | [shell](https://github.com/HorneroOS/shell) (catálogo), [config](https://github.com/HorneroOS/config) (valor de fábrica) | Composición de barras |
| Tema | [config](https://github.com/HorneroOS/config) (temas), [hornero](https://github.com/HorneroOS/hornero) (aplicación) | Roles Signal |

La shell mantiene la regla de composición: un modo solo puede activar una
capacidad si la edición la provee, y una capacidad ausente se informa como
no disponible en vez de simularse.

## Capas dentro de la shell

- **Modelo puro**, `services/experience.js`: perfiles, validación de campos,
  salvaguardas, lectura de estado, migración de presets y la decisión de
  cambio automático. Corre bajo Node en las pruebas y no toca nada.
- **Servicio**, `services/Experience.qml`: el único consumidor QML. Persiste
  el estado, expone los campos efectivos al resto de la shell y publica el
  target IPC `experience`.
- **Modelo del deck**, `services/deck.js`: el solver de layout puro del deck
  de instrumentos Signal.
- **Página**, `modules/controlcenter/experience/ExperiencePane.qml`: Ajustes
  → Experience.
- **Consumidores**: la barra, el movimiento, las notificaciones, la capa de
  escritorio y PluginKit leen campos efectivos y nunca perfiles crudos.

### Perfiles y campos efectivos

Un perfil es dato declarativo: un mapa plano de campos con puntos como
`motion`, `density`, `glow`, `scanlines`, `telemetry.rateHz`,
`desktopWidgets`, `notifications.hold`, `layout.preset`, `layout.apply`,
`power.suggest` y `hooks.*`. Cada campo tiene un validador. El perfil
efectivo se calcula en un orden fijo:

1. el perfil de fábrica del modo;
2. los overrides válidos del usuario en `shell.json`, clave
   `experience.modes.<modo>`;
3. las salvaguardas bloqueadas (brillo y scanlines apagados en Focus y
   Gaming, movimiento apagado en Gaming), que ignoran los overrides.

Los overrides iguales al valor de fábrica, las claves desconocidas y los
valores inválidos se descartan al leer el archivo. Un id de preset que la
auditoría de layouts eliminó se migra una vez al leer, así que un
`layout.preset` viejo nunca apunta a la nada. Los consumidores ven el
movimiento forzado a `off` por los ajustes de movimiento reducido y el
brillo condicionado por la polaridad del tema, el alto contraste y el nivel
de movimiento; un modo no puede pisar esas reglas de accesibilidad.

### Estado y persistencia

- Modo activo, modo anterior, origen (user, auto, cli, reset, migration) y
  la marca de automático: `$XDG_STATE_HOME/hornero/experience.json`.
- Overrides por modo: `shell.json`, `experience.modes`.
- Overrides del deck Signal (instrumentos ocultos, geometría por modo y por
  pantalla): `shell.json`, `experience.deck`.
- Cambio automático y avisos: `shell.json`, `experience.auto` y
  `experience.toasts`.

El archivo de estado de sesión está separado de `shell.json` a propósito:
cambiar de modo es un acto de tiempo de ejecución, no una edición de
configuración, y no debe reescribir tus barras.

### Cambiar, revertir y resetear

- `set`, `toggle` y `revert` pasan por una única función de transición del
  modelo. Cada transición registra su origen, así la shell distingue una
  elección explícita de una automática.
- **Revert** vuelve al modo anterior. **Reset** elige Everyday y le pide a
  `horneroctl shell preset apply cockpit --yes` y al pipeline de temas el
  tema Signal Night. Reset conserva las personalizaciones por modo; borrarlas
  es una acción aparte por modo que además limpia el deck de ese modo.
- Aplicar el layout preferido de un modo es un acto explícito o una opción
  por modo, porque un preset reescribe la configuración de las barras.
- Los ganchos de edición son de mejor esfuerzo y reversibles. El pedido de
  audio de Studio registra el perfil anterior y lo restaura al salir del
  modo; el ajuste del compositor de Gaming depende de la tabla de
  capacidades del compositor.

### Cambio automático

La función de decisión recibe el estado, el id de aplicación de la ventana
con foco, su marca de pantalla completa y una lista de patrones (por
defecto cubren Steam, Gamescope y ejecutables de Windows). Devuelve `enter`,
`leave` o nada. Nunca pisa una elección explícita: solo sale de un modo al
que entró ella misma. Viene apagada por defecto y no lee nada más de la
sesión.

## El deck de instrumentos Signal

La capa de escritorio de Signal usa `desktopWidgets: instruments`. El deck
son widgets de escritorio de PluginKit, no un segundo motor de widgets:

- `services/deck.js` resuelve la ubicación por pantalla en píxeles lógicos
  dentro del área que la capa de escritorio ya reserva para las barras,
  manteniendo reservada la caja del reloj de escritorio. Dos rieles
  laterales, un centro libre y descarte por prioridad en lugar de
  superposición.
- Los seis instrumentos (System Insight, Network Scope, Audio Deck,
  Calendar, Agenda, Moon Phase) salen del catálogo propio de
  [plugins](https://github.com/HorneroOS/plugins) y se cargan solo cuando el
  payload instalado es de confianza. El deck nunca escribe estado del ciclo
  de vida de las extensiones.
- El brillo sale de un presupuesto único de toda la shell (`acquireGlow`):
  tres elementos en total, compartidos entre los instrumentos nativos y las
  trazas de extensiones, sin que las extensiones tomen nunca el último lugar.
- Al salir del modo el deck se desvanece antes de descargar los widgets. En
  Focus y Gaming no se instancia ningún widget, así que se liberan todos los
  leases de proveedores y nada hace polling para el escritorio.

Los proveedores de telemetría compartidos siguen el `telemetry.rateHz` del
modo (`Theme.telemetryIntervalMs` para las extensiones); mirá los
[proveedores de datos](../../development/extensions.md#shared-data-providers).

## Qué está validado, y dónde

| Pieza | Evidencia | Dónde corrió |
| --- | --- | --- |
| Perfiles, salvaguardas, estado | Pruebas en Node | CI, sin pantalla |
| Layout del deck | Pruebas del solver, un diagrama | CI, sin pantalla |
| Página Experience y búsqueda | Pruebas QML offscreen | CI, offscreen |
| Costo en reposo por modo | `scripts/perf-signal-deck.sh` | Todavía no corrió |
| Resultado visual de cada modo | Captura en VM de QA | Todavía no corrió |
| Comportamiento en el host | Validación con una persona | Todavía no corrió |

Las cifras del layout del deck (1366×768 muestra cuatro instrumentos, un
ultrawide de 3440 píxeles muestra seis) salen de las pruebas del solver y de
un diagrama de layout, no de un render.

La evidencia solo se registra como validada para el lugar donde se produjo.
La tabla de [estado de implementación de la RFC 0001](../../development/rfc-0001-hornero-signal.md#implementation-status)
lleva el panorama general.
