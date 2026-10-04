# Development and contribution

HorneroOS is developed across repositories. Start by identifying the layer
that owns the behavior, then read that repository's `AGENTS.md`, README, and
contributor instructions before editing.

## Choose a contributor path

- [Architecture](../architecture/README.md) — find the owner of a change.
- [Testing](testing.md) — select focused checks and graphical acceptance.
- [Contributing](contributing.md) — branch, review, and cross-repository
  expectations.
- [Internationalization](i18n.md) — current language and string contract.
- [Historical dotfiles wiki disposition](dotfiles-wiki-disposition.md) — how
  earlier knowledge was evaluated before being reused.

## Source-of-truth rule

Implement behavior in the repository that owns it. Keep this handbook
focused on user and contributor guidance; keep API details and code-level
contracts with their implementation. The website imports this repository at
a reviewed commit and owns navigation and presentation, not a parallel copy
of the documentation.

## Product truth

HorneroOS is in development. A working developer setup or component package
does not imply a supported end-user installation. Check current release and
installation status before writing guides or claims. Label preview-only
behavior and package-specific constraints explicitly.

## Report a bug

Open a focused report in the repository that owns the failing behavior. Include
the component revision, expected and actual result, shortest reproduction,
and the first relevant sanitized error lines. Never attach private screenshots
or full personal logs.

- [Shell](https://github.com/HorneroOS/shell/issues) — desktop and Settings.
- [Config](https://github.com/HorneroOS/config/issues) — defaults and theme packs.
- [horneroctl](https://github.com/HorneroOS/hornero/issues) — CLI behavior.
- [Website](https://github.com/HorneroOS/website/issues) — public pages and
  docs presentation.
