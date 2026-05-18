# Customization Guide

## Safe customization areas

You can customize the framework by extending:

- agent instructions under `.claude/agents/`
- rules under `.claude/rules/`
- hooks under `.claude/hooks/`
- validators under `.claude/validators/`
- skills under `.claude/skills/`

## Recommended approach

1. Keep artifact paths stable.
2. Change one phase at a time.
3. Update contracts when phase inputs or outputs change.
4. Keep smoke and validation scripts passing after every change.
