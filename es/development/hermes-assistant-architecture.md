# Arquitectura del asistente Hermes

> Traducción al español rioplatense de la
> [versión en inglés](../../development/hermes-assistant-architecture.md), que
> es la canónica.

Contrato de diseño para el primer corte vertical de Hornero Assistant
respaldado por Hermes. La implementación sigue este documento; donde el código y
este documento discrepen, el código gana y este documento debe corregirse.

## Resumen de decisiones

- **Backend**: Hermes Agent (Nous Research, MIT), estudiado en
  `f14699a1379838862d3020b97785796aa555d36d`. Hermes es el motor de
  razonamiento, uso de herramientas, skills y memoria. HorneroOS no
  reimplementa un bucle de agente y no forkea Hermes.
- **Transporte**: servidor API del gateway de Hermes — HTTP/SSE compatible con
  OpenAI en `127.0.0.1:8642` con una clave Bearer `API_SERVER_KEY`
  (`gateway/platforms/api_server.py` en Hermes). Elegido por sobre el gateway
  TUI JSON-RPC stdio (ciclo de vida frágil del proceso, comportamiento de
  auto-aprobación en el host) y ACP (errores por diferencia de versión;
  sesiones no pertenecientes a la superficie API).
- **Modelo de procesos**: un servicio de asistente Hornero a nivel usuario
  (nunca root) es dueño del ciclo de vida de Hermes. Tal como se publicó
  (`hornero#174`), habilitar el asistente nunca inicia nada:
  `horneroctl assistant gateway start --yes` escribe e inicia la unidad de
  usuario de systemd `hornero-hermes.service`, y `gateway stop --yes` detiene
  solo esa unidad. La shell nunca orquesta modelos.
- **UI**: Hornero Companion (Quickshell/QML) es solo presentación, según el ADR
  002 en el repositorio de la shell. Los estados reservados existentes
  `listening / thinking / acting / success / warning / error` mapean a la
  actividad del asistente; el IPC existente de Companion sigue siendo el límite
  de presentación.

## Ciclo de vida del gateway (publicado, hornero#174)

`horneroctl assistant gateway` es dueño de iniciar y detener el gateway:

- `gateway status` (por defecto): informa el estado clasificado — `disabled`,
  `not-installed`, `installed-not-running`, `running-incompatible` o
  `running-compatible` — más el estado de la unidad de usuario
  `hornero-hermes.service`. La misma clasificación aparece como `state` en
  `assistant health`.
- `gateway start --yes`: exige que el asistente esté habilitado y Hermes en
  PATH (la guía de instalación nombra un paquete fijado y auditable; esta CLI
  nunca descarga Hermes). Escribe
  `~/.config/systemd/user/hornero-hermes.service` solo cuando el contenido
  cambió, recarga el daemon e inicia la unidad. Si el gateway ya responde, lo
  informa y no inicia un duplicado. Sin una sesión de usuario de systemd
  degrada a la guía "ejecutá `hermes gateway run` manualmente".
- `gateway stop --yes`: detiene solo la unidad que administra Hornero. Un
  gateway iniciado en otro lado se informa, nunca se mata: Hornero no termina
  procesos que no le pertenecen.

Ninguno de los dos comandos necesita root, habilita nada al iniciar sesión ni
amplía el endpoint loopback. Ambos requieren `--yes` explícito (`--dry-run`
previsualiza), igual que `assistant enable`.

`horneroctl assistant setup [--dry-run|--yes]` realiza la mitad propiedad de
Hornero para levantar Hermes (`hornero#191`): habilitación con la clave 0600,
la unidad del gateway y la skill de Hornero instalada en el home de Hermes
desde una copia embebida (refrescada solo cuando cambia). Cuando falta Hermes
falla antes de cambiar nada e imprime el contrato de fuente fijado —
`NousResearch/hermes-agent` en el commit estudiado, disposición local de
usuario — porque `horneroctl` nunca descarga Hermes ni ejecuta un script
remoto de instalación. `setup --remove` revierte solo lo que `setup` escribió
(una skill modificada por el usuario se conserva y se informa); la instalación
propia de Hermes es propiedad del usuario. Empaquetar el binario de Hermes como
paquete sigue siendo una decisión del carril de instalador.

`assistant knowledge` exporta el catálogo vivo de solo lectura como una
instantánea acotada en Markdown (fechada y sellada con procedencia) para
agentes que no pueden ejecutar comandos; `assistant tools --json` en vivo sigue
siendo la verdad.

## Contrato de transporte (desde el código de Hermes)

| Operación | Endpoint |
| --- | --- |
| Capacidades | `GET /v1/capabilities` |
| Iniciar run | `POST /v1/runs` |
| Transmitir eventos | `GET /v1/runs/{id}/events` |
| Cancelar | `POST /v1/runs/{id}/stop` |
| Aprobación | `POST /v1/runs/{id}/approval` |
| Aclaración | `POST /v1/runs/{id}/clarify` |

Notas:

- Las capacidades se negocian antes de cualquier run; las expectativas se fijan
  por versión soportada de Hermes.
- Iniciar envía un `Idempotency-Key`. Las sesiones pertenecen a la API: sesiones
  externas CLI/TUI/ACP devuelven 409, así que el asistente crea y mantiene sus
  propias sesiones.
- Los eventos se transmiten por SSE: tokens, actividad de herramientas y
  pedidos de aprobación.
- Cancelar debe conectarse a la acción de cancelar de la UI y a los estados
  success/error de Companion.
- Hermes pide aprobación; el usuario decide en la UI nativa. Las aprobaciones
  nunca se auto-responden.

Autenticación: una clave Bearer generada por usuario, guardada con permisos
restrictivos (`0600`) en el directorio de configuración del usuario, nunca
commiteada, nunca registrada en logs. Solo loopback; ningún listener sale de
`127.0.0.1`.

## Primer corte vertical (alcance)

1. El usuario habilita explícitamente el asistente (Ajustes y superficie de
   Companion, con paridad en `horneroctl`). Valor por defecto: **disabled**. El
   escritorio normal está completo con Hermes ausente.
2. El servicio inicializa Hermes. Salud significa un `GET /v1/capabilities`
   exitoso.
3. Companion abre una conversación; el usuario envía un mensaje; Hermes
   transmite una respuesta real; Companion muestra estados de pensando y
   hablando.
4. Las herramientas nativas de solo lectura (abajo) son invocables por Hermes.
   La actividad de herramientas es visible en la UI. El usuario puede cancelar a
   mitad de ejecución.
5. Preguntas como "por qué mi sistema está usando memoria" o "qué
   actualizaciones hay" se responden desde salida real de `horneroctl`, nunca
   respuestas fijas.
6. Rutas de fallo — Hermes faltante, versión incorrecta, conflicto de puerto,
   proveedor sin configurar — devuelven cada una un mensaje humano de
   recuperación, nunca un stack trace.
7. Deshabilitar detiene la integración y el daemon. Costo cero en reposo cuando
   está apagado.

## Catálogo de herramientas nativas (corte 1: solo lectura)

Expuestas como argv literal mediante el límite `exec` existente de
`hornero_core` (sin interpolación de shell). Todas devuelven la envoltura
uniforme `--json`. Clase de cada herramienta abajo: lectura segura.

- Información del sistema: `horneroctl system info --json`
- Estado de apariencia: `horneroctl appearance status --json`
- Catálogo de temas: `horneroctl appearance theme list --json` y
  `horneroctl appearance theme show <id> --json` (los ids se validan: se
  rechazan `/`, `..` y vacíos)
- Estado de GTK: `horneroctl appearance gtk list --json` y
  `horneroctl appearance gtk current --json`
- Chequeo de actualizaciones: `horneroctl package updates --json` y
  `horneroctl package check --json` (el texto de UX advierte el carril de
  ~30 s del AUR)
- Estado de Companion: `qs ipc call companion status`

Las mutaciones (aplicar tema, instalar paquetes, cambios de ajustes) están
**fuera del corte 1**. El corte 2 las suma solo detrás de la aprobación de
Hermes expuesta en UI nativa, una capacidad por vez, cada una con dry-run
donde `horneroctl` lo soporte.

## Modelo de seguridad

- Deshabilitado por defecto; habilitar es explícito y reversible.
- Servicio a nivel usuario; sin root, sin ampliación de polkit en el corte 1.
- El modelo de aprobación de Hermes nunca se debilita ni se auto-responde.
- No se exponen capturas, portapapeles, micrófono, archivos ni contenido de
  ventanas en el corte 1. Cada uno es una capacidad futura separada con su
  propio consentimiento.
- Secretos: las claves de proveedor pertenecen a la propia configuración de
  Hermes. Hornero guarda solo su clave Bearer local, `0600`, propiedad del
  usuario.
- Postura ante inyección de prompt: los resultados de herramientas son datos, no
  instrucciones; la lista blanca de herramientas de arriba es exhaustiva para el
  corte 1.
- Auditabilidad: el historial de runs y herramientas queda en la sesión de
  Hermes, más un registro local legible por el usuario de invocaciones de
  herramientas (comando y estado del resultado, sin material secreto).

## Empaquetado y versiones

- Hermes se instala por un camino reproducible, fijado por versión y auditable
  (paquete de Arch o runtime aislado administrado). Nunca `curl | bash`.
- El rango de versiones soportado de Hermes se registra junto a la
  implementación; la negociación de capacidades falla cerrada con un mensaje de
  actualización. Tal como está implementado: Hermes no expone semver del
  gateway, así que `horneroctl assistant status` negocia el protocolo — exige
  la plataforma `hermes-agent` más los flags de funcionalidad que llama el
  cliente (`run_submission`, `run_events_sse`, `run_stop`,
  `run_approval_response`, `approval_events`) e informa el commit upstream
  estudiado (`f14699a13798…`) contra el cual se verificó. Un gateway
  incompatible hace fallar `status` con las capacidades faltantes exactas.
- Instalar, actualizar, deshabilitar y desinstalar son operaciones separadas y
  probadas. Desinstalar nunca borra configuración de usuario sin consentimiento
  explícito.

## Gates de rendimiento

- Asistente deshabilitado: cero procesos, cero costo en reposo.
- Habilitado pero inactivo: se miden y registran RSS/CPU del daemon. No se
  cargan modelos locales ni se descargan pesos sin acción explícita del
  usuario.
- Sobrecarga de la shell: la UI de streaming no debe regresar las líneas base
  del lanzador ni de cuadros (las herramientas de rendimiento de la shell son
  dueñas de la medición).

## Pruebas de aceptación (corte 1)

- Compatibilidad de protocolo contra la versión fijada de Hermes (backend mock
  más Hermes real).
- Streaming, cancelación y reconexión tras un reinicio del daemon.
- Ruta de denegación de aprobación: denegar debe bloquear la acción.
- Cumplimiento de lista blanca de herramientas: un prompt que pide una acción no
  listada no obtiene ejecución.
- Deshabilitar y desinstalar dejan el escritorio común totalmente funcional.
- Reporte de recursos para estados deshabilitado, inactivo y transmitiendo.

## Aceptación con Hermes real (ejecutada el 2026-10-19)

Contra Hermes en el commit fijado corriendo localmente con un proveedor real
(OpenAI), a nivel usuario y solo en loopback:

- `assistant status` negocia el protocolo como compatible; `assistant ask`
  devolvió una respuesta real del modelo.
- Uso de herramientas desde la skill `hornero` incluida: el agente respondió
  los temas GTK instalados a partir de `horneroctl appearance gtk list --json`
  (20 temas), no desde conocimiento genérico.
- Flujo de aprobación con `approvals.mode: manual`: un run de `rm -rf` quedó
  estacionado en `waiting_for_approval`; `assistant approve` lo ejecutó
  (verificado por el agente), y un segundo run denegado dejó intacto el
  objetivo. Esto detectó y corrigió el protocolo de cable de aprobaciones
  (`hornero#168`): la ruta autorizada del gateway requiere
  `{request_id, execution_generation, choice}` desde `pending_controls`, con
  `approve` mapeado únicamente a `once`.
- Streaming en vivo en la CLI (`--stream`) con deltas temporizados.

Todavía abierto: aceptación gráfica de Companion en una sesión de escritorio
en vivo, reporte de recursos y el ciclo de vida administrado (`hornero#174`).
El empaquetado de Hermes para usuarios finales **no** está decidido; la
aceptación local usó un runtime de código fijado con `uv sync --frozen`, nunca
un script de instalación.

## Frente a Ryoku Rashin (estudiado en `98a0368`)

Rashin (`docs/rashin.md`, `ryoku/rashin/` de Ryoku) es un daemon en Go con una
bóveda generada de conocimiento, un dashboard web en loopback sin autenticar
(chequeado por Origin), chat ACP, un carril rápido de consulta de solo lectura e
instalación de Hermes en un clic vía el instalador oficial. HorneroOS difiere
deliberadamente donde es más estricto:

| Eje | Rashin | HorneroOS |
| --- | --- | --- |
| Auth de transporte | ninguna (Origin) | Auth Bearer, archivo `0600` |
| Instalación Hermes | instalador oficial | runtime fijado, auditable |
| Seguridad protocolo | puente ACP/stdio | negociación de capacidades |
| Aprobaciones | prompts ACP | protocolo verificado en vivo |
| UI | dashboard web | panel nativo de chat Companion |
| Conocimiento | bóveda generada | horneroctl vivo + skill |
| Alcance de agente | cualquier agente | Hermes como backend oficial |

La bóveda de Rashin, su carril rápido de consulta y la UX de historial de
sesiones siguen valiendo estudio; adoptar cualquiera de ellas es trabajo aparte
basado en evidencia, no imitación por sí misma.

## Fuera de alcance para el corte 1

Entrada/salida de voz, sugerencias proactivas, ejecución arbitraria de
comandos, mutaciones de paquetes, acceso a archivos, administración de claves
multi-proveedor del lado de Hornero y cualquier afirmación de operación
offline.

## Arnés seguro (Javi, 2026-11)

El corte 1 anterior mantuvo a propósito al agente en solo lectura y confió en
las aprobaciones de Hermes. El arnés seguro suma las capas de cumplimiento que
faltaban en `horneroctl`, fuera del proceso del agente, siguiendo el propio
`SECURITY.md` §2.2 de Hermes (solo el aislamiento a nivel de SO es un límite):

- **Sandbox de kernel.** La unidad `hornero-hermes.service` que escribe
  `horneroctl` está endurecida con systemd y, cuando bubblewrap está
  disponible, corre todo el proceso de Hermes en una vista bwrap: home
  enmascarado, solo `~/.hermes` y el espacio de trabajo activo de Javi
  enlazados, directorio de runtime de sesión enmascarado (sin socket Wayland
  ni D-Bus). Sin bwrap, el estado informa honestamente
  `systemd-only (not sandboxed)`.
- **Política ABAC.** `horneroctl assistant policy` evalúa
  Principal+Action+Resource+Context con denegación por defecto, primacía de
  denegación, denegaciones duras (rutas protegidas, shell desatendida,
  remoción de paquetes), aprobaciones atadas a acción+recurso+vencimiento
  exactos e intersección de delegación. Presets: read-only (por defecto),
  workspace-agent, desktop-assistant; `revoke-all` aplica en el acto.
- **Broker tipado.** `horneroctl assistant tool` ejecuta un catálogo fijo
  (herramientas de solo lectura del sistema, ajuste de tema oficial, lista y
  foco de ventanas, notificación, captura mediada) solo tras una autorización
  de política; cada resultado queda en log de auditoría. No hay herramienta
  genérica de comandos.
- **Espacios de trabajo.** El alcance de escritura del agente vive bajo el
  directorio de datos XDG, nunca `$HOME`; el registro y el archivo de política
  quedan fuera del sandbox para que el agente no pueda ampliar su propio
  alcance.
- **Modos.** Las sesiones son Ask / Agent / Chat. Ask y Chat nunca escalan:
  `horneroctl` deniega sus aprobaciones de Hermes del lado del servidor.
- **Prompt.** El system prompt de usuario es el `SOUL.md` de Hermes, editable
  mediante `horneroctl assistant prompt` con historial de versiones y vuelta
  atrás. Solo comportamiento — nunca autorización.

Diseño completo, riesgos residuales y evidencia de pruebas en host:
`HorneroOS/hornero: docs/javi-secure-harness.md` (`hornero#374`, `shell#353`).
