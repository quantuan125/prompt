---
task_id: 'T102'
prefix_id: 'SPS-T102'
parent_task: 'T101' 
task_type: 'system'
target: 'prompt/templates/consultant'
name: 'Consultancy Layer Architecture'
artifact_type: 'SPS'
version: '1.0.0'
date: '2025-08-02'
status: 'ready_for_review'
dependencies: 
    - 'sps_structural_template.md' 
    - 'request_structural_template.md' 
    - 'sps_consultant-general_T101A.md'
author: 'LLM Consultant'
decision_owner_role: 'Client'
---

# SYNTHESIZED PROBLEM STATEMENT (SPS): Consultancy Layer Architecture - T102

## I. EXECUTIVE SUMMARY

This document defines the requirements for a comprehensive, three-stage consultancy workflow (`SPS` → `Request` → `Concept`) designed to transform ambiguous client ideas into architecturally-ready solution concepts. The initial challenge of simply linking two templates has been expanded to formalize an end-to-end process that aligns with industry standards (e.g., Double Diamond, ISO 29148). The solution will establish three distinct but interconnected artifacts, define their procedural handoffs, ensure robust requirement traceability, and manage LLM context limitations, culminating in a `Concept` artifact that serves as the definitive, client-approved bridge to the `System Architect`.

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

#### 1. The Problem
The current system lacks a formalized, end-to-end workflow for transforming a client's raw, ambiguous idea into a set of validated, high-level solution concepts ready for architectural design. The existing `SPS` (exploratory) and `Request` (structured) artifacts were designed in isolation, creating operational friction, traceability gaps, and no clear path to solutioning. This forces the `LLM_Consultant` to perform poorly when asked to design concept-level solutions directly from an `SPS`, as there is no intermediate step to ground the problem in project reality or a final artifact to document the proposed solution concepts.

#### 2. The Desired Outcome
To implement a robust, three-stage consultancy workflow (`SPS` → `Request` → `Concept`) supported by a suite of integrated templates and procedural guidelines. This system will:
1.  Preserve the distinct philosophies of `SPS` (unconstrained problem exploration) and `Request` (grounded requirements analysis).
2.  Introduce a new `Concept` artifact to systematically explore and document high-level solutions.
3.  Ensure seamless, traceable, and partially-automated handoffs between each stage.
4.  Effectively manage LLM context windows and align with industry standards for requirements engineering.

### B. Key Specifications & Requirements

#### 1. Functional Requirements
*   **SPS-T102-001:** The `Request` template must be able to ingest a finalized `SPS` artifact, summarizing its key findings to bootstrap the internal analysis process and bypass redundant initial discovery steps.
*   **SPS-T102-002:** The `request_procedural_guideline.md` must be updated with conditional logic to handle "fast-track" scenarios where a pre-approved SPS exists, marking initial gates as pre-approved.
*   **SPS-T102-003:** A new `Concept` artifact, including a structural template (`concept_structural_template.md`) and procedural guideline (`concept_procedural_guideline.md`), must be created.
*   **SPS-T102-004:** The `Concept` procedural guideline must be based on the "Phase 2: Develop & Deliver" workflow defined in the `sps_consultant-general_T101A` artifact.
*   **SPS-T102-005:** The `Concept` template must include an "Architectural Detail Level" rubric (e.g., High/Mid/Low) that requires sign-off from the `System Architect` to formalize the handoff contract.
*   **SPS-T102-006:** A lightweight, automatable mechanism (e.g., a script or defined mapping table) for ensuring requirement ID traceability from `SPS-ID` to `REQ-ID` must be defined.
*   **SPS-T102-007:** All artifact templates (`SPS`, `Request`, `Concept`) must include a `Source-Artefact-Version` field in their headers to support change control.
*   **SPS-T102-008:** The `Request` procedural guideline must mandate that raw Q&A dialogue is externalized to a separate `raw_consultation.md` file to manage token context.
*   **SPS-T102-009:** The `prompt_main.md` documentation must be updated to describe the finalized three-stage consultancy workflow and the purpose of the `SPS`, `Request`, and `Concept` artifacts under the `Consultant` role definition.
*   **SPS-T102-010:** The `sps_structural_template.md` must be revised to: 
    *   (a) Update the `VIII. NEXT STEPS` section to explicitly name the `Request` artifact as the recipient, and 
    *   (b) Add a new item to the `VI. VALIDATION CHECKLIST`: `[ ] The 'Next Steps' section clearly defines the handoff to the Request workflow.`
*   **SPS-T102-011:** The `sps_structural_template.md` must be streamlined by removing the `Success Metrics / Acceptance Criteria` section to enforce a clear separation of concerns, deferring all solution-oriented criteria to the `Request` artifact.
*   **SPS-T102-012:** While the `LLM_Consultant` is the designated role for all three consultancy stages, distinct system prompts must be developed for each artifact (`SPS`, `Request`, `Concept`). These prompts must be stored in a designated repository path (e.g., `prompt/roles/consultant/prompts/`) and any change to a prompt must trigger a minor version bump of its associated procedural guideline.
*  **SPS-T102-013:** The `Concept` template's validation checklist must include a mandatory "Technical Feasibility Sign-off" item to be actioned by the `LLM_Planner` upon intake.
*  **SPS-T102-014:** The `sps_procedural_guideline.md` must be updated to include a rubric for assigning ownership of `Open Issues` based on the core mandate of the responsible role.


#### 2. Non-functional / Quality Attributes
*   **SPS-T102-015:** The entire workflow must maintain architectural clarity, avoiding monolithic document structures in favor of separate but linked artifacts.
*   **SPS-T102-016:** The solution must preserve a clear audit trail across the external-facing (`SPS`) and internal-facing (`Request`, `Concept`) phases.
*   **SPS-T102-017:** All template modifications and new artifacts must be designed to minimize LLM agent parsing complexity and operate within practical context window limits.
*   **SPS-T102-018:** The system must support machine-readable outputs (e.g., JSON side-car files) for key artifacts to future-proof traceability and automation tooling.

#### 3. Design Constraints & Business Rules
*   **SPS-T102-019:** The philosophical distinction between `SPS` (external, exploratory) and `Request` (internal, structured) workflows must be preserved as a core architectural principle.
*   **SPS-T102-020:** The workflow must align with the Double Diamond design model (Discover/Define → Develop/Deliver).

### C. Governance & Assumptions

#### 1. Governance
*   **Decision Owner / Accountable Role:** Client

#### 2. Key Assumptions & Dependencies
*   The three-stage workflow (`SPS` → `Request` → `Concept`) is the approved standard for the consultancy layer.
*   `SPS` workflow represents completed external exploration (Discover).
*   `Request` workflow serves internal analysis and structured decomposition (Define).
*   `Concept` workflow facilitates high-level solution exploration (Develop/Deliver).
*   This architecture is dependent on the procedural guidelines defined in `SPS_T101A` for the `Concept` phase.
*   Claude Code agents operate within defined context window limitations.

### D. Open Issues & Risks

| ID | Description | Owner | Status | Target Date |
|:---|:---|:---|:---|:---|
| ISSUE-01 | The specific data handoff and summarization logic for the `SPS` → `Request` transition needs to be defined. | LLM_Consultant | Open | TBD |
| ISSUE-02 | A full change-impact workflow (beyond simple version tracking) needs to be designed. This should include a minimum viable impact-analysis checklist, potentially referencing ISO 29148 Annex C. | Client | Open | TBD |
| ISSUE-03 | The specific tooling or strategy (e.g., vector stores, chunking) for managing large context windows for multi-issue packages must be selected. | LLM_Planner | Open | TBD |

### E. Exploratory Notes & Parking Lot
<details>
<summary>Click to expand contextual notes & out-of-scope items</summary>

**Architectural Philosophy Context:**
The three-artifact workflow (`SPS` → `Request` → `Concept`) is a deliberate implementation of the Double Diamond design model. The `SPS` completes the first diamond (Discover/Define), resulting in a validated problem. The `Request` and `Concept` artifacts complete the second diamond (Develop/Deliver), resulting in a validated high-level solution. This separation prevents premature solutioning and ensures each phase has a clear purpose and deliverable.

**Agent Compatibility Considerations:**
Claude Code environment constraints favor focused, well-structured documents over large, complex artifacts. This technical reality reinforces the philosophical preference for separate but linked workflows.

**Industry Benchmarks & Standards:**
The proposed architecture aligns with established industry frameworks and standards, which should be used as a reference during implementation:
*   **Design Council:** The Double Diamond Model (Discover/Define → Develop/Deliver).
*   **ISO/IEC/IEEE 29148:** Requirements Engineering (for traceability and change control).
*   **IIBA BABOK v3:** Separation of Elicitation & Collaboration vs. Requirements Analysis.
*   **SAFe:** Hierarchy mapping from Epic Hypothesis (≈SPS) to Capability/Feature (≈Request).
*   **ISO/IEC/IEEE 24765, IEEE Std 15288 & 12207, INCOSE Requirements Management Primer:** For consistent terminology, lifecycle alignment, and change-impact templates.

</details>

### F. Project Glossary

*   **SPS Artifact:** The first artifact in the consultancy workflow, focused on exploratory problem discovery (Discover phase).
*   **Request Artifact:** The second artifact, focused on structured problem decomposition and grounding against project context (Define phase).
*   **Concept Artifact:** The third and final artifact in the consultancy workflow, focused on solution exploration and selection (Develop/Deliver phase). It translates the "what" from the `Request` into potential "how" options.
*   **Requirement Lineage:** The traceable chain linking requirements from `SPS` through `Request` to implementation.
*   **Fast-Track Scenario:** A workflow path within the `Request` process that bypasses initial problem-framing steps when a pre-approved `SPS` artifact is provided as input.
*   **Architectural Detail Level:** A rubric within the `Concept` artifact used by the `Consultant` and `System Architect` to agree on the required level of technical detail for a solution proposal before it is finalized.
---

## IV. GLOSSARY

*   **BABOK (Business Analysis Body of Knowledge):** A globally recognized standard for the practice of business analysis.
*   **Double Diamond:** A design thinking model representing a process of exploring an issue more widely or deeply (divergent thinking) and then taking focused action (convergent thinking).
*   **ISO/IEC/IEEE 29148:** An international standard for requirements engineering.
*   **RACI Matrix:** A responsibility assignment chart that maps out what project tasks and deliverables each person or role is Responsible, Accountable, Consulted, and Informed for.

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
- [ ] The 'Next Steps' section clearly defines the handoff to the Request workflow.

---

## VII. STAKEHOLDER SIGN-OFF

By signing off, stakeholders agree that the problems and requirements detailed in this document accurately reflect the desired work. Architectural and implementation design will be based on the contents of this artifact.

*   **Client:** _________________________ (Name, Date)
*   **Consultant:** _________________________ (Name, Date)

---


## VIII. NEXT STEPS

**Primary Stakeholder & Decision Owner:** `Client` 

**Downstream Consumer:** `LLM_Planner` 

**Implementation Actions & Responsibilities (RACI):**

| # | Action | Responsible | Accountable | Consulted | Informed |
|:--|:---|:---|:---|:---|:---|
| 1 | Create/modify the `SPS`, `Request`, and `Concept` structural templates and procedural guidelines. | `LLM_Consultant` | `Client` | `LLM_Planner` | `LLM_Developer` |
| 2 | Develop the distinct system prompts for each stage of the consultancy workflow. | `LLM_Consultant` | `Client` | `LLM_Planner` | - |
| 3 | Develop the required ID-mapping mechanism/script. | `LLM_Developer` | `LLM_Planner` | `LLM_Consultant` | - |
| 4 | Update the `prompt_main.md` documentation with the new workflow description. | `LLM_Developer` | `Client` | `LLM_Consultant` | - |

---

## IX. CHANGELOG

*   **v1.0.0_i1:** Initial SPS creation documenting the problem of linking two templates.
*   **v1.0.0_i2:** Major revision to expand scope to the full three-artifact (`SPS` → `Request` → `Concept`) workflow, incorporating external feedback and requirements from T101A.
*   **v1.0.0_i3:** Final revision incorporating multiple rounds of external feedback. Globally replaced `SYSTEM_ARCHITECT`, renumbered all requirements, removed success metrics from scope, and added new requirements for template governance and automation hooks. Set `Client` as final Decision Owner, corrected Issue ownership, added Planner sign-off to Concept, renumbered all requirements, and clarified Next Steps with a RACI matrix.
