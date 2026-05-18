# custom-agent-framework roadmap

## Tier 1: make it functional

This is the minimum practical implementation layer.

### Status

Tier 1 foundation is now in place.

### Goals

- complete the missing deployment phase
- make the orchestrator stateful
- add handoff contracts
- add basic validation
- add core rules/hooks

### What was added

- populated `custom-agent-framework/.claude/agents/9 Deployment/`
- added `custom-agent-framework/.claude/runtime/`
- added `custom-agent-framework/.claude/contracts/`
- populated `custom-agent-framework/.claude/rules/`
- populated `custom-agent-framework/.claude/hooks/`
- added scripts under `custom-agent-framework/.claude/scripts/`
- added `custom-agent-framework/tests/test-smoke.sh`
- added `custom-agent-framework/README.md`

### Outcome

The framework is now operationally usable as a guided pipeline starter and passes its smoke test.

## Tier 2: make it robust

This is the depth and reliability layer.

### Status

Tier 2 has started.

### Goals

- deepen all agent specifications
- add validation and reusable skills
- add real documentation
- add fixtures and example outputs

### Work items

1. Expand each agent with richer prompts and acceptance checks
2. Add `custom-agent-framework/.claude/validators/`
3. Add `custom-agent-framework/.claude/skills/`
4. Add framework docs under `custom-agent-framework/docs/`
5. Add tests and fixtures
6. Add sample output artifacts under `custom-agent-framework/output/docs/`

### Already added

- validator layer under `.claude/validators/`
- starter skills under `.claude/skills/`
- starter framework docs under `docs/`
- sample output artifacts under `output/docs/`
- starter fixture content under `tests/fixtures/`

### Outcome

The framework is becoming credible for repeated delivery use, but deeper agent specifications and broader tests are still needed.

## Tier 3: make it enterprise-ready

This is the scale and operability layer.

### Goals

- add a real execution surface
- improve governance
- support packaging and reuse

### Work items

1. Add a CLI or runnable script entrypoint
2. Add approval and audit checkpoints
3. Add packaging/distribution support
4. Add CI/CD integration patterns
5. Add multi-project or tenant-aware controls if needed

### Outcome

The framework becomes suitable for larger delivery teams and repeated rollout.

## Recommended order

Build in this sequence:

1. Deeper agent prompts
2. Broader validators and tests
3. Stronger runtime behavior
4. Richer docs/examples
5. CLI/package/governance scale-up

## Recommended immediate next step

Continue with **Tier 2**.

If only one item is tackled now, make it this:

- deepen the agent files with richer prompts, acceptance criteria, and failure handling

That gives the biggest functional improvement with the least ambiguity.
