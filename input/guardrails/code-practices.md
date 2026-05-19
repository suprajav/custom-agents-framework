# Guardrail: Function App Code Practices

## Scope
Applies to all Azure Function App projects. Covers DI/startup, configuration, auth,
input validation, HTTP clients, logging, error handling, serialization, and models.

---

## 1. Dependency Injection and Startup
- Use `HostBuilder` with `ConfigureFunctionsWorkerDefaults` for all startup wiring
- Register expensive, stateless helpers as **singletons** (e.g. pre-parsed schema validator)
- Use `IHttpClientFactory` (`AddHttpClient`) — never instantiate `HttpClient` directly
- Register `TokenCredential` as a singleton to centralise auth
- `Program.cs` is the ONLY place for DI wiring — no service location elsewhere

## 2. Configuration and Secrets
- Read local settings from `local.settings.json`; production settings from environment variables
- Support both flat keys and `Values:` style keys via `IConfiguration`
- **Never** hard-code secrets — use environment variables backed by Azure Key Vault references
  - Pattern: `@Microsoft.KeyVault(SecretUri=https://vault.vault.azure.net/secrets/name/)`
- Use `DefaultAzureCredential` for managed identity; use `ClientSecretCredential` only in non-prod where explicitly required
- **Fail fast**: validate required App Settings at startup; throw `InvalidOperationException` for missing mandatory config

## 3. Authentication and Authorisation
- Apply auth middleware scoped to named functions using `UseWhen` — not global handlers
- Centralise role constants in a static `AppRoles` class; resolve values from App Settings (`%RoleName%`)
- Return HTTP 401 before any business processing if auth fails

## 4. Input Validation and Schema Enforcement
- Validate raw JSON payloads against a **versioned JSON Schema** before deserialisation
- Return HTTP 400 with field-level error messages on validation failure
- Parse and cache schemas at startup as singletons — never re-read from disk per request
- Schema files are versioned in their filename: `{Entity}_CDM_{version}.json`

## 5. HTTP Clients, Token Acquisition, and Retry
- Centralise all outbound HTTP logic in a dedicated helper (e.g. `{Feature}HttpClientHelper`)
- The helper is responsible for: token acquisition, header injection, retry policy, response mapping
- Use a shared retry policy wrapper (e.g. `TransientHttpFailureRetryPolicy`) with configurable max retries
- Read all backend URLs and keys from environment variables — never hardcode

## 6. Logging and Observability
- Use `ILogger<T>` in every class
- Include a request-scoped correlation ID in every log statement (use `requestIdentifier` or equivalent from inbound payload)
- Use structured logging message templates for queryable Application Insights telemetry
- Log entry and exit of every public method in integration-critical paths

## 7. Error Handling and HTTP Responses
- Use a central `ErrorResponseHelper` for all error responses: `{ code, message, timestamp }`
- Map exceptions to HTTP status codes:
  - Schema/argument/JSON errors → 400
  - Auth failures → 401
  - Unhandled exceptions → 500
- **Never** forward raw downstream error responses to callers

## 8. Serialization
- Use `System.Text.Json` with `PropertyNameCaseInsensitive = true`
- Configure once in DI, not per-request
- Always validate JSON against schema before deserialising

## 9. Domain Model Design
- Keep inbound (CDM) models strictly separate from outbound (Target) models — never share or cast between them
- Initialise collection properties to empty lists; use nullable types for optional fields
- Models are data containers only — no business logic in model classes

## 10. Naming and Routes
- Use explicit `[Function("Name")]` attributes on all triggers
- Include API version in all routes: `/v1/{resource}`
- Use `AuthorizationLevel.Anonymous` at the trigger and enforce auth via middleware
