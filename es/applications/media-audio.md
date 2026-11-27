# Medios y audio

La Shell provee controles alrededor de los dispositivos de audio y los
reproductores multimedia del host. No reemplaza al servidor de audio ni al
reproductor dueño de la música o el video.

## Dispositivos de audio

La página Audio en el Centro de control elige los dispositivos de salida y
entrada del host. Las teclas de volumen cambian la salida por defecto, la
tecla de micrófono alterna la entrada por defecto y la Shell muestra un aviso
OSD breve de volumen. Un mezclador como `pavucontrol` puede exponer flujos por
aplicación y ruteo de dispositivos; es una aplicación opcional del host, no la
instala `hornero-config`.

PipeWire y WirePlumber son componentes habituales de audio en Arch, pero su
instalación exacta y estado de servicios pertenecen a la configuración del
host. Revisá el estado actual en el Centro de control antes de cambiar
servicios. Mirá la
[guía de PipeWire de ArchWiki](https://wiki.archlinux.org/title/PipeWire) y
[pavucontrol](https://freedesktop.org/software/pulseaudio/pavucontrol/).

## Reproductores de medios

La Shell observa reproductores compatibles con MPRIS y muestra los metadatos y
controles de transporte del reproductor activo. Las teclas multimedia usan
`playerctl` en la configuración curada de Hyprland. El reproductor lo elige el
usuario; mpv es una herramienta opcional de reproducción en el setup personal
de dotfiles, no una dependencia obligatoria de Hornero.

Abrir un archivo de audio o video usa la asociación MIME del host. Esto es
independiente del reproductor seleccionado actualmente para los controles
multimedia de la Shell. Mirá [Aplicaciones por defecto](default-apps.md) para
cambiar asociaciones de archivos.

## Visualizador

Cava es opcional y usa un tema de Hornero Config que sigue el tema aplicado en
el escritorio. El visualizador de escritorio de la Shell viene desactivado por
defecto. Activarlo requiere una fuente de audio funcionando y la integración
de audio configurada; tener Cava instalado por sí solo no lo inicia.

Solución de problemas:

- Si el OSD de volumen se mueve pero el sonido no cambia, verificá el servicio
  de audio del host y el dispositivo de salida seleccionado.
- Si los controles multimedia no muestran ningún reproductor, iniciá un
  reproductor compatible con MPRIS.
- Si las teclas multimedia no hacen nada, verificá que `playerctl` esté
  instalado y que el reproductor activo acepte comandos MPRIS.

Upstream: [MPRIS](https://specifications.freedesktop.org/mpris-spec/latest/),
[playerctl](https://github.com/altdesktop/playerctl),
[manual de mpv](https://mpv.io/manual/stable/),
[Cava](https://github.com/karlstav/cava).
