# Incidente: caída del bloqueo de sesión tras reiniciar la shell (2026-10-20)

> Traducción al español rioplatense de la
> [versión en inglés][canonical], que es la canónica.

**Severidad:** Alta (reinicio forzado, sin pérdida de datos)
**Estado:** Mitigado; la resiliencia a largo plazo se sigue por separado
**Seguimiento:** HorneroOS/shell#255 (cerrado), HorneroOS/shell#257 (abierto)

## Resumen

El 2026-10-20 el host de desarrollo se reinició dos veces luego de que la sesión
gráfica se bloqueara mientras Quickshell se detenía o reiniciaba para un
despliegue. Cuando el proceso de Quickshell murió, su superficie `WlSessionLock`
murió con él, Hyprland cayó a su pantalla de recuperación de bloqueo caído y la
única salida segura fue reiniciar desde una TTY. Nunca se salteó la contraseña
de usuario ni se perdieron datos.

## Análisis de causa raíz

- La shell de Hornero es dueña del bloqueo de sesión dentro del proceso:
  `modules/lock/Lock.qml` crea un único `WlSessionLock` mediante
  `Lock.requestLock()` (ver `docs/LOCKING.md` en HorneroOS/shell).
- Detener o reiniciar Quickshell destruye entonces la superficie de bloqueo de
  una sesión ya bloqueada. El compositor no puede recrear esa superficie desde
  un proceso nuevo, así que muestra el respaldo de pantalla de bloqueo caída y
  la sesión queda irrecuperable en el lugar.
- Factor contribuyente: el reinicio se emitió durante esperas largas de CI
  mientras la sesión se había bloqueado por inactividad, por lo que el estado de
  bloqueo no era obvio del lado del operador.
- Brecha de detección hallada durante el arreglo: `LockedHint` de logind sigue
  en `no` bajo el bloqueo de la shell en Hyprland, y puede no existir ningún
  proceso `hyprlock` en ejecución (el bloqueo es la superficie propia de la
  shell). Ninguna de las dos señales por sí sola sirve para concluir "no
  bloqueado".

## Arreglo publicado

1. `horneroctl shell stop|restart` ahora rechaza ejecutarse mientras la sesión
   está bloqueada (HorneroOS/hornero PR #197). `--dry-run` sigue permitido para
   poder inspeccionar el plan.
2. La sonda autorizada de bloqueo es la propia shell:
   `qs ipc call lock isLocked`, probada primero contra el `QS_CONFIG_PATH` de
   quien llama y luego contra el directorio de configuración resuelto de la
   shell (HorneroOS/hornero PR #199). `LockedHint` de logind y una sonda de
   proceso `hyprlock` quedan solo como respaldos; todas las sondas fallan
   abiertas para que un error de sonda nunca bloquee un reinicio desbloqueado.
3. Prueba en vivo en el host afectado: con el bloqueo de la shell activo, el
   `horneroctl` recompilado rechazó `shell stop --yes` con "refusing to stop the
   shell while the session is locked" y el bloqueo siguió activo.
4. Regla operativa documentada en `docs/LOCKING.md` de HorneroOS/shell: nunca
   detener ni reiniciar Quickshell mientras está bloqueado; desbloquear primero.
   La recuperación de un bloqueo ya caído es solo por TTY y está documentada
   ahí.

## Qué no funcionó

- Confiar en `LockedHint` de logind: informó `no` mientras el bloqueo de la
  shell estaba visiblemente activo.
- Confiar en una sonda de proceso `hyprlock`: el bloqueo pertenece al proceso de
  la shell, así que en esta configuración no existe ningún proceso `hyprlock`.

## Riesgo remanente

Si el proceso de la shell cae de forma espontánea mientras está bloqueado (OOM,
segfault), todavía puede ocurrir la misma pantalla de respaldo del compositor;
ningún cambio de QML ni de CLI puede reparar un bloqueo de compositor huérfano a
posteriori. HorneroOS/shell#257 sigue la evaluación de opciones de resiliencia
(por ejemplo un supervisor externo mínimo de bloqueo) sin debilitar el modelo de
seguridad del bloqueo.

## Lista de prevención

- Desbloqueá la sesión antes de cualquier `horneroctl shell stop|restart`.
- Confiá en el rechazo integrado; no agregues salteos estilo `--force`.
- Después de cualquier reinicio de la shell en un host, confirmá con
  `qs ipc call lock isLocked` y `horneroctl shell status --json`.
- Mantené límites `MemoryMax` en compilaciones locales para que un build no
  pueda matar por OOM al proceso de la shell con la sesión bloqueada.

[canonical]: ../../development/incident-2026-10-20-session-lock-crash.md
