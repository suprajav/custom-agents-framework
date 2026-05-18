#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

python3 .claude/validators/validate-inputs.py
python3 .claude/validators/validate-artifacts.py
python3 .claude/validators/validate-phase-handoff.py
