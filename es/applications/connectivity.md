# Redes y Bluetooth

El Centro de control ofrece acceso nativo de Hornero al estado de red y
Bluetooth, pero el host sigue siendo dueño de los servicios y drivers de
dispositivos subyacentes.

## Red

El panel Red usa el servicio de red del host para mostrar y gestionar las
conexiones disponibles. En el entorno de referencia Arch actual ese servicio
es NetworkManager, con `nmcli` como herramienta de diagnóstico por línea de
comandos. Hornero Config no instala NetworkManager como dependencia de
aplicación.

Si la lista aparece vacía, verificá que el servicio de red del host esté
corriendo y que el adaptador sea visible para el sistema operativo. Evitá
pegar contraseñas o perfiles de conexión completos en reportes de bugs.

## Bluetooth

El panel Bluetooth habla con BlueZ en el host. Emparejar requiere un adaptador
Bluetooth funcionando, el servicio BlueZ y cualquier firmware necesario. Un
adaptador o servicio faltante es un problema de configuración del host;
reinstalar la Shell no va a crear el soporte de hardware.

Usá primero el estado que muestra el Centro de control. Para diagnósticos a
nivel de sistema, consultá la
[guía de NetworkManager de ArchWiki](https://wiki.archlinux.org/title/NetworkManager)
o la [guía de Bluetooth](https://wiki.archlinux.org/title/Bluetooth).

## VPN

El panel VPN gestiona conexiones ya provistas por el stack de red del host y
los plugins instalados. Hornero no agrega un proveedor de VPN en silencio.
Instalá y configurá el proveedor en el que confíes y después usá el panel para
inspeccionar o activar su conexión.
