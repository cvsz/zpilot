# ZEAZ AI Reusable Layer

ZPilot uses the ZEAZ cross-agent execution framework while retaining its own product-specific engineering contract.

## Base contracts

- ../../zeaz.md — canonical ZeaZDev policy
- ../../AGENTS.md — repository agent contract
- ../../ZEAZ-INTRODUCTION.md — lifecycle and evidence-state definitions
- ../../CLAUDE.md — Claude Code supplement
- ../../OPENCODE.md — OpenCode supplement
- ../../GEMINI.md — Gemini CLI supplement

## Guides

- guides/ecc-integration.md
- guides/github-repository-admin.md
- guides/skill-catalog-architecture.md
- guides/harness-compatibility.md
- guides/cost-token-budget.md

## Playbooks

- playbooks/zpilot-convergence.md — bounded task execution, self-healing, completion gates, and governed delivery.
- playbooks/autonomous-repo-upgrade.md
- playbooks/repository-production-readiness.md
- playbooks/security-audit.md
- playbooks/github-pr-ci-recovery.md
- playbooks/ci-failure-modes.md
- playbooks/incident-response.md
- playbooks/saas-release.md
- playbooks/kubernetes.md

## Prompts

- prompts/universal-autonomous-engineering.md
- prompts/repository.md
- prompts/code-review.md
- prompts/architecture.md
- prompts/testing.md
- prompts/devops.md

## ZPilot operating model

ZPilot is the execution controller. Agent prompts are untrusted task inputs and do not grant additional authority. The agent edits only in an isolated worktree; independent validators establish completion evidence. GitHub review, branch protection, and repository policy remain authoritative.

Select only the guidance relevant to the task. Do not copy the entire ecosystem policy into generated prompts or override more-specific repository instructions.
