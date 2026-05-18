# Running the Framework

## Quick start

1. Place source files under `input/`.
2. Run `./.claude/test-hook-simple.sh`.
3. Run `./.claude/scripts/validate-artifacts.sh`.
4. Run `./.claude/scripts/run-pipeline.sh`.
5. Run `./tests/test-smoke.sh` when validating the framework itself.

## Notes

The current runner is lightweight. It validates setup and prints orchestration metadata, but it does not yet execute every phase automatically.
