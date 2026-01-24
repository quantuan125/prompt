# CONSULTANCY REPORT: Research Brief Framework Review
**Subject**: Comparative Analysis of `T801A-RES-001` vs `T801A-RES-002` & Enhancement Recommendations
**To**: LLM_Consultant
**Date**: 2026-01-03
**Status**: DRAFT FOR REVIEW

---

## 1. Comparative Analysis (Task 1)

**Objective**: Assess `T801A-RES-001` (Backend TTI Architecture) and `T801A-RES-002` (System Architecture) to determine the best structural exemplar for the initiative.

### **A. T801A-RES-001 (The "External" Brief)**
*   **Strengths**:
    *   **Rigorous Structure**: Follows a standard academic/professional research structure (`Exec Summary` → `Scope` → `Methodology` → `Dependencies` → `Success Criteria`).
    *   **Governance Integration**: Section V ("Critical Dependencies") explicitly maps research topics to specific E-RIDs (QG, DEP, ASSUM), ensuring the research has immediate normative value.
    *   **Integration Analysis**: Explicitly asks how topics interact (e.g., "Scoring ↔ File Format"), preventing siloed findings.
    *   **Methodology Definition**: Defines *how* to research ("Comparative Analysis Framework"), ensuring consistent quality.
*   **Weaknesses**:
    *   Slightly verbose for purely internal system checks (forensics).

### **B. T801A-RES-002 (The "Internal" Brief)**
*   **Strengths**:
    *   **"Input Packet" (Section VI)**: This is a **critical innovation**. By providing explicit file paths and context pointers (`sps`, `code`, `prompts`, `data`), it drastically reduces "time-to-context" for the researching agent. This is superior to RES-001's generic "Industry Standards" sourcing.
    *   **Actionable Forensics**: The questions are grounded in specific file paths (`components/tv_ingest/...`), making hallucinations nearly impossible.
*   **Weaknesses**:
    *   **Structural Drift**: Lacks standard sections found in RES-001 (Methodology, Constraints, Timeline), making it feel less like a formal commission and more like a TODO list.
    *   **Missing Integration Layer**: It asks for forensic facts (Topics 1-3) and design definitions (Topic 4-5) but lacks a specific section challenging the researcher to harmonize them (e.g., "Does the current Webhook Schema support the proposed Minimal Market Context?").

### **Verdict & Exemplar Decision**
**A New Standard is Required.**
Neither RES-001 nor RES-002 is perfect on its own. `T801A-RES-001` has the correct *governance structure*, but `T801A-RES-002` has the superior *context mechanism* (Input Packet).

**Decision**: We will unify these into a **Single Standard Brief Structure** moving forward. `T801A-RES-002` (once refined) will become the first instance of this new standard.

**Action**: A unified template has been created at:
`prompt\artifacts\tasks\T801\research\brief\template_research_brief.md`

---

## 2. Detailed Analysis of T801A-RES-002 & Standardization (Task 2)

**Objective**: Elevate `T801A-RES-002` to become the definitive "Structural Exemplar" by injecting the missing rigorous sections from RES-001 and standardizing the widely-praised "Input Packet".

### **A. Structural Gaps (Critical)**
The draft is missing three key sections required by the Initiative Standard (RES-001):
1.  **Methodology Framework**: Even for internal forensics, the brief must define the "Hierarchy of Truth."
    *   *Example*: "If Code (`webhook_processor.py`) conflicts with Data (`master.csv`), which is authoritative? If Documentation (`main.md`) conflicts with Code, which wins?" (RES-002 implies Code > Data, but this must be explicit).
2.  **Constraints & Assumptions**: Explicitly stating strict constraints saves cycles.
    *   *Example*: "Constraint: No external API calls allowed—analysis must be static code analysis and file forensics only."
    *   *Example*: "Assumption: The `tv_ingest` component is the only writer to `master.csv`."
3.  **Cross-Topic Integration**:
    *   Topics 1-3 are "Current State" (Forensics).
    *   Topics 4-5 are "Future State" (Requirements).
    *   *Gap*: There is no question asking: "Gap Analysis: What specific fields are missing in the *Current State* (Topic 3) that are required to support the *Future State* (Topic 4)?"

### **B. Content Improvements**
1.  **Refine Topic 4 (Minimal Market Context)**:
    *   *Current*: Asks for "Lean JSON."
    *   *Improvement*: Explicitly request a **Token Cost Analysis**. "Estimate the token count of the proposed 'Minimum Context' vs 'Full Context' to justify the 'Minimal' selection against `T801A-IG-010` (Artifact Size Guidance)."
2.  **Refine Topic 5 (Historical Data)**:
    *   *Current*: Asks "What history depth is needed?"
    *   *Improvement*: Frame this as a **Dependency Check**. "Does the current PineScript export capability (Topic 2 analysis) support the required depth, or does this confirm `T801A-DEP-004` (Expanded Data Structure) as a hard blocker?"
3.  **Enhance Section VI (Input Packet)**:
    *   Add **"Anti-Patterns/Red Herrings"**: Explicitly list files/directories to IGNORE (e.g. `storage/tv_ingest/` which the brief mentions in text but should be formally excluded in the input packet to prevent contamination).

### **C. Standardization Action**
A dedicated template file has been created to enforce this structure for all future briefs. You can view the template here:
> `prompt\artifacts\tasks\T801\research\brief\template_research_brief.md`

**Recommendation**: Rewrite `T801A-RES-002` to perfectly match this template. This will officially designate it as the "v1.0.0 Exemplar" for the initiative.

---

## 3. High-Level Clarifying Questions

As your Consultant, I need you to clarify the following before we finalize the brief:

1.  **Hierarchy of Truth**: In the event of a conflict between the *Code implementation* (`components/tv_ingest`) and the *Stored Data Artifacts* (`master.csv`), which should the researcher treat as the "de facto" specification for the Current State? (Code reflects intent; Data reflects reality).
2.  **Scope of "Minimal Context"**: For Topic 4, are we optimizing primarily for **Token Cost** (keep it small) or **Information Sufficiency** (keep it accurate)? (This guides the trade-off analysis).
3.  **Research Output Format**: Do you want the researcher to modify the existing `proposal_..._v1.0.0.md` file directly with findings, or produce a separate `report_T801A-RES-002...md` linked from it? (RES-001 implies a separate report, but Phase 1 pace is fast).
