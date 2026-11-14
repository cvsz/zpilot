#!/usr/bin/env bash
# Safe local discovery wrapper. Never clones, deletes, commits, or pushes.
set -euo pipefail
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <local-repository-path>" >&2
  exit 2
fi
SCRIPT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/../zpilot.py" --repo "$1" --discover-only --json
