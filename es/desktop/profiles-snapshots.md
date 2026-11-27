# Perfiles y Instantáneas

Los **Perfiles e Instantáneas** de HorneroOS (`horneroctl profile`) brindan
administración universal y 100% en espacio de usuario para la configuración de
tu espacio de trabajo. Están diseñados para ser totalmente reversibles por
construcción—sin requerir **privilegios de root**, **ningún kernel de tiempo
real personalizado**, y **sin tocar nunca bases de datos privadas de
aplicaciones**.

Ya sea que estés pasando de programación profunda a producción musical en
vivo, juegos o presentaciones, los Perfiles capturan y aplican tu entorno
exacto en segundos.

---

## Los 5 Dominios Composables

Cada perfil de HorneroOS encapsula exactamente 5 dominios composables,
permitiéndote agrupar o aplicar selectivamente aspectos de tu configuración:

1. **Experiencia (Experience)**: Modo visual, variantes de temas Signal y
   ajustes preestablecidos de diseño de ventanas (diseños `hypr`, perfiles de
   animación).
2. **Audio y Enrutamiento (Audio & Routing)**: Modo de audio de estudio,
   ajustes de reloj/quantum de PipeWire, selecciones de dispositivos
   predeterminados con advertencias inteligentes de hardware faltante, enlaces
   simbólicos a drop-ins de usuario para PipeWire/JACK, enlaces personalizados
   de PipeWire y reglas de enrutamiento por aplicación.
3. **Energía (Power)**: Perfil de energía activo (`balanced`, `performance`,
   `power-saver`) y reglas de inhibición de inactividad / mantenerse despierto
   (`caffeine` / redshift / apagado de pantalla).
4. **Extensiones (Extensions)**: Extensiones habilitadas de Hornero PluginKit
   y estados de plugins de Hyprland.
5. **Aplicaciones Compañeras (Companion Apps)**: Aplicaciones de usuario
   detectadas automáticamente durante la captura (los daemons del sistema se
   excluyen estrictamente). Las aplicaciones compañeras ofrecen una propuesta
   de lanzamiento opt-in al cambiar de perfil mediante la interfaz de
   Quickshell o `horneroctl profile launch-apps`, ¡nunca un inicio automático
   a ciegas!

---

## Red de Seguridad Automática

HorneroOS protege tu espacio de trabajo con una sólida arquitectura de
seguridad de múltiples niveles:

- **Baseline Inmutable**: La primera vez que capturás o aplicás un perfil,
  HorneroOS registra automáticamente una instantánea `baseline` inmutable de
  tu estado inicial del sistema.
- **Respaldo Automático Previo**: Cada vez que aplicás un perfil o revertís
  cambios, el sistema guarda automáticamente una instantánea `previous`
  previa.
- **Barra de Seguridad de 15 Segundos en Quickshell**: Al aplicar perfiles
  desde el centro de control de Quickshell o la línea de comandos, aparece una
  barra de confirmación de 15 segundos que te permite conservar o revertir
  instantáneamente los cambios si el hardware o el estado de las pantallas se
  comportan mal.

---

## Tutorial de la Interfaz Quickshell

El entorno de escritorio Quickshell integra los perfiles profundamente en tres
paneles principales:

### Centro de Control → Perfiles

- **Capturar Instantánea**: Tomá una instantánea de tu espacio de trabajo
  actual con un nombre y descripción personalizados.
- **Perfiles Guardados**: Visualizá todos los perfiles con insignias de estado
  que indican compatibilidad de hardware y disponibilidad de aplicaciones
  compañeras.
- **Vista Previa de Diff**: Inspeccioná las diferencias de configuración
  contra el estado actual del sistema antes de aplicar.
- **Banner de Seguridad de 15s**: Barra de confirmación con reversión
  automática por tiempo agotado si no se confirma.
- **Aviso de Aplicaciones Compañeras**: Diálogo opt-in que ofrece lanzar las
  aplicaciones compañeras faltantes.
- **Restaurar Baseline / Revertir**: Restauración instantánea en 1 clic a tu
  instantánea original `baseline` o `previous`.

### Centro de Control → Studio

- **Cambio Rápido de Perfil**: Alterná rápidamente entre modos de estudio y de
  escritorio.
- **Kits de Enrutamiento de Audio en 1 Clic**: Habilitá kits preconfigurados
  de enrutamiento virtual:
  - `live-call`: Enrutamiento sin eco para Discord/Zoom con retornos de
    hardware.
  - `browser-backing`: Enrutamiento de audio del navegador hacia entradas de
    tu DAW.
  - `reaper-low-latency`: Enrutamiento PipeWire de quantum ultrabajo para
    REAPER.
- **Abrir qpwgraph**: Iniciá el patchbay visual de gráficos PipeWire en 1 clic.

### Centro de Control → Audio

- **Selector de Salida por Aplicación**: Enrutá flujos de aplicaciones
  individuales a sinks de audio específicos sin necesidad de usar
  `pavucontrol`.
- **Alerta de Volumen Cero**: Detección automática de flujos silenciados o a
  `0%` con un botón de **Restaurar 100%** en 1 clic.

---

## Referencia Completa de CLI (`horneroctl profile`)

Administrá tus instantáneas de espacio de trabajo directamente desde la
terminal:

```bash
# Listar todos los perfiles y el estado de baseline/previous
horneroctl profile list --json

# Mostrar detalles completos del perfil + estado en vivo de hardware y apps
horneroctl profile show music-prod --json

# Capturar espacio de trabajo en vivo
horneroctl profile capture music-prod \
  --name "Producción musical" \
  --description "REAPER + ruteo PipeWire" --yes

# Comparar perfil contra el estado actual del sistema
horneroctl profile diff music-prod --json

# Aplicar dominios del perfil bajo el principio de mejor esfuerzo
horneroctl profile apply music-prod \
  --domains experience,audio --launch-apps --yes

# Revertir al estado anterior (predeterminado) o baseline
horneroctl profile revert --to previous --yes

# Lanzar aplicaciones compañeras faltantes instaladas de forma desacoplada
horneroctl profile launch-apps music-prod --yes

# Exportar paquete JSON portátil autónomo
horneroctl profile export music-prod ./music-prod.json --portable --yes

# Importar un paquete JSON
horneroctl profile import ./music-prod.json --id studio-rig --yes

# Eliminar un perfil de usuario (rechaza baseline)
horneroctl profile delete music-prod --yes
```

---

## Kits de Enrutamiento de Studio Reversibles (`horneroctl studio routing`)

Administrá los drop-ins de enrutamiento de audio virtual sin tocar tus
dotfiles personales:

```bash
# Mostrar estado del kit, sinks activos y flujos
horneroctl studio routing status --json

# Habilitar un kit de enrutamiento virtual
horneroctl studio routing enable live-call --yes

# Deshabilitar un kit
horneroctl studio routing disable live-call --yes

# Mover un flujo activo (ID) a un sink de destino
horneroctl studio routing move-stream 42 discord_call --yes

# Desmutear flujo y configurar volumen (0..150)
horneroctl studio routing fix-volume 42 100 --yes
```

---

## Portabilidad y Flujo de Dotfiles

Los perfiles se pueden exportar como paquetes JSON portátiles e independientes
usando `horneroctl profile export <id> <file> --portable`. Estos paquetes
eliminan rutas absolutas locales e identificadores específicos de la máquina,
haciéndolos ideales para guardar en tu repositorio de dotfiles o compartir
entre distintas máquinas con HorneroOS mediante `horneroctl profile import
<file>`.

---

## Reversión Completa (Rollback)

Si la configuración de tu espacio de trabajo llega a un estado no deseado,
podés restaurar instantáneamente tu entorno inicial pristino con:

```bash
horneroctl profile revert --to baseline --yes
```
