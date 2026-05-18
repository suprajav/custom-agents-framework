# Input Folder Guide

This folder contains the source material for the greenfield pipeline.

## Required files

- `Automate Insurance Quote Extraction Process_PDD.md`: primary problem statement and business context
- `User Stories List.md`: user stories and acceptance-oriented requirements
- `technical-mandates.md`: non-negotiable technical constraints
- `coding-best-practices.md`: coding and engineering standards
- `compliance-requirements.md`: compliance and control expectations
- `branding-guidelines.md`: visual and content branding rules
- `README.md`: this guide

## How the pipeline uses these files

1. Requirement agents read the PDD and user stories.
2. Design agents combine requirements with mandates and standards.
3. Planner and Implementation agents derive work from the design outputs.
4. Testing, Quality, Compliance, and Coverage phases validate the planned solution.
5. Consolidated Report and Documentation summarize the final state in `output/docs/`.

## Authoring guidance

Keep each file concise, current, and specific. If a requirement is not final, mark it clearly so downstream agents can preserve it as an open question.
