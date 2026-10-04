# Contributing

HorneroOS changes are reviewed in the repository that owns them. Before
starting, check open pull requests and issues so that parallel work is not
duplicated, and read that repository's current contribution instructions.

## A focused contribution

1. State the user problem and expected behavior.
2. Identify the owning repository and any downstream consumers.
3. Make a focused branch from the canonical repository's current `main`.
4. Follow the repository's style and test instructions.
5. For visual work, include before/after runtime evidence and exercise the
   changed interaction.
6. Update user documentation and product data when their truth changes.
7. Request review and resolve findings before merging.

For cross-repository work, land the source-of-truth change first, then update
consumers to reviewed revisions. Preserve contributor authorship when moving
existing work. Do not force-push over work you do not own or bypass repository
branch protections.

Use [Testing](testing.md) to choose acceptance evidence and
[Architecture](../architecture/README.md) to identify ownership.
