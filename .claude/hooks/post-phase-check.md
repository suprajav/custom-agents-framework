# Post-phase Check Hook

## Purpose

Run after each phase completes.

## Minimum checks

- expected phase artifact was written
- the artifact contains the required section headings
- unresolved issues remain visible in `Open Questions`
- next phase has enough context to continue

## Failure behavior

If the expected artifact is missing, do not advance the pipeline state.
