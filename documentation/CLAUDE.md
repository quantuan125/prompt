# Claude Configuration Management

## System Overview

Claude operates as an LLM Agent in a semi-automated development workflow with human oversight. This document orchestrates role activation and ensures proper data flow.

## Workflow Process

```
Human → Consultant → Human → Planner → Human → Developer → Human → Reviewer → Human
```

## Available Roles & Activation

### 🎯 Quick Activation Commands
- `/consult` - Activate Consultant role for architectural analysis
- `/plan` - Activate Planner role for development planning
- `/develop` - Activate Developer role for implementation
- `/review` - Activate Reviewer role for quality assurance

### 📋 Role Descriptions

#### Consultant (Analysis Mode)
**Purpose**: Analyze problems and propose architectural solutions  
**Activation**: `/consult` or tasks mentioning "analyze", "recommend", "architecture"  
**Configuration**: `@prompt/consultant/consultant_system.md`  
**Auto-inputs**: Component docs, project context  
**Output**: `@prompt/artifacts/consultations/[component]/consultation_v[X.Y.Z].md`

#### Planner (Planning Mode)
**Purpose**: Transform consultations into executable development plans  
**Activation**: `/plan` or tasks mentioning "plan", "design", "structure"  
**Configuration**: `@prompt/planner/planner_system.md`  
**Auto-inputs**: Latest consultation, templates  
**Output**: `@prompt/artifacts/plans/[component]/plan_v[X.Y.Z].md`

#### Developer (Implementation Mode)
**Purpose**: Implement plans with production-ready code  
**Activation**: `/develop` or tasks mentioning "implement", "code", "build"  
**Configuration**: `@prompt/developer/developer_system.md`  
**Auto-inputs**: Latest plan, source code  
**Output**: `@prompt/artifacts/developments/[component]/devnotes_v[X.Y.Z].md`

#### Reviewer (Review Mode)
**Purpose**: Ensure quality and compliance  
**Activation**: `/review` or tasks mentioning "review", "check", "validate"  
**Configuration**: `@prompt/reviewer/reviewer_system.md`  
**Auto-inputs**: Plan, dev notes, code changes  
**Output**: `@prompt/artifacts/reviews/[component]/review_v[X.Y.Z].md`

## Automatic Context Loading

When activated, each role automatically:

1. **Loads role configuration** from system prompts
2. **Reads workflow state** from `@prompt/config/workflow_state.json`
3. **Fetches latest inputs** based on `@prompt/config/orchestration.json`
4. **Applies project context** from `@prompt/config/project_context.json`

## Human Instruction Format

Provide clear instructions with:
- **Component name**: "for the tv_ingest component"
- **Task context**: "implement the caching feature"
- **Special requirements**: "ensure backward compatibility" (optional)

### Example Instructions

**To Consultant**:
```
/consult
Please analyze the performance issues in the tv_ingest component and 
recommend caching strategies.
```

**To Planner**:
```
/plan
Create a development plan for the tv_ingest component based on the latest 
consultation. Focus on incremental implementation.
```

**To Developer**:
```
/develop
Implement the caching feature for tv_ingest following plan v2.5.2. 
Ensure all tests pass.
```

**To Reviewer**:
```
/review
Review the tv_ingest implementation against the plan and verify all 
requirements are met.
```

## State Management

Claude automatically:
- Updates `workflow_state.json` after completing tasks
- Increments version numbers based on change type
- Archives old versions when creating new major versions

## Error Handling

If Claude cannot find required inputs:
1. Checks `@prompt/config/workflow_state.json` for last known state
2. Prompts human for clarification
3. Suggests next appropriate action

## Configuration References

- **System Documentation**: `@prompt/documentation/unified_system_documentation.md`
- **Shared Definitions**: `@prompt/config/shared_definitions.json`
- **Project Context**: `@prompt/config/project_context.json`
- **Orchestration Rules**: `@prompt/config/orchestration.json`
- **Current State**: `@prompt/config/workflow_state.json`

---

*Use the appropriate slash command or natural language to activate the desired role. Claude will handle the rest automatically.*