# Studio: AI-assisted creative production (optional)

HorneroOS Studio ships the creative applications (Kdenlive, Blender,
GIMP, Krita, Inkscape, OBS Studio, REAPER, FFmpeg/MLT). Driving them
with an AI agent is **optional** and provided by
[Agent Toolkit Creative Studio](https://github.com/ulises-jeremias/agent-toolkit/blob/main/docs/creative-studio/README.md)
(portable skills + reviewed MCP integrations, ADR-046 there). HorneroOS
does not bundle an agent runtime, does not install MCP servers or AI
models by default, and never requires them for a successful Studio
installation.

## What HorneroOS provides natively

- The Studio application catalogue and specializations (see
  [Studio applications](studio.md)); REAPER and other proprietary apps
  stay explicit opt-in.
- Typed render jobs: `horneroctl studio jobs` with allow-listed
  adapters (`blender-render`, `ffmpeg-export`, `kdenlive-render`,
  `melt-render`). Jobs run synchronously after explicit submission;
  existing output is never overwritten and sources are never modified.
  Cancellation is a recorded state transition, not a process kill.
- Read-only diagnostics: `horneroctl studio doctor` reports optional
  creative tooling (ffmpeg, ffprobe, melt, kdenlive, blender) as
  `warn` when absent — never as a failure.

## Enable AI-assisted editing (Kdenlive example)

```bash
pipx install mcp-kdenlive        # PyPI name is mcp-kdenlive
kdenlive-mcp diagnose            # must print "ready"
```

Then point your MCP-capable agent client at the `kdenlive` server with
`KDENLIVE_MCP_ALLOWED_ROOTS` set to your project directory only (see
Agent Toolkit's `mcp/templates/kdenlive/`). The agent edits a real
`.kdenlive` project you can keep editing in Kdenlive; a timestamped
backup is written before each edit.

## Security and privacy

- Creative MCP servers run locally over stdio/loopback; nothing is
  uploaded by HorneroOS for this workflow.
- Blender MCP integrations can execute Python inside Blender. Treat
  them as arbitrary code execution: enable only explicitly, work on
  copies, and keep writes inside your project directory.
- Recording, streaming and microphone access are never enabled
  automatically. OBS integrations must be started by you, per session.
- Transcription/AI models (e.g. Whisper) are large downloads and are
  never fetched silently; install them only when you choose to.

## Resources

Renders are heavy. Check `horneroctl studio doctor` and free disk/GPU
headroom first, and bound long jobs, e.g.
`systemd-run --user --scope -p MemoryMax=6G -p MemorySwapMax=0 …`.
Hardware encoding (NVENC/VAAPI) depends on your GPU and drivers;
HorneroOS does not promise it.

## Troubleshooting

- `kdenlive-mcp diagnose` not ready → install `kdenlive mlt ffmpeg`
  from the repositories and re-run.
- Job `failed` with partial output → the partial file is identified as
  partial, never a finished render; read
  `horneroctl studio jobs log <id>` (redacted on read), fix the cause,
  resubmit to a new output path.
- Job `interrupted` → a previous run ended mid-render; resubmit safely
  (outputs are never overwritten).

## Disable / uninstall

Remove the MCP entry from your agent client and
`pipx uninstall mcp-kdenlive`. Remove the Agent Toolkit
`agent-toolkit-creative-studio` product with Agent Toolkit's normal
flow. Your projects, native editor files and backups are user data and
are never deleted by uninstalling.
