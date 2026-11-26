# Popups, foco y movimiento

Cómo se abren los menús, paneles y tooltips, dónde aparecen, cómo se cierran
y cómo se mueve el escritorio, o deja de moverse, cuando lo pedís.

> **Development.** El contrato de interacción de abajo está en la rama
> `main` de Shell desde noviembre de 2026. Las ISO preview hasta la
> v0.2.0-preview32 inclusive se comportan distinto. El solver de ubicación,
> los niveles de movimiento y la cascada de Escape están cubiertos por las
> pruebas automáticas de Shell (sin pantalla y en modo offscreen). La
> geometría de los popups, los tiempos de movimiento y el comportamiento de
> teclado en Niri todavía no se validaron en una máquina virtual ni en un
> escritorio físico.

## Dónde aparecen los popups

Todo popout, menú de la bandeja, tooltip y popover de extensión lo ubica una
sola regla compartida, así que ningún layout, estilo de barra ni extensión
inventa la suya:

- **Alejándose de la barra dueña.** Una barra superior abre hacia abajo, una
  inferior hacia arriba, un riel izquierdo hacia la derecha y un riel
  derecho hacia la izquierda.
- **Pegado a su disparador.** Un popout de una barra attached queda a ras del
  borde interior de la barra. Las barras flotantes, island, inset, dock y
  Cockpit Clear dejan un espacio chico. Una línea ámbar fina, tan ancha como
  el disparador, recorre el borde que lo mira, así ves de dónde salió el
  popup incluso con el movimiento apagado.
- **Siempre en pantalla.** Se centra en su disparador y después se mantiene
  dentro del área útil de la pantalla, lejos de cada barra y con un margen de
  8 px. Si no entra, pasa al otro lado una sola vez; si no entra en ninguno,
  toma el tamaño más grande que entre y se desplaza con scroll.
- **Siguiendo a su disparador.** Si la barra se reordena o cambia un
  monitor, un popup abierto lo sigue. Cada pantalla de una configuración con
  escalas mixtas se resuelve de la misma forma.

Con las dos barras de Cockpit, los popups del riel superior abren hacia
abajo y nunca llegan a la tira inferior; los de la tira abren hacia arriba
y se detienen debajo del riel superior. Los popups de Cockpit Clear son
tarjetas opacas, porque no hay placa de barra a la que pegarse.

![Ajustes, página Notifications: el interruptor de no molestar, el
tiempo de expiración automática, la opción de línea de tiempo y la
posición del popup en el borde superior, a la izquierda, al centro o a
la derecha.](https://www.horneroos.com/captures/cap-cc-11.png)

*Los popups de notificaciones tienen página propia: Ajustes →
Notifications define cuánto tiempo permanecen y en qué parte del borde
superior aparecen. Captura real del escritorio en el equipo del
maintainer, 19 de noviembre de 2026.*

## Abrir y cerrar

- **Hover.** Apoyarte sobre un ítem de la barra alrededor de una décima de
  segundo abre su popup; pasar al ítem siguiente transforma el popup hacia
  ahí en vez de cerrarlo y reabrirlo. Los popups por hover nunca toman el
  foco del teclado.
- **Clic o teclado.** Hacer clic en un ítem, o apretar Enter o Espacio sobre
  él, abre el popup con el foco adentro. Se queda abierto aunque el puntero
  se vaya.
- **Salir.** Si te movés fuera del ítem y del popup empieza un breve período
  de gracia (alrededor de un cuarto de segundo) antes de cerrarse; si
  volvés, se cancela. El espacio entre una barra flotante y su tarjeta no
  cuenta como salir.
- **Tooltips.** Las pistas cortas aparecen con hover **y** con foco de
  teclado después de la misma demora, y nunca contienen algo que necesites
  leer o apretar.
- **Dashboard y utilities** se abren cuando el puntero toca el borde de la
  pantalla y se cierran cuando se va. No le sacan el foco del teclado a
  otras apps con hover. Abrirlos con un atajo sí toma el foco.

### Escape

Toda superficie transitoria se cierra desde el teclado, y **un Escape cierra
exactamente una superficie**, de adentro hacia afuera:

1. El estado interno sin terminar: se cancela el renombrado de un espacio de
   trabajo, se desarma una acción de energía, la página de contraseña de
   Wi-Fi vuelve a la lista de redes.
2. Se cierra el popup que tiene el teclado y el foco vuelve al ítem que lo
   abrió.
3. Después, el cajón abierto de más arriba: selector de layouts, menú de
   sesión, lanzador, dashboard, barra lateral o utilities.

El indicador en pantalla (OSD) y los avisos se vencen por su propio
temporizador; nunca toman foco. La pantalla de bloqueo ignora Escape,
porque tiene que autenticar.

En Niri, un clic fuera de un cajón abierto lo cierra y ese clic lo consume
el cierre: volvé a hacer clic en la ventana de abajo para usarla.

### Buscar un ajuste

**Ctrl + ,** abre una búsqueda sobre todas las páginas de Ajustes y los
controles comunes (probá *reduce motion*, *wallpaper* o *fonts*). Escape
borra la consulta, después cierra la búsqueda y después cierra Ajustes.
El [mapa del Centro de control](control-center.md) lista las páginas.

## Niveles de movimiento

La shell anima popups, paneles y algunos indicadores con un único conjunto
de tiempos. Cuatro niveles controlan cuánto:

| Nivel | Lo usan | Qué ves |
| --- | --- | --- |
| Full | Modo Signal | Los efectos más ricos |
| Standard | Everyday, Studio | Los popups crecen desde el disparador |
| Reduced | Focus | Aparecen en su lugar, deslizamiento mínimo |
| Off | Gaming, reduce motion | Instantáneo, fundidos de hasta 90 ms |

Con **Full** y **Standard** está activo todo lo que se describe abajo.
**Reduced** quita el crecimiento y el escalonado. **Off** muestra cada
cambio de golpe; solo quedan fundidos rápidos, así un cambio nunca pasa
inadvertido.

Cómo se siente el nivel estándar: un popup crece desde su disparador en
alrededor de un tercio de segundo, sus filas entran con un escalonado corto
(como máximo ocho filas), pasar entre ítems vecinos transforma el popup en
vez de cerrarlo y reabrirlo, y cerrar es un fundido rápido. Nada parpadea ni
pulsa en reposo.

### Bajar el movimiento

- **Ajustes → Accessibility → Reduce motion** (el mismo interruptor está en
  **Appearance → Animations**) fuerza el nivel a Off en todos los modos de
  experiencia.
- También se respeta el ajuste global de GNOME
  `org.gnome.desktop.interface enable-animations`.
- **Ajustes → Accessibility → Animation speed** estira o acorta todas las
  duraciones sin cambiar el nivel.
- Un [modo de experiencia](experience-modes.md) define el nivel inicial, pero
  los ajustes de accesibilidad siempre ganan.

## Más información

- [Contrato de interacción para autores de extensiones](../development/interaction-contract.md)
  — las reglas de ubicación y movimiento que debe seguir una superficie.
- [Referencia de interacción de Shell](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md)
  — la tabla completa de cierre por superficie y los detalles del focus grab.
- [Hornero Signal](hornero-signal.md) — el lenguaje visual, incluida la
  accesibilidad.
