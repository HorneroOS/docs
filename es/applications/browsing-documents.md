# Navegación, edición y documentos

Hornero no exige un navegador, editor gráfico, visor de imágenes ni lector de
PDF en particular. Le pide al registro de aplicaciones XDG del escritorio que
abra un enlace web o un archivo, para que puedas elegir las herramientas que
mejor se adapten a tu trabajo.

## Navegación

Presioná **Super + W** para abrir el manejador `WebBrowser` del host. El
navegador lo selecciona el entorno de escritorio; Hornero Config no instala ni
fija un navegador universal. El
[repositorio público de dotfiles](https://github.com/ulises-jeremias/dotfiles)
puede instalar Zen Browser en una estación de trabajo Arch personal, pero es
una elección personal opcional.

Si un enlace no hace nada, verificá que haya un paquete de navegador
instalado, que provea una entrada de escritorio bajo
`/usr/share/applications/` y que haya un manejador XDG `WebBrowser` elegido.
`horneroctl config default-apps list` informa los manejadores de escritorio
visibles actualmente. La privacidad, sincronización y perfiles del navegador
pertenecen al navegador que elijas.

Ejemplos upstream: [Firefox](https://support.mozilla.org/products/firefox),
[Zen Browser](https://docs.zen-browser.app/).

## Editores

No existe un editor gráfico único para todo Hornero. Instalá el editor que
prefieras y elegí su entrada de escritorio para `text/plain`. Los programas de
shell usan `$EDITOR` o `$VISUAL` solo cuando esas variables de entorno están
definidas. El perfil personal de Zsh en dotfiles define ambas como `nvim`;
Hornero no fija ese valor globalmente.

Revisá la entrada de escritorio de un editor antes de cambiar la asociación:

```sh
horneroctl config default-apps list
horneroctl config default-apps set text/plain org.example.Editor.desktop --dry-run
horneroctl config default-apps set text/plain org.example.Editor.desktop --yes
```

Reemplazá `org.example.Editor.desktop` por un ID de archivo `.desktop`
instalado. El comando actualiza esa asociación MIME; no define un editor de
terminal para cada shell o aplicación. Mirá el
[manual de usuario de Neovim](https://neovim.io/doc/user/) si usás el perfil
de estación de trabajo personal. Cuando usás
[Hornero Chromatic](../desktop/chromatic.md#plantillas-de-aplicaciones),
también renderiza `:colorscheme hornero-chromatic` para Neovim y un tema
`hornero-chromatic` para Helix.

## PDFs, imágenes y archivos multimedia

Hacer doble clic en un PDF, una imagen, un audio o un video usa su asociación
MIME. El abridor de archivos es independiente de los controles multimedia de
la Shell. Un host puede usar programas distintos para formatos de imagen o
tipos multimedia; Hornero no asume un paquete único. `poppler` e ImageMagick
pueden ayudar con vistas previas de archivos, pero ninguno es un visor gráfico
de PDF o imágenes.

Cuando un tipo abre en el programa equivocado, inspeccioná la asociación en
vez de tocar los controles multimedia:

```sh
xdg-mime query default application/pdf
xdg-mime query default image/png
xdg-mime query default video/mp4
xdg-mime query default audio/mpeg
```

Si el resultado nombra una aplicación que no está instalada, instalá o elegí
una entrada de escritorio válida y después definí el tipo MIME correspondiente
con [`horneroctl config default-apps`](default-apps.md). El flujo personal de
Yazi puede abrir video en `mpv` cuando está instalado; eso no define el
reproductor por defecto del sistema.

Para manejo de archivos comprimidos y vistas previas, mirá [Archivos](files.md).
Para controles de reproducción activos y ruteo de audio, mirá
[Medios y audio](media-audio.md). La
[especificación XDG MIME Applications](https://specifications.freedesktop.org/mime-apps-spec/latest/)
describe el modelo de asociaciones del escritorio.
