# Contributing to ZPilot

## Development workflow

1. Read zeaz.md, AGENTS.md, and applicable nested instructions.
2. Inspect the exact branch, HEAD, worktree, manifests, workflows, and existing implementation.
3. Create a focused feature branch.
4. Keep changes small and reviewable.
5. Add or update tests for behavior changes.
6. Run compile, unit tests, repository validation, and relevant adapter tests.
7. Update documentation and CHANGELOG.md when behavior or contracts change.
8. Open a pull request and complete the review checklist.

## Requirements

- Python 3.11+ for the orchestration core.
- Standard-library-first implementation unless a reviewed requirement justifies a dependency.
- English for source, configuration, filenames, commit messages, and technical documentation.
- Subprocess calls use argument arrays and shell=False.
- External operations have explicit timeouts and error handling.
- No implicit dependency installation.
- Preserve unrelated work and avoid destructive cleanup.

## Local checks

    python -m compileall -q zpilot.py scripts tests
    python -m unittest discover -s tests -v
    python zpilot.py --discover-only --json
    python scripts/validate_repo.py

## Pull requests

Describe objective, scope, design, tests, security impact, compatibility, operational impact, and rollback. Identify any checks that are blocked or not applicable.

ZPilot-generated changes must be independently reviewed. The author and coding agent must not approve their own pull request. Required checks must pass for the exact current head.

## Security

Do not report exploitable vulnerabilities in public issues. Follow SECURITY.md. Never commit credentials, populated .env files, private keys, personal data, or production data.
