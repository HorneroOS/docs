# Pantalla de bloqueo y login

La pantalla de bloqueo y la pantalla de login corren en momentos distintos de
una sesión. Hyprlock bloquea una sesión activa de Hyprland. SDDM y Hornero
Greeter muestran la pantalla de login antes de que empiece una sesión.

## Bloquear la sesión

Presioná **Super + L** para pedir un bloqueo a Hornero Shell. Hypridle maneja
los temporizadores de inactividad en la sesión configurada y puede pedir un
bloqueo antes de acciones de energía de pantalla o suspensión. El host debe
tener instaladas las herramientas de Hyprland y los servicios de sistema
correspondientes.

![La pantalla de sesión bloqueada: un reloj grande y fecha sobre un fondo
oscuro, un campo de contraseña en un panel chico y una tarjeta de
notificaciones que queda ilegible hasta desbloquear.](https://www.horneroos.com/captures/cap-lock-01.png)

*La pantalla de bloqueo de sesión (Hyprlock) en el equipo del maintainer — el
nombre de usuario mostrado es el suyo. Esta es la pantalla de bloqueo, no el
greeter de login. Captura, 19 de noviembre de 2026.*

Si la pantalla no se bloquea, revisá primero la Shell y la sesión de Hyprland:

```sh
horneroctl doctor
horneroctl shell logs --lines 100
```

No corras un segundo bloqueador en paralelo con el bloqueador activo de la
sesión.

![Ajustes, página Pantalla de bloqueo con interruptores para ocultar
notificaciones al bloquear, recolorear el logo, desbloqueo con huella digital
con contador de intentos, la línea de marca, reloj de 12 horas y ancho del
panel de bloqueo.](https://www.horneroos.com/captures/cap-cc-12.png)

*Ajustes → Pantalla de bloqueo: privacidad, huella digital y apariencia del
próximo bloqueo. Captura de escritorio en vivo en el equipo del maintainer,
19 de noviembre de 2026.*

## Hornero Greeter

Hornero Greeter es un paquete opcional de tema SDDM mantenido en
[HorneroOS/greeter](https://github.com/HorneroOS/greeter). SDDM es dueño del
servicio de login y elige su tema mediante la configuración de SDDM del
sistema. Los perfiles de release actuales de Hornero no instalan ni configuran
SDDM como lo haría un instalador para usuario final.

El empaquetado del greeter, los requisitos de runtime Qt, los assets y las
instrucciones de release pertenecen a ese repositorio. Después de cambiar un
paquete de greeter o un tema SDDM, inspeccioná su camino documentado de vista
previa y los archivos del paquete antes de confiar en el próximo login. No
reinicies SDDM desde un escritorio activo solo para probar un tema.

Mirá [estado de releases](https://horneroos.com/releases),
[estado de instalación](https://horneroos.com/install) y el
[repositorio del greeter](https://github.com/HorneroOS/greeter) antes de
instalar o actualizar componentes de login.
