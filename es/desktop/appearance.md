# Apariencia: temas y modo

Empezá en **Ajustes → Apariencia** cuando quieras un cambio coordinado. Un
tema es un aspecto completo: define todos los colores de la interfaz y
además elige un fondo por defecto, un tema GTK, un tema de íconos y el modo
claro u oscuro. Todos los temas usan el lenguaje de diseño
[Hornero Signal](hornero-signal.md).

> **Development.** Esta página describe Hornero Signal, en las ramas `main`
> desde noviembre de 2026. Las ISO actual hasta la v0.2.0-preview32
> todavía traen el sistema de apariencia anterior, generado a partir del
> fondo.

## Elegí un tema

El catálogo tiene **20 temas**, todos con paletas Signal completas:

- **Hornero Signal**: Signal Night (valor de fábrica), Signal Day y Signal
  High Contrast.
- **Hornero Originals**: Buenos Aires Nocturno, Cuyo, Fin del Mundo, Iberá,
  Iguazú, Pampa, Patagonia, Quebrada y Sierras; paletas regionales, cada
  una con una fotografía acreditada.
- **Ports de la comunidad**: Catppuccin Latte, Catppuccin Mocha,
  Everforest, Gruvbox, Landscape, Monochrome, Nord Dreams y Rosé Pine,
  llevados a los roles de Signal.

En **Ajustes → Apariencia → Temas**, previsualizá una tarjeta y elegila
para aplicarla. Si falta el tema GTK o de íconos de un tema, el resto del
aspecto se aplica igual; los detalles del tema y la
[guía de solución de problemas](../troubleshooting/README.md) muestran qué
falta. Hornero no descarga temas de terceros sin avisar.

![Ajustes, página Apariencia con la sección Chromatic abierta. El panel
de vista previa muestra los colores extraídos y las proporciones de
contraste verificadas para texto, texto atenuado y
acento.](https://www.horneroos.com/captures/cap-appearance-01.png)

*Ajustes → Apariencia. La vista previa verifica el contraste (15,5:1
para el texto acá) antes de aplicar nada. Captura real del escritorio
en el equipo del maintainer, 19 de noviembre de 2026.*

Desde una terminal, inspeccioná antes de aplicar:

```sh
horneroctl appearance theme list
horneroctl appearance theme show patagonia
horneroctl appearance theme apply patagonia --dry-run
horneroctl appearance theme apply patagonia --yes
horneroctl appearance theme get
```

Usá `apply` para cualquier tema instalado. `set` es el cambio verificado
entre los tres temas Signal incorporados: después chequea que el esquema y
GTK coincidan y, si no, intenta volver al tema incorporado anterior:

```sh
horneroctl appearance theme set hornero-signal-day --dry-run
horneroctl appearance theme set hornero-signal-day --yes
```

Los comandos que modifican algo piden `--yes`; `--dry-run` muestra la
acción propuesta. Después de un cambio, `horneroctl appearance doctor`
chequea que el esquema en vivo sea válido, que las fuentes IBM Plex estén
instaladas y que los archivos derivados coincidan.

## Qué cambia al aplicar un tema

Aplicar un tema escribe el esquema de colores en vivo en
`~/.local/state/hornero/signal/scheme.json` (bajo `$XDG_STATE_HOME` si está
definido). La shell observa ese archivo y cambia los colores al instante.
El mismo paso reescribe los colores de los bordes de Hyprland y de
hyprlock, cambia el include del tema de Kitty, regenera las paletas de
Alacritty, Ghostty, btop y Cava, y aplica el tema GTK del tema. Las apps Qt
lo siguen cuando qt6ct es el tema de plataforma.

Para ver el estado actual sin cambiar nada:

```sh
horneroctl appearance status
horneroctl appearance scheme status
horneroctl appearance colors status
```

## Claro y oscuro

Cada tema tiene un modo fijo: Signal Day, Cuyo, Quebrada, Sierras y
Catppuccin Latte son claros; el resto son oscuros. Para pasar de claro a
oscuro, elegí un tema del otro modo; para el par principal, alterná entre
Signal Night y Signal Day.

La preferencia de esquema de color de GTK es un ajuste aparte que les
indica a las apps GTK y libadwaita qué variante preferir. Inspeccionala o
cambiala con `horneroctl appearance gtk color-scheme`; cambiarla no cambia
el tema de la shell.

## Accesibilidad

- **Alto contraste**: **Ajustes → Accesibilidad → Alto contraste** le da a
  la shell la paleta Signal High Contrast y apaga la transparencia,
  manteniendo el tema elegido. Aplicá `hornero-signal-contrast` para
  usarla también en GTK, Qt y las terminales.
- **Reducir movimiento**: en **Ajustes → Accesibilidad** o **Apariencia →
  Animaciones**. La shell también respeta la preferencia
  `enable-animations` de GNOME.
- **Tamaño del texto** y **velocidad de animación**: en **Ajustes →
  Accesibilidad**.

## Fondos

Un fondo nunca cambia los colores, salvo que vos lo decidas. Cada tema
nombra un fondo y una colección por defecto; podés elegir cualquier otra
imagen sin afectar la paleta. Para derivar la paleta de un fondo, una imagen
o un color, usá la sección opcional [Hornero Chromatic](chromatic.md). Mirá
[Fondos](wallpapers.md).

## Si venís de una preview anterior

Hornero Dark, Hornero Light, Hornero 199X, Neon City, Vapor Dreams, Soft
Morning y Warm Sunset se retiraron. Una selección guardada que nombre
alguno de ellos se migra una sola vez a Signal Night o Signal Day. Se
eliminó la antigua generación de colores estilo Material a partir del
fondo; su reemplazo es [Hornero Chromatic](chromatic.md), con sus propias
variantes. Después de actualizar, corré:

```sh
horneroctl appearance sync --dry-run
horneroctl appearance sync --yes
```

## Paquetes de temas

Los archivos de tema y sus reglas de validación viven en
[HorneroOS/config](https://github.com/HorneroOS/config/tree/main/profiles/themes)
(`profiles/themes/<id>/theme.json`, versión de esquema 2). El catálogo se
genera a partir de esos paquetes. Un paquete define todos los roles de
color de Signal y una paleta de terminal de 16 colores; los chequeos de
Config verifican el contraste de cada paquete publicado, y `horneroctl`
solo lista y aplica paquetes de esquema v2.

La guía de arquitectura explica cómo fluyen los temas desde
Config, pasando por `horneroctl`, hasta la shell, GTK, Qt y las terminales:
[Sistema de apariencia](../architecture/appearance-system.md). Para los
detalles de las terminales, mirá [Terminal](../applications/terminal.md).
