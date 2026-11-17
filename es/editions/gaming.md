# Gaming: jugá a tu manera

Gaming es Desktop más un modo de experiencia Gaming, diagnósticos y ayudas
para Steam, Proton, Feral GameMode, Gamescope y MangoHud. El objetivo es no
estorbar a tu juego.

**Madurez: Preview.** La sesión Gamescope para handhelds está rotulada como
Experimental y sin calificar en ningún dispositivo. Ningún juego está
certificado.

## Qué pasa en modo Gaming

Cambiá con `horneroctl mode set gaming` (o el launcher). Bajo una ventana en
pantalla completa en Hyprland:

| Comportamiento | Garantía |
| --- | --- |
| Barras y drawers | Los drawers se cierran, se quitan las regiones de entrada, la barra se deshabilita; solo el selector de área usa la capa Overlay |
| Foco de teclado | La shell no pide foco exclusivo (salvo superficies que abrís vos: selector de área, chat del companion) |
| Notificaciones | Los avisos no críticos se archivan sin popup y se cuentan; los críticos se muestran |
| Sondeo | Telemetría de sistema y red en pausa |
| Widgets y reloj de escritorio | Ocultos |
| Reposo | Inhibido en pantalla completa |
| Movimiento, brillo, scanlines | Apagados, no se pueden sobrescribir |
| Ajuste de Hyprland | Gaps, redondeo, sombra y blur desactivados; tearing permitido; se restaura recargando tu configuración al salir |

Límites: la detección es solo de Hyprland; una ventana sin bordes que solo
llena la pantalla es una ventana normal para el compositor y no cuenta como
pantalla completa; el manejo de mandos es del compositor y de Steam, la
shell no agrega reglas.

## Diagnósticos y ayudas

- `horneroctl gaming doctor`: loader/ICD Vulkan (64 y 32 bits), coherencia
  del driver de GPU, Steam, builds de Proton, GameMode y sus librerías
  cliente, `vm.max_map_count`, modeset DRM de NVIDIA y userspace de 32 bits,
  PipeWire, portal, mandos. Gamescope y MangoHud son **opcionales**: si
  faltan es `WARN`, no un fallo (Gamescope falla solo si elegiste el perfil
  Handheld).
- `horneroctl gaming launch-options --gamemode --mangohud`: imprime una
  cadena de opciones de lanzamiento de Steam con las herramientas
  instaladas. Nunca edita Steam. La composición con Gamescope
  (`--gamescope --width --height --refresh --fullscreen`) es una plantilla,
  no una recomendación.

### Flujo: un juego con Proton (por ejemplo Cyberpunk 2077)

1. `horneroctl gaming doctor` y corregí cualquier `FAIL` (típicos:
   userspace de 32 bits del driver, `vm.max_map_count`, modeset de NVIDIA).
2. En Steam, activá una build de Proton para el juego.
3. `horneroctl gaming launch-options` y pegá el resultado en las opciones de
   lanzamiento del juego (`gamemoderun %command%` por defecto).
4. `horneroctl mode set gaming` e iniciá el juego en pantalla completa.
5. Salí con `horneroctl mode set everyday`.

Ningún ajuste por defecto toca el kernel, el planificador, el governor ni la
memoria.

## Verificado

| Qué | Dónde |
| --- | --- |
| Política bajo pantalla completa (avisos retenidos, sondeo en pausa, capa de escritorio oculta, inhibición de reposo, guardas) y test de bits de pantalla completa | pruebas unitarias offscreen (node), CI |
| Solo las superficies intencionales toman foco de teclado; Overlay solo para el selector de área; los drawers se retiran | pruebas de contrato estáticas, CI |
| Sondas del doctor, WARN de herramientas opcionales, composición de launch-options | pruebas unitarias de V, CI |
| `gaming doctor` en un Arch real con Steam, GameMode y GPU NVIDIA (solo lectura) | equipo real, solo lectura |
| Comportamiento en vivo en pantalla completa y ajuste de Hyprland con Hyprland solo-Lua | escenarios de VM `experience/gaming-fullscreen`, `gaming/hyprland-tuning-lua` (resultado indicado en el PR) |

## No validado

- Cualquier juego concreto, incluido Cyberpunk 2077; el comportamiento de
  Proton; anti-cheat (el anti-cheat a nivel kernel no está soportado).
- Rendimiento, frame pacing, latencia, VRR, HDR, tearing.
- Gamescope en NVIDIA, la sesión Gamescope para handhelds, navegación solo
  con mando, suspensión/reanudación, batería/TDP en handhelds.
- MangoHud y Gamescope **no estaban instalados** en el equipo inspeccionado,
  así que esas composiciones nunca se ejecutaron.
- Perfiles Wine/Lutris/Bottles/VR (planeados o solo de referencia).
