# ZPilot — Autonomous Repository Engineering Orchestrator

[![CI](https://github.com/cvsz/zpilot/actions/workflows/ci.yml/badge.svg)](https://github.com/cvsz/zpilot/actions/workflows/ci.yml) [![CodeQL](https://github.com/cvsz/zpilot/actions/workflows/codeql.yml/badge.svg)](https://github.com/cvsz/zpilot/actions/workflows/codeql.yml) [![Secret Scan](https://github.com/cvsz/zpilot/actions/workflows/secret-scan.yml/badge.svg)](https://github.com/cvsz/zpilot/actions/workflows/secret-scan.yml)

ZPilot is the cross-platform engineering control plane for understanding, validating, repairing, and delivering changes to software repositories through bounded, evidence-driven automation.

## Mission

ZPilot coordinates a controlled engineering lifecycle:

1. **Discover** repository root, branch/head, working-tree state, instructions, nested projects, manifests, lockfiles, CI workflows, toolchains, and platform.
2. **Understand** ZeaZDev and repository-specific operating rules before delegating work.
3. **Plan** validation adapters from discovered manifests and existing project scripts.
4. **Implement** inside a dedicated Git worktree isolated from the operator's checkout.
5. **Converge** through bounded repair/validation rounds, timeouts, and no-progress detection.
6. **Self-heal** by passing exact failed checks to a coding agent and independently rerunning validation.
7. **Complete** only after tests, diff hygiene, and secret scanning pass.
8. **Deliver** through a feature branch and pull request, exact-head CI, and independent review.
9. **Synchronize** the local base branch using fast-forward only after GitHub confirms the remote merge.

The product-level **both** merge mode means remote pull-request merge plus local fast-forward synchronization. The GitHub merge strategy is selected separately: merge, squash, or rebase.

## Product boundaries

ZPilot is an engineering orchestrator, not a general-purpose deployment agent. It does not deploy infrastructure, rotate credentials, modify repository settings, approve its own pull requests, bypass branch protection, force-push, rewrite history, or delete operator data.

It does not silently install dependencies. It runs only discovered, available validation commands and explicit package scripts. Missing adapters and prerequisites must remain visible as unverified or blocked.

## Requirements

- Python 3.11+
- Git
- GitHub CLI (gh), authenticated for PR delivery
- OpenCode CLI for AI-assisted repair
- Gitleaks for the pre-commit secret gate

Discovery requires only Python and Git. Execution requires the integrations above and permission to push a feature branch and create/read/merge a PR. GitHub branch protection and required approvals remain authoritative.

## Quick start

    python zpilot.py --version
    python zpilot.py --discover-only --json
    python zpilot.py

The default mode is read-only discovery. Execution is explicit:

    python zpilot.py --execute --task "Describe the requested repository change" --max-iterations 3 --timeout 900 --merge-method squash

Use --base when the checkout is detached or the intended base differs from the current branch. ZPilot waits up to 24 hours by default for CI and independent review; set --review-timeout to change the bounded wait.

A dirty source checkout is rejected. Existing operator changes are never staged, reset, stashed, or overwritten. ZPilot performs agent work in a separate Git worktree and preserves that worktree for inspection when a gate fails.

## Configuration

Copy .env.example to .env for local-only settings. The loader parses assignments as data; it never sources or evaluates shell code. Process environment variables take precedence.

- ZPILOT_AGENT selects the compatible agent executable; default: opencode.
- ZPILOT_REPORT selects the JSON run-report path; default: ~/.zpilot/last-run.json.

Do not put credentials in .env or commit populated environment files. Authenticate GitHub CLI through its supported credential flow.

## Supported discovery and validation

Discovery recognizes Python, JavaScript/TypeScript, Go, Rust, Java/Maven, Java/Gradle, Kotlin, .NET, Ruby, PHP, Swift, Dart/Flutter, C/C++, Elixir, Scala, Julia, Terraform, Helm, Docker, Docker Compose, and Make.

Validation is intentionally narrower than discovery. It runs a command only when the required toolchain and manifest or package script exist. Supported adapters include Python compile/unittest, package.json scripts, go test, cargo test, dotnet test, Maven/Gradle tests, Swift/Flutter tests, Terraform formatting/validation, Compose configuration, and Helm lint. It does not invent missing scripts or install dependencies.

Monorepo discovery scans nested manifests while excluding common generated, cache, vendor, and dependency directories. Detection is not equivalent to validation coverage; adapter gaps must be disclosed.

## Architecture

- zpilot.py — standard-library CLI, dotenv loader, discovery, adapter planning, bounded convergence, worktree lifecycle, secret gate, PR delivery, and report generation.
- scripts/ — compatibility wrappers and repository administration utilities.
- tests/ — unit tests for parsing, discovery, and adapter selection.
- .github/workflows/ — cross-platform CI, CodeQL, dependency review, secret scanning, independent-review enforcement, read-only audit, and source release.
- docs/ — architecture, development, operations, security, and release contracts.
- ZEAZ-INTRODUCTION.md and zeaz.md — ecosystem operating policy and evidence semantics.

## Security model

- Read-only discovery is the default; mutation requires --execute.
- Dirty source checkouts are rejected.
- Agent edits are isolated in a dedicated Git worktree.
- Subprocesses use argument arrays, shell disabled, and bounded timeouts.
- No credentials are passed in prompts or reports.
- Gitleaks must pass before commit/push.
- Only a feature branch is pushed; protected base branches are never pushed directly.
- PR checks must pass for the current exact head SHA.
- Independent/human approval is mandatory before merge.
- GitHub enforces branch protection; ZPilot never uses an admin bypass.
- Remote merge and local fast-forward are separate completion gates.

Repository administrators must configure required status checks, independent reviewers, branch protection/rulesets, secret scanning, and least-privilege Actions permissions. Workflow files alone do not prove effective repository settings.

## Evidence and readiness

Use the canonical states in ZEAZ-INTRODUCTION.md: VERIFIED, PARTIALLY VERIFIED, UNVERIFIED, BLOCKED, and NOT APPLICABLE. Missing tools, skipped checks, unavailable permissions, and missing runtime environments cannot silently become PASS.

A successful repository run is not proof that an application has been deployed or is production ready. Application readiness also requires environment-specific security, operations, recovery, capacity, observability, ownership, and incident-response evidence.

## Development

    python -m compileall -q zpilot.py scripts tests
    python -m unittest discover -s tests -v
    python zpilot.py --discover-only --json

See docs/architecture.md, docs/development.md, docs/operations.md, docs/security.md, and docs/release.md.

## Governance

Read zeaz.md and AGENTS.md before changing this repository. Preserve ZEAZ governance, independent review, least-privilege workflows, and repository administration controls. See SECURITY.md for vulnerability reporting.

## License

MIT. See LICENSE.
