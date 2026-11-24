# Create your own desktop companion

This guide walks an artist or developer from finished artwork to a
companion walking on a HorneroOS desktop. No Shell QML knowledge is
required: a companion package is **data only** — JSON definitions
plus PNG/WebP sprites, rendered by trusted native components.
The normative contract lives in the Shell repository
(`docs/COMPANION_PLATFORM.md`); this page is the practical journey.

## 1. Prepare the artwork

- One consistent character model: same proportions, palette and
  lighting in every pose. Design for 64–256 logical pixels first;
  a beautiful 1024 px illustration that turns to mud at 128 px is
  not a desktop sprite yet.
- Transparent PNG or WebP frames on one shared canvas (for example
  512 × 512), or one sprite atlas with a regular grid. Keep every
  pose on the same ground line and record `ground`/`center` anchors.
- Only `idle` is mandatory. Add the semantic actions your character
  honestly supports (`walk`, `greet`, `sleep`, `think`, …). Missing
  actions fall back inside the same skin, never to another skin or
  character.
- Skins are complete visual variations of the same character. A
  skin that lacks an action shows its own idle instead of silently
  borrowing unclothed or differently-styled frames.

## 2. Lay out the package

```text
my-companion/
  manifest.json
  Main.qml            (canonical inert scaffold, never loaded)
  README.md
  LICENSE
  companions/<character-id>/
    companion.json
    frames/*.png
```

The plugin manifest declares PluginKit 6 and `dataOnly`:

```json
{
  "schemaVersion": 3,
  "pluginKit": 6,
  "dataOnly": true,
  "id": "my-companion",
  "name": "My Companion",
  "version": "1.0.0",
  "description": "A data-only desktop companion.",
  "author": "Your name",
  "license": "MIT",
  "entrypoint": "Main.qml",
  "placement": "background",
  "files": [
    "Main.qml", "README.md", "LICENSE",
    "companions/capi/companion.json",
    "companions/capi/frames/idle-01.png"
  ],
  "capabilities": {"processCommands": [], "networkHosts": [], "settings": {}},
  "contributes": {
    "companions": [{
      "id": "capi",
      "title": "Capi",
      "definition": "companions/capi/companion.json",
      "preview": "companions/capi/frames/idle-01.png"
    }]
  }
}
```

`Main.qml` must be byte-for-byte the canonical scaffold from the
Shell example; the host never instantiates it. Any other QML file,
process command, network host, setting, action or executable
surface rejects the data-only classification.

## 3. Write the character definition

`companion.json` is a closed, versioned document
(`schemas/companion-definition.schema.json` in the Shell repo):
localized names, author/license provenance, preview, canvas and
anchors, capabilities, skins with semantic animations, and
optionally a habitat, personalities (traits and canned lines only —
never prompts or tools) and assistant compatibility metadata.
Budgets are enforced at install time: image dimensions and decoded
pixels, frame counts and animation durations are all bounded, and
every referenced asset must be a listed package-local file. Remote
assets are rejected.

Copy `examples/plugins/example-companion` from the Shell repository
as your starting point; it ships two complete characters.

## 4. Validate and install

```bash
horneroctl plugin install-local ./my-companion --yes
horneroctl plugin enable my-companion --yes
qs ipc call plugins reload
```

Validation runs during install; the Shell validator is the
admission authority. When the install asks you to record trust
for the payload, follow its prompt before enabling.

Then open Control Center → Companions: your character appears in
the collection. **Add to desktop** creates an independent instance
with its own skin, monitor, size, habitat and reaction settings.
Removing the package keeps instance records as unavailable instead
of deleting unrelated configuration.

## 5. Publish

Community packages go through the HorneroOS/plugins catalogue flow
(manifest validation, catalogue regeneration, bilingual permission
reasons, quality record). Only publish artwork you have the rights
to redistribute; a privately installed character never needs the
catalogue. Keep the licence and attribution in the definition's
provenance — the Shell displays package authorship, it cannot grant
rights you do not have.

## Troubleshooting

- **Validation names a budget:** shrink frames or split the pack;
  the error states the exact limit that tripped.
- **Character missing in the collection:** run
  `qs ipc call plugins status` and look for the package's
  diagnostic; a malformed definition is omitted, never fatal.
- **Wrong feet position:** your `ground` anchor must sit on the
  frame's ground contact row; all poses share one canvas.
- **Washed-out edges:** export with straight alpha and clean
  mattes; avoid green spill from chroma-key sources.
