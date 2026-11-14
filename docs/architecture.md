# ZPilot Architecture

## 1. Purpose

ZPilot is a cross-platform repository engineering orchestrator. It coordinates repository discovery, validation, isolated repair, pull-request delivery, and local synchronization. It is not an application deployment runtime.

## 2. Principles

- Discovery precedes mutation.
- ZEAZ and repository-local instructions govern agent work.
- A standard-library core minimizes dependencies and bootstrap cost.
- The operator checkout is protected from agent edits.
- Loops, subprocesses, scans, and waits are bounded.
- The agent proposes changes; independent validators establish evidence.
- GitHub branch protection and independent review remain authoritative.
- Unknown capability is blocked or unverified, never passed.

## 3. Components

### CLI and configuration

The CLI validates arguments, resolves the Git root, loads .env as inert key/value data, and preserves process-environment precedence. It does not evaluate shell syntax.

### Repository discovery

The engine inventories root and nested project manifests, lockfiles, package-manager hints, Git branch/head/remotes/working-tree state, GitHub Actions workflows, agent instruction files, available toolchains, and operating-system details. Generated/vendor/cache directories are excluded. Discovery is bounded and reports truncation.

### Validation adapters

Adapters are selected from discovered manifests and installed executables. Existing package scripts are preferred over invented commands. ZPilot does not install dependencies. A discovered ecosystem without a validated adapter remains a coverage gap.

### Isolated execution workspace

Execution requires a clean source checkout. ZPilot fetches the selected base and creates a dedicated Git worktree and feature branch. Agent edits do not occur in the operator's working directory. Failed worktrees are preserved.

### Agent repair

OpenCode receives the requested task and exact validation failures. The prompt prohibits push, merge, deployment, credential operations, destructive changes, and security-gate weakening. High-privilege environment variables are filtered; GitHub CLI config and Git global/system credential helpers are isolated. Common credential patterns are redacted from prompts and reports. Agent output is untrusted and never accepted as proof.

### Convergence controller

Each iteration executes the validation plan. Failures are passed to the repair adapter. The controller stops on success, maximum iterations, command timeout, agent failure, or unchanged-worktree detection. Infinite retries are not permitted.

### Completion gate

Before commit, ZPilot requires passing applicable validations, a non-empty change set, diff hygiene, and Gitleaks secret scanning. Missing Gitleaks blocks commit and push.

### GitHub delivery

ZPilot pushes only a feature branch and opens a PR. It waits for GitHub checks, verifies the exact PR head SHA and base, requires an approved review decision, and requests a normal GitHub merge. It never uses an admin bypass or force operation.

### Local synchronization

After reading back the remote merged state, ZPilot fetches the base branch and uses git merge --ff-only. A divergent local branch is not rewritten; synchronization is blocked and reported.

## 4. Sequence

1. Resolve repository root and read-only inventory.
2. Reject dirty source checkout for execution.
3. Fetch the base branch and verify local history is not ahead/diverged.
4. Create isolated worktree and feature branch.
5. Build validation plan from manifests, package scripts, and installed tools.
6. Run the requested task in the agent worktree.
7. Execute checks; repair failures within the configured bound.
8. Run secret and diff gates.
9. Commit in the worktree and push the feature branch.
10. Create/read back the PR.
11. Wait for exact-head checks and required review decision.
12. Request normal GitHub merge; GitHub enforces repository rules.
13. Verify remote merge and fast-forward the local base.
14. Persist a JSON report outside the repository.

## 5. Evidence

Reports contain timestamps, source/base/feature refs, exact head SHA, per-round results, gate states, PR URL, and merge/synchronization outcomes. Reports must not contain credentials or raw secret-scanner output.

Evidence states are defined centrally in ZEAZ-INTRODUCTION.md. Implementation, verification, deployment, and production readiness are distinct.

## 6. Failure handling

- Missing executable: BLOCKED.
- Invalid manifest: recorded; adapter selection may be unavailable.
- Validation failure: bounded repair path.
- No progress: stop and preserve worktree.
- Missing Gitleaks: stop before commit.
- Push/PR/check/review/merge denial: leave branch/worktree available for human action.
- Remote merge succeeded but local fast-forward failed: remote merge remains verified; local synchronization is blocked. Never reset local state.

## 7. Trust boundaries

Repository files, package scripts, build systems, test code, workflow definitions, agent output, PR content, and logs are untrusted inputs. Validation commands execute project code; run them only against repositories the operator is authorized to execute. A Git worktree is isolation from the source checkout, not a security sandbox. Use host/container isolation and credential scoping for untrusted repositories.

## 8. Limitations

Discovery is broader than automatic validation. CI must verify each supported OS. GitHub CLI output and branch rules can vary by repository policy; GitHub's final merge response is authoritative. No adapter claims production deployment or runtime readiness.
