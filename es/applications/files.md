# Archivos y carpetas

Hornero soporta un gestor de archivos gráfico y un explorador de archivos en
terminal. Sirven para tareas distintas y comparten los mismos archivos en
disco.

## Thunar para gestión visual de archivos

Presioná **Super + F** para abrir la asociación XDG `FileManager` del host
mediante `exo-open`. Thunar es el gestor de archivos gráfico curado en Hornero
Config y trae valores por defecto para aceleradores, renombrado masivo y dos
acciones personalizadas útiles. La configuración de usuario vive bajo
`~/.config/Thunar/`; los valores por defecto del paquete están bajo
`/etc/xdg/Thunar/`. El paquete `hornero-config` no instala `uca.xml` en la
ruta del sistema porque Thunar es dueño de ese archivo; una materialización de
usuario puede igual proveer las acciones en la configuración del usuario.

Cuando arranca la sesión configurada, le pide al demonio de Thunar que quede
listo para que las ventanas siguientes abran más rápido. Las acciones del menú
contextual **Open in Yazi** y **Open Terminal Here** usan la asociación de
terminal elegida; **Open in Yazi** también necesita Yazi instalado. Son flujos
integrados, no programas de compresión ni terminales empaquetados.

Upstream: [documentación de Thunar](https://docs.xfce.org/xfce/thunar/start).

La captura de abajo muestra ambos gestores lado a lado sobre la misma carpeta
de demostración: vista de íconos de Thunar a la izquierda y columnas manejadas
por teclado de Yazi a la derecha. La carpeta es contenido demo del equipo del
maintainer, no parte del paquete base de Hornero.

![Thunar y Yazi lado a lado sobre la misma carpeta. Thunar muestra íconos de
carpetas y un archivo README a la izquierda; Yazi muestra el árbol de
directorios, las entradas de la carpeta actual y una columna de vista previa
vacía a la derecha.](https://www.horneroos.com/captures/cap-term-06.png)

*Thunar (izquierda) y Yazi (derecha) sobre una carpeta demo preparada. Captura
de escritorio en vivo en el equipo del maintainer, 19 de noviembre de 2026.*

## Yazi para navegar desde el teclado

Presioná **Super + E** para abrir Yazi en una ventana de la terminal
configurada y restaurar su último directorio. El valor inicial de Hornero es
Kitty. Si elegís Alacritty o Ghostty como terminal, el mismo flujo sigue esa
selección. Desde adentro de una terminal existente,
`horneroctl apps terminal-file` abre Yazi en la ventana actual; usá
`--new-window` para abrir una ventana de terminal aparte. La CLI también puede
abrir un directorio o seleccionar un archivo:

```sh
horneroctl apps terminal-file --help
horneroctl apps terminal-file --cheatsheet
horneroctl apps terminal-file --path ~/Downloads
horneroctl apps terminal-file --new-window --path ~/Downloads
```

Hornero Config no declara Yazi como dependencia. Tanto la terminal configurada
como Yazi deben estar instalados para este flujo. Cambiá la terminal con
[`horneroctl config default-apps`](default-apps.md). El
[repositorio público de dotfiles](https://github.com/ulises-jeremias/dotfiles)
puede instalar Yazi y helpers de vista previa para una estación de trabajo
Arch personal; no son dependencias de la composición de release de Hornero.

Los atajos de Yazi se pueden consultar desde la hoja de referencia de la CLI
de Hornero. En la configuración personal, `~/.config/yazi/yazi.toml`,
`keymap.toml` y `theme.toml` definen abridores de archivos, atajos extra y
colores de terminal. Ese perfil suma atajos de directorios con `g`, `D D` para
mandar elementos a la papelera y `Alt + T` para abrir una selección en Thunar.
El soporte de vistas previas depende de herramientas opcionales del host como
`ffmpegthumbnailer`, `poppler` e ImageMagick; que falte una vista previa no
significa que falte el archivo. Upstream de Yazi:
[documentación](https://yazi-rs.github.io/docs/). En la captura de arriba, la
columna de vista previa de Yazi está vacía porque hay una carpeta seleccionada.

## Apertura de archivos y archivos comprimidos

`exo-open` lanza el gestor de archivos y la terminal por defecto. `handlr` y
`xdg-mime` resuelven asociaciones MIME, como qué app abre un PDF o una imagen.
Thunar delega operaciones de archivos comprimidos a utilidades y plugins
compatibles instalados en el host; Xarchiver es una elección opcional de la
estación de trabajo personal. Yazi puede listar y extraer archivos comprimidos
cuando están disponibles las herramientas de vista previa y compresión
correspondientes. Hornero Config no descarga helpers faltantes.

Inspeccioná el manejador actual de directorios con:

```sh
horneroctl apps files --info
horneroctl config default-apps list
```

Cambiá una asociación de archivo siguiendo las instrucciones en
[Aplicaciones por defecto](default-apps.md). Hornero no instala ni descarga en
silencio dependencias de compresión o vista previa.
