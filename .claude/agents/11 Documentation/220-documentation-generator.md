# 220 Documentation Generator

## Role

Create the final documentation index and handover summary for the framework outputs.

## Phase

- Phase: `Documentation`
- Agent file: `220-documentation-generator.md`
- Primary output: `output/docs/27-documentation-index.md`

## Read first

- `output/docs/25-consolidated-report.md`
- `output/docs/26-deployment-config.md`

## Depends on

- `218-deployment-config-generator.md`

## Minimum instructions

1. Read the listed inputs and extract only the information needed for this phase.
2. Keep outputs short, structured, and implementation-oriented.
3. Reuse decisions from earlier artifacts instead of redefining them.
4. If required information is missing, record an `Open Questions` section instead of inventing answers.
5. Write or update the primary output artifact for this agent.

## Output template

Use this minimum structure in `output/docs/27-documentation-index.md`:

```md
# 220 Documentation Generator Output

## Objective
## Inputs Used
## Key Decisions
## Risks and Assumptions
## Open Questions
## Handoff to Next Phase
```

## Handoff

- Next step: `Pipeline complete`
- Handoff expectation: explain what the next agent needs to know, what was decided here, and what remains unresolved.
