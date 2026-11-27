# RFC 0002 — Hornero Chromatic

> Traducción al español rioplatense de la
> [versión en inglés](../../development/rfc-0002-hornero-chromatic.md),
> que es la canónica.

- **Estado** — Aceptado (2026-11-17)
- **Implementación** — No iniciada. Nada de este RFC está implementado ni
  validado todavía; ver [Despliegue](#16-despliegue-y-migración).
- **Enmienda** — [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md):
  reemplaza en parte el §1 (la exclusión de la síntesis desde el fondo de
  pantalla), la lista "eliminado sin reemplazo" del §3.1 (variantes, "seguir
  el fondo") y la cláusula "los fondos nunca recolorean la interfaz" del §9.
  Todo lo demás del RFC 0001 sigue vigente: nombres de roles, paletas
  curadas, tipografía, glifos, movimiento, superficies ancladas, Cockpit.
- **Alcance** — Shell (motor, vista previa, Centro de control, PluginKit),
  horneroctl (apply, estado, rollback, salidas), config (esquema, gates,
  plantillas), plugins (plantillas de extensiones), sitio web (presentación
  una vez publicado)
- **Seguimiento** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)
  (misión), [docs#122](https://github.com/HorneroOS/docs/issues/122) (este
  RFC), [shell#525](https://github.com/HorneroOS/shell/issues/525) (motor),
  [shell#526](https://github.com/HorneroOS/shell/issues/526) (UI del shell
  y PluginKit), [hornero#428](https://github.com/HorneroOS/hornero/issues/428)
  (horneroctl), [config#140](https://github.com/HorneroOS/config/issues/140)
  (esquema, gates, plantillas),
  [plugins#70](https://github.com/HorneroOS/plugins/issues/70)
  (extensiones),
  [website#232](https://github.com/HorneroOS/website/issues/232) (sitio web)

## 1. Problema

El RFC 0001 eliminó la maquinaria de Material 3 que el shell heredó de
Caelestia. Fue lo correcto para el lenguaje de diseño y un error para una
capacidad que los usuarios valoraban: un escritorio cuyos colores salen del
fondo de pantalla, con variantes que cambian su carácter. Eliminar Material
Design no debe significar perder el color dinámico.

Hornero Chromatic recupera esa capacidad como un motor propio que produce
**roles de Signal directamente**: el conjunto de roles del RFC 0001 §3.1, el
`glow` opcional y los 16 colores de terminal. Es una **opción**. Los temas
curados Signal Night, Signal Day y Signal High Contrast siguen siendo el
valor de fábrica y el respaldo ante cualquier falla. Los algoritmos de color
y el diseño visual son cosas separadas: Chromatic cambia el matiz y el croma
dentro de la estructura de Signal; no cambia la anatomía, la tipografía, los
glifos, el movimiento ni las superficies.

Restricciones no negociables:

- Nada de roles de Material, widgets o símbolos de Material, capa de
  compatibilidad, ni envolver una biblioteca externa de color de Material
  bajo otros nombres.
- Nada de componentes visuales de Caelestia. Se le reconoce a Caelestia el
  linaje de la funcionalidad; no se copia código de Caelestia.
- Las barras Cockpit Clear se quedan con opacidad cero. Chromatic puede
  cambiar la tinta de primer plano, nunca agregar fondo, tinte, velo ni
  desenfoque.
- Un dueño por cada asunto: horneroctl aplica y escribe el estado; config es
  dueño del esquema de temas, la tabla de gates y las plantillas incluidas;
  el shell es dueño de la presentación (`Signal`) y de la vista previa
  interactiva.
- Un fondo de pantalla nunca debe volver ilegible la interfaz.

## 2. Qué existía antes y qué conservamos

### 2.1 Caelestia (shell y cli)

Estudiado en `caelestia-dots/shell` y `caelestia-dots/cli` `main`
(GPL-3.0):

- **Extracción de semillas** — Caelestia: Python: cuantizador Celebi de 128
  colores sobre una miniatura de 128 px por vecino más cercano, "score" de
  Material (objetivo de croma 48, ponderación por proporción de matiz),
  corrección de colores desagradables; Evaluación: idea probada; RGB/HCT,
  la miniatura por vecino más cercano produce aliasing; una sola semilla
- **Paleta** — Caelestia: las clases de esquema de la biblioteca externa de
  color de Material (tonal spot, vibrant, expressive, fidelity, content,
  fruit salad, rainbow, neutral, monochrome); Evaluación: variantes ricas,
  pero la salida son roles de Material
- **Sabores** — Caelestia: `default` / `hard` (hard oscurece las
  superficies); Evaluación: perilla útil de "profundidad de superficie"
- **Inferencia inteligente** — Caelestia: Modo: promedio Lanczos 1×1 con
  tono > 60 → claro. Variante: colorido de Hasler–Süsstrunk < 10 neutral,
  < 20 content, si no tonal spot; Evaluación: barata; el promedio de un
  solo píxel se confunde con imágenes partidas
- **Terminal / colores con nombre** — Caelestia: tablas fijas de Gruvbox y
  Catppuccin rotadas hacia el matiz de la semilla; Evaluación: buena idea;
  sin verificación de contraste
- **Contraste** — Caelestia: lo que dé el esquema de Material; Evaluación:
  sin gate, sin protección sobre superficies translúcidas
- **Video / GIF** — Caelestia: primer cuadro con `ffmpeg`; GIF cuadro 0;
  Evaluación: los primeros cuadros suelen ser fundidos a negro
- **Vista previa** — Caelestia: el shell lanza la CLI de Python por cada
  vista previa (`wallpaper -p`), parsea JSON, cambia una paleta de vista
  previa; Evaluación: modelo correcto (vista previa en memoria), latencia
  alta
- **Aplicación** — Caelestia: un proceso de Python escribe el estado del
  esquema, Hyprland, GTK, Qt, terminales (OSC a cada `/dev/pts`), muchas
  plantillas de apps, plantillas de usuario (`{{ $role }}`) y después un
  comando de shell arbitrario `postHook`; Evaluación: cobertura amplia;
  escribe en terminales de sesiones de otros usuarios que pueda abrir; los
  hooks de shell son inseguros
- **Caché** — Caelestia: por hash de imagen: miniatura, score, opciones
  inteligentes, esquema por variante/sabor/modo; Evaluación: bueno
- **Analizador del shell** — Caelestia: `ImageAnalyser` en C++ (color
  dominante, luminancia) usado para compensar la transparencia;
  Evaluación: buena semilla nativa para nuestro trabajo

### 2.2 HorneroOS antes de Signal

Antes de shell#475, hornero#421 y config#128:

- El `ThemePipeline.qml` del shell encadenaba varios procesos por cada
  cambio (escritura del puntero con `sh -c`, generación M3 a través de
  horneroctl, sincronización de estado, regeneración de Hyprland,
  `hyprctl reload`, hyprlock, notificaciones). El `ImageAnalyser` nativo
  (en `plugin/src/Hornero`, todavía presente) solo alimentaba una pista de
  luminancia (`WallpaperAnalysis.qml`).
- `smartcolor.v` y `run_m3_synthesis` de horneroctl resolvían un intérprete
  de Python que tuviera instalada la biblioteca externa de Material y
  ejecutaban el `generate-m3-colors.py` de config (tipo de esquema, colores
  de éxito y de terminal armonizados, una verificación de contraste de
  terminal de `terminal_themes.py`). `appearance doctor` fallaba cuando no
  existía ese Python.
- Las salidas eran nombres de roles de Material, así que cada generador
  posterior cargaba con un vocabulario de Material.

### 2.3 Lo perdido, lo débil y lo mejor

- **Capacidad** — Conservado del linaje: semillas desde el fondo,
  variantes, profundidad de superficie, modo/variante inteligentes,
  armonización de terminal, vista previa antes de aplicar, plantillas de
  apps, caché; Débil, no se repite: dependencia de Python + biblioteca
  externa; roles de Material; cadenas de procesos; video solo con el
  primer cuadro; inferencia de modo con un solo píxel; comandos de shell
  `postHook`; escrituras OSC a cada pty; Chromatic lo hace mejor: motor
  nativo usado en el proceso para las vistas previas y por un helper para
  aplicar; roles de Signal producidos directamente; estadísticas
  perceptuales (OKLab); multi-semilla; contraste resuelto por construcción
  y revalidado antes de escribir; opacidad mínima de superficie sobre el
  fondo; salida dorada determinista; aplicación transaccional con rollback

## 3. Decisión de arquitectura

### 3.1 Decisión

**Un motor, escrito una sola vez en C++, en el repositorio del shell.**

- `libs/chromatic/` — una biblioteca estática, C++20, que depende solo de
  Qt6 Core y Gui (`QImage`, `QImageReader`, `QColorSpace`). Es dueña de la
  decodificación, el análisis, la inferencia, la síntesis y el solver de
  contraste.
- `plugin/src/Hornero/Chromatic/` — el módulo QML `Hornero.Chromatic`, que
  enlaza la biblioteca, para vistas previas instantáneas dentro del
  proceso.
- `extras/chromatic/` — el helper `hornero-chromatic`, instalado en
  `/usr/lib/hornero/hornero-chromatic`, que enlaza la misma biblioteca.
  horneroctl lo llama para toda generación que se vaya a aplicar.
- **horneroctl** sigue siendo el único que escribe el esquema vivo
  (`${XDG_STATE_HOME}/hornero/signal/scheme.json`), las salidas de apps
  posteriores, el estado de Chromatic y el historial usado para el
  rollback.
- **config** es dueño de las extensiones del esquema, la tabla de gates y
  las plantillas incluidas. **El shell** es dueño de la presentación de
  `Signal`, la vista previa y la UI del Centro de control.

Los fondos de video se analizan a partir de un único cuadro extraído una
vez por `ffmpeg` (dependencia opcional). Sin `ffmpeg`, una fuente de video
informa `chromatic.source-unreadable` y la paleta actual se mantiene.

### 3.2 Alternativas consideradas

- **Motor en V dentro de horneroctl** — V no tiene decodificadores de
  primera clase para WebP, AVIF, JPEG XL, perfiles ICC ni cuadros
  animados; el shell igual necesitaría una segunda implementación, nativa
  o en JavaScript, para vistas previas con sliders a 60 fps. Dos
  implementaciones se desvían.
- **Motor en QML/JavaScript** — Demasiado lento para decodificar 4K y
  agrupar en el hilo de la GUI; no sirve fuera del shell.
- **Motor en Python (config)** — Reintroduce la dependencia que el RFC 0001
  eliminó; costo de arranque en cada apply.
- **Enlazar el motor en horneroctl mediante una ABI de C** — Mete Qt en
  `horneroctl-bin`; los decodificadores de imágenes correrían dentro del
  proceso que es dueño del estado. Un helper de vida corta aísla los
  cuelgues de los decodificadores alimentados con archivos no confiables.
- **El shell calcula, horneroctl solo guarda la paleta del shell** — Rompe
  el uso por scripts y al iniciar sesión sin un shell corriendo, y vuelve
  al shell un segundo escritor.
- **Un repositorio separado `HorneroOS/chromatic`** — Versionado limpio,
  pero un paquete y un pipeline de releases nuevos durante un congelamiento
  de releases. El helper se distribuye en `hornero-shell`, que ya instala
  binarios en `/usr/lib/hornero`. La extracción sigue siendo posible
  porque la biblioteca no depende de QML.

### 3.3 Consecuencias

- La vista previa y la aplicación usan el mismo decodificador y el mismo
  build de la biblioteca, así que una paleta previsualizada y la aplicada
  son idénticas byte a byte (§13); el resultado trae un `fingerprint` que
  el shell compara después de aplicar.
- horneroctl funciona sin el paquete del shell para los temas curados;
  Chromatic no está disponible (`chromatic.engine-missing`) cuando falta
  el helper.
- Cero Python en la ruta de ejecución. Dependencias nuevas de ejecución:
  ninguna. `ffmpeg` pasa a ser una dependencia opcional de `hornero-shell`.
  `qt6-imageformats` / `kimageformats` opcionales amplían los formatos
  decodificables; no son obligatorios.

## 4. Ciencia del color

Toda la aritmética es de doble precisión IEEE sin fast-math. Los colores
se analizan en **OKLab / OKLCH** (Björn Ottosson, 2020) y se emiten como
sRGB `#RRGGBB`. El contraste usa la luminancia relativa de WCAG 2.x,
exactamente como el `signal_theme.py` de config; la separación de
terminal usa ΔE CIE76 sobre CIELAB D65, también como config, de modo que
el motor y todos los validadores coincidan.

### 4.1 Decodificación

1. Abrir con `QImageReader`; rechazar fuentes de más de 100 megapíxeles o
   con encabezados ilegibles (`source-unreadable`).
2. Usar decodificación escalada donde el formato lo soporte (JPEG) hasta
   un lado mayor de 512 px; si no, decodificar y reducir.
3. Convertir a sRGB mediante el perfil de color embebido
   (`QImage::convertToColorSpace`), para que las fotos Display P3 y
   Adobe RGB se lean correctamente.
4. GIF/WebP/APNG animados: muestrear `n = min(8, frameCount)` cuadros en
   los índices `floor(i × frameCount / n)` para `i = 0 … n−1`; los
   píxeles de todos los cuadros muestreados se juntan con igual peso por
   cuadro. La elección depende solo del archivo, nunca del tiempo
   transcurrido. Un archivo cuya cantidad de cuadros se desconoce usa solo
   el cuadro 0; un cuadro muestreado que falla al decodificar hace fallar
   la fuente (`source-unreadable`) en lugar de omitirse.
5. Video (`.mp4 .mkv .webm .mov .avi`): un cuadro a 1 s (o en 0 cuando el
   video es más corto), escalado a 512 px, extraído con una llamada a
   `ffmpeg` hacia la caché (§15). Nunca más de una vez por identidad de
   archivo; nunca mientras el video se reproduce.
6. Reducir a un lado mayor de **256 px** con un filtro de caja en **luz
   lineal**. Se ignoran los píxeles con alfa < 0.5; la entrada
   premultiplicada se des-premultiplica primero.

### 4.2 Estadísticas

Sobre la imagen de trabajo de 256 px, ponderadas por área, con las bandas
superior e inferior del 8 % (donde viven las barras) con peso 2×:

- Luminosidad: media `L̄`, `Lmin`, `Lmax`, percentiles `L5`, `L50`, `L95`,
  desviación estándar.
- Croma: media, `C90`, `C95`; colorido `Cf = C90`.
- Histograma de matiz: 36 contenedores ponderados por croma; entropía de
  matiz (bits).
- Detalle: laplaciano absoluto medio de L (cantidad de ruido visual).
- Estadísticas de banda para las bandas superior e inferior (L media,
  desviación).
- Una grilla de luminancia de 96 × 54 (media y desviación por celda),
  cacheada para el muestreador de Cockpit Clear
  (signal-visual-language §12.5). La adopción por ClearInk es un
  seguimiento, no un requisito de este RFC.

### 4.3 Cuantización

Determinista, sin aleatoriedad:

1. Construir un histograma de los píxeles de trabajo sobre una grilla sRGB
   de 5 bits por canal (≤ 32 768 contenedores), cada uno guardando
   población y OKLab medio.
2. Inicializar 16 clústeres por **corte por mediana en OKLab** (dividir la
   caja con mayor varianza ponderada por población a lo largo de su eje
   más largo; los empates se resuelven por orden de eje L, a, b).
3. Correr 8 iteraciones de k-means de Lloyd ponderado por población en
   OKLab, en orden de contenedor. Descartar los clústeres vacíos; fusionar
   los clústeres más cercanos que ΔEOK 0.02.

Resultado: hasta 16 clústeres `{oklab, proporción de población}`.

### 4.4 Puntaje de semillas

Para cada clúster con OKLCH `(L, C, h)` y proporción `s`:

```text
score = 0.70 * sqrt(s) * 10
      + 0.30 * min(C, 0.20) / 0.20 * 10
      + 0.10 * hueNeighbourhood(h)     # parte de masa de croma en ±15°
      - 4.0  if C < 0.02               # casi neutro
      - 2.0  if L < 0.15 or L > 0.95   # aplastado o quemado
      - 1.5  if 90° <= h <= 115° and L < 0.60 and C > 0.04
                                       # oliva sucio
```

- **Semilla primaria**: el mayor puntaje con `s >= 0.005` (un objeto
  pequeño y saturado sobre un campo gris igual gana).
- **Semilla secundaria**: el clúster de mayor puntaje cuyo matiz difiera
  del primario al menos 50°.
- **Matiz neutro**: el matiz del clúster más grande con `C >= 0.01`; si no,
  el matiz primario. Las superficies toman este matiz en la variante
  `faithful`.
- **Imágenes acromáticas** (`C90 < 0.025`): si existe el matiz medio
  ponderado por croma de los píxeles con `C > 0.005`, se vuelve el matiz
  de la semilla con croma 0.06; si no, se usan los **matices de la casa de
  Signal** (signal 69°, cue 236°) y `inference.reasons` lo dice.

Se informan hasta cinco semillas ordenadas para que el usuario pueda
elegir otra.

### 4.5 La estructura de Signal es fija

Las paletas curadas son una escalera de luminosidad con temperatura
dividida: Signal Night combina superficies de grafito frío (matiz ≈ 256°)
con tinta cálida (≈ 85°); Signal Day combina papel cálido (≈ 87°) con
tinta fría (≈ 252°). Chromatic conserva la **escalera** (elevación,
niveles de tinta, fuerza de las reglas) y la **temperatura dividida**, y
toma de la imagen **solo el matiz y el croma**. El modelo de referencia de
estas reglas reproduce Signal Night a partir de una semilla ámbar con un
CIE76 ΔE medio de 3.3.

Objetivos de luminosidad OKLCH (antes del solver):

| Rol | Oscuro | Claro |
| --- | --- | --- |
| `ground` | 0.167 | 0.910 |
| `sunken` | 0.189 | 0.877 |
| `base` | 0.203 | 0.950 |
| `panel` | 0.229 | 0.968 |
| `raised` | 0.263 | 0.983 |
| `lifted` | 0.305 | 0.995 |
| `rule` | 0.318 | 0.847 |
| `ruleStrong` | 0.575 | 0.537 |
| `ink` | 0.926 | 0.234 |
| `inkMuted` | 0.739 | 0.443 |
| `inkFaint` | 0.573 | 0.597 |
| `signal` / `cue` | 0.78 / 0.78 | 0.49 / 0.47 |
| `phosphor` / `alert` | 0.80 / 0.70 | 0.47 / 0.50 |
| `*Well` | 0.29 | 0.915 |
| `on*Well` | 0.91 | 0.28 |
| `on*` (sobre rellenos de acento) | 0.18 | 0.995 |

`surfaceDepth: deep` (el sabor "hard" de Caelestia, renombrado) baja la
escalera de superficies oscuras en 0.03 y sube la clara en 0.015 (con
tope en 1.0).

### 4.6 Síntesis de roles

Con matiz primario `hp`, croma `cp`, matiz secundario `hs` (opcional),
matiz neutro `hn` y los parámetros de variante del §6:

- **Superficies** (`ground` … `lifted`, `rule`, `ruleStrong`): matiz `hn`,
  croma `sC × k` con `k` = 0.75, 0.85, 1.0, 1.1, 1.25, 1.3, 1.3, 1.4.
- **Niveles de tinta**: matiz `hn + 180°`, croma `iC` (`ink`) e `iC / 2`
  (`inkMuted`, `inkFaint`).
- **Anclas de estado** conservan su significado en todo fondo: `alert`
  matiz 29° y `phosphor` matiz 150°, cada una rotada hacia `hp` una cuarta
  parte de la diferencia de matiz, con tope en el `harm` de la variante
  (≤ 20°).
- **`signal`**: matiz `hp`, croma `clamp(cp × 1.15, aCmin, aCmax)` limitado
  al gamut sRGB en su luminosidad (`faithful`: `cp` sin escalar).
- **`cue`**: el primer candidato cuyo matiz esté a ≥ 35° de ambas anclas
  de estado y a ≥ 60° de `signal`, en orden: `hs`, `hp + r`, `hp − r`,
  `hp + 180°`, el cue de la casa 236° rotado ≤ 15° hacia `hp`,
  `hp ± 120°` (`r` es la rotación de la variante). Si ninguno califica, el
  candidato más lejano de las anclas.
- **Separación**: `signal` y `cue` se rotan para quedar a ≥ 30° de `alert`
  y `phosphor` (en `faithful` se mueve `alert` en su lugar, dentro de
  10°–45°), de modo que "en vivo" nunca se lea como "error" y "foco"
  nunca se lea como "sano".
- **Wells**: matiz del acento, croma `min(C × 0.32, 0.055)`; **on-wells**:
  croma `min(C × 0.5, 0.085)`; **on-fills**: matiz del acento, croma 0.03
  (oscuro) o blanco neutro (claro).
- `inverse` = `ink`, `onInverse` = `panel`, `inverseSignal` = matiz de
  signal en 0.49 (oscuro) / 0.776 (claro). `focus` = `cue`. `scrim` y
  `shadow` siguen siendo `#000000`.
- **`glow`**: solo en modos oscuros (y nunca `monochrome`,
  `high-contrast`): matiz de signal, luminosidad `signal + 0.05`, croma
  `signal × 1.1` dentro del gamut. Los esquemas claros lo omiten (cae
  a `signal`, y el presupuesto de glow ya desactiva el glow en los temas
  de día).
- **Mapeo de gamut**: mantener L y h, reducir el croma por bisección
  (24 pasos) hasta que el color quede dentro de sRGB.

### 4.7 Solver de contraste

Las superficies nunca se mueven. Los primeros planos se mueven solo en
luminosidad, alejándose de sus fondos, por bisección (30 pasos) hasta que
cada par con gate alcance su mínimo más un **margen de 0.15**:

1. `ink`, `inkMuted`, `signal`, `cue`, `phosphor`, `alert` sobre `sunken`,
   `base`, `panel`, `raised`.
2. `ruleStrong` sobre `base`, `panel`, `lifted` y las superficies de
   texto; `focus` sobre todas las superficies (más estricto que config,
   que aplica gate a `focus` sobre `base`); `inkFaint` 3:1 sobre `base` y
   `panel`. `inkFaint` es decorativo y nunca lleva texto esencial (RFC
   0001 §3.1), por lo que no es un rol de texto en ningún nivel; el piso
   de 3:1 mantiene visibles las marcas decorativas.
3. Cada `on*` sobre su relleno; `onInverse` e `inverseSignal` sobre
   `inverse`.
4. Terminal: normales (1–6) 4.5:1 y brillantes (9–14) 3:1 sobre `base`;
   rojo, verde y amarillo separables (ΔE ≥ 10); cada paso de normal →
   brillante ΔE ≥ 6.

Si un objetivo es inalcanzable al final del rango, el croma baja a 0 y el
color va a la luminosidad extrema, que siempre pasa sobre las superficies
de la escalera. Los mínimos vienen de la tabla de gates de config (§9.3)
y del nivel de contraste (§5.3). El orden del solver es fijo, así que la
salida es determinista.

El modelo de referencia de §4.5–§4.7 se corrió sobre 360 matices de
semilla × 5 cromas × 2 opciones de secundaria × 8 variantes × 2 modos
(11 520 paletas); todas pasaron `signal_theme.py validate` de config. Fue
un modelo de referencia descartable, no el motor que se distribuye; lo
reemplaza el test de propiedades del propio motor (§15).

### 4.8 ANSI 16 de terminal

- 1 rojo = matiz de `alert`, 2 verde = matiz de `phosphor`; 3 amarillo
  85°, 4 azul 255°, 5 magenta 325°, 6 cian 190°, cada uno rotado hacia
  `hp` como máximo el tope `term` de la variante.
- Normales con L 0.77 (oscuro) / 0.48 (claro); brillantes con 0.87 / 0.39
  con 0.85× el croma; croma 0.14 (0.09 `muted`, 0.06 `monochrome`; nunca
  por debajo de lo que necesita el gate de separación).
- 0 = matiz de superficie con L 0.26 / 0.23; 7 y 15 = matiz de tinta; 8 =
  matiz de superficie con L 0.54 / 0.44.
- Después se aplica el paso 4 del solver.

### 4.9 Sobre el fondo de pantalla

Dos salidas protegen la legibilidad donde el fondo se transparenta:

- **`minSurfaceAlpha`**: para cada rol de superficie translúcida, la menor
  opacidad con la que `ink` e `inkMuted` todavía pasan su gate cuando la
  superficie se compone sobre los píxeles más oscuros y más claros del
  fondo (`Lmin`, `Lmax` de la imagen de trabajo, §4.2), de modo que
  ningún parche del fondo pueda bajar el contraste por debajo del límite.
  `Signal` usa `max(opacidad del usuario, minSurfaceAlpha)`.
- **`clearInk`**: los conjuntos de primer plano de Cockpit Clear para
  ambas polaridades (`ink`, `inkMuted`, `signal`, `alert`, `halo`)
  vueltos a dar matiz desde el esquema y resueltos a 4.5:1 contra el halo
  de la polaridad opuesta. ClearInk sigue eligiendo la polaridad por
  región (signal-visual-language §12.1). Esto cambia **solo primeros
  planos**; una barra clear nunca recibe relleno, tinte, velo ni
  desenfoque.

## 5. Inferencia inteligente

Todo valor inferido es un valor por defecto que el usuario puede
sobrescribir; el resultado lista `reasons` (legibles para personas) y una
`confidence` de 0 a 1.

### 5.1 Modo

`L̄` es la luminosidad media ponderada por bandas (§4.2):

- `L̄ < 0.58` → oscuro; `L̄ > 0.68` → claro.
- Entre ambos, se mantiene el modo actual (histéresis, para que una
  carpeta de fondos rotativos no alterne el escritorio), o oscuro cuando
  no hay ninguno.
- Si las bandas superior e inferior discrepan de la imagen completa en más
  de 0.25, deciden las bandas (ahí están las superficies del shell).

### 5.2 Variante

La elección automática se limita a `balanced`, `vibrant`, `expressive` y
`muted`:

| Condición | Variante |
| --- | --- |
| `C90 < 0.025` | `muted` (matices de la casa si la imagen no tiene matiz) |
| `C90 < 0.06` | `balanced` |
| `C90 < 0.12` y dos semillas a ≥ 50°, cada una ≥ 10 % | `expressive` |
| `C90 < 0.12` | `balanced` |
| `C90 >= 0.12` | `vibrant` |

`neon` se **sugiere** (nunca se aplica automáticamente) cuando
`L̄ < 0.30` y `C95 > 0.18` con `L > 0.6`. `faithful`, `monochrome` y
`high-contrast` nunca se sugieren automáticamente.

### 5.3 Nivel de contraste

`standard` (gates de config), `boosted` y `maximum` (§11). Automático:
cuando la transparencia está habilitada y el detalle (§4.2) supera 0.08,
se recomienda `boosted`; la recomendación se muestra, no se aplica, salvo
que el usuario haya puesto el contraste en `auto`.

### 5.4 Personalidad

Una etiqueta corta para la UI construida a partir de la inferencia (por
ejemplo "Oscuro · balanced · ámbar cálido · calmo"), más una clase de
croma (`grey`, `soft`, `rich`, `intense`) y temperatura (`warm` para
matices de semilla de 20°–110°, `cool` para 180°–300°, si no `neutral`).

## 6. Variantes

Las variantes son conjuntos de parámetros para §4.6–§4.8. `sC` croma de
superficie, `iC` croma de tinta, `aC` rango de croma de acento, `r`
rotación del cue, `harm`/`term` topes de matiz.

- `balanced` (por defecto) — Linaje: tonal spot; `sC`: 0.016; `iC`: 0.014;
  `aC`: 0.09–0.15; `r`: 165°; `harm` / `term`: 10° / 10°; Comportamiento:
  carácter de Signal Night/Day con otro matiz; superficies tranquilas, un
  acento confiado
- `vibrant` — Linaje: vibrant; `sC`: 0.028; `iC`: 0.014; `aC`: 0.14–gamut;
  `r`: 165°; `harm` / `term`: 12° / 15°; Comportamiento: acentos más
  fuertes y cromo teñido
- `expressive` — Linaje: expressive, fruit salad, rainbow; `sC`: 0.022;
  `iC`: 0.016; `aC`: 0.11–0.17; `r`: 120°; `harm` / `term`: 20° / 20°;
  Comportamiento: cue triádico salvo que la imagen tenga un segundo matiz;
  colores de estado más armonizados
- `faithful` — Linaje: fidelity, content; `sC`: 0.020; `iC`: 0.012; `aC`:
  croma de la semilla; `r`: 165°; `harm` / `term`: 8° / 8°;
  Comportamiento: `signal` es la semilla misma cuando pasa los gates; las
  superficies toman el matiz dominante de la imagen
- `muted` — Linaje: neutral; `sC`: 0.008; `iC`: 0.008; `aC`: 0.05–0.08;
  `r`: 165°; `harm` / `term`: 5° / 5°; Comportamiento: cromo casi neutro,
  acentos suaves
- `monochrome` — Linaje: monochrome; `sC`: 0; `iC`: 0; `aC`: 0.035; `r`:
  165°; `harm` / `term`: 0 / 0; Comportamiento: cromo y tinta neutros; los
  acentos susurran el matiz de la semilla; los colores de estado conservan
  su significado; sin `glow`
- `high-contrast` — `sC`: 0.006; `iC`: 0; `aC`: 0.12–0.17; `r`: 165°;
  `harm` / `term`: 5° / 5°; Comportamiento: gates `maximum`, fondo más
  profundo, tinta más brillante; sin `glow`; sin translucidez
- `neon` — `sC`: 0.030; `iC`: 0.020; `aC`: 0.16–gamut; `r`: 180°; `harm` /
  `term`: 0 / 0; Comportamiento: solo oscuro (un pedido claro devuelve
  oscuro con un motivo); cue complementario, terminal saturada, `glow` al
  gamut; presupuesto de glow sin cambios

Perillas ortogonales: `surfaceDepth` (`standard` / `deep`), escala de
`chroma` (0.5–1.5, multiplica `sC`, `iC` y `aC`), `hueShift` (−180° a
180°, aplicado a las semillas).

Reglas fijas para toda variante: el presupuesto de glow (enmienda 2 del
RFC 0001), sin glow en las barras Cockpit Clear, movimiento y anatomía
intactos.

## 7. Fuentes

- `wallpaper` (por defecto) — El puntero actual del fondo, por monitor 0
- `image:<path>` — Cualquier archivo de imagen o video
- `seed` — Uno o dos colores manuales (`#RRGGBB`); el primero → `signal`,
  el segundo → `cue`
- `house` — Matices de la casa de Signal; solo el tinte de las superficies
  sigue al fondo (`balanced` "Signal tinted")

Los colores manuales en `faithful` se mantienen exactos cuando pasan; si
no, el resultado lista `adjustments` como `signal #F2E200 → #C9BB00
(contrast on panel)`.

## 8. Esquema vivo y extensiones de temas

Todas las adiciones son opcionales y aditivas; la versión del esquema
sigue en 2 y los lectores existentes las ignoran.

### 8.1 Esquema vivo (`scheme.json`)

```json
{
  "schemaVersion": 2,
  "id": "hornero-chromatic",
  "mode": "dark",
  "palette": { "ground": "#0F1114", "…": "#……" },
  "terminal": ["#……", "… 16 colours"],
  "chromatic": {
    "version": 1,
    "engine": "1.0.0",
    "algorithm": 1,
    "fingerprint": "sha256:…",
    "request": {
      "source": "wallpaper",
      "variant": "balanced",
      "mode": "auto",
      "contrast": "standard",
      "surfaceDepth": "standard",
      "chroma": 1.0,
      "hueShift": 0
    },
    "resolved": {
      "mode": "dark",
      "variant": "balanced",
      "contrast": "standard"
    },
    "seeds": ["#D98A3A", "#3A7FD9"],
    "sourceKey": "sha256:…"
  },
  "minSurfaceAlpha": { "base": 0.82, "panel": 0.86 },
  "clearInk": {
    "light": {
      "ink": "#……", "inkMuted": "#……", "signal": "#……",
      "alert": "#……", "halo": "#……"
    },
    "dark": {
      "ink": "#……", "inkMuted": "#……", "signal": "#……",
      "alert": "#……", "halo": "#……"
    }
  }
}
```

`hornero-chromatic` es un id de tema reservado sin directorio de
catálogo. Los temas curados siguen escribiendo el documento sin los tres
bloques opcionales.

### 8.2 Archivos de tema (`theme.json`)

Una paleta Chromatic guardada es un tema ordinario de esquema v2 en
`${XDG_DATA_HOME}/hornero/themes/<id>/theme.json` con
`collection: "user"` y un objeto opcional de procedencia `chromatic`
(`engine`, `algorithm`, `request`, `seeds`, `createdAt`). Se lista,
aplica, exporta y valida como cualquier tema del catálogo. El
`tokens.schema.json` de config incorpora la propiedad `chromatic` y la
colección `user`; un nuevo `scheme.schema.json` describe el §8.1.

### 8.3 Preferencias (`shell.json`)

Las preferencias del usuario viven en `appearance.chromatic` (esquema del
que es dueño el shell, incluido en `shell.default.json`, resincronizado
hacia config):

```json
{
  "appearance": {
    "theme": "hornero-signal-night",
    "chromatic": {
      "source": "wallpaper",
      "seeds": [],
      "variant": "auto",
      "mode": "auto",
      "contrast": "standard",
      "surfaceDepth": "standard",
      "chroma": 1.0,
      "hueShift": 0,
      "follow": "auto",
      "perMode": {
        "dark": { "variant": "auto" },
        "light": { "variant": "auto" }
      },
      "fallback": {
        "dark": "hornero-signal-night",
        "light": "hornero-signal-day"
      },
      "transition": "smooth"
    }
  }
}
```

Chromatic está activo solo cuando `appearance.theme` es
`hornero-chromatic`. `follow` es `off`, `auto` (recolorear cuando cambia
el fondo) o `ask` (vista previa con un aviso temporizado Aplicar /
Mantener actual). El shell edita estas preferencias; horneroctl las lee.
Un `apply` de horneroctl siempre selecciona Chromatic (pone
`appearance.theme` en `hornero-chromatic`); por defecto además guarda su
pedido en `appearance.chromatic`, y `--no-persist` omite solo esa segunda
escritura, de modo que un pedido puntual por CLI no reemplace las
preferencias guardadas.

## 9. Propiedad

### 9.1 Archivos

- `$XDG_STATE_HOME/hornero/signal/scheme.json` — Dueño: horneroctl;
  Escribe: horneroctl (el shell todavía lo escribe para sus temas
  incorporados, como hoy)
- `$XDG_STATE_HOME/hornero/chromatic/state.json` — Dueño: horneroctl;
  Escribe: horneroctl: último pedido aplicado, fingerprint, marcas de
  tiempo
- `$XDG_STATE_HOME/hornero/chromatic/history/NNNN.json` — Dueño:
  horneroctl; Escribe: horneroctl: anillo de 10 instantáneas para el
  rollback
- `$XDG_CACHE_HOME/hornero/chromatic/` — Dueño: motor; Escribe: helper y
  plugin del shell: análisis, cuadros, paletas (descartable)
- `$XDG_CONFIG_HOME/hornero/chromatic/templates.d/*.json` — Dueño:
  usuario; Escribe: plantillas del usuario (§12.2)
- `/usr/share/hornero/chromatic/templates/` — Dueño: config; Escribe:
  plantillas propias incluidas
- `profiles/themes/contrast-gates.json` — Dueño: config; Escribe: tabla de
  gates (§9.3)
- `shell.json` `appearance.chromatic` — Dueño: shell; Escribe: UI del
  shell; horneroctl con `--persist`

### 9.2 Flujo

```text
Centro de control ─en el proceso─▶ Hornero.Chromatic (vista previa, sin
      │ Aplicar                    escrituras)
      ▼
[horneroctl] appearance chromatic apply ─▶ hornero-chromatic generate
      │                                    (JSON)
      │ validar con la tabla de gates ─ falla → no escribe nada, exit 1
      │ lock → instantánea (esquema, salidas, claves appearance de
      │        shell.json)
      │ renderizar esquema, salidas y shell.json a archivos temporales
      │ rename de scheme.json, salidas y después shell.json
      │ cualquier falla → restaurar cada archivo renombrado desde la
      │                   instantánea
      ▼
Signal (FileView) adopta el esquema con una transición; las apps
recargan de forma nativa
```

### 9.3 Tabla de gates

`profiles/themes/contrast-gates.json` en config es la única fuente de los
pares de contraste y los mínimos por nivel (`standard`, `boosted`,
`maximum`), incluidas las reglas de terminal y de separación. El
validador de config la lee; el motor y horneroctl compilan una copia
vendorizada, y cada repositorio tiene un test de sincronización contra el
archivo vendorizado (el mismo patrón que `shell.default.json`).

## 10. Contrato de horneroctl

Todos los verbos viven bajo `appearance chromatic` de horneroctl. Todo
verbo acepta `--json`; los verbos que escriben aceptan `--dry-run` (no
escribe nada, imprime el plan) y exigen `--yes` cuando no es interactivo.

- `status` — Activo o no, preferencias, último pedido aplicado y
  fingerprint, disponibilidad del helper y de `ffmpeg`
- `analyze [--source …]` — Solo análisis e inferencia
- `preview [request]` — Genera y valida sin escribir; imprime el esquema y
  el informe de gates
- `apply [request] [--no-persist]` — Genera, valida, toma instantánea,
  escribe esquema y salidas, selecciona `hornero-chromatic` en
  `shell.json`; `--no-persist` deja `appearance.chromatic` sin cambios
- `follow` — Reaplica desde el fondo actual cuando Chromatic está activo y
  `follow` es `auto`; si no, un no-op exitoso que informa `skipped`
- `rollback [--steps N]` — Restaura una instantánea anterior (curada o
  Chromatic) por el mismo camino de escritura
- `history` — Lista las instantáneas
- `save --id ID --name NAME` — Guarda el esquema Chromatic actual (o el
  pedido) como tema de usuario
- `export [--output FILE]` — Escribe el esquema actual como archivo de
  tema de esquema v2
- `import FILE` — Valida e instala un archivo de tema como tema de usuario
- `variants` — Variantes con descripciones y parámetros
- `off` — Sale de Chromatic: aplica el tema de respaldo por modo
- `doctor` — Salud del helper, `ffmpeg`, formatos de imagen, caché y
  estado
- `templates list` / `render` / `check` — Inspeccionar, renderizar y
  validar plantillas

Flags del pedido: `--source wallpaper|image:PATH|seed|house`, `--seed HEX`
(repetible, hasta 2), `--variant NAME|auto`, `--mode auto|dark|light`,
`--contrast auto|standard|boosted|maximum`, `--depth standard|deep`,
`--chroma F`, `--hue-shift DEG`. Los flags no especificados vienen de
`appearance.chromatic`.

Los códigos de salida siguen a horneroctl: `0` éxito, `1` falla, `2` uso.
Las fallas traen un `error.code` estable: `chromatic.engine-missing`,
`chromatic.source-unreadable`, `chromatic.gates-failed`,
`chromatic.locked`, `chromatic.write-failed`, `chromatic.state-corrupt`,
`chromatic.template-invalid`.

Reglas:

- `wallpaper set` (y el shell después de un cambio de fondo, con debounce
  de 1.5 s) ejecuta `follow`.
- Un `state.json` o una entrada del historial corruptos se apartan a
  `*.corrupt` y se informan; el esquema vivo nunca queda parcial.
- El lock de aplicación es `$XDG_RUNTIME_DIR/hornero/appearance.lock`; un
  segundo apply falla rápido con `chromatic.locked`.

### 10.1 Contrato del helper

`hornero-chromatic` es un helper interno (no está en el `PATH`); su
interfaz se versiona con `schemaVersion` en su salida.

- `analyze --source PATH [--frames N]` — `{schemaVersion, engine, source,
  analysis, inference}`
- `generate (--source PATH | --seed HEX…) [request flags] [--current-mode
  M]` — `{schemaVersion, engine, request, analysis, inference, scheme,
  gates, adjustments, fingerprint}`
- `validate --scheme FILE [--level L]` — `{schemaVersion, passed, rows}`
- `variants` — `{schemaVersion, variants}`
- `version` — `{schemaVersion, engine, algorithm, qt, formats, ffmpeg}`

Flags comunes: `--cache-dir DIR` (por defecto
`$XDG_CACHE_HOME/hornero/chromatic`), `--no-cache`. Códigos de salida:
`0` ok, `2` uso, `3` fuente ilegible o no soportada, `4` gates
inalcanzables (un bug; se informa, nunca se escribe), `5` error interno.

## 11. Accesibilidad

- Niveles de gate: **standard** = gates de config; **boosted** = `ink`
  7:1, `inkMuted` 5.5:1, `ruleStrong` y `focus` 4.5:1; **maximum** = todo
  rol de texto y todo par on- 7:1, límites 4.5:1.
- `focus` alcanza 3:1 (standard) sobre **todas** las superficies, no solo
  sobre `base`.
- El significado del estado nunca depende solo del matiz (las reglas del
  RFC 0001 siguen vigentes), y los matices de estado están anclados
  (§4.6).
- El interruptor `appearance.highContrast` está **protegido**: siempre
  muestra la tabla curada `hornero-signal-contrast` y desactiva la
  translucidez, sin importar lo que produzca Chromatic. La variante
  `high-contrast` es un aspecto aparte y opcional.
- Las superficies translúcidas respetan `minSurfaceAlpha` (§4.9).
- Reducir movimiento desactiva las transiciones de paleta.
- horneroctl revalida antes de escribir; una paleta que falla nunca se
  aplica.

## 12. Salidas de tema

### 12.1 Adaptadores

horneroctl renderiza cada salida a partir de los roles, tanto para
esquemas curados como Chromatic:

- **Hornero Shell y PluginKit** — Esquema vivo (`Signal`, `Theme.palette`)
- **Hyprland, hyprlock** — Renderizadores existentes de horneroctl
- **alacritty, ghostty, btop, cava** — Renderizadores existentes de
  horneroctl
- **kitty** — Plantilla → `kitty/hornero-chromatic.conf`, cambio de
  include, recarga mediante la señal de recarga de configuración propia de
  kitty
- **GTK 3 / GTK 4 (libadwaita)** — Plantillas → overrides de
  `@define-color` y recoloreo de `gtk-4.0/gtk.css`; árbol de tema GTK
  elegido por modo
- **Qt (qt5ct / qt6ct)** — Plantilla → `qt6ct/colors/hornero-chromatic.conf`,
  edición de línea existente de qt6ct
- **foot, fuzzel, neovim, zed** — Plantillas incluidas (config)
- **Apps de usuario y de extensiones** — Plantillas (§12.2)

Los adaptadores nuevos para salida dinámica son **plantillas** de las que
es dueño config, renderizadas por el motor de plantillas de horneroctl,
así los formatos quedan en config y no se agrega a horneroctl ningún
renderizador escrito a mano.

### 12.2 Mecanismo de plantillas

Una plantilla es un archivo de texto con marcadores; un manifiesto dice
adónde va.

```json
{
  "name": "waybar",
  "template": "waybar.css.tmpl",
  "output": "~/.config/waybar/hornero.css"
}
```

- Marcadores: `{{ ink }}` (`#RRGGBB`), `{{ ink.hex }}`, `{{ ink.bare }}`
  (sin `#`), `{{ ink.rgb }}` (`r, g, b`), `{{ ink.rgba 0.8 }}`,
  `{{ ink.r }}` / `.g` / `.b`, `{{ term3 }}`, `{{ mode }}`, `{{ id }}`.
- Secciones: `{{#dark}}…{{/dark}}`, `{{#light}}…{{/light}}`. Nada más: sin
  bucles, sin expresiones, sin includes, sin ejecución de comandos.
- Los marcadores desconocidos hacen fallar el renderizado; no se escribe
  la salida.
- Las salidas deben resolver bajo `$XDG_CONFIG_HOME`, `$XDG_CACHE_HOME` o
  `$XDG_DATA_HOME` después de resolver symlinks; se escriben de forma
  atómica, con modo 0644.
- Sin hooks. Las recargas existen solo en adaptadores propios.
- Las extensiones declaran `theme.templates` en el manifest v3; sus
  salidas van solo a `$XDG_CACHE_HOME/hornero/themes/ext/<extension-id>/`,
  renderizadas por horneroctl, nunca por la extensión.

## 13. API del shell y de PluginKit

### 13.1 `Hornero.Chromatic` (módulo QML)

- `ChromaticEngine` (singleton): `available`, `engineVersion`,
  `analyse(source) → ChromaticJob`, `generate(request) → ChromaticJob`,
  `contrast(a, b) → real`, `ensureContrast(fg, bg, min) → color`.
- `ChromaticRequest` (objeto de valor): `source`, `seeds`, `variant`,
  `mode`, `contrast`, `surfaceDepth`, `chroma`, `hueShift`, `currentMode`.
- `ChromaticJob`: `running`, `cancel()`, señales `finished(result)` y
  `failed(code, message)`. Un job cancelado nunca emite.
- `ChromaticResult`: `scheme` (objeto JS con la forma del §8.1),
  `analysis`, `inference`, `gates`, `adjustments`, `fingerprint`.

El trabajo corre en un pool de hilos; los resultados de análisis se
cachean en memoria (LRU, 8 fuentes) y en disco (§15). Un cambio de slider
vuelve a sintetizar a partir del análisis cacheado.

### 13.2 `Signal`

- `beginPreview(scheme)`, `commitPreview()`, `cancelPreview()`,
  `previewing`. La vista previa cambia solo la paleta en memoria. Cancelar
  restaura la paleta anterior; no se escribe nada.
- Transiciones: los cambios de paleta interpolan en OKLab durante como
  máximo 240 ms en como máximo 12 pasos, una notificación por paso;
  instantáneas con reducir movimiento, modo gaming, alto contraste o
  `transition: "instant"`.
- `chromatic` (solo lectura): `active`, `variant`, `mode`, `seeds`,
  `fingerprint`; `minSurfaceAlpha` y `clearInk` se consumen internamente.

### 13.3 Centro de control

Una sección Apariencia → Chromatic: selector de fuente (fondo, imagen,
color, casa de Signal), chips de semillas ordenadas, galería de
variantes, modo, contraste, profundidad de superficie, sliders de croma y
matiz, preferencias por modo, política de seguimiento y un tablero de
muestras (tira de barra, popout, notificación, fila del lanzador,
botones, muestra de terminal, muestra de botón GTK, informe de gates).
Acciones: Aplicar, Cancelar, Guardar como tema, Exportar, Importar,
Rollback. Construida con el kit de controles Bezel existente; sin
componentes visuales nuevos.

### 13.4 PluginKit

`Theme.palette` ya sigue el esquema vivo. Adiciones: `Theme.chromatic`
(estado de solo lectura, sin ruta del fondo), `Theme.revision` (se
incrementa en cada cambio de paleta, para canvases), `Theme.contrast(a,
b)` y `Theme.ensureContrast(fg, bg, min)` para colores guiados por datos.
Las extensiones no pueden correr el motor sobre imágenes arbitrarias en
esta versión.

## 14. Presupuestos de rendimiento

Medidos en el runner de CI por `chromatic-bench`; el CI falla a 3× el
presupuesto.

- **Decodificar + analizar JPEG 4K** — ≤ 60 ms
- **Decodificar + analizar PNG 4K** — ≤ 150 ms
- **Síntesis + solver desde análisis cacheado** — ≤ 2 ms
- **Helper de punta a punta con acierto de caché** — ≤ 20 ms
- **`apply` con acierto de caché, sin recargas de GTK ni Hyprland** —
  ≤ 150 ms
- **Paso de transición de paleta (offscreen, shell completo)** — ≤ 2 ms de
  trabajo de bindings
- **Memoria pico del helper, fuente 4K / 8K** — ≤ 96 MB / ≤ 220 MB
- **Costo en reposo** — Cero: sin timers, sin watchers más allá del
  watcher del esquema existente

Nunca: análisis continuo de video, análisis al iniciar el shell (el shell
lee el último esquema), regeneración cuando el pedido y la identidad de la
fuente no cambiaron.

## 15. Determinismo, caché y tests

- **Determinismo**: los mismos bytes de fuente y el mismo pedido producen
  JSON idéntico byte a byte del mismo build, entre corridas y cantidades de
  hilos. Los resultados entre arquitecturas pueden diferir como máximo
  ΔEOK 0.005 por rol (se verifica en CI cuando hay una segunda
  arquitectura disponible).
- **Claves de caché**: `sourceKey = sha256(content digest, algorithm)`,
  donde el content digest es el SHA-256 de los bytes del archivo (para
  archivos de más de 64 MiB, en la práctica videos: del tamaño más los
  primeros y últimos 4 MiB). Ruta, tamaño y mtime son solo un índice
  rápido hacia un digest guardado y nunca se confía en ellos solos; un
  archivo cambiado con el mismo tamaño y mtime se detecta porque un acierto
  vuelve a hashear el archivo antes de reutilizar. Clave de paleta =
  `sha256(analysis digest, canonical request, algorithm)`. Las entradas
  llevan su propio digest; una discrepancia o falla de parseo borra la
  entrada y recalcula. Tope de tamaño 64 MB, poda LRU al escribir.
  La caché nunca es obligatoria: `--no-cache` da el mismo resultado.
- **Corpus**: generado por el arnés de tests, sin blobs binarios — negro,
  blanco, gris medio, ruido, división complementaria 50/50, punto saturado
  de 0.3 % sobre gris, neón sobre negro, pastel en clave alta, sepia,
  dominado por piel, oliva sucio, gradiente de matiz, dominado por rojo
  (colisión con alert), dominado por verde (colisión con phosphor), PNG
  semitransparente, PNG de 16 bits, JPEG CMYK, JPEG Display P3, GIF
  animado con cuadros distintos, 1×1, tira de 16384×1, archivo truncado,
  archivo vacío, y un video generado cuando existe `ffmpeg` — más los
  fondos acreditados del catálogo de config.
- **Archivos dorados**:
  `tests/chromatic/golden/<case>__<variant>__<mode>.json`; todo cambio
  sube `algorithm` y se revisa.
- **Tests de propiedades**: corpus × 8 variantes × 2 modos × 3 niveles de
  contraste × 64 semillas manuales deterministas → todo gate pasa, la
  separación se mantiene, y `signal_theme.py validate` de config acepta
  cada esquema.
- **horneroctl**: tests de despacho con un helper falso, inyección de
  fallas en cada rename (estado restaurado), contención de lock, estado y
  caché corruptos, dry-run no escribe nada, ida y vuelta del rollback.
- **Shell**: la vista previa y la cancelación no escriben nada (árbol XDG
  aislado), reducir movimiento desactiva las transiciones, los píxeles de
  la barra Cockpit Clear son iguales a los del fondo, se respeta
  `minSurfaceAlpha`.
- **VM de QA**: un escenario de aplicación sobre cuatro clases de fondo
  (oscuro, brillante, detallado, gris) con capturas; sin afirmaciones
  sobre el host sin evidencia del host.

## 16. Despliegue y migración

1. RFC (este documento) e issues de seguimiento.
2. Biblioteca del motor, helper y corpus dorado (shell#525).
3. Verbos de horneroctl, esquema de config, tabla de gates y plantillas
   (hornero#428, config#140).
4. Vista previa del shell, transiciones, Centro de control, PluginKit
   (shell#526), después plantillas de extensiones (plugins#70).
5. Evidencia en la VM de QA; texto del sitio web solo después del release
   (website#232).

Migración: ninguna requerida. Las selecciones existentes conservan sus
ids de tema y siguen funcionando; Chromatic está apagado hasta que un
usuario lo elija. Los curados Signal Night / Day / High Contrast siguen
siendo el valor de fábrica. Las selecciones migradas por el RFC 0001 no
se vuelven a color dinámico automáticamente; Bienvenida y el Centro de
control ofrecen Chromatic como opción.

## 17. Atribución

- El linaje de la funcionalidad — semillas desde el fondo, variantes,
  sabores, modo y variante inteligentes, plantillas de apps — viene de
  [Caelestia](https://github.com/caelestia-dots) (GPL-3.0). Chromatic es
  una implementación nueva: no se copian código ni tablas de Caelestia.
  El `NOTICE` y el `docs/PROVENANCE.md` del shell conservan su atribución
  a Caelestia y registran este linaje.
- OKLab y OKLCH: Björn Ottosson, "A perceptual color space for image
  processing" (2020); se usan las matrices de conversión publicadas.
- Luminancia relativa y razón de contraste de WCAG 2.x (W3C).
- El corte por mediana (Heckbert, 1982) y el k-means de Lloyd son
  algoritmos de manual.
