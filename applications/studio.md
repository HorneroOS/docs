# Studio applications

Verified application, source, license, and support matrix for HorneroOS
Studio. This page is a reading view of the canonical Hornero catalogue
([`editions/catalogue.yaml`](https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml)
in HorneroOS/hornero); it is not a second catalogue. If this page and the
catalogue disagree, the catalogue wins and this page is stale.

**Last verified: 2026-10-25** against the
[Arch package index](https://archlinux.org/packages/). Package presence is
not Hornero support: Studio is **Planned**, no application below is
QA-validated by Hornero yet, and no row promises that an app installs,
runs, or is supported on any hardware.

## Matrix

| Application | Packages | Source | License | Install | Status | Groups |
| --- | --- | --- | --- | --- | --- | --- |
| Ardour | ardour | [arch-extra](https://archlinux.org/packages/extra/x86_64/ardour/) | open-source (CC0-1.0, GPL-2.0-or-later, GPL-3.0-or-later, MIT) | pacman-repository | Planned — not QA-validated | Audio & Music Production |
| Guitarix | guitarix | [arch-extra](https://archlinux.org/packages/extra/x86_64/guitarix/) | open-source (GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later) | pacman-repository | Planned — not QA-validated | Audio & Music Production |
| Carla | carla | [arch-extra](https://archlinux.org/packages/extra/x86_64/carla/) | open-source (GPL-2.0-or-later) | pacman-repository-opt-in | Planned — not QA-validated | Audio & Music Production |
| Audacity | audacity | [arch-extra](https://archlinux.org/packages/extra/x86_64/audacity/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Planned — not QA-validated | Audio & Music Production |
| REAPER | reaper | [arch-extra](https://archlinux.org/packages/extra/x86_64/reaper/) | proprietary (LicenseRef-EULA) | pacman-repository-opt-in | Planned — not QA-validated | Audio & Music Production |
| yabridge (Windows VST bridge) | yabridge, yabridgectl | [arch-extra](https://archlinux.org/packages/extra/x86_64/yabridge/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Planned — not QA-validated | Audio & Music Production |
| OBS Studio | obs-studio, ffmpeg | [arch-extra](https://archlinux.org/packages/extra/x86_64/obs-studio/) | open-source (GPL-2.0-only, GPL-3.0-only) | pacman-repository | Planned — not QA-validated | Streaming & Content Creation |
| Kdenlive | kdenlive, ffmpeg | [arch-extra](https://archlinux.org/packages/extra/x86_64/kdenlive/) | open-source (GPL-2.0-or-later, GPL-3.0-only) | pacman-repository | Planned — not QA-validated | Video Editing & Post-Production |
| Blender | blender | [arch-extra](https://archlinux.org/packages/extra/x86_64/blender/) | open-source (Apache-2.0, BSD-2-Clause, BSD-3-Clause, GPL-2.0-or-later, GPL-3.0-or-later, LGPL-2.1-or-later, MIT, MPL-2.0, Zlib) | pacman-repository | Planned — not QA-validated | Video Editing & Post-Production; 3D, Animation & VFX; Game Development; Maker & CAD |
| Krita | krita | [arch-extra](https://archlinux.org/packages/extra/x86_64/krita/) | open-source (GPL3) | pacman-repository | Planned — not QA-validated | Graphic Design & Illustration; 3D, Animation & VFX; Game Development |
| GIMP | gimp | [arch-extra](https://archlinux.org/packages/extra/x86_64/gimp/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Planned — not QA-validated | Graphic Design & Illustration; Photography & RAW Processing |
| Inkscape | inkscape | [arch-extra](https://archlinux.org/packages/extra/x86_64/inkscape/) | open-source (GPL, LGPL) | pacman-repository-opt-in | Planned — not QA-validated | Graphic Design & Illustration; Game Development; Maker & CAD |
| darktable | darktable | [arch-extra](https://archlinux.org/packages/extra/x86_64/darktable/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Planned — not QA-validated | Photography & RAW Processing |
| RawTherapee | rawtherapee | [arch-extra](https://archlinux.org/packages/extra/x86_64/rawtherapee/) | open-source (GPL-3.0-or-later) | pacman-repository-opt-in | Planned — not QA-validated | Photography & RAW Processing |
| Graphite | graphite | [arch-extra](https://archlinux.org/packages/extra/x86_64/graphite/) | open-source (GPL-2.0-or-later, LGPL-2.1-or-later, MPL-2.0) | pacman-repository-opt-in | Planned — not QA-validated | Graphic Design & Illustration |
| Penpot | — | — | — | none | Planned — not QA-validated | Custom Selection |
| Scribus | scribus | [arch-extra](https://archlinux.org/packages/extra/x86_64/scribus/) | open-source (GPL-2.0-or-later) | pacman-repository-opt-in | Planned — not QA-validated | Graphic Design & Illustration |
| FreeCAD | freecad | [arch-extra](https://archlinux.org/packages/extra/x86_64/freecad/) | open-source (LGPL-2.0-only) | pacman-repository-opt-in | Planned — not QA-validated | Maker & CAD |
| Godot | godot | [arch-extra](https://archlinux.org/packages/extra/x86_64/godot/) | open-source (MIT) | pacman-repository-opt-in | Planned — not QA-validated | Game Development |

## Reading the matrix

- **Source** is the Arch repository that ships the package today
  (`arch-extra` for every installable row). AUR and vendor artifacts are
  kept separate in the catalogue and are never installed by executing
  AUR build recipes.
- **License class** summarises the catalogue's `licenseClass`; the
  identifiers are the Arch package metadata values. Catalogue metadata
  never grants a software or plugin license.
- **Install method** `pacman-repository` means the package is part of the
  resolved Studio package set; `pacman-repository-opt-in` means it only
  enters a plan when the user selects the application or specialization.
  Proprietary applications additionally need an explicit application
  selection (see REAPER).
- **Hornero status** stays `Planned — not QA-validated` until HorneroOS/qa
  publishes acceptance evidence for that workflow.

## Proprietary and compatibility notes

- **REAPER** is proprietary software under Cockos's EULA
  (`LicenseRef-EULA`). It is opt-in only, HorneroOS ships no license for
  it, and selecting a specialization that lists it never installs it
  without an explicit REAPER selection.
- **yabridge/yabridgectl** are open-source Windows VST compatibility
  tools. They require Wine and Windows plugins the user has legally
  obtained; HorneroOS supplies neither Wine configuration nor plugins.
- **Penpot** has no Arch package. It is reference-only in the catalogue:
  use the hosted service or a self-hosted instance. It cannot be
  selected for installation.
- **Graphite** is marked experimental in the catalogue and is flagged as
  such in every selection plan.

## Specializations

Users combine the ten catalogue specializations (Audio & Music
Production; Video Editing & Post-Production; Streaming & Content
Creation; Graphic Design & Illustration; Photography & RAW Processing;
3D, Animation & VFX; Game Development; Maker & CAD; Complete Creative
Workstation; Custom Selection) at install time or later through
`horneroctl` and Control Center. Complete Creative Workstation is the
union of the curated groups; Custom Selection picks applications with no
mandatory group. See [Editions](../architecture/editions.md).
