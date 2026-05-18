# Analysis Report

## 1. Executive Summary

`custom-agent-framework` is the broadest SDLC scaffold in terms of visible phase decomposition. It models an 11-phase AI-assisted delivery pipeline that runs from raw business inputs through design, planning, implementation, testing, quality, compliance, coverage analysis, deployment, consolidated reporting, and documentation.

Its biggest strengths are:

- very clear phase breakdown
- explicit artifact ownership and handoff contracts
- lightweight runtime, validators, scripts, and smoke tests already present
- transparent "open questions over hidden assumptions" mindset
- easy-to-understand folder structure

Its biggest weakness is maturity depth. Compared with `sdlc`, it is more scaffold than platform. Compared with `spec-kit`, it has stronger end-to-end pipeline coverage but weaker artifact depth and execution method. It has the bones of a serious framework, but many parts are still template-level rather than production-strength.

## 2. Framework Overview

### Purpose

The framework is meant to take a set of required markdown inputs and move them through a greenfield delivery pipeline composed of specialized agents. The intended output is a broad set of delivery artifacts under `output/docs/`.

### Primary Operating Model

The repo centers on:

1. source inputs in `input/`
2. phase and agent definitions under `.claude/agents/`
3. contracts, validators, rules, hooks, and runtime state under `.claude/`
4. generated outputs in `output/docs/`

The current model is largely sequential and declarative: the repo explains what each phase should read, write, and hand off, and provides helper scripts to validate the framework structure.

### Key Repo Signals

- `README.md` positions the project as a usable framework starter, not a full enterprise runtime.
- `docs/framework-overview.md` confirms the 11-phase flow.
- `.claude/200-greenfield-orchestrator.md` is the center of the orchestration design.
- `.claude/contracts/*` define artifact ownership and phase I/O.
- `tests/test-smoke.sh` proves the framework now has more than just a directory diagram.

## 3. What Exists in the Repository

### Core Building Blocks

| Area | Evidence | Notes |
|---|---|---|
| Orchestration spec | `.claude/200-greenfield-orchestrator.md` | Central process definition. |
| Agent library | `.claude/agents/1 Requirement/` through `11 Documentation/` | Broad lifecycle coverage. |
| Contracts | `.claude/contracts/artifact-registry.yaml`, `phase-input-output-map.yaml`, `input-schema.json` | Good structural discipline. |
| Runtime state | `.claude/runtime/project-state.yaml`, `orchestrator-runner.py` | Present, but lightweight. |
| Validators | `.claude/validators/*.py` | Better than a pure prompt scaffold. |
| Hooks and rules | `.claude/hooks/`, `.claude/rules/` | Governance intent is visible. |
| Scripts | `.claude/scripts/*.sh` | Basic execution and inspection support. |
| Tests | `tests/test-smoke.sh` | Minimal but useful. |
| Docs and internal analysis | `docs/*.md`, `docs/analysis/*.md` | The framework is self-reflective about its maturity. |

### Important Files

- `README.md`: gives an honest maturity statement and a recommended reading order.
- `diagram.md`: captures the original directory/phase design.
- `docs/framework-overview.md`: concise summary of the main flow.
- `.claude/contracts/phase-input-output-map.yaml`: a key file for phase handoffs.
- `.claude/contracts/artifact-registry.yaml`: important for artifact ownership.
- `.claude/runtime/orchestrator-runner.py`: evidence of initial runtime support.
- `tests/test-smoke.sh`: validates key framework assets exist and basic runtime inspection works.
- `docs/analysis/FRAMEWORK_EXECUTIVE_SUMMARY.md`: useful context, but parts of it reflect an earlier maturity snapshot and should not be treated as the sole source of truth for the current repo.

## 4. SDLC Coverage

| Phase | Coverage | Evidence | Assessment |
|---|---|---|---|
| Requirement | Strong | multiple requirement agents | Good decomposition of intake and consolidation. |
| Design | Strong | architecture, DB, API, tech stack agents | Broad design coverage. |
| Planner | Moderate | dedicated planner agent | Clear phase, but output depth depends on execution quality. |
| Implementation | Moderate | backend, frontend, DB, component library agents | Good structural split, still template-driven. |
| Testing | Moderate | test suite, frontend tests, accessibility, test data | Broader than most starter frameworks. |
| Quality | Moderate | code, design, branding checks | Valuable distinction from generic testing. |
| Compliance | Moderate | dedicated compliance phase | Present, but not deeply industrialized. |
| Coverage / security / performance | Moderate | coverage analyzer phase | Strong conceptually; evidence of deep automation is limited. |
| Deployment | Moderate | deployment phase exists and smoke test checks a deployment agent | Better than older analysis docs suggested. |
| Consolidated reporting | Moderate | dedicated reporting phase | Useful for leadership/traceability. |
| Documentation | Moderate | final documentation phase | Good lifecycle completeness. |

### Overall SDLC Position

In terms of visible lifecycle breadth, this framework is the most comprehensive of the three. In terms of enforcement depth and execution maturity, it is not. It covers "what phases should exist" better than "how each phase is executed reliably at scale."

## 5. Architecture and Operating Model

### Strengths in the Architecture

1. **Excellent phase decomposition**
   The 11-phase model separates concerns more clearly than most AI workflow repos.

2. **Contracts as first-class objects**
   Artifact registry and phase I/O mapping are good design choices. They reduce ambiguity between stages.

3. **Minimal runtime dependency**
   The framework is lightweight and understandable. It does not require a heavy platform to inspect or start using.

4. **Governance surfaces exist**
   Hooks, rules, validators, and scripts are all represented, which is a positive signal.

### Architectural Limits

1. Many agents are still instruction templates rather than deeply engineered prompts.
2. Runtime behavior is still shallow compared with the conceptual pipeline.
3. There is little evidence of branching logic, rollback behavior, or advanced orchestration.
4. The framework is currently more single-pattern than multi-platform or multi-customer.

## 6. Inputs, Outputs, and Artifact Contracts

### What It Does Well

- Requires a defined set of input files.
- Explicitly maps which phase reads and writes which artifacts.
- Separates ownership from execution.
- Emphasizes transparent handling of unresolved questions.

### Why This Matters

Many AI-SDLC frameworks fail because later phases consume vague or inconsistent context. This framework is directionally correct in using contracts and registries to reduce that problem.

### Remaining Gaps

- Artifact schemas are lighter than in `sdlc`.
- Outputs are mostly markdown documents rather than strongly typed lifecycle contracts.
- There is limited evidence of automatic change propagation or traceability analytics.

## 7. Governance, Guardrails, and Compliance

### Pros

- Governance is explicitly represented through hooks, rules, validators, and compliance gates.
- Compliance is treated as its own lifecycle phase, not folded vaguely into testing.
- Branding and design compliance are modeled separately, which is a useful enterprise distinction.

### Cons

- Governance artifacts are still relatively shallow in comparison to the breadth of the pipeline.
- Policy layering is not as sophisticated as `sdlc`'s core/sdlc/platform/customer model.
- There is limited evidence of deterministic compliance measurement at the same level as `sdlc`'s compliance runner.

### Industry Alignment

The framework aligns with best practices around:

- explicit artifact handoffs
- broad SDLC coverage
- validation before/after phase transitions
- preserving unresolved questions instead of inventing answers

It aligns less strongly with:

- enterprise guardrail composition
- measurable evaluation programs
- observability and run analytics

## 8. Testing, Validation, and Evaluation

### What Exists

- input validation
- artifact validation
- phase handoff validation
- smoke test
- runtime inspection script

### Pros

- More validation exists than the repo's starter-kit appearance might initially suggest.
- The smoke test is practical and verifies framework wiring.
- Validators indicate the framework is moving toward enforceable contracts rather than pure documentation.

### Cons

- Testing depth is still shallow relative to the number of phases.
- No clear evaluation harness for agent output quality, consistency, or failure recovery.
- Performance, security, and coverage are modeled as phases, but not yet obviously backed by rich automated pipelines.

## 9. Developer Experience and Extensibility

### Pros

- Very readable and easy to navigate.
- The phase numbering is intuitive.
- Good onboarding path through README and docs.
- Easier to reason about than a highly abstract policy engine.

### Cons

- There is no strong packaged CLI/API/runtime surface for broad reuse.
- Extensibility is less industrial than `sdlc`; there is no equally clear platform/customer scaffolding story.
- Scaling beyond the original greenfield pattern likely requires significant framework engineering.

## 10. Maturity Scorecard

| Dimension | Rating | Notes |
|---|---|---|
| Lifecycle breadth | High | The 11-phase spread is the broadest of the three. |
| Execution depth | Low to moderate | Much stronger conceptually than operationally. |
| Governance strength | Moderate | Good structural components, but not yet deep enough. |
| Machine-readable contracts | Moderate | Contracts exist, but typed artifact rigor is still lighter than `sdlc`. |
| Extensibility | Moderate | Adaptable, but not yet industrialized as a reusable platform. |
| Observability | Low | Minimal runtime analytics and run history. |
| Evaluation discipline | Low | Major opportunity area. |
| Enterprise readiness | Moderate-minus | Promising starter, not yet a high-confidence enterprise platform. |

## 11. Best Fit and Misfit Scenarios

### Best Fit

- teams designing a custom AI delivery framework from scratch
- groups that want a visible, teachable multi-phase SDLC model
- organizations prioritizing phase clarity and artifact ownership before deep automation
- internal experiments where a lightweight framework is preferable to a heavier platform

### Misfit / Caution Areas

- teams needing proven execution depth and rich telemetry immediately
- enterprises requiring strong multi-platform policy overlays and packaged runtime targets
- delivery programs that need benchmarked output quality and reliable automated recovery behavior

## 12. Pros

1. **Best visible end-to-end SDLC breadth**
   Requirement through documentation is all represented clearly.

2. **Clear handoff thinking**
   Contracts and registries are a real strength.

3. **Honest and transparent framework design**
   The repo is explicit about current maturity rather than pretending to be finished.

4. **Lightweight and understandable**
   Easy for a team to inspect and adapt.

5. **Separate quality/compliance/coverage/deployment concerns**
   This is closer to how real delivery organizations think than a generic build/test loop.

## 13. Cons

1. **Template depth is still limited**
   The number of phases is impressive, but many agent definitions are still thin.

2. **Operational maturity trails conceptual maturity**
   The framework explains the pipeline better than it executes it.

3. **Weak observability**
   There is little evidence of metrics, run histories, dashboards, or failure analytics.

4. **Limited enterprise packaging story**
   Compared with `sdlc`, there is less evidence of runtime-targeted distribution and platform composition.

5. **Evaluation is underdeveloped**
   Breadth exists, but quality measurement and benchmark discipline do not yet match it.

## 14. Alignment with Industry AI-SDLC Best Practices

| Best-Practice Area | Current Alignment | Notes |
|---|---|---|
| Requirements traceability | Moderate | Good phase I/O mapping, lighter machine-readability. |
| Human approval gates | Moderate | Review mindset is present, but explicit gate mechanics are lighter than `sdlc`. |
| Policy guardrails | Moderate | Governance surfaces exist, but layering is less advanced. |
| Artifact contracts | Moderate | Good design intent, moderate enforcement maturity. |
| Testing and validation | Moderate | Better than many starter kits, still not deep enough for full confidence. |
| Compliance evidence | Moderate | Dedicated compliance phase is a plus. |
| CI/CD integration | Weak to moderate | Some scripts exist, but pipeline integration is not a major differentiator yet. |
| Observability | Weak | One of the largest gaps. |
| Continuous evaluation | Weak | Major opportunity area. |
| Prompt/tool safety | Weak to moderate | The framework is structured, but explicit tool-safety and prompt-injection controls are not yet prominent. |
| Audit trails and approvals | Weak to moderate | There is state and validation, but approval history and reviewer traceability are limited. |
| Cost and latency governance | Weak | No strong visible runtime budgeting or resource controls. |
| Model portability | Moderate | The phase design is portable, but explicit multi-runtime/model conformance is limited. |

## 15. Recommended Improvements

### Priority 1: Deepen agent specifications

- expand each agent prompt with richer instructions, examples, failure handling, and output quality checks
- make phase outputs less template-like and more execution-ready

### Priority 2: Strengthen runtime behavior

- turn the orchestrator from inspector/starter into a true execution engine
- add explicit approval states, resumability, retries, and rollback logic

### Priority 3: Improve artifact rigor

- add machine-readable schemas for key outputs
- validate every handoff automatically
- make artifact versions and lineage explicit

### Priority 4: Add observability and evaluation

- record run events, durations, retries, and validation failures
- create benchmark scenarios per phase
- score output completeness and defect leakage

### Priority 5: Improve packaging and scale-out

- add a reusable CLI/API surface
- support multiple platform or customer overlays
- integrate with CI/CD and release evidence workflows

### Priority 6: Add operating controls and measurable safety

- add explicit approval gates with durable audit history
- define prompt-injection and tool-execution safety rules
- track run duration, cost, retries, and failed handoffs
- introduce benchmark projects and conformance tests across phases

## 16. Bottom Line

`custom-agent-framework` has the strongest SDLC breadth and one of the clearest phase-by-phase conceptual models in the comparison. It is especially good for teams that want a visible, teachable delivery pipeline with explicit handoffs and specialized responsibilities.

Its challenge is not vision; it is depth. To become a high-confidence framework, it needs stronger prompts, stronger runtime execution, stronger machine-readable contracts, and much better observability. If those are added, it could become a compelling bridge between prompt-first scaffolds and enterprise-grade AI delivery systems.
