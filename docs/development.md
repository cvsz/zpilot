# Development Guide

## Requirements

- Python 3.11+
- Git 2.30+
- Optional execution integrations: GitHub CLI, OpenCode, and Gitleaks
- Project-specific toolchains for the target repository

The orchestration core has no third-party Python dependency.

## Setup

    git clone https://github.com/cvsz/zpilot.git
    cd zpilot
    python zpilot.py --version
    python zpilot.py --discover-only --json

Copy .env.example to .env only when local configuration is needed. Never commit the populated file.

## Local validation

    python -m compileall -q zpilot.py scripts tests
    python -m unittest discover -s tests -v
    python zpilot.py --discover-only --json

CI is configured to run the core tests and discovery on Ubuntu, Windows, and macOS. Verify the exact workflow runs before treating portability as VERIFIED. The repository baseline also validates required files, Markdown links, and workflow syntax.

## Execution mode

Execution is explicit:

    python zpilot.py --execute --task "Describe the requested repository change" --max-iterations 3 --timeout 900 --merge-method squash

The source checkout must be clean and on a named branch. Configure GitHub CLI authentication, OpenCode, and Gitleaks first. The selected base defaults to the current branch; use --base when needed.

ZPilot does not install dependencies. Ensure required project dependencies are available before execution. Missing tools must block their adapter rather than being treated as successful checks.

## Agent behavior

The OpenCode adapter runs in an isolated worktree and receives the requested objective plus validation failures. It must not push, merge, deploy, modify GitHub settings, or weaken gates. ZPilot reruns validation independently after every repair round.

The agent is not a trusted validator. Review its diff and exact CI results.

## Configuration

- ZPILOT_AGENT: executable name/path; defaults to opencode.
- ZPILOT_REPORT: JSON report destination; defaults to ~/.zpilot/last-run.json.

The .env loader never evaluates shell syntax. Existing process variables take precedence.

## Standards

- Keep the core dependency-light.
- Use typed interfaces and explicit state transitions.
- Use subprocess argument arrays with shell disabled.
- Bound every external command with a timeout.
- Preserve unrelated work and avoid destructive cleanup.
- Add tests for parsing, discovery, adapter selection, and failure paths.
- Update architecture and operations docs when contracts change.
