# Arquitectura

Hornero es un conjunto de repositorios que colaboran con propiedad
explícita. Los repositorios se componen en la release firmada publicada
`v0.2.0-preview42` (ISO de Desktop, Studio y Gaming más QCOW2 de Desktop);
ningún repositorio por sí solo es el sistema operativo instalable. El
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
| [playground](https://github.com/HorneroOS/playground) | Demos efímeras KVM en navegador, lanzadores locales de VM, IaC y modo presentador |
| [docs](https://github.com/HorneroOS/docs) | Este manual de usuarias, usuarios y colaboradores |
| [website](https://github.com/HorneroOS/website) | Presentación pública del producto y la vista renderizada de este manual |

## Guías

- [Lenguaje de diseño](../development/design-language.md) — identidad de
  producto compartida, principios de interfaz y el mapa de repositorios
  para las decisiones de diseño.
- [Ediciones y composición de paquetes](editions.md) —
  el catálogo compartido, el modelo de composición y el límite honesto
  de madurez.
- [ADR: arquitectura de Hornero Apps (en inglés)][adr-apps] —
  arquitectura de la tienda de software, opciones descartadas y taxonomía
  de procedencia.
- [ADR: arquitectura de Hornero Welcome (en inglés)][adr-welcome] —
  dirección creativa Signal Flight, tokens de movimiento, vistas previas
  transaccionales y esquema v2.
- [Modelo de amenazas de Hornero Apps (en inglés)][tm-apps] —
  análisis STRIDE y política de cadena de suministro para Hornero Apps.
- [ADR: arquitectura de Hornero Playground (en inglés)][adr-playground] —
  límites de `HorneroOS/playground`, matriz de virtualización y economía de
  streaming.
- [Modelo de amenazas de Hornero Playground (en inglés)][tm-playground] —
  análisis STRIDE multi-tenant de KVM efímero y runbook de incidentes.
- [Kit de decisión de proveedores cloud](../infrastructure/cloud-provider-decision-kit.md)
  — matriz verificada de proveedores, latencia desde Argentina y presupuestos.
- [Runbook de despliegue de Playground](../infrastructure/playground-deployment-runbook.md)
  — secuencia final de 19 pasos y kill-switch de emergencia.
- [Sistema de apariencia](appearance-system.md) —
  responsabilidades de temas, fondos, paleta y toolkits.
- [Modos de experiencia](experience-modes.md) — cómo se combinan los modos
  con la edición, el layout y el tema, y cómo se arma el deck Signal.
- [Actualizaciones y entrega](updates-delivery.md) —
  cómo se relacionan el código fuente, los paquetes y las composiciones
  probadas.
- [Energía y rendimiento](power-performance.md) —
  medición y datos de referencia actuales.

Los contratos detallados quedan cerca de su implementación: ver los
documentos de
[arquitectura](https://github.com/HorneroOS/shell/blob/main/docs/ARCHITECTURE.md),
[layout](https://github.com/HorneroOS/shell/blob/main/docs/LAYOUTS.md) y
[foco](https://github.com/HorneroOS/shell/blob/main/docs/FOCUS.md) de la
Shell.

[adr-apps]: ../../architecture/adr-hornero-apps.md
[adr-welcome]: ../../architecture/adr-hornero-welcome.md
[tm-apps]: ../../architecture/hornero-apps-threat-model.md
[adr-playground]: ../../architecture/adr-hornero-playground.md
[tm-playground]: ../../architecture/hornero-playground-threat-model.md
