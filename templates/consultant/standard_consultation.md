# Consultant Notes: [High-Level Goal or Target]

## 1. Task Context & Executive Summary
### 1.1. Task Context
**Task ID:** [T001]
**Task Type:** [system_architecture/component_feature/documentation_update]
**Target:** [component_name]
**Artifact Type:** [Plan/Consultation/Development/Review]
**Version:** [X.Y.Z] 
**Author:** [LLM Role]
**Date:** [YYYY-MM-DD]
**Status:** [in_progress/ready_for_review/approved]
**Dependencies:** [List of prerequisite tasks or components]

### 1.2. Executive Summary
[A high-level summary for stakeholders. Start by stating the core business/technical goal. Briefly describe the major issues identified and the essence of the recommended solution path. 2-3 paragraphs max.]

### 1.3. Summary of Recommendations
[A scannable, bulleted list of the final recommendations for each identified issue. This gives reviewers a quick overview before the deep dive.]
- **For Issue #1 (e.g., Source of Truth Conflict):** Recommend **Approach 1A: The State-First Protocol**.
- **For Issue #2 (e.g., Unsafe State Management):** Recommend **Approach 2A: The Central State Manager Script**.
- **For Issue #3 (e.g., Lack of Task Abstraction):** Recommend **Approach 3B: The Formal Task Object Model**.

---

## 2. System-Wide Issues Analysis (The Diagnosis)

[This section is the heart of the analysis. It details the problems discovered, independent of the solutions.]

### Issue #1: [Clear, Descriptive Title of the Issue, e.g., "Source of Truth Conflict"]
- **Problem Statement:** [A concise description of the issue.]
- **Impact Analysis:** [What are the consequences of this issue? (e.g., "Leads to unpredictable agent behavior and potential data loss.")]
- **Root Cause:** [What underlying architectural flaw causes this problem? (e.g., "System relies on two conflicting authorities: the filesystem and the state file.")]
- **Affected Components:** `path_utilities.py`, `prompt_main.md`, Agent Execution Logic.

### Issue #2: [Clear, Descriptive Title of the Issue, e.g., "Unsafe and Brittle State Management"]
- **Problem Statement:** [...]
- **Impact Analysis:** [...]
- **Root Cause:** [...]
- **Affected Components:** [...]

*(...Continue for all identified issues...)*

---

## 3. Solution Design & Recommendations (The Prescription)

[This section proposes and evaluates solutions for each issue identified in Section 2.]

### For Issue #1: [Title of Issue #1]

#### ► Approach 1A: [Descriptive Name, e.g., "The State-First Protocol"]
- **Overview:** [High-level conceptual description.]
- **Implementation Steps:** 
    1.  [Clear, actionable step 1, e.g., "Deprecate and remove the `find_latest_artifact` function from `path_utilities.py`."]
    2.  [Clear, actionable step 2, e.g., "Introduce a new function `get_task_inputs(task_id)` to the `state_manager.py` script."]
    3.  [Clear, actionable step 3, e.g., "Refactor all agent `Execution Protocols` to call `get_task_inputs` as their first step."]
- **Implementation Example:** [Provide a concrete example that illustrates the core of the implementation. Use code blocks for code, JSON, YAML, or file structures.]
- **Advantages:** ✅ [Specific benefit]
- **Disadvantages:** ❌ [Specific drawback]

#### ► Approach 1B: [Descriptive Name, e.g., "Filesystem-Led with State Verification"]
- **Overview:** [...]
- **Implementation Steps:** [...]
- **Implementation Example:** [...]
- **Advantages:** ✅ [...]
- **Disadvantages:** ❌ [...]

#### ► Recommendation for Issue #1
- **Decision:** **Approach 1A: The State-First Protocol**
- **Rationale:** [Clear reasoning why this is the optimal choice, explicitly linking back to the problem statement and system goals.]

---

### For Issue #2: [Title of Issue #2]

#### ► Approach 2A: [Descriptive Name, e.g., "The Central State Manager Script"]
- ... (structure as above) ...

#### ► Approach 2B: [Descriptive Name, e.g., "The SQLite Database Model"]
- ... (structure as above) ...

#### ► Recommendation for Issue #2
- **Decision:** **Approach 2A: The Central State Manager Script**
- **Rationale:** [...]

*(...Continue for all identified issues...)*

---

## 4. Consolidated Implementation Plan

[This section synthesizes all the *recommended* solutions into a single, cohesive, and phased implementation plan.]

### 4.1. Prerequisites & Dependencies
- **Knowledge Prerequisites:** Team must understand [concepts].
- **Tooling Prerequisites:** Requires `pytest`, `python > 3.9`.
- **Task Dependencies:** This plan assumes completion of [other task ID if any].

### 4.2. Phased Rollout Strategy

**Phase 1: Foundational Refactoring (The Bedrock)**
- **Goal:** Implement the core architectural changes.
- **Tasks:**
    1.  **Implement State Manager:** Create `state_manager.py` (from Solution 2A).
    2.  **Redesign State Object:** Refactor `workflow_state.json` to use the Task Object Model (from Solution 3B).
    3.  **Deprecate Old Logic:** Remove `find_latest_artifact` from all scripts.
- **Deliverable:** A stable, state-driven core with a test suite.

**Phase 2: Structural & Documentation Cleanup**
- **Goal:** Align the system's structure and documentation with the new architecture.
- **Tasks:**
    1.  **Execute Directory Cleanup:** Implement the migration plan (from Solution 5).
    2.  **Refactor `prompt_main.md`:** Rewrite to v2.0.0 based on the new standards.
    3.  **Enforce Hierarchy:** Implement the DRY refactoring pass on all documents (from Solution 4 & 6).
- **Deliverable:** A clean, organized repository where all documentation is consistent and trustworthy.

**Phase 3: System Integration & Validation**
- **Goal:** Connect all components and validate end-to-end functionality.
- **Tasks:**
    1.  **Implement Orchestration Logic:** Refactor `orchestration.json` and the logic that reads it (from Solution 7).
    2.  **Define Feedback Loop:** Implement the Reviewer feedback loop in the state manager.
    3.  **Standardize Role Prompts:** Update all `[role]_system.md` files with the new required sections.
- **Deliverable:** A fully functional, integrated, and documented agentic system.

---

## 5. Global Risk Assessment & Mitigation

[A summary of the most significant risks from all proposed solutions.]

| Risk Category | Key Risk | Mitigation Plan |
| :--- | :--- | :--- |
| **Technical** | A bug in the new `state_manager.py` could halt the system. | Develop a comprehensive `pytest` suite for the script, covering all edge cases, and run it in a CI/CD pipeline. |
| **Process** | Agents may struggle to adapt to the new task-centric model. | Update all `[role]_system.md` prompts with explicit instructions and examples of the new workflow and CLI commands. |
| **Migration** | The one-time directory cleanup could break existing paths or tools. | Perform the migration on a separate branch, run a global search-and-replace for paths, and run all tests before merging. |

---

## 6. Validation & Success Metrics

The entire initiative will be considered a success when:

- **Stability:** The system can run 10 consecutive end-to-end tasks of varying types without state corruption or workflow stalls.
- **Maintainability:** A new `task_type` can be added to the system by modifying only `orchestration.json` and adding the relevant templates/prompts, with no changes to the core scripts.
- **Clarity:** A new developer can understand the agentic workflow by reading only `prompt_main.md` and the relevant `[role]_system.md` file.
- **Compliance:** The `validate_system.py` test suite passes with 100% success, confirming all documentation and prompts adhere to the new standards.