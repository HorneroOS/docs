# Audio en Studio: configuración, ruteo y recuperación

> [!NOTE]
> Podés capturar tu configuración completa de audio de Studio junto con la
> experiencia y el ruteo en un perfil de instantánea conmutable usando
> `horneroctl profile capture` o desde el `Centro de control → Perfiles`. Mirá
> [Perfiles e instantáneas](../desktop/profiles-snapshots.md).

Cómo funciona el audio de Studio en HorneroOS: el contrato de modos, los
perfiles portables de política, el ruteo diario y cómo recuperarte cuando algo
suena mal. Studio es una edición **Soportada** — esta guía describe los
contratos revisados y la configuración que existen hoy, no soporte validado en
QA para ninguna interfaz específica.

Contratos fuente, en orden de propiedad:

- Semántica de modos: HorneroOS/hornero
[`editions/catalogue.yaml`](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml)
  (`studioAudioModes`), resuelto por `scripts/resolve-edition.py`.
- Valores portables de política: `docs/STUDIO-AUDIO.md` en HorneroOS/config y
  los perfiles `desktop/pipewire` + `desktop/studio-audio`.
- Afirmaciones de soporte medido: solo HorneroOS/qa.

## Modos

| Modo | Cuándo | Qué cambia |
| --- | --- | --- |
| Balanced (por defecto) | Siempre seguro | Nada; sigue al dispositivo |
| Baja Latencia (opt-in) | Rutas cortas de monitoreo | Quantum de 128 cuadros |
| Avanzado (opt-in) | Calibración por interfaz | Tus valores medidos |
| Rendimiento Temporal | Renders y exportaciones | Perfil de energía temporal |

Detalles de los modos:

- **Balanced** sigue la frecuencia y el quantum del dispositivo; WirePlumber
  gestiona las sesiones.
- **Baja Latencia** propone un quantum de 128 cuadros a 48 kHz (mínimo 64,
  máximo 256) para interfaces que puedan sostenerlo. Son valores propuestos,
  no soporte medido.
- **Avanzado** no trae números fijos a propósito.
- **Rendimiento Temporal** reutiliza `power-profiles-daemon` y restaura el
  perfil anterior por timeout, cancelación, error o reinicio.

El quantum es un período de planificación. **No** es latencia física de ida y
vuelta, y ninguna superficie de Hornero lo presenta así; solo una medición
física de loopback informa la latencia real. Si una interfaz tiene underruns
(clics, cortes) a 128 cuadros, volvé a Balanced — ese es el comportamiento
esperado, no una falla para parchar con trucos del sistema.

## Configuración

1. Balanced no necesita configuración: el perfil de config instala un drop-in
   explícito sin overrides en
   `~/.config/pipewire/pipewire.conf.d/10-hornero-studio-balanced.conf`.
2. Para probar Baja Latencia, copiá la plantilla y reiniciá los servicios de
   usuario:

   ```sh
   cp ~/.config/hornero/studio-audio/low-latency.conf \
     ~/.config/pipewire/pipewire.conf.d/50-hornero-studio-low-latency.conf
   systemctl --user restart pipewire wireplumber
   ```

3. Avanzado: escribí tu frecuencia y quantum medidos en una copia de
   `advanced.conf` de la misma manera. Mantené un archivo por interfaz si
   difieren; nunca copies nombres de dispositivos ni valores de otra máquina.

Chequeá la selección y salud actuales en cualquier momento con:

```sh
horneroctl studio doctor
horneroctl studio selection show --json
```

![Una terminal mostrando la salida de studio doctor con el modo Low Latency
registrado. Dos chequeos aparecen marcados como WARN: los xruns contados desde
que arrancaron los nodos de audio y el perfil de baja latencia activo, junto
con el comando que lo
revierte.](https://www.horneroos.com/captures/cap-studio-04.png)

*`horneroctl studio doctor` con Baja Latencia registrado: las advertencias
quedan visibles, incluyendo el conteo de xruns. Los valores de quantum son un
período de planificación, no latencia medida. Captura en el equipo del
maintainer, 19 de noviembre de 2026.*

## Ruteo

- Usá herramientas compatibles con WirePlumber (`wpctl`, `qpwgraph` o los
  puertos PipeWire/JACK de tu DAW) para rutear flujos de aplicaciones.
  Hornero no define reglas específicas de dispositivo, así que tu ruteo
  sobrevive cambios de hardware.
- Las aplicaciones de audio profesional conectan mediante `pipewire-jack`; el
  legado `pipewire-media-session` no forma parte de Studio.
- Los dispositivos Bluetooth y de consumo siguen la política de sesión por
  defecto; cambiar a un modo de Studio nunca los reprioriza.
- Para un ruteo reversible de micrófono, guitarra, DAW, Discord, OBS y
  pista del navegador, mirá [Studio: ruteo en vivo](studio-live-routing.md).

## Recuperación

Todos los modos son reversibles por construcción:

- Borrá el drop-in copiado y reiniciá los servicios de usuario para restaurar
  el estado anterior de forma exacta:

  ```sh
  rm ~/.config/pipewire/pipewire.conf.d/50-hornero-studio-low-latency.conf
  systemctl --user restart pipewire wireplumber
  ```

- Un cambio de modo nunca requiere reinicio, cambio de kernel ni cambio de
  privilegios. Hornero nunca instala un kernel RT, no toca IRQ ni gobernadores
  de CPU ni edita planificadores de E/S — si una guía externa te dice que lo
  hagas, no forma parte de HorneroOS Studio.
- ¿Sigue andando mal después de restaurar? Revisá `horneroctl studio doctor`,
  luego `systemctl --user status pipewire wireplumber`, y quitá cualquier otro
  archivo que hayas agregado bajo `~/.config/pipewire/pipewire.conf.d/`.

## Límites

- No se incluyen ni requieren plantillas personales de proyectos, cachés de
  plugins, licencias ni nombres de dispositivos.
- REAPER y las herramientas VST de Windows siguen los términos de sus
  fabricantes (mirá la [matriz de aplicaciones de Studio](studio.md)).
- Las afirmaciones de soporte para interfaces, frecuencias de muestreo o
  cargas de trabajo específicas pertenecen a la evidencia de aceptación de
  HorneroOS/qa, no a esta guía.
