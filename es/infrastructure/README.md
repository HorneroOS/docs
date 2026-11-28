# Infraestructura

Guías para evaluar proveedores de alojamiento y desplegar **HorneroOS Browser
Playground** (`HorneroOS/playground`) en forma autoalojada o en la nube.

> **Nota de alcance:** Si querés probar HorneroOS sin administrar servidores,
> empezá por [Probá HorneroOS sin instalar](../getting-started/try-horneroos.md).
> Los documentos de infraestructura están orientados a operadores que despliegan
> el stack efímero de KVM y WebRTC seguido en `HorneroOS/playground#1`.

## Guías

- [Kit de decisión de proveedores cloud](cloud-provider-decision-kit.md) —
  matriz verificada de proveedores (DistroSea, AWS Open Source Credits,
  OSUOSL, Google Cloud, AWS EC2, OVHcloud/Kimsufi Eco y Hetzner Dedicated),
  latencia RTT desde Buenos Aires, escenarios de presupuesto, compromiso de
  gasto cero y resumen listo para DistroSea.
- [Runbook de despliegue de Playground](playground-deployment-runbook.md) —
  checklist corto posterior a elegir proveedor y el procedimiento final de 19
  pasos con validación de hardware y kill-switch de emergencia.

## Arquitectura relacionada

- [ADR: arquitectura de Hornero Playground (en inglés)](../../architecture/adr-hornero-playground.md)
- [Modelo de amenazas de Hornero Playground (en inglés)](../../architecture/hornero-playground-threat-model.md)
