# Documentación de Hornero OS

[![lint](https://github.com/HorneroOS/docs/actions/workflows/lint.yml/badge.svg)](https://github.com/HorneroOS/docs/actions/workflows/lint.yml)
[![Licencia: MIT](https://img.shields.io/github/license/HorneroOS/docs)](../LICENSE)

Buscá una guía según la tarea que querés completar. Este repositorio es el
manual de usuarias, usuarios y colaboradores; los contratos de
implementación quedan en los repositorios de la
[Shell](https://github.com/HorneroOS/shell), la
[CLI](https://github.com/HorneroOS/hornero) y la
[configuración](https://github.com/HorneroOS/config).

> HorneroOS es una familia de sistemas operativos basada en Arch, en
> desarrollo. Su edición Desktop es Wayland-first, con Hyprland como
> compositor validado por defecto y Niri como backend experimental. Hay
> publicada una ISO preview firmada (Desktop, Studio y Gaming,
> v0.2.0-preview32); no es una release estable ni soportada, y la propia
> v0.2.0-preview32 todavía no tiene validación ni aceptación en hardware
> físico. La [página de releases](https://horneroos.com/releases) y el
> [estado de instalación](https://horneroos.com/install) son la fuente
> actual de qué se puede instalar.

## Elegí un camino

| Si querés… | Empezá acá |
| --- | --- |
| Entender el estado de releases e instalación | [Primeros pasos](getting-started/README.md) |
| Instalar y dar los primeros pasos | [Instalar paso a paso](getting-started/install-step-by-step.md) · [Primeros pasos post-instalación](applications/post-install-first-steps.md) |
| Instalar sobre un Arch Linux existente | [Instalar en Arch](getting-started/install-on-arch.md) |
| Conocer qué está probado y qué no | [Probado y no probado](hardware/tested-and-untested.md) · [Problemas por síntoma](troubleshooting/by-symptom.md) |
| Usar el escritorio, las apps y el Centro de control | [Desktop](desktop/README.md) · [Apps y flujos](applications/README.md) |
| Conocer el aspecto Hornero Signal: temas, tipografía, accesibilidad | [Hornero Signal](desktop/hornero-signal.md) |
| Cambiar temas, colores o el fondo | [Apariencia](desktop/appearance.md) · [Fondos](desktop/wallpapers.md) |
| Elegir una disposición de barra | [Layouts](desktop/layouts.md) |
| Bloquear, reiniciar o apagar la sesión | [Menú de sesión](desktop/session-menu.md) |
| Buscar un atajo de teclado | [Atajos](desktop/shortcuts.md) |
| Automatizar o inspeccionar el sistema desde una terminal | [horneroctl](desktop/horneroctl.md) |
| Actualizar el sistema y entender los límites de recuperación | [Actualizaciones y recuperación: todavía no hay vuelta atrás del sistema](desktop/updates-and-rollback.md) |
| Entender seguridad, cifrado y límites de confianza | [Seguridad y privacidad](security/README.md) |
| Diagnosticar problemas de gráficos o dispositivos | [Hardware](hardware/README.md) · [Solución de problemas](troubleshooting/README.md) |
| Entender las ediciones y los límites del sistema | [Arquitectura](architecture/README.md) |
| Compilar, probar o contribuir | [Desarrollo](development/README.md) |
| Diseñar una interfaz para HorneroOS | [Lenguaje de diseño](development/design-language.md) |

![Overlay de atajos de teclado con los binds vivos de Hyprland y
buscador, grupo Essential Applications expandido.](https://www.horneroos.com/captures/cap-shell-08.png)

*El overlay de atajos, leído en vivo desde Hyprland — ver
[Atajos](desktop/shortcuts.md). Captura real; se reutiliza
intencionalmente la misma captura de esa guía, no es una copia nueva.*

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
- [Hornero Signal](desktop/hornero-signal.md) — el lenguaje visual de
  HorneroOS: temas, tipografía IBM Plex, glifos, alto contraste y
  movimiento reducido.
- [Apps y flujos](applications/README.md) — el catálogo de aplicaciones
  configurado y los caminos que conectan esas herramientas con Hornero.
- [horneroctl](desktop/horneroctl.md) — puntos de entrada de línea de
  comandos soportados.
- [Hardware](hardware/README.md) — diagnóstico de dispositivos y guía de
  gráficos.
- [Seguridad y privacidad](security/README.md) — cifrado de disco, Secure
  Boot, firewall, firma de releases y límites de confianza.
- [Solución de problemas](troubleshooting/README.md) — recuperate de los
  fallos comunes.
- [Arquitectura](architecture/README.md) — ediciones, propiedad y flujo de
  datos.
- [Desarrollo](development/README.md) — código, QA y caminos de
  contribución.
- [Lenguaje de diseño](development/design-language.md) — identidad del
  producto, principios de UI, mapa de fuentes de verdad y guía para quien
  contribuye al instalador. La autoridad de diseño es la
  [RFC 0001 — Hornero Signal](development/rfc-0001-hornero-signal.md).

## Licencia

[MIT](../LICENSE).

---

[Sitio web](https://www.horneroos.com) ·
[Docs](https://www.horneroos.com/docs) ·
[`HorneroOS/shell`](https://github.com/HorneroOS/shell) ·
[`HorneroOS/hornero`](https://github.com/HorneroOS/hornero) ·
[`HorneroOS/config`](https://github.com/HorneroOS/config) ·
[Issues](https://github.com/HorneroOS/docs/issues) ·
[Licencia](../LICENSE)
