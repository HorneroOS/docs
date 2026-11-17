# Contrato de interacción para autores de extensiones

> Traducción al español rioplatense de la
> [versión en inglés](../../development/interaction-contract.md), que es la canónica.

Las extensiones comparten los popups, los tooltips, las reglas de foco y el
movimiento del shell. Esta página es el resumen para autores del conjunto de
reglas; la implementación y las tablas completas viven en el repositorio del
Shell ([`docs/INTERACTION.md`][interaction] y [`docs/PLUGINS.md`][plugins]).
La autoridad de diseño es la sección 4 (superficies ancladas) y la sección 3.6
(movimiento) de [RFC 0001](../../development/rfc-0001-hornero-signal.md), y las
secciones 7 y 11 de
[Signal Visual Language](../../development/signal-visual-language.md). Para lo
que experimenta una persona, mirá
[Popups, foco y movimiento](../desktop/popups-and-motion.md).

> **Desarrollo.** Esto describe Shell `main` desde noviembre de 2026 y el
> módulo PluginKit 3 que incluye. El solver de ubicación, su copia en
> PluginKit, la cascada de Escape y los niveles de movimiento están cubiertos
> por las pruebas headless y offscreen del Shell. Todavía no se validó nada de
> esto en una máquina virtual ni en un escritorio físico.

## La regla única

**Una extensión nunca posiciona su popup, ni lo dimensiona respecto de la
pantalla, ni lo anima.** Nombra un disparador (trigger); el host ubica y anima
la superficie. No calcules coordenadas de pantalla, no crees tu propia ventana
ni agregues tus propias animaciones de apertura y cierre a un popover o a un
tooltip.

## Usá los componentes del host

- **Un panel rico desde un indicador de la barra:**
  `UiPopover { target: indicator }`. No armes un `Item` de panel para anclarlo
  a mano.
- **Una pista al pasar el cursor o al enfocar:** `tooltipText` en `UiButton`,
  `UiToggle`, `UiSlider` o `UiActionRow`, o `UiTooltip { target; text }`. No
  muestres una etiqueta flotante propia.
- **Un mensaje transitorio:** `Notifications.toast(summary, body, glyph)`. No
  dibujes tu propio toast.

En una barra, el contenido del popover se entrega al popout propio del shell.
Se abre al pasar el cursor después de la demora (dwell), crece desde el
disparador, hace morph cuando el puntero pasa a un disparador vecino, respeta
la gracia de cierre y se cierra con el mismo fundido que los popouts nativos.
En el dashboard o en el escritorio, el popover se ubica solo con
`Placement.js`, una copia textual del solver del shell dentro de
`Hornero.PluginKit`.

La API estable de popover y tooltip es `target`, `text`, `delay`, `timeout`,
`preferredSide`, `accessibleName`, `contentPadding`, `initialFocusItem`,
`open()`, `close()`, `toggle()`, `dismiss()`, `actualSide` y
`placementFor(...)`.

### Ubicación con la que podés contar

- `preferredSide: "auto"` (el valor por defecto) se abre alejándose de la
  barra dueña: hacia abajo desde una barra superior, hacia arriba desde una
  inferior, hacia adentro desde un riel. Un disparador fuera de una barra
  prefiere la mitad vertical libre.
- Un lado explícito se invierte una vez si quedaría recortado. El panel se
  mantiene dentro de la pantalla menos un margen de 8 px y sigue a su
  disparador ante movimientos, cambios de tamaño y cambios de escala.
- Las superficies abiertas desde barras Cockpit Clear son tarjetas opacas; no
  asumas que hay una placa de barra detrás de tu contenido.
- Dale al popover un tamaño acotado. Cuando ningún lado alcanza, el host lo
  reduce al tamaño más grande que entre y desplaza la página, así que el
  contenido tiene que tolerar una caja más chica y nunca depender de una
  altura fija.

## Teclado y foco

- Los popovers por hover nunca toman el foco. Los que se abren con clic o
  teclado mueven el foco al panel (`initialFocusItem`, o si no el primer
  control enfocable) y lo devuelven al disparador al cerrarse.
- **Escape cierra primero tu popover**, antes que cualquier cosa debajo, y se
  consume ahí. Un Escape cierra una superficie. Manejá Escape para el estado
  interno propio (un campo de renombrado, un paso de confirmación) antes de
  dejarlo pasar.
- Definí `accessibleName` en el popover y en su disparador. Un tooltip también
  se expone como descripción accesible del disparador, así que nunca pongas
  información esencial, ni nada interactivo, solo en un tooltip.
- Toda acción alcanzable con el puntero tiene que ser alcanzable con el
  teclado; los anillos de foco se muestran solo cuando la última entrada fue
  del teclado (`Theme.keyboardFocus`).
- Los widgets de escritorio viven debajo de las ventanas y nunca le quitan el
  foco del teclado a las aplicaciones.

## Movimiento y movimiento reducido

Leé el movimiento desde `Theme`; no fijes duraciones a mano.

- `Theme.duration(name)`: `quick` 90, `short` 160, `medium` 240, `long` 360,
  `scan` 480, `settleFast` 220 y `settle` 320 ms, más `fade` para la
  opacidad.
- `Theme.anim.curves.<name>`: `standard`, `enter`, `exit`, `sweep`, `settle`
  y `settleFast`.
- `Theme.motionLevel`: `full`, `standard`, `reduced` u `off`.
- `Theme.reducedMotion`: verdadero cuando la persona pidió menos movimiento;
  fuerza `off`.

Reglas que verifica la revisión:

- Usá las curvas `settle` solo para mover posición, tamaño o forma, nunca
  opacidad ni color.
- En el nivel `off` las duraciones son 0, salvo `fade`, que se limita a
  90 ms; en `reduced` no hay morph ni stagger. Tus propias transiciones
  tienen que colapsar igual, así que consultá `Theme.motionLevel` o usá
  `Theme.duration(...)`, que ya lo hace.
- Nada parpadea, pulsa ni se anima en reposo. Un `UiProgress` indeterminado
  es estático.
- Los acentos luminosos (`glow`) nunca se dibujan a mano. Los aplican los
  componentes de instrumentos, y solo mientras se cumpla `Theme.glowEnabled`,
  que es verdadero únicamente en la experiencia Signal con un tema oscuro,
  sin alto contraste y con movimiento permitido. Sin una concesión (lease)
  del presupuesto de glow de todo el shell, una traza dibuja la misma línea
  sin el halo.
- El sondeo (polling) sigue a la experiencia: leé `Theme.telemetryIntervalMs`
  o usá los proveedores compartidos en lugar de tus propios temporizadores.
  En Gaming y Focus la capa de escritorio no instancia ningún widget, así que
  un widget de escritorio tiene que liberar todo cuando se destruye. Mirá
  [Extensiones](../../development/extensions.md#shared-data-providers).

## Lista de verificación

- [ ] Los popups usan `UiPopover` o `UiTooltip`; sin coordenadas manuales.
- [ ] El contenido funciona en una caja más chica que la diseñada.
- [ ] Escape cierra el popover y el foco vuelve al disparador.
- [ ] `accessibleName` está definido en el disparador y en el popover; nada
  esencial vive solo en un tooltip.
- [ ] Las transiciones usan `Theme.duration(...)` y colapsan en `off`.
- [ ] Sin animación en reposo y sin glow dibujado a mano.
- [ ] Verificado en los niveles de movimiento `standard` y `off`, y solo con
  el teclado. Registrá dónde se verificó (offscreen, máquina virtual o host).

[interaction]: https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md
[plugins]: https://github.com/HorneroOS/shell/blob/main/docs/PLUGINS.md
