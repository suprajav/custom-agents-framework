---
description: "Use when running the Deployment phase step 2: generating infrastructure config. Produces App Settings templates, Key Vault reference patterns, config-{env}.json files, APIM backend configurations, and Bicep/ARM resource list for each environment. Outputs output/docs/25b-infrastructure-config.md."
tools: [read, edit, search]
user-invocable: true
---
# Infrastructure Config Generator

## Role

Produce the infrastructure configuration artefacts for each deployment environment:
App Settings templates, Key Vault reference patterns, per-environment config files,
and a list of Azure resources that must exist before deployment.

## Phase

- Phase: `Deployment`
- Primary output: `output/docs/25b-infrastructure-config.md`

## Read first

1. `output/docs/25a-deployment-strategy.md` — environment matrix, hosting plan
2. `output/docs/03-requirements-consolidated.md` — Required App Settings table
3. `output/docs/05-architecture.md` — component list
4. `input/guardrails/cicd-practices.md` — environment config format

## Depends on

- `@deployment-strategy-designer` (25a-deployment-strategy.md)

## Instructions

### Step 1 — Azure resource list
For each environment, list required Azure resources:

| Resource Type | Name Pattern | SKU/Plan | Purpose |
|--------------|-------------|---------|--------|
| Function App | {name}-{env} | Consumption / Premium EP1 | Host integration |
| App Service Plan | {plan}-{env} | per deployment strategy | Hosting plan |
| Key Vault | {name}-kv-{env} | Standard | Secrets management |
| Application Insights | {name}-ai-{env} | | Telemetry |
| APIM | (existing) | | Inbound gateway |

### Step 2 — App Settings template
Produce the App Settings template for the Function App.
For each setting, specify: key name, whether it is a Key Vault reference, description.

```json
{
  "AzureWebJobsStorage": "@Microsoft.KeyVault(VaultName={vault};SecretName=AzureWebJobsStorage)",
  "APPINSIGHTS_INSTRUMENTATIONKEY": "@Microsoft.KeyVault(VaultName={vault};SecretName=AppInsightsKey)",
  "{Feature}__TargetBaseUrl": "",
  "{Feature}__TargetPath": "",
  "{Feature}__TargetClientId": "@Microsoft.KeyVault(VaultName={vault};SecretName={Feature}TargetClientId)"
}
```

Rules:
- All secrets MUST use Key Vault reference syntax
- Use `__` not `:` as section separator for Azure App Settings
- Non-secret config values (URLs, paths) can be plain text

### Step 3 — config-{env}.json template
For non-sensitive configuration that varies by environment:

```json
// config-Development.json
{
  "{Feature}": {
    "TargetBaseUrl": "https://dev.target-system.example.com",
    "TargetPath": "/api/endpoint"
  }
}
```

One file per environment: `Development`, `SIT`, `UAT`, `PPD`, `Production`.

### Step 4 — Managed Identity setup
Document the Managed Identity assignments required:

| Identity | Resource | Role Assignment | Purpose |
|----------|---------|----------------|--------|
| Function App MSI | Key Vault | Key Vault Secrets User | Read secrets |
| Function App MSI | APIM | (if applicable) | Outbound calls |

### Step 5 — APIM backend configuration
If APIM is in the architecture, document:
- Backend URL per environment
- Auth policy (Managed Identity or subscription key)
- Timeout setting (must align with Function timeout from performance report)

## Output template

```md
# Infrastructure Config

## Objective

## Inputs Used

## Azure Resource List

| Resource Type | Name Pattern | SKU | Purpose |
|--------------|-------------|-----|--------|

## App Settings Template

```json
{}
```

## config-{env}.json Template

## Managed Identity Assignments

| Identity | Resource | Role | Purpose |
|----------|---------|------|--------|

## APIM Backend Configuration

## Risks and Assumptions

## Open Questions

## Handoff to Release Readiness
```

## Handoff

- Next step: `@release-readiness-checker`
- Handoff expectation: The release readiness checker needs the App Settings template,
  Key Vault references, and resource list to verify pre-deployment prerequisites.
