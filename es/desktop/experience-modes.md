# Modos de experiencia

Un modo de experiencia cambia cómo se *comporta* el escritorio ahora mismo:
cuánto anima, qué tan densa es la barra, qué widgets hay en el escritorio y
si las notificaciones te interrumpen. Nunca reemplaza tu layout ni tu tema.

> **Development.** Los modos de experiencia están en la rama `main` de Shell
> desde noviembre de 2026. Las ISO Preview hasta la v0.2.0-preview32
> inclusive no los traen. El comportamiento de esta página está cubierto
> por las pruebas automáticas de Shell (lógica de perfiles, layout del deck
> y página Experience, ejecutadas sin pantalla y en modo offscreen). Todavía
> no se validó visualmente en una máquina virtual ni en un escritorio
> físico, así que tomá el aspecto de cada modo como no verificado hasta que
> se publique esa evidencia.

## Los cinco modos

La interfaz todavía está solo en inglés, así que los nombres de los controles
se citan tal como aparecen en pantalla.

| Modo | Movimiento | Barra | Escritorio |
| --- | --- | --- | --- |
| **Focus** | Reducido | Solo íconos | Vacío |
| **Everyday** | Estándar | Valores | Tus widgets |
| **Signal** | Completo | Con etiquetas | Deck de instrumentos |
| **Gaming** | Apagado | Solo íconos | Vacío |
| **Studio** | Estándar | Valores | Tus widgets |

Everyday es el modo con el que arranca una instalación nueva. Cada modo es un
conjunto de campos que podés ver y cambiar de a uno (mirá
[Personalizar un modo](#personalizar-un-modo)).

### Qué hace cada modo

- **Focus** reduce el movimiento, muestra solo íconos en la barra, retiene las
  notificaciones mientras está activo y las mantiene calladas sobre ventanas
  a pantalla completa. Sin brillo y sin widgets de escritorio. Su layout
  preferido es Minimal Top.
- **Everyday** es Cockpit con movimiento estándar y los valores visibles en
  la barra. No se retiene ni se oculta nada.
- **Signal** es el modo donde vive la telemetría más rica: movimiento
  completo, entradas de barra con etiquetas, telemetría muestreada a 2 Hz en
  vez de 1 Hz, un leve acento luminoso en las trazas y scanlines. El
  escritorio muestra el [deck de instrumentos Signal](#el-deck-de-instrumentos-signal).
- **Gaming** apaga el movimiento, encola las notificaciones emergentes
  mientras el modo está activo, pausa la telemetría bajo pantalla completa y
  mantiene la pantalla despierta sobre ventanas a pantalla completa. También
  sugiere el perfil de energía de rendimiento y activa el gancho de ajuste
  del compositor cuando el compositor lo soporta; un gancho que el sistema
  no puede cumplir se muestra como no disponible, nunca simulado. Los
  widgets de escritorio se descargan, así que el escritorio no gasta
  procesador ni gráficos bajo un juego. Su layout preferido es Gaming.
- **Studio** mantiene un lienzo estable para el trabajo creativo: movimiento
  estándar, sin brillo, tus propios widgets de escritorio y notificaciones
  suprimidas sobre ventanas a pantalla completa. Su layout preferido es
  Studio. Un ajuste opcional le pide al stack de audio el perfil de baja
  latencia mientras el modo está activo y restaura tu perfil anterior al
  salir (usa `horneroctl studio mode audio`; mirá
  [Studio](../../applications/studio.md)).

Hay dos salvaguardas que no se pueden pisar: el brillo y las scanlines están
siempre apagados en Focus y Gaming, y Gaming nunca anima. El brillo y las
scanlines también quedan apagados con temas de día, en alto contraste y con
niveles de movimiento bajos, diga lo que diga el modo.

## Cómo se combinan los modos con todo lo demás

Se combinan cuatro elecciones independientes. Un modo nunca reemplaza a las
otras:

| Elección | Qué decide | Dónde la cambiás |
| --- | --- | --- |
| Edición (Desktop, Studio, Gaming) | Qué software hay instalado | La instalación; mirá [Ediciones](../../architecture/editions.md) |
| Modo de experiencia | Cómo se comporta el sistema | Ajustes → Experience |
| Preset de layout | Qué barras y rieles existen | [Layouts](layouts.md) |
| Tema | Colores y fondo | [Apariencia](appearance.md) |

Un modo solo activa capacidades que tu edición tiene instaladas. Un gancho
para una capacidad que falta, como el ajuste del compositor en un
compositor que no lo soporta, se muestra como no disponible.

Cada modo nombra un *layout preferido*, pero cambiar de modo **no** reescribe
tus barras por defecto, porque un preset de layout reemplaza la
configuración de las barras. Aplicá el layout preferido desde la página
Experience cuando lo quieras, o activá **Apply preferred layout on switch**
para que el layout acompañe al modo.

## Cambiar de modo

Cambiás de modo de forma explícita. Cualquiera de estas sirve:

- **Ajustes → Experience.** Elegí un modo y apretá **Switch**.
- **El lanzador.** Buscá *Focus mode*, *Everyday mode*, *Signal mode*,
  *Gaming mode*, *Studio mode* o *Revert mode*.
- **El indicador de modo en la barra.** Cockpit y Cockpit Clear muestran un
  indicador chico (`FOC`, `SIG`, `GAM`, `STU`) en todos los modos menos
  Everyday. Al hacer clic se abre la página Experience.
- **Un script.** La shell expone las mismas acciones por `qs ipc call
  experience ...`; mirá la
  [referencia de Experience en Shell](https://github.com/HorneroOS/shell/blob/main/docs/EXPERIENCE.md).

Un aviso corto confirma cada cambio (se puede desactivar). **Revert mode**,
también **Revert to previous mode** en la página Experience, vuelve al modo
en el que estabas antes del último cambio.

### Cambio automático

El cambio automático viene **apagado por defecto**. Cuando lo activás en
Ajustes → Experience (**Switch to Gaming automatically for fullscreen
games**), la shell entra en Gaming mientras tenga foco una ventana a
pantalla completa que parezca un juego (por defecto, juegos de Steam,
Gamescope y ejecutables de Windows; podés listar tus propios patrones de id
de aplicación) y vuelve a tu modo anterior cuando esa ventana deja de estar
a pantalla completa.

- La detección es local: la shell solo mira el id de aplicación y el estado
  de pantalla completa de la ventana con foco. Nada sale de la máquina.
- Solo sale de un modo al que entró ella misma. Si elegiste Gaming vos, se
  queda hasta que lo cambies.
- El aviso de un cambio automático lo dice, y **Revert mode** lo deshace en
  una sola acción. Apagar el cambio automático mientras está activo también
  revierte.

## El deck de instrumentos Signal

En modo Signal el escritorio muestra un deck de hasta seis instrumentos en
vivo sobre dos rieles, con el centro libre para las ventanas:

| Prioridad | Instrumento | Muestra |
| --- | --- | --- |
| 1 | System Insight | Procesador, gráficos, memoria y almacenamiento |
| 2 | Network Scope | Trazas de descarga y subida |
| 3 | Audio Deck | Reproducción y espectro de audio |
| 4 | Calendar | El mes y la hora |
| 5 | Agenda | Datos de fecha, semana y año |
| 6 | Moon Phase | La fase aproximada |

- El deck se arma por pantalla y nunca tapa una barra. Lo que no entra se
  descarta por prioridad en vez de superponerse: una pantalla de 1366×768
  muestra cuatro instrumentos, un ultrawide de 3440 píxeles de ancho
  muestra los seis.
- Los valores nunca se inventan: un sensor que tu hardware no tiene se
  muestra como no disponible.
- El deck solo usa las seis extensiones propias cuando están instaladas y
  son de confianza. Nunca las habilita en Extensions. Un instrumento
  ausente, sin confianza o que falló se lista en la página Experience y se
  deja afuera.
- El acento luminoso es compartido: brillan como máximo tres trazas a la
  vez, y solo en modo Signal con un tema oscuro y el movimiento permitido.

Apagá un instrumento para Signal o restaurá el deck de fábrica (**Reset
deck**) desde Ajustes → Experience, y movelos o cambiales el tamaño con
**Edit widgets**. Los cambios se guardan solo para Signal y no tocan los
widgets de tu escritorio Everyday.

## Personalizar un modo

Ajustes → Experience te deja cambiar el movimiento, la densidad de la barra,
el brillo, las scanlines, la frecuencia de telemetría, los widgets de
escritorio, la retención de notificaciones, la supresión bajo pantalla
completa, el layout preferido, las pistas de inactividad y energía y los
ganchos de un modo. Tus cambios:

- se guardan por modo y sobreviven a cambiar de modo y a reiniciar la shell;
- nunca modifican los otros modos;
- se ignoran en las dos salvaguardas bloqueadas de arriba.

**Reset customisations** devuelve un modo (y su deck) al perfil de fábrica.

## Volver al escritorio de fábrica

**Factory reset** en la página Experience (pide confirmación) elige Everyday,
aplica el layout Cockpit y el tema Signal Night. Conserva tus
personalizaciones por modo; usá **Reset customisations** para borrarlas.

## Movimiento reducido y alto contraste

Los modos de experiencia van por encima de tus opciones de accesibilidad.
Si activás **Reduce motion** (o tu ajuste de animaciones de todo el
escritorio lo pide), el nivel de movimiento se fuerza a apagado diga lo que
diga el modo. El alto contraste mantiene la paleta Signal High Contrast en
todos los modos. Mirá [Popups, foco y movimiento](popups-and-motion.md) para
los cuatro niveles de movimiento.

## Más información

- [Arquitectura de los modos de experiencia](../architecture/experience-modes.md)
  — cómo se construyen los perfiles, el estado y el deck.
- [Layouts](layouts.md) — el catálogo de layouts.
- [RFC 0001](../../development/rfc-0001-hornero-signal.md) — la autoridad de
  diseño, sección 5a (en inglés).
