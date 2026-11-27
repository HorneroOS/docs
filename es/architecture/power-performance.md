# Energía y rendimiento

Cómo se *siente* el escritorio: qué tan rápido llega al primer cuadro después
del login, qué tan silencioso queda en reposo y si las interacciones siguen
fluidas mientras la shell hace trabajo real.

## Una regla

Un cambio de rendimiento entra con un número o no entra. Medí, cambiá, volvé a
medir; dejá el cambio solo si el número se movió. Cerrá tickets con mediciones,
no con teorías.

## La línea base (lo más barato, hacelo primero)

En una sesión de referencia limpia, registrá:

- login hasta la primera superficie pintada de la shell
- costo por cuadro de cada superficie en reposo, animando y reproduciendo audio
- memoria residente de cada proceso QML y demonio al iniciar sesión
- CPU en reposo y consumo eléctrico

Cómo hacerlo con lo que existe hoy: `systemd-analyze` para la cadena de
arranque, `horneroctl shell logs` para tiempos del lado de la shell y la suite
nativa `horneroctl apps performance` (`startup`, `memory`, `benchmark`,
`report`, `mode`). Lo que falta es la corrida de referencia comiteada: la
salida de `performance report` registrada en hardware de referencia y guardada
en el repositorio para que quienes revisan puedan verla — esa tabla es el
entregable, no una medición suelta.

Hecho significa: un script comiteado, línea base registrada en hardware de
referencia y números visibles en el repositorio (no en notas personales).

## Corridas de referencia (equipo documentado, filas fechadas)

Una fila por corrida de referencia, agregada al final y nunca sobrescrita. Son
resúmenes, no reportes crudos (`PERF_BASELINE.md` en shell mantiene los
reportes crudos fuera del repositorio). Los números describen solo al equipo
documentado — nunca son umbrales universales.

| Fecha | Shell | RSS | PSS | IPC | Capas | QML | Δ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-29 | #71 | ~635M | ~433M | ~27ms | 7 | 343 | 0 |

Fila 1: PR #71 de shell (merge `2b02392`), harness `scripts/perf-baseline.sh`,
estado estable en 24c / 15 GB / 1×1080p / qs 0.3.1-git. Fuente: el cuerpo del
PR (primera corrida en vivo).

Volvé a medir con el mismo harness en el mismo equipo antes y después de
cambios de rendimiento; mismo equipo, mismas condiciones, o la comparación no
vale.

## Presupuestos a defender

- Login en frío hasta primera superficie: no puede regresar sin un número que
  lo justifique.
- Costo en reposo: sin analizadores, pollers ni animaciones siempre encendidas
  cuando el escritorio está quieto; el trabajo caro se paga en el primer uso,
  no en el login.
- Costo de actualización: las operaciones de `horneroctl` quedan fuera del
  camino de cuadro; reconciliaciones pesadas (`doctor`, snapshots) nunca
  bloquean el login.

## Dónde viven los costos

- Parseo y compilación de QML al iniciar sesión, por superficie (shell,
  superficies tipo hub y pantalla de bloqueo lo pagan cada una).
- Singletons ansiosos que se inicializan antes de que haya algo visible.
- Análisis de fondos y generación de paletas en el camino de login.

El trabajo de implementación entra en [HorneroOS/shell][shell] y
[HorneroOS/hornero][hornero]; esta página es dueña de los números.

[shell]: https://github.com/HorneroOS/shell
[hornero]: https://github.com/HorneroOS/hornero
