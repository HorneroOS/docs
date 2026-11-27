# Auditoría de calidad visual — Hornero Signal

> Traducción al español rioplatense de la
> [versión en inglés](../../development/visual-quality-audit.md), que es la
> canónica.

- **Estado** — Auditoría independiente, 2026-11-17
- **Seguimiento** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28) y el
  issue de seguimiento de la auditoría visual enlazado desde ahí
- **Autoridad de diseño** — [RFC 0001](rfc-0001-hornero-signal.md)
  con sus enmiendas y
  [Signal Visual Language](signal-visual-language.md)
- **Audiencia** — mantenedores que deciden qué bloquea el lanzamiento de
  Signal, contribuyentes que toman trabajo visual

Esto es una auditoría de crítico, no un informe de estado. Juzga lo que existe
en la evidencia, como si fuera para un showcase curado de r/unixporn (WOW) y
para una estación de trabajo usada ocho horas por día (WORK). Cada hallazgo se
registra como un issue `visual-audit` en el repositorio que es dueño del
arreglo. Nada de este documento se verificó contra una sesión en vivo: el
auditor trabajó solo con la evidencia existente y pide las capturas listadas en
[Qué no se verificó](#qué-no-se-verificó).

## 1. Método y clases de evidencia

Las imágenes se abrieron y se leyeron, no se confió en los informes. Las clases
de evidencia, de la más fuerte a la más débil:

- **H, host real** — la sesión Hyprland del mantenedor: dashboard, launcher,
  Apariencia del Centro de control, Cockpit, bloqueo y tiras de 64 px de cada
  preset y borde. Se usó para barras, dashboard, launcher, bloqueo y
  Apariencia.
- **V, VM de QA** — `qa` `docs/evidence/signal-vm-20261117/` y los bundles de
  ejecución `20261117T02*` a `T03*` (1280x800). Se usó para layouts, popouts,
  tinta Clear y la puerta del instalador.
- **O, offscreen** — `shell` `.github/evidence/**` (Qt offscreen, fondo de
  reemplazo). Se usó para todas las superficies del shell en Night, Day y Alto
  Contraste.
- **W, web y greeter** — `greeter` `screens/signal/`, `website`
  `.github/evidence/signal-*` y `public/og/`. Se usó para el greeter, el sitio
  web y las tarjetas sociales.
- **C, concepto** — `docs` `development/assets/signal-visual-language/`. No es
  evidencia de producto; no se usó para calificar nada.

Las capturas del host contienen fragmentos de la terminal y del navegador del
mantenedor. Se citan por nombre en palabras y no se copiaron a ningún
repositorio.

Dos advertencias aplican a toda calificación:

1. **Desactualización.** Las capturas del host de 00:2x a 01:33 y las
   ejecuciones de VM hasta 03:2x se tomaron sobre imágenes y checkouts más
   viejos que el main del shell (`f47f323`). Las galerías de VM muestran
   barras de 52 px y 46 px; main ahora entrega 28 px y 24 px (#517-#520).
   Cuando es probable que un merge posterior haya arreglado un hallazgo, se
   dice y se pide una recaptura en lugar de afirmar un defecto.
2. **Escenario vacío.** Las capturas de VM muestran un fondo de grilla tipo
   plano sin ninguna ventana, así que no pueden mostrar cómo se relacionan las
   barras con el contenido (hallazgo VA-24).

## 2. Veredicto

**El lenguaje de diseño es sólido y el producto está cerca de alcanzarlo, pero
la barra todavía no es un showcase y un artefacto entregado bloquea el
lanzamiento.**

Lo que es genuinamente excelente, y conviene proteger:

- El dashboard de Rendimiento en el host: eyebrows numerados por canal, scopes
  con retícula, medidores segmentados, una línea de cota debajo de la barra de
  memoria. Es el único lugar que no se parece a nada más en r/unixporn.
- El greeter: una cinta de franjas del día de 24 h, pozos de lectura y
  esquineros sobre fotos fijas argentinas con crédito. Distintivo, legible y
  coherente.
- El reloj del bloqueo, la tipografía del sitio web y la anatomía del popup de
  notificación.
- Las barras finas. Las tiras del host a 28 px con radios de 3 px son la
  primera vez que las barras parecen instrumentos y no tabletas.
- Los estados vacíos honestos (guion largo, segmentos apagados) cuando faltan
  los datos.

Lo que le impide ser un showcase:

- **Disciplina cromática en la barra.** Seis tonos en una tira de 28 px (VA-04)
  y el logo de la distro en verde donde corresponde la única marca ámbar
  permanente (VA-03).
- **Dos gramáticas.** Notificaciones popup versus historial (VA-08), paneles
  Signal versus subpáginas más viejas (VA-18), encabezados eyebrow versus una
  barra de título genérica (VA-07).
- **Las interacciones estrella no tienen pruebas.** Ningún popout en host
  real, ninguna captura de movimiento, ninguna captura de glow en ningún lado
  (VA-11, VA-06).
- **Plugins a escala.** Los ítems de barra de plugins se superponen con los
  segmentos del núcleo y los widgets se solapan (VA-05, VA-06).
- **Primeras impresiones fuera del shell.** La sesión live de la ISO es
  pre-Signal y está visiblemente rota (VA-01), el sitio web abre con la
  apariencia anterior (VA-20), la página Atajos de la primera ejecución está
  vacía (VA-09).

Recomendación de lanzamiento: **VA-01 es el único P0.** El conjunto P1 de abajo
debería entrar antes de anunciar la preview de Signal; VA-11 (prueba del
popout) es un P1 que pasa a P0 si las notas de la versión anuncian la
interacción de popout anclado.

## 3. Tablero de calificaciones

Las calificaciones van de 1 (falla) a 5 (ejemplar); `-` significa que no existe
evidencia para esa puerta, no una buena nota. Puertas: **VE** excelencia
visual, **OR** originalidad frente a derivados de Material/Caelestia, **CO**
consistencia de tokens entre superficies, **US** usabilidad, **DI**
descubribilidad, **AC** accesibilidad, **PF** rendimiento, **TQ** calidad
técnica del renderizado, **CP** completitud. Las clases de evidencia son las de
la sección 1. `PF` es `-` en todas partes: no existe ninguna cifra de tiempo de
cuadro ni de CPU en reposo para ninguna superficie (RFC 0001 sección 7.1 y
lenguaje visual 11.4 las exigen).

| Superficie | Ev | VE OR CO US DI AC PF TQ CP |
| ---------- | -- | ----------------------- |
| Cockpit (por defecto de fábrica) | HVO | 3  4  3  4  3  3  -  4  3 |
| Cockpit Clear | VO | 2  4  3  3  3  3  -  3  2 |
| Horizon | HV | 4  3  3  4  3  3  -  4  3 |
| Islands | HV | 3  4  3  4  3  3  -  3  3 |
| Minimal Float (cozy-minimal) | HV | 4  3  4  4  3  3  -  4  3 |
| Dock | HV | 3  3  3  4  4  3  -  3  3 |
| Classic arriba / abajo | HV | 3  2  3  4  4  3  -  4  3 |
| Minimal Top | HV | 4  3  4  4  3  3  -  4  3 |
| Minimal Left (riel) | V | 3  4  3  3  2  3  -  3  2 |
| Studio | HV | 3  3  3  4  3  3  -  3  2 |
| Gaming | HV | 3  3  3  3  3  3  -  3  2 |
| Hornero Left / Right | HV | 3  2  3  4  3  3  -  3  3 |
| Indicadores de workspace y ventana | HVO | 4  4  4  4  3  4  -  4  3 |
| Launcher | HO | 4  3  4  4  4  3  -  4  4 |
| Dashboard (las cuatro pestañas) | HO | 4  4  4  3  3  3  -  3  3 |
| Marco de ventana del Centro de control | HV | 2  2  2  3  3  3  -  3  3 |
| Apariencia, temas, fondos | HVO | 2  2  2  2  3  3  -  3  3 |
| Audio, Pantallas, Energía, A11y, Entrada | O | 4  3  4  4  3  3  -  4  3 |
| Red, Bluetooth, VPN | O | 2  2  2  3  3  3  -  3  2 |
| Paneles Barras, Layout, Ventanas, Atajos | O | 3  3  3  2  2  3  -  3  3 |
| Selector de layout | O | 2  2  3  2  2  3  -  3  3 |
| Ajustes rápidos (cajón de utilidades) | O | 3  2  3  4  4  3  -  3  3 |
| Popups y toasts de notificación | O | 4  4  4  4  3  3  -  4  4 |
| Historial de notificaciones (barra lateral) | O | 2  2  2  3  3  3  -  3  3 |
| OSD | O | 3  3  3  3  3  3  -  3  3 |
| Menú de sesión / energía | O | 3  2  3  4  3  3  -  4  3 |
| Popouts anclados y tooltips | V | 3  4  3  -  3  -  -  3  1 |
| Telemetría, scopes, medidores, deck | HVO | 4  5  4  3  3  3  -  3  3 |
| Compañero (Javi) | O | 3  3  2  3  3  3  -  3  1 |
| Ítems de barra de plugins | V | 2  3  2  2  2  3  -  2  3 |
| Widgets de escritorio/dashboard de plugins | OV | 4  4  4  3  3  3  -  3  3 |
| Popovers de plugins | - | -  -  -  -  -  -  -  -  - |
| Marketplace (panel Extensiones) | O | 3  3  3  3  3  3  -  3  2 |
| Bloqueo | HO | 3  4  4  3  -  3  -  4  3 |
| Greeter | W | 4  5  4  3  3  3  -  4  3 |
| Instalador (Calamares y diapositivas) | VW | 2  2  2  3  3  2  -  2  1 |
| Bienvenida | O | 3  3  3  2  3  3  -  3  2 |
| Páginas del sitio web | W | 4  4  4  4  4  -  -  4  3 |
| Tarjetas sociales | W | 3  3  4  -  -  -  -  3  2 |
| Sitio de documentación | - | -  -  -  -  -  -  -  -  - |

Hallazgos y notas por superficie:

- Cockpit (por defecto de fábrica): VA-03, 04, 11, 12
- Cockpit Clear: VA-10
- Horizon: VA-04, 12
- Islands: VA-04; las píldoras de la VM son anteriores a #517
- Minimal Float (cozy-minimal): VA-04
- Dock: íconos de apps a todo color dentro de una barra monocromática
- Classic arriba / abajo: VA-04
- Minimal Top: VA-12
- Minimal Left (riel): solo numerales; no hay captura con una ventana
- Studio: no se vieron los medidores según la especificación 14.12
- Gaming: ocultarse bajo pantalla completa sin verificar
- Hornero Left / Right: VA-04; de inspiración Caelestia por diseño, con
  atribución
- Indicadores de workspace y ventana: VA-12; falta el numeral activo en un
  render offscreen
- Launcher: la superficie diaria más fuerte
- Dashboard (las cuatro pestañas): VA-13
- Marco de ventana del Centro de control: VA-07
- Apariencia, temas, fondos: VA-07, shell#514
- Audio, Pantallas, Energía, A11y, Entrada: VA-16
- Red, Bluetooth, VPN: VA-18; el panel VPN no se capturó
- Paneles Barras, Layout, Ventanas, Atajos: VA-17, 18
- Selector de layout: VA-17
- Ajustes rápidos (cajón de utilidades): VA-16
- Popups y toasts de notificación: VA-15
- Historial de notificaciones (barra lateral): VA-08
- OSD: VA-15
- Menú de sesión / energía: lista grande y genérica de íconos
- Popouts anclados y tooltips: VA-11
- Telemetría, scopes, medidores, deck: VA-06, 13
- Compañero (Javi): VA-18; la UI de chat no se capturó
- Ítems de barra de plugins: VA-05
- Widgets de escritorio y dashboard de plugins: VA-06, 22
- Popovers de plugins: sin captura
- Marketplace (panel Extensiones): el catálogo muestra 0 instalados en todas
  partes
- Bloqueo: VA-14
- Greeter: VA-19
- Instalador (Calamares y diapositivas): VA-01, 02
- Bienvenida: VA-09
- Páginas del sitio web: VA-20, 21
- Tarjetas sociales: VA-20
- Sitio de documentación: VA-21; sin captura

La accesibilidad se califica con 3 donde el contraste y los roles son
plausibles pero no están medidos (solo la tinta Clear tiene números); nada se
calificó por encima de 3 sin números, nada por debajo sin un defecto
específico.

## 4. Crítica transversal

### Escala tipográfica

El RFC define escalones (`small 11`, `body 13/14`, `title 18`, `display 28`).
Tamaños observados en las superficies: ~9 (error del greeter y del bloqueo),
10 (descripciones del Compañero), 11, 12, 13, 14, 16, 18, 22, 24 y ~34
(`Preview` de Apariencia). Solo los eyebrows aparecen en ~11, ~14 (widgets del
deck) y ~16-18 (historial de notificaciones). Los dos extremos son los peores
infractores: errores y líneas de estado por debajo de 11 px (VA-14, VA-19) y
encabezados de tamaño display en etiquetas triviales (VA-07). Aplica la
advertencia de "fontslop" de Marathon, citada en el propio lenguaje visual.

### Ritmo de espaciado y alineación

Las barras están sobre la grilla de 4 px y se leen bien, pero varias
alineaciones fallan: el token `ST` queda ~3 px por debajo de la línea base de
sus vecinos (VA-12); las columnas del dashboard terminan a alturas distintas
(VA-13); las filas del Centro de control van de visiblemente menos de 32 px
(Barras) a ~44 px (Audio) frente a un mínimo de 32 px (VA-18); los ítems de
barra de plugins usan tres líneas base (VA-05).

### Color

El lenguaje promete el ámbar como una señal racionada. En la práctica el ámbar
está en cada thumb de slider, cada chip seleccionado, los vecinos de la marca y
varios tiles, mientras que el verde (reloj, marca) y el cian (estado) llenan la
barra (VA-04). La gramática de selección del Centro de control cambia entre
filas rellenas de ámbar, pozos marrones y chips azul oscuro (VA-16).

### Forma

La disciplina de radios es mayormente buena (3 px). Excepciones: las cápsulas de
slider de Clear (VA-10), las píldoras de Islands en la VM (anteriores a #517,
recapturar), las ventanas redondeadas de 10-12 px en el host bajo la vieja
configuración de Hyprland (config#138 y #139 lo arreglaron en main; no se
recapturó) y la barra de título del Centro de control. La regla del usuario "sin
píldoras sobredimensionadas" se cumple en las tiras de las 01:33 y no está
probada en otros lados.

### Originalidad

No es Material, no deriva de Caelestia, con dos excepciones deliberadas (Hornero
Left/Right, con atribución). Los scopes, pozos, eyebrows de canal y la cinta de
franjas del día son originales. Riesgo: cada vez que el shell recurre a filas
genéricas (historial de la barra lateral, subpáginas de Bluetooth/Red, menú de
sesión) se lee como una app de ajustes oscura competente. La originalidad es
una propiedad de la superficie más débil que una captura de pantalla alcance a
mostrar.

### Movimiento

No se evidenció movimiento en ningún compositor real. El storyboard es un
render conceptual. Toda afirmación sobre movimiento en la especificación está
sin verificar (ver cobertura).

### Rendimiento

Sin números. El presupuesto de 60 fps y 4 ms del lenguaje visual 11.4 no se
puede confirmar; shell#47 y #228 son los issues base existentes.

### WOW versus WORK

- **WOW:** las barras Cockpit más el dashboard merecen una captura de pantalla
  solo una vez que VA-03/04 entren y se muestre un popout; el modo Signal no se
  distingue visiblemente de Everyday (shell#511); el bloqueo es tan sobrio que
  se vuelve olvidable (VA-14); el sitio web muestra la apariencia anterior
  (VA-20).
- **WORK:** las barras finas, las celdas de workspace y el launcher son una UI
  buena para uso diario. El ruido de toasts (VA-15), las páginas vacías de la
  primera ejecución (VA-09) y los paneles densos del Centro de control (VA-18)
  le restan comodidad al día a día.

## 5. Hallazgos y backlog priorizado

P0 bloquea el lanzamiento. P1 debería entrar antes de anunciar la preview de
Signal. P2 es pulido. Los issues llevan la etiqueta `visual-audit` y el prefijo
de título `[Pn]` en el repositorio dueño.

### P0

- **VA-01** [installer#101](https://github.com/HorneroOS/installer/issues/101):
  La primera ejecución de la ISO live muestra un escritorio pre-Signal roto:
  nombres de ligaduras de íconos como texto, banner de Calamares recortado

### P1

- **VA-02** [installer#102](https://github.com/HorneroOS/installer/issues/102):
  No hay captura de las páginas de Calamares con tema Signal; la presentación
  es Signal pero el chrome del instalador está sin verificar
- **VA-03** [shell#529](https://github.com/HorneroOS/shell/issues/529): La marca
  de la barra es el logo de la distro en verde fósforo, no la marca Hornero en
  ámbar señal
- **VA-04** [shell#530](https://github.com/HorneroOS/shell/issues/530):
  Disciplina cromática de la barra: marca y reloj verdes, íconos de estado
  cian, sliders ámbar, energía roja, bandeja a todo color
- **VA-05** [shell#531](https://github.com/HorneroOS/shell/issues/531): Los
  ítems de barra de plugins se superponen con los segmentos del núcleo e
  ignoran la escala tipográfica y el desborde de la barra
- **VA-06** [shell#532](https://github.com/HorneroOS/shell/issues/532): Deck de
  instrumentos del escritorio: los widgets se solapan y recortan su propio
  contenido
- **VA-07** [shell#533](https://github.com/HorneroOS/shell/issues/533): Centro
  de control, Apariencia: encabezado Preview sobredimensionado, IDs de fondo
  sin procesar, barra de título genérica, control de encabezado ambiguo
- **VA-08** [shell#534](https://github.com/HorneroOS/shell/issues/534): El
  historial de notificaciones de la barra lateral no es Signal: tiles de
  ícono, título y cuerpo corridos, controles sobredimensionados
- **VA-09** [shell#535](https://github.com/HorneroOS/shell/issues/535):
  Bienvenida abre con una página Atajos vacía y redacción de desarrollador en
  el flujo de primera ejecución
- **VA-10** [shell#536](https://github.com/HorneroOS/shell/issues/536): Cockpit
  Clear: el contorno sólido arregla la legibilidad pero vuelve la barra clara
  pesada y parecida a una calcomanía
- **VA-11** [shell#537](https://github.com/HorneroOS/shell/issues/537): Los
  popouts anclados, la interacción estrella de Signal, no tienen captura en
  host real ni en VM poblada
- **VA-19** [greeter#45](https://github.com/HorneroOS/greeter/issues/45): El
  mensaje de fallo de login del greeter y la sesión por defecto empañan una
  primera impresión por lo demás sólida
- **VA-20** [website#233](https://github.com/HorneroOS/website/issues/233): El
  sitio y las tarjetas sociales todavía muestran el escritorio pre-Signal; no
  hay captura real de Signal arriba del pliegue
- **VA-24** [qa#88](https://github.com/HorneroOS/qa/issues/88): Los escenarios
  visuales capturan un fondo vacío a 1280x800; faltan contenido real, popouts,
  resoluciones y números

### P2

- **VA-12** [shell#538](https://github.com/HorneroOS/shell/issues/538): Pulido
  del cluster final de la barra: token `ST` sin etiqueta bajo la línea base,
  medidores inferiores solo con glifo, ritmo de íconos apretado
- **VA-13** [shell#539](https://github.com/HorneroOS/shell/issues/539):
  Pestaña Rendimiento del dashboard: scopes vacíos al abrir, nombre de CPU
  truncado, fondos de columna desparejos
- **VA-14** [shell#540](https://github.com/HorneroOS/shell/issues/540):
  Pantalla de bloqueo: tarjeta de autenticación chica, línea fina atravesando
  el reloj, poco WOW para una superficie estrella
- **VA-15** [shell#541](https://github.com/HorneroOS/shell/issues/541): OSD y
  toasts de rutina: OSD de doble canal sobredimensionado, ruido de `Config
  loaded` y `Num lock enabled`
- **VA-16** [shell#542](https://github.com/HorneroOS/shell/issues/542): El
  control switch es un balancín de dos celdas cuyo estado apagado parece
  seleccionado
- **VA-17** [shell#543](https://github.com/HorneroOS/shell/issues/543): Las
  miniaturas del Selector de layout son wireframes casi idénticos y las
  descripciones se truncan
- **VA-18** [shell#544](https://github.com/HorneroOS/shell/issues/544): Los
  paneles del Centro de control mezclan generaciones: encabezados de
  subpágina, etiquetas minúsculas y estilos de chip distintos entre paneles
- **VA-21** [website#234](https://github.com/HorneroOS/website/issues/234): El
  sitio de documentación y las páginas de cola larga no tienen evidencia
  visual
- **VA-22** [plugins#71](https://github.com/HorneroOS/plugins/issues/71): El
  texto de los widgets propios filtra detalles de implementación; fixtures y
  regiones vacías en la evidencia
- **VA-23** [docs#124](https://github.com/HorneroOS/docs/issues/124): El
  lenguaje visual todavía especifica barras de 36/30 px y ejemplos de radio de
  3 px; las barras finas entregadas son de 28/24 px con un factor de densidad

Issues existentes sobre los que se apoya esta auditoría en lugar de duplicarlos:
shell#511 (modo Signal indistinguible), #512 (marca de muesca perdida de 6
px), #513 (popout de Energía recortado), #514 (nombres y chips de las tarjetas de
tema), #515 (borde de la barra en Signal Contrast), #516 (volcado de debug de
segunda salida), #485 y #478 (recomposición de superficies y deck),
plugins#21 (Extension Quality Gate), qa#81 (Premium Acceptance Matrix), qa#17
y #19, website#222 (regeneración retenida), hornero#427 (lanzamiento de
Signal).

## 6. Detalle de los hallazgos

### VA-01 (P0)

Defecto: La primera ejecución de la ISO live muestra un escritorio pre-Signal
roto: nombres de ligaduras de íconos como texto, banner de Calamares recortado

- **Superficie** — Instalador (Calamares) + shell de la sesión live + Bienvenida
- **Puertas** — Excelencia visual, Consistencia, Completitud, Calidad técnica
- **Issue** — [installer#101](https://github.com/HorneroOS/installer/issues/101)
- **Evidencia**
  - `HorneroOS/qa`
    `docs/evidence/signal-vm-20261117/installer-preview32-live-3gib-ram-gate.png`
    (VM, ISO preview32 firmada, 1280x800).

La única captura del camino del instalador entregado muestra cuatro fallas
visuales que bloquean el lanzamiento, todas a la vez. (1) La Bienvenida de
Hornero de la sesión live muestra los nombres de las ligaduras de íconos como
texto literal (`waving_hand`, `explore`, `terminal`, `chevron_right`, `apps`):
la fuente de íconos no se resuelve, así que cada fila tiene una palabra cruda de
20 px donde debería haber un glifo y el título de la página dice `waving_hand`.
(2) El shell de la ISO es el pre-Signal: el indicador de workspace es una
píldora crema redondeada con texto recortado (fragmentos `rmin`/`rmin`), el
riel izquierdo está cortado a mitad de palabra (`p_wi`, `ndar_m`, `_setting`),
los acentos son terracota y rosa, no ámbar Signal. (3) Calamares es el gris
claro de fábrica (cuerpo y botones Qt por defecto) con un banner terracota
oscuro recortado en el borde derecho (el chip `PREVIEW` queda cortado en `PRE`)
porque el banner es más ancho que el área de diapositivas de 1280 px. (4) El
estado de error (`does not have enough working memory`) es un bloque rosa con
texto negro de 14 px sobre una página gris: sin tratamiento Signal, sin eyebrow,
sin jerarquía. Un usuario nuevo se encuentra con esto antes que con cualquier
superficie de Signal.

**Dirección del arreglo.** Reconstruir la ISO desde los mains de Signal y
agregar un escenario smoke de la sesión live que falle si algún texto visible
coincide con `^[a-z_]{4,}$` dentro de un slot de ícono o si `fc-match 'Hornero
Glyphs'` cae en otra fuente. Incluir las fuentes de glifos y IBM Plex en el
conjunto de paquetes live. Recortar de nuevo el banner de Calamares a un ancho
máximo de 1024 px y aplicar los tokens Signal a `stylesheet.qss` (repositorio
installer `image/calamares/branding/hornero/`); reutilizar el lenguaje de
eyebrow/línea fina del sitio web que ya usa la presentación.

**No verificado.** Las páginas reales de Calamares distintas de la puerta de
bienvenida no tienen captura de la era Signal. Los cuadros de la presentación
son renders web, no el instalador en ejecución.

### VA-02 (P1)

Defecto: No hay captura de las páginas de Calamares con tema Signal; la
presentación es Signal pero el chrome del instalador está sin verificar

- **Superficie** — Instalador (páginas de Calamares, presentación)
- **Puertas** — Completitud, Consistencia, Accesibilidad
- **Issue** — [installer#102](https://github.com/HorneroOS/installer/issues/102)
- **Evidencia**
  - `HorneroOS/installer` `.github/evidence/signal-installer-2026-11/` (banner,
    slideshow-00..04, niri-card): renders web/Qt solo de las diapositivas.
  - `HorneroOS/installer`
    `.github/evidence/provisional-installer-2026-10/live-boot-20261023/` muestra
    el chrome gris de fábrica.

La presentación es el mejor activo del instalador (numerales de índice grandes
`00`/`02`/`04` en `inkFaint`, líneas finas, etiquetas eyebrow, filas de chips).
Pero el texto del cuerpo de las diapositivas es chico en relación con el lienzo,
y el numeral de índice muy grande es el elemento más fuerte de la diapositiva
sin aportar información. Nada prueba que el chrome de Calamares que la rodea lo
siga: la evidencia de octubre es la de fábrica. No existe captura con escala
(1.25x/1.5x) ni HiDPI, ni variante Day.

**Dirección del arreglo.** Agregar escenarios `install/signal-pages` a qa (ver
qa#19), extender el README de evidencia con una lista de verificación por
página y ajustar la escala tipográfica de la presentación a los escalones del
RFC (display 28, title 18, body 14 -> 16 para diapositivas).

**No verificado.** Todas las páginas de Calamares salvo la de bienvenida; tema
Day; escala > 1; textos en español (el sitio es ES-first).

### VA-03 (P1)

Defecto: La marca de la barra es el logo de la distro en verde fósforo, no la
marca Hornero en ámbar señal

- **Superficie** — Barras (Cockpit, Classic, Horizon, Studio, rieles),
  disparador del launcher
- **Puertas** — Excelencia visual, Originalidad, Consistencia
- **Issue** — [shell#529](https://github.com/HorneroOS/shell/issues/529)
- **Evidencia**
  - Capturas del host (locales del mantenedor, no commiteadas):
    `host/04-cockpit.png`, `host/layouts/cockpit-top.png`,
    `host/layouts/horizon-top.png`; chevron verde `A` al inicio de la barra en
    cada layout.
  - VM: `docs/evidence/signal-vm-20261117/shell-night-reference.png` y todas las
    ejecuciones `layouts-gallery-*` muestran el mismo glifo sobre una imagen de
    HorneroOS.
  - Código: `modules/bar/components/OsIcon.qml` dibuja `SysInfo.osLogo` con
    `Signal.palette.phosphor`.
  - Especificación: `signal-visual-language.md` sección 4.1 ("Mark ... in
    `signal`. It is the launcher trigger and the only permanently amber item");
    RFC 0001 sección 5.

El único elemento de marca de la barra es el logo de Arch Linux, teñido de
verde. En una instalación de HorneroOS lo primero en la barra Cockpit es el logo
de otra distribución, y lleva el color `phosphor` (dato/nivel) en lugar del
único acento ámbar permanente que el lenguaje reserva para la marca. La tarjeta
Station del dashboard también dice "Arch Linux".

**Dirección del arreglo.** Entregar la marca como glifo simbólico en Hornero
Glyphs (o un SVG monocromático), hacer de `osLogo` una opción
(`bar.mark = hornero|distro|custom`), con hornero por defecto, coloreada con
`Signal.palette.signal`.

**No verificado.** El comportamiento en una instalación real de HorneroOS a
través del conjunto de paquetes (contenido de os-release).

### VA-04 (P1)

Defecto: Disciplina cromática de la barra: marca y reloj verdes, íconos de
estado cian, sliders ámbar, energía roja, bandeja a todo color

- **Superficie** — Barras (Cockpit, Horizon, Studio, Classic, rieles)
- **Puertas** — Excelencia visual, Originalidad, Consistencia
- **Issue** — [shell#530](https://github.com/HorneroOS/shell/issues/530)
- **Evidencia**
  - Host (local del mantenedor): `host/04-cockpit.png`,
    `host/layouts/cockpit-top.png`, `horizon-top.png`, `studio-top.png`;
    `host/layouts/sheet-1.png` a `sheet-3.png`.
  - VM: `layouts-gallery-cockpit-1`,
    `signal-vm-20261117/shell-night-reference.png`.
  - Especificación: `signal-visual-language.md` sección 4.1 (glifos `ink`,
    clusters secundarios `inkMuted`, ámbar solo para lo vivo), RFC sección 2
    ("Amber marks only what is live").

Una sola tira de 28 px muestra al menos seis tonos: glifo de calendario verde y
minutos verdes en el reloj (`04 : 22`), una marca verde, glifos de estado cian
(volumen, wifi, bluetooth, modo), thumbs de slider ámbar y `SIG` ámbar, energía
roja, e íconos de bandeja a todo color blanco/rojo (tijeras, monitor rojo). La
disciplina de la especificación (ink, inkMuted, un solo ámbar) es lo que la
separaría de una Polybar arcoíris; hoy se lee como un dashboard con tema. El
color partido del reloj hace que la hora y los minutos parezcan dos lecturas.
El ámbar además se gasta en cada thumb de slider (permanentemente encendido al
43 %), así que ya no marca lo que está vivo.

**Dirección del arreglo.** Introducir `Segment.tone` (`ink`, `muted`, `live`,
`alert`) y encaminar cada componente de la barra a través de él; eliminar los
colores `phosphor`/`cue` por componente; reutilizar el camino de recoloreo de
ClearInk para los íconos de la bandeja.

**No verificado.** Barra con tema Day en el host; Alto Contraste en el host.

### VA-05 (P1)

Defecto: Los ítems de barra de plugins se superponen con los segmentos del
núcleo e ignoran la escala tipográfica y el desborde de la barra

- **Superficie** — Widgets de plugins (slots de barra), isla de Extensiones
- **Puertas** — Excelencia visual, Consistencia, Usabilidad, Calidad técnica
- **Issue** — [shell#531](https://github.com/HorneroOS/shell/issues/531)
- **Evidencia**
  - Evidencia de VM local de la misión `evidence/plugin-e2e/shots/dash-ext-12.png`
    y `bar-18-top.png` (36 plugins habilitados, 1280x800).

Con los 36 plugins del catálogo habilitados la barra superior es inusable:
`96.00 BPM` se dibuja encima de la marca Hornero, los primeros glifos del
cluster de acciones rápidas quedan sobreimpresos, `No input device` y `No output
device` son etiquetas de 14 px (el texto de la barra es de 11-12 px), `No
player` no tiene relleno de segmento, conviven tres líneas base distintas (`Moon
~49%`, `Sun Card`, `Aa`) y nada se colapsa en la isla de Extensiones. Los textos
de relleno (`No input device`, `No player`) ocupan ancho permanente de la barra
cuando lo correcto sería ocultarlos. 36 plugins habilitados es un caso extremo,
pero 6 a 8 es un usuario normal y la lógica de superposición es la misma.

**Dirección del arreglo.** Medir los anchos implícitos de los plugins en el host
de la barra, limitarlos a un ancho máximo (p. ej. 160 px) con puntos suspensivos,
aplicar los escalones de texto de `Density` mediante un `Theme.text` inyectado y
agregar el colapso por desborde en `ExtensionsIsland`.

**No verificado.** Host real con plugins habilitados (el host del usuario corre
plugins v3 pero no existe captura de la barra con ellos).

### VA-06 (P1)

Defecto: Deck de instrumentos del escritorio: los widgets se solapan y recortan
su propio contenido

- **Superficie** — Deck de instrumentos Signal / widgets de escritorio
- **Puertas** — Excelencia visual, Calidad técnica, Completitud
- **Issue** — [shell#532](https://github.com/HorneroOS/shell/issues/532)
- **Evidencia**
  - Evidencia de VM local de la misión `evidence/plugin-e2e/shots/all36-desktop.png`
    (1280x800).
  - `HorneroOS/shell` `.github/evidence/signal-deck/deck-layout.png` es un
    diagrama del solver, no un render.

El widget Moon Phase se sienta encima del widget Now Playing (el eyebrow `NO
PLAYER` se asoma en el borde derecho del encabezado de Moon); System Insight
está cortado a mitad de fila (`CORES` recortado en su borde inferior, la
tarjeta es más corta que su contenido); Network Scope deja una zona muerta de
70 px debajo de `SESSION DOWN/UP`. Los eyebrows de los widgets son visiblemente
más grandes que el eyebrow de 11-12 px que se usa en el dashboard y los
paneles. Esta es la superficie que va a estar en cada captura de r/unixporn del
modo Signal.

**Dirección del arreglo.** Pasar los tamaños implícitos reales a
`services/deck.js` y renderizar a partir de él; agregar un test de geometría QML
que instancie el deck con los 6 widgets del deck y verifique que no haya
solapamiento y que `contentHeight <= height`.

**No verificado.** Glow/scanlines en el deck; CPU en reposo con el deck
corriendo (RFC 7.1 pide números).

### VA-07 (P1)

Defecto: Centro de control, Apariencia: encabezado Preview sobredimensionado, IDs
de fondo sin procesar, barra de título genérica, control de encabezado ambiguo

- **Superficie** — Ventana del Centro de control, panel Apariencia
- **Puertas** — Excelencia visual, Consistencia, Usabilidad
- **Issue** — [shell#533](https://github.com/HorneroOS/shell/issues/533)
- **Evidencia**
  - Host (local del mantenedor): `host/03-cc-appearance.png` (1920x1080).
  - VM:
    `docs/evidence/signal-vm-20261117/shell-appearance-pane-chips-overlap.png`.

La jerarquía está invertida: la columna derecha abre con `Preview` en ~34 px en
negrita Plex Sans, el texto más grande de la ventana, sobre una tarjeta cuyo
contenido real (nombre del tema 16 px, descripción 13 px, cinco muestras de 16
px) es chico; el título del panel `Appearance` (24 px) lleva un ícono de flechas
de orden a la derecha sin etiqueta ni evidencia de tooltip. La barra de título
de la ventana es un `Hornero Settings - Appearance` genérico y centrado con un
ícono de app diminuto y una X, que no usa el lenguaje de eyebrow/registro de los
paneles que tiene debajo (`14 · SOUND & ALERTS`). Las miniaturas de fondos
están rotuladas con nombres de archivo crudos (`wallhaven 73v179`, `wallhaven
lqxdqy`). En la captura del host diez encabezados de acordeón (THEMES ...
HEALTH & SYNC) están colapsados, de modo que el contenido principal de un
panel de Apariencia, las tarjetas de tema, no se ve sin un clic (arreglado en
parte por #519 para configuraciones actualizadas; no se recapturó).

**Dirección del arreglo.** Mover la barra de título al encabezado de canal
Signal; derivar nombres para mostrar en el modelo de fondos (`displayName`);
reducir Preview al eyebrow compartido de `PaneHeader`.

**No verificado.** Apariencia en Day y Alto Contraste en el host; escala
1.25x/1.5x.

### VA-08 (P1)

Defecto: El historial de notificaciones de la barra lateral no es Signal: tiles
de ícono, título y cuerpo corridos, controles sobredimensionados

- **Superficie** — Barra lateral / historial de notificaciones
- **Puertas** — Excelencia visual, Consistencia, Usabilidad, Descubribilidad
- **Issue** — [shell#534](https://github.com/HorneroOS/shell/issues/534)
- **Evidencia**
  - `HorneroOS/shell`
    `.github/evidence/sidebar/after-night-offscreen-notifications.png` (470x700)
    frente a `.github/evidence/notifications/after-night-offscreen.png`.

Las notificaciones popup usan la receta Signal: eyebrow (`BUILDS · NOW`), título
en negrita de 16 px en su propia línea, cuerpo de 14 px, borde de estado de 1
px. La lista de historial al lado no: cada tarjeta tiene un cuadrado con
contorno de ~40 px que contiene un glifo genérico de globo de diálogo (el mismo
glifo para Terminal, Mail y Files, así que no aporta información), el nombre de
la app y `now` comparten fila con un expansor `1 v` enmarcado, y el título y el
cuerpo corren juntos en una línea con ajuste (`Build passed All 1,246 tests
passed.`, con el título distinguido solo por el peso). `Clear all` es un botón
relleno de ~30 px, el control más grande de la columna, mientras que la
tarjeta urgente es un tile de ícono completamente relleno de rojo. El
encabezado `04 · NOTIFICATIONS` es mono de ~16-18 px, muy por encima del
eyebrow de 11 px que se usa en otros lados. Mismos datos, dos gramáticas.

**Dirección del arreglo.** Extraer la tarjeta del popup a una `NotificationCard`
compartida, usada por el popup y por el historial, parametrizada por `compact`.

**No verificado.** Notificaciones con cuerpo largo, muchas acciones e imágenes
en el historial; navegación con teclado.

### VA-09 (P1)

Defecto: Bienvenida abre con una página Atajos vacía y redacción de
desarrollador en el flujo de primera ejecución

- **Superficie** — Bienvenida
- **Puertas** — Completitud, Usabilidad, Descubribilidad
- **Issue** — [shell#535](https://github.com/HorneroOS/shell/issues/535)
- **Evidencia**
  - `HorneroOS/shell`
    `.github/evidence/welcome/after-night-offscreen-shortcuts.png`,
    `after-night-offscreen-start.png`.

La página Atajos, la que se le dice a un usuario nuevo que abra para aprender el
escritorio, muestra un glifo de teclado y "No keybindings found. Regenerate the
shortcuts manifest." Eso es una instrucción del sistema de compilación mostrada
a usuarios finales. La página Inicio lista "Compositor tuning - Not available"
y "Low-latency audio profile - Checked on first use" en tres columnas de
registro diminutas (11 px) cuyas filas se ajustan a 60 caracteres, así que la
primera pantalla es texto de estado denso sin una única llamada a la acción (las
tres filas de acción de abajo compiten por igual). El chip de filtro `All` es
una caja de ~46x27 px con borde ámbar y una sola opción.

**Dirección del arreglo.** Generar el manifiesto de atajos en el empaquetado de
`hornero-config` (o leer los binds con `hyprctl binds -j` en tiempo de
ejecución) y condicionar la página a que haya datos; simplificar el texto de
StartPage.

**No verificado.** Bienvenida en español; Day; texto grande.

### VA-10 (P1)

Defecto: Cockpit Clear: el contorno sólido arregla la legibilidad pero vuelve la
barra clara pesada y parecida a una calcomanía

- **Superficie** — Barras (Cockpit Clear, tira inferior de Horizon)
- **Puertas** — Excelencia visual, Originalidad, Accesibilidad
- **Issue** — [shell#536](https://github.com/HorneroOS/shell/issues/536)
- **Evidencia**
  - Offscreen local de la misión `evidence/ink/v3/*.png` (glaciar, agua,
    follaje, ciudad): contornos claros/oscuros de 2 px en cada glifo; la pista
    del slider dibujada como contorno de píldora blanca.
  - VM antes del arreglo: `signal-vm-20261117/shell-clear-ink-iguazu-detailed.png`,
    `...quebrada-vivid.png`, `...ibera-bright.png` (ilegible), y las
    ejecuciones `wallpapers-ink-cockpit-clear-*` (barras de 52 px/46 px,
    pre-finas).
  - Especificación: `signal-visual-language.md` sección 12 (halo de 1 px,
    sombra suave de 4 px solo en regiones con detalle, los pozos pasan a ser un
    contorno de 1 px).

shell#524 arregló el P0 (el texto de Clear era ilegible sobre agua y follaje en
las capturas de VM). La respuesta actual usa un contorno sólido más ancho que el
halo de 1 px de la especificación: los trazos son lo bastante gruesos como para
que las etiquetas mono de 11 px (`CPU`, `MEM`) se empasten, y las pistas de los
sliders de volumen y brillo pasan a ser cápsulas blancas de radio completo, las
únicas formas de píldora que quedan en la barra. Los dígitos del reloj tienen
contorno mientras que el glifo de calendario a su lado no, así que el grupo se
ve desparejo. Sobre el fondo glaciar brillante el contraste p5 del peor cluster
sigue en 2.86 (objetivo >= 4.5 mediana, >= 3 peor).

**Dirección del arreglo.** Ajustar ClearInk a halo de 1 px + sombra condicional,
cambiar el dibujo de pistas a `Rectangle` con `radius:
Appearance.rounding.small` y aplicar el halo a nivel de `Segment` para que los
grupos mixtos de glifo/texto coincidan.

**No verificado.** Cockpit Clear con un fondo de video o de presentación; en el
host después de las barras finas; a 2x.

### VA-11 (P1)

Defecto: Los popouts anclados, la interacción estrella de Signal, no tienen
captura en host real ni en VM poblada

- **Superficie** — Popouts (audio, red, estado, recursos), tooltips, muesca
- **Puertas** — Completitud, Excelencia visual, Calidad técnica
- **Issue** — [shell#537](https://github.com/HorneroOS/shell/issues/537)
- **Evidencia**
  - Host (local del mantenedor): `host/05-top-audio-popout.png`,
    `05b-top-network-popout.png`, `06-bottom-popout.png` no muestran ningún
    popout; solo se ve un tooltip de `Settings`.
  - VM: `docs/evidence/signal-vm-20261117/shell-power-popout-text-clipped.png`,
    `shell-closed-popout-notch-crop-10x.png`, `shell-scaled-output-popout.png`;
    ejecuciones `bars-popout-placement-*`.

Tres intentos en el host de abrir popouts con movimientos sintéticos del cursor
no produjeron ninguno (la intención de hover es de 120 ms; el puntero se mueve
en pasos de 12 ms y la captura espera 1.4 s). O el movimiento sintético no
genera los eventos de hover, o los popouts por hover no se abren en el host; la
captura no permite distinguirlo. Las capturas de popout en VM muestran un fondo
vacío detrás de un panel de 285 px de ancho con texto truncado (`Power profile:
E`), y la marca de muesca ámbar de 6 px persiste cuando no hay ningún popout
abierto (shell#512). Nada demuestra el morph, la continuidad de la muesca ni
las variantes anclada/flotante en el compositor real.

**Dirección del arreglo.** Exponer los ids de popout en el target IPC
existente, agregar una acción de paso de qa `popout.open` y agregar los casos a
los escenarios de layouts-gallery.

**No verificado.** Todo lo relativo al movimiento (tiempos del morph, stagger)
en cualquier compositor real; comportamiento de hover frente a clic en el host.

### VA-12 (P2)

Defecto: Pulido del cluster final de la barra: token `ST` sin etiqueta bajo la
línea base, medidores inferiores solo con glifo, ritmo de íconos apretado

- **Superficie** — Barras (cluster final de Cockpit, tira inferior)
- **Puertas** — Excelencia visual, Descubribilidad, Accesibilidad
- **Issue** — [shell#538](https://github.com/HorneroOS/shell/issues/538)
- **Evidencia**
  - Host (local del mantenedor): `host/layouts/cockpit-top.png`,
    `horizon-top.png`, `studio-top.png`, `host/04-cockpit.png` (tira
    inferior).

Un token de dos letras `ST` sigue a los íconos de estado en cada tira de la
familia Cockpit, queda unos 3 px más abajo que sus vecinos (centro en y 21 frente
a 18 en una tira de 28 px) y no tiene etiqueta de hover en ninguna captura, así
que un extraño no puede saber qué es. La tira inferior del host
(`04-cockpit.png`) muestra `US`, tres porcentajes solo con glifo (`1%`, `43%`,
`64%`) y un valor de termómetro sin etiquetas (densidad `values`), de modo que
`43%` es ambiguo entre memoria y CPU; la tira de horizon sí muestra `CPU MEM DSK
TMP`. El espaciado de íconos dentro del cluster de estado es de 18 px pero la
separación con la bandeja es de 22 px y con el chevron de 16 px: tres ritmos en
140 px.

**Dirección del arreglo.** Auditar con el volcado de debug de la barra (`qs ipc
call debug bars`) los desfases de línea base; hacer que Density elija `labels`
según el ancho.

**No verificado.** Qué representa `ST` en el build en ejecución.

### VA-13 (P2)

Defecto: Pestaña Rendimiento del dashboard: scopes vacíos al abrir, nombre de CPU
truncado, fondos de columna desparejos

- **Superficie** — Dashboard (Rendimiento, Medios, Clima)
- **Puertas** — Excelencia visual, Usabilidad, Completitud
- **Issue** — [shell#539](https://github.com/HorneroOS/shell/issues/539)
- **Evidencia**
  - Host (local del mantenedor): `host/02-dashboard.png` (pestaña Rendimiento).
  - `HorneroOS/shell`
    `.github/evidence/dashboard/after-night-offscreen-media.png`,
    `...-weather.png`.

Lo bueno: los eyebrows con números de canal, los scopes con retícula, los
medidores segmentados y la línea de cota debajo de la barra de memoria son la
mejor ejecución de Signal del producto. Defectos: (1) ambos scopes de 60 s
abren sobre una retícula con un muñón de una muestra en el borde derecho, así
que el primer minuto parece roto (no hay estado `COLLECTING`); (2) la etiqueta
de la CPU se trunca a `AMD RYZEN 9 5900X 12-`; (3) la columna izquierda termina
en y 595 y la derecha en y 550, así que el fondo del panel queda desparejo y
`GPU` es más alto que `NETWORK`; (4) el trazo del scope es fino y de bajo
contraste en el host (la especificación pide un trazo fósforo de 1.5 px con
persistencia); (5) la pestaña Medios sin reproductor dibuja un pozo de segmento
vacío de ancho completo que parece una barra de búsqueda rota; (6) Clima sin
ubicación es un panel grande y vacío.

**Dirección del arreglo.** Agregar un estado `samples < window` a `ScopeTrace`;
usar `elide: Text.ElideMiddle`; armar la página Rendimiento con un Grid de 2
columnas con row spans.

**No verificado.** Pestañas Workspaces y Extensiones en el host; dashboard a
1366x768.

### VA-14 (P2)

Defecto: Pantalla de bloqueo: tarjeta de autenticación chica, línea fina
atravesando el reloj, poco WOW para una superficie estrella

- **Superficie** — Bloqueo
- **Puertas** — Excelencia visual, Originalidad, Accesibilidad
- **Issue** — [shell#540](https://github.com/HorneroOS/shell/issues/540)
- **Evidencia**
  - Host (local del mantenedor): `host/08-signal-mode.png` (en realidad es la
    pantalla de bloqueo, 1920x1080).
  - `HorneroOS/shell` `.github/evidence/lock/after-night-offscreen-idle.png`,
    `...wrong-password.png`.

El reloj condensado de 120 px y la regla ámbar de 48 px son excelentes. La
tarjeta de autenticación es de 360x125 px a 1080p con texto de 11 px (`Num lock
is ON.`, `01 · LOCKED`), así que el elemento interactivo es lo más chico de la
pantalla, el mensaje de contraseña incorrecta es de unos 9 px rojo sobre grafito
(cuadro offscreen `wrong-password` de 1600x900), y la línea fina diagonal de
(975,105) a (0,1080) cruza el `1` inicial del reloj. `Num lock is ON.` es una
línea de estado que debería aparecer solo cuando está APAGADO. La superficie es
un `ground` plano con dos tarjetas en las esquinas: sobria, pero para la
pantalla de bloqueo, la captura que más se publica, es la superficie menos
memorable.

**Dirección del arreglo.** Parametrizar la tarjeta por `Density` y altura de
pantalla; mover la línea fina detrás de una máscara de recorte; agregar un slot
opcional `lock.instrument` alimentado por los proveedores del deck.

**No verificado.** Estado de huella digital; bloqueo multimonitor; bloqueo sobre
el fondo real.

### VA-15 (P2)

Defecto: OSD y toasts de rutina: OSD de doble canal sobredimensionado, ruido de
`Config loaded` y `Num lock enabled`

- **Superficie** — OSD, toasts
- **Puertas** — Excelencia visual, Usabilidad, Rendimiento
- **Issue** — [shell#541](https://github.com/HorneroOS/shell/issues/541)
- **Evidencia**
  - `HorneroOS/shell` `.github/evidence/osd/after-night-offscreen.png`
    (300x330), `.github/evidence/toasts/after-night-offscreen.png`.
  - Host (local del mantenedor): `host/01-first-boot.png`, `host/04-cockpit.png`
    (toast sobre la tira inferior).

El OSD de volumen es una losa flotante de ~130x230 px que muestra OUT y BRI
juntos incluso cuando solo cambió el volumen; BRI marca 0 en una máquina sin
retroiluminación. El medidor es una columna acanalada y densa de segmentos muy
chicos, así que se lee como una textura y no como un instrumento. En el host se
disparan dos toasts por eventos de rutina: `Config loaded in 909ms` (en cada
recarga/arranque) y `Num lock enabled`; ambos se superponen con el contenido
inferior derecho y el segundo se apila sobre la barra inferior. Las severidades
de los toasts mezclan una franja izquierda (done, warning, note) con un borde
rojo completo (error), de modo que el error es una forma distinta y no un
estado más fuerte.

**Dirección del arreglo.** Conducir el contenido del OSD desde la última
propiedad que cambió; degradar los avisos de config/numlock al historial sin
popup; unificar los bordes de `Toast`.

**No verificado.** Tiempos de movimiento del OSD (entrada 90 ms, permanencia
1200 ms); apilado de toasts con 4+ ítems en el host.

### VA-16 (P2)

Defecto: El control switch es un balancín de dos celdas cuyo estado apagado
parece seleccionado

- **Superficie** — Centro de control y ajustes rápidos (cada toggle)
- **Puertas** — Usabilidad, Accesibilidad, Consistencia
- **Issue** — [shell#542](https://github.com/HorneroOS/shell/issues/542)
- **Evidencia**
  - `HorneroOS/shell`
    `.github/evidence/controlcenter-settings-panes/accessibility-night-offscreen.png`
    (ampliada), `controlcenter-daily-panes/audio-night-offscreen.png`,
    `controlcenter-hubs/studio-hub-night-offscreen.png`.

El switch es un balancín de dos celdas de 42x25 px: OFF enciende la celda
izquierda (relleno elevado y un rectángulo relleno), ON enciende la celda
derecha en ámbar con una `I` fina. Una celda izquierda encendida se lee como
seleccionada/activa para cualquiera que no esté familiarizado con las marcas
I/O; un bloque relleno no es una `O` reconocible; la `I` fina mide 1 px de
ancho sobre la celda oscura. El estado lo lleva sobre todo el relleno, sin
texto, y el control mide exactamente 24 px de alto (el mínimo de WCAG 2.5.8). Al
lado, los grupos de chips (panel Barras `Speakers`, `Microphone` ...) usan
relleno ámbar para lo seleccionado y gris azul oscuro para lo no seleccionado,
una tercera gramática de selección.

**Dirección del arreglo.** Redibujar el thumb de `UiToggle`/`SwitchRow` con un
par `O`/`I` claro; migrar los grupos de chips a `SegmentedControl`.

**No verificado.** Toggle a escala 1.5x; anuncios del lector de pantalla.

### VA-17 (P2)

Defecto: Las miniaturas del Selector de layout son wireframes casi idénticos y
las descripciones se truncan

- **Superficie** — Selector de layout, panel Layout
- **Puertas** — Descubribilidad, Excelencia visual
- **Issue** — [shell#543](https://github.com/HorneroOS/shell/issues/543)
- **Evidencia**
  - `HorneroOS/shell`
    `.github/evidence/controlcenter-hubs/layout-presets-night-offscreen.png`,
    `.github/evidence/layout-picker-mixed-label/`.

Dieciséis tarjetas usan el mismo wireframe oscuro con una barra ámbar fina
movida a otro borde, así que Cockpit, Classic Top, Studio y Productivity son
indistinguibles de un vistazo, lo que frustra a un selector cuyo trabajo es
comparar. Las descripciones se cortan a los 28 caracteres (`After Polybar
default +...`, `After Waybar cozy-min...`), la atribución (un requisito del RFC
para Hornero Left/Right) es lo primero que se trunca, y la evidencia todavía
lista `Floating Island` y `Productivity`, que el lenguaje eliminó (sección 14),
así que la captura está desactualizada o los datos todavía los contienen.

**Dirección del arreglo.** Generar las miniaturas a partir del JSON del preset
(un `PresetThumbnail` en QML que dibuje los mismos segmentos a escala 1/8).

**No verificado.** Selector de layout a 1366x768; el selector en el host.

### VA-18 (P2)

Defecto: Los paneles del Centro de control mezclan generaciones: encabezados de
subpágina, etiquetas minúsculas y estilos de chip distintos entre paneles

- **Superficie** — Centro de control (paneles Bluetooth, Red, Compañero,
  Dashboard, Barras, Ventanas)
- **Puertas** — Consistencia, Descubribilidad
- **Issue** — [shell#544](https://github.com/HorneroOS/shell/issues/544)
- **Evidencia**
  - `HorneroOS/shell`
    `.github/evidence/controlcenter-network-bt-bars/bluetooth-night-offscreen.png`,
    `wireless-night-offscreen.png`, `companion-night-offscreen.png`,
    `windows-night-offscreen.png`, `taskbar-night-offscreen.png`,
    `controlcenter-daily-panes/audio-night-offscreen.png`.

Audio, Pantallas, Extensiones, Energía y Accesibilidad abren con eyebrow `NN ·
SECTION`, título de 28 px y subtítulo. Las subpáginas de Bluetooth y Red abren
con `Bluetooth Settings` / `Network settings` (un glifo diminuto, título de 18
px, sin eyebrow de canal) y una fila de cuatro chips de ícono verdes/azules/ámbar
arriba a la izquierda; Compañero usa un título de 22 px pero etiquetas de 11 px
y descripciones de 10 px en una densidad de 3 columnas; Barras es un mosaico de
seis paneles con más de 20 chips y cada fila es de 11 px. Las alturas de fila
van de claramente menos de 32 px (Barras) a ~44 px (Audio); los tamaños de
etiqueta de 10 a 13 px. La especificación pide filas de 32 px como mínimo.

**Dirección del arreglo.** Imponer `PaneHeader` mediante el registro de paneles
(patrón de shell#460) y un test de lint para las raíces de panel; dividir Barras
en pestañas Secciones / Estado / Comportamiento.

**No verificado.** Day y Alto Contraste en ventanas reales; los 30 paneles a
1366x768.

### VA-19 (P1)

Defecto: El mensaje de fallo de login del greeter y la sesión por defecto
empañan una primera impresión por lo demás sólida

- **Superficie** — Greeter (SDDM)
- **Puertas** — Accesibilidad, Usabilidad, Completitud
- **Issue** — [greeter#45](https://github.com/HorneroOS/greeter/issues/45)
- **Evidencia**
  - `HorneroOS/greeter` `screens/signal/05-login-failed.jpg`,
    `01-signal-night-golden-hour.jpg`, `06-session-list-open.jpg`,
    `04-high-contrast-large-text.jpg`.

El greeter es la superficie mejor realizada del conjunto (cinta de franjas del
día de 24 h, pozos de lectura SEC/ZONE/DAYPART, esquineros de línea fina, fotos
fijas con crédito en el pie). Defectos: (1) la línea de login fallido (`Login
failed`) mide unos 9 px en rojo sobre casi negro a 1920x1080, por debajo de lo
legible aunque el campo recibe un pozo de alerta; (2) cada cuadro preselecciona
`HorneroOS Gaming Session (Experimental)` mientras la lista de sesiones la
muestra por encima de las otras sesiones Hyprland, de modo que un usuario por
defecto terminaría en la sesión experimental (orden del modo de prueba, sin
verificar); (3) el botón `Login` ámbar de ancho completo es el bloque más
estridente del panel, más que las lecturas y cercano al reloj en peso visual. El
fallback Day usa una foto de atardecer con chip `STILL` pero sin verificación de
la paleta Signal Day.

**Dirección del arreglo.** Subir la línea de estado al escalón `small`; ordenar
las sesiones por una prioridad estable desde `hornero-config`; ajustar el estilo
de estados del botón.

**No verificado.** Reproducción de video y chip `LIVE`; sesión real del display
manager SDDM en una VM; 4K; lista de varios usuarios.

### VA-20 (P1)

Defecto: El sitio y las tarjetas sociales todavía muestran el escritorio
pre-Signal; no hay captura real de Signal arriba del pliegue

- **Superficie** — Home del sitio web, tarjetas OG/sociales, showroom
- **Puertas** — Excelencia visual, Originalidad, Completitud
- **Issue** — [website#233](https://github.com/HorneroOS/website/issues/233)
- **Evidencia**
  - `HorneroOS/website` `.github/evidence/signal-homepage/home-night-1920.png`,
    `home-en-day-1280.png`, `home-experience-concepts-1280.png`;
    `public/og/default.png`, `editions.png`, `greeter.png`.

La tipografía, el ritmo y el chrome Signal del sitio son excelentes (titular en
Plex Sans Condensed, tira de telemetría, bilingüe, selector de tema de tres
vías). Pero la única imagen de escritorio de la home y de la tarjeta OG por
defecto es una captura de terminal `btop and yazi` fechada 2026-10-25 y
rotulada `PREVIEW · PREVIOUS APPEARANCE`; no hay Cockpit, ni popout, ni
dashboard ni deck en ninguna tarjeta social. A 1920x1080 el hero ocupa el 55 %
izquierdo y el 45 % derecho es espacio de línea fina muerto; la imagen del
producto queda debajo del pliegue. Para un lanzamiento de nivel r/unixporn el
sitio debe abrir con el escritorio. Tarjetas OG: el titular y el cuerpo están
separados por ~120 px de espacio vacío, la marca Hornero mide unos 20 px, y
`Greeter` es una recreación en navegador rotulada `NOT A SCREENSHOT`.

**Dirección del arreglo.** Usar una escena de VM con guion (escenario qa
`showroom/signal-hero`) para producir los activos del hero y de OG; regenerar
primero los datos de producto desde los mains de Signal.

**No verificado.** Sitio de producción en vivo; todas las páginas salvo home,
editions, download, gaming, install; sitio de documentación; búsqueda; 404.

### VA-21 (P2)

Defecto: El sitio de documentación y las páginas de cola larga no tienen
evidencia visual

- **Superficie** — Sitio de documentación, temas, fondos, layouts, showroom,
  extensiones, compañero, terminales, versiones, búsqueda, 404
- **Puertas** — Completitud, Accesibilidad, Rendimiento
- **Issue** — [website#234](https://github.com/HorneroOS/website/issues/234)
- **Evidencia**
  - `HorneroOS/website` `.github/evidence/` contiene capturas de home,
    editions, download, gaming, install y de un rediseño más viejo; ninguna de
    `/docs`, `/search`, `/layouts`, `/themes`, `/showroom`, `/companion`,
    `/terminals`, `/releases`.

El sitio de documentación es donde aterrizan los contribuyentes y los lectores
de unixporn después del hero, y no se capturó para nada en la era Signal. Los
bloques de código, tablas, barra lateral, resultados de búsqueda, admoniciones y
las 16 tarjetas de layout están sin verificar a 360, 768, 1280 y 1920 en ambos
modos de color.

**Dirección del arreglo.** Agregar un script de barrido con Playwright
(`scripts/capture-evidence.mjs`) que recorra el sitemap y escriba el conjunto.

**No verificado.** Todo lo anterior.

### VA-22 (P2)

Defecto: El texto de los widgets propios filtra detalles de implementación;
fixtures y regiones vacías en la evidencia

- **Superficie** — Widgets de plugins, popovers, entradas del catálogo
- **Puertas** — Excelencia visual, Consistencia, Usabilidad
- **Issue** — [plugins#71](https://github.com/HorneroOS/plugins/issues/71)
- **Evidencia**
  - Local de la misión
    `evidence/plugins/batch3-time/hornero-calendar.desktop.night.png`,
    `hornero-quick-notes.dashboard.night.png`,
    `hornero-world-clock.dashboard.day.png`,
    `batch5-widgets/hornero-system-insight.desktop.day.png`,
    `hornero-audio-deck.desktop.night.png`,
    `hornero-weather.dashboard.night.png`.

Los widgets comparten bien el vocabulario Signal (eyebrows de canal, pozos,
medidores segmentados), lo cual es un logro real. Problemas restantes: Calendar
dice "No calendar events source is available to extensions yet; this widget
shows dates only."; Quick Notes termina con un párrafo de 4 líneas (`Saved
automatically via Settings; restored when this extension loads again. Disabling
flushes any pending edit ...`); World Clock termina con un párrafo de
descargo de DST más alto que los datos; Weather deja vacío el 40 % de su
tarjeta; los numerales del calendario son de 22 px en negrita mientras que el
calendario del dashboard usa 14 px; el trazo de CPU de System Insight en la
evidencia Day es una onda senoidal (datos de fixture), lo que contradice la
regla de datos reales y confundiría a cualquiera que lo use como referencia; la
evidencia del audio deck muestra `Fixture Artist · Fixture Album` y `Fixture
Speakers`.

**Dirección del arreglo.** Mover las notas de limitaciones al `notes` del
manifiesto, mostrado en el catálogo; agregar un chequeo de CI de `plugins` que
falle cuando `Fixture` aparece en los datos fuente de las capturas; recortar los
rellenos mediante un componente `Card` compartido.

**No verificado.** Superficies de popover/menú de las extensiones; panel
Marketplace con catálogo en vivo (muestra 0 instaladas en todas las capturas);
orientación (rieles).

### VA-23 (P2)

Defecto: El lenguaje visual todavía especifica barras de 36/30 px y ejemplos de
radio de 3 px; las barras finas entregadas son de 28/24 px con un factor de
densidad

- **Superficie** — Docs (signal-visual-language.md secciones 4, 7, 14; enmienda
  del RFC)
- **Puertas** — Consistencia, Completitud
- **Issue** — [docs#124](https://github.com/HorneroOS/docs/issues/124)
- **Evidencia**
  - `HorneroOS/shell` `.github/evidence/thin-bars/README.md` y
    `after-cockpit-1080-offscreen.png` (arriba 28 px, abajo 24 px); `docs`
    `development/signal-visual-language.md` secciones 4.1 y 14.1.

La implementación pasó a barras finas (shell#517-#520) con
`Density.screenHeight`; la autoridad de diseño todavía dice riel de 36 px y
tira de 30 px y el ítem abierto 16 menciona 40/32. Los revisores que usen el
documento como contrato van a marcar mal las barras entregadas, y los números
nuevos (y los tamaños a 720/768/960) no tienen dónde vivir.

**Dirección del arreglo.** PR solo de docs después de que se mergee la
auditoría de calidad visual; tabla de preset x altura lógica.

### VA-24 (P1)

Defecto: Los escenarios visuales capturan un fondo vacío a 1280x800; faltan
contenido real, popouts, resoluciones y números

- **Superficie** — Escenarios y evidencia de la VM de QA
- **Puertas** — Completitud, Rendimiento, Accesibilidad
- **Issue** — [qa#88](https://github.com/HorneroOS/qa/issues/88)
- **Evidencia**
  - Cada ejecución bajo `~/.local/share/hornero/qa/runs/20261117T02*`..`T03*`
    (`layouts-gallery-*`, `wallpapers-ink-*`, `experience-mode-*`): 1280x800,
    sin ventanas, sin popout, barras de 52/46 px (pre-finas).
  - `docs/evidence/signal-vm-20261117/README.md` lista 14 cuadros; ninguno
    muestra un escritorio poblado.

La galería de VM juzga las barras contra un fondo de grilla tipo plano con un
pájaro, sin ninguna ventana detrás, de modo que no se puede evaluar la
alineación entre contenido y barra, el blur/la transparencia, los bordes y
espacios de las ventanas ni la relación entre el radio de la barra y el de la
ventana. La resolución es una sola (1280x800) mientras que la especificación y
la evidencia de barras finas piden 1366x768, 1920x1080, 2560x1440 a 1.25x,
3840x2160 a 2x. Solo una captura Day y ninguna de Alto Contraste. No se
registra ningún número de tiempo de cuadro ni de CPU en reposo aunque el
lenguaje visual (11.4) los exige. Las ejecuciones previas a las 01:31 son
imágenes pre-barras finas; se las está leyendo como actuales.

**Dirección del arreglo.** Extender el esquema de escenarios con `windows:` y
`popout:`; reutilizar la alarma de evidencia desactualizada de qa#17.

**No verificado.** N/A (este issue es el plan de cobertura).

## Qué no se verificó

No existe captura real de lo siguiente. Cada ítem es una brecha de calificación,
no un aprobado.

- **Movimiento**: morph de popout, stagger, tooltip, launcher, barrido del
  dashboard, reflujo de notificaciones, deslizamiento de workspace, cambio de
  layout, revelado del bloqueo, movimiento reducido. No se capturó nada animado
  en ningún lado.
- **Popouts anclados en el host** (VA-11) y con ventanas reales detrás.
- **Glow, scanlines y persistencia** en modo Signal (shell#511, VA-06).
- **Day y Alto Contraste en ventanas reales** para cualquier superficie salvo el
  cuadro de VM de Cockpit; texto grande y movimiento reducido en el host.
- **Escala y resolución**: 1366x768 más allá del offscreen de Cockpit,
  2560x1440 a 1.25x, 3840x2160 a 2x, ultrawide; popouts con escala fraccionaria
  más allá de los cuadros de VM a 1.5x.
- **Multimonitor** con distinta escala y barras por salida en el host (solo hay
  ejecuciones de VM con imágenes de octubre).
- **Modos de experiencia** Focus, Gaming y Studio en la imagen actual: las
  ejecuciones existen pero no se releyeron contra la especificación después de
  las barras finas.
- **Chromatic** (RFC 0002) colores, previews y plantillas: en curso.
- **UI de chat del Compañero**, voz, aprobaciones.
- **Popovers y menús contextuales de plugins**; el Marketplace con un catálogo
  en vivo.
- **Greeter en un display SDDM real** con video; **páginas del instalador**
  distintas de la puerta de memoria; **sitio de documentación y 8+ rutas del
  sitio web**.
- **Navegador de fondos** con el catálogo entregado (solo se vieron los archivos
  propios del host).
- **Rendimiento**: CPU en reposo, tiempo de cuadro, entrada al primer cuadro de
  cualquier superficie.
- **Paneles VPN, Entrada, Atajos y Captura** en hardware real.
- **El token 'ST'** y el significado de los glifos de la tira inferior en el
  build en ejecución.
- **Anomalías offscreen**: en `thin-bars/after-cockpit-1080-offscreen.png` faltan
  la marca y el numeral del workspace activo; los cuadros de VM y del host
  muestran ambos, así que esto se lee como una brecha del arnés, pero no está
  probado.

La lista de verificación completa de capturas está en el issue de seguimiento.

## Fortalezas que vale la pena mencionar

Cosas específicas que deberían sobrevivir a cualquier refactor: la numeración
de canal por superficie (`01 · STATION`), las líneas de cota debajo de los
medidores particionados, el sistema de eyebrows `NOTE`/`WARNING`/`ERROR`, la
cinta de franjas del día del greeter, el reloj condensado del bloqueo con su
regla ámbar, los pozos de lectura hundidos, los estados vacíos honestos con
guion largo, los bordes de estado de 1 px en las notificaciones y los radios
Bezel finos.
