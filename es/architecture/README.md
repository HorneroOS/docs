# Arquitectura

Hornero es un conjunto de repositorios que colaboran con propiedad
explícita. Los repositorios se componen en la ISO Preview firmada
publicada v0.2.0-preview32 (Desktop, Studio y Gaming Preview); ningún
repositorio por sí solo es el sistema operativo instalable. El
[ledger de releases](https://github.com/HorneroOS/hornero/releases)
registra qué revisiones de componentes se compusieron juntas.

## Dónde pertenece un cambio

| Repositorio | De qué es dueño |
| --- | --- |
| [hornero](https://github.com/HorneroOS/hornero) | CLI del sistema basada en V, puntos de entrada de capacidades y composición de releases |
| [config](https://github.com/HorneroOS/config) | Valores de fábrica, metadatos de paquetes, packs de temas y catálogos generados |
| [shell](https://github.com/HorneroOS/shell) | UI Quickshell y servicios de sesión en vivo: barras, lanzador, Dashboard, Ajustes, notificaciones, bloqueo y apariencia |
| [greeter](https://github.com/HorneroOS/greeter) | Tema de SDDM, assets Qt/QML y validación de paquetes |
| [qa](https://github.com/HorneroOS/qa) | Corridas de aceptación gráfica aisladas y evidencia |
| [docs](https://github.com/HorneroOS/docs) | Este manual de usuarias, usuarios y colaboradores |
| [website](https://github.com/HorneroOS/website) | Presentación pública del producto y la vista renderizada de este manual |

## Guías

- [Design language](../../development/design-language.md) — identidad de
  producto compartida, principios de interfaz y el mapa de repositorios
  para las decisiones de diseño.
- [Ediciones y composición de paquetes](../../architecture/editions.md) —
  el catálogo compartido, el modelo de composición y el límite honesto
  de madurez.
- [Sistema de apariencia](../../architecture/appearance-system.md) —
  responsabilidades de temas, fondos, paleta y toolkits.
- [Actualizaciones y entrega](../../architecture/updates-delivery.md) —
  cómo se relacionan el código fuente, los paquetes y las composiciones
  probadas.
- [Energía y rendimiento](../../architecture/power-performance.md) —
  medición y datos de referencia actuales.

Los contratos detallados quedan cerca de su implementación: ver los
documentos de
[arquitectura](https://github.com/HorneroOS/shell/blob/main/docs/ARCHITECTURE.md),
[layout](https://github.com/HorneroOS/shell/blob/main/docs/LAYOUTS.md) y
[foco](https://github.com/HorneroOS/shell/blob/main/docs/FOCUS.md) de la
Shell.
