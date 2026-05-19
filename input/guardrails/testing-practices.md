# Guardrail: Testing Practices

## Scope
Applies to all Azure Function App test projects. Covers structure, coverage strategy,
mocking, assertions, test data, and project configuration.

---

## 1. Test Project Structure
- Maintain a dedicated test project mirroring production namespaces
- One test class per production class (1:1 mapping)
- Place test helpers under `Helpers/` (e.g. `UnitTestHelper.cs`, `HttpRequestDataHelper.cs`)
- Use `GlobalUsings.cs` for project-wide `using` directives (e.g. `global using Xunit`)

## 2. Coverage Strategy
- **Overall minimum**: 80% line coverage
- **Critical path minimum**: 95% for: HTTP Trigger, Mapper, HTTP Client Helper, Schema Validator
- Cover all layers: Function trigger, mapper, HTTP helper, schema validator, error helper
- Cover **all** exception paths: 400, 401, 500, schema failure, null deserialisation, empty response
- Cover boundary cases in mappers: null collections, missing fields, partial data, empty arrays

## 3. Mocking and Isolation
- Use **Moq** for all interface mocks
- Mock interfaces, not concrete classes: `IHttpClientHelper`, `IMapper`, `ISchemaValidationHelper`, `ILogger<T>`, `TokenCredential`
- Use `Moq.Protected()` to mock `HttpMessageHandler.SendAsync` for `HttpClient` tests
- Centralise mock setup in `UnitTestHelper` helper factories
- Provide `LoggerMock<T>` to assert on logged messages and levels

## 4. Assertions
- Use **FluentAssertions** for all assertions: `response.StatusCode.Should().Be(HttpStatusCode.OK)`
- Assert on:
  - Response status codes
  - Response body content (deserialized)
  - Outbound HTTP headers (Bearer token, subscription key, correlation ID)
  - Log entries (message, level, correlation ID)

## 5. Test Data Management
- Store representative JSON payloads under `Tests/TestData/{FunctionName}/`
- Required fixtures per feature:
  - `Valid{Entity}Request.json` — happy path with all fields
  - `Invalid{Entity}Request_MissingMandatoryFields.json` — missing required fields
  - `Invalid{Entity}Request_MalformedJson.json` — unparseable JSON
  - `Invalid{Entity}Request_{EdgeCase}.json` — one per significant edge case
  - `Valid{Target}Response.json` — downstream success response
- Copy production JSON schemas into test project `Schemas/` with `CopyToOutputDirectory: PreserveNewest`
- Use realistic domain data in fixtures — not placeholder values

## 6. Test Project Configuration
- Mark csproj with `<IsTestProject>true</IsTestProject>`
- Enable nullable reference types: `<Nullable>enable</Nullable>`
- Include `coverlet.collector` and enforce coverage thresholds in CI
- Use `<Using Include="Xunit" />` in csproj to reduce per-file using statements
- Required packages: `xunit`, `Moq`, `FluentAssertions`, `coverlet.collector`, `Microsoft.NET.Test.Sdk`
