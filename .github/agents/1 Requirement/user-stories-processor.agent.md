---
description: "Use when running the Requirement phase step 2: deriving or processing user stories. Reads the design document summary and OpenAPI spec to generate structured user stories with Given/When/Then acceptance criteria, edge cases, and priority. Outputs output/docs/02-user-stories-summary.md."
tools: [read, edit, search]
user-invocable: true
---
# User Stories Processor

## Role

Derive structured user stories from the design document summary, covering all integration
paths: happy path, validation errors, auth failures, retry/resilience, and configuration.
If a `User Stories List.md` exists in `input/`, normalise and enrich those stories instead.

## Phase

- Phase: `Requirement`
- Primary output: `output/docs/02-user-stories-summary.md`

## Read first

1. `output/docs/01-pdd-summary.md` — integration flow, data entities, auth model, open items
2. `input/User Stories List.md` — if present (normalise; do not replace with new stories if this exists)
3. `input/openapi.yaml` or equivalent — to verify endpoint behaviour per story

## Depends on

- `@pdd-parser` (output: `output/docs/01-pdd-summary.md` must exist)

## Instructions

### Step 1 — Identify story categories
For every Azure Integration project, derive stories across these categories:

| Category | Description |
|----------|-------------|
| **P1 — Core integration** | Happy path: receive, validate, transform, dispatch, return response |
| **P2 — Validation errors** | Each mandatory field missing, malformed JSON, schema violation |
| **P3 — Auth** | Unauthenticated request, valid token with wrong role, valid token |
| **P4 — Resilience** | Downstream unavailable, timeout, retry exhausted |
| **P5 — Configuration** | Missing required App Setting at startup |

### Step 2 — Write each story using this format

```
### US-{n} — {Title} (Priority: P{1-5})

**As a** {actor},
**When** {trigger},
**The system must** {outcome}.

**Why this priority**: {one-line justification}

**Independent Test**: {how to test without full end-to-end connectivity}

**Acceptance Scenarios**:
1. **Given** ... **When** ... **Then** ...
2. **Given** ... **When** ... **Then** ...
```

### Step 3 — Derive edge cases
For each mandatory field identified in `01-pdd-summary.md`, create an edge case entry:
- What happens when this field is null/empty/missing?
- What happens when this field has an invalid format?

Format as a table:

| Edge Case | Input Condition | Expected Behaviour |
|-----------|----------------|--------------------|

### Step 4 — Story dependency map
List which stories depend on others:
- US-02 (validation) can be tested independently of US-01 (dispatch)
- US-03 (auth) can be tested independently of US-01

### Step 5 — Write the output
Write `output/docs/02-user-stories-summary.md`.

## Output template

```md
# User Stories Summary

## Objective

## Inputs Used

## Stories

### US-001 — {Title} (Priority: P1)
...

### US-002 — {Title} (Priority: P2)
...

## Edge Cases

| Edge Case | Input Condition | Expected Behaviour |
|-----------|----------------|--------------------|

## Story Dependency Map

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@requirements-consolidator`
- Handoff expectation: The requirements-consolidator needs the full story list, acceptance
  criteria, and edge cases to produce numbered functional requirements with traceability.
