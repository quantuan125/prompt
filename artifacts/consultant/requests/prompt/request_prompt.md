# CLIENT'S REQUEST
**Version:** 2.0.0
**Component:** prompt  
**Author:** Client
**Date:** 2025-07-13
**Status:** Request

---
## Section 2: Directory Structure
Is this really the best structure?
```
prompt/
├── artifacts/           # All role outputs
│   ├── consultations/   # Consultant outputs
│   ├── plans/          # Planner outputs
│   ├── developments/   # Developer outputs
│   └── reviews/        # Reviewer outputs
├── config/             # System configuration (JSON)
│   ├── orchestration.json
│   ├── project_context.json
│   ├── shared_definitions.json
│   └── workflow_state.json
├── templates/          # Role-specific templates ONLY
│   ├── consultant/
│   ├── planner/
│   ├── developer/
│   └── reviewer/
├── [role_name]/        # Role system files
│   ├── [role]_system.md
│   ├── CLAUDE_[ROLE].md (if exists)
│   └── conversation.md
├── documentation/      # System documentation
├── scripts/           # Utility scripts
│   └── path_utilities.py  # Standard path resolution
└── archive/           # Historical versions
    ├── artifacts/
    ├── config/
    ├── roles/
    └── templates/
```

The current version we have is leveraging the fact each agent has their own path under <roles> and everything is inside it including their own notes, system file, templates files and archive all in one place. The proposed solution currently seesm like we need to repeat this pattern for each path:
```
│   ├── consultant/
│   ├── planner/
│   ├── developer/
│   └── reviewer/
```
---
## 3. Role Definitions
All of this section assume we are only dealing with developing components only wherease in reality we could also be dealing with developing documentation and developing tests for example. This will be specified by the human in the loop, but we do need a standardize framework to ensure that there is a chain of logics here where the consultant notes will define the type of task we are doing and the plan and the implementation and reviewing process must following accordingly. For now the human in the loop will specify the task as it communicate with the consultant and outlined in the first deliverable "Consultant's Notes" as to what task we are doing. 
---
## 4. File Management
This is fine but we need an actual reference to this script in here:
"""
### 4.3 Finding Latest Version
Each role uses this pattern to find the latest artifact:
```python
# Uses path_utilities.py
from scripts.path_utilities import find_latest_artifact
latest = find_latest_artifact(component, artifact_type)
```
"""
---
## 5. Workflow Process
This part is strange:
"""
5.2 Human Instructions Format
Each human instruction should include:
1. **Component name**: "for the tv_ingest component"
2. **Task context**: "implement the plan" or "review the implementation"
3. **Special requirements**: "focus on performance" (optional)
"""

The human usually gives instruction in the prompt however usually even without any instructions the agent can either ask for further clarification or automatically figure (through the inputs files). This section make it seems like the human HAS to give instruction with a specific format. 

We need proper file path reference here:
"""
### 5.3 State Tracking
""
---
## 6. Configuration Files
Similarly we need file path references in all subsections.
---
## 7. Template Design Guidelines
We need reference to all available templates here:
"""
### 7.3 Template Types
Each role maintains multiple templates:
- **Consultant**: standard, performance_analysis, security_assessment
- **Planner**: new_feature, bug_fix, refactor, performance_optimization
- **Developer**: standard_development, hotfix, phased_implementation
- **Reviewer**: standard_review, security_review, performance_review 
"""

which currently includes: template_consulting.md, template_planning.md, planner_template_documentation.md, template_reviewing.md, template_developing.md
---
## 8. System Prompt Design
This section does not mentioned any of the system files we have to match the 7.3 section on template types. These need to be reference directly in the documentation which include: reviewer_system.md, planner_system.md, developer_system.md, consultant_system.md.
---
## 9. Archive Strategy
This section seems to be specific, does this follow general.md yet or has a completely different logics? 
---
## 10. Communication Guidelines
This section seems to be inconflict with section '## 3. Role Definitions". Could we merge? Additionally these communication guidelines are outlined in the speicific templates inside the system prompt referenced in section 8. It does not make sense to outline these here in this document. If we changes something in one of the system prompt we would then have to changes it here in this main document? This overload the process of maintaing this document.
---
## 11. Implementation Guide
This section seems oddly specific to a speicific task (developing a completely new compoennt) and not general enough. It make sense to have for example "**Initialize in workflow_state.json**" after each tasks complete for example, however these need to be more generalized. 
Currently the system prompt outlined the specific workflows for each agent, which is to read the inputs, process in the puts (taking actions) and produce an outputs (usually according to a template) and then after this it can initialize/update the works flow for the speicfic task it is doing in this json file. 
---
## 13. Quick Reference
Not sure what htis is "Headers: TargetRole, Severity" in:
"""
**Reviewer**:
```
Input:
  - @prompt/artifacts/plans/[component]/plan_v[X.Y.Z].md
  - @prompt/artifacts/developments/[component]/devnotes_v[X.Y.Z].md
Output: @prompt/artifacts/reviews/[component]/review_v[X.Y.Z].md
Headers: TargetRole, Severity
```
"""
----
## 14. Change History
Shouldn't this section merged with section "## 12. Maintaining This Document". 
---