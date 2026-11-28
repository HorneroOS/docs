# Flujo de producción para YouTube y contenido

- **Resolución base:** Full HD `1920×1080` a `60 FPS` (`scale = 1.0`)
- **Variantes soportadas:** QHD (`2560×1440`), 4K UHD (`3840×2160`), Shorts
  verticales (`1080×1920`, `9:16`)
- **Herramientas principales:** Hornero Demo Studio, `hornero-presenter`, OBS
  Studio, PipeWire, Portales XDG Desktop y Kdenlive

Este flujo convierte una sesión limpia de HorneroOS (en escritorio o VM VirGL)
en un video listo para YouTube con lista de capítulos, subtítulos, miniaturas y
un proyecto editable de **Kdenlive (`.kdenlive`)**, sin filtrar notificaciones,
datos privados del host ni habilitar por accidente micrófono o cámara.

---

## 1. Privacidad y preparación antes de grabar

Cada captura de Hornero Demo Studio sigue reglas estrictas de privacidad:

1. **Nunca auto-habilitar micrófono ni cámara.** Ambos dispositivos quedan
   silenciados o desconectados por defecto. Quien graba habilita la entrada
   manualmente solo cuando graba locución o cámara:

   ```sh
   horneroctl hardware mic status
   horneroctl hardware mic toggle
   ```

2. **Usá un usuario demo o un overlay limpio de Playground.** Nunca grabes
   desde una cuenta personal con claves SSH, cookies de navegador, redes Wi-Fi
   ni tokens reales. Usá `build-vm-image.sh --demo` o
   `demo/apply-demo-overlay.sh` para obtener un workspace `hornero` curado.
3. **Activá el Modo Presentador y limpiá el historial de avisos:**

   ```sh
   qs ipc call notifs clear
   hornero-presenter on
   horneroctl mode set studio
   ```

   `hornero-presenter on` guarda tu estado previo de No Molestar en Quickshell,
   ejecuta `qs ipc call notifs enableDnd` y verifica escala `1.0`. Al terminar,
   restaurá todo con:

   ```sh
   hornero-presenter off
   horneroctl mode set signal
   ```

---

## 2. Perfiles de captura y resoluciones objetivo

Alineá el monitor de salida antes de abrir OBS Studio para que la tipografía
(IBM Plex) y los marcos Signal escalen idénticos entre tomas:

| Perfil | Geometría | Escala | FPS | Mejor para |
| --- | --- | --- | --- | --- |
| **Base Full HD** | `1920×1080` | `1.0` | `60` | Docs oficiales y tours |
| **QHD** | `2560×1440` | `1.0` | `60` | Código / DAW multi-ventana |
| **4K UHD** | `3840×2160` | `1.5`/`2.0` | `60` | Vitrina HiDPI y zooms |
| **Vertical** | `1080×1920` | `1.0` | `60` | YouTube Shorts y Reels |

Verificá el modo activo de pantalla antes de grabar:

```sh
hyprctl monitors       # En Hyprland
niri msg outputs       # En Niri (experimental)
```

---

## 3. OBS Studio, PipeWire y Portales XDG Desktop

HorneroOS es Wayland-first, así que OBS captura cuadros y audio mediante
portales estándar en lugar de capturas X11 de ventana raíz:

1. **Fuente de video (XDG Desktop Portal):**
   - En **Hyprland**, `xdg-desktop-portal-hyprland` provee la fuente **Captura
     de pantalla (PipeWire)** dentro de OBS (`obs-studio`, `ffmpeg`).
   - En **Niri**, `xdg-desktop-portal-gnome` expone el mismo stream de portal.
   - Activá **Mostrar cursor** de forma explícita para tutoriales, u ocultalo
     para tomas B-roll limpias.
2. **Separá el bitrate de streaming interactivo del master local de alta
   calidad:**
   - **Grabación master local (fuente para edición):** Usá **MKV (Matroska)**
     con VA-API / NVENC por hardware (`CQP 16–18`) o `x264` (`CRF 16`,
     `veryfast`) para que un reinicio inesperado del compositor nunca corrompa
     el archivo. Remultiplexá a MP4 recién al cerrar la toma.
   - **Stream o preview interactivo:** Mantené los encoders RTMP/WebRTC en
     bitrate constante (**CBR 6000–8000 kbps** para `1080p60`) en una **pista
     de codificador separada** en OBS, así los masters locales jamás heredan
     artefactos de compresión de red.
3. **Pistas de audio independientes (Escritorio + Micrófono opcional):**
   - Activá el kit reversible de ruteo PipeWire de Hornero Studio (sin cambios
     permanentes en el sistema):

     ```sh
     horneroctl studio routing enable live-call
     horneroctl studio routing status
     ```

   - Asigná la **Pista 1** a monitoreo combinado (opcional) o reservá la
     **Pista 2** exclusivamente para **Audio de escritorio / sistema** (sink
     PipeWire) y la **Pista 3** exclusivamente para **Micrófono** (solo cuando
     lo desmuteás a mano).
   - Mantené **Pista 2** y **Pista 3** separadas en Kdenlive para nivelar o
     aplicar ducking a música, efectos del sistema y voz sin volver a grabar.

   Revertí el ruteo al finalizar:

   ```sh
   horneroctl studio routing disable live-call
   ```

---

## 4. Diez escenarios de YouTube listos para grabar

Cada escenario tiene un objetivo determinista de escena, layout y resolución
base (`1920×1080` a `60 FPS`, salvo el escenario Vertical):

| # | ID de escenario | Título | Tamaño | Dur. |
| --- | --- | --- | --- | --- |
| 1 | `yt-01-first-flight` | First Flight y Welcome | `1080p` | 3–4m |
| 2 | `yt-02-signal-chromatic` | Signal y 24 temas | `1080p` | 4–5m |
| 3 | `yt-03-hyprland-niri` | Hyprland + Niri dual | `1080p` | 4–6m |
| 4 | `yt-04-layouts-modes` | Layouts y Modos | `1080p` | 3–4m |
| 5 | `yt-05-hornero-apps` | Hornero Apps (`main`) | `1080p` | 3–5m |
| 6 | `yt-06-horneroctl-cli` | Tour con `horneroctl` | `1080p` | 5–6m |
| 7 | `yt-07-studio-routing` | Studio: PipeWire | `1080p` | 5–7m |
| 8 | `yt-08-gaming-edition` | Gaming y MangoHud | `1080p` | 4–6m |
| 9 | `yt-09-try-playground` | Probá HorneroOS | `1080p` | 3–4m |
| 10 | `yt-10-short-theme-flip` | Temas en 60s (Short) | `1080×1920` | 45s |

### Desglose de cobertura por escenario

- **`yt-01-first-flight`:** `hornero-greeter`, Welcome Center y selectores de
  tema y layout.
- **`yt-02-signal-chromatic`:** `hornero-signal-night`/`day`/`contrast` y
  paletas dinámicas Chromatic v3.
- **`yt-03-hyprland-niri`:** atajos tiling de Hyprland, cinta desplazable de
  Niri y `Super + Return` / `Super + D`.
- **`yt-04-layouts-modes`:** `horneroctl shell preset` y modos `Signal`,
  `Focus`, `Studio` y `Gaming`.
- **`yt-05-hornero-apps`:** `horneroctl store list`, Apps Store y perfiles
  curados de estación de trabajo.
- **`yt-06-horneroctl-cli`:** flujos con `doctor`, `appearance`, `mode`,
  `profile` y `capture`.
- **`yt-07-studio-routing`:** `horneroctl studio doctor`, aislamiento DAW +
  micrófono + OBS.
- **`yt-08-gaming-edition`:** `horneroctl gaming doctor`, opciones de
  lanzamiento y límites honestos.
- **`yt-09-try-playground`:** Browser Playground WebRTC, Quickemu
  `horneroos.conf` y camino Live USB.
- **`yt-10-short-theme-flip`:** paso rápido 9:16 por Night, Day, Dusk y
  Cockpit Clear.

> **Regla de verdad del producto:** Al grabar el Escenario 5 (Hornero Apps) o
> flujos de Niri/Studio/Gaming, indicá en pantalla y en la descripción qué está
> en **Preview**, qué es **Experimental** (`Niri`) y qué vive en `main` frente
> a la ISO `v0.2.0-preview32`.

---

## 5. Proyecto Kdenlive, capítulos, subtítulos y miniaturas

Una vez reunidas las tomas MKV crudas y las capturas opcionales con
`horneroctl capture screenshot`, Hornero Demo Studio ordena la postproducción
en cuatro entregables:

1. **Paquete editable `.kdenlive`:**
   - Ubicá el video master en `V1`, placas de título/llamados (con IBM Plex
     Sans / Mono y tokens Signal) en `V2`, audio de escritorio aislado en `A1`
     y locución de micrófono en `A2`.
   - Usá rutas relativas a la carpeta del proyecto para que cualquier maintainer
     pueda reabrir, reeditar o localizar el proyecto XML `.kdenlive` sin clips
     rotos.
2. **Capítulos de YouTube (`chapters.txt`):**
   - Exportá las guías de línea de tiempo desde Kdenlive (`00:00 Intro`, `00:35
     First Flight`, etc.) arrancando en `00:00` con >= 10 s de separación para
     los capítulos de la descripción.
3. **Subtítulos (`subtitles.en.srt`, `subtitles.es.srt`):**
   - Exportá archivos `.srt` limpios junto al video para ofrecer accesibilidad
     bilingüe EN/ES nativa en YouTube sin quemar subtítulos fijos en imagen.
4. **Miniaturas (`thumbnail-1080p.png`, `thumbnail-720p.png`):**
   - Sacá capturas PNG nítidas (`1920×1080` master y `1280×720` para subida a
     YouTube) directo dentro de la sesión con `horneroctl capture screenshot`
     (o captura visual `hornero-qa` en `1920×1080`)—nunca reescaladas desde
     cuadros comprimidos de video.

### Checklist previo a publicar

- [ ] No aparecen nombres de usuario personales, IPs LAN, SSIDs Wi-Fi, correos
  ni tokens de API en historial de terminal, notificaciones o archivos.
- [ ] El micrófono y la cámara permanecen apagados en todas las tomas mudas o
  automatizadas.
- [ ] El audio de escritorio (`A1`) y el de micrófono (`A2`) están nivelados y
  sin saturación (`<= -1 dBTP`).
- [ ] Se guardaron `.kdenlive`, `chapters.txt`, `.srt` y las miniaturas PNG con
  el mismo ID de escenario.
- [ ] Desactivaste el Modo Presentador (`hornero-presenter off`).

---

## Guías relacionadas

- [Estaciones virtuales, perfiles de pantalla y fábrica de capturas](../contributing/virtual-workstations-and-screenshots.md)
- [Studio: ruteo en vivo para mic, guitarra, DAW, Discord y OBS](../applications/studio-live-routing.md)
- [Capturas y grabación](../applications/capture.md)
- [Probá HorneroOS sin instalar](../getting-started/try-horneroos.md)
