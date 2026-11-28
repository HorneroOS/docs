# Ediciones y composición de paquetes

HorneroOS se organiza como una única familia de sistema operativo. Sus
ediciones comparten una base y componen roles y capacidades; no son
distribuciones separadas con scripts de paquetes copiados.

El modelo canónico de producto vive en el
[catálogo de ediciones de `HorneroOS/hornero`](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml).
El resolvedor en
[`scripts/resolve-edition.py`](https://github.com/HorneroOS/hornero/blob/main/scripts/resolve-edition.py)
transforma una edición y un compositor opcional en una lista determinística de
paquetes Arch. No construye una imagen ni certifica el sistema resultante.

## Modelo de composición

```text
Base + desktop + compositor:hyprland  → Desktop / Hyprland
Base + desktop + compositor:niri      → Desktop / Niri
Base + server                          → Server
Base + server + agent-host             → Agents
Base + desktop + studio                → Studio
```

El mismo modelo alimenta al instalador gráfico. El instalador Calamares
(`3.4.3`) en `HorneroOS/installer` lo consume para construir la ISO
publicada y firmada `v0.2.0-preview42` y la QCOW2 preinstalada de Desktop.

## Madurez actual

- **Desktop — Soportado.** Producto de escritorio y composición de paquetes
  de uso diario; se instala desde la ISO firmada `v0.2.0-preview42` o corre
  desde la QCOW2 de Desktop.
- **Gaming — Soportado.** Se instala desde la misma ISO firmada
  `v0.2.0-preview42` con herramientas de gaming; de uso diario y validado en
  KVM y en estaciones físicas (juegos puntuales y handhelds quedan sin
  certificar).
- **Hyprland — Soportado.** Sesión de escritorio por defecto.
- **Niri — Soportado.** Opción de compositor Wayland con columnas desplazables
  y backend real de Shell. Mirá [Compositores Wayland](../desktop/compositors.md)
  para los límites puntuales de capacidades.
- **Server — Planificado.** Se describe un conjunto de paquetes headless; no
  hay imagen booteable ni aceptación completa de administración remota.
- **Agents — Planificado.** Podman rootless y systemd Quadlet son la dirección;
  el aprovisionamiento de Hermes, el aislamiento, los secretos, el ciclo de
  vida y la recuperación no están certificados.
- **Studio — Soportado.** Se instala desde la misma ISO firmada
  `v0.2.0-preview42` con especializaciones creativas seleccionables; incluye
  perfiles de audio y diagnósticos, mientras que las apps creativas de
  terceros y las interfaces de audio puntuales siguen sin certificación por
  dispositivo.
- **Labwc — Planificado.** No se ofrece backend ni conjunto de paquetes de
  Hornero.

Estas etiquetas describen evidencia de producto, no si existe un paquete
upstream ni si un componente individual anda por separado.

## Intención de cada edición

- **Desktop** es un escritorio Wayland-first impulsado por Hornero Shell.
  Hyprland es el backend por defecto; Niri también está soportado.
- **Server** apunta a ser un sistema headless chico y operable en forma remota.
  Su propuesta actual de paquetes excluye la Shell gráfica y los paquetes de
  compositor.
- **Agents** apunta a extender Server con cargas de trabajo aisladas para
  agentes. El modelo prohíbe exponer un socket Docker privilegiado del host o
  incrustar credenciales en imágenes. Son restricciones de diseño, no una
  afirmación de que el runtime de cargas de trabajo esté listo.
- **Studio** apunta a extender Desktop con herramientas de producción creativa.
  REAPER y las integraciones de VST de Windows siguen siendo opcionales, con
  licencia propia y provistas por el usuario; ninguna licencia personal ni
  plugin forma parte de HorneroOS.

## Revisar la composición de paquetes

Desde un checkout de HorneroOS/hornero, inspeccioná el resultado exacto de
paquetes sin instalar nada:

```sh
python3 scripts/resolve-edition.py desktop --json
python3 scripts/resolve-edition.py desktop --compositor niri --json
python3 scripts/resolve-edition.py server --json
python3 scripts/resolve-edition.py agents --json
python3 scripts/resolve-edition.py studio --compositor hyprland --json
python3 scripts/resolve-edition.py studio \
  --specialization audio-music-production --application reaper
```

Las selecciones de Studio son componibles: las especializaciones y las
aplicaciones individuales se resuelven a un plan determinístico con
trazabilidad de origen (mirá [Aplicaciones de Studio](../applications/studio.md)).

La resolución de paquetes es un chequeo de arquitectura. Un producto pasa a ser
instalable recién cuando sus servicios, el comportamiento en ejecución, la
recuperación, la imagen o el camino de instalación y la evidencia de aceptación
están implementados y probados.
