# Desktop: construí tu mundo

La edición base: Hornero Shell sobre Wayland, con Hyprland (por defecto) y
Niri como backends de compositor soportados, visuales Hornero Signal, 14
layouts, temas, modos de experiencia y un sistema de plugins. Studio y
Gaming la extienden; no la reemplazan.

**Madurez: Supported.** Usada a diario en producción en múltiples estaciones
físicas y validada en KVM con UEFI y Legacy BIOS. Se instala desde la ISO o
QCOW2 firmada `v0.2.0-preview42` (ver la
[página de releases](https://horneroos.com/releases)).

## Qué podés construir

- Elegí un layout (Cockpit es el predeterminado), un tema y un modo de
  experiencia (Focus, Everyday, Signal, Gaming, Studio) por separado. Cambiar
  de modo nunca cambia tu layout ni tu tema.
- Agregá widgets de escritorio y extensiones de barra desde el panel
  Extensiones.

## Verificado

- **Pruebas unitarias y de contrato de la Shell, lint QML, política de modos
  bajo pantalla completa**: Dónde: CI + offscreen
- **El escritorio arranca a una sesión lista, cambio de modos, capturas**:
  Dónde: VM de QA (Hyprland)
- **Composición de paquetes de la edición**: Dónde:
  `scripts/resolve-edition.py` en CI

## No validado

- Cada laptop de terceros, cableado híbrido de GPU o dock externo fuera de
  las estaciones probadas.
- Paridad de Niri con funciones exclusivas de Hyprland (ver
  [Compositores Wayland](../desktop/compositors.md)).
- Multi-monitor con escalas mixtas y ultrawide (solo capturas parciales).
- Presupuestos de rendimiento (tiempo de frame, latencia de entrada, CPU en
  reposo) no medidos para todos los layouts.
