# ZPilot Security Policy

## Reporting a vulnerability

Do not disclose exploitable vulnerabilities in public issues, pull requests, discussions, commit messages, logs, or generated evidence bundles.

Use GitHub private vulnerability reporting/security advisories when enabled, or the repository's documented private security contact.

Include affected versions/commits, reproduction details, impact, prerequisites, and suggested remediation when available.

## Supported versions

Security fixes target the latest supported release and the active default branch. Maintainers will document additional support windows when established.

## Security controls

ZPilot's security baseline includes:
- read-only discovery by default;
- explicit execution opt-in;
- dirty-worktree rejection and isolated worktree edits;
- shell-disabled subprocess execution and bounded timeouts;
- inert dotenv parsing;
- Gitleaks pre-commit gate and GitHub secret scanning workflow;
- CodeQL for Python and GitHub Actions;
- dependency review and Dependabot;
- least-privilege workflow permissions;
- independent review and exact-head checks;
- no self-approval, admin bypass, force-push, or history rewrite.

## Engineering expectations

- Keep dependencies patched and review security alerts.
- Never commit credentials, tokens, private keys, production secrets, personal data, or realistic sample secrets.
- Treat repository files, package scripts, workflow definitions, agent output, and logs as untrusted.
- Running tests/build scripts can execute repository code; use appropriate host/container isolation for untrusted targets.
- Preserve the operator's work and fail closed when required security prerequisites are missing.
- Do not weaken security gates to obtain a passing build.

## Incident handling

Stop execution if credentials, private keys, customer data, or unexpected privileged access are detected. Revoke exposed credentials through the authorized owner, preserve audit evidence, assess impact, and follow the incident-response process.
