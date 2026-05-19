---
description: "Run the swagger-first pipeline. Use when the main outcome is an API-first or Swagger-oriented workflow, starting from the orchestrator and requirement outputs to produce the API contract as the source of truth."
---
# Swagger Pipeline

## Purpose

Use this prompt when the main outcome is an API-first or Swagger-oriented workflow.

## Steps

1. Invoke `@greenfield-orchestrator` or start from the Requirement outputs.
2. Prioritize `@tech-stack-configurator` and `@api-contract-designer`.
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
- Downstream implementation and test artifacts that reference the contract
