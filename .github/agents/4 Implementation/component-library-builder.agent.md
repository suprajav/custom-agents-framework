---
description: "Use when running the Implementation phase step 4: shared library or component extraction. Identifies cross-cutting concerns and shared utilities to extract into a reusable helper layer. For Azure Integration projects: response builder, config extensions, validation helpers, and logging extensions. Outputs output/docs/12-component-library.md."
tools: [read, edit, search]
user-invocable: true
---
# Shared Library / Component Builder

## Role

Review the implementation artifacts and identify cross-cutting utilities that should be
extracted into shared helpers. For Azure Integration projects this is NOT a UI component
library — it is a shared C# helpers/extensions layer. For UI projects, document the
component catalogue.

## Phase

- Phase: `Implementation`
- Primary output: `output/docs/12-component-library.md`

## Read first

1. `output/docs/09-backend-implementation.md`
2. `output/docs/11-database-implementation.md`
3. `input/guardrails/code-practices.md` — error handling, logging, serialization sections

## Depends on

- `@database-implementation` (11-database-implementation.md)

## Instructions

### Step 1 — Identify candidates for extraction
Scan backend and data model implementations for repeated patterns:
- Response builder: construct `HttpResponseData` with standard JSON shape
- Serialization options: singleton `JsonSerializerOptions` with project-wide settings
- Logging extensions: `ILogger` extension methods for correlation ID, structured events
- Validation helper: `ValidationResult` to problem-details response mapping
- Config extensions: `IServiceCollection` extension methods to keep `Program.cs` clean
- Guard clauses: null-check, range-check helpers if used in multiple places

### Step 2 — For each candidate
Document:
- Class/method name and namespace (`{SolutionName}.Functions.Helpers/`)
- Signature
- Why extracted (duplicated in N places or cross-cutting)
- Code block with implementation

### Step 3 — For UI projects
Document each component:
- Name, file path, props, variants, accessibility notes
- When to use / when not to use
- Dependencies on design tokens from `input/branding-guidelines.md`

### Step 4 — Extraction decision
For any pattern that appears in only one place: state "Not extracted — single use" rather
than creating unnecessary abstractions.

## Output template

```md
# Shared Library / Component Catalogue

## Objective

## Inputs Used

## Extraction Candidates Review

| Pattern | Occurrences | Decision | Notes |
|---------|------------|----------|-------|

## Extracted Helpers

### ResponseBuilder
<!-- Code block -->

### SerializationOptions
<!-- Code block -->

### LoggingExtensions
<!-- Code block -->

### {ServiceCollectionExtension}
<!-- Code block -->

## Not Extracted
<!-- Patterns considered but not extracted, with reason -->

## Key Decisions

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@test-suite-generator`
- Handoff expectation: The test suite generator needs the full list of classes and methods
  (including shared helpers) to determine what requires unit test coverage.
