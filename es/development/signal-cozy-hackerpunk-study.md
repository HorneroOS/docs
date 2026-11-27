# Signal: estudio Cozy Hackerpunk

> Traducción al español rioplatense de la
> [versión en inglés](../../development/signal-cozy-hackerpunk-study.md),
> que es la canónica.

- **Estado** — Dirección aceptada (2026-11-17) para
  [RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md),
  enmienda 4
- **Seguimiento** —
  [HorneroOS/.github#28](https://github.com/HorneroOS/.github/issues/28)
  (requisitos L1, L2, K4)
- **Audiencia** — colaboradores de shell, PluginKit, config, sitio web, marca
  y QA

La dirección en una línea: **Cozy Hackerpunk, retrofuturismo argentino,
computación personal.** Signal Bezel sigue siendo la estructura; suma una
lámpara cálida, detalles de lugar habitado y una voz tipográfica más afilada.
Es una evolución de
[Signal Visual Language](signal-visual-language.md), no un
reinicio.

> **Todas las imágenes de acá son renders conceptuales originales** (muestras
> HTML/CSS renderizadas en modo headless a 1920×1080, con fuentes en
> `assets/signal-cozy-hackerpunk/sources/`), rotuladas "CONCEPT RENDER", con
> valores de ejemplo y sin telemetría en vivo. No se descargó, calcó ni
> reutilizó ninguna obra de terceros.

## 1. La evidencia y sus límites

La referencia creativa es la serie animada argentina *Electro Andes*
(Bellolandia Studio). Se estudió **solo por sus principios**.

Lo que dicen realmente las fuentes públicas:

- La página del estudio describe una serie de fantasía 2D orientada a la
  familia, ambientada en "Arcadia Iruyana", un futuro de tecnología, colapso
  ambiental y herencia andina ([Bellolandia][bellolandia]). Da sinopsis y
  créditos, **no** paleta, iluminación ni tipografía.
- La prensa la presenta como "a cyberpunk ethno mythological action
  adventure horror story" ([80.lv][80lv]), con un aspecto comparado con
  *Cyberpunk: Edgerunners* y una sensación hip-hop / neón
  ([Cultura Geek][culturageek]).
- El escenario está inspirado en Iruya (Salta) y en el pueblo minero peruano
  de La Rinconada; el director compara el enfoque con una versión ficticia de
  una cultura "sin hacer una representación literal"; entre las referencias
  hay un "trashy future" y el neón; la banda sonora es *electro-folklore*
  del norte; Kiwi, el hacker, es llamado "el personaje más simpático"
  ([421.news][421news]).

No inspeccioné la obra gráfica en sí, y ninguna fuente describe su color ni su
iluminación. Cuando este estudio habla de calidez, lámparas y equipo con
huellas de uso, eso es **el brief del dueño del producto (2026-11-17)** y
nuestro propio criterio, no una afirmación sobre la serie. Los principios
transferibles que la evidencia sí respalda:

1. **Anclar el futuro en un lugar real.** La tecnología se lee a través de
   una región específica, no de una ciudad genérica. Para nosotros: la
   cultura gráfica industrial y de broadcast de Buenos Aires, paletas
   regionales argentinas, microcopy en español con voseo.
2. **Estilizar, nunca transcribir.** Una cultura se toma como una versión
   ficticia, no se copia de forma literal. Para nosotros: ningún motivo
   folklórico o andino trasladado a la interfaz; solo símbolos propios.
3. **Hackers simpáticos.** Las personas técnicas son cálidas y cercanas. Para
   nosotros: un escritorio que te saluda, con instrumentos que se pueden leer.
4. **Sonido e imagen comparten una misma cultura** (electro-folklore). Para
   nosotros: los temas de sonido y las paletas se crean en pareja más
   adelante (no en este tramo).
5. **Cyberpunk sin esterilidad.** El "trashy future" implica desgaste e
   improvisación: etiquetas escritas a mano, lámparas que no combinan, notas
   pegadas con cinta.

## 2. Lo que no debemos copiar

- El diseño, la apariencia, las siluetas, la ropa, los accesorios, los guiones
  de color, el logo o cualquier fotograma de Kiwi, y cualquier composición de
  la serie.
- Nombres y lugares de la serie como marca (Arcadia Iruyana, Montaña Negra),
  imaginería sagrada andina (figuras y gestos de Killa/Inti), motivos
  grabados.
- El neón sobre negro al estilo Edgerunners como valor por defecto.
- Cualquier cosa descargada del estudio o de la prensa. Nuestra mascota es
  Javi el Hornero (un personaje original, un pájaro hornero); sus estados se
  especifican en el requisito L8, no acá.

## 3. Diferencias respecto del Signal actual

- **Ánimo** — Signal (RFC 0001 + enmiendas): frontal de instrumento preciso;
  Cozy Hackerpunk: la misma precisión, en una habitación iluminada, donde
  alguien trabaja
- **Neutros** — Signal: grafito frío (Night), papel (Day); Cozy Hackerpunk:
  suma un anochecer carbón-berenjena cálido (Dusk); se conservan
  Night/Day/Contrast
- **Luz** — Signal: el ámbar es *vivo*; el glow tiene presupuesto; Cozy
  Hackerpunk: además un baño de lámpara y una luz superior interior suave
  (atmósfera), con alfas diminutos
- **Textura** — Signal: ninguna (plano, líneas finas); Cozy Hackerpunk: grano
  fino y viñeta opcionales, apagados en Alto Contraste y por accesibilidad
- **Rótulos** — Signal: eyebrows en mono; Cozy Hackerpunk: suma rótulos de
  "placa" grabados y acentos de microcopy tipo nota en papel
- **Voz** — Signal: neutral; Cozy Hackerpunk: cálida, rioplatense, breve; una
  voz neutra queda a un solo interruptor de distancia
- **Uso del color** — Signal: ámbar / cian / verde; Cozy Hackerpunk: suma
  ocasionalmente rosa/violeta como acento *raro* (terminal 5, etiquetas)

## 4. Comparación de tres direcciones coherentes

*Render conceptual eliminado (2026-11-20): Render conceptual: tres direcciones. Capturas reales: [Showroom](https://horneroos.com/showroom/).*

- **Encaja con Signal, extiende en vez de reemplazar** — A Bezel Cálido: 5;
  B Taller: 3; C Noche Norteña: 1
- **Comodidad durante todo el día** — A: 5; B: 3; C: 2
- **Distinto del cyberpunk genérico** — A: 4; B: 4; C: 2
- **GlowBudget y costo de rendimiento** — A: 5; B: 3; C: 1
- **Funciona con paletas derivadas del fondo de pantalla** — A: 5; B: 3;
  C: 3
- **Variantes Day / Alto Contraste** — A: 5; B: 3; C: 2
- **Encanto a primera vista** — A: 4; B: 5; C: 4

Las opciones:

- **A. Bezel Cálido (lámpara sobre el banco)** — Signal Bezel sin cambios de
  estructura; neutros cálidos, un baño de lámpara, luz interior suave, grano,
  tinta crema, señal ámbar cobre. La luz es una señal de instrumento, nunca un
  resplandor ambiental.
- **B. Taller (taller de radioaficionado)** — chapa pintada de verde oliva,
  etiquetas de papel, tornillos, biseles dobles. Encantador, pero con una
  textura skeuomórfica por superficie, pesado para sesiones largas y en
  pugna con las paletas derivadas del fondo de pantalla.
- **C. Noche Norteña (neón electro-folk)** — violeta/magenta/cian saturados
  con el glow como lenguaje. Lo más cercano al neón genérico que el brief
  rechaza e incompatible con el presupuesto de glow.

**Elegida: A, tomando de B y C** lo que sale barato: de B, la nota de papel
crema y el rótulo de placa grabada (tipografía, no textura); de C, un acento
raro rosa/violeta para etiquetas, el magenta de la terminal y momentos
especiales, nunca como color de superficie por defecto.

## 5. La dirección elegida

*Render conceptual eliminado (2026-11-20): Render conceptual: escritorio Signal Dusk. Capturas reales: [Showroom](https://horneroos.com/showroom/).*

### 5.1 Atmósfera emocional

Una noche tardía en el banco de trabajo: una lámpara de escritorio de un lado,
un resplandor cian del monitor del otro, instrumentos que dicen la verdad en
voz baja, una nota pegada en el bisel que te saluda. Cálido pero exacto;
encantador pero no infantil. Lo kawaii lo aporta la mascota y unos pocos
toques suaves, nunca la estructura.

### 5.2 Color (dirección de arte, no un sistema nuevo)

- Los mismos roles del RFC §3.1 y las mismas compuertas de contraste
  (`contrast-gates.json`). **No se agregan roles nuevos al esquema**: la
  calidez la aportan (a) una paleta curada nueva y (b) valores de atmósfera
  derivados de la paleta que esté activa (el `services/atmosphere.js` del
  shell deriva chips de lámpara y rubor a partir de la paleta, así que las
  paletas personalizadas y las de Chromatic también se calientan).
- **Signal Dusk** (`hornero-signal-dusk`, config): superficies
  carbón-berenjena `#14100F → #3B312E`, tinta crema `#F1E6D2`, señal ámbar
  cobre `#F29A4A`, indicio cian `#74C6E8`, fósforo `#93D79B`, rosa en la
  terminal. Pasa las compuertas compartidas (el par de texto más débil es
  4.98:1). Night, Day y Alto Contraste no cambian.
- Chromatic sigue derivando paletas desde los fondos de pantalla (RFC 0002);
  el sesgo cálido es un tema de política de Chromatic para quien tenga a su
  cargo las paletas, no una bifurcación.

*Render conceptual eliminado (2026-11-20): Render conceptual: paleta Dusk, contraste y roles tipográficos. Capturas reales: [Showroom](https://horneroos.com/showroom/).*

Medido en Dusk: `ink` ≥ 10.2:1 y `inkMuted` ≥ 6.2:1 sobre todas las
superficies, `signal` ≥ 5.7:1, `ruleStrong` ≥ 3.3:1 sobre `lifted`. `alert`
es 4.36:1 sobre `lifted` (la compuerta lo verifica sobre sunken hasta
raised): no pongas texto de alerta en los tooltips.

### 5.3 La tipografía como activo premium

Plex se queda, porque es OFL-1.1, está empaquetada en Arch (`ttf-ibm-plex`) y
tiene los pesos, un corte condensado y cifras tabulares verdaderas. Se
evaluaron y descartaron alternativas con licencia abierta (Space Grotesk,
JetBrains Mono, Big Shoulders): cada una agrega una segunda superfamilia para
distribuir y probar a cambio de una ganancia marginal. Roles:

- **UI** — IBM Plex Sans 13; uso: texto cotidiano
- **Readout** — IBM Plex Mono, `tnum`; uso: números, código, temporizadores
- **Eyebrow** — IBM Plex Mono 11, mayúsculas, +8 %; uso: rótulos de sección
  y de canal (ya existe)
- **Plate** — IBM Plex Sans Condensed SemiBold, mayúsculas, +14 %; uso:
  placas grabadas de modo y de estado (nuevo)
- **Display** — IBM Plex Sans Condensed Light, −2 % de espaciado; uso: reloj,
  bloqueo, greeter

Reglas: como máximo cuatro tratamientos por pantalla, cifras tabulares donde
sea que un valor cambie, tamaños display un pelo más ajustados, placas solo
sobre enumerados (modo, estado), nunca sobre oraciones.

### 5.4 Material y luz

- Las superficies siguen planas, con líneas finas y radio chico (RFC: nada de
  píldoras gigantes). El aspecto "Cozy" existente escala el redondeo a 1.6;
  se recomienda limitar el radio efectivo a `small × 2` en barras y tarjetas
  para que lo suave no termine en píldora (mirá §8).
- La luz cálida son tres alfas pequeños (baño de lámpara, resalte superior
  interior suave, viñeta) más grano opcional, todos con techos duros y
  deslizadores para el usuario.
- Indicadores: un LED chico por cada cosa viva, solo con datos reales. El glow
  se mantiene dentro del presupuesto del RFC §3.2 (≤ 3 elementos con glow,
  blur ≤ 4 px, alfa ≤ 40 %), apagado en Day, Alto Contraste, Gaming y en
  Cockpit Clear.

### 5.5 Movimiento

Coreografía sin cambios (RFC §3.6, lenguaje visual §11). Agregados: los
cambios de modo funden la lámpara en 400–600 ms; nada se repite en bucle
salvo la actividad real; el **movimiento reducido** cambia cada fundido por un
estado instantáneo y desactiva el centelleo del grano (el grano es estático de
todos modos); el **bajo consumo** descarta primero el grano, la viñeta y el
glow.

### 5.6 Restricciones de accesibilidad y rendimiento

- Las compuertas de contraste de texto no cambian; las capas de atmósfera van
  debajo del texto y no pueden reducir el contraste de texto medido (techo de
  viñeta 0.30, lámpara 0.20).
- El grano y la viñeta son una única textura o un solo degradado, no shaders;
  se apagan en Alto Contraste; el usuario puede desactivarlos (AGENT-RULES
  §6).
- El microcopy nunca lleva información que no lleve también un tooltip o una
  etiqueta.
- El rosa/violeta nunca es el único portador de significado.

## 6. Oportunidades de personalización por plugins

- Los plugins leen la atmósfera a través de los mismos tokens (lámpara, luz
  suave, grano) para que los widgets combinen con la habitación; no pueden
  definir su propio glow fuera del presupuesto (shell#600 ya encamina los
  glows de plugins por la intensidad).
- Un manifiesto de **Look pack** (paleta + atmósfera + escala tipográfica +
  skin de la mascota + voz del microcopy) instalable como una sola extensión,
  con vista previa antes de aplicarlo.
- Los widgets de instrumentos (placa de reloj, VU, osciloscopio) declaran
  lecturas `tabular` y el estilo de placa mediante ajustes tipados.
- Temas de sonido emparejados con los Look packs (más adelante).

## 7. Narrativa del sitio web

Empezar por la habitación, no por la lista de funciones: un hero cálido (el
escritorio Dusk en una captura real cuando esté disponible), la línea "Pasá,
sentate.", después la historia de los instrumentos (datos reales, nada
simulado), y por último la personalización como "armá tu propio banco de
trabajo". Se mantienen las etiquetas de publicado / experimental /
planificado. Usar renders originales marcados como CONCEPT hasta que existan
capturas del host. Fuentes autoalojadas (Plex), sin pedidos a terceros,
imágenes con tamaños explícitos, oscuro y claro.

## 8. Decisiones y puntos abiertos

- Implementado ahora: `hornero-signal-dusk` en config; este estudio; la
  enmienda 4 del RFC 0001; las muestras. La capa de atmósfera del shell
  (lámpara, luz suave, viñeta, grano, presets de Look, microcopy) ya está en
  una rama separada del shell (`feat/cozy-atmosphere`) y a propósito no se
  duplica acá.
- Ajustes recomendados para esa capa: limitar el redondeo del aspecto "Cozy"
  (§5.4); desactivar automáticamente el grano y la viñeta en Alto Contraste y
  en bajo consumo; agregar el estilo de rótulo Plate (§5.3) como un pequeño
  componente `Plate` con un control de espaciado.
- No se decide acá: los estados de Javi (L8), la dirección de arte del
  bloqueo, el greeter y el instalador, la política de sesgo cálido de
  Chromatic, el emparejamiento de sonido.

[bellolandia]: https://www.bellolandia.com/work/electro-andes
[80lv]: https://80.lv/articles/electro-andes-cyberpunk-ethno-mythological-horror-animated-show
[culturageek]: https://culturageek.com.ar/electro-andes-como-sera-el-anime-argentino-con-estetica-cyberpunk-que-promete-romperla-toda/
[421news]: https://www.421.news/en/electro-andes-animated-series/
