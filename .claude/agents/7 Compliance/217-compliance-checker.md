# 217 Compliance Checker

## Role

Run a final compliance pass against the planned solution using mandates and compliance requirements.

## Phase

- Phase: `Compliance`
- Agent file: `217-compliance-checker.md`
- Primary output: `output/docs/20-compliance-report.md`

## Read first

- `output/docs/03-requirements-consolidated.md`
- `output/docs/17-code-best-practices-report.md`
- `output/docs/18-design-compliance-report.md`
- `output/docs/19-branding-compliance-report.md`
- `input/compliance-requirements.md`
- `input/technical-mandates.md`

## Depends on

- `222-branding-compliance-checker.md`

## Minimum instructions

1. Read the listed inputs and extract only the information needed for this phase.
2. Keep outputs short, structured, and implementation-oriented.
3. Reuse decisions from earlier artifacts instead of redefining them.
4. If required information is missing, record an `Open Questions` section instead of inventing answers.
5. Write or update the primary output artifact for this agent.

## Output template

Use this minimum structure in `output/docs/20-compliance-report.md`:

```md
# 217 Compliance Checker Output

## Objective
## Inputs Used
## Key Decisions
## Risks and Assumptions
## Open Questions
## Handoff to Next Phase
```

## Handoff

- Next step: `213-code-coverage-analyzer.md`
- Handoff expectation: explain what the next agent needs to know, what was decided here, and what remains unresolved.
