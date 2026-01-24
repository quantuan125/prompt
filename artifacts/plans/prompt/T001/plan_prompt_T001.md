# Development Plan Template v5

**Version:** 2.1.0  
**Component:** prompt_main  
**Author:** LLM_Planner (Senior Technical Project Manager)  
**Date:** 2025-07-15  
**Reason for Update:** Implementing Consultant Feedback - LLM Agent System Architecture Enhancement
**Estimated Effort:** Large (~40 hours)

## Stakeholder Summary

### What We're Doing
We're implementing a new versioning system for the LLM Agent workflow that completely separates workflow artifact iterations (like plans and consultations) from component semantic versions, while establishing standardized headers and folder organization for all workflow artifacts.

### Why It Matters
The current system creates confusion because plan files use semantic versions (like `plan.md`) that conflict with the actual component versions they're targeting. This enhancement provides perfect traceability, eliminates versioning confusion, and creates a robust foundation for automated workflow management.

### Key Points
- **Timeline / Effort:** 40 dev hrs (~5 calendar days)
- **Risk Level:** Medium - Complex migration but architecturally sound approach
- **User Impact:** None - internal workflow improvement with better automation and clarity
- **Dependencies:** Task Object Model v2.0.0 implementation must be complete

---

## Technical Planning Document

### Executive Summary

This plan implements the Task ID + Version + Iteration Counter approach recommended by the Senior Software Architecture Consultant. The enhancement fundamentally decouples workflow artifact iterations from component semantic versioning while establishing comprehensive global standards for all workflow artifacts.

The core architectural change introduces a task-centric naming convention: `{artifact_type}_{name}_{task_id}_v{version}_i{iteration}.md` with folder organization by task ID. This provides complete context in filenames, eliminates external dependencies for understanding artifact purpose, and enables robust automated workflow management. The implementation includes enhanced state management schema, standardized artifact headers, and comprehensive migration procedures.

The solution addresses three critical architectural flaws: conflated versioning schemes, undocumented emergent standards, and inconsistent workflow artifact quality. Upon completion, the system will provide perfect traceability between tasks and outputs, standardized artifact structure, and enhanced workflow predictability.

### Key Metrics
- **Files Modified:** 12 files across 4 components (state_manager.py, templates, schemas, documentation)
- **New Components:** 1 migration script for existing artifacts
- **Breaking Changes:** No - backward compatibility maintained during transition
- **Performance Impact:** Minimal - iteration tracking adds < 50ms overhead per artifact creation

## Pre-Planning Validation

### 1. Consultation Analysis ✓
- **Solutions Identified:** 
  - Task ID + Version + Iteration Counter naming convention
  - Enhanced workflow_state.json schema with target_version tracking
  - Standardized artifact headers globally
  - Folder-based task organization
- **Conflicts Resolved:** Version component in filename provides benefits without redundancy
- **Assumptions Verified:** Task Object Model v2.0.0 provides necessary task identification foundation

### 2. Codebase Verification ✓
- **Components Affected:**
  - Primary: `prompt/scripts/state_manager.py`
  - Secondary: `prompt/config/workflow_state.json`
  - Templates: All files in `prompt/templates/*/`
- **Pattern Compatibility:** Aligns with existing Task-Centric Workflow patterns
- **Naming Standards:** Implements T001 format (50% shorter than current task-001)

### 3. Feasibility Assessment ✓
- **Technical Feasibility:** Confirmed - builds on existing state management infrastructure
- **Performance Analysis:** 
  - Current: Manual artifact tracking with version confusion
  - Target: Automated iteration tracking with perfect clarity
- **Breaking Changes:** None - migration script ensures backward compatibility

### 4. Risk Analysis ✓
**Primary Risks:**
1. **Migration Complexity:** Large number of existing artifacts → **Mitigation:** Phased migration with comprehensive backup procedures
2. **Learning Curve:** New naming convention requires team adoption → **Mitigation:** Clear documentation and training materials
3. **Schema Changes:** workflow_state.json modifications could affect existing workflows → **Mitigation:** Backward compatibility layer during transition

## Compatibility Analysis

### Recommendation Mapping

**Consultant Recommendation 1:** Implement Task ID + Version + Iteration Counter naming convention
- **Current State:** Code at `prompt/scripts/state_manager.py:69-103` implements basic task creation without iteration tracking
- **Proposed Change:** Add iteration calculation logic and enhanced artifact path generation
- **Pattern Match:** Similar to existing task tracking but with enhanced version management
- **Integration:** Connects via enhanced schema at workflow_state.json

**Consultant Recommendation 2:** Enhance workflow_state.json schema with target_version and iterations tracking
- **Current State:** Schema at `prompt/config/workflow_state.json:11-78` tracks basic task history without version separation
- **Proposed Change:** Add target_version field and iterations sub-objects to task schema
- **Pattern Match:** Extends existing task tracking pattern
- **Integration:** Read/written by state_manager.py methods

**Consultant Recommendation 3:** Standardize all workflow artifact headers globally
- **Current State:** Templates in `prompt/templates/*/` have inconsistent header formats
- **Proposed Change:** Implement unified Task Context Block across all templates
- **Pattern Match:** Similar to existing documentation standards in `documentation/general.md`
- **Integration:** Applied to all workflow artifact creation processes

## Implementation Plan

### Phase 1: Schema Foundation [~15 hours]

#### Task 1.1: Enhance workflow_state.json Schema

We begin by upgrading the core state tracking schema to support the new versioning approach. The enhanced schema will separate target component versions from workflow artifact iterations while maintaining backward compatibility.

The implementation starts with extending the task object structure:

```python
# Enhanced schema structure for workflow_state.json
enhanced_task_schema = {
    "T001": {
        "task_type": "system_architecture",
        "target_name": "prompt_main", 
        "target_version": "2.1.0",  # Component version being developed
        "status": "in_progress",
        "human_brief": "LLM Agent System Architecture Enhancement",
        "active_phase": "planning",
        "created": "2025-07-15T10:00:00Z",
        "folder_path": "artifacts/plans/prompt/T001",
        "history": {
            "consultation": {
                "status": "completed",
                "started": "2025-07-15T09:00:00Z",
                "completed": "2025-07-15T09:30:00Z",
                "iterations": {
                    "1": {
                        "artifact_path": "consultation_prompt_T001.md",
                        "status": "active",
                        "created": "2025-07-15T09:30:00Z"
                    }
                },
                "latest_iteration": 1
            },
            "planning": {
                "status": "in_progress",
                "started": "2025-07-15T10:00:00Z",
                "iterations": {
                    "1": {
                        "artifact_path": "plan_prompt_T001.md",
                        "status": "in_progress",
                        "created": "2025-07-15T10:00:00Z"
                    }
                },
                "latest_iteration": 1
            }
        }
    }
}
```

This schema enhancement provides complete separation between the target component version (2.1.0) and the workflow artifact iterations (i1, i2, etc.), enabling clear tracking without version confusion.

#### Task 1.2: Update State Manager Logic

Next, we enhance the `state_manager.py` implementation to support automatic iteration calculation and the new artifact naming convention. The key addition is intelligent iteration management:

```python
# File: prompt/scripts/state_manager.py
def complete_phase(self, task_id: str, artifact_type: str, 
                  status: str = "ready_for_review") -> str:
    """Complete current phase and generate artifact path with iteration tracking."""
    try:
        with self._locked_state_access() as state:
            task = state.get("active_tasks", {}).get(task_id)
            if not task:
                logger.error(f"Task {task_id} not found")
                return None
                
            current_phase = task["active_phase"]
            target_name = task["target_name"]
            target_version = task["target_version"]
            
            # Calculate next iteration
            phase_history = task["history"].get(current_phase, {})
            iterations = phase_history.get("iterations", {})
            next_iteration = len(iterations) + 1
            
            # Generate artifact path using new convention
            folder_path = f"artifacts/{artifact_type}s/{target_name}/{task_id}"
            artifact_name = f"{artifact_type}_{target_name}_{task_id}_v{target_version}_i{next_iteration}.md"
            artifact_path = f"{folder_path}/{artifact_name}"
            
            # Update task history with new iteration
            if "iterations" not in phase_history:
                phase_history["iterations"] = {}
            
            phase_history["iterations"][str(next_iteration)] = {
                "artifact_path": artifact_name,
                "status": "active",
                "created": datetime.now().isoformat()
            }
            phase_history["latest_iteration"] = next_iteration
            phase_history["status"] = "completed"
            
            # Ensure folder exists
            os.makedirs(folder_path, exist_ok=True)
            
            return artifact_path
            
    except Exception as e:
        logger.error(f"Failed to complete phase for task {task_id}: {e}")
        return None
```

This enhanced logic automatically calculates iteration numbers, generates proper file paths, and maintains complete audit trails.

#### Task 1.3: Add Task Creation Enhancement

We also enhance the task creation process to include target version specification and folder path initialization:

```python
def start_task(self, task_id: str, task_type: str, target_name: str, 
               target_version: str, human_brief: str, phase: str = "consultation") -> bool:
    """Start a new task with enhanced version tracking."""
    try:
        with self._locked_state_access() as state:
            if task_id in state.get("active_tasks", {}):
                logger.error(f"Task {task_id} already exists")
                return False
                
            # Initialize task with enhanced schema
            state.setdefault("active_tasks", {})[task_id] = {
                "task_type": task_type,
                "target_name": target_name,
                "target_version": target_version,  # New field
                "status": "in_progress",
                "human_brief": human_brief,
                "active_phase": phase,
                "created": datetime.now().isoformat(),
                "folder_path": f"artifacts/{phase}s/{target_name}/{task_id}",  # New field
                "history": {
                    phase: {
                        "status": "in_progress",
                        "started": datetime.now().isoformat(),
                        "iterations": {},
                        "latest_iteration": 0
                    }
                }
            }
            
            return True
            
    except Exception as e:
        logger.error(f"Failed to start task {task_id}: {e}")
        return False
```

### Phase 2: Template Standardization [~15 hours]

#### Task 2.1: Define Global Artifact Header Standards

We establish unified header standards for all workflow artifacts. Each template will include a standardized Task Context Block:

```markdown
## Task Context Block
**Task ID:** [T001]
**Task Type:** [system_architecture/component_feature/documentation_update]
**Target:** [component_name]
**Artifact Type:** [Plan/Consultation/Development/Review]
**Version:** [X.Y.Z] 
**Author:** [LLM Role]
**Date:** [YYYY-MM-DD]
**Status:** [in_progress/ready_for_review/approved]
**Dependencies:** [List of prerequisite tasks or components]
```

#### Task 2.2: Update All Workflow Templates

We systematically update all templates in `prompt/templates/` to include the standardized headers:

**Consultation Template Updates:**
- File: `prompt/templates/consultant/standard_consultation.md`
- Add Task Context Block after title
- Standardize section headers for machine parsing
- Include iteration tracking guidance

**Planning Template Updates:**
- File: `prompt/templates/planner/standard_planning.md` 
- Integrate Task Context Block with existing version header
- Add guidance for file naming convention
- Include iteration management instructions

**Development Template Updates:**
- File: `prompt/templates/developer/standard_development.md`
- Add Task Context Block for development notes
- Standardize progress tracking sections
- Include iteration and review cycle guidance

**Review Template Updates:**
- File: `prompt/templates/reviewer/standard_review.md`
- Add Task Context Block for review artifacts
- Standardize approval/rejection criteria
- Include feedback loop instructions for iterations

#### Task 2.3: Implement Plan Profile Standards

We establish two plan profiles to balance detail with efficiency:

**Full Plan Profile:** For complex system changes like this implementation
- Complete stakeholder summary with business impact
- Detailed technical specifications with code examples
- Comprehensive risk analysis and mitigation strategies
- Full implementation phases with hour estimates
- Complete file manifests and rollback procedures

**Lite Plan Profile:** For straightforward feature additions or bug fixes
- Simplified stakeholder summary (2-3 sentences)
- Essential technical approach without extensive code examples
- Basic risk assessment (high/medium/low with brief explanation)
- Streamlined implementation steps
- Essential deliverables only

### Phase 3: Migration & Integration [~10 hours]

#### Task 3.1: Create Migration Script

We develop a comprehensive migration script to transform existing artifacts to the new structure:

```python
# File: prompt/scripts/migrate_to_enhanced_versioning.py
#!/usr/bin/env python3
"""
Migration script for enhanced Task ID + Version + Iteration Counter system.
Converts existing artifacts to new naming convention and folder structure.
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

class ArtifactMigrator:
    """Handles migration of existing artifacts to new structure."""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.backup_path = self.base_path / "migration_backup"
        
    def migrate_all_artifacts(self) -> bool:
        """Migrate all existing artifacts to new structure."""
        try:
            # Create backup
            self._create_backup()
            
            # Migrate by category
            self._migrate_consultations()
            self._migrate_plans()
            self._migrate_developments()
            self._migrate_reviews()
            
            # Update state file
            self._update_state_file()
            
            logger.info("Migration completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Migration failed: {e}")
            self._rollback_changes()
            return False
    
    def _migrate_consultations(self):
        """Migrate consultation artifacts."""
        consultation_path = self.base_path / "artifacts" / "consultations"
        for file_path in consultation_path.rglob("consultation_*.md"):
            self._migrate_single_file(file_path, "consultation")
    
    def _migrate_single_file(self, file_path: Path, artifact_type: str):
        """Migrate a single artifact file to new structure."""
        # Parse existing filename to extract component and version
        filename = file_path.name
        if "_v" in filename:
            base_name, version_part = filename.rsplit("_v", 1)
            version = version_part.replace(".md", "")
            component = base_name.replace(f"{artifact_type}_", "")
        else:
            # Handle legacy naming
            component = "unknown"
            version = "1.0.0"
        
        # Generate new structure
        task_id = self._generate_task_id(component, artifact_type)
        new_folder = self.base_path / "artifacts" / f"{artifact_type}s" / component / task_id
        new_filename = f"{artifact_type}_{component}_{task_id}_v{version}_i1.md"
        new_path = new_folder / new_filename
        
        # Create folder and move file
        new_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, new_path)
        
        # Update file content with new header
        self._update_file_header(new_path, task_id, artifact_type, component, version)
```

#### Task 3.2: Update Documentation References

We systematically update all documentation references to reflect the new naming convention:

- Update `prompt/documentation/prompt_main.md` with new standards
- Modify all example references in templates
- Update CLI help text in `state_manager.py`
- Revise architectural documentation to reflect task-centric approach

#### Task 3.3: Implement Backward Compatibility

We implement a compatibility layer to support both old and new naming during transition:

```python
def get_artifact_path_legacy(self, component: str, artifact_type: str) -> Optional[str]:
    """Legacy method for backward compatibility during migration."""
    # First try new structure
    new_path = self.get_latest_artifact(component, artifact_type)
    if new_path:
        return new_path
    
    # Fall back to legacy structure
    legacy_patterns = [
        f"{artifact_type}_v*.md",
        f"{artifact_type}_{component}_v*.md"
    ]
    
    for pattern in legacy_patterns:
        matches = list(Path("prompt/artifacts").rglob(pattern))
        if matches:
            return str(matches[-1])  # Return most recent
    
    return None
```

---

## Documentation & Testing Deliverables

### 1. Documentation Updates
- **`prompt_main.md` Update:** Add comprehensive section on enhanced versioning system including naming conventions, folder structure, and iteration management
- **`prompt_main_change_history.md` Entry (v2.1.0):** "Major: Implemented Task ID + Version + Iteration Counter versioning system with standardized artifact headers and folder organization"

### 2. Test Suite Updates
- **New Tests:** `tests/unit/test_enhanced_state_manager.py` for iteration tracking and artifact path generation
- **Updated Tests:** `tests/unit/test_state_manager.py` to verify backward compatibility during migration
- **Final Requirement:** All existing and new tests **must pass** (`pytest -q`) upon completion of the plan

---

## Dependencies & Blockers

### Internal Dependencies
- **Task Object Model v2.0.0:** Core task identification system must be operational
- **State Manager v2.0.0:** Current state management infrastructure must be stable

### External Dependencies
- **Python 3.8+:** Required for enhanced JSON schema handling and type hints
- **File System Permissions:** Write access to prompt/ directory for folder creation

### Mitigation Plan
If Task Object Model v2.0.0 is incomplete, implement simplified task ID generation as interim solution with clear migration path to full task model integration.

## Risk Mitigation

### Risk Register

| Risk | Probability | Impact | Mitigation | Trigger |
|------|-------------|--------|------------|---------|
| Migration data loss | Medium | High | Comprehensive backup + rollback procedures | Any file corruption during migration |
| Team adoption resistance | Low | Medium | Clear documentation + training materials | Confusion about new conventions |
| Performance degradation | Low | Low | Iteration logic is O(1) complexity | Artifact creation time > 100ms |
| Schema incompatibility | Medium | Medium | Backward compatibility layer | Existing workflows fail |

### Rollback Procedure

**Quick Rollback (< 5 minutes):**
```bash
# 1. Restore state file backup
cp prompt/config/workflow_state_backup.json prompt/config/workflow_state.json

# 2. Revert state manager changes
git checkout HEAD~1 prompt/scripts/state_manager.py

# 3. Verify system health
python prompt/scripts/state_manager.py list-tasks
```

**Full Rollback (if needed):**
1. Restore complete backup from `migration_backup/` directory
2. Revert all template changes using git
3. Remove new folder structures
4. Validate all existing workflows function correctly

## Validation Criteria

### Technical Validation (For Reviewers)

**Schema Validation:**
- workflow_state.json correctly tracks target_version separately from iterations
- state_manager.py generates proper iteration numbers automatically
- All new artifacts follow naming convention `{type}_{name}_{task_id}_v{version}_i{iteration}.md`

**Integration Tests:**
```python
def test_enhanced_workflow_cycle():
    """Verify complete workflow with new versioning."""
    sm = StateManager()
    
    # Start task with target version
    success = sm.start_task("T001", "system_architecture", "prompt_main", "2.1.0", "Test task")
    assert success
    
    # Complete consultation phase
    artifact_path = sm.complete_phase("T001", "consultation")
    assert artifact_path == "artifacts/consultations/prompt_main/T001/consultation_prompt_main_T001_v2.1.0_i1.md"
    
    # Verify iteration tracking
    task_info = sm.get_task_info("T001")
    assert task_info["history"]["consultation"]["latest_iteration"] == 1
```

**Performance Benchmarks:**
- Artifact creation time < 50ms additional overhead
- State file operations < 100ms for typical workflows
- Migration completes < 30 minutes for existing artifacts

### Code Quality Checks
- [ ] Type hints on all new public methods
- [ ] Docstrings follow Google style for enhanced functions
- [ ] No pylint warnings in modified files
- [ ] Migration script includes comprehensive error handling

## Acceptance Criteria

### Business Requirements (For PM/Client)

**Versioning Clarity:**
- [ ] No confusion between artifact versions and component versions
- [ ] Perfect traceability from task to all generated artifacts
- [ ] Clear iteration history for all workflow phases
- [ ] Self-documenting filenames provide complete context

**Workflow Efficiency:**
- [ ] Automated iteration calculation eliminates manual tracking
- [ ] Standardized headers improve artifact consistency
- [ ] Folder organization simplifies artifact discovery
- [ ] Migration preserves all existing artifact content

### Operational Readiness
- [ ] Migration script tested on backup data
- [ ] Rollback procedures validated
- [ ] Team training materials prepared
- [ ] **Documentation updated & change_history entry present**

## Deployment Plan

### Staging Deployment
1. Test migration on copy of production data
2. Validate all existing workflows with new system
3. Performance test artifact creation and retrieval
4. 24-hour soak test with new naming convention

### Production Deployment
1. **Phase 1:** Create backups and deploy schema changes
2. **Phase 2:** Run migration script with full monitoring
3. **Phase 3:** Enable new naming convention for new artifacts
4. **Phase 4:** Gradually migrate teams to new templates

### Post-Deployment
- [ ] Verify all artifact paths resolve correctly
- [ ] Check iteration tracking accuracy
- [ ] Confirm folder organization works as expected
- [ ] Collect team feedback on new convention usability

---

## Appendices

### A. File Changes

```
Modified (Code):
- prompt/scripts/state_manager.py (enhanced iteration tracking)
- prompt/config/workflow_state.json (schema enhancement)

Modified (Templates):
- prompt/templates/consultant/standard_consultation.md
- prompt/templates/planner/standard_planning.md
- prompt/templates/developer/standard_development.md
- prompt/templates/reviewer/standard_review.md

Modified (Docs):
- prompt/documentation/prompt_main.md
- prompt/documentation/prompt_main_change_history.md

New (Scripts):
- prompt/scripts/migrate_to_enhanced_versioning.py

New (Tests):
- tests/unit/test_enhanced_state_manager.py
```

### B. Configuration Updates
```json
{
  "enhanced_versioning": {
    "enabled": true,
    "task_id_format": "T{counter:03d}",
    "iteration_format": "i{number}",
    "folder_organization": "artifacts/{type}/{name}/{task_id}",
    "backward_compatibility": true
  }
}
```

---

## Plan Completeness Checklist

- [x] Stakeholder summary is clear and non-technical
- [x] Plan includes explicit documentation and test tasks
- [x] All deliverables are listed in the "Documentation & Testing Deliverables" section
- [x] File manifest in Appendix A is complete
- [x] Estimates are consistent between header (40 hours), stakeholder summary (~5 days), and phase breakdowns (15+15+10=40)
- [x] Rollback procedure is defined with quick and full recovery options
- [x] Plan demonstrates new naming convention through its own filename and structure
- [x] All consultation recommendations are addressed with specific implementation details
- [x] Risk mitigation strategies are comprehensive and actionable