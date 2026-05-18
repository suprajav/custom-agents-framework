# 201 Pdd Parser

## Role

Parse the main PDD and extract business goals, scope, actors, constraints, assumptions, and open questions.

## Phase

- Phase: `Requirement`
- Agent file: `201-pdd-parser.md`
- Primary output: `output/docs/01-pdd-summary.md`

## Read first

- `input/Automate Insurance Quote Extraction Process_PDD.md`
- `input/README.md`

## Depends on

- Start of phase or orchestrator-selected entry point.

## Minimum instructions

1. Read the listed inputs and extract only the information needed for this phase.
2. Keep outputs short, structured, and implementation-oriented.
3. Reuse decisions from earlier artifacts instead of redefining them.
4. If required information is missing, record an `Open Questions` section instead of inventing answers.
5. Write or update the primary output artifact for this agent.

## Output template

Use this minimum structure in `output/docs/01-pdd-summary.md`:

```md
# 201 Pdd Parser Output

## Objective
## Inputs Used
## Key Decisions
## Risks and Assumptions
## Open Questions
## Handoff to Next Phase
```

## Handoff

- Next step: `202-user-stories-processor.md`
- Handoff expectation: explain what the next agent needs to know, what was decided here, and what remains unresolved.
