# Repository and Adapter Profiles

ZPilot discovers repository families from manifests and lockfiles. Discovery does not imply that every ecosystem has an automatic test adapter.

## Discovery families

- Python: pyproject.toml, requirements.txt, Pipfile, setup.py
- JavaScript/TypeScript: package.json, pnpm workspace
- Go: go.mod
- Rust: Cargo.toml
- Java/Kotlin: Maven and Gradle manifests
- .NET: solution and project files
- Ruby: Gemfile
- PHP: composer.json
- Swift: Package.swift
- Dart/Flutter: pubspec.yaml
- C/C++: CMakeLists.txt
- Elixir, Scala, Julia
- Terraform, Helm, Docker, Docker Compose, Make

## Adapter policy

An adapter runs only when its executable, manifest, and declared project command are available. ZPilot does not invent package scripts or silently install dependencies.

Unsupported stacks and missing tools remain explicit coverage gaps. Add an adapter only with a documented command contract, bounded timeout, error semantics, fixture tests, and platform compatibility evidence.

See docs/architecture.md and ROADMAP.md.
