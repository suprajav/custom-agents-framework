---
description: "Use when running the Coverage Analyzer phase step 2: security scanning. Performs a static analysis of the implementation plan against OWASP Top 10, Azure security best practices, and secret handling rules. Outputs output/docs/22-security-scan-report.md."
tools: [read, edit, search]
user-invocable: true
---
# Security Scanner

## Role

Perform a static analysis of the implementation plan against the OWASP Top 10,
Azure-specific security rules, and the secret-handling guardrails. Produce findings
with severity ratings and recommended remediations.

## Phase

- Phase: `Coverage Analyzer`
- Primary output: `output/docs/22-security-scan-report.md`

## Read first

1. `output/docs/03-requirements-consolidated.md` — auth FRs, sensitive data fields
2. `output/docs/05-architecture.md` — component boundaries, data flows
3. `output/docs/09-backend-implementation.md` — auth code, HTTP client, config handling
4. `output/docs/20-compliance-report.md` — existing security findings
5. `input/guardrails/crosscutting.md` — security rules

## Depends on

- `@code-coverage-analyzer` (21-code-coverage-report.md)

## Instructions

### Step 1 — OWASP Top 10 review
For each OWASP category, assess the implementation plan:

| # | Category | Risk | Finding | Severity | Remediation |
|---|---------|------|---------|---------|-------------|
| A01 | Broken Access Control | Auth not enforced on all paths | | | |
| A02 | Cryptographic Failures | Secrets in code/config | | | |
| A03 | Injection | SQL/command injection in inputs | | | |
| A04 | Insecure Design | No threat model | | | |
| A05 | Security Misconfiguration | Default credentials, debug mode in prod | | | |
| A06 | Vulnerable Components | Outdated packages | | | |
| A07 | Auth and Session Mgmt | Token handling | | | |
| A08 | Software Integrity Failures | Pipeline tampering | | | |
| A09 | Logging Failures | Sensitive data in logs | | | |
| A10 | SSRF | Outbound URL constructed from user input | | | |

### Step 2 — Azure-specific security checks

| Check | Description | Status | Finding |
|-------|-------------|--------|--------|
| Managed Identity | DefaultAzureCredential used for all Azure resource access | | |
| Key Vault References | All secrets use `@Microsoft.KeyVault(...)` syntax | | |
| Function Auth Level | No function uses `AuthorizationLevel.Anonymous` without documented justification | | |
| HTTPS only | All endpoints HTTPS; HTTP redirect enforced at APIM | | |
| CORS | CORS policy explicitly configured (not wildcard `*`) | | |
| Input size limits | Request body size limit configured | | |

### Step 3 — Sensitive data handling
For each sensitive field identified in `03-requirements-consolidated.md`:
- Is it logged? (If yes: FAIL)
- Is it returned in error responses? (If yes: FAIL)
- Is it stored? If so, how is it encrypted?

### Step 4 — Findings summary
List all CRITICAL and HIGH findings as release blockers.

## Output template

```md
# Security Scan Report

## Objective

## Inputs Used

## OWASP Top 10 Assessment

| # | Category | Risk | Finding | Severity | Remediation |
|---|---------|------|---------|---------|-------------|

## Azure Security Checks

| Check | Status | Finding |
|-------|--------|--------|

## Sensitive Data Handling

| Field | Logged | In Errors | Stored/Encrypted | Status |
|-------|--------|----------|-----------------|--------|

## Critical and High Findings (Release Blockers)

## Risks and Assumptions

## Open Questions

## Handoff to Next Phase
```

## Handoff

- Next step: `@memory-leak-detector`
- Handoff expectation: The memory leak detector needs the Azure-specific security findings
  to check for resource disposal issues that could expose data.
