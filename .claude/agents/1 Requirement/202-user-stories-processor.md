# 202 User Stories Processor

## Role

Normalize the user story list into structured user journeys, acceptance criteria, and story groupings.

## Phase

- Phase: `Requirement`
- Agent file: `202-user-stories-processor.md`
- Primary output: `output/docs/02-user-stories-summary.md`

## Read first

- `input/User Stories List.md`
- `output/docs/01-pdd-summary.md`

## Depends on

- `201-pdd-parser.md`

## Minimum instructions

1. Read the listed inputs and extract only the information needed for this phase.
2. Keep outputs short, structured, and implementation-oriented.
3. Reuse decisions from earlier artifacts instead of redefining them.
4. If required information is missing, record an `Open Questions` section instead of inventing answers.
5. Write or update the primary output artifact for this agent.

## Output template

Use this minimum structure in `output/docs/02-user-stories-summary.md`:

```md
# 202 User Stories Processor Output

## Objective
## Inputs Used
## Key Decisions
## Risks and Assumptions
## Open Questions
## Handoff to Next Phase
```

## Handoff

- Next step: `203-requirements-consolidator.md`
- Handoff expectation: explain what the next agent needs to know, what was decided here, and what remains unresolved.
