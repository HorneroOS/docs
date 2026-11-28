# Usá el escritorio

El escritorio de Hornero se construye alrededor de la sesión Quickshell.
Una barra o riel da acceso rápido a los espacios de trabajo y a las
acciones de la shell; el lanzador abre aplicaciones y comandos; el
Dashboard reúne resúmenes del escritorio; y el Centro de control contiene
los ajustes persistentes del sistema y de la shell.

## Buscá una tarea

| Tarea | Guía |
| --- | --- |
| Usar el recorrido First Flight, Explore y What's New | [Hornero Welcome](hornero-welcome.md) |
| Entender el aspecto Hornero Signal | [Hornero Signal](hornero-signal.md) |
| Elegir un aspecto coordinado | [Temas y apariencia](appearance.md) |
| Colorear el escritorio desde un fondo o un color | [Hornero Chromatic](chromatic.md) |
| Encontrar un ajuste en el Centro de control | [Mapa del Centro de control](control-center.md) |
| Instalar, actualizar o quitar una extensión | [Extensiones](extensions.md) |
| Cambiar cómo se comporta el escritorio: Focus, Signal, Gaming | [Modos de experiencia](experience-modes.md) |
| Capturar, aplicar y sincronizar configuraciones universales del espacio de trabajo | [Perfiles e instantáneas](profiles-snapshots.md) |
| Cambiar o entender un fondo | [Fondos](wallpapers.md) |
| Elegir o solucionar un compositor de sesión | [Compositores Wayland](compositors.md) |
| Entender popups, Escape y movimiento reducido | [Popups, foco y movimiento](popups-and-motion.md) |
| Moverte entre rieles, barras, islas o docks | [Layouts](layouts.md) |
| Bloquear, reiniciar o apagar la sesión | [Menú de sesión](session-menu.md) |
| Usar bien el teclado | [Atajos](shortcuts.md) |
| Abrir archivos o lanzar aplicaciones | [Apps cotidianas](everyday-apps.md) |
| Descubrir, instalar y administrar aplicaciones | [Hornero Apps](hornero-apps.md) |
| Entender cómo encajan las aplicaciones configuradas | [Apps y flujos](../applications/README.md) |
| Abrir una página de Ajustes o automatizar un cambio | [horneroctl](horneroctl.md) |
| Actualizar el sistema y entender los límites de recuperación | [Actualizaciones y recuperación: todavía no hay vuelta atrás del sistema](updates-and-rollback.md) |
| Arrancar kernel principal o de respaldo | [Kernel y arranque de respaldo](kernel-and-fallback.md) |

## Superficies del escritorio

- El **lanzador** busca aplicaciones y ofrece acciones de la shell.
- El **Dashboard** reúne información útil del escritorio sin reemplazar a
  las aplicaciones dedicadas.
- El **Centro de control** agrupa conectividad, medios, apariencia, shell
  y controles del sistema.
- El **selector de layouts** previsualiza la topología de la barra antes
  de elegir un layout.
- **Notificaciones, OSD y menú de sesión** tienen trabajos distintos: las
  notificaciones guardan eventos accionables, el OSD refleja cambios de
  hardware de corta vida y el
  [menú de sesión](session-menu.md) contiene las acciones de
  bloqueo y energía.
- El **Companion** es un personaje chico de la shell, no una fuente de
  actividad del sistema.

Estas superficies son parte del paquete de la shell. Su implementación y
sus contratos de foco de teclado viven en el
[repositorio Shell](https://github.com/HorneroOS/shell/tree/main/docs).

HorneroOS Desktop es Wayland-first. Hyprland es el valor por defecto
validado; [Niri es experimental](compositors.md) y tiene una
superficie de funciones verificada menor. La misma identidad de Hornero
Shell abarca ambos backends donde las capacidades están implementadas.

## Límites de configuración

Usá el Centro de control para los ajustes interactivos soportados y
`horneroctl` para scripts y diagnósticos. `horneroctl config paths`
informa qué archivos de usuario están activos; `horneroctl config
validate` chequea la configuración materializada de la shell. El
[repositorio de configuración](https://github.com/HorneroOS/config) es
dueño de los valores de fábrica. Mantené tus cambios personales en tu
configuración de usuario en vez de editar archivos empaquetados.
