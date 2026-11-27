# Primeros pasos en Studio: tu primer proyecto

¿Sos nuevo en HorneroOS? Empezá por [Primeros pasos](../getting-started/README.md)
para descargar, verificar e instalar la ISO actual y después volvé acá.

Desde un escritorio HorneroOS recién instalado hasta tu primer proyecto
creativo con la selección de Studio que realmente querés — sin instalar nada
más que lo que elegiste. Studio es una edición **Soportada**: el instalador de
la ISO actual instala las aplicaciones de las especializaciones que elegís, y
`horneroctl studio` registra y aplica bloques de configuración revisados. Los
cambios de paquetes post-instalación mediante `horneroctl` siguen siendo
intención registrada en esta preview, y ningún paso acá afirma lo contrario.

## 1. Elegí tus cargas de trabajo

Abrí **Ajustes → Studio** y activá las especializaciones que coincidan con tu
trabajo (por ejemplo Audio & Music Production o Streaming & Content Creation),
o elegí aplicaciones individuales bajo Custom Selection. ¿Preferís la
terminal? El mismo estado vive en un solo archivo y una sola CLI:

```sh
horneroctl studio selection set \
  --specialization audio-music-production --application krita
horneroctl studio selection show --json
horneroctl studio doctor
```

Registrar una selección no instala nada. Es la intención revisada que consumen
el instalador y los pasos posteriores del ciclo de vida de `horneroctl`, y
podés cambiarla cuando quieras — quitar una carga de trabajo nunca borra tus
archivos, ajustes ni proyectos.

![Ajustes, página Studio con los resultados de Studio doctor. Nueve de diez
chequeos pasan; el chequeo de xrun de PipeWire figura como FAIL e informa los
xruns contados desde que arrancaron los nodos de audio, sugiriendo un quantum
mayor o el modo Balanced.](https://www.horneroos.com/captures/cap-cc-13.png)

*Ajustes → Studio corre el mismo doctor: resultados honestos, incluyendo una
falla. Acá el chequeo de xrun falla en el equipo del maintainer y lo dice tal
cual. Studio es una edición Soportada. Captura de escritorio en vivo,
19 de noviembre de 2026.*

## 2. Adaptá el escritorio a tu flujo

Aplicá el preset de layout **Studio** desde el selector de layouts si querés
la barra de creación (medios, deslizador de audio, recursos) con un lienzo
reservado y estable. Es opt-in y reversible desde el mismo selector, y no
contiene estado de monitores ni de proyectos.

## 3. Configurá el audio (Balanced primero)

Empezá en **Balanced**: sigue exactamente a tu interfaz y es el valor por
defecto adecuado hasta que sepas que necesitás menos latencia. El recorrido
completo de modos, ruteo y recuperación está en
[Audio en Studio](studio-audio.md). Probá Baja Latencia solo como la plantilla
opt-in descripta ahí, y volvé atrás borrando un solo archivo.

## 4. Creá el proyecto

Usá la estructura de almacenamiento de la política de almacenamiento de Studio
salvo que la hayas cambiado:

- `~/Studio/Projects` — el proyecto en sí (con backup, nunca se borra
  automáticamente).
- `~/Studio/Assets` — medios fuente (también con backup).
- `~/Studio/Scratch` — renders e intermedios (seguro para limpiar con vista
  previa).

Creá tu primer proyecto en la aplicación que elijas dentro de
`~/Studio/Projects`, guardá los medios fuente en `Assets` y apuntá la salida
de render a `Scratch`. Esa separación es lo que permite limpiar cachés y
respaldar proyectos sin dudar.

![REAPER abierto con una plantilla de grabación vocal: pistas nombradas para
acompañamiento, bus vocal y voz principal, mezclador abajo, línea de tiempo
vacía y transporte detenido. La barra de título muestra una licencia de
evaluación.](https://www.horneroos.com/captures/cap-mode-05.png)

*Una plantilla vocal de REAPER lista para grabar — una plantilla, no una
sesión grabada, corriendo bajo su licencia de evaluación en el equipo del
maintainer. Captura, 19 de noviembre de 2026.*

## 5. Conocé los límites antes de necesitarlos

- REAPER es propietario y siempre es una elección extra explícita; yabridge
  necesita Wine y tus propios plugins de Windows obtenidos legalmente. Mirá la
  [matriz de aplicaciones de Studio](studio.md).
- El aviso de poco espacio en disco salta al 10% libre y un render debería
  detenerse de forma segura al 3%: limpiá primero las vistas previas en
  Scratch, nunca los medios del proyecto.
- Todo lo etiquetado como Planificado o "sin validar en QA" significa
  exactamente eso. Las afirmaciones de soporte de hardware y flujos llegan con
  evidencia de aceptación de HorneroOS/qa, no con esta guía.
