---
artifact_type: 'REPORT'
initiative_id: '[ID]'
epic_id: '[ID]'
research_id: '[ID]-RES-[###]'
version: '1.0.0'
iteration: '1'
date: 'YYYY-MM-DD'
status: 'draft'
author: '[Role]'
decision_owner_role: '[Role]'
---

# RESEARCH REPORT: [Title]

## I. EXECUTIVE SUMMARY

**Context**: Briefly restate *why* this research was commissioned (the blocker).
**Verdict**: Explicit "GO", "NO-GO", or "PIVOT" recommendation for the initiative.
**Key Findings**:
*   **Finding 1**: High–level summary of the most critical discovery.
*   **Finding 2**: ...

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Did the research stay within bounds?
**Source of Truth Audit**:
*   **Code base**: [List canonical files verified]
*   **Data Artifacts**: [List data files inspected]
**Limitations**: What could *not* be verified?

---

## III. TOPIC FINDINGS

### Topic 1: [Title]
**Objective**: [Restate objective]

#### A. Evidence & Forensics
*   **Source**: `[Specific File/Line]`
*   **Observation**: Raw fact (e.g., "The file has 5 columns").

#### B. Analysis
*   **Synthesis**: What does the evidence mean? (e.g., "The schema is missing the 'VWAP' field").
*   **Gap Analysis**: Discrepancy between Current State and Required State.

#### C. Governance Implication
*   **Decision Impact**: "This confirms option A in T801A-ADR-001."
*   **Risk**: "This creates a migration risk (T801A-RISK-001)."

---

### Topic 2: [Title]
...

---

## IV. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**
 ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[SCOPE]-ISSUE-###` | | | | OPEN | | | | |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[SCOPE]-RISK-###` | | | | OPEN | | | | |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `T801A-IF-001` | Table 3 | Update schema | See Topic 2.A |
| `T801A-ADR-001` | Section 2 | Paste Diagram | See Topic 1.A |

---

## VI. SOURCE MATERIAL
*   **Brief Version**: `[Version of Brief used]`
*   **Code Commit/Tag**: `[Git hash or tag if available]`
*   **Files Cited**:
    *   `components/...`
    *   `data/...`
