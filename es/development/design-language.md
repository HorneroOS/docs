# Lenguaje de diseño de HorneroOS

> Traducción al español rioplatense de la
> [versión en inglés](../../development/design-language.md), que es la canónica.

Esta guía es el punto de partida compartido para quienes diseñan o implementan
una interfaz de HorneroOS, incluido el instalador gráfico (Calamares). Reúne la
dirección a nivel de producto y apunta al repositorio dueño de cada regla
concreta. No reemplaza esos contratos de implementación ni crea una segunda
copia de sus valores cambiantes de tokens.

## Estado y autoridad

El sistema de diseño concreto es
[RFC 0001 — Hornero Signal](rfc-0001-hornero-signal.md). Define los roles de
tokens, las paletas insignia, la tipografía, los glifos, el movimiento, el
contrato de superficies ancladas y el valor por defecto Cockpit. Donde esta
guía y la RFC discrepen, gana la RFC.

HorneroOS es una familia de productos en desarrollo. La dirección de diseño de
abajo es la política transversal entre componentes; los repositorios enlazados
siguen siendo la autoridad para sus activos, tokens, detalles de interacción y
capacidades probadas. Cuando esta guía y una implementación discrepen, reportá
el desfasaje y verificá el producto actual antes de cambiar cualquiera de los
dos. No infieras madurez a partir de un mockup, un paquete o una configuración
experimental.

Para colaboradores del instalador, usá esta guía para la identidad de producto
y los principios de interacción, y luego usá los archivos de marca de Config
para activos oficiales y el catálogo de ediciones para las opciones que el
instalador puede ofrecer. Mantené la marca en Calamares alineada con Hornero
Signal sin crear una fuente de verdad separada.

## Carácter del producto

HorneroOS es una familia de sistemas operativos independiente y cuidadosamente
compuesta, basada en Arch. Sus interfaces deben sentirse pensadas, capaces,
cálidas y directas. La identidad argentina pertenece a la marca del Hornero,
los orígenes del proyecto y lugares y referencias visuales reales; no debe
depender de banderas, clichés ni un tratamiento neón obligatorio.

El pájaro hornero y el motivo del arco de su nido forman la firma visual
canónica. El lenguaje de diseño es **Hornero Signal**: una estación de trabajo
de ingeniería contemporánea de una Argentina alternativa de los años 90 — salas
de control de transmisión, biseles de osciloscopio, cartas de ajuste y láminas
de dibujo técnico — ejecutada con sobriedad moderna. El cromo es calmo y mate;
el ámbar `signal` marca lo que está vivo o es primario, y el celeste `cue`
marca el foco y la información. Los temas regionales pueden tener paletas y
climas distintos, pero cada tema llena los mismos roles Signal. No es Material
Design, no es vidrio y no es neón genérico. La
[introducción a Hornero Signal](../desktop/hornero-signal.md) lo explica para
personas usuarias; la especificación
[Signal Visual Language](signal-visual-language.md) da las reglas concretas
para barras, medidores, paneles y movimiento.

La interfaz debe priorizar la tarea frente al usuario. El ornamento, el
movimiento, la transparencia y la imaginería no deben reducir la legibilidad,
el acceso por teclado, el feedback del sistema ni la confianza alrededor de
acciones con consecuencias.

## Reglas de diseño

### 1. Usá la identidad compartida de Hornero

- Usá el logo canónico, el wordmark, el ícono de app y el favicon chico desde
  los [activos de marca de Config][brand-assets].
- Seguí la [dirección de marca de Config][brand-doc] para variantes de marca,
  intención de color y ubicación. No redibujes el pájaro ni introduzcas una
  mascota o marca de producto competidora.
- Mantené la identidad de Hornero visible pero subordinada a la tarea actual del
  usuario. Las pantallas del instalador deben identificar el producto sin
  convertir cada paso en un panel promocional.

### 2. Componé desde roles semánticos de apariencia

- En el escritorio, usá los roles Signal (superficies `ground` … `lifted`,
  niveles `ink`, `rule`/`ruleStrong`, `signal`, `cue`, `phosphor`, `alert`)
  para superficies, texto, contornos, foco y estado. No fijes valores hex ni
  una apariencia solo oscura, y nunca derives colores de UI del fondo de
  pantalla.
- Config es dueño de los packs de temas, el contrato de tokens schema-v2, los
  catálogos de temas y las referencias de fondos. Shell es dueño de la
  presentación en vivo de la paleta y del comportamiento de apariencia en
  tiempo de ejecución. Su límite y comportamiento de respaldo se describen en
  la [arquitectura de apariencia](../architecture/appearance-system.md).
- Para un instalador independiente o el greeter, mapeá a los valores de rol de
  Signal Night y Signal Day y usá activos de marca canónicos. No finjas que el
  instalador implementa cambio de temas de escritorio.
- Preservá el contraste para texto, controles, indicadores de foco,
  advertencias y pasos destructivos en todo modo soportado. Mirá el
  [esquema de tokens de tema][tokens-schema] de Config y los chequeos de
  contraste antes de agregar tokens de tema al producto.

### 3. Mantené claras la jerarquía y el lenguaje

- Hacé fáciles de identificar la pantalla actual, la siguiente acción y la ruta
  de recuperación.
- Usá etiquetas llanas para las tareas de usuario. Dejá nombres de
  implementación como verbos IPC, identificadores de paquetes y strings de
  despacho del compositor fuera del texto principal orientado al usuario salvo
  que deba actuar sobre ellos.
- Explicá las consecuencias antes de formatear discos, reemplazar entradas de
  arranque, cambiar particiones o ejecutar otra acción difícil de revertir.
  Mostrá un paso de revisión con el destino y edición elegidos antes de
  ejecutar.
- Distinguí elecciones obligatorias de personalizaciones opcionales. Usá
  revelación progresiva en vez de atiborrar el primer arranque con cada ajuste
  avanzado.
- Usá los mismos nombres de producto y edición que el
  [catálogo de ediciones][editions-cat]. No ofrezcas un backend, capacidad o
  afirmación de instalación que el catálogo y el estado de release actuales no
  soporten.

### 4. Hacé la interacción predecible y accesible

- Toda acción esencial debe funcionar con teclado y tener un estado visible de
  foco. El orden de foco sigue el orden visual y de la tarea; moverse entre
  pasos no debe dejar varado al foco.
- Usá un comportamiento consistente de Escape y Atrás. No descartes valores
  ingresados en silencio ni ocultes la única ruta para recuperarse de un error.
- Dale a los controles nombres explícitos, estado y mensajes útiles de
  validación. Nunca comuniques significado solo por color.
- Respetá los ajustes de escala de texto y contraste del sistema donde el
  framework lo permita. Usá valores por defecto legibles, áreas táctiles
  cómodas y contraste suficiente; evitá depender de transparencia sobre
  imágenes variables para texto crítico.
- El movimiento es feedback breve, no un requisito para entender. Evitá fondos
  animados y transiciones no esenciales en flujos de instalación; respetá las
  preferencias de movimiento reducido cuando estén soportadas.
- Seguí el [contrato de foco][shell-focus] probado de la Shell y el
  [contrato de interacción][shell-inter] al implementar superficies de la Shell.
  Estos detalles no definen automáticamente el comportamiento del toolkit del
  instalador.

### 5. Sé honesto sobre las capacidades del sistema

- HorneroOS Desktop es Wayland-first. Hyprland y Niri exponen distintas
  capacidades de compositor; el sistema no es sinónimo de ninguno de los dos
  compositores.
- Mostrá solo opciones de instalación que puedan instalarse y validarse.
  Etiquetá opciones planificadas o experimentales en la opción misma, no solo
  en un pie de página.
- Degradá con gracia cuando dispositivos opcionales, redes, portales o
  servicios no estén disponibles. Explicá la condición y ofrecé un siguiente
  paso seguro.
- Usá capturas reales y revisadas del producto para afirmaciones del producto.
  Marcá claramente el arte conceptual, las recreaciones en navegador y los
  bocetos aún no publicados del instalador.

## Tipografía, íconos e imaginería

Hornero Signal usa tres familias IBM Plex (Arch `ttf-ibm-plex`, OFL-1.1): IBM
Plex Sans para texto de interfaz, IBM Plex Mono para lecturas, numerales,
eyebrows y código, e IBM Plex Sans Condensed para el reloj, la pantalla de
bloqueo y títulos grandes. Los números usan cifras tabulares. Los íconos de la
Shell son Hornero Glyphs, un subconjunto curado de Tabler Icons (MIT) usado
mediante `Glyph { name: "wifi" }`; Material Symbols no se usa en ningún lado.
Los roles y la escala se definen en RFC 0001 §3.3–3.4 y se implementan en
[`AppearanceConfig.qml`][app-cfg] de la Shell. Herramientas independientes que
no puedan cargar Plex deben elegir una tipografía disponible y licenciada con
claridad y densidad similares.

Usá íconos con un significado consistente y reconocible; acompañá los íconos
poco familiares o de alto impacto con texto. Preferí íconos genuinos de app
para aplicaciones. Las fotografías y fondos de pantalla deben ser auténticos,
acreditados y licenciados para su contexto de distribución. Usá el manifiesto y
los créditos de fondos de Config como autoridad para los fondos de escritorio
incluidos; no copies archivos de vista previa del sitio web en un paquete como
atajo.

## Composición y densidad

Preferí alineación clara, una pequeña cantidad de grupos significativos y
espacio suficiente para separar tareas no relacionadas. Una vista densa de
información es apropiada cuando ayuda a comparar o revisar; no debe volver
difícil encontrar la acción primaria. Usá bordes, elevación y esquinas
redondeadas para comunicar agrupación o interacción, no como decoración en cada
elemento.

En el instalador, mantené estable la navegación por pasos, enfocado el
contenido principal y en un lugar predecible la acción primaria. El banner de
producto y las diapositivas son contexto de apoyo; el estado de instalación, la
validación, la selección de destino y las instrucciones de recuperación toman
prioridad visual.

## Dónde viven las reglas

| Tema | Fuente autorizada | Qué gobierna |
| --- | --- | --- |
| Identidad | [BRAND][brand-doc], [assets][brand-assets] | Marca, wordmark |
| Temas | [Apariencia][arch-app], [temas][c-th], [fondos][c-wp] | Packs/fondos |
| Sistema | [RFC 0001][rfc1], [Visual Lang.][svl] | Roles, tipo, glifos |
| Tokens | [AppCfg][app-cfg], [Signal][sig], [Native][nat] | `Signal.palette` |
| Interacción | [Focus][shell-focus], [Inter][shell-inter] | Foco y cierre |
| Compositores | [Comp][comp], [Layouts][lay] | Soporte y layout |
| Login/bloqueo | [Greeter UX][greeter-ux] | Jerarquía auth, teclado |
| Ediciones | [Catálogo][editions-cat], [Ediciones][arch-ed] | Nombres, madurez |
| Instalador | [Calamares][cal-brand] | Assets Signal Night |
| Sitio web | [Estilos web][web-style] | Composición, paleta |
| Evidencia QA | [Escenarios][qa-scen], [Medios][qa-media] | Capturas, pruebas |

El sitio web usa los mismos roles Hornero Signal y familias IBM Plex que el
escritorio, adaptados a diagramación editorial. No define una paleta aparte
para el escritorio ni para el instalador.

## Cómo aplicar esta guía al instalador gráfico

El instalador debe sentirse como HorneroOS por su marca, nomenclatura, idioma,
colores y tipografía Signal, y por el cuidado en decisiones con consecuencias.
Sigue siendo una utilidad de instalación, no una shell de escritorio en
miniatura. Quien lo visite debe poder distinguir qué edición se instala, adónde
irá, qué cambiará y si una opción es planificada o experimental antes de
confirmarla.

Mantené el trabajo específico de Calamares localizado en su marca y
configuración de módulos. Preferí un pequeño adaptador desde el catálogo
compartido de ediciones antes que duplicar verdades de paquetes o capacidades
en la UI del instalador. Cuando una opción todavía no pueda ejecutarse o
probarse, etiquetala como no disponible o planificada en lugar de presentarla
como completa. Mantené la integración de Calamares modular para que cualquier
futuro instalador propio pueda compartir el mismo catálogo y principios.

Antes de dar por listo un diseño del instalador, validá un flujo completo de
instalación en un entorno UEFI y BIOS descartable, incluyendo tanto uso por
teclado como caminos de fallo y recuperación. Una vista previa de marca o un
parseo de configuración de Calamares por sí solos no certifican la seguridad de
la instalación.

## Proponer un cambio de diseño

1. Identificá el repositorio dueño en la tabla de arriba.
2. Describí la necesidad del usuario, la tarea relevante y cualquier límite de
   capacidad o madurez del que dependa el diseño.
3. Reutilizá los activos canónicos de identidad y los tokens del componente
   dueño. Si hace falta una nueva regla o token compartido, actualizá su fuente
   de verdad y generadores/esquemas/pruebas en el mismo cambio.
4. Incluí capturas reales o evidencia reproducible para cambios en el
   comportamiento visible del producto. Indicá qué compositor, tema, viewport y
   revisión de release representa la evidencia.
5. Comprobá operación por teclado, contraste, movimiento reducido, layouts
   angostos y estados de fallo. No afirmes una prueba que no se corrió.
6. Actualizá este mapa solo cuando cambien la propiedad entre repositorios, los
   principios a nivel de producto o los enlaces de fuente. Mantené las reglas
   detalladas de implementación junto a la implementación.

[brand-assets]: https://github.com/HorneroOS/config/tree/main/assets/brand
[brand-doc]: https://github.com/HorneroOS/config/blob/main/docs/BRAND.md
[tokens-schema]: https://github.com/HorneroOS/config/blob/main/profiles/themes/tokens.schema.json
[editions-cat]: https://github.com/HorneroOS/hornero/blob/main/editions/catalogue.yaml
[shell-focus]: https://github.com/HorneroOS/shell/blob/main/docs/FOCUS.md
[shell-inter]: https://github.com/HorneroOS/shell/blob/main/docs/INTERACTION.md
[app-cfg]: https://github.com/HorneroOS/shell/blob/main/config/AppearanceConfig.qml
[arch-app]: ../architecture/appearance-system.md
[c-th]: https://github.com/HorneroOS/config/tree/main/profiles/themes
[c-wp]: https://github.com/HorneroOS/config/blob/main/docs/WALLPAPERS.md
[rfc1]: rfc-0001-hornero-signal.md
[svl]: signal-visual-language.md
[sig]: https://github.com/HorneroOS/shell/blob/main/services/Signal.qml
[nat]: https://github.com/HorneroOS/shell/blob/main/docs/NATIVE-APPEARANCE.md
[comp]: https://github.com/HorneroOS/shell/blob/main/docs/COMPOSITORS.md
[lay]: https://github.com/HorneroOS/shell/blob/main/docs/LAYOUTS.md
[greeter-ux]: https://github.com/HorneroOS/greeter/blob/main/docs/UX_CHECKLIST.md
[arch-ed]: ../architecture/editions.md
[cal-brand]: https://github.com/HorneroOS/installer/tree/main/image/calamares/branding/hornero
[web-style]: https://github.com/HorneroOS/website/blob/main/docs/COMPONENTS_AND_STYLING.md
[qa-scen]: https://github.com/HorneroOS/qa/blob/main/docs/SCENARIOS.md
[qa-media]: https://github.com/HorneroOS/qa/blob/main/docs/MEDIA.md
