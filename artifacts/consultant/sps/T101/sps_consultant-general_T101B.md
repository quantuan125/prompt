---
task_id: 'T101B'
prefix_id: 'SPS-T101B'
parent_task: 'T101A'
task_type: 'system/documentation'
target: 'prompt/templates/sps'
artifact_type: 'SPS'
version: '1.0.0_i3'
author: 'LLM_Consultant'
date: '2025-07-22'
status: 'ready_for_review'
dependencies: ['sps_consultant-general_T101-A_v1.0.0_i4.md']
decision_owner_role: 'Client'
---

# SYNTHESIZED PROBLEM STATEMENT (SPS): prompt/templates/sps - T101B

## I. EXECUTIVE SUMMARY

This document defines the finalized requirements and specifications for creating the version 1.0.0 **SPS Artifact Family** at `prompt/templates/sps` (`SPS Structural Template`, `SPS Procedural Guideline`, and `sps_manifest.json`). It incorporates multiple rounds of client and expert feedback to ensure the resulting templates are compliant with system-wide standards, enable robust automation, and equip the `LLM_Consultant` to perform its "general" consultation task effectively. This specification serves as the formal "Problem Alignment Gate" for Task T101B; upon approval, it will guide the development of the draft template files.

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
IV. [Glossary of Template Terms](#iv-glossary-of-template-terms)
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
The `LLM_Consultant` needs a standardized set of tools to execute its "general" consultation task as defined in T101A. Without a formal structural template (SPSST) and procedural guideline (SPSPG), the consultant's output would be inconsistent, difficult to automate, and would not integrate cleanly with the downstream `request` workflow. This creates a critical gap in our system's front-door process for handling ambiguous ideas.

#### 2. The Desired Outcome
To produce the v1.0.0 artifact family (`SPSST`, `SPSPG`, `sps_manifest.json`) that equips the `LLM_Consultant` to generate a lean, focused, and validated **SPS Artifact**. This output will serve as the formal, machine-parseable input to the `request` workflow, effectively standardizing and replacing its initial "Problem Framing & Validation" step.

### B. Key Specifications & Requirements
<!-- Each requirement below MUST be prefixed with a unique, traceable ID (e.g., SPS-T101B-001). -->

#### 1. SPS Structural Template (SPSST) Requirements
*   **SPS-T101B-001:** The SPSST MUST adopt the full standard shell from `prompt_main.md`, with non-essential sections included as minimal stubs.
*   **SPS-T101B-002:** The SPSST MUST use a YAML Frontmatter header for all metadata, replacing the legacy Markdown block.
*   **SPS-T101B-003:** The `IV. CORE CONTENT` section MUST be custom-designed according to the industry-aligned structure finalized in our consultation (Problem Definition, Requirements, Governance, Issues, Notes, Project Glossary).
*   **SPS-T101B-004:** The SPSST MUST include a `Validation Checklist` with 3-5 verifiable self-check items specific to the SPS artifact.

#### 2. SPS Procedural Guideline (SPSPG) Requirements
*   **SPS-T101B-005:** The SPSPG WILL be a machine-readable contract, with agent behaviors defined in discrete `SCOPE` blocks. Each block MUST include `prereq` and `success` criteria to serve as an entry/exit gate for the agent's execution protocol. The initial scopes are `framing_sps`, `defining_sps`, `feedback_sps`, and `branching_sps`.
*   **SPS-T101B-006:** The SPSPG MUST contain a "Table of Tokens" that explicitly documents the mapping from SPSST fields to `request` structural template (`RST`) tokens to ensure a seamless automated handoff.
*   **SPS-T101B-007:** The `branching_sps` scope MUST encode the three-step procedure for transparently executing the Branch Decision Framework (state checklist, recommend, seek approval).
*   **SPS-T101B-008:** The `feedback_sps` scope MUST encode the "Synthesize & Propose" protocol for handling external feedback.
*   **SPS-T101B-009:** The SPSPG MUST provide a one-sentence rubric to guide the agent in classifying information between "Open Issues" and "Exploratory Notes".
*   **SPS-T101B-010:** The SPSPG MUST document the versioning rule (`major.minor.patch` for structure, `_iN` for in-consultation iteration).

#### 3. `sps_manifest.json` Requirements
*   **SPS-T101B-011:** A new `sps_manifest.json` file WILL be created with a schema that is a direct clone of the `request_manifest.json` schema.

### C. Governance & Assumptions

#### 1. Governance
*   **Decision Owner / Accountable Role:** `Client`

#### 2. Key Assumptions & Dependencies
*   The `LLM_Consultant`'s core execution protocol (Block 5) will be a generic interpreter capable of executing `SCOPE` blocks from a provided procedural guideline (like this SPSPG).
*   This SPSPG is the Single Source of Truth for the procedures defined in `sps_consultant-general_T101-A_v1.0.0_i4.md`.

### D. Open Issues & Risks
<!-- Use this log to track items requiring action or monitoring. -->
| ID | Description | Owner | Status | Target Date |
|:---|:---|:---|:---|:---|
| ISSUE-01 | No open issues identified during the problem definition phase. | N/A | Closed | N/A |

### E. Exploratory Notes & Parking Lot
<details>
<summary>Click to expand contextual notes & out-of-scope items</summary>

*   **Heavy Governance Deferral:** It was determined that heavy governance tracking items (e.g., a formal Risk Register, a full Decision Log, RACI Matrix) are out of scope for the lean SPS artifact and are explicitly deferred to the downstream `request` workflow.
*   **Procedural Gates Deferral:** The implementation of formal "Hard Gates" (H-Gates) within the SPSPG has been deferred to a future version (v2.0.0 or later) pending further testing.
*   **Process History:** This final specification was shaped by an iterative consultation process that included the analysis of two rounds of external "second opinion" feedback. This feedback was instrumental in aligning the artifact with industry standards (BABOK, IEEE 29148) and adding the necessary rigor for automation and traceability.

*   **SPSPG Workflow Delegation Details**: The SPSPG will operationalize the following specific procedures defined in SPS_T101A:

1. **Handling External Feedback (`feedback_sps` scope):** A structured 4-step "Synthesize & Propose" protocol triggered when clients introduce expert feedback or second opinions. The procedure includes acknowledgment, critical assessment, synthesis, and approval-seeking phases.
2.  **Handling Emergent Dependencies (`branching_sps` scope):** A triage system for scope creep management using a 4-question Branch Decision Framework that evaluates whether new requests should create parallel tasks or be handled in-line. Decision criteria include deliverable independence, longevity, expertise requirements, and timeline impact
3.  **Phased Conversational Workflow:** The complete Phase 0-3 structure covering Intake & Framing, Problem Space exploration (Discover & Define), Solution Space development (Develop & Deliver), and Formal Handoff with specific gates and validation checkpoints.

This delegation ensures the SPSPG serves as the Single Source of Truth for execution procedures while maintaining clean separation between conceptual design (SPS_T101A) and operational implementation (SPSPG).

</details>

### F. Project Glossary
<!-- This glossary captures key client-originating terms to build a shared understanding for this specific project. -->
*   **Term:** `SPSST` (SPS Structural Template)
*   **Definition:** The standard Markdown template that defines the structure, sections, and headers for all SPS artifacts.
*   **Term:** `SPSPG` (SPS Procedural Guideline)
*   **Definition:** The machine-readable contract that defines the step-by-step procedures, scopes, and rules the `LLM_Consultant` must follow.

---

## IV. GLOSSARY
*   **NFR (Non-Functional Requirement):** A quality standard for the system (like speed or security) rather than a specific feature.
*   **Ubiquitous Language:** A shared, common language developed by a team in a specific domain, as per Domain-Driven Design (DDD).

---

## V. APPENDIX

### A. Field Reference (Token Mapping)

#### Table 1: Tokens Within "III. CORE CONTENT"

| Token | Subsection | Instruction |
|-------|------------|-------------|
| `*[PROBLEM_NARRATIVE]*` | III-A-1 | A concise statement of the business pain, challenge, or opportunity. |
| `*[OUTCOME_NARRATIVE]*` | III-A-2 | A clear description of the future state or business value to be achieved. |
| `*[FUNCTIONAL_REQUIREMENT]*` | III-B-1 | A specific statement of capability or behavior the system must provide. |
| `*[NON_FUNCTIONAL_REQUIREMENT]*` | III-B-2 | A requirement related to performance, security, usability, etc. (an NFR). |
| `*[CONSTRAINT_OR_RULE]*` | III-B-3 | A business rule or technical constraint that the solution must adhere to. |
| `*[SUCCESS_METRIC]*` | III-B-4 | An early articulation of how success will be measured (KPI or AC). |
| `*[ASSUMPTION_OR_DEPENDENCY]*` | III-C-2 | A documented assumption or dependency believed to be true. |
| `*[ISSUE_DESCRIPTION]*` | III-D | Concise description of the issue or risk in the log. |
| `*[ISSUE_OWNER]*` | III-D | The role or name of the person responsible for the issue. |
| `*[ISSUE_STATUS]*` | III-D | The current status of the issue (e.g., Open, Blocked). |
| `*[ISSUE_TARGET_DATE]*` | III-D | The target resolution date for the issue. |
| `*[EXPLORATORY_NOTE]*` | III-E | Contextual information or deferred ideas not part of the core scope. |
| `*[PROJECT_TERM]*` | III-F | A key client-originating term for the project-specific glossary. |
| `*[PROJECT_TERM_DEFINITION]*` | III-F | The agreed-upon definition for the project-specific term. |

---

## VI. VALIDATION CHECKLIST

- [ ] The Problem Statement (Section III-A) has received explicit client approval.
- [ ] All requirements in Section III-B are prefixed with a unique, traceable ID (e.g., `SPS-T101B-001`).
- [ ] The Decision Owner / Accountable Role has been identified in Section III-C.
- [ ] All known open issues, risks, and dependencies have been logged in Section III-D.
- [ ] The artifact's YAML header is complete and syntactically correct.

---

## VII. STAKEHOLDER SIGN-OFF

By signing off, stakeholders agree that the problems and requirements detailed in this document accurately reflect the desired work. Architectural and implementation design will be based on the contents of this artifact.

*   **Client:** _________________________ (Name, Date)
*   **Consultant:** _________________________ (Name, Date)

---

## VIII. NEXT STEPS

**Recipient:** `LLM_Consultant`

**Action:** With client approval of this SPS artifact, Task T101B will formally pass the **Problem Alignment Gate** and move into the **Develop & Deliver** phase. The primary deliverable of the next phase will be the draft v1.0.0 files for the `sps_structural_template.md`, `sps_procedural_guideline.md`, and `sps_manifest.json`, built according to the specifications herein.

---

## IX. CHANGELOG

*   **v1.0.0_i3:** Refactored artifact into the final `sps_structural_template.md` structure. Greatly expanded `SPSPG` specifications to serve as the SSOT for the consultant's procedural logic, incorporating behaviors from T101A.
*   **v1.0.0_i2:** Initial creation of the comprehensive problem statement for Task T101B.
*   **v1.0.0_i1:** Initial raw draft.