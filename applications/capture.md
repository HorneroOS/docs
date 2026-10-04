# Screenshots and recording

Hornero routes screen capture commands through `horneroctl capture`. The
available screenshot and recording backends depend on which host tools are
installed and can access the Wayland session.

## Screenshots

- Press **Print** to capture the screen.
- Press **Shift + Print** to select a region.
- Preview a capture with `horneroctl capture screenshot --dry-run`.

The packaged CLI resolves the `sss` screenshot helper when it is available.
The personal dotfiles source installs `sss` with `grim` and `slurp` support.
Those packages are not dependencies of Hornero Config. Without the helper,
the screenshot command reports that its backend is missing rather than
silently installing software.

## Screen recording

The CLI and Shell expose recording actions backed by GPU Screen Recorder.
Check its available options before recording:

```sh
horneroctl capture record start --dry-run
horneroctl capture record stop --dry-run
```

Recording writes files and starts a process. Mutating commands require an
explicit `--yes`; use the documented dry-run option first when scripting.
The output folder follows the user's XDG Videos directory where available.

## Troubleshooting

- A screenshot or recording can fail if the helper is absent, the output
  directory is unwritable, or the compositor capture protocol is unavailable.
- For a region capture, check that the selector backend is installed.
- Keep recordings out of support logs unless the file has been reviewed for
  private content.

Upstream: [grim](https://github.com/emersion/grim),
[slurp](https://github.com/emersion/slurp),
[GPU Screen Recorder](https://git.dec05eba.com/gpu-screen-recorder/about/).
See also [Hornero CLI capture help](../desktop/horneroctl.md).
