# Auditoría de backlog — 2026-10-19

*Traducción al español rioplatense de la
[versión en inglés](../../development/backlog-audit-2026-10-19.md), que es la
canónica.*

> **Instantánea fechada.** Esta auditoría es previa a la ISO Preview firmada y
> publicada v0.2.0-preview22 (2026-10-26) y a la promoción de Studio a Preview.
> Las afirmaciones sobre instalación y madurez describen la fecha de su
> auditoría.

Estado: auditoría completada; carga de issues y reconciliación ejecutadas el
mismo día. Este informe es un resumen e índice. El estado de los issues vive en
GitHub, no acá; la hoja de ruta sigue siendo
[hornero#154](https://github.com/HorneroOS/hornero/issues/154).

## Método

- Inspección a nivel de código fuente de cada repositorio de HorneroOS más el
  repositorio personal de dotfiles (puntos de entrada, módulos, pruebas, CI,
  empaquetado), en los HEADs de abajo.
- Reconciliación en vivo con GitHub: todos los issues y PRs abiertos obtenidos
  (28 issues abiertos, 1 PR abierto al inicio de la auditoría), issues
  conocidos leídos con comentarios, PRs fusionados recientemente cotejados
  contra el código.
- Estudio upstream: referencias clonadas previamente (Omarchy, Ryoku,
  DankMaterialShell, Noctalia, Hermes Agent en commits fijados) más un
  relevamiento a nivel de documentación de KDE/GNOME/COSMIC, Fedora Atomic,
  NixOS y chezmoi para la matriz de capacidades. Las comparaciones a nivel de
  documentación están marcadas como tales en los issues que las usan; no se
  clonó ni ejecutó nada de instaladores upstream.
- Pasada independiente de revisión sobre cada issue cargado: propiedad, forma
  de plantilla, etiquetas canónicas (`governance/labels.yml`), duplicados,
  criterios de aceptación comprobables.

## Estado de los repositorios al auditar

| Repositorio | HEAD | Issues abiertos (antes → después) |
| --- | --- | --- |
| HorneroOS/hornero | `63d2752` | 2 → 15 |
| HorneroOS/shell | `2c78e9f` | 3 → 12 |
| HorneroOS/config | `76a552f` | 0 → 3 |
| HorneroOS/installer | `d310242` | 3 → 4 |
| HorneroOS/greeter | `179a99b` | 0 → 1 |
| HorneroOS/qa | `a5e7381` | 0 → 4 |
| HorneroOS/docs | `1f0ca9f` | 0 → 1 (+este informe) |
| HorneroOS/website | `fe8c7a0` | 0 → 2 |
| HorneroOS/.github | `74d2143` | 1 → 3 |
| ulises-jeremias/dotfiles | `c156a606` | 19 → 19 (solo comentarios) |

## Principales hallazgos verificados

1. **Las aprobaciones de Hermes están rotas en el cable** (`hornero#168`): el
   cliente envía una clave `decision`; el gateway upstream fijado lee `choice`.
   Probado desde ambos códigos fuente; no se realizó ninguna llamada a un
   gateway en vivo.
2. **Brechas de endurecimiento del asistente** cargadas a nivel de requisito
   (`hornero#169` validación de host del endpoint, `#170` clave CSPRNG, `#172`
   límites HTTP/SSE, `#173` `Idempotency-Key`). No se publica detalle de
   exploit; se siguió la guía `area:security`.
3. **No existen pruebas de contrato con mock de Hermes** (`hornero#171`), que
   es cómo llegó a producción el hallazgo 1. La CI de `horneroctl` además
   corre sus pruebas sin bloquear hoy (riesgo residual anotado en el issue).
4. **La aceptación del instalador está implementada-no-validada**: el arreglo
   de `installer#11` se fusionó (PR `#13`) pero de instalación a primer
   arranque nunca se ejecutó; escenarios de QA cargados como `qa#19`.
5. **La evidencia de smoke/QA en VM de Preview19 está vencida** (último
   paquete preview13): `qa#16`–`#18`.
6. **La migración a Lua de Hyprland está preparada, no activa** en dotfiles
   (punto de entrada heredado activo); consumidores de producto seguidos en
   `hornero#176`/`#177` y `config#88`.
7. **Brechas de completitud del escritorio sin issues previos**: paneles de
   Pantallas, Accesibilidad, Entrada (`shell#220`/`#221`/`#226`), accesibilidad
   del greeter (`greeter#36`), ruptura de contrato de PluginKit (`shell#222` —
   el validador permite un import que el runtime no puede satisfacer).
8. **Actualización/vuelta atrás sigue honestamente sin implementar** (`#62`);
   hijos cargados: `hornero#178` (carril de estado), `#179` (spike de snapshots
   con prueba en VM).

## Reconciliación de issues existentes

| Issue | Clasificación | Acción |
| --- | --- | --- |
| hornero#154 | épica parcial | etiquetas + índice de hijos |
| hornero#62 | parcial | etiquetas + hijos #178/#179 |
| shell#24 | bloqueado (upstream) | etiquetas incl. `status:blocked` |
| shell#47 | impl. sin validar | etiquetas + resto shell#228 |
| shell#77 | subespecificado | etiquetas + pedido de decisión |
| installer#11 | impl. sin validar | nota de vigencia (PR 13 fusionado) |
| installer#12 | preciso | sin cambios (gates del dueño) |
| installer#3 | preciso | nota dividida (hornero#180); ISO igual |
| .github#9 | bloqueado (humano) | `status:blocked`; verificar en #20 |
| dotfiles Lua | épica parcial | comentario y enlaces de producto |
| dotfiles#170-#178 | decisión pendiente | comentario de re-alcance |
| dotfiles#187/#200 | posibles duplicados | consolidación en #200 |
| dotfiles#201 | ruta superada | puntero a config#89 |

La auditoría no cerró ningún issue: los cierres exigen evidencia de validación
ejecutada, algo que una pasada de investigación no produce.

## Nuevos issues cargados (36)

Cargados con los formularios de issues de la organización (encabezados,
prefijos de título, exactamente un `type:*`, a lo sumo un `area:*`, prioridad
según taxonomía) y enlazados a `#154` donde correspondía:

- `hornero`: `#168`–`#180` (corrección/seguridad/pruebas de Hermes, ciclo de
  vida, registro de auditoría, consumidores Lua, carril de actualización, firma)
- `shell`: `#220`–`#228` (paneles, PluginKit, cancelación de Companion,
  notificaciones, luz nocturna, ADR de IA, remanente de rendimiento)
- `config`: `#87` (guarda de deriva GTK), `#88` (puerto Lua), `#89` (pack de
  temas)
- `greeter`: `#36` (accesibilidad)
- `qa`: `#16`–`#19` (evidencia smoke, cadencia, matriz de escenarios, escenarios
  del instalador)
- `docs`: `#45` (cobertura del manual)
- `website`: `#126` (gate de a11y), `#127` (CI de bump de datos)
- `.github`: `#19` (incorporación de colaboradores), `#20` (verificación AUR)
- `installer`: `#14` (pin de label-sync)

Duplicados evitados por diseño: alrededor de diez candidatos de auditoría eran
enmiendas a issues existentes (`#154`, `#62`, `#24`, `#47`, `#77`, `#11`,
`installer#3`, `.github#9`, épica Lua de dotfiles) y se cargaron como
comentarios/etiquetas en lugar de nuevos issues; la firma de ISO quedó dentro de
`installer#3`.

## Manejo de seguridad

Dos temas de endurecimiento se siguen solo a nivel de requisito en issues
públicos (sin formas de salteo, payloads ni análisis de entropía). El trabajo de
custodia de claves sigue en los issues públicos preexistentes (`.github#9`,
`installer#3`, `hornero#180`) con las acciones humanas señaladas. No se publicó
nada sensible.

## Sin resolver / sin cubrir

- No se corrió ninguna VM en vivo, sesión gráfica ni gateway real de Hermes; la
  aceptación gráfica y con Hermes real siguen abiertas (`qa#16`–`#19`,
  `hornero#171`).
- Las comparaciones con GNOME/KDE/COSMIC son a nivel de documentación y deben
  reverificarse antes de implementar `shell#220`/`#221`.
- Sin auditar en profundidad: internos de PAM/sesión del greeter, modelo de
  privilegios de Calamares en el instalador, superficie de `horneroctl` fuera
  del asistente, internos de autenticación de pantalla de bloqueo, paneles de
  impresoras/cuentas de usuario, aceptación NVIDIA/GPU híbrida. Se cargaron
  candidatos solo donde hubo evidencia.
- Si los hijos de `#154` deben convertirse en sub-issues de GitHub es una
  decisión de gobernanza de los mantenedores; en su lugar se usaron enlaces.

## Secuencia sugerida

1. M0: `hornero#168` + `#171` (corrección de aprobaciones con pruebas),
   `qa#16` (evidencia preview19), ejecución de `installer#11` (`qa#19`).
2. M1: `shell#227` (ADR de IA) → `#220`/`#221`/`#226`; `greeter#36`.
3. M2: `shell#222` (PluginKit + persistencia de ubicación).
4. M3: `hornero#174` (ciclo de vida), `#175`, `shell#223` (cancelación real).
5. M0/M4 en paralelo: hijos de `#62` (`#178` → `#179`), firma (`#180`,
   `installer#3`, `.github#9` → `#20`).
