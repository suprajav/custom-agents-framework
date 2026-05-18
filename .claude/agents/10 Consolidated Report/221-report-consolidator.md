# 221 Report Consolidator

## Role

Summarize the outputs of all completed phases into one delivery-ready health report.

## Phase

- Phase: `Consolidated Report`
- Agent file: `221-report-consolidator.md`
- Primary output: `output/docs/25-consolidated-report.md`

## Read first

- `output/docs/03-requirements-consolidated.md`
- `output/docs/08-task-plan.md`
- `output/docs/20-compliance-report.md`
- `output/docs/21-code-coverage-report.md`
- `output/docs/22-security-scan-report.md`
- `output/docs/23-memory-leak-report.md`
- `output/docs/24-performance-report.md`

## Depends on

- `216-performance-analyzer.md`

## Minimum instructions

1. Read the listed inputs and extract only the information needed for this phase.
2. Keep outputs short, structured, and implementation-oriented.
3. Reuse decisions from earlier artifacts instead of redefining them.
4. If required information is missing, record an `Open Questions` section instead of inventing answers.
5. Write or update the primary output artifact for this agent.

## Output template

Use this minimum structure in `output/docs/25-consolidated-report.md`:

```md
# 221 Report Consolidator Output

## Objective
## Inputs Used
## Key Decisions
## Risks and Assumptions
## Open Questions
## Handoff to Next Phase
```

## Handoff

- Next step: `218-deployment-config-generator.md`
- Handoff expectation: explain what the next agent needs to know, what was decided here, and what remains unresolved.
