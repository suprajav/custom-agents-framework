---
name: schema-checker
description: "Use when validating handoffs between phases, checking whether a document includes required sections, or verifying an artifact matches the expected structure described by framework contracts."
---
# Schema Checker

## Purpose

Review whether an input or output artifact matches the expected structure described by the framework contracts.

## Use when

- Validating handoffs between phases.
- Checking whether a document includes the required sections (Objective, Inputs Used, Key Decisions, Risks and Assumptions, Open Questions, Handoff).
- Verifying a new artifact before passing it to the next phase.

## Rules

- Validate structure before content quality.
- Report missing sections explicitly — do not silently accept malformed artifacts.
- Do not invent content for missing sections.

## Required sections for every output artifact

1. Objective
2. Inputs Used
3. Key Decisions
4. Risks and Assumptions
5. Open Questions
6. Handoff to Next Phase
