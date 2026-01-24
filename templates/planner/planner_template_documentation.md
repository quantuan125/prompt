# Documentation Update Plan

**Version:** [X.Y.Z]
**Document Path:** [path/to/the/document.md]
**Author:** [LLM_Planner designation]
**Date:** [YYYY-MM-DD]
**Reason for Update:** [e.g., Implementing Consultant Feedback, Aligning with New Process, Client Request]

---

## 1. Executive Summary

### What We're Changing
[1-2 sentence plain language explanation of the change to the document.]

### Why It Matters
[The impact of this change, e.g., "To standardize our documentation workflow," "To clarify a critical process," "To fix outdated information."]

---

## 2. Analysis of Required Changes

### Source Interpretation
- **Source of Request:** [e.g., Consultant Note, Client Note, Internal Review]
- **Key Directives:**
  - [Directive 1 from notes, e.g., "Externalize the update workflow into a Python script."]
  - [Directive 2 from notes, e.g., "Define a 'Discovery Protocol' for the agent."]
  - [Directive 3 from notes, e.g., "Add governance fields like Owner and Status to the header."]

### Document Impact Assessment
- **Primary Document:** `[path/to/document.md]`
- **Associated Files:** `[path/to/_change_history.md]`
- **Structural Impact:** [e.g., "Major restructuring of Section 4," "Addition of a new header field," "No structural impact, just content correction."]

---

## 3. Implementation Plan for Documentation Update

This plan outlines the precise steps for the next agent to follow, adhering strictly to the process defined in `@documentation/general.md`.

### Step 1: Discovery & Variable Preparation

The implementing agent must first gather all necessary information by inspecting the target document and the request notes.

- **`DOC_PATH`**: `[path/to/the/document.md]`
- **`CURRENT_VERSION`**: [The agent will read this from the document's header, e.g., "2.0.0"]
- **`NEW_VERSION`**: [Planner's calculated next version, e.g., "2.1.0"]
- **`CHANGE_TYPE`**: [e.g., "Minor"]
- **`SUMMARY_TEXT`**: [Planner's one-line summary for the changelog, e.g., "Externalized update workflow to a central script."]

### Step 2: Execute Maintenance Script

The agent will execute the central script to handle archiving and change history updates. The content of the document itself is **not** modified by this script.

```bash
# Command to be executed:
python documentation/scripts/update_doc.py \
    --doc-path "[DOC_PATH from Step 1]" \
    --current-version "[CURRENT_VERSION from Step 1]" \
    --new-version "[NEW_VERSION from Step 1]" \
    --change-type "[CHANGE_TYPE from Step 1]" \
    --summary "[SUMMARY_TEXT from Step 1]"
```

### Step 3: Apply Content Changes

After the script completes successfully, the agent will modify the content of the target document (`[path/to/document.md]`) as follows:
- **Update the Header:** Change the `Version` and `Last Updated` fields to reflect the new state.
- **Modify Section 4:** Replace the existing workflow with the new "Discovery Protocol" and script execution steps.
- **Add Section X:** [Detail other specific content changes based on the source notes.]

---

## 4. Validation & Acceptance Criteria

### Technical Validation
- [ ] The `update_doc.py` script executes without errors.
- [ ] A new version of the document is correctly created in the `archive/` directory.
- [ ] The `_change_history.md` file is correctly updated with a new table row and a detailed entry at the top.
- [ ] The live document's header (`Version`, `Last Updated`) is correct.

### Content Validation
- [ ] All directives from the source notes have been implemented.
- [ ] The final document is free of formatting errors and typos.
- [ ] All links within the document are correct.

---

## 5. File Manifest

### Files to be Modified by this Plan:
- `[path/to/document.md]`
- `[path/to/_change_history.md]`

### Files to be Created by this Plan:
- `[path/to/archive/document_vX.Y.Z.md]` (Handled by the script)

