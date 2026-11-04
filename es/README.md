# Documentación de Hornero OS

Buscá una guía según la tarea que querés completar. Este repositorio es el
manual de usuarias, usuarios y colaboradores; los contratos de
implementación quedan en los repositorios de la
[Shell](https://github.com/HorneroOS/shell), la
[CLI](https://github.com/HorneroOS/hornero) y la
[configuración](https://github.com/HorneroOS/config).

> HorneroOS es una familia de sistemas operativos basada en Arch, en
> desarrollo. Su edición Desktop es Wayland-first, con Hyprland como
> compositor validado por defecto y Niri como backend experimental. Hay
> publicada una ISO Preview firmada (Desktop, Studio y Gaming Preview,
> v0.2.0-preview32); no es una release estable ni soportada, y la propia
> v0.2.0-preview32 todavía no tiene validación ni aceptación en hardware
> físico. La [página de releases](https://horneroos.com/releases) y el
> [estado de instalación](https://horneroos.com/install) son la fuente
> actual de qué se puede instalar.

## Elegí un camino

| Si querés… | Empezá acá |
| --- | --- |
| Entender el estado de releases e instalación | [Primeros pasos](getting-started/README.md) |
| Usar el escritorio, las apps y el Centro de control | [Desktop](desktop/README.md) · [Apps y flujos](applications/README.md) |
| Cambiar temas, colores o el fondo | [Apariencia](../desktop/appearance.md) · [Fondos](../desktop/wallpapers.md) |
| Elegir una disposición de barra | [Layouts](../desktop/layouts.md) |
| Bloquear, reiniciar o apagar la sesión | [Menú de sesión](../desktop/session-menu.md) |
| Buscar un atajo de teclado | [Atajos](../desktop/shortcuts.md) |
| Automatizar o inspeccionar el sistema desde una terminal | [horneroctl](../desktop/horneroctl.md) |
| Diagnosticar problemas de gráficos o dispositivos | [Hardware](hardware/README.md) · [Solución de problemas](troubleshooting/README.md) |
| Entender las ediciones y los límites del sistema | [Arquitectura](architecture/README.md) |
| Compilar, probar o contribuir | [Desarrollo](development/README.md) |
| Diseñar una interfaz para HorneroOS | [Design language](../development/design-language.md) |

## Cómo se mantiene precisa esta documentación

Los pasos describen comportamiento disponible en el producto publicado,
salvo que estén marcados como **Development** o **Preview**. La
disponibilidad de paquetes, instalador y releases puede cambiar; revisá
las páginas vivas de releases e instalación antes de seguir notas viejas.
Los comandos salen de la ayuda de `horneroctl` y de la configuración
actual del producto. Los ejemplos de máquinas personales de la antigua
wiki de dotfiles no son requisitos del sistema.

El sitio web importa estas páginas Markdown en un commit revisado y suma
su propia navegación, búsqueda y presentación responsive. Este
repositorio es dueño del contenido; el sitio no mantiene una segunda
copia.

## Áreas

- [Primeros pasos](getting-started/README.md) — estado de releases y una
  primera mirada segura.
- [Desktop](desktop/README.md) — apariencia, fondos, layouts, compositores
  y atajos.
- [Apps y flujos](applications/README.md) — el catálogo de aplicaciones
  configurado y los caminos que conectan esas herramientas con Hornero.
- [horneroctl](../desktop/horneroctl.md) — puntos de entrada de línea de
  comandos soportados.
- [Hardware](hardware/README.md) — diagnóstico de dispositivos y guía de
  gráficos.
- [Solución de problemas](troubleshooting/README.md) — recuperate de los
  fallos comunes.
- [Arquitectura](architecture/README.md) — ediciones, propiedad y flujo de
  datos.
- [Desarrollo](development/README.md) — código, QA y caminos de
  contribución.
- [Design language](../development/design-language.md) — identidad del
  producto, principios de UI, mapa de fuentes de verdad y guía para quien
  contribuye al instalador.

## Licencia

[MIT](../LICENSE).
