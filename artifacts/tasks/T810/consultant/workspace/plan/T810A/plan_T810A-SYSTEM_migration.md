---
artifact_type: 'PLAN'
initiative_id: 'T810'
epic_id: 'T810A'
version: '1.0.0'
date: '2025-10-12'
status: 'proposal'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# T810A Epic Population Plan — Scope Elevation, GDR Alignment, Issues Triage

## 1. Context & Sources
- Epic dossier: `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md`
- Feature request (T810A1): `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md`
- Templates & rules: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`, `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` (T102-ADR-004, T102-ADR-005)
- Concept ADR index (for future ADR placement): `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md`

### 1.1 Core Implementation Standards

* **T102-ADR-004 (Decision Records Index) {#t102-adr-004-drs-index}**

  **Specification**

    1) **T102-ADR-004-FR-001 (DR Index Schema)**
    `<GDR/ADR> ID | Title | Status | Owner | Effective | Supersedes | Anchor`
       -  `ID`: Pattern T102-GDR-### (initiative GDRs), T102-ADR-### (initiative ADRs), <E-ID>-ADR-### (epic), <F-ID>-ADR-### (feature)
       -  `Title`: Descriptive name using Title Case, 2-8 words maximum for readability
       -  `Status`: {Proposed, Accepted, Deprecated}
       -  `Owner`: Field for governance authority or implementation responsibility (typically "Client") 
       -  `Effective`: ISO-8601 date (YYYY-MM-DD) when decision becomes active
       -  `Supersedes`: List of superseded IDs or — for new decisions
       -  `Anchor:` Lower-kebab format of title, stable across potential file splits

    2) **T102-ADR-004-FR-002 (Decision Records Body)**
       - Placement: Construct directly below the `DR Index Schema` table.
       - Title format: Start the body with a single list item using this exact pattern:
         Examples:
         * **T102-GDR-004 (Decision Records Standard) — {#t102-gdr-004-drs-standard}**
         * **T102-ADR-004 (Decision Records Index) — {#t102-adr-004-drs-index}**
         Rules:
         - ID: literal token at start; Title: Title Case; Anchor: lower-kebab derived from title, prefixed with the ID in lower-kebab form.
         - Keep one space before the anchor block; include braces `{#...}` exactly.
       - Shared subheadings (use bold labels with trailing periods):
         - **Context:** Why this decision is needed; the gap it resolves.
         - **Decision:** What is adopted/changed and who owns it.
         - **Consequences:** Impacts using (+)/(±)/(-) bullets.
         - **References:** Canonical links/anchors to governing rules and related items.
       - ADR additions:
         - **Specification:** Functional requirements (FR-##), constraints, and acceptance notes.
         - **Alternatives Considered:** Rejected options with rationale.
         - **Provenance:** Evidence/design sources supporting the decision.

    3) **T102-ADR-004-FR-003 (Placement Standards)**
       - SPS artifacts: Section titled "<SCOPE> Governance Decisions" containing governance decisions only
       - Concept artifacts: Section titled "<SCOPE> Architectural Decisions" with mirror sections for Epic/Feature areas as needed
       - Consistency requirement: All placement follows established artifact section numbering without local deviations

    4) **T102-ADR-004-FR-004 (Entry Creation Workflow)** Add a new row to the appropriate index table, assign the next sequential ID, and create the matching body section using the required template. 

    5) **T102-ADR-004-FR-005 (Cross-Artifact Linking)**
       - **GDR → Decision (Adoption Statement).** If a GDR formally adopts or mandates an ADR, the adoption MUST be stated in **Decision** using this informal reference pattern (single line):
          + Pattern: "Adopt `<ADR-ID>`, <one-line rationale>..."
          + Example: "Adopt `T102-ADR-004` as the single, Client-owned standard for decision record schemas across artifacts."
       - **ADR → Context (Authority Citation).** If an ADR is governed by a GDR, the governing policy MUST be cited in **Context** using this informal reference pattern as the first sentence of Context:
          + Pattern: "Per `<GDR-ID>`, <one-line rationale>..."
          + Example: "Per `T102-GDR-004`, a unified DR schema is required to prevent drift."

    6) **T102-ADR-004-FR-006 (Anchor Title Stability)**
      - **Anchor & title stability.** Use lower-kebab anchors derived from Title; anchors remain stable across file moves/splits.

    7) **T102-ADR-004-FR-007 (Lifecycle Coherence)**
      When a GDR that is cited by ADRs changes **Status** or is **Superseded**, affected ADRs MUST:
         + update the **Context** authority sentence to the new governing GDR ID/title; and
         + add the prior GDR ID to **Supersedes/References** as appropriate.
         + Perform this update in the next modification to the ADR or in a dedicated “governance sync” change set.

    8) **T102-ADR-004-FR-008 (Status Management)**
      `Proposed → Accepted → Deprecated` lifecycle; document superseded IDs in the **Supersedes** column and, in body text where applicable.

    9) **T102-ADR-004-FR-009 (Precedence Hierarchy)**
      Initiative GDR > Initiative ADR > Epic ADR > Feature ADR > Story ADR for conflict resolution. (See `T102-ADR-003` and `T102-ADR-005` for details.)

    10) **T102-ADR-004-FR-010 (Automation Linting)**
       Authors SHOULD pass the following checks:
        - GDR body contains a **Decision** line matching regex: `` `^Adopt\s+`T[0-9]{3,}(?:[A-Z][0-9A-Z]*)?-ADR-[0-9]{3}`,\s+.+$` ``
        - ADR body **Context** starts with: `` `^Per\s+`T[0-9]{3,}(?:[A-Z][0-9A-Z]*)?-GDR-[0-9]{3}`,\s+.+$` ``

    11) **T102-ADR-004-FR-011 (Consequences Scope)**
        -  **GDR Consequences:** Policy/precedence impacts; compliance expectations; migration & rollout; automation/traceability effects. 
        -  **ADR Consequences:** Quality trade-offs; constraints introduced; operational effects; debt/risks.

    12) **T102-ADR-004-FR-012 (References & Provenance )**
      - **References** in both records include formal reference following `T102-ADR-005-FR-006`
      - **Provenance** store relevant file names only. 


* **T102-ADR-005 (ID Specification & Rules) {#t102-adr-005-id-spec}**

  **Specification**

    1) **T102-ADR-005-FR-001 (ID Scope)**
      - I-ID (initiative): `^T\d{3}$` (e.g., `T102`).
      - E-ID (epic): `^T\d{3}[A-Z]$` (e.g., `T102A`).
      - F-ID (feature): `^T\d{3}[A-Z]-[A-Z0-9_]+$` (e.g., `T102A-SPSST`).
      - S-ID (story): `^T\d{3}[A-Z]-[A-Z0-9_]+-S\d+$` (e.g., `T102A-SPSST-S3`).

    2) **T102-ADR-005-FR-002 (ID Terminologies)**
      - Scope IDs: `I-ID`/`E-ID`/`F-ID`/`S-ID` are artifact identifiers (initiative/epic/feature/story), e.g., `I-ID = T102`, `F-ID = T102A-SPSST`.
      - Rule IDs: `I-RID`/`E-RID`/`F-RID`/`S-RID` are conS-IDeration/rule identifiers defined by category tokens at each scope (e.g., `T102-QG-02`, `T102A-SPSST-NFR-002`).
      - Decision Record IDs: `I-GDR`/`E-GDR`/`F-GDR`/`S-GDR` denotes governance decisions; `I-ADR`/`E-ADR`/`F-ADR`/`S-ADR` denotes architecture decision at each scope. 
      - Usage guidance: Use `<SCOPE>ID` when referring to artifact scope; use `<RULE>-ID` when referring to rule items; use `<SCOPE>-ADR/GDR` for decision records.

    3) **T102-ADR-005-FR-003 (Precedence & Directionality)**
      - Precedence: I-RIDs > I-GDRs > I-ADRs > E-RIDs > E-GDRs > E-ADRs > F-RIDs > F-GDRs > F-ADRs > S-RIDs > S-GDRs > S-ADRs.
      - Directionality: Upstream never references downstream. Lower/equal scopes MAY reference higher/equal scopes; higher MUST NOT reference lower. Variances MUST cite the overridden upstream item.

    4) **T102-ADR-005-FR-004 (ID Categories)**
      - Token map and definitions:
        - DR Category:
          - `GDR` — Governance: Policy-level governance decision record.
          - `ADR` — Architecture: Architecture/implementation decision record.
        - Main Category:
          - `ASSUM` — Assumption: Items believed true but not yet verified; inform approach and risk.
          - `CON` — Constraint: Non‑negotiable boundary or limitation that must be respected.
          - `QG` — Quality Goal: Measurable outcome that defines success (verifiable, stable).
          - `DEP` — Dependency: External condition, interface, asset, or approval required.
          - `IG` — Implementation Guidance: Normative authoring/process guidance; not a design choice.
          - `NOTE` — Note: Informational remark to aid context or authoring; non‑normative.
          - `RES` — Research: Formally commissioned research with approved brief and validated report artifacts; traceable via Research Artifacts Index per `T102-ADR-006`.
          - `ISSUE` — Open Issue: Known gap requiring decision or action; tracked to resolution.
          - `RISK` — Risk: Potential negative event with likelihood/impact; track mitigation/acceptance.
        - Sub Category
          - `FR` — Functional Requirement: Behavior the system must provide; testable acceptance.
          - `NFR` — Non‑Functional Requirement: Quality attribute (performance, security, etc.); testable.
          - `IF` — Interface: Data or integration interface definitions and contracts.
          - `INT` — Integration Note: Cross‑artifact/process integration guidance or placement rules.
      - Allowed tokens by scope
        - Initiative/Epic (I‑ID/E‑ID): `ASSUM`, `CON`, `QG`, `DEP`, `IG`, `NOTE`, `RES`, `ISSUE`, `RISK`.
        - Feature (F‑ID): additive from Epic: `FR`, `NFR`, `IF`, `INT`, `CON`, `RES`.
        - Story (S‑ID): inherits Feature tokens.
      - Universal construction: `{SCOPE_ID}-{CATEGORY}-{NNN}` for all Rule IDs and Decision Record IDs.
      - ADR sub-IDs within a decision: append `-FR-{NNN}` (e.g., `T102-ADR-003-FR-001`).

    5) **T102-ADR-005-FR-005 (ID Title & Construction)**
      - General format: `* **<ID> (<Title>)** — <concise description>` on a single line.
      - Scope: Applies to I‑ID/E‑ID/F‑ID/S‑ID items when introduced; for ADRs/GDRs use the body title pattern in `T102-ADR-004`.
      - Examples:
        - **T102-QG-001 (Client Readability)** — Artifacts are understandable by non‑technical stakeholders (aim ≥ "clear" on internal rubric).
        - **T102A-DEP-001 (Planner Integration)** — Planner consumes Concept + referenced Design Logs; align handoff schema.
        - **T102A-SPSST-NFR-002 (Author Usability)** — Section names/order intuitive for non‑technical authors.
        - **T102A-SPSST-S3-FR-001 (Epic Dossier Schema)** — Epic block includes YAML header, standardized subsections, and Feature Register.
      - Relation to DRs: For the ADR/GDR body section heading, follow `T102-ADR-004-FR-002 (Decision Records Body)` for the exact list‑item title and anchor format.

    6) **T102-ADR-005-FR-006 (ID References)**
      - Formal (References subsections; Inherited ConS-IDerations tables): back‑ticked `ID (Title)` tokens, e.g., `T102-CON-001 (Format Requirements)`.
      - Informal (inline prose): flexible between formal reference and bare back‑ticked ID tokens, e.g., `T102-CON-001`.

    7)  **T102-ADR-005-FR-007 (Migration & Stability)**
      - Keep anchors stable when moving content; deprecate IDs via index when replaced. If titles change, anchors remain unchanged.




Goal: Extract cross-cutting requirements from T810A1 that should govern all child features; promote to Epic scope (`E-RIDs`), align Epic GDR references to E-RIDs (no F-RIDs), and triage Epic Issues & Risks.

## 2. Promotion Candidates (Feature → Epic)

**Approach**: Promote Feature-level RIDs from T810A1 to Epic-level governance where they set cross-feature policy/quality bars per T102-ADR-005.

**Detailed Analysis**: See `proposal_T810A-GASTRO_phase2_v1.0.0.md` for comprehensive architectural analysis, scope justifications, and promotion rationales.

**Categories Processed**:

1. **Assumptions (→ T810A-ASSUM-###)**: Foundational platform/user assumptions applicable across all Epic features
2. **Dependencies (→ T810A-DEP-###)**: Inter-feature dependencies and Epic-level external requirements
3. **Constraints (→ T810A-CON-###)**: Platform/architectural boundaries governing entire Epic
4. **Quality Goals (→ T810A-QG-###)**: Epic-level cross-feature quality standards abstracted from Feature NFRs
5. **Implementation Guidance (→ T810A-IG-###)**: Epic-level operational patterns to operationalize Quality Goals

**ID Migration Traceability**:

*Assumptions*:
- T810A1-ASSUM-001 → T810A-ASSUM-001 (Patient Profile) [Direct]
- T810A1-ASSUM-002 → T810A-ASSUM-002 (Input Modality & Quality) [Direct]
- T810A1-ASSUM-003 → T810A-ASSUM-003 (LLM Capability) [Direct]
- T810A1-ASSUM-004 → T810A-ASSUM-004 (Platform Memory Uncertainty) [Hybrid - Epic principle]
- T810A1-ASSUM-004 → T810A1-ASSUM-004 (Session-Scoped Memory Model) [Hybrid - Feature implementation retained]

*Dependencies*:
- T810A1-DEP-001 → T810A-DEP-001 (Platform) [Direct]
- T810A1-DEP-002 → T810A-DEP-002 (Long-term Analysis) [Rewording]
- T810A1-DEP-003 → T810A-DEP-003 (Toolbox Interface) [Rewording]
- T810A1-DEP-004 → T810A-DEP-004 (Patient Data Structures) [Rewording]
- T810A1-DEP-005 → T810A-DEP-005 (Clinical Safety Framework) [Reference fix]
- T810A1-DEP-008 → T810A1-DEP-008 (Protocol Triggering Research) [Retained at Feature - demoted]

*Constraints*:
- T810A1-CON-001 → T810A-CON-001 (System Prompt Scope) [Title + content refinement]
- T810A1-CON-006 → T810A-CON-002 (Platform Compatibility) [Direct]
- T810A1-CON-007 → T810A-CON-003 (Clinical Compliance Deferral) [Reference update]
- T810A1-CON-008 → T810A-CON-004 (ChatGPT Architectural Constraints) [Content refinement]
- T810A1-CON-004 → T810A-QG-008 (Clarification Over Guessing) [Reclassified CON → QG, Epic principle]
- T810A1-CON-004 → T810A1-NFR-009 (Probe-Before-Answer Enforcement) [Reclassified, Feature implementation retained]
- T810A1-CON-002, CON-003, CON-005 [Retained at Feature - not promoted]

*Quality Goals*:
- T810A1-NFR-001 → T810A-QG-001 (Clinical Protocol Reliability) [Hybrid - Epic abstraction]
- T810A1-NFR-001 → T810A1-NFR-001 (5-Phase Protocol Execution) [Hybrid - Feature retained]
- T810A1-NFR-002 → T810A-QG-002 (Persona & Tone) [Hybrid - Epic abstraction]
- T810A1-NFR-002 → T810A1-NFR-002 (Protocol Phase Tone Mapping) [Hybrid - Feature retained]
- T810A1-NFR-003 → T810A-QG-003 (Performance) [Direct]
- T810A1-NFR-004 → T810A-QG-004 (Holistic Analysis) [Content refinement]
- T810A1-NFR-005 → T810A-QG-005 (Architecture Maintainability) [Hybrid - Epic abstraction]
- T810A1-NFR-005 → T810A1-NFR-005 (9-Block Prompt Structure) [Hybrid - Feature retained]
- T810A1-NFR-006 → T810A-QG-006 (Usability) [Major content enhancement]
- T810A1-NFR-007 → T810A-QG-007 (Confidence Communication) [Direct]
- T810A1-NFR-008 → T810A1-NFR-008 (Protocol Triggering Intelligence) [Retained at Feature - demoted]

*Implementation Guidance (NEW)*:
- T810A-IG-001 (Protocol Triggering Guidance) [Synthesized from T810A1-NFR-008, T810A1-IF-004]
- T810A-IG-002 (Probe Phase Enforcement) [Synthesized from T810A1-NFR-009, T810A1-NFR-001]
- T810A-IG-003 (Explicit Classification) [Synthesized from T810A1-IF-003, T810A1-NFR-007]
- T810A-IG-004 (Dynamic JSON Single-Entry Pattern) [Synthesized from T810A1-IF-006, T810A1-INT-004]
- T810A-IG-005 (Memory Review Protocol) [Synthesized from T810A1-INT-005]
- T810A-IG-006 (Session Context Injection & Handoff) [Synthesized from T810A1-INT-002, T810A1-IF-005]

**Summary**: 27 Epic E-RIDs created (4 ASSUM, 5 DEP, 4 CON, 8 QG, 6 IG); Feature deltas retained where implementation-specific

## 3. Epic GDR Alignment Plan (REVISED — Research-Driven Workflow)

### 3.1 Phase 3A: Research-Driven Scope Assessment — ✅ COMPLETE

**Objective**: Classify all 6 Epic GDRs as Epic-level (E-GDR) or Feature-specific (F-GDR) before individual consultations to prevent rework.

**Research Deliverable**: `prompt/artifacts/tasks/T810/consultant/workspace/T810A/analysis/analysis_T810A-SYSTEM_gdr-scope-assessment.md`

**Key Findings**:
- **F-GDR (Demote to Feature)**: GDR-001 (Tracking-First Protocol), GDR-004 (Session Workflow Architecture) — HIGH priority demotion
- **E-GDR (Retain at Epic)**: GDR-002 (Trust-and-Verify), GDR-003 (Stable/Dynamic JSON), GDR-005 (GI Knowledge Sources), GDR-006 (Dual-Purpose Reporting) — HIGH priority refinement (GDR-005 MEDIUM)
- **Epic ADRs Required**: T810A-ADR-002 (Confidence Policy), T810A-ADR-005 (GI Sources Catalog), T810A-ADR-006 (Dual-Purpose Reporting)
- **No Blocking Issues**: Immediate proceed to Phase 3B approved

**Status**: ✅ Research complete; analysis report accepted; Phase 3B ready to begin

---

### 3.2 Phase 3B: E-GDR Sequential Consultations & ADR Stub Creation

**Objective**: Revise 4 retained E-GDRs with Epic-level language; create ADR stubs for Phase 3C full drafting; address critical questions from research.

**Workspace File**: `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/proposal_T810A-SYSTEM_phase3.md`
- **Purpose**: Dynamic consultation workspace + communication channel with client for Phase 3
- **Structure Exemplar**: `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A1/proposal_T810A1-PROMPT_phase3.md`
- **Usage Pattern**: All GDR/ADR proposals drafted in proposal file → approved by client → implemented in SPS/Concept artifacts

**Sequencing**: Sequential consultation of 4 E-GDRs in priority order (HIGH → MEDIUM)
- **GDR-002** (Trust-and-Verify) — HIGH priority → ADR-002 stub
- **GDR-003** (Stable/Dynamic JSON) — HIGH priority → No ADR (uses E-IG refs)
- **GDR-006** (Dual-Purpose Reporting) — HIGH priority → ADR-006 stub
- **GDR-005** (GI Knowledge Sources) — MEDIUM priority → ADR-005 stub

**Per-GDR Consultation Workflow** (Standardized 6-Step Process):

1. **Present Research Findings** (from analysis Section VI)
   - Epic Scope Test result (PASS / NEEDS ABSTRACTION)
   - Feature applicability matrix (T810A1/A2/A3/A4)
   - Implementation details identified with handling decisions
   - E-RID mapping validation (authority, completeness, circularity, gaps)
   - Recommended revision strategy with rationale

2. **Address Critical Questions** (from analysis Section VIII)
   - GDR-002: Retain numeric confidence thresholds (70%, 90%) in ADR or remove entirely? → Research recommends Option A (retain in ADR-002)
   - GDR-003: Reference E-IG-005/006 for session init or keep inside GDR body? → Research recommends Option B (IG refs only)
   - GDR-006: "First-person voice" and "100-200 token" as Epic GDR rule or ADR guidance? → Research recommends Option B (ADR-006 guidance)
   - Cross-reference style: Allow F-RID citations or require E-RID substitution only? → Research recommends Option B (E-RID only)

3. **Client Review & Decision**
   - Confirm abstraction approach (ADR extraction vs. hybrid split vs. pure abstraction)
   - Resolve critical question for this GDR
   - Approve E-RID reference updates

4. **Draft Revised Epic GDR Language** (in proposal file)
   - Epic-level language (remove feature-specific details per research)
   - Apply consistent abstraction patterns: "Block 4" → "designated knowledge storage"
   - E-RID references only (no F-RID citations per T102-ADR-005)
   - **Target**: Concise, direct, authoritative GDR body per client guidance

5. **Draft Epic ADR Stub** (if required for this GDR)
   - **ADR Stub Components**: Title + Anchor + Content Scope Outline + Key Decisions
   - **Format Compliance**: Follow T102-ADR-004 structure (Context, Decision, Specification, Consequences, Alternatives Considered, References)
   - **Deferred to Phase 3C**: Full ADR body text with detailed specifications
   - **Target Artifact**: `concept_T810-GASTRO.md` Section III.B.1 (Epic ADR Index) after Phase 3C approval

6. **Client Approval Gate**
   - Approve revised GDR language
   - Approve ADR stub content scope (if applicable)
   - Authorize move to next GDR

**Success Criteria**:
- [ ] All 4 E-GDRs revised with Epic-level language in proposal file
- [ ] All F-RID references replaced with E-RID references
- [ ] 3 Epic ADR stubs created (ADR-002, 005, 006) with content scope definitions
- [ ] All 5 critical questions from research resolved with client decisions
- [ ] Client approval obtained for all revisions

**Time Estimate**: 60-80 minutes (15-20 min per GDR × 4 GDRs)

---

### 3.3 Phase 3C: Epic ADR Full Draft Development

**Objective**: Expand ADR stubs from Phase 3B into full Epic ADR drafts compliant with T102-ADR-004 format.

**ADR Development Sequence**:

**T810A-ADR-002 (Trust-and-Verify Confidence Policy)**
- **Content Scope** (from research Section VI + XI):
  - Qualitative tiers (high/moderate/low confidence) with example phrasings
  - Optional internal numeric ranges (70%, 90%) as guidance (NOT user-facing)
  - Image-specific classification examples
  - Cross-modality applicability assessment
  - **Explicit Prohibition**: "Numeric confidence values, when used, are internal only and must not appear in user-facing communication"
  - Alignment with T810A-QG-007 (Confidence Communication) and T810A-IG-003 (Explicit Classification)
- **Linked GDR**: GDR-002 (revised)
- **Sequencing**: Draft ADR → align with A2 schema semantics for confidence fields → validate with A1 prompt patterns

**T810A-ADR-005 (GI Knowledge Sources Catalog)**
- **Content Scope** (from research Section VI + XI):
  - Authoritative source list (ROME IV, Bristol Stool Scale, ACG/AGA Guidelines, alarm features)
  - Versioning metadata and update cadence policy
  - Source deprecation and replacement procedures
  - Maintenance governance (who updates, when, approval gates)
- **Linked GDR**: GDR-005 (revised)
- **Sequencing**: Compile v1 catalog → confirm with A1 knowledge usage → publish and link from SPS

**T810A-ADR-006 (Dual-Purpose Reporting Policy)**
- **Content Scope** (from research Section VI + XI):
  - Narrative voice mandate (first-person patient perspective: "I experienced...")
  - Length targets (100-200 tokens) as efficiency guidance
  - Content pattern (Time → Event → Symptom/Meal/Stool → Analysis Summary)
  - Trigger commands for report generation
  - Validation loop specifics for report quality assurance
  - JSON export schema format
  - A1/A3 coordination rules for handoff/aggregation
  - Ties to T810A-IG-006 (Session Context Injection & Handoff)
- **Linked GDR**: GDR-006 (revised)
- **Sequencing**: Coordinate with A3 aggregation design → finalize voice/length guidance → update A1 trigger/validation flows

**ADR Format Compliance** (T102-ADR-004):
- **Required Sections**:
  - **Context**: Why this decision is needed; the gap it resolves
  - **Decision**: What is adopted/changed and who owns it
  - **Specification**: Functional requirements (ADR-XXX-FR-###), constraints, acceptance notes
  - **Consequences**: Impacts using (+)/(±)/(-) bullets
  - **Alternatives Considered**: Rejected options with rationale
  - **References**: Canonical links/anchors to governing rules (E-RIDs, E-GDRs) and related items
  - **Provenance**: Evidence/design sources supporting the decision (research report, analysis findings)

**Target Artifact**: `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md` Section III.B.1 (Epic ADR Index)

**Success Criteria**:
- [ ] All 3 ADRs drafted with complete T102-ADR-004 sections
- [ ] ADR content aligns with GDR abstraction decisions from Phase 3B
- [ ] Cross-ADR consistency validated (no contradictions)
- [ ] ADR Index table updated in Concept artifact with proper anchors

**Time Estimate**: 20-30 minutes (3 ADRs)

---

### 3.4 Phase 3D: GDR ID Renumbering & Feature Demotion Handoff

**Objective**: Renumber 4 retained E-GDRs sequentially by priority (highest = 001); hand off 2 demoted GDRs to T810A1 subconsultant.

#### **3.4.1 GDR ID Renumbering**

**Renumbering Map** (Priority-First Sequence):
- **GDR-002** (Trust-and-Verify) → **GDR-001** (HIGH priority)
- **GDR-003** (Stable/Dynamic JSON) → **GDR-002** (HIGH priority)
- **GDR-006** (Dual-Purpose Reporting) → **GDR-003** (HIGH priority)
- **GDR-005** (GI Knowledge Sources) → **GDR-004** (MEDIUM priority)

**Renumbering Scope**:
- SPS Section III.C.1.vii (Epic Governance Decisions): Update GDR IDs in index table + body sections
- Concept Section III.B.1 (Epic ADR Index): Update ADR-GDR cross-references (ADR-001 → GDR-001, ADR-004 → GDR-004, ADR-003 → GDR-003)
- Analysis report references (informational only; no file edits required)

**Success Criteria**:
- [ ] All 4 retained GDRs renumbered in SPS with sequential IDs (001-004)
- [ ] All ADR cross-references updated to match new GDR IDs
- [ ] No broken anchor links after renumbering

#### **3.4.2 Feature GDR Demotion Handoff**

**Demoted GDRs** (from research findings):
- **GDR-001** (Tracking-First Protocol) → `T810A1-GDR-001`
- **GDR-004** (Session Workflow Architecture) → `T810A1-GDR-002`

**Demotion Rationale** (trust research recommendation per client guidance Q4):
- GDR-001: 5-phase protocol + 2-loop pattern are A1 conversational workflow, not Epic governance
- GDR-004: Step 0/1/2 session init is A1-specific prompting pattern

**Handoff Process**:
1. Extract current GDR-001/004 content from SPS (before renumbering)
2. Remove GDR-001/004 from Epic GDR section in SPS
3. Prepare for T810A1 subconsultant handoff brief (deferred to Phase 3E)
4. Document demotion in SPS changelog

**Success Criteria**:
- [ ] GDR-001/004 removed from Epic GDR section in SPS
- [ ] Demoted GDR content preserved for T810A1 handoff brief
- [ ] SPS changelog notes demotion with rationale reference to research

---

### 3.5 Phase 3E: SPS/Concept Implementation & T810A1 Coordination Brief

**Objective**: Apply all approved revisions to SPS/Concept artifacts; draft comprehensive T810A1 subconsultant handoff brief covering Phase 2 + Phase 3 changes.

#### **3.5.1 SPS Document Updates**

**Epic GDR Section Updates** (`sps_T810-GASTRO.md` Section III.C.1.vii):
- **Remove**: Original GDR-001 (Tracking-First Protocol), GDR-004 (Session Workflow Architecture) — demoted to T810A1
- **Add**: Revised GDR-001/002/003/004 (renumbered from 002/003/006/005) with Epic-level language from Phase 3B
- **References**: Update all GDR "References" subsections with E-RID formal syntax per T102-ADR-005

**SPS Changelog Entry** (Section IV):
```markdown
### v1.1.0 (2025-10-27) — Epic GDR Alignment & Feature Demotions

**Epic Governance Refinement**:
- **Demoted**: GDR-001 (Tracking-First Protocol) → T810A1-GDR-001 (Feature-specific conversational workflow)
- **Demoted**: GDR-004 (Session Workflow Architecture) → T810A1-GDR-004 (Feature-specific session init pattern)
- **Renumbered & Revised**: GDR-002 → GDR-001 (Trust-and-Verify) — Abstracted numeric thresholds to T810A-ADR-002
- **Renumbered & Revised**: GDR-003 → GDR-002 (Stable/Dynamic JSON) — Abstracted "Block 4" to "designated knowledge storage"; added E-IG refs
- **Renumbered & Revised**: GDR-006 → GDR-003 (Dual-Purpose Reporting) — Abstracted format/voice/length to T810A-ADR-006
- **Renumbered & Revised**: GDR-005 → GDR-004 (GI Knowledge Sources) — Abstracted maintenance policy to T810A-ADR-005

**Epic ADRs Created**:
- T810A-ADR-002 (Trust-and-Verify Confidence Policy)
- T810A-ADR-005 (GI Knowledge Sources Catalog)
- T810A-ADR-006 (Dual-Purpose Reporting Policy)

**Reference Compliance**: All E-GDRs now reference E-RIDs only (no F-RID citations); formal syntax per T102-ADR-005
```

#### **3.5.2 Concept Artifact Updates**

**Concept Document**: `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md`

**ADR Body Sections**: Add full ADR drafts from Phase 3C with T102-ADR-004 format compliance

**Success Criteria**:
- [ ] All 3 Epic ADRs added to Concept artifact with proper anchors
- [ ] ADR Index table populated with Status=Proposed
- [ ] ADR body sections include all required subsections (Context, Decision, Specification, Consequences, Alternatives, References, Provenance)

#### **3.5.3 LLM_Developer Handoff Brief** ✅ COMPLETE

**Brief File**: `prompt/artifacts/tasks/T810/consultant/workspace/communication/developer/handoff_brief_T810A_phase3-gdr-alignment.md`

**Brief Content**: Client-approved Phase 3B+3C proposals for Epic GDR alignment and Epic ADR creation.

**Scope**:
- SPS updates: 4 revised Epic GDRs with renumbered IDs (001-004)
- Concept updates: 3 new Epic ADRs with full T102-ADR-004 format compliance (ADR-001, ADR-003, ADR-004)
- Format validation requirements and post-implementation actions

**Status**: ✅ Brief created; ready for LLM_Developer implementation

**Success Criteria**:
- [x] Developer handoff brief drafted with complete implementation instructions
- [x] All 4 revised GDR content included (exact text from approved proposals)
- [x] All 3 Epic ADR full drafts included (exact text from approved proposals)
- [x] Format validation checklist provided (T102-ADR-004/005 compliance)

---

#### **3.5.4 T810A1 Subconsultant Coordination Brief** ⏸️ DEFERRED TO PHASE 5

**Deferral Rationale**: Per client guidance, T810A1 coordination brief compilation is deferred to **Phase 5 (Epic Issues & Risks Triage)** to ensure all Risks & Issues ID items are addressed before compiling comprehensive handoff covering Phase 2 + Phase 3 + Phase 4 changes.

**Brief File** (Phase 5): `prompt/artifacts/tasks/T810/consultant/workspace/communication/handoff_brief_T810A_t810a1-epic-changes_v1.0.0.md`

**Brief Content** (Comprehensive Phase 2 + Phase 3 + Phase 4 Changes):

**Phase 2 Changes (E-RID Promotion)**:
- **Promoted E-RIDs** (27 total): 4 ASSUM, 5 DEP, 4 CON, 8 QG, 6 IG
- **Inherited Considerations Table**: T810A1 Request must add table referencing all 27 Epic E-RIDs per T102-ADR-003
- **F-RID Reference Updates**: Replace promoted F-RID refs with E-RID refs in T810A1 Request where applicable

**Phase 3 Changes (GDR Demotion + E-RID Substitution)**:
- **Demoted Epic GDRs**: GDR-001 (Tracking-First Protocol) → T810A1-GDR-001, GDR-004 (Session Workflow Architecture) → T810A1-GDR-004
- **Demoted GDR Content**: Provide full current text from SPS for integration into T810A1 Request
- **Placement Guidance**: Add T810A1-GDR-001/004 to Request Section "Feature Governance Decisions" (follow T102-ADR-004 format)
- **E-RID Reference Updates in S05**: Replace direct GDR body references with E-IG/E-QG refs where implementation details moved
  - Example: Replace "Probe phase SHALL ask ≥2 clarifying questions per GDR-001" → "Probe phase SHALL enforce minimum probing per T810A-IG-002"
- **Numeric Confidence Prohibition**: Maintain in user-facing text; allow machine-only in JSON per T810A-ADR-001

**Phase 4 Changes (Issues & Risks)**:
- To be compiled after Phase 4 completion

**Coordination Owner**: LLM_Consultant (T810A Epic)

**Target Phase**: Phase 5.3 (T810A1 Delta Specification Review)

**Success Criteria** (Phase 5):
- [ ] Handoff brief drafted with Phase 2 + Phase 3 + Phase 4 comprehensive changes
- [ ] Demoted GDR content included with integration guidance
- [ ] E-RID reference update examples provided for S05 Execution Protocol
- [ ] Issues & Risks impact on T810A1 documented
- [ ] T810A1 subconsultant acknowledged receipt (coordination complete)

---

### 3.6 Phase 3 Validation Checklist (from research Section X) — ✅ PHASE 3B+3C COMPLETE

**GDR Content Integrity**:
- [x] GDR-001/002/003/004 (renumbered): All F-RID references replaced with E-RID references
- [x] Original GDR-001/004: Removed from Epic GDR section (demoted to T810A1)
- [x] All revised GDRs use formal reference syntax per T102-ADR-005-FR-006

**Epic ADR Integration**:
- [x] T810A-ADR-001 created with proper linking to GDR-001 (renumbered from 002)
- [x] T810A-ADR-004 created with proper linking to GDR-004 (renumbered from 005)
- [x] T810A-ADR-003 created with proper linking to GDR-003 (renumbered from 006)

**E-RID Reference Compliance**:
- [x] Authority preserved: No E-GDR references downstream F-RIDs
- [x] Completeness: All GDR concepts covered by E-RIDs or Epic ADRs
- [x] No circular references: E-RIDs don't reference GDRs that reference them back
- [x] Missing coverage: Numeric confidence guidance in ADR-001; no uncovered concepts

**Coordination Completion**:
- [x] LLM_Developer handoff brief created (Phase 3D+3E implementation)
- [ ] T810A1 subconsultant briefed (demoted GDRs + E-RID updates + S05 changes) — ⏸️ DEFERRED TO PHASE 5
- [x] T810A2/A3 coordination deferred per client guidance (focus T810A1 only)

**Document Updates** (Implementation via LLM_Developer):
- [ ] SPS changelog entry drafted for v1.1.0 — ⏳ Developer implementation pending
- [ ] Concept artifact updated with 3 new Epic ADRs — ⏳ Developer implementation pending
- [ ] GDR ID renumbering complete (priority-first sequence) — ⏳ Developer implementation pending

**Phase 3B+3C Status**: ✅ All proposals client-approved; ready for developer implementation

---

### 3.7 Phase 3 Success Criteria — ✅ CONSULTATION COMPLETE; ⏳ IMPLEMENTATION PENDING

Phase 3 Consultation complete when:
- ✅ **Phase 3A**: Research analysis accepted (E-GDR vs. F-GDR classification validated)
- ✅ **Phase 3B**: 4 E-GDRs revised with Epic-level language; 3 ADR full drafts created; 5 critical questions resolved
- ✅ **Phase 3C**: 3 Epic ADRs fully drafted with T102-ADR-004 compliance (combined with Phase 3B per client approval)
- ✅ **Phase 3D**: GDR renumbering plan finalized (priority-first: 002→001, 003→002, 006→003, 005→004); demoted GDR content preserved for T810A1 handoff
- ✅ **Phase 3E (Partial)**: LLM_Developer handoff brief created with complete implementation instructions
- ⏸️ **Phase 3E (T810A1 Handoff)**: Deferred to Phase 5 per client guidance (after Phase 4 Epic Issues & Risks)
- ✅ **Epic Governance Integrity**: All GDRs contain Epic-level policy only; all F-RID refs replaced; formal reference syntax compliance

**Phase 3 Implementation Status**:
- ✅ **Consultation**: Complete (all proposals client-approved)
- ✅ **Implementation**: Complete 
- ⏸️ **T810A1 Coordination**: Deferred to Phase 5

**→ GATE 3: Epic GDR Alignment Consultation Complete — Ready for Phase 4 (Epic Issues & Risks Triage)**

**Next Actions**:
1. LLM_Developer implements Phase 3D+3E changes per handoff brief
2. LLM_Consultant proceeds to Phase 4 (Epic Issues & Risks Triage)
3. T810A1 coordination brief compiled in Phase 5 after Issues & Risks resolution

---

### 3.8 Preliminary E-RID Mapping (From Phase 2 Analysis)

**Note**: These mappings are preliminary guidance for Phase 3A research. Final mappings will be determined during Phase 3B consultations based on research findings.

**T810A-GDR-001 (Tracking-First Clinical Protocol)**:
- Proposed E-RID refs: T810A-QG-001 (Clinical Protocol Reliability), T810A-QG-002 (Persona & Tone), T810A-IG-001 (Protocol Triggering), T810A-IG-002 (Probe Enforcement), T810A-IG-004 (Dynamic JSON Single-Entry)
- Research refs: T810A-RES-001 (System Architecture & Clinical Validation), T810A-RES-002 (Conversation-Driven Empirical Validation)
- Abstraction concern: "2-loop pattern" detail may need Epic ADR

**T810A-GDR-002 (Trust-and-Verify Workflow Standard)**:
- Proposed E-RID refs: T810A-QG-007 (Confidence Communication), T810A-IG-003 (Explicit Classification), T810A-CON-004 (ChatGPT Architectural Constraints)
- Abstraction concern: Numeric confidence thresholds (70%, 90%) in Epic GDR vs. qualitative user-facing communication

**T810A-GDR-003 (Stable/Dynamic JSON Architecture)**:
- Proposed E-RID refs: T810A-IG-004 (Dynamic JSON Single-Entry), T810A-IG-005 (Memory Review Protocol), T810A-CON-004 (ChatGPT Constraints), T810A-DEP-004 (Patient Data Structures), T810A-DEP-002 (Long-term Analysis)
- Abstraction concern: "Block 4" references feature-specific prompt structure; need generalization

**T810A-GDR-004 (Session Workflow Architecture)**:
- Proposed E-RID refs: T810A-IG-005 (Memory Review Protocol), T810A-QG-002 (Persona & Tone), T810A-IG-006 (Session Context Handoff)
- Abstraction concern: "Step 0/1/2" workflow may be feature-specific implementation

**T810A-GDR-005 (GI Knowledge Base Sources)**:
- Proposed E-RID refs: T810A-QG-004 (Holistic Analysis), T810A-IG-003 (Explicit Classification), T810A-CON-002 (Platform Compatibility), T810A-CON-003 (Clinical Compliance Deferral), T810A-DEP-005 (Clinical Safety Framework)
- Abstraction concern: "Block 4" knowledge base reference needs feature-agnostic language

**T810A-GDR-006 (Dual-Purpose Clinical Reporting)**:
- Proposed E-RID refs: T810A-IG-006 (Session Context Handoff), T810A-QG-002 (Persona & Tone), T810A-DEP-002 (Long-term Analysis)
- Abstraction concern: "100-200 tokens" specific target may need Epic ADR; first-person timeline structure may be feature-specific


## 4. Epic Issues & Risks — Strategic Demotion Decision ✅ COMPLETE

### 4.1 Analysis Summary

**Current State** (SPS §III.C.viii): 9 Items labeled "Epic" but containing Feature-specific implementation details.

**Scope Assessment Results**:
- **Issues (4 total)**: 0 Epic-level / 4 Feature-specific (T810A1)
  - ISSUE-001: T810A1 ↔ T810A2 coordination (references "Surface-level references in T810A1")
  - ISSUE-002: T810A1 S05 implementation (references "S05 Execution Protocol development")
  - ISSUE-003: T810A1 prompt engineering (references "S08 exemplars", "S05 execution instructions")
  - ISSUE-004: T810A1 S05/S08 enforcement (references "S05 execution protocol instructions and S08 exemplars")

- **Risks (5 total)**: 1 Borderline / 4 Feature-specific (T810A1)
  - RISK-001: T810A1 Probe phase (references "S08 exemplars, S05 explicit Probe enforcement")
  - RISK-002: T810A1 ↔ T810A2 coordination (borderline; references "Surface-level JSON references in T810A1")
  - RISK-003: T810A1 MVP scope (borderline clarification; demoted per client decision)
  - RISK-004: T810A1 2-loop pattern (directly tied to **demoted GDR-001**)
  - RISK-005: T810A1 Stable JSON implementation (references "INT-005", "Probe phase", "S04")

**Critical Finding**: RISK-004 references "2-loop conversation pattern" from **T810A-GDR-001 (Tracking-First Protocol)**, which was demoted to T810A1-GDR-001 in Phase 3. This creates architectural inconsistency requiring demotion.

**Overall**: **78% of current "Epic" Issues & Risks are Feature-specific (T810A1)**.

---

### 4.2 Client Decision: Strategic Demotion & Clean Slate Approach

**Decision**: **ALL 9 current Issues & Risks demoted to T810A1 Feature scope**.

**Rationale**:
1. **Scope Misalignment**: Comprehensive analysis shows 78% are Feature-specific (T810A1 implementation details)
2. **Architectural Consistency**: RISK-004 tied to demoted GDR-001; maintaining Epic-level creates governance contradiction
3. **Clean Governance**: Starting fresh for Epic Issues & Risks ensures proper Epic-level scoping from the start
4. **Efficiency**: Demotion more efficient than rewriting; avoids rework if scope assumptions prove incorrect

**Outcome**:
- **SPS Epic Issues & Risks Section**: Cleared (0 Items)
- **Demoted Items**: Preserved for T810A1 handoff coordination brief (Phase 5.3)
- **New Epic Issues & Risks**: Will be introduced in Phase 5 (Holistic Migration Review) with proper Epic scope validation

---

### 4.3 Demoted Items Inventory

**Items for T810A1 Coordination Brief** (Phase 5.3):

**Issues** (4 demoted to T810A1):
1. `T810A1-ISSUE-001` (formerly T810A-ISSUE-001): Stable/Dynamic JSON Architecture Dependency
2. `T810A1-ISSUE-002` (formerly T810A-ISSUE-002): Protocol Triggering Logic Implementation
3. `T810A1-ISSUE-003` (formerly T810A-ISSUE-003): ChatGPT Assistant Mode Override Strategy
4. `T810A1-ISSUE-004` (formerly T810A-ISSUE-004): Controlled Vocabulary Validation

**Risks** (5 demoted to T810A1):
1. `T810A1-RISK-001` (formerly T810A-RISK-001): ChatGPT Override Insufficient
2. `T810A1-RISK-002` (formerly T810A-RISK-002): T810A2 Development Delays
3. `T810A1-RISK-003` (formerly T810A-RISK-003): Scope Expansion Beyond MVP
4. `T810A1-RISK-004` (formerly T810A-RISK-004): Minimum 2-Loop Pattern Non-Compliance
5. `T810A1-RISK-005` (formerly T810A-RISK-005): Stable JSON Manual Update Friction

**Placement Guidance** (T810A1 subconsultant): Add to T810A1 Request Section "Feature Issues & Risks" with IDs updated to T810A1-* per T102-ADR-005 Feature scope standards.

---

### 4.4 Phase 4 Validation Checklist — ✅ COMPLETE

**Scope Assessment**:
- [x] All 9 current Items analyzed for Epic vs. Feature scope
- [x] Epic Scope Test applied (cross-feature impact, Epic governance authority, Feature implementation details)
- [x] Analysis results documented (78% Feature-specific; architectural inconsistency with demoted GDR-001)
- [x] Client decision obtained (demote ALL to T810A1; start fresh for Epic)

**Demotion Execution**:
- [x] Demoted items inventory compiled (4 Issues + 5 Risks)
- [x] ID migration mapping defined (T810A-* → T810A1-*)
- [x] Placement guidance documented for T810A1 subconsultant coordination
- [x] Epic Issues & Risks section cleared in SPS (ready for Phase 5 new items)

**Coordination Planning**:
- [x] Demoted items preserved for T810A1 handoff brief (Phase 5.3)
- [x] New Epic Issues & Risks deferred to Phase 5 (proper scope validation)
- [x] Architectural consistency maintained (RISK-004 demotion aligns with GDR-001 demotion)

---

### 4.5 Phase 4 Success Criteria — ✅ CONSULTATION COMPLETE

Phase 4 complete when:
- ✅ **Scope Analysis**: All 9 current Items analyzed with Epic Scope Test applied
- ✅ **Client Decision**: Strategic demotion decision obtained (ALL Items → T810A1)
- ✅ **Demotion Plan**: Demoted items inventory compiled with ID migration mapping and placement guidance
- ✅ **Epic Governance Integrity**: Epic Issues & Risks section cleared; no Feature-specific items remain
- ✅ **Coordination Handoff**: Demoted items documented for T810A1 coordination brief (Phase 5.3)

**Phase 4 Status**: ✅ **COMPLETE** (Strategic demotion decision; no SPS implementation required)

**→ GATE 4: Epic Issues & Risks Triage Complete — Ready for Phase 5 (Holistic Migration Review)**

**Next Actions**:
1. LLM_Consultant proceeds to **Phase 5 (T810A1 Subconsultant Coordination & Handoff)**
2. Phase 5: Compile comprehensive T810A1 coordination brief with Phase 2/3/4 changes
3. Phase 6: Conduct Holistic Migration Review with NEW Epic Issues & Risks validation

---

## 5. T810A1 Subconsultant Coordination & Handoff — PRIORITY PHASE

### 5.1 Phase Context & Strategic Priority

**Objective**: Ensure T810A1 subconsultant receives comprehensive coordination brief covering ALL Phase 2/3/4 Epic changes BEFORE Epic-level holistic review begins.

**Strategic Rationale**:
1. **T810A1 Implementation Priority**: Feature-level work can proceed in parallel with Epic governance finalization
2. **Prevent Rework**: T810A1 needs Phase 2/3/4 results to update Request document; deferring creates blocking dependencies
3. **Clear Separation of Concerns**: Complete Feature handoff before Epic holistic review ensures clean scope boundaries
4. **Architectural Consistency**: T810A1 receives demoted GDRs (GDR-001/004) and Issues/Risks (9 items) requiring immediate integration

**Phase 5 Scope**:
- Compile comprehensive coordination brief documenting Phase 2 E-RID promotion (27 E-RIDs)
- Document Phase 3 GDR demotion (GDR-001/004 → T810A1-GDR-001/004)
- Document Phase 4 Issues & Risks demotion (9 items → T810A1)
- Provide implementation guidance for T810A1 Request document updates
- Establish handoff coordination pattern for subconsultant communication

---

### 5.2 Phase 2 Summary: E-RID Promotion (27 Epic Requirements)

**Promoted Categories**:
- **Assumptions (4 E-RIDs)**: T810A-ASSUM-001 through ASSUM-004
- **Dependencies (5 E-RIDs)**: T810A-DEP-001 through DEP-005
- **Constraints (4 E-RIDs)**: T810A-CON-001 through CON-004
- **Quality Goals (8 E-RIDs)**: T810A-QG-001 through QG-008
- **Implementation Guidance (6 E-RIDs)**: T810A-IG-001 through IG-006

**T810A1 Integration Requirements**:
1. **Inherited Considerations Table**: Add table in T810A1 Request referencing all 27 Epic E-RIDs per T102-ADR-003
2. **F-RID Reference Updates**: Replace promoted F-RID references with E-RID references throughout Request
3. **Feature Delta Retention**: Maintain Feature-specific implementation details (S01-S10 Stories, F-IFs, F-INTs, F-CONs, F-NFRs) that were NOT promoted

**Detailed Mapping**: See plan Section 2 (lines 168-229) for complete ID migration traceability.

---

### 5.3 Phase 3 Summary: GDR Alignment & Demotion

**Epic GDR Revisions** (4 retained at Epic):
- **T810A-GDR-001** (Trust-and-Verify Workflow Standard) — formerly GDR-002
- **T810A-GDR-002** (Stable/Dynamic JSON Architecture) — formerly GDR-003
- **T810A-GDR-003** (Dual-Purpose Clinical Reporting) — formerly GDR-006
- **T810A-GDR-004** (GI Knowledge Base Sources) — formerly GDR-005

**Demoted GDRs** (2 → T810A1):
- **T810A1-GDR-001** (formerly T810A-GDR-001): Tracking-First Clinical Protocol
  - **Rationale**: 5-phase protocol + 2-loop pattern are T810A1-specific conversational workflow
  - **Content**: Preserve full current GDR-001 text from SPS for T810A1 integration
- **T810A1-GDR-002** (formerly T810A-GDR-004): Session Workflow Architecture
  - **Rationale**: Step 0/1/2 session initialization is T810A1-specific prompting pattern
  - **Content**: Preserve full current GDR-004 text from SPS for T810A1 integration

**T810A1 Integration Requirements**:
1. **Feature Governance Decisions Section**: Add T810A1-GDR-001/002 to Request Section "Feature Governance Decisions" (follow T102-ADR-004 format)
2. **E-RID Reference Updates in S05**: Replace direct GDR body references with E-IG/E-QG refs where implementation details moved
   - Example: Replace "Probe phase SHALL ask ≥2 clarifying questions per GDR-001" → "Probe phase SHALL enforce minimum probing per T810A-IG-002"
3. **Numeric Confidence Prohibition**: Maintain in user-facing text; allow machine-only in JSON per T810A-ADR-001

**Epic ADRs Created** (3 new):
- T810A-ADR-001 (Trust-and-Verify Confidence Policy)
- T810A-ADR-003 (Dual-Purpose Reporting Policy)
- T810A-ADR-004 (GI Knowledge Sources Catalog)

**Detailed Content**: See Phase 3 developer handoff brief (`handoff_brief_T810A_phase3-gdr-alignment.md`) for exact GDR/ADR text.

---

### 5.4 Phase 4 Summary: Issues & Risks Strategic Demotion

**Decision**: ALL 9 current "Epic" Issues & Risks demoted to T810A1 Feature scope.

**Demoted Issues** (4 → T810A1):
1. **T810A1-ISSUE-001** (formerly T810A-ISSUE-001): Stable/Dynamic JSON Architecture Dependency
2. **T810A1-ISSUE-002** (formerly T810A-ISSUE-002): Protocol Triggering Logic Implementation
3. **T810A1-ISSUE-003** (formerly T810A-ISSUE-003): ChatGPT Assistant Mode Override Strategy
4. **T810A1-ISSUE-004** (formerly T810A-ISSUE-004): Controlled Vocabulary Validation

**Demoted Risks** (5 → T810A1):
1. **T810A1-RISK-001** (formerly T810A-RISK-001): ChatGPT Override Insufficient
2. **T810A1-RISK-002** (formerly T810A-RISK-002): T810A2 Development Delays
3. **T810A1-RISK-003** (formerly T810A-RISK-003): Scope Expansion Beyond MVP
4. **T810A1-RISK-004** (formerly T810A-RISK-004): Minimum 2-Loop Pattern Non-Compliance
5. **T810A1-RISK-005** (formerly T810A-RISK-005): Stable JSON Manual Update Friction

**Rationale**: Comprehensive analysis showed 78% Feature-specific (T810A1 implementation details); RISK-004 directly tied to demoted GDR-001 (2-loop pattern).

**T810A1 Integration Requirements**:
1. **Feature Issues & Risks Section**: Add to T810A1 Request Section "Feature Issues & Risks" with IDs updated to T810A1-* per T102-ADR-005
2. **Current Content Preservation**: Maintain existing Issue/Risk descriptions; update references from T810A-* to T810A1-*
3. **Status Maintenance**: Preserve current Status/Priority/Owner fields

**Detailed Analysis**: See plan Section 4 (lines 605-706) for scope assessment rationale.

---

### 5.5 T810A1 Delta Specification Analysis

**Objective**: Define what remains in T810A1 Request as feature-specific after promoting 20+ E-RIDs to Epic scope.

**Approach**: Analyze feature-specific content (S01-S10 Stories, F-IFs, F-INTs, F-CONs, F-NFRs); define Inherited Considerations table structure.

**Deliverable**:
1. T810A1 delta specification outline showing ~50% Epic inheritance + ~50% feature-specific delta
2. Inherited Considerations table template with 27 Epic E-RIDs

**Note**: T810A1 Coordination Brief completed in Phase 5; this subsection focuses on delta analysis only.

---

**Detailed Analysis**: See `proposal_T810A-SYSTEM_phase5.md` for comprehensive delta specification matrices, inheritance tables, and feature-level guidance.

---

---

### 5.6 Coordination Brief Creation & Handoff

**Brief File**: `prompt/artifacts/tasks/T810/consultant/workspace/communication/consultant/handoff_brief_T810A1-PROMPT_epic-changes.md`

**Brief Structure** (following T810A2 handoff exemplar):
1. **Executive Summary**: Phase 2/3/4 changes overview + critical context
2. **Phase 2 Changes**: E-RID promotion details (27 E-RIDs with categories and migration mapping)
3. **Phase 3 Changes**: GDR demotion (2 GDRs with full content) + E-RID reference update guidance
4. **Phase 4 Changes**: Issues & Risks demotion (9 items with ID migration and placement guidance)
5. **Integration Requirements**: Inherited Considerations Table template, F-RID→E-RID replacement patterns, Feature-specific delta retention
6. **Implementation Guidance**: Request document section updates, format compliance, coordination checkpoints

**Success Criteria**:
- [x] Coordination brief drafted with comprehensive Phase 2/3/4 changes
- [x] Demoted GDR-001/004 full content included from SPS
- [x] Demoted Issues/Risks content preserved with ID migration mapping
- [x] E-RID reference update examples provided for S05 Execution Protocol
- [x] Inherited Considerations Table template provided with 27 E-RIDs
- [ ] Phase 5.5 delta analysis validated coordination brief accuracy
- [ ] T810A1 subconsultant acknowledged receipt (handoff complete)

---

### 5.7 Phase 5 Success Criteria — ✅ COMPLETE

Phase 5 complete when:
- [x] **Coordination Brief**: Comprehensive T810A1 handoff brief drafted covering Phase 2/3/4 changes
- [x] **Demoted Content**: GDR-001/004 full text + Issues/Risks content included
- [x] **Integration Guidance**: Inherited Considerations Table, F-RID replacement patterns, placement guidance
- [x] **Reference Materials**: E-RID update examples provided for S05 Execution Protocol
- [x] **Inherited Considerations**: Table template delivered with 27 E-RIDs
- [x] **Delta Validation**: Phase 5.5 analysis validated coordination brief accuracy (Activity 5.5 complete 2025-11-22)
- [ ] **Handoff Confirmation**: T810A1 subconsultant acknowledged receipt (PENDING external delivery)

**Phase 5 Status**: ✅ **COMPLETE** (All validation complete; brief ready for T810A1 delivery)

**Phase 5 Summary**:
- **Activity 5.5 Delta Analysis** completed comprehensive T810A1 Request baseline review
- **F-RID→E-RID Mapping**: 27 E-RIDs promoted (47% inheritance), 30 F-RIDs retained (53% delta)
- **Handoff Brief Enhanced** with 6 critical corrections:
  1. Section III.E split guidance (Inherited Considerations + Assumptions/Dependencies)
  2. Table format corrected to match Request exemplar (`Source Artifact | Source ID | Category | Inherited Rule IDs`)
  3. GDR placement corrected (Section III.K: after J, before L)
  4. Issues & Risks guidance updated (use existing Section III.L, not create new)
  5. RID renumbering instructions added (10 F-RIDs renumbered to start from 001)
  6. Pre-implementation context materials section added (6 required review documents)
- **Proposal File Enhanced**: `proposal_T810A-SYSTEM_phase5.md` expanded from 166→447 lines with detailed delta specification analysis
- **Handoff Brief Validated**: Ready for T810A1 delivery with comprehensive implementation guidance

**Delivery Note**: Coordination brief (`handoff_brief_T810A1-PROMPT_epic-changes.md`) validated and ready for T810A1 delivery. Brief includes 6-step implementation checklist, 4 coordination checkpoints, and 7-category success criteria.

**→ GATE 5: Coordination Brief Validated & Ready for Delivery** ✅

**Next Actions**:
1. ✅ Phase 5.5 delta analysis complete
2. ✅ Handoff brief corrections applied per QA feedback
3. **PENDING**: Deliver brief to T810A1 subconsultant and obtain acknowledgment

---

## 6. Holistic Migration Review (Pre-Implementation Gate)

**Purpose**: Conduct comprehensive review of entire migration plan before implementation to ensure architectural coherence, identify cross-category dependencies, and surface potential risks not visible in category-by-category analysis.

**Detailed Analysis**: See `proposal_T810A-SYSTEM_phase6.md` for comprehensive validation framework, full risk/issue specifications, detailed matrices/tables, and implementation sequencing analysis.

**Note**: This phase renamed from Phase 5 to Phase 6 to prioritize T810A1 subconsultant coordination (new Phase 5) before Epic holistic review.

---

### 6.1 Cross-Category Consistency Check

**Objective**: Ensure promoted E-RIDs form coherent Epic governance framework without contradictions or gaps.

**Approach**: Validate alignment across category pairs using 4 key questions (Assumptions ↔ Constraints, Dependencies ↔ Quality Goals, Implementation Guidance ↔ Constraints, Quality Goals ↔ Assumptions).

**Deliverable**: Consistency matrix documenting validated alignments and flagged conflicts.

---

### 6.2 Epic Scope Boundary Validation

**Objective**: Confirm all promoted E-RIDs are truly Epic-level (apply to ≥3 of 4 features: A1/A2/A3/A4).

**Approach**: Feature applicability matrix assessing each E-RID across features with promotion validation threshold (✅ applicable to ≥3 features OR ✅ to 2 features + ❓ to 1 feature).

**Deliverable**: Feature applicability matrix; recommendations for demotions if needed (Result: No demotions required; all 27 E-RIDs validated for Epic scope).

---


### 6.3 GDR-to-E-RID Dependency Mapping

**Objective**: Ensure all 4 Epic GDRs (revised in Phase 3) properly reference promoted E-RIDs without broken references or circular dependencies.

**Approach**: Trace GDR → E-RID references; validate Epic ADR linkages; confirm no circular dependencies.

**Deliverable**: GDR dependency map; validation that Phase 3 revisions achieved proper E-RID integration.

**Status**: Phase 3 already completed GDR→E-RID alignment; this subsection validates implementation correctness.

---

### 6.4 Implementation Sequence Dependency Analysis

**Objective**: Identify critical path and gate dependencies to ensure proper implementation sequencing.

**Approach**: Dependency graph analysis showing parallel vs. sequential work streams; critical decision identification blocking implementation phases.

**Deliverable**: Implementation sequence with gate definitions.

---

### 6.5 New Epic Risk & Issue Identification

**Objective**: Surface Epic-level risks/issues not visible in category-level analysis through holistic cross-cutting review.

**Timing**: After Phase 6.4 (GDR-to-E-RID Dependency Mapping) per client guidance.

**Identified**: 5 new Epic Risks + 2 new Epic Issues:
- **RISK-006** (T810A1 Delta Specification Coordination Failure): Medium likelihood, High impact — duplication and maintenance burden; mitigate via explicit coordination step, validation checklist, Inherited Considerations table template
- **RISK-007** (Epic Over-Prescription): Medium likelihood, Medium impact — reduced feature autonomy from over-prescriptive E-RIDs; mitigate via careful abstraction review, principle-based E-RIDs, feature variance protocol
- **RISK-008** (GDR Abstraction Loss of Meaning): Low likelihood (with ADR mitigation), Medium impact — vague GDRs without implementation guidance; mitigate via Epic ADR placeholders, GDR rationale preservation, feature implementation examples
- **RISK-009** (Constraint Enforcement Inconsistency): Medium likelihood, Medium impact — features implement constraints differently; mitigate via prescriptive MUST/SHALL language with features determining HOW, document enforcement expectations when patterns emerge
- **RISK-010** (Default Behavior Override Insufficient Guidance): Medium likelihood, Medium-High impact — inconsistent Consultant/Analyst mode enforcement; mitigate via monitoring T810A1 S05 development, create Epic IG/ADR if patterns emerge, revisit post-A1 validation
- **ISSUE-005**: Reserved placeholder for future issues
- **ISSUE-006** (Feature Impact Analysis Gap): Medium priority — no documented E-RID impact analysis for A2/A3/A4; resolve via Feature Impact Analysis document creation during Phase 6.5

**Detailed Analysis**: See `proposal_T810A-SYSTEM_phase6.md` Section VI for full risk/issue specifications including likelihood, impact, mitigation strategies, monitoring plans, and traceability to client guidance.

**Deliverable**: Updated Epic Risks (10 total: 5 new) and Issues (6 total: 2 new + 1 reserved) sections in SPS.

---

### 6.6 Validation Checklist Expansion

**Objective**: Ensure post-migration validation covers all critical integrity checks identified during holistic review.

**Approach**: Expand from 5 basic categories to 8 comprehensive categories adding: (6) Epic Governance Coherence, (7) E-RID Scope Validation, (8) GDR Reference Integrity & Abstraction.

**Deliverable**: 8-category comprehensive validation checklist for Gate 7 (Implementation Complete) covering document structure, E-RID formal compliance, cross-reference integrity, content abstraction, precedence compliance, governance coherence, scope validation, and GDR integrity.

---

### 6.7 Client Decision Summary (Pre-Implementation)

**Objective**: Consolidate all client decisions required before implementation can begin with dependency-ordered sequencing.

**Critical Decisions**: 8 total (6 resolved, 2 pending):
- **D-1** (ASSUM-004 Scope): ✅ RESOLVED — Hybrid split adopted (Epic ASSUM-004 + A1 ASSUM-004)
- **D-2** (QG-001 Scope): ⚠️ UNRESOLVED — **CRITICAL** — Epic abstracted vs. demote to A1; blocks Epic QG section + GDR-001 references
- **D-3** (QG-005 Abstraction): ⚠️ UNRESOLVED — **HIGH** — Keep Epic maintainability principle vs. demote; blocks Epic QG section
- **D-4** (DEP-008 Scope): ✅ RESOLVED — Demoted to T810A1 (feature-specific research)
- **D-5** (GDR-002 Confidence Thresholds): ✅ RESOLVED — Mandatory numeric in ADR-001 (Phase 3 implementation)
- **D-6** (Epic ADR Creation Timing): ✅ RESOLVED — Created in Phase 3C (ADR-001, ADR-003, ADR-004)
- **D-7** (ISSUE-002 Scope): ✅ RESOLVED — Follows D-4 (demoted to T810A1)
- **D-8** (CON-004 Category & Scope): ✅ RESOLVED — Reclassified to T810A-QG-008 + hybrid split (Epic QG-008 + A1 NFR-009)

**Updated Status**: D-5 and D-6 resolved during Phase 3; only D-2 and D-3 remain unresolved.

**Decision Sequencing**: Critical Path — address D-2, D-3 (blocks Epic QG section).

**Deliverable**: Client decision tracking matrix with options, recommendations, blocking impact, and priority; decision session agenda for efficient resolution.

---

### 6.8 Phase 6 Success Criteria

Phase 6 complete when:
- [ ] Cross-category consistency validated (no contradictions)
- [ ] Epic scope boundaries confirmed (all E-RIDs apply cross-feature)
- [ ] GDR dependency mapping validated (Phase 3 E-RID integration confirmed correct)
- [ ] Implementation sequence dependencies identified
- [ ] New Epic risks/issues documented (5 new risks, 2 new issues with full specifications)
- [ ] Validation checklist expanded to 8 categories
- [ ] Client decisions prioritized (2 pending: D-2, D-3; 6 resolved)

**Phase 6 Consultation Sequence** (client-directed order):
1. **Subphase 6.1**: Cross-Category Consistency Check
   - Validate Epic E-RID coherence across all 5 categories
   - Apply 4 validation questions (Assumptions↔Constraints, Dependencies↔Quality Goals, IGs↔Constraints, QGs↔Assumptions)

2. **Subphase 6.2**: Epic Scope Boundary Validation
   - Apply feature applicability matrix to all 27 E-RIDs
   - Confirm cross-feature applicability (≥3 of 4 features: A1/A2/A3/A4)

3. **Subphase 6.3**: GDR-to-E-RID Dependency Mapping
   - Validate Phase 3 GDR revisions properly reference promoted E-RIDs
   - Confirm no broken references or circular dependencies

4. **Subphase 6.4**: Implementation Sequence Dependency Analysis
   - Refresh dependency graph and gate handoffs
   - Confirm sequencing for post-decision SPS population work

5. **Subphase 6.5**: New Epic Risk & Issue Identification
   - Add RISK-006 through RISK-010 and ISSUE-005/006 with mitigations
   - Ensure risk ownership/monitoring aligns with Epic governance

6. **Subphase 6.6**: Validation Checklist Expansion
   - Expand the checklist to 8 categories covering governance, scope, and GDR integrity

7. **Subphase 6.7**: Client Decision Summary
   - Prepare decision tracking matrix and briefing materials for D-2/D-3 session

**Phase 6 Status**: ⏳ **READY TO BEGIN** (Phase 5 coordination brief complete; dependencies cleared for holistic review kickoff)

**→ GATE 6A: Subphases 6.1-6.4 Complete** — Core Holistic Checks Finished (Phase 5.5 already validated coordination brief)  
**→ GATE 6B: Subphases 6.5-6.7 Complete** — Holistic Review Approved, New Risks/Issues Documented  
**→ GATE 6C: Client Decision Session** — Critical Decisions Resolved (D-2, D-3), Ready for Phase 7 SPS Implementation

---

## 7. Implementation Steps (upon approval)
1) Add Epic Requirements to SPS
- Create sections under `##### v. Epic Requirements` for: Quality Goals, Assumptions, Constraints, Dependencies, Implementation Guidance.
- Insert promoted items with exact titles/text; update IDs to `T810A-*` per mapping.

2) Introduce Epic IGs (E-RIDs) to support GDR references
- Add `T810A-IG-001..006` with concise, governing statements.

3) Revise Epic GDR bodies
- Replace all F-RID references with E-RIDs and research IDs using formal reference syntax.
- Remove solution specifics; shift them into placeholder ADRs under Concept (III.B.1), linked from GDR “Consequences/References”.

4) Tidy Epic Issues & Risks
- Rewrite descriptions to reference E-RIDs and Feature IDs (`T810A2/3/4`) where needed, avoiding story-level or F-RIDs.

5) Coordination with T810A1 subconsultant
- Completed in Phase 5 (T810A1 Subconsultant Coordination & Handoff)
- Confirm that promoted items remain referenced in A1 as inherited (delta-only) per T102-ADR-003; avoid duplication in A1.
- If A1 needs additional feature-specific detail beyond Epic guidance, document locally as F-RIDs.

## 8. Traceability & ID Governance
- Follow T102-ADR-005: scope ID regex, category tokens, and reference rules.
- GDRs stay at Epic scope; ADRs for design/implementation go to `concept_T810-GASTRO.md` under Epic ADR Index.
- T810A1 Inherited Considerations table provided in Phase 5 coordination brief.

---

### 8.1 Feature Coordination Dependencies

**T810A1 (PROMPT) Coordination**:
- **Status**: Phase 5 coordination brief created (`handoff_brief_T810A1-PROMPT_epic-changes.md`)
- **Delivery Status**: NOT YET DELIVERED (awaiting Phase 5.5 delta analysis validation)
- **Handoff Timing**: Post-Phase 5.5 completion (T810A1 Delta Specification Analysis confirms brief accuracy)
- **Parallel Development**: T810A1 Request updates can proceed in parallel with Phase 6 Epic holistic review after brief delivery

**T810A2 (SCHEMA) Coordination**:
- **Status**: Development IN PROGRESS
- **Request Document**: `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md`
- **Epic Dependencies**:
  - `T810A-DEP-004` (Patient Data Structures) — Epic E-RID depends on T810A2 schema authority
  - `T810A-IG-004` (Dynamic JSON Single-Entry Pattern) — Epic E-RID references T810A2 schema patterns
  - `T810A-GDR-002` (Stable/Dynamic JSON Architecture) — Epic GDR references T810A2 deliverables
- **Coordination Requirement**: Monitor T810A2 schema specifications (Stable JSON, Dynamic JSON) for material changes impacting Epic E-RID content
- **Handoff Timing**: TBD — coordinate after T810A2 schema specifications finalized
- **Risk**: Schema changes may require Epic E-RID content revision (DEP-004, IG-004)
- **Mitigation**:
  - Track T810A2 development progress
  - Conduct T810A2 coordination review in Phase 6 or Phase 7 if schemas ready
  - Surface-level schema references in Epic E-RIDs minimize coupling

**T810A3 (REPORT) & T810A4 (TOOLS) Coordination**:
- **Status**: Not yet scoped
- **Epic Dependencies**:
  - `T810A-DEP-002` (Long-term Analysis) — depends on T810A3 REPORT
  - `T810A-DEP-003` (Toolbox Interface) — depends on T810A4 TOOLS
- **Coordination Timing**: Future phases (post-Epic implementation)

## 9. Open Questions (for Client)
1) Should Confidence Communication (now QG-007) apply uniformly to all child features, or do we allow feature-specific variants (e.g., different confidence phrasing for imaging vs. diet analysis)?
2) Do we formalize the minimum probing requirement (≥2 questions) as a hard Epic constraint or keep as IG-level guidance with enforcement in features?
3) For Protocol Triggering, do you prefer we keep the current keyword-first heuristic at Epic IG or defer entirely to feature-level execution guidance?
4) Are there additional cross-cutting compliance constraints (e.g., privacy/legal) we should encode at Epic scope now, beyond `T810A-CON-002/003`?
5) Do you want placeholder Epic ADRs created now (titles + anchors only) to capture the moved implementation specifics referenced by GDRs?
   - **RESOLVED**: Epic ADRs (ADR-001, ADR-003, ADR-004) created in Phase 3C with full specifications.

---

## 10. Summary

This migration plan elevates shared requirements from `T810A1` to Epic-level E-RIDs through a structured, phased approach:

**Phase 1-4**: Category-by-category promotion analysis and implementation:
- **Phase 2**: E-RID Promotion (27 E-RIDs created: 4 ASSUM, 5 DEP, 4 CON, 8 QG, 6 IG)
- **Phase 3**: Epic GDR Alignment (4 GDRs revised, 2 GDRs demoted to T810A1, 3 Epic ADRs created)
- **Phase 4**: Issues & Risks Triage (ALL 9 items demoted to T810A1; clean slate for Epic)

**Phase 5**: T810A1 Subconsultant Coordination & Handoff (PRIORITY PHASE)
- Comprehensive coordination brief covering Phase 2/3/4 changes
- Demoted GDR-001/004 full content + Issues/Risks integration guidance
- Inherited Considerations Table template with 27 E-RIDs
- T810A1 delta specification analysis (Feature inheritance vs. feature-specific delta)
- Feature-level work proceeds in parallel with Epic governance finalization

**Phase 6**: Holistic Migration Review (Pre-Implementation Gate)
- Cross-category consistency validation
- Epic scope boundary confirmation (all E-RIDs apply to min 3 of 4 features)
- GDR-to-E-RID dependency mapping validation
- Implementation sequence analysis
- New Epic risk/issue identification (RISK-006 through RISK-010, ISSUE-005/006)
- Expanded 8-category validation checklist
- Client decision prioritization (2 pending: D-2, D-3; 6 resolved)

**Phase 7**: Implementation execution (Epic SPS population, T810A1 final coordination) following client approval of Phase 6 holistic review and resolution of critical decisions.

**Current Status**:
- ✅ **Phases 2-4**: Complete (E-RID promotion, GDR alignment, Issues/Risks demotion)
- ⏳ **Phase 5**: In Progress (T810A1 coordination brief creation)
- ⏸️ **Phase 6**: Pending (awaiting Phase 5 completion)
- ⏸️ **Phase 7**: Pending (awaiting Phase 6 completion)
