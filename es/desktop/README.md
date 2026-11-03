# Usá el escritorio

El escritorio de Hornero se construye alrededor de la sesión Quickshell.
Una barra o riel da acceso rápido a los espacios de trabajo y a las
acciones de la shell; el lanzador abre aplicaciones y comandos; el
Dashboard reúne resúmenes del escritorio; y el Centro de control contiene
los ajustes persistentes del sistema y de la shell.

## Buscá una tarea

| Tarea | Guía |
| --- | --- |
| Elegir un aspecto coordinado | [Temas y apariencia](../../desktop/appearance.md) |
| Cambiar o entender un fondo | [Fondos y color](../../desktop/wallpapers.md) |
| Elegir o solucionar un compositor de sesión | [Compositores Wayland](../../desktop/compositors.md) |
| Moverte entre rieles, barras, islas o docks | [Layouts](../../desktop/layouts.md) |
| Bloquear, reiniciar o apagar la sesión | [Menú de sesión](../../desktop/session-menu.md) |
| Usar bien el teclado | [Atajos](../../desktop/shortcuts.md) |
| Abrir archivos o lanzar aplicaciones | [Apps cotidianas](../../desktop/everyday-apps.md) |
| Entender cómo encajan las aplicaciones configuradas | [Apps y flujos](../applications/README.md) |
| Abrir una página de Ajustes o automatizar un cambio | [horneroctl](../../desktop/horneroctl.md) |

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
  [menú de sesión](../../desktop/session-menu.md) contiene las acciones de
  bloqueo y energía.
- El **Companion** es un personaje chico de la shell, no una fuente de
  actividad del sistema.

Estas superficies son parte del paquete de la shell. Su implementación y
sus contratos de foco de teclado viven en el
[repositorio Shell](https://github.com/HorneroOS/shell/tree/main/docs).

HorneroOS Desktop es Wayland-first. Hyprland es el valor por defecto
validado; [Niri es experimental](../../desktop/compositors.md) y tiene una
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
