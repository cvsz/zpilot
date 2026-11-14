# ZPilot Governance

## Scope

This document defines governance for the ZPilot repository engineering orchestrator and its source, workflows, documentation, and release process.

## Roles

- **Maintainers** review changes, protect quality/security, manage releases, and maintain repository controls.
- **Contributors** propose focused changes through issues and pull requests and follow CONTRIBUTING.md.
- **Security contacts** receive vulnerability reports through the private path defined in SECURITY.md.
- **Repository administrators** maintain branch/ruleset, Actions, security-feature, and emergency-access settings.

## Change control

Normal changes flow through pull requests with required checks and independent review. Repository administration controls should be verified with:

    python3 scripts/github_admin.py --repo cvsz/zpilot --verify

A document or workflow does not prove that branch protection or security settings are effective.

## Decisions

Significant architecture, security, compatibility, data, or operational decisions should use an ADR under docs/adr/. Decisions affecting public CLI contracts, adapters, GitHub delivery, merge semantics, or report schema require maintainer review and evidence appropriate to risk.

## Emergency changes

Emergency changes use the smallest reversible scope, record the reason and operator, preserve security controls, and receive retrospective review. Routine bypass of required checks or protected-branch controls is prohibited.

## Conflicts of interest

Reviewers disclose material conflicts and avoid sole approval when independent review is reasonably available. An agent must never attest to its own independent review.

## Evidence and readiness

Governance approval, accepted risk, and production readiness are separate concepts. Accepted risk never converts an unverified readiness gate into VERIFIED. Use the canonical evidence states in ZEAZ-INTRODUCTION.md.

## Amendments

Governance changes are made by pull request and explain rationale, impact, migration expectations, validation, and rollback.
