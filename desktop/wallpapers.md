# Wallpapers and color

Use **Settings → Appearance → Background** to work with the desktop
background. Wallpaper files are user media: theme packs can refer to them, but
third-party images are not automatically downloaded when you select a theme.
This keeps theme changes usable offline and avoids an unexpected network
fetch.

## Set a local wallpaper

The CLI applies an image already present on your machine. Preview the action
first, then confirm it:

```sh
horneroctl wallpaper current
horneroctl wallpaper set "$HOME/Pictures/Wallpapers/night.jpg" --dry-run
horneroctl wallpaper set "$HOME/Pictures/Wallpapers/night.jpg" --yes
```

`horneroctl wallpaper current` reports the resolved current image. The path
can be a file in Pictures or another readable location. `horneroctl wallpaper
reload --yes` re-runs the color pipeline for the current image; it does not
choose a different one.

## Curated wallpaper collection

The public [dotfiles repository](https://github.com/ulises-jeremias/dotfiles/tree/main/home/dot_local/share/hornero/wallpapers)
includes optional wallpaper artwork for personal Arch workstations. The
collection ranges from **Neon City** and **Vapor Dreams** to **Patagonia** and
**Fin del Mundo**. The latter are original generated artworks inspired by
glacial water, basalt, southern forest, and Beagle Channel light. When the
optional wallpaper profile is applied, images are linked under
`~/Pictures/Wallpapers/<collection>/`. The Hornero Config package owns theme
metadata and does not fetch these images.

The deployed website [Themes gallery](https://hornero-os.vercel.app/themes)
shows desktop captures for Neon City, Vapor Dreams, and Soft Morning, as well as
Hornero QA captures of Hornero Light on a Patagonian landscape and Pampa on a
grassland scene. These are labelled desktop captures; wallpaper artwork is not
presented as a screenshot of a running desktop.

## How wallpaper and colors work together

The desktop wallpaper is a visual choice. The shell can also analyse its
colors and derive a palette for dynamic appearances. Hornero keeps the image
and the generated shell palette as separate, user-visible choices. A wallpaper
change can therefore alter shell accents and surfaces while keeping the theme
name and light or dark mode. Semantic Hornero themes use curated roles; recipe
themes may use generated colors. The [Appearance guide](appearance.md)
explains the difference and the advanced controls.

Check the current state without changing it:

```sh
horneroctl wallpaper current
horneroctl appearance scheme status
horneroctl appearance colors status
horneroctl appearance doctor
```

## When a theme wallpaper is unavailable

A theme's manifest can identify a default image and a wallpaper collection
without shipping the image itself. If that media is not present, the theme is
still a theme pack; it is not evidence that the shell or theme catalog is
broken. Choose one of the images already installed or point the CLI at a
local file. Hornero does not fetch an arbitrary image on your behalf.

To inspect pack wallpaper metadata:

```sh
horneroctl appearance theme list --full
horneroctl appearance theme show vapor-dreams
```

The canonical theme and wallpaper manifest are maintained in
[HorneroOS/config](https://github.com/HorneroOS/config/tree/main/profiles/themes).
For a real product comparison across color and image directions, visit the
[Showroom](https://github.com/HorneroOS/website/tree/main/src/content/showroom).
