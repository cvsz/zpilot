# Start Using ZPilot

## Requirements

Install Python 3.11+, Git, and (for execution) GitHub CLI, OpenCode, and Gitleaks.

## Clone and inspect

    git clone https://github.com/cvsz/zpilot.git
    cd zpilot
    python zpilot.py --version
    python zpilot.py --discover-only --json

Discovery is read-only and requires no GitHub authentication.

## Configure integrations

Authenticate GitHub CLI using its supported login flow. Install OpenCode and Gitleaks. Copy .env.example to .env only if you need to select an alternate agent executable or report path.

Do not put secrets in .env. Process environment takes precedence.

## Execute a task

Start from a clean source checkout:

    python zpilot.py --execute --task "Describe the engineering objective" --max-iterations 3 --timeout 900 --merge-method squash

ZPilot creates an isolated worktree and feature branch, implements the task, runs supported validation, performs bounded repair, scans secrets, opens a PR, waits for CI and independent review, requests a normal merge, then fast-forwards the local base branch.

## Verify operations

Read docs/operations.md and IMPLEMENTATION-CHECKLIST.md. Configure branch protection and independent reviewers in GitHub. Workflow files alone do not enforce repository settings.

## Container discovery

    docker build -t zpilot:local .
    docker run --rm -v "$PWD:/workspace:ro" zpilot:local

The container is read-only discovery only. It does not include GitHub CLI, OpenCode, or Gitleaks and cannot execute repair or PR delivery.
