---
artifact_type: 'PLAN'
initiative_id: 'T801'
epic_id: 'T801A'
epic_code: 'TTI'
version: '1.20.0'
date: '2026-01-10'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CONSULTANCY PLAN: `T801A` Epic Foundation Establishment (`TTI`)

## I. EXECUTIVE SUMMARY

This plan defines the consultancy workflow to establish a **lean, traceable foundation** for Epic `T801A (TTI)` inside the initiative SSOT:
- SSOT file: `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md`

**Role boundary**
- `LLM_Consultant`: requirements analysis, governance mapping, proposal drafts, approval gates
- `LLM_Developer`: SSOT implementation and any codebase work (post-approval)
- `Client`: decision owner and approval authority

**Phasing intent**
- **Phase 0**: make the SSOT epic dossier structurally correct + minimal; no Epic Requirements (E-RIDs) authored yet.
- **Phase 1**: develop Epic Requirements (`QG/DEP/ASSUM/CON/IF/IG`) + epic governance decisions (`GDR/ADR`) and then implement into SSOT after approval.
- **Phase 2 (preview)**: author Feature Request artifacts for `T801A1–T801A3` and link them from the Feature Register.

---

## II. CONTEXT MATERIALS & PREREQUISITES

### A. Required Reading Before Each Phase

**CRITICAL**: Before proceeding with any consultancy task in this plan, LLM_Consultant MUST review the following materials to maintain contextual understanding:

**Initiative Governance**:
- `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` — ID specification standards (T102-STD-004/005)
- `documentation/general.md` — Master governance document for entire repository

**Structural Exemplars** (T810 GASTRO as reference):
- `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md` — SPS structure and Epic dossier pattern
- `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md` — Concept structure and ADR patterns

**T810 Workspace Governance** (for proposal/completion structure):
- `prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md` — Plan/Proposal/Completion artifact roles
- `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A1/proposal_T810A1-PROMPT_phase1.md` — Proposal structural exemplar

**Current Work in Progress**:
- Conversation history from this session (contains Draft Problem Statement)
- `components/tv_ingest/data/BINANCE_BTCUSDT/master.csv` — Current CSV data structure
- `prompt/roles/VPA/main_v2.1.md` — LLM_Trader system prompt with TTI protocol

**Decision Record Standards** (MANDATORY for Phase 1):
- T102-STD-004: Decision Records Index (schema, body format, placement)
- T102-STD-005: ID Specification & Rules (categories, hierarchy, referencing)

**Research Integration Analysis** (Subphase 1.0 source):
- `prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-SYSTEM_research-integration.md` — Cross-research findings mapped to E-RIDs

### B. Working Assumptions

1. **Hybrid Architecture**: Backend provides deterministic TTI calculation → LLM_Trader interprets + adds contextual nuance
2. **Backward Compatibility**: Parallel playground development; existing system remains operational
3. **Research-Gated Design**: File format, PA detection, scoring system require research before detailed design
4. **Component Integration**: tv_ingest backend is the implementation foundation

### C. Role Boundaries: LLM_Consultant vs LLM_Research

**CRITICAL DISTINCTION**: Research and consultancy have distinct, non-overlapping responsibilities. This boundary MUST be maintained throughout Phase 1.

#### LLM_Research Responsibilities (Forward-Looking)

| Scope | Description | Example |
|:------|:------------|:--------|
| **Industry Standards Research** | Investigate industry-standard practices, comparative analysis | "What are industry-standard numeric scales for trend scoring?" |
| **Technical Feasibility Analysis** | Assess implementation approaches, trade-offs, complexity | "Can MSB/CHOCH/BOS be reliably detected algorithmically?" |
| **Comparative Recommendations** | Recommend options with pros/cons tables | "JSON vs YAML vs Markdown for TTI file format" |
| **Implementation Guidance** | Provide technical specifications, pseudo-code | "Swing point detection algorithm pseudo-code" |
| **Cross-Topic Integration** | Synthesize how research topics interact within a single brief | "How does scoring system influence file format schema?" |

**Research reports are FORWARD-LOOKING**: They inform decisions, NOT prescribe governance mappings.

#### LLM_Consultant Responsibilities (Governance & Integration)

| Scope | Description | Example |
|:------|:------------|:--------|
| **E-RID/E-GDR/E-ADR Mapping** | Infer governance implications from research findings | "Topic 1 findings → T801A-QG-001, T801A-ASSUM-001" |
| **Cross-Research Coordination** | Integrate findings from multiple research briefs | "T801-RES-001 timeframe matrix informs T801A scoring weights" |
| **Client Consultancy Dialogue** | Socratic inquiry to develop requirements | "What does deterministic consistency mean in practice?" |
| **Governance Artifact Creation** | Create E-RIDs, E-GDRs, E-ADRs with client approval | "Draft T801A-GDR-002 (Numeric Scoring Foundation)" |
| **Research-to-Governance Translation** | Translate research recommendations into governance decisions | "Research recommends JSON → GDR: Adopt JSON as file format standard" |

**Consultants are BACKWARD-INTEGRATING**: They map research findings to governance artifacts.

---

## III. PHASE 0: EPIC DOSSIER FOUNDATION (LEAN)

**Objective**: Update the SSOT so `III.C (Epics & Breakdown)` includes a correct, compact dossier for `T801A (TTI)` that downstream agents can consume without excessive token cost.

**Constraint**: Phase 0 MUST NOT author Epic Requirements (E-RIDs) in SSOT.

### Phase 0 Activities

#### A. Correct SSOT Structure + Naming

**File**: `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md`

**Action**
1. Confirm `III.C.0 (Initiative WBS Map)` includes `T801A | TTI` as a structural index entry.
2. Replace `III.C.1 (T801A)` content to remove unrelated residue and align the Epic name to `TTI — Timeframe Trend Identification`.
3. Replace everything under `III.C.1` EXCEPT `III.C.1.vi (Epic Research & Notes)` (retain existing content unchanged).

#### B. Insert Minimal Epic Content (No E-RIDs)

Populate only minimal content for:
- `III.C.1.i (Purpose)` — 1 short paragraph + ≤3 bullets
- `III.C.1.ii (Scope)` — In-scope / out-of-scope bullets (MVP boundaries only)
- `III.C.1.iii (Inherited Considerations)` — references only (no duplicated text)
- `III.C.1.iv (Governance & Roadmap)` — ownership + feature register + phases + checkpoints
- `III.C.1.v (Epic Requirements)` — placeholder headings only (Phase 1 populates)
- `III.C.1.vii–ix` — empty placeholders (tables) only

#### C. Feature Register (Phase 0)

In `III.C.1.iv`, include `T801A1/T801A2/T801A3` as `proposed` with `TBD` canonical Request links:
- `T801A1 (BACKEND)` — deterministic engine + structured output (includes isolated validation environment)
- `T801A2 (PINE)` — upstream input enrichment
- `T801A3 (INTEGRATION)` — operating workflow consumption updates

### Phase 0 Success Criteria (Checklist)

- [ ] `III.C.0` includes `T801A | TTI`
- [ ] `III.C.1` is free of unrelated residue (e.g., “Gastro”, `T810A-*`)
- [ ] Epic dossier remains compact (token budget honored)
- [ ] Feature Register includes `T801A1–T801A3` as `proposed`
- [ ] `III.C.1.v (Epic Requirements)` is placeholders only (no E-RIDs in Phase 0)
- [ ] `III.C.1.vi (Epic Research & Notes)` is unchanged

---

## IV. PHASE 1: EPIC REQUIREMENTS & DECISIONS

**Objective**: Develop all Epic Requirements (E-RIDs) and key governance decisions for `T801A`, using structured inquiry + research integration, then implement into SSOT after Client approval.

**Duration**: 120–180 minutes (consultancy dialogue; excludes engineering implementation time)

### Phase 1 Subphases (Consolidated)

| Subphase | Name | Objective |
|:---------|:-----|:----------|
| **1.0** | Phase 1 Initialization | Confirm research scope/findings (complete) and initialize the Phase 1 proposal skeleton (hard gate before Subphase 1.1) |
| **1.1** | E-RID Development | Consolidated consultancy dialogue for all E-RID categories (QG, DEP, ASSUM, CON, IF, IG) |
| **1.2** | Epic Governance Decisions | Develop E-GDRs + paired E-ADR references |
| **1.3** | Assessment & Finalization | Research integration, risk assessment, cross-category compliance review, and proposal finalization |
| **1.4** | Client Approval & SSOT Implementation | Formal approval gate + SSOT insertion (dual-gate checkpoint) |

---

### Subphase 1.0: Phase 1 Initialization

#### Activity 1.0.1: Research Integration (Complete)

**Status**: ✅ Complete

**Deliverable**: `prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-SYSTEM_research-integration.md`

**Research Registered**:
- `T801-RES-001 (Indicator Design Standards)` — Initiative-level
- `T801A-RES-001 (Backend TTI Architecture)` — Epic-level

#### Activity 1.0.2: Proposal Initialization (Skeleton First)

**Purpose**: Initialize the Phase 1 proposal file as the **single working communication channel** for Subphase 1.1 onward (live note capture + future normative bodies), without prematurely authoring full E-RID/GDR/ADR bodies.

**Hard Gate**: Subphase 1.1 MUST NOT begin until this proposal skeleton exists.

##### Task 1.0.2.1: Create proposal file stub

- **File (deliverable)**: `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md`

**Inputs required to initialize the proposal**
- Current plan: `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md`
- Prior detailed plan (reference source): `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md`
- Research integration baseline: `prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-SYSTEM_research-integration.md`
- Workspace governance rules: `prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md`
- Target SSOT: `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md`
- Current operator protocol (integration impact surface): `prompt/roles/VPA/main_v2.1.md`

**Initialization rules**
- Proposal MUST include: (1) Phase 1 executive summary, (2) candidate ID inventories, (3) working dialogue notes sections, (4) “open questions” register, (5) approval gate checklist, (6) changelog.
- Proposal MUST NOT include finalized E-RID/GDR/ADR bodies at initialization time (Subphase 1.3 writes full bodies).
- Working notes sections are allowed, but MUST be clearly labeled as non-normative; normative text lives in the E-RID/GDR/ADR body sections.

##### Task 1.0.2.2: Create from skeleton template (create as-is, then edit during Phase 1)
```markdown
---
artifact_type: 'PROPOSAL'
initiative_id: 'T801'
epic_id: 'T801A'
epic_code: 'TTI'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md'
analysis_reference: 'prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-SYSTEM_research-integration.md'
governance_rules: 'prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md'
target_document: 'prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md'
target_section: 'III.C.1 (Epic: T801A)'
---

# PHASE 1 PROPOSAL: `T801A / TTI` — Epic Requirements & Governance

## I. EXECUTIVE SUMMARY

## II. CANDIDATE INVENTORY (WORKING INDEX; NOT FULL BODIES)
<!-- PURPOSE: Single index of IDs we will validate; keep summaries to 1 line each. -->

### A. Assumptions (T801A-ASSUM-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|

### B. Constraints (T801A-CON-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|

### C. Quality Goals (T801A-QG-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|

### D. Dependencies (T801A-DEP-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|

### E. Interfaces (T801A-IF-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|

### F. Implementation Guidance (T801A-IG-###)
| ID | Title | 1-line Summary | Source | Status | Spec Reference |
|:---|:------|:---------------|:-------|:-------|:---------------|

## III. E-RID BODIES (NORMATIVE; POPULATED IN SUBPHASE 1.3)
<!-- PURPOSE: This section becomes the canonical spec during the phase. -->

### A. Assumptions (T801A-ASSUM-###)
### B. Constraints (T801A-CON-###)
### C. Quality Goals (T801A-QG-###)
### D. Dependencies (T801A-DEP-###)
### E. Interfaces (T801A-IF-###)
### F. Implementation Guidance (T801A-IG-###)

## IV. EPIC GOVERNANCE DECISIONS (E-GDR) + ARCHITECTURAL REFERENCES (E-ADR)

### A. E-GDR Index
| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|

### B. E-GDR Bodies (NORMATIVE; POPULATED IN SUBPHASE 1.3)

### C. E-ADR Index (Reference Links)
| ADR ID | Title | Paired GDR | Status | Canonical Link |
|:-------|:------|:-----------|:-------|:---------------|

## V. CONSULTANCY DIALOGUE NOTES (WORKING; NON-NORMATIVE)
<!-- PURPOSE: Capture raw dialogue so nothing is lost; convert into normative bodies above. -->

### A. DEP Dialogue Notes
### B. CON Dialogue Notes
### C. ASSUM Dialogue Notes
### D. QG Dialogue Notes
### E. IF Dialogue Notes
### F. IG Dialogue Notes

## VI. OPEN QUESTIONS REGISTER (WORKING)
| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:---|:------|:---------|:------|:-------|:--------------|:-------------|

## VII. APPROVAL GATE (CLIENT)
- [ ] All E-RIDs approved
- [ ] All E-GDRs approved
- [ ] Open questions resolved or explicitly deferred with rationale

## VIII. CHANGELOG
```

---

### Subphase 1.1: E-RID Development (Consolidated)

**Objective**: Develop all Epic Requirements through structured Socratic dialogue per category, using research findings as a starting point while discovering additional requirements through Client inquiry.

**Critical Principle**: Research/analysis provides suggested E-RIDs as a **starting point**; full Socratic dialogue per category is **mandatory** to ensure comprehensive coverage beyond research suggestions.

**Hard Gate**: This subphase MUST run “with the proposal open” (Activity 1.0.2). The proposal file is the live note capture + working index during dialogue.

**Compliance**
- **ID Compliance**: All RID/GDR/ADR bodies MUST follow `T102-STD-005-FR-005 (ID Title & Construction)` (`prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`).

#### A. Category Dialogue Method (Applies to Each Category)

The consolidated E-RID Development subphase follows a **three-task execution sequence** per category:

**Research Baseline Presentation**
- Present research-derived E-RID candidates for the category
- Summarize key research findings informing each candidate
- Note any gaps or areas where research is incomplete

**Socratic Dialogue (Full Inquiry)**
- Conduct **≥2 clarifying questions** per category to discover missing requirements
- Explore edge cases, stakeholder concerns, and operational realities
- Validate research assumptions through Client perspective
- Identify any requirements NOT covered by research

**Confirmation & Refinement**
- Confirm final E-RID specifications with Client
- Refine wording based on dialogue outcomes
- **Populate proposal file** with confirmed E-RID bodies (Section III) and dialogue notes (Section V) for the category
- Update candidate inventory (Section II) with status "confirmed"
- Mark category as "confirmed pending cross-category review"

#### B. Category Sequence (Dialogue Order)

Baseline derived from `prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-SYSTEM_research-integration.md`, extended to include Interfaces (IF), updated through dialogue refinement.

| Order | Category | Candidate Count | Dialogue Focus |
|:------|:---------|:----------------|:---------------|
| **1** | Dependencies (DEP) | 4 confirmed (3 research + 1 ASSUM-derived) | Integration points, ownership, timing, cross-category implications |
| **2** | Constraints (CON) | 4 confirmed | Non-negotiable boundaries, MVP scope limits (2 reclassified to IG) |
| **3** | Assumptions (ASSUM) | 6 confirmed | Platform reliability, operational acceptance, scoring/PA feasibility, volume integration, LLM performance |
| **4** | Quality Goals (QG) | 8 confirmed (6 research + 1 ASSUM-derived + 1 dialogue-derived) | Measurable acceptance criteria, performance targets, context sufficiency, MVP simplicity |
| **5** | Interfaces (IF) | 3 confirmed (1 partial pending research) | Contracts, handoffs, sole input artifact, human-editable format, silent override, schema governance (pending T801A-RES-002) |
| **6** | Impl. Guidance (IG) | 16 confirmed (1 partial pending research) | Technical patterns generalized from research; configuration-driven rules; scoring mechanism; PA detection approach; crossover config; validation (input + output); context content baseline |

**Rationale for Sequence**: Dependencies and Constraints frame the boundaries; Assumptions test viability within those boundaries; Quality Goals define measurable success; Interfaces clarify handoffs/contracts; Implementation Guidance provides execution patterns.

#### C. Completed Activity References

**Canonical Sources** (detailed inventories and dialogue outcomes):
- **Proposal Inventory**: `proposal_T801A_phase1.md` Section II (candidate index with status)
- **Proposal Bodies**: `proposal_T801A_phase1.md` Section III (normative E-RID specifications)
- **Dialogue Notes**: `proposal_T801A_phase1.md` Section V (per-category refinement decisions)
- **Research Integration**: `analysis_T801A-SYSTEM_research-integration.md`

#### D. Completed Activities Summary

##### Activity 1.1.1: Dependencies (T801A-DEP-###)
**Status**: ✅ Complete — 4 DEP items confirmed
**Reference**: `proposal_T801A_phase1.md` Section II.D (Inventory) + Section III.D (Bodies)
**Key Outcomes**: DEP-001 (Timeframe-Correct Input), DEP-002 (tv_ingest Backend), DEP-003 (LLM_Trader Consumption), DEP-004 (Expanded Data Structure)

##### Activity 1.1.2: Constraints (T801A-CON-###)
**Status**: ✅ Complete — 4 CON items confirmed (2 reclassified to IG)
**Reference**: `proposal_T801A_phase1.md` Section II.B (Inventory) + Section III.B (Bodies)
**Key Outcomes**: CON-001 (Backward Compatibility), CON-002 (Operational Continuity), CON-003 (Manual Workflow), CON-004 (Complexity Management)

##### Activity 1.1.3: Assumptions (T801A-ASSUM-###)
**Status**: ✅ Complete — 6 ASSUM items confirmed
**Reference**: `proposal_T801A_phase1.md` Section II.A (Inventory) + Section III.A (Bodies)
**Key Outcomes**: ASSUM-001 to ASSUM-006; ASSUM-003 flagged HIGH RISK (T801A-RISK-001)

##### Activity 1.1.4: Quality Goals (T801A-QG-###)
**Status**: ✅ Complete — 8 QG items confirmed
**Reference**: `proposal_T801A_phase1.md` Section II.C (Inventory) + Section III.C (Bodies)
**Key Outcomes**: QG-001 to QG-008; QG-007 reframed to Context Sufficiency; QG-008 added for MVP Simplicity

##### Activity 1.1.5: Interfaces (T801A-IF-###)
**Status**: ✅ Complete — 3 IF items confirmed (IF-001 finalized via T801A-RES-002)
**Reference**: `proposal_T801A_phase1.md` Section II.E (Inventory) + Section III.E (Bodies)
**Key Outcomes**: IF-001 (Webhook Input Contract), IF-002 (Backend Output Contract), IF-003 (LLM_Trader Consumption)

##### Activity 1.1.6: Implementation Guidance (T801A-IG-###)
**Status**: ✅ Complete — 16 IG items confirmed (IG-014 finalized via T801A-RES-002)
**Reference**: `proposal_T801A_phase1.md` Section II.F (Inventory) + Section III.F (Bodies)
**Key Outcomes**: IG-001 to IG-016; GDR/ADR candidates identified for Subphase 1.2

#### E. Success Criteria (Checklist)

- [ ] All 6 E-RID categories completed via Socratic dialogue
- [ ] Proposal file exists and is used as the live working channel (candidate inventory + dialogue notes updated in-session)
- [ ] Each category has ≥2 clarifying questions answered by Client
- [ ] Research-derived candidates confirmed or refined
- [ ] Additional requirements (beyond research) captured
- [ ] All E-RIDs marked "confirmed pending proposal"

---

### Subphase 1.2: Epic Governance Decisions

**Objective**: Develop Epic Governance Decision Records (E-GDRs) with paired Architectural Decision Record (E-ADR) references.

**Compliance**
- **DR Body Compliance**: All GDR/ADR bodies MUST follow `T102-STD-004-FR-002 (Decision Records Body)` (`prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`).

**GDR/ADR Development Checklist**
- [x] Research Baseline Presentation (6 GDR candidates from analysis + IG dialogue + GAP-GDR-A)
- [x] GDR-to-E-RID Traceability Validation (each GDR references supporting E-RIDs)
- [x] Socratic Dialogue (5 clarifying questions on governance scope, pairing model, specification depth, playground scope, research timing)
- [ ] GDR Index Population (Section IV.A per T102-STD-004-FR-001)
- [ ] GDR Body Development (per T102-STD-004-FR-002: Context, Decision, Consequences, References)
- [ ] Cross-Artifact Linking (GDR→ADR adoption statements per T102-STD-004-FR-005)
- [ ] ADR-to-GDR Pairing Validation (each ADR paired with governing GDR)
- [ ] ADR Index Population (Section IV.C per T102-STD-004-FR-001)
- [ ] ADR Body Development (per T102-STD-004-FR-002: Context, Decision, Specification, Consequences, Alternatives Considered, References, Provenance)
- [ ] GDR Context Citation (ADR→GDR per T102-STD-004-FR-005)
- [ ] E-RID Cross-Reference Validation (ADR specifications reference implementing E-RIDs)
- [ ] Confirmation & Refinement

**E-GDR Candidates** (from research integration + IG dialogue):

| GDR ID | Title | Context Summary | Decision Summary | Research Basis |
|:-------|:------|:----------------|:-----------------|:---------------|
| `T801A-GDR-001` | Hybrid TTI Architecture | Current LLM-based TTI unreliable; inconsistent timeframe rule application | Adopt hybrid architecture: backend deterministic calculation → LLM interpretive layer | T801-RES-001, T801A-RES-001; Plan §II.B |
| `T801A-GDR-002` | Numeric Scoring Foundation | Subjective BEARISH/NEUTRAL/BULLISH classifications inconsistent | Adopt -2 to +2 scoring scale with defined thresholds | T801A-RES-001 §II |
| `T801A-GDR-003` | Playground-First Mandate | Daily trading operations depend on current system reliability | Mandate isolated playground for all T801A development; parallel deployment required | Plan §II.B; T801A-CON-001 |
| `T801A-GDR-004` | Backend File Format Standard | File format impacts LLM consumption, manual override, maintainability | Adopt JSON with lean schema | T801A-RES-001 §III |
| `T801A-GDR-005` | Initiative Standard Compliance | Epic T801A must align with Initiative T801 design standards | Epic SHALL comply with T801-RES-001 Initiative Standards 1-6 | T801-RES-001 §V |
| `T801A-GDR-006` | Research Baseline Adoption | Research recommendations from T801-RES-001 and T801A-RES-001 vary in prescription level | Adopt explicit baseline/flexible classification for Epic T801A development | T801-RES-001, T801A-RES-001; IG-008 |

**E-ADR Candidates** (paired with GDRs):

| ADR ID | Title | Paired GDR | Specification Summary | Research Basis |
|:-------|:------|:-----------|:----------------------|:---------------|
| `T801A-ADR-001` | Hybrid Integration Pattern | GDR-001 | Define integration pattern: file-based handoff, webhook trigger, LLM consumption protocol | T801A-RES-001 §VI |
| `T801A-ADR-002` | Scoring Algorithm Specification | GDR-002 | Define scoring formula: +1/-1 for direction, momentum, confirmation, contradiction; thresholds for each level | T801A-RES-001 §II |
| `T801A-ADR-003` | Playground Deployment Architecture | GDR-003 | Define playground infrastructure: branch strategy (minimal per QG-008) | Plan §IV.C |
| `T801A-ADR-004` | TTI File Schema | GDR-004 | Define JSON schema: schema_version, trend_score, trend_label, signals object, override fields | T801A-RES-001 §III |
| `T801A-ADR-005` | Timeframe Applicability Enforcement | GDR-005 | Define enforcement mechanism: backend validation of indicator set against matrix | T801-RES-001 §II |
| `T801A-ADR-006` | Research Baseline Specification | GDR-006 | Define mandatory baselines (SHALL) vs flexible guidances (SHOULD/MAY) from research recommendations | T801-RES-001, T801A-RES-001 |

**Note**: GDR/ADR candidates identified from research integration (analysis file Section VI) and confirmed during IG dialogue (Activity 1.1.6) and Subphase 1.2 GAP analysis. Full body development in Subphase 1.2. ADR-003 scope minimized per QG-008; GDR-006/ADR-006 added per GAP-GDR-A resolution.

---

### Subphase 1.3: Assessment & Finalization

**Objective**: Commission research for partial items, conduct risk assessment per T102-STD-007, perform cross-category compliance review per T102-STD-005/T102-STD-004, and prepare proposal for Client approval.

**File**: `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md`

**Activity Sequence**: 1.3.1 (Research Gate) → 1.3.2 (Risk Assessment) → 1.3.3 (Cross-Category Compliance) → 1.3.4 (Final Preparation)

**Compliance References**:
- E-RID Compliance: `T102-STD-005 (ID Specification & Rules)`
- E-DR Compliance: `T102-STD-004 (Decision Records Index)`
- Issues/Risks Compliance: `T102-STD-007 (Issues & Risks Index)`

#### Activity 1.3.1: Research Commission Gate

**Purpose**: Review open issues and risks identified during E-RID development (Subphase 1.1) and commission additional research to address knowledge gaps before Feature-level development.

**Trigger**: Completion of Subphase 1.1 (all 6 E-RID categories) — if any E-RID is marked "partial" or "pending research"

**Identified Research Needs (from Subphase 1.1)**:

| RES-ID | Title | Purpose | Scope | Blocking Items |
|:-------|:------|:--------|:------|:---------------|
| **T801A-RES-002** | System Architecture Research | Map current tv_ingest → LLM_Trader pipeline; document I/O contracts; propose schema governance model; define "minimal market context" | Internal research on existing system + governance proposal | IF-001 (schema governance), IG-014 (context content), QG-007 (context sufficiency) |

**T801A-RES-002 Research Topics (Foundational Baseline)**:
1. **Current System Pipeline Mapping**: Document TV webhook → tv_ingest → master.csv → LLM_Trader flow with I/O specifications at each stage
2. **Webhook Payload Structure**: Document current PineScript export format, field inventory, schema patterns
3. **Error Handling Patterns**: Document current error handling in tv_ingest backend for malformed/missing data
4. **Schema Version Governance**: Propose governance model for schema versioning between T801A1 (Backend) and T801A2 (PineScript)
5. **Minimal Market Context Definition**: Define scope of "minimal market context" for IF-002 Option B per QG-007 (Context Sufficiency)
6. **Historical Data Format**: Document requirements for expanded master.csv format supporting multi-candle data per DEP-004

**Research Commission Gate Checklist**:
- [x] Review all "partial" or "pending research" E-RIDs from Subphase 1.1
- [x] Compile research brief for T801A-RES-002 with detailed topics
- [x] Identify research execution approach (internal subagent vs LLM_Research)
- [x] Commission research and capture deliverable reference
- [x] Update proposal with research findings (v1.9.0)
- [x] Finalize "partial" E-RIDs (IF-001, IG-014) after research completion

**Completion Date**: 2026-01-05
**Research Delivered**: `prompt/artifacts/tasks/T801/research/report/report_T801A-RES-002_system-architecture-research.md`
**Analysis Created**: `prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-RES-002_system-architecture-research.md`

#### Activity 1.3.2: Risk & Open Issue Assessment

**Purpose**: Consolidate and assess all Issues & Risks per `T102-STD-007 (Issues & Risks Index)`, prioritize resolution approaches, and integrate into proposal Section VI.

**Status**: ⏳ PENDING CONSULTATION

**Reference**: 
- `prompt\artifacts\tasks\T801\consultant\workspace\proposal\T801A\proposal_T801A_phase1.md` Section VI (Issues & Risks Register)
- `prompt\artifacts\tasks\T102\consultant\concept\concept_T102-CONSULTANT.md` (T102-STD-007)

##### Task 1.3.2.1: Issues/Risks Register Review

**Consultation Scope**: Review all Issues & Risks in proposal Section VI (including items imported from T801A-RES-002 and any additional Epic-discovered items).

**Register Contents** (per T801A-RES-002):
- **8 Issues**: ISSUE-001 to ISSUE-008 (5 HIGH, 3 MEDIUM priority)
- **8 Risks**: RISK-001 to RISK-008 (3 HIGH, 5 MEDIUM priority)
- **+1 Epic Risk**: RISK-009 (Volume Integration Risk; discovered via ASSUM-003)

##### Task 1.3.2.2: Issue Resolution Consultation

**Consultation Guidelines** (per T102-STD-007-FR-002/003/007 and `prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-RES-002_system-architecture-research.md`):

1. **Status Progression**: Review each Issue and determine appropriate status:
   - `OPEN` → Item requires action; not yet being addressed
   - `IN-REVIEW` → Item actively being addressed; resolution pending
   - `RESOLVED` → Item addressed; resolution documented
   - `BLOCKED` → Item cannot progress; blocker identified
   - `DEFERRED` → Item postponed to future scope with rationale

2. **Resolution Notes Requirement** (FR-007): Populate the `Resolution Notes` column:
   - If `Status = IN-REVIEW`, notes are proposed and unapproved resolution extracted from analysis
   - If `Status ∈ {RESOLVED, BLOCKED, DEFERRED}`, notes MUST include finalized summary + back-ticked governing IDs

3. **Priority-Based Review**:
   - **HIGH Priority**: Require explicit resolution strategy or deferral rationale
   - **MEDIUM Priority**: May be deferred to Feature scope with documented rationale

4. **E-RID Impact Assessment**: For each Issue, identify:
   - Which E-RIDs/E-DRs govern the issue (to be cited by the Issue row; see `T102-STD-005-FR-010`)
   - Whether resolution requires modifying governing E-RIDs/E-DRs (note: governing items MUST NOT reference Issue/Risk IDs)

**Execution Checklist** — ✅ COMPLETE (2026-01-06):
- [x] Review all 8 Issues in proposal Section VI
- [x] Classify each Issue: 4 RESOLVED, 4 DEFERRED
- [x] Populate Resolution Notes with governing E-RID citations
- [x] Populate Resolution Dates (ISO-8601)
- [x] Create Feature-Level subsection per T102-STD-007-FR-009
- [x] Promote ISSUE-007/008 to `T801A2-ISSUE-001/002`
- [x] Update proposal changelog (v1.10.0)

**Outcome**: Proposal updated v1.9.0 → v1.10.0

##### Task 1.3.2.3: Risk Mitigation Consultation

**Consultation Guidelines** (per T102-STD-007-FR-004/005/008 and `prompt/artifacts/tasks/T801/consultant/workspace/analysis/analysis_T801A-RES-002_system-architecture-research.md`):

1. **Status Progression**: Review each Risk and determine appropriate status:
   - `OPEN` → Risk identified; mitigation not yet planned
   - `MONITORED` → Risk tracked; mitigation plan in place
   - `MITIGATED` → Risk reduced to acceptable level
   - `ACCEPTED` → Risk acknowledged; no mitigation (with rationale)
   - `CLOSED` → Risk no longer applicable

2. **Mitigation Notes Requirement** (FR-008): Populate the `Mitigation Notes` column:
   - If `Status = MONITORED`, notes are proposed and unapproved mitigation extracted from analysis
   - If `Status ∈ {MITIGATED, ACCEPTED, CLOSED}`, notes MUST include finalized summary + back-ticked governing IDs

3. **Priority-Based Review**:
   - **HIGH Priority**: Require explicit mitigation strategy or acceptance rationale from Client
   - **MEDIUM Priority**: May be monitored with documented trigger conditions

4. **E-RID Impact Assessment**: For each Risk, identify:
   - Which E-RIDs/E-DRs govern the mitigation (to be cited by the Risk row; see `T102-STD-005-FR-010`)
   - Whether additional governing E-RIDs/E-DRs are needed (note: governing items MUST NOT reference Issue/Risk IDs)
   - Fallback strategies documented in related ASSUM items (cited from the Risk row)

**Execution Checklist** — ✅ COMPLETE (2026-01-06):
- [x] Review all 9 Risks in proposal Section VI
- [x] Classify each Risk: 5 MITIGATED, 2 ACCEPTED, 2 promoted to Feature
- [x] Populate Mitigation Notes with governing E-RID citations
- [x] Populate Mitigation Dates (ISO-8601) for closed statuses
- [x] Add T801A1 Feature Risks subsection
- [x] Promote RISK-006/009 to `T801A1-RISK-001/002`
- [x] Update proposal changelog (v1.11.0)

**Outcome**: Proposal updated v1.10.0 → v1.11.0

##### Task 1.3.2.4: Cross-Reference Validation & Checklist Update

**Consultation Action**: Validate that Issue/Risk resolutions are properly cross-referenced:
- [x] Each Issue/Risk row cites governing E-RIDs/E-DRs via `Description` and/or `Resolution Notes` / `Mitigation Notes`
- [x] Status/date coupling satisfied per `T102-STD-007` (OPEN ⇒ notes/date = `—`; closed statuses ⇒ date present)
- [x] No E-RID/E-DR bodies reference Issue/Risk IDs (per `T102-STD-005-FR-010`)
- [x] No conflicts between Issue resolutions and confirmed E-RIDs

##### Task 1.3.2.5: Open Questions Consultation

**Consultation Action**: Review and extend proposal Section VII:
- [x] Review `proposal_T801A_phase1.md` → `## VII. OPEN QUESTIONS REGISTER (WORKING)`
- [x] Add any new OQ items discovered during Issues/Risks consultation dialogue
- [x] Confirm each OQ’s blocking impact (which E-RIDs/E-DRs it blocks) and ownership

#### Activity 1.3.3: Cross-Category Compliance Review

**Purpose**: Review and finalize all E-RIDs and E-DRs for T102 framework compliance and PID-style content quality.

**Status**: ⏳ PENDING CONSULTATION

**Reference**:
- E-RID Bodies: `proposal_T801A_phase1.md` Section III
- E-DR Bodies: `proposal_T801A_phase1.md` Section IV
- T102 Specifications: `concept_T102-CONSULTANT.md`

##### Task 1.3.3.1: E-RID T102-STD-005 Compliance Review

**Consultation Scope**: Review all 41 E-RIDs across 6 categories for T102-STD-005 compliance.

**Structural Compliance Checklist**:
- [ ] **FR-004 (Category Definitions)**: Each E-RID correctly classified per category definition
  - DEP = External condition, interface, asset, or approval required
  - CON = Non-negotiable boundary or limitation
  - ASSUM = Items believed true but not yet verified
  - QG = Measurable outcome that defines success
  - IF = Data or integration interface definitions
  - IG = Normative authoring/process guidance
- [ ] **FR-005 (ID Title & Construction)**: All IDs follow `T801A-[CAT]-###` format with 2-3 word titles
- [ ] **FR-006 (ID References)**: Cross-references use formal `ID (Title)` format in References sections
- [ ] **FR-009 (Assumption Rules)**: ASSUM items include validation method, timing, fallback, status tracking

**Content Quality Checklist** (PID-Style Standards):
- [ ] **Concise Language**: Each E-RID body ≤200 words; avoid verbose explanations
- [ ] **Formal Tone**: Use SHALL/SHOULD/MAY per RFC 2119; avoid conversational language
- [ ] **Direct Structure**: Lead with requirement statement; supporting context follows
- [ ] **No Justification Prose**: Remove "rationale" and "because" explanations from normative bodies
- [ ] **Cross-Reference Only**: No inline duplication of content from other E-RIDs

##### Task 1.3.3.2: E-DR T102-STD-004 Compliance Review

**Consultation Scope**: Review all 6 GDRs + 6 ADRs for T102-STD-004 compliance.

**GDR Compliance Checklist** (per T102-STD-004-FR-001/002/005):
- [x] **Index Schema**: GDR Index follows `ID | Title | Status | Owner | Effective | Supersedes | Anchor`
- [x] **Body Structure**: Each GDR has Context, Decision, Consequences, References
- [x] **Adoption Statement**: Decision section contains adoption statement per FR-005
- [x] **FR-006 (Anchor Stability)**: All anchors use lower-kebab format prefixed with ID
- [x] **FR-010 (Automation Linting)**: Decision bodies contain required adoption/citation patterns
- [x] **FR-012 (References Format)**: References sections use formal `ID (Title)` format per T102-STD-005-FR-006

**ADR Compliance Checklist** (per T102-STD-004-FR-001/002/005):
- [x] **Index Schema**: ADR Index follows `ID | Title | Paired GDR | Status | Canonical Link`
- [x] **Body Structure**: Each ADR has Context, Decision, Specification, Consequences, Alternatives Considered, References, Provenance
- [x] **Context Citation**: Context section begins with `Per <GDR-ID>...` per FR-005
- [x] **Specification FRs**: Specification section uses FR-### sub-IDs per `T102-STD-005-FR-004`
- [x] **FR-006 (Anchor Stability)**: All anchors use lower-kebab format prefixed with ID
- [x] **FR-012 (References & Provenance)**: References use formal format; Provenance lists source files

**Content Quality Checklist** (PID-Style Standards):
- [x] **Context**: ≤50 words; state the gap/problem only
- [x] **Decision**: ≤30 words; state what is adopted with Why/What/Benefit
- [x] **Specification**: Use numbered FR list; each FR ≤100 words
- [x] **Consequences**: Use (+)/(±)/(-) bullets; ≤5 consequences total

##### Task 1.3.3.3: Cross-Category Dependency Validation

**Consultation Scope**: Validate cross-category references are complete and bidirectional; verify OID category completeness per T102-STD-005/006.

**A. RID Cross-Category Matrix (Bidirectional)**:

| Direction | Validation Rule | Reverse Check |
|:----------|:----------------|:--------------|
| DEP→CON | Each DEP references governing CON constraints | CON bodies cite dependent DEPs |
| DEP→ASSUM | Each DEP references supporting ASSUM items | ASSUM bodies cite dependent DEPs |
| DEP→IF | Each DEP references implementing IF contracts | IF bodies cite governing DEPs |
| CON→QG | Each CON has corresponding QG validation criteria | QG bodies cite governing CONs |
| ASSUM→CON | Each ASSUM extending CON cites the CON item | — (upstream direction) |
| QG→IG | Each QG has supporting IG implementation guidance | IG bodies cite governing QGs |
| IF→IG | Each IF has corresponding IG validation/workflow | IG bodies cite governing IFs |

**B. DID Cross-Category Matrix (per T102-STD-005-FR-003)**:

| Direction | Validation Rule | Note |
|:----------|:----------------|:-----|
| GDR→ADR | Each GDR has paired ADR specification | 1:1 pairing per QG-008 |
| ADR→RID | Each ADR Specification references implementing E-RIDs | DIDs reference RIDs only |
| GDR→RID | GDR References cite governing RIDs | DIDs reference RIDs only |

**C. OID Category Completeness (per T102-STD-005-FR-004 + T102-STD-006)**:

- [ ] **RES Completeness**: All commissioned research indexed in Section VIII per T102-STD-006-FR-002
- [ ] **ISSUE Completeness**: All unresolved gaps tracked in Section VI.A per T102-STD-007
- [ ] **RISK Completeness**: All identified risks tracked in Section VI.B per T102-STD-007
- [ ] **NOTE Completeness**: Relevant non-normative context captured per T102-STD-006-FR-007/008

**D. Gap Identification Checklist**:

- [ ] No orphan RIDs (every RID referenced by at least one other RID or DID)
- [ ] No missing reverse references (bidirectional traceability complete)
- [ ] No undocumented ISSUE/RISK items from dialogue notes
- [ ] No relevant NOTE content uncaptured from dialogue notes

##### Activity 1.3.3 Success Criteria (Consolidated Checklist)

**Gate Criteria**: All items below MUST be checked before proceeding to Activity 1.3.4:

**E-RID Compliance (Task 1.3.3.1)**:
- [x] All 41 E-RIDs pass T102-STD-005 structural compliance
- [x] All E-RID bodies meet PID-style content quality standards
- [x] All cross-references valid per FR-006

**E-DR Compliance (Task 1.3.3.2)**:
- [x] All 6 GDRs pass T102-STD-004 structural compliance
- [x] All 6 ADRs pass T102-STD-004 structural compliance
- [x] All GDR→ADR pairings complete with adoption/citation statements

**Cross-Category Validation (Task 1.3.3.3)**:
- [x] RID cross-category matrix validated (bidirectional)
- [x] DID cross-category matrix validated (DIDs→RIDs only)
- [x] OID category completeness verified (RES, ISSUE, RISK, NOTE)
- [x] No orphan RIDs or missing reverse references
- [x] All Issues/Risks have appropriate status per T102-STD-007

**Issues/Risks Compliance (from Task 1.3.3.3)**:
- [x] All 17 Issues/Risks have appropriate status per T102-STD-007
- [x] All Resolution/Mitigation Notes complete for closed items
- [x] No conflicts between Issue resolutions and confirmed E-RIDs

#### Activity 1.3.4: Integration & Final Preparation

**Purpose**: Final integration check and proposal packaging for Client approval gate.

**Status**: ⏳ PENDING (after Activity 1.3.3 completion)

**Final Preparation Checklist**:
- [x] **Cross-Category Consistency**: Validate DEP, CON, ASSUM, QG, IF, IG are internally consistent
- [x] **Dependency Resolution**: Ensure dependencies between categories properly captured
- [x] **Completeness Validation**: Confirm all dialogue-discovered requirements captured
- [ ] **Executive Summary Update**: Summarize key findings, decisions, and implications
- [ ] **Proposal Version Increment**: Update to final Phase 1 version
- [ ] **Checkpoint Approval Preparation**: Ensure proposal ready for Client gate

---

### Subphase 1.4: Client Approval & SSOT Implementation

**Objective**: Finalize the Phase 1 proposal for signature, capture explicit Client approval, then implement the approved content into SSOT (SPS + Concept) in the correct locations, followed by a final end-to-end verification sweep.

**Context** (reference set; used throughout Activities below):
- **Plan (this file)**: `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` — Phase gating + execution checklist authority
- **Proposal (source of approved bodies)**: `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md` — E-RID/GDR/ADR bodies + Issues/Risks register + Approval block
- **SSOT (SPS)**: `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md` — initiative SSOT; T801A dossier insertion target
- **SSOT (Concept)**: `prompt/artifacts/tasks/T801/consultant/concept/concept_T801-TRADER.md` — ADR compendium SSOT; Epic ADR insertion target
- **Workspace governance rules**: `prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md` — Plan vs Proposal vs Completion boundaries (“don’t duplicate; link by ID”)
- **ID/Decision standards (reference)**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` — Decision record + ID discipline baseline

**Approval Scope (final)**:
- **E-RIDs**: 41 total (ASSUM 6, CON 4, DEP 4, IF 3, IG 16, QG 8)
- **E-GDRs**: 6 total (index + full bodies)
- **E-ADRs**: 6 total (implemented into Concept SSOT)
- **Epic Issues/Risks**: 17 total (8 Issues + 9 Risks)
- **Exclusion**: Do NOT implement Feature-level promoted/deferred items (e.g., `T801A1-*`, `T801A2-*`) into SPS for this subphase; keep SPS strictly Epic-level.

#### Planned Activities

##### Activity 1.4.1: Proposal Finalization (Ready-to-Sign)

**Purpose**: Complete the remaining Phase 1 packaging tasks so the proposal is internally consistent and ready for explicit Client approval.

**Target**:
- `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md`

**Task List**:
1. **Executive Summary Update**: Refresh summary to reflect final, approved scope (41 E-RIDs, 6 GDR, 6 ADR, 17 Issues/Risks) and the practical implications for Phase 2/implementation.
2. **Proposal Version Increment**: Bump proposal version and set YAML `date` consistent with the finalization day.
3. **Approval Gate Alignment**: Ensure `## IX. APPROVAL GATE (CLIENT)` explicitly matches the approval scope:
   - E-RIDs (41)
   - E-GDRs (6)
   - E-ADRs (6)
   - Epic Issues/Risks (17)
   - Open questions resolved or explicitly deferred (if none, state “None” explicitly)
4. **Open Questions Hygiene**: Remove/repair any references to non-existent OQ items (either populate them or eliminate references so there are no “phantom blockers”).

**Success Criteria Checklist**:
- [x] Proposal executive summary reflects final counts + implications
- [x] Proposal YAML `version/date/status` are consistent with changelog timing
- [x] `## IX. APPROVAL GATE (CLIENT)` lists the full approval scope (including ADRs + Issues/Risks)
- [x] No orphan references to non-existent Open Questions

---

##### Activity 1.4.2: Client Approval Capture (Single Statement Block)

**Purpose**: Capture formal approval in a simple, unambiguous statement within the proposal (so implementation is audit-friendly and not “implied”).

**Target**:
- `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md`

**Task List**:
1. Under `## IX. APPROVAL GATE (CLIENT)`, add a single approval statement block (one block, not a long section) that clearly states:
   - what is approved (41 E-RIDs / 6 GDR / 6 ADR / 17 Issues-Risks)
   - who approved (Client)
   - approval date
2. Update proposal YAML `status` to reflect approval state (if your convention supports it).

**Success Criteria Checklist**:
- [x] Proposal contains a single explicit approval statement under `## IX`
- [x] Approval statement scope exactly matches “Approval Scope (final)” above

---

##### Activity 1.4.3: SSOT Implementation — SPS (Epic Requirements + GDR + Issues/Risks)

**Purpose**: Insert approved Epic content into the SPS SSOT in the correct subsections (no placeholders remain for Phase 1 areas).

**Target**:
- `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md`

**Insertion Map (authoritative for this activity)**:
- E-RID bodies → `III.C.1.v (Epic Requirements)`
- GDR index + full bodies → `III.C.1.vii (Epic Governance Decisions)`
- Epic Issues + Epic Risks → `III.C.1.viii (Epic Issues & Risks)`
- Epic changelog update → `III.C.1.ix (Epic Changelog)`

**Task List**:
1. Populate `III.C.1.v` with the approved E-RID bodies (all six categories; total 41).
2. Populate `III.C.1.vii` with **GDR index + full GDR bodies** (6 total).
3. Populate `III.C.1.viii` with **Epic-level** Issues and Risks only (17 total). (Do not add `T801A1-*` / `T801A2-*` here.)
4. Update `III.C.1.ix` with a concise changelog entry for this subphase.
5. Increment SPS YAML `version/date` as appropriate for a material SSOT update.

**Success Criteria Checklist**:
- [x] SPS contains all 41 E-RIDs in `III.C.1.v`
- [x] SPS contains GDR index + 6 full bodies in `III.C.1.vii`
- [x] SPS contains exactly 17 Epic Issues/Risks in `III.C.1.viii` (no feature-level promoted items)
- [x] SPS epic changelog updated; SPS YAML version/date updated

---

##### Activity 1.4.4: SSOT Implementation — Concept (Epic ADR Compendium Cleanup + T801A ADR Insert)

**Purpose**: Ensure the Concept SSOT ADR Compendium is correct for T801/T801A by removing unrelated residue and inserting the approved Epic ADR bodies.

**Target**:
- `prompt/artifacts/tasks/T801/consultant/concept/concept_T801-TRADER.md`

**Insertion Map (authoritative for this activity)**:
- Epic ADR index + bodies → `III.B.2 (Epic Architectural Decisions)`

**Task List**:
1. Remove/replace unrelated content currently under `III.B.2` (e.g., `T810A` Gastro residue) so the Concept SSOT reflects the TRADER initiative.
2. Add the `T801A / TTI` Epic ADR index table entry/entries and insert the **6 E-ADR bodies** exactly as approved in the proposal.
3. Ensure each ADR includes a stable anchor matching your ADR anchor conventions.
4. Increment Concept YAML `version/date` as appropriate.

**Success Criteria Checklist**:
- [x] No unrelated (non-T801) residue remains under `III.B.2`
- [x] Concept contains ADR index + 6 full ADR bodies for `T801A`
- [x] Anchors are present and consistent
- [x] Concept YAML version/date updated

---

##### Activity 1.4.5: Subphase 1.4 Final Verification & Closeout (Cross-Doc Consistency)

**Purpose**: Perform a final, high-level verification sweep to ensure the proposal approval, SPS SSOT, and Concept SSOT are consistent and complete, then mark Subphase 1.4 done.

**Target**:
- `prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A/proposal_T801A_phase1.md`
- `prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md`
- `prompt/artifacts/tasks/T801/consultant/concept/concept_T801-TRADER.md`

**Verification Checklist** (high-level; outcome must be binary pass/fail):
- [x] Proposal `## IX. APPROVAL GATE (CLIENT)` contains the single approval statement block with correct scope
- [x] SPS contains 41 E-RIDs (and all are placed under `III.C.1.v`)
- [x] SPS contains 6 GDRs (index + full bodies under `III.C.1.vii`)
- [x] SPS contains exactly 17 Epic Issues/Risks under `III.C.1.viii` (no feature-level promoted items)
- [x] Concept contains 6 ADRs for `T801A` under `III.B.2` and no unrelated residue remains
- [x] All three artifacts have reasonable version/date consistency for the approval/implementation event

**Completion Criteria**: Subphase 1.4 is complete when all checklist items above are checked and the SSOTs reflect the approved proposal content in the correct locations.

---

## V. PHASE 2 (PREVIEW): FEATURE SPECIFICATION & AUTHORING

**Objective**: Create Feature-level Request artifacts for `T801A1–T801A3` and link them from the `III.C.1.iv (Feature Register)` canonical links.

**Constraint**: Phase 2 defines features as Requests; it does not expand SSOT into detailed design specifications.

---

## VI. CHANGELOG

- **v1.20.0** (2026-01-10): Subphase 1.4 refactor per QA:
  - Replaced Gate A/Gate B headings with activity-based structure (Planned Activities + Activity 1.4.1–1.4.5)
  - Added Subphase-level **Context** and per-activity **Target** blocks for consistent referencing
  - Corrected approval scope counts (41 E-RIDs, 6 GDRs, 6 ADRs, 17 Issues/Risks) and clarified exclusions (no feature-level promoted items in SPS)
  - Corrected SSOT placement rules (GDRs in SPS `III.C.1.vii`; ADRs in Concept `III.B.2`)

- **v1.19.0** (2026-01-06): Activity 1.3.2 execution tracking:
  - **Task 1.3.2.2**: Added execution checklist (Issue Resolution complete)
  - **Task 1.3.2.3**: Added execution checklist (Risk Mitigation complete)
  - **Next**: Task 1.3.2.4 (Cross-Reference Validation) + Task 1.3.2.5 (Open Questions)

- **v1.18.0** (2026-01-05): Subphase 1.3 restructuring + plan optimization per QA feedback:
  - **Activity Resequencing**: Activities 1.3.2 ↔ 1.3.3 swapped — Risk Assessment now 1.3.2, Cross-Category Compliance now 1.3.3 (industry-standard sequencing: Issues/Risks may affect E-RIDs)
  - **Activity 1.3.2 (Risk Assessment)**: Replaced detailed ID lists with T102-STD-007 consultation guidelines; marked PENDING CONSULTATION
  - **Activity 1.3.3 (Cross-Category Compliance)**: Added separate E-DR compliance task (T102-STD-004); added PID-style content quality standards; consolidated success criteria checklist; marked PENDING CONSULTATION
  - **Subphase Consolidation**: Subphases 1.4 + 1.5 merged into single Subphase 1.4 (Client Approval & SSOT Implementation) with dual-gate checkpoint (Gate A: Approval, Gate B: Implementation)
  - **Subphase 1.1 Optimization**: Replaced detailed candidate inventory tables (Activities 1.1.1-1.1.6) with references to proposal/analysis files per Option B (keep category sequence + dialogue focus summaries)
  - **Token Optimization**: ~2500 tokens removed from Subphase 1.1 via reference pointers
  - **Activity 1.3.2 Status**: ⏳ PENDING CONSULTATION
  - **Activity 1.3.3 Status**: ⏳ PENDING CONSULTATION
  - **Next Steps**: Execute Activity 1.3.2 consultation, then Activity 1.3.3 consultation

- **v1.17.0** (2026-01-05): Activity 1.3.1/1.3.3 completion + T801A-RES-002 integration:
  - **Activity 1.3.1 Complete**: Research Commission Gate checklist fully completed; research delivered and integrated
  - **T801A-RES-002 Delivered**: System Architecture Research report completed covering 6 topics (Pipeline Map, Webhook Contract, Storage Drift, Minimal Context, Historical Format, Schema Governance)
  - **Analysis File Created**: `analysis_T801A-RES-002_system-architecture-research.md` with raw findings + consultant synthesis
  - **16 Issues/Risks Integrated**: 8 Issues (5 HIGH, 3 MEDIUM) + 8 Risks (3 HIGH, 5 MEDIUM) from T801A-RES-002 imported to proposal Section VI
  - **Activity 1.3.1 Status**: ✅ Complete (2026-01-05) — Research delivered, partial E-RIDs finalized (IF-001, IG-014)
