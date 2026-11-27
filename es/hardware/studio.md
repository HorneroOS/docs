# Hardware y límites de rendimiento de Studio

Qué afirma y qué no afirma hoy HorneroOS Studio sobre hardware creativo, y los
límites que respeta cada flujo de Studio. Studio es una edición **Soportada**:
todavía no existe una lista de hardware probado por Hornero ni ninguna
interfaz, GPU, tableta o superficie de control certificada. Las afirmaciones de
soporte llegan recién con evidencia de aceptación de HorneroOS/qa.

## El panorama honesto de soporte

| Área | Hoy | Evidencia necesaria |
| --- | --- | --- |
| Interfaces de audio | Valores por defecto de PipeWire | Fixtures de loopback de QA |
| GPUs | Drivers upstream de Arch | Matriz de capacidades de QA |
| Pantallas | Shell por salida | Fixtures de pantallas de QA |
| Tabletas/MIDI/superficies | Stack upstream | Escenarios de dispositivos de QA |
| Almacenamiento | Umbrales de política | Validación de rutas en la CLI |

Notas por área:

- **Audio:** todavía sin afirmaciones medidas por Hornero sobre latencia ni
  XRUNs.
- **GPUs:** todavía sin certificación de render ni codificación.
- **Pantallas:** el preset Studio no trae geometría fija.
- **Tabletas/MIDI/superficies:** comportamiento de kernel, libinput y PipeWire
  tal como llega de upstream.

Si un dispositivo funciona, funciona gracias al stack upstream. Vale la pena
usarlo — simplemente no es una promesa de soporte de Hornero.

## Límites de rendimiento que Studio nunca cruza

- No se instala ni se requiere ningún kernel RT.
- No se hace ajuste de hilos IRQ, gobernador de CPU, reloj de GPU ni
  planificador de E/S.
- El modo Rendimiento Temporal solo reutiliza `power-profiles-daemon` y
  restaura el perfil anterior; no escribe valores de gobernador.
- Los valores de quantum de Baja Latencia son propuestas para probar por
  interfaz, nunca una garantía de latencia (quantum es un período de
  planificación, no latencia de ida y vuelta).
- Benchmarks, afirmaciones térmicas y comparaciones de tiempos de render son
  evidencia de QA o no son afirmaciones.

## Flujos creativos, tal como están hoy

- **Audio/música:** PipeWire Balanced con ruteo WirePlumber;
  Ardour/Guitarix/Carla/Audacity desde el catálogo, REAPER solo por opt-in
  propietario explícito y yabridge para tus propios VST de Windows.
- **Video/streaming:** OBS Studio y Kdenlive mediante captura PipeWire en el
  compositor que ya corrés; la codificación por GPU depende por completo de tu
  stack de drivers upstream.
- **Diseño/foto/3D:** Krita, GIMP, Inkscape, darktable, RawTherapee, Blender,
  FreeCAD y Godot como aplicaciones comunes de Arch con valores por defecto de
  Hornero alrededor — sin builds forkeadas.
- **Selección y estado:** Ajustes → Studio o `horneroctl studio selection`
  registra intención; `horneroctl studio doctor` informa salud de la selección
  y del stack de audio en solo lectura.

## Antes de comprar o culpar al hardware

1. Corré `horneroctl doctor` y `horneroctl studio doctor`.
2. Revisá la vista upstream (`lspci -nnk`, `wpctl status`, `pw-top` mientras
   corre audio) antes de cambiar cualquier ajuste.
3. Quedate en audio Balanced salvo que hayas medido una razón para no hacerlo;
   cambiá una variable por vez y mantené el camino de borrar-para-restaurar de
   la [guía de audio en Studio](../applications/studio-audio.md).

Mirá también la [matriz de aplicaciones de Studio](../applications/studio.md) y
[primeros pasos en Studio](../applications/studio-getting-started.md).
