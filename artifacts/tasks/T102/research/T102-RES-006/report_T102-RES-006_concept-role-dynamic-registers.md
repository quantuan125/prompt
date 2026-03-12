---
artifact_type: 'RESEARCH_REPORT'
initiative_id: 'T102'
research_id: 'T102-RES-006'
version: '1.0.0'
iteration: '2'
date: '2026-02-10'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: Concept Role + Dynamic SSOT Registers (`T102-RES-006`)

## I. EXECUTIVE SUMMARY

**Context**: The current `concept_T102-CONSULTANT.md` already behaves like an initiative navigation hub (standards index, research register, design register), while `T102-STD-001-CLAUSE-003` still frames Concept primarily as an ADD/ADR compendium. This creates governance/expectation drift and amplifies a known failure mode: centralized registers that are not maintained become unreliable (broken links, “ghost artifacts”), undermining the “audit surface” role required by `T102-RES-005` and referenced by `T102-STD-006`.

**Verdict**: **RECOMMENDATION ONLY** (no GO/NO-GO gate requested for the whole initiative). This report provides decision-ready recommendations for Concept’s role, register-family placement, and standards alignment impacts (recommendations-only; no clause drafting).

**Recommended Concept Architecture (primary)**: **Hub-first with thresholds** (Option **(e)** from the brief):
1) **Concept as the coordination audit surface**: indexes + a small number of cross-scope registers that enable discovery, cross-scope visibility, and drift detection indicators (manual first).
2) **SPS/Request as embedded minimum viable local emphasis**: keep local tables required by standards, but minimize repetition and avoid duplicative “register-like” bodies.
3) **INT as transient coordination guidance** with explicit promotion when relied on as policy (per `T102-STD-005-CLAUSE-005C`).

**Issues & Risks in Concept (Topic 7)**: **CONDITIONAL (GO) as aggregation-only dashboard** (not canonical hosting):
- **Canonical hosting remains SPS** (RES-004 baseline).
- Concept MAY add a *non-normative* I&R aggregation register **only when triggers are met** (see Topic 7), using pointers + staleness indicators rather than duplicating canonical rows.

**Key Findings**:
1) **Concept is currently “index + partial registers + placeholders”**: core sections (Identity/Rules, Readiness Snapshot, Handoff Snapshot, Integration, Governance) are placeholders; Feature Register is empty; Research Register exists but contains broken versioned links; Design Register exists and links to story-level design logs. This is consistent with “candidate hub” behavior but inconsistent with “ADR compendium” expectations. (Topic 1)
2) **The drift/tooling failure mode is real today**: ADR extraction tooling expects anchors in Concept and fails (`extract_adr.py --adr-id ADR-005` fails), and the Concept research register points to non-existent versioned filenames. These are concrete audit-surface reliability failures. (Topics 1, 6)
3) **Standards already imply Concept is a dynamic registers surface**: `T102-STD-006` mandates a Concept master research register; `T102C-STD-001` defines Concept as an eight-section architecture including readiness/handoff and registers. `T102-STD-001` is the lagging artifact and should be aligned. (Topics 3, 6)
4) **External benchmarking supports lightweight decision records (ADRs) + linking (avoid duplication)** for architecture decisions and supporting rationale. [1][2]
5) **External benchmarking supports baselines + change control + bidirectional traceability** as recurring requirements-management themes. [3][4][5]
6) **Documentation system guidance supports modular, audience-focused docs and a “single source of truth” posture** (to reduce duplication/drift via link-first patterns). [6][7][8]

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Research followed the commissioned brief topics (Topics 1–10), treated accepted RES-004/RES-005 outputs as authoritative inputs (no re-litigation), and produced recommendations only (no SSOT/standards clause drafting).

**Source of Truth Audit**:
- **SSOT artifacts (primary evidence)**:
  - `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
  - `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
- **Standards (authoritative constraints)**:
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md`
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md`
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
  - `prompt/artifacts/tasks/T102/T102C/standard/standard_T102C-STD-001_concept-architectural-framework.md`
- **Accepted dependency inputs**:
  - `prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md`
  - `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md`
  - `prompt/artifacts/tasks/T102/research/T102-RES-005/report_T102-RES-005_cross-scope-coordination-architecture.md`
  - `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md`
- **Governance / intent (non-normative)**:
  - `prompt/artifacts/tasks/T102/workspace/PH001/ST004/plan_T102-PH001-ST004.md`
  - `prompt/artifacts/tasks/T102/workspace/PH001/ST004/AC003/notes_T102-PH001-ST004-AC003.md`
  - `prompt/artifacts/tasks/T102/workspace/PH001/ST004/AC000/raw/raw_T102-PH001-ST004_AC000_2026-02-09_p1.txt`

**External sources (for “industry best practice” claims)**:
- ADR best practices and linking to avoid duplication. [1][2]
- Requirements/change management: baselines, change control, bidirectional traceability. [3][4][5]
- Scaled coordination artifacts for dependency visibility (central boards). [9]
- Documentation modularity and “only what stakeholders need” posture. [6][8]
- “Single source of truth” motivation (reduce duplication/out-of-date via link-first). [7][8]

**Limitations**:
- Repository is not a Git worktree in this environment, so a commit hash/tag cannot be recorded (see Section VI).
- Some external standards named in T102 artifacts (e.g., ISO/IEC/IEEE 29148) are not freely accessible; benchmarking relies on openly accessible practitioner guidance (NASA, SEBoK, SAFe, ADR references).

---

## Ingestion Directive Traceability (RES-004 + RES-005)

The following table maps all 8 ingestion directives (RES-004 + RES-005) to the exact report locations where they are addressed, as required for consultant/client handoff.

| Directive Source | Directive # | Directive (1 sentence) | Where Addressed | Status | Notes / Follow-up |
| :--- | :---: | :--- | :--- | :---: | :--- |
| RES-004 | 1 | Pattern (c) viability assessment: Concept as an I&R aggregation/dashboard surface (structural design + tradeoffs vs SPS-only). | Topic 7.B (viability verdict + structural design + thresholds) | SATISFIED | — |
| RES-004 | 2 | Register-family scoping for I&R: where I&R sits relative to STD indexes, research registers, workscope registers; separate section vs unified register surface. | Topic 3.B (role model + register families) + Topic 7.B (I&R as conditional aggregation-only family) + Topic 10.B (default vs conditional surfaces) | SATISFIED | — |
| RES-004 | 3 | STD-007 interaction clause implications: “must be available for each scope” reading + directionality constraints + Concept aggregation semantics. | Topic 7.B (STD-007 interaction + directionality interaction) + Artifact Updates (`T102-STD-007`, `T102-STD-005`) | SATISFIED | — |
| RES-004 | 4 | Staleness dashboard feasibility: can Concept provide cross-scope staleness visibility; maintenance cost vs SPS-only cadence. | Topic 7.B (Age/Staleness Flag; manual-first) + Topic 6.B (Last Verified / Link Status indicators) | SATISFIED | — |
| RES-005 | 5 | Concept as coordination audit surface: evaluate register families Concept should host and define governance boundaries per family. | Topic 3.B (candidate role models + authority tiers) + Topic 10.B (option set + default/conditional register families) | SATISFIED | — |
| RES-005 | 6 | Register family interaction model: how Concept registers interact with embedded minimum viable SPS/Request snapshots + INT promotion loop boundary. | Exec Summary (embedded minimum viable + INT promotion) + Topic 3.B (authority tiers + interaction boundary) + Topic 7.B (pointers-only register rules) | SATISFIED | — |
| RES-005 | 7 | STD-001 coordination role clarification: absorb/refine vs confirm RES-005 Deltas D1–D2 into a comprehensive Concept role spec. | Topic 3.B (STD-001 alignment approach + RES-005 D1–D2 handling) + Artifact Updates (`T102-STD-001`) | SATISFIED | — |
| RES-005 | 8 | Drift detection feasibility: can Concept host drift detection indicators (e.g., link integrity, staleness signals) as register-level feature(s). | Topic 1.B (drift failure modes) + Topic 6.B (link integrity + “Last Verified”) + Topic 7.B (staleness signals) | SATISFIED | — |

---

## III. TOPIC FINDINGS

### Topic 1: Concept Inventory & Drift Audit
**Objective**: Establish the current Concept shape, what is active vs placeholder, and the major drift/tooling failure modes.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md:14`
  - **Observation**: “Identity & Operating Rules” is a placeholder comment block, not populated.
- **Source**: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md:66`
  - **Observation**: “Readiness Snapshot” and “Handoff Snapshot” sections are placeholders.
- **Source**: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md:83`
  - **Observation**: “Feature Register” section exists but is empty.
- **Source**: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md:86`
  - **Observation**: “Design Register” exists and points to story-level design logs.
- **Source**: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md:94`
  - **Observation**: “Research Artifacts Register” exists and uses version-suffixed filenames in links (e.g., `_v1.0.0`) and a versioned SPS source filename.
- **Source**: `prompt/scripts/skills/extract_adr.py:12`
  - **Observation**: ADR extraction tooling targets Concept as the SSOT (`DEFAULT_CONCEPT_PATH`).
- **Source**: Repro evidence snippet (local):
  - **Command**: `python3 -B prompt/scripts/skills/extract_adr.py --adr-id ADR-005`
  - **Key output**:
    ```text
    ERROR: Failed to extract ADR block: ADR start marker not found: {#t102-adr-005-id-spec}
    ```
  - **Observation**: Confirms current Concept does not contain the expected ADR anchor marker, so strict ADR extraction fails.

#### B. Analysis
**Current-state inventory table (active vs placeholder)**:

| Section / Surface | Location | Authority intent | Status | Drift / failure modes |
|:--|:--|:--|:--|:--|
| Identity & Operating Rules | Concept §III.A | Informative (process manual) | Placeholder | Missing “operating rules” encourages repetition elsewhere |
| Decision system: Initiative STD Index | Concept §III.B.1 | Index to normative standards | Active | Low drift risk if table kept small; path integrity required |
| Decision system: Epic/Feature STD Index | Concept §III.B.2–3 | Index | Active | Potential directionality ambiguity (upstream links to downstream artifacts) |
| Readiness Snapshot | Concept §III.C | Intended authoritative (per `T102C-STD-001`) | Placeholder | No readiness roll-up / blockers surface yet |
| Handoff Snapshot | Concept §III.D | Intended authoritative (per `T102C-STD-001`) | Placeholder | No package manifest / acceptance signals yet |
| Feature Register | Concept §III.E.1 | Candidate register | Empty | Undefined schema/ownership; risk of ad-hoc growth later |
| Design Register | Concept §III.E.2 | Links-only index (per `T102-STD-001-CLAUSE-003`) | Active | Possible directionality conflict; needs explicit “pointers-only” posture |
| Research Artifacts Register | Concept §III.E.3 | Normative register (per `T102-STD-006`) | Active but unreliable | Broken links (versioned filenames not present); source path drift |
| Integration & Interfaces | Concept §III.F | Informative | Placeholder | Missing “how registers interact” guidance |
| Governance | Concept §III.G | Normative/informative mix | Placeholder | No change-control policy described |

**Primary drift failure modes** (confirmed):
- **Broken link integrity in a normatively required register** (Research Register), which invalidates “Concept as master research landscape” in practice.
- **Tooling mismatch**: ADR extraction scripts assume Concept contains ADR blocks/anchors; it currently does not.

#### C. Governance Implication
- Concept is already performing “hub” duties (indices + registers), but without explicit operating rules, authority tiers, and maintenance protocol, it will remain a high-drift surface.
- Any recommended Concept role must include: (1) an explicit “pointers-only” boundary for downstream links, and (2) an explicit link-integrity + “last verified” discipline for registers that are treated as audit surfaces.

---

### Topic 2: SPS/Request “Bloat Drivers” and Candidate Offload Surfaces
**Objective**: Identify repeat patterns that drive bloat/duplication and propose offload targets that preserve “link-don’t-duplicate”.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md:214`
  - **Observation**: SPS already describes a “dynamic workspace” that aggregates exploration/decisions/linkages in parallel to stable documents, aligning with the Concept-as-hub framing.
- **Source**: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md:236`
  - **Observation**: Initiative-level Research table exists (local index).
- **Source**: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md:412`
  - **Observation**: Epic dossiers repeat “Research & Notes” and “Issues & Risks” surfaces per epic.
- **Source**: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md:270`
  - **Observation**: WBS map exists in SPS as the “what exists” index (initiative → epics → features).

#### B. Analysis
**Bloat-driver taxonomy (>=5 exemplars)**:

1) **Cross-scope discovery content repeats as narrative instead of as registers**
   - Symptom: WBS/discovery appears as both narrative and tables across multiple places.
   - Offload: Concept “Workscope Register + File Register” (Topic 5) as the initiative discovery index; SPS keeps WBS as authoritative input but references Concept for navigation.

2) **Coordination reminders repeat as boilerplate**
   - Symptom: Multiple artifacts restate workflow philosophy / “link-don’t-duplicate” rationale.
   - Offload: Concept “Operating Rules” section becomes the single referenced process manual; downstream artifacts reference it rather than restating.

3) **Register-like surfaces proliferate inside SPS**
   - Symptom: Research tables + I&R tables exist in initiative and each epic dossier (standards require them), which is structurally repetitive.
   - Mitigation (not full offload): Keep required local tables, but make Concept the “audit surface” (central navigation + drift indicators) so local tables can remain minimal and focused.

4) **Evidence-rich content and external benchmarking gets embedded as Notes**
   - Symptom: Notes sections include externally sourced “industry alignment” claims (and can grow unbounded).
   - Offload: Convert recurring “benchmark” notes into formal research artifacts (RES-###) indexed via `T102-STD-006` (Concept register + local tables), keeping Notes short.

5) **Broken-link risk creates compensating duplication**
   - Symptom: When Concept registers are unreliable (broken links), authors compensate by duplicating links/summaries in SPS/Request.
   - Offload: Repair and govern Concept registers; add manual link-integrity “last verified” fields so authors can trust the hub.

**Offload candidate list (Concept vs other vs keep local)**:
- **Move to Concept (register/index surface)**:
  - Workscope Register / File Register / Directory Outline pointers (Topic 5)
  - STD & decision navigation surfaces (Topic 4)
  - Research master register (Topic 6; already mandated)
  - Conditional: I&R aggregation dashboard (Topic 7)
- **Keep local (SPS/Request)**:
  - Minimum viable Inherited Considerations emphasis tables (per RES-005 hybrid architecture)
  - Local Research tables (mandated by `T102-STD-006`)
  - Canonical Issues & Risks tables per scope (mandated by `T102-STD-007`)
- **Move to dedicated artifacts (not Concept)**:
  - Full research bodies (already in `research/report/`)
  - Detailed design bodies (remain in `design/`)

#### C. Governance Implication
- The only sustainable way to reduce bloat without breaking standards is to **tighten the boundary**: local artifacts remain “minimum viable embedded”, while Concept becomes the **central index + audit surface** with strict “pointers-only” and drift-detection indicators.

---

### Topic 3: Concept Role Model (Process Manual + Hub) vs Alternatives
**Objective**: Define candidate role models and select a minimal viable role that satisfies both “initiative bridge/process manual” and RES-005’s “coordination audit surface”.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md:18`
  - **Observation**: Concept is defined as ADD + ADR compendium and includes a Design Log Register.
- **Source**: `prompt/artifacts/tasks/T102/T102C/standard/standard_T102C-STD-001_concept-architectural-framework.md:5`
  - **Observation**: Concept is defined as an eight-section architecture including readiness/handoff snapshots and registers.
- **Source**: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md:12`
  - **Observation**: Concept is mandated to host the master Research Artifacts Register (E.3).
- **Source**: `prompt/artifacts/tasks/T102/research/T102-RES-005/report_T102-RES-005_cross-scope-coordination-architecture.md` (Exec Summary and findings)
  - **Observation**: RES-005 explicitly positions Concept registers as the coordination “audit surface”.

#### B. Analysis
**Candidate role models (operational definition)**:

1) **ADR/ADD-first (legacy)**:
   - Concept is primarily ADR bodies + architecture description; registers are secondary.
   - Risk: encourages Concept bloat; conflicts with current reality (Concept already hosts indices/registers and is missing ADR bodies); does not address drift indicators.

2) **Hub-first (indexes + selected registers + audit surface)**
   - Concept is the initiative’s navigation + audit surface:
     - Indices: standards + decisions
     - Registers: research (mandatory), design (links-only), workscope/file (recommended)
     - Snapshots: readiness/handoff (lean, structured)
   - ADR bodies remain in their canonical homes (standards combined files and/or dedicated ADR files); Concept links to them.

3) **Index-only navigation surface**
   - Concept is only an index of links; no registers beyond what standards mandate.
   - Risk: fails the “audit surface” requirement (cannot provide cross-scope visibility or drift indicators); still leaves bloat pressure in SPS/Request.

**Recommended minimal viable Concept role (decision-ready)**:
- **Role**: “Initiative bridge / process manual” + “coordination audit surface” + “handoff authority surface”.
- **Authority tiers**:
  - **Normative bodies**: standards (`STD` + `CLAUSE`) and their nested ADR rationale (`<STD-ID>-ADR-###`).
  - **Authoritative snapshot**: Concept Handoff Snapshot package manifest + acceptance signals (per `T102C-STD-001-CLAUSE-002`).
  - **Audit registers**: Concept registers are **pointers-only** surfaces that aggregate metadata and IDs, never duplicate canonical bodies.
- **Interaction boundary (embedded vs centralized vs INT)**:
  - **Embedded minimum viable**: SPS/Request keep only the minimum tables/snapshots required by standards to preserve local emphasis.
  - **Centralized audit**: Concept hosts cross-scope indexes/registers as pointers-only inventories and drift indicators (manual first).
  - **INT promotion loop**: Coordination guidance MAY live in INT transiently, but MUST be promoted when relied upon as policy (`T102-STD-005-CLAUSE-005C`).
- **Strict exclusions**:
  - No full requirements bodies (Request owns)
  - No full design bodies (Design owns)
  - No duplicated research bodies (Research reports own)
  - No canonical I&R hosting (SPS owns; Concept may aggregate conditionally)

**RES-005 Deltas D1–D2 handling (STD-001 alignment packaging)**:
- RES-006 **confirms** the RES-005 “Concept as coordination audit surface” role and recommends `T102-STD-001` absorb the D1–D2 deltas as the **baseline**, then extend them into a comprehensive Concept role specification (recommendations-only; no clause drafting here).

#### C. Governance Implication
- `T102-STD-001-CLAUSE-003` requires alignment to reflect Concept’s already-mandated register role (STD-006) and the accepted audit-surface role (RES-005), while preserving the “Design Log Register links-only” intent.

---

### Topic 4: Standards + Decisions Surface: “STD Compendium” and Indexing Conventions
**Objective**: Define indexing conventions for STD/CLAUSE and nested decision records consistent with `T102-STD-005`.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md:62`
  - **Observation**: Clause IDs are `STDCID` = `<STD-ID>-CLAUSE-###`; decision records may be STD-nested (`<STD-ID>-ADR-###`).
- **Source**: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md:22`
  - **Observation**: Concept already provides an Initiative STD Index with canonical paths.

#### B. Analysis
**Recommended indexing conventions (recommendations-only)**:

1) **STD indexing (in Concept)**
   - Keep the existing Concept STD index table as the primary navigation surface:
     - `STD ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path`
   - Rule: Concept contains **links only** to canonical standard files; no duplication of clause text.

2) **Clause indexing (do not centralize in Concept by default)**
   - Clause IDs (`<STD-ID>-CLAUSE-###`) are already self-indexing inside the standard file structure.
   - Recommendation: Do not maintain a Concept-wide clause index unless a specific consumer requires it (high drift risk).
   - If a clause index is needed, prefer **per-STD mini-index inside the STD file** (closest to the canonical body).

3) **Decision record indexing**
   - Recognize two DRID constructions (per `T102-STD-005`):
     - Standalone ADRs: `<SID>-ADR-###` (if used)
     - STD-nested ADRs: `<STD-ID>-ADR-###` (informative rationale annex)
   - Recommendation: In Concept, maintain a *minimal* Decision Index only for “active/high-impact” decision records that are frequently referenced (<=20 entries), to limit maintenance burden.

4) **Tooling alignment (ADR extraction)**
   - Current ADR extraction scripts expect anchors in Concept and currently fail.
   - Recommendation package must choose one of:
     - **A. Restore ADR anchors/bodies in Concept** (and ensure they match the extraction format), OR
     - **B. Retarget extraction tooling to standards combined files** (extract `<STD-ID>-ADR-###` bodies from the canonical standard file instead of Concept).
   - Given “link-don’t-duplicate” and current migration to standards, **B** is the lower-drift target.

#### C. Governance Implication
- Without resolving ADR extraction alignment, any attempt to position Concept as a governed hub will continue to break “mechanical verification” workflows and impair standards enforcement skills that depend on extraction.

---

### Topic 5: Workscope + File Registers (Navigation & Discovery)
**Objective**: Define a minimal Concept workscope/file register set that supports onboarding and reduces “where is X?” bloat.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md:270`
  - **Observation**: SPS already contains an authoritative WBS map listing initiative/epics/features.
- **Source**: Directory layout under `prompt/artifacts/tasks/T102/consultant/` (filesystem)
  - **Observation**: Canonical subtrees exist (`concept/`, `sps/`, `request/`, `design/`, `standards/`, `research/`, `workspace/`).

#### B. Analysis
**Recommended minimal register set** (Concept hosts, pointers-only):

1) **Workscope Register** (what exists)
   - Purpose: initiative-level “inventory of scopes” to reduce repeated narrative and speed discovery.
   - Proposed schema:
     - `| Scope | Scope ID | Type | Name | Owner | Status | Canonical Artifact(s) | Last Verified |`
   - Example rows (seed from SPS WBS map):
     - `Initiative | T102 | Initiative | Consultancy Layer Architecture | Client | review | ../sps/sps_T102-CONSULTANT.md | 2026-02-10`
     - `Epic | T102A | SPS | SPS Workflow Implementation | LLM_Consultant | review | ../sps/sps_T102-CONSULTANT.md#1-t102a-epic-sps---sps-workflow | 2026-02-10`
     - `Epic | T102B | REQUEST | Request Workflow Implementation | LLM_Consultant | draft | ../sps/sps_T102-CONSULTANT.md#2-t102b-epic-request---request-workflow | 2026-02-10`
     - `Epic | T102C | CONCEPT | Concept Workflow Implementation | — | — | ../standards/T102C-STD-001_concept-architectural-framework.md | 2026-02-10`

2) **File Register** (where things live)
   - Purpose: map key artifacts to their roles; prevent drift across “versioned filename vs canonical filename” conventions.
   - Proposed schema:
     - `| Artifact | Role | Canonical Path | Owner | Update Trigger | Last Verified |`
   - Example entries:
     - `SPS | Stable governance baseline | ../sps/sps_T102-CONSULTANT.md | LLM_Consultant | Gate approvals | 2026-02-10`
     - `Concept | Audit surface + handoff locus | concept_T102-CONSULTANT.md | LLM_Consultant | Gate approvals; register updates | 2026-02-10`
     - `Research briefs | Commission scope | ../research/brief/* | LLM_Consultant | New commission; revision | 2026-02-10`
     - `Research reports | Evidence outputs | ../research/report/* | LLM_Researcher | Report acceptance; revision | 2026-02-10`

**Governance rules (to minimize drift)**:
- Every register row MUST be “pointers-only” (no duplicated bodies).
- Every register includes `Last Verified` (manual) and a clear `Owner`.
- Link integrity is checked at gates (manual checklist first; tooling later).

#### C. Governance Implication
- A workscope/file register is a low-cost way to operationalize “Concept as bridge” without turning Concept into a narrative dump.

---

### Topic 6: Research Registers (Interface with `T102-STD-006`)
**Objective**: Validate the dual-index model under an expanded Concept role and recommend maintenance protocol deltas.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md:12`
  - **Observation**: Dual-index model is normative: local SPS tables + Concept aggregation register (E.3).
- **Source**: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md:94`
  - **Observation**: Concept E.3 exists but references versioned filenames (`..._v1.0.0.md`) that are not present in `research/brief` and `research/report`.
- **Source**: Repro evidence snippet (local filesystem checks; key outputs only):
  - **Command**: `ls -la prompt/artifacts/tasks/T102/research/T102-RES-001/brief_T102-RES-001_research-integration-workflow.md`
    - **Key output**: `brief_T102-CONSULTANT_research-integration-workflow.md`
  - **Command**: `ls -la prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102-CONSULTANT_research-integration-workflow_v1.0.0.md`
    - **Key output**: `ls: cannot access 'prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102-CONSULTANT_research-integration-workflow_v1.0.0.md': No such file or directory`
  - **Command**: `ls -la prompt/artifacts/tasks/T102/consultant/research/report/report_T102-CONSULTANT_research-integration-workflow_v1.0.0.md`
    - **Key output**: `ls: cannot access 'prompt/artifacts/tasks/T102/consultant/research/report/report_T102-CONSULTANT_research-integration-workflow_v1.0.0.md': No such file or directory`
  - **Command**: `ls -la prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT_v1.1.0.md`
    - **Key output**: `ls: cannot access 'prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT_v1.1.0.md': No such file or directory`

#### B. Analysis
**Fit-for-purpose conclusion**:
- The dual-index architecture remains sound as the target *if* Concept’s register is made reliable (link integrity + filename discipline). This is consistent with RES-005’s conclusions and STD-006’s own Consequences section (manual verification drift risk).

**Recommended maintenance protocol deltas (recommendations-only)**:
1) **Concept remains the master “landscape view”** (consistent with `T102-STD-006-CLAUSE-006`), but only if:
   - All links use canonical (existing) filenames
   - “Source” column paths point to existing artifacts/anchors (no stale versioned filenames)
2) Add “manual drift indicators” to the Concept Research Register:
   - `Last Verified` (date) and `Link Status` (`OK` / `BROKEN`) columns
   - This enables Concept to fulfill an audit-surface role without automation (aligns with minimal automation constraint).

#### C. Governance Implication
- A normatively mandated “master register” that contains broken links is worse than having no master register: it creates false confidence and downstream duplication. Link integrity must be treated as a gate-time check until tooling exists.

---

### Topic 7: Issues & Risks Registers in Concept (Conditional Candidate)
**Objective**: Determine viability of Concept as an I&R aggregation/dashboard surface without violating RES-004’s SPS-only canonical baseline and without breaking directionality constraints.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md` (Findings; staleness discussion)
  - **Observation**: RES-004 recommends SPS-only baseline for I&R and identifies staleness visibility as a governance need (e.g., 90-day review policy recommendation).
- **Source**: `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md:288`
  - **Observation**: AC003 ingestion directives explicitly require evaluating Concept I&R aggregation viability and its interaction with STD-007 and directionality.
- **Source**: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` (spec)
  - **Observation**: I&R tables MUST be available for each scope and follow a strict schema and closure coupling rules.
- **Source**: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md:73`
  - **Observation**: Directionality rule forbids higher scope referencing lower scope (except INT exception), creating ambiguity for “Concept aggregates lower-scope I&R” unless a governed exception exists.

#### B. Analysis
**Viability verdict**: **CONDITIONAL (GO) — aggregation-only dashboard in Concept is viable** *if and only if* it is treated as a **pointers-only, non-normative** register family and does not replace canonical SPS scope tables.

**Structural design (if GO)**:
- Add Concept register family: **Issues & Risks Aggregation Register** (separate from canonical tables).
- Schema (proposed; pointers-only):
  - `| Item Type | Scope | Scope ID | ID | Title | Status | Priority | Age (days) | Staleness Flag | Source | Last Verified |`
- Rules:
  - **Do not duplicate** `Description`, `Resolution Notes`, `Mitigation Notes` (canonical remains in SPS).
  - `Source` points to the canonical scope section (at minimum the relevant Issues & Risks heading anchor; per-item anchors are an optional enhancement).
  - `Age` and `Staleness Flag` are computed manually at review time (no automation required).

**Threshold triggers (when to adopt vs defer)**:
- Adopt the Concept I&R aggregation register when any of:
  1) **2+ epics** have open I&R items, OR
  2) Initiative-level open issues average age exceeds **90 days**, OR
  3) Client requests cross-scope staleness visibility for gate review.
- Defer if:
  - Only a single scope has I&R and SPS remains clearly scannable without roll-ups.

**STD-007 interaction (recommendations-only)**:
- Clarify that “must be available for each scope” means **canonical tables exist in the scope’s SSOT artifact**, and Concept aggregation is an optional audit surface enhancement.

**Directionality interaction (recommendations-only)**:
- If Concept aggregates lower-scope I&R IDs, define a governed exception:
  - “Concept registers MAY reference downstream IDs for inventory/audit purposes when explicitly labeled pointers-only and non-normative.”

#### C. Governance Implication
- Without an explicit directionality exception and a strict pointers-only schema, Concept I&R aggregation risks becoming duplication and drifting into a second canonical log.

---

### Topic 8: Initiative Overview Assets (Diagrams, Directory Outlines)
**Objective**: Define rules for including overview assets without causing Concept bloat.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md:66`
  - **Observation**: “Readiness Snapshot” and “Handoff Snapshot” are planned but not implemented; overview assets are not yet present.
- **Source**: External documentation guidance emphasizes matching docs to user needs and using modular, link-first structure to avoid duplication. [6][8]

#### B. Analysis
**Governance rubric for overview assets**:
- Allowed asset types (max 1 each unless Client approves):
  - System context diagram (text-based or link)
  - High-level component diagram (C4 L2-style, minimal)
  - Directory outline (tree or link to file register)
- Inclusion rule:
  - Include only if it answers a recurring onboarding question that cannot be answered by registers alone.
- Anti-sprawl controls:
  - Every asset row includes `Owner` + `Last Verified`.
  - Assets MUST be links to canonical files when possible; avoid embedding large diagrams inline.

#### C. Governance Implication
- Overview assets should be treated as a governed register family, not as an open-ended narrative section.

---

### Topic 9: PM Link Surfaces (Plans/Roadmaps pointers)
**Objective**: Link to planning artifacts without collapsing artifact boundaries.

#### A. Evidence & Forensics
- **Source**: `prompt/artifacts/tasks/T102/workspace/PH001/ST004/plan_T102-PH001-ST004.md` (stream plan)
  - **Observation**: Plans exist as workspace governance artifacts; they are not SSOT execution artifacts but are essential navigation for initiative work.
- **Source**: Concept has placeholder “Integration & Interfaces” and “Governance” sections intended to host coordination pointers (but not planning logs). (`concept_T102-CONSULTANT.md:104`)

#### B. Analysis
**Pointers-only pattern**:
- In Concept, create a “Plans & Roadmaps” mini-index (<=10 links):
  - `| Artifact | Purpose | Canonical Path | Owner | Last Verified |`
- Rules:
  - No operational task logs in Concept.
  - Concept only links to the latest canonical plan per stream/phase.
  - Planning artifacts remain the execution surface; Concept is the discovery hub.

#### C. Governance Implication
- This preserves the boundary: Concept is the bridge; workspace plans are the process record.

---

### Topic 10: Options Matrix (3–5 architectures) + Weighted Rubric
**Objective**: Compare Concept architectures and recommend a target role model, explicitly accounting for RES-004/RES-005 constraints and drift risks.

#### A. Evidence & Forensics
- **Source**: Current Concept is already partly “hub + registers” (STD index + design + research). (`concept_T102-CONSULTANT.md:22`, `:86`, `:94`)
- **Source**: Dual-index drift is already observed (broken links in Concept research register). (`concept_T102-CONSULTANT.md:94`; see Topic 6)
- **Source**: RES-005 requires Concept to act as an audit surface in a hybrid coordination architecture.

#### B. Analysis
**Scoring rubric** (1–5, higher is better). **Weights sum to 100**:
- Governance fit / authority clarity: 25
- Drift risk / maintainability: 25
- Scanability (human): 20
- LLM context cost: 15
- Audit-surface completeness (RES-005 fit): 15

**Options matrix**:

| Option | Summary | Gov Fit (25) | Drift (25) | Scan (20) | LLM (15) | Audit (15) | Weighted Score |
|:--|:--|--:|--:|--:|--:|--:|--:|
| (a) Index-only | Indices only; minimal registers | 3 | 4 | 4 | 5 | 2 | 3.60 |
| (b) Hub + selected registers | Indices + research + design + workscope/file | 4 | 3 | 4 | 4 | 4 | 3.75 |
| (c) Hub + expanded registers | Adds I&R + overview assets + readiness/handoff | 4 | 2 | 3 | 3 | 5 | 3.30 |
| (d) Dedicated registers artifacts | Move registers to separate files; Concept indexes | 3 | 4 | 3 | 4 | 4 | 3.55 |
| (e) Hybrid thresholds | Start with (b), add (c) families only when triggers met | 5 | 4 | 4 | 4 | 5 | 4.40 |

**Rationale (high-level)**:
- (a) fails the audit-surface requirement (RES-005) because it cannot host drift indicators or cross-scope summaries without becoming more than an index.
- (c) meets audit-surface completeness but increases maintenance burden and drift risk unless scale justifies it.
- (e) scores best because it makes the architecture explicit, limits default surface area, and introduces register families only when they pay for their maintenance cost (consistent with link-first / SSOT guidance to reduce duplication and drift). [6][7][8]

**Recommendation**: Adopt **Option (e)** with an explicit “default register set” and explicit triggers:
- Default Concept surfaces (always):
  - Initiative STD index
  - Design register (links-only)
  - Research artifacts register (mandatory per STD-006)
  - Workscope/file registers (recommended baseline)
  - Readiness/handoff snapshots (lean; per T102C-STD-001)
- Conditional surfaces (only when triggers are met):
  - I&R aggregation dashboard (Topic 7)
  - Overview assets (Topic 8)
  - Expanded coordination inventories (dependencies roll-ups) if hybrid coordination scales

#### C. Governance Implication
- This option requires a standards alignment package (recommendations-only) to eliminate the current mismatch between STD-001’s Concept framing and the already-standardized register role (STD-006) and Concept framework (T102C-STD-001).

---

## IV. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-006-ISSUE-001` | ADR extraction tooling | ADR-print scripts fail due to missing Concept anchors; reduces ability to mechanically validate governance ADR surfaces that depend on Concept extraction | LLM_Researcher | `OPEN` | `MEDIUM` | 2026-02-09 | — | — |
| `T102-RES-006-ISSUE-002` | Scope overlap control | RES-006 touches Concept implications also discussed in RES-004/RES-005; researcher must avoid re-evaluating settled dependency inputs | LLM_Researcher | `RESOLVED` | `LOW` | 2026-02-09 | Resolved by strict adherence to dependency hierarchy: RES-004 baseline (SPS-only I&R) and RES-005 hybrid coordination treated as inputs; this report focused on Concept role + register boundaries only. | 2026-02-10 |
| `T102-RES-006-ISSUE-003` | Concept research register link drift | Concept E.3 Research Register contains broken versioned links and stale source paths, undermining Concept’s “audit surface” reliability | LLM_Researcher | `OPEN` | `HIGH` | 2026-02-10 | — | — |
| `T102-RES-006-ISSUE-004` | Directionality ambiguity for Concept registers | `T102-STD-005` directionality forbids upstream→downstream references (except INT), but Concept audit-surface registers may need downstream pointers/aggregation | LLM_Researcher | `IN-REVIEW` | `MEDIUM` | 2026-02-10 | Proposed resolution: define an explicit “pointers-only audit register” exception for Concept surfaces and clarify that this does not affect inheritance/obligation directionality. | — |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-006-RISK-001` | Unfalsifiable Concept hub | “Process manual” framing may expand scope beyond decision-ready evaluation, producing an unfalsifiable report | LLM_Researcher | `MITIGATED` | `MEDIUM` | 2026-02-09 | Mitigated by forcing a weighted options matrix (Topic 10) + explicit “what belongs / does not belong” boundary list (Topic 3) + conditional triggers (Topics 7–9). | 2026-02-10 |
| `T102-RES-006-RISK-002` | Dependency churn | RES-006 conclusions may change materially after RES-005 coordination architecture recommendations, forcing re-scope at GATE-001B | LLM_Researcher | `CLOSED` | `LOW` | 2026-02-09 | Closed: RES-004 and RES-005 reports were accepted before this report; their integration analyses were treated as fixed inputs. | 2026-02-10 |
| `T102-RES-006-RISK-003` | Manual audit surface drift | Concept registers require manual synchronization; without gate-time checks, Concept can become unreliable and drive duplication elsewhere | LLM_Researcher | `MONITORED` | `HIGH` | 2026-02-10 | Mitigation: add “Last Verified” + link integrity checks at gates; keep register surfaces small by default (Option e thresholds). | — |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `T102-STD-001` | `T102-STD-001-CLAUSE-003` | Recommendations-only: align Concept definition to include “coordination audit surface + register hub” and reference Concept framework (`T102C-STD-001`) and register obligations (`T102-STD-006`) | Topic 3, Topic 10 |
| `T102-STD-005` | `T102-STD-005-CLAUSE-003` (Directionality) | Recommendations-only: clarify whether Concept audit-surface registers may point to downstream artifacts/IDs as non-normative inventory, and define the exception boundaries | Topic 3, Topic 7 |
| `T102-STD-006` | CLAUSE-004 (maintenance protocol) | Recommendations-only: add explicit link integrity verification step and/or “Last Verified” indicators for Concept master register; repair filename/link discipline | Topic 6 |
| `T102-STD-007` | CLAUSE-001 / CLAUSE-009 (interpretation) | Recommendations-only: clarify canonical hosting vs optional aggregation, and how Concept aggregation (if adopted) interacts with per-scope availability rules | Topic 7 |
| `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` | `9. Research` | **ReportOnly packaging requirement**: register `T102-RES-006` in the SPS local Research table per `T102-STD-006` (include canonical brief/report paths and metadata; do not use version-suffixed filenames unless they exist). | This report metadata + Section VI (Brief Version) |
| `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md` | `E.3 Research Artifacts Register` | **ReportOnly packaging requirement**: register `T102-RES-006` in the Concept master Research Artifacts Register per `T102-STD-006`, and verify link integrity (no version-suffixed “ghost artifact” filenames). | This report metadata + Topic 6 evidence |
| `concept_T102-CONSULTANT.md` | §III.A, §III.C–G, §III.E | Implement role boundaries: fill “Operating Rules”; add workscope/file registers; repair Research Register links; clarify “pointers-only” policy for downstream links; implement lean readiness/handoff surfaces | Topic 1, Topic 3, Topic 5, Topic 6, Topic 10 |
| `prompt/scripts/skills/extract_adr.py` (+ extractor dependencies) | ADR extraction target | Decide: restore ADR anchors in Concept OR retarget extraction to canonical standards combined files; update tooling accordingly | Topic 1, Topic 4 |

---

## VI. SOURCE MATERIAL

**Brief Version**: `prompt/artifacts/tasks/T102/research/T102-RES-006/brief_T102-RES-006_concept-role-dynamic-registers.md` v2.0.0 (2026-02-10)

**Code Commit/Tag**: `—` (environment is not a Git repository; `git rev-parse` unavailable)

**Files Cited (non-exhaustive)**:
- `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
- `prompt/artifacts/tasks/T102/T102C/standard/standard_T102C-STD-001_concept-architectural-framework.md`
- `prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md`
- `prompt/artifacts/tasks/T102/research/T102-RES-005/report_T102-RES-005_cross-scope-coordination-architecture.md`
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md`
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md`
- `prompt/scripts/skills/extract_adr.py`

**External Sources (for cited “best practice” claims)**:
- [1] Michael Nygard — “Documenting Architecture Decisions” — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions — Accessed: 2026-02-10
- [2] MADR — “Use Markdown Architectural Decision Records” — https://adr.github.io/madr/decisions/0000-use-markdown-architectural-decision-records.html — Accessed: 2026-02-10
- [3] SEBoK — “Requirements Management” — https://sebokwiki.org/wiki/Requirements_Management — Accessed: 2026-02-10
- [4] NASA — “Requirements Management” — https://www.nasa.gov/reference/6-2-requirements-management/ — Accessed: 2026-02-10
- [5] NASA — *NASA Systems Engineering Handbook* (NASA/SP-2016-6105 Rev2) — https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf — Accessed: 2026-02-10
- [6] Diátaxis Framework — https://diataxis.fr/ — Accessed: 2026-02-10
- [7] GitLab Handbook — “Handbook usage” (single source of truth; handbook-first linking) — https://handbook.gitlab.com/handbook/about/handbook-usage/ — Accessed: 2026-02-10
- [8] arc42 — “Tips (1–22)” (cross-referencing; avoid duplication) — https://docs.arc42.org/tips/1-22/ — Accessed: 2026-02-10
- [9] SAFe — “PI Planning” (dependencies visibility) — https://scaledagileframework.com/pi-planning/ — Accessed: 2026-02-10
