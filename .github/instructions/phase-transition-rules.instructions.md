---
description: "Use when advancing between pipeline phases, checking phase dependencies, or validating that required artifacts exist before starting a new phase. Covers phase transition gates and dependency checks."
applyTo: "**"
---
# Phase Transition Rules

1. A phase can advance only when its expected output artifact exists.
2. A later phase must read the earlier outputs listed in the contracts.
3. Do not skip Deployment, Consolidated Report, or Documentation once they are part of the configured flow.
4. If a dependency artifact is missing, stop and report the gap rather than guessing.
