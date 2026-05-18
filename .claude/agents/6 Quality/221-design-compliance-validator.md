# 221 Design Compliance Validator

## Role

Validate whether the design and implementation plans still satisfy the intended architecture and requirements.

## Phase

- Phase: `Quality`
- Agent file: `221-design-compliance-validator.md`
- Primary output: `output/docs/18-design-compliance-report.md`

## Read first

- `output/docs/03-requirements-consolidated.md`
- `output/docs/05-architecture.md`
- `output/docs/09-backend-implementation.md`
- `output/docs/10-frontend-implementation.md`

## Depends on

- `220-code-best-practices-enforcer.md`

## Minimum instructions

1. Read the listed inputs and extract only the information needed for this phase.
2. Keep outputs short, structured, and implementation-oriented.
3. Reuse decisions from earlier artifacts instead of redefining them.
4. If required information is missing, record an `Open Questions` section instead of inventing answers.
5. Write or update the primary output artifact for this agent.

## Output template

Use this minimum structure in `output/docs/18-design-compliance-report.md`:

```md
# 221 Design Compliance Validator Output

## Objective
## Inputs Used
## Key Decisions
## Risks and Assumptions
## Open Questions
## Handoff to Next Phase
```

## Handoff

- Next step: `222-branding-compliance-checker.md`
- Handoff expectation: explain what the next agent needs to know, what was decided here, and what remains unresolved.
