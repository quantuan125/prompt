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

### A. Problem Frame & Decision Criteria  <!-- SAD-lite, moved from Concept §A -->
- **Problem statement:** (1–2 lines) → link SPS §III-A
- **Constraints (deltas only):** IDs referencing SPS Initiative Considerations
- **Success criteria:** measurable, singular
- **Decision criteria & weights:** (stable; used by downstream designs)
- **Option Register (catalog-only):**
  | Option ID | Title | Intent (1 line) | Links (ADR/Design) |
  |---|---|---|---|
- **Architecture snapshots (optional):**
  - C4 Context (ref to asset)
  - C4 Container (ref to asset)
- **Quality Attribute Scenarios (3–5):** (e.g., perf, reliability, security)

### B. Source & Scope
- In-scope / Out-of-scope
- Canonical references (SPS, other Requests)

### C. Business Objectives & Success Signals

### D. Stakeholders & Roles

### E. Assumptions & Dependencies

### F. Non-Functional Requirements (ISO 25010)
- NFR table with verification method

### G. Interfaces & Data Contracts
- External systems, schemas, protocols

### H. Constraints (legal, tech, operational)

### I. Feature Integration Notes

### K. Story Register (thin)
| Story ID | Title | FR IDs | Notes |
|---|---|---|---|

### L. Acceptance Criteria Register (Gherkin, per Story)
```gherkin
Story: <Story ID - Title>
  Scenario: <name>
    Given ...
    When ...
    Then ...
```

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


