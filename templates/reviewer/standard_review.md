# Technical Review: [Component Name]

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

---

## 1. Executive Verdict

- **Final Verdict:** [APPROVED / CONDITIONAL APPROVAL / REJECTED]
- **Compliance Score:** [X/10]*
- **Reason:** [A one-sentence summary explaining the verdict.]

_*Compliance Score is calculated as: 10 – (2 × # of Critical Issues + 1 × # of Major Issues), clamped at a minimum of 0._

---

## 2. Root Cause Analysis
*_[Analyze the relationship between the plan, the execution, and the outcome. Assign responsibility for any failures.]*_

- **Plan Quality:** [Assess if the plan was clear, complete, and achievable.]
- **Execution Fidelity:** [Assess if the developer followed the plan accurately by comparing the code diff to the plan's requirements.]
- **Reporting Accuracy:** [Assess if the dev notes accurately reflect the code diff and the work performed.]

---

## 3. Detailed Findings & Issues

### 3.1. Test-Suite Validation
- **Overall Status:** [PASSED / FAILED / PARTIAL]
- **Coverage Assessment:** [Briefly assess if new code is covered by meaningful tests.]
- **Key Findings:** [Note any flaky tests, missing edge cases, or significant failures.]

### 3.2. General Findings
*_[List all other identified issues, categorized by severity. Each finding must be backed by evidence.]*_

#### 🔴 CRITICAL ISSUES (Requires Escalation)
- **None.**

#### 🟡 MAJOR ISSUES (Requires Rework or New Plan)
1.  **[MAJOR] Short Title of Issue**
    - **Evidence:** `components/.../file.py` lines 123-140 (or commit hash)
    - **Plan Reference:** [e.g., Phase 2, Task 2.1 or a specific `Validation Criterion`]
    - **Impact:** [Describe the consequence of this issue.]
    - **Root Cause:** [Plan / Execution / Reporting]
    - **Recommendation:** [Provide a specific, actionable fix.]

#### 🟢 MINOR ISSUES (For Future Improvement)
- **None.**
---

## 4. Actionable Next Steps
*_[Provide clear, specific, and assigned tasks for the next agents in the workflow.]*_

### For the AI Consultant:
- **[CONSULTATION REQUIRED]** [Describe the new solutions to be created or issues that need to be address.]

### For the AI Planner:
- **[PLANNING REQUIRED]** [Describe the new plan that needs to be created.]

### For the AI Developer:
- **[REWORK REQUIRED]** [Describe the specific changes that need to be made to the code.]

### For the Human Overseer:
- **[ACTION REQUIRED]** [Describe any tasks that require human intervention.]