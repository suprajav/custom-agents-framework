# custom-agent-framework missing files and likely next additions

## Remaining empty or missing content in existing structure

### Still light today

- `custom-agent-framework/card demo/` is still a placeholder only

Also still missing in practice:

- richer example outputs under `custom-agent-framework/output/docs/`
- richer fixture content under `custom-agent-framework/tests/fixtures/`

## Strongly justified new directories and files

These are the best next additions if the framework is meant to become more robust.

### Contracts

- `custom-agent-framework/.claude/contracts/artifact-registry.yaml`
- `custom-agent-framework/.claude/contracts/phase-input-output-map.yaml`
- `custom-agent-framework/.claude/contracts/input-schema.json`

### Runtime

- `custom-agent-framework/.claude/runtime/project-state.yaml`
- `custom-agent-framework/.claude/runtime/orchestrator-runner.py`

### Validators

- `custom-agent-framework/.claude/validators/validate-content-quality.py`
- `custom-agent-framework/.claude/validators/validate-report-completeness.py`

### Tests

- `custom-agent-framework/tests/test-phase-flow.py`
- `custom-agent-framework/tests/test-validator-failures.sh`
- `custom-agent-framework/tests/fixtures/`

### Documentation

- `custom-agent-framework/docs/framework-overview.md`
- `custom-agent-framework/docs/running-the-framework.md`
- `custom-agent-framework/docs/customization-guide.md`
- `custom-agent-framework/docs/troubleshooting.md`
- `custom-agent-framework/docs/phase-by-phase-guide.md`
- `custom-agent-framework/docs/output-artifact-guide.md`

## Existing folders that should be populated next

### hooks

Already added:

- `custom-agent-framework/.claude/hooks/pre-run-validation.md`
- `custom-agent-framework/.claude/hooks/post-phase-check.md`

Next useful additions:

- `custom-agent-framework/.claude/hooks/pre-release-gate.md`
- `custom-agent-framework/.claude/hooks/post-documentation-check.md`

### rules

Already added:

- `custom-agent-framework/.claude/rules/core-output-rules.md`
- `custom-agent-framework/.claude/rules/phase-transition-rules.md`
- `custom-agent-framework/.claude/rules/compliance-gate-rules.md`

Next useful additions:

- `custom-agent-framework/.claude/rules/deployment-readiness-rules.md`
- `custom-agent-framework/.claude/rules/documentation-quality-rules.md`

### scripts

Already added:

- `custom-agent-framework/.claude/scripts/run-pipeline.sh`
- `custom-agent-framework/.claude/scripts/run-phase.sh`
- `custom-agent-framework/.claude/scripts/inspect-state.sh`

Next useful additions:

- `custom-agent-framework/.claude/scripts/validate-artifacts.sh`
- `custom-agent-framework/.claude/scripts/publish-docs.sh`

### skills

Already added:

- `custom-agent-framework/.claude/skills/artifact-summarizer.md`
- `custom-agent-framework/.claude/skills/schema-checker.md`
- `custom-agent-framework/.claude/skills/openapi-helper.md`

Next useful additions:

- `custom-agent-framework/.claude/skills/deployment-checklist-helper.md`
- `custom-agent-framework/.claude/skills/test-design-helper.md`
- `custom-agent-framework/.claude/skills/documentation-summarizer.md`

## Why these matter

These additions close the biggest remaining framework gaps:

- Deeper validators make outputs trustworthy.
- Skills reduce duplication across agents.
- Docs and examples make the framework reusable by others.
- Sample outputs make expectations concrete.
- Broader tests make it safer to evolve.
