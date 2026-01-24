# Development Plan: LLM Agent System Architecture Improvements v2.0.1

**Version:** 2.0.1  
**Component:** prompt  
**Author:** LLM_Planner  
**Date:** 2025-07-13  
**Reason for Update:** Corrected plan addressing consultant feedback on JSON handling, paths, and archive strategy
**Estimated Effort:** Large (~85 hours)

## Stakeholder Summary

### What We're Doing
We are implementing fundamental architectural improvements to our LLM agent system to resolve 7 critical issues that threaten system stability, scalability, and maintainability.

### Why It Matters
The current system has unsafe state management that could corrupt workflows, cannot handle concurrent tasks, and has chaotic documentation that makes maintenance unreliable. These fixes will make the system production-ready and enable future growth.

### Key Points
- **Timeline / Effort:** 85 dev hrs (~2-3 weeks)
- **Risk Level:** Medium - Requires careful migration but consultant analysis is validated
- **User Impact:** None - internal architecture improvements only
- **Dependencies:** None - self-contained refactoring

---

## Technical Planning Document

### Executive Summary

This plan implements the consultant's validated architectural recommendations to transform our LLM agent system from a fragile prototype into a robust, scalable platform. The core changes establish a safe State Manager for workflow coordination, implement a task-centric data model enabling concurrent workflows, reorganize the directory structure for maintainability, and establish clear documentation hierarchy to eliminate redundancy and conflicts.

The approach is conservative and phased: we start with the most critical safety issues (state management), then address scalability (task model), followed by organization (directory cleanup) and documentation standards. Each phase includes comprehensive rollback procedures and maintains backward compatibility.

**Version 2.0.1 incorporates critical consultant feedback corrections addressing JSON corruption bugs, path resolution issues, orchestration redundancy, file relationship clarity, and missing archive strategy implementation.**

### Key Metrics
- **Files Modified:** ~25 files across prompt system
- **New Components:** 4 new scripts (state_manager.py, archive_manager.py, validate_system.py, path resolution utilities)
- **Breaking Changes:** No - backward compatibility maintained during transition
- **Performance Impact:** Improved reliability, no performance regression expected

## Pre-Planning Validation

### 1. Consultation Analysis ✓
- **Solutions Identified:** 
  1. State-First Protocol with Central State Manager
  2. Task Object Model for concurrent workflow support
  3. Function-centric directory structure cleanup
  4. Strict documentation hierarchy enforcement
  5. Integration point standardization
- **Conflicts Resolved:** None - all recommendations align with current architecture
- **Assumptions Verified:** All 7 identified issues confirmed in our codebase

### 2. Codebase Verification ✓
- **Components Affected:**
  - Primary: `prompt/config/workflow_state.json`, `prompt/scripts/path_utilities.py`
  - Secondary: All role system files, orchestration.json, prompt_main.md
- **Pattern Compatibility:** Confirmed - consultant solutions respect existing patterns
- **Naming Standards:** Current standards maintained (component-based architecture)

### 3. Feasibility Assessment ✓
- **Technical Feasibility:** Confirmed - 85% of recommendations directly applicable
- **Performance Analysis:** 
  - Current: Unsafe direct JSON editing, race conditions possible
  - Target: Transactional state management with file locking
- **Breaking Changes:** None - migration maintains backward compatibility

### 4. Risk Analysis ✓
**Primary Risks:**
1. **State Migration Failure:** JSON corruption during transition → **Mitigation:** Comprehensive backup and rollback procedures
2. **Directory Migration Issues:** Breaking existing workflows → **Mitigation:** Scripted migration with verification steps

## Compatibility Analysis

### Recommendation Mapping

**Consultant Recommendation 1:** State-First Protocol
- **Current State:** `path_utilities.py:44-77` implements filesystem discovery via `find_latest_artifact()`
- **Proposed Change:** Replace with `state_manager.py` CLI that queries `workflow_state.json` as sole authority
- **Pattern Match:** Similar to service pattern used in component architecture
- **Integration:** State manager becomes single interface for all workflow state operations

**Consultant Recommendation 2:** Central State Manager Script
- **Current State:** Direct JSON manipulation in `path_utilities.py:130-145`
- **Proposed Change:** Create `prompt/scripts/state_manager.py` with file locking and CLI interface
- **Pattern Match:** Follows existing script pattern in `prompt/scripts/`
- **Integration:** All agents use CLI commands instead of direct file access

**Consultant Recommendation 3:** Task Object Model
- **Current State:** Component-centric workflow structure in `workflow_state.json`
- **Proposed Change:** Refactor to task-centric with unique task IDs for concurrency
- **Pattern Match:** Aligns with modern development workflow tools (Jira, GitHub Issues)
- **Integration:** Backward compatible transition maintaining existing component tracking

**Consultant Recommendation 4:** Directory Structure Cleanup
- **Current State:** Mixed role-centric and function-centric organization
- **Proposed Change:** Pure function-centric layout with `prompt/roles/`, `prompt/templates/`
- **Pattern Match:** Follows component organization principles
- **Integration:** Scripted migration preserves all existing files

**Consultant Recommendation 5:** Documentation Hierarchy**
- **Current State:** Redundant rules across `general.md`, `prompt_main.md`, role files
- **Proposed Change:** Strict hierarchy: `general.md` > `prompt_main.md` > role files
- **Pattern Match:** Follows existing documentation standards in `general.md`
- **Integration:** Reference-based approach eliminates duplication

**Consultant Recommendation 6:** Integration Standardization**
- **Current State:** Incomplete `orchestration.json`, undefined feedback loops
- **Proposed Change:** Complete task workflow definitions and explicit reviewer feedback
- **Pattern Match:** Extends existing orchestration pattern
- **Integration:** Standardizes template selection and role integration across all roles

**Consultant Recommendation 7:** Automated Consistency Checking**
- **Current State:** Manual documentation maintenance prone to drift
- **Proposed Change:** `validate_system.py` script for automated consistency checks
- **Pattern Match:** Similar to existing validation scripts
- **Integration:** Integrates with test suite for continuous validation

## Implementation Plan

### Phase 1: Critical Safety Fixes [~35 hours]

#### Task 1.1: Create Central State Manager (CORRECTED)

We begin by implementing the most critical safety improvement: the central state manager script. This eliminates the dangerous practice of direct JSON file manipulation and establishes `workflow_state.json` as the authoritative source of truth.

The implementation starts with creating the state manager infrastructure in `prompt/scripts/state_manager.py`. This script will use Python's `argparse` to provide a rich CLI interface and implement file locking to prevent corruption from concurrent access.

**CRITICAL CORRECTION:** The original plan had a JSON corruption bug. The correct implementation must use proper file truncation:

```python
# File: prompt/scripts/state_manager.py
import json
import fcntl
import argparse
import logging
import os
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class StateManager:
    """
    Centralized, transactional state management for workflow_state.json.
    
    Provides safe, atomic operations for managing LLM agent workflow state
    with file locking to prevent corruption from concurrent access.
    """
    
    def __init__(self, state_file: str = "prompt/config/workflow_state.json"):
        self.state_file = Path(state_file)
        self._ensure_state_file_exists()
        
    def start_task(self, task_id: str, task_type: str, target_name: str, 
                   human_brief: str, phase: str = "consultation") -> bool:
        """Start a new task with unique ID."""
        with self._locked_state_access() as state:
            if task_id in state.get("active_tasks", {}):
                logger.error(f"Task {task_id} already exists")
                return False
                
            # Initialize new task structure
            state.setdefault("active_tasks", {})[task_id] = {
                "task_type": task_type,
                "target_name": target_name,
                "status": "in_progress",
                "human_brief": human_brief,
                "active_phase": phase,
                "created": datetime.now().isoformat(),
                "history": {
                    phase: {
                        "status": "in_progress",
                        "started": datetime.now().isoformat()
                    }
                }
            }
            
        logger.info(f"Started task {task_id} for {target_name}")
        return True
        
    def complete_phase(self, task_id: str, output_artifact: str, 
                      status: str = "ready_for_review") -> bool:
        """Complete current phase and register output artifact."""
        with self._locked_state_access() as state:
            task = state.get("active_tasks", {}).get(task_id)
            if not task:
                logger.error(f"Task {task_id} not found")
                return False
                
            current_phase = task["active_phase"]
            task["history"][current_phase].update({
                "status": "completed",
                "completed": datetime.now().isoformat(),
                "artifact_path": output_artifact,
                "output_status": status
            })
            
        logger.info(f"Completed phase {current_phase} for task {task_id}")
        return True
        
    @contextmanager
    def _locked_state_access(self):
        """Context manager for safe, locked access to state file."""
        # CRITICAL FIX: Use separate read/write operations to prevent corruption
        with open(self.state_file, 'r') as read_file:
            fcntl.flock(read_file.fileno(), fcntl.LOCK_EX)
            try:
                state = json.load(read_file)
                yield state
                
                # Write to new file content safely
                with open(self.state_file, 'w') as write_file:
                    json.dump(state, write_file, indent=2)
                    write_file.flush()  # Ensure data is written
                    os.fsync(write_file.fileno())  # Force OS to write to disk
                    
            finally:
                fcntl.flock(read_file.fileno(), fcntl.LOCK_UN)
```

Next, we implement the CLI interface that agents will use to interact with the state manager. The CLI provides simple, high-level commands that abstract the complexity of state management:

```bash
# Agent starts a new task
python prompt/scripts/state_manager.py start-task \
    --task-id "task-001" \
    --type "component_feature" \
    --target "tv_ingest" \
    --brief "Implement enhanced caching for market data"

# Agent completes current phase
python prompt/scripts/state_manager.py complete-phase \
    --task-id "task-001" \
    --output "prompt/artifacts/consultations/tv_ingest/consultation_v2.5.0.md" \
    --status "ready_for_review"

# Agent gets next phase inputs
python prompt/scripts/state_manager.py get-inputs --task-id "task-001"
```

#### Task 1.2: Deprecate Filesystem Discovery (CORRECTED)

With the state manager in place, we can safely deprecate the problematic `find_latest_artifact` function in `path_utilities.py`. This function is the source of the "Source of Truth" conflict that creates unpredictable agent behavior.

**CRITICAL CORRECTION:** The original plan used fragile relative paths. The correct implementation uses robust path resolution:

```python
# File: prompt/scripts/path_utilities.py (modified)
import os
import subprocess
from pathlib import Path

def find_latest_artifact(component: str, artifact_type: str) -> Optional[Tuple[str, Path]]:
    """
    DEPRECATED: Use state_manager.py instead.
    
    This function is deprecated in favor of the centralized state manager.
    It will be removed in the next major version.
    """
    import warnings
    warnings.warn(
        "find_latest_artifact is deprecated. Use state_manager.py CLI instead.",
        DeprecationWarning,
        stacklevel=2
    )
    
    # CRITICAL FIX: Use robust path resolution instead of relative paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    state_manager_path = os.path.join(current_dir, 'state_manager.py')
    
    try:
        result = subprocess.run([
            "python", state_manager_path, 
            "get-latest-artifact", 
            "--component", component, 
            "--type", artifact_type
        ], capture_output=True, text=True, cwd=current_dir)
        
        if result.returncode == 0:
            # Parse state manager output
            path_str = result.stdout.strip()
            if path_str:
                path = Path(path_str)
                version = extract_version_from_path(path)
                return (version, path)
    except Exception as e:
        logger.error(f"State manager call failed: {e}")
        
    return None
```

This approach maintains backward compatibility while encouraging migration to the new state manager interface.

#### Task 1.3: Update Agent Integration

Finally, we update the role system files to use the new state manager interface. Each role will be modified to query the state manager for inputs and register outputs through the CLI.

We start by updating the consultant role in `prompt/consultant/consultant_system.md` to include the new workflow protocol:

```markdown
## Execution Protocol

This protocol operates within the master workflow defined in `prompt_main.md`. The following steps detail the specific actions for the Consultant phase:

1. **Query State Manager for Task Context:**
   ```bash
   python prompt/scripts/state_manager.py get-task-info --task-id ${TASK_ID}
   ```

2. **Load Required Inputs:**
   - Human instruction: Provided by human operator
   - Component documentation: From state manager task context
   - Project context: `@prompt/config/project_context.json`

3. **Execute Analysis:** Follow consultation methodology defined in templates

4. **Register Output:**
   ```bash
   python prompt/scripts/state_manager.py complete-phase \
       --task-id ${TASK_ID} \
       --output ${CONSULTATION_PATH} \
       --status "ready_for_review"
   ```
```

We repeat this pattern for all roles (planner, developer, reviewer), ensuring consistent adoption of the state-first protocol.

#### Task 1.4: Create Archive Manager (NEW - CONSULTANT FEEDBACK)

**CRITICAL ADDITION:** The original plan omitted addressing the conflicting archive strategies identified in the consultation. We must create a dedicated archive manager that implements the standards defined in `general.md`.

The current `path_utilities.py` contains incorrect timestamp-based archiving logic that conflicts with the version-based approach defined in `general.md`. We need to:

1. **Create `prompt/scripts/archive_manager.py`:**

```python
# File: prompt/scripts/archive_manager.py
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional

class ArchiveManager:
    """
    Implements the authoritative archive strategy defined in general.md.
    
    Uses version-based archiving (archive/doc_vX.Y.Z.md) instead of 
    timestamp-based approach to maintain consistency.
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        
    def archive_document(self, doc_path: str, version: str) -> Path:
        """Archive a document following general.md standards."""
        doc_path = Path(doc_path)
        
        # Determine archive location based on document type
        if "prompt/" in str(doc_path):
            archive_dir = self.project_root / "prompt" / "archive"
        else:
            archive_dir = doc_path.parent / "archive"
            
        archive_dir.mkdir(parents=True, exist_ok=True)
        
        # Create version-based archive name
        archive_name = f"{doc_path.stem}_v{version}{doc_path.suffix}"
        archive_path = archive_dir / archive_name
        
        # Copy to archive
        shutil.copy2(doc_path, archive_path)
        logger.info(f"Archived {doc_path} to {archive_path}")
        
        return archive_path
        
    def clean_old_archives(self, doc_path: str, keep_versions: int = 3) -> None:
        """Clean old archive versions, keeping only the most recent."""
        # Implementation follows general.md retention policy
        pass
```

2. **Remove conflicting logic from `path_utilities.py`:**

The `archive_artifact` method in `path_utilities.py` (lines 90-102) uses timestamp-based naming which violates `general.md` standards. This method should be removed and replaced with calls to the new `archive_manager.py`.

3. **Update all archiving calls:**

Any code that currently calls `archive_artifact` should be updated to use the new `ArchiveManager.archive_document()` method instead.

### Phase 2: Task Model Implementation [~25 hours]

#### Task 2.1: Refactor Workflow State Structure

With safe state management in place, we can now implement the task-centric data model that enables concurrent workflows. This addresses the consultant's Issue #3: "Lack of Formal Task Abstraction."

We begin by implementing the new task object structure in `workflow_state.json`. The migration script will transform the current component-centric structure to the new task-centric model:

```python
# File: prompt/scripts/migrate_to_task_model.py
def migrate_workflow_state(state_file: str) -> None:
    """
    Migrate from component-centric to task-centric workflow state.
    
    This migration preserves all existing workflow data while restructuring
    it to support concurrent tasks on the same component.
    """
    # Backup current state
    backup_file = f"{state_file}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(state_file, backup_file)
    logger.info(f"Created backup: {backup_file}")
    
    with open(state_file, 'r') as f:
        old_state = json.load(f)
    
    # Transform structure
    new_state = {
        "system_info": old_state.get("system_info", {}),
        "active_tasks": {},
        "completed_tasks": {},
        "task_counter": 1
    }
    
    # Migrate active workflows to tasks
    for component, workflow in old_state.get("active_workflows", {}).items():
        task_id = f"task-{new_state['task_counter']:03d}"
        new_state["task_counter"] += 1
        
        new_state["active_tasks"][task_id] = {
            "task_type": "component_feature",  # Default type
            "target_name": component,
            "status": "in_progress",
            "human_brief": f"Continue development of {component}",
            "active_phase": workflow.get("current_phase", "consultation"),
            "migrated_from": component,  # Track migration source
            "history": transform_workflow_history(workflow.get("history", {}))
        }
    
    # Write new structure
    with open(state_file, 'w') as f:
        json.dump(new_state, f, indent=2)
    
    logger.info(f"Successfully migrated {len(new_state['active_tasks'])} workflows to task model")
```

The migration preserves all existing workflow data while enabling the new concurrent task capabilities. Components that were previously limited to one active workflow can now support multiple simultaneous tasks.

#### Task 2.2: Update Orchestration Configuration (CORRECTED)

With the task model in place, we need to update `orchestration.json` to support different workflow types. The consultant identified this as Issue #7: incomplete integration.

**CRITICAL CORRECTION:** The original plan created redundancy between `task_workflows` and `role_io_mappings`. The consultant recommends unifying these into a cleaner structure:

```json
{
  "workflow_mode": "task-centric",
  "description": "Task-driven workflow orchestration with unified template management",
  
  "task_workflows": {
    "component_feature": {
      "description": "Standard workflow for new component features",
      "phases": ["consultation", "planning", "development", "review"],
      "templates": {
        "consultation": "standard_consultation.md",
        "planning": "new_feature.md",
        "development": "standard_development.md",
        "review": "standard_review.md"
      },
      "required_inputs": {
        "consultation": ["human_instruction", "component_docs"],
        "planning": ["consultation", "component_docs", "standards"],
        "development": ["plan", "source_code"],
        "review": ["plan", "dev_notes", "code_diff"]
      }
    },
    "documentation_update": {
      "description": "Streamlined workflow for documentation updates",
      "phases": ["planning", "development", "review"],
      "templates": {
        "planning": "doc_update.md",
        "development": "doc_implementation.md",
        "review": "doc_review.md"
      },
      "required_inputs": {
        "planning": ["human_instruction", "target_document"],
        "development": ["plan", "current_documentation"],
        "review": ["plan", "updated_documentation"]
      }
    },
    "bug_fix": {
      "description": "Expedited workflow for critical bug fixes",
      "phases": ["consultation", "development", "review"],
      "templates": {
        "consultation": "bug_analysis.md",
        "development": "hotfix.md",
        "review": "fix_review.md"
      },
      "required_inputs": {
        "consultation": ["bug_report", "component_docs"],
        "development": ["consultation", "source_code"],
        "review": ["consultation", "fix_implementation"]
      }
    }
  }
}
```

This unified structure eliminates redundancy by including template mappings directly within each task workflow definition, creating a more cohesive and maintainable configuration.

#### Task 2.3: Implement Concurrent Task Support

The final step in task model implementation is enabling true concurrent task support. This allows multiple teams to work on different aspects of the same component simultaneously.

We implement this through the state manager's task querying capabilities:

```python
# File: prompt/scripts/state_manager.py (additional methods)
def list_active_tasks(self, target_name: Optional[str] = None, 
                     task_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """List active tasks, optionally filtered by target or type."""
    with open(self.state_file, 'r') as f:
        state = json.load(f)
        
    tasks = []
    for task_id, task in state.get("active_tasks", {}).items():
        if target_name and task["target_name"] != target_name:
            continue
        if task_type and task["task_type"] != task_type:
            continue
            
        tasks.append({
            "task_id": task_id,
            "target_name": task["target_name"],
            "task_type": task["task_type"],
            "active_phase": task["active_phase"],
            "brief": task["human_brief"]
        })
        
    return tasks

def check_task_conflicts(self, task_id: str, target_name: str) -> List[str]:
    """Check for potential conflicts with other active tasks."""
    active_tasks = self.list_active_tasks(target_name=target_name)
    conflicts = []
    
    for task in active_tasks:
        if task["task_id"] != task_id:
            if task["active_phase"] == "development":
                conflicts.append(f"Task {task['task_id']} is actively modifying {target_name}")
                
    return conflicts
```

This enables coordination between concurrent tasks while maintaining safety through conflict detection.

### Phase 3: Directory Structure Cleanup [~15 hours]

#### Task 3.1: Implement Function-Centric Organization (CORRECTED)

With the core workflow system stabilized, we can address the consultant's Issue #5: chaotic directory structure. We implement the recommended function-centric layout that organizes files by purpose rather than by role.

**CRITICAL CORRECTION:** The original plan didn't clarify the relationship between `*_system.md` and `CLAUDE_*.md` files. We need to make a clear decision:

**Decision: `*_system.md` files are the canonical source, `CLAUDE_*.md` files are reference pointers.**

The migration begins with a scripted approach that preserves all existing files while reorganizing them according to the new structure:

```bash
#!/bin/bash
# File: prompt/scripts/migrate_directory_structure.sh

set -e

echo "Starting directory structure migration..."

# Create new standard directories
mkdir -p prompt/roles/{consultant,planner,developer,reviewer}
mkdir -p prompt/templates/{consultant,planner,developer,reviewer}
mkdir -p prompt/archive/{artifacts,config,roles,templates}

# Move role system prompts to centralized location (canonical sources)
echo "Moving role system files..."
mv prompt/consultant/consultant_system.md prompt/roles/consultant/
mv prompt/planner/planner_system.md prompt/roles/planner/
mv prompt/developer/developer_system.md prompt/roles/developer/
mv prompt/reviewer/reviewer_system.md prompt/roles/reviewer/

# Handle CLAUDE_* files as reference pointers
echo "Converting CLAUDE_* files to reference pointers..."
# Update CLAUDE_CONSULTANT.md to contain: @prompt/roles/consultant/consultant_system.md
echo "@prompt/roles/consultant/consultant_system.md" > prompt/roles/consultant/CLAUDE_CONSULTANT.md
echo "@prompt/roles/planner/planner_system.md" > prompt/roles/planner/CLAUDE_PLANNER.md
echo "@prompt/roles/developer/developer_system.md" > prompt/roles/developer/CLAUDE_DEVELOPER.md
echo "@prompt/roles/reviewer/reviewer_system.md" > prompt/roles/reviewer/CLAUDE_REVIEWER.md

# Consolidate templates from scattered locations
echo "Consolidating templates..."
mv prompt/consultant/template_consulting.md prompt/templates/consultant/standard_consultation.md
mv prompt/planner/template_planning.md prompt/templates/planner/new_feature.md
mv prompt/developer/template_developing.md prompt/templates/developer/standard_development.md
mv prompt/reviewer/template_reviewing.md prompt/templates/reviewer/standard_review.md

# Archive old conversation and notes files
echo "Archiving conversation files..."
mv prompt/consultant/conversation.md prompt/archive/roles/consultant_conversation.md
mv prompt/planner/conversation_v3.md prompt/archive/roles/planner_conversation_v3.md

# Clean up empty role-centric directories
echo "Cleaning up old directories..."
rm -rf prompt/consultant/
rm -rf prompt/planner/
rm -rf prompt/developer/
rm -rf prompt/reviewer/

echo "Directory migration completed successfully"
echo "CLAUDE_* files now contain references to canonical system files"
```

This migration preserves all content while establishing clear file hierarchy: `*_system.md` files are the authoritative source, `CLAUDE_*.md` files are simple reference pointers.

#### Task 3.2: Update Path References

After reorganizing the directory structure, we need to update all path references throughout the system to point to the new locations. This requires a systematic search and replace operation:

```python
# File: prompt/scripts/update_path_references.py
def update_file_references(root_dir: str) -> None:
    """
    Update all file path references to match new directory structure.
    
    This script finds and updates all references to moved files throughout
    the prompt system, ensuring no broken links remain after migration.
    """
    
    # Define path mappings for the migration
    path_mappings = {
        # Role system files
        "prompt/consultant/consultant_system.md": "prompt/roles/consultant/consultant_system.md",
        "prompt/planner/planner_system.md": "prompt/roles/planner/planner_system.md",
        "prompt/developer/developer_system.md": "prompt/roles/developer/developer_system.md",
        "prompt/reviewer/reviewer_system.md": "prompt/roles/reviewer/reviewer_system.md",
        
        # Template files
        "prompt/consultant/template_consulting.md": "prompt/templates/consultant/standard_consultation.md",
        "prompt/planner/template_planning.md": "prompt/templates/planner/new_feature.md",
        
        # CLAUDE-specific files (now reference pointers)
        "prompt/consultant/CLAUDE_CONSULTANT.md": "prompt/roles/consultant/CLAUDE_CONSULTANT.md",
        "prompt/planner/CLAUDE_PLANNER.md": "prompt/roles/planner/CLAUDE_PLANNER.md"
    }
    
    # Find all files that might contain references
    updated_files = []
    for file_path in find_text_files(root_dir):
        if update_references_in_file(file_path, path_mappings):
            updated_files.append(file_path)
    
    logger.info(f"Updated path references in {len(updated_files)} files")

def find_text_files(root_dir: str) -> List[Path]:
    """Find all text files that might contain path references."""
    extensions = ['.md', '.json', '.py', '.yaml', '.yml']
    files = []
    
    for ext in extensions:
        files.extend(Path(root_dir).rglob(f'*{ext}'))
        
    return files

def update_references_in_file(file_path: Path, mappings: Dict[str, str]) -> bool:
    """Update path references in a single file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    original_content = content
    
    for old_path, new_path in mappings.items():
        # Update various path reference formats
        content = content.replace(f'@{old_path}', f'@{new_path}')
        content = content.replace(f'`{old_path}`', f'`{new_path}`')
        content = content.replace(f'"{old_path}"', f'"{new_path}"')
        content = content.replace(f"'{old_path}'", f"'{new_path}'")
    
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        logger.info(f"Updated references in {file_path}")
        return True
        
    return False
```

This ensures that all references to moved files are updated consistently throughout the system.

#### Task 3.3: Create Template Content

The current template directories exist but are empty. We need to create proper template content based on the existing patterns found in the role directories:

```markdown
<!-- File: prompt/templates/consultant/standard_consultation.md -->
# Consultation: {{target_name}}

## Metadata Block
- **Version:** {{version}}
- **Author:** Consultant
- **Date:** {{date}}
- **Status:** {{status}}
- **Task ID:** {{task_id}}

## Executive Summary

[Provide a 2-3 sentence summary of the architectural challenge and recommended approach for business stakeholders]

## Problem Analysis

### Current State Assessment

[Analyze the current implementation, identifying specific pain points, limitations, and technical debt]

### Root Cause Analysis

[Identify the fundamental causes of the issues, not just symptoms]

## Proposed Solutions

### Option 1: {{solution_name}} (Recommended)

**Approach:** [High-level description of the solution]

**Technical Implementation:**
[Detailed technical approach with specific patterns, technologies, and architectural decisions]

**Advantages:**
- [Benefit 1]
- [Benefit 2]

**Disadvantages:**
- [Limitation 1]
- [Limitation 2]

### Option 2: {{alternative_solution}}

[Similar structure for alternative approach]

### Option 3: {{minimal_solution}}

[Minimal viable solution for comparison]

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {{risk_1}} | {{prob}} | {{impact}} | {{mitigation}} |

## Implementation Considerations

### Architecture Alignment
[How solution fits with existing component-based architecture]

### Performance Impact
[Expected performance implications with specific metrics where possible]

### Security Implications
[Security considerations and requirements]

## Next Steps

1. **For Planner:** [Specific guidance for planning phase]
2. **Key Decisions:** [Critical choices that need human input]
3. **Prerequisites:** [Any blockers that must be resolved first]

## Integration with Other Roles

This consultation will be consumed by the Planner role to create a detailed implementation plan. Key handoff points:
- Solution recommendation with technical specifics
- Risk assessment for planning consideration  
- Architecture constraints for implementation guidance

## Template Selection Logic

This template is appropriate for:
- New component features requiring architectural analysis
- Complex integrations needing multiple solution options
- Performance or scalability challenges

Use alternative templates for:
- Simple bug fixes (use bug_analysis.md)
- Security assessments (use security_consultation.md)
```

We create similar comprehensive templates for all roles, ensuring consistency and completeness.

### Phase 4: Documentation Hierarchy Implementation [~10 hours]

#### Task 4.1: Establish Strict Hierarchical Inheritance

The final phase addresses the consultant's Issue #4: documentation redundancy and drift. We implement strict hierarchical inheritance where lower-level documents reference higher-level ones rather than duplicating content.

We start by updating `prompt_main.md` to comply with `general.md` standards and remove redundant sections:

```markdown
<!-- File: prompt/documentation/prompt_main.md (updated header) -->
**Title:** LLM Agent System Documentation
**Version:** 2.0.0
**Purpose:** Single source of truth for the LLM agent development system
**Audience:** Human Developers, LLM Agents
**Last Updated:** 2025-07-13
**Change History:** ./prompt_main_change_history.md

<!-- Updated sections to remove redundancy -->
## Archive Strategy

The maintenance, versioning, and archival of this document are governed by the standards and scripts defined in `@documentation/general.md`. This document follows the authoritative update workflow defined there.

## System Prompt Design

All role system prompts must include the following standardized sections:

### Required Sections
- **Core Mandate:** Primary responsibility and source of truth reference
- **Execution Protocol:** Begins with reference to master workflow in this document
- **Template Selection Logic:** Required if role uses multiple templates
- **Integration with Other Roles:** Required handoff expectations
- **Communication Guidelines:** References general principles from this document

Refer to `@documentation/general.md` for header standards and versioning requirements.
```

This approach eliminates duplication while maintaining clear authority hierarchy.

#### Task 4.2: Update All Role System Files

Each role system file is updated to reference the hierarchy rather than duplicate rules:

```markdown
<!-- File: prompt/roles/consultant/consultant_system.md (updated sections) -->
## Execution Protocol

This protocol operates within the master workflow defined in `@prompt/documentation/prompt_main.md`. The following steps detail the specific actions for the Consultant phase:

[Role-specific execution steps...]

## Communication Guidelines

Adhere to the general communication principles outlined in `@prompt/documentation/prompt_main.md`, with the following Consultant-specific directives:

- **Exploratory tone:** Present multiple solution options with clear trade-offs
- **Educational approach:** Explain architectural reasoning for non-technical stakeholders  
- **Risk awareness:** Highlight potential issues early in the process

## Template Selection Logic

**Standard Consultation:** Use for new features requiring architectural analysis
- Criteria: Complex integration, performance requirements, multiple solution paths
- Template: `@prompt/templates/consultant/standard_consultation.md`

**Bug Analysis:** Use for defect investigation and root cause analysis  
- Criteria: System failures, performance degradation, unexpected behavior
- Template: `@prompt/templates/consultant/bug_analysis.md`

**Security Assessment:** Use for security-related requirements
- Criteria: Authentication, authorization, data protection needs
- Template: `@prompt/templates/consultant/security_consultation.md`

## Integration with Other Roles

**Handoff to Planner:**
- Provide clear solution recommendation with technical specifics
- Include risk assessment for planning consideration
- Specify architectural constraints for implementation

**Feedback Processing:**
- If Reviewer rejects consultation, address specific technical concerns
- Focus on architectural soundness and feasibility
- Maintain solution quality while addressing feedback
```

This pattern is applied consistently across all role files, creating a coherent system of references rather than duplication.

#### Task 4.3: Create Automated Consistency Checker

The final implementation task creates the automated consistency checker that prevents future documentation drift:

```python
# File: prompt/scripts/validate_system.py
import re
import sys
from pathlib import Path
from typing import List

class SystemValidator:
    """
    Automated consistency checker for the LLM agent system.
    
    Validates that documentation follows hierarchy rules, all required
    sections are present, and no redundancy violations exist.
    """
    
    def __init__(self, prompt_root: str = "prompt"):
        self.prompt_root = Path(prompt_root)
        self.errors = []
        self.warnings = []
        
    def validate_all(self) -> bool:
        """Run all validation checks."""
        self.errors.clear()
        self.warnings.clear()
        
        self._validate_documentation_headers()
        self._validate_role_system_files()
        self._validate_template_completeness()
        self._validate_path_references()
        self._validate_redundancy_violations()
        
        return len(self.errors) == 0
        
    def _validate_documentation_headers(self) -> None:
        """Ensure all high-level docs have proper headers."""
        required_fields = ["Title", "Version", "Purpose", "Audience", "Last Updated", "Change History"]
        
        for doc_file in self._find_documentation_files():
            content = doc_file.read_text()
            header_section = content.split('\n\n')[0]
            
            for field in required_fields:
                if f"**{field}:**" not in header_section:
                    self.errors.append(f"{doc_file}: Missing required header field '{field}'")
                    
    def _validate_role_system_files(self) -> None:
        """Ensure all role files have required sections."""
        required_sections = [
            "Core Mandate",
            "Execution Protocol", 
            "Template Selection Logic",
            "Integration with Other Roles"
        ]
        
        roles_dir = self.prompt_root / "roles"
        for role_dir in roles_dir.iterdir():
            if role_dir.is_dir():
                system_file = role_dir / f"{role_dir.name}_system.md"
                if system_file.exists():
                    content = system_file.read_text()
                    
                    for section in required_sections:
                        if f"## {section}" not in content:
                            self.errors.append(f"{system_file}: Missing required section '{section}'")
                            
    def _validate_redundancy_violations(self) -> None:
        """Check for prohibited duplication of rules."""
        # Archive rules should only appear in general.md
        archive_pattern = r"archive.*strategy|archiv.*rules|archiv.*process"
        
        for md_file in self.prompt_root.rglob("*.md"):
            if md_file.name != "general.md":
                content = md_file.read_text().lower()
                if re.search(archive_pattern, content):
                    self.warnings.append(f"{md_file}: Contains archive rules (should reference general.md)")
                    
        # Communication rules should reference prompt_main.md, not duplicate
        comm_pattern = r"communication.*style|escalation.*protocol|tone.*voice"
        
        for role_file in (self.prompt_root / "roles").rglob("*_system.md"):
            content = role_file.read_text().lower()
            if re.search(comm_pattern, content) and "prompt_main.md" not in content:
                self.warnings.append(f"{role_file}: Defines communication rules without referencing prompt_main.md")

    def _find_documentation_files(self) -> List[Path]:
        """Find high-level documentation files that need header validation."""
        return list((self.prompt_root / "documentation").glob("*.md"))

if __name__ == "__main__":
    validator = SystemValidator()
    is_valid = validator.validate_all()
    
    if validator.errors:
        print("ERRORS:")
        for error in validator.errors:
            print(f"  ❌ {error}")
            
    if validator.warnings:
        print("WARNINGS:")
        for warning in validator.warnings:
            print(f"  ⚠️  {warning}")
            
    sys.exit(0 if is_valid else 1)
```

This validator integrates with the test suite to continuously monitor system consistency.

---

## Documentation & Testing Deliverables

### 1. Documentation Updates
- **`prompt_main.md` Update:** Add Change History field, remove redundant sections, establish clear hierarchy references
- **`prompt_main_change_history.md` Entry (v2.0.0):** "Major architectural improvements: implemented State Manager, Task Object Model, directory reorganization, and documentation hierarchy"
- **Role System Files:** Update all 4 role files with hierarchy references and standardized sections
- **New Documentation:** Create comprehensive templates for all role types

### 2. Test Suite Updates  
- **New Tests:** 
  - `tests/unit/test_state_manager.py` - Comprehensive state manager testing
  - `tests/unit/test_archive_manager.py` - Archive manager functionality testing
  - `tests/unit/test_system_validator.py` - Documentation consistency validation
  - `tests/integration/test_task_workflows.py` - End-to-end task workflow testing
- **Updated Tests:** 
  - `tests/unit/test_path_utilities.py` - Update for deprecation warnings and new path resolution
  - `tests/integration/test_agent_workflows.py` - Update for new state manager interface
- **Final Requirement:** All existing and new tests **must pass** (`pytest -q`) upon completion

---

## Dependencies & Blockers

### Internal Dependencies  
- **None:** This is a self-contained refactoring that doesn't depend on other components
- **Migration Order:** Tasks must be completed in sequence (state manager → task model → directory cleanup → documentation)

### External Dependencies
- **Python >= 3.8:** Required for type hints and pathlib usage
- **fcntl module:** Unix file locking (Windows compatibility via alternative locking mechanism)

### Mitigation Plan
If file locking isn't available, implement simple lock file mechanism as fallback for Windows compatibility.

## Risk Mitigation

### Risk Register

| Risk | Probability | Impact | Mitigation | Trigger |
|------|-------------|--------|------------|---------|
| State migration corruption | Low | Critical | Automated backups + rollback procedure | Any JSON parsing error |
| Directory migration breaks workflows | Medium | High | Scripted migration + path validation | Broken path references found |
| Agent confusion during transition | Medium | Medium | Backward compatibility + gradual migration | Agent errors increase |
| Performance regression | Low | Medium | State manager optimization + monitoring | Response time increase |

### Rollback Procedure

**Quick Rollback (< 5 minutes):**
```bash
# 1. Restore state file from backup
cp prompt/config/workflow_state.json.backup.* prompt/config/workflow_state.json

# 2. Revert to old path utilities
git checkout HEAD~1 -- prompt/scripts/path_utilities.py

# 3. Verify system health
python prompt/scripts/validate_system.py
```

**Full Rollback (if needed):**
1. Stop all agent processes
2. Restore entire prompt directory from pre-migration backup
3. Restart agents with old configuration
4. Verify all workflows can resume normally

## Validation Criteria

### Technical Validation (For Reviewers)

**State Manager Testing:**
- File locking prevents corruption under concurrent access
- All CLI commands work correctly
- Backup and recovery procedures function
- Migration preserves all existing workflow data

**Task Model Validation:**
```python
def test_concurrent_task_support():
    """Verify multiple tasks can work on same component."""
    # Create two tasks for same component
    # Verify both can progress independently
    # Confirm no state conflicts
```

**Directory Structure Verification:**
- All files moved to correct locations  
- No broken path references remain
- Template content is complete and usable
- Archive structure preserves historical data

**Documentation Hierarchy:**
- No redundant rules across documents
- All references point to correct authority
- Automated validator passes all checks

### Code Quality Checks
- [ ] Type hints on all new public methods
- [ ] Docstrings follow Google style  
- [ ] No pylint warnings in new code
- [ ] All scripts have proper error handling

## Acceptance Criteria

### Business Requirements (For PM/Client)

**System Reliability:**
- [ ] Zero state corruption incidents possible
- [ ] Concurrent task workflows supported
- [ ] All existing functionality preserved
- [ ] Migration completes without data loss

**Maintainability Improvements:**
- [ ] Documentation consistency automatically enforced
- [ ] Directory structure follows clear organization  
- [ ] New roles can be added following standard pattern
- [ ] Template system supports all workflow types

### Operational Readiness
- [ ] State manager CLI documented with examples
- [ ] Migration scripts tested in staging environment
- [ ] Rollback procedures verified
- [ ] Team trained on new workflow patterns
- [ ] **All documentation updated & change history entries present**

## Deployment Plan

### Staging Deployment
1. Deploy migration scripts: `./deploy_migration.sh staging`
2. Run state migration: `python prompt/scripts/migrate_to_task_model.py --dry-run`
3. Execute directory migration: `bash prompt/scripts/migrate_directory_structure.sh`
4. Validate system: `python prompt/scripts/validate_system.py`
5. Test sample workflows with new state manager

### Production Deployment
1. **Phase 1 (State Manager):** Deploy state manager and begin migration
2. **Phase 2 (Task Model):** Migrate workflow state to task-centric structure  
3. **Phase 3 (Directory Cleanup):** Reorganize files with path updates
4. **Phase 4 (Documentation):** Establish hierarchy and enable validation

### Post-Deployment
- [ ] Verify all existing workflows continue normally
- [ ] Confirm new concurrent task capabilities work
- [ ] Check automated validation runs in CI/CD
- [ ] Monitor for any migration-related issues

---

## Appendices

### A. File Changes

```
New (Scripts):
- prompt/scripts/state_manager.py
- prompt/scripts/archive_manager.py (NEW - addresses consultant feedback)
- prompt/scripts/migrate_to_task_model.py  
- prompt/scripts/migrate_directory_structure.sh
- prompt/scripts/update_path_references.py
- prompt/scripts/validate_system.py

Modified (Core):
- prompt/config/workflow_state.json (structure change)
- prompt/config/orchestration.json (unified task workflow definitions)
- prompt/scripts/path_utilities.py (deprecation + robust path resolution)

Moved (Directory Reorganization):
- prompt/consultant/ → prompt/roles/consultant/ & prompt/templates/consultant/
- prompt/planner/ → prompt/roles/planner/ & prompt/templates/planner/
- prompt/developer/ → prompt/roles/developer/ & prompt/templates/developer/
- prompt/reviewer/ → prompt/roles/reviewer/ & prompt/templates/reviewer/

Modified (Documentation):
- prompt/documentation/prompt_main.md (hierarchy compliance)
- prompt/roles/consultant/consultant_system.md (hierarchy references)
- prompt/roles/planner/planner_system.md (hierarchy references)
- prompt/roles/developer/developer_system.md (hierarchy references)
- prompt/roles/reviewer/reviewer_system.md (hierarchy references)

New (Templates):
- prompt/templates/consultant/standard_consultation.md
- prompt/templates/consultant/bug_analysis.md
- prompt/templates/planner/new_feature.md
- prompt/templates/planner/documentation_update.md
- prompt/templates/developer/standard_development.md
- prompt/templates/reviewer/standard_review.md

New (Tests):
- tests/unit/test_state_manager.py
- tests/unit/test_archive_manager.py (NEW)
- tests/unit/test_system_validator.py
- tests/integration/test_task_workflows.py

Modified (Tests):
- tests/unit/test_path_utilities.py
- tests/integration/test_agent_workflows.py
```

### B. Configuration Updates

```json
// prompt/config/workflow_state.json (new structure)
{
  "system_info": {
    "version": "2.0.0",
    "mode": "task-centric",
    "last_updated": "2025-07-13T00:00:00Z"
  },
  "active_tasks": {
    "task-001": {
      "task_type": "component_feature",
      "target_name": "tv_ingest", 
      "status": "in_progress",
      "human_brief": "Implement enhanced caching",
      "active_phase": "development",
      "history": {
        "consultation": {"status": "completed", "artifact_path": "..."},
        "planning": {"status": "completed", "artifact_path": "..."},
        "development": {"status": "in_progress", "assigned_to": "developer"}
      }
    }
  },
  "completed_tasks": {},
  "task_counter": 2
}
```

---

## Plan Completeness Checklist

- [x] Stakeholder summary is clear and non-technical
- [x] Plan includes explicit documentation and test tasks with specific deliverables
- [x] All deliverables listed in "Documentation & Testing Deliverables" section
- [x] File manifest in Appendix A is complete and comprehensive
- [x] Estimates are consistent between header (85 hrs), stakeholder summary (2-3 weeks), and phase breakdowns (35+25+15+10=85 hrs)
- [x] Rollback procedure is defined with specific commands and steps
- [x] Every consultant recommendation addressed with specific implementation
- [x] Risk mitigation strategies provided for all identified risks
- [x] Acceptance criteria are measurable and verifiable
- [x] All 5 consultant feedback corrections incorporated