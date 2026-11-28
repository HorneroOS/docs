# Fondos

Usá **Ajustes → Apariencia → Fondo** para trabajar con el fondo del
escritorio. Un fondo es solo la imagen detrás de tus ventanas: por defecto
nunca cambia los colores de la interfaz. Los colores salen del
[tema](appearance.md) elegido, así que podés combinar cualquier imagen con
cualquier tema. Para derivar colores de un fondo a propósito, usá
[Hornero Chromatic](chromatic.md).

> **Estado de release.** Los colores independientes del fondo llegaron con
> [Hornero Signal](hornero-signal.md) y vienen incluidos en `v0.2.0-preview42`
> (ISO y QCOW2 de Desktop) además de `main`/AUR. Las ISO anteriores hasta la
> `v0.2.0-preview32` generaban los colores de la shell a partir del fondo.

## Poné un fondo local

La CLI aplica una imagen que ya está en tu máquina. Previsualizá la acción
primero y después confirmala:

```sh
horneroctl wallpaper current
horneroctl wallpaper set "$HOME/Pictures/Wallpapers/night.jpg" --dry-run
horneroctl wallpaper set "$HOME/Pictures/Wallpapers/night.jpg" --yes
```

`horneroctl wallpaper current` imprime la imagen actual resuelta. `set`
reemplaza el puntero de fondo que observa la shell y actualiza el fondo de
la pantalla de bloqueo; nunca cambia un color. La ruta puede ser cualquier
archivo legible.

## Fondos que vienen con HorneroOS

- **Signal Night y Signal Day** usan fondos procedurales dibujados con los
  colores del tema (una grilla de dibujo técnico, la diagonal de La Plata y
  marcas de registro), renderizados en tu máquina a partir de fuentes SVG
  bajo la licencia MIT del proyecto. Signal High Contrast reutiliza el
  fondo de Night.
- Cada **Hornero Original** trae una fotografía con licencia del lugar que
  le da nombre: Buenos Aires Nocturno, Cuyo, Fin del Mundo, Iberá, Iguazú,
  Pampa, Patagonia, Quebrada y Sierras. Son imágenes de Wikimedia Commons
  bajo CC BY 2.0 o CC BY-SA 4.0; autoría, fuente y licencia figuran en los
  [créditos de fondos](https://github.com/HorneroOS/config/blob/main/profiles/themes/WALLPAPER-CREDITS.md)
  de Config y se instalan en `/usr/share/licenses/hornero-config/`.
- Los **ports de la comunidad** nombran una colección de fondos opcional,
  que se busca en `~/Pictures/Wallpapers/<colección>/` o en
  `~/.local/share/hornero/wallpapers/<colección>/`; no incluyen imágenes.

Los fondos empaquetados se instalan en `/usr/share/hornero/wallpapers/`.

![Un escritorio vacío sobre el fondo Patagonia: picos nevados y un
glaciar sobre un lago calmo al atardecer, con las barras superior e
inferior de la Shell visibles.](https://www.horneroos.com/captures/cap-theme-05.png)

*El Original Patagonia aplicado. La autoría, la fuente y la licencia
de la fotografía figuran en los créditos de Config enlazados arriba.
Captura real del escritorio en el equipo del maintainer,
19 de noviembre de 2026.*
Las ilustraciones retiradas de Hornero Dark, Light y 199X ya no se
distribuyen.

## Colecciones de fondos opcionales y personales

El [repositorio público de dotfiles](https://github.com/ulises-jeremias/dotfiles/tree/main/home/dot_local/share/hornero/wallpapers)
tiene ilustraciones opcionales para estaciones de trabajo Arch personales.
Cuando se aplica el perfil de fondos opcional, las imágenes se enlazan en
`~/Pictures/Wallpapers/<colección>/`. Siguen siendo medios de la persona
usuaria y el paquete Hornero Config no las redistribuye.

El sitio web mantiene separadas estas colecciones: recorré el
[catálogo de temas](https://horneroos.com/themes), la
[galería de fondos fotográficos](https://horneroos.com/wallpapers) y el
[Showroom](https://horneroos.com/showroom). Los epígrafes identifican
fotografías, ilustraciones originales, renders conceptuales y capturas del
escritorio en funcionamiento según su procedencia real; las capturas
tomadas antes de Hornero Signal están etiquetadas como apariencia anterior.

## Cuando el fondo de un tema no está disponible

El manifiesto de un tema puede nombrar una imagen por defecto y una
colección sin incluir la imagen. Si ese archivo no está, el tema se aplica
igual; elegí una imagen instalada o pasale a la CLI un archivo local.
Hornero no descarga imágenes por su cuenta.

Para inspeccionar los metadatos de fondos de todos los temas instalados:

```sh
horneroctl appearance theme list --full
horneroctl appearance theme show hornero-signal-night
```

Los manifiestos de temas y fondos se mantienen en
[HorneroOS/config](https://github.com/HorneroOS/config/tree/main/profiles/themes).
