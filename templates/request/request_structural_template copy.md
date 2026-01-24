---
task_id: '[TASK_ID]'
prefix_id: 'SPS-[TASK_ID]'
parent_task: '[PARENT_TASK_ID]' # Optional
task_type: '[system/component/documentation/testing]'
target: '[component_name/document_name]'
artifact_type: 'SPS'
version: '[X.Y.Z]'
author: '[LLM Role]'
date: '[YYYY-MM-DD]'
status: '[in_progress/ready_for_review/approved]'
dependencies: '[List of prerequisite tasks or components]'
decision_owner_role: '[DECISION_OWNER_ROLE]'
#SPECIFIC METADATA BLOCK
status: '[in_progress/ready_for_review/approved]'
priority: '[High/Medium/Low]' 
---

<!--TPG_V2.2.0-->
# CLIENT REQUEST: [Target] - [Task ID]

## I. EXECUTIVE SUMMARY

*[EXECUTIVE_SUMMARY]*
---

## II. TABLE OF CONTENTS
I. [Executive Summary](#i-executive-summary)
II. [Table of Contents](#ii-table-of-contents)
III. [Core Content](#iii-core-content)
   A. [Problem Framing & Validation](#a-problem-framing--validation)
      - [1. Key Points from Raw Request](#1-key-points-from-raw-request)
      - [2. Consultant's Initial Problem Statement](#2-consultants-initial-problem-statement)
      - [3. General Clarification Dialogue](#3-general-clarification-dialogue)
      - [4. Validated Problem Mandate](#4-validated-problem-mandate)
   B. [Problem Analysis & Research](#b-problem-analysis--research)
      - [1. Issue 1: [ISSUE_TITLE]](#1-issue-1-issue_title)
      - [2. Issue 2: [ISSUE_TITLE]](#2-issue-2-issue_title)
   C. [Issue Refinement Log](#c-issue-refinement-log)
      - [1. `REQ-[TASK_ID]-1`: [REFINEMENT_TITLE]](#1-req-task_id-1-refinement_title)
      - [2. `REQ-[TASK_ID]-2`: [REFINEMENT_TITLE]](#2-req-task_id-2-refinement_title)
   D. [Validated Problem Summary](#d-validated-problem-summary)
   E. [Global Solution Constraints](#e-global-solution-constraints)
      - [1. Non-Functional Requirements (NFRs)](#1-non-functional-requirements-nfrs)
      - [2. Scope Boundaries (What is explicitly "Out of Scope")](#2-scope-boundaries-what-is-explicitly-out-of-scope)
IV. [Glossary](#iv-glossary)
V. [Appendix](#v-appendix)
VI. [Validation Checklist](#vi-validation-checklist)
VII. [Stakeholder Sign-off](#vii-stakeholder-sign-off)
VIII. [Next Steps](#viii-next-steps)
IX. [Changelog](#ix-changelog)
---

## III. CORE CONTENT

### A. Problem Framing & Validation

#### 1. Key Points from Raw Request
**Source:** *[ARCHIVE_LINK]*

<details>
<summary>Key Points Summary</summary>

> *[KEY_POINTS_SUMMARY]*

</details>

#### 2. Consultant's Initial Problem Statement
*[PROBLEM_STATEMENT]*

#### 3. General Clarification Dialogue
<details>
<summary>Click to expand the initial clarification dialogue</summary>

1. **Question `[PENDING]`:** *[VALIDATION_QUESTION]*

2.  **Question `[RESOLVED]`:** *[RESOLVED_QUESTION]*
    *   **Client Answer:** *[CLIENT_ANSWER]*
    *   **Concise Summary:** *[ANSWER_SUMMARY]*

</details>
<!-- P1: General Clarification Dialogue Complete -->

#### 4. Validated Problem Mandate

**Final Agreed-Upon Problem:**
*[VALIDATED_MANDATE]*

---
**Gate A: Mandate Approval**
*   [ ] The `Validated Problem Mandate` above is approved by the client.
---

### B. Problem Analysis & Research


| `Req. ID`        | Title                      | Status*   |
|------------------|----------------------------|-----------|
| `REQ-[TASK_ID]-1`| Centralize File Paths      | PROCEED   |
| `REQ-[TASK_ID]-2`| *[ISSUE_TITLE]*            | SKIP      |
---

#### 1. Issue 1: *[ISSUE_TITLE]*

**Requirement ID:** `REQ-[TASK_ID]-1`
**Priority:** `[High / Medium / Low]`
**Business Rationale:** *[BUSINESS_RATIONALE]*
**Dependencies:** *[DEPENDENCIES]*
**Status:** `[Analysis / Refinement / Completed]`
🔗 **Full context:** [See refinement log for REQ-[TASK_ID]-1 »](#req-task_id-1-title-from-section-2)

**Analysis:**
*[ANALYSIS]*

**Assumptions & Constraints (Optional):**
*   *[ASSUMPTION]*
*   *[CONSTRAINT]*

**Research:**
<details>
<summary>Click to see detailed technical research</summary>

**1. Technical Context:**
- *[TECH_CONTEXT]*
- *[SYSTEM_DESCRIPTION]*

**2. Key Findings & Gaps:**
- *[KEY_FINDINGS]*
- *[TECHNICAL_DEBT]*

**3. Immediate Constraints & Dependencies:**
- *[TECH_LIMITATIONS]*
- *[ISSUE_DEPENDENCIES]*

</details>

**Assessment:** `[PROCEED / SKIP]` - *[ASSESSMENT_REASONING]*

#### 2. Issue 2: *[ISSUE_TITLE]*
---
*(Continue creating Issue Cards for all identified problems, incrementing the Requirement ID number.)*

---

### C. Issue Refinement Log

<!-- (all scaffolded blocks appear here) -->

---
**Gate B: Analysis & Research Approval**
*   [ ] All issues have been analyzed and assessed, and initial refinement questions have been scaffolded.
---

#### 1. `REQ-[TASK_ID]-1`: *[REFINEMENT_TITLE]*

##### i. Description 
*[ISSUE_DESCRIPTION]*

##### ii. Refinement Dialogue
1.  **Question `[PENDING]`:** *[REFINEMENT_QUESTION]*

2.  **Question `[RESOLVED]`:** *[RESOLVED_QUESTION]*
    *   **Client Answer:** *[CLIENT_ANSWER]*
    *   **Concise Summary:** *[ANSWER_SUMMARY]*
    *   **Consultant's Finding (Optional):** *[CONSULTANT_FINDING]*
<!-- P2: Refinement Dialogue Complete -->

##### iii. Acceptance Criteria
*   **Given** *[GIVEN_CONTEXT]*,
    **When** *[WHEN_ACTION]*,
    **Then** *[THEN_OUTCOME]*.
*   **And** *[AND_OUTCOME]*.
*   ↩ Relates-to: `REQ-[TASK_ID]-1`


##### iv. Refinement Summary
*[REFINEMENT_SUMMARY]*

#### 2. `REQ-[TASK_ID]-2`: *[REFINEMENT_TITLE]*

*(Repeat the refinement block for each issue marked "PROCEED".)*

---
**Gate C: Refinement Approval**
*   [ ] All `PROCEED` issues have been fully refined, with ACs defined and summaries written.
---

### D. VALIDATED PROBLEM SUMMARY

| `Req. ID` | Priority | Title | Description |
|-----------|----------|-------|-------------|
|`REQ-[TASK_ID]-1`| High | Centralize File Paths | The `prompt_main.md` document contains many hardcoded paths, making it difficult to maintain. |
| *[...] * | *[...] * | *[...] * | *[PROBLEM_SUMMARY]* |
<!-- P3: Validated Problem Summary completed -->

---

### E. Global Solution Constraints

#### 1. Non-Functional Requirements (NFRs)
*   **Performance:** *[PERFORMANCE_REQ]*
*   **Security:** *[SECURITY_REQ]*
*   **Regulatory / Compliance:** *[COMPLIANCE_REQ]*
*   **Usability:** *[USABILITY_REQ]*
*   **Maintainability:** *[MAINTAINABILITY_REQ]*

#### 2. Scope Boundaries (What is explicitly "Out of Scope")
*   *[SCOPE_BOUNDARIES]*

---
**Gate D: Global Constraints Approval**
*   [ ] The NFRs and Scope Boundaries have been collaboratively defined and approved.
---

## IV. GLOSSARY

*   **NFR (Non-Functional Requirement):** A quality standard for the system (like speed or security) rather than a specific feature.
*   **Acceptance Criteria:** A checklist of conditions that must be met for a requirement to be considered "done."

---

## V. APPENDIX 


### A. Amendment Log
| Date | Change Requester | Affected Req. ID | Summary of Change |
|------|------------------|------------------|-------------------|
| *[YYYY-MM-DD]* | *[Client Name]* | `REQ-[TASK_ID]-X` | *[AMENDMENT_SUMMARY]* |

---

## VI. VALIDATION CHECKLIST

- [ ] All issues from the raw request have been captured in Section II.
- [ ] The full ToC is generated.
- [ ] Every "PROCEED" issue has a completed Refinement Log in Section III.
- [ ] Acceptance Criteria are defined for every refined issue.
- [ ] All "PENDING" questions have been resolved and documented.
- [ ] The Validated Problem Summary table is complete and accurate.
- [ ] Stakeholder sign-off has been obtained.

---

## VII. STAKEHOLDER SIGN-OFF

By signing off, stakeholders agree that the problems and requirements detailed in this document accurately reflect the desired work. Architectural and implementation design will be based on the contents of this artifact.

*   **Client:** _________________________ (Name, Date)
*   **Consultant:** _________________________ (Name, Date)

---



## VIII. NEXT STEPS

**Recipient:** [Architect/Planner]

**Action:** Review this finalized request artifact. Use the **Validated Problem Summary** (Section V) as your checklist and the **Issue Refinement Logs** (Section III) for detailed context, constraints, and acceptance criteria to develop a comprehensive technical plan.

---

## IX. CHANGELOG

*   **v[X.Y.Z]_i1:** *[CHANGE_SUMMARY]*
*   **v[X.Y.Z]_i2:** *[CHANGE_SUMMARY]*


