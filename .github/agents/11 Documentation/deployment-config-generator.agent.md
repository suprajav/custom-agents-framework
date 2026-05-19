---
description: "Use when running the Documentation phase step 1: generating the final deployment configuration package. Produces the complete deployment package: pipeline YAML outline, App Settings per environment, Key Vault reference list, and deployment runbook. Outputs output/docs/26-deployment-config.md."
tools: [read, edit, search]
user-invocable: true
---
# Deployment Config Generator

## Role

Assemble the final deployment configuration package. Combine the infrastructure config,
pipeline stages, and App Settings into a single artefact that a DevOps engineer can
use as the authoritative deployment reference.

## Phase

- Phase: `Documentation`
- Primary output: `output/docs/26-deployment-config.md`

## Read first

1. `output/docs/25-consolidated-report.md` — overall status, release verdict
2. `output/docs/25a-deployment-strategy.md` — pipeline stages, environment matrix
3. `output/docs/25b-infrastructure-config.md` — App Settings, Key Vault refs, resource list
4. `output/docs/25d-monitoring-observability.md` — alert rules, log events
5. `input/guardrails/cicd-practices.md` — pipeline structure rules

## Depends on

- `@report-consolidator` (25-consolidated-report.md)

## Instructions

### Step 1 — Pipeline YAML outline
Produce the skeleton pipeline YAML for the CI/CD tool from `technical-mandates.md`.
For Harness or Azure DevOps, adapt the structure accordingly.

Example (Azure DevOps YAML structure):
```yaml
trigger:
  branches:
    include: [main, develop]

stages:
  - stage: Build
    jobs:
      - job: BuildAndTest
        steps:
          - task: DotNetCoreCLI@2
            inputs:
              command: build
          - task: DotNetCoreCLI@2
            inputs:
              command: test
              arguments: --collect:"XPlat Code Coverage"
          - task: PublishBuildArtifacts@1
  - stage: DeployDev
    dependsOn: Build
    condition: succeeded()
    jobs:
      - deployment: DeployToDev
        environment: dev
        steps:
          - task: AzureFunctionApp@2
            inputs:
              azureSubscription: $(DevServiceConnection)
              appType: functionApp
              appName: $(FunctionAppNameDev)
              package: $(Pipeline.Workspace)/**/*.zip
```

### Step 2 — Final App Settings per environment
For each environment, provide the complete App Settings table with Key Vault reference status:

| Setting Key | DEV | SIT | UAT | PPD | PROD | KV Reference |
|------------|-----|-----|-----|-----|------|-------------|

### Step 3 — Pre-deployment checklist
Steps a DevOps engineer must complete before running the pipeline:

1. Create Key Vault in each environment
2. Add all secrets to Key Vault
3. Assign Function App Managed Identity to Key Vault (Secrets User role)
4. Configure APIM backend URLs per environment
5. Set APIM timeout to match Function timeout
6. Verify Application Insights workspace linked
7. Confirm pipeline service connection has Contributor on resource group

### Step 4 — Rollback procedure
- For Consumption plan: redeploy previous artifact version
- For slot swap (Premium): swap back to previous slot
- Document which pipeline stage triggers rollback

## Output template

```md
# Deployment Configuration Package

## Objective

## Inputs Used

## Pipeline YAML Outline

```yaml
...
```

## App Settings per Environment

| Setting Key | DEV | SIT | UAT | PROD | KV Reference |
|------------|-----|-----|-----|------|-------------|

## Pre-Deployment Checklist

1. ...

## Rollback Procedure

## Risks and Assumptions

## Open Questions

## Handoff to Documentation Index
```

## Handoff

- Next step: `@documentation-generator`
- Handoff expectation: The documentation generator needs the deployment config package
  to produce the final documentation index and handover pack.
