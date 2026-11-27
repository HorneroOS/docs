# Studio: audio de baja latencia sin humo

Un camino que funciona por el audio Studio de HorneroOS: empezá
confiable, medí tu propia interfaz y recién ahí bajá el quantum.
Esta guía extiende [Audio Studio](studio-audio.md);
esa página es dueña del contrato de modos y de la recuperación.

## Empezá en Balanced, siempre

```sh
horneroctl studio doctor
horneroctl studio selection show
horneroctl mode set studio
```

Balanced sigue rate y quantum de tu dispositivo y no necesita
ajuste. Grabá o reproducí una pasada limpia en Balanced primero:
esa es la base contra la que se compara todo experimento.

![Página Studio de Settings con resultados del doctor. Nueve de
diez chequeos pasan; el de xruns de PipeWire está en FAIL y
reporta xruns desde que arrancaron los nodos, sugiriendo quantum
mayor o modo Balanced.](https://www.horneroos.com/captures/cap-cc-13.png)

*Settings → Studio corre el mismo doctor: resultados honestos,
incluido un fail. Captura del 19 de noviembre de 2026.*

## Qué cambia realmente cada modo

| Modo | Cuándo usarlo | Qué cambia |
| --- | --- | --- |
| Balanced | Por defecto, siempre seguro | Nada; sigue al dispositivo |
| Low Latency | Monitoreo corto | Propuesta de quantum de 128 frames |
| Advanced | Calibración por interfaz | Tus valores medidos |
| Temporary Performance | Renders largos | Perfil de energía temporal |

PipeWire y WirePlumber corren la sesión en todos los modos;
cambiar de modo nunca reprioriza Bluetooth ni dispositivos de
consumo, y HorneroOS nunca instala un kernel RT ni retoca
governors por Studio.

## Quantum no es latencia

Un quantum es un período de scheduling. La propuesta Low Latency
es 128 frames a 48 kHz; no es latencia round-trip medida, y
ninguna superficie HorneroOS la presenta como tal. Solo una
medición física en loopback sobre tu interfaz reporta latencia
real. Medí la tuya si ese número importa para tu trabajo.

![Una terminal con la salida de studio doctor con Low Latency
registrado. Dos chequeos en WARN: xruns desde que arrancaron los
nodos y el perfil de baja latencia activo, con el comando que lo
revierte.](https://www.horneroos.com/captures/cap-studio-04.png)

*`horneroctl studio doctor` con Low Latency: los avisos quedan
visibles, incluido el conteo de xruns. El quantum es período de
scheduling, no latencia medida. Captura del 19 de noviembre de
2026.*

## Prueba segura de Low Latency

1. Seguí los pasos de copia y reinicio en
   [Audio Studio](studio-audio.md#configuración) para activar Low Latency.
2. Reproducí o grabá el mismo material que tu base Balanced.
3. Clicks, cortes o xruns significan que tu interfaz no sostiene
   ese quantum: volvé a Balanced. Es el comportamiento esperado,
   no un fallo para tunear alrededor.
4. `rtkit` es parte de la sesión PipeWire normal; HorneroOS no
   te pide reemplazarlo ni subir límites a mano.

## Ruteo

Ruteá con herramientas WirePlumber (`wpctl`, `qpwgraph`, o los
puertos PipeWire/JACK de tu DAW). HorneroOS no fija reglas por
dispositivo, así tu ruteo sobrevive a cambios de equipo. Los
programas pro se conectan vía `pipewire-jack`. Para un paso a paso
completo con Discord, OBS y pista del navegador, mirá
[Studio: ruteo en vivo](studio-live-routing.md).

## Cuando el audio se rompe

Quitá el drop-in copiado y reiniciá los servicios de usuario,
exactamente como en
[recuperación de Audio Studio](studio-audio.md#recuperación), y volvé
a correr `horneroctl studio doctor` antes de cambiar otra cosa.
