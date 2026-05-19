---
name: openapi-helper
description: "Use when working with the swagger pipeline, updating API contracts, or keeping contract decisions aligned across architecture, API design, testing, and documentation phases."
---
# OpenAPI Helper

## Purpose

Support API-oriented phases by keeping contract decisions aligned across architecture, API design, testing, and documentation.

## Use when

- Working with the swagger-first pipeline (`/swagger-pipeline`).
- Updating API contracts or API-driven implementation plans.
- Ensuring downstream phases consume the API contract as the source of truth.

## Rules

- Keep the API contract (`output/docs/07-api-contract.md`) as the source of truth.
- Propagate changes consistently to downstream phases.
- Flag any mismatch between the contract and implementation plans.
