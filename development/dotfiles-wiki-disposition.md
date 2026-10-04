# Historical dotfiles wiki review

The [historical wiki in the dotfiles repository](https://github.com/ulises-jeremias/dotfiles/tree/main/docs/wiki)
was mined as input, not copied as current HorneroOS documentation. Its setup
instructions mixed product behavior with one person's hardware, applications,
package choices, scripts, and workflows. This inventory records every
Markdown page in that wiki.

## Current guidance derived from historical material

These pages offered useful subjects, but their procedures and paths were
rewritten or revalidated before publication:

- **Needs rewrite — `Audio-Devices.md`:** audio concepts may inform future
  troubleshooting; personal PipeWire setup is not a product default.
- **Needs rewrite — `CONTRIBUTING.md`:** replaced by this repository's
  repository-scoped [contribution guide](contributing.md).
- **Needs rewrite — `Customization.md`:** general customization informed
  [Appearance](../desktop/appearance.md); chezmoi steps were excluded.
- **Needs rewrite — `Hardware-nvidia-troubleshooting.md`:** generic graphics
  diagnostics inform [Hardware](../hardware/README.md); driver instructions
  require current Arch guidance.
- **Needs rewrite — `Hardware.md`:** broad hardware topics informed the new
  hardware index; machine inventory was excluded.
- **Needs rewrite — `Hyprland-Keybindings.md`:** shortcuts were checked
  against current shipped config for [Shortcuts](../desktop/shortcuts.md).
- **Needs rewrite — `Lockscreen.md`:** concepts were revalidated against the
  current Shell before including lock-screen guidance.
- **Needs rewrite — `Network-Manager.md`:** general connection diagnostics
  inform [Troubleshooting](../troubleshooting/README.md); personal scripts
  were excluded.
- **Needs rewrite — `Quickshell-Shell.md`:** shell concepts informed the
  [Desktop guide](../desktop/README.md); runtime detail stays with Shell docs.
- **Needs rewrite — `Rice-System-Theme-Management.md`:** current concepts are
  in [Appearance](../desktop/appearance.md) and
  [Wallpapers](../desktop/wallpapers.md); old state paths were discarded.
- **Needs rewrite — `Security.md`:** current privacy claims were checked
  against the Shell before inclusion in [Security](../security/README.md).
- **Needs rewrite — `Smart-Colors-System.md`:** color ideas informed current
  appearance docs; old paths and commands were discarded.
- **Needs rewrite — `Testing.md`:** replaced by [current testing
  guidance](testing.md) and the existing Hornero QA project.
- **Needs rewrite — `Window-Managers.md`:** general context is useful, but
  shipped layouts and bindings must come from current config.

## Historical, personal, or obsolete material

- **Historical — `Changelog-2025.md`:** dotfiles chronology, not HorneroOS
  release history.
- **Historical — `Home.md`:** former wiki landing page, superseded by this
  handbook and the website docs navigation.
- **Historical — `Quickshell-Parity-Checklist.md`:** old migration checklist;
  active work belongs in current issues and Shell architecture docs.
- **Historical — `Theme-Gallery.md`:** old gallery does not define the live
  theme catalogue.
- **Historical — `_Sidebar.md`:** former wiki navigation, now superseded.
- **Personal-only — `CopyQ-Customization.md`:** personal application styling,
  not a supported desktop contract.
- **Personal-only — `Hybrid-GPU-Performance.md`:** benchmarks depend on one
  laptop, GPU, display wiring, and driver state.
- **Personal-only — `Kitty.md`:** personal terminal setup and aliases.
- **Personal-only — `Nix-Home-Manager.md`:** optional personal configuration,
  not Hornero package support.
- **Personal-only — `Studio.md`:** personal audio production stack and
  provisioning scripts.
- **Personal-only — `Thunar-Side-Panel.md`:** personal file-manager bookmarks.
- **Personal-only — `Yazi.md`:** personal file-manager selection and bindings.
- **Personal-only — `Zsh.md`:** personal shell configuration, not a system
  default or CLI contract.
- **Obsolete — `Dots-Backup.md`:** retired dotfiles wrapper and naming.
- **Obsolete — `Dots-Eject.md`:** instructions for leaving a personal
  chezmoi setup; unrelated to supported product use.
- **Obsolete — `Dots-Scripts.md`:** personal script catalogue, not the OS CLI.

## Reuse rules

- Rewrite retained guidance against current packages, config, and CLI
  behavior.
- Do not copy hardware results, personal tools, provisioning scripts,
  private paths, or machine assumptions into product docs.
- Keep historical material labelled as history and separate from current
  user instructions.
- Do not revive retired `dots-*` commands. Use the current
  [horneroctl guide](../desktop/horneroctl.md) and CLI help as the command
  contract.

## Application material carried forward

The wiki's application pages were checked against current config, CLI, and
Shell sources before any workflow was added to the public handbook:

| Historical page | Source classification | Current handbook treatment |
| --- | --- | --- |
| `Kitty.md` | Personal-only | [Terminal](../applications/terminal.md) |
| `Yazi.md` | Personal-only | [Files](../applications/files.md) |
| `CopyQ-Customization.md` | Personal-only | [Clipboard](../applications/clipboard.md) |
| `Thunar-Side-Panel.md` | Personal-only | [Files](../applications/files.md) |
| `Zsh.md` | Personal-only | [Terminal](../applications/terminal.md) |
| `Audio-Devices.md` | Needs rewrite | [Media and audio](../applications/media-audio.md) |
| `Network-Manager.md` | Needs rewrite | [Connectivity](../applications/connectivity.md) |
| `Studio.md` | Personal-only | See the note below. |
| `Dots-Scripts.md` | Obsolete | [`horneroctl`](../desktop/horneroctl.md) · [Apps](../applications/README.md) |

Kitty palettes and current shortcuts were checked against Hornero Config.
Personal aliases and prompt setup remain out of product defaults. The Yazi
guide now follows the current Super+E binding and `horneroctl
apps terminal-file`; preview tools remain optional. The CopyQ guide describes
the current CopyQ/cliphist/minimal fallback and generated theme. Old commands
and unsupported sync or encryption claims were removed. Thunar bookmarks,
Zsh setup, and REAPER/Guitarix presets remain personal. Current Thunar actions
and audio integration are documented in the linked workflow pages.

Other historical pages retain the dispositions above. In particular,
NVIDIA/hybrid-GPU benchmarks, personal browser/editor choices, host package
scripts, security-tool suggestions, and machine-specific paths are not
Hornero defaults. The
[dotfiles repository](https://github.com/ulises-jeremias/dotfiles) is a useful
reference for one configured workstation, but its provisioning scripts do
not define the HorneroOS package contract.
