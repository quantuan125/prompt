---
artifact_type: 'SPS'
initiative_id: 'T102'
initiative_code: ''
version: '1.0.0'
date: '2025-08-16'
status: '<draft|review|approved|deprecated>'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---


### B. Initiative Considerations

<!-- HOW TO ADD AN ITEM TO III‑B (S4)
1) Pick the right subsection using the boundary rules:
   - Assumption = believed-true, not confirmed.
   - Constraint = non-negotiable limit.
   - Quality Goal/Success Signal = measurable “what good looks like” at initiative level (NOT story ACs).
   - Dependency & Interface = external actor/system/contract or role handoff.
   - Implementation Guidance = internal “how we author/operate” rules.
   - Notes & Parking Lot = context/questions/out-of-scope; mandatory and groomed.
   - Initiative GDR Index = 
2) Create an ID with the right prefix and 2-digit counter:
   - [IID]-ASSUM-## | [IID]-CON-## | [IID]-QG-## | [IID]-DEP-## | [IID]-IG-## | [IID]-NOTE-##
3) One line (≤ 25 words). Be atomic; add a brief rationale if useful.
4) Constraint vs Dependency quick test: if within our control and mandatory → Constraint; if external commitment/contract → Dependency.
5) Initiative GDR Index
   - Use table columns exactly as listed (automation relies on them).
   - ID pattern: T102-GDR-#### (initiative); 
   - Anchor: lower-kebab, e.g., {#t102-gdr-0002-title}.
   - Body structure: Context → Decision → Consequences → References (governance only; no technical ADR content).
Examples:
- T102-CON-03 Review SLA ≤2 business days. (Keeps gates flowing)
- T102-ASSUM-05 Client will use Markdown/YAML editors.
- T102-QG-04 ≥90% sections pass validator on first pass.
- T102-DEP-03 Planner consumes Concept handoff schema v1.
- T102-IG-09 Approvals listed in document body, not YAML.
- T102-NOTE-02 Consider consolidating validation logs at epic level.
-->

#### 1. Project Assumptions
<!-- Believed‑true, not yet verified (BABOK). -->
*[One line per item (≤25 words); prefix `[IID]-ASSUM-##`.]*

#### 2. Project Constraints
<!-- Non‑negotiable limits (policy/tech/time/cost); ISO 29148 verifiability. -->
*[List constraints; prefix `[IID]-CON-##`.]*

#### 3. Quality Goals 
<!-- Measurable “what good looks like” at initiative level; NOT story Acceptance Criteria. -->
*[List measurable goals; prefix `[IID]-QG-##`.]*

#### 4. Dependencies & Interfaces
<!-- External actors/systems/contracts; role handoffs; interface/migration dependencies. -->
*[List dependencies & interfaces; prefix `[IID]-DEP-##`.]*

#### 5. Implementation Guidance
<!-- Internal authoring/operation rules (templates, ID patterns, approvals in body). -->
*[List house rules; prefix `[IID]-IG-##`.]*

#### 6. Notes & Parking Lot
<!-- Contextual notes, questions, out‑of‑scope; mandatory container; define grooming cadence. -->
*[Capture context/backlog notes; prefix `[IID]-NOTE-##`.]*

#### 7. Initiative GDR Index 
<!-- Provide a single, auditable index of initiative-level governance decisions that guide governance, artifacts, and gates across the initiative. -->
*[Assign IDs as [IID]-GDR-###; set Client as default owner; keep governance-only decisions (no technical ADRs); use lower-kebab anchors pointing to decision bodies]*

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|--------|-------|--------|-------|-----------|------------|--------|
| [IID]-GDR-001 | <Concise governance decision title> | `Proposed/Accepted/Deprecated` | Client | YYYY-MM-DD | <IDs or —> | #[iID-gdr-001-kebab-title] | 

* **`[IID]-GDR-001` — <Concise Title> — {#[iid-gdr-001-kebab-title]}**
  - **Context**: Brief rationale and background for the governance decision.
  - **Decision**: Single-sentence decision statement (what is adopted/mandated).
  - **Consequences**: Key impacts/tradeoffs; approvals or policy implications.
  - **References**: Related considerations & rules with links/IDs reference (e.g., `T102-CON-01 (Format Requirements)`) and external or internal scopes and standards if relevant (e.g: `T101`, `T102A-SPSST`, `T102D`)


### C. Epics & Breakdown
<!-- PURPOSE:
This section is the Initiative’s Work Breakdown Structure (WBS) at the Epic level.
The SPS acts as the PID-equivalent (Initiative/Epic), Requests act as the WBS Dictionary (Feature specification),
and Concept consumes **approved** Requests. -->

<!-- PROCEDURE GUIDELINE: Decomposition Method *(authoring cues — to be formalized in `SPSPG`)*
1. Decomposition Principles
- Split by **deliverable/capability**, not by activity or role. *(WHY: aligns to WBS best practices; improves planning & ownership.)*
- A **Feature** is specified within a **single Request artifact** (that may contain multiple Stories). If a Request becomes unwieldy, split into additional Features/Requests.
- Each Feature SHALL name an **Owner**, declare **Interfaces/Dependencies** (prefer IDs), and include a 1–2 line **Purpose**.
- SPS remains free of **Story-level ACs**; **Epic-level Quality Goals** may be stated here; **FRs/NFRs/ACs** live in the Request; Concept consumes **approved** Requests.

2. Readiness & Exit Signals *(visibility only)*
- **Ready → Request (Feature-level, tracked here):** Purpose clear; Owner set; Interfaces/Dependencies listed (IDs). Mark Status = `in-request`.
- **Ready → Concept (Feature-level, tracked here):** Request **Gate R2** approved (source of truth is the Request). Mark Status = `approved` (then `in-concept` when design starts).
*[Instructions: SPS only **tracks** these states; the **criteria** live in the Request.]*

3. Status Taxonomy (Feature Register)
- `proposed`, `in-discovery`, `in-request`, `approved`, `in-concept`, `in-delivery`, `done`, `parked`
*[Instructions: Use these exact values for consistency.]*

4. Link & ID Discipline
- Canonical link form: **Repository Path + Anchor** → e.g., `../request/request_T102A-SPSST_T102_v1.0.0.md#iii-core-content`.
- Cross-epic dependencies MUST reference **IDs**; optional free-text notes may follow the ID in parentheses.

5. Change Control (Epic/Feature scope)
- Any change to the **Feature Register** requires a **Ripple Note** under the Epic (what changed, why, impact).
- If a Request exists, bump the Request **SemVer** and update its Change Log.
- Material changes to Readiness/Exit signals require Owner acknowledgment and a Status update. -->

<!-- HOW TO ADD/MANAGE EPICS
This section is the Initiative’s WBS at Epic scope. It contains:
  (a) a non‑operational Initiative WBS Map (index only), and
  (b) one Epic dossier per Epic (identity YAML + descriptive subsections + registers/logs).
The detailed HOW lives in the SPSPG; this block provides authoring cues only. -->

#### 0. Initiative WBS Map
<!-- PURPOSE: A high-level structural index of the project's scope. It shows hierarchy only; keep synchronized with Epic/Feature sections below. -->
*[Column rules: Level=1/2/3 (Initiative/Epic/Feature); PM Type ∈ {Initiative,Epic,Feature}; ID uses canonical pattern; Name is a short label.]*


| Level | PM Type | ID | Name |
| :---: | :------ | :- | :--- |

---

#### 1. `<EPIC_ID>` Epic: `<EPIC_CODE>` — <EPIC_TITLE>

```yaml
epic_id: '<EPIC_ID>'
epic_code: '<EPIC_CODE>'
epic_title: '<EPIC_TITLE>'
epic_type: '<new|existing|general>'
epic_status: '<draft|review|approved|deprecated>'
epic_owner: '<OWNER_ROLE_OR_NAME>'
```

**Purpose**
<!-- PURPOSE: State the primary goal and outcome of this Epic. -->
*[Write 1–2 short paragraphs in business language; avoid implementation detail.]*

**Scope**
<!-- PURPOSE: Define the explicit boundaries of this Epic. -->
*[Use bullets; separate clearly into In Scope vs Out of Scope.]*
- In Scope: …
- Out of Scope: …

**Governance**
<!-- PURPOSE: PM control parameters for this Epic; the detailed HOW lives in SPSPG. -->
*[Use a two‑column table. Keep items concise; link to Request for gate policy.]*

| Control Item       | Details |
| :----------------- | :------ |
| Tolerances         | (e.g., “Scope change ≤X% before re-baseline”) |
| Reporting Cadence  | (e.g., “Weekly status @ Fri 16:00 CET”) |
| Downstream Handoff | Request approval policy (see Request) |

**Inherited Considerations**
<!-- PURPOSE: Lists the most critical rules inherited from the Initiative Considerations that govern this Epic. Full inheritance is assumed. -->
*[Group rules by category; emphasize most critical inherited rules with their corresponding IDs and titles in parentheses under `Inherited Rule IDs`]*
| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |

**Epic Quality Goals**
<!-- PURPOSE: Measurable success criteria specific to this Epic. -->
*[Use IDs `[EPIC_ID]-QG-##`; keep atomic and measurable.]*

**Epic Dependencies & Interfaces**
<!-- PURPOSE: Prerequisites and contractual touchpoints specific to this Epic. -->
*[Use IDs `[EPIC_ID]-DEP-##`; include brief rationale or reference.]*

**Epic Assumptions (Optional)**
<!-- PURPOSE: Epic‑specific assumptions that are deltas vs Initiative only. Optional subheading. -->
*[Use IDs `[EPIC_ID]-ASSUM-##`; do not repeat Initiative assumptions.]*

**Epic Constraints (Optional)**
<!-- PURPOSE: Epic‑specific constraints that are deltas vs Initiative only. Optional subheading.-->
*[Use IDs `[EPIC_ID]-CON-##`; do not repeat Initiative constraints.]*

**Epic Notes & Parking Lot**
<!-- PURPOSE: Background, research, and context; keep concise. -->
*[Use IDs `[EPIC_ID]-NOTE-##`; one idea per bullet.]*

**Epic GDR Index**
<!-- Provide a single, auditable index of epic-level governance decisions that guide governance, artifacts, and gates across the epic. -->
*[Assign IDs as [EID]-GDR-###; set Client as default owner; keep governance-only decisions (no technical ADRs); use lower-kebab anchors pointing to decision bodies]*

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|--------|-------|--------|-------|-----------|------------|--------|
| [EID]-GDR-001 | <Concise governance decision title> | `Proposed/Accepted/Deprecated` | Client | YYYY-MM-DD | <IDs or —> | #[eid-gdr-001-kebab-title] | 

* **`[EID]-GDR-001` — <Concise Title> — {#[eid-gdr-001-kebab-title]}**
  - **Context**: Brief rationale and background for the governance decision.
  - **Decision**: Single-sentence decision statement (what is adopted/mandated).
  - **Consequences**: Key impacts/tradeoffs; approvals or policy implications.
  - **References**: Related considerations & rules with links/IDs reference (e.g., `T102-CON-01 (Format Requirements)`, `T102A-QG-01 (Clarity)`) and external or internal scopes and standards if relevant (e.g: `T101`, `T102A-SPSST`, `T102D`)

**Feature Register**
<!-- PURPOSE: Official list of features with canonical links to Requests. -->
*[Add rows according to the table instructions. Keep owner `Client` by default. Canonical Link = repo‑relative Request path.]*

| Feature ID | Name | Purpose (1–2 lines) | Owner | Status | Canonical Link (Request) |
| :--------- | :--- | :------------------ | :---- | :----- | :----------------------- |
| [EPIC_ID]-[FEATURE_CODE] | <Short feature name> | <Brief purpose description> | Client | `proposed, in‑discovery, in‑request, approved, in‑concept, in‑delivery, done, parked` | <../path/to/request.md> |

**Epic Issues & Risks**
<!-- PURPOSE: Log Epic‑specific issues/risks. -->
*[Add rows according to the table instructions. Keep owner `Client` by default. ID must be categorized as either an issue or risk]*

| ID | Description | Owner | Status |
| :--| :---------- | :---- | :----- |
| [EPIC_ID]-ISSUE-## / [EPIC_ID]-RISK-## | <Issue/risk description> | <Owner role/name> | `Open, In Review, Blocked, Resolved, Deferred` |

**Epic Changelog**
<!-- PURPOSE: Lightweight audit trail for scope/governance changes. -->
*[Bullets using `**YYYY‑MM‑DD** — change summary`.]*
```