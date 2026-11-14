#!/usr/bin/env bash
# Compatibility entry point. ZPilot owns repair/convergence behavior.
# Discovery is the default; mutation requires explicit --execute and --task.
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/../zpilot.py" "$@"
