# Framework Enrichment Plan

## Objective

Transform the custom-agents-framework from placeholder templates into production-quality agent prompts capable of delivering Azure Integration projects end-to-end. The enrichment must be **generic** — applicable to any Azure Integration Services project, not just EMP.

---

## Reference Material

- **EMP Repo** (`AXAXL.Integration.EMP`): A completed Azure Function App project built using SpecKit
- **EMP Inputs** (placed in `input/emp-usecase/`):
  - `EMP-System Adaptor- Low Level De_*.pdf` — Low-Level Design document
  - `EMP_OpenAPI.yaml` — Inbound/outbound API contract
- **EMP Guardrails** (from EMP repo `guardrails/`):
  - `00-project-structure.md` — Solution layout rules
  - `01-functionapp-code-practices.md` — DI, config, auth, validation, HTTP clients, logging, errors
  - `02-testing-practices.md` — Test structure, coverage, mocking, assertions, fixtures
  - `03-cicd-practices.md` — Pipeline, build, artifacts, deployment, environment parity
  - `04-crosscutting-practices.md` — Shared libs, runtime, source control, AI guardrails

---

## Current State vs Target State

| Dimension | Current | Target |
|-----------|---------|--------|
| Agent prompt length | ~40 lines (template) | 150-250 lines (executable instructions) |
| Input awareness | Generic placeholders | Knows LLD, OpenAPI, guardrails, constitution |
| Output depth | "Objective / Key Decisions" prose | Mapping tables, decision matrices, code, configs |
| Technology awareness | None | Azure Functions, APIM, .NET 8, Key Vault, Harness |
| Validation | Section headings only | Constitution checks, guardrail compliance matrix |
| Test output | "Write tests" | xUnit classes, Moq setup, JSON fixtures, coverage targets |

---

## New Input Schema

### Expected Inputs for Azure Integration Projects

```
input/
├── README.md                    ← Input manifest (describes what's provided)
├── lld.md (or lld.pdf)          ← Low-Level Design document (primary source)
├── openapi.yaml                 ← API contract (inbound and/or outbound)
├── guardrails/                  ← Organisation standards
│   ├── project-structure.md     ← Solution layout rules
│   ├── code-practices.md        ← DI, config, auth, validation patterns
│   ├── testing-practices.md     ← Test strategy, mocking, coverage
│   ├── cicd-practices.md        ← Pipeline, deployment, artifacts
│   └── crosscutting.md          ← Shared libraries, runtime, naming
├── constitution.md              ← Non-negotiable architecture principles
└── {usecase-name}/              ← Use-case specific files (optional)
    ├── *.pdf                    ← Source design documents
    └── *.yaml                   ← API specs
```

---

## Phase-by-Phase Enrichment

### Phase 1: Requirement (3 agents)

| Agent | Current Role | New Role | Key Changes |
|-------|-------------|----------|-------------|
| `pdd-parser` | Parse generic PDD | **LLD Parser** — parse design document | Extract: integration flow (source → function → target), data entities, environments, APIs consumed/exposed, auth model, SLAs, constraints |
| `user-stories-processor` | Normalize stories | **Story Derivation** — derive from LLD | Generate stories per integration path (happy, error, auth, retry) with Given/When/Then acceptance criteria and edge cases |
| `requirements-consolidator` | Merge inputs | **Requirements Baseline** | Produce numbered FR-001/NFR-001 list, traceability matrix (LLD section → FR → story), mandatory field lists |

### Phase 2: Design (4 agents)

| Agent | New Behaviour |
|-------|---------------|
| `tech-stack-configurator` | Decision matrix evaluating options against guardrails. Output: runtime, framework, auth, serialization, testing, packages — all with one-line justification |
| `architecture-designer` | C4 Level 2 Mermaid diagram + project structure (`Functions/Maps/Helpers/Models/Interfaces`), DI registrations, middleware pipeline, data flow sequence |
| `database-designer` | Becomes **Data Model Designer**: CDM inbound models, target outbound models, JSON Schemas, field types and constraints |
| `api-contract-designer` | Parse OpenAPI input → produce field mapping table (source → target), mandatory field validation rules, error response shapes, auth requirements |

### Phase 3: Planner (1 agent)

| Agent | New Behaviour |
|-------|---------------|
| `task-planner` | Phased backlog: P0 (prerequisites/blockers), P1 (scaffold + config), P2 (per-story implementation). Each task → FR-xxx. Dependency graph. Effort estimates (S/M/L) |

### Phase 4: Implementation (4 agents)

| Agent | Current Role | New Role |
|-------|-------------|----------|
| `backend-implementation` | Describe backend | Generate C# code: Program.cs (DI wiring), HTTP Trigger Processor, Mapper class, HTTP client helper, Schema validator, Error helper — all behind interfaces |
| `frontend-implementation` | Describe frontend | **Configuration & Harness**: deploy scripts, config-{env}.json with Key Vault refs, pipeline YAML, local.settings.example.json |
| `database-implementation` | Describe DB implementation | **Schema & Model Implementation**: C# model classes (CDM/ and Target/), JSON Schema files, NuGet.Config, Directory.Build.props |
| `component-library-builder` | Define UI components | **Shared Library Integration**: identify internal NuGet packages (auth, retry, serialization, exceptions), wire into DI, document version pins |

### Phase 5: Testing (4 agents)

| Agent | New Behaviour |
|-------|---------------|
| `test-suite-generator` | Generate xUnit test classes per layer (Processor, Mapper, Helper, Validator). Moq setup for interfaces. Coverage targets (80% overall, 95% critical). Test project structure |
| `frontend-test-generator` | **Integration Test Generator**: end-to-end HTTP trigger tests with mocked downstream, contract validation tests |
| `accessibility-validator` | **Schema Validation Tests**: JSON Schema pass/fail scenarios, malformed input tests, boundary cases |
| `test-data-generator` | Generate JSON test fixtures: valid payload, missing mandatory fields, malformed JSON, empty arrays, partial data. Stored in TestData/{FunctionName}/ |

### Phase 6: Quality (3 agents)

| Agent | New Behaviour |
|-------|---------------|
| `code-best-practices-enforcer` | Validate against guardrails: all services behind interfaces, singleton registrations, IHttpClientFactory usage, structured logging, no hardcoded secrets, fail-fast startup |
| `design-compliance-validator` | Compare implementation against architecture: undocumented endpoints, missing DI registrations, middleware gaps, model separation violations |
| `branding-compliance-checker` | **Naming & Convention Checker**: route naming (versioned), folder structure compliance, NuGet source compliance, .gitignore completeness |

### Phase 7: Compliance (1 agent)

| Agent | New Behaviour |
|-------|---------------|
| `compliance-checker` | Constitution check matrix (principle → evidence → pass/fail). Guardrail compliance table. Open items with severity ratings |

### Phase 8: Coverage Analyzer (4 agents)

| Agent | New Behaviour |
|-------|---------------|
| `code-coverage-analyzer` | Coverage heatmap: requirement × test type. Identify untested code paths. Recommend additional test scenarios |
| `security-scanner` | OWASP Top 10 check against architecture/code: auth bypass, injection points, secret exposure, transport security. Severity + mitigation |
| `memory-leak-detector` | Identify: unclosed HTTP clients, unbounded collections, event handler leaks, singleton state mutations |
| `performance-analyzer` | Identify: blocking async calls, missing cancellation tokens, large payload serialization, missing retry circuit breakers |

### Phase 9: Deployment (4 agents)

| Agent | New Behaviour |
|-------|---------------|
| `deployment-strategy-designer` | Multi-stage: Build → Approval → Deploy per env. Atomic zip deploy. Config-only deploy flag. Environment matrix |
| `infrastructure-config-generator` | Generate config-{env}.json templates, Key Vault reference patterns, App Settings validation list, Managed Identity setup |
| `release-readiness-checker` | Go/no-go checklist: packages resolvable, hostnames populated, tests green, coverage thresholds met, compliance gaps accepted |
| `monitoring-observability-planner` | Structured logging format, correlation ID propagation, Application Insights config, alert thresholds, health check endpoints |

### Phase 10-11: Reporting & Documentation (3 agents)

| Agent | New Behaviour |
|-------|---------------|
| `report-consolidator` | Executive dashboard: RAG per phase, top risks, compliance score, coverage %, open blockers |
| `deployment-config-generator` | Runbook: deploy steps, rollback procedure, env URLs, health checks, secret rotation |
| `documentation-generator` | Generate: API docs (from contract), project README, onboarding guide, artifact index with status |

---

## Implementation Order

| Step | Scope | Files Changed |
|------|-------|---------------|
| 1 | Rewrite `input/README.md` with new input schema | 1 file |
| 2 | Create `input/guardrails/` with generic templates | 5 files |
| 3 | Enrich Phase 1 agents (`.github/agents/1 Requirement/`) | 3 agent files |
| 4 | Enrich Phase 2 agents (`.github/agents/2 Design/`) | 4 agent files |
| 5 | Enrich Phase 3 agent (`.github/agents/3 Planner/`) | 1 agent file |
| 6 | Enrich Phase 4 agents (`.github/agents/4 Implementation/`) | 4 agent files |
| 7 | Enrich Phase 5 agents (`.github/agents/5 Testing/`) | 4 agent files |
| 8 | Enrich Phase 6-7 agents (`.github/agents/6 Quality/` + `7 Compliance/`) | 4 agent files |
| 9 | Enrich Phase 8 agents (`.github/agents/8 Coverage Analyzer/`) | 4 agent files |
| 10 | Enrich Phase 9 agents (`.github/agents/9 Deployment/`) | 4 agent files |
| 11 | Enrich Phase 10-11 agents (`.github/agents/10*/` + `11*/`) | 3 agent files |
| 12 | Update orchestrator to reflect new input schema | 1 agent file |
| 13 | Update `.github/copilot-instructions.md` | 1 file |

**Total: ~39 files to create/update**

---

## Key Design Principles

1. **Generic, not EMP-specific** — agents reference patterns (e.g. "CDM → Target mapping") not specific field names
2. **Guardrails as first-class inputs** — agents validate against provided guardrails, not hardcoded rules
3. **Constitution-driven** — every implementation decision traces back to a stated principle
4. **Output depth matches SpecKit** — tables, matrices, code blocks, not just prose
5. **Testable end-to-end** — place the EMP inputs in `input/` and run the full pipeline to validate
