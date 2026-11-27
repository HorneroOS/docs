# Estudio de referencias de experiencia de escritorio

*Traducción al español rioplatense de la
[versión en inglés](../../development/experience-reference-study.md), que es
la canónica.*

> Verificado contra las fuentes públicas de los proyectos el 2026-10-14.
> **Superado en parte, 2026-10-26:** la ISO Preview firmada v0.2.0-preview22
> ya está publicada y Studio es una edición Preview. Las afirmaciones abajo
> sobre que no hay ISO publicada o que Studio es planificada describen el
> estado del 2026-10-14. Este es un estudio de ingeniería de producto, no un
> tablero de puntaje de funciones ni una afirmación de que los proyectos tengan
> el mismo público. Reverificá las fuentes enlazadas antes de usar esta página
> para tomar una decisión de release.
>
> **Superado en parte, 2026-11-16:** Hornero Signal
> ([RFC 0001](rfc-0001-hornero-signal.md)) reemplazó la paleta Material 3
> derivada del fondo de pantalla. Los temas ahora son paletas Signal completas
> de autor y los fondos nunca recolorean el escritorio; las referencias de abajo
> a un esquema derivado del fondo describen el estado del 2026-10-14.

HorneroOS tiene su propia historia de producto, lenguaje de diseño y límites de
sistema operativo. Este estudio registra patrones útiles de Caelestia, Ryoku y
Omarchy, y luego define qué ideas encajan en HorneroOS y cuáles no. El objetivo
es mejorar el producto sin copiar la estructura ni la identidad de otro
proyecto.

## Posición actual de HorneroOS

HorneroOS es una familia de sistemas operativos basada en Arch en desarrollo.
Desktop es Wayland-first; Hyprland es su compositor validado por defecto,
mientras que Niri sigue siendo experimental hasta que pase su matriz de sesión
más amplia. En ese momento, el sitio web del producto decía que no había ISO
instalable publicada y que Server, Agents y Studio eran ediciones planificadas
(Studio ahora es Preview; la ISO preview22 está publicada). Estos límites de
madurez forman parte de la calidad del producto y deben mantenerse visibles en
los docs y la comunicación.

El escritorio ya tiene una identidad compuesta: una UI basada en Quickshell,
una interfaz de sistema `horneroctl`, datos compartidos de temas y fondos de
pantalla, activos fotográficos reales vinculados a la Argentina con procedencia,
y adaptadores de paleta para Kitty, Alacritty, Ghostty, btop y Cava. Hornero
Config deriva formatos nativos para las cinco aplicaciones desde el esquema del
fondo activo. Los emuladores de terminal son integraciones curadas; btop y Cava
siguen siendo aplicaciones opcionales. Mirá los
[renderizadores de paleta][renderers], la
[ruta de aplicación de apariencia][apply] y las
[pruebas de integración][tests]. Las responsabilidades están divididas a
propósito entre `shell`, `hornero`, `config`, `docs` y `website`; mirá el
[mapa de repositorios](../architecture/README.md) y el
[lenguaje de diseño](design-language.md).

## Qué hacen bien las referencias

### [Caelestia](https://github.com/caelestia-dots/shell)

**Patrón.** La shell y su CLI son proyectos separados. La shell documenta su
IPC, mientras la CLI es dueña de operaciones como esquema, fondo de pantalla,
grabación, capturas y actualizaciones. Los ajustes de la shell son JSON
explícito, con overrides por monitor e integración con Home Manager.

**Transferencia.** Mantené la presentación de la UI separada de los comandos
estables del sistema operativo. Hacé que controles de la shell, comandos de la
CLI y docs describan las mismas transiciones de estado. Dejá los ajustes
específicos de máquina fuera de los valores por defecto empaquetados.

**Mantener distinto.** La shell de Caelestia está orientada explícitamente a
Hyprland. La identidad de escritorio de HorneroOS es Wayland-first, y las
operaciones específicas de compositor deben permanecer detrás de adaptadores
conscientes de capacidades.

### [Ryoku](https://github.com/Ryoku-dev/ryoku)

**Patrón.** El repositorio presenta la definición del sistema, el escritorio,
el instalador y las herramientas de release como un solo producto. Describe
sesiones Hyprland y Niri, entrega firmada de paquetes, snapshots de
actualización y vuelta atrás al arrancar. Sus docs explican de frente el
público buscado y los límites del sistema.

**Transferencia.** Tratá la instalación, la actualización y la recuperación
como experiencias de producto, no como tareas de lista de paquetes. Una
release soportada futura de Hornero necesita una cadena de artefactos
verificable y una ruta de recuperación documentada. Mantené la etiqueta de
madurez de Niri atada a la aceptación real de sesión.

**Mantener distinto.** HorneroOS tiene límites establecidos de propiedad entre
repositorios y trabajo sobre un instalador provisional con otro dueño a largo
plazo. No colapses repositorios ni tomes la arquitectura del instalador para
imitar a Ryoku.

### [Omarchy](https://github.com/omacom/omarchy)

**Patrón.** Los temas son paquetes de datos. Las definiciones de color
alimentan configuración generada de aplicaciones, y un tema puede incluir
fondos, vistas previas, imágenes de bloqueo, elecciones de íconos, color de
teclado y una marca de modo claro. Su CLI y menú exponen operaciones de temas
directas y automatizables.

**Transferencia.** Seguí moviendo el soporte de temas hacia adaptadores
generados desde una única paleta revisada, con vistas previas visuales y
metadatos explícitos claro/oscuro. Mantené en acuerdo al selector de temas, la
línea de comandos y la documentación.

**Mantener distinto.** Las plantillas de Omarchy pueden producir configuración
ejecutable para aplicaciones. HorneroOS debe conservar sus propias licencias,
revisión de confianza y límites de archivos generados. Un tema o extensión no
debe convertirse en un permiso implícito de ejecución de código.

## Decisiones de producto para HorneroOS

### Mantener explícita la propiedad del producto

El modelo actual multi-repositorio es útil cuando cada contrato tiene un dueño:

- `shell` es dueño de la presentación del escritorio y la sesión interactiva.
- `hornero` es dueño de la CLI estable y las operaciones del sistema operativo.
- `config` es dueño de los valores por defecto empaquetados, temas, fondos de
  pantalla y materialización de aplicaciones.
- `docs` es dueño de las guías para personas usuarias y colaboradoras.
- `website` publica datos de producto revisados y fijados, y capturas reales.

No dupliques verdades de paquetes, temas, ediciones o compositores para hacer
más fácil una página o un instalador. Extendé en cambio los contratos
legibles por máquina existentes.

### Hacer de la profundidad de integración una función de primer orden

La calidad de un tema no es la cantidad de paletas. Es cuántas aplicaciones
adoptan correctamente una paleta elegida, la fidelidad de las variantes clara y
oscura, y si aplicar o revertir un tema restaura un escritorio coherente.
Hornero Config hoy renderiza un esquema derivado del fondo en archivos nativos
de Kitty, Alacritty, Ghostty, btop y Cava. Sumá otro adaptador solo cuando su
formato se genere desde la paleta compartida y el resultado tenga pruebas.
Esto evita que los colores por app deriven en copias separadas editadas a
mano. Las guías de [utilidades del sistema](../applications/system-utilities.md)
y [medios y audio](../applications/media-audio.md) explican qué apps son
opcionales y qué cambia la integración de paleta.

### Tratar la confiabilidad como parte de la experiencia de escritorio

La shell visual es solo una parte de una estación de trabajo confiable. El
trabajo de producto también debe cubrir integridad de actualizaciones,
recuperación, mensajes de error claros y primer arranque seguro. Los
repositorios firmados, snapshots y vuelta atrás al arrancar son patrones útiles
de referencia de Ryoku, pero cada uno necesita un modelo explícito de amenazas
y mantenimiento propio de HorneroOS antes de adoptarse.

### Soportar compositores por evidencia

Hyprland sigue siendo el valor por defecto validado. Niri es experimental hasta
que los gráficos, el estado de espacios de trabajo y ventanas, los portales, el
comportamiento de bloqueo, los múltiples monitores y los flujos ligados a
captura pasen la matriz de QA. No describas una abstracción genérica de
Wayland como completa mientras acciones esenciales todavía dependan de un solo
compositor. Labwc sigue siendo un backend futuro hasta tener un adaptador real
y cobertura de aceptación.

### Mantener el sitio web atado al producto en ejecución

La paleta Buenos Aires cyberpunk del sitio web y la fotografía argentina le dan
a HorneroOS una identidad reconocible. Mantené las tomas de producto reales,
los epígrafes respaldados por procedencia y la madurez de ediciones precisa.
Los proyectos de referencia pueden informar la interacción y la ingeniería de
releases, pero sus capturas, nombres y sistemas visuales no pertenecen al
material de producto de HorneroOS.

## Notas de fuentes

Las afirmaciones anteriores se basan en la documentación actual y los árboles
de código fuente de los propios proyectos:

- [README de shell de Caelestia][caelestia-shell] y
  [CLI de Caelestia][caelestia-cli].
- [README de Ryoku][ryoku-readme], [visión][ryoku-vision],
  [mapa de instalación][ryoku-install] y [entrega de paquetes][ryoku-pkg].
- [Temas de Omarchy][omarchy-theme] y [CLI][omarchy-cli].
- [Estado de ediciones][h-editions], [estado de instalación][h-install],
  [integraciones de terminal][h-terms] y
  [documentación de arquitectura](../architecture/README.md) de HorneroOS.

## Cadencia de revisión

Actualizá este estudio cuando un proyecto referenciado cambie un límite de
producto que afecte decisiones de HorneroOS, o cuando HorneroOS publique una
capacidad que cambie la comparación. Registrá la evidencia de repositorio y los
resultados de pruebas junto con el cambio. No conviertas cantidad de
estrellas, frecuencia de releases o volumen de capturas en afirmaciones de
calidad.

[renderers]: https://github.com/HorneroOS/config/blob/main/lib/hornero/terminal_themes.py
[apply]: https://github.com/HorneroOS/config/blob/main/lib/hornero/apply-appearance.sh
[tests]: https://github.com/HorneroOS/config/blob/main/tests/test_apply_official.sh
[caelestia-shell]: https://github.com/caelestia-dots/shell#readme
[caelestia-cli]: https://github.com/caelestia-dots/cli
[ryoku-readme]: https://github.com/Ryoku-dev/ryoku#readme
[ryoku-vision]: https://github.com/Ryoku-dev/ryoku-docs/blob/main/docs/vision.mdx
[ryoku-install]: https://github.com/Ryoku-dev/ryoku/blob/main/installation/README.md
[ryoku-pkg]: https://github.com/Ryoku-dev/ryoku/blob/main/release/packages/README.md
[omarchy-theme]: https://github.com/omacom/omarchy/blob/quattro/docs/theming.md
[omarchy-cli]: https://github.com/omacom/omarchy/blob/quattro/manual/14-omarchy-cli.md
[h-editions]: https://horneroos.com/editions
[h-install]: https://horneroos.com/install
[h-terms]: https://horneroos.com/terminals
