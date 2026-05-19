---
description: "Use when running the Implementation phase step 3: data model implementation. For stateless integrations, generates the C# model classes and JSON schema file. For projects with persistence, generates the storage client, migrations, and seed data. Outputs output/docs/11-database-implementation.md."
tools: [read, edit, search]
user-invocable: true
---
# Data Model Implementation

## Role

Translate the data model design into runnable code. For stateless Azure Integration projects,
this means generating the C# model classes, JSON schema file, and any embedded resources.
For projects with persistence, generate the storage client, connection setup, and migrations.

## Phase

- Phase: `Implementation`
- Primary output: `output/docs/11-database-implementation.md`

## Read first

1. `output/docs/08-task-plan.md`
2. `output/docs/06-database-design.md` — all model tables, field mapping, JSON schema
3. `output/docs/09-backend-implementation.md` — namespace conventions, model class names
4. `input/guardrails/code-practices.md` — model conventions section

## Depends on

- `@frontend-implementation` (10-frontend-implementation.md)

## Instructions

### Step 1 — Assess persistence type
From `06-database-design.md`:
- If "This integration is stateless" → proceed to Step 2 only
- If persistence is required → proceed to Step 2 and Step 3

### Step 2 — C# model classes and JSON schema

**Model classes** (`{SolutionName}.Functions.Models/`):
- Generate every class from the inbound/outbound model tables in `06-database-design.md`
- Use C# records for immutable models, classes if mutation is required
- `System.Text.Json.Serialization.JsonPropertyNameAttribute` on every property
- `System.ComponentModel.DataAnnotations` attributes for mandatory fields
- Nested class for each nested object (not flattened)

**JSON schema file** (`{SolutionName}.Functions/Schemas/{Feature}Request.schema.json`):
- Generate from the JSON Schema section of `06-database-design.md`
- Set as `EmbeddedResource` in the `.csproj`
- Document the resource path used to load it in the ValidationService

### Step 3 — Persistence implementation (if applicable)

**Storage client** (`{SolutionName}.Functions.Helpers/StorageClient.cs`):
- Use Azure SDK client (CosmosClient, BlobServiceClient, etc.)
- Inject via DI; configure connection string from `IOptions<T>`
- No direct connection string in code — always from configuration

**Schema/migrations** (if SQL):
- Migration scripts in `db/migrations/` with sequential numbering
- Up and down scripts per migration
- Seed data scripts in `db/seed/` (non-production environments only)

## Output template

```md
# Data Model Implementation

## Objective

## Inputs Used

## Persistence Assessment
<!-- "Stateless" or describe persistence type -->

## Model Classes

### {InboundModelClass}
<!-- Code block -->

### {OutboundModelClass}
<!-- Code block -->

## JSON Schema File
<!-- Path and code block -->

## Persistence Implementation (if applicable)

### Storage Client
### Connection Configuration
### Migrations / Schema

## Key Decisions

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@component-library-builder`
- Handoff expectation: The shared library builder needs the full list of model classes,
  interfaces, and helpers to determine what should be extracted into a shared library.
