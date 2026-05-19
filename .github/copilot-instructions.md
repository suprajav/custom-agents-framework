# Custom Agents Framework — Copilot Instructions

This workspace contains a multi-phase greenfield delivery framework for Azure Integration
/ .NET projects. It runs a sequenced pipeline of specialist agents that take design
documents and requirements as inputs and produce a full set of design, implementation,
quality, compliance, deployment, and documentation artifacts.

## Framework structure

| Folder | Purpose |
|--------|---------|
| `input/` | Source documents: LLD, OpenAPI spec, guardrails, technical mandates, compliance requirements |
| `input/guardrails/` | Reusable coding/testing/CI-CD/project-structure standards |
| `output/docs/` | All generated phase artifacts land here (27 files total) |
| `.github/agents/` | Copilot custom agents — one per pipeline phase |
| `.github/instructions/` | Always-on pipeline rules (output format, phase transitions, compliance gates) |
| `.github/skills/` | On-demand utilities: artifact summarizer, OpenAPI helper, schema checker |
| `.github/prompts/` | Focused entry-point prompts (e.g. swagger-first pipeline) |
| `.claude/` | Original Claude-format equivalents — kept for dual compatibility |

## Input schema (what agents expect)

| File / Folder | Purpose | Required |
|--------------|---------|----------|
| `input/lld.md` OR `input/{usecase}/` | Primary design document (LLD, PDD, or equivalent) | YES |
| `input/openapi.yaml` OR `input/{usecase}/*.yaml` | OpenAPI specification | Recommended |
| `input/technical-mandates.md` | Mandatory technology and process requirements | YES |
| `input/compliance-requirements.md` | Regulatory and organisational compliance rules | YES |
| `input/guardrails/project-structure.md` | Solution layout rules | YES |
| `input/guardrails/code-practices.md` | DI, config, auth, HTTP, error handling rules | YES |
| `input/guardrails/testing-practices.md` | Test naming, coverage targets, patterns | YES |
| `input/guardrails/cicd-practices.md` | Pipeline structure and deployment rules | YES |
| `input/guardrails/crosscutting.md` | NuGet, naming, source control, security | YES |
| `input/User Stories List.md` | Pre-existing user stories (optional enrichment) | Optional |
| `input/branding-guidelines.md` | UI branding rules (UI projects only) | Optional |

## Pipeline phases (in order)

1. **Requirement** — LLD parser → user stories processor → requirements consolidator
2. **Design** — tech stack → architecture → data model → API contract
3. **Planner** — task planner (P0/P1/P2 task backlog)
4. **Implementation** — backend (C#/.NET 8) → adapter/frontend → data model → shared library
5. **Testing** — test suite (xUnit/Moq/FA) → adapter tests → contract validator → test data
6. **Quality** — code best practices → design compliance → naming/standards compliance
7. **Compliance** — compliance checker (final gate)
8. **Coverage Analyzer** — coverage → security (OWASP) → memory/resource → performance
9. **Deployment** — strategy → infrastructure config → release readiness → monitoring
10. **Consolidated Report** — report consolidator (RAG status + blockers table)
11. **Documentation** — deployment config package → documentation index + handover

## Key rules (always apply)

- Every phase writes its output under `output/docs/` using the prescribed file name.
- Every output must include: Objective, Inputs Used, Key Decisions, Risks and Assumptions, Open Questions, Handoff.
- Do not advance a phase if its expected output artifact does not yet exist.
- Compliance findings must remain visible in the final report — never suppress them.
- A later phase must read the earlier outputs listed in its agent file before making new decisions.
- All blockers from any phase are release blockers until explicitly resolved.

## Running the pipeline

Use the `@greenfield-orchestrator` agent to run the full pipeline, or invoke individual
phase agents directly for a single phase. Before running, ensure `input/README.md` exists
and the required input files are in place.

