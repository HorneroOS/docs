# Signal Visual Language

> Traducción al español rioplatense de la
> [versión en inglés](../../development/signal-visual-language.md), que es la
> canónica.

- **Estado** — Dirección aceptada (2026-11-16) para
  [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md), enmienda 1
- **Seguimiento** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)
- **Audiencia** — ingenieros QML (shell, PluginKit, extensiones),
  colaboradores de temas y marca, revisores

Este documento convierte la dirección creativa de la RFC en reglas concretas:
anatomía de barra, indicador de espacios de trabajo, medidores, encuadre de
paneles, estados, detalles luminosos y de fósforo, coreografía de movimiento,
Cockpit Clear y la dirección artística de cada preset de layout. La RFC sigue
siendo la autoridad para nombres de tokens, familias tipográficas, la API de
glifos, nombres de movimiento y el contrato de superficies ancladas. Este
documento solo usa esos contratos; donde propone un cambio lo indica y ese
cambio necesita primero una enmienda a la RFC.

> **Toda imagen referenciada en este documento era un render conceptual**,
> armado como espécimen HTML/CSS y renderizado headlessly con Playwright a
> 1920×1080. No son capturas de producto y muestran valores de ejemplo, no
> telemetría en vivo. Cada imagen llevaba una etiqueta "CONCEPT RENDER". La
> evidencia de producto proviene de capturas en host bajo RFC §7.1.

## 1. Base de investigación

Siete observaciones dieron forma a las reglas de abajo. Los diseños se
estudiaron por sus principios, no se copiaron.

1. **Los escritorios fuertes muestran poco y lo tipografían bien.** Los skins
   mínimos de Rainmeter se centran en un reloj, fecha y unas pocas lecturas de
   sistema, mantienen una paleta monocroma que se adapta al fondo y podan
   módulos agresivamente ([resumen][ref-rainmeter]). Los scripts longevos de
   anillos de Conky (*Rings* de londonali1010, *Seamod* de SeaJey) funcionan
   porque cada anillo está rotulado y comparte un acento ([Rings][ref-rings],
   [Seamod][ref-seamod]).
2. **Las barras intencionales codifican estado de espacios de trabajo, no
   decoración.** Los módulos de espacios de trabajo de Waybar exponen estados
   distintos activo, visible, vacío y urgente como ganchos de estilo
   ([waybar-sway-workspaces(5)][ref-waybar-man],
   [configuración de Waybar][ref-waybar-wiki]). Las mejores configuraciones le
   dan a cada estado su propio tratamiento visible que no depende solo del
   color.
3. **La UI ficticia se apoya en ingeniería real, pero optimizada para una
   audiencia.** Territory Studio investiga pantallas militares e industriales
   reales antes de inventar interfaces para cine, y dice que el objetivo de
   los gráficos en pantalla es explicar información de un vistazo al espectador
   ([entrevista en Pushing Pixels][ref-territory]). Tomamos la base real
   (retículas, etiquetas de canal, medidores segmentados) y rechazamos la
   densidad, porque una persona operadora usa esto durante horas.
4. **Cyberpunk 2077 muestra qué evitar tanto como qué conservar.** Una crítica
   detallada señala elementos decorativos que comparten el rojo funcional, un
   mapa monocromo que no separa zonas, pestañas que se mueven y rompen la
   memoria espacial y marcadores animados que roban atención; elogia
   elementos HUD contextuales que aparecen solo cuando son relevantes
   ([Interface In Game][ref-cp-iig], [charla GDC 2023][ref-cp-gdc]).
5. **Demasiados tratamientos tipográficos por pantalla se leen como ruido.** La
   UI de "realismo gráfico" de *Marathon* de Bungie fue criticada como
   "fontslop": demasiadas fuentes, pesos, tamaños y espaciados en una página
   ([Creative Bloq][ref-marathon-cb], [PC Gamer][ref-marathon-pcg]).
6. **Una restricción de época vuelve coherente a un retrofuturo.** *Alien:
   Isolation* limitó su tecnología a lo que podía existir en el set de 1979, lo
   que produjo una estética "lo-fi sci-fi" consistente
   ([Engadget][ref-alien]). Nuestra restricción: solo lo que un fabricante
   argentino de instrumentos de unos 1990 alternativos podría construir —
   segmentos, retículas, pozos, canales rotulados — sin hologramas, vidrio ni
   partículas.
7. **Los gráficos de broadcast mantienen legible el texto sobre imagen móvil
   con sobriedad.** La práctica de lower-thirds usa una línea primaria corta,
   una línea secundaria más chica, áreas seguras y una sombra o respaldo sutil
   detrás del tipo sobre material cargado ([StudioBinder][ref-lt-sb],
   [Frame.io][ref-lt-frame]). Cockpit Clear toma prestada la sombra solo en
   los glifos, no el respaldo.

## 2. Tres direcciones y la elección

Las tres direcciones usan los roles de la RFC, IBM Plex y glifos derivados de
Tabler. Cada una se armó como un espécimen Cockpit completo: barra doble sobre
un fondo licenciado de HorneroOS (Buenos Aires Nocturno, Luis Argerich, CC BY
2.0), un popout de audio abierto anclado a su disparador, medidores
segmentados, un indicador de espacios de trabajo, un panel de instrumentación y
un espécimen tipográfico.

### 2.1 A — Bezel

Placas frontales de instrumentos montadas en rack. Las barras son placas mate
`base` divididas en módulos por líneas finas cortas; los números cambiantes
se ubican en pozos de lectura `sunken`; el panel de instrumentación es un
osciloscopio con retícula y traza `phosphor`. El ámbar marca solo lo vivo.

*Render conceptual quitado (2026-11-20): Render conceptual: dirección A, Bezel.
Capturas reales: [Showroom](https://horneroos.com/showroom/).*

### 2.2 B — Carta

Una lámina de dibujo técnico. Las celdas de barra se leen como un rótulo
(epígrafe sobre valor), los espacios de trabajo van sobre una regla con un
triángulo índice ámbar, los paneles son hojas de grilla de puntos con líneas de
cota y rótulo, y una línea guía celeste une el popout con su disparador.

*Render conceptual quitado (2026-11-20): Render conceptual: dirección B, Carta.
Capturas reales: [Showroom](https://horneroos.com/showroom/).*

### 2.3 C — Transmisión

Una sala de control de transmisión. Barras oscuras `ground`, reloj grande
condensado con segundos, espacios de trabajo con lámpara testigo y brillo
ámbar suave, un indicador "MIC LIVE", tiras de canal de consola con tiras
rotuladas en el popout de audio y un panel multivista de telemetría con
etiquetas programa/previa.

*Render conceptual quitado (2026-11-20): Render conceptual: dirección C,
Transmisión. Capturas reales: [Showroom](https://horneroos.com/showroom/).*

### 2.4 Comparación

Los puntajes van de 1 (pobre) a 5 (fuerte), juzgados sobre renders 1:1.

| Criterio | A Bezel | B Carta | C Tx |
| --- | --- | --- | --- |
| Legibilidad de un vistazo | 5 | 3 | 4 |
| Distinto de Caelestia/Material | 4 | 5 | 4 |
| Comodidad todo el día | 5 | 3 | 3 |
| Costo QML (GPU, complejidad) | 5 | 3 | 4 |
| Escala entre modos | 5 | 3 | 4 |
| Calidad de tema día | 4 | 5 | 2 |
| WOW a primera vista | 4 | 4 | 5 |

- **A — Bezel** es la más legible y económica: rectángulos, líneas finas y un
  trazo `Shape` por onda. Su riesgo es leerse como un dashboard plano; el
  osciloscopio, los pozos y la muesca le dan carácter propio, y tiene el
  camino más claro desde Focus (despojar todo) hasta Signal (osciloscopio,
  fósforo, glow).
- **B — Carta** es la más original y la mejor a luz del día, pero las celdas de
  dos líneas empujan epígrafes a 10 px (debajo del `small 11` de la RFC), la
  grilla de puntos cansa detrás de texto denso y la línea guía suma un tercer
  elemento entre disparador y popout.
- **C — Transmisión** es la más cinematográfica, pero el glow testigo en el
  espacio activo está siempre encendido, los testigos rojos chocan con la
  semántica de `alert`, y la tira de barras de color es decoración. Sirve para
  momentos Gaming y Studio, no para ocho horas de código.

**Elegida: Signal Bezel (A), refinada con dos préstamos.** De B, líneas de cota
para cantidades particionadas (memoria usada/caché, disco). De C, tiras de
canal de consola para el popout de audio en modo Studio y el chip on-air,
reformulado en `signal` porque RFC §2 ya define ámbar como *en vivo*. La tira
de barras de color, la regla de espacios de trabajo, las grillas de puntos y
los segundos en el reloj de barra no se arrastran.

### 2.5 Especímenes finales

Signal Night, modo Everyday, paleta final (§3):

*Render conceptual quitado (2026-11-20): Render conceptual: dirección final,
Signal Night. Capturas reales: [Showroom](https://horneroos.com/showroom/).*

Signal Day sobre Patagonia (Perito Moreno, ThartmannWiki, CC BY-SA 4.0):

*Render conceptual quitado (2026-11-20): Render conceptual: dirección final,
Signal Day. Capturas reales: [Showroom](https://horneroos.com/showroom/).*

## 3. Cambios de paleta y contraste

Las paletas insignia de la RFC pasan AA sobre `base`, `panel` y `raised`, que
es lo que afirma la RFC. Este lenguaje pone números en pozos `sunken` y dibuja
límites `ruleStrong` sobre tooltips `lifted`, donde algunos roles fallan.
Cambios de valor propuestos, para que W1 (config) los adopte mediante una
enmienda a la RFC:

| Tema | Rol | RFC | Propuesto |
| --- | --- | --- | --- |
| Night | `ruleStrong` | `#66707B` | `#707A85` |
| Day | `ruleStrong` | `#857F73` | `#736D62` |
| Day | `signal` | `#9A5100` | `#8F4B00` |
| Day | `cue` | `#1D6894` | `#1A5F88` |
| Day | `focus` | `#1D6894` | `#1A5F88` |
| Day | `phosphor` | `#2A7341` | `#256A3B` |
| Day | `alert` | `#B0371F` | `#A8341C` |

Contraste mínimo de cada rol en las seis superficies (`ground`, `sunken`,
`base`, `panel`, `raised`, `lifted`), calculado con la fórmula de luminancia
relativa WCAG 2.x:

| Tema | Rol | Valor | Mín | Peor sup. | Mín RFC |
| --- | --- | --- | --- | --- | --- |
| Night | `ink` | `#ECE6DA` | 10.75 | lifted | igual |
| Night | `inkMuted` | `#A8ABAD` | 5.78 | lifted | igual |
| Night | `ruleStrong` | `#707A85` | 3.06 | lifted | 2.65 |
| Night | `signal` | `#F2A33A` | 6.41 | lifted | igual |
| Night | `cue` | `#7EC1EA` | 6.81 | lifted | igual |
| Night | `phosphor` | `#8BD49A` | 7.62 | lifted | igual |
| Night | `alert` | `#F0705A` | 4.56 | lifted | igual |
| Day | `ink` | `#1B1E22` | 11.55 | sunken | igual |
| Day | `inkMuted` | `#4E545B` | 5.28 | sunken | igual |
| Day | `ruleStrong` | `#736D62` | 3.54 | sunken | 2.75 |
| Day | `signal` | `#8F4B00` | 4.57 | sunken | 4.08 |
| Day | `cue` | `#1A5F88` | 4.77 | sunken | 4.19 |
| Day | `phosphor` | `#256A3B` | 4.53 | sunken | 4.00 |
| Day | `alert` | `#A8341C` | 4.57 | sunken | 4.25 |

Pares que cambian con la propuesta, tema Day: `onSignal` `#FFFFFF` sobre
`signal` 6.62; `onCue` sobre `cue` 6.92; `#FFFFFF` sobre `phosphor` 6.56;
`onAlert` sobre `alert` 6.62; `signal` sobre `signalWell` 5.03. En Night,
`onSignal` sobre `signal` sigue en 8.90.

`inkFaint` sigue siendo solo decorativo (mínimo Night 3.04, Day 2.76). Nada en
este lenguaje lo usa para texto que una persona necesite leer, incluido el
contexto de encabezado de popout, que usa `inkMuted`.

### 3.1 Rol propuesto: `glow`

Se propone un nuevo rol para el acento luminoso (§9): `glow` = `#FFB650` en
Night (7.67:1 sobre `lifted`, 10.65:1 detrás de `onSignal`), e igual a `signal`
en Day, donde nunca se renderiza glow. Es un color de emisión para halos,
nunca un color de texto ni relleno. Hasta que la RFC lo sume, las
implementaciones usan `signal` (o `phosphor` para trazas) con los límites de
alfa en §9; nada en este documento depende de que el rol exista.

## 4. Anatomía de barra

Todos los valores son píxeles lógicos a escala 1 en la grilla de 4 px de la
RFC.

### 4.1 Barras horizontales

> Los tamaños de esta sección son los objetivos originales. Los tamaños
> publicados y calibrados están en la sección 4.4 y tienen prioridad.

- **Riel superior (actuar)** — 36 px de alto, relleno `base`. Estilo inset:
  6 px desde los bordes de pantalla, borde 1 px `rule`, radio `small` (3).
  Estilo pegado (attached): sin borde exterior, 1 px `rule` solo en el borde
  interno.
- **Tira inferior (saber)** — 30 px de alto, pegada, relleno `base`, 1 px
  `rule` en el borde interno (superior), radio 0.
- **Grupos** — inicio, centro, fin. El grupo central se centra en la pantalla,
  no entre sus vecinos, para que el reloj nunca se mueva cuando cambian los
  módulos.
- **Segmento** — la unidad de composición. Relleno horizontal 12, brecha interna
  8 entre glifo, etiqueta y valor, todo el alto de la barra como área de clic.
- **Separadores** — línea de 1 px `rule` entre segmentos, metida 8 px desde
  los bordes superior e inferior (20 px de alto en un riel de 36 px). Sin
  separador dentro de un grupo de íconos: los ítems adyacentes solo-ícono
  (Wi-Fi + Bluetooth, acciones rápidas, bandeja) forman un segmento con 12 px
  de separación.
- **Glifos** — Hornero Glyphs de 18 px en `ink`; grupos secundarios (acciones
  rápidas, bandeja) en `inkMuted`.
- **Etiquetas** — estilo eyebrow dentro de barras: IBM Plex Mono 11,
  mayúsculas, tracking +8 %, `inkMuted`, a lo sumo cuatro caracteres (`OUT`,
  `BRI`, `CPU`, `MEM`, `TMP`). Hay etiqueta solo cuando el glifo no se explica
  solo o el ajuste de densidad es `values`.
- **Valores** — IBM Plex Mono 12, cifras tabulares, `ink`. Los valores que
  ajusta la persona (volumen, brillo) van en un **pozo de lectura**: relleno
  `sunken`, borde 1 px `rule`, radio 3, relleno 1 × 6, 18 px de alto. Los
  valores de solo lectura (CPU, memoria) no llevan pozos.
- **Reloj** — IBM Plex Sans Condensed Medium 18 en el riel, fecha en Plex Mono
  12 mayúsculas `inkMuted`, 8 px aparte. Sin segundos en barras.
- **Marca** — marca simbólica Hornero, 20 px, en `signal`. Es el disparador
  del lanzador y el único ítem permanentemente ámbar.
- **Chip on-air** — indicadores de micrófono, cámara, pantalla compartida y
  grabación: Plex Mono 11 SemiBold mayúsculas `onSignal` sobre relleno
  `signal`, radio 3, relleno 4 × 6. Estático. Se muestra solo mientras la
  captura es real y activa.
- **Hover/presión** — relleno de todo el segmento, ver §8.

### 4.2 Rieles verticales

Los rieles izquierdo y derecho (Hornero Left/Right, Minimal Left) rotan la
anatomía:

- Grosor 40 px (Hornero) o 32 px (Minimal). Los segmentos se apilan con 8 px
  de relleno vertical y separadores horizontales metidos 8 px desde cada lado.
- El texto nunca rota salvo el título de ventana activa en Hornero Left/Right,
  que conserva su título vertical inspirado en Caelestia; usa Plex Sans 13 y
  trunca con puntos suspensivos.
- Los valores se apilan debajo de su glifo (glifo 18, valor Plex Mono 11).
- La barra on-air se ubica en el borde que mira al contenido (borde derecho de
  un riel izquierdo, borde izquierdo de un riel derecho).

### 4.3 Densidad

El ajuste existente `density` mapea a: `icons` (solo glifo, etiquetas y
valores en tooltips), `values` (glifo y valor, etiquetas ocultas), `labels`
(glifo, eyebrow y valor). Cockpit trae `values`; el modo Signal puede subir a
`labels`, Focus baja a `icons`.

### 4.4 Tamaños calibrados (publicados)

La primera pasada de barras finas (`shell#520`) dejó cada barra en 24 a 28 px
con texto de 11 px y se leía apretada. Los valores calibrados reemplazan los
objetivos 36/30 de arriba y el 40/32 del ítem abierto 16; son el contrato que
publica la shell (`presets/*.json`, `tests/test_thin_bars.py`). El grosor es el
cuerpo de la barra; el margen es la distancia extra al borde de pantalla para
estilos inset, floating, islands y dock.

- Las barras horizontales son de 26 a 34 px (Cockpit 34 arriba y 26 abajo,
  ambas inset por 6 px; Classic 32; Minimal 30). Hornero Left/Right conservan
  un riel generoso de 48 px, Minimal Left 38 px, el dock Console 46 px con
  mosaicos de app de 28 px.
- Cada placa lleva una línea fina de 1 px `rule` (en todo el contorno para
  inset, floating e islands; solo en el borde interno para attached). Los
  radios son de a lo sumo 4 px; nada es vidrio translúcido.
- Factor de densidad: la altura lógica `h` da `f = 0.94 + 0.06 x (h - 720) /
  360` hasta 1080 px y `f = 1 + 0.10 x (h - 1080) / 1080` por encima (máximo
  1.10), por el multiplicador del usuario 0.75 a 1.5. El texto primario es
  12 px (nunca menor), epígrafes 11 px, íconos de barra 15 a 18 px, relleno de
  segmento 12 px (8 px en rieles, piso 8 y 6), y ninguna barra es más fina que
  el área táctil de 24 px. La altura lógica ya divide por la escala del
  compositor, así que 1920×1080 a 1.5 es 720p.
- Disciplina cromática: primeros planos `ink` e `inkMuted`, un acento `signal`
  (marca, espacio de trabajo activo, chip de modo, chips on-air, interacción
  viva); el reloj es de un solo color; los íconos de bandeja son monocromos
  por defecto.

Grosor en px por altura lógica (redondeado; piso 24):

<!-- markdownlint-disable MD013 -->

| Preset | Estilo | Margen | 720p | 768p | 960p | 1080p | 1440p | 2160p |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cockpit top / bottom | inset | 6 | 32 / 24 | 32 / 25 | 33 / 25 | 34 / 26 | 35 / 27 | 37 / 29 |
| Cockpit Clear | inset | 6 | 32 / 24 | 32 / 25 | 33 / 25 | 34 / 26 | 35 / 27 | 37 / 29 |
| Horizon top / bottom | inset | 6 | 30 / 24 | 30 / 25 | 31 / 25 | 32 / 26 | 33 / 27 | 35 / 29 |
| Classic Top / Bottom | attached | 6 | 30 | 30 | 31 | 32 | 33 | 35 |
| Minimal Top | attached | 6 | 28 | 28 | 29 | 30 | 31 | 33 |
| Minimal Float | floating | 8 | 28 | 28 | 29 | 30 | 31 | 33 |
| Floating Island | floating | 10 | 32 | 32 | 33 | 34 | 35 | 37 |
| Islands | islands | 8 | 30 | 30 | 31 | 32 | 33 | 35 |
| Productivity | inset | 6 | 30 | 30 | 31 | 32 | 33 | 35 |
| Studio | attached | 6 | 30 | 30 | 31 | 32 | 33 | 35 |
| Gaming | floating | 8 | 26 | 27 | 27 | 28 | 29 | 31 |
| Dock Bottom | dock | 8 | 43 | 44 | 45 | 46 | 48 | 51 |
| Hornero Left / Right | attached | 6 | 45 | 46 | 47 | 48 | 50 | 53 |
| Minimal Left | attached | 6 | 36 | 36 | 37 | 38 | 39 | 42 |

<!-- markdownlint-enable MD013 -->

Evidencia de producto: HorneroOS/shell `.github/evidence/layouts-calibration/`
(tiras antes/después offscreen en 1080, 768 y 720). Los renders conceptuales
conservan su etiqueta CONCEPT y no son evidencia de producto.

## 5. Indicador de espacios de trabajo

El indicador de espacios de trabajo es una fila de celdas fijas — nunca
píldoras, nunca puntos que cambian de tamaño.

- **Celda** — 30 × 30 px en la tira inferior (30 × 36 en riel superior,
  40 × 30 en riel vertical), numeral en Plex Mono 12 Medium, centrado.
- **Vacío** — numeral en `inkMuted`, sin marca. Se muestra solo para el rango
  persistente (por defecto 1–9) o cuando el compositor lo informa.
- **Ocupado** — numeral en `inkMuted` más una marca de ocupación de 4 × 2 px
  en `inkMuted`, a 4 px del borde alejado del contenido.
- **Activo** — numeral en `ink`, relleno de celda `raised` y la barra on-air:
  una barra `signal` de 2 px en todo el ancho de la celda sobre el borde que
  mira al contenido (borde superior en tira inferior, borde inferior en riel
  superior, borde interno en rieles).
- **Visible en otro monitor** — numeral en `ink`, trazo `ruleStrong` de 1 px
  en el mismo borde que la barra on-air, sin relleno.
- **Urgente** — numeral y marca en `alert`. Sin parpadeo; el estado persiste
  hasta visitar el espacio de trabajo.
- **Especial/scratchpad** — una celda rotulada `S` después de un separador de
  1 px `rule`.
- **Hover** — relleno `raised`; el tooltip lista las ventanas de ese espacio.
- Cada estado difiere en al menos dos de: color de numeral, relleno, marca,
  barra. El color nunca es la única señal.

## 6. Medidores, indicadores y telemetría

### 6.1 La regla de datos reales

Solo se dibuja telemetría real. Un medidor, sparkline, osciloscopio o lectura
se enlaza a un servicio nativo de la shell o a un proveedor declarado de
PluginKit (RFC §5b). Cuando falta una fuente, el instrumento muestra una raya
em en `inkMuted`, todos los segmentos apagados y un tooltip que nombra qué
falta. Sin ondas de relleno, sin animación en reposo, sin muestras
interpoladas más allá de una línea recta entre dos muestras reales y sin
"actividad" inventada. Cada gráfico declara su ventana y escala en un eyebrow
(`CPU · 10 %/DIV`, `60 S WINDOW`).

### 6.2 Medidor segmentado

- Segmento de 3 × 10 px en barras, 3 × 12 en paneles, brecha de 2 px, esquinas
  cuadradas.
- Cantidad: 8 (recursos en barra), 10 (ajustables en barra), 12 (filas de
  stream), 24–32 (filas de panel), 12–14 vertical (por núcleo).
- Segmentos apagados `rule`; segmentos encendidos `ink`; segmentos sobre el
  umbral `signal` (85 % para niveles, 80 % para temperatura del valor crítico);
  `alert` solo por encima de un umbral crítico real informado por el sensor.
- Los vúmetros verticales (VU) en paneles usan `phosphor` para segmentos
  encendidos — el único lugar donde verde significa "nivel", siguiendo
  convenciones de vúmetros de hardware.
- Picos de audio: los segmentos atacan al instante y sueltan 1 segmento cada
  30 ms; marcador de retención de pico por 1.5 s, ambos desde datos de pico de
  PipeWire.
- El valor numérico siempre va al lado del medidor en cifras tabulares de
  Plex Mono. Un medidor nunca aparece solo.

### 6.3 Lecturas

Las lecturas grandes (dashboard, widgets) usan Plex Sans Condensed Medium
22–28 para el número y Plex Mono 13 `inkMuted` para la unidad, dentro de un
pozo `sunken` con borde de 1 px `rule` y una etiqueta eyebrow arriba.

### 6.4 Sparklines y osciloscopio

- **Sparkline** — en línea, 18–24 px de alto, trazo de 1.5 px, `cue` para red,
  `phosphor` para carga, `signal` para temperatura. Sin relleno bajo la línea,
  sin ejes, el valor actual impreso al lado.
- **Scope** — el instrumento insignia. Pozo `sunken`, radio 3, borde 1 px
  `rule`; retícula de 10 × 4 divisiones en `rule`, línea central punteada 2/3;
  una traza `phosphor` de 1.5 px. La traza de la ventana anterior se dibuja al
  22 % de opacidad como **persistencia** (datos reales, de una ventana atrás).
  Glow y scanlines siguen §9–§10.
- **Particiones** — memoria y disco usan una sola barra dividida en
  usado/caché/libre (relleno `ink`, `inkFaint`, vacío) con una línea de cota
  debajo: línea de 1 px `inkFaint`, marcas finales de 9 px, etiquetas en Plex
  Mono 11 `inkMuted` sobre un corte `panel`. Las particiones muestran
  proporciones, no movimiento.

### 6.5 Tasas de actualización

Tasas de proveedores compartidos: 1 Hz en Everyday, 2 Hz en modo Signal, en
pausa en Gaming salvo que un instrumento visible la necesite, y en pausa para
instrumentos en superficies ocultas o sin mapear. Los gráficos avanzan en cada
muestra sin interpolación.

## 7. Paneles y popouts

### 7.1 Encuadre

- Relleno `panel`, borde 1 px `rule`, radio `small` (3). `large` (8) solo para
  láminas a pantalla completa como la grilla del lanzador y el menú de sesión.
- **Popouts pegados** (abiertos desde una barra) apoyan al ras del borde
  interno de la barra y omiten el borde de ese lado. Una **muesca** — una
  línea `signal` de 2 px exactamente del ancho del disparador — corre por el
  borde pegado bajo el disparador, continuando el subrayado de estado abierto
  del disparador. Así es como la superficie nace visiblemente de su disparador
  con las animaciones apagadas.
- **Popouts flotantes** (desde barras floating, island o dock) conservan un
  hueco de 4 px y los cuatro bordes; la muesca se dibuja en el borde que mira
  al disparador.
- **Chaflán mecanizado (machined fillet)** — donde un popout pegado o cajón
  encuentra la barra o el marco, un pequeño arco cóncavo de cuarto de círculo
  (radio `border.fillet`, por defecto 6, 0 = unión cuadrada al ras) deja que la
  superficie crezca desde el bisel, como fresada de la misma placa. El `rule`
  de 1 px corre continuo desde la línea del borde del marco por el arco hasta
  el borde de la superficie. Las esquinas libres conservan radio `small`. Sin
  chaflán junto a una barra flotante o clear (aplica la regla del hueco de
  4 px) ni en un borde desnudo de pantalla sin marco ni barra. Solo arcos: sin
  shader, blob ni fusión líquida.
- **Marca de registro** — una marca `signal` de 2 × 10 px en la esquina
  superior inicial cuando la superficie tiene foco de teclado (RFC §2).
- **Encabezado** — eyebrow con número de canal opcional a la izquierda
  (`01 · AUDIO`), contexto en eyebrow `inkMuted` a la derecha. Relleno 12
  arriba, 8 abajo, 16 a los lados.
- **Filas** — altura mínima 32 px, relleno lateral 16 px, brecha 12 px.
  Secciones separadas por 1 px `rule` con márgenes de 8 px. El ítem
  seleccionado usa relleno `signalWell` con contenido `onSignalWell` y un
  eyebrow `ACTIVE`.
- **Ancho** — 320–420 px para popouts; el contenido dicta el alto hasta el alto
  utilizable de pantalla menos el margen, luego el cuerpo hace scroll (RFC
  §4).
- **Ritmo de rack** — las superficies compuestas (dashboard, popouts de barra,
  hubs del Centro de control) usan una sola cadencia: 8 entre ítems dentro de
  un módulo, 12 entre módulos, 16 de margen interno de superficie, 24 para un
  corte de sección (1 px `rule`, márgenes 8 px). Cada brecha e inserción es un
  token de espaciado o relleno, nunca un literal, y los altos de marco son
  contenido más tokens. La densidad viene del tamaño de las celdas, no de cuán
  juntas se sientan.
- **Presets de densidad** — Apariencia › Escalas ofrece Compact (0.75), Cosy
  (1.0, por defecto) y Airy (1.25). Un preset escribe juntas las escalas de
  espaciado y relleno para que el ritmo conserve sus proporciones; los
  deslizadores quedan como control fino y cualquier otro par se lee como
  Custom. Compact es el preset para pantallas de 768 px de alto.

### 7.2 Elevación

La elevación es el rol de superficie más a lo sumo una sombra:

| Nivel | Rol | Usado por | Sombra |
| --- | --- | --- | --- |
| 0 | `ground` | Escritorio, fondo de bloqueo | no |
| 1 | `base` | Barras, cuerpos de ventana | no |
| 2 | `panel` | Popouts, dashboard, widgets | sí |
| 3 | `raised` | Filas hover/elegidas, anidadas | no |
| 4 | `lifted` | Tooltips, presionados, menús | sí |

La sombra es la sombra única de la RFC: `shadow` al 35 %, 12 px de
desenfoque, 4 px de desplazamiento alejándose del borde de anclaje. Las barras
pegadas nunca proyectan sombra.

## 8. Estados de interacción

| Estado | Tratamiento |
| --- | --- |
| Reposo | Colores de rol según lo especificado |
| Hover | Relleno `raised` (sobre `base`/`panel`) |
| Presionado | Relleno `lifted`; sin escala, sin ripple |
| Abierto | Relleno `raised` + subrayado 2 px `signal` |
| Foco | Anillo 2 px `focus`, 2 px afuera, radio +2 |
| Seleccionado | Relleno `signalWell`, contenido `onSignalWell` |
| Activo | Barra on-air (2 px `signal`) borde al contenido |
| En vivo | Chip on-air (relleno `signal`, etiqueta `onSignal`) |
| Deshabilitado | Glifo `inkFaint`, sin hover; tooltip explica |

- En barras el anillo de foco se dibuja 2 px hacia adentro del segmento para
  que nunca se recorte.
- Los cambios hover y presionado usan `standard`/`quick` (90 ms); ver §11.
- El foco de teclado nunca se quita por estética y nunca se transmite con glow.

## 9. Reglas de acento luminoso

El glow existe para hacer que unas pocas cosas *en vivo* se sientan emisivas.
Está racionado.

- **Permitido en** — (1) trazas de scope y sparkline; (2) la barra on-air del
  espacio de trabajo activo y los chips on-air, solo en modo Signal. Nada más.
- **Nunca en** — texto, glifos, bordes de panel, anillos de foco, botones,
  barras, segmentos apagados de medidores ni nada decorativo.
- **Intensidad** — radio de desenfoque ≤ 4 px, color `glow` (respaldo
  `signal`; las trazas usan `phosphor`) a ≤ 40 % de alfa, sin expansión. A lo
  sumo tres ítems brillantes en pantalla.
- **Estático** — el glow nunca pulsa, respira ni sigue al cursor. Cambia solo
  cuando cambia el valor o estado subyacente.
- **Apagado** — en temas claros, Alto Contraste, modos Focus y Gaming, en
  barras Cockpit Clear, con transparencia reducida y con los niveles bajos de
  movimiento. El diseño debe estar completo sin él: cada render de este
  documento es legible quitando el glow.

## 10. Detalles de CRT y fósforo

Los detalles de fósforo pertenecen a los instrumentos, no al cromo.

- **Dónde** — dentro de pozos de osciloscopio, el panel de telemetría del
  dashboard y el reloj de bloqueo/greeter. Nunca en barras, popouts, bloques
  de texto ni ventanas de aplicaciones.
- **Persistencia** — la ventana de muestras previa al 22 % de opacidad (§6.4).
- **Scanlines** — solo en modo Signal: líneas horizontales estáticas, 1 px
  cada 3 px, `ink` al 4 % de alfa, recortadas al pozo. Apenas visibles por
  diseño.
- **Nunca** — curvatura de pantalla, parpadeo, barras rodantes, ruido,
  aberración cromática, desplazamiento glitch ni tracking VHS. Están excluidos
  por RFC §2 y por legibilidad.
- Los temas claros conservan persistencia (estética de registrador gráfico) y
  quitan scanlines y glow.

## 11. Coreografía de movimiento

El movimiento usa solo los nombres de RFC §3.6: `standard`, `enter`, `exit`,
`sweep`, `settle` (`0.32, 1.24, 0.42, 1`, 320 ms) y `settleFast`
(`0.34, 1.3, 0.5, 1`, 220 ms). Muestreada numéricamente, `settle` sobrepasa
1.9 % del recorrido y `settleFast` 3.0 %, ambas dentro del techo de 4 % de la
RFC. Las curvas settle animan posición, tamaño y forma únicamente — nunca
opacidad ni color. Para recorridos mayores a 200 px usá `enter` en su lugar,
para que el sobreimpulso nunca exceda 8 px.

**Estilos de curva.** El techo de 4 % sigue siendo el valor por defecto.
Apariencia › Aspecto › Estilo de movimiento ofrece tres personalidades
espaciales; la opacidad y el color nunca sobrepasan en ninguna:

| Estilo | `settle` | `settleFast` | Pico |
| --- | --- | --- | --- |
| Smooth | `0.32, 1.24, 0.42, 1` | `0.34, 1.3, 0.5, 1` | 1.9 % / 3.0 % |
| Snappy | `standard` | `standard` | 0 |
| Lively | `0.3, 1.4, 0.4, 1` | `0.34, 1.42, 0.5, 1` | 5.3 % / 5.8 % |

Smooth es el valor por defecto. Lively es el estilo resorte
(`appearance.anim.curveStyle: "lively"`), topeado en 6 % de sobreimpulso: una
aguja de instrumento asentándose, nunca una gelatina rebotando. La regla de
8 px de arriba aplica a todo estilo, usando el sobreimpulso de ese estilo. Sin
resortes que crucen toda la pantalla.

**Bordes delantero y trasero.** Un indicador que viaja (barra de pestaña de
dashboard, placa de espacio de trabajo) puede mover sus dos bordes por
separado: el borde hacia el destino usa `settleFast`, el borde lejano la misma
curva sobre `settleFast × trailRatio` (`appearance.anim.trailRatio`, 1.0–2.5,
por defecto 1.6), de modo que se estira hacia el destino y lo alcanza. Solo en
los niveles `full` y `standard`; `reduced` y `off` mueven ambos bordes juntos.

*Render conceptual quitado (2026-11-20): Render conceptual: guión gráfico de
apertura de popout. Capturas reales: [Showroom][showroom].*

### 11.1 Popouts desde barras (morph con origen en disparador)

1. **Marco** — un rectángulo de fondo hace morph desde el rectángulo del
   disparador (ancho del disparador, altura cero, en el borde interno de la
   barra) hacia el rectángulo final, `settle` 320 ms. Opacidad del marco 0 → 1
   con `enter` 90 ms. La muesca y la sombra viajan sobre el marco.
2. **Contenido** — las filas se revelan mediante el scan-in de la RFC: recorte
   desde el borde de anclaje, 4 px de viaje desde el lado de anclaje y fundido,
   `enter` 160 ms, escalonado 24 ms por fila empezando en 60 ms. Como máximo
   ocho filas escalonan; las filas siguientes arrancan con la octava. El
   contenido nunca se escala.
3. **Interactivo desde el cuadro 1** — la superficie acepta entrada de puntero
   y teclado de inmediato; un clic sobre una fila que todavía está apareciendo
   la activa.
4. **Cierre** — contenido y marco se desvanecen juntos con 4 px de viaje hacia
   el anclaje, `exit` 90 ms. Sin morph inverso.
5. **Cambio** entre popouts adyacentes de barra mientras uno está abierto
   (audio → red): el marco hace morph desde el rectángulo actual al nuevo con
   `settle` 320 ms; el contenido viejo se desvanece en 90 ms, el nuevo entra
   con `enter` 160 ms y sin escalonado. La superficie nunca se cierra y vuelve
   a abrir.
6. Los popouts **abiertos por hover** siguen la demora de intención de la RFC
   (120 ms) y usan `settleFast` 220 ms para el marco sin escalonado.

### 11.2 Otras superficies

- **Tooltips** — fundido con 4 px de viaje desde el anclaje, `enter` 90 ms;
  salida `exit` 90 ms. Sin morph.
- **Lanzador** — el marco hace morph desde la marca Hornero, `settle` 320 ms;
  los resultados escalonan 16 ms, como máximo seis.
- **Dashboard y cajones** (superficies grandes) — barrido de recorte `sweep`
  360 ms desde el borde de anclaje más 6 px de viaje; sin settle en la lámina
  (viaje demasiado largo). Los marcos del inicio del Dashboard entran
  escalonados 24 ms desde 60 ms, en orden de lectura; cambios de tamaño de
  contenido de pestaña y el deslizamiento de panel usan `settle`.
- **Notificaciones** — tarjeta nueva: recorte desde el borde de anclaje de la
  pila más 6 px, `enter` 160 ms; las tarjetas existentes refluyen con `settle`
  320 ms. Una tarjeta deslizada sale en la dirección de su gesto (`exit` con
  viaje = ancho de tarjeta, 240 ms). Una tarjeta vencida o cerrada conserva el
  fundido `exit` de 90 ms. De cualquier forma las tarjetas de abajo cierran el
  hueco con `settle`. Una tarjeta que expira muestra su tiempo límite como una
  línea `signal` de 2 px en su borde de anclaje que se drena con el tiempo y
  se congela mientras se pasa el cursor o se arrastra (`notifs.timeoutTick`,
  encendido por defecto). Las tarjetas críticas no expiran y no tienen línea.
  Reduced: 4 px de viaje más el fundido; off: el fundido topeado, y la línea
  avanza por cuartos.
- **OSD** (volumen, brillo) — si el segmento de barra es visible, el OSD es un
  popout desde ese segmento; si no aparece arriba de la barra inferior. `enter`
  90 ms, retención 1200 ms, `exit` 90 ms.
- **Cambio de espacio de trabajo** — la barra on-air se desliza a la celda
  nueva con `settleFast` 220 ms; los colores de numerales cambian con
  `standard` 160 ms; las marcas de ocupación aparecen en 90 ms.
- **Medidores y gráficos** — sin animación más allá de la balística VU (§6.2).
  Los numerales actualizan al instante; sin contadores rodantes.
- **Cambio de preset de layout** — las barras salientes se desvanecen `exit`
  90 ms, las entrantes entran con `sweep` 360 ms desde su propio borde. Sin
  resortes de punta a punta de la pantalla.
- **Cambio de modo de experiencia** — la densidad de instrumentación hace
  fundido cruzado `standard` 240 ms; nada se mueve.
- **Bloqueo** — el reloj se revela una vez con un recorte `sweep` sobre `scan`
  480 ms.

### 11.3 Niveles de movimiento y movimiento reducido

| Nivel | Usado por | Comportamiento |
| --- | --- | --- |
| full | Modo Signal | Todo lo de arriba |
| standard | Everyday, Studio | Todo lo de arriba |
| reduced | Focus, bajo consumo | Sin morph/stagger; 4 px + fundido |
| off | Gaming, mov. reducido | Instantáneo; fundidos ≤ 90 ms |

`appearance.reducedMotion` o la preferencia del sistema fuerza `off`, como
exige la RFC: las duraciones pasan a 0 salvo fundidos cruzados de opacidad
topeados en 90 ms. `full` y `standard` comparten tiempos; el modo Signal suma
glow y scanlines, no animaciones más largas.

### 11.4 Presupuesto de rendimiento

- 60 fps a 1920×1080 en gráficos integrados; el tiempo de render de la shell
  por cuadro queda debajo de 4 ms durante cualquier coreografía.
- Entrada a primer cuadro ≤ 16 ms: las superficies se instancian una vez y se
  alternan, no se crean al abrir.
- Animá solo la geometría del marco y la opacidad del contenido. Sin
  `layer.enabled` en barras; sin desenfoque animado en ningún lado; el glow es
  una sombra `MultiEffect` cacheada en a lo sumo tres ítems.
- Las trazas de scope son un `Shape` con un `PathPolyline` de ≤ 120 puntos.
- Medí tiempo de cuadro y entrada a primer cuadro en el host para cada
  superficie (RFC §7.1) y registrá los números con la evidencia.

## 12. Cockpit Clear

Cockpit Clear usa la anatomía Cockpit **sin ningún fondo de barra**: sin
relleno, tinte, placa, desenfoque, velo ni sombra de fondo (RFC §5.1). La
legibilidad proviene únicamente de tratamientos aplicados a los propios glifos
de primer plano.

*Render conceptual quitado (2026-11-20): Render conceptual: Cockpit Clear sobre
Iguazú. Capturas reales: [Showroom](https://horneroos.com/showroom/).*

### 12.1 Tinta adaptativa

1. Cuando cambia el fondo de pantalla o la geometría de barra (nunca por
   cuadro), muestrá la región del fondo bajo cada elemento en primer plano —
   cada glifo, etiqueta, valor, medidor y celda de espacio de trabajo, con
   2 px de margen.
2. Calculá la luminancia relativa media de la región y su desviación estándar.
3. Elegí la **polaridad** que dé el mayor contraste contra la media:
   - *light* — roles Night: `ink` `#ECE6DA`, `inkMuted` `#A8ABAD`, acento en
     vivo `#FFB650`, `alert` `#F0705A`; halo `ground` `#0C0F13`.
   - *dark* — roles Day: `ink` `#1B1E22`, `inkMuted` `#4E545B`, `signal`
     `#8F4B00`, `alert` `#A8341C`; halo `#FFFFFF`.
4. Dibujá cada glifo con un **halo** de 1 px en el color del halo al 88 % de
   alfa (un contorno de texto, no una caja). Cuando la desviación de
   luminancia de la región supera 0.12 (fondos detallados) sumá una sombra
   suave de glifo de 4 px en el mismo color.
5. Los segmentos de medidor reciben un anillo halo de 1 px; los segmentos
   apagados son la tinta de la polaridad al 30 %. Los pozos pasan a un
   contorno de 1 px en la tinta actual. El disparador abierto muestra solo su
   subrayado `signal` de 2 px.

La polaridad elige entre los roles propios Night y Day del tema; nunca deriva
colores del fondo de pantalla, lo que mantiene intacto RFC §9 ("los fondos
nunca recolorean la UI").

### 12.2 Resultados medidos

Desde el propio muestreador del espécimen (50 elementos de primer plano por
render):

| Clase de fondo | Fondo | Clara | Oscura | Detallada | Media mín |
| --- | --- | --- | --- | --- | --- |
| Detallado | Iguazú | 19 | 31 | 13 | 3.78 |
| Brillante | Quebrada | 0 | 50 | 19 | 4.15 |
| Oscuro | Buenos Aires | 50 | 0 | 1 | 5.63 |
| Alto contraste | Pampa | 50 | 0 | 0 | 5.14 |
| Mixto | Patagonia | 44 | 6 | 2 | 3.93 |

"Media mín" es el contraste más bajo entre la tinta elegida y el color medio
de la región, antes de cualquier halo. Píxeles individuales bajo un glifo
pueden coincidir con la tinta (el peor contraste por píxel alcanzó 1.01:1), por
eso el halo es obligatorio. Peor caso con el halo compuesto sobre el extremo
opuesto (halo oscuro al 88 % sobre blanco, halo blanco al 88 % sobre negro):

| Polaridad | `ink` | `inkMuted` | Acento vivo | `alert` |
| --- | --- | --- | --- | --- |
| Clara | 11.30 | 6.08 | 8.06 | 4.79 |
| Oscura | 12.67 | 5.80 | 5.01 | 5.01 |

Cada rol de texto mantiene por lo tanto al menos 4.5:1 contra su propio halo
sobre cualquier fondo.

*Render conceptual quitado (2026-11-20): Render conceptual: tiras de Cockpit
Clear sobre cinco clases de fondo. Capturas reales:
[Showroom](https://horneroos.com/showroom/).*

### 12.3 Estilos de primer plano

Seleccionable por el usuario en el Selector de layouts y Ajustes:

- **Auto** (por defecto) — §12.1 tal como está escrito.
- **Outline** — siempre el halo de 1 px y nunca la sombra suave (más nítido
  sobre fondos planos).
- **Shadow** — solo sombra suave de glifo de 2 px, para quienes no gustan de
  los contornos; cualquier elemento cuya media de contraste esté debajo de 3:1
  cae a Outline.
- **Contrast** — halo de 2 px y pesos SemiBold; para uso de Alto Contraste y
  baja visión.

Los popouts abiertos desde barras Clear son paneles Signal opacos comunes. El
glow nunca se usa en barras Clear.

### 12.4 Límites conocidos

Un único glifo montado sobre un borde duro claro/oscuro (línea de nubes de
Patagonia, rocío de Iguazú) recibe una polaridad, así que parte de él depende
del halo. Sigue legible pero se ve más cargado; el estilo Contrast o un fondo
más calmo es el arreglo. La validación en host debe cubrir al menos las cuatro
clases de arriba (RFC §7.1).

### 12.5 Notas de implementación

La grilla de luminancia puede calcularse una vez por fondo mediante el pipeline
de fondos existente (por ejemplo 96 × 54 celdas de media y desviación) y
cachearse junto al fondo procesado, de modo que la shell solo hace consultas.
En QML, el halo mapea a `Text.Outline` con `styleColor`; la sombra suave a una
sombra `MultiEffect` sobre el contenido del segmento, re-renderizada solo
cuando cambian los valores (1 Hz).

## 13. Modos de experiencia

Los modos (RFC §5a) cambian densidad, nivel de movimiento, glow y layout
preferido, no el lenguaje.

- **Focus** — layout preferido Minimal Top; densidad `icons`; movimiento
  `reduced`; sin glow, sin scanlines; solo chips on-air y espacios de trabajo
  urgentes usan `signal`; notificaciones retenidas.
- **Everyday** (por defecto) — Cockpit; densidad `values`; movimiento
  `standard`; persistencia de scope encendida, glow apagado.
- **Signal** (inmersivo) — Cockpit más widgets de instrumentación de escritorio
  (scope, VU por núcleo, red); densidad `labels`; movimiento `full`; glow y
  scanlines según §9–§10; telemetría 2 Hz.
- **Gaming** — preset Gaming; movimiento `off`; sin glow; telemetría pausada
  salvo que sea visible; la barra se oculta bajo pantalla completa y nunca toma
  foco.
- **Studio** — preset Studio; el popout de audio pasa a tiras de canal de
  consola (vúmetros verticales `phosphor`, etiquetas tipo scribble-strip con
  borde superior de 2 px del color de rol); lecturas de xrun y carga DSP solo
  cuando PipeWire las informa; movimiento `standard`; sin glow.

## 14. Presets de layout

Veredictos para cada archivo en [`shell/presets/`][shell-presets]. "Quitar"
significa borrar el archivo de preset y migrar una selección existente una
sola vez hacia el sobreviviente nombrado.

| Preset | Veredicto | Pasa a ser |
| --- | --- | --- |
| cockpit | Conservar | Insignia, defecto de fábrica |
| cockpit-clear | Conservar | Cockpit sin fondo |
| horizon | Rediseñar | Línea única de instrumentos |
| islands | Rediseñar | Tres módulos de rack |
| floating-island | Rediseñar | Módulo flotante compacto (rest.) |
| cozy-minimal | Rediseñar | Tira flotante mínima |
| dock-bottom | Rediseñar | Dock de consola |
| classic-top | Conservar | Barra única convencional |
| classic-bottom | Conservar | Variante inferior de classic-top |
| minimal-top | Rediseñar | Layout Focus, absorbe prod. |
| productivity | Rediseñar | Composición calma (restaurado) |
| minimal-left | Rediseñar | Riel de instrumentos |
| studio | Rediseñar | Layout de modo Studio |
| gaming | Rediseñar | Layout de modo Gaming |
| hornero-left | Conservar | Riel izq. inspirado en Caelestia |
| hornero-right | Conservar | Riel der. inspirado en Caelestia |

Dieciséis presets se publican; cada uno tiene una composición y un propósito
distintos. Floating Island y Productivity fueron quitados en la primera
auditoría y restaurados tras revisión, rediseñados en Signal Bezel (secciones
14.5 y 14.10).

### 14.1 cockpit — conservar

Por qué: la insignia de la RFC; arriba actúa, abajo sabe. Objetivo:

- Riel superior 36 px inset 6 px (el archivo actual usa 40 px y margen 8 —
  alinear con la RFC). Inicio: marca, acciones rápidas (captura, selector de
  layouts, ajustes), brillo (solo cuando existe luz de fondo). Centro: reloj,
  fecha, clima. Fin: chips on-air, grupo Wi-Fi + Bluetooth, audio (pozo `OUT`,
  ancla para el popout de audio), bandeja, extensiones, notificaciones, energía.
- Tira inferior 30 px pegada (actualmente 32): espacios de trabajo; centro
  ventana activa y transporte de medios; fin distribución de teclado,
  mini-medidores CPU/MEM/TMP, batería cuando hay (mover batería desde arriba a
  la derecha, según RFC §5).
- El deslizador de audio se mueve desde arriba al inicio hacia el segmento de
  audio del grupo de estado; su popout lleva los controles completos.

### 14.2 cockpit-clear — conservar

Por qué: el escritorio de barra transparente que quieren muchas personas
usuarias de Polybar, hecho legible. Objetivo: anatomía y tamaños idénticos a
Cockpit (36/30, actualmente 40/28) para que cambiar conserve memoria muscular;
§12 para todo lo demás.

### 14.3 horizon — rediseñar

Por qué: el único preset que mezcla una placa sólida con una tira clara; bueno
en pantallas chicas de laptop. Objetivo: un riel superior de 36 px inset con
módulos de actuar y saber (medidores CPU/TMP y batería se suman al grupo
final), y una línea clara de espacios de trabajo de 24 px abajo usando tinta
adaptativa §12 solo con espacios de trabajo. El clima pasa junto al reloj.

### 14.4 islands — rediseñar

Por qué: la composición multiparte de Polybar es una alternativa real a las
placas, pero el aspecto actual son islas píldora. Objetivo: tres módulos
flotantes de 36 px (inicio, centro, fin), a 10 px del borde superior, relleno
`base`, borde 1 px `rule`, radio 3 — no radio completo. La isla dueña de un
popout abierto muestra la marca de registro; los popouts mantienen un hueco de
4 px.

### 14.5 floating-island — restaurado

Por qué: las personas usuarias valoran el aspecto flotante. La píldora
vidriosa y brillante se fue (RFC §2); el preset es ahora un módulo flotante
compacto con línea fina de 1 px `rule`, radio 3, relleno `base`. Objetivo:
34 px, a 10 px del borde superior, dimensionado al contenido y centrado: marca
y espacios de trabajo, reloj, grupo de estado y energía. Reserva espacio como
todo preset flotante (margen incluido) y se distingue de Minimal Float por su
módulo más grande, margen más ancho y contenido más completo.

### 14.6 cozy-minimal — rediseñar

Por qué: una única tira flotante quieta es una elección válida para todos los
días. Objetivo: retitular "Minimal Float"; una tira flotante de 36 px, a 14 px
desde arriba, radio 3, relleno `base`; inicio marca + espacios de trabajo,
centro reloj, fin grupo de estado, batería, notificaciones. Sin acciones
rápidas, sin bandeja (movida al popout de estado). Quitar el emoji de flor de
los metadatos.

### 14.7 dock-bottom — rediseñar

Por qué: el único layout con lanzador primero. Objetivo: "Console dock" — un
dock flotante inferior de 44 px, radio 3, a 12 px del borde. Las apps fijadas
se sientan como celdas de canal (mosaicos de glifo de 32 px) con la barra
on-air en su borde superior para apps enfocadas y marcas de ocupación para las
que corren; marca y espacios de trabajo al inicio; reloj y grupo de estado al
fin. Los popouts abren hacia arriba.

### 14.8 classic-top y classic-bottom — conservar

Por qué: el escritorio convencional de una barra que la gente espera de otros
sistemas. Objetivo: una barra pegada de 36 px; inicio marca, espacios de
trabajo; centro reloj; fin pozo de audio, grupo de estado, bandeja, energía.
Los deslizadores de brillo y audio salen del grupo inicial hacia el grupo de
estado. `classic-bottom` es la misma dirección artística en el borde inferior;
el Selector de layouts presenta ambos como una tarjeta con selector de borde.

### 14.9 minimal-top — rediseñar

Por qué: el layout más quieto. Objetivo: una tira superior pegada de 30 px con
espacios de trabajo al inicio, reloj al centro y energía al fin.

### 14.10 productivity — restaurado

Por qué: una composición calma de trabajo enfocado es una alternativa real a
Minimal Top. Objetivo: un riel superior inset de 32 px (6 px): espacios de
trabajo y título de ventana activa al inicio, reloj y fecha al centro, solo
bandeja, isla de extensiones, grupo de estado y energía al fin; densidad
`glyphs`; sin deslizadores, clima ni medidores; las notificaciones expiran a
los 4 s.

### 14.11 minimal-left — rediseñar

Por qué: un riel vertical angosto es el mejor ajuste para pantallas ultrawide
y es distinto de los rieles Hornero. Objetivo: "Instrument rail" — riel
izquierdo pegado de 32 px: marca, celdas de espacios de trabajo (32 × 30) con
la barra on-air en el borde derecho, reloj apilado como horas sobre minutos en
Plex Sans Condensed, energía al fin. Los popouts abren hacia la derecha.

### 14.12 studio — rediseñar

Por qué: el modo Studio necesita el audio primero y un lienzo estable.
Objetivo: una barra superior pegada de 36 px; inicio marca, espacios de
trabajo, ventana activa; centro transporte de medios y reloj; fin chips
on-air, medidores de pico de salida y entrada (10 segmentos cada uno, picos
reales de PipeWire), carga DSP y conteo de xrun cuando están disponibles,
medidor de CPU, grupo de estado, energía. El popout de audio usa las tiras de
canal de consola de §13.

### 14.13 gaming — rediseñar

Por qué: el modo Gaming debe mantenerse fuera del camino. Objetivo: una tira
inferior flotante de 30 px que no reserva espacio, se oculta bajo ventanas en
pantalla completa, no toma foco y no dibuja medidores salvo que se pidan; solo
espacios de trabajo con contenido y grupo de estado; movimiento `off`; sin glow;
telemetría pausada mientras está oculta.

### 14.14 hornero-left y hornero-right — conservar

Por qué: la composición es querida y reconocible. Ambos presets están
**inspirados en el layout de Caelestia** y sus descripciones deben decirlo con
atribución (RFC §5.1, §8; `shell/docs/PROVENANCE.md`). Objetivo: conservar la
composición — riel pegado de 40 px con marca y espacios de trabajo arriba, el
título vertical de ventana activa al medio, reloj, estado, bandeja,
extensiones y energía abajo — renderizada en Signal: riel `base`, borde
interno de 1 px `rule`, celdas de espacios de trabajo con la barra on-air en el
borde que mira al contenido, glifos de Hornero Glyphs, popouts que abren hacia
el contenido con el morph de §11. No vuelve ningún token, forma ni API de
Material.

## 15. Bloques constructivos QML

Estas primitivas compartidas cubren cada regla de arriba; ningún layout
necesita sus propios trucos.

- `Segment` — relleno, separador, estados hover/presionado/abierto/foco.
- `Well` — lectura `sunken` con borde de 1 px.
- `SegmentMeter` — horizontal o vertical, cantidad, umbrales, enlace de valor,
  estado no disponible.
- `ScopeTrace` — retícula, traza, persistencia, glow y scanlines opcionales.
- `OnAirBar`, `OnAirChip`, `RegistrationTick`, `Notch`.
- `SurfaceFrame` — el fondo con morph usado por `AnchoredSurface`.
- `ClearInk` — consulta de polaridad y estilos de halo para Cockpit Clear.
- `Choreography` — escalonado de filas y resolución de nivel de movimiento.

## 16. Ítems abiertos

- Adoptar los valores de paleta de §3 y decidir sobre el rol `glow` (enmienda
  a la RFC y W1 config).
- Los archivos de preset actualmente usan barras Cockpit de 40/32 px; alinear
  con el 36/30 de la RFC.
- Validar todo lo aquí escrito en el host según RFC §7.1. Los renders
  conceptuales de arriba son solo intención de diseño.

## 17. Atmósfera

Anexo (2026-11-17, regla de misión: retrofuturista, cyberpunk, acogedor,
kawaii, nunca infantil). Signal es un instrumento; la atmósfera es la lámpara
que queda encendida al lado. Es una capa fina y opcional dibujada sobre las
superficies existentes; el Bezel, los roles y las reglas de glow anteriores no
cambian, y cada render de este documento sigue correcto si se quita la capa.
La shell la implementa en `services/Atmosphere.qml`, `services/atmosphere.js` y
`components/atmosphere/`; cada valor es un ajuste bajo `appearance.atmosphere.*`
(Centro de control, Apariencia, Atmósfera) con reinicio.

### 17.1 Luz

- **Lámpara** — un lavado radial cálido desde una esquina de la superficie
  (lanzador: borde superior; dashboard y riel del Centro de control: arriba a la
  izquierda; OSD: arriba a la derecha; menú de sesión: izquierda; bloqueo y
  Welcome: abajo a la izquierda y arriba a la derecha). Alfa pico 14 % en
  perilla 1, techo duro 20 %; el color es el chip `lamp`. Es un lavado de luz,
  no un halo emisivo, así que queda fuera del límite del 40 % de halo de la
  sección 9, pero toma una concesión del mismo presupuesto de glow (como
  máximo tres ítems, un lugar siempre reservado para la barra on-air y trazas
  de scope) y simplemente se omite cuando se agota el presupuesto.
- **Brillo interno suave** — una línea cálida de 1 px bajo el borde superior
  que se desvanece hacia ambos extremos, más un lavado de 28 px debajo. Pico
  7 %, techo 10 %.
- **Viñeta** — un oscurecimiento radial transparente sobre el 62 % central y
  que alcanza como máximo 30 % de `shadow` en las esquinas. Solo temas oscuros.
- **Grano y scanlines** — van debajo del contenido para que el texto y los
  glifos sigan nítidos. El grano es un mosaico sin sesgo de 128 px hasta un
  14 %; las scanlines son las líneas de la sección 10 (1 px cada 3, blanco
  cálido) hasta un 6 %, apagadas por defecto, solo temas oscuros.
- **Temas claros** conservan una lámpara a mitad de fuerza y el brillo interno,
  y quitan viñeta y scanlines.
- **Nunca** — en texto, anillos de foco ni notificaciones críticas; animado;
  siguiendo al cursor; en Alto Contraste; en modos Focus, Gaming o Studio. Las
  tarjetas de notificación reciben solo el brillo interno (sin lámpara por
  tarjeta).

### 17.2 Chips de acento y la mascota

Dos chips de acento derivados extienden la paleta sin cambiar un archivo de
paleta: `lamp` (el `glow` de la paleta, cayendo a `signal`, corrido hacia
`blush` según la perilla de calidez) y `blush` (un rosa polvoriento a partir
de `alert` y la ranura magenta de terminal de la paleta). Ambos se acercan a
`ink` hasta alcanzar 4.5:1 en las seis superficies, de modo que los gates de
contraste se cumplen para paletas personalizadas y Chromatic. Un tema puede
incluirlos luego como roles opcionales; nada depende de ello.

La mascota es el hornero como un sprite de 16 × 14 píxeles, dibujado en
colores de la paleta (lomo rufo desde `signal` entibiado por `alert`, vientre
desde `ink` en temas oscuros y un tinte cálido en temas claros, una mejilla
`blush`). Aparece en estados vacíos (lanzador sin resultados, bandejas de
notificaciones), saludos (tarjeta de estación del dashboard, pantalla de
bloqueo) y pie del menú de sesión, parpadea una vez cada siete segundos salvo
que el movimiento esté reducido y está oculta a tecnologías asistivas. Una
mascota por superficie, nunca junto a un error.

### 17.3 Microcopy

Dos voces, ambas completas para cada clave: `plain` (neutral) y `cozy`. Reglas
de `cozy`: como máximo 48 caracteres, sin signos de exclamación ni pregunta,
sin emojis ni kaomoji, sin apodos afectivos, nada que culpe al usuario, y la
redacción neutral sigue siendo el nombre accesible donde importa. Ejemplos:
"All quiet in the nest" para una bandeja vacía de notificaciones, "Nothing by
that name yet" para una búsqueda vacía, "Good evening. Settle in" en el
dashboard. Los saludos según la hora del día se refrescan cada cinco minutos.

### 17.4 Tipografía y pulido de movimiento

IBM Plex Sans para lectura, Plex Sans Condensed para numerales de pantalla,
Plex Mono para etiquetas de canal, sin cambios. Cifras de ancho fijo (OpenType
`tnum`) en lecturas y relojes para que los dígitos nunca desplacen a sus
vecinos; los relojes grandes tienen un tracking ~1.5 % más cerrado. Las capas
de atmósfera aparecen con la duración `fade`; la única escala de esta sección
es el asentamiento 1.0 a 0.98 de estados vacíos, bien dentro del límite de
resorte del 4 %, y todo queda estático bajo movimiento reducido.

### 17.4a Seguimientos de Bezel Cálido (estudio y Enmienda 4)

- **Plate** — etiqueta grabada: IBM Plex Sans Condensed SemiBold, mayúsculas,
  tracking 0.14 em (ajuste de usuario 0 a 0.3), cifras tabulares. Solo enums (un
  modo, un estado, un canal como LAUNCH del lanzador), nunca oraciones. A lo
  sumo cuatro tratamientos tipográficos por pantalla: UI, lectura, eyebrow,
  plate o display.
- **Bajo consumo** — el perfil de ahorro de energía quita lámpara, viñeta,
  grano y scanlines; el brillo interno queda. Alto Contraste, Focus, Gaming y
  Studio ocultan toda la capa.
- **Fundido** — un cambio de modo o interruptor desvanece la capa en 480 ms
  (la duración `scan`, dentro del rango de 400 a 600 ms); movimiento reducido y
  bajo consumo lo vuelven instantáneo.
- **Radios** — el aspecto Cozy escala el redondeo por 1.2, así que los radios
  efectivos quedan en o debajo de `small × 2` (6 px): suave, nunca píldora.
- **Cockpit Clear** — la capa nunca se adosa a barras, así que una barra clear
  no tiene tinte ni fondo de ningún tipo.
- **Alerta sobre `lifted`** — donde una paleta deja al `alert` plano debajo
  de 4.5:1 sobre tooltips (Dusk: 4.36), el texto de alerta usa `alertText`,
  `alert` acercado a `ink` hasta que pasa en las seis superficies.

### 17.5 Control

| Control | Clave | Rango | Fábrica |
| --- | --- | --- | --- |
| Atmósfera | `enabled` | on/off | on |
| Luz lámpara | `lamp` | 0 a 1.5 | 0.8 |
| Tinte lámpara | `warmth` | 0 a 1 | 0.2 |
| Brillo interno | `innerLight` | 0 a 1.5 | 0.8 |
| Viñeta | `vignette` | 0 a 1 | 0.4 |
| Grano de film | `grain` | 0 a 1 | 0.3 |
| Scanlines | `scanlines` | 0 a 1 | 0 |
| Mascota hornero | `mascot` | on/off | on |
| Voz microcopy | `tone` | cozy, plain | cozy |

Aspecto › Cozy ajusta las perillas de atmósfera junto con los tokens escalares
(lámpara 1.2, tinte 0.45, brillo 1.1, viñeta 0.5, grano 0.4); Aspecto › Hornero
es la fila de fábrica. Mirá `docs/CUSTOMISATION.md` en shell.

## 18. Fuentes de especímenes

Los especímenes se redactaron como una página HTML/CSS y se renderizaron con
Playwright (Chromium headless, 1920×1080, escala 1). Los fondos provienen de
[HorneroOS/config][wp-credits]: Buenos Aires de noche (Luis Argerich, CC BY
2.0), Panorama del Glaciar Perito Moreno (ThartmannWiki, CC BY-SA 4.0),
Argentina-Iguazu vista cercana de catarata (Güldem Üstün, CC BY 2.0), Serranía
de Hornocal 03 (Bernard Gagnon, CC BY-SA 4.0), Atardecer en el caldenal
(Juanedc, CC BY 2.0). Los glifos son Tabler Icons (MIT) y la tipografía es IBM
Plex (OFL-1.1).

[ref-rainmeter]: https://www.rankred.com/rainmeter-skins/
[ref-rings]: https://www.deviantart.com/londonali1010/art/Rings-Meters-for-Conky-141961783
[ref-seamod]: https://art.cleberg.net/post/seajey/Conky-Seamod-v0-1-283461046
[ref-waybar-man]: https://man.archlinux.org/man/extra/waybar/waybar-sway-workspaces.5.en
[ref-waybar-wiki]: https://github.com/Alexays/Waybar/wiki/Configuration
[ref-territory]: https://www.pushing-pixels.org/2014/08/07/the-craft-of-screen-graphics-and-movie-user-interfaces-interview-with-david-sheldon-hicks-of-territory-studio.html
[ref-cp-iig]: https://interfaceingame.com/articles/cyberpunk-2077-ux-ui-critique
[ref-cp-gdc]: https://gdcvault.com/play/1034160/User-Interface-in-Cyberpunk-2077
[ref-marathon-cb]: https://www.creativebloq.com/3d/video-game-design/bungies-art-director-explains-marathons-controversial-art-style
[ref-marathon-pcg]: https://www.pcgamer.com/games/fps/marathon-ui-designer-declares-himself-the-fontslop-merchant-and-promises-bungie-will-never-remove-the-sauce-from-the-ui
[ref-alien]: https://www.engadget.com/2014-10-07-alien-isolation-launch-interview.html
[ref-lt-sb]: https://www.studiobinder.com/blog/what-is-a-lower-third/
[ref-lt-frame]: https://blog.frame.io/2017/12/04/create-lower-thirds-titles-that-dont-suck/
[shell-presets]: https://github.com/HorneroOS/shell/tree/main/presets
[wp-credits]: https://github.com/HorneroOS/config/blob/main/profiles/themes/WALLPAPER-CREDITS.md
[showroom]: https://horneroos.com/showroom/
