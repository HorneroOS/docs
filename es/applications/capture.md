# Capturas y grabación

Hornero rutea los comandos de captura de pantalla a través de
`horneroctl capture`. Los backends disponibles de captura y grabación dependen
de qué herramientas del host estén instaladas y puedan acceder a la sesión
Wayland.

## Capturas de pantalla

- Presioná **Print** para capturar la pantalla.
- Presioná **Shift + Print** para seleccionar una región.
- Previsualizá una captura con `horneroctl capture screenshot --dry-run`.

La CLI empaquetada resuelve el helper de capturas `sss` cuando está
disponible. El repositorio personal de dotfiles instala `sss` con soporte de
`grim` y `slurp`. Esos paquetes no son dependencias de Hornero Config. Sin el
helper, el comando de captura informa que falta su backend en vez de instalar
software en silencio.

## Grabación de pantalla

La CLI y la Shell exponen acciones de grabación respaldadas por GPU Screen
Recorder. Revisá sus opciones disponibles antes de grabar:

```sh
horneroctl capture record start --dry-run
horneroctl capture record stop --dry-run
```

Grabar escribe archivos e inicia un proceso. Los comandos que modifican estado
requieren `--yes` explícito; usá primero la opción dry-run documentada al
armar scripts. La carpeta de salida sigue el directorio XDG Videos del usuario
cuando está disponible.

## Solución de problemas

- Una captura o grabación puede fallar si falta el helper, si el directorio de
  salida no tiene permisos de escritura o si el protocolo de captura del
  compositor no está disponible.
- Para una captura de región, verificá que esté instalado el backend selector.
- Dejá las grabaciones fuera de logs de soporte salvo que hayas revisado el
  archivo para quitar contenido privado.

Upstream: [grim](https://github.com/emersion/grim),
[slurp](https://github.com/emersion/slurp),
[GPU Screen Recorder](https://git.dec05eba.com/gpu-screen-recorder/about/).
Mirá también la [ayuda de captura de la CLI de Hornero](../desktop/horneroctl.md).
