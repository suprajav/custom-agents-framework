# Input Folder Guide

This folder contains all source material consumed by the pipeline agents.
The pipeline is designed for **Azure Integration Services** projects using .NET,
but the patterns apply to any event-driven or API-integration project.

---

## Required Inputs

### 1. Design Document (`lld.md` or a PDF in `{usecase}/`)
The primary source of truth. May be a Low-Level Design, Solution Design, or equivalent.
Agents parse this to extract:
- Integration flow: source system → integration layer → target system
- Data entities and canonical model
- Authentication and authorisation model
- Environment matrix (DEV / SIT / UAT / PPD / PROD)
- SLAs, constraints, and known open items

### 2. API Contract (`openapi.yaml` or `{usecase}/openapi.yaml`)
OpenAPI 3.x specification covering inbound and/or outbound APIs.
Agents use this to derive:
- Endpoint routes, methods, request/response schemas
- Field mapping tables (source → target)
- Mandatory vs optional fields
- Error response shapes and auth schemes

### 3. Guardrails (`guardrails/`)
Organisation-level coding and delivery standards.
Each file is consumed by specific phases:

| File | Used by |
|------|---------|
| `guardrails/project-structure.md` | Architecture, Implementation |
| `guardrails/code-practices.md` | Implementation, Quality |
| `guardrails/testing-practices.md` | Testing, Quality |
| `guardrails/cicd-practices.md` | Deployment |
| `guardrails/crosscutting.md` | All phases |

### 4. Constitution (`constitution.md`)
Non-negotiable architecture principles. Agents produce a **constitution check matrix**
(principle → evidence → pass/fail) as part of the Compliance phase.

### 5. Technical Mandates (`technical-mandates.md`)
Platform constraints, hosting targets, excluded technologies, NFRs.

### 6. Compliance Requirements (`compliance-requirements.md`)
Regulatory, security, and audit expectations.

---

## Optional Inputs

- `User Stories List.md` — pre-authored user stories (if provided; otherwise agents derive from LLD)
- `branding-guidelines.md` — visual and naming conventions
- `coding-best-practices.md` — project-level coding rules (supplements guardrails)
- `{usecase}/` — subfolder with use-case specific PDFs, specs, or schemas

---

## How the Pipeline Uses These Files

| Phase | Primary Inputs |
|-------|---------------|
| 1 Requirement | `lld.md`, `openapi.yaml`, `User Stories List.md` |
| 2 Design | Requirement outputs, `technical-mandates.md`, `guardrails/project-structure.md`, `openapi.yaml` |
| 3 Planner | All design outputs |
| 4 Implementation | Design outputs, `guardrails/code-practices.md`, `guardrails/crosscutting.md` |
| 5 Testing | Implementation outputs, `guardrails/testing-practices.md` |
| 6 Quality | Implementation + test outputs, `guardrails/code-practices.md` |
| 7 Compliance | Quality outputs, `compliance-requirements.md`, `constitution.md` |
| 8 Coverage Analyzer | Testing + compliance outputs |
| 9 Deployment | Coverage outputs, `guardrails/cicd-practices.md` |
| 10 Consolidated Report | All phase outputs |
| 11 Documentation | Consolidated report + deployment outputs |

---

## Authoring Guidance

- Mark unconfirmed values as `[TBC]` so agents record them as open questions
- Keep each file focused on its domain — do not merge concerns
- Version your OpenAPI spec in the `info.version` field
- Store environment-specific values in guardrails, not in the LLD
