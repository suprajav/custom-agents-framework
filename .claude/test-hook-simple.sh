#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

required=(
  "${PROJECT_DIR}/input/Automate Insurance Quote Extraction Process_PDD.md"
  "${PROJECT_DIR}/input/User Stories List.md"
  "${PROJECT_DIR}/input/technical-mandates.md"
  "${PROJECT_DIR}/input/coding-best-practices.md"
  "${PROJECT_DIR}/input/compliance-requirements.md"
  "${PROJECT_DIR}/input/branding-guidelines.md"
  "${PROJECT_DIR}/input/README.md"
)

missing=0
for path in "${required[@]}"; do
  if [ ! -f "$path" ]; then
    echo "Missing required input: $path"
    missing=1
  fi
done

mkdir -p "${PROJECT_DIR}/output/docs"

if [ "$missing" -ne 0 ]; then
  echo "Pre-run validation failed."
  exit 1
fi

echo "Pre-run validation passed."
