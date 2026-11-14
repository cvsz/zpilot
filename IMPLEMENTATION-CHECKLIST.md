# ZPilot Production Engineering Checklist

Checked boxes indicate implemented repository artifacts or controls, not end-to-end production verification. Use ZEAZ-INTRODUCTION.md evidence states and attach exact CI/runtime evidence before closing release gates.

## Identity
- [x] Project purpose and product boundaries documented
- [ ] GitHub description, topics, and homepage reviewed by repository owner
- [ ] CODEOWNERS identifies active maintainers
- [ ] License and attribution reviewed

## Runtime and portability
- [x] Python standard-library core
- [x] Python 3.11+ requirement
- [x] Windows/macOS/Linux CI matrix
- [ ] End-to-end execution verified on each supported OS
- [ ] Windows process-tree cancellation and worktree recovery tested

## Discovery and adapters
- [x] Nested manifest discovery
- [x] Instruction and workflow inventory
- [x] Toolchain availability inventory
- [x] Existing package-script selection
- [ ] Monorepo dependency graph and package-level orchestration
- [ ] Adapter contract tests for every advertised ecosystem

## Safety and security
- [x] Read-only default
- [x] Explicit execution opt-in
- [x] Dirty source checkout rejection
- [x] Isolated worktree for agent edits
- [x] shell=False and bounded command timeouts
- [x] Gitleaks source and worktree completion gates
- [x] Filter privileged environment variables from agent subprocesses
- [x] Isolate GitHub CLI and Git credential configuration for agent subprocesses
- [x] Redact common credential patterns from task/output text
- [x] No self-approval or admin bypass
- [ ] Verify Gitleaks and GitHub secret scanning on protected test repositories
- [ ] Threat-model review of agent sandbox and network egress
- [ ] Verify branch protection/rulesets through authorized admin read-back

## Convergence and delivery
- [x] Bounded iterations and no-progress detection
- [x] Independent validation after agent repair
- [x] Feature branch push and PR creation
- [x] Exact-head check and review decision gate
- [x] Normal GitHub merge request
- [x] Remote merge read-back
- [x] Local fast-forward synchronization
- [ ] Integration tests for concurrent PR updates and branch advancement
- [ ] Resumable interrupted-run handling

## GitHub requirements
- [ ] Require repository-baseline CI
- [ ] Require CodeQL and Dependency Review where applicable
- [ ] Require verify-independent-approval
- [ ] Require at least one independent approval and dismiss stale reviews
- [ ] Require conversation resolution
- [ ] Block force-push and protected-branch deletion
- [ ] Enforce rules for administrators
- [ ] Set Actions default token permissions to read-only
- [ ] Enable Dependabot alerts/security updates
- [ ] Enable secret scanning and push protection where available
- [ ] Verify effective settings; workflow presence is not evidence of enforcement

## Operations and release
- [x] JSON run report and failure worktree preservation
- [x] Failure recovery guidance
- [ ] Validate report permissions/retention on supported hosts
- [ ] Exercise backup/recovery of long-running execution state
- [ ] Establish maintainer/on-call ownership and support expectations
- [ ] All required checks pass on exact release SHA
- [ ] Independent and security review complete
- [ ] Supported OS integration evidence attached
- [ ] No production-readiness claim until every applicable gate is VERIFIED
