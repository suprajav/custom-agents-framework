---
description: "Use when running the Testing phase step 4: generating test data. Produces JSON fixture files for all test scenarios: happy path, mandatory field missing, invalid format, auth failure, downstream error. Maps each fixture to a user story and FR. Outputs output/docs/16-test-data.md."
tools: [read, edit, search]
user-invocable: true
---
# Test Data Generator

## Role

Produce the minimum set of JSON fixture files needed to exercise every test scenario
defined in the test suite. For each fixture, document which user story and FR it covers.
Fixtures must be self-contained — no external system required to use them.

## Phase

- Phase: `Testing`
- Primary output: `output/docs/16-test-data.md`

## Read first

1. `output/docs/03-requirements-consolidated.md` — mandatory field list, edge cases
2. `output/docs/06-database-design.md` — inbound model structure, field types
3. `output/docs/13-test-suite.md` — test class list, scenarios covered

## Depends on

- `@accessibility-validator` (15-accessibility-report.md)

## Instructions

### Step 1 — Fixture catalogue
List all fixtures needed before generating them:

| Fixture File | Scenario | US | FR | Expected Result |
|-------------|---------|----|----|----------------|
| `valid-request.json` | All mandatory fields present and valid | US-001 | FR-001 | 200 OK |
| `missing-{field}.json` | {field} absent | US-002 | FR-002 | 400 Validation Error |
| `invalid-format-{field}.json` | {field} has wrong format | US-002 | FR-002 | 400 Validation Error |
| `empty-body.json` | Empty JSON object `{}` | US-003 | FR-002 | 400 |

Generate one `missing-{field}.json` per mandatory field.

### Step 2 — Generate fixture files
For each fixture, produce the JSON content:

```json
// valid-request.json
{
  // All mandatory fields with valid values
  // Optional fields omitted
}
```

```json
// missing-{FieldName}.json
{
  // All mandatory fields EXCEPT {FieldName}
}
```

Rules:
- Use realistic but non-production values (no real PII, no real account numbers)
- Use placeholder formats: GUIDs like `"00000000-0000-0000-0000-000000000001"`, dates like `"2024-01-15"`, amounts like `"1000.00"`
- String values that should look real but aren't: `"TEST_POLICY_001"`, `"TEST_ACCOUNT_001"`

### Step 3 — Downstream mock responses
Produce mock response fixtures for the dispatch tests:

```json
// downstream-200-response.json
{ /* success response from target system */ }
```

```json
// downstream-400-response.json  
{ /* validation error from target system */ }
```

```json
// downstream-500-response.json
{ /* error from target system */ }
```

### Step 4 — File placement
Document where fixture files should be placed in the test project:
```
{SolutionName}.Functions.Tests/
  Fixtures/
    Requests/
      valid-request.json
      missing-{field}.json
    Responses/
      downstream-200.json
      downstream-400.json
      downstream-500.json
```

## Output template

```md
# Test Data

## Objective

## Inputs Used

## Fixture Catalogue

| Fixture File | Scenario | US | FR | Expected Result |
|-------------|---------|----|----|----------------|

## Request Fixtures

### valid-request.json
```json
{}
```

### missing-{FieldName}.json
```json
{}
```

## Downstream Response Fixtures

### downstream-200.json
### downstream-400.json
### downstream-500.json

## File Placement

## Key Decisions

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@code-best-practices-enforcer`
- Handoff expectation: The quality phase needs the fixture catalogue and test coverage plan
  to validate that all FRs have test coverage.
