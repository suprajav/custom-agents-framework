#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <phase-name>"
  exit 1
fi

echo "Phase runner placeholder for: $1"
echo "Use the contracts and agent files in .claude/agents/ to execute this phase."
