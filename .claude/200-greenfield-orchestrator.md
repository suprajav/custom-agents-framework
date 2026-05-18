# 200 Greenfield Orchestrator

## Purpose

Coordinate the full greenfield pipeline shown in `diagram.md` from `input/` through `output/docs/`.

## Inputs

- `input/Automate Insurance Quote Extraction Process_PDD.md`
- `input/User Stories List.md`
- `input/technical-mandates.md`
- `input/coding-best-practices.md`
- `input/compliance-requirements.md`
- `input/branding-guidelines.md`
- `input/README.md`
- `.claude/commands/swagger-pipeline.md`

## Output location

- Primary destination: `output/docs/`

## Execution model

1. Confirm the required input files exist.
2. Run each phase in order.
3. Ensure each agent reads the previous phase outputs before making new decisions.
4. Keep artifacts lightweight but traceable.
5. Track state using `.claude/runtime/project-state.yaml` when running the pipeline.
6. Use the contract files under `.claude/contracts/` to keep phase handoffs consistent.
7. Finish by producing a consolidated report and documentation pack.

## Phase order

### 1 Requirement
- `201-pdd-parser.md` -> `output/docs/01-pdd-summary.md`
- `202-user-stories-processor.md` -> `output/docs/02-user-stories-summary.md`
- `203-requirements-consolidator.md` -> `output/docs/03-requirements-consolidated.md`

### 2 Design
- `204-tech-stack-configurator.md` -> `output/docs/04-tech-stack.md`
- `205-architecture-designer.md` -> `output/docs/05-architecture.md`
- `206-database-designer.md` -> `output/docs/06-database-design.md`
- `207-api-contract-designer.md` -> `output/docs/07-api-contract.md`

### 3 Planner
- `208-task-planner.md` -> `output/docs/08-task-plan.md`

### 4 Implementation
- `209-backend-implementation.md` -> `output/docs/09-backend-implementation.md`
- `210-frontend-implementation.md` -> `output/docs/10-frontend-implementation.md`
- `211-database-implementation.md` -> `output/docs/11-database-implementation.md`
- `214-component-library-builder.md` -> `output/docs/12-component-library.md`

### 5 Testing
- `212-test-suite-generator.md` -> `output/docs/13-test-suite.md`
- `216-frontend-test-generator.md` -> `output/docs/14-frontend-tests.md`
- `218-accessibility-validator.md` -> `output/docs/15-accessibility-report.md`
- `219-test-data-generator.md` -> `output/docs/16-test-data.md`

### 6 Quality
- `220-code-best-practices-enforcer.md` -> `output/docs/17-code-best-practices-report.md`
- `221-design-compliance-validator.md` -> `output/docs/18-design-compliance-report.md`
- `222-branding-compliance-checker.md` -> `output/docs/19-branding-compliance-report.md`

### 7 Compliance
- `217-compliance-checker.md` -> `output/docs/20-compliance-report.md`

### 8 Coverage Analyzer
- `213-code-coverage-analyzer.md` -> `output/docs/21-code-coverage-report.md`
- `214-security-scanner.md` -> `output/docs/22-security-scan-report.md`
- `215-memory-leak-detector.md` -> `output/docs/23-memory-leak-report.md`
- `216-performance-analyzer.md` -> `output/docs/24-performance-report.md`

### 9 Deployment
- `225-deployment-strategy-designer.md` -> `output/docs/25a-deployment-strategy.md`
- `226-infrastructure-config-generator.md` -> `output/docs/25b-infrastructure-config.md`
- `227-release-readiness-checker.md` -> `output/docs/25c-release-readiness.md`
- `228-monitoring-observability-planner.md` -> `output/docs/25d-monitoring-observability.md`

### 10 Consolidated Report
- `221-report-consolidator.md` -> `output/docs/25-consolidated-report.md`

### 11 Documentation
- `218-deployment-config-generator.md` -> `output/docs/26-deployment-config.md`
- `220-documentation-generator.md` -> `output/docs/27-documentation-index.md`


## Minimum orchestration rules

- Do not skip Requirement, Design, Planner, Implementation, Testing, Quality, Compliance, Coverage Analyzer, Consolidated Report, or Documentation.
- Use the runtime state file and scripts to keep track of progress.
- Store every deliverable as a Markdown artifact under `output/docs/`.
- Preserve unresolved items in `Open Questions` sections instead of hiding them.

## Success criteria

The pipeline is considered complete when the following exist in `output/docs/`:

- consolidated requirements
- design artifacts
- task plan
- implementation summaries
- testing and quality reports
- compliance and coverage reports
- consolidated report
- deployment config outline
- documentation index
