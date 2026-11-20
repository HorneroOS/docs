# Hardware y funciones: probado, solo VM y no probado

HorneroOS se usa y se mantiene todos los días. Esa afirmación
cubre el sistema en conjunto; cada función de abajo conserva su
estado honesto, y un sistema de uso diario igual tiene
limitaciones concretas y declaradas. Usá esta página antes de
asumir que un camino funciona en tu máquina.

## Madurez por función

| Área | Estado hoy | Qué significa |
| --- | --- | --- |
| Escritorio Hyprland | Validado por defecto | Sesión por defecto de la ISO |
| Sesión Niri | Experimental | VM de una salida, sin paridad |
| Rollback de sistema | Planificado | Backend `none`; sin restore |
| Launchers extra | Planificado o referencia | No es soporte instalado |
| Handheld y VR | Planificado o experimental | Ningún dispositivo cualificado |
| Ediciones Server y Agents | Planificado | Sin imagen instalable |

El detalle de ediciones está en [Ediciones](../editions/README.md);
el contrato de rollback, en
[Actualizaciones y recuperación](../desktop/updates-and-rollback.md).

## Probado

- Instalaciones Desktop, Studio y Gaming UEFI sin cifrar
  pasaron en la ISO v0.2.0-preview32 en máquinas virtuales
  descartables.
- Una ASUS ROG Strix G16 está registrada USER-VERIFIED en
  preview24 más fixes post-instalación en HorneroOS/qa. Es una
  sola máquina, en un artefacto más viejo.

## Solo VM o no corrido en la ISO publicada

- El artefacto preview32 no tiene validación en hardware físico.
- Instalaciones cifradas LUKS, legacy BIOS, sesiones Niri en la
  ISO y copy-to-RAM no se corrieron en preview32 y no deben
  darse por pasados.

## No testeado específicamente

- NVENC, corrección Vulkan y captura HDMI en la aceptación en
  hardware registrada.
- Cualquier generación NVIDIA puntual, cableado híbrido,
  handheld, casco VR, interfaz de audio o pantalla. Tu propio
  chequeo, reportado con versiones y logs, es la evidencia que
  vale.

## Reportar tu hardware

Corré `horneroctl doctor`, guardá `lspci -nnk` y las líneas de
kernel relevantes, y contá la ruta exacta de instalación que
usaste (firmware, cifrado, edición, compositor). Quitá datos
personales antes de compartir. Mirá
[Solución de problemas por síntoma](../troubleshooting/by-symptom.md).
