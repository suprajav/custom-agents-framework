#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cat "$ROOT_DIR/.claude/runtime/project-state.yaml"
