# ZPilot Capability Inventory

This document tracks the ZPilot product surface rather than a generic template file inventory.

| Capability | Source of truth | Current scope |
|---|---|---|
| CLI and configuration | zpilot.py | Standard-library Python 3.11+ |
| Repository discovery | zpilot.py | Nested manifests, lockfiles, instructions, workflows, tools |
| Validation adapters | zpilot.py | Conservative adapters selected from available tools |
| Agent integration | zpilot.py | OpenCode CLI |
| Convergence | zpilot.py | Bounded rounds, timeout, no-progress detection |
| Completion gate | zpilot.py | Validation, diff hygiene, Gitleaks |
| GitHub delivery | zpilot.py | Feature branch, PR, exact-head checks, approval gate |
| Local synchronization | zpilot.py | Fast-forward only after remote merge |
| CI/security | .github/workflows | CI, CodeQL, Dependency Review, Gitleaks, independent review |
| Operational contract | docs/operations.md | Prerequisites, failure recovery, evidence |

See ROADMAP.md for planned adapter and hardening work.
