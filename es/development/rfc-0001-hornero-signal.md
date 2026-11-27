# RFC 0001 — Hornero Signal

> Traducción al español rioplatense de la
> [versión en inglés](../../development/rfc-0001-hornero-signal.md), que es la
> canónica.

- **Estado** — Aceptada (2026-11-16); **superada en parte** por
  [RFC 0002 — Hornero Chromatic](rfc-0002-hornero-chromatic.md) (2026-11-17,
  enmienda 3: color dinámico opcional; §1, §3.1 y §9 abajo llevan notas donde
  aplica); enmendada el 2026-11-17 (enmienda 4: atmósfera Cozy Hackerpunk, ver
  el final de este documento); enmendada el 2026-11-16 (enmienda 2: ajustes de
  paleta guiados por contraste, rol opcional `glow`, dirección Signal Bezel;
  enmienda 1: ambición WOW + WORK, resortes de movimiento, catálogo de layouts,
  modos de experiencia, instrumentación, contratos de integración)
- **Implementación** — En progreso; nada está validado en un host físico
  todavía. Mirá [Estado de implementación](#estado-de-implementación).
- **Alcance** — Toda superficie de primera parte de HorneroOS: shell,
  PluginKit y extensiones, config (GTK/Qt/terminal/compositor), horneroctl,
  greeter, installer, website, docs, brand
- **Reemplaza** — El sistema de tokens derivado de Material 3 (`M3Palette`,
  roles `m3*`, Material Symbols, síntesis de fondo Material) y el tema
  opcional "Hornero 199X"
- **Seguimiento** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)

## 1. Por qué

La shell heredó la arquitectura Material 3 de Caelestia: cada color es un rol
tonal `m3*`, los íconos son ligaduras de Material Symbols, el movimiento usa
resortes "expressive" de M3 y los temas se sintetizan desde el fondo de
pantalla con `materialyoucolor`. Eso hacía que HorneroOS pareciera un Caelestia
con otro tema y ataba todo el stack de apariencia (shell, horneroctl, config) a
un sistema de diseño externo. Hornero 199X demostró que una dirección
retrofuturista argentina es la correcta para el proyecto, pero salió solo como
un pack de color opcional montado sobre la maquinaria M3.

Hornero Signal reemplaza la maquinaria, no solo los colores. Es un cambio
disruptivo intencional. **No** hay capa de compatibilidad con Material ni
sistema heredado en paralelo.

Enmienda 3: quitar la maquinaria Material no quita el color dinámico.
[RFC 0002 — Hornero Chromatic](rfc-0002-hornero-chromatic.md) devuelve las
paletas y variantes derivadas del fondo de pantalla como una **opción**, con un
motor nativo que produce directamente los roles Signal del §3.1. Las paletas
curadas del §3.2 siguen siendo el valor por defecto y el respaldo.

## 2. Dirección creativa

> Una estación de trabajo de ingeniería contemporánea de una Argentina
> alternativa de los años 90: salas de control de transmisión, biseles de
> osciloscopio, cartas de ajuste, láminas de dibujo técnico y la geometría
> diagonal de La Plata — ejecutada con sobriedad moderna.

La enmienda 1 sube la ambición: HorneroOS debe sentirse como una estación de
trabajo extraordinaria de un futuro tecnológico alternativo — computación
retrofuturista y cyberpunk interpretada por un diseñador de primer nivel —
inspirada en los mejores escritorios Rainmeter/Conky, configuraciones
intencionales de Polybar/Waybar, interfaces de la era Cyberpunk 2077 y sistemas
operativos ficticios. Deben convivir dos experiencias sin comprometerse entre
sí:

- **WOW** — inconfundiblemente original, cinematográfica, encantadora al
  descubrirla.
- **WORK** — ágil, accesible, confiable para horas de programación, producción
  musical, trabajo creativo y gaming.

El lenguaje visual concreto (anatomía de barra, medidores, encuadre, acentos
luminosos, detalles de fósforo, dirección artística por layout, coreografía de
movimiento) se especifica en
[Signal Visual Language](signal-visual-language.md). Enmienda 2: la dirección
elegida es **Signal Bezel** (módulos de instrumento mate, pozos de lectura
hundidos, telemetría de osciloscopio, muescas de disparador), elegida por sobre
*Carta* y *Transmisión* tras una comparación documentada; toma líneas de cota
de Carta y tiras de canal / chips on-air de Transmisión. El modo de experiencia
`signal` debe ser visiblemente más rico que `everyday` (composiciones de
instrumentos enmarcadas, trazas luminosas en vivo, telemetría más grande) —
no el mismo escritorio con más widgets. Debe verse excepcional con las
animaciones deshabilitadas.

Principios, en orden de prioridad:

1. **Primero el trabajo.** El cromo es calmo y mate. El acento es una señal, no
   una decoración: el ámbar significa *en vivo / activo / primario*, el celeste
   significa *foco / selección / información*.
2. **Instrumento, no juguete.** Líneas finas, radios chicos, numerales
   tabulares, medidores segmentados, canales rotulados, acentos luminosos
   sobrios de señal. Sin píldoras por todos lados, sin vidrio, sin gradientes
   neón, sin decoración hex al azar, sin efectos glitch, sin parpadeo
   constante, sin cromo pixel-art.
3. **Legible de un vistazo.** Todo rol de texto pasa WCAG AA sobre cada
   superficie en la que se usa; los bordes de UI pasan 3:1.
4. **Un solo lenguaje en todos lados.** Shell, extensiones, apps GTK/Qt,
   greeter, instalador y sitio web usan los mismos roles, tipografía, glifos y
   movimiento.

Detalles de firma (usalos con consistencia, nunca como ornamento al azar):

- **Eyebrows** — etiquetas de sección en IBM Plex Mono, mayúsculas, tracking
  +8 %, `inkMuted`, opcionalmente precedidas por un número de canal
  (`01 · AUDIO`).
- **Marca de registro** — el panel enfocado o activo muestra una marca `signal`
  de 2×10 px en su esquina superior inicial en lugar de un halo.
- **Barra on-air** — el estado activo en tiras (espacios de trabajo, pestañas,
  ítems de riel) es una barra `signal` de 2–3 px en el borde que mira al
  contenido, no una píldora rellena.
- **Medidores segmentados** — volumen, brillo, batería, CPU y lecturas
  similares se dibujan como segmentos discretos (estilo vúmetro) con valores
  mono tabulares.
- **Diagonal** — la diagonal de 45° de La Plata aparece solo en superficies de
  marca (bloqueo, greeter, instalador, hero del sitio web, fondos), nunca
  dentro de controles.

## 3. Tokens

El contrato de tokens es propiedad de **HorneroOS/config**
(`profiles/themes/tokens.schema.json`, versión de esquema 2). La shell consume
los mismos nombres de rol mediante el singleton `Signal`
(`Signal.palette.<role>`). Los generadores de GTK, Qt, terminal, Hyprland,
hyprlock, greeter, instalador y sitio web mapean solo desde estos roles.

### 3.1 Roles de color

- `ground` — Nivel más atrás / escritorio, velos sobre el fondo, fondo de
  bloqueo
- `sunken` — Pozos de entrada, fondos de pistas, áreas hundidas
- `base` — Barras, cuerpo de ventanas y diálogos
- `panel` — Tarjetas, popouts, menús
- `raised` — Filas con cursor o seleccionadas, tarjetas anidadas
- `lifted` — Mayor elevación, tooltips, estados presionados
- `ink` — Texto y glifos primarios
- `inkMuted` — Texto secundario, eyebrows, glifos inactivos
- `inkFaint` — Deshabilitado / solo decorativo — nunca texto esencial
- `rule` — Separadores finos dentro de una superficie
- `ruleStrong` — Límites de controles, contornos que deben pasar 3:1
- `signal` / `onSignal` — Acción primaria, estado vivo/activo (ámbar)
- `signalWell` / `onSignalWell` — Relleno primario de bajo énfasis (chip
  elegido)
- `cue` / `onCue` — Anillo de foco, selección, información (celeste)
- `cueWell` / `onCueWell` — Relleno informativo de bajo énfasis
- `phosphor` / `onPhosphor` — Positivo/saludable/conectado (verde fósforo)
- `phosphorWell` / `onPhosphorWell` — Relleno positivo de bajo énfasis
- `alert` / `onAlert` — Destructivo/error
- `alertWell` / `onAlertWell` — Relleno de error de bajo énfasis
- `inverse` / `onInverse` / `inverseSignal` — Snackbars y toasts invertidos
- `scrim`, `shadow` — Capas superpuestas y el único color de sombra
- `glow` — Acento luminoso opcional para telemetría en vivo (enmienda 2)
- `focus` — Anillo de foco por teclado (por defecto `cue`)
- `term0`…`term15` — Paleta ANSI de terminal

Quitados sin reemplazo: todos los `*Fixed*`, `*_paletteKeyColor`, `surfaceTint`,
`surfaceVariant`, `onBackground` y la biblioteca externa de color Material. Se
quitan los tipos de esquema Material y la síntesis Material "seguir al fondo";
la enmienda 3 reemplaza la capacidad (no los roles ni el algoritmo) por las
variantes Hornero Chromatic y una política opcional de seguimiento de fondo,
especificada en la [RFC 0002](rfc-0002-hornero-chromatic.md).

Mapeo Material → Signal usado **una sola vez** para la migración (no mantenido
como tabla de alias): `background/surfaceDim/surfaceContainerLowest → ground`,
`surfaceContainerLow → sunken`, `surface → base`, `surfaceContainer → panel`,
`surfaceContainerHigh → raised`,
`surfaceContainerHighest/surfaceBright → lifted`, `onSurface → ink`,
`onSurfaceVariant → inkMuted`, `outlineVariant → rule`,
`outline → ruleStrong`, `primary* → signal*`, `secondary* → cue*`,
`tertiary* → phosphor*`, `success* → phosphor*`, `error* → alert*`,
`*Container → *Well`.

### 3.2 Paletas insignia

`hornero-signal-night` es el valor de fábrica: paneles de grafito frío con
tinta cálida fósforo-crema. `hornero-signal-day` es papel cálido de dibujo
técnico con texto negro tinta.

| Rol              | Signal Night | Signal Day |
| ---------------- | ------------ | ---------- |
| `ground`         | `#0C0F13`    | `#E6E1D5`  |
| `sunken`         | `#101419`    | `#DCD6C8`  |
| `base`           | `#13171D`    | `#F2EEE5`  |
| `panel`          | `#181D24`    | `#F7F4EE`  |
| `raised`         | `#1F252E`    | `#FBF9F5`  |
| `lifted`         | `#283039`    | `#FFFFFF`  |
| `ink`            | `#ECE6DA`    | `#1B1E22`  |
| `inkMuted`       | `#A8ABAD`    | `#4E545B`  |
| `inkFaint`       | `#737980`    | `#7A8086`  |
| `rule`           | `#2C333C`    | `#D3CCBD`  |
| `ruleStrong`     | `#707A85`    | `#736D62`  |
| `focus`          | `#7EC1EA`    | `#1A5F88`  |
| `signal`         | `#F2A33A`    | `#8F4B00`  |
| `onSignal`       | `#1A1205`    | `#FFFFFF`  |
| `signalWell`     | `#3A2A12`    | `#F6DDB8`  |
| `onSignalWell`   | `#FFD9A3`    | `#3D2200`  |
| `cue`            | `#7EC1EA`    | `#1A5F88`  |
| `onCue`          | `#06151F`    | `#FFFFFF`  |
| `cueWell`        | `#16303F`    | `#D3E7F3`  |
| `onCueWell`      | `#CDE8F8`    | `#0B2E44`  |
| `phosphor`       | `#8BD49A`    | `#256A3B`  |
| `onPhosphor`     | `#07170C`    | `#FFFFFF`  |
| `phosphorWell`   | `#173222`    | `#D5EBD9`  |
| `onPhosphorWell` | `#CDEFD4`    | `#0E2E17`  |
| `alert`          | `#F0705A`    | `#A8341C`  |
| `onAlert`        | `#1E0905`    | `#FFFFFF`  |
| `alertWell`      | `#3D1A14`    | `#F7D7D0`  |
| `onAlertWell`    | `#FFD3CA`    | `#4A1209`  |
| `inverse`        | `#ECE6DA`    | `#1B1E22`  |
| `onInverse`      | `#181D24`    | `#F2EEE5`  |
| `inverseSignal`  | `#8A5200`    | `#F2A33A`  |
| `scrim`          | `#000000`    | `#000000`  |
| `shadow`         | `#000000`    | `#000000`  |
| `glow`           | `#FFB650`    | `#8F4B00`  |

**Signal High Contrast** mantiene los roles, usa fondo `ground` `#000000`, tinta
`#FFFFFF`, `signal` `#FFC247`, `cue` `#8FD3FF` y `ruleStrong` blanco puro.

Otros temas del catálogo (temas fotográficos regionales de la Argentina,
puertos comunitarios) siguen siendo válidos **si** proveen un conjunto completo
de roles schema-v2 que pase las pruebas de contraste. Los temas que solo
existían como semillas M3 se quitan o se portan.

Enmienda 2: los valores de arriba se ajustaron para que cada rol de texto pase
también 4.5:1 sobre pozos de lectura `sunken` y `ruleStrong` pase 3:1 sobre
tooltips `lifted`. `glow` es un rol opcional (por defecto: `signal`) para
acentos luminosos: solo en trazas de telemetría en vivo y, en el modo de
experiencia `signal`, la barra on-air activa y los chips on-air; desenfoque
≤ 4 px, alfa ≤ 40 %, a lo sumo tres ítems brillantes en pantalla, nunca
animado, deshabilitado en temas claros, alto contraste, modos `focus` y
`gaming`, y en barras Cockpit Clear. La validación se extiende a `sunken` y
`lifted`.

### 3.3 Tipografía

| Familia   | Fuente                  | Uso                                   |
| --------- | ----------------------- | ------------------------------------- |
| `sans`    | IBM Plex Sans           | Texto de UI                           |
| `mono`    | IBM Plex Mono           | Lecturas, numerales, eyebrows, código |
| `display` | IBM Plex Sans Condensed | Reloj, bloqueo, títulos grandes       |

Paquete: `ttf-ibm-plex` (Arch `extra`, OFL-1.1). Escala (px a escala 1):
`small 11`, `smaller 12`, `normal 13`, `larger 15`, `large 18`,
`extraLarge 28`, `display 56`. Los números siempre usan cifras tabulares.

### 3.4 Glifos

**Hornero Glyphs** — un subconjunto curado de Tabler Icons (contorno, MIT)
compilado en `assets/fonts/hornero-glyphs.ttf` con `fonttools`, más una tabla
generada de nombre→punto de código. Los componentes usan
`Glyph { name: "wifi" }`. Se quitan Material Symbols del código, valores por
defecto y empaquetado. El trazo se lee como 1.5–2 px a 16–24 px, en sintonía
con el lenguaje de líneas finas.

### 3.5 Geometría y espaciado

Grilla de 4 px. Radio: `small 3`, `normal 5`, `large 8`, `full` solo para
elementos genuinamente circulares (avatares, puntos de radio). Espaciado:
`small 4`, `smaller 8`, `normal 12`, `larger 16`, `large 24`. Relleno (padding):
`small 4`, `smaller 6`, `normal 8`, `larger 12`, `large 16`. Bordes: 1 px `rule`
dentro de superficies, 1 px `ruleStrong` en controles. La elevación se expresa
mediante el rol de superficie más una sombra sobria (`shadow` al 35 %, 12 px de
desenfoque, 4 px de desplazamiento alejándose del borde de anclaje). Sin vidrio
con desenfoque trasero por defecto.

### 3.6 Movimiento

| Curva        | Bezier                | Uso                                   |
| ------------ | --------------------- | ------------------------------------- |
| `standard`   | `0.2, 0, 0, 1`        | Cambios de estado                     |
| `enter`      | `0.05, 0.7, 0.1, 1`   | Elementos que aparecen                |
| `exit`       | `0.3, 0, 1, 1`        | Elementos que salen                   |
| `sweep`      | `0.65, 0, 0.35, 1`    | Barridos de revelación, transiciones  |
| `settle`     | `0.32, 1.24, 0.42, 1` | Pequeño rebote elegante               |
| `settleFast` | `0.34, 1.3, 0.5, 1`   | Controles rápidos, chips              |

Duraciones: `quick 90`, `short 160`, `medium 240`, `long 360`, `scan 480`,
`settleFast 220`, `settle 320` ms.

Enmienda 1: el asentamiento de inspiración física forma parte del lenguaje. El
sobreimpulso (overshoot) se mantiene acotado (≤ 4 % del recorrido), se usa solo
para movimiento espacial (posición, tamaño, transformación de forma), nunca
para opacidad ni color, y cada superficie define su coreografía (morph desde el
origen del disparador, cambio de tamaño/forma entre controles vecinos,
escalonado de contenido, profundidad en capas) mediante primitivas compartidas
— sin trucos por layout. El movimiento no debe sumar latencia de entrada: las
superficies son interactivas desde su primer cuadro, los presupuestos se miden
(§7), y el hardware de bajo consumo puede elegir un nivel de movimiento
reducido. **Scan-in**: las superficies ancladas se revelan con un barrido de
recorte desde el borde de anclaje más 6 px de desplazamiento y un fundido
(`enter`/`short` a `medium`); la salida es un fundido más 4 px de regreso hacia
el anclaje (`exit`/`quick`). Movimiento reducido (`appearance.reducedMotion` o
la preferencia del sistema) pone las duraciones en 0 salvo fundidos de opacidad
topeados en 90 ms.

## 4. Contrato de interacción — superficies ancladas

Todo popout, tooltip, cajón, menú, notificación y popover de extensión es
posicionado por un único solver compartido (`AnchoredSurface` + `Placement` en
la shell, re-exportado a PluginKit). Entradas: el ítem disparador, su barra
dueña (borde, estilo, grosor, margen, reserva, flotante/pegada), la pantalla
dueña (geometría, escala, áreas reservadas) y el tamaño preferido de la
superficie.

Reglas:

1. La dirección de expansión se deriva del borde de la barra dueña: arriba →
   abajo, abajo → arriba, izquierda → derecha, derecha → izquierda. Las
   superficies sin barra dueña usan un borde preferido explícito.
2. La alineación en el eje transversal se centra en el disparador y luego se
   ajusta al rectángulo utilizable de la pantalla menos el margen (8 px ×
   escala). Si la dirección preferida no entra, se invierte una vez; si ninguna
   entra, se acota y se desplaza el contenido.
3. El anclaje está vivo: la superficie sigue los cambios de geometría del
   disparador (reordenamiento de barra, cambio de tamaño de isla, cambio de
   monitor) sin un cuadro desfasado.
4. El movimiento se origina en el borde del disparador (scan-in) — nunca desde
   el centro de la pantalla.
5. Foco: los popouts por hover nunca toman foco de teclado; las superficies
   abiertas por clic/teclado toman foco y lo devuelven al disparador con
   Escape. Un Escape cierra exactamente una superficie (cascada de Escape
   existente).
6. Los popouts por hover tienen una demora de intención de apertura de 120 ms y
   una gracia de cierre de 240 ms puenteada sobre el hueco
   disparador↔superficie; sin parpadeo al cruzar.
7. Las extensiones reciben el mismo contrato; no pueden posicionarse en
   coordenadas absolutas de pantalla.

La corrección se verifica con pruebas unitarias del solver para los cuatro
bordes, rectángulos multi-monitor de escala mixta y espacio restringido, más
capturas en host (§7).

## 5. Cockpit — escritorio por defecto de fábrica

**Barra superior = actuar. Barra inferior = saber. Centro = trabajo sin
interrupciones.**

- **Riel superior** (36 px, `base`, 1 px `rule` en el borde interno, margen
  6 px): inicio — marca Hornero (lanzador), acciones rápidas; centro — reloj y
  fecha en IBM Plex Sans Condensed; fin — grupo de estado (red, Bluetooth,
  audio), bandeja, isla de extensiones, notificaciones, energía.
- **Tira inferior** (30 px, pegada): inicio — espacios de trabajo con barra
  on-air y marcas de ocupación; centro — título de ventana activa y transporte
  de medios; fin — distribución de teclado, recursos (mini-medidores
  segmentados), batería cuando hay.
- Cockpit es el valor por defecto en `shell.default.json`, valores por defecto
  de config, reset de horneroctl, primer arranque del instalador y todas las
  ediciones. Cockpit es la insignia reconocible y recibe la mayor dirección de
  arte.

### 5.1 Catálogo de layouts (enmienda 1)

Cada preset publicado se audita y tiene dirección artística; los presets flojos
se mejoran, fusionan o quitan por mérito, no se mantienen para preservar un
conteo. Cada sobreviviente tiene una identidad visual y funcional distinta
definida en la especificación de lenguaje visual.

- **Hornero Left / Hornero Right** se conservan como layouts pulidos y
  soportados. Sus descripciones reconocen que están inspirados en el layout de
  Caelestia, con atribución. Adoptan tokens Signal, el contrato compartido de
  interacción y las primitivas de movimiento manteniendo su composición
  reconocible. Esto no reintroduce tokens ni APIs de Material.
- **Cockpit Clear** tiene una ausencia genuina de fondo de barra: cero
  opacidad de fondo, sin tinte, placa, desenfoque, velo de borde ni sombra de
  fondo. La legibilidad proviene de tratamientos solo sobre el primer plano
  (tinta adaptativa elegida por región de fondo, contorno de glifo/texto o
  sombra solo en el primer plano, estilos de primer plano seleccionables por
  el usuario). Los popouts abiertos desde barras Clear siguen siendo
  superficies Signal totalmente opacas. Validado contra fondos claros,
  oscuros, detallados y de alto contraste en el host real.

## 5a. Modos de experiencia (enmienda 1)

Cuatro ejes independientes se combinan; ninguno es una shell aparte:

1. **Edición** (Desktop, Studio, Gaming) — capacidades y paquetes instalados.
   Propiedad de HorneroOS/hornero.
2. **Modo de experiencia** — cómo se comporta el sistema ahora mismo: `focus`,
   `everyday` (por defecto), `signal` (inmersivo), `gaming`, `studio`. Un modo
   es un perfil declarativo de: nivel de movimiento, densidad de
   instrumentación, widgets de escritorio, política de notificaciones (no
   molestar, supresión en pantalla completa), preset de layout preferido,
   pistas de reposo/energía y ganchos de edición (GameMode, quantum de
   PipeWire, Gamescope). Propiedad de la shell (`services/Experience`) con el
   grupo de comandos `horneroctl mode` (list, get, set, reset, status) como
   interfaz del sistema.
3. **Preset de layout** — composición de barras (Cockpit, Hornero Left, …).
4. **Tema** — roles Signal y fondo de pantalla.

Reglas: el usuario cambia de modo explícitamente (lanzador, Centro de control,
IPC, CLI); el cambio automático opcional (p. ej. juego en pantalla completa →
`gaming`) viene apagado por defecto, es solo local, se muestra en la UI y es
reversible con una acción. Las personalizaciones del usuario por modo se
conservan; el verbo `horneroctl mode reset` y una acción del Centro de control
vuelven a `everyday` de fábrica + Cockpit + Signal Night. Los modos solo
habilitan capacidades que la edición instalada posee; una capacidad faltante
se muestra como no disponible, no se simula. **Gaming** nunca debe dibujar
encima de aplicaciones en pantalla completa, robar foco ni sondear con costo;
**Focus** maximiza el espacio útil y aquieta movimiento y notificaciones;
**Signal** es donde viven la telemetría y el movimiento más ricos.

## 5b. Instrumentación (enmienda 1)

Los escritorios clase Rainmeter/Conky se construyen sobre PluginKit, no sobre
un motor de widgets competidor: módulos de barra, widgets de escritorio
(flotantes, layer-shell) y paneles contextuales comparten una única API de
superficie de widget, tokens Signal, primitivas de movimiento y el contrato de
superficies ancladas. Los datos provienen de servicios nativos de la shell
(`SystemUsage`, `Network`, `Audio`, `Players`, `Battery`, `Hypr/Niri`) y
proveedores declarados con permisos; los valores nunca se inventan — sensores
no disponibles se muestran como no disponibles. El sondeo es compartido y con
tasa limitada por proveedor con costo de CPU medido. La instrumentación cubre
carga y temperatura de CPU/GPU, memoria, almacenamiento, red,
audio/reproducción, salud de hardware, espacios de trabajo, relojes y
calendarios.

## 6. Propiedad y orden de integración

- **W1 Tokens + esquema de tema v2 + temas insignia, generadores
  GTK/Qt/kitty/Hyprland, valor por defecto Cockpit** — config; *depende de:*
  RFC
- **W2 Base de shell: singleton `Signal`, fuentes, Hornero Glyphs, tokens de
  movimiento, remoción de código M3** — shell; *depende de:* RFC
- **W3 Backend de apariencia: quitar síntesis `materialyoucolor`, aplicar temas
  schema-v2** — hornero (`horneroctl`); *depende de:* W1
- **W4 Superficies de shell: componentes, barras, Cockpit, solver de superficies
  ancladas, lanzador, dashboard, Centro de control, notificaciones, OSD,
  bloqueo, sesión, bienvenida** — shell; *depende de:* W2
- **W5 PluginKit + extensiones de primera parte sobre Signal** — shell,
  plugins; *depende de:* W2
- **W6 Greeter, marca del instalador, arranque** — greeter, installer; *depende
  de:* RFC
- **W7 Reposicionamiento del sitio web + activos de marca** — website, config;
  *depende de:* RFC
- **W8 Docs, perfil de org, READMEs** — docs, .github, todos; *depende de:*
  W1–W7
- **W9 QA: matriz de host, instalación VM, evidencia** — qa; *depende de:*
  W4–W6

Los contratos entre frentes son los nombres de rol (§3.1), familias
tipográficas (§3.3), API del componente glifo (§3.4), nombres de movimiento
(§3.6) y la API de superficies ancladas (§4). Cambiar cualquiera exige enmendar
esta RFC.

## 7. Validación y definición de terminado

El [issue de misión](https://github.com/HorneroOS/.github/issues/28) guarda la
lista. En resumen: no quedan referencias a `m3`, `Material`,
`materialyoucolor` ni Material Symbols en código o empaquetado de primera
parte (escaneo estático en CI); pasan las pruebas de contraste para cada tema
publicado; el solver pasa pruebas de bordes/escala/multi-monitor; Cockpit y los
presets soportados se capturan en el host real a las resoluciones y escalas
listadas; una instalación descartable en VM llega al primer arranque en
Cockpit + Signal Night. La evidencia indica dónde se produjo (host, VM o CI) y
nunca se fabrica.

### 7.1 Validación visual (enmienda 1)

Que pasen las pruebas no es evidencia de buen diseño. Cada cambio de superficie
se corre en el host real (o en VM cuando el host no puede ejercitarlo), se
captura, inspecciona y compara antes/después; los resultados flojos se iteran.
Cobertura requerida: 1280×720, 1366×768, 1920×1080, ultrawide; escalas
100/125/150/200 %; monitor único, múltiple y escala mixta (salidas virtuales
donde falte hardware, etiquetadas como tales); los cuatro bordes de barra;
cada preset sobreviviente; Cockpit Clear sobre al menos cuatro clases de fondo;
claro/oscuro, movimiento reducido; arranque, reinicio, persistencia. El
movimiento se mide (tiempo de cuadro, entrada a primer cuadro) y se registra
donde sea posible. Los renders conceptuales siempre llevan etiqueta de
concepto.

## 8. Atribución

Se mantienen la ascendencia de Caelestia, sus licencias y archivos NOTICE, y
las descripciones de los presets Hornero Left/Right acreditan el layout de
Caelestia y siguen siendo precisas (`shell/docs/PROVENANCE.md`). Tabler Icons
(MIT) e IBM Plex (OFL-1.1) se acreditan en archivos NOTICE donde se distribuyen.

## 9. Contratos de integración

- **Archivo de tema** — `config/profiles/themes/<id>/theme.json`, esquema v2:
  `schemaVersion: 2`, `id`, `name`, `mode` (`dark` | `light`), `palette`
  (exactamente los roles de §3.1; `glow` opcional, ausente → `signal`),
  `terminal` (arreglo de 16 colores hex), `gtkTheme`, `iconTheme`,
  `defaultWallpaper`, `wallpaperDir`; opcionales `description`, `tags`,
  `collection`, `collectionOrder`, `colorOnly`, `version`, `$schema`. Quitados
  sin reemplazo: semillas M3, `schemeType`, variantes, flavours, `darkMode`,
  `gtkPreferDark`, `family`, `tokensVersion`, `components`.
- **Esquema en vivo** —
  `${XDG_STATE_HOME:-~/.local/state}/hornero/signal/scheme.json` =
  `{"schemaVersion":2,"id":…,"mode":…,"palette":{role:"#RRGGBB"},"terminal":[16]}`
  (`glow` solo cuando el tema lo define), escrito de forma atómica por la ruta
  de aplicación de tema de horneroctl (o la shell para integrados) y observado
  por la shell. Con un tema curado, los fondos nunca cambian la paleta (solo
  la elección por región de Cockpit Clear entre las tintas noche y día del
  tema sigue al fondo). Enmienda 3: el id reservado `hornero-chromatic`
  selecciona Hornero Chromatic; horneroctl escribe entonces un esquema generado
  con los bloques opcionales y aditivos `chromatic`, `minSurfaceAlpha` y
  `clearInk` ([RFC 0002](rfc-0002-hornero-chromatic.md) §8).
- **Ids integrados** — `hornero-signal-night` (por defecto),
  `hornero-signal-day`, `hornero-signal-contrast`; las selecciones
  `hornero-dark/light/199x` migran una vez a night/day/night. Los retirados
  `neon-city`, `vapor-dreams`, `soft-morning` y `warm-sunset` no tienen
  equivalente Signal y migran a night o day según su modo. Es una migración de
  datos de única vez, no una capa de alias.
- **Fuentes y glifos** — familias `IBM Plex Sans`, `IBM Plex Mono`,
  `IBM Plex Sans Condensed` desde `ttf-ibm-plex`;
  `assets/fonts/hornero-glyphs.ttf` cargada por la shell mediante
  `Glyph { name }`, sin dependencia de fuente de íconos del sistema.
- **Preset por defecto** — `cockpit`; modo por defecto — `everyday`.

## Estado de implementación

*Al 2026-11-17, desde las ramas `main` de cada repositorio. Esta sección
registra qué está fusionado y dónde se comprobó. No es una afirmación de que el
diseño esté aceptado visualmente: ninguna parte de esta RFC se validó en un
host físico, y solo un escenario smoke corrió en la máquina virtual de QA.* La
lista de misión y discusión viven en
[HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28).

### Dónde está cada frente de trabajo

| Frente (sección 6) | Repo | Fusionado en `main` |
| --- | --- | --- |
| W1 Tokens, esquema v2, temas | config | [128][c128], [133–136][c133] |
| W2 Base shell, movimiento, sin M3 | shell | [475][s475] |
| Solver anclado y popouts (sec. 4) | shell | [477][s477], [482][s482] |
| W3 Backend de apariencia | hornero | [421][h421], [424][h424] |
| W4 Barra, Cockpit, celdas | shell | [483][s483], [484][s484], [494][s494] |
| W4 Cockpit Clear con tinta adaptativa | shell | [490][s490] |
| W4 Lanzador, notif., OSD, sesión | shell | [481][s481] |
| W4 Dashboard, bloqueo, Welcome, fondo | shell | [492–500][s492] |
| W4 Centro de control (en progreso) | shell | [488–508][s488] |
| W4 Companion y selector de área | shell | [496][s496] |
| Modos de experiencia (sección 5a) | shell | [479][s479], [487][s487] |
| Deck Signal (sec. 5b) | shell | [503][s503], [505][s505], [507][s507] |
| W5 Host PluginKit 3 | shell | [486][s486] |
| W5 Extensiones de 1.ª parte PK3 | plugins | [63–69][p63] |
| W6 Greeter | greeter | [44][g44] |
| W6 Marca del instalador | installer | [98][i98], [100][i100] |
| W7 Sitio web | website | [224–230][w224] |
| W8 Docs | docs | [107–113][d107] y fase 2 |
| W9 Herramientas QA | qa | [85][q85], [86][q86] |

Notas detalladas de PRs de esa tabla: `config` [133][c133], [134][c134],
[135][c135], [136][c136] resincronizan valores por defecto de la shell;
`shell` Dashboard/bloqueo/utilidades incluye [492][s492], [493][s493],
[497][s497], [499][s499], [500][s500]; Centro de control incluye [488][s488],
[489][s489], [491][s491], [495][s495], [501][s501], [504][s504], [506][s506],
[508][s508]; `plugins` incluye [63][p63], [64][p64], [65][p65], [66][p66],
[67][p67], [68][p68], [69][p69]; `website` incluye [224][w224], [225][w225],
[226][w226], [227][w227], [229][w229], [230][w230]; `docs` incluye
[107][d107], [108][d108], [110][d110], [111][d111], [113][d113] y las páginas
de fase 2.

Sin terminar, por diseño o todavía no alcanzado:

- El resto de los paneles del Centro de control y unas pocas superficies
  (selector de layout, info de ventana, polkit y la UI de companion), seguido
  en [shell#485](https://github.com/HorneroOS/shell/issues/485), y la
  evidencia restante de modos de experiencia en
  [shell#478](https://github.com/HorneroOS/shell/issues/478).
- La actualización de datos de producto del sitio web y una imagen QA fresca
  acuñada desde los `main` fusionados.
- Cada ítem de la sección 7.1 que necesita el host real.

### Dónde se validó cada parte

"Offscreen / CI" significa pruebas automatizadas, chequeos de esquema y
contraste, escaneos estáticos y renders QML offscreen que corrieron en CI o en
una máquina de desarrollo sin compositor. "QA VM" significa el guest descartable
en [HorneroOS/qa](https://github.com/HorneroOS/qa). "Host" significa una sesión
de escritorio real en hardware físico.

| Área | Offscreen / CI | QA VM | Host |
| --- | --- | --- | --- |
| Esquema, paletas y contraste | Sí | No | No |
| Base shell, glifos, escaneo M3 | Sí | No | No |
| Solver de ubicación | Sí | No | No |
| Geometría popout, tiempos, perf | Pruebas offscreen | No | No |
| Barra, Cockpit, Cockpit Clear | Renders offscreen | No | No |
| Lanzador, OSD, sesión, bloqueo | Renders offscreen | No | No |
| Paneles del Centro de control | Renders offscreen | No | No |
| Perfiles de modo y solver deck | Sí | No | No |
| Página Experience y deck Signal | Pruebas offscreen | No | No |
| Costo de procesador por modo | No | No | No |
| Host PluginKit 3 y 36 ext. | Validadores, offscreen | No | No |
| Backend apariencia `horneroctl` | Pruebas unitarias | No | No |
| Marca de greeter e instalador | CI | No | No |
| Sitio web | Build, a11y, capturas | No | No |
| Escritorio listo en imagen | n/d | Solo smoke | No |

El único resultado de QA VM es el escenario `smoke/desktop-ready`, que pasó en
una imagen construida desde `main` anteriores de Signal (cargó el esquema
Signal vivo y una persona inspeccionó una captura del escritorio). No cubre
las superficies fusionadas desde entonces. Cockpit Clear no se comprobó sobre
fondos reales, los popouts anclados no se midieron en tiempo sobre un
compositor y ningún preset se capturó a las resoluciones y escalas listadas en
la sección 7.1. Hasta que exista esa evidencia, tratá las afirmaciones visuales
de las páginas de usuario como intención, no resultado.

### Definición de terminado (sección 7)

| Criterio | Estado |
| --- | --- |
| Sin referencias Material en código | Gate en shell y plugins |
| Pruebas de contraste por tema | En config (`test_contrast.sh`) |
| Pruebas de bordes/escala del solver | En pruebas de shell |
| Cockpit y presets capturados en host | Sin hacer |
| Install en VM arranca en Cockpit | Sin hacer |

El escaneo Material tiene gate solo en los repositorios shell y plugins; los
otros repositorios todavía no tienen gate de escaneo estático.

## Enmienda 4 — Cozy Hackerpunk (2026-11-17)

Dirección: **Cozy Hackerpunk, retrofuturismo argentino, computación personal**
([estudio](signal-cozy-hackerpunk-study.md)). Signal Bezel sigue siendo la
estructura; esta enmienda cambia la atmósfera, no los contratos.

- **Roles sin cambios.** §3.1 no suma roles. La calidez viene de una paleta
  curada y de valores de atmósfera derivados de la paleta activa.
- **Nueva paleta insignia.** `hornero-signal-dusk` (colección `hornero-signal`,
  orden 4): superficies carbón-berenjena cálidas, tinta crema `#F1E6D2`, señal
  cobre `#F29A4A`, `cue` cian, `phosphor`, `glow` `#FFB070`. Mismos gates que
  Night; Night, Day y High Contrast mantienen sus valores.
- **Atmósfera** (lavado de lámpara, luz interna suave, viñeta, grano) se
  permite como capa de bajo alfa debajo del texto con techos duros, ajustable
  por el usuario, deshabilitada en High Contrast y por ahorro de energía, y
  nunca contada como glow. El presupuesto de glow de la Enmienda 2 no cambia.
- **Tipografía.** IBM Plex sigue siendo la familia. Suma un estilo de etiqueta
  *plate* (Plex Sans Condensed SemiBold, mayúsculas, tracking +14 %) para
  estados enum, a lo sumo cuatro tratamientos tipográficos por pantalla, cifras
  tabulares para todo valor cambiante.
- **Rosa/violeta** son acentos raros (terminal, etiquetas, momentos
  especiales), nunca el único portador de significado.
- **Voz.** Microcopy cálido en el idioma del usuario (voseo en español) con una
  voz neutral siempre a un interruptor de distancia.
- **Originalidad.** La serie de referencia informa solo principios; no se usa
  ningún personaje, obra de arte, logo ni objeto de terceros (estudio §2).

[c128]: https://github.com/HorneroOS/config/pull/128
[c133]: https://github.com/HorneroOS/config/pull/133
[c134]: https://github.com/HorneroOS/config/pull/134
[c135]: https://github.com/HorneroOS/config/pull/135
[c136]: https://github.com/HorneroOS/config/pull/136
[s475]: https://github.com/HorneroOS/shell/pull/475
[s477]: https://github.com/HorneroOS/shell/pull/477
[s482]: https://github.com/HorneroOS/shell/pull/482
[h421]: https://github.com/HorneroOS/hornero/pull/421
[h424]: https://github.com/HorneroOS/hornero/pull/424
[s483]: https://github.com/HorneroOS/shell/pull/483
[s484]: https://github.com/HorneroOS/shell/pull/484
[s494]: https://github.com/HorneroOS/shell/pull/494
[s490]: https://github.com/HorneroOS/shell/pull/490
[s481]: https://github.com/HorneroOS/shell/pull/481
[s492]: https://github.com/HorneroOS/shell/pull/492
[s493]: https://github.com/HorneroOS/shell/pull/493
[s497]: https://github.com/HorneroOS/shell/pull/497
[s499]: https://github.com/HorneroOS/shell/pull/499
[s500]: https://github.com/HorneroOS/shell/pull/500
[s488]: https://github.com/HorneroOS/shell/pull/488
[s489]: https://github.com/HorneroOS/shell/pull/489
[s491]: https://github.com/HorneroOS/shell/pull/491
[s495]: https://github.com/HorneroOS/shell/pull/495
[s501]: https://github.com/HorneroOS/shell/pull/501
[s504]: https://github.com/HorneroOS/shell/pull/504
[s506]: https://github.com/HorneroOS/shell/pull/506
[s508]: https://github.com/HorneroOS/shell/pull/508
[s496]: https://github.com/HorneroOS/shell/pull/496
[s479]: https://github.com/HorneroOS/shell/pull/479
[s487]: https://github.com/HorneroOS/shell/pull/487
[s503]: https://github.com/HorneroOS/shell/pull/503
[s505]: https://github.com/HorneroOS/shell/pull/505
[s507]: https://github.com/HorneroOS/shell/pull/507
[s486]: https://github.com/HorneroOS/shell/pull/486
[p63]: https://github.com/HorneroOS/plugins/pull/63
[p64]: https://github.com/HorneroOS/plugins/pull/64
[p65]: https://github.com/HorneroOS/plugins/pull/65
[p66]: https://github.com/HorneroOS/plugins/pull/66
[p67]: https://github.com/HorneroOS/plugins/pull/67
[p68]: https://github.com/HorneroOS/plugins/pull/68
[p69]: https://github.com/HorneroOS/plugins/pull/69
[g44]: https://github.com/HorneroOS/greeter/pull/44
[i98]: https://github.com/HorneroOS/installer/pull/98
[i100]: https://github.com/HorneroOS/installer/pull/100
[w224]: https://github.com/HorneroOS/website/pull/224
[w225]: https://github.com/HorneroOS/website/pull/225
[w226]: https://github.com/HorneroOS/website/pull/226
[w227]: https://github.com/HorneroOS/website/pull/227
[w229]: https://github.com/HorneroOS/website/pull/229
[w230]: https://github.com/HorneroOS/website/pull/230
[d107]: https://github.com/HorneroOS/docs/pull/107
[d108]: https://github.com/HorneroOS/docs/pull/108
[d110]: https://github.com/HorneroOS/docs/pull/110
[d111]: https://github.com/HorneroOS/docs/pull/111
[d113]: https://github.com/HorneroOS/docs/pull/113
[q85]: https://github.com/HorneroOS/qa/pull/85
[q86]: https://github.com/HorneroOS/qa/pull/86
