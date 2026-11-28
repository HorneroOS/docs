# Hornero Welcome

Hornero Welcome es tu plataforma de inicio en HorneroOS y tu guía permanente
para descubrir qué puede hacer el escritorio. Acompaña a quienes arrancan por
primera vez con una configuración tranquila, se convierte en un centro de
exploración cuando terminás y muestra novedades concisas tras una
actualización sin hacerte repetir el recorrido inicial.

> **Development.** La CLI `horneroctl welcome` y la ventana inicial de
> Welcome ya están en `main`, mientras que el rediseño de 3 modos **Signal
> Flight** (`First Flight`, `Explore Hornero` y `What's New`) avanza en
> `HorneroOS/shell#751` y `HorneroOS/hornero#506`. Las ISO actuales hasta
> `v0.2.0-preview32` todavía traen la ventana anterior de 11 páginas.

## Tres modos en una sola ventana

| Modo | Cuándo se abre | Propósito |
| --- | --- | --- |
| **First Flight** | Primer inicio (`showOnLogin`) | Guía de 9 escenas |
| **Explore Hornero** | Aperturas manuales | Buscar funciones y atajos |
| **What's New** | Tras actualizar (`showOnLogin`) | Novedades de versión |

Abrí Welcome en cualquier momento desde el Lanzador (**Ctrl + Space**),
**Ajustes** o una terminal:

```sh
horneroctl welcome open
horneroctl welcome status
horneroctl welcome set-show-on-login false --yes
```

Si más adelante querés repetir el recorrido guiado, corré `horneroctl welcome
reset --yes`. Todo comando que modifica estado acepta `--dry-run` antes de
confirmar con `--yes`.

## First Flight: llegada guiada

En lugar de una lista interminable de tarjetas, **First Flight** abre una
ventana serena de `1080×680` con una barra superior mínima y un riel inferior
compacto. Podés alternar **Show on login**, elegir **Skip tour** cuando
quieras o avanzar paso a paso por nueve escenas con composiciones propias:

1. **Arrival:** Muestra tu edición y compositor activos (`Hyprland` o `Niri`)
   sobre arte verificado de la Argentina con crédito visible del autor.
2. **Make It Yours:** Probá temas, fondos, acentos de Chromatic y layouts de
   barra con vistas previas reversibles en vivo.
3. **Workstation Builder:** Elegí un modo de experiencia y explorá perfiles de
   software para tu estación de trabajo.
4. **Meet Javi:** Personalizá el aspecto visual de Javi y revisá cómo el
   asistente de IA local permanece apagado hasta que vos lo habilites.
5. **Move & Fly:** Practicá cuatro acciones reales del escritorio usando tus
   atajos de teclado activos.
6. **Extensions & Ecosystem:** Explorá extensiones curadas de PluginKit v3 con
   sus límites de privilegios y recuperación en Modo Seguro.
7. **Create · Build · Play:** Chequeá la disponibilidad real de Studio Audio,
   herramientas de desarrollo/agentes y Gaming.
8. **Trust, Diagnostics & Recovery:** Revisá la salud con `horneroctl doctor` y
   la diferencia entre instantáneas de configuración y sondas Btrfs del SO.
9. **Ready to Fly:** Repasá tus elecciones confirmadas y saltá directo al
   Lanzador o a **Explore Hornero**.

## Make It Yours: vistas previas reversibles

La escena 2 te deja experimentar con la estética del escritorio sin riesgo de
dejar una configuración rota:

- **Polaridad y temas:** Alterná en vivo entre **Signal Day** (cerámica
  blanca), **Signal Night** (grafito de hora azul), **Signal High Contrast** y
  los originales argentinos (`jacaranda`, `glaciar`, `ceibo`).
- **Fondos argentinos con licencia verificada:** Welcome exhibe únicamente los
  2 SVG procedurales MIT de Signal y las 3 fotografías argentinas bajo CC BY 2.0
  (*Buenos Aires after dark* de Luis Argerich, *Beagle Channel* de RAYANDBEE y
  *Quebrada del Condorito* de Kevin Jones) con atribución visible. Mirá
  [Fondos](wallpapers.md).
- **Hornero Chromatic v3:** Previsualizá acentos armonizados con el fondo
  (`Balanced`, `Vibrant` o `Muted`) manteniendo limpias las superficies de
  cerámica o grafito. Mirá [Hornero Chromatic](chromatic.md).
- **Layouts de barra:** Alterná entre `Cockpit`, `Hornero Left`, `Islands` y
  `Dock Bottom` sobre un escenario en miniatura en vivo. Mirá
  [Layouts](layouts.md).

Las vistas previas de tema, Chromatic y fondo corren primero en memoria.
Cuando una vista previa de layout escribe en disco, Welcome guarda tu línea
base en `$XDG_STATE_HOME/hornero/welcome-preview-tx.json` y muestra una barra
no bloqueante con **Revert** y **Apply & Keep**. Si apretás **Escape** o
cerrás la ventana, se revierten los cambios sin confirmar; si la shell se
cierra de golpe, el próximo inicio restaura automáticamente tu aspecto previo.

## Armá tu estación de trabajo

### Modos de experiencia

La escena 3 combina un selector asimétrico para los cinco [Modos de
experiencia](experience-modes.md) (**Everyday**, **Focus**, **Signal**,
**Studio** y **Gaming**) con una ficha técnica en vivo que muestra nivel de
movimiento, tasa de telemetría, presupuesto de brillo, retención de popups y
el estado real del equipo (como disponibilidad de Studio Audio PipeWire o
ajustes de Hyprland).

### Perfiles de software curados con Hornero Apps

La instalación de aplicaciones desde Welcome se apoya en [Hornero
Apps](hornero-apps.md) y su catálogo declarativo firmado (`catalog/apps.v1.json`)
en lugar de scripts ad-hoc. Tanto usuarios individuales como equipos pueden
inspeccionar perfiles y políticas de confianza antes de instalar nada:

```sh
horneroctl store profiles
horneroctl store profile-show ai-workstation --json
horneroctl store policy show --json
```

Cada paquete muestra su insignia de procedencia (**Oficial**, **Verificada**,
**Comunidad** o **Web App**) y su licencia. El software propietario y las
recetas AUR opt-in nunca se instalan sin confirmación explícita, y las
organizaciones pueden fijar fuentes permitidas con `horneroctl store policy` o
replicar flotas con `horneroctl store manifest` (toda mutación queda registrada
en `~/.local/state/hornero/store/audit.jsonl`).

### Cargas de trabajo y límites honestos de edición

La escena 7 (`Create · Build · Play`) se adapta a lo que realmente está
instalado en tu máquina:

- **Create (Studio):** Muestra el estado real de PipeWire Studio Audio y los
  kits de ruteo (`live-call`, `browser-backing`, `reaper-low-latency`).
- **Build (Dev & Agents):** Abre tu terminal configurada, el gestor Yazi y el
  **Agent Center** (`ControlCenter("agents")`) para revisar agentes de código
  locales y telemetría de uso. (La edición dedicada `Agents` sigue en estado
  **Planned**.)
- **Play (Gaming):** Muestra la preparación de GameMode a pantalla completa
  (`gamescope` y `mangohud`).
- **Compositores y ediciones planificadas:** Hyprland es el valor por defecto
  validado; [Niri](compositors.md) es **Experimental** y oculta funciones
  exclusivas de Hyprland. `Labwc` y `Server` están marcados como **Planned** y
  quedan fuera de Welcome.

## Conocé a Javi y su Companion

La escena 4 separa con claridad los dos roles de Javi para que siempre sepas
qué corre en tu equipo:

- **Javi Companion (compañero visual):** Un personaje expresivo de escritorio
  con ocho skins (`default`, `argentina`, `gaucho`, `blue-gold`, `nocturnal`,
  `retro-terminal`, `mono` y `red`) y poses interactivas (`Greet`, `Think`,
  `Work`, `Sleep`) que reaccionan a la batería, compilaciones y modos.
- **Javi IA / Asistente Hermes (opcional y solo local):** Apagado por defecto
  y nunca iniciado automáticamente desde Welcome. Si lo habilitás aparte,
  ejecuta lecturas locales vía `horneroctl`, bloquea adjuntos con pinta de
  secretos (archivos `.env` y claves privadas) antes de enviar prompts y exige
  una puerta explícita de **Aprobación** antes de cambiar algo en el sistema.

Hornero Welcome no pide **cuentas obligatorias**, **inicio de sesión en la
nube** ni envía **telemetría**.

## Tutoriales interactivos (`Move & Fly`)

La escena 5 enseña la navegación principal sin tildes falsos por tiempo. Lee
tus **atajos activos** en tiempo real (reflejando tus reasignaciones, o
mostrando `Unbound — use action button or Bar` si está libre) y marca cada
misión como completa recién cuando ocurre el evento real en la shell o el
compositor:

1. **Lanzador:** Abrí el Lanzador con tu atajo activo o **Try Launcher**.
2. **Dashboard:** Alterná el panel del Dashboard.
3. **Cambiar de espacio de trabajo:** Pasá a otro espacio en `Hyprland` o
   `Niri`.
4. **Abrir Ajustes:** Lanzá el Centro de control mientras Welcome queda
   abierto en segundo plano para mostrarte el tilde verde al volver.

En Hyprland se suma la pista **Toggle Scratchpad**; en Niri se oculta de
forma automática. Podés avanzar con **Continue** cuando quieras.

## Explore Hornero: tu centro permanente

Una vez completado `First Flight`, abrir Welcome manualmente te lleva directo a
**Explore Hornero**:

- **Búsqueda unificada al instante:** Filtrá funciones de Hornero, páginas del
  Centro de control y atajos activos desde una sola barra.
- **Categorías ordenadas:** Saltá con enlaces tipados y seguros a Navegación y
  Shell, Apariencia y Chromatic, Javi e IA, Cargas y Ediciones, y Seguridad y
  Recuperación.
- **Referencia de atajos buscable:** Consultá tus combinaciones reales junto a
  la guía de [Atajos](shortcuts.md).
- **Extensiones y registro de confianza:** Explorá [Extensiones](extensions.md)
  curadas con el aviso explícito de que los plugins de Quickshell corren sin
  sandbox bajo tus permisos de usuario (`HORNERO_SAFE_MODE=1` los desactiva
  para recuperar la sesión), además de un registro claro que separa las
  **instantáneas de configuración de Hornero** (soportadas) de las sondas de
  **recuperación Btrfs del SO** (solo lectura, mirá [Actualizaciones y
  recuperación](updates-and-rollback.md)).

## What's New y actualizaciones

Si ya venís usando HorneroOS y actualizás el sistema, **nunca** te volvemos a
meter en `First Flight`. Welcome desacopla haber completado el primer inicio
(`firstRunCompleted`) del seguimiento de versión (`lastSeenReleaseVersion`):

- Si desactivaste el arranque automático (`showOnLogin: false`), Welcome **no
  se abre solo** al iniciar sesión, ni siquiera tras una actualización grande.
- Si mantuviste el arranque automático y ya completaste `First Flight`, una
  actualización abre directo **What's New** una vez por versión con los
  destacados y enlaces directos a cada ajuste nuevo.

## Accesibilidad y eficiencia energética

Hornero Welcome sigue los contratos de [Hornero Signal](hornero-signal.md) y
[Popups, foco y movimiento](popups-and-motion.md):

- **Control total por teclado:** Cada escena, pestaña, muestra y tutorial
  funciona con el teclado, con anillo de foco celeste de `2 px`
  (`Signal.palette.focus`) y manejo predecible de **Escape**.
- **Semántica AT-SPI y escala de texto:** Los controles exponen nombres y
  estados accesibles y respetan **Ajustes → Accesibilidad → Tamaño del
  texto**.
- **Modos de contraste:** Signal Day (`>= 5.27:1` en el texto más suave),
  Signal Night y **Signal High Contrast** (`hornero-signal-contrast`) aplican
  en todas las escenas, con velos direccionales en la escena 1 para garantizar
  legibilidad sobre fotografía.
- **Movimiento reducido y cero despertares en reposo:** Con **Reducir
  movimiento** (o `org.gnome.desktop.interface enable-animations = false`),
  las transiciones se acotan a fundidos de `<= 90 ms`, Javi queda quieto en el
  cuadro `0` (`holdStill`), `HorneroSprite` detiene su parpadeo y toda
  animación se pausa cuando la ventana queda oculta o minimizada.

## Guías relacionadas

- [ADR: arquitectura de Hornero Welcome (en inglés)][adr-welcome]
- [Hornero Signal](hornero-signal.md) · [Temas y apariencia](appearance.md)
- [Hornero Chromatic](chromatic.md) · [Fondos](wallpapers.md)
- [Hornero Apps](hornero-apps.md) · [Modos de experiencia](experience-modes.md)
- [Atajos](shortcuts.md) · [Extensiones](extensions.md)
- [Actualizaciones y recuperación](updates-and-rollback.md) ·
  [`horneroctl`](horneroctl.md)

[adr-welcome]: ../../architecture/adr-hornero-welcome.md
