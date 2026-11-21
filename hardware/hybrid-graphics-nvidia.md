# Hybrid graphics and NVIDIA

Most laptops with two GPUs render the desktop on the integrated
GPU and should run only heavy work on the dedicated NVIDIA GPU.
HorneroOS does not maintain a separate NVIDIA driver installer or
a universal hybrid-GPU profile today, and no GPU model is
qualified by this guide. What follows is how to identify your
hardware, run a program on the dedicated GPU, and report a problem
with evidence.

## Identify both GPUs first

```sh
lspci -nnk
horneroctl doctor
hyprctl monitors -j
```

Record which kernel driver is in use for each GPU and which GPU
each connected monitor is wired to. External ports are often wired
directly to the dedicated GPU; that wiring, not a setting, decides
which GPU an external display uses.

## Install the right driver for your kernel

Driver choice depends on GPU generation and kernel package. Follow
the current [ArchWiki NVIDIA guide](https://wiki.archlinux.org/title/NVIDIA)
for the driver that matches your hardware, and
[PRIME](https://wiki.archlinux.org/title/PRIME) for hybrid
rendering. Do not copy driver packages, module options or monitor
layouts from another machine guide: check them against your own
`lspci -nnk` output first.

## Run one program on the dedicated GPU

PRIME render offload runs a single program on the dedicated GPU
while the session stays on the integrated one. The environment
variables and launcher settings are the ArchWiki PRIME ones linked
above; in Steam, put the offload variables in that game's launch
options before `%command%`. Confirm it worked from the program's
own renderer or GPU report, not from the command having run.

If a game does not start only when offloaded, test it once on the
integrated GPU: that separates an offload problem from a game or
Proton problem. See [Gaming](../applications/gaming-proton-gamemode.md).

## Honest limits

- No HorneroOS NVIDIA installer and no per-model qualification
  exist today; a working report for one laptop proves nothing for
  another generation or firmware.
- NVENC, Vulkan correctness and HDMI capture were not specifically
  tested on the recorded physical-hardware acceptance. Treat them
  as unverified until your own check passes.
- A kernel update can leave the NVIDIA module unbuilt for the new
  kernel. Boot the [fallback kernel](../desktop/kernel-and-fallback.md)
  to confirm, then rebuild or report with both kernel versions.

## Report with evidence

Include both GPU models, the kernel and driver packages, whether
the failure is before or after login, and the first relevant lines
from `journalctl -b -k -p warning`. Remove usernames, hostnames,
serial numbers and network identifiers before sharing logs. See
[Troubleshooting by symptom](../troubleshooting/by-symptom.md).
