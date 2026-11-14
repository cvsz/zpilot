# ZPilot Roadmap

## Foundation

- [x] Cross-platform Python CLI foundation
- [x] Safe dotenv parsing with process-environment precedence
- [x] Repository and monorepo manifest discovery
- [x] Git state, instructions, workflow, and toolchain inventory
- [x] Read-only discovery mode and JSON output
- [x] Stack-aware validation adapter selection
- [x] Isolated worktree execution
- [x] Bounded convergence and no-progress detection
- [x] OpenCode repair adapter with independent revalidation
- [x] Gitleaks completion gate
- [x] Feature branch and pull-request delivery
- [x] Exact-head CI and independent-review gate
- [x] Normal GitHub merge and local fast-forward semantics
- [x] JSON execution report
- [x] Cross-platform CI baseline

## Hardening

- [ ] Verify end-to-end execution on Ubuntu, Windows, and macOS with isolated GitHub test repositories
- [ ] Add integration tests for GitHub CLI output/version compatibility
- [ ] Add adapter contract tests and explicit unavailable-state reporting
- [ ] Add monorepo workspace graph and per-package execution
- [ ] Add process-tree cancellation and graceful timeout handling on Windows
- [ ] Add configurable sandbox/container execution profiles
- [ ] Add SARIF aggregation and signed run evidence
- [ ] Add optional SBOM/provenance generation
- [ ] Add branch-ruleset read-back integration where API permissions permit
- [ ] Add resumable run state and idempotency for interrupted delivery
- [ ] Add benchmark fixtures for representative repositories

## Non-goals

- Bypassing required reviews or branch protection
- Self-approval or fabricated independent review
- Force push or history rewriting
- Implicit dependency installation
- Production deployment or infrastructure apply
- Credential rotation or secrets-manager replacement
- Claiming production readiness from green CI alone
