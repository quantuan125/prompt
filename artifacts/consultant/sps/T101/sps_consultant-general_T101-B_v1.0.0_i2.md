# SPS Artifact: consultant/general.md - T101B

## I. METADATA BLOCK
---
**Task ID:** T101B
**Task Type:** system/documentation
**Target:** `sps_structural_template.md`, `sps_procedural_guideline.md`
**Artifact Type:** SPS
**Version:** 1.0.0
**Author:** LLM_Consultant
**Date:** 2025-07-22
**Status:** ready_for_review
**Dependencies:** `sps_consultant-general_T101-A_v1.0.1_i4.md`
---

## II. EXECUTIVE SUMMARY
This document defines the finalized requirements and specifications for creating the version 1.0.0 **SPS Artifact Family** (`SPSST`, `SPSPG`, and `sps_manifest.json`). It incorporates detailed feedback to ensure the resulting templates are compliant with system-wide standards, enable robust automation, and equip the `LLM_Consultant` to perform its "general" consultation task effectively.

This specification serves as the formal "Problem Alignment Gate" for Task T101B. Upon approval, it will guide the development of the draft template files.

## III. TABLE OF CONTENTS
I. [EXECUTIVE SUMMARY](#i-executive-summary)
II. [TABLE OF CONTENTS](#ii-table-of-contents)
III. [FINALIZED PROBLEM STATEMENT (T101B)](#iii-finalized-problem-statement-t101b)
IV. [CORE CONTENT: DETAILED SPECIFICATIONS](#iv-core-content-detailed-specifications)
    A. [SPS Structural Template (SPSST) Specifications](#a-sps-structural-template-spsst-specifications)
    B. [SPS Procedural Guideline (SPSPG) Specifications](#b-sps-procedural-guideline-spspg-specifications)
    C. [`sps_manifest.json` Specifications](#c-sps_manifestjson-specifications)
    D. [Exploratory Notes & Deferred Items](#d-exploratory-notes--deferred-items)
V. [VALIDATION CHECKLIST](#v-validation-checklist)
VI. [NEXT STEPS](#vi-next-steps)
VII. [CHANGELOG](#vii-changelog)


## IV. CORE CONTENT: DETAILED SPECIFICATIONS

### The Core Challenge
We need to design and produce the first versions (v1.0.0) of two foundational artifacts: the **SPS Structural Template (SPSST)** and the **SPS Procedural Guideline (SPSPG)**, along with a corresponding `sps_manifest.json`.

These artifacts will equip the `LLM_Consultant` with the standardized tools required to execute its "general" consultation task. The primary goal is to enable the consultant to produce a lean, focused, and validated **SPS (Synthesized Problem Statement) Artifact**. This SPS artifact will serve as the formal, machine-parseable input for the downstream `request` workflow, effectively replacing and standardizing the "Problem Framing & Validation" step of that process.

### A. SPS Structural Template (SPSST) Specifications
1.  **Standard Shell Compliance:** The SPSST MUST adopt the full standard template shell mandated by Section 7 of `prompt_main.md`. Non-essential sections for this artifact's purpose (e.g., `Executive Summary`, `Stakeholder Sign-off`) WILL be included but marked as minimal placeholders to ensure system-wide structural consistency.
2.  **Core Content Design:** The `IV. CORE CONTENT` section MUST be lean and contain the following subsections:
    *   **A. Finalized Problem Statement:** The primary narrative output of the consultation's discovery phase.
    *   **B. Open Issues:** A bulleted list to log parked questions, unresolved items, and dependencies.
    *   **C. Glossary:** A section for the Ubiquitous Language, which MUST include a one-sentence "collection principle" (e.g., "This glossary captures key client-originating terms to build a shared understanding.").
    *   **D. Governance Hooks:** A minimal section to capture the `Decision Owner Role` and a placeholder for `High-Level Risks`.
    *   **E. Exploratory Notes:** A clearly demarcated section for logging context from external feedback or other sources that are useful but not part of the binding problem statement.
3.  **YAML Header Schema:** The SPSST MUST include a YAML header with the following schema:
    *   `task_id`
    *   `parent_task` (Optional)
    *   `task_type`
    *   `target`
    *   `artifact_type` (Value: "SPS")
    *   `version`
    *   `author`
    *   `date`
    *   `status`
    *   `dependencies`
    *   `decision_owner_role`
4.  **Validation Checklist:** The SPSST MUST include a `Validation Checklist` section with 3-5 verifiable self-check items (e.g., "Problem Statement has received explicit client approval.").

### B. SPS Procedural Guideline (SPSPG) Specifications
1.  **Machine-Readable Contract:** The SPSPG WILL be a machine-readable contract using `SCOPE` blocks. Each `SCOPE` block MUST include `prereq` and `success` criteria, defining its operational contract.
2.  **Scope Definition:** The SPSPG will include the following initial `SCOPE`s:
    *   `framing_sps`
    *   `defining_sps`
    *   `feedback_sps` (for handling external feedback)
    *   `branching_sps` (for triaging emergent dependencies)
3.  **Token Mapping:** The SPSPG MUST contain a "Table of Tokens" that explicitly documents the mapping from SPSST fields to `request` structural template (`RST`) tokens. Example:
    *   `SPSST Finalized Problem Statement` → `RST *[VALIDATED_MANDATE]*`
    *   `SPSST Open Issues` → `RST *[KEY_POINTS_SUMMARY]*` (as initial input)
4.  **Branching Procedure:** The `branching_sps` scope MUST encode the three-step procedure for transparently executing the Branch Decision Framework:
    1.  The agent states the four checklist questions and its Y/N assessment for each.
    2.  The agent states the final branching recommendation (`branch` or `continue`).
    3.  The agent asks for explicit client approval to proceed with the recommendation.
5.  **Information Classification Rubric:** The SPSPG MUST provide a one-sentence rubric to guide the agent in classifying information between "Open Issues" and "Exploratory Notes".
    *   **Open Issue:** "An unresolved question or dependency that blocks progress and requires a future action."
    *   **Exploratory Note:** "Contextual information that is valuable for awareness but is not part of the core problem and does not require a direct action."
6.  **Versioning Rule:** The SPSPG MUST document the versioning and iteration rule: "The artifact's semantic `version` is updated only on structural changes to the template. The `_iN` iteration count increments with each save/update during a single consultation."

### C. `sps_manifest.json` Specifications
1.  A new `sps_manifest.json` file WILL be created.
2.  Its schema MUST be a direct clone of the `request_manifest.json` schema to ensure system consistency.

### D. Exploratory Notes & Deferred Items
*This section logs key decisions and deferred topics from the consultation that shaped the final requirements but are not part of the specification itself.*
*   **Heavy Governance Deferral:** It was determined that heavy governance tracking items (e.g., a formal Risk Register, a full Decision Log, RACI Matrix) are out of scope for the lean SPS artifact. These requirements are explicitly deferred to the more comprehensive, downstream `request` workflow.
*   **Procedural Gates Deferral:** The implementation of formal "Hard Gates" (H-Gates) within the SPSPG has been deferred to a future version (v2.0.0 or later) pending further testing. The initial version will focus on the `SCOPE` contract.
*   **Process History:** This final specification was shaped by an iterative consultation process that included the analysis of external "second opinion" feedback. This feedback was instrumental in adding the necessary rigor and compliance details to the requirements.

## V. VALIDATION CHECKLIST
- [ ] Does the SPSST specification include the full standard template shell?
- [ ] Is the YAML header schema for the SPSST fully defined?
- [ ] Does the SPSPG specification require a `prereq`/`success` contract for each `SCOPE`?
- [ ] Is the mapping from SPS tokens to `request` tokens specified as a requirement?
- [ ] Is the procedure for transparent branching clearly defined?
- [ ] Are the versioning rules and classification rubrics included as requirements?

## VI. NEXT STEPS
With client approval of this SPS artifact, Task T101B will formally pass the **Problem Alignment Gate** and move into the **Develop & Deliver** phase.

The primary deliverable of the next phase will be the draft v1.0.0 files for:
1.  `sps_structural_template.md`
2.  `sps_procedural_guideline.md`
3.  `sps_manifest.json`

## VII. CHANGELOG
*   **v1.0.0:** Initial creation and finalization of the comprehensive problem statement for Task T101B, incorporating all client and expert feedback.