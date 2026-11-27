# Lista de verificación de preparación para release

> Traducción al español rioplatense de la
> [versión en inglés](../../development/release-readiness.md), que es la
> canónica.

**Estado: Preview publicada; NO LISTA para un lanzamiento estable.**
`v0.2.0-preview30` está publicada como ISO Preview firmada (Desktop, Studio y
Gaming Preview). Los gates para lanzamiento estable de abajo siguen abiertos. Un
gate es PASS únicamente cuando la evidencia siguiente existe para la composición
candidata exacta; las pruebas sobre código fuente y los chequeos en el host de
mantenimiento no prueban aceptación de un sistema instalado.

Última revisión: 2026-11-03.

Release publicada actual: [`hornero-0.2.0-preview30`][candidate], seleccionada
por [`manifests/candidate`][candidate-pointer] (producto
`bcc53ede593d54f6b9e7562a50cf6c620e56b275`, instalador
`c8fbc359843c2249945adf0091d732c628330d8f`). Su ISO pasó la matriz de
instalación en máquina virtual sobre la composición preview21 arrastrada, con
el escenario de cancelación-limpieza re-probado de punta a punta; mirá el
[checklist de preview30][p30-chk].

## Gates

- **La ISO instala en hardware limpio o VM — PARTIAL (VM PASS, hardware
  BLOCKED).** Panda Foss es dueño del instalador oficial y de su aceptación. La
  ISO publicada v0.2.0-preview30 (SHA-256
  `474a0405fdc7366848d110b730c65d6f29ac36e66d9b36a9cd1f61e7c6dd1356`) está
  firmada con la clave de releases de HorneroOS
  `FCFBEE43925AB5429362278AE59EAB44AA2498DC` y publicada; su matriz de
  instalación Desktop y Studio (UEFI y BIOS heredado, cifrado y sin cifrar)
  pasó en VMs descartables sobre la composición preview21 arrastrada. La
  cancelación y la limpieza tras instalación exitosa quitaron los montajes
  temporales de destino. El primer login BIOS llegó al escritorio instalado;
  UEFI llegó a la pantalla de login, pero la autenticación no se verificó. La
  paridad de paquetes y perfiles instalados sigue sin verificarse. No se
  validó ninguna instalación en hardware físico. Mirá el
  [registro de validación R11][r11-val], el [issue #11][inst-11] de installer y
  el [issue #19][qa-19] de QA.
- **Arranque al escritorio tras instalar — BLOCKED.** BIOS heredado alcanzó un
  escritorio autenticado en la ISO provisional R11. La autenticación UEFI
  todavía no está verificada, y QA no produjo una corrida aprobada de
  instalación a primer arranque contra el candidato exacto preview20. El
  escenario existente `smoke/desktop-ready` verifica una imagen QA preparada;
  no prueba una instalación completada.
- **Matriz de soporte de compositores — FAIL.** Hyprland es el valor por
  defecto validado. Niri sigue siendo experimental y no tiene aceptación de
  paridad en release candidata.
- **Integridad de paquetes — FAIL.** [hornero#180][h-180] sigue abierto. La
  ingeniería del flujo de firma aterrizó en [hornero#275][h-275], y su smoke en
  CI usa una clave efímera. Eso no prueba que un activo publicado haya sido
  firmado con la clave de release de producción. No hay clave pública de
  release ni secreto de firma de producción aprovisionado (este texto es
  anterior a preview22; la ISO v0.2.0-preview30 está firmada con la clave de
  releases de HorneroOS y la clave pública está commiteada en
  `packaging/keys/hornero-release.pub.asc`). Los checksums del AUR por sí solos
  no establecen autenticidad del mantenedor.
- **Actualizaciones seguras y vuelta atrás del sistema — FAIL.**
  [hornero#216][h-216] sumó carriles de propiedad de solo lectura. El backend
  de vuelta atrás ([hornero#179][h-179]) y los carriles mutantes de
  actualización ([hornero#62][h-62]) siguen abiertos.
  `horneroctl package check` no es una transacción de actualización, y restaurar
  configuración no es una vuelta atrás del sistema operativo.
- **Hermes Companion — PASS solo en el host de desarrollo.** El gateway y el
  chat de Javi se ejercitaron con aprobaciones, historial, adjuntos, voz y
  eventos de actividad. El ciclo de vida de unidad de usuario aterrizó en
  [hornero#252][h-252]; configuración y exportación de conocimiento aterrizaron
  en [hornero#253][h-253]. Empaquetar el runtime de Hermes para una instalación
  limpia sigue abierto en [hornero#191][h-191]. Este PASS no afirma una prueba
  de instalación limpia ni de imagen de release. El arreglo de propiedad de
  instalación/remoción en [hornero#278][h-278] está fusionado, pero no está en
  el candidato preview20 y no hay ninguna release firmada de la CLI que lo
  contenga publicada. La migración dependiente de dotfiles sigue en borrador
  [dotfiles#383][df-383], esperando una release de la CLI y una revisión
  independiente.
- **Ciclo de vida de plugins — PASS para los plugins oficiales probados.** La
  CLI valida, instala datos inertes, lista, habilita, deshabilita y quita
  plugins. El arreglo del host en Shell está en [shell#269][sh-269]. La
  evidencia en tiempo de ejecución registró tres plugins oficiales cargados
  mediante `qs ipc call plugins status`.
- **Marketplace oficial de extensiones — PASS para el catálogo oficial.** El
  catálogo fijado [HorneroOS/plugins][plugins-repo], la instalación verificada
  por CLI, el marketplace en el Centro de control y los metadatos están
  integrados en [hornero#214][h-214], [shell#268][sh-268],
  [plugins#6][pl-6], [hornero#273][h-273] y [shell#309][sh-309]. El
  marketplace también está vivo en [horneroos.com][web-mp]. La fase separada de
  índice comunitario sigue abierta en [shell#251][sh-251]: la custodia de clave
  de registro de producción y el consumo de punta a punta de un índice
  comunitario verificado no están completos. Shell [#318][sh-318] suma
  entradas comunitarias verificadas al Centro de control. El timeout de
  Ajustes de Terminal se corrigió en [shell#321][sh-321], cuyos chequeos
  pasan. La corrida alojada de matriz [40129324336][run-1] expuso luego un
  overlay separado de Welcome al primer inicio de sesión: su ventana de nivel
  superior cubría Ajustes, y la animación del cursor hizo que un chequeo
  inadecuado de diversidad de píxeles aceptara la pantalla equivocada. El
  commit `a325e1e` de Shell #318 cierra Welcome antes de navegar Ajustes y
  verifica que la VM limpia lo descartó antes de los chequeos de Ajustes. La
  corrida alojada en HEAD exacto [40131614836][run-2] falló antes de capturar
  paneles: la CLI `qs` emitió una advertencia de locale de Qt antes del JSON
  válido `{"open":false,"page":"start"}`, y el script smoke pasó ambas líneas
  directo a `jq`. El commit rebaseado `78877c2` de Shell #318 extrae el último
  objeto JSON de la salida IPC y prueba casos de advertencia y sin JSON. La
  corrida [40134380723][run-3] quedó superada luego de que un chequeo de
  gobernanza rechazara su historial con merge commits. El PR se rebaseó
  preservando commits con autoría; una revisión de seguridad también redujo el
  token del workflow de VM a solo lectura de contenidos, ya que el valor por
  defecto de la organización era escritura. La corrida [40136330518][run-4]
  falló en la primera captura de Ajustes de Terminal: el preflight de CLI
  pasó, pero el panel quedó en su spinner de carga. El commit `b5048dd` de
  Shell #318 arregló terminación acotada de procesos, manejo de Welcome cuando
  falla la asignación de Ajustes, expansión de entorno de captura en VM,
  timeouts de diagnóstico SSH, una carrera en pruebas de socket QEMU y
  persistencia de credenciales de checkout. La captura fallida expuso otro
  caso borde: el timer retornaba temprano cuando el proceso ya no corría,
  dejando la carga trabada si no llegaba respuesta ni señal de salida. El
  commit `e59026f` reporta timeout en ese estado y señala solo un proceso vivo.
  La suite enfocada de paneles (37 pruebas) y pre-commit pasan; la suite
  completa pasó antes 641 pruebas con Pillow disponible. La matriz
  [40138798423][run-5] repitió el spinner después de 78 segundos pese al
  arreglo en `e59026f`. El commit `e25ba78` enlaza el timeout al estado de
  carga/proceso en vez de reiniciarlo imperativamente. Build, pruebas, QML,
  lint, harness-lint, smoke-dryrun, gobernanza/Danger y revisión de CodeRabbit
  están en verde en `e25ba78`; no hay hilos de revisión sin resolver. La
  corrida [40140797051][run-6] se canceló a los 25 minutos mientras el guest
  compilaba el plugin QML nativo (el último progreso fue 48%). Su artefacto no
  contiene capturas de paneles; `assertions.json` dice `session start`, lo que
  no coincide con la última salida de build, así que el diagnóstico no es
  concluyente. La corrida fresca [40142966617][run-7] falló en la primera
  captura de Ajustes de Terminal: el título de ventana y la navegación se
  dibujaron, pero la región de contenido del panel quedó vacía. La revisión
  rastreó esto a que el `ColumnLayout` trasladado en `Panes.qml` no tenía
  ancho ni alto explícitos; los tamaños implícitos de hijos no daban geometría
  real al layout. El commit `e02b2ae` de Shell #318 fija la pila al ancho del
  viewport y al alto implícito completo de la pila, con una prueba de
  regresión. La suite completa (642 pruebas), QML lint, pre-commit, build
  CMake y escaneos de higiene pasan en ese commit. La matriz
  [40145172696][run-8] demostró que este arreglo era incompleto. La revisión
  visual halló que su captura smoke era el estado vacío del fondo de
  escritorio, Red mostraba contenido de Apariencia bajo un título de Red y
  Bluetooth tenía una región de contenido vacía; los chequeos previos de
  color/diferencia habían aceptado los dos primeros. El commit `ddd67cf`
  reemplaza el dimensionado implícito de layout por una pila de páginas del
  tamaño del viewport y posiciones/dimensiones explícitas por panel. La matriz
  [40147893239][run-9] confirmó que esto seguía sin renderizar contenidos de
  Terminal ni Bluetooth. La corrida [40150595999][run-10] mostró que la página
  activa de Terminal y el ítem cargado coinciden con la geometría del viewport
  y el Loader está Ready, pero el contenido de la página sale en blanco. El
  commit `1b917b9` agrega diagnósticos para la superficie interior de
  TerminalPane, Flickable, content layout, header y section. La matriz de
  diagnóstico [40152601907][run-11] está en cola. Mirá la
  [última evidencia del issue][sh-251-cmt]. Mantené bloqueado el merge hasta
  que esta matriz complete con éxito y se revisen las 25 capturas. No
  presentes el PASS del catálogo oficial como aceptación de registro
  comunitario; la custodia de clave de producción y la instalación,
  actualización y vuelta atrás comunitarias de punta a punta siguen
  incompletas.
- **Seguridad de bloqueo/sesión — BLOCKED.** La Shell rechaza sus acciones de
  stop/restart mientras está bloqueada y protege pedidos detectables de
  bloqueo en competencia. El fallo de bloqueo huérfano en [shell#24][sh-24]
  sigue sin resolverse: Quickshell v0.3.2 incluye una guarda de adquisición
  fallida, pero el escenario exacto entre bloqueadores no se volvió a correr
  con esa versión; el issue upstream [quickshell#1054][qs-1054] sigue
  abierto. La actualización y evidencia requerida están registradas en el
  [último comentario de shell#24][sh-24-cmt]. La recuperación tras una caída
  espontánea de la Shell mientras está bloqueada sigue abierta en
  [shell#257][sh-257]. La superficie de bloqueo además carece de una pasada
  real de aceptación con lector de pantalla; mirá el gate de accesibilidad.
- **Auditoría de accesibilidad — FAIL.** Los chequeos estáticos cubren los
  controles inventariados y algunos recorridos AT-SPI. La superficie real de
  bloqueo de sesión, una pasada de completitud de tareas con lector de
  pantalla y la exposición en runtime para delegados colapsados siguen sin
  verificarse. Seguí [shell#221][sh-221] y el
  [inventario de accesibilidad de shell 2026-10-21][sh-a11y]. Shell
  [#310][sh-310] tiene CI en verde y evidencia visual para su paleta
  persistida de alto contraste; el PR está abierto y la tarea con Orca sigue
  sin verificarse. Greeter [#37][gr-37] está fusionado con texto grande, alto
  contraste y controles opcionales de teclado virtual. La vista previa Qt 6 de
  SDDM y los chequeos de controles AT-SPI pasaron localmente, pero no se
  registró completitud de tareas con lector de pantalla ni aceptación sobre
  imagen candidata.
- **Aceptación de runtime de PluginKit — BLOCKED.** Shell [#312][sh-312] tiene
  CI en verde para los slots públicos de PluginKit y widgets de escritorio,
  pero la carga en runtime, la persistencia al reiniciar la Shell y el
  comportamiento al desconectar/reconectar pantallas siguen sin verificarse.
  Mantené el PR en borrador hasta que pasen esos chequeos.
- **Línea base de rendimiento — FAIL.** Los números de arranque en frío y por
  superficie en el host de desarrollo están publicados en el
  [informe de shell 2026-10-21][sh-perf]. No fueron reproducidos por el arnés
  descartable de QA; no hay ninguna afirmación de rendimiento aprobada. Seguí
  [shell#47][sh-47] y [shell#228][sh-228].
- **Documentación y vidriera — PASS para las superficies publicadas.**
  HorneroOS/docs es dueño del contenido técnico canónico; el sitio web
  renderiza un commit revisado y fijado. Los PRs de Website
  [#148][web-148] y [#149][web-149] publican el marketplace y una captura en
  vivo de la estación de trabajo en el showroom. La captura no es evidencia de
  instalación, compatibilidad de hardware ni release.
- **CI de gobernanza de repositorios — PASS.** El issue [#14][inst-14] de
  installer está cerrado tras [installer#15][inst-15], que alineó el pin de
  gobernanza. La corrección de evidencia del PR #24 de installer y su merge a
  main pasaron CI en las corridas [40071650350][inst-run1] y
  [40071650330][inst-run2]. Esto no dice nada sobre la aceptación de
  instalación de la ISO.
- **Aceptación de QA — FAIL.** El checklist de preview30 todavía tiene gates
  sin marcar de VM con pin exacto y de Hornero QA. Mirá el
  [checklist del candidato][p30-chk] y los issues de QA [#16][qa-16],
  [#18][qa-18] y [#19][qa-19]. La última corrida exitosa de CI rápida de QA es
  [39957901125][qa-run] del 2026-10-23 (Ruff, Mypy, pytest, matriz de
  escenarios, lint de Markdown). Prueba código del repositorio, no una VM
  candidata ni una ISO instalada.

## Comandos de evidencia

Corré estos comandos desde la raíz del repositorio nombrado. Adjuntá la salida
del comando y un enlace a la corrida o paquete de evidencia al cambiar un gate.
Usá los SHAs candidatos exactos de arriba. Estos comandos ayudan a reunir
evidencia; solo el alcance de aceptación dentro del gate determina PASS.

### Composición

Corré en `HorneroOS/hornero`:

```sh
python3 scripts/check-manifests.py
python3 scripts/check-pins.py
python3 -m pytest tests/ -q
./scripts/compose.sh --yes
```

Esto valida la composición. No construye ni arranca una ISO.

### Construcción de ISO y escritorio instalado

En `HorneroOS/installer`, lo siguiente construye la imagen provisional de
Calamares únicamente en una VM dedicada y descartable de Arch, contra un
checkout limpio y con el proceso de aceptación de Panda Foss. No reemplaza la
aceptación del instalador oficial de Panda. No corras esto en el host de
mantenimiento. Usá directorios de trabajo y salida nuevos y separados para cada
compilación. Reservá 40 GiB para trabajo y 12 GiB para salida (52 GiB si
comparten un sistema de archivos):

```sh
run_dir="$(sudo mktemp -d /mnt/build/hornero-XXXXXX)"
sudo env VJOBS=2 ./scripts/build-iso.sh \
  --work "${run_dir}/work" \
  --output "${run_dir}/output"
```

En `HorneroOS/qa`:

```sh
uv run hornero-qa list
uv run hornero-qa run smoke/desktop-ready
uv run hornero-qa inspect <run-id>
```

El escenario actual valida una imagen lista. QA#19 debe agregar y aceptar la
matriz de instalación a primer arranque antes de que esto pruebe una ISO
instalada.

El siguiente chequeo histórico en tiempo de ejecución sobre la imagen en vivo
se corrió el 2026-10-23. Mirá el nuevo [registro de validación R11][r11-val]
para evidencia actual. Para reproducir el chequeo histórico en un guest
descartable, usá DNS funcional y corré:

```sh
getent ahostsv4 archive.archlinux.org
curl -I --connect-timeout 6 archive.archlinux.org
pacman -Q qt6-base calamares
calamares
```

La prueba del 2026-10-23 resolvió el mirror a `49.12.124.107` y recibió HTTP
301. Los paquetes informaron `qt6-base 6.11.2-3` y `calamares 3.4.3-1`; el
último comando informó que el binario de Calamares requiere `Qt_6.12`, que la
biblioteca Qt en vivo no proveía en esa imagen. Esto registra la
incompatibilidad de runtime superada y no es un aprobado de aceptación de
instalación.

### Compositores

En `HorneroOS/qa`, corré ambos escenarios contra la imagen candidata:

```sh
uv run hornero-qa run smoke/desktop-ready
uv run hornero-qa run compositors/niri-desktop-baseline
```

Niri sigue siendo experimental hasta que su escenario pase en el candidato.

### Integridad de paquetes

En `HorneroOS/hornero`:

```sh
./scripts/test-signing.sh
./scripts/verify-release.sh <asset> [signature]
```

El primer comando usa una clave descartable. El segundo es el chequeo de
release; la clave pública de producción está commiteada en
`packaging/keys/hornero-release.pub.asc` en HorneroOS/hornero.

### Actualizaciones y vuelta atrás

Corré `horneroctl package check --json` en el sistema destino. Es estado de
solo lectura. No existe ningún comando de vuelta atrás del sistema de punta a
punta mientras `hornero#179` y `#62` sigan abiertos.

### Hermes

En un sistema de pruebas aprovisionado, corré
`horneroctl assistant gateway status --json` y
`qs ipc call companion status`. Esto es evidencia solo de host de desarrollo.
No pongas credenciales de proveedor en fixtures de QA ni logs de CI.

### Ciclo de vida y catálogo de plugins

En `HorneroOS/plugins`:

```sh
python3 scripts/validate_plugins.py
python3 scripts/gen_catalog.py --check
```

En la imagen candidata:

```sh
horneroctl plugin catalog --json
horneroctl plugin catalog install hornero-pomodoro --dry-run
qs ipc call plugins status
```

Un listado del catálogo o un dry run exitoso no prueban que el plugin haya
cargado en la imagen de release.

### Seguridad de bloqueo y sesión

En `HorneroOS/qa`:

```sh
uv run hornero-qa run lock/lock-keyboard
uv run hornero-qa run regressions/shell-24-lock-after-hyprlock
```

El escenario de recuperación ante caídas debe pasar en el candidato antes de
que pueda aprobar el gate.

### Accesibilidad

En `HorneroOS/shell`:

```sh
python3 -m pytest tests/test_a11y_names.py tests/test_lock_a11y.py \
  tests/test_appearance_a11y.py tests/test_shared_controls_a11y.py \
  tests/test_pane_rows_a11y.py
```

En `HorneroOS/qa`, corré también `uv run hornero-qa run lock/lock-keyboard`.
Las pruebas estáticas y el smoke de bloqueo no son la pasada faltante de
completitud de tareas con lector de pantalla.

### Rendimiento

En `HorneroOS/qa`, corré `uv run hornero-qa run perf/baseline`. En
`HorneroOS/shell`, corré:

```sh
./scripts/perf-baseline.sh --samples 5 --interval 1 --format json
```

El comando de la Shell mide el host de desarrollo. Solo la corrida en imagen QA
puede respaldar afirmaciones de rendimiento de release.

### Documentación

En `HorneroOS/docs`, corré `npx --yes markdownlint-cli2 '**/*.md'` y
`python3 scripts/check-horneroctl-refs.py`. Ambos deben pasar en el mismo
commit de docs fijado por el sitio web.

### QA y release candidata

En `HorneroOS/hornero`, corré `tests/vm/smoke.sh`. En `HorneroOS/qa`, corré
`uv run hornero-qa run smoke/desktop-ready`. Ambas corridas deben identificar
los pines candidatos exactos y adjuntar su evidencia. El script de Hornero
requiere KVM y una imagen base preparada; `VM-SMOKE-SKIP` no es un aprobado.
Solo cuenta un `VM-SMOKE-PASS` de pin exacto más la evidencia QA del candidato.
Una corrida previa o de `main` mutable no cuenta.

## Reglas

- Nunca publiques una ISO, captura, benchmark o afirmación de compatibilidad
  salvo que su gate esté en PASS con evidencia enlazada para el candidato
  actual.
- Los gates del instalador se mueven únicamente con la aceptación de Panda
  Foss. HorneroOS no se auto-certifica el instalador.
- Mantené las afirmaciones PASS acotadas a lo que prueba el comando. Una
  prueba smoke, prueba sobre código, observación en host de desarrollo o CI de
  composición en verde no reemplazan una corrida de aceptación de una ISO de
  release instalada.
- Actualizá este archivo en el mismo PR que cambia el estado o evidencia de un
  gate.

[candidate]: https://github.com/HorneroOS/hornero/blob/main/manifests/v0.2.0-preview30.yaml
[candidate-pointer]: https://github.com/HorneroOS/hornero/blob/main/manifests/candidate
[p30-chk]: https://github.com/HorneroOS/hornero/blob/main/releases/v0.2.0-preview30-checklist.md
[r11-val]: https://github.com/HorneroOS/installer/blob/main/docs/r11-validation.md
[inst-11]: https://github.com/HorneroOS/installer/issues/11
[qa-19]: https://github.com/HorneroOS/qa/issues/19
[h-180]: https://github.com/HorneroOS/hornero/issues/180
[h-275]: https://github.com/HorneroOS/hornero/pull/275
[h-216]: https://github.com/HorneroOS/hornero/pull/216
[h-179]: https://github.com/HorneroOS/hornero/issues/179
[h-62]: https://github.com/HorneroOS/hornero/issues/62
[h-252]: https://github.com/HorneroOS/hornero/pull/252
[h-253]: https://github.com/HorneroOS/hornero/pull/253
[h-191]: https://github.com/HorneroOS/hornero/issues/191
[h-278]: https://github.com/HorneroOS/hornero/pull/278
[df-383]: https://github.com/ulises-jeremias/dotfiles/pull/383
[sh-269]: https://github.com/HorneroOS/shell/pull/269
[plugins-repo]: https://github.com/HorneroOS/plugins
[h-214]: https://github.com/HorneroOS/hornero/pull/214
[sh-268]: https://github.com/HorneroOS/shell/pull/268
[pl-6]: https://github.com/HorneroOS/plugins/pull/6
[h-273]: https://github.com/HorneroOS/hornero/pull/273
[sh-309]: https://github.com/HorneroOS/shell/pull/309
[web-mp]: https://www.horneroos.com/marketplace
[sh-251]: https://github.com/HorneroOS/shell/issues/251
[sh-318]: https://github.com/HorneroOS/shell/pull/318
[sh-321]: https://github.com/HorneroOS/shell/pull/321
[run-1]: https://github.com/HorneroOS/shell/actions/runs/40129324336
[run-2]: https://github.com/HorneroOS/shell/actions/runs/40131614836
[run-3]: https://github.com/HorneroOS/shell/actions/runs/40134380723
[run-4]: https://github.com/HorneroOS/shell/actions/runs/40136330518
[run-5]: https://github.com/HorneroOS/shell/actions/runs/40138798423
[run-6]: https://github.com/HorneroOS/shell/actions/runs/40140797051
[run-7]: https://github.com/HorneroOS/shell/actions/runs/40142966617
[run-8]: https://github.com/HorneroOS/shell/actions/runs/40145172696
[run-9]: https://github.com/HorneroOS/shell/actions/runs/40147893239
[run-10]: https://github.com/HorneroOS/shell/actions/runs/40150595999
[run-11]: https://github.com/HorneroOS/shell/actions/runs/40152601907
[sh-251-cmt]: https://github.com/HorneroOS/shell/issues/251#issuecomment-6392198620
[sh-24]: https://github.com/HorneroOS/shell/issues/24
[qs-1054]: https://github.com/quickshell-mirror/quickshell/issues/1054
[sh-24-cmt]: https://github.com/HorneroOS/shell/issues/24#issuecomment-6387620388
[sh-257]: https://github.com/HorneroOS/shell/issues/257
[sh-221]: https://github.com/HorneroOS/shell/issues/221
[sh-a11y]: https://github.com/HorneroOS/shell/blob/main/docs/a11y-audit-2026-10-21.md
[sh-310]: https://github.com/HorneroOS/shell/pull/310
[gr-37]: https://github.com/HorneroOS/greeter/pull/37
[sh-312]: https://github.com/HorneroOS/shell/pull/312
[sh-perf]: https://github.com/HorneroOS/shell/blob/main/docs/perf-baselines/2026-10-21-cold-start.md
[sh-47]: https://github.com/HorneroOS/shell/issues/47
[sh-228]: https://github.com/HorneroOS/shell/issues/228
[web-148]: https://github.com/HorneroOS/website/pull/148
[web-149]: https://github.com/HorneroOS/website/pull/149
[inst-14]: https://github.com/HorneroOS/installer/issues/14
[inst-15]: https://github.com/HorneroOS/installer/pull/15
[inst-run1]: https://github.com/HorneroOS/installer/actions/runs/40071650350
[inst-run2]: https://github.com/HorneroOS/installer/actions/runs/40071650330
[qa-16]: https://github.com/HorneroOS/qa/issues/16
[qa-18]: https://github.com/HorneroOS/qa/issues/18
[qa-run]: https://github.com/HorneroOS/qa/actions/runs/39957901125
