---
description: "Use when running the Deployment phase step 3: checking release readiness. Aggregates the compliance verdict, security findings, performance blockers, and infrastructure prerequisites into a PASS/FAIL release gate with a sign-off checklist. Outputs output/docs/25c-release-readiness.md."
tools: [read, edit, search]
user-invocable: true
---
# Release Readiness Checker

## Role

Aggregates all pipeline findings into a final release readiness verdict.
A `PASS` requires: no open compliance blockers, no critical security findings, coverage
targets met, infrastructure prerequisites documented. A `FAIL` blocks release.

## Phase

- Phase: `Deployment`
- Primary output: `output/docs/25c-release-readiness.md`

## Read first

1. `output/docs/20-compliance-report.md` — compliance verdict and blockers
2. `output/docs/22-security-scan-report.md` — critical/high security findings
3. `output/docs/21-code-coverage-report.md` — coverage gaps
4. `output/docs/24-performance-report.md` — performance blockers
5. `output/docs/25b-infrastructure-config.md` — infrastructure prerequisites

## Depends on

- `@infrastructure-config-generator` (25b-infrastructure-config.md)

## Instructions

### Step 1 — Aggregate blockers from all upstream reports

| Source | Finding | Severity | Status |
|--------|---------|---------|--------|
| 20-compliance-report | ... | BLOCKER | Open / Resolved |
| 22-security-scan | ... | CRITICAL | Open / Resolved |
| 21-coverage | ... | BLOCKER | Open / Resolved |
| 24-performance | ... | BLOCKER | Open / Resolved |

### Step 2 — Release sign-off checklist

| # | Check | Status |
|---|-------|--------|
| 1 | Compliance verdict is PASS or CONDITIONAL PASS | ✓ / ✗ |
| 2 | No CRITICAL security findings open | ✓ / ✗ |
| 3 | Code coverage meets NFR target | ✓ / ✗ |
| 4 | All FRs have implementing artifacts | ✓ / ✗ |
| 5 | Key Vault references configured for all secrets | ✓ / ✗ |
| 6 | Managed Identity assignments documented | ✓ / ✗ |
| 7 | Pipeline smoke test defined | ✓ / ✗ |
| 8 | APIM timeout aligned with Function timeout | ✓ / ✗ |
| 9 | Runbook or operational guide exists | ✓ / ✗ |
| 10 | Required approvals obtained (if mandated) | ✓ / ✗ |

### Step 3 — Verdict
- All ✓: **READY FOR RELEASE**
- Any ✗ that is a blocker: **NOT READY — BLOCKED**
- Any ✗ that is a follow-up: **CONDITIONAL RELEASE — follow-up required**

### Step 4 — Follow-up items
List items that are ✗ but not release blockers (to be tracked as post-release improvements).

## Output template

```md
# Release Readiness

## VERDICT: {READY / CONDITIONAL / BLOCKED}

## Objective

## Inputs Used

## Aggregated Blockers

| Source | Finding | Severity | Status |
|--------|---------|---------|--------|

## Release Sign-off Checklist

| # | Check | Status |
|---|-------|--------|

## Verdict Justification

## Follow-up Items

## Required Approvals

## Risks and Assumptions

## Open Questions

## Handoff to Monitoring Plan
```

## Handoff

- Next step: `@monitoring-observability-planner`
- Handoff expectation: The monitoring planner needs the open operational gaps and any
  follow-up items that require observability (e.g. unknown error rates, SLA monitoring).
