# Arquitectura de apariencia

Esta página describe la propiedad y el flujo de datos para colaboradores. Para
el modelo de usuario, empezá por [Hornero Signal](../desktop/hornero-signal.md),
[Apariencia](../desktop/appearance.md) y [Fondos](../desktop/wallpapers.md). La
autoridad de diseño es
[RFC 0001 — Hornero Signal](../../development/rfc-0001-hornero-signal.md); los
nombres de tokens, familias tipográficas, la API de glifos, los nombres de
movimiento y el contrato de superficies ancladas solo cambian enmendándola.

## Propiedad

- **`HorneroOS/config`** es dueño del contrato de tokens
  (`profiles/themes/tokens.schema.json`, versión de esquema 2), de todos los
  paquetes de temas, del catálogo de temas generado, de los manifiestos y
  créditos de fondos, de los assets de marca, de los generadores para
  GTK/Qt/terminales/compositor (`lib/hornero/signal_theme.py`,
  `lib/hornero/signal_render.py`) y de los valores de fábrica, incluidos
  Cockpit y Signal Night.
- **`HorneroOS/shell`** es dueño de la presentación en vivo: el singleton
  `Signal` (`Signal.palette.<role>`), los roles tipográficos IBM Plex, Hornero
  Glyphs, los tokens de movimiento, las vistas previas de temas, los overrides
  de accesibilidad y el solver de superficies ancladas.
- **`HorneroOS/hornero`** es dueño de las operaciones estables de `horneroctl`:
  resolución del catálogo, aplicación y verificación de temas, migración única
  de selecciones retiradas, diagnósticos y reporte de errores.
- **Los datos de usuario** guardan overrides explícitos y estado generado en
  los directorios de configuración, estado y caché del usuario. Los catálogos
  del sistema bajo `/usr/share` son de solo lectura.

El catálogo de temas se genera a partir de los paquetes instalados; no es una
segunda lista mantenida a mano. Las lecturas consultan primero el catálogo del
usuario y después el catálogo de solo lectura del sistema.

## Un solo tipo de paquete de tema

Cada tema es `profiles/themes/<id>/theme.json` con `schemaVersion: 2`: `id`,
`name`, `mode` (`dark` o `light`), `palette` (exactamente los roles de la
RFC §3.1, más el `glow` opcional), `terminal` (16 colores), `gtkTheme`,
`iconTheme`, `defaultWallpaper` y `wallpaperDir`; `description`, `tags`,
`collection` y `collectionOrder` son metadatos opcionales de presentación. No
hay semillas, tipos de esquema, variantes ni paquetes parciales "de receta". Un
paquete que no defina el conjunto completo de roles es inválido, y el chequeo
de contraste de Config corre sobre cada paquete publicado.

`collection` describe solo autoría y presentación (`hornero-signal`,
`hornero-originals`, ports de la comunidad); nunca implica un modelo de tokens
distinto.

## Flujo de color

```text
paquete de tema de config (esquema v2)
          │  horneroctl appearance theme apply|set   (o la shell, para los incorporados)
          ▼
$XDG_STATE_HOME/hornero/signal/scheme.json   ← escrito de forma atómica
          │
          ├── Shell: observa el archivo → Signal.palette.<role>
          ├── Bordes de Hyprland, variables de hyprlock
          ├── Include de Kitty, paletas de Alacritty, Ghostty, btop y Cava
          ├── Recoloreado GTK 3/4 + libadwaita (árbol gtkTheme del paquete)
          └── Qt vía esquema de color de qt6ct
```

El esquema en vivo es
`{"schemaVersion":2,"id":…,"mode":…,"palette":{role:"#RRGGBB"},"terminal":[16]}`.
Para los temas curados, los fondos nunca alimentan este flujo y el puntero del
fondo es un archivo aparte que la shell observa solo por la imagen. El tema
opcional **Hornero Chromatic** (`hornero-chromatic`,
[RFC 0002](../development/rfc-0002-hornero-chromatic.md), implementado en
`main`; guía de usuario: [Hornero Chromatic](../desktop/chromatic.md)) suma un
paso delante del mismo escritor: `horneroctl` ejecuta el helper nativo
`hornero-chromatic` (incluido con la shell) para sintetizar los roles Signal a
partir del fondo, una imagen o un color elegido, los valida contra la tabla de
compuertas de config y luego escribe el esquema en vivo y cada salida igual que
para un tema curado. No hay paso Material ni Python en ese camino.

Alto contraste (`appearance.highContrast`) es un override solo de la shell: la
shell renderiza la tabla `hornero-signal-contrast` y desactiva la
translucidez sin cambiar el tema persistido. Movimiento reducido
(`appearance.reducedMotion` o `enable-animations` de GNOME) pone las duraciones
en cero salvo fundidos cortos de opacidad.

Mantené la lógica de visualización en QML, la coordinación de sesión en vivo en
servicios de la shell, las operaciones de SO en `horneroctl` y los datos en los
paquetes de Config. `horneroctl` sigue siendo usable sin el Centro de control.

## Aplicar y recuperar

Aplicar un tema escribe primero el esquema en vivo de forma atómica, luego los
archivos derivados, después GTK, y persiste la selección. Cada consumidor tiene
capacidades distintas en tiempo de ejecución, así que toda la aplicación es una
transacción verificada de mejor esfuerzo en vez de un solo rename atómico. Debe
validar el paquete antes de escribir, chequear el estado resultante, informar
fallas parciales con precisión y, para `appearance theme set`, volver al tema
incorporado anterior si algo falla. Nunca informes éxito solo porque arrancó un
proceso.

Los IDs retirados (`hornero-dark`, `hornero-light`, `hornero-199x`,
`neon-city`, `vapor-dreams`, `soft-morning`, `warm-sunset`) son rechazados por
`apply` indicando su reemplazo. Una selección persistida que nombre alguno de
ellos migra una sola vez, al cargar la shell o mediante
`horneroctl appearance sync --yes`. Es una migración de datos, no una capa de
alias.

El contrato de comandos está documentado en
[horneroctl](../desktop/horneroctl.md) y en `horneroctl appearance --help`.

## Archivos multimedia de fondos

Los binarios de los fondos están separados de los metadatos del paquete. Los
manifiestos de Config nombran el archivo esperado y su origen; las fotografías
con licencia y sus créditos vienen con `hornero-config`, y los fondos de Signal
se renderizan desde SVG en el equipo destino. Un fondo por defecto faltante
produce un estado no disponible, no un tema malformado. Nunca se descarga una
imagen como efecto secundario de elegir un tema.

## Checklist de cambios

Al cambiar datos o comportamiento de apariencia, actualizá la fuente dueña y
sus tests, y después revisá los consumidores aguas abajo:

- RFC 0001, si cambia un rol, una familia, la API de glifos o un nombre de
  movimiento.
- Esquema de Config, paquetes, chequeo de contraste y catálogo generado.
- Aplicación, verificación, migración y reporte de errores en `horneroctl`.
- Roles `Signal` de la Shell, vistas previas y renderizado en vivo.
- Salida para GTK, íconos, Qt y terminales.
- Evidencia de QA para transiciones visibles al usuario, indicando dónde corrió.
- Datos de producto y capturas del sitio web solo después de que el
  comportamiento se haya publicado.

Referencias de implementación: [config](https://github.com/HorneroOS/config),
[shell `docs/NATIVE-APPEARANCE.md`](https://github.com/HorneroOS/shell/blob/main/docs/NATIVE-APPEARANCE.md)
y [hornero](https://github.com/HorneroOS/hornero).
