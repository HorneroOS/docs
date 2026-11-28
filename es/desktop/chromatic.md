# Hornero Chromatic: colores a partir de tu fondo

Hornero Chromatic es una forma opcional de colorear el escritorio. En vez de
elegir un [tema](appearance.md) ya armado, dejás que Hornero lea un fondo,
una imagen o un color que elijas, y arme con eso una paleta completa de
[Hornero Signal](hornero-signal.md). Los temas curados (Signal Night, Signal
Day y Signal High Contrast) siguen siendo el valor de fábrica y el respaldo
cuando algo sale mal.

> **Estado de release.** Chromatic v3 viene incluido en `v0.2.0-preview42` (ISO
> y QCOW2 de Desktop) y en `main`/AUR tanto en Hornero Shell como en
> `horneroctl`. Las ISO anteriores hasta la `v0.2.0-preview32` no lo
> incluían. El ajuste de acento (mirá [Ajuste de acento](#ajuste-de-acento))
> sigue separado.

## Qué es y qué no es

- Solo colorea el escritorio. Cambia el matiz y la intensidad dentro de la
  estructura fija de Signal; las formas, la tipografía, los glifos y el
  movimiento no cambian.
- **No** es Material You. No hay roles Material ni una biblioteca de color
  externa: un único motor nativo arma directamente los roles de Signal.
- No se aplica nada hasta que lo decidas. La vista previa es solo en
  memoria; cancelar no escribe nada.
- Un fondo nunca puede dejar la interfaz ilegible. Cada paleta se verifica
  contra los umbrales de contraste antes de escribir nada, y una paleta que
  no los cumple no se aplica.
- Las barras Cockpit Clear siguen totalmente transparentes. Chromatic puede
  cambiar el color de su texto, nunca agregar un fondo, un tinte ni un
  desenfoque.

## Probalo

Abrí **Ajustes → Apariencia → Chromatic**. La sección dibuja un escritorio de
muestra (barra, popout, tarjeta, fila del lanzador, notificación, colores de
terminal) con la paleta candidata, así ves el resultado antes de aplicarlo.

1. Elegí una **fuente**: el fondo actual, otra imagen, uno o dos colores, o
   la paleta de la casa Signal.
2. Mirá lo que Hornero dedujo (modo, variante, contraste, una descripción
   corta como "Oscuro · equilibrado · ámbar cálido · calmo"). Cada ítem
   muestra su motivo y tiene un control para pisarlo; **Auto** significa
   seguir a la imagen.
3. Previsualizá en el escritorio. **Cancelar** o **Escape** restaura la
   paleta anterior y no escribe nada.
4. **Aplicá** cuando te guste.

![Ajustes, Apariencia, sección Chromatic siguiendo el fondo actual. Se
listan cinco colores extraídos con sus valores hexadecimales y el panel
de vista previa muestra la paleta candidata con sus proporciones de
contraste.](https://www.horneroos.com/captures/cap-chroma-07.png)

*Chromatic leyendo el fondo actual: los colores extraídos a la
izquierda, la paleta previsualizada y su contraste verificado a la
derecha. Captura real del escritorio en el equipo del maintainer,
19 de noviembre de 2026.*

Desde una terminal, el mismo flujo es:

```sh
horneroctl appearance chromatic preview --seed "#D98A3A"
horneroctl appearance chromatic apply --variant vibrant --dry-run
horneroctl appearance chromatic apply --yes
```

`preview` y `--dry-run` nunca escriben. `apply` requiere `--yes`.

## Fuentes

- **Fondo** (por defecto) — el fondo actual. Funcionan imágenes fijas, GIF,
  WebP y APNG animados, y archivos de video; el video necesita `ffmpeg`
  instalado y, sin él, esa fuente se informa como ilegible.
- **Imagen** — cualquier otro archivo de imagen: `--source image:PATH`.
- **Color** — uno o dos colores `#RRGGBB` (`--seed`, hasta dos). El primero
  es el acento principal y el segundo el acento secundario. El Centro de
  control ofrece chips de color ordenados tomados de tu imagen, un selector
  de matiz e intensidad y un campo hexadecimal.
- **Casa Signal** — los matices de fábrica de Signal; solo el tinte de las
  superficies sigue al fondo.

Si un color que elegiste no cumple los umbrales de contraste, Hornero lo
mueve lo mínimo necesario y te dice qué color cambió y por qué.

## Variantes

Una variante define el carácter de la paleta:

- **Balanced** (equilibrada, por defecto) — superficies tranquilas y un
  acento seguro; el aire de Signal Night o Day en el matiz de la imagen.
- **Vibrant** (vibrante) — acentos más fuertes y un marco apenas teñido.
- **Expressive** (expresiva) — un segundo acento de un matiz más lejano y
  colores de estado más coloridos.
- **Faithful** (fiel) — el acento es tu color mismo cuando cumple los
  umbrales de contraste, y las superficies toman el matiz dominante de la
  imagen.
- **Muted** (apagada) — marco casi neutro con acentos suaves.
- **Monochrome** (monocromática) — marco y texto neutros; los acentos solo
  susurran el matiz. Los colores de estado conservan su significado.
- **High contrast** (alto contraste) — el nivel de contraste más estricto,
  un fondo más profundo, texto más brillante, sin brillo y sin
  translucidez.
- **Neon** — acentos saturados y un brillo más fuerte. Solo oscuro: si
  pedís claro devuelve oscuro y explica por qué.

`horneroctl appearance chromatic variants` lista lo que ofrece el motor
instalado. Con la variante en **Auto**, Hornero elige entre Balanced,
Vibrant, Expressive y Muted según cuán colorida sea la imagen. Puede
sugerir Neon para imágenes oscuras con colores neón brillantes, pero nunca
lo aplica solo.

Además de la variante, podés ajustar:

- **Modo** — Auto, Oscuro o Claro. Auto sigue cuán clara es la imagen y no
  se da vuelta de un lado al otro cuando rota una carpeta de fondos.
- **Contraste** — Auto, Standard, Boosted o Maximum.
- **Profundidad de superficies** — Standard o Deep.
- **Intensidad** — escala la cantidad de color de 0,5 a 1,5.
- **Rotación de matiz** — gira los colores elegidos de -180 a 180 grados.
- **Preferencia por modo** — guardá una variante distinta para oscuro y
  claro.

## Seguir al fondo

La **política de recoloreado** decide qué pasa cuando cambia el fondo
mientras Chromatic está activo:

- **Off** — no cambia nada hasta que apliques de nuevo.
- **Auto** — la paleta se regenera para el fondo nuevo
  (`horneroctl appearance chromatic follow`).
- **Ask** — Hornero muestra una vista previa y te deja aplicar o **Keep
  current** (mantener la actual).

Los cambios de paleta se funden suavemente. El fundido es instantáneo con
movimiento reducido, en el modo de experiencia Gaming y con alto contraste,
y podés apagar la transición suave en la sección.

## Paletas guardadas

Una paleta que te gusta se puede conservar: **guardá** la paleta activa como
un tema con nombre y aparece junto a los demás temas. También podés
renombrarla, borrarla, exportarla a un archivo e importar el archivo de tema
de otra persona. Las importaciones se verifican contra los mismos umbrales
de contraste y los campos de texto libre se validan antes de instalar nada.

```sh
horneroctl appearance chromatic list
horneroctl appearance chromatic save --id amber-dusk --name "Amber dusk" --yes
horneroctl appearance chromatic export --output amber-dusk.json
horneroctl appearance chromatic import amber-dusk.json --yes
```

## Ajuste de acento

Chromatic y los temas curados eligen el acento principal por vos. El ajuste
de acento te deja fijar tu propio color de acento, por separado para modo
oscuro y claro y por modo de experiencia, con un conjunto opcional de
presets cálidos y suaves y un **Restablecer** que vuelve al acento propio
del tema. Está pendiente de revisión
([shell#614](https://github.com/HorneroOS/shell/pull/614)); hasta que
llegue, usá la fuente **Color** (`--seed`) con la variante Faithful para
armar una paleta alrededor del acento que quieras.

## Plantillas de aplicaciones

Además de la Shell, Hyprland, GTK, Qt y los renderizadores integrados de
terminales, `horneroctl` renderiza plantillas de Chromatic propias de config
bajo `/usr/share/hornero/chromatic/templates/` (23 manifiestos oficiales que
cubren terminales, barras, lanzadores, editores y herramientas de diff) cuando
existe el directorio de configuración de cada app:

- **Neovim (`nvim-colorscheme` y `nvim`):** `nvim-colorscheme` escribe
  `~/.config/nvim/colors/hornero-chromatic.lua` (grupos de UI, sintaxis, diff,
  diagnósticos, LSP y Treesitter); activalo con
  `:colorscheme hornero-chromatic`. La plantilla `nvim` también escribe un
  módulo de paleta Lua en `~/.config/nvim/lua/hornero_chromatic.lua`.
- **Helix (`helix`):** escribe `~/.config/helix/themes/hornero-chromatic.toml`
  con definiciones de UI, diagnósticos, diff, sintaxis y `[palette]`; elegí
  `theme = "hornero-chromatic"` en `~/.config/helix/config.toml`.
- **git-delta (`delta`):** escribe `~/.config/git/hornero-chromatic.gitconfig`
  con un bloque `[delta "hornero-chromatic"]` consciente del modo claro/oscuro
  más secciones `[color "diff"]`, `[color "branch"]` y `[color "status"]`;
  incluilo desde `~/.config/git/config.user`:

  ```ini
  [include]
    path = ~/.config/git/hornero-chromatic.gitconfig
  [delta]
    features = hornero-chromatic
  ```

Inspeccioná o previsualizá plantillas con `horneroctl`:

```sh
horneroctl appearance chromatic templates list
horneroctl appearance chromatic templates render --all
```

Los manifiestos propios del usuario van en
`$XDG_CONFIG_HOME/hornero/chromatic/templates.d/*.json`; validalos con
`horneroctl appearance chromatic templates check <archivo>`.

## Volver atrás

Cada aplicación es transaccional: Hornero toma una instantánea del estado
actual, escribe de forma atómica y restaura la instantánea si algo falla.
También podés volver atrás vos:

```sh
horneroctl appearance chromatic history
horneroctl appearance chromatic rollback --dry-run
horneroctl appearance chromatic rollback --steps 2 --yes
```

`history` lista las diez instantáneas más nuevas. `rollback` restaura el
estado de `--steps` aplicaciones atrás (por defecto 1). Para salir de
Chromatic del todo, corré `horneroctl appearance chromatic off --yes`:
aplica el tema de respaldo para el modo actual. También podés elegir
cualquier tema curado.

## Accesibilidad

- **Alto contraste** (**Ajustes → Accesibilidad**) está protegido: siempre
  muestra la paleta curada Signal High Contrast y apaga la translucidez,
  sin importar lo que haya producido Chromatic. La sección avisa cuando
  está activo.
- **Niveles de contraste** — Standard sigue los umbrales de Signal; Boosted
  sube el texto a 7:1 y Maximum exige 7:1 en todos los pares de texto. El
  anillo de foco llega a 3:1 en todas las superficies, y el significado de
  los estados nunca depende solo del matiz.
- **Las superficies translúcidas** mantienen legible su texto sobre tu fondo
  real, subiendo su opacidad cuando la imagen es muy cargada.
- **Movimiento reducido** hace instantáneos los cambios de paleta.

## Solución de problemas

```sh
horneroctl appearance chromatic doctor
horneroctl appearance chromatic status
```

`doctor` revisa el ayudante del motor, `ffmpeg`, las plantillas de
aplicaciones, el estado guardado y el bloqueo. La sección informa con
claridad cuando falta el ayudante, una imagen es ilegible, un video
necesita `ffmpeg`, no hay fondo o una paleta no pasó los umbrales. Después
de cualquier cambio, `horneroctl appearance doctor` verifica que el
esquema activo sea válido.

Para ver cómo encaja Chromatic en el resto del sistema de apariencia, mirá
[Sistema de apariencia](../architecture/appearance-system.md). El diseño
es la [RFC 0002](../development/rfc-0002-hornero-chromatic.md).
