# custom-agent-framework

`custom-agent-framework` is a greenfield delivery scaffold built from the structure in `diagram.md` and then extended into a working starter framework.

It now contains:

- a phase-based agent pipeline from Requirement through Documentation
- a populated Deployment phase
- a basic orchestrator plus runtime state and runner
- contracts for artifact ownership and phase handoffs
- starter hooks, rules, scripts, validators, and skills
- framework documentation and analysis notes
- smoke-test coverage and sample output artifacts

This is not yet a full enterprise runtime, but it is now a usable framework starter rather than just a folder tree.

## What is in this folder

### Core framework files

- `diagram.md`  
  The original structure/reference diagram used to build this framework.

- `.claude/200-greenfield-orchestrator.md`  
  The top-level orchestration spec for the whole flow.

- `.claude/settings.json` and `.claude/settings.local.json`  
  Core framework configuration.

### Agent pipeline

The main phase agents live under:

- `.claude/agents/1 Requirement/`
- `.claude/agents/2 Design/`
- `.claude/agents/3 Planner/`
- `.claude/agents/4 Implementation/`
- `.claude/agents/5 Testing/`
- `.claude/agents/6 Quality/`
- `.claude/agents/7 Compliance/`
- `.claude/agents/8 Coverage Analyzer/`
- `.claude/agents/9 Deployment/`
- `.claude/agents/10 Consolidated Report/`
- `.claude/agents/11 Documentation/`

### Runtime and contracts

- `.claude/runtime/project-state.yaml`  
  Starter state tracking file.

- `.claude/runtime/orchestrator-runner.py`  
  Lightweight runtime entrypoint for validating and inspecting the framework.

- `.claude/contracts/artifact-registry.yaml`  
  Maps important artifacts to their owning agent.

- `.claude/contracts/phase-input-output-map.yaml`  
  Defines phase handoffs and expected read/write paths.

- `.claude/contracts/input-schema.json`  
  Simple machine-readable input inventory contract.

### Governance and validation

- `.claude/hooks/`  
  Pre/post framework checks.

- `.claude/rules/`  
  Core output, phase transition, and compliance gate rules.

- `.claude/validators/`  
  Input, artifact, and phase-handoff validation scripts.

- `.claude/skills/`  
  Reusable starter skills for summarization, schema checking, and API-focused work.

### Scripts and testing

- `.claude/scripts/run-pipeline.sh`  
  Runs the lightweight validation and runtime flow.

- `.claude/scripts/run-phase.sh`  
  Placeholder phase runner.

- `.claude/scripts/inspect-state.sh`  
  Prints the current runtime state file.

- `.claude/scripts/validate-artifacts.sh`  
  Runs the current validator set.

- `tests/test-smoke.sh`  
  End-to-end smoke check for the framework starter.

- `tests/fixtures/`  
  Starter fixture content.

### Inputs and outputs

- `input/`  
  Source materials the framework expects.

- `output/docs/`  
  Sample output artifacts and future generated documents.

### Documentation and analysis

- `docs/`  
  Usage and customization guides.

- `docs/analysis/`  
  Moved analysis files, roadmaps, and framework gap notes.

- `card demo/`  
  Placeholder area for a demo project or showcase flow.

## How to use it

### 1. Review the framework structure

Start with:

- `diagram.md`
- `.claude/200-greenfield-orchestrator.md`
- `docs/framework-overview.md`

### 2. Prepare inputs

Populate or refine the files under `input/`:

- `Automate Insurance Quote Extraction Process_PDD.md`
- `User Stories List.md`
- `technical-mandates.md`
- `coding-best-practices.md`
- `compliance-requirements.md`
- `branding-guidelines.md`
- `README.md`

### 3. Run the basic checks

From the framework root:

```bash
./.claude/test-hook-simple.sh
./.claude/scripts/validate-artifacts.sh
./tests/test-smoke.sh
```

### 4. Inspect the framework runtime

```bash
python3 .claude/runtime/orchestrator-runner.py
./.claude/scripts/inspect-state.sh
```

### 5. Follow the phase flow

Use the orchestrator and agent files as the source of truth for phase order:

1. Requirement
2. Design
3. Planner
4. Implementation
5. Testing
6. Quality
7. Compliance
8. Coverage Analyzer
9. Deployment
10. Consolidated Report
11. Documentation

## Recommended reading order

If you are new to this framework, use this order:

1. `README.md`
2. `diagram.md`
3. `docs/framework-overview.md`
4. `docs/running-the-framework.md`
5. `.claude/200-greenfield-orchestrator.md`
6. `docs/analysis/custom_fw_gap_summary.md`
7. `docs/analysis/custom_fw_roadmap.md`

## Current maturity

The framework currently has:

- a complete visible phase structure
- a working Tier 1 foundation
- early Tier 2 additions such as validators, starter docs, skills, and sample outputs

It still needs:

- deeper agent prompts and richer acceptance criteria
- stronger runtime behavior
- broader tests
- richer documentation/examples
- a CLI or API surface for larger-scale use

## Quick summary

If you want to work on it next, the best next step is:

1. deepen the agent files
2. expand the validator/test depth
3. improve runtime behavior
4. grow the docs and examples
5. add a real execution surface
