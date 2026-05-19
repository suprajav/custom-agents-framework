---
description: "Use when running the Documentation phase step 2: generating the documentation index and handover pack. Creates the final delivery handover document: artifact index, key decisions log, architectural summary, operational contacts, and unresolved items register. Outputs output/docs/27-documentation-index.md."
tools: [read, edit, search]
user-invocable: true
---
# Documentation Generator

## Role

Create the final delivery handover document. This is what the team leaves behind:
a complete artifact index, key decisions log, known gaps register, and operational
guidance for whoever maintains this integration.

## Phase

- Phase: `Documentation`
- Primary output: `output/docs/27-documentation-index.md`

## Read first

1. `output/docs/25-consolidated-report.md` — overall status and phase summary
2. `output/docs/26-deployment-config.md` — deployment configuration
3. `output/docs/03-requirements-consolidated.md` — FR/NFR baseline
4. `output/docs/05-architecture.md` — architecture decisions
5. `output/docs/25d-monitoring-observability.md` — operational runbook

## Depends on

- `@deployment-config-generator` (26-deployment-config.md)

## Instructions

### Step 1 — Artifact index
List every generated artifact with its file path, phase, and one-line purpose:

| # | File | Phase | Purpose |
|---|------|-------|--------|
| 1 | output/docs/01-pdd-summary.md | Requirement | Design document summary |
| 2 | output/docs/02-user-stories-summary.md | Requirement | User stories |
| ... | ... | ... | ... |
| 27 | output/docs/27-documentation-index.md | Documentation | This document |

### Step 2 — Key decisions log
From architecture, tech stack, and design decisions across all phases:

| Decision | Choice | Rationale | Source Artifact |
|----------|--------|-----------|----------------|
| Runtime | .NET 8 isolated | Mandate + performance | 04-tech-stack |
| Auth (outbound) | DefaultAzureCredential | Security guardrail | 04-tech-stack |
| Serialization | System.Text.Json | Performance, no Newtonsoft dependency | 04-tech-stack |
| Retry | Polly WaitAndRetry 3x | NFR resilience requirement | 09-backend |

### Step 3 — Architecture snapshot
One-paragraph description of the integration suitable for a new team member:
- Source system → trigger → Function logic → target system
- Authentication model
- Key configuration parameters
- Environments

### Step 4 — Unresolved items register
All open questions from all phases that were not resolved during the pipeline run:

| # | Phase | Question | Impact | Owner |
|---|-------|---------|--------|-------|

### Step 5 — Maintenance guidance
- Where to find the source code and which branch is production
- How to re-run the pipeline for a new feature: which agents to invoke
- Which guardrail files to update if project standards change
- Key contacts (from operational runbook in `25d`)

### Step 6 — Pipeline completion confirmation
Confirm that all expected artifacts exist:

| Expected Artifact | Present |
|------------------|--------|
| 01-pdd-summary.md | ✓ / ✗ |
| 02-user-stories-summary.md | ✓ / ✗ |
| 03-requirements-consolidated.md | ✓ / ✗ |
| ... all 27 artifacts ... | |

## Output template

```md
# Documentation Index and Handover Pack

## Objective

## Inputs Used

## Artifact Index

| # | File | Phase | Purpose |
|---|------|-------|--------|

## Key Decisions Log

| Decision | Choice | Rationale | Source |
|----------|--------|-----------|--------|

## Architecture Snapshot

## Unresolved Items Register

| # | Phase | Question | Impact | Owner |
|---|-------|---------|--------|-------|

## Maintenance Guidance

## Pipeline Completion Confirmation

| Expected Artifact | Present |
|------------------|--------|

## Risks and Assumptions

## Open Questions
```

## Handoff

- Next step: Pipeline complete.
- Confirm all 27 artifacts are present in `output/docs/`.
