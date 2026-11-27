# Aseguramiento de calidad e ingeniería de releases

> Traducción al español rioplatense de la
> [versión en inglés](../../development/quality-and-releases.md), que es la
> canónica.

Esta página es la referencia técnica de cómo se prueba, firma y publica
HorneroOS. Las páginas de producto describen qué hace HorneroOS; esta página
explica cómo sabemos que funciona y dónde vive la evidencia de cada afirmación.

A propósito no registra el estado de los gates por release. El estado pertenece
a las listas de verificación por release en
[HorneroOS/hornero/releases][releases], que se escriben una sola vez por
release y nunca se editan después.

## Clases de evidencia

Cada afirmación de aceptación en HorneroOS lleva una de cuatro etiquetas. No son
intercambiables:

- `AUTOMATED-VERIFIED`: un chequeo determinístico o un escenario gráfico se
  ejecutó y registró el resultado.
- `SCREENSHOT-VERIFIED`: una persona o revisor inspeccionó una captura real del
  sistema en ejecución.
- `USER-VERIFIED`: quien mantiene el proyecto informa que funciona en hardware
  real en uso diario.
- `NOT SPECIFICALLY TESTED`: nadie tiene evidencia en un sentido ni en otro.
  Nunca se presenta como funcionando.

Un resultado en máquina virtual nunca es evidencia de hardware físico, y una
captura sola nunca hace pasar un escenario: el runner determinístico es la
autoridad, las capturas son evidencia de respaldo.

## Cómo funciona la aceptación gráfica

[HorneroOS/qa][qa] arranca las revisiones exactas fijadas de shell, config y
`horneroctl` — o la ISO exacta publicada — en máquinas virtuales QEMU/KVM
descartables, las conduce con entrada sintética y registra un paquete de
evidencia por corrida: resultado del escenario, capturas, hashes y las
revisiones fijadas del producto.

- Modelo de escenarios y taxonomía de fallos:
  [qa/docs/ARCHITECTURE.md][qa-arch]
- Registro generado de escenarios:
  [qa/docs/SCENARIO-MATRIX.md][qa-matrix]
- Gates de edición que fallan cerrado y nunca cambian por sí solos la madurez
  del producto:
  [STUDIO-ACCEPTANCE.md][qa-studio],
  [GAMING-ACCEPTANCE.md][qa-gaming],
  [BLUETOOTH-ACCEPTANCE.md][qa-bt]
- Registro de paridad en estación de trabajo física:
  [qa/docs/PELICANO-PARITY.md][qa-pelicano]

Las pruebas destructivas de instalación solo corren contra discos virtuales
descartables. Los chequeos en hardware físico ocurren después de la release, en
máquinas reales, y se registran con la clase de evidencia que realmente aplica.

## Ingeniería de releases

Una release de HorneroOS es una composición, no una instantánea de lo que había
instalado en una estación de trabajo:

1. Cada release se describe mediante un manifiesto inmutable en
   [HorneroOS/hornero][hornero] (`manifests/`), resuelto desde el catálogo
   canónico de ediciones. Los manifiestos etiquetados nunca se editan; una
   nueva composición implica una nueva release.
2. Los cinco gates de validación (chequeos de manifiestos, chequeos de pines,
   suites de pruebas, lint de documentación y el gate ejecutable de
   composición) deben pasar antes de etiquetar. El proceso está documentado en
   [hornero/docs/RELEASE_PROCESS.md][rel-proc].
3. Los paquetes se compilan en orden — `horneroctl`, config, shell, installer —
   y la ISO se construye en un entorno de compilación descartable, nunca sobre
   los discos de una estación de trabajo de desarrollo.
4. La ISO final exacta se instala en VMs descartables (Desktop, Studio y Gaming)
   y se ejercita en el primer arranque antes de publicar nada.
5. Los artefactos se firman con la clave de releases de HorneroOS
   `FCFBEE43925AB5429362278AE59EAB44AA2498DC`. La distribución de claves y el
   paso humano de firma están documentados en
   [hornero/docs/RELEASE_SIGNING.md][rel-sign]; la clave pública viene en el
   repositorio en `packaging/keys/hornero-release.pub.asc`, así que la
   verificación nunca depende de un keyserver.
6. Cada release publica su ISO, suma SHA-256, firma desacoplada y un checklist
   que registra qué pasó, qué se arrastra de antes y qué sigue sin probar. El
   índice derivado es [releases/LEDGER.md][ledger].

## Verificá una descarga por tu cuenta

La [página de instalación][install] imprime los comandos junto a la descarga. En
resumen: comprobá el SHA-256 contra el `.sha256` publicado, importá la clave
pública desde el repositorio, verificá el `.sig` desacoplado y confirmá la
huella de arriba. Una copia alterada debe fallar la verificación — ese caso
negativo forma parte de cada checklist de release.

## Reproducí las pruebas

Quien contribuya puede correr el mismo pipeline de evidencia de forma local:

- Chequeos por cambio acordes al riesgo: mirá [Pruebas](testing.md).
- Escenarios gráficos: cloná [HorneroOS/qa][qa] y seguí el inicio rápido de su
  README (`doctor`, `list`, `run`, `inspect`, `studio-gate`). Los carriles
  gráficos necesitan un host con KVM; no corren en runners estándar alojados
  por GitHub.
- Integridad del sitio web y la documentación: el build del sitio corre
  chequeos de verdad de releases, sincronización de datos, paridad i18n y
  enlaces internos, para que el texto público no pueda desviarse en silencio de
  los datos canónicos de release.

[releases]: https://github.com/HorneroOS/hornero/tree/main/releases
[qa]: https://github.com/HorneroOS/qa
[qa-arch]: https://github.com/HorneroOS/qa/blob/main/docs/ARCHITECTURE.md
[qa-matrix]: https://github.com/HorneroOS/qa/blob/main/docs/SCENARIO-MATRIX.md
[qa-studio]: https://github.com/HorneroOS/qa/blob/main/docs/STUDIO-ACCEPTANCE.md
[qa-gaming]: https://github.com/HorneroOS/qa/blob/main/docs/GAMING-ACCEPTANCE.md
[qa-bt]: https://github.com/HorneroOS/qa/blob/main/docs/BLUETOOTH-ACCEPTANCE.md
[qa-pelicano]: https://github.com/HorneroOS/qa/blob/main/docs/PELICANO-PARITY.md
[hornero]: https://github.com/HorneroOS/hornero
[rel-proc]: https://github.com/HorneroOS/hornero/blob/main/docs/RELEASE_PROCESS.md
[rel-sign]: https://github.com/HorneroOS/hornero/blob/main/docs/RELEASE_SIGNING.md
[ledger]: https://github.com/HorneroOS/hornero/blob/main/releases/LEDGER.md
[install]: https://www.horneroos.com/install
