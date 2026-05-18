# 226 Infrastructure Config Generator

## Role

Create a minimal infrastructure and configuration outline that matches the chosen deployment strategy.

## Phase

- Phase: `Deployment`
- Agent file: `226-infrastructure-config-generator.md`
- Primary output: `output/docs/25b-infrastructure-config.md`

## Read first

- `output/docs/25a-deployment-strategy.md`
- `output/docs/05-architecture.md`
- `output/docs/06-database-design.md`

## Depends on

- `225-deployment-strategy-designer.md`

## Minimum instructions

1. Define the major infrastructure components required to run the solution.
2. Capture application configuration categories, secrets boundaries, and environment-specific concerns.
3. Keep the result implementation-neutral unless the stack clearly dictates otherwise.
4. Write the result to `output/docs/25b-infrastructure-config.md`.

## Output template

```md
# Infrastructure Config

## Objective
## Required Components
## Environment Configuration
## Secrets and Sensitive Settings
## Risks and Assumptions
## Handoff to Release Readiness
```

## Handoff

- Next step: `227-release-readiness-checker.md`
- Handoff expectation: identify what must be true before a release can be considered ready.
