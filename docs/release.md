# Release Process

## Versioning

Use Semantic Versioning. The current CLI reports version 1.0.0. Breaking changes to command-line flags, report schema, adapter behavior, or merge semantics require a major version increment.

## Admission

1. Confirm the exact release commit and tag.
2. Require configured CI/security workflows on the exact commit.
3. Require independent review and resolved conversations.
4. Verify repository rules and release permissions.
5. Run unit and cross-platform CI.
6. Review dependency and secret-scan results.
7. Update CHANGELOG.md and compatibility notes.
8. Disclose known limitations and evidence states.

## Publication

The release workflow creates a source release from an existing tag after verifying that the tagged commit is reachable from the protected default branch. It does not deploy services or publish packages.

## Rollback

For a CLI release, deprecate the affected release through an authorized maintainer, publish a corrected patch release, and communicate breaking behavior. Do not rewrite protected history. Existing execution worktrees and JSON reports remain operator-managed.

## Production readiness

A successful release workflow proves only source-release admission. It does not prove production deployment, host isolation, external integration reliability, or readiness of repositories processed by ZPilot.
