# Extensiones

Las extensiones suman widgets, elementos de barra, resultados del lanzador y
paneles al escritorio. En **Centro de control > Extensions** explorás el
catálogo oficial y las instalás, actualizás, revertís, quitás, activás y
desactivás. No hace falta una terminal.

> **Development.** Esta página describe la tienda de Extensions en la rama
> `main` de Shell junto con los cambios de horneroctl y del catálogo que la
> acompañan (noviembre de 2026). El recorrido completo se probó con una
> extensión de prueba en una ejecución offscreen de la página real; todavía no
> se revisó en un escritorio físico, y los textos y la disposición pueden
> cambiar.

## Qué puede hacer una extensión

Una extensión activada corre como vos, sin sandbox. Puede hacer todo lo que
puede tu cuenta de usuario. El catálogo lista lo que cada extensión *declara*
usar, y Hornero lo muestra antes de instalar, pero esas declaraciones son un
texto para revisar: nada las hace cumplir. Activá solo extensiones en las que
confiás.

Instalar y activar son pasos separados a propósito:

- **Instalar** copia los archivos de la extensión después de compararlos con el
  hash SHA-256 del catálogo. No se ejecuta nada.
- **Activar** la ejecuta. Este es el paso que necesita tu confianza.

## Explorar el catálogo

El catálogo aparece debajo de tus extensiones instaladas. Cada tarjeta
muestra:

- **Firmado por**: Quién respalda el código. Las extensiones oficiales las
  revisa HorneroOS y quedan fijadas a un commit y a un hash SHA-256.
- **Estado**: Disponible, Instalada o *Actualización disponible: 1.0.0 → 1.1.0*.
- **Lo que declara usar**: Una línea por programa que puede ejecutar, host de
  red al que se puede conectar, datos compartidos que lee (por ejemplo el uso de
  CPU o el reloj) y configuración que guarda. Los programas y hosts vienen con
  el motivo, como "Lista tus contenedores con podman ps (solo lectura)".
- **Historial**: El cambio más nuevo; **Más** muestra el historial completo, la
  compatibilidad y los hashes.
- **Captura**: Una captura del catálogo, comparada con su hash antes de
  mostrarse.

La búsqueda filtra el catálogo por nombre, autor, categoría o ubicación.

![Ajustes, página Extensions. Un aviso explica que las extensiones
activadas se ejecutan con tu usuario y sin sandbox. Debajo hay una
tarjeta instalada que muestra su estado, un botón para activarla,
otro para actualizarla y uno para
quitarla.](https://www.horneroos.com/captures/cap-cc-07.png)

*Ajustes → Extensions: primero el aviso de confianza, después cada
extensión con su estado y acciones. Captura real del escritorio en el
equipo del maintainer, 19 de noviembre de 2026.*

## Instalar, actualizar, revertir, quitar

Los nombres de los botones siguen el idioma del shell; acá aparecen como se
ven con el shell en español.

Cada acción lleva dos clics. El primero te cuenta en palabras simples qué va
a pasar; el segundo lo hace. **Cancelar** la deshace antes de empezar.

- **Instalar…** y después **Confirmar instalación**: Copia los archivos
  verificados. La extensión queda apagada.
- **Actualizar…** y después **Confirmar actualización**: Reemplaza los archivos
  por la versión del catálogo y guarda la actual. Si estaba activada, sigue
  activada.
- **Revertir…** y después **Confirmar reversión**: Restaura la versión anterior
  guardada. Solo aparece después de una actualización.
- **Quitar…** y después **Confirmar quitar**: Borra los archivos, la versión
  anterior guardada y el registro de instalación. Su configuración se conserva,
  así que al reinstalarla vuelve.
- **Activar…** y después **Confirmar activación**: Ejecuta la extensión.

Mientras una acción corre, una franja arriba de la página dice qué está
pasando y hace cuánto, por ejemplo *Instalando Hornero Pomodoro… descargando
el catálogo, verificando SHA-256, validando y copiando · 3 s*. El resultado
aparece en la tarjeta. Si algo falla, la tarjeta dice qué salió mal y qué
hacer, por ejemplo "El catálogo cambió mientras lo leías. Actualizalo y revisá
la versión nueva." Una acción fallida nunca cambia el resto del escritorio.

Instalar y actualizar usan exactamente la versión del catálogo que estabas
leyendo. Si el catálogo cambió entretanto, Hornero se niega y te pide
actualizarlo, así nunca recibís código que no revisaste.

## Costo

Las extensiones instaladas muestran cuánto tardaron en cargar (por ejemplo
*Carga 42 ms*). **Detalles** suma el costo medido de los datos compartidos que
leen, como "system: 0.02% de un núcleo (2 s, 0.4 ms, compartido entre 2)".

Hornero no muestra un número de CPU o memoria por extensión. Todas corren
dentro del único proceso del shell, así que no hay una forma honesta de
repartirlo, y la página lo dice en lugar de adivinar.

## Preferencias

Al lado de **Actualizar catálogo**:

- **Cargar al abrir** (activado por defecto): carga el catálogo al abrir la
  página. Si lo apagás, abrir Extensions no hace ningún pedido de red; usá
  **Actualizar catálogo** cuando quieras explorar.
- **Mostrar costo** (activado por defecto): muestra tiempos de carga y costos.
- **Idioma de la tienda**: *Idioma del shell* (por defecto), *English* o
  *Español* para las líneas de permisos, las indicaciones y el progreso del
  catálogo.

## Desde una terminal

La página ejecuta los mismos comandos que podés correr vos, por ejemplo
`horneroctl plugin catalog install hornero-pomodoro --dry-run`. Sumá `--json` a
cualquiera para obtener una salida legible por máquinas. Las claves JSON, los
códigos de salida y los códigos de error están en el
[contrato JSON del ciclo de vida de plugins](https://github.com/HorneroOS/hornero/blob/main/docs/PLUGIN_LIFECYCLE_JSON.md)
de horneroctl (en inglés).

## Agent Deck: suscripciones de agentes de código

**Hornero AI Usage** (Agent Deck) vigila los agentes de código en los que ya
iniciaste sesión —Claude Code, Codex, Muse Code, Cursor y OpenCode— y
muestra las ventanas de cuota reales, los restablecimientos y el plan de cada
suscripción junto a la actividad de tokens de esta máquina. No hay nada que
registrar: activás la extensión y los agentes que Hornero encuentra aparecen
solos.

- La **barra** muestra la cuota más justa que te queda; al hacer clic se ven
  todas las cuentas. El panorama completo está en la solapa **Agentes** del
  Dashboard, junto a Media y Performance (la solapa viene de la extensión y
  desaparece cuando la desactivás).
- Una cuota se muestra solo cuando su proveedor la reporta. **Desconocida
  nunca significa 0% usado**, los datos viejos lo dicen, y las cifras de toda
  la cuenta nunca se suman a la actividad de esta máquina. No hay límites,
  restablecimientos ni costos inventados.
- Las sesiones quedan como están: las comprobaciones corren de solo lectura
  dentro de `horneroctl`, con la sesión que cada herramienta ya guardó. Nada
  se vuelve a cargar, refrescar ni cambiar, no se hace ninguna llamada al
  modelo solo para medir, y la extensión nunca toca credenciales ni la red.
  Comprobalo a mano cuando quieras con `horneroctl agent usage`.

## Dev Pulse: actividad de desarrollo en GitHub

**Hornero Dev Pulse** (`hornero-github-stats`) muestra lo que estuviste
construyendo: contribuciones que GitHub reconoce, pull requests creados
y mergeados, issues, revisiones y una bandeja accionable (PRs abiertos,
pedidos de revisión, issues asignados, checks fallando), con una
comparación opcional junto a Agent Deck. Nada que configurar: reusa la
sesión de GitHub CLI que ya tenés.

- Instalá `gh` una vez (`sudo pacman -S github-cli`) e iniciá sesión
  con `gh auth login`. Dev Pulse nunca pide un token, y ningún token
  se muestra, registra ni guarda — revisá los datos crudos cuando
  quieras con `horneroctl github status`, `horneroctl github stats`
  y `horneroctl github inbox`.
- La **barra** muestra PRs abiertos, checks fallando y pedidos de
  revisión; el panel completo es la pestaña **Dev Pulse** del
  Dashboard. Ventanas de 7/30/90/365 días, más filtros opcionales de
  organización/repositorio en los ajustes de la extensión.
- Los números son reales o no están: las métricas desconocidas se
  omiten, nunca se ponen en cero, y los totales vienen de los conteos
  de GitHub por fecha real del evento. La comparación con Agent Deck
  solo ubica la actividad de IA y de GitHub en el mismo período —
  ningún pull request se atribuye a un agente solo por coincidencia
  temporal.
- Los reportes quedan locales: `horneroctl github export --format
  markdown --output report.md` (`--public-only` omite repositorios
  privados).

## Si una extensión rompe el escritorio

Usá **Activar modo seguro (recuperación)** arriba de Extensions. En modo
seguro no se carga ninguna extensión, así que podés desactivar o quitar la que
falla y volver a apagar el modo seguro. Para escribir tu propia extensión,
mirá la [guía de autoría de extensiones](../development/extensions.md).
