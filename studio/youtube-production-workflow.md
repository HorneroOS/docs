# YouTube and content production workflow

- **Baseline resolution:** Full HD `1920×1080` at `60 FPS` (`scale = 1.0`)
- **Supported variants:** QHD (`2560×1440`), 4K UHD (`3840×2160`), Vertical
  Shorts (`1080×1920`, `9:16`)
- **Primary tools:** Hornero Demo Studio, `hornero-presenter`, OBS Studio,
  PipeWire, XDG Desktop Portals, and Kdenlive

This workflow turns a clean HorneroOS desktop or VirGL VM session into a
publish-ready YouTube video, chapter list, subtitle track, thumbnail set, and
editable **Kdenlive (`.kdenlive`)** project—without leaking notifications,
private host data, or accidental microphone/camera input.

---

## 1. Privacy and staging defaults before recording

Every Hornero Demo Studio capture follows strict privacy and staging hygiene:

1. **Never auto-enable microphone or camera.** Both devices remain muted or
   disconnected by default. Creators explicitly arm an input only when shooting
   voiceover or camera segments:

   ```sh
   horneroctl hardware mic status
   horneroctl hardware mic toggle
   ```

2. **Use a demo user or clean Playground overlay.** Never record from a host
   account holding SSH keys, browser cookies, Wi-Fi SSIDs, or personal tokens.
   Use `build-vm-image.sh --demo` or `demo/apply-demo-overlay.sh` for a seeded
   `hornero` workspace.
3. **Enable Presenter Mode and clear notification history:**

   ```sh
   qs ipc call notifs clear
   hornero-presenter on
   horneroctl mode set studio
   ```

   `hornero-presenter on` saves your prior Quickshell Do Not Disturb setting,
   runs `qs ipc call notifs enableDnd`, and verifies output scale `1.0`. When
   done, restore your prior state with:

   ```sh
   hornero-presenter off
   horneroctl mode set signal
   ```

---

## 2. Capture profiles and resolution targets

Match the output monitor before opening OBS Studio so UI typography (IBM Plex)
and Signal bezels scale identically across takes:

| Profile | Geometry | Scale | FPS | Best For |
| --- | --- | --- | --- | --- |
| **Full HD Base** | `1920×1080` | `1.0` | `60` | Docs & release tours |
| **QHD** | `2560×1440` | `1.0` | `60` | Multi-window coding / DAW |
| **4K UHD** | `3840×2160` | `1.5`/`2` | `60` | HiDPI showcase & zooms |
| **Vertical** | `1080×1920` | `1.0` | `60` | YouTube Shorts & Reels |

Verify the live display mode before hitting Record:

```sh
hyprctl monitors       # On Hyprland
niri msg outputs       # On Niri
```

---

## 3. OBS Studio, PipeWire, and XDG Desktop Portals

HorneroOS runs Wayland-first, so OBS captures composited frames and audio
through standard portals rather than X11 root-window grabs:

1. **Video source (XDG Desktop Portal):**
   - On **Hyprland**, `xdg-desktop-portal-hyprland` serves the **Screen Capture
     (PipeWire)** source in OBS (`obs-studio`, `ffmpeg`).
   - On **Niri**, `xdg-desktop-portal-gnome` provides the same portal stream.
   - Select **Show Cursor** intentionally for walkthroughs, or hide cursor for
     cinematic B-roll.
2. **Separate interactive stream bitrate from high-quality master capture:**
   - **Local master recording (editing source):** Use **MKV (Matroska)** with
     hardware VA-API / NVENC (`CQP 16–18`) or `x264` (`CRF 16`, `veryfast`),
     so an unexpected compositor restart never corrupts the file. Remux to MP4
     only after the take finishes.
   - **Interactive stream / preview:** Keep live RTMP/WebRTC stream encoders at
     constant bitrate (**CBR 6000–8000 kbps** for `1080p60`) on a **separate
     OBS encoder track** so local masters never inherit streaming compression
     artifacts.
3. **Independent audio tracks (Desktop + Optional Mic):**
   - Enable Hornero Studio's reversible PipeWire routing kit (no permanent
     system edits):

     ```sh
     horneroctl studio routing enable live-call
     horneroctl studio routing status
     ```

   - Assign **Track 1** to combined monitoring (optional) or **Track 2**
     exclusively to **Desktop / System Audio** (PipeWire sink) and **Track 3**
     exclusively to **Microphone** (only when manually unmuted).
   - Keep **Track 2** and **Track 3** isolated in Kdenlive so music, desktop
     SFX, and voiceover can be balanced or ducked independently without
     re-shooting.

   Revert routing cleanly afterwards:

   ```sh
   horneroctl studio routing disable live-call
   ```

---

## 4. Ten ready-to-shoot YouTube scenarios

Every scenario below ships with a deterministic staging goal, target layout,
and baseline resolution (`1920×1080` at `60 FPS` unless marked Vertical):

| # | Scenario ID | Title | Size | Len |
| --- | --- | --- | --- | --- |
| 1 | `yt-01-first-flight` | First Flight & Welcome | `1080p` | 3–4m |
| 2 | `yt-02-signal-chromatic` | Signal & 24 Themes | `1080p` | 4–5m |
| 3 | `yt-03-hyprland-niri` | Hyprland + Niri Dual | `1080p` | 4–6m |
| 4 | `yt-04-layouts-modes` | Bar Layouts & Modes | `1080p` | 3–4m |
| 5 | `yt-05-hornero-apps` | Hornero Apps (`main`) | `1080p` | 3–5m |
| 6 | `yt-06-horneroctl-cli` | `horneroctl` Tour | `1080p` | 5–6m |
| 7 | `yt-07-studio-routing` | Studio PipeWire | `1080p` | 5–7m |
| 8 | `yt-08-gaming-edition` | Gaming & MangoHud | `1080p` | 4–6m |
| 9 | `yt-09-try-playground` | Try HorneroOS | `1080p` | 3–4m |
| 10 | `yt-10-short-theme-flip` | 60s Theme Flip | `1080×1920` | 45s |

### Scenario coverage breakdown

- **`yt-01-first-flight`:** `hornero-greeter`, Welcome Center, theme/layout
  pickers.
- **`yt-02-signal-chromatic`:** `hornero-signal-night`/`day`/`contrast` and
  Chromatic v3 dynamic palettes.
- **`yt-03-hyprland-niri`:** Hyprland tiling binds, Niri scrollable strip,
  `Super + Return` / `Super + D`.
- **`yt-04-layouts-modes`:** `horneroctl shell preset`, `Signal`, `Focus`,
  `Studio`, and `Gaming` modes.
- **`yt-05-hornero-apps`:** `horneroctl store list`, Apps Store, and curated
  workstation profiles.
- **`yt-06-horneroctl-cli`:** `doctor`, `appearance`, `mode`, `profile`, and
  `capture` workflows.
- **`yt-07-studio-routing`:** `horneroctl studio doctor`, DAW + mic + OBS
  track isolation.
- **`yt-08-gaming-edition`:** `horneroctl gaming doctor`, launch options, and
  honest VM/hardware limits.
- **`yt-09-try-playground`:** Browser WebRTC Playground, Quickemu
  `horneroos.conf`, and Live USB path.
- **`yt-10-short-theme-flip`:** Rapid 9:16 switch across Night, Day, Dusk, and
  Cockpit Clear.

> **Honest product labeling rule:** When recording Scenario 5 (Hornero Apps) or
> Niri/Studio/Gaming workflows, state on-screen and in video descriptions what
> is **Supported** (`Desktop`, `Studio`, `Gaming`, `Hyprland`, `Niri` in
> `v0.2.0-preview42`) versus what remains **Planned** (`Server`, `Agents`,
> `Labwc`, full OS root rollback) or uncertified per-device.

---

## 5. Kdenlive project, chapters, subtitles, and thumbnails export

Once raw MKV takes and optional `horneroctl capture screenshot` stills are
collected, Hornero Demo Studio structures post-production into four outputs:

1. **Editable `.kdenlive` project bundle:**
   - Place master video on `V1`, title/callout cards (using IBM Plex Sans /
     Mono and Signal tokens) on `V2`, isolated desktop audio on `A1`, and
     voiceover mic audio on `A2`.
   - Keep timelines relative to the project folder so maintainers can re-open,
     re-cut, or localize the `.kdenlive` XML project without missing asset
     paths.
2. **YouTube chapters (`chapters.txt`):**
   - Export timeline guides from Kdenlive (`00:00 Intro`, `00:35 First Flight`,
     etc.) starting at `00:00` with >= 10 s spacing for YouTube description
     chapters.
3. **Subtitles (`subtitles.en.srt`, `subtitles.es.srt`):**
   - Export clean `.srt` captions alongside the video so bilingual EN/ES
     accessibility works natively on YouTube without burned-in hardsubs.
4. **Thumbnails (`thumbnail-1080p.png`, `thumbnail-720p.png`):**
   - Capture crisp PNG stills (`1920×1080` master and `1280×720` YouTube
     upload) directly inside the session using `horneroctl capture screenshot`
     (or `hornero-qa` visual capture on `1920×1080`)—never upscaled from
     compressed video frames.

### Final pre-publish checklist

- [ ] No personal usernames, LAN IPs, Wi-Fi SSIDs, emails, or API tokens appear
  in terminal history, notifications, or file managers.
- [ ] Microphone and camera stay off/unarmed in all silent/automated takes.
- [ ] Desktop audio (`A1`) and mic audio (`A2`) are balanced and free of
  clipping (`<= -1 dBTP`).
- [ ] `.kdenlive`, `chapters.txt`, `.srt`, and PNG thumbnails are saved with
  matching scenario IDs.
- [ ] Presenter Mode is turned back off (`hornero-presenter off`).

---

## Related guides

- [Virtual workstations, display profiles, and screenshot factory](../contributing/virtual-workstations-and-screenshots.md)
- [Studio: live routing for mic, guitar, DAW, Discord, and OBS](../applications/studio-live-routing.md)
- [Screenshots and recording](../applications/capture.md)
- [Try HorneroOS without installing](../getting-started/try-horneroos.md)
