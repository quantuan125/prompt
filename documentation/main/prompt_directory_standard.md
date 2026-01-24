# LLM Agent System: Directory Structure Standards & Framework

## 1. Overview

This document defines the standard directory structure and file organization framework for the LLM Agent Development System. Following these standards ensures consistency, maintainability, and automation readiness.

## 2. Core Principles

### 2.1 Separation of Concerns
- **System files** (prompts, templates) separate from **outputs** (artifacts)
- **Configuration** centralized and versioned
- **Archives** consolidated in one location

### 2.2 Predictable Paths
- All paths follow deterministic patterns
- Automation can locate files without searching
- Version numbers embedded in filenames

### 2.3 Scalability First
- Easy to add new roles
- Simple to support new components
- Clear patterns for extension

## 3. Directory Structure

### 3.1 Root Structure
```
prompt/                    # System root
├── config/              # Central configuration
├── templates/           # Document templates  
├── archive/             # Historical artifacts
├── roles/                # Role definitions
├── artifacts/            # Work products
├── components/           # Component metadata
└── scripts/              # Automation tools
```

### 3.2 Special Directories (underscore prefix)

#### `config/` - Central Configuration
Houses all shared configuration files:
- `shared_definitions.yaml` - Enums, constants, patterns
- `project_context.yaml` - Architecture, standards
- `workflow_state.yaml` - Current execution state
- `orchestration.yaml` - Automation rules

#### `templates/` - Document Templates
All artifact templates in one location:
- Named by artifact type: `consultation.md`, `planning.md`, etc.
- Version controlled separately from outputs
- Single source of truth for structure

#### `archive/` - Historical Artifacts
Organized by date for easy cleanup:
```
_archive/
└── YYYY-MM/
    └── [timestamp]_[component]_[artifact_type]_v[X.Y.Z].md
```

### 3.3 Standard Directories

#### `roles/` - Role Definitions
Each role gets a subdirectory:
```
roles/
└── [role_name]/
    ├── system.md              # Generic system prompt
    ├── CLAUDE_[ROLE].md      # Claude-specific version
    └── conversation.md        # User interaction template
```

#### `artifacts/` - Work Products
Organized by type, then component:
```
artifacts/
└── [artifact_type]s/          # Note plural form
    └── [component_name]/
        └── [artifact_type]_v[X.Y.Z].md
```

#### `components/` - Component Metadata
Component-specific resources:
```
components/
└── [component_name]/
    ├── context.yaml           # Component description
    ├── dependencies.yaml      # Dependency graph
    └── history.yaml          # Version history
```

## 4. File Naming Standards

### 4.1 System Files
| File Type | Pattern | Example |
|-----------|---------|---------|
| System Prompt | `system.md` | `roles/planner/system.md` |
| Claude Version | `CLAUDE_[ROLE].md` | `CLAUDE_PLANNER.md` |
| Conversation | `conversation.md` | `roles/consultant/conversation.md` |
| Template | `[type].md` | `_templates/planning.md` |

### 4.2 Artifacts
| Artifact Type | Pattern | Example |
|---------------|---------|---------|
| Consultation | `consultation_v[X.Y.Z].md` | `consultation_v2.5.0.md` |
| Plan | `plan_v[X.Y.Z].md` | `plan.md` |
| Dev Notes | `devnotes_v[X.Y.Z].md` | `devnotes.md` |
| Review | `review_v[X.Y.Z].md` | `review.md` |
| Test Report | `test_report_v[X.Y.Z].md` | `test_report_v2.5.1.md` |

### 4.3 Version Numbering
Follow semantic versioning:
- **Major** (X.0.0): Breaking changes, major refactors
- **Minor** (0.Y.0): New features, non-breaking changes
- **Patch** (0.0.Z): Bug fixes, minor improvements

## 5. Path Resolution

### 5.1 Artifact Path Formula
```
prompt/artifacts/{artifact_type}s/{component}/{artifact_type}_v{version}.md
```

### 5.2 Role Path Formula
```
prompt/roles/{role_name}/{file_type}.md
```

### 5.3 Archive Path Formula
```
prompt/_archive/{YYYY-MM}/{timestamp}_{component}_{artifact_type}_v{version}.md
```

## 6. Configuration Files

### 6.1 shared_definitions.yaml
```yaml
# Enums and constants used across roles
statuses:
  - draft
  - in_progress
  - ready_for_review
  - completed
  - blocked

artifact_types:
  - consultation
  - plan
  - devnotes
  - review
  - test_report

roles:
  - consultant
  - planner
  - developer
  - reviewer
  - qa_engineer
  - product_owner
```

### 6.2 workflow_state.yaml
```yaml
# Current state of all active work
active_components:
  tv_ingest:
    current_phase: "development"
    current_version: "2.5.1"
    assigned_roles:
      planner: "planner_alpha"
      developer: "developer_beta"
    status: "in_progress"
    last_updated: "2024-01-07T10:30:00Z"
```

### 6.3 Component context.yaml
```yaml
# Component-specific metadata
component:
  name: "tv_ingest"
  description: "TradingView webhook ingestion system"
  owner: "trading_team"
  created: "2023-06-15"
  architecture:
    pattern: "service-facade"
    language: "python"
  interfaces:
    - "webhook_endpoint"
    - "data_export"
```

## 7. Automation Integration

### 7.1 Path Utilities
```python
class ArtifactPath:
    """Standard path resolution for artifacts"""
    
    @staticmethod
    def build(component: str, artifact_type: str, version: str) -> str:
        """Build standard artifact path"""
        return f"prompt/artifacts/{artifact_type}s/{component}/{artifact_type}_v{version}.md"
    
    @staticmethod
    def parse(path: str) -> dict:
        """Parse artifact path into components"""
        # Extract component, type, version from path
        pattern = r"artifacts/(\w+)s/(\w+)/(\w+)_v([\d.]+)\.md"
        match = re.match(pattern, path)
        return {
            "artifact_type": match.group(1),
            "component": match.group(2),
            "version": match.group(4)
        }
```

### 7.2 State Management
```python
class WorkflowState:
    """Manage workflow state across components"""
    
    def __init__(self):
        self.state_file = "prompt/_config/workflow_state.yaml"
        self.state = self.load_state()
    
    def update_component_status(self, component: str, status: str):
        """Update component status and save"""
        self.state["active_components"][component]["status"] = status
        self.state["active_components"][component]["last_updated"] = datetime.now().isoformat()
        self.save_state()
```

## 8. Migration Guide

### 8.1 From Old to New Structure
1. **Backup current structure**: `cp -r prompt prompt_backup`
2. **Run migration script**: `python scripts/migrate_structure.py`
3. **Verify artifacts**: `python scripts/validate_structure.py`
4. **Update automation**: Point scripts to new paths
5. **Archive old structure**: Move backup to `_archive/migration/`

### 8.2 Validation Checklist
- [ ] All templates in `_templates/`
- [ ] All artifacts in `artifacts/` with correct structure
- [ ] Each role has complete file set
- [ ] Configuration files valid YAML
- [ ] No artifacts in role directories
- [ ] Archive consolidated and organized

## 9. Best Practices

### 9.1 DO's
- ✅ Always use standard path utilities
- ✅ Version every artifact
- ✅ Keep templates separate from outputs
- ✅ Archive old versions promptly
- ✅ Update workflow state on changes

### 9.2 DON'Ts
- ❌ Don't create custom directory structures
- ❌ Don't mix artifacts with system files
- ❌ Don't skip version numbers
- ❌ Don't modify archived files
- ❌ Don't hardcode paths

## 10. Maintenance

### 10.1 Regular Tasks
- **Weekly**: Archive completed artifacts older than 30 days
- **Monthly**: Clean up `_archive/` folders older than 6 months
- **Quarterly**: Review and update templates
- **Annually**: Audit entire structure for consistency

### 10.2 Health Checks
```bash
# Validate structure
python scripts/validate_structure.py

# Check for orphaned artifacts
python scripts/find_orphans.py

# Generate structure report
python scripts/structure_report.py
```

## Appendix: Quick Reference

### Common Paths
```
# Get latest plan for component
prompt/artifacts/plans/tv_ingest/plan_v*.md

# Find all Claude prompts
prompt/roles/*/CLAUDE_*.md

# Locate component context
prompt/components/tv_ingest/context.yaml

# Access templates
prompt/_templates/*.md
```

### Path Variables
- `{component}` - Component name (e.g., "tv_ingest")
- `{role}` - Role name (e.g., "planner")
- `{artifact_type}` - Type singular (e.g., "plan")
- `{version}` - Semantic version (e.g., "2.5.1")

This framework ensures consistent, scalable, and automation-ready organization of the LLM Agent Development System.