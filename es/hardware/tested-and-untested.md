# Hardware y funciones: probado y no probado

HorneroOS se usa a diario en producción en múltiples estaciones de trabajo
físicas y está validado en KVM con UEFI y Legacy BIOS. Esa afirmación cubre
el sistema en conjunto; cada función de abajo conserva su estado honesto, y
un sistema de uso diario igual tiene limitaciones concretas y declaradas.
Usá esta página antes de asumir que un dispositivo puntual anda en tu máquina.

## Madurez por función

| Área | Estado hoy | Qué significa |
| --- | --- | --- |
| Escritorio Hyprland | Soportado (por defecto) | Sesión Wayland por defecto |
| Sesión Niri | Soportado | Opción de compositor desplazable |
| Rollback de sistema | Planificado | Backend `none`; sin restore |
| Launchers extra | Planificado o referencia | No es soporte instalado |
| Handheld y VR | Planificado o experimental | Ningún dispositivo cualificado |
| Ediciones Server y Agents | Planificado | Sin imagen instalable |

El detalle de ediciones está en [Ediciones](../editions/README.md);
el contrato de rollback, en
[Actualizaciones y recuperación](../desktop/updates-and-rollback.md).

## Probado

- HorneroOS corre a diario en producción en al menos tres estaciones de
  trabajo físicas (incluida una ASUS ROG Strix G16 registrada
  `USER-VERIFIED`).
- `v0.2.0-preview42` aprobó validación de arranque e instalación en KVM
  tanto con UEFI como con Legacy BIOS (Desktop, Studio y Gaming), más
  validación E2E en KVM UEFI de la QCOW2 preinstalada de Desktop.

## No corrido o sin certificar por dispositivo

- Chequeos especializados por dispositivo: NVENC, corrección Vulkan y
  captura HDMI en combinaciones arbitrarias de hardware.
- Cualquier generación NVIDIA puntual de terceros, cableado híbrido,
  handheld, casco VR, interfaz de audio o pantalla fuera de los equipos
  probados. Tu propio chequeo, reportado con versiones y logs, es la
  evidencia que vale.

## Reportar tu hardware

Corré `horneroctl doctor`, guardá `lspci -nnk` y las líneas de
kernel relevantes, y contá la ruta exacta de instalación que
usaste (firmware, cifrado, edición, compositor). Quitá datos
personales antes de compartir. Mirá
[Solución de problemas por síntoma](../troubleshooting/by-symptom.md).
