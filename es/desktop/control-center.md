# Mapa del Centro de control

El Centro de control (también llamado Ajustes) reúne todos los ajustes
persistentes del escritorio. Esta página lista dónde vive cada cosa. Las
páginas están agrupadas en siete categorías en el riel izquierdo; el id de
página de la última columna es lo que abre
`horneroctl config gui --pane <id>`.

> **Development.** La lista de categorías y páginas de abajo se lee del
> registro de paneles de la rama `main` de Shell (noviembre de 2026).
> Varias páginas se recompusieron para Hornero Signal y otras se siguen
> rehaciendo, así que los nombres y la ubicación todavía pueden cambiar. El
> registro y la búsqueda están cubiertos por las pruebas offscreen
> automáticas de Shell; las páginas todavía no se validaron visualmente en
> una máquina virtual ni en un escritorio físico.

## Abrirlo y encontrar cosas

- Abrí el Centro de control desde el lanzador o desde la acción de ajustes
  de una barra. Desde una terminal, usá `horneroctl config gui` y sumá
  `--pane <id>` para saltar a una página.
- **Ctrl + ,** abre *Find a setting*. Busca en nombres de página,
  descripciones y controles comunes como wallpaper, VPN, reduce motion,
  fonts o transparency; Enter abre el resultado. Mirá
  [Popups, foco y movimiento](popups-and-motion.md#buscar-un-ajuste).

Los nombres de las páginas se muestran en inglés, tal como aparecen en
pantalla.

![El Centro de control abierto en la página Appearance. La columna
izquierda lista las páginas de Conexiones, Aspecto y Escritorio; el
panel de vista previa muestra el tema Hornero Signal Night con sus
proporciones de contraste.](https://www.horneroos.com/captures/cap-cc-01.png)

*El Centro de control con Appearance abierto: categorías en la columna
izquierda, página actual en el medio, vista previa en vivo a la
derecha. Captura real del escritorio en el equipo del maintainer,
19 de noviembre de 2026.*

## Conexiones

| Página | Qué cubre | Id |
| --- | --- | --- |
| Network | Wi-Fi, redes cableadas, conexiones | `network` |
| Bluetooth | Emparejar y administrar dispositivos cercanos | `bluetooth` |
| VPN | Conexiones de red privada | `vpn` |

## Aspecto (Look & feel)

| Página | Qué cubre | Id |
| --- | --- | --- |
| Appearance | Temas, fondo, fuentes, íconos, transparencia | `appearance` |
| Night Light | Entibiar la pantalla para la noche | `nightlight` |
| Accessibility | Tamaño de texto, reduce motion, velocidad | `accessibility` |
| Experience | Modos, deck, cambio automático, reset | `experience` |

Appearance está explicada en [Temas y apariencia](appearance.md) y
[Fondos](wallpapers.md). Experience está explicada en
[Modos de experiencia](experience-modes.md).

## Escritorio (Desktop)

| Página | Qué cubre | Id |
| --- | --- | --- |
| Bars | Qué entradas muestra cada barra y su orden | `taskbar` |
| Layout | Presets de layout y estilos de Cockpit Clear | `layout` |
| Dashboard | Contenido y comportamiento del dashboard | `dashboard` |
| Launcher | Cómo funcionan la búsqueda y el lanzamiento | `launcher` |
| Windows | Espacios, bordes, foco y reglas | `windows` |
| Lock screen | Privacidad, huella, bloqueo por inactividad | `lockscreen` |

Los presets de layout están descritos en [Layouts](layouts.md). Reordenar
las secciones del layout activo está en Bars.

![Ajustes, página Bars para el layout Cockpit. Las secciones de la barra
superior están agrupadas en Left, Center y Right, cada entrada con
flechas para reordenar y un interruptor para activarla o
desactivarla.](https://www.horneroos.com/captures/cap-cc-03.png)

*Ajustes → Bars: reordená u ocultá lo que muestra cada barra del layout
activo. Captura real del escritorio en el equipo del maintainer,
19 de noviembre de 2026.*

## Sonido y alertas

| Página | Qué cubre | Id |
| --- | --- | --- |
| Audio | Elegir dispositivos y ajustar el sonido | `audio` |
| Notifications | Cuándo y cómo aparecen los avisos | `notifications` |
| On-screen display | Aviso de volumen y brillo | `osd` |

## Dispositivos

| Página | Qué cubre | Id |
| --- | --- | --- |
| Displays | Pantallas, disposición, brillo, layout de ventanas | `displays` |
| Input | Distribución de teclado y entrada | `input` |
| Keybinds | Ver, buscar y reasignar atajos de sesión | `keybinds` |
| Power | Batería y comportamiento de energía | `power` |
| Capture | Capturas, grabación y backends de captura | `capture` |

## Apps y asistentes

| Página | Qué cubre | Id |
| --- | --- | --- |
| Javi | El companion del escritorio | `companion` |
| Agent Center | Agentes de código en esta máquina y estado de Javi | `agents` |
| Studio | Cargas de trabajo y aplicaciones creativas | `studio` |
| Gaming | Preparación para juegos, perfiles y modo gaming | `gaming` |
| Terminal | La terminal que usan las acciones de Hornero | `terminal` |
| Extensions | Extensiones, su confianza y estado de carga | `extensions` |

![El panel de Javi abierto en el escritorio, con las pestañas Ask,
Agent y Chat, una pregunta enviada y el área de actividad vacía con el
texto "No activity yet".](https://www.horneroos.com/captures/cap-javi-08.png)

*Javi, el companion del escritorio, sin actividad todavía: preguntas,
aprobaciones y artefactos aparecen en este panel. Captura real del
escritorio en el equipo del maintainer, 19 de noviembre de 2026.*

## Sistema

| Página | Qué cubre | Id |
| --- | --- | --- |
| System | Información del sistema y diagnóstico | `system` |
| Updates | Actualizaciones, copias y recuperación | `updates` |
| Session | Comportamiento y atajos del menú de sesión | `session` |

## Dónde encontrar tareas comunes

- Cambiar el tema o el fondo: Appearance. Los colores siempre salen del
  tema; mirá [Hornero Signal](hornero-signal.md).
- Bajar el movimiento: Accessibility, o Appearance → Animations.
- Pasar a Focus, Signal o Gaming: Experience.
- Cambiar a otro layout de barra: Layout, o el selector de layouts con
  **Super + Shift + B**.
- Instalar, actualizar, quitar, habilitar o inspeccionar una extensión, o
  recuperarte de una rota con el modo seguro: Extensions. Mirá
  [Extensiones](extensions.md) y la
  [guía de autoría de extensiones](../../development/extensions.md) (en
  inglés).
- Actualizar el sistema, restaurar ajustes de Hornero desde una
  instantánea de configuración o una copia, o chequear la preparación
  para recuperación: Updates. HorneroOS hoy no tiene vuelta atrás del
  sistema; mirá [Actualizaciones y recuperación](updates-and-rollback.md).
- Revisar problemas de configuración: System → Diagnostics, o
  `horneroctl doctor`.
