# Infrastructure

Guides for evaluating hosting providers and deploying the self-hosted or cloud
**HorneroOS Browser Playground** (`HorneroOS/playground`).

> **Scope note:** End users who want to test HorneroOS without managing servers
> should start at [Try HorneroOS without installing](../getting-started/try-horneroos.md).
> Infrastructure deployment documents target operators deploying the
> ephemeral KVM and WebRTC stack tracked under `HorneroOS/playground#1`.

## Guides

- [Cloud provider decision kit](cloud-provider-decision-kit.md) — verified
  provider matrix (DistroSea, AWS Open Source Credits, OSUOSL, Google Cloud,
  AWS EC2, OVHcloud/Kimsufi Eco, and Hetzner Dedicated), Buenos Aires RTT
  latency, budget scenarios, zero-spend commitment, and DistroSea summary.
- [Playground deployment runbook](playground-deployment-runbook.md) — remaining
  post-selection checklist and the 19-step final cloud deployment, validation,
  and emergency kill-switch procedure.

## Related architecture

- [ADR: Hornero Playground architecture](../architecture/adr-hornero-playground.md)
- [Hornero Playground threat model](../architecture/hornero-playground-threat-model.md)
