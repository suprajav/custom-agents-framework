# Troubleshooting

## Common issues

### Missing input files
Run `./.claude/test-hook-simple.sh` to see which required files are missing.

### Contract validation failures
Run `./.claude/scripts/validate-artifacts.sh` and review the failing validator.

### Smoke test failure
Run `./tests/test-smoke.sh` directly and inspect the first failing command.

### Empty output folder
The framework currently validates and scaffolds behavior; it does not yet generate a full artifact set automatically.
