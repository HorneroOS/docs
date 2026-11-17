# Layouts de barra

Los layouts cambian dónde van las barras, rieles y docks del escritorio. No
cambian la disposición de las ventanas: eso lo controla el perfil de layout
de ventanas del compositor. Así se mantienen separadas dos elecciones útiles:
**dónde viven los controles de la shell** y **cómo se acomodan las ventanas**.

> **Development.** El catálogo de 14 presets, el valor por defecto Cockpit y
> Cockpit Clear están en la rama `main` de Shell y Config desde noviembre de
> 2026. Las ISO Preview hasta la v0.2.0-preview32 inclusive traen el
> catálogo anterior de quince presets. El catálogo está cubierto por las
> pruebas automáticas de Shell (esquema de presets, ubicación y
> comportamiento de las barras, ejecutadas sin pantalla y en modo
> offscreen). Todavía no se validó visualmente en una máquina virtual ni en
> un escritorio físico, y Cockpit Clear no se probó sobre fondos reales en un
> host real.

Abrí el selector de layouts con **Super + Shift + B**. Las vistas previas de
topología muestran si un preset usa un riel lateral, una o dos barras
horizontales, superficies claras, islas separadas o un dock. Elegí una vista
previa para aplicarla; con Escape salís sin aplicar.

## Presets

Hornero trae catorce presets. **Cockpit es el valor de fábrica** en todas las
ediciones y después de un reseteo de fábrica.

| Familia | Presets |
| --- | --- |
| Rieles | Hornero Left, Hornero Right, Minimal Left |
| Barras horizontales | Minimal Top, Classic Top, Classic Bottom |
| Multisuperficie | Cockpit, Cockpit Clear, Horizon, Islands, Minimal Float |
| Dock y enfoque | Dock Bottom, Studio, Gaming |

Para qué sirve cada uno:

- **Cockpit** — dos barras: *actuar* arriba, *saber* abajo y trabajo sin
  interrupciones en el medio. Un riel superior inset de 36 px tiene la marca
  del lanzador, las acciones rápidas, el reloj, los íconos de estado, la
  bandeja y la energía. Una tira inferior attached de 30 px tiene los
  espacios de trabajo, la ventana activa y los medios, y los medidores de
  recursos.
- **Cockpit Clear** — la misma anatomía sin ningún fondo de barra. Los
  controles y la telemetría quedan directamente sobre el fondo de pantalla
  ([detalles](#cockpit-clear)).
- **Horizon** — una sola placa lleva todos los controles y lecturas; los
  espacios de trabajo descansan en una línea clara debajo.
- **Islands** — tres islas flotantes: controles, hora, estado.
- **Minimal Float** — una cinta superior flotante y suave con espacios de
  trabajo, la hora y unas pocas herramientas (id de preset `cozy-minimal`,
  antes llamado Cozy Minimal).
- **Classic Top** y **Classic Bottom** — una barra tradicional con el
  conjunto completo de íconos de estado.
- **Minimal Top** y **Minimal Left** — espacios de trabajo y reloj, o
  espacios de trabajo y energía, y poco más.
- **Dock Bottom** — un dock inferior con lanzador, espacios de trabajo,
  apps fijadas, herramientas y estado.
- **Studio** — una barra superior para trabajo creativo: medios y audio a
  mano y un lienzo estable reservado.
- **Gaming** — una barra inferior mínima, sin logo.
- **Hornero Left** y **Hornero Right** — una barra lateral completa en el
  borde izquierdo o derecho. Su composición está inspirada en el layout de
  Caelestia, el proyecto del que desciende Hornero Shell, y se conserva acá
  con atribución. Usan el aspecto Signal como cualquier otro preset.

Polybar y Waybar influyeron en algunas topologías; la shell usa un solo
sistema de layouts de Quickshell en lugar de implementaciones de barra
históricas separadas.

### Presets que se eliminaron

El catálogo pasó de quince a catorce presets porque dos repetían a otros:
**Floating Island** duplicaba a Minimal Float y **Productivity** duplicaba a
Minimal Top. Cozy Minimal pasó a llamarse Minimal Float.

Si usabas alguno, no se rompe nada. Aplicar un preset copia sus barras a tu
propia configuración, así que un escritorio que ya usa un preset eliminado
sigue funcionando igual; solo el selector deja de listarlo. Si un modo de
experiencia nombraba un preset eliminado como layout preferido, la shell
migra esa elección una sola vez (Floating Island a Minimal Float,
Productivity a Minimal Top). Volvé a aplicar un layout desde el selector
cuando quieras cambiarte.

## Cockpit Clear

Cockpit Clear no dibuja fondo de barra: ni relleno, ni tinte, ni desenfoque,
ni sombreado de borde, ni sombra, en todos los modos, incluido alto
contraste. La legibilidad sale solo del primer plano:

- **Tinta adaptativa.** La shell mira el fondo de pantalla debajo de cada
  entrada de la barra y elige tinta clara u oscura, la que contraste más.
  Solo elige entre las tintas de noche y de día del propio tema: el fondo
  nunca recolorea la interfaz. Los fondos de video y las imágenes ilegibles
  vuelven a la tinta del tema.
- **Estilos de primer plano.** Elegí **Auto**, **Outline**, **Shadow** o
  **Contrast** en el selector de layouts o en Ajustes → Layout. Auto agrega
  un halo fino y, sobre zonas cargadas, una sombra suave. Shadow vuelve a
  Outline cuando no llega a un contraste de 3:1. Contrast agrega un halo
  más grueso y un peso más marcado, y Alto contraste siempre lo usa.
- **Los popouts siguen opacos.** Los menús y paneles que se abren desde una
  barra clara son paneles Signal sólidos comunes con su propio borde; flotan
  unos píxeles separados de la barra.

Como las reglas de legibilidad se miden contra fondos de pantalla, un fondo
poco común todavía puede leerse mal. Si una barra cuesta de leer, pasá el
estilo a Contrast o aplicá un layout sólido como Cockpit.

## El indicador de modo y las celdas de espacios de trabajo

Cockpit y Cockpit Clear muestran un indicador chico en el grupo final del
riel superior cuando hay activo un [modo de experiencia](experience-modes.md)
distinto de Everyday (`FOC`, `SIG`, `GAM` o `STU` junto al glifo del modo).
Al hacer clic se abren los Ajustes.

Los indicadores de espacios de trabajo son rectángulos chicos, no píldoras.
Cada estado se distingue por al menos dos señales, así que el color nunca es
la única: el espacio activo tiene una celda elevada y una barra ámbar en el
borde que mira a tus ventanas, uno ocupado lleva una marca chica, uno visible
en otro monitor tiene una línea fina y uno urgente se vuelve rojo de alerta
hasta que lo visitás.

## Aplicar desde una terminal

Usá la CLI para listar los presets disponibles e inspeccionar la elección
actual:

```sh
horneroctl shell preset list --full
horneroctl shell preset current
horneroctl shell preset apply cockpit-clear --dry-run
horneroctl shell preset apply cockpit-clear --yes
```

Aplicar un preset reemplaza los ajustes de los que el preset es dueño y
conserva las demás preferencias de la shell. Mantené tus ediciones
personales en la configuración de usuario, no dentro de un preset del
paquete. Reordená, ocultá o agregá secciones del layout activo desde
Ajustes → Bars.

## Cuando una barra tapa una ventana

Las barras attached y los docks reservan espacio en el borde. Las
superficies flotantes normalmente se superponen al escritorio; algunos
presets reservan espacio de forma explícita para conservar la legibilidad.
Probá otro preset antes de editar la geometría. Para el esquema, el
comportamiento de los bordes, las opciones de entrada, los ajustes por
monitor y la topología de las barras, mirá el
[contrato de layout en el repositorio Shell](https://github.com/HorneroOS/shell/blob/main/docs/LAYOUTS.md).
La [página de Layouts](https://github.com/HorneroOS/website/blob/main/src/pages/layouts.astro)
del sitio muestra capturas y descripciones cortas; fijate en su fecha antes
de confiar en las capturas, porque las anteriores muestran la apariencia
previa.
