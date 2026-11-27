# Aplicaciones de Studio

Matriz verificada de aplicaciones, origen, licencia y soporte para HorneroOS
Studio. Esta página es una vista de lectura del catálogo canónico de Hornero
([`editions/catalogue.yaml`](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml)
en HorneroOS/hornero); no es un segundo catálogo. Si esta página y el catálogo
difieren, gana el catálogo y esta página está desactualizada.

**Última verificación: 2026-11-12** contra el
[índice de paquetes de Arch](https://archlinux.org/packages/). La presencia de
un paquete no equivale a soporte de Hornero: Studio es una edición
**Soportada** (decisión del maintainer en HorneroOS/hornero#318), ninguna
aplicación de abajo está validada por QA de Hornero en hardware físico todavía
y ninguna fila promete que una app se instale, corra o esté soportada en un
hardware específico.

## Matriz

| Aplicación | Paquetes | Origen | Licencia | Instalación | Estado | Grupos |
| --- | --- | --- | --- | --- | --- | --- |
| Ardour | ardour | [arch-extra](https://archlinux.org/packages/extra/x86_64/ardour/) | open-source (CC0-1.0, GPL-2.0-or-later, GPL-3.0-or-later, MIT) | pacman-repository | Preview — sin validar en QA | Audio & Music Production |
| Guitarix | guitarix | [arch-extra](https://archlinux.org/packages/extra/x86_64/guitarix/) | open-source (GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later) | pacman-repository | Preview — sin validar en QA | Audio & Music Production |
| Carla | carla | [arch-extra](https://archlinux.org/packages/extra/x86_64/carla/) | open-source (GPL-2.0-or-later) | pacman-repository-opt-in | Preview — sin validar en QA | Audio & Music Production |
| Audacity | audacity | [arch-extra](https://archlinux.org/packages/extra/x86_64/audacity/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Preview — sin validar en QA | Audio & Music Production |
| REAPER | reaper | [arch-extra](https://archlinux.org/packages/extra/x86_64/reaper/) | propietaria (LicenseRef-EULA) | pacman-repository-opt-in | Preview — sin validar en QA | Audio & Music Production |
| yabridge (puente VST de Windows) | yabridge, yabridgectl | [arch-extra](https://archlinux.org/packages/extra/x86_64/yabridge/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Preview — sin validar en QA | Audio & Music Production |
| OBS Studio | obs-studio, ffmpeg | [arch-extra](https://archlinux.org/packages/extra/x86_64/obs-studio/) | open-source (GPL-2.0-only, GPL-3.0-only) | pacman-repository | Preview — sin validar en QA | Streaming & Content Creation |
| Kdenlive | kdenlive, ffmpeg | [arch-extra](https://archlinux.org/packages/extra/x86_64/kdenlive/) | open-source (GPL-2.0-or-later, GPL-3.0-only) | pacman-repository | Preview — sin validar en QA | Video Editing & Post-Production |
| Blender | blender | [arch-extra](https://archlinux.org/packages/extra/x86_64/blender/) | open-source (Apache-2.0, BSD-2-Clause, BSD-3-Clause, GPL-2.0-or-later, GPL-3.0-or-later, LGPL-2.1-or-later, MIT, MPL-2.0, Zlib) | pacman-repository | Preview — sin validar en QA | Video Editing & Post-Production; 3D, Animation & VFX; Game Development; Maker & CAD |
| Krita | krita | [arch-extra](https://archlinux.org/packages/extra/x86_64/krita/) | open-source (GPL3) | pacman-repository | Preview — sin validar en QA | Graphic Design & Illustration; 3D, Animation & VFX; Game Development |
| GIMP | gimp | [arch-extra](https://archlinux.org/packages/extra/x86_64/gimp/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Preview — sin validar en QA | Graphic Design & Illustration; Photography & RAW Processing |
| Inkscape | inkscape | [arch-extra](https://archlinux.org/packages/extra/x86_64/inkscape/) | open-source (GPL, LGPL) | pacman-repository-opt-in | Preview — sin validar en QA | Graphic Design & Illustration; Game Development; Maker & CAD |
| darktable | darktable | [arch-extra](https://archlinux.org/packages/extra/x86_64/darktable/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Preview — sin validar en QA | Photography & RAW Processing |
| RawTherapee | rawtherapee | [arch-extra](https://archlinux.org/packages/extra/x86_64/rawtherapee/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Preview — sin validar en QA | Photography & RAW Processing |
| Graphite | graphite | [arch-extra](https://archlinux.org/packages/extra/x86_64/graphite/) | open-source (GPL-2.0-or-later, LGPL-2.1-or-later, MPL-2.0) | pacman-repository-opt-in | Preview — sin validar en QA | Graphic Design & Illustration |
| Penpot | — | — | — | none | Preview — sin validar en QA | Custom Selection |
| Scribus | scribus | [arch-extra](https://archlinux.org/packages/extra/x86_64/scribus/) | open-source (GPL-2.0-or-later) | pacman-repository-opt-in | Preview — sin validar en QA | Graphic Design & Illustration |
| FreeCAD | freecad | [arch-extra](https://archlinux.org/packages/extra/x86_64/freecad/) | open-source (LGPL-2.0-only) | pacman-repository-opt-in | Preview — sin validar en QA | Maker & CAD |
| Godot | godot | [arch-extra](https://archlinux.org/packages/extra/x86_64/godot/) | open-source (MIT) | pacman-repository-opt-in | Preview — sin validar en QA | Game Development |
| ArtCraft Launcher | ai.storyteller.artcraft-launcher | [vendor](https://github.com/storytold/craft-launcher/releases) | open-source (MIT, Apache-2.0) | manual | Experimental — sin validar en QA | Custom Selection (solo opt-in explícito de aplicación; nunca en una especialización) |

## Cómo leer la matriz

- **Origen** es el repositorio de Arch que distribuye el paquete hoy
  (`arch-extra` en cada fila instalable). Los artefactos de AUR y de
  fabricantes quedan separados en el catálogo y nunca se instalan ejecutando
  recetas de compilación de AUR.
- **Clase de licencia** resume el `licenseClass` del catálogo; los
  identificadores son los valores de metadatos del paquete en Arch. Los
  metadatos del catálogo nunca otorgan una licencia de software ni de plugins.
- **Método de instalación** `pacman-repository` significa que el paquete forma
  parte del conjunto resuelto de Studio; `pacman-repository-opt-in` significa
  que solo entra en un plan cuando el usuario elige la aplicación o la
  especialización. Las aplicaciones propietarias requieren además una
  selección explícita de la aplicación (mirá REAPER).
- **Estado Hornero** se mantiene en `Preview — sin validar en QA` hasta que
  HorneroOS/qa publique evidencia de aceptación para ese flujo.

## Notas sobre software propietario y compatibilidad

- **REAPER** es software propietario bajo el EULA de Cockos
  (`LicenseRef-EULA`). Es solo opt-in, HorneroOS no incluye ninguna licencia
  para él y elegir una especialización que lo liste nunca lo instala sin una
  selección explícita de REAPER.
- **yabridge/yabridgectl** son herramientas open-source de compatibilidad para
  VST de Windows. Requieren Wine y plugins de Windows que el usuario haya
  obtenido legalmente; HorneroOS no provee configuración de Wine ni plugins.
- **Penpot** no tiene paquete en Arch. Es solo de referencia en el catálogo:
  usá el servicio alojado o una instancia propia. No se puede seleccionar para
  instalar.
- **Graphite** figura como experimental en el catálogo y aparece marcado así
  en cada plan de selección.
- **ArtCraft Launcher** es experimental, distribuido por el fabricante y de
  instalación exclusivamente manual: nunca entra en un plan de paquetes, ni
  siquiera al seleccionarlo, y ningún componente de HorneroOS lo descarga.
  Mirá [ArtCraft Launcher](studio-artcraft.md) para ver su ciclo de vida.

## Especializaciones

Podés combinar las diez especializaciones del catálogo (Audio & Music
Production; Video Editing & Post-Production; Streaming & Content Creation;
Graphic Design & Illustration; Photography & RAW Processing; 3D, Animation &
VFX; Game Development; Maker & CAD; Complete Creative Workstation; Custom
Selection) al instalar o más adelante mediante `horneroctl` y el Centro de
control. Complete Creative Workstation es la unión de los grupos curados;
Custom Selection elige aplicaciones sin ningún grupo obligatorio. Mirá
[Ediciones](../architecture/editions.md).
