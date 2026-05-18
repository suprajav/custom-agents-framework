#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

./.claude/test-hook-simple.sh
./.claude/scripts/validate-artifacts.sh
python3 .claude/runtime/orchestrator-runner.py > /tmp/custom-agent-framework-smoke.txt

test -f .claude/contracts/artifact-registry.yaml
test -f .claude/contracts/phase-input-output-map.yaml
test -f .claude/runtime/project-state.yaml
test -f .claude/agents/9\ Deployment/225-deployment-strategy-designer.md

echo "custom-agent-framework smoke test passed"
