# Hornero Signal

Hornero Signal es el lenguaje visual de HorneroOS: un mismo conjunto de
colores, tipografía, glifos y movimiento compartido por la shell del
escritorio, las apps GTK y Qt, las terminales, el compositor, la pantalla de
bloqueo, el greeter de inicio de sesión, el instalador y el sitio web.
Reemplaza la apariencia derivada de Material 3 que la shell heredó de
Caelestia.

> **Development.** Hornero Signal está en las ramas `main` de Shell, Config
> y `horneroctl` desde noviembre de 2026. Las ISO actual hasta la
> v0.2.0-preview32 inclusive todavía traen el sistema de apariencia
> anterior. Varias superficies de la shell (popouts, barras, páginas del
> Centro de control) se siguen rediseñando; esta página describe solo lo
> que ya está integrado.

## La idea en un párrafo

Pensá en una estación de trabajo de ingeniería contemporánea de una
Argentina alternativa de los años 90: salas de control de broadcast, biseles
de osciloscopio, cartas de ajuste y planos técnicos, resueltos con
moderación moderna. El cromo es sobrio y mate para que tu trabajo quede
adelante. El color se usa como señal, no como decoración:

- El **ámbar** (`signal`) significa *en vivo, activo o principal*: el
  espacio de trabajo con foco, el botón principal, un micrófono encendido.
- El **celeste** (`cue`) significa *foco, selección o información*: el
  anillo de foco del teclado y los elementos seleccionados.
- El **verde fósforo** (`phosphor`) significa *sano o conectado*.
- El **rojo** (`alert`) queda reservado para errores y acciones
  destructivas.

El texto siempre cumple el contraste WCAG AA sobre la superficie en la que
está, y los contornos de los controles cumplen 3:1. El significado nunca
depende solo del color.

## Temas

Todos los temas definen el mismo conjunto de roles con nombre, así que
cualquier tema funciona en todos lados. El catálogo tiene 20 temas:

- **Hornero Signal**: Signal Night (valor de fábrica), Signal Day y
  Signal High Contrast.
- **Hornero Originals**: Buenos Aires Nocturno, Cuyo, Fin del Mundo, Iberá,
  Iguazú, Pampa, Patagonia, Quebrada y Sierras.
- **Ports de la comunidad**: Catppuccin Latte, Catppuccin Mocha,
  Everforest, Gruvbox, Landscape, Monochrome, Nord Dreams y Rosé Pine.

Los tres temas Signal y los Originals, con más detalle:

- **Signal Night**: paneles de instrumental en grafito frío, texto crema
  fósforo cálido, señal ámbar y cue celeste.
- **Signal Day**: papel cálido de dibujo técnico con texto negro tinta.
- **Signal High Contrast**: fondo negro puro, texto y contornos blancos,
  ámbar y celeste más brillantes.
- **Hornero Originals**: paletas regionales teñidas por un lugar de la
  Argentina, cada una con una fotografía acreditada de ese lugar.

Elegí un tema en **Ajustes → Apariencia → Temas**, o mirá
[Apariencia](appearance.md) para los comandos de terminal.

## Los fondos nunca cambian los colores

El tema decide todos los colores. Cambiar el fondo cambia solo la imagen
detrás de tus ventanas; la shell, las apps y las terminales mantienen la
paleta del tema. Las previews anteriores de HorneroOS generaban colores a
partir del fondo; ese comportamiento se eliminó. Mirá
[Fondos](wallpapers.md).

## Tipografía y glifos

| Uso | Tipografía |
| --- | --- |
| Texto de la interfaz | IBM Plex Sans |
| Números, lecturas, etiquetas, código y terminales | IBM Plex Mono |
| Reloj, pantalla de bloqueo y títulos grandes | IBM Plex Sans Condensed |

Las fuentes vienen del paquete `ttf-ibm-plex` de Arch (SIL Open Font
License), que instala `hornero-config`. Los números usan cifras tabulares
para que los valores no salten al cambiar. Las etiquetas chicas en
mayúsculas con Plex Mono, como `01 · AUDIO`, marcan secciones.

Los íconos de la shell son **Hornero Glyphs**, un conjunto curado de íconos
de contorno derivados de Tabler Icons (MIT) que viene con la shell. No hace
falta ninguna fuente de íconos del sistema. Los íconos de las aplicaciones
siguen saliendo de tu tema de íconos (Papirus por defecto).

## Detalles de firma

- Una **barra al aire**, una línea ámbar fina en el borde que mira a tu
  contenido, marca el espacio de trabajo, la pestaña o el ítem del riel
  activo, en lugar de una píldora rellena.
- Los **medidores segmentados** muestran volumen, brillo, batería y
  recursos como segmentos discretos con el valor impreso al lado.
- Una pequeña **marca de registro** ámbar señala el panel con foco en lugar
  de un brillo.
- La **diagonal de La Plata** a 45° aparece solo en superficies de marca
  (bloqueo, greeter, instalador, sitio web y fondos), nunca dentro de los
  controles.
- Los radios son chicos (3–8 px), los bordes son líneas finas y no hay
  desenfoque de vidrio detrás de las superficies por defecto.

![Un panel de escritorio con instrumentos etiquetados: carga y
temperatura del procesador y de gráficos, barras por núcleo, memoria,
almacenamiento y red, cada lectura impresa junto a su
medidor.](https://www.horneroos.com/captures/cap-signal-01.png)

*Instrumentos Signal en el escritorio: medidores segmentados con el
valor impreso al lado. Las lecturas son del equipo del maintainer,
capturadas el 19 de noviembre de 2026; son un ejemplo, no un
requisito.*

## Accesibilidad

- **Alto contraste**: **Ajustes → Accesibilidad → Alto contraste** pasa la
  shell a la paleta Signal High Contrast y desactiva la transparencia sin
  cambiar el tema elegido. Para usar la paleta de alto contraste en todos
  lados, incluidos GTK y las terminales, aplicá el tema
  `hornero-signal-contrast`.
- **Movimiento reducido**: **Ajustes → Accesibilidad → Reducir movimiento**
  (también en **Apariencia → Animaciones**) elimina el desplazamiento y
  deja solo fundidos cortos. La shell también respeta el ajuste global de
  GNOME `org.gnome.desktop.interface enable-animations`.
- **Tamaño del texto**: **Ajustes → Accesibilidad → Tamaño del texto**
  escala el texto de la shell.

Esos mismos interruptores se guardan como `appearance.highContrast` y
`appearance.reducedMotion` en tu configuración de la shell.

## Movimiento

El movimiento es breve y tiene un propósito: las cosas aparecen desde el
control que las abrió, se asientan con un rebote muy chico y se van con un
fundido rápido. Nada parpadea ni se anima en reposo. Cada superficie se
puede usar con las animaciones apagadas.

## Si venís de una preview anterior

Los temas anteriores Hornero Dark, Hornero Light y Hornero 199X se
retiraron. Una configuración que todavía los nombre se migra una sola vez:
Dark y 199X pasan a Signal Night, Light pasa a Signal Day. Neon City, Vapor
Dreams, Soft Morning y Warm Sunset también se retiraron y migran a Signal
Night o Signal Day según su modo. Se eliminaron sin reemplazo: la
generación de colores a partir del fondo, las variantes de esquema (Tonal
spot, Vibrant, etc.), el ajuste de color de acento, Material Symbols y la
tipografía Rubik. Después de actualizar, corré esto una vez para migrar y
regenerar los archivos de color derivados:

```sh
horneroctl appearance sync --dry-run
horneroctl appearance sync --yes
```

Las capturas y los videos publicados antes de noviembre de 2026 muestran la
apariencia anterior. En el sitio web están etiquetados como *Preview —
apariencia anterior*.

## Para saber más

- [Apariencia](appearance.md): elegir y aplicar un tema.
- [Fondos](wallpapers.md): poner la imagen detrás de tus ventanas.
- [Arquitectura de la apariencia](../../architecture/appearance-system.md)
  (en inglés): cómo fluyen los temas desde Config, pasando por
  `horneroctl`, hasta la shell y las apps.
- [RFC 0001 — Hornero Signal](../../development/rfc-0001-hornero-signal.md)
  (en inglés): la autoridad de diseño, con roles, paletas, tipografía,
  glifos, movimiento y el contrato de superficies ancladas.
- [Signal Visual Language](../../development/signal-visual-language.md)
  (en inglés): reglas detalladas para barras, medidores, paneles,
  movimiento y cada layout.
