# Swagger Pipeline

## Purpose

Use this command when the main outcome is an API-first or Swagger-oriented workflow.

## Minimum behavior

1. Start from the orchestrator and Requirement outputs.
2. Prioritize `204-tech-stack-configurator.md` and `207-api-contract-designer.md`.
3. Produce or refine `output/docs/07-api-contract.md` as the source of truth for service interfaces.
4. Pass the contract into planning, backend implementation, testing, and documentation.

## Inputs

- `input/Automate Insurance Quote Extraction Process_PDD.md`
- `input/User Stories List.md`
- `output/docs/03-requirements-consolidated.md`
- `output/docs/04-tech-stack.md`
- `output/docs/05-architecture.md`

## Outputs

- `output/docs/07-api-contract.md`
- downstream implementation and test artifacts that reference the contract
