# Desarrollo y contribución

HorneroOS se desarrolla entre repositorios. Empezá identificando la capa
dueña del comportamiento y después leé el `AGENTS.md`, el README y las
instrucciones para colaboradores de ese repositorio antes de editar.

## Elegí un camino de contribución

- [Arquitectura](../architecture/README.md) — encontrá al dueño de un
  cambio.
- [Design language](../../development/design-language.md) — identidad de
  producto compartida, principios de interfaz y fuentes de diseño
  autorizadas entre repositorios.
- [Testing](../../development/testing.md) — elegí chequeos enfocados y
  aceptación gráfica.
- [Calidad y releases](../../development/quality-and-releases.md) —
  clases de evidencia, aceptación gráfica, firma y cómo se construyen
  las releases.
- [Contributing](../../development/contributing.md) — expectativas de
  ramas, revisión y trabajo entre repositorios.
- [Internationalization](../../development/i18n.md) — contrato actual de
  idioma y strings.
- [Wiki de dotfiles histórica](../../development/dotfiles-wiki-disposition.md) —
  cómo se evaluó el conocimiento anterior antes de reutilizarlo.
- [Estudio de experiencia](../../development/experience-reference-study.md) —
  patrones de producto actuales de proyectos relacionados y las
  decisiones que HorneroOS toma a partir de ellos.
- [Matriz competitiva](../../development/competitive-capability-matrix.md) —
  comparación respaldada por evidencia contra referencias de escritorio
  upstream.
- [Asistente Hermes](../../development/hermes-assistant-architecture.md) —
  el contrato de diseño del asistente opcional de Hornero respaldado por
  Hermes.
- [Auditoría de backlog](../../development/backlog-audit-2026-10-19.md) —
  hallazgos de la auditoría del ecosistema, reconciliación del backlog e
  índice de issues creadas.

## Regla de fuente de verdad

Implementá el comportamiento en el repositorio dueño. Mantené este
manual enfocado en guía para usuarias, usuarios y colaboradores; dejá
los detalles de API y los contratos a nivel código con su implementación.
El sitio web importa este repositorio en un commit revisado y es dueño
de la navegación y la presentación, no de una copia paralela de la
documentación.

## Verdad del producto

HorneroOS está en desarrollo. Que un entorno de desarrollo funcione o
que exista el paquete de un componente no implica una instalación
soportada para usuarios finales. Revisá el estado actual de releases e
instalación antes de escribir guías o afirmaciones. Etiquetá
explícitamente el comportamiento solo-preview y las restricciones
específicas de paquetes.

## Reportá un bug

Abrí un reporte enfocado en el repositorio dueño del comportamiento que
falla. Incluí la revisión del componente, el resultado esperado y el
real, la reproducción más corta y las primeras líneas de error
relevantes ya sanitizadas. Nunca adjuntés capturas privadas ni logs
personales completos.

- [Shell](https://github.com/HorneroOS/shell/issues) — escritorio y
  Ajustes.
- [Config](https://github.com/HorneroOS/config/issues) — valores por
  defecto y packs de temas.
- [horneroctl](https://github.com/HorneroOS/hornero/issues) —
  comportamiento de la CLI.
- [Website](https://github.com/HorneroOS/website/issues) — páginas
  públicas y presentación de la documentación.
- [Installer](https://github.com/HorneroOS/installer/issues) — arranque
  de la ISO, instalación con Calamares y reportes del primer arranque.
