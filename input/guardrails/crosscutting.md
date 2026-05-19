# Guardrail: Cross-cutting and General Practices

## Scope
Cross-cutting concerns that apply to all phases: shared libraries, runtime targets,
source control, naming, AI-SDLC guardrails, and NuGet configuration.

---

## 1. Shared Library Usage
- Prefer **internal NuGet packages** for cross-cutting concerns: auth, retry, serialization, exceptions
- Pin shared package versions explicitly in csproj — no floating versions (`*`)
- Search internal registry first before using public NuGet.org packages
- Document any gap where no internal equivalent exists
- `NuGet.Config` MUST be committed at solution root and MUST NOT contain credentials

**NuGet.Config pattern:**
```xml
<configuration>
  <packageSources>
    <add key="Internal" value="{internal-registry-url}" />
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
  </packageSources>
</configuration>
```

## 2. .NET and Azure Functions Runtime
- Target `net8.0` and Azure Functions **v4 isolated worker model**
- Enable nullable reference types: `<Nullable>enable</Nullable>`
- Enable implicit usings: `<ImplicitUsings>enable</ImplicitUsings>`
- `OutputType` must be `Exe` for isolated worker model

## 3. Source Control and Branching
- `.gitignore` must exclude: `local.settings.json`, `bin/`, `obj/`, `.vs/`, `TestResults/`
- Commit `local.settings.example.json` as a template — never the actual secrets file
- Feature branches follow: `{issue-id}-{short-description}` (e.g. `001-emp-exposure-processor`)

## 4. AI SDLC Guardrails
The following rules apply to all AI-generated code in this project:
- Validate generated JSON payloads against versioned schemas before dispatch
- Never emit secrets or credentials in generated code
- Every new function or helper MUST have corresponding unit tests (happy + exception paths)
- All outbound HTTP calls MUST go through the central helper with retry, token, and logging
- Use structured logging with a correlation ID in every log statement
- Introduce all helpers and services behind interfaces
- Keep environment-specific config in `config-{env}.json` and Key Vault references
- Tests MUST run as a mandatory gate in CI
- Version artifacts and store in a private registry before deployment
- Version schema files in filenames; keep in sync with contract changes

## 5. Naming Conventions
- Solution: `{Org}.{Domain}.{System}.{Component}`
- Projects: `{SolutionName}.Functions`, `{SolutionName}.Tests`
- Classes: PascalCase; Interfaces prefix `I`
- App Settings: `{Feature}__{SettingName}` (double underscore for nested config)
- Routes: lowercase kebab-case with version prefix `/v{n}/{resource}`
