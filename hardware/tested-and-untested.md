# Hardware and features: tested, VM-only and untested

HorneroOS is used and maintained daily. That statement covers the
system as a whole; each feature below keeps its own honest state,
and a daily-use system still has concrete, declared limitations.
Use this page before assuming a path works on your machine.

## Maturity by feature

| Area | State today | What that means |
| --- | --- | --- |
| Hyprland desktop | Validated default | Default session of the ISO |
| Niri session | Experimental | Single-output VM surface, no desktop parity |
| System rollback | Planned | Backend `none`; no restore command exists |
| Launchers beyond Steam | Planned or reference-only | Not installed support |
| Handheld and VR | Planned or experimental | No device qualified |
| Server and Agents editions | Planned | No installable image |

Edition detail lives in [Editions](../editions/README.md); the
rollback contract is in
[Updates and recovery](../desktop/updates-and-rollback.md).

## Tested

- Desktop, Studio and Gaming UEFI unencrypted installs passed on
  the v0.2.0-preview32 ISO in disposable virtual machines.
- One ASUS ROG Strix G16 workstation is recorded USER-VERIFIED on
  preview24 plus post-install fixes in HorneroOS/qa. That is one
  machine, on an older artifact.

## VM-only or not run on the published ISO

- The preview32 artifact has no physical-hardware validation.
- LUKS-encrypted installs, legacy BIOS, Niri sessions in the ISO
  and copy-to-RAM were not run on preview32 and must not be carried
  forward as passed.

## Not specifically tested

- NVENC, Vulkan correctness and HDMI capture on the recorded
  hardware acceptance.
- Any specific NVIDIA generation, hybrid wiring, handheld, VR
  headset, audio interface or display. Your own check, reported
  with versions and logs, is the evidence that counts.

## Report your hardware

Run `horneroctl doctor`, keep `lspci -nnk` and the relevant kernel
log lines, and state the exact install path you used (firmware,
encryption, edition, compositor). Remove personal identifiers
before sharing. See
[Troubleshooting by symptom](../troubleshooting/by-symptom.md).
