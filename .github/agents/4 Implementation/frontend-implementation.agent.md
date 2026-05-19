---
description: "Use when running the Implementation phase step 2: frontend or adapter implementation. For API integration projects with no UI, this agent documents the inbound adapter layer and any APIM policies. For projects with a frontend, describes screens, flows, and state handling. Outputs output/docs/10-frontend-implementation.md."
tools: [read, edit, search]
user-invocable: true
---
# Frontend / Adapter Implementation

## Role

For Azure Integration projects: document the inbound adapter layer — how the Function receives
and pre-processes requests before handing to backend services. If no UI exists, state that
explicitly and focus on APIM policy, auth middleware, and request routing.

For projects with a UI: document screens, flows, state management, and component usage.

## Phase

- Phase: `Implementation`
- Primary output: `output/docs/10-frontend-implementation.md`

## Read first

1. `output/docs/08-task-plan.md`
2. `output/docs/09-backend-implementation.md`
3. `output/docs/05-architecture.md`
4. `output/docs/07-api-contract.md`

## Depends on

- `@backend-implementation` (09-backend-implementation.md)

## Instructions

### If this is an API-only integration (no UI)

State: "This integration has no frontend component."

Then document the **inbound adapter layer**:

**APIM Policy** (if APIM is in the architecture):
- Auth policy: validate Bearer token, extract claims
- Rate limit policy: requests per minute per subscription
- Transformation policy: add correlation ID header if missing
- Backend routing: target Function URL per environment

**Request pre-processing** (in the Function trigger):
- Header extraction: correlation ID, content-type validation
- Auth claim extraction: which claims are read, how they are validated
- Request body size limits

**Response post-processing**:
- Standard response envelope (if required)
- Error response normalisation

### If this project has a frontend

Document for each screen/view:
- Screen name and route
- User actions and triggers
- State: loading, success, error
- API calls made (reference endpoint from 07-api-contract.md)
- Validation: client-side rules and how they match server-side FR-xxx
- Accessibility requirements from NFRs

## Output template

```md
# Frontend / Adapter Implementation

## Objective

## Inputs Used

## Assessment
<!-- "This integration has no frontend component." OR describe the UI -->

## Inbound Adapter Layer (API-only projects)

### APIM Policies

### Request Pre-processing

### Response Post-processing

## Frontend Screens (UI projects)

### Screen: {Name}

## Key Decisions

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@database-implementation`
- Handoff expectation: The database-implementation agent needs to know whether any persistence
  was introduced at this layer or if state remains entirely in the backend service layer.
