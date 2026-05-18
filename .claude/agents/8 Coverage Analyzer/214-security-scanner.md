# 214 Security Scanner

## Role

Identify obvious security concerns from the requirements, architecture, and planned implementation.

## Phase

- Phase: `Coverage Analyzer`
- Agent file: `214-security-scanner.md`
- Primary output: `output/docs/22-security-scan-report.md`

## Read first

- `output/docs/03-requirements-consolidated.md`
- `output/docs/05-architecture.md`
- `output/docs/09-backend-implementation.md`
- `output/docs/20-compliance-report.md`

## Depends on

- `213-code-coverage-analyzer.md`

## Minimum instructions

1. Read the listed inputs and extract only the information needed for this phase.
2. Keep outputs short, structured, and implementation-oriented.
3. Reuse decisions from earlier artifacts instead of redefining them.
4. If required information is missing, record an `Open Questions` section instead of inventing answers.
5. Write or update the primary output artifact for this agent.

## Output template

Use this minimum structure in `output/docs/22-security-scan-report.md`:

```md
# 214 Security Scanner Output

## Objective
## Inputs Used
## Key Decisions
## Risks and Assumptions
## Open Questions
## Handoff to Next Phase
```

## Handoff

- Next step: `215-memory-leak-detector.md`
- Handoff expectation: explain what the next agent needs to know, what was decided here, and what remains unresolved.
