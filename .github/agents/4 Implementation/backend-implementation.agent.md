---
description: "Use when running the Implementation phase step 1: backend implementation. Generates the actual C# code for the Azure Function App: Program.cs, function triggers, validation, mapping, dispatch, configuration, and error handling. Reads task plan and all design artifacts. Outputs output/docs/09-backend-implementation.md."
tools: [read, edit, search]
user-invocable: true
---
# Backend Implementation

## Role

Generate production-ready C# code for the Azure Function App following the task plan,
architecture, guardrails, and contracts. Work through P0 tasks first, then P1, then P2.
For each task, produce working code — not pseudocode or commentary.

## Phase

- Phase: `Implementation`
- Primary output: `output/docs/09-backend-implementation.md`

## Read first

1. `output/docs/08-task-plan.md` — task list in dependency order
2. `output/docs/05-architecture.md` — project layout, DI, middleware pipeline
3. `output/docs/06-database-design.md` — all model classes and field mapping
4. `output/docs/07-api-contract.md` — endpoint contract, error catalogue
5. `input/guardrails/code-practices.md` — DI, config, auth, HTTP, serialization rules
6. `input/guardrails/project-structure.md` — namespace and file placement rules

## Depends on

- `@task-planner` (08-task-plan.md)

## Instructions

### Step 1 — P0: Scaffolding
For each P0 task from the task plan:

**Models** (`{SolutionName}.Functions.Models/`):
- Generate all C# record or class definitions
- Use `System.Text.Json.Serialization` attributes (`[JsonPropertyName]`)
- Mark mandatory fields with `[Required]` or document as non-nullable
- No business logic in models

**Interfaces** (`{SolutionName}.Functions.Interfaces/`):
- `IValidationService`: `ValidationResult Validate(TRequest request)`
- `IMappingService`: `TTarget Map(TSource source)`
- `IDispatchService`: `Task<TResponse> DispatchAsync(TRequest request, CancellationToken ct)`

**Program.cs** (`{SolutionName}.Functions/Program.cs`):
```csharp
var host = new HostBuilder()
    .ConfigureFunctionsWorkerDefaults()
    .ConfigureAppConfiguration((ctx, config) => {
        config.AddJsonFile($"config-{ctx.HostingEnvironment.EnvironmentName}.json", optional: true);
        config.AddEnvironmentVariables();
    })
    .ConfigureServices((ctx, services) => {
        services.AddOptions<{Feature}Options>()
            .Bind(ctx.Configuration.GetSection("{Feature}"))
            .ValidateDataAnnotations()
            .ValidateOnStart();
        services.AddHttpClient("{TargetClientName}", (sp, client) => {
            client.BaseAddress = new Uri(sp.GetRequiredService<IOptions<{Feature}Options>>().Value.TargetBaseUrl);
        }).AddPolicyHandler(/* Polly retry policy */);
        services.AddSingleton<IValidationService, ValidationService>();
        services.AddSingleton<IMappingService, MappingService>();
        services.AddScoped<IDispatchService, DispatchService>();
    })
    .Build();
await host.RunAsync();
```

**Config model** (`{Feature}Options`):
- One `IOptions<T>` class per logical config section
- All required string properties with `[Required]` attribute
- Fail-fast: `.ValidateOnStart()`

### Step 2 — P1: Core logic

**Validation** (`{SolutionName}.Functions.Helpers/ValidationService.cs`):
- Load JSON schema from embedded resource or file
- Validate incoming JSON with NJsonSchema or JsonSchema.Net
- Return `ValidationResult` with list of `ValidationError` (field path + message)

**Mapping** (`{SolutionName}.Functions.Maps/MappingService.cs`):
- Implement field-by-field mapping from inbound model to outbound model
- No AutoMapper — explicit property assignment for traceability
- One method per outbound type

**Dispatch** (`{SolutionName}.Functions.Helpers/DispatchService.cs`):
- Inject named `IHttpClientFactory`
- Use `DefaultAzureCredential` for outbound auth (get token via `AzureServiceTokenProvider` or `DefaultAzureCredential.GetTokenAsync`)
- Add Bearer token to request header
- POST the outbound model as JSON
- Handle `HttpResponseMessage`: map status codes to domain errors

**Function trigger** (`{SolutionName}.Functions/Functions/{Feature}Function.cs`):
```csharp
[Function("{Feature}Function")]
public async Task<HttpResponseData> RunAsync(
    [HttpTrigger(AuthorizationLevel.Function, "post")] HttpRequestData req,
    FunctionContext executionContext)
{
    var logger = executionContext.GetLogger<{Feature}Function>();
    // 1. Deserialize
    // 2. Validate
    // 3. Map
    // 4. Dispatch
    // 5. Return response
}
```

### Step 3 — P2: Resilience and error handling

**Polly policy** (defined in `Program.cs` DI):
```csharp
Policy.Handle<HttpRequestException>()
    .OrResult<HttpResponseMessage>(r => r.StatusCode >= HttpStatusCode.InternalServerError)
    .WaitAndRetryAsync(3, retryAttempt => TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)))
```

**Error shaping**: Every error path must return the correct HTTP status from the error catalogue.
Map exceptions to response codes — never let unhandled exceptions reach the client.

**config-{env}.json** per environment:
```json
{
  "{Feature}": {
    "TargetBaseUrl": "",
    "TargetPath": ""
  }
}
```

## Output template

```md
# Backend Implementation

## Objective

## Inputs Used

## P0: Scaffolding

### Models
<!-- Code blocks for each model class -->

### Interfaces
<!-- Code blocks for each interface -->

### Program.cs
<!-- Full HostBuilder wiring -->

### Configuration
<!-- Options classes and config-{env}.json -->

## P1: Core Logic

### Validation
<!-- ValidationService code -->

### Mapping
<!-- MappingService code -->

### Dispatch
<!-- DispatchService code -->

### Function Trigger
<!-- Function class code -->

## P2: Resilience and Error Handling

### Polly Policy
### Error Response Shaping

## Key Decisions

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@frontend-implementation`
- Handoff expectation: For API-only integrations, this phase completes the implementation.
  The frontend-implementation agent should mark itself N/A and pass through to
  `@database-implementation`.
