---
task_id: 'T102'
prefix_id: 'SPS-T102'
parent_task: '' # Optional
task_type: 'system'
target: 'prompt_template_architecture'
artifact_type: 'SPS'
version: '1.0.0'
author: 'LLM Consultant (SPS Role)'
date: '2025-08-01'
status: 'ready_for_review'
dependencies: 'sps_structural_template.md, request_structural_template.md'
decision_owner_role: 'SYSTEM_ARCHITECT'
---

# SYNTHESIZED PROBLEM STATEMENT (SPS): Prompt Template Architecture - T102

## I. EXECUTIVE SUMMARY

This SPS addresses the foundational challenge of integrating the Synthesized Problem Statement (SPS) workflow with the Request Analysis workflow while preserving the philosophical distinction between external exploratory consultation and internal structured analysis. The problem emerged from the need to bypass Gate A in request templates when an approved SPS already exists, requiring architectural decisions that maintain workflow integrity while optimizing for agent compatibility and requirement traceability.

---

## II. TABLE OF CONTENTS
I. [Executive Summary](#i-executive-summary)
II. [Table of Contents](#ii-table-of-contents)
III. [Core Content](#iii-core-content)
    A. [Problem Definition](#a-problem-definition)
    B. [Key Specifications & Requirements](#b-key-specifications--requirements)
    C. [Governance & Assumptions](#c-governance--assumptions)
    D. [Open Issues & Risks](#d-open-issues--risks)
    E. [Exploratory Notes & Parking Lot](#e-exploratory-notes--parking-lot)
    F. [Project Glossary](#f-project-glossary)
IV. [Glossary](#iv-glossary)
V. [Appendix](#v-appendix)
VI. [Validation Checklist](#vi-validation-checklist)
VII. [Stakeholder Sign-off](#vii-stakeholder-sign-off)
VIII. [Next Steps](#viii-next-steps)
IX. [Changelog](#ix-changelog)
---

## III. CORE CONTENT

### A. Problem Definition
<!-- This section aligns with BABOK best practices by separating the 'pain' from the 'gain'. -->
#### 1. The Problem
The current template architecture lacks integration between the SPS (external exploratory) and Request (internal structured) workflows, creating philosophical and operational tensions. When a client has already completed the external exploration phase through SPS consultation, the Request template's Section III-A (Problem Framing & Validation) becomes redundant, forcing artificial gate validation for pre-approved problems. This creates workflow friction, cognitive overhead, and potential requirement traceability gaps between external discovery and internal analysis phases.

#### 2. The Desired Outcome
Establish a unified template architecture that preserves the fundamental philosophical distinction between external exploratory consultation (SPS) and internal structured analysis (Request) while enabling seamless workflow transitions when SPS artifacts exist. The solution should maintain the Double Diamond model integrity, optimize for Claude Code agent compatibility, and provide clear requirement lineage from external discovery through internal implementation planning.

### B. Key Specifications & Requirements
<!-- Each requirement below MUST be prefixed with a unique, traceable ID (e.g., SPS-T101-A-001). -->

#### 1. Functional Requirements
*   **SPS-T102-001:** Template architecture must support dual-mode entry - direct Request creation for well-defined problems and SPS-to-Request progression for exploratory problems
*   **SPS-T102-002:** Request template must conditionally handle pre-approved SPS artifacts and bypass Gate A validation when appropriate
*   **SPS-T102-003:** System must maintain explicit requirement traceability from SPS requirements (SPS-XXX-XXX) to Request requirements (REQ-XXX-XXX)

#### 2. Non-functional / Quality Attributes
*   **SPS-T102-004:** Template modifications must preserve Claude Code agent compatibility with manageable context windows and parsing complexity
*   **SPS-T102-005:** Workflow transitions must maintain architectural clarity and avoid monolithic document structures
*   **SPS-T102-006:** Solution must preserve audit trail integrity across external and internal workflow phases

#### 3. Design Constraints & Business Rules
*   **SPS-T102-007:** External (SPS) and Internal (Request) workflow distinction must be preserved as core architectural principle
*   **SPS-T102-008:** Double Diamond model progression (Discover/Define → Develop/Deliver) must remain intact
*   **SPS-T102-009:** Template changes must maintain backward compatibility with existing non-SPS Request workflows

#### 4. Success Metrics / Acceptance Criteria (Optional)
*   Template integration reduces workflow friction for SPS-to-Request transitions
*   Requirement traceability maintains 100% lineage from SPS to implementation
*   Agent processing complexity remains within acceptable performance bounds

### C. Governance & Assumptions

#### 1. Governance
*   **Decision Owner / Accountable Role:** SYSTEM_ARCHITECT

#### 2. Key Assumptions & Dependencies
*   SPS workflow represents completed external exploration and validated problem statements
*   Request workflow serves internal analysis and structured decomposition purposes
*   Claude Code agents operate within defined context window limitations
*   Template modifications will be implemented incrementally with validation checkpoints

### D. Open Issues & Risks
<!-- Use this log to track items requiring action or monitoring. -->
| ID | Description | Owner | Status | Target Date |
|:---|:---|:---|:---|:---|
| ISSUE-01 | Template conditional logic complexity may impact maintainability | SYSTEM_ARCHITECT | Open | TBD |
| ISSUE-02 | Requirement ID mapping conventions need standardization across workflows | SYSTEM_ARCHITECT | Open | TBD |

### E. Exploratory Notes & Parking Lot
<details>
<summary>Click to expand contextual notes & out-of-scope items</summary>

**Architectural Philosophy Context:**
The distinction between external and internal workflows reflects the fundamental difference between consultative problem discovery (where client needs exploration and guidance) versus structured analysis (where problem scope is defined and decomposition is the primary objective). This philosophical foundation drives the dual-template approach rather than monolithic document evolution.

**Agent Compatibility Considerations:**
Claude Code environment constraints favor focused, well-structured documents over large, complex artifacts. This technical reality reinforces the philosophical preference for separate but linked workflows.

**Future Considerations:**
- Template versioning strategy for evolutionary changes
- Cross-workflow consistency validation tools
- Automated requirement mapping capabilities

</details>

### F. Project Glossary
<!-- This glossary captures key client-originating terms to build a shared understanding for this specific project. -->
*   **External Workflow:** SPS-based exploratory consultation process for problem discovery and validation
*   **Internal Workflow:** Request-based structured analysis process for problem decomposition and solution planning
*   **Gate A:** Mandate approval checkpoint in Request template, bypassed when SPS pre-approval exists
*   **Requirement Lineage:** Traceability chain from SPS requirements through Request analysis to implementation

---

## IV. GLOSSARY

*   **NFR (Non-Functional Requirement):** A quality standard for the system (like speed or security) rather than a specific feature.
*   **Acceptance Criteria:** A checklist of conditions that must be met for a requirement to be considered "done."
*   **Double Diamond:** Design thinking model with Discover/Define (problem space) and Develop/Deliver (solution space) phases.

---

## V. APPENDIX 

### A. Field Reference (Token Mapping)

#### Table 1: Tokens Within "III. CORE CONTENT"

| Token | Subsection | Instruction |
|-------|------------|-------------|
| `*[PROBLEM_NARRATIVE]*` | III-A-1 | Template architecture integration challenges and workflow friction points |
| `*[OUTCOME_NARRATIVE]*` | III-A-2 | Unified architecture preserving external/internal distinction with seamless transitions |
| `*[FUNCTIONAL_REQUIREMENT]*` | III-B-1 | Specific template capabilities for dual-mode operation and conditional processing |
| `*[NON_FUNCTIONAL_REQUIREMENT]*` | III-B-2 | Agent compatibility, performance, and architectural clarity requirements |
| `*[CONSTRAINT_OR_RULE]*` | III-B-3 | Workflow distinction preservation and Double Diamond model adherence |
| `*[SUCCESS_METRIC]*` | III-B-4 | Workflow friction reduction and traceability integrity measures |
| `*[ASSUMPTION_OR_DEPENDENCY]*` | III-C-2 | Workflow role definitions and agent environment constraints |
| `*[EXPLORATORY_NOTE]*` | III-E | Architectural philosophy context and future evolution considerations |

### **Table 2: Tokens Outside "IV. CORE CONTENT"**

| Token | Section | Instruction |
|-------|---------|-------------|
| `*[EXECUTIVE_SUMMARY]*` | I | High-level overview of template architecture integration challenge |
| `*[AMENDMENT_SUMMARY]*` | V-B | Summary of changes made in amendments |
| `*[CHANGE_SUMMARY]*` | X | Brief description of changes for change history entries |

### B. Amendment Log
| Date | Change Requester | Affected Req. ID | Summary of Change |
|------|------------------|------------------|-------------------|
| 2025-08-01 | Client | Initial | Initial SPS creation |

---

## VI. VALIDATION CHECKLIST

- [x] The Problem Statement (Section III-A) has received explicit client approval.
- [x] All requirements in Section III-B are prefixed with a unique, traceable ID (e.g., `SPS-T102-001`).
- [x] The Decision Owner / Accountable Role has been identified in Section III-C.
- [x] All known open issues, risks, and dependencies have been logged in Section III-D.
- [x] The artifact's YAML header is complete and syntactically correct.

---

## VII. STAKEHOLDER SIGN-OFF

By signing off, stakeholders agree that the problems and requirements detailed in this document accurately reflect the desired work. Architectural and implementation design will be based on the contents of this artifact.

*   **Client:** _________________________ (Name, Date)
*   **Consultant:** _________________________ (Name, Date)

---



## VIII. NEXT STEPS

**Recipient:** `LLM_Analyst`

**Action:** Review this finalized SPS artifact. Use its content to create detailed technical analysis in corresponding outline artifact. Focus on architectural options, tradeoff analysis, and implementation strategy while maintaining reference to this philosophical foundation.

---

## IX. CHANGELOG

*   **v1.0.0_i1:** Initial SPS creation documenting template architecture integration problem and requirements