# Consultant Notes: Prompt System Architecture Enhancement

## Metadata Block
- **Task ID:** T001
- **Task Type:** system_architecture
- **Target:** prompt_main
- **Artifact Type:** Consultation
- **Version:** 2.1.0
- **Author:** Senior Software Architecture Consultant
- **Date:** 2025-07-15
- **Status:** ready_for_review
- **Dependencies:** Task Object Model v2.0.0, workflow_state.json schema, state_manager.py
- **Consultation Type:** architecture

## Executive Summary

The LLM Agent System requires critical architectural improvements to address versioning ambiguity and standardization gaps that threaten system scalability and maintainability. Our analysis has identified three interconnected issues that demand immediate resolution: conflated artifact/component versioning, undocumented emergent standards, and inconsistent workflow artifact quality.

The recommended solution implements a **Task ID + Iteration Counter** approach that fundamentally decouples workflow artifact iterations from component semantic versioning, while establishing comprehensive global standards for all workflow artifacts. This approach provides perfect traceability, eliminates versioning confusion, and creates a robust foundation for automated workflow management.

### Key Recommendations
- **Primary Solution:** Task ID + Iteration Counter versioning with global artifact standards
- **Estimated Complexity:** High (requires schema changes, script updates, template revisions)
- **Risk Level:** Medium (migration complexity, learning curve)
- **Expected Outcome:** Complete versioning clarity, enhanced traceability, standardized workflow artifacts

---

## Problem Analysis

### Problem Statement
The current LLM Agent System suffers from three critical architectural flaws that prevent effective iteration, automation, and quality assurance: (1) versioning scheme conflates artifact iterations with component versions, (2) superior workflow standards exist but are not formally codified, and (3) workflow artifacts lack consistent structure and traceability.

### Current State Assessment
- **Existing Implementation:** Artifacts use semantic versioning (e.g., `plan.md`) that conflicts with component versions
- **Pain Points:** 
  - Cannot iterate on plans without version confusion
  - No standardized headers for workflow artifacts
  - Poor traceability between tasks and outputs
  - Inconsistent file manifests and planning quality
- **Constraints:** Must maintain backward compatibility during migration
- **Success Criteria:** Complete separation of artifact/component versioning, standardized artifact headers, enhanced workflow predictability

### Requirements Breakdown
**Functional Requirements:**
- Implement Task ID + Iteration Counter naming convention
- Enhance workflow_state.json schema with target_version and iterations tracking
- Update state_manager.py for automatic iteration handling
- Standardize all workflow artifact headers globally

**Non-Functional Requirements:**
- Performance: Minimal impact on workflow execution time
- Security: Maintain existing access controls and validation
- Scalability: Support unlimited iterations per task/phase

## Solution Exploration

### Approach 1: Metadata Fix (Clarify SemVer Usage)

**Overview**
Retain semantic versioning for artifacts but add metadata fields to explicitly distinguish artifact versions from target component versions.

**Technical Implementation**
```markdown
**Task ID:** task-001
**Artifact Type:** Plan
**Version:** 2.5.1  // This plan's version
**Target:** tv_ingest
**Target Version:** 2.6.0 // The component version this plan will create
```

**Component Mapping**
- Primary Changes: `prompt/templates/*/template_*.md` (header updates)
- Secondary Changes: `prompt/scripts/state_manager.py` (dual version tracking)
- New Components: None

**Advantages**
- ✅ Minimal change to existing file naming conventions
- ✅ Preserves current script logic with minor modifications

**Disadvantages**
- ❌ Doesn't solve core confusion - why does `plan_v2.5.1` produce `component_v2.6.0`?
- ❌ Unbounded versioning - artifact versions grow indefinitely without meaning
- ❌ High cognitive load - requires parsing headers to understand context

**Effort Estimate:** 20 developer hours
**Risk Assessment:** Medium - Addresses symptoms but not root cause

### Approach 2: Timestamp-Based Artifact Naming

**Overview**
Abandon semantic versioning for artifacts entirely, using timestamps for unique identification while tracking component versions separately in workflow_state.json.

**Technical Implementation**
```python
# New naming convention
artifact_name = f"{artifact_type}_{target_name}_{timestamp}.md"
# Example: plan_tv-ingest_20250715-143000.md
```

**Component Mapping**
- Primary Changes: `prompt/scripts/state_manager.py` (timestamp generation)
- Secondary Changes: All artifact references in documentation
- New Components: Timestamp utility functions

**Advantages**
- ✅ Guarantees unique filenames with chronological order
- ✅ Complete decoupling of artifact and component versions
- ✅ Simple collision-free naming scheme

**Disadvantages**
- ❌ Lacks iteration context - unclear if files are related iterations
- ❌ Not human-friendly - timestamps difficult to remember and reference
- ❌ No clear relationship between consecutive iterations

**Effort Estimate:** 25 developer hours
**Risk Assessment:** Low - Simple implementation but poor usability

### Approach 3: Task ID + Version + Iteration Counter (Recommended)

**Overview**
Leverage the Task Object Model to create artifact names that explicitly link to tasks with iteration counters AND embed the target version for complete context, while maintaining authoritative version tracking in workflow_state.json.

**Enhancement Analysis: Adding Version Component**
The addition of `v<version>` to the filename provides significant architectural benefits:

**Benefits of Version in Filename:**
- **Complete Self-Documentation**: Filename alone provides full artifact context
- **Historical Auditability**: Clear version targeting for compliance and review
- **Operational Clarity**: No state file dependency to understand artifact purpose
- **Search/Filter Capability**: Easy discovery of version-specific artifacts

**Addresses Redundancy Concerns:**
- **Not True Redundancy**: Filename serves different purpose than state tracking
- **Filename = Immediate Context**: For human readability and tooling
- **State File = Authoritative Source**: For programmatic workflow management
- **No Confusion Risk**: Unlike old system, version scope is completely clear

**Scope Change Handling:**
- Target version changes mid-task are rare in practice
- When they occur, file renames provide clear audit trail
- Folder organization contains scope changes within task boundary

**Technical Implementation**
```python
# Enhanced naming convention with version and folder organization
folder_path = f"artifacts/{artifact_type}/{name}/{task_id}"
artifact_name = f"{artifact_type}_{name}_{task_id}_v{version}_{iteration}.md"
full_path = f"{folder_path}/{artifact_name}"

# Examples:
# artifacts/consultations/prompt/T001/consultation_prompt_T001.md
# artifacts/plans/prompt/T001/plan_prompt_T001.md

# Enhanced workflow_state.json schema with version tracking
task_schema = {
    "T001": {
        "task_type": "system_architecture",
        "target_name": "prompt_main", 
        "target_version": "2.1.0",  # Official component version
        "folder_path": "artifacts/consultations/prompt/T001",
        "history": {
            "consultation": {
                "status": "completed",
                "iterations": {
                    "1": {"artifact_path": "consultation_prompt_T001.md", "status": "active"}
                },
                "latest_iteration": 1
            },
            "planning": {
                "status": "pending"
            }
        }
    }
}
```

**Component Mapping**
- Primary Changes: `prompt/scripts/state_manager.py` (iteration logic, schema updates)
- Secondary Changes: `prompt/templates/*/template_*.md` (header standardization)
- New Components: Migration script for existing artifacts

**Advantages**
- ✅ Complete context - filename `consultation_prompt_T001.md` provides full artifact context
- ✅ Folder organization - each task isolated in `artifacts/consultations/prompt/T001/`
- ✅ Concise task IDs - `T001` vs `task-001` (50% shorter)
- ✅ Enhanced scoping - name component prevents target confusion
- ✅ Version clarity - target version explicit in filename for historical auditing
- ✅ Self-documenting - no external dependencies to understand artifact purpose
- ✅ Supports clear feedback loops - "Rejecting T001_v2.1.0_i1, please produce i2"
- ✅ Aligns with Task-Centric Model from v2.0.0 architecture

**Disadvantages**
- ❌ Dependent on v2.0.0 Task Object Model implementation
- ❌ Longer filenames due to version component (manageable trade-off for clarity)
- ❌ Requires comprehensive migration strategy
- ❌ Potential file renames if target version changes mid-task (rare occurrence)

**Effort Estimate:** 40 developer hours
**Risk Assessment:** Medium - Complex but architecturally sound

## Recommended Solution

### Selected Approach
**Decision:** Approach 3 - Task ID + Version + Iteration Counter (Enhanced)

**Rationale:**
This enhanced approach represents the optimal solution that addresses the root cause of versioning confusion while providing complete context and robust workflow automation. Unlike the metadata fix which patches symptoms, or timestamps which sacrifice usability, the Task ID + Version + Iteration Counter approach creates a versioning scheme that is purpose-built for iterative workflow artifacts with complete self-documentation. The version component eliminates any external dependencies for understanding artifact context, while the task-centric organization enables perfect traceability. The integration with the existing Task Object Model creates architectural coherence and enables advanced features like automated iteration tracking and intelligent feedback loops.

### Implementation Strategy

**Phase 1: Schema Foundation** [~15 hours]
- Enhance `workflow_state.json` schema with `target_version` and `iterations` tracking
- Update `state_manager.py` with iteration calculation logic
- Implement `complete_phase` auto-generation of iteration numbers
- Deliverable: Enhanced state management infrastructure

**Phase 2: Standardization** [~15 hours]
- Define global artifact header standards in `prompt_main.md`
- Update all templates with standardized Task Context Block headers:
  ```markdown
  **Task ID:** [T001]
  **Task Type:** [component_feature/system_architecture/etc.]
  **Target:** [component_name]
  **Artifact Type:** [Plan/Consultation/etc.]
  **Version:** [X.Y.Z]
  **Author:** [LLM Role]
  **Date:** [YYYY-MM-DD]
  ```
- Implement plan profile standards (Full/Lite) and file manifest requirements
- Deliverable: Comprehensive artifact standards documentation

**Phase 3: Migration & Integration** [~10 hours]
- Create migration script for existing artifacts
- Update all existing documentation references
- Implement backward compatibility mechanisms
- Deliverable: Fully migrated system with new naming convention

### Technical Specifications

**Architecture Pattern:** Task-Centric Workflow with Iteration Tracking
```
Task Object Model (v2.0.0)
     |
     v
Task ID + Iteration Counter
     |
     v
Workflow Artifacts --> Perfect Traceability
```

**Key Interfaces:**
```python
class StateManager:
    """Enhanced state manager with iteration tracking"""
    def complete_phase(self, task_id: str, phase: str, artifact_content: str) -> str:
        """Auto-generates next iteration and updates task history"""
        current_iteration = self.get_latest_iteration(task_id, phase)
        next_iteration = current_iteration + 1
        folder_path = f"artifacts/{phase}s/{target_name}/{task_id}"
        artifact_name = f"{phase}_{target_name}_{task_id}_v{target_version}_i{next_iteration}.md"
        artifact_path = f"{folder_path}/{artifact_name}"
        self.update_task_history(task_id, phase, artifact_path)
        return artifact_path
```

**Data Flow:**
1. Task creation includes explicit `target_version` for final component
2. Phase completion triggers automatic iteration calculation
3. Artifact creation uses `[artifact_type]_[task_id]_i[iteration]` naming
4. State tracking maintains complete iteration history and status

**Integration Points:**
- Connects to: `workflow_state.json` for task and iteration tracking
- Depends on: Task Object Model v2.0.0 for task identification
- Affects: All workflow processes by providing enhanced traceability

## Risk Analysis

### Technical Risks
| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|-------------------|
| Migration Data Loss | Medium | High | Comprehensive backup and rollback procedures |
| Schema Compatibility | Low | Medium | Backward compatibility layer during transition |
| Performance Degradation | Low | Low | Iteration logic is O(1) complexity |

### Implementation Risks
- **Complexity Creep:** Limit scope to core versioning and standards - avoid feature expansion
- **Integration Issues:** Phase implementation to validate each component before proceeding
- **Performance Impact:** Minimal - iteration tracking adds negligible overhead

## Dependencies & Prerequisites

### Technical Dependencies
- **Task Object Model v2.0.0:** Must be implemented before Task ID system
- **Python 3.8+:** Required for enhanced JSON schema handling
- **Existing workflow_state.json:** Base schema must be functional

### Process Dependencies
- **v2.0.0 Completion:** Task Object Model implementation must be complete
- **Template Audit:** All existing templates must be catalogued before updates

### Knowledge Prerequisites
- Team should understand Task-Centric Workflow concepts
- Familiarity with JSON schema validation helpful

## Validation Criteria

The solution will be considered successful when:

**Functional Validation:**
- [ ] All new artifacts follow `[artifact_type]_[name]_[task_id]_v[version]_i[iteration].md` naming
- [ ] All artifacts organized in `artifacts/{type}/{name}/{task_id}/` folder structure
- [ ] Version component clearly indicates target component version
- [ ] workflow_state.json correctly tracks target_version separately from iterations
- [ ] state_manager.py automatically generates correct iteration numbers
- [ ] All templates include standardized Task Context Block headers

**Performance Validation:**
- [ ] Artifact creation time < 50ms additional overhead
- [ ] State file size growth < 10% for typical workflows
- [ ] Migration completes < 30 minutes for existing artifacts

**Quality Validation:**
- [ ] Migration script preserves all existing artifact content
- [ ] Backward compatibility maintained during transition period
- [ ] All templates validate against new standards

## Consultation Checklist

Before handing off to the Planner:
- [x] All approaches have concrete examples with code snippets
- [x] File paths and components are specific (state_manager.py, workflow_state.json)
- [x] Estimates include buffer time (40 hours total with phases)
- [x] Risks have mitigation strategies (backup, rollback, phased implementation)
- [x] Dependencies are clearly stated (v2.0.0 Task Object Model)
- [x] Success criteria are measurable (naming compliance, performance metrics)
- [x] Integration points are identified (workflow_state.json, state_manager.py)
- [x] Architecture aligns with project patterns (Task-Centric Workflow)

## Next Steps

### For the Planner
1. Transform this consultation into detailed implementation plan with specific file changes
2. Pay special attention to migration strategy and backward compatibility requirements
3. Clarify if needed: Specific template update priorities and rollback procedures

### For the Client
1. Review and approve the Task ID + Iteration Counter approach
2. Confirm the 40-hour timeline meets project needs
3. Identify any additional workflow standardization requirements

---

## Appendix: Additional Context

### Related Consultations
- Task Object Model v2.0.0 architectural foundation

### Reference Materials
- `prompt/documentation/prompt_main.md` - Current workflow standards
- `prompt/config/workflow_state.json` - Existing state schema
- `prompt/scripts/state_manager.py` - Current state management logic

### Glossary
- **Workflow Artifact:** Transactional outputs like plans, consultations, reviews
- **Foundational Document:** Long-lived standards like prompt_main.md, general.md
- **Task ID:** Unique identifier linking workflow artifacts to originating tasks
- **Iteration Counter:** Simple numeric sequence (i1, i2, i3) for artifact revisions

---

## File Naming Convention
**IMPLEMENTATION DEMONSTRATION:** This consultation document implements the fully enhanced Task ID + Version + Iteration Counter system. The file is located at:

`prompt/artifacts/consultations/prompt/T001/consultation_prompt_T001.md`

Demonstrates the complete approach where:
- `consultation` = artifact type
- `prompt` = target name/component scope
- `T001` = concise unique task identifier
- `v2.1.0` = target component version being developed
- `i1` = first iteration of this consultation
- Folder `T001/` contains all iterations and related artifacts for this task

This provides complete context in the filename alone, superior organization, and eliminates all versioning confusion while maintaining perfect traceability.