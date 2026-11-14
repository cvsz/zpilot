# Operations Runbook

## Operating modes

Discovery is the default and is read-only:

    python zpilot.py --discover-only --json

Execution is explicit:

    python zpilot.py --execute --task "Describe the change" --max-iterations 3 --timeout 900 --review-timeout 86400 --merge-method squash

Execution creates a dedicated worktree and feature branch. The source checkout must be clean. The original checkout is not changed until a verified remote merge is followed by fast-forward synchronization.

## Prerequisites

1. Confirm the repository is authorized for code execution.
2. Confirm source branch and remote origin.
3. Authenticate GitHub CLI with minimum permissions needed for feature-branch push and PR operations.
4. Install OpenCode and Gitleaks.
5. Run only against trusted repositories unless the agent is additionally isolated in a dedicated VM/container; a Git worktree is not a sandbox.
6. Require CI and independent review in branch protection/rulesets.
7. Ensure the independent reviewer is not the PR author.
8. Verify required status checks on the protected base branch.

## Convergence policy

Default maximum iterations: 3; maximum allowed: 10. Each command has a bounded timeout. Repair is triggered only by failed validations. Repeated unchanged worktree state stops the loop. Authorization failures, policy denials, and non-retryable failures are not retried.

## Merge semantics

The product-level both behavior means a normal remote PR merge followed by local fast-forward synchronization. The GitHub merge strategy is selected separately. ZPilot waits up to 24 hours by default for current-head CI and independent approval; configure --review-timeout to change the bounded wait. It never self-approves, uses an admin bypass, force-pushes, or rewrites history. If independent approval or required checks are missing, the PR remains open.

## Failure recovery

- Validation failure: inspect the preserved worktree and JSON report.
- Missing Gitleaks: install the scanner and rerun after review.
- Agent failure/no progress: inspect the worktree and use a manual repair path.
- Push/PR permission failure: preserve branch and worktree; correct permissions through the repository owner.
- Required check failure: inspect GitHub Actions logs and fix the cause; do not disable the check.
- Review missing: request an independent reviewer; do not self-approve.
- Merge denied: read GitHub's reason and satisfy repository policy.
- Remote merged/local sync blocked: inspect local branch divergence and reconcile manually; never reset or force-update local work.

## Reports

Default report: ~/.zpilot/last-run.json. Override with ZPILOT_REPORT. Reports contain operational metadata and command results; do not add secrets, tokens, or private customer data. Apply host-level access control and retention.

## Incident handling

Stop execution if credentials, private keys, customer data, or unexpected privileged access are detected. Revoke exposed credentials through the authorized owner, preserve relevant audit evidence, and follow SECURITY.md. Do not print secrets into issues or PRs.
