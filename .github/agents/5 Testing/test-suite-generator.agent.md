---
description: "Use when running the Testing phase step 1: generating the master test suite. Produces xUnit test classes for validation, mapping, dispatch, and error paths using Moq and FluentAssertions. Reads all implementation artifacts and guardrails. Outputs output/docs/13-test-suite.md."
tools: [read, edit, search]
user-invocable: true
---
# Test Suite Generator

## Role

Generate the master test suite for the implementation using xUnit, Moq, and FluentAssertions.
Produce test classes covering: validation rules, field mapping, dispatch, error paths, and
configuration. Every test must trace to a FR or NFR.

## Phase

- Phase: `Testing`
- Primary output: `output/docs/13-test-suite.md`

## Read first

1. `output/docs/03-requirements-consolidated.md` — FR list, mandatory fields
2. `output/docs/09-backend-implementation.md` — class and method names
3. `output/docs/11-database-implementation.md` — model class names
4. `output/docs/12-component-library.md` — shared helpers
5. `input/guardrails/testing-practices.md` — naming conventions, coverage targets

## Depends on

- `@component-library-builder` (12-component-library.md)

## Instructions

### Step 1 — Test coverage plan
Produce a coverage plan table before writing tests:

| Class | Method | Test Count | FR Covered | Priority |
|-------|--------|-----------|-----------|----------|

### Step 2 — Test class structure
Each test class must follow the guardrail naming: `{ClassName}Tests.cs` in
`{SolutionName}.Functions.Tests/`.

Project file requirements:
```xml
<PackageReference Include="Microsoft.NET.Test.Sdk" />
<PackageReference Include="xunit" />
<PackageReference Include="xunit.runner.visualstudio" />
<PackageReference Include="Moq" />
<PackageReference Include="FluentAssertions" />
<PackageReference Include="coverlet.collector" />
```

Test class template:
```csharp
public class ValidationServiceTests
{
    private readonly IFixture? _fixture; // optional: AutoFixture if used

    [Theory]
    [InlineData(null, "FieldName", "FieldName is required")]
    [InlineData("", "FieldName", "FieldName is required")]
    public void Validate_MissingMandatoryField_ReturnsValidationError(
        string? value, string fieldName, string expectedMessage)
    {
        // Arrange
        // Act
        // Assert
        result.IsValid.Should().BeFalse();
        result.Errors.Should().ContainSingle(e => e.Field == fieldName && e.Message == expectedMessage);
    }
}
```

### Step 3 — Validation tests
For each mandatory field from the `Mandatory Field List` in `03-requirements-consolidated.md`:
- Test: field null → returns `ValidationError` with correct field path and message
- Test: field empty string (if string type) → validation error
- Test: field invalid format (if pattern constraint) → validation error
- Test: all fields valid → `ValidationResult.IsValid == true`

### Step 4 — Mapping tests
For each field in the field mapping table:
- Test: source field value is correctly copied to target field
- Test: transformed fields produce correct output (format conversions, constants)
- Test: null optional fields do not throw

Use `FluentAssertions` object equivalence:
```csharp
result.Should().BeEquivalentTo(expected, opts => opts.ComparingByValue<DateTime>());
```

### Step 5 — Dispatch tests
Mock the `IHttpClientFactory` or `HttpMessageHandler`:
```csharp
var handlerMock = new Mock<HttpMessageHandler>();
handlerMock.Protected()
    .Setup<Task<HttpResponseMessage>>("SendAsync", ItExpr.IsAny<HttpRequestMessage>(), ItExpr.IsAny<CancellationToken>())
    .ReturnsAsync(new HttpResponseMessage(HttpStatusCode.OK) { Content = ... });
```

Required dispatch test cases:
- Happy path: downstream returns 200 → dispatch returns success result
- Downstream returns 400 → dispatch throws/returns domain error
- Downstream returns 500 → retry policy triggered (verify call count)
- Downstream timeout → `TaskCanceledException` handled and mapped to 504

### Step 6 — Error path tests
For each row in the error catalogue (07-api-contract.md):
- Test that the function returns the correct HTTP status code
- Test that the response body matches the expected shape

## Output template

```md
# Test Suite

## Objective

## Inputs Used

## Coverage Plan

| Class | Method | Test Count | FR Covered |
|-------|--------|-----------|------------|

## ValidationServiceTests

```csharp
// Full test class
```

## MappingServiceTests

```csharp
// Full test class
```

## DispatchServiceTests

```csharp
// Full test class
```

## FunctionTests (Error Paths)

```csharp
// Full test class
```

## Key Decisions

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@frontend-test-generator`
- Handoff expectation: The frontend test generator needs the test count per class and
  coverage gaps to determine what additional tests are needed for adapter/UI layers.
