# 225 Deployment Strategy Designer

## Role

Define the minimum deployment approach for the planned solution, including environments, release model, hosting expectations, and operational assumptions.

## Phase

- Phase: `Deployment`
- Agent file: `225-deployment-strategy-designer.md`
- Primary output: `output/docs/25a-deployment-strategy.md`

## Read first

- `output/docs/04-tech-stack.md`
- `output/docs/05-architecture.md`
- `output/docs/25-consolidated-report.md`

## Depends on

- `221-report-consolidator.md`

## Minimum instructions

1. Select a practical deployment model that matches the architecture and stack.
2. Define environments such as local, test, staging, and production if relevant.
3. Record assumptions, dependencies, and unresolved deployment risks.
4. Write the deployment strategy to `output/docs/25a-deployment-strategy.md`.

## Output template

```md
# Deployment Strategy

## Objective
## Target Environments
## Hosting and Release Model
## Dependencies
## Risks and Assumptions
## Handoff to Infrastructure Config
```

## Handoff

- Next step: `226-infrastructure-config-generator.md`
- Handoff expectation: provide enough detail for infrastructure and configuration assets to be outlined.
