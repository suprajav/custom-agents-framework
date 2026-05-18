#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

./.claude/test-hook-simple.sh
python3 .claude/runtime/orchestrator-runner.py
