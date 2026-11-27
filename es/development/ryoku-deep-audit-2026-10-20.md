# Spike: escritorio Ryoku vs HorneroOS — ¿dónde debe ser mejor Hornero?

*Traducción al español rioplatense de la
[versión en inglés][canonical], que es la canónica.*

> **Instantánea fechada.** Esta auditoría es previa a la ISO Preview firmada y
> publicada v0.2.0-preview22 (2026-10-26) y a la promoción de Studio a Preview.
> Las afirmaciones sobre instalación y madurez describen la fecha de su
> auditoría.

**Responsable:** mantenedores de HorneroOS (auditoría asistida por IA)
**Ventana:** sesión del 2026-10-20
**Estado:** Completa

## Propósito

Ryoku (`github.com/Ryoku-dev/ryoku`, auditado en HEAD `98a0368`) es la
referencia open-source más cercana de un escritorio Linux nativo en IA basado
en Quickshell, con una superficie de ajustes Hub, un lanzador federado y el
acompañante Rashin/Hermes. Este spike responde: cuáles de sus fortalezas ya
iguala o supera HorneroOS, cuáles son brechas reales y cuál es la estrategia de
implementación para cerrarlas sin copiar su arquitectura de golpe.

## Enfoque

- Auditoría multi-agente de solo lectura del árbol de Ryoku (lanzador/barra,
  widgets/plugins/temas, DevEx/instalador, esquema Hub) contra los árboles de
  shell/hornero de HorneroOS, con cada afirmación atada a archivos
  inspeccionados (ver Referencias).
- Reconciliación de brechas contra el backlog vivo en GitHub (HorneroOS/shell,
  HorneroOS/hornero), creando solo issues que no existían.
- Implementación en orden de dependencias: backends reales primero
  (`horneroctl`), luego paneles del Centro de control, cada uno verificado en
  vivo en el host de desarrollo.

## Hallazgos

1. **Chat/IA.** Needle/PanelChat de Ryoku transmite respuestas en línea y
   tiene listas de sesiones y selectores de modelo; Rashin copia una bóveda
   estática de conocimiento del sistema (408 filas de esquema) al contexto del
   agente. Hornero ya supera esto en veracidad (catálogo vivo
   `horneroctl assistant tools --json`, transporte loopback autenticado,
   acciones nunca auto-aprobadas) y ahora en paridad básica (streaming NDJSON,
   adjuntos, ruta de voz, historial persistente). La UI de sesiones/modelos se
   sigue en `hornero#189`; el patrón de bóveda de conocimiento se responde con
   instantáneas generadas (`hornero#191`, corte 1 publicado) en lugar de copias
   a mano.
2. **Lanzador.** Ryoku federa 12 proveedores detrás de un despachador por
   prefijos. Hornero tenía apps + prefijos calc/scheme/theme y un `>ai` de
   disparo y olvido. Publicado desde entonces: proveedor de ventanas `>win`
   (`shell#252`) y proveedor acotado de archivos `>file` (`shell#253`, sin
   daemon indexador por diseño). Pendiente: IA transmitida en línea y
   proveedores definidos por plugins (`shell#250`).
3. **Profundidad de ajustes (Hub).** El Hub de Ryoku expone superficies
   profundas por área (ventanas, atajos, captura). El Centro de control de
   Hornero llegó a 24 paneles reales en esta pasada — Pantallas (`#249`),
   Entrada (`#249`), geometría de Ventanas con un nuevo escritor en `horneroctl`
   (`#196` + `#254`), Luz nocturna (`#259`) — cada uno enlazado a backends CLI
   confirmados, nunca interruptores decorativos. Pendiente: reglas de
   foco/flotado (`#235`), panel de atajos sobre el modelo de lectura compatible
   con Lua (`#236` + `hornero#176`, parser publicado en `hornero` PR#202),
   captura/rendimiento (`#237`).
4. **Widgets/plugins/temas.** Ryoku trae 7 widgets de escritorio, un plugin kit
   con descubrimiento y un repositorio de paquetes firmado; sus docs afirman
   tener 57 temas mientras el árbol auditado lista 10 estáticos + dinámico —
   un desvío sin resolver entre docs y código que conviene no repetir. Hornero
   tiene PluginKit + ciclo de vida (`shell#222`, parcial) pero sin diseño de
   firma/procedencia de plugins ni registro (`shell#251`), y la ubicación y
   persistencia de widgets es parcial en `#222`.
5. **DevEx/instalador.** Ryoku es un monorepo con repo/ISO firmado y matriz de
   dry-run; el instalador de Hornero es Calamares provisional (propiedad de
   Panda Foss), sin evidencia de instalación a primer arranque todavía — la
   brecha honesta de madurez, seguida en `HorneroOS/installer`, que no se
   puede cerrar desde la shell.
6. **Lección de seguridad (hallazgo propio).** Reiniciar Quickshell mientras el
   bloqueo de sesión dentro de la shell estaba activo dejó huérfano el bloqueo
   del compositor y forzó un reinicio (`shell#255`, cerrado): `horneroctl`
   ahora rechaza stop/restart mientras está bloqueado, sondeando el IPC de la
   shell porque `LockedHint` de logind queda en `"no"` bajo el bloqueo de la
   shell en Hyprland.

## Recomendación

Mantené la arquitectura de Hornero (un solo proceso de shell, backends propios
de `horneroctl`, catálogo vivo de herramientas por sobre bóvedas copiadas) y
cerrá las brechas restantes de paridad con Ryoku en este orden:

1. `hornero#189` contrato backend de sesiones/modelos, luego selectores del
   panel.
2. `shell#250` IA transmitida en línea en el lanzador.
3. `shell#236` panel de atajos sobre el modelo de lectura `hornero#176`.
4. `shell#222`/`#251` ubicación, firma y procedencia de plugins.
5. `shell#237` captura/rendimiento solo con números medidos.

## Compromisos de diseño

- La búsqueda acotada de archivos bajo demanda (sin daemon) resigna resultados
  instantáneos a cambio de privacidad y costo nulo en reposo; revisitar solo
  con controles de indexado visibles para la persona usuaria.
- Las instantáneas de conocimiento generadas cambian un pequeño paso de
  regeneración por contexto de agente nunca desactualizado; preferible a las
  bóvedas estáticas estilo Rashin.
- Rechazar reinicios de shell con la sesión bloqueada resigna conveniencia por
  una sesión que no puede perder su superficie de bloqueo; desbloquear primero
  es la UX correcta.

## Preguntas abiertas

- El desvío de 57 vs 10 temas de Ryoku: docs viejos o un almacén externo de
  temas fuera del árbol auditado (sin resolver upstream).
- Resiliencia del bloqueo si el proceso de la shell cae mientras está bloqueado
  (`shell#257`): proceso dedicado de bloqueo vs re-bloqueo supervisado —
  necesita prototipo, todavía sin agendar.
- Empaquetado de configuración de Hermes para usuarios finales (`hornero#191`
  corte 2, condicionado a decisiones de ciclo de vida en `hornero#174`).

## Referencias

- Ryoku: [ryoku-dev/ryoku](https://github.com/Ryoku-dev/ryoku) (HEAD `98a0368`)
- Issues de `HorneroOS/shell` `#220`–`#260`, `HorneroOS/hornero` `#176`,
  `#189`–`#202`
- `development/competitive-capability-matrix.md`,
  `development/hermes-assistant-architecture.md`,
  `development/backlog-audit-2026-10-19.md` (este repositorio)
- `HorneroOS/shell` `docs/LOCKING.md`, `docs/NOTIFICATIONS.md`

[canonical]: ../../development/ryoku-deep-audit-2026-10-20.md
