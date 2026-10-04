# Clipboard

The Wayland clipboard has two parts: the current copied item, provided by
Wayland clipboard tools, and an optional history manager. Hornero's session
configuration records text and image clipboard selections with `cliphist`
when the needed tools are installed.

## Open clipboard history

Press **Super + V** or run:

```sh
horneroctl capture clipboard
```

The CLI chooses an available backend. On Wayland it prefers CopyQ, then
`cliphist`, then a minimal current-clipboard read. CopyQ opens its GUI. The
`cliphist` CLI path lists recent entries; it is not an interactive picker.
The minimal fallback displays a short text preview and does not provide
history.

## What Hornero configures

CopyQ is an optional dependency of `hornero-config`, which provides its base
configuration under `~/.config/copyq/`. The appearance pipeline can generate
a matching CopyQ palette. `cliphist` and `wl-clipboard` are separate host
packages; the personal dotfiles session starts text and image history
collection with `wl-paste --watch`.

Clipboard contents may include passwords, tokens, or private text. Treat
history as sensitive data. Review CopyQ's retention and privacy settings and
clear items you do not want to keep. Hornero does not promise encrypted
clipboard history or cross-device synchronization.

Troubleshooting:

- If history is empty, check whether a history backend is installed and
  whether the session collector is running.
- If CopyQ does not open, run `horneroctl capture clipboard --backend copyq`
  and verify that CopyQ starts independently.
- If CopyQ's colors are stale, reapply the active theme from Appearance
  Settings.

Upstream: [CopyQ manual](https://copyq.readthedocs.io/en/latest/),
[cliphist](https://github.com/sentriz/cliphist),
[wl-clipboard](https://github.com/bugaevc/wl-clipboard).
