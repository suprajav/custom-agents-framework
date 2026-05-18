# 228 Monitoring Observability Planner

## Role

Define the minimum monitoring, logging, alerting, and observability expectations for the deployed solution.

## Phase

- Phase: `Deployment`
- Agent file: `228-monitoring-observability-planner.md`
- Primary output: `output/docs/25d-monitoring-observability.md`

## Read first

- `output/docs/05-architecture.md`
- `output/docs/25a-deployment-strategy.md`
- `output/docs/25c-release-readiness.md`

## Depends on

- `227-release-readiness-checker.md`

## Minimum instructions

1. Define the main signals the system should expose: logs, metrics, traces, and alerts.
2. Focus on business-critical and failure-critical paths.
3. Note any operational gaps that must be closed before production.
4. Write the result to `output/docs/25d-monitoring-observability.md`.

## Output template

```md
# Monitoring and Observability Plan

## Objective
## Logs
## Metrics
## Alerts
## Dashboards and Reporting
## Open Operational Gaps
```

## Handoff

- Next step: `221-report-consolidator.md` or `218-deployment-config-generator.md` depending on workflow refinement.
- Handoff expectation: provide deployment evidence that can be referenced by reporting and documentation.
