# LLM Development System: Principles & Guidelines

## 1. Core Principles

### 1.1 Single Responsibility Principle
Each role has ONE primary function:
- **Consultant**: Explore and recommend solutions
- **Planner**: Transform ideas into executable steps
- **Developer**: Implement plans precisely
- **Reviewer**: Ensure quality and compliance

### 1.2 Structured Communication
All inter-role communication uses standardized templates:
- Templates enforce completeness
- Versions enable traceability
- Structured data enables automation

### 1.3 Fail-Safe Design
The system assumes things will go wrong:
- Every role has a blocker protocol
- Escalation paths are predefined
- Recovery procedures are documented

### 1.4 Continuous Improvement
The system learns from its execution:
- Reviews generate improvement items
- Patterns trigger template updates
- Metrics drive optimization

## 2. Template Design Guidelines

### 2.1 Template Structure
Every template MUST contain:

```markdown
# [Role] [Artifact Type]: [Component Name]

## Metadata Block
- **Version:** [Semantic version]
- **Author:** [Role designation]
- **Date:** [ISO 8601]
- **Status:** [Predefined status]
- **Dependencies:** [Related artifacts]

## Executive Summary
[Plain language summary for all stakeholders]

## Core Content
[Role-specific sections]

## Validation Checklist
- [ ] [Self-check items]

## Next Steps
[Clear handoff to next role]
```

### 2.2 Section Guidelines

#### Metadata Block
- Use semantic versioning: `major.minor.patch`
- Reference related artifacts by exact version
- Status from predefined enum (see Section 3.2)

#### Executive Summary
- Maximum 3 paragraphs
- No technical jargon
- Focus on "what" and "why"

#### Core Content
- Use subsections for organization
- Balance detail with readability
- Include examples where helpful

#### Validation Checklist
- 5-10 items maximum
- Each item must be verifiable
- Include both content and process checks

#### Next Steps
- Explicitly name the next role
- Provide specific actions
- Include any prerequisites

### 2.3 Formatting Standards
- **Headers**: ATX-style (`#`), max depth of 4
- **Lists**: Bullets for unordered, numbers for sequences
- **Code**: Triple backticks with language identifier
- **Emphasis**: Bold for key terms, italic for examples

## 3. System Prompt Design

### 3.1 Prompt Architecture

Every system prompt follows this structure:

```markdown
# Role
[One sentence role definition]

## Core Mandate: [Memorable Title]
[2-3 sentences on primary responsibility and source of truth]

## Input Locations
[Instructions to automatically fetch relevant artifacts based on roles]

## Competencies
[Bulleted list of 4-6 key skills/knowledge areas]

## Communication Guidelines


## Execution Protocol
[Numbered steps for standard workflow]

## Collaboration Points
[How this role interacts with others]

## Deliverables
- **Primary**: [Main output with template reference]
- **Secondary**: [Supporting outputs]

## Quality Standards
[Specific, measurable criteria for success]

## Escalation Protocol
[When and how to raise issues]
```

### 3.2 Shared Definitions

All prompts reference these shared definitions:

```json
{
  "statuses": [
    "draft",
    "ready_for_review",
    "in_progress",
    "completed",
    "blocked",
    "rejected"
  ],
  "verdicts": [
    "approved",
    "conditional_approval",
    "rejected",
    "needs_clarification"
  ],
  "file_paths": {
    "consultant": "artifacts/consultations/{component}/consultation_v{version}.md",
    "planner": "artifacts/plans/{component}/plan_v{version}.md",
    "developer": "artifacts/developments/{component}/development_v{version}.md",
    "reviewer": "artifacts/reviews/{component}/review_v{version}.md"
  }
}
```

### 3.3 Context Injection

Prompts are assembled dynamically:

```python
# Pseudo-code for prompt assembly
final_prompt = base_prompt + shared_context + task_context

# Where:
# - base_prompt = role-specific instructions
# - shared_context = project standards, conventions
# - task_context = specific component, version, dependencies
```

## 4. Workflow Automation

### 4.1 File Management
- All paths follow the patterns in `shared_definitions.json`
- Versions auto-increment based on change type
- Previous versions archived, not overwritten

### 4.2 State Tracking
```json
{
  "component_name": {
    "current_phase": "planning",
    "current_version": "2.5.1",
    "assigned_to": "planner",
    "blocked": false,
    "history": [
      {
        "phase": "consultation",
        "version": "2.5.0",
        "completed": "2024-01-07T10:00:00Z",
        "verdict": "approved"
      }
    ]
  }
}
```

### 4.3 Dependency Management
- Explicit dependencies in metadata block
- Automated conflict detection
- Parallel execution where possible

## 5. Quality Assurance

### 5.1 Template Validation
Before acceptance, every template must:
- [ ] Follow the standard structure
- [ ] Include all required sections
- [ ] Use consistent formatting
- [ ] Pass automated linting

### 5.2 Prompt Testing
New prompts must be tested with:
- Typical use cases (happy path)
- Edge cases (boundary conditions)
- Error cases (invalid inputs)
- Integration scenarios (handoffs)

### 5.3 Continuous Monitoring
Track these metrics:
- Blocker frequency by role
- Revision cycles per component
- Time per phase
- Verdict distribution

## 6. Maintenance Guidelines

### 6.1 Template Evolution
- Changes require approval from 2+ roles
- Backward compatibility for 2 versions
- Migration guide for breaking changes

### 6.2 Prompt Updates
- Test changes in sandbox first
- Roll out gradually (10%, 50%, 100%)
- Monitor metrics for regression

### 6.3 Documentation
- Keep examples current
- Update guidelines with learnings
- Version control all changes

## 7. Implementation Checklist

When creating or modifying system components:

- [ ] Template follows standard structure
- [ ] System prompt includes all required sections
- [ ] File paths match conventions
- [ ] Dependencies explicitly declared
- [ ] Validation criteria are measurable
- [ ] Next steps are unambiguous
- [ ] Tested with real scenarios
- [ ] Documentation updated
- [ ] Metrics tracking enabled
- [ ] Team training completed