---
artifact_type: 'BRIEF'
initiative_id: '[ID]'
epic_id: '[ID]'
research_id: '[ID]-RES-[###]'
version: '1.0.0'
iteration: '1'
date: 'YYYY-MM-DD'
status: 'template'
author: '[Role]'
decision_owner_role: '[Role]'
---

# RESEARCH BRIEF: [Title]

## I. EXECUTIVE SUMMARY

**Context**: One paragraph describing *why* this research is needed now. What blocker does it resolve?
**Objective**: Clear statement of what this research must achieve.
**Target Deliverable**: Description of the output and who is the consumer? (e.g. Architect, Consultant or Developer).

## II. RESEARCH SCOPE & TOPICS

### Part A: [Category Name - e.g. Current State]

#### Topic 1: [Topic Title] ([Priority])
**Objective**: What specific question needs answering?
**Context**: Why is this hard/unknown?
**Specific Questions**:
*   [Question 1]
*   [Question 2]
**Deliverable**: [Specific output for this topic]

#### Topic 2: [Topic Title] ([Priority])
...

### Part B: [Category Name - e.g. Future State]

#### Topic X: [Topic Title] ([Priority])
**Objective**: ...
**Context**: ...
**Specific Questions**:
*   ...
**Deliverable**: ...

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
*   **Boundary**: [e.g., No external API calls, Internal Codebase Only, etc.]
*   **Timebox**: [e.g., 5-10 minutes]

### B. Assumptions
*   **[Assumption Item]**: [e.g., The provided master.csv is the source of truth for schema...]

### C. Methodology "Hierarchy of Truth"
Define how to resolve conflicts between sources:
1.  **Code** (`components/...`) — [Role, e.g. Highest Authority (Intent)]
2.  **Data** (`storage/...`) — [Role, e.g. Secondary Authority (Reality)]
3.  **Documentation** (`docs/...`) — [Role, e.g. Tertiary Authority (Context)]

---

## IV. CROSS-TOPIC INTEGRATION
*Force the researcher to synthesize, not just list facts.*
*   **Integration Question 1**: How does Topic 1 impact Topic 2?
*   **Gap Analysis**: What is missing in Current State to support Future State?

---

## V. INPUT PACKET (CONTEXT MAP)
*Mandatory section to reduce context-loading time. Point to EXACT files.*

### A. Core Governance
*   SSOT: `[path to sps]`
*   Plan: `[path to plan]`

### B. Canonical Codebase (Authoritative)
*   `[path to file 1]`
*   `[path to file 2]`

### C. Reference Data / Artifacts
*   `[path to sample csv]`
*   `[path to log file]`

### D. Anti-Patterns / Exclusions
*   **IGNORE**: `[path to legacy/backup folders]` - Do not read.

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt\templates\researcher\template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1.  **Section I (Exec Summary)**: [Specific instruction]
2.  **Section III (Topic Findings)**:
    *   **Topic 1**: [Specific format requirement, e.g. Diagrams]
3.  **Completeness**: Do NOT delete empty sections. If a topic has no implications, explicitly state "None".

---

## VII. ISSUES & RISKS REGISTER (T102-ADR-007)

The research report MUST include an “Issues & Risks” section that implements `T102-ADR-007 (Issues & Risks Index)` exactly.

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**ID Rules**
*   IDs MUST use the scoped, sequential format: `<SCOPE_ID>-ISSUE-###` and `<SCOPE_ID>-RISK-###` (e.g., `T801A-ISSUE-001`).
*   IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (E-RID MAPPING)
*Map research findings to the specific governance artifacts they inform.*

*   **[GOV-ID]**: Topic 1 findings will define this interface.
*   **[GOV-ID]**: Topic 2 findings will provide this guidance.

---

## IX. SUCCESS CRITERIA
*   [Criterion 1]
*   [Criterion 2]
