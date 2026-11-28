# Hardware and features: tested and untested

HorneroOS is used daily in production across multiple physical workstations
and validated across UEFI and Legacy BIOS KVM. That statement covers the
system as a whole; each feature below keeps its own honest state, and a
daily-driven system still has concrete, declared limitations. Use this page
before assuming a specific device path works on your machine.

## Maturity by feature

| Area | State today | What that means |
| --- | --- | --- |
| Hyprland desktop | Supported (default) | Default Wayland session |
| Niri session | Supported | Scrolling Wayland compositor option |
| System rollback | Planned | Backend `none`; no restore command exists |
| Launchers beyond Steam | Planned or reference-only | Not installed support |
| Handheld and VR | Planned or experimental | No device qualified |
| Server and Agents editions | Planned | No installable image |

Edition detail lives in [Editions](../editions/README.md); the
rollback contract is in
[Updates and recovery](../desktop/updates-and-rollback.md).

## Tested

- HorneroOS runs daily in production across at least three physical
  workstations (including an ASUS ROG Strix G16 recorded `USER-VERIFIED`).
- `v0.2.0-preview42` passed both UEFI and Legacy BIOS KVM boot and
  installation validation (Desktop, Studio, Gaming) plus E2E UEFI KVM
  validation of the preinstalled Desktop QCOW2.

## Not run or uncertified per-device

- Specialized per-device checks: NVENC, Vulkan correctness, and HDMI
  capture on arbitrary hardware combinations.
- Any specific third-party NVIDIA generation, hybrid wiring, handheld,
  VR headset, audio interface, or display beyond tested machines. Your
  own check, reported with versions and logs, is the evidence that counts.

## Report your hardware

Run `horneroctl doctor`, keep `lspci -nnk` and the relevant kernel
log lines, and state the exact install path you used (firmware,
encryption, edition, compositor). Remove personal identifiers
before sharing. See
[Troubleshooting by symptom](../troubleshooting/by-symptom.md).
