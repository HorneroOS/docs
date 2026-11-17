# Desktop: construí tu mundo

La edición base: Hornero Shell sobre Wayland, Hyprland como backend validado
(Niri experimental), visuales Hornero Signal, 16 layouts, temas, modos de
experiencia y un sistema de plugins. Studio y Gaming la extienden; no la
reemplazan.

**Madurez: Preview.** Se instala desde la ISO preview firmada (ver la
[página de releases](https://horneroos.com/releases)); no es una release
estable.

## Qué podés construir

- Elegí un layout (Cockpit es el predeterminado), un tema y un modo de
  experiencia (Focus, Everyday, Signal, Gaming, Studio) por separado. Cambiar
  de modo nunca cambia tu layout ni tu tema.
- Agregá widgets de escritorio y extensiones de barra desde el panel
  Extensiones.

## Verificado

| Qué | Dónde |
| --- | --- |
| Pruebas unitarias y de contrato de la Shell, lint QML, política de modos bajo pantalla completa | CI + offscreen |
| El escritorio arranca a una sesión lista, cambio de modos, capturas | VM de QA (Hyprland) |
| Composición de paquetes de la edición | `scripts/resolve-edition.py` en CI |

## No validado

- Hardware físico de cualquier tipo.
- Niri más allá de un recorrido en VM con una sola salida.
- Multi-monitor con escalas mixtas y ultrawide (solo capturas parciales).
- Presupuestos de rendimiento (tiempo de frame, latencia de entrada, CPU en
  reposo) no medidos para todos los layouts.
