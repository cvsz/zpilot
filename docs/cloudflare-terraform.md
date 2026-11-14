# Cloudflare and Terraform Ownership Boundary

ZPilot does not own public DNS, Cloudflare zones, shared tunnels, or Terraform state. These resources must remain in the single infrastructure repository designated by ZeaZDev.

## Boundary

- ZPilot may discover Terraform and Cloudflare manifests as repository inputs.
- ZPilot must not create, import, apply, destroy, or mutate DNS, tunnel, network, or cloud resources.
- A task that touches shared infrastructure must be handled in the designated infrastructure repository with its own plan, review, approval, and rollback.
- Never copy credentials, provider state, tunnel tokens, certificates, or sensitive plan output into ZPilot.

## Requesting infrastructure work

1. Identify the authoritative infrastructure repository and resource owner.
2. Inspect current source and provider state.
3. Prepare a focused change in the owning repository.
4. Review the plan for unrelated modifications and destructive actions.
5. Require maintainer approval before apply.
6. Verify both control-plane state and data-plane health.
7. Record rollback and recovery evidence.

A successful ZPilot repository run is not authorization to apply infrastructure changes.
