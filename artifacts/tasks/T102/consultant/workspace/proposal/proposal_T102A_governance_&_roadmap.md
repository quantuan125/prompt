---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
epic_id: 'T102A'
epic_code: 'SPS'
version: '1.0.0'
date: '2026-01-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_documents:
  - 'prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md'
  - 'prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md'
target_topics:
  - 'T102A-STD-001 (Governance & Roadmap standard)'
  - 'Organization & Responsibilities baseline (III.B) and epic deltas (III.C)'
  - 'References semantics (plan files + evidence links)'
---

# PROPOSAL: Governance & Roadmap Standardization (T102A) — Org Baseline + Epic Snapshot

## I. EXECUTIVE SUMMARY

This proposal resolves recurring confusion and drift around **Governance & Roadmap** by standardizing:

1. **Where roles/responsibilities live** (initiative baseline vs epic delta).
2. **What “Scope & Ownership” means vs what “Org & Responsibilities” means**.
3. **What “References” in Governance & Roadmap is for** (links to living plans and evidence, not operational detail).
4. A revised **`T102A-STD-001`** body (ADR-004 compliant) that becomes the canonical standard for every Epic’s Governance & Roadmap section.

**Industry-aligned principle (PID/Charter practice):**
- Keep the SPS/PID view **stable and executive-readable** (governance baseline + phase gates).
- Keep the operational truth (tasks, evolving sequencing, day-to-day status) in **plan artifacts / external PM tools**, referenced from the snapshot.

## II. PROPOSAL SCOPE

### A. In scope

1. **Standard**: Proposed full text for `T102A-STD-001 (Governance Snapshot Framework)` that defines:
   - required section structure,
   - maintenance cadence,
   - boundaries between governance snapshot and living plans,
   - org baseline vs epic delta rules.
2. **Example adoption (T801)**:
   - Example `III.B` “Organization & Responsibilities (baseline)” for initiative `T801`.
   - Example `T801A` epic “Governance & Roadmap” that:
     - references the `III.B` org baseline,
     - correctly reflects **Phase 0** and **Phase 1** as described in `plan_T801A_phase0-1.md`,
     - uses “References” to link the living plan artifact.

### B. Out of scope

- Editing/patching the target SPS/Concept files in this proposal (this document provides SSOT-ready blocks only).
- Creating new external PM tooling or automation.
- Defining feature-level acceptance criteria (belongs in Feature Requests / Stories).

## III. KEY DEFINITIONS (TO REMOVE AMBIGUITY)

### A. “Scope & Ownership” vs “Organization & Responsibilities”

1. **Scope & Ownership** answers: “Who are the key people/roles for this Epic?”
   - It is a short roster: decision authority + primary coordination + technical authority.
2. **Organization & Responsibilities** answers: “For governance events, who decides vs who executes vs who must be consulted?”
   - It is a lightweight RACI-style mapping **for gates**, not a task-level breakdown.

### B. Initiative baseline vs Epic snapshot (delta model)

1. `III.B` contains **initiative baseline** roles and gate responsibilities (stable).
2. Each Epic’s Governance & Roadmap contains **epic deltas only**:
   - the Epic Lead assignment,
   - epic-specific gate touchpoints if they differ from baseline.

## IV. ACCEPTANCE CRITERIA

1. `T102A-STD-001` is written in **ADR-004 body format** with a compliant ADR index row schema and required headings.
2. `T102A-STD-001` **explicitly** defines:
   - Org baseline location (`III.B`) and epic delta rule (`III.C`).
   - Phase sequence as *indicative baseline* (no fixed dates; duration bands allowed).
   - Success checkpoints as *phase exits* (governance-level, evidence-linked).
   - References semantics (links to plans/evidence; no operational PM detail).
3. The `T801A` Governance & Roadmap example:
   - includes Phase 0 and Phase 1 consistent with `plan_T801A_phase0-1.md`,
   - includes the required roles: `Client`, `LLM_Consultant`, `LLM_Planner`, `LLM_Researcher`, `LLM_Developer`.
4. All dedicated “References” sections use **full reference style** (ID + title) for external IDs per `T102-STD-005-FR-006`.

## V. SSOT-READY INSERT BLOCKS (COPY/PASTE)

### A. Example adoption in `T801` — Initiative Org Baseline (`III.B`)

**Target file:** `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md`

**Placement:** Under `### B. Initiative Considerations` (recommended near `#### 5. Interfaces` so roles and governance touchpoints stay adjacent).

```md
#### 1. Organization & Responsibilities 

**Role Definitions**
| Actor | Role Title(s) | Decision Rights | Primary Responsibilities | Scope Notes |
| :--- | :--- | :--- | :--- | :--- |
| `Client` | Decision Owner | Approves baselines and cutover | Sets priorities; resolves scope conflicts; provides acceptance decisions | Initiative-wide |
| `LLM_Consultant` | Technical Consultant, Project Manager, Product Lead | Proposes baselines/requests; no final approval authority | Leads governance, requirements definition, and high-level project management; coordinates contributors; maintains SSOT coherence | Initiative/Epic/Feature (by assignment) |
| `LLM_Planner` | Planner | Authors implementation plans; no approval authority | Produces feature-level implementation plans and updates plan artifacts | Feature scope |
| `LLM_Researcher` | Research Analyst | No approval authority | Produces research, options, and trade-offs to support decisions | Initiative-wide |
| `LLM_Developer` | Technical Lead, Lead Engineer | No baseline approval authority; advises go/no-go | Implements changes; produces validation evidence; advises feasibility and architecture | Feature delivery |

**Governance RACI**
| Governance Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
| :--- | :--- | :--- | :--- | :--- |
| Approve Initiative baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Epic baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Feature baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Feature implementation plan | `LLM_Planner` | `Client` | `LLM_Consultant`, `LLM_Developer` | `LLM_Researcher` |
| Approve cutover | `LLM_Developer` | `Client` | `LLM_Consultant`, `LLM_Planner` | `LLM_Researcher` |
```

**How this links to `III.C` (epic Governance & Roadmap):**
- Each Epic’s `##### iv. Governance & Roadmap`:
  - references this baseline block, and
  - declares epic-specific governance execution signals via the **Phase & Gates** table (gate exits + Phase Lead).

---

### B. Example adoption in `T801A` — 

#### 1. Epic Governance & Roadmap (delta model; phase 0/1 aligned)

**Target file:** `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md`

**Target section:** `III.C.1 (Epic: T801A) → ##### iv. Governance & Roadmap`

```md
##### iv. Governance & Roadmap

<!-- Milestone-level oversight. Detailed planning lives in plan artifacts / external PM tools. -->

**Scope & Ownership**
- Gate Approver / Decision Owner (A): `Client`
- Governance / Requirements / PM Lead (R): `LLM_Consultant` (Project Manager, Product Lead; assigned to this Epic scope)
- Planning support (feature-level plans): `LLM_Planner` (Planner)
- Support: `LLM_Researcher`, `LLM_Developer`
- Org baseline (RACI): see `III.B.1 (Organization & Responsibilities)`

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | **EPIC DOSSIER FOUNDATION** | Make the epic dossier structurally correct and token-lean | `T801A` dossier clean; Feature list present; no premature E-RIDs | 1–2 sessions | `Client` | `LLM_Consultant` | `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` |
| 1 | **EPIC REQUIREMENTS & DECISIONS** | Develop Epic Requirements + governance decisions, then implement into SSOT after approval | Phase 1 proposal approved by `Client`; epic baseline established for Requests | 2–4 sessions | `Client` | `LLM_Consultant` | `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` |
| 2 | **FEATURE SPECIFICATION & AUTHORING** | Author Feature Request artifacts for all registered features | Feature Requests approved; implementation unblocked | TBD | `Client` | `LLM_Consultant` | TBD (Phase 2 plan) |
| 3 | **SANDBOX BUILD & VALIDATION** | Implement in isolated environment and validate | Sandbox evidence meets acceptance signals; no production disruption | TBD | `Client` | `LLM_Consultant` | TBD (Phase 3 plan) |
| 4 | **ACCEPTANCE & CUTOVER** | Final acceptance and explicit cutover decision | Cutover approved by `Client` with rollback controls confirmed | TBD | `Client` | `LLM_Consultant` | TBD (Phase 4 plan) |

**References**
- External PM tracking (if used): ticktick (TBD link)
- Research: `T801-RES-001 (Indicator Design Standards)`, `T801A-RES-001 (Backend TTI Architecture)`
```

#### 2. Epic Feature Register

```md
##### v. Feature Register
<!-- PURPOSE: The official list of work for this Epic. Each Feature is fully specified in its own Request artifact (the WBS dictionary). -->
| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A1` | `BACKEND` | Backend TTI Engine | Deterministic classification + scoring + structured output generation (includes isolated validation environment) | `LLM_Consultant` | `proposed` | TBD |
| `T801A2` | `PINE` | PineScript Enhancement | Improve upstream exported inputs needed for deterministic classification | `LLM_Consultant` | `proposed` | TBD |
| `T801A3` | `LLM_TRADER` | LLM_Trader System Prompt | Update system prompt to consume TTI output for trading analysis operations | `LLM_Consultant` | `proposed` | TBD |
| `T801A4` | `INTEGRATION` | Trader/LLM Integration | Update operating workflow to consume the structured output artifact | `LLM_Consultant` | `proposed` | TBD |
```
---

### C. Proposed Standards (ADR-004 compliant)

**Target file:** 
- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT_v1.1.0.md`

**Target section:** Epic ADR body under `T102A` (exact placement to follow that file’s ADR index conventions).

#### 1) Proposed Standard — `T102A-STD-001` (Epic Governance & Roadmap)

##### a) Proposed ADR index row (schema per `T102-STD-004`)

```md
| ADR ID | Title | Paired GDR | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A-STD-001` | Governance & Roadmap Snapshot | `T102A-GDR-001` | Proposed | Client | 2026-01-11 | — | #t102a-std-001-governance-roadmap-snapshot |
```

##### b) Proposed ADR body (format per `T102-STD-004`)

```md
* **T102A-STD-001 (Governance & Roadmap Snapshot) — {#t102a-std-001-governance-roadmap-snapshot}**

  **Context:** Per `T102A-GDR-001`, each Epic in an SPS must include a concise governance & roadmap snapshot that preserves traceability into living plans without importing operational planning detail into the SPS.

  **Decision:** Adopt `T102A-STD-001`, establish a single, mandatory structure and maintenance policy for every Epic subsection titled **“Governance & Roadmap”**.

  **Specification:**

    1) **T102A-STD-001-FR-001 (Canonical Placement & Title)**
       - Each Epic dossier SHALL include a subsection titled exactly: `##### iv. Governance & Roadmap`.
       - The subsection SHALL appear after `Inherited Considerations` and before `Feature Register` in the Epic dossier skeleton.

    2) **T102A-STD-001-FR-002 (Section Structure)**
       The section SHALL contain, in this order:
       - **Scope & Ownership**
       - **Phase & Gates** (table; indicative; no fixed dates)
       - **References**

    3) **T102A-STD-001-FR-003 (Scope & Ownership Rules)**
       - Scope & Ownership SHALL name the Decision Owner and the Epic Lead at minimum.
       - If present, Initiative Lead, Research Authority, and Technical Authority MAY be listed for clarity.
       - Scope & Ownership SHOULD include a single baseline reference line pointing to the initiative-level Org baseline (see `T102-STD-008`).

    4) **T102A-STD-001-FR-004 (Baseline Alignment)**
       - The initiative-level **Organization & Responsibilities** SHALL be defined in `III.B` and treated as the canonical source of truth (see `T102-STD-008 (Organisation Baseline Standard)`).
       - The Epic dossier SHALL NOT duplicate baseline RACI. Instead, the Epic’s Governance & Roadmap section SHALL:
         - reference the baseline, and
         - express epic-specific execution signals via the **Phase & Gates** table (Phase Lead and gate exits).

    5) **T102A-STD-001-FR-005 (Org & Responsibilities Boundaries)**
       - Org & Responsibilities SHALL map responsibilities only for governance events (phase/baseline approvals and handoffs).
       - Org & Responsibilities SHALL NOT include story/task-level responsibility assignment.
       - Feature lead/ownership remains a Feature Register concern (governed by `T102A-STD-002`).

    6) **T102A-STD-001-FR-006 (Phase & Gates Contract)**
       The **Phase & Gates** table SHALL use this exact schema:
       - `Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link`
       Fill rules:
       - `Phase`: numeric phase sequence starting at 0.
       - `Title`: short, Title Case; stable across minor plan revisions.
       - `Intent`: one sentence describing purpose; governance-level, not task-level.
       - `Key Exit Milestone`: one sentence describing the approval-ready exit signal (evidence-linked where possible).
       - `Duration Band`: optional band (e.g., “1–2 sessions”); SHALL be `—` if unknown.
       - `Gate Approver (A)`: the Decision Owner role for phase exit (typically `Client`).
       - `Phase Lead (R)`: the accountable coordinator for producing the exit package (typically `LLM_Consultant`).
       - `Plan Link`: repo-relative link to the plan artifact governing that phase; MAY be shared across phases, but SHOULD be split per phase over time.

    7) **T102A-STD-001-FR-007 (Operational Boundaries)**
       - Governance & Roadmap SHALL NOT contain sprint calendars, capacity plans, or WBS task breakdown.
       - Story-level acceptance criteria belong in Feature Requests and Stories, not in the Phase & Gates table.

    8) **T102A-STD-001-FR-008 (References Semantics)**
       - References SHOULD link to the external PM tracking system (if used) and evidence artifacts for gate completion (proposals/completions/validation notes).
       - References SHOULD include evidence links for checkpoint completion when available (proposal approvals, completion artifacts, validation notes).
       - References SHOULD NOT duplicate plan links already present in the Phase & Gates table.

    9) **T102A-STD-001-FR-009 (Maintenance Policy)**
       - The Governance & Roadmap snapshot SHALL be updated only when a phase gate is approved or when a material governance baseline change occurs.
       - Day-to-day schedule drift remains in plan artifacts / external PM tools referenced from the snapshot.

  **Alternatives Considered:**
  (a) Embed operational plans inside SPS — rejected (creates churn and breaks governance snapshot intent).
  (b) Remove roadmap/checkpoints from SPS entirely — rejected (reduces governance visibility and weakens handoff oversight).

  **Consequences:**
  (+) Separates stable governance snapshot from living plans while preserving traceability.
  (+) Reduces role confusion by splitting “owner roster” from “gate responsibilities”.
  (+) Enables consistent epic governance reporting across initiatives.
  (±) Requires discipline: only update the snapshot at gates/baseline changes.
  (-) Some existing epics may require refactor to align with the baseline/delta model.

  **References:**
  `T102A-GDR-001 (Governance Snapshot Standard)`,
  `T102A-GDR-002 (Governance Freeze Standard)`,
  `T102-STD-004 (Decision Records Index)`,
  `T102-STD-005 (ID Specification & Rules)`,
  `T102-STD-008 (Organisation Baseline Standard)`,
  `T102A-STD-002 (Feature Register Standard)`,
  `T102-RES-002 (Roadmap Viability)`,
  `T102A-RES-001 (SPS Workflow Optimization)`

  **Provenance**
  `concept_T102-CONSULTANT.md`
  `report_T102-CONSULTANT_roadmap-viability.md`
  `report_T102A-SPS_sps-workflow-optimization.md`
```

#### 2) Proposed Standard — `T102A-STD-002` (Epic Feature Register)

##### a) Proposed ADR index row (schema per `T102-STD-004`)

```md
| ADR ID | Title | Paired GDR | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A-STD-002` | Feature Register Index | `T102A-GDR-001` | Proposed | Client | 2026-01-11 | — | #t102a-std-002-feature-register-index |
```

##### b) Proposed ADR body (format per `T102-STD-004`)

```md
* **T102A-STD-002 (Feature Register Index) — {#t102a-std-002-feature-register-index}**

  **Context:** Per `T102A-GDR-001 (Governance Snapshot Standard)`, each Epic dossier must be governance-readable while preserving traceability into living artifacts. Feature scope lists were previously embedded inside Governance & Roadmap, causing churn and mixing governance with scope inventory.

  **Decision:** Adopt `T102A-STD-002` as the mandatory standard for Epic Feature Register placement, schema, and maintenance policy.

  **Specification:**

    1) **T102A-STD-002-FR-001 (Canonical Placement & Title)**
       - Each Epic dossier SHALL include a subsection titled exactly: `##### v. Feature Register`.
       - The subsection SHALL appear after `Governance & Roadmap` and before `Epic Requirements`.

    2) **T102A-STD-002-FR-002 (Table Contract)**
       The Feature Register table SHALL use this exact schema:
       - `ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request)`
       Fill rules:
       - `ID`: the Feature scope identifier (e.g., `T801A1`).
       - `Code`: short feature code (e.g., `BACKEND`, `PROMPT`).
       - `Title`: human-readable feature name.
       - `Purpose`: one sentence; scope-level, not design-level.
       - `Feature Lead (R)`: the responsible coordination role for the Feature (typically `LLM_Consultant`).
       - `Status`: one of the allowed status values (see `T102A-STD-002-FR-003`).
       - `Canonical Link (Request)`: repo-relative link to the Feature Request artifact once created; SHALL be `—` prior to request creation.

    3) **T102A-STD-002-FR-003 (Allowed Status Values; Minimal Set)**
       Feature Register status SHALL be one of:
       - `proposed`, `in-request`, `approved`, `in-build`, `done`, `deferred`, `dropped`

    4) **T102A-STD-002-FR-004 (Status Transition Rules)**
       - `proposed → in-request`: when a Request artifact is created (draft).
       - `in-request → approved`: when the Decision Owner approves the Request.
       - `approved → in-build`: when implementation begins.
       - `in-build → done`: when acceptance evidence exists and is recorded.
       - `* → deferred`: Decision Owner explicitly defers.
       - `* → dropped`: Decision Owner explicitly removes from scope.

    5) **T102A-STD-002-FR-005 (Change Control & Stability)**
       - Adding/removing a Feature row is a governance baseline change and MUST be traceable (proposal/completion reference).
       - Feature Register SHALL remain an index only; detailed requirements/design belong in Feature Request artifacts.

  **Alternatives Considered:**
  (a) Keep Feature Register inside Governance & Roadmap — rejected (increases churn; mixes scope inventory with governance snapshot).
  (b) Move Feature Register to Concept only — rejected (reduces visibility in the SSOT epic dossier).

  **Consequences:**
  (+) Keeps Governance & Roadmap stable while preserving scope visibility
  (+) Enforces traceability: each feature has a canonical Request link
  (±) Requires discipline to treat register changes as baseline events

  **References:**
  `T102A-GDR-001 (Governance Snapshot Standard)`,
  `T102-STD-004 (Decision Records Index)`,
  `T102-STD-005 (ID Specification & Rules)`,
  `T102-RES-002 (Roadmap Viability)`

  **Provenance:** None
```

#### 3) Proposed Standard — `T102-GDR-008` (Organisation Baseline Requirement)

##### a) Proposed GDR index row (schema per `T102-STD-004`)

```md
| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-GDR-008` | Organisation Baseline Standard | Proposed | Client | 2026-01-12 | — | #t102-gdr-008-organisation-baseline-standard |
```

##### b) Proposed GDR body (format per `T102-STD-004`)

```md
* **T102-GDR-008 (Organisation Baseline Standard) — {#t102-gdr-008-organisation-baseline-standard}**

  **Context:** Organization responsibilities are referenced across initiative and epic dossiers; without a stable baseline, actor labels drift and governance ownership becomes ambiguous.

  **Decision:** Adopt `T102-STD-008`, to mandate a single initiative-level `III.B.1 Organization & Responsibilities` baseline with a stable actor-to-role mapping and governance RACI.

  **Consequences:**
  (+) Keeps actor labels consistent across epics and feature registers
  (+) Enables governance snapshots to stay stable while plans evolve
  (±) Requires occasional baseline updates when the operating model changes

  **References:**
  `T102-GDR-003 (Inheritance Model Standard)`, `T102-GDR-001 (Operating Model Standard)`
```

#### 4) Proposed Standard — `T102-STD-008` (Initiative Org Baseline)

##### a) Proposed ADR index row (schema per `T102-STD-004`)

```md
| ADR ID | Title | Paired GDR | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-STD-008` | Organisation Baseline Index | `T102-GDR-008` | Proposed | Client | 2026-01-12 | — | #t102-std-008-org-baseline-index |
```

##### b) Proposed ADR body (format per `T102-STD-004`)

```md
* **T102-STD-008 (Organisation Baseline Index) — {#t102-std-008-org-baseline-index}**

  **Context:** Per `T102-GDR-008 (Organisation Baseline Standard)`, the initiative requires a stable org baseline so epic governance snapshots can reference consistent actor labels and decision rights without duplication or drift.

  **Decision:** Adopt `T102-STD-008` to standardize the structure and maintenance policy of the initiative-level `III.B` “Organization & Responsibilities” subsection.

  **Specification:**

    1) **T102-STD-008-FR-001 (Canonical Placement)**
       - Each initiative SPS SHOULD include `III.B.1 Organization & Responsibilities` (baseline) as the canonical governance role mapping for the initiative.
       - Epics SHALL reference this baseline rather than duplicating it (see `T102A-STD-001`).

    2) **T102-STD-008-FR-002 (Required Content)**
       The baseline subsection SHALL contain, in this order:

       (a) **Role Definitions**
       - A single combined table that maps *actors* to conventional role titles and governance semantics.
       - The Role Definitions table SHALL use this exact schema:
         - `Actor | Role Title(s) | Decision Rights | Primary Responsibilities | Scope Notes`
       - `Role Title(s)` SHOULD use conventional PID/charter labels (e.g., Sponsor/Decision Owner, Project Manager, Product Lead, Technical Lead, Planner).
       - The table SHALL include every *actor label* referenced anywhere else in the initiative SPS (including all epic `##### iv. Governance & Roadmap` and `##### v. Feature Register` sections).
       - Minimum required actors (may be extended per initiative, but not omitted):
         - `Client`
         - `LLM_Consultant`
         - `LLM_Planner`
         - `LLM_Researcher`
         - `LLM_Developer`

       (b) **Governance RACI**
       - A RACI table with the exact column schema:
         - `Governance Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed)`
       - The table SHALL include, at minimum, these governance activities (row titles may be adapted, but intent must remain):
         - Approve Initiative baseline
         - Approve Epic baseline
         - Approve Feature baseline (Feature Request)
         - Approve cutover
       - Rows MAY be added for initiative-specific governance (e.g., “Approve architecture baseline”, “Approve data migration plan”), but SHOULD be kept stable and baseline-level.
       - RACI cells SHALL reference actors using the exact actor labels defined in the Role Definitions table above (no new actor labels introduced only inside the table).

    3) **T102-STD-008-FR-003 (Maintenance Policy)**
       - Update the baseline only when roles/responsibilities materially change.
       - Treat baseline edits as governance changes; maintain traceability via proposal/completion references where applicable.

  **Alternatives Considered:**
  (a) Embed governance RACI inside each epic — rejected (duplication and drift).

  **Consequences:**
  (+) Reduces drift by enforcing a single baseline
  (+) Improves consistency across epics within an initiative
  (±) Requires initial discipline to keep epics delta-only

  **References:**
  `T102-GDR-008 (Organisation Baseline Standard)`,
  `T102-GDR-003 (Inheritance Model Standard)`,
  `T102-STD-003 (Explicit Inheritance Model)`,
  `T102-STD-004 (Decision Records Index)`,
  `T102-STD-005 (ID Specification & Rules)`

  **Provenance:**
  - `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102A_governance_&_roadmap.md`
```

---

## VI. IMPLEMENTATION PLAN (HIGH-LEVEL)

1. Update this proposal as the SSOT blueprint:
   - Consolidate `##### iv. Governance & Roadmap` into **Scope & Ownership** + **Phase & Gates** + **References**.
   - Mandate `##### v. Feature Register` and adopt `T102A-STD-002` minimal status set.
   - Standardize `III.B.1 Organization & Responsibilities` to a single combined **Role Definitions** mapping table (Actor → conventional Role Title(s) + Decision Rights) and include `LLM_Planner`.
   - Introduce `T102-GDR-008` and re-pair `T102-STD-008` to `T102-GDR-008` (remove incorrect pairing to `T102-GDR-003`).
2. Apply governance standards into initiative SSOT templates:
   - Update target SSOT file(s) to reflect the consolidated Governance & Roadmap and separated Feature Register (next target: `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md`).
3. Promote standards into `T102` governance:
   - Update `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` to include `T102A-STD-001` updates, add `T102A-STD-002`, add `T102-GDR-008`, and update `T102-STD-008`, ensuring DR index schemas conform to `T102-STD-004`.
   - Implement `T102-GDR-008` under `III.B.9` in `prompt/artifacts/tasks/T102/consultant/sps/archive/sps_T102-CONSULTANT_v1.1.0.md` (and update any downstream ADR contexts if the governing GDR changes status/supersedes per `T102-STD-004-FR-007`).
