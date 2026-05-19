---
description: "Use when running the Testing phase step 2: generating adapter or frontend tests. For API integration projects, tests the inbound adapter layer (APIM policy simulation, auth enforcement, request routing). For UI projects, defines component and journey tests. Outputs output/docs/14-frontend-tests.md."
tools: [read, edit, search]
user-invocable: true
---
# Adapter / Frontend Test Generator

## Role

For Azure Integration projects: generate tests for the inbound adapter layer, including
correlation ID propagation, auth header validation, content-type enforcement, and request
routing to the correct function.

For UI projects: generate component interaction tests and user journey tests.

## Phase

- Phase: `Testing`
- Primary output: `output/docs/14-frontend-tests.md`

## Read first

1. `output/docs/10-frontend-implementation.md` — adapter/APIM layer or UI screens
2. `output/docs/13-test-suite.md` — coverage plan and existing test classes
3. `output/docs/07-api-contract.md` — security requirements, header requirements

## Depends on

- `@test-suite-generator` (13-test-suite.md)

## Instructions

### For API-only integrations (no UI)

Document that frontend tests are N/A and produce adapter-layer tests instead:

**Auth enforcement tests** (Function trigger level):
- Request with no Authorization header → 401
- Request with expired token → 401
- Request with valid token but wrong audience → 403
- Request with valid token and correct audience → passes to validation

**Header tests**:
- Request missing `Content-Type: application/json` → 415
- Request with `X-Correlation-Id` header → value propagated to response headers and logs
- Request without `X-Correlation-Id` header → generated GUID propagated

**Content tests**:
- Empty body → 400
- Non-JSON body → 400
- Valid JSON not matching schema → 400 with field-level errors

### For UI projects

For each screen from `10-frontend-implementation.md`:
- Renders without errors given valid props
- Shows loading state while API call is in-flight
- Shows error state when API returns 4xx/5xx
- User action (button click, form submit) triggers correct API call

## Output template

```md
# Adapter / Frontend Tests

## Objective

## Inputs Used

## Assessment
<!-- "API-only integration: adapter tests generated" or "UI project: component tests generated" -->

## Adapter Layer Tests (API integrations)

```csharp
// Auth tests, header tests, content tests
```

## Frontend Component Tests (UI projects)

## Key Decisions

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@accessibility-validator`
- Handoff expectation: The accessibility validator needs to know if a UI exists and
  what WCAG level is required by NFRs.
