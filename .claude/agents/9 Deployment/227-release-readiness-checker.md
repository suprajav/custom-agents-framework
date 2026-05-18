# 227 Release Readiness Checker

## Role

Check whether the planned solution has the minimum documentation, validation, and operational readiness needed for release.

## Phase

- Phase: `Deployment`
- Agent file: `227-release-readiness-checker.md`
- Primary output: `output/docs/25c-release-readiness.md`

## Read first

- `output/docs/25a-deployment-strategy.md`
- `output/docs/25b-infrastructure-config.md`
- `output/docs/20-compliance-report.md`
- `output/docs/24-performance-report.md`

## Depends on

- `226-infrastructure-config-generator.md`

## Minimum instructions

1. Review deployment, compliance, and coverage outputs together.
2. Identify blockers, open risks, and required approvals.
3. Separate release blockers from follow-up improvements.
4. Write the result to `output/docs/25c-release-readiness.md`.

## Output template

```md
# Release Readiness

## Objective
## Ready Items
## Blockers
## Follow-up Actions
## Required Approvals
## Handoff to Monitoring Plan
```

## Handoff

- Next step: `228-monitoring-observability-planner.md`
- Handoff expectation: explain what needs monitoring, alerting, and operational visibility.
