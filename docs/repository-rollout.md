# ZPilot Adoption in Existing Repositories

ZPilot can inspect an existing repository without copying its governance tree or overwriting project files.

## Adoption steps

1. Read the canonical zeaz.md policy and repository-specific instructions.
2. Run ZPilot in discovery-only mode.
3. Review detected manifests, lockfiles, workflows, nested instructions, and missing adapters.
4. Identify the source of truth for each build, test, security, deployment, and release contract.
5. Add only compatible validation adapters and repository-specific documentation.
6. Preserve existing branch protection, CODEOWNERS, CI, release, and infrastructure ownership.
7. Validate on a feature branch and open a reviewable PR.

Do not bulk-copy template files, mass-deploy workflows, or propagate credentials across repositories. Each repository requires classification, scoped permissions, independent review, and its own evidence.
