# Guardrail: Project Structure

## Scope
Defines the internal layout of any generated Azure Integration project.
This guardrail MUST be applied when scaffolding or modifying any project in this pipeline.

---

## Solution Layout

```
{SolutionName}/
├── {SolutionName}.sln
├── NuGet.Config                        ← Internal registry first, public fallback
├── .gitignore
├── Directory.Build.props               ← Shared MSBuild properties
├── Directory.Build.targets
│
├── Functions/                          ← Main Function App project
│   └── {SolutionName}.Functions.csproj
│
├── {SolutionName}.Tests/               ← Unit test project
│   └── {SolutionName}.Tests.csproj
│
├── harness/                            ← CI/CD pipeline and deployment
│   ├── .harness/
│   └── deploy/
│
└── docs/                               ← Architecture and guardrail docs
```

**Rules:**
- Top-level folders MUST be exactly: `Functions`, `{Name}.Tests`, `harness`, `docs`
- No business logic outside these folders
- Solution name follows: `{Org}.{Domain}.{System}.{Component}` e.g. `AXAXL.Integration.UWB.EMP`

---

## Functions Project — Internal Layout

```
Functions/
├── {SolutionName}.Functions.csproj     ← net8.0, AzureFunctionsVersion v4, OutputType=Exe
├── Program.cs                          ← ONLY place for HostBuilder / DI wiring
├── host.json
├── local.settings.example.json         ← Template (commit this, NOT local.settings.json)
│
├── Functions/                          ← One file per HTTP Trigger
│   └── {Feature}Processor.cs
│
├── Interfaces/                         ← One interface per helper/service
│   ├── I{Feature}HttpClientHelper.cs
│   ├── ICdmTo{Target}Mapper.cs
│   └── ISchemaValidationHelper.cs
│
├── Maps/                               ← Transformation logic only
│   └── CdmTo{Target}Mapper.cs
│
├── Helpers/                            ← Infrastructure / utility classes
│   ├── {Feature}HttpClientHelper.cs
│   ├── ErrorResponseHelper.cs
│   └── SchemaValidationHelper.cs
│
├── Authorization/                      ← Auth constants only — no logic
│   ├── AppRoles.cs
│   └── Scopes.cs
│
├── Models/
│   ├── CDM/                            ← Inbound canonical model
│   └── {Target}/                       ← Outbound target system model
│
└── Schemas/
    └── {Entity}_CDM_{version}.json     ← Versioned JSON Schema files
```

---

## Tests Project — Internal Layout

```
{SolutionName}.Tests/
├── GlobalUsings.cs
├── {Feature}ProcessorTests.cs
├── CdmTo{Target}MapperTests.cs
├── {Feature}HttpClientHelperTests.cs
├── SchemaValidationHelperTests.cs
├── ErrorResponseHelperTests.cs
│
├── Helpers/
│   ├── UnitTestHelper.cs               ← Shared mock factories
│   └── HttpRequestDataHelper.cs
│
├── Schemas/                            ← Copy of production schemas
│
└── TestData/
    └── {Feature}/                      ← JSON fixtures per scenario
```
