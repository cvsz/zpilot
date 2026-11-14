# ZEAZ Policy and Guidance Synchronization

ZPilot does not perform unattended template synchronization or bulk policy writes.

When the canonical ZeaZDev policy changes:
1. Inspect the target repository and its local constraints.
2. Identify applicable policy changes.
3. Propose a focused feature branch and pull request.
4. Preserve stricter local rules and upstream/vendor boundaries.
5. Require independent review and exact-head CI.
6. Record the merged commit and rollout evidence.

Never mass-copy policy or propagate credentials across repositories.
