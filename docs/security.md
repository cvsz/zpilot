# ZPilot Security Model

## Objectives

Protect operator work, credentials, repository integrity, GitHub governance, and completion evidence.

## Controls

- Read-only discovery is the default.
- Explicit --execute is required for mutation.
- Dirty source checkouts are rejected.
- Agent modifications run in a separate Git worktree.
- Subprocess calls use argument arrays and shell=False.
- External commands have bounded timeouts.
- Dotenv is parsed as inert data, not sourced.
- High-privilege environment credentials are filtered from the agent process.
- GitHub CLI configuration and Git global/system credential helpers are isolated for agent subprocesses.
- Common credential patterns are redacted from task text, validation output, and reports.
- OpenCode's own model-auth store remains accessible to the OpenCode process; this is not a complete sandbox.
- Gitleaks must pass before commit/push.
- Only feature branches are pushed.
- Exact PR head SHA and base are rechecked before merge.
- Human/independent review is mandatory.
- GitHub branch protections are never bypassed.

## Threat model

Untrusted inputs include repository files, build scripts, package scripts, test code, workflow definitions, model output, issue/PR content, logs, and downloaded dependencies. Running repository validation can execute project code. Operators must use an isolated host/container/VM appropriate to the target repository's trust level.

A worktree protects the operator's checked-out files from agent edits, but is not a security sandbox. Agent environment filtering reduces exposure of ambient credentials, but OpenCode's own auth store and same-user files may remain accessible. Apply OS/container isolation, network egress controls, and dedicated low-privilege credentials for untrusted repositories.

## Secrets

Never embed credentials in source, prompts, reports, test fixtures, or workflow output. Use GitHub CLI's supported authentication flow. Do not expose scanner output in public PRs. Rotate credentials that were committed or logged.

## Residual risks

- A compromised local agent or repository build script may attempt actions permitted by the host.
- Gitleaks can have false positives and false negatives.
- GitHub ruleset and branch-protection configuration must be verified on the repository.
- Merge and CI state can change concurrently; GitHub remains authoritative at merge time.
- Current adapters do not provide full SAST, DAST, IaC, runtime, or production-environment assurance.

Report vulnerabilities privately using SECURITY.md.
