# ZPilot Bounded Convergence Playbook

## Objective

Execute an authorized repository task through discovery, isolated implementation, independent validation, bounded repair, and governed pull-request delivery.

## Mandatory preflight

1. Read zeaz.md, AGENTS.md, and applicable nested/tool instructions.
2. Confirm repository identity, source branch, exact HEAD, origin, and clean worktree.
3. Discover nested manifests, lockfiles, workflows, tools, and existing test commands.
4. Identify unsupported stacks and missing prerequisites.
5. Define task scope, acceptance criteria, affected contracts, and rollback.
6. Confirm GitHub branch protection and independent reviewer requirements.

## Execution

- Default to read-only discovery.
- Require explicit execution authorization and a concrete task.
- Use a dedicated Git worktree; never edit the operator's source checkout.
- Run only existing project scripts or supported adapters.
- Never install dependencies implicitly.
- Bound every command, agent run, and convergence loop.
- Pass exact failures to the agent; rerun validation independently.
- Stop on no progress, timeout, missing security tooling, or policy denial.
- Scan secrets before commit and push only a feature branch.
- Open a PR and wait for exact-head checks and independent approval within the configured review timeout.
- Request normal GitHub merge; never bypass rules.
- Verify remote merge, then fast-forward the local base branch.

## Completion report

Include repository, base, feature branch, exact head SHA, task identifier/hash, per-round checks, security gates, PR URL, review/check state, merge method, remote merge state, local sync state, and all blocked/unverified gates.

Do not claim production readiness unless all applicable production gates are independently verified.
