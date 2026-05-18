# Pre-run Validation Hook

## Purpose

Run before the orchestrator or any phase execution begins.

## Minimum checks

- required input files exist
- `output/docs/` exists or can be created
- settings and state files are present
- deployment phase visibility is known

## Failure behavior

If a required input or runtime file is missing, stop the run and report the missing path explicitly.
