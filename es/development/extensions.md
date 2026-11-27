# Extensiones: guía de autoría para PluginKit 3

> Traducción al español rioplatense de la
> [versión en inglés](../../development/extensions.md), que es la canónica.

**Desarrollo.** Las extensiones de Hornero Shell son paquetes QML que la shell
descubre, carga en su propio `Loader` y renderiza en la barra, el dashboard,
el lanzador, el escritorio o en Ajustes. Desde noviembre de 2026 en las ramas
`main` de Shell y Plugins se escriben contra **PluginKit 3**, el contrato de
extensiones de Hornero Signal. Esta página es el punto de entrada del manual
para autoras y autores: indica qué se publicó, qué cambió desde Extensions 2.0
y qué no se verificó todavía en un escritorio en vivo. No es la referencia de
API.

La implementación es dueña del contrato, y esta página enlaza a ella en vez de
copiarlo:

- Contrato de la shell, manifiesto, PluginKit y validadores:
  [`HorneroOS/shell` `docs/PLUGINS.md`][shell-plugins], el
  [esquema JSON de manifiesto][shell-schema] y el validador de la shell en
  `scripts/validate_plugin.py` en ese repositorio.
- Flujo de catálogo de primera parte y gate de calidad:
  [`HorneroOS/plugins` `docs/DEVELOPING.md`][plugins-developing],
  [`docs/CONTRIBUTING.md`][plugins-contributing] y
  [`docs/SECURITY.md`][plugins-security].
- Autoridad de diseño: [RFC 0001](rfc-0001-hornero-signal.md) y
  [Signal Visual Language](signal-visual-language.md). Las reglas de popups,
  foco y movimiento están en el
  [contrato de interacción](interaction-contract.md).
- Ciclo de vida por línea de comandos: la propia ayuda de la CLI para la
  familia de comandos `plugin`. La página del manual para esos comandos se
  sigue por separado en [HorneroOS/docs#45][docs-45]; hasta que aterrice,
  tratá la ayuda de la CLI como autorizada y esta página como resumen.

Donde una guía enlazada y esta página discrepen, gana el contrato de la shell
para el comportamiento del manifiesto y PluginKit, y gana la ayuda de la CLI
para la sintaxis de comandos.

> **Cambio disruptivo.** PluginKit 3 quita de cuajo la API de la era Material.
> La shell publicada carga únicamente manifiestos con `"schemaVersion": 3` y
> rechaza `1` y `2` con un puntero a los pasos de migración. No hay capa de
> compatibilidad. Los paquetes escritos para Extensions 2.0 necesitan la
> migración mecánica descripta en
> [Migrar desde PluginKit 1 y 2](#migrar-desde-pluginkit-1-y-2).

## Leé primero el modelo de confianza

El QML de extensiones corre **en proceso dentro de Quickshell con los permisos
del usuario que inició sesión. No está en sandbox.** Ningún campo del
manifiesto cambia eso:

- `capabilities` (`processCommands`, `networkHosts`, `providers`, `settings` y
  la lista `actions` del broker abajo) son declaraciones para revisión
  mostradas antes del consentimiento. No son una concesión de permisos del
  sistema operativo y la shell no las impone sobre el QML en ejecución.
- Los validadores estáticos rechazan paquetes mal formados y un conjunto
  conservador de patrones sospechosos. Pasar la validación no es una
  certificación de seguridad, y los chequeos textuales pueden esquivarse con
  código dinámico.
- El componente `Settings` de PluginKit selecciona un espacio de nombres por
  `pluginId`. Ese ID no prueba la identidad de quien llama y no aísla una
  extensión de otra.
- Instalar un paquete copia datos inertes. Habilitar es una acción separada de
  consentimiento explícito, y habilitar revalida el payload instalado. Leé el
  código fuente antes de habilitar una extensión comunitaria.
- Nunca distribuyas credenciales, helpers con privilegios, binarios compilados
  ni configuración personal dentro de un paquete de extensión.

Existe un límite real, y es acotado: las llamadas hechas **mediante el broker
tipado de capacidades de la CLI** (los comandos de acciones de plugin en la
ayuda de la CLI) corren solo cuando el paquete es propiedad de recibo, está
habilitado y es confiable, cuando la acción está declarada en
`capabilities.actions` y cuando la política ABAC de la CLI lo permite. Las
llamadas mutantes al broker también necesitan confirmación explícita y cada
decisión de corrida del broker queda registrada en log de auditoría. El broker
gobierna solo las llamadas hechas a través de él. No mete en sandbox, observa
ni restringe el propio QML de la extensión.

## Qué se publicó y qué no

| Área | Estado |
| --- | --- |
| Manifiesto `schemaVersion` 3 | Única versión que el host carga |
| `background`, `bar`, `dashboard`, `desktop` | Alojados |
| Superficies `launcher` y `settings` | Alojadas |
| UI generada de ajustes | Alojada en Centro de control |
| Widgets de escritorio (libres) | Alojados; modo edición, por pantalla |
| Deck de instrumentos Signal | Seis widgets en modo Signal |
| Proveedores compartidos y `Telemetry` | Alojados, una fuente por dominio |
| Capturas, paquete instalado | Mostradas, sin correr código |
| Capturas, aún sin instalar | Solo epígrafe, sin imagen local |
| `compatibility` en Marketplace | Metadatos de revisión, no bloquea |
| Panel catálogo comunitario | Solo lectura; ciclo de vida en CLI |
| Clave producto registro comunitario | Sin publicar; falla cerrado |
| Interruptores por usuario y superficie | Todavía no forma parte del contrato |

El catálogo oficial tiene **36 extensiones, todas portadas a PluginKit 3**
(mirá [El catálogo oficial](#el-catálogo-oficial)).

### Todavía sin verificar en un escritorio en vivo

Los contratos de abajo están cubiertos por pruebas unitarias, de host, de
esquema y QML offscreen en los repositorios de shell, CLI y plugins. Eso no es
lo mismo que aceptación gráfica, y esta página no la afirma:

- Ninguna extensión de PluginKit 3 se validó todavía en la máquina virtual de
  QA ni en un escritorio físico. El puerto de las 36 extensiones del catálogo,
  los widgets de instrumentos y el deck Signal están verificados por
  validadores, pruebas de esquema y QML offscreen, no por un render capturado.
- El layout de contexto de host entre bordes de barra, pantallas y escalas de
  salida está probado por contrato, todavía no verificado en una sesión de
  compositor multi-monitor en vivo.
- El comportamiento de teclado está conducido por una sonda QML offscreen.
  Todavía hace falta una sesión en ejecución para verificar capturas de foco
  en vivo del compositor y anuncios de lector de pantalla (AT-SPI).
- El argumento de costo en reposo de los proveedores compartidos es análisis
  estático fijado por pruebas, no una medición de energía o wakeups en host;
  lo mismo aplica al costo en reposo por modo del deck.
- La auditoría de calidad de primera parte (mirá
  [Gate de calidad](#gate-de-calidad)) actualmente clasifica **toda**
  extensión del catálogo como `needs-upgrade`. La auditoría es estática; un
  puerto fusionado a PluginKit 3 es código publicado, no una afirmación de
  listo para producción ni de aceptación gráfica.

## Forma del paquete

Un directorio por extensión, que contiene exactamente `manifest.json` más cada
archivo listado en el arreglo `files` del manifiesto:

- el `entrypoint` QML declarado (y un punto de entrada por cada superficie
  adicional),
- `README.md` y `LICENSE` para todo lo que distribuyas,
- catálogos de traducción e imágenes de vista previa, cuando estén declarados.

Las rutas son relativas al paquete y no pueden escapar de él. Se rechazan
enlaces simbólicos, binarios compilados o bytecode, bits setuid/setgid,
archivos escribibles por cualquiera y archivos ejecutables. La superficie de
imports de extensiones es acotada a propósito: módulos públicos de Qt Quick y
Quickshell más `Hornero.PluginKit`. Los imports desde la implementación interna
de Hornero se rechazan.

## Manifiesto v3

`"schemaVersion": 3` es el único valor aceptado. Conserva las formas de
identidad, `surfaces`, `capabilities`, `translations` y `marketplace` que
introdujo el manifiesto v2 y suma las reglas Signal alrededor: los dominios de
datos que leés se declaran en `capabilities.providers`, los íconos son nombres
de Hornero Glyph y los colores salen de `Theme.palette`. Los campos
desconocidos, nombres de superficie desconocidos y versiones de esquema
desconocidas se rechazan. La referencia canónica campo por campo es el
[contrato de la shell][shell-plugins] y el [esquema JSON][shell-schema]; el
resumen de abajo sirve de orientación.

- Identidad requerida: `id`, `name`, `version`, `description`, `author`,
  `license`, `entrypoint` en nivel superior y `files`.
- `placement` elige la superficie primaria: `background` (sin interfaz, por
  defecto), `bar`, `dashboard` o `desktop`.
- `surfaces` mapea nombres de superficies adicionales a su propio
  `entrypoint`, con un indicador opcional de defecto de manifiesto `enabled`
  (por defecto `true`), para que un paquete pueda renderizar en varios
  lugares. Redeclarar la superficie primaria se permite solo con el mismo
  `entrypoint` que el par de nivel superior.
- La superficie `dashboard` puede sumar una pista `size` (`compact`,
  `standard` o `wide`) y una etiqueta corta de agrupación `category`. Ambos
  son pistas; la disposición persistida del dashboard del usuario manda.
- La superficie `desktop` puede sumar pistas de geometría: `width`, `height`,
  `minWidth`, `minHeight` (80 a 1600 píxeles lógicos), `resizable` y `anchor`
  (una de nueve posiciones iniciales).
- `capabilities` declara `processCommands` (nombres base exactos de
  ejecutables), `networkHosts`, `providers`, `settings` tipados y la lista
  opcional `actions` del broker. Sub-declarar un proceso, host o proveedor que
  tu código realmente usa es un fallo en revisión.
- Los bloques opcionales `translations` y `marketplace` se cubren abajo.

### Tipos de superficie

| Superficie | Dónde se renderiza |
| --- | --- |
| `bar` | Grupo final de la barra; abrí paneles con `UiPopover` |
| `dashboard` | Tarjeta en la pestaña Extensions del dashboard |
| `desktop` | Widget de escritorio en cada pantalla |
| `background` | Sin interfaz; declarala solo si se justifica |
| `launcher` | Consulta oculta y fila de resultado en el lanzador |
| `settings` | Pestaña propia en Centro de control junto a la generada |

El contrato del lanzador es un `Item` raíz con un string asignable `query` y un
`result` de solo lectura de la forma `{ ok, text }`. El prefijo es el id del
plugin sin `hornero-` adelante, y activar un resultado copia su texto. La
superficie `settings` se ubica junto a la UI generada de ajustes, que ya
renderiza `capabilities.settings` sin ella. Ambas corren en proceso con la
misma confianza que cualquier otra superficie.

### Contexto de host y layout adaptable

La misma extensión debe renderizar en una barra horizontal, un riel vertical,
una tarjeta del dashboard y un widget de escritorio. Declará cualquiera de las
propiedades de contexto del host en tu ítem raíz de entrada — orientación,
borde, superficie, ancho y alto disponibles, indicador compacto y nombre de
pantalla — y el host las mantiene enlazadas a la superficie real. No declarar
ninguna no cambia nada. Dale a las propiedades valores por defecto acordes a tu
layout actual, respetá los topes de tamaño disponible en lugar de fijar
tamaños, y dejá que el componente de pila adaptable de PluginKit apile los
controles en superficies angostas o verticales. Los nombres exactos de
propiedades, tipos y topes por superficie están en el
[contrato de la shell][shell-plugins].

## El tema Signal

`Theme` lleva exactamente los tokens Signal de la shell, bajo los mismos
nombres que usa la shell. Nunca fijes a mano un color, fuente, tamaño ni
duración.

- **Roles de color**, `Theme.palette.<role>`: superficies `ground`, `sunken`,
  `base`, `panel`, `raised`, `lifted`; texto `ink`, `inkMuted`, `inkFaint`;
  líneas `rule`, `ruleStrong`, `focus`; acentos `signal` (ámbar), `cue`
  (celeste), `phosphor` (verde) y `alert` (rojo), cada uno con sus compañeros
  `on…` y `…Well`; más `inverse`, `scrim`, `shadow` y `glow`.
- **Tipografía**, `Theme.font.family.sans`, `.mono` y `.display` (IBM Plex
  Sans, Mono y Sans Condensed), y `Theme.font.size.<small…display>`.
- **Forma y ritmo**: `Theme.rounding.small`, `.normal`, `.large`;
  `Theme.spacing.*`; `Theme.padding.*`.
- **Movimiento**: `Theme.duration(name)`, `Theme.anim.curves.*`,
  `Theme.motionLevel` y `Theme.reducedMotion`; mirá el
  [contrato de interacción](interaction-contract.md).
- **Estado**: `Theme.light`, `Theme.highContrast`, `Theme.experience` (el
  [modo de experiencia](../desktop/experience-modes.md) activo),
  `Theme.glowEnabled`, `Theme.scanlines`, `Theme.telemetryIntervalMs` y
  `Theme.keyboardFocus`.

El lenguaje es deliberado. `signal` significa *en vivo, activo o primario* y
`cue` significa *foco, selección o información*. Los números usan cifras
tabulares. Los paneles son `panel` con borde de 1 px `rule` y radio chico,
nunca píldoras ni vidrio. `inkFaint` es solo decorativo. Nada parpadea ni
pulsa, y el halo (`glow`) nunca se dibuja a mano: lo aplican los componentes
de instrumentos, únicamente mientras se cumpla `Theme.glowEnabled`.

### Hornero Glyphs

Los íconos son **nombres de Hornero Glyph**: el subconjunto curado de contorno
de Tabler Icons incluido en la shell, en kebab-case, por ejemplo `wifi`,
`clock`, `calculator`, `wave-sine` o `player-play`. Los usan
`UiIcon { name }`, `glyph` en botones, filas, chips, tarjetas y filas de
detalle, el `icon` de un proveedor del lanzador y el tercer argumento de
`Notifications.toast()`. Los glifos son solo contorno, así que no hay eje de
relleno; mostrá el estado con color o con un chip on-air. El validador
comprueba los nombres contra la lista vendored (`schema/hornero-glyphs.names`
en el repositorio plugins) y rechaza nombres desconocidos y de estilo Material
antes de instalar. En tiempo de ejecución un nombre desconocido no dibuja
nada. Pedí un glifo faltante en un issue de Shell en lugar de incluir una
fuente de íconos.

## PluginKit de un vistazo

El paquete de la shell instala el módulo QML estable `Hornero.PluginKit` para
que las extensiones nunca importen internos de la shell:

```qml
import QtQuick
import Hornero.PluginKit
```

- **Tu propio estado:** `Settings` (valores tipados declarados en el
  manifiesto), `Translations` (los catálogos de tu paquete) y `Desktop`
  (estado de widget en solo lectura).
- **Aspecto y respuesta:** `Theme` (arriba) y `Notifications.toast()` para un
  toast acotado dentro de la shell. Un toast no es una notificación persistente
  de escritorio.
- **Fachadas de datos:** `System`, `Network`, `Media`, `Weather`, `Time`,
  `Power`, `Audio` y `Workspaces`, más el historial compartido `Telemetry` para
  instrumentos. Son de solo lectura excepto transporte de medios, volumen y
  silencio de audio, y foco de espacio de trabajo, que pertenecen solo a
  manejadores iniciados por el usuario. No hay ejecución de procesos ni shell
  en PluginKit, y no se expone ninguna cuota de IA: nunca muestres una cuota
  supuesta como conocida.
- **Primitivas de UI:** texto, eyebrow, ícono, tarjeta, pozo, botón,
  interruptor, deslizador, métrica, fila de detalle, fila de acción, chip,
  progreso, marcador de estado, tooltip, popover y la pila adaptable, más los
  componentes de instrumentos `UiSegmentMeter`, `UiMeterRow`, `UiSparkline`,
  `UiScope` y `UiPartition`. Usan tokens de `Theme`, declaran nombres
  accesibles y muestran foco visible.

Las propiedades y métodos exactos viven en el
[contrato de la shell][shell-plugins]. Construí contra esa página y el módulo
instalado, no contra este resumen.

### Proveedores y permisos

Las fachadas son presentación sobre **proveedores** compartidos de instancia
única: una fuente propiedad de la shell por dominio, para que muchas
extensiones que leen el mismo dominio nunca dupliquen sus temporizadores,
lecturas de archivo ni procesos hijos. Dos reglas:

- **Declará lo que leés.** Listá cada dominio en `capabilities.providers`
  (`system`, `network`, `spectrum`, `weather`, `media`, `time`, `power`,
  `audio`, `workspaces`). El validador rechaza una fachada o suscripción cuyo
  dominio no declare el manifiesto. Como toda capacidad, es divulgación para
  revisión, no imposición.
- **Arrendá dominios con sondeo.** `system` y `network` son los dominios con
  sondeo; `spectrum` es un stream. Mantené un `Subscription { domain: "…" }`
  mientras tu superficie esté cargada. Cada dominio con sondeo tiene un único
  temporizador controlado por conteo de referencias, así que diez suscriptores
  cuestan uno. La cadencia sigue la experiencia activa (1 Hz, 2 Hz en Signal).
  En Focus y Gaming la capa de escritorio no carga widgets, así que toda
  concesión se libera.

`weather` está cacheado (una búsqueda compartida por ubicación, cada hora);
`media`, `time`, `power`, `audio` y `workspaces` son orientados a eventos. Los
valores nunca se inventan: un sensor faltante informa una bandera de
disponibilidad en falso (`System.cpuTempAvailable`, `Power.hasBattery`, …), y
vos renderizás "no disponible", nunca cero. Sin concesión, el sondeo se
detiene y las lecturas devuelven los últimos valores conocidos. Preferí una
señal de fachada o `Subscription` antes que tu propio temporizador sub-segundo.

### Widgets de escritorio y el deck Signal

Una superficie `desktop` es un widget en la capa de escritorio de cada
pantalla. El host es dueño del **módulo**: relleno `panel`, borde de 1 px
`rule`, sombra y encabezado eyebrow (`02 · SYSTEM INSIGHT`). Tu ítem raíz puede
declarar `widgetTitle` y `widgetContext` para ese encabezado, y dibuja solo su
contenido en la caja del host (`hostAvailableWidth` por
`hostAvailableHeight`). Dentro de un widget, `UiCard` no dibuja un segundo
marco.

Las personas mueven y redimensionan widgets en modo edición (`qs ipc call
plugins editDesktop`), ajustados a una grilla de 8 px y guardados por
pantalla. El código del plugin puede leer geometría mediante `Desktop` pero no
tiene setter. Los widgets viven debajo de las ventanas y nunca quitan foco de
teclado a las aplicaciones.

Qué contiene la capa de escritorio depende del
[modo de experiencia](../desktop/experience-modes.md). Everyday y Studio
muestran los widgets que habilitó la persona; Signal muestra el **deck** curado
de seis instrumentos (System Insight, Network Scope, Audio Deck, Calendar,
Agenda y Moon Phase), cargado desde paquetes de primera parte instalados cuyo
payload es confiable, sin habilitarlos en Extensiones; Focus y Gaming no cargan
ninguno. Construí instrumentos desde ventanas de `Telemetry` y `UiScope`,
`UiSparkline` y `UiSegmentMeter`, y dejá que el host aplique el halo: las
trazas toman prestado de un presupuesto único de toda la shell de tres ítems.

## Esquema de ajustes

Declará ajustes una vez, bajo `capabilities.settings`, indexados por IDs en
camelCase. Cada declaración es un `type` más un `default`, con un
`description` opcional orientado al usuario y las restricciones de su tipo:

| Tipo | Restricciones | Control generado |
| --- | --- | --- |
| `boolean` | — | Interruptor |
| `integer` | `minimum`, `maximum` | Spin box (+ slider si acotado) |
| `number` | `minimum`, `maximum` | Spin box (+ slider si acotado) |
| `string` | `minLength`, `maxLength` | Campo de texto |
| `enum` | `options` (requerido) | Un botón de opción por valor |

El conjunto de tipos es cerrado. Deliberadamente no hay tipo ruta: los ajustes
son valores planos propiedad de la shell, nunca rutas del sistema de archivos
que la shell abra. El Centro de control genera un campo validado y accesible
por teclado por cada ajuste declarado, con reinicio por campo y un reinicio
general confirmado, leyendo y escribiendo el mismo almacenamiento que el
componente `Settings` de PluginKit. Declará ajustes y frená ahí; no necesitás
código de ajustes. Una superficie personalizada `settings` es opcional y
aparece junto a la UI generada.

Las actualizaciones nunca reescriben valores almacenados. Un valor almacenado
se revalida contra la declaración vigente en cada lectura: uno que todavía
cumple su declaración sigue funcionando, y cualquier otra cosa (un tipo
cambiado, una opción enum quitada, un rango ajustado) se lee como el valor por
defecto declarado en lugar de coercionarse o fallar. Renombrar una clave crea
un ajuste nuevo con su propio valor por defecto.

## Traducciones

Un paquete distribuye sus propias traducciones como catálogos JSON planos, sin
paso de compilación. Declará el locale fuente (el idioma escrito en tu QML),
los locales que incluís y opcionalmente un directorio (por defecto
`translations`). Cada catálogo es un objeto plano `<directorio>/<locale>.json`
que mapea strings fuente a traducciones, y cada catálogo debe figurar en
`files`.

Leé strings mediante `Translations` de PluginKit, mantené oraciones completas
como unidades traducibles únicas con marcadores estilo `%1`, y formateá fechas
y números con sus formateadores conscientes del locale. La resolución sigue el
locale de la shell (sistema), prueba la etiqueta completa luego su idioma, y
si no vuelve a los strings fuente. Un catálogo faltante o mal formado degrada
al texto fuente; nunca hace fallar la extensión. Dos reglas sorprenden a
autores que vienen del código de la shell:

- No uses `qsTr()` en QML de extensiones. La shell no instala ningún traductor
  Qt para extensiones, así que nunca traduciría; el validador lo rechaza. Los
  catálogos compilados `.qm` también se rechazan.
- Un locale declarado debe estar completo para strings literales: cada literal
  pasado a la llamada de traducción necesita una entrada no vacía con los
  mismos marcadores en cada catálogo declarado. Diseñá para expansión de texto
  en lugar de anchos fijos; la línea base de toda la organización es
  [inglés primero](i18n.md).

## Contrato de accesibilidad y teclado

La UI de extensiones sigue las mismas reglas que la UI nativa de la shell.
Usar los controles de PluginKit te da el contrato gratis; los ítems
interactivos hechos a mano deben proveerlo por su cuenta. Las reglas de
popups, Escape y movimiento están en el
[contrato de interacción](interaction-contract.md).

- Todo control interactivo expone un nombre accesible y rol. Dale un nombre
  explícito a controles solo de ícono o ambiguos, y nombrá siempre un
  deslizador según lo que ajusta.
- El orden de Tab es el orden de declaración, una parada de tabulación por
  control, y los controles deshabilitados no son paradas de tabulación. Enter,
  Return y Space activan; flechas en deslizadores, teclas de página, Home y End
  siguen el comportamiento del kit.
- Escape descarta primero el transitorio más interno: tooltip, luego popover y
  después la superficie debajo. Cerrar un popover devuelve el foco a su
  disparador; nunca dejes el foco en un ítem oculto.
- El foco debe ser visible. Usá los controles del kit o dibujá una indicación
  igual de visible con `Theme.palette.focus`; el estilo de hover solo no es
  foco.
- El movimiento reducido y el alto contraste se heredan del host. Enrutá tus
  propias duraciones de animación mediante `Theme.duration(...)`.
- Un clic solo con mouse sin ruta por teclado es una violación del contrato.
  El validador de la shell imprime una advertencia de accesibilidad para
  acciones solo con mouse, y quienes revisan tratan las nuevas advertencias
  como bloqueantes.

## Metadatos del marketplace

Un bloque opcional `marketplace` permite que el Centro de control describa un
paquete sin ejecutar su código: `screenshots` estáticas (imágenes planas
`.png`, `.jpg`, `.jpeg` o `.webp` incluidas en `files`, con texto `alt`
accesible), un rango de compatibilidad `compatibility` de versión de shell, un
`changelog` del más nuevo al más viejo y un aviso `deprecation` con un ID de
reemplazo opcional. La vista de detalle también explica las capacidades
declaradas en lenguaje llano junto a las declaraciones crudas, y el panel
Extensiones muestra chips de compatibilidad y madurez.

Los límites honestos importan al escribir estos metadatos:

- Una entrada del catálogo aún no instalada no tiene payload local, así que sus
  capturas aparecen solo como epígrafes. Las imágenes se renderizan después de
  instalar el paquete.
- `compatibility` se muestra a los usuarios; no impide que cargue un paquete
  fuera de rango.
- La deprecación advierte y deja de ofrecer nuevas instalaciones de esa
  entrada del catálogo. Nunca deshabilita ni quita una copia instalada, y la
  vuelta atrás queda en el contrato verificado de CLI existente, no en estos
  metadatos.
- Las capturas deben ser tomas reales de la shell en ejecución. El arte
  generado debe etiquetarse como obra gráfica, nunca presentarse como captura.

## Ciclo de vida

La CLI es dueña de instalar, actualizar, confiar, habilitar, deshabilitar y
quitar. La shell descubre paquetes que la CLI informa como instalados y
habilitados, y el Centro de control es una superficie más acotada: puede
confiar y habilitar con confirmación explícita, mientras que instalar,
actualizar y quitar siguen siendo acciones de CLI. Leé los flags exactos desde
la ayuda de la CLI; la página de comandos del manual se sigue en
[HorneroOS/docs#45][docs-45]. La forma estable en la que cada autor y usuario
puede confiar es:

1. **Crear plantilla** fuera del catálogo con `horneroctl plugin new`, o copiá
   la plantilla inicial del repositorio plugins para un envío de primera
   parte. Verificá la plantilla contra la versión actual de esquema antes de
   empezar.
2. **Validar** el directorio del paquete estáticamente antes de que algo lo
   instale (mirá [Validar y probar](#validar-y-probar)).
3. **Instalar** copia únicamente datos inertes del paquete. Nada carga y nada
   corre (`horneroctl plugin install-local` para un directorio local,
   `horneroctl plugin catalog` para el catálogo oficial).
4. **Confiar** registra confianza explícita para el payload actual donde no
   aplica ya procedencia revisada. Un cambio en el payload invalida la
   confianza registrada, y se requiere consentimiento de nuevo.
5. **Habilitar** (`horneroctl plugin enable`) revalida primero el payload
   instalado; ante un fallo la extensión queda deshabilitada. Solo cargan
   extensiones habilitadas.
6. **Cargar** instancia cada superficie habilitada en su propio `Loader`, así
   que un fallo queda confinado a esa extensión. El estado de carga, los
   diagnósticos y una recarga por extensión son visibles en el Centro de
   control y mediante el IPC de estado de plugins de la shell.
7. **Deshabilitar** descarga la extensión y libera sus concesiones de
   proveedores. **Quitar** borra el paquete propiedad de recibo. Actualizar por
   catálogo conserva el payload previo para que la ruta de vuelta atrás de la
   CLI pueda restaurarlo.

El catálogo oficial se explora e instala mediante los comandos de catálogo de
la CLI, con el SHA-256 del payload y la revisión fijada verificados desde el
catálogo del repositorio plugins antes de copiar nada. El listado comunitario
es de solo lectura: la shell muestra entradas solo después de que la CLI
verifica la firma desacoplada del registro, falla cerrada cuando faltan la
clave, la firma, el índice o la herramienta de verificación, y una firma
verificada prueba publicación por ese registro, no que HorneroOS haya revisado
el código. El panel comunitario no instala, actualiza, habilita ni revierte
entradas.

Una advertencia operativa del contrato de la shell: los cambios fusionados de
la shell llegan a una sesión en vivo únicamente mediante la shell empaquetada.
Un checkout de git no es lo que ejecuta una sesión corriendo salvo que
Quickshell se haya iniciado explícitamente con esa configuración, así que
revisá qué configuración corre tu sesión antes de culpar a una extensión por
comportamiento viejo del host.

## El catálogo oficial

El catálogo `HorneroOS/plugins` lista **36 extensiones oficiales**, cada una un
paquete PluginKit 3 con confianza `official` (revisado por mantenedores de
HorneroOS, fijado por commit y SHA-256, igual sin sandbox). Por superficie
primaria:

- **Widgets de escritorio (6):** Agenda, Audio Deck, Calendar, Moon Phase,
  Network Scope, System Insight. Estos seis forman el deck Signal. Calendar y
  Agenda muestran datos de fecha y el mes; no tienen datos de eventos porque
  PluginKit no tiene fuente de calendario, y lo aclaran.
- **Barra (18):** Base Converter, Battery, Calculator, Color Converter, Date
  Calculator, Countdown, Dual Clock, JSON Tools, Metronome, Microphone, Now
  Playing, Pomodoro, Stopwatch, Studio Audio, Text Tools, Unit Converter,
  Uptime y Volume.
- **Dashboard (12):** AI Usage, Disk Usage, Focus Card, Network Monitor, Quick
  Notes, Quiet Notes, Studio Jobs, Sun Card, System Health, System Monitor,
  Weather y World Clock.

Varios paquetes suman una segunda superficie (por ejemplo una tarjeta de
dashboard o una entrada de lanzador para los conversores y calculadoras). Usá
`horneroctl plugin catalog --json` para la lista en vivo, con el id, versión,
categoría, capacidades declaradas y hash del payload de cada entrada. El
índice del catálogo es generado y nunca se edita a mano.

## Expectativas de rendimiento y modo seguro

Los presupuestos de rendimiento son diagnósticos informativos, nunca imposición:
QML en proceso no puede ser interrumpido preventivamente, así que superar un
presupuesto se señala, no se castiga.

- Una carga que toma más de 2000 ms desde el descubrimiento o recarga hasta
  cargada/fallida se señala como carga lenta.
- Cinco o más intentos de carga en 60 segundos se señalan como agitación de
  carga.
- El validador advierte (nunca falla) sobre un intervalo literal de `Timer`
  menor a 1000 ms, porque los temporizadores internos de extensiones no son
  observables en tiempo de ejecución. El sondeo sub-segundo es tu olor a
  corregir.
- Los fallos de carga y recargas se guardan en un registro acotado de
  diagnósticos con valores que parezcan credenciales redactados antes de
  guardarse o mostrarse. Los diagnósticos nunca necesitan llevar secretos.

Escribí ajustándote al presupuesto igual: suscribite a proveedores compartidos
en lugar de armar tu propio sondeo, mantené chicos los puntos de entrada y
dejá que las tarjetas del dashboard carguen asincrónicamente. Cuando una
extensión vuelve inutilizable a la shell, el modo seguro es la ruta de
recuperación: iniciada con modo seguro activo, la shell no parsea ningún
manifiesto de extensión ni instancia ningún QML de extensión, así que el panel
Extensiones (del núcleo de la shell) sigue alcanzable para deshabilitar el
paquete roto. El modo seguro en sí nunca habilita, deshabilita ni quita nada,
y no mete en sandbox un plugin que corre normalmente.

## Ejemplo completo: un reloj de dos superficies

Este paquete completo es un reloj de manifiesto v3: una superficie primaria
`bar` que oculta su día de la semana en superficies compactas, una tarjeta
`dashboard` sobre el proveedor compartido `system`, un ajuste tipado
renderizado por la UI generada de ajustes y un catálogo en español. No declara
capacidad de proceso, red ni broker. Está modelado sobre los paquetes de
referencia de la shell (`examples/plugins/example-clock` y
`examples/plugins/example-multi-surface` en el repositorio de la shell). El
validador de la shell pasó sobre este conjunto exacto de archivos en el commit
`8cab8d0` de Shell; eso es un aprobado estático, no un render.

### `manifest.json`

<!-- markdownlint-disable MD013 -->

```json
{
  "schemaVersion": 3,
  "id": "example-worked-clock",
  "name": "Example Worked Clock",
  "version": "1.0.0",
  "description": "PluginKit 3 example: bar clock plus dashboard card.",
  "author": "Example Author",
  "license": "MIT",
  "entrypoint": "Main.qml",
  "placement": "bar",
  "surfaces": {
    "dashboard": {
      "entrypoint": "Dashboard.qml",
      "size": "standard",
      "category": "Examples"
    }
  },
  "translations": {
    "sourceLocale": "en",
    "locales": ["es"],
    "directory": "translations"
  },
  "files": [
    "Main.qml",
    "Dashboard.qml",
    "README.md",
    "LICENSE",
    "translations/es.json"
  ],
  "capabilities": {
    "processCommands": [],
    "networkHosts": [],
    "providers": ["time", "system"],
    "settings": {
      "twentyFourHour": {
        "type": "boolean",
        "default": true,
        "description": "Show the time in 24-hour format instead of 12-hour AM/PM."
      }
    }
  }
}
```

<!-- markdownlint-enable MD013 -->

### `Main.qml` (superficie primaria de barra)

```qml
import QtQuick
import Hornero.PluginKit

Item {
    id: root

    // Contexto de host: declarar una propiedad opta a que el host
    // la mantenga enlazada a la superficie real.
    property bool hostCompact: false

    implicitWidth: label.implicitWidth + Theme.spacing.small * 2
    implicitHeight: label.implicitHeight

    Settings {
        id: pluginSettings
        pluginId: "example-worked-clock"
    }

    Translations {
        id: i18n
        pluginId: "example-worked-clock"
    }

    // Un UiButton real, no un MouseArea solo de mouse: parada Tab,
    // activación Enter/Space, foco visible y descripción accesible
    // vienen de PluginKit. Time.date se actualiza cada segundo, así
    // que no hace falta ningún Timer.
    UiButton {
        id: label
        anchors.centerIn: parent
        variant: "quiet"
        glyph: "clock"
        text: i18n.formatDateTime(Time.date,
            pluginSettings.value("twentyFourHour", true)
                ? (root.hostCompact ? "HH:mm" : "ddd, HH:mm")
                : (root.hostCompact ? "h:mm ap" : "ddd, h:mm ap"))
        tooltipText: i18n.tr("Clock details")
        onClicked: Notifications.toast(
            i18n.tr("Worked Example Clock"),
            i18n.tr("Today is %1").arg(
                i18n.formatDateTime(Time.date, "dddd, d MMMM")),
            "clock")
    }
}
```

### `Dashboard.qml` (superficie de dashboard)

```qml
import QtQuick
import Hornero.PluginKit

UiCard {
    title: i18n.tr("Worked Example")
    channel: "01 · CLOCK"

    // La concesión mantiene vivo el único timer system compartido
    // mientras esta tarjeta está cargada; no crea timer propio.
    Subscription { domain: "system" }

    Settings {
        id: pluginSettings
        pluginId: "example-worked-clock"
    }

    Translations {
        id: i18n
        pluginId: "example-worked-clock"
    }

    UiMetric {
        label: i18n.tr("Current time")
        value: i18n.formatDateTime(Time.date,
            pluginSettings.value("twentyFourHour", true)
                ? "HH:mm" : "h:mm ap")
    }
    UiMeterRow {
        label: i18n.tr("CPU")
        value: System.cpuPerc
        valueText: Math.round(System.cpuPerc * 100) + "%"
    }
}
```

### `translations/es.json`

Cada string literal de arriba aparece una vez, preservando marcadores:

```json
{
  "CPU": "CPU",
  "Current time": "Hora actual",
  "Today is %1": "Hoy es %1",
  "Worked Example": "Ejemplo completo",
  "Clock details": "Detalles del reloj",
  "Worked Example Clock": "Reloj del ejemplo completo"
}
```

### `README.md` y `LICENSE`

El README dice qué hace el paquete, cómo validarlo e instalarlo y repite la
nota de confianza. Mantenelo honesto:

```markdown
# Example Worked Clock

A PluginKit 3 example: a bar clock plus a dashboard card over the shared
`time` and `system` providers, one typed setting, and a Spanish catalog.
It starts no processes and contacts no network hosts.

Quickshell QML is not sandboxed and runs with your user permissions.
Validation is a review aid, not a security guarantee. Read the source
before enabling any extension.
```

Incluí el texto completo de tu licencia elegida como `LICENSE` (este ejemplo
usa MIT, coincidiendo con el campo `license` del manifiesto).

### Validá el ejemplo

Desde un checkout del repositorio shell, apuntá el validador al directorio del
paquete (mirá [Validar y probar](#validar-y-probar) para el equivalente de CLI
y qué prueba y qué no prueba un aprobado):

```sh
python3 scripts/validate_plugin.py path/to/example-worked-clock
```

Esperado: una línea de aprobado para el paquete, con el aviso permanente de
que la validación es una ayuda estática de revisión y los plugins de Quickshell
no están en sandbox.

## Migrar desde PluginKit 1 y 2

Portar es mecánico porque el validador rechaza cada nombre quitado con su
reemplazo. La tabla completa está en el [contrato de la shell][shell-plugins];
en líneas generales:

1. Fijá `"schemaVersion": 3` y declará `capabilities.providers`.
2. Los colores pasan a roles: `Theme.primary` a `Theme.palette.signal`,
   `secondary` a `cue`, `tertiary` y `success` a `phosphor`, `error` a `alert`,
   superficies a `base`, `panel`, `raised` y `lifted`, y `onSurface` a `ink`.
3. Los tokens pasan a grupos: `Theme.spacing.small`, `Theme.rounding.normal`,
   `Theme.font.family.sans`, `Theme.font.size.*` y `Theme.duration("medium")`.
4. Los íconos pasan a nombres de Hornero Glyph: `UiIcon { icon }` a `name`,
   `iconName` a `glyph`, sin eje de relleno.
5. Variantes: `ghost` pasa a `quiet`; `tonal` y `outlined` pasan a `secondary`;
   tono de chip `primary` pasa a `signal` y `error` pasa a `alert`. No hay
   ondulaciones (ripples).

## Validar y probar

Corré cada gate que aplique adónde vivirá el paquete. Ninguno renderiza tu
extensión:

1. **Validador de la shell** (cualquier paquete): el script validador nombrado
   arriba, corrido contra el directorio del paquete desde un checkout de shell.
   El comando de validación de plugins de la CLI corre el mismo contrato y es
   el que hay que usar en un sistema instalado; leé su forma exacta desde la
   ayuda de la CLI.
2. **Gate del catálogo de plugins** (envíos de primera parte): el validador del
   repositorio plugins revisa cada paquete del catálogo, el inventario de
   procedencia y la auditoría de calidad, y CI verifica que el catálogo
   generado esté al día y que ningún manifiesto heredado pase. Los payloads de
   catálogo y el índice generado se commitean en pasos separados; seguí
   [`docs/DEVELOPING.md`][plugins-developing] para ese flujo.
3. **Una shell real**: instalá inerte, habilitá con consentimiento, luego
   confirmá que la extensión aparezca en el IPC de estado de plugins de la
   shell y ejercitá cada superficie, ajuste y ruta de teclado a mano. Un
   aprobado del validador más un listado IPC prueban carga, no que la UI sea
   correcta, accesible en uso ni barata en reposo.
4. **La máquina virtual de QA** para cualquier cosa visual: el repositorio QA
   corre un guest descartable y registra capturas. Registrá dónde corrió cada
   chequeo (offscreen, máquina virtual o host).

Decile a quienes revisan cuáles de estos corriste realmente. "Validado" nunca
debe escribirse como "probado en un escritorio" cuando solo corrieron gates
estáticos.

## Gate de calidad

El catálogo de primera parte lleva una auditoría de calidad mantenida por
extensión en el repositorio plugins. Cada extensión oficial se clasifica
(`premium-ready`, `needs-upgrade`, `consolidated` o
`deprecated-with-replacement`) y se puntúa en tooltips, accesibilidad,
traducción, ajustes, tokens de tema, orientación, estados de carga/error,
rendimiento y capturas. Las dimensiones que un script puede decidir se sondean
desde el payload y la auditoría debe coincidir exactamente con la sonda, así
que la auditoría no puede sobre-afirmar ni quedar vieja en silencio.
`premium-ready` requiere además una revisión gráfica registrada. Las
dimensiones fallidas o sin verificar son advertencias por defecto y errores en
el modo estricto del gate.

Estado actual, dicho con claridad: las 36 extensiones del catálogo están
clasificadas `needs-upgrade`, y la auditoría dice en su propio descargo que es
estática y no aceptación gráfica. Tratá "premium" en esta guía como la vara
contra la cual escribir — primitivas de PluginKit, ajustes tipados,
traducciones, nombres accesibles, tokens Signal, proveedores compartidos,
declaraciones honestas de capacidades — no como un estado con el que se haya
certificado alguna extensión publicada.

## Lista de verificación para autores

- Manifiesto v3 con `files` exactos, un README y un archivo de licencia; sin
  binarios, enlaces simbólicos ni bits ejecutables.
- Cada proceso, host, proveedor, ajuste y acción de broker que usa tu código
  está declarado; nada está sub-declarado.
- UI construida con primitivas de PluginKit y roles `Theme.palette`, nombres
  Hornero Glyph y sin nombres de la era Material, con nombres accesibles, foco
  visible y ruta por teclado para cada acción de puntero.
- Contexto de host respetado; sin colores, duraciones ni tamaños de superficie
  fijos a mano; el layout sobrevive superficies compactas y verticales.
- Los popups usan `UiPopover` y `UiTooltip`; el movimiento colapsa en el nivel
  `off`; nada se anima en reposo.
- Datos leídos mediante proveedores compartidos con una concesión de
  suscripción; sin temporizadores sub-segundo ni sondeo por extensión; sensores
  no disponibles mostrados como no disponibles.
- Strings visibles para el usuario mediante `Translations`, con un catálogo
  completo para cada locale declarado y formateo consciente del locale.
- Metadatos de marketplace, cuando están presentes, usan capturas reales.
- El validador de la shell pasa; el gate de catálogo pasa para envíos de
  primera parte; el ejercicio en shell en vivo y máquina virtual se registra
  por separado de los resultados estáticos.

## Referencias

- [Contrato de extensiones de la Shell][shell-plugins]: manifiesto, PluginKit,
  Theme, superficies, ajustes, traducciones, proveedores, widgets de
  escritorio, diagnósticos.
- [Esquema JSON de manifiesto][shell-schema]: el contrato cerrado de campos.
- [Guía de desarrollo de plugins][plugins-developing],
  [guía de contribución][plugins-contributing] y
  [modelo de seguridad][plugins-security]: flujo de catálogo, procedencia, gate
  de calidad y contexto de firma.
- [Contrato de interacción](interaction-contract.md),
  [Signal Visual Language](signal-visual-language.md) y
  [RFC 0001](rfc-0001-hornero-signal.md) en este manual.
- [Pruebas](testing.md) e [Internacionalización](i18n.md) en este manual.
- [HorneroOS/docs#45][docs-45]: página pendiente del manual para las familias
  de comandos `plugin` y `assistant` de la CLI.

[shell-plugins]: https://github.com/HorneroOS/shell/blob/main/docs/PLUGINS.md
[shell-schema]: https://github.com/HorneroOS/shell/blob/main/schemas/plugin-manifest.schema.json
[plugins-developing]: https://github.com/HorneroOS/plugins/blob/main/docs/DEVELOPING.md
[plugins-contributing]: https://github.com/HorneroOS/plugins/blob/main/docs/CONTRIBUTING.md
[plugins-security]: https://github.com/HorneroOS/plugins/blob/main/docs/SECURITY.md
[docs-45]: https://github.com/HorneroOS/docs/issues/45
