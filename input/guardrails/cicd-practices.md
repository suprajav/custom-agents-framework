# Guardrail: CI/CD and Deployment Practices

## Scope
Applies to all Azure Function App delivery pipelines. Covers build stages, artifact
management, deployment strategy, environment parity, and pipeline authentication.

---

## 1. Pipeline Structure
- Use a **multi-stage pipeline**: Build → Approval → Deploy (per environment)
- Gate all non-Dev deployments with a mandatory **human approval step**
- Only trigger full build for Dev; higher environments deploy pre-built, versioned artifacts
- Tests are a **mandatory gate** — never skip in build stage

## 2. Build Stage
- Sequence: `dotnet restore` → `dotnet build` → `dotnet test` → `dotnet publish`
- Set memory limits on build containers
- Publish with `--self-contained false` and explicit runtime (e.g. `win-x64`) for Azure Functions
- Use private registries for Docker and NuGet in production
- Enforce coverage thresholds in `dotnet test`; fail build if thresholds not met

## 3. Artifact Management and Versioning
- Version artifacts using Git tag or pipeline sequence ID for Dev snapshots
- Compress build output to a **versioned ZIP** before upload: `{SolutionName}_{version}.zip`
- Upload to a private artifact registry (e.g. Artifactory/JFrog)
- Never commit build artifacts to source control

## 4. Deployment Strategy
- Download versioned artifact at deploy time — **decouple build and deploy stages**
- Use `az functionapp deployment source config-zip` for atomic deployments
- Apply App Settings with `az functionapp config appsettings set` using environment-specific JSON
- Support `configDeploy` flag to update settings without a code change
- Restart Function App after settings changes; verify health endpoint responds

## 5. Environment Parity and Configuration
- Maintain `config-{env}.json` per environment with App Settings and Key Vault references
- Maintain per-environment shell scripts for infrastructure identifiers (subscription, resource group, function app name)
- Environments: DEV, SIT, UAT, PPD, PROD (minimum)
- Sensitive values in Key Vault; reference via `@Microsoft.KeyVault(SecretUri=...)`

## 6. Infrastructure Authentication in Pipelines
- Use a dedicated **SPN per environment** passed as pipeline variables
- Never hard-code credentials in YAML or scripts
- Rotate SPNs per organisational policy

## 7. Environment Configuration File Format

```json
[
  { "name": "EMP__ApimOutboundBaseUrl", "value": "@Microsoft.KeyVault(SecretUri=...)", "slotSetting": false },
  { "name": "EMP__ApimSubscriptionKey",  "value": "@Microsoft.KeyVault(SecretUri=...)", "slotSetting": false }
]
```
