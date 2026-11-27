# RFC 0003 — Superficies de contribución de PluginKit

> Traducción al español rioplatense de la
> [versión en inglés][canonical], que es la canónica.

- **Estado** — Propuesta (2026-11-17)
- **Implementación** — Parcial. La sección 12 indica, por punto de
  contribución, qué está fusionado, qué está en revisión y qué no comenzó. No
  se afirma aquí nada como publicado salvo que la sección 12 lo diga.
- **Enmienda** — [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md) §5b
  (PluginKit 3: superficies, proveedores compartidos). Todo lo demás sigue
  vigente.
- **Alcance** — Shell (PluginKit, servicio `Plugins`, hosts, Centro de control ›
  Extensiones, `scripts/validate_plugin.py`, esquema de manifiesto), plugins
  (espejo del validador, generador de catálogo), horneroctl (sin cambios:
  delega la validación del manifiesto al validador de la Shell)
- **Seguimiento** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)
  (misión), requisito K1/K2 en la matriz de misión

## 1. Problema

PluginKit 3 (`apiLevel` 3) permite que un paquete renderice en seis lugares:
ítem de barra, tarjeta del dashboard, widget de escritorio, fondo, proveedor de
lanzador y pestaña personalizada de ajustes. Es un buen comienzo y no es una
plataforma:

1. Un widget es **una instancia por plugin**. Dos relojes, dos osciloscopios de
   red o dos tarjetas de notas con ajustes distintos son imposibles, porque la
   geometría, el anclaje, los ajustes y el estado de carga están todos indexados
   por el id del plugin.
2. Los ajustes son cinco tipos escalares. No hay color, lista ni selección
   múltiple, texto multilínea, ruta, agrupación, paso ni unidad, ni forma de
   ver el efecto de un cambio antes de salir del panel.
3. Una extensión no puede agregar un panel del Centro de control, un mosaico de
   ajuste rápido, una acción con nombre que pueda invocar una fila del
   lanzador, un atajo de teclado o un script, una fuente de notificaciones ni un
   elemento de pantalla de bloqueo. Esas funciones están codificadas fijas en
   la Shell o son imposibles.
4. No hay historia de versionado menor a una ruptura de `schemaVersion`:
   agregar un campo hoy implica que validadores y hosts viejos rechacen el
   paquete por "campo desconocido", lo cual es correcto pero no le da al autor
   nada contra qué apuntar.

El objetivo de producto (brief de usuario, 2026-11-17) es uno de los
escritorios Linux más extensibles: un núcleo sobrio y APIs de extensión
estables y reutilizables en lugar de funciones fijas en código, con todo
personalizable desde el Centro de control (AGENT-RULES §6).

## 2. Principios

1. **Contribuir, no parchar.** Una extensión suma a una superficie con nombre
   mediante un contrato tipado. Nunca edita archivos de la Shell, nunca toca
   internos de la Shell y nunca necesita una release de la Shell para
   aparecer.
2. **Primero declarativo, después código.** Todo lo que la Shell pueda mostrar
   sin correr código de la extensión (nombres, glifos, ajustes, vistas previas,
   listas de acciones, metadatos de mosaicos) se declara en `manifest.json`, se
   valida estáticamente y se renderiza sin instanciar el paquete. El código se
   carga de forma perezosa, por superficie, solo cuando esa superficie está en
   pantalla o es invocada.
3. **Un solo modelo de ajustes.** Toda superficie de una instancia lee los
   mismos ajustes tipados; el Centro de control los renderiza; el usuario puede
   restablecer cualquiera de ellos.
4. **El fallo queda local.** Una superficie fallida marca fallida solo a esa
   superficie de esa instancia. Nunca bloquea al host, a otra instancia, a otra
   extensión ni a la UI de recuperación.
5. **Seguridad honesta.** QML corre dentro del proceso como el usuario y no está
   en sandbox (`docs/PLUGINS.md` › Trust boundary). Esta RFC no pretende otra
   cosa. Agrega *consentimiento y visibilidad* (lo que contribuye una extensión
   se lista y se conmuta individualmente) y *contención* (presupuestos,
   aislamiento de fallos, modo seguro); no suma ninguna vía nueva para correr
   código fuera del contrato existente ni ningún privilegio nuevo.
6. **Aditivo.** Nada en `apiLevel` 3 cambia de significado. Un paquete que no
   usa ninguna de las funciones nuevas queda idéntico byte a byte.

## 3. Versionado y retrocompatibilidad

- `schemaVersion` sigue en **3**. Versiona la *estructura* del manifiesto (y
  Signal), y romperlo se reserva para una reescritura como el paso de Material
  a Signal.
- `PluginKitInfo.apiLevel` pasa a **4** ("Platform"): el nivel de capacidad del
  kit instalado. Es el único número que compara el host.
- Un nuevo campo opcional del manifiesto, **`pluginKit`** (entero, por defecto
  `3`), es el `apiLevel` mínimo que necesita el paquete. El validador deriva el
  nivel que realmente requiere un manifiesto a partir de las funciones que usa
  (sección 4 y 5) y rechaza un manifiesto que use una función de nivel 4
  declarando `pluginKit` menor a 4 u omitiéndolo. Los autores no pueden
  sub-declarar.
- Host: `Plugins.requiredKitLevel` mantiene el piso para alojar cualquier cosa
  (3). Un paquete cuyo `pluginKit` supera el `PluginKitInfo.apiLevel` resuelto
  se rechaza con el mensaje llano existente "actualizá el paquete
  hornero-shell", como estado por paquete (`failed`), no un bloqueo global del
  kit.
- Shells viejas (`apiLevel` 3) rechazan un manifiesto que contenga `pluginKit`
  como campo de nivel superior desconocido (regla existente "se rechazan los
  campos desconocidos"). Ese es el fallo buscado: el paquete no se puede
  instalar donde no puede correr, y `horneroctl` lo informa mediante el
  validador de la Shell al que ya delega. El catálogo registra el nivel por
  paquete para que el registro oculte lo que una Shell dada no pueda correr.
- Deprecación: un punto de contribución o campo se marca deprecado durante al
  menos un `apiLevel` antes de quitarse; el validador advierte, el host sigue
  funcionando. No hay ninguna remoción planificada.

## 4. La matriz de puntos de contribución

"Superficie" es dónde aparece; "Contrato" es qué provee la extensión; "Carga"
es cuándo corre su código. Nivel es el `apiLevel` que lo introdujo.

- **1. `bar` (ítem de barra)** — Superficie: isla de barra; Contrato: `Item`
  `surfaces.bar`; contexto de host; `section` opcional; Carga: siempre mientras
  está habilitada; Multi-instancia: por pantalla (existente); Nivel: 3; Estado:
  Publicado
- **2. Popover / popup** — Superficie: anclada al ítem de barra o widget;
  Contrato: `UiPopover` / `UiTooltip` desde la superficie de barra o
  escritorio; no es una superficie aparte; Carga: con su superficie anfitriona;
  Multi-instancia: sigue al host; Nivel: 3; Estado: Publicado
- **3. `desktop` (widget de escritorio)** — Superficie: capa de escritorio;
  Contrato: `Item` `surfaces.desktop`, pistas de geometría; Carga: mientras
  está habilitada y el modo lo permite; Multi-instancia: **Sí** (instancias);
  Nivel: 3, instancias 4; Estado: Instancias: esta RFC
- **4. Tarjeta `dashboard`** — Superficie: Dashboard › Extensiones; Contrato:
  `Item` `surfaces.dashboard`, `size`, `category`; Carga: mientras el
  dashboard está abierto; Multi-instancia: Sí (instancias); Nivel: 3, instancias
  4; Estado: Instancias: seguimiento
- **5. Sección `settings`** — Superficie: Centro de control › Extensiones;
  Contrato: generada desde el esquema tipado; `Item` personalizado opcional
  `surfaces.settings`; Carga: mientras la sección está expandida;
  Multi-instancia: por instancia; Nivel: 3; Estado: Publicado; esquema v2 nivel
  4
- **6. Proveedor `launcher`** — Superficie: Lanzador; Contrato: contrato
  `query` / `result`; Carga: oculta, mientras está habilitada; Multi-instancia:
  No; Nivel: 3; Estado: Publicado
- **7. `contributes.commands`** — Superficie: filas del lanzador, IPC, atajos
  de teclado, scripts; Contrato: `{id, title, glyph, keywords}` declarados más
  un manejador `surfaces.commands` `run(actionId, args)`; Carga: manejador
  cargado en la primera invocación; Multi-instancia: No; Nivel: 4; Estado: Esta
  RFC
- **8. `contributes.quickSettings`** — Superficie: interruptores rápidos de
  Utilidades, resumen del Centro de control; Contrato: mosaico declarado
  `{id, title, glyph, kind}` más un `Item` `surfaces.quickSetting` que expone
  `checked`/`state` y `toggle()`; Carga: mientras el mosaico está colocado;
  Multi-instancia: No; Nivel: 4; Estado: Esta RFC
- **9. `contributes.panels`** — Superficie: navegación del Centro de control
  (grupo Extensiones); Contrato: `{id, title, glyph}` declarado más un `Item`
  `surfaces.panel`; Carga: solo mientras el panel está abierto;
  Multi-instancia: por instancia; Nivel: 4; Estado: Esta RFC
- **10. Fuente de notificaciones** — Superficie: centro de notificaciones;
  Contrato: un id de fuente y un `post({summary, body, glyph, urgency,
  actions})` tipado a través de PluginKit; agrupado y consciente de DND por el
  host; Carga: fondo; Multi-instancia: No; Nivel: 5; Estado: Diseñado, sin
  iniciar
- **11. Slot de sesión / pantalla de bloqueo** — Superficie: bloqueo,
  superficies adyacentes al greeter; Contrato: tarjeta declarativa de solo
  lectura (subconjunto `UiMetric`) renderizada por el host, nunca código de
  extensión en la superficie de bloqueo; Carga: nunca en bloqueo;
  Multi-instancia: No; Nivel: 5; Estado: Diseñado, sin iniciar; ver 7.5
- **12. Hooks** — Superficie: eventos de Shell (cambio de modo, bloqueo,
  despertar, espacio de trabajo); Contrato: suscripciones declaradas entregadas
  a `surfaces.background` como señales en una fachada `Hooks`; Carga: fondo;
  Multi-instancia: No; Nivel: 5; Estado: Diseñado, sin iniciar
- **13. Plantillas de tema** — Superficie: horneroctl theme apply; Contrato:
  `theme.templates` (existente); Carga: solo CLI; Multi-instancia: No; Nivel:
  3; Estado: Publicado
- **14. Página `dashboardTab` (`shell#709`)** — Superficie: pestaña superior
  del Dashboard; Contrato: `contributes.dashboardTabs` `{id, title, glyph}` más
  un `Item` `surfaces.dashboardTab`; clave estable `<pluginId>:<tabId>`, Loader
  perezoso aislado por fallos, enlace profundo
  `qs ipc call drawers dashboardTab <key>`; Carga: mientras la pestaña (o una
  vecina) está seleccionada; Multi-instancia: No (máx. 2 páginas por paquete);
  Nivel: 5; Estado: Publicado (`shell#710`); primer consumidor
  `hornero-ai-usage` página Agents

Fundamento del orden. Las filas 3 y 5 (instancias y el esquema de ajustes) son
el multiplicador: cualquier otra contribución resulta más útil una vez que una
extensión puede configurarse por instancia con controles reales. Las filas 7 a
9 son los tres contratos más pequeños que quitan funciones fijas en código. Las
filas 10 a 12 requieren una revisión de seguridad propia y quedan fuera de este
paquete a propósito.

### 4.1 Metadatos declarados: `contributes`

Las contribuciones de las filas 7 a 9 se declaran en un objeto opcional del
manifiesto para que la Shell, el Centro de control, el lanzador y el catálogo
puedan listarlas sin correr código:

```json
"pluginKit": 4,
"contributes": {
  "actions": [
    { "id": "startFocus", "title": "Start focus session",
      "glyph": "player-play", "keywords": ["pomodoro", "timer"] }
  ],
  "quickSettings": [
    { "id": "focus", "title": "Focus timer", "glyph": "hourglass",
      "kind": "toggle" }
  ],
  "panels": [
    { "id": "stats", "title": "Focus statistics", "glyph": "chart-bar" }
  ]
},
"surfaces": {
  "actions":      { "entrypoint": "Actions.qml" },
  "quickSetting": { "entrypoint": "Tile.qml" },
  "panel":        { "entrypoint": "Panel.qml" }
}
```

Reglas: los ids cumplen `^[a-z][a-zA-Z0-9]{0,31}$`, son únicos por tipo, a lo
sumo 16 acciones, 4 mosaicos y 4 paneles por paquete; `title` de a lo sumo 48
caracteres; `glyph` debe ser un nombre de Hornero Glyph (verificado contra la
tabla de nombres publicada); cada tipo declarado requiere su punto de entrada de
superficie y viceversa. Todos los strings son texto plano; ninguno se interpreta
como marcado ni como comando.

### 4.2 Acciones (lanzador, IPC, atajos de teclado)

- El registro vive en el servicio `Plugins` y se construye *solo desde los
  manifiestos*: listar acciones nunca ejecuta código de la extensión.
- Lanzador: el prefijo `>` lista acciones de extensiones instaladas y
  habilitadas (título, glifo, nombre de extensión, coincidencia difusa por
  título y palabras clave). Activar una llama al manejador.
- IPC: `qs ipc call plugincommands list` (JSON),
  `qs ipc call plugincommands run <pluginId> <commandId> [args]` (devuelve `ok`,
  o un error de una línea). Esta es la superficie estable para atajos de
  teclado (`bind = SUPER, F9, exec, qs ipc call plugins action hornero-pomodoro
  startFocus`) y scripts. La Shell no escribe atajos de teclado por sí misma: el
  usuario es dueño del atajo, el Centro de control muestra el comando exacto
  para copiar.
- Contrato del manejador: el punto de entrada `surfaces.commands` es un `Item`
  con `function run(actionId: string, args: string): string` que devuelve un
  string vacío en caso de éxito o un error corto. El host carga el manejador
  en la primera invocación y lo conserva durante la sesión, en su propio Loader
  asincrónico. Un manejador que lanza error o demora afecta solo esa llamada
  (el host reporta el error como un toast y un diagnóstico).
- Los argumentos son un único string plano, de a lo sumo 512 caracteres, nunca
  interpretados por el host.

### 4.3 Mosaicos de ajuste rápido

- Un mosaico es un `Item` chico que expone `bool checked`, `string subtitle`,
  `bool busy` y `function toggle()`. El host dibuja el marco del mosaico (misma
  geometría y capa de estado que los interruptores integrados); la extensión es
  dueña solo del estado que informa y de lo que hace `toggle()`. Esto conserva
  un único aspecto y vuelve al mosaico accesible por construcción (rol y nombre
  provistos por el host).
- La ubicación es del usuario: los mosaicos de extensiones aparecen en un
  selector en Centro de control › Utilidades y vienen **apagados por defecto**.

### 4.4 Paneles del Centro de control

- Un panel es un `Item` mostrado dentro del Centro de control bajo un grupo
  "Extensions" del riel de navegación, con título y glifo tomados del
  manifiesto. Se carga solo mientras está abierto y se descarga al salir, así
  que no cuesta nada cuando no se usa.
- Un panel recibe el contexto estándar del host (`hostSurface: "panel"`) y
  puede usar `Settings`, las fachadas de datos y el kit Ui. No puede navegar ni
  modificar otros paneles.

### 4.5 Slots de sesión / pantalla de bloqueo (solo diseño)

Nunca se instancia código de extensión en la superficie de bloqueo: la pantalla
de bloqueo es un límite de seguridad y un plugin fallido o colgado no debe
poder afectar el desbloqueo. Una contribución de pantalla de bloqueo es por lo
tanto una **tarjeta declarada** que renderiza el host (un título, un glifo,
hasta tres métricas enlazadas a un dominio de proveedor compartido), sin código
de extensión en la superficie de bloqueo. Es la fila 11 de la sección 12.

## 5. Esquema de ajustes tipados v2 (`apiLevel` 4)

El conjunto cerrado de tipos crece; los cinco tipos existentes y sus reglas no
cambian. Los nuevos tipos y campos requieren `pluginKit: 4`.

- **`colour`** — Valor: string `#RRGGBB` o `#RRGGBBAA`; Restricciones: `alpha`
  (bool, por defecto false); Control generado: muestra de color con campo hex y
  la paleta Signal como presets
- **`list`** — Valor: arreglo de strings; Restricciones: `options` (requerido,
  1–32 strings únicos), `minItems`, `maxItems`; Control generado: grupo de
  botones de conmutación (selección múltiple), preservando el orden declarado
- **`text`** — Valor: string, puede contener saltos de línea; Restricciones:
  `minLength`, `maxLength` (≤ 4096), `rows` (1–12); Control generado: área de
  texto multilínea
- **`path`** — Valor: string; Restricciones: `kind`: `file` o `directory`;
  `mustExist` (bool) es solo una pista de UI; Control generado: campo de texto
  con botón Explorar; ver 5.1

Campos disponibles en **todo** tipo (solo visualización, nunca cambian la
validación):

- `title`: etiqueta mostrada en lugar de la clave (≤ 48 caracteres).
- `group`: encabezado de sección bajo el cual se ubica el control (≤ 32
  caracteres); los grupos se renderizan en orden de primera aparición, primero
  los ajustes sin grupo.
- `unit`: sufijo corto (`px`, `%`, `s`, `°C`, ≤ 8 caracteres) para números.
- `step` (`integer`/`number`): incremento para el spin box y el deslizador.
- `visibleWhen`: `{ "key": "<otro ajuste>", "equals": <valor> }`. El control
  se muestra solo cuando el ajuste referenciado equivale al valor; el validador
  rechaza claves desconocidas, auto-referencias y ciclos. Es solo UI: un ajuste
  oculto conserva su valor y sigue siendo legible para la extensión.

### 5.1 `path` es un string, no una capacidad

Un ajuste `path` guarda un string que **la Shell nunca abre**. Explorar usa el
diálogo de archivos del Centro de control, que es iniciado por el usuario. Lo
que haga el código de la extensión con el string queda cubierto por el límite
de confianza (corre como el usuario, y `capabilities.processCommands` / el
broker siguen siendo los puntos de declaración y cumplimiento). Consecuencias
codificadas en el validador y el host:

- el validador exige que el valor por defecto de un `path` sea vacío o una
  ruta relativa segura (sin `/` inicial, sin `~`, sin `..`), para que un
  paquete no pueda incluir un defecto que apunte a `~/.ssh` o `/etc`;
- un ajuste `path` obliga a que la tarjeta de la extensión muestre una línea
  "lee una ruta que vos elegís" en el resumen de permisos;
- los valores almacenados se revalidan en cada lectura como cualquier ajuste.

### 5.2 Vista previa en vivo

Centro de control › Extensiones muestra, encima de los controles generados, un
**marco de vista previa**: la superficie propia de la extensión (widget de
escritorio, ítem de barra o tarjeta de dashboard, en ese orden de preferencia)
instanciada a su tamaño de manifiesto en un marco propiedad del host, enlazada
a la instancia que se está editando. Como los ajustes fluyen por el
almacenamiento compartido `Settings`, cada cambio en un control se ve de
inmediato, sin escribir código en la extensión para ello. La vista previa
obedece las mismas reglas que la superficie real (su propio Loader asincrónico,
fallo mostrado en línea, sin vista previa en modo seguro) y se instancia solo
mientras la sección está expandida.

## 6. Configuración por instancia (`apiLevel` 4)

- Una **instancia** es una copia colocada del widget `desktop` de un plugin
  (primer paso) o tarjeta `dashboard` (seguimiento). El plugin siempre tiene
  una instancia *primaria* implícita con id de instancia vacío, que es
  exactamente el widget de hoy; nada cambia para quienes no agregan instancias.
- Las instancias extra se guardan como `plugins.instances = { "<pluginId>": [
  { "id": "a1b2", "label": "Home" } ] }`. Los ids de instancia cumplen
  `^[a-z0-9]{1,8}$` y los genera la Shell. A lo sumo 8 instancias extra por
  plugin.
- La **clave de instancia** es `<pluginId>` para la primaria y
  `<pluginId>#<instanceId>` para el resto. Cada registro por instancia usa la
  clave: `plugins.settings[key]`, `plugins.desktopWidgets[screen][key]`,
  `plugins.desktopWidgetSlots[screen][key]`. La clave primaria es el id del
  plugin, así que **no se migran datos almacenados**.
- Una nueva instancia puede arrancar desde valores por defecto o **duplicar**
  los ajustes de otra instancia. Quitar una instancia borra sus ajustes,
  geometría y slot. Quitar o deshabilitar el plugin oculta las instancias sin
  borrarlas; desinstalar las elimina (la limpieza de ciclo de vida ya usada
  para ajustes).
- Lado del plugin: el host inyecta `hostInstanceId` (string, vacío para la
  primaria) junto con las demás propiedades de contexto de host, y `Settings`
  tiene una nueva propiedad `instanceId`. Una extensión se suma con dos líneas:
  `property string hostInstanceId: ""` en su raíz y
  `Settings { pluginId: "..."; instanceId: root.hostInstanceId }`. Las
  extensiones que no se suman igual renderizan una vez por instancia pero
  comparten los ajustes de la primaria; el Centro de control lo indica ("Esta
  extensión no soporta ajustes separados por instancia").
- El estado de carga, los diagnósticos y el presupuesto de rendimiento quedan
  **por plugin** (el fallo de Loader de una instancia marca al plugin, el error
  nombra la instancia), porque sobre eso actúan `horneroctl` y el modo seguro.
- El deck Signal (`experience.deck`) es curado y conserva una instancia por
  widget del deck; las instancias aplican a los widgets de escritorio propios
  del usuario.

## 7. Modelo de capacidades y permisos

Lo que existe hoy y sigue igual: `capabilities.processCommands`, `networkHosts`
y `providers` son **declaraciones para revisión**, no imposición técnica;
`capabilities.actions` lo verifica el broker de `horneroctl` al momento de
llamar; confianza (hash de payload, recibo) y habilitación son pasos
explícitos del usuario en el Centro de control o la CLI.

Lo que agrega esta RFC, sin que nada de ello sea un sandbox:

1. **Consentimiento de contribuciones.** Habilitar una extensión no la coloca
   en todos lados. Los paneles aparecen en el grupo Extensiones (visibles,
   quitables deshabilitando), los mosaicos están apagados hasta que el usuario
   los agrega, las acciones se listan pero solo corren tras un gesto del
   usuario o una llamada explícita IPC/atajo de teclado, y las instancias
   existen solo cuando el usuario las agrega. El diálogo de habilitación lista
   cada contribución que declara el paquete, de modo que el usuario consiente
   toda la superficie de una vez.
2. **Datos divulgados y puntos de contacto con el sistema.** Los ajustes `path`
   y cada tipo de `contributes` se resumen en la tarjeta de la extensión junto
   a las declaraciones existentes.
3. **Contención.** Cada superficie de cada instancia tiene su propio Loader
   asincrónico; los fallos son por superficie; los presupuestos existentes de
   tiempo de carga y agitación (`slow-load`, `load-churn`) aplican por
   superficie y son informativos; el modo seguro sigue sin instanciar nada; los
   manejadores corren únicamente ante un gesto del usuario.
4. **Sin ruta nueva de código.** Los hosts cargan únicamente puntos de entrada
   `.qml` listados en el manifiesto mediante el mismo Loader y la misma lista
   blanca de imports. No hay `eval`, ninguna API nueva de procesos, ningún
   escape de shell invocable por el host. Las reglas estáticas del validador
   (imports, `Process`, metacaracteres de shell, nombres de glifos) aplican a
   cada punto de entrada nuevo.
5. **Límites honestos.** Una extensión hostil que habilitaste igual puede hacer
   todo lo que puede hacer el usuario. El aislamiento fuera de proceso (una
   instancia de Quickshell por extensión o un subproceso restringido con un
   puente tipado) es el arreglo real y corresponde a una RFC aparte; los
   contratos de contribución de arriba son deliberadamente tipados (propiedades
   escalares, `run(actionId, args)`) para que moverlos detrás de un puente así
   más adelante no cambie código de las extensiones.

## 8. Ciclo de vida

`descubrir → validar → (confiar) → habilitar → activación de superficie →
ejecutar → actualizar → deshabilitar → quitar`, conducido por `horneroctl`
(dueño del ciclo de vida) y el servicio `Plugins` (estado). La activación de
superficies es perezosa según cada fila de la Sección 4: fondo mientras está
habilitada; barra, escritorio y dashboard mientras se muestra su anfitrión;
panel mientras está abierto; manejador en la primera invocación; mosaico
mientras está colocado; vista previa mientras la sección está expandida. Las
actualizaciones aplican sin reiniciar la shell (las URLs de entrada llevan la
versión del paquete, comportamiento existente); las instancias y sus ajustes
sobreviven a las actualizaciones y se revalidan contra la nueva declaración al
leerse (regla de migración de `shell#374`).

## 9. Contención de errores

- Declaración de manifiesto o ajustes inválida: el paquete es rechazado con un
  mensaje accionable por el validador (CLI) y, si alguno se filtra, por los
  normalizadores en tiempo de ejecución, que descartan la declaración mal
  formada en lugar de hacer fallar al plugin.
- Fallo de Loader: `Plugins.markFailed(id, detail, surface)` nombra la
  superficie (extendida con la clave de instancia en el detalle), acotada y
  redactada, visible en el Centro de control y `qs ipc call plugins status`.
- Fallo de manejador de acción: toast más diagnóstico `action-failed`, nunca
  una excepción sin capturar en el lanzador o IPC.
- Un kit más viejo que lo que necesita un paquete: ese paquete queda en
  `failed` con el mensaje de actualización; los demás no se ven afectados.

## 10. Funciones fijas en código a extraer

El núcleo de la Shell se mantiene sobrio solo si las funciones de primera parte
usan los mismos contratos. Candidatos, en el orden en que se vuelven seguros
(cada uno preserva el comportamiento y necesita el punto de contribución que
nombra):

1. **Registro de interruptores rápidos**
   (`modules/utilities/cards/Toggles.qml`).
   Los interruptores propios de la Shell (Wi-Fi, Bluetooth, micrófono, gaming,
   DND, VPN) pasan a ser mosaicos *internos* registrados leídos desde el mismo
   registro que usan los mosaicos de extensiones; la fila renderiza el
   registro. Sin cambio de comportamiento, y el contrato de extensiones obtiene
   un primer consumidor real. Necesita la fila 8.
2. **Tarjeta Clima del Dashboard** (`modules/dashboard/dash/Weather.qml`,
   `modules/dashboard/weather`). `hornero-weather` ya sale en el catálogo y
   `Weather` es una fachada de PluginKit, así que la tarjeta duplica una
   extensión de primera parte. Volverla una extensión de primera parte
   habilitada por defecto manteniendo la tarjeta de la Shell solo como respaldo
   cuando se quita la extensión. Necesita instancias de la fila 4 solo si el
   usuario quiere dos ubicaciones.
3. **Atajos de inhibir reposo y grabación** (`utilities/cards/IdleInhibit.qml`,
   `Record.qml`): acciones más mosaicos sobre servicios existentes de la Shell.
   Necesita filas 7 y 8 y una fachada tipada para ambos servicios.
4. **Calculadora y proveedores similares del lanzador** ya son extensiones y
   son la referencia para la fila 6.

La extracción ocurre únicamente cuando el reemplazo es demostrablemente
idéntico en la VM de QA; hasta entonces permanece lo integrado. La Sección 12
registra lo realizado.

## 10a. Deseos de API del catálogo, priorizados

La auditoría del catálogo (`plugins#80`, `#81`) lista brechas de API que
bloquean extensiones publicadas o planificadas. La prioridad es según cuántas
extensiones desbloquea cada una, y si es un cambio aditivo chico en nivel 4.

- **1. Configuración por instancia** — Plan: Sección 6; Nivel: 4; Estado: En
  revisión (`shell#603`)
- **2. Almacenamiento de estado oculto (temporizadores que persisten plazos no
  deben mostrarse en ajustes generados)** — Plan: campo de visualización
  `hidden: true` en cualquier ajuste: almacenado, validado y legible como
  cualquier otro, nunca renderizado ni contado por Restablecer todo; o una
  fachada `Storage` aparte si el estado oculto debe sobrevivir al Reset; Nivel:
  4; Estado: Próximo PR chico
- **3. Tipos de ajuste `string-list` y `path`** — Plan: `path` publicado en
  esquema de ajustes v2; `strings` libre (lista de hasta 32 strings de a lo
  sumo 128 chars, filas de texto) sumado junto a `list` (que es selección
  múltiple sobre opciones declaradas); Nivel: 4; Estado: `path` en revisión
  (`shell#602`); `strings` siguiente
- **4. Capacidad `experience` en vez de lanzar `horneroctl`** — Plan: una
  fachada tipada `Experience` (leer modo; `set(mode)` ante gesto de usuario)
  sobre el servicio existente, declarada en `capabilities.providers`; Nivel: 5;
  Estado: Diseñado
- **5. Señal de fallo de proceso (un ejecutable faltante nunca reporta salida)**
  — Plan: el host es dueño de una fachada `Run`: argv solo desde
  `processCommands`, señales `started`/`failed(reason)`/`finished(code)`, un
  timeout, un lugar para el caso no-encontrado; Nivel: 5; Estado: Diseñado;
  necesita revisión de seguridad ya que es la única API nueva de procesos
- **6. Host de superficie de lanzador** — Plan: ya alojado
  (`PluginLauncherHost`, `shell#250` cerrado); `commands` (`shell#605`) suma
  filas de acción; Nivel: 3/4; Estado: Publicado
- **7. Contrato de contenido y scroll en widget de escritorio** — Plan:
  `UiScrollArea` provisto por el host en PluginKit y una regla documentada de
  que el contenido más grande que el marco hace scroll en lugar de recortarse;
  Nivel: 4; Estado: Próximo PR chico
- **8. Capturas de shell real en metadatos del marketplace** — Plan:
  `marketplace.screenshots` existente; la herramienta de captura de QA VM debe
  escribirlas; Nivel: -; Estado: Herramientas, repo plugins
- **9. Proveedores: `Power.devices`, calendario, portapapeles (con
  consentimiento), biblioteca de juegos, tiempo de cuadro** — Plan: un dominio
  de proveedor compartido cada uno (RFC 0001 sección 5b); portapapeles y
  biblioteca necesitan un paso explícito de consentimiento por extensión, no
  solo una declaración en el manifiesto; Nivel: 5; Estado: Diseñado;
  `Power.devices` primero (sin consentimiento necesario)

Los que desbloquean extensiones publicadas (1, 2, 3, 7) son nivel 4 y aditivos;
4, 5 y 9 introducen capacidades nuevas y salen como nivel 5 cada uno con su
propia revisión.

## 11. Alternativas consideradas

- **Romper a `schemaVersion` 4.** Rechazada: nada estructural se rompe, una
  ruptura obligaría a re-portar las 36 extensiones del catálogo sin ganancia, y
  `pluginKit` da el mismo comportamiento de rechazo con un campo aditivo.
- **UI libre de ajustes por extensión.** Rechazada: es lo que ya permite la
  superficie personalizada `settings`; el punto es que el esquema tipado da
  controles consistentes, validados, buscables, previsualizables y
  restablecibles.
- **Código visible por el host en manifiestos (eval, expresiones).** Rechazada
  por seguridad; `visibleWhen` es dato, no código.
- **Por instancia copiando el paquete.** Rechazada: bifurca actualizaciones y
  estado de carga; las instancias son configuración de un paquete instalado.

## 12. Despliegue y estado

- **Esta RFC** — Repo: docs; Estado: Propuesta (`docs#130`)
- **Campo `pluginKit`, `apiLevel` 4, validador, esquema; esquema de ajustes v2
  y vista previa en vivo** — Repo: shell; Estado: En revisión: `shell#602` (CI
  verde)
- **Widgets de escritorio por instancia** — Repo: shell; Estado: Borrador:
  `shell#603` (apilado sobre `#602`)
- **Comandos (lanzador, IPC)** — Repo: shell; Estado: Borrador: `shell#605`
  (apilado sobre `#603`)
- **Espejo de validador, esquema y catálogo** — Repo: plugins; Estado: En
  revisión: `plugins#82`
- **Mosaicos de ajuste rápido, paneles del Centro de control** — Repo: shell;
  Estado: Sin iniciar
- **Ajustes ocultos, `strings`, área de scroll (Sección 10a 2, 3, 7)** — Repo:
  shell; Estado: Sin iniciar
- **Fuente de notificaciones, tarjeta de bloqueo, hooks, nuevos proveedores** —
  Repo: shell; Estado: Diseñado aquí, sin iniciar
- **Extracciones (Sección 10)** — Repo: shell, plugins; Estado: Sin iniciar
- **Páginas de dashboard (fila 14, `apiLevel` 5)** — Repo: shell, plugins;
  Estado: Publicado: `shell#710` (contrato) + plugins Agent Deck (primer
  consumidor)
- **Página del manual en español** — Repo: docs; Estado: Sin iniciar

Los números de PR y el estado exacto están registrados en el issue de
seguimiento y en `docs/PLUGINS.md` de la Shell, que es el contrato; esta RFC es
el diseño.

[canonical]: ../../development/rfc-0003-pluginkit-contribution-surfaces.md
