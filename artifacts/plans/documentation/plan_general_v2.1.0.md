# Documentation Update Plan

**Version:** 2.1.0
**Document Path:** documentation/general.md
**Author:** LLM_Planner
**Date:** 2025-07-11
**Reason for Update:** Implementing Consultant Feedback for Agent Discovery Protocol and Python Script Externalization

---

## 1. Executive Summary

### What We're Changing
Implementing an agent discovery protocol and externalizing the update workflow from inline shell commands to a central Python script in `general.md`.

### Why It Matters
This transforms `general.md` from a theoretical workflow to an operational one, making LLM agents more autonomous while improving maintainability and reducing token overhead by approximately 50%. The change addresses critical gaps between theoretical documentation and practical agent operation.

---

## 2. Analysis of Required Changes

### Source Interpretation
- **Source of Request:** Consultant Note - Critical Analysis of Agent Workflow Feasibility
- **Key Directives:**
  - **Directive 1:** Implement agent discovery protocol where agents derive context from filesystem inspection rather than external variable feeding
  - **Directive 2:** Externalize the update workflow into a Python script to reduce token overhead and improve maintainability
  - **Directive 3:** Add explicit `Change History` field to standardized header for machine-readable file relationships
  - **Directive 4:** Align with Python-based ecosystem consistency throughout the codebase

### Document Impact Assessment
- **Primary Document:** `documentation/general.md`
- **Associated Files:** `documentation/general_change_history.md`
- **Structural Impact:** Major restructuring of Section 4 (The Authoritative Update Workflow), addition of new header field, creation of external script infrastructure

---

## 3. Implementation Plan for Documentation Update

This plan outlines the precise steps for the next agent to follow, adhering strictly to the process defined in `@documentation/general.md`.

### Step 1: Discovery & Variable Preparation

The implementing agent must first gather all necessary information by inspecting the target document and the request notes.

- **`DOC_PATH`**: `documentation/general.md`
- **`CURRENT_VERSION`**: 2.0.0 (The agent will read this from the document's header)
- **`NEW_VERSION`**: 2.1.0 (Planner's calculated next version)
- **`CHANGE_TYPE`**: Minor (New non-breaking sections and workflow improvements)
- **`SUMMARY_TEXT`**: "Implemented agent discovery protocol and externalized update workflow to central Python script"

### Step 2: Create Central Python Script

Before executing maintenance script, the agent must first create the `documentation/scripts/update_doc.py` script as specified in the consultant notes:

**Key Script Features:**
- Argument parsing for all required variables (doc-path, current-version, new-version, change-type, summary)
- Archive function that creates versioned copies in archive/ directories
- Change history update function that maintains both table and detailed entries
- Robust error handling with proper exit codes
- Semantic versioning logic integration

### Step 3: Execute Maintenance Script

The agent will execute the central script to handle archiving and change history updates. The content of the document itself is **not** modified by this script.

```bash
# Command to be executed:
python documentation/scripts/update_doc.py \
    --doc-path "documentation/general.md" \
    --current-version "2.0.0" \
    --new-version "2.1.0" \
    --change-type "Minor" \
    --summary "Implemented agent discovery protocol and externalized update workflow to central Python script"
```

### Step 4: Apply Content Changes

After the script completes successfully, the agent will modify the content of the target document (`documentation/general.md`) as follows:

- **Update the Header:** Add `Change History` field and update `Version` and `Last Updated` fields to reflect v2.1.0
- **Replace Section 4:** Replace existing workflow with new "Agent Discovery Protocol" (5-step process) and script execution steps
- **Update Section 3.1:** Add `Change History` field requirement to standardized header block
- **Add Section 7:** Add reference to the central maintenance script
- **Update Quick Reference:** Remove verbose shell commands, replace with script execution examples

---

## 4. Validation & Acceptance Criteria

### Technical Validation
- [ ] The `update_doc.py` script executes without errors
- [ ] A new version of the document (general_v2.0.0.md) is correctly created in the `archive/` directory
- [ ] The `general_change_history.md` file is correctly updated with a new table row and detailed entry at the top
- [ ] The live document's header (`Version`, `Last Updated`, `Change History`) is correct
- [ ] Script directory structure (`documentation/scripts/`) is properly created

### Content Validation
- [ ] All directives from the consultant notes have been implemented
- [ ] Agent discovery protocol is clearly defined with 5 specific steps
- [ ] External script execution workflow is documented with proper command examples
- [ ] The final document maintains all existing functionality while adding new capabilities
- [ ] Documentation is approximately 50% more concise in the workflow sections
- [ ] All links within the document are correct and functional

### Compatibility Validation
- [ ] Changes maintain backward compatibility with existing governed documents
- [ ] Script works with existing file structure patterns
- [ ] No breaking changes to the established documentation standards

---

## 5. File Manifest

### Files to be Modified by this Plan:
- `documentation/general.md` (Version update: 2.0.0 → 2.1.0)
- `documentation/general_change_history.md` (New entry addition)

### Files to be Created by this Plan:
- `documentation/scripts/update_doc.py` (New central maintenance script)
- `documentation/scripts/` (New directory)
- `documentation/archive/general_v2.0.0.md` (Handled by the script)

### Dependencies:
- Python 3.x environment (already available in codebase)
- Existing archive/ and change history infrastructure (already in place)
- Pathlib library (Python standard library)

---

## 6. Risk Assessment & Mitigation

### Low Risk Items:
- **Script Creation:** Simple Python script with standard library dependencies
- **Documentation Update:** Non-breaking changes to existing structure
- **File System Operations:** Well-established patterns already in use

### Mitigation Strategies:
- **Backup Strategy:** The script itself creates archives before any modifications
- **Validation Steps:** Multiple checkpoints ensure each phase completes successfully
- **Rollback Procedure:** Archive versions provide immediate rollback capability
- **Testing:** Script can be tested independently before integration

---

## 7. Success Metrics

### Quantitative Measures:
- Token reduction of ~50% in workflow sections (from ~150 lines to ~75 lines)
- Script execution time under 2 seconds for typical documentation updates
- Zero errors in archive and change history operations

### Qualitative Measures:
- Agent can autonomously discover all required variables without external input
- Documentation maintains clarity while improving operational efficiency
- Script provides consistent, reliable automation for all future updates
- Enhanced maintainability through separation of concerns (documentation vs. execution)

---

## 8. Post-Implementation Notes

This plan represents a significant improvement in the operational capabilities of the documentation maintenance system. The consultant's feedback correctly identified the critical gap between theoretical workflows and practical agent operation. By implementing the discovery protocol and externalizing the script logic, we achieve:

1. **Enhanced Autonomy:** Agents become self-sufficient in variable discovery
2. **Improved Maintainability:** Central script eliminates duplication and versioning issues
3. **Better Performance:** Reduced token overhead improves processing efficiency
4. **Ecosystem Alignment:** Python-native solution matches existing codebase standards

The implementation should be straightforward given the existing infrastructure and follows established patterns already proven in the codebase.