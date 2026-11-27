# Revisión de la wiki histórica de dotfiles

> Traducción al español rioplatense de la
> [versión en inglés](../../development/dotfiles-wiki-disposition.md), que es la
> canónica.

La [wiki histórica del repositorio de dotfiles][wiki] se minó como insumo, no
se copió como documentación actual de HorneroOS. Sus instrucciones de armado
mezclaban comportamiento del producto con el hardware, las aplicaciones, las
elecciones de paquetes, los scripts y los flujos de trabajo de una sola
persona. Este inventario registra cada página Markdown de esa wiki.

## Guía actual derivada de material histórico

Estas páginas aportaron temas útiles, pero sus procedimientos y rutas se
reescribieron o revalidaron antes de publicarse:

- **Requiere reescritura — `Audio-Devices.md`:** los conceptos de audio pueden
  informar soluciones futuras; la configuración personal de PipeWire no es un
  valor por defecto del producto.
- **Requiere reescritura — `CONTRIBUTING.md`:** reemplazada por la
  [guía de contribución](contributing.md) propia de este repositorio.
- **Requiere reescritura — `Customization.md`:** la personalización general
  nutrió [Apariencia](../desktop/appearance.md); se excluyeron pasos de chezmoi.
- **Requiere reescritura — `Hardware-nvidia-troubleshooting.md`:** los
  diagnósticos genéricos de gráficos nutren [Hardware](../hardware/README.md);
  las instrucciones de controladores requieren la guía actual de Arch.
- **Requiere reescritura — `Hardware.md`:** los temas amplios de hardware
  nutrieron el nuevo índice de hardware; se excluyó el inventario de máquina.
- **Requiere reescritura — `Hyprland-Keybindings.md`:** los atajos se
  verificaron contra la configuración actual publicada para
  [Atajos](../desktop/shortcuts.md).
- **Requiere reescritura — `Lockscreen.md`:** los conceptos se revalidaron
  contra la Shell actual antes de incluir guía sobre la pantalla de bloqueo.
- **Requiere reescritura — `Network-Manager.md`:** los diagnósticos generales de
  conexión nutren [Solución de problemas](../troubleshooting/README.md); se
  excluyeron scripts personales.
- **Requiere reescritura — `Quickshell-Shell.md`:** los conceptos de shell
  nutrieron la [guía del escritorio](../desktop/README.md); el detalle de
  tiempo de ejecución queda en los docs de la Shell.
- **Requiere reescritura — `Rice-System-Theme-Management.md`:** los conceptos
  actuales están en [Apariencia](../desktop/appearance.md) y
  [Fondos](../desktop/wallpapers.md); las rutas de estado viejas se
  descartaron.
- **Requiere reescritura — `Security.md`:** las afirmaciones actuales de
  privacidad se verificaron contra la Shell antes de incluirse en
  [Seguridad y privacidad](../security/README.md).
- **Requiere reescritura — `Smart-Colors-System.md`:** las ideas de color
  nutrieron los docs actuales de apariencia; rutas y comandos viejos se
  descartaron.
- **Requiere reescritura — `Testing.md`:** reemplazada por la
  [guía actual de pruebas](testing.md) y el proyecto Hornero QA existente.
- **Requiere reescritura — `Window-Managers.md`:** el contexto general es útil,
  pero los layouts y atajos publicados deben salir de la configuración actual.

## Material histórico, personal u obsoleto

- **Histórico — `Changelog-2025.md`:** cronología de dotfiles, no historial de
  releases de HorneroOS.
- **Histórico — `Home.md`:** antigua portada de la wiki, superada por este
  manual y la navegación de docs del sitio web.
- **Histórico — `Quickshell-Parity-Checklist.md`:** vieja lista de migración;
  el trabajo activo pertenece a issues actuales y docs de arquitectura de la
  Shell.
- **Histórico — `Theme-Gallery.md`:** la galería vieja no define el catálogo de
  temas en vivo.
- **Histórico — `_Sidebar.md`:** antigua navegación de wiki, ahora superada.
- **Solo personal — `CopyQ-Customization.md`:** estilo personal de aplicación,
  no es un contrato soportado del escritorio.
- **Solo personal — `Hybrid-GPU-Performance.md`:** los benchmarks dependen de
  una laptop, GPU, cableado de pantalla y estado de controladores puntuales.
- **Solo personal — `Kitty.md`:** configuración y alias personales de terminal.
- **Solo personal — `Nix-Home-Manager.md`:** configuración personal opcional,
  no es soporte de paquetes de Hornero.
- **Solo personal — `Studio.md`:** stack personal de producción de audio y
  scripts de aprovisionamiento.
- **Solo personal — `Thunar-Side-Panel.md`:** marcadores personales del gestor
  de archivos.
- **Solo personal — `Yazi.md`:** selección y atajos personales del gestor de
  archivos.
- **Solo personal — `Zsh.md`:** configuración personal de shell, no es un valor
  por defecto del sistema ni contrato de CLI.
- **Obsoleto — `Dots-Backup.md`:** envoltorio y nomenclatura retirados de
  dotfiles.
- **Obsoleto — `Dots-Eject.md`:** instrucciones para salir de una instalación
  personal de chezmoi; ajeno al uso soportado del producto.
- **Obsoleto — `Dots-Scripts.md`:** catálogo de scripts personales, no la CLI
  del SO.

## Reglas de reutilización

- Reescribí las guías retenidas contra los paquetes, la configuración y el
  comportamiento actual de la CLI.
- No copies resultados de hardware, herramientas personales, scripts de
  aprovisionamiento, rutas privadas ni supuestos de máquina en los docs del
  producto.
- Mantené el material histórico etiquetado como historia y separado de las
  instrucciones actuales de usuario.
- No revivas comandos retirados `dots-*`. Usá la
  [guía de horneroctl](../desktop/horneroctl.md) y la ayuda de la CLI como
  contrato de comandos.

## Material de aplicaciones llevado adelante

Las páginas de aplicaciones de la wiki se verificaron contra las fuentes
actuales de config, CLI y Shell antes de sumar cualquier flujo al manual
público:

| Página histórica | Clasificación | Tratamiento actual |
| --- | --- | --- |
| `Kitty.md` | Solo personal | [Terminal][app-term] |
| `Yazi.md` | Solo personal | [Archivos][app-files] |
| `CopyQ-Customization.md` | Solo personal | [Portapapeles][app-clip] |
| `Thunar-Side-Panel.md` | Solo personal | [Archivos][app-files] |
| `Zsh.md` | Solo personal | [Terminal][app-term] |
| `Audio-Devices.md` | Reescritura | [Medios y audio][app-media] |
| `Network-Manager.md` | Reescritura | [Conectividad][app-conn] |
| `Studio.md` | Solo personal | Ver la nota abajo. |
| `Dots-Scripts.md` | Obsoleto | [`horneroctl`][cli] · [Apps][apps] |

Las paletas de Kitty y los atajos actuales se verificaron contra Hornero
Config. Los alias personales y la configuración del prompt quedan fuera de los
valores por defecto del producto. La guía de Yazi ahora sigue el atajo actual
Super+E y `horneroctl apps terminal-file`; las herramientas de vista previa
siguen siendo opcionales. La guía de CopyQ describe el respaldo actual
CopyQ/cliphist/mínimo y el tema generado. Se quitaron comandos viejos y
afirmaciones no soportadas sobre sincronización o cifrado. Los marcadores de
Thunar, la configuración de Zsh y los presets de REAPER/Guitarix siguen siendo
personales. Las acciones actuales de Thunar y la integración de audio están
documentadas en las páginas de flujo enlazadas.

El resto de las páginas históricas conserva las disposiciones anteriores. En
particular, los benchmarks de NVIDIA/GPU híbrida, elecciones personales de
navegador o editor, scripts de paquetes de host, sugerencias de herramientas de
seguridad y rutas específicas de máquina no son valores por defecto de Hornero.
El [repositorio de dotfiles][dotfiles] es una referencia útil para una estación
de trabajo configurada, pero sus scripts de aprovisionamiento no definen el
contrato de paquetes de HorneroOS.

[wiki]: https://github.com/ulises-jeremias/dotfiles/tree/main/docs/wiki
[app-term]: ../applications/terminal.md
[app-files]: ../applications/files.md
[app-clip]: ../applications/clipboard.md
[app-media]: ../applications/media-audio.md
[app-conn]: ../applications/connectivity.md
[cli]: ../desktop/horneroctl.md
[apps]: ../applications/README.md
[dotfiles]: https://github.com/ulises-jeremias/dotfiles
