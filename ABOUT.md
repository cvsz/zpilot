# About ZPilot

**ZPilot** is the ZeaZDev cross-platform autonomous repository engineering orchestrator.

It coordinates repository discovery, architecture-aware validation, bounded AI-assisted repair, self-healing convergence, completion gates, GitHub pull-request delivery, and local branch synchronization.

## Problem

Engineering automation is fragmented across shell scripts, coding agents, CI workflows, and manual GitHub operations. Those tools often assume one operating system or language, repeat work without bounds, overwrite pre-existing changes, or treat an agent's success message as proof.

ZPilot provides one controlled lifecycle and a consistent evidence model.

## Core capabilities

- Cross-platform CLI on Linux, macOS, and Windows using Python 3.11+.
- Nested repository and monorepo discovery across common language, build, infrastructure, and container manifests.
- Safe dotenv parsing without shell evaluation; process environment has precedence.
- Repository instruction discovery, including ZEAZ policy and tool-specific agent instructions.
- Stack-aware validation planning without blind dependency installation.
- Isolated Git worktree execution to protect the operator's original checkout.
- Bounded convergence with per-command timeout, retry limit, and no-progress detection.
- OpenCode repair adapter with independent post-repair validation.
- Completion gate requiring validation, diff hygiene, and Gitleaks.
- Feature-branch push and pull-request creation through GitHub CLI.
- Exact-head CI and independent-review checks before normal GitHub merge.
- Remote PR merge followed by local fast-forward synchronization.
- Machine-readable discovery inventory and JSON execution report.

## Non-goals and safety limits

ZPilot is not a deployment platform, secrets manager, or general-purpose shell executor. It does not self-approve, bypass branch protection, force-push, rewrite history, mutate production infrastructure, rotate credentials, or clean operator worktrees. Human approval and GitHub policy remain authoritative.

## Technology

The orchestration core uses Python standard library APIs and Git. Optional integrations are GitHub CLI, OpenCode, and Gitleaks. Project-specific test/build tools are detected and invoked only when manifests, scripts, and executables are present.

## Readiness

The project targets production-oriented engineering workflows. Production readiness is evidence-backed, not a marketing claim. Each supported OS, adapter, GitHub policy configuration, and recovery path must be verified in CI or an appropriate environment before being declared verified.
