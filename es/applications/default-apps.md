# Aplicaciones por defecto

Hornero usa archivos `.desktop` y asociaciones MIME para que puedas elegir tu
propio navegador, editor, visor de PDF, visor de imágenes, reproductor de
video, reproductor de audio y gestor de archivos. El release actual de Hornero
no exige un navegador, editor, visor de imágenes, lector de PDF ni reproductor
multimedia en particular. Mirá
[Navegación, edición y documentos](browsing-documents.md) para ejemplos
prácticos y distinciones de paquetes.

## Cómo funciona el lanzamiento de aplicaciones

Los atajos por defecto del compositor activo le piden a `exo-open` el
manejador XDG `TerminalEmulator`, `FileManager` o `WebBrowser`. Los tipos de
archivo como `text/plain`, `application/pdf` e `image/png` usan asociaciones
MIME. Una asociación faltante o un archivo `.desktop` inexistente puede hacer
que falle un atajo o la apertura de un archivo.

El repositorio de configuración actual provee una configuración opcional de
`handlr`. `horneroctl config default-apps list` lee el helper de terminal de
Exo, la preferencia genérica XDG de terminal y los valores MIME por defecto
actuales. Si `handlr` opcional no está instalado, igual informa los ajustes de
terminal y marca los valores MIME como no disponibles. La respuesta JSON
también lista los comandos de terminal soportados encontrados en `PATH` para
que los muestre Ajustes. Informa lo que está configurado en esta máquina, no
lo que instala Hornero. Un archivo `<desktop>-xdg-terminals.list` específico
del escritorio puede sobrescribir la preferencia genérica XDG para una sesión
particular.

## Cambiar una asociación de archivo

Para asociaciones de archivos, usá la app de ajustes del escritorio del host o
la CLI. Primero buscá el ID `.desktop` de la aplicación, generalmente un
archivo bajo `/usr/share/applications/`, luego previsualizá y aplicá el cambio
MIME:

```sh
horneroctl config default-apps set application/pdf org.example.Reader.desktop --dry-run
horneroctl config default-apps set application/pdf org.example.Reader.desktop --yes
```

Reemplazá el ID de ejemplo por un archivo `.desktop` instalado. Los cambios
MIME usan `xdg-mime`. Para cambiar la terminal usada por **Super + T** o
**Super + Enter**, abrí **Ajustes → Terminal** en Hornero Shell y elegí una
opción instalada, o definí la preferencia de terminal con la CLI:

```sh
horneroctl config default-apps set terminal ghostty --dry-run
horneroctl config default-apps set terminal ghostty --yes
```

Ajustes lista las terminales soportadas encontradas en `PATH`. El selector de
terminal soporta Kitty, Alacritty y Ghostty, y requiere que el programa
elegido esté instalado. Mantiene alineados el helper `TerminalEmulator` de Exo
y la preferencia genérica `$XDG_CONFIG_HOME/xdg-terminals.list` (o
`~/.config/xdg-terminals.list`). Las entradas existentes de helpers,
comentarios, directivas y otras opciones de terminal permanecen en su lugar;
se quita cualquier exclusión de respaldo de la terminal elegida para que pueda
seleccionarse. La terminal elegida toma la primera prioridad en la lista XDG.
Cuando está instalado, `xdg-terminal-exec` lee esa preferencia. Los archivos
de preferencia específicos del escritorio pueden seguir teniendo precedencia.
`--dry-run` informa ambas rutas destino sin escribir; `--yes` es obligatorio
para aplicar.

Para revisar los nombres de aplicaciones seleccionadas y los backends de
lanzamiento disponibles, corré:

```sh
horneroctl config default-apps list
horneroctl apps launch --list
```

## Elección de navegador y editor

**Super + W** lanza el manejador `WebBrowser` actual. Hornero no elige un
navegador universal. Zen Browser aparece en los scripts personales de
aprovisionamiento de dotfiles, así que debe tratarse como una elección
personal opcional.

No hay un editor por defecto para todo Hornero. Instalá un editor y definí su
ID `.desktop` para `text/plain` si querés que hacer doble clic en archivos de
texto lo abra. Quienes usan la línea de comandos pueden definir `$EDITOR` en
su propia configuración de shell; Hornero Config no incluye un archivo de
arranque de shell de usuario.

Otros valores por defecto también son elecciones del sistema. Revisá y definí
el tipo MIME correspondiente para imágenes (`image/png`), video (`video/mp4`),
audio (`audio/mpeg`) y PDF (`application/pdf`). Los controles multimedia MPRIS
de la Shell están separados de la asociación de archivo usada para abrir un
archivo multimedia.

La asociación MIME se aplica a archivos abiertos desde gestores de archivos y
otras aplicaciones compatibles con XDG. No cambia a qué programa apuntan los
controles MPRIS de la Shell ni qué terminal inicia una shell.

Para el flujo actual de directorios y gestor de archivos, mirá
[Archivos](files.md). Para controles de reproducción multimedia, mirá
[Medios y audio](media-audio.md), y para más guías por tipo de aplicación mirá
[Navegación, edición y documentos](browsing-documents.md). Referencias
upstream: [especificación XDG MIME applications](https://www.freedesktop.org/wiki/Specifications/mime-apps-spec/),
[exo](https://docs.xfce.org/xfce/exo/start),
[XDG default terminal execution](https://github.com/Vladimir-csp/xdg-terminal-exec),
[handlr-regex](https://github.com/chmln/handlr).
