# Studio getting started: your first project

New to HorneroOS? Start with [Getting started](../getting-started/README.md)
to download, verify and install the Preview ISO, then come back here.

From a fresh HorneroOS desktop to a first creative project with the
Studio selection you actually want — nothing more installed than you
chose. Studio is a **Preview** edition: the Preview ISO installer
installs the applications for the specializations you select, and
`horneroctl studio` records and applies reviewed configuration
building blocks. Post-install package changes through `horneroctl`
remain recorded intent in this preview, and no step here claims
otherwise.

## 1. Pick your workloads

Open **Settings → Studio** and switch on the specializations that match
your work (for example Audio & Music Production, or Streaming &
Content Creation), or pick individual applications under Custom
Selection. Prefer the terminal? The same state lives in one file and
one CLI:

```sh
horneroctl studio selection set \
  --specialization audio-music-production --application krita
horneroctl studio selection show --json
horneroctl studio doctor
```

Recording a selection installs nothing. It is the reviewed intent that
the installer and later `horneroctl` lifecycle steps consume, and you
can change it at any time — removing a workload never deletes your
files, settings, or projects.

## 2. Make the desktop yours

Apply the **Studio** layout preset from the layout picker if you want
the creator bar (media, audio slider, resources) with a reserved,
stable canvas. It is opt-in and reversible from the same picker, and
it contains no monitor or project state.

## 3. Set up audio (Balanced first)

Start on **Balanced**: it follows your interface exactly and is the
right default until you know you need less latency. The full mode,
routing, and recovery walkthrough is in
[Studio audio](studio-audio.md). Try Low Latency only as the opt-in
template described there, and go back by deleting one file.

## 4. Create the project

Use the storage layout from the Studio storage policy unless you
changed it:

- `~/Studio/Projects` — the project itself (backed up, never
  auto-deleted).
- `~/Studio/Assets` — source media (also backed up).
- `~/Studio/Scratch` — renders and intermediates (safe to clean with
  a preview).

Create your first project in your application of choice inside
`~/Studio/Projects`, keep source media in `Assets`, and point render
output at `Scratch`. That separation is what lets caches be cleaned
and projects be backed up without thinking twice.

## 5. Know the boundaries before you need them

- REAPER is proprietary and always an explicit extra choice; yabridge
  needs Wine and your own legally obtained Windows plugins. See the
  [Studio application matrix](studio.md).
- Low disk space warns at 10% free and a render should stop safely
  at 3%: clean Scratch previews first, never project media.
- Anything labelled Planned or "not QA-validated" means exactly
  that. Hardware and workflow support claims arrive with HorneroOS/qa
  acceptance evidence, not with this guide.
