# Menú de sesión

El menú de sesión agrupa acciones para bloquear o cerrar la sesión actual del
escritorio. Es parte de Hornero Shell y está separado de la pantalla de login
de SDDM.

## Abrir y navegar

Presioná **Super + X** para abrir el menú. Usá **Arriba** y **Abajo** para
moverte entre acciones, **Tab** y **Shift + Tab** para avanzar o retroceder, y
**Enter** para activar la acción con foco. El menú ofrece **Log out** (cerrar
sesión), **Shut down** (apagar), **Hibernate** (hibernar) y **Restart**
(reiniciar). Los comandos exactos los provee la configuración activa de
Hornero, así que un sistema puede personalizar su comportamiento.

El atajo por defecto está configurado tanto para la sesión validada de Hyprland
como para la sesión experimental de Niri. Los atajos del usuario pueden variar;
mirá [Atajos de teclado](shortcuts.md) y
[soporte de compositores](compositors.md) para el nivel de soporte actual.

## Confirmar una acción de energía

Cada acción del menú usa confirmación en dos pasos. La primera activación arma
la acción y cambia su etiqueta a **Confirm?**; activala de nuevo mientras sigue
con foco para ejecutarla. Mover el foco afuera o hacer clic en otro lado limpia
el estado armado. Presioná **Escape** una vez para desarmar una acción
pendiente; presionalo otra vez para cerrar el menú. Un clic afuera cierra el
menú donde el compositor soporta esa interacción.

Esta confirmación ayuda a evitar que una tecla apretada por accidente cierre la
sesión. Para un bloqueo rápido sin abrir el menú, presioná **Super + L**. La
[guía de bloqueo y login](../applications/login-lock.md) explica el bloqueo de
sesión y la pantalla de login separada.

## Configuración

La configuración empaquetada define los comandos de acción, los íconos y la
animación opcional de sesión del menú. La configuración personal puede
sobrescribir esos valores. Usá las rutas de configuración soportadas en vez de
editar archivos empaquetados; `horneroctl config paths` informa qué archivos
están activos. La implementación y los detalles de interacción viven en el
[módulo de sesión de Hornero Shell](https://github.com/HorneroOS/shell/tree/main/modules/session)
y la [guía de interacción](https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md).
