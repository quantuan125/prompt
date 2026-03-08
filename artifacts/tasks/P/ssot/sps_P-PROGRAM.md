---
artifact_type: 'SPS'
initiative_id: 'P'
initiative_code: 'PROGRAM'
version: '0.7.0'
date: '2026-03-07'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

## III. CORE CONTENT

### A. Problem Definition

#### 1. The Problem

There is no canonical, program-level SSOT home for cross-initiative governance (e.g., program standards, program status orchestration). Without a deterministic root, program standards become coupled to individual initiatives, and adoption becomes inconsistent across `prompt/artifacts/tasks/**`.

#### 2. The Desired Outcome

Establish a program governance spine that:
1) Provides a deterministic program SSOT root (`prompt/artifacts/tasks/P/**`).
2) Defines program standards (`P-STD-*`) to govern artifact placement and status reporting for `prompt/artifacts/tasks/**`.
3) Enables consistent downstream adoption (e.g., `T104` as first adopter) without duplication drift.

#### 3. Business Case

Program-level determinism reduces governance overhead and prevents cross-initiative drift, enabling reliable agentic retrieval and future automation (e.g., status orchestration) without forcing retroactive bulk migrations.

### B. Initiative Considerations

#### 1. Organization & Responsibilities

**Role Definitions**

| Actor | Role Title(s) | Decision Rights | Primary Responsibilities | Scope Notes |
| :--- | :--- | :--- | :--- | :--- |
| `Client` | Decision Owner | Approves baselines and cutover | Sets priorities; resolves scope conflicts; approves standards and status model | Program-wide |
| `LLM_Consultant` | Technical Consultant | Proposes baselines; no final approval | Authors plans/standards drafts; maintains program SSOT coherence | Program-wide |
| `LLM_Developer` | Lead Engineer | Advises feasibility | Implements approved changes; provides verification evidence | Implementation-only |

**Governance RACI**

| Governance Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
| :--- | :--- | :--- | :--- | :--- |
| Approve program baseline | `LLM_Consultant` | `Client` | `LLM_Developer` | — |
| Approve program standards | `LLM_Consultant` | `Client` | `LLM_Developer` | — |
| Approve status model | `LLM_Consultant` | `Client` | `LLM_Developer` | — |

#### 2. Project Assumptions

* **P-ASSUM-001 (Forward-only Adoption)** — Program standards MAY be adopted forward-only without requiring immediate bulk migration of legacy artifacts, unless explicitly scoped.

#### 3. Project Constraints

* **P-CON-001 (Authority Boundary)** — Program standards govern `prompt/artifacts/tasks/**` only (including raw + SSOT + workspace artifacts) and do not govern all of `prompt/**`.
* **P-CON-002 (Link Don’t Duplicate)** — Adopter initiatives SHALL reference program standards by ID/path and SHALL NOT duplicate program normative content.
* **P-CON-003 (Artifact Format Governance)** — (A) Planning, SSOT, and governance specification artifacts — including plans, notes, roadmaps, SPS files, combined standard-specification files, and decision records — SHALL be Markdown files (`.md`) with YAML frontmatter, per `P-STD-001`. (B) Programmatic execution artifacts — including status ledgers and machine-readable schema files — MAY use non-Markdown formats (e.g., `.yaml`, `.json`) when explicitly permitted by the governing standard for that artifact type. File naming and placement SHALL still conform to `P-STD-004`.

#### 4. Quality Goals

* **P-QG-001 (Deterministic Retrieval)** — Program artifacts SHALL have deterministic paths and predictable naming to support agentic and human retrieval.
* **P-QG-002 (Traceability Integrity)** — Cross-artifact links SHALL preserve single-source-of-truth integrity (link-don’t-duplicate).

#### 5. Dependencies

* **P-DEP-001 (T102 Standards Stack)** — Program governance SHALL remain consistent with `T102` governance (ID rules, research workflow, issues/risks patterns) and explicitly cite adopted references where applicable.

#### 6. Interfaces

* **P-IF-001 (Status Interface)** — Program status reporting SHALL be expressed as a machine-readable artifact (planned under `P-PH000-ST002`).

#### 7. Project Standards

| STD ID | Title | Status | Owner | Effective | Supersedes | Canonical Path | Verification | Governed By | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:---------------|:-------------|:------------|:----------|
| `P-STD-001` | **Program Governance Standard** | `accepted` | LLM_Consultant | 2026-02-22 | `T102-STD-004` | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` | Review: all CLAUSEs re-identified; alias window documented; guideline/template aligned; gap remediation per promotion contract; SES003 derivative conformance audit passed | `P-STD-005` | — |
| `P-STD-002` | **Program Status Standard** | `accepted` | LLM_Consultant | 2026-03-04 | — | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | Review: GATE-001 verification completed and authoritative GDR recorded (APPROVE, 2026-03-04); standard governs canonical 7-state lifecycle, transitions, health/RAG, dependency visibility, evidence linkage, update protocol, and status artifact rules | `P-STD-001` | `P-RES-001` |
| `P-STD-003` | **Program Governance Standards Model** | `planned` | LLM_Consultant | — | — | `prompt/artifacts/tasks/P/standard/P-STD-003_governance-standards-and-dr-index.md` | Review: combined governance spec aligns with ADR-004 + ADR-009; enforce adoption/authoring requirements | `P-STD-001` | `T102-STD-009` |
| `P-STD-004` | **File Naming & Directory Convention** | `draft` | LLM_Consultant | — | — | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` | Review: initiative dirs conform to naming/directory rules; CI: lint file prefixes + directory structure | `P-STD-001` | — |
| `P-STD-005` | **Universal ID Specification** | `draft` | LLM_Consultant | — | `T102-STD-005` | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` | CI: regex validation of all IDs; Review: scope/token compliance | `P-STD-001` | `T102-STD-005`, `T104-STD-002` |

* **P-STD-001 (Program Governance Standard)** — All combined standard-specification files across `prompt/artifacts/tasks/**` MUST conform to the authoring model defined by this standard's canonical specification. Governs file structure, CLAUSE construction, substandard architecture, decision record format, STD index schema, conformance coupling, and specification lifecycle.
  - **Minimum Viable Conformance**: Combined files follow `P-STD-001-CLAUSE-001` canonical structure; CLAUSEs render per `P-STD-001-CLAUSE-018B`; ADR bodies use `P-STD-001-CLAUSE-025` template; STD Index entries conform to `P-STD-001-CLAUSE-012A` schema.
  - External Reference: `P-STD-005 (Universal ID Specification)`, `T102-CON-009 (Controlled Vocabulary for Normative Language)`

* **P-STD-002 (Program Status Standard)** — Program work-item status reporting across `prompt/artifacts/tasks/**` MUST use the canonical lifecycle authority defined by this standard. It governs the 7-state status vocabulary, allowed transition rules, health/RAG assessment, dependency visibility, evidence linkage, update protocol, and status artifact contract.
  - **Minimum Viable Conformance**: Work-item surfaces use canonical lifecycle states per `P-STD-002-CLAUSE-001`; lifecycle transitions follow `P-STD-002-CLAUSE-005`; `blocked` vs `on_hold` semantics follow `P-STD-002-CLAUSE-009`; manual-gate/waiting-approval mappings follow `P-STD-002-CLAUSE-011`; status artifacts follow the authority and schema rules defined in `P-STD-002E`.
  - External Reference: `P-STD-001 (Program Governance Standard)`, `P-STD-005 (Universal ID Specification)`, `P-RES-001 (Status Standard Research)`, `P-RES-002 (Agentic Status Systems Research)`

* **P-STD-004 (File Naming & Directory Convention)** — All initiative directories under `prompt/artifacts/tasks/` SHALL follow standardized file naming prefixes and directory structure conventions. This standard will codify deterministic artifact placement to support agentic retrieval and cross-initiative consistency.
  - **Minimum Viable Conformance**: TBD (pending proposal from `T104-PH001-ST002-AC000`)
  - Canonical Path: `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`

* **P-STD-005 (Universal ID Specification)** — All program and initiative artifacts SHALL conform to a unified ID specification governing scope IDs, tokenized IDs, timeline entity UIDs, and file naming derivations. This standard unifies workscope rules (superseding `T102-STD-005`) and absorbs timeline UID scope (planned as `T104-STD-002`) into a single program-level normative specification. `P-STD-003 (Governance Standards Model)` serves as an extension of this standard for `STD` token-type specifics.
  - **Minimum Viable Conformance**: All IDs conform to `P-STD-005-CLAUSE-001` (Patterns 1–4); formal references conform to `P-STD-005-CLAUSE-004` (Reference Semantics).
  - External Reference: `T102-CON-009 (Normative Keywords)`, `P-STD-003 (Program Governance Standards Model)`

#### 8. Project Guidances & Notes

**Implementation Guidance**
* **P-IG-001** — Keep Phase `PH000` limited to planning spine + SSOT shells; defer normative standard bodies to `P-PH000-ST001`.

**Integration Guidance**
* **P-INT-001** — Adopter initiatives (e.g., `T104`) should bind via a single initiative-scoped RID that cites `P-STD-001` and `P-STD-002` once authored.

**Notes**
* **P-NOTE-001** — `P-RES-###` is permitted because the `RES` token allows Program scope under `P-STD-005` (see `P-STD-005-CLAUSE-002`).

#### 9. Research

| Research ID | Title | Summary | Reference | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-001` | **Status Standard Research** | Deep research into program-level status governance: canonical 7-state enum + transition rules, health/RAG thresholds, unified dependency schema (FS/SS/FF/SF), evidence linkage protocol, update protocol (role accountability), status artifact format options. Consumed by `P-PH000-ST001-AC003`. | `P-PH000-ST001-AC003` | `prompt/artifacts/tasks/P/research/P-RES-001/brief_P-RES-001_status-standard-research.md` | `prompt/artifacts/tasks/P/research/P-RES-001/report_P-RES-001_status-standard-research.md` |
| `P-RES-002` | **Agentic Status Systems Research** | Research benchmarking agentic CLI + orchestration-layer status systems (Codex CLI, Claude Code, Gemini CLI; GitHub Actions + GitLab CI/CD; GitHub Checks vs Commit Status) to inform repo-native evidence linkage, aggregation semantics, and bridging patterns for `P-STD-002`. Consumed by `P-PH000-ST001-AC003`. | `P-PH000-ST001-AC003` | `prompt/artifacts/tasks/P/research/P-RES-002/brief_P-RES-002_agentic-status-research.md` | `prompt/artifacts/tasks/P/research/P-RES-002/report_P-RES-002_agentic-status-research.md` |

#### 10. Issues & Risks

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | — | — | — | — | — | — | — |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| `P-RISK-001` | T102 grandfathering dual-pattern | T102 `consultant/` structure is grandfathered indefinitely; creates two incompatible patterns. | LLM_Consultant | `Active` | `Medium` | 2026-02-11 | Sunset milestone when T102 enters next phase after current active epics complete. | |
| `P-RISK-002` | P-STD-004 scope creep | T104-specific choices may get baked into P-level standard without cross-validation. | LLM_Consultant | `Active` | `High` | 2026-02-11 | P-STD-004 MUST validate against minimum 2 additional initiatives before `effective` status. | |


### C. Epics & Breakdown

#### 0. Initiative WBS Map

| Level | PM Type | ID | Name |
| :--- | :--- | :--- | :--- |
| 1 | Initiative | P | Program Governance |

---

## IV. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.7.0 | 2026-03-07 | Amendment | P-STD-002 registered as `accepted` after authoritative GATE-001 approval (effective 2026-03-04). Added P-STD-002 body entry with minimum viable conformance + external references. Evidence: `proposal_P-PH000-ST001-AC003-GATE-001_gir-disposition-package.md` and AC003 TK005 implementation. |
| v0.6.1 | 2026-03-01 | Update | P-STD-004 registered as `draft` with Canonical Path set to the authored standard file. |
| v0.6.0 | 2026-02-25 | Amendment | Registered `P-RES-002` in the Research table with brief + report links. |
| v0.5.0 | 2026-02-23 | Amendment | P-STD-005 promotion recorded: status `draft`, supersedes `T102-STD-005`, canonical path set. P-STD-001 now governed by `P-STD-005`. P-NOTE-001 updated (RES allows Program scope). |
| v0.4.0 | 2026-02-23 | Amendment | P-CON-003 revised to `(Artifact Format Governance)` with (A) MD for planning/SSOT, (B) non-MD permitted for programmatic artifacts (DEC-003). P-STD-002 row updated: broad-scope description, Canonical Path, Reference `P-RES-001` (DEC-001). P-RES-001 registered in Research table (DEC-007). Evidence: `raw_P-PH000-ST001-AC003-SES001.txt` |
| v0.3.0 | 2026-02-22 | Major | STD Index schema migrated to `P-STD-001-CLAUSE-012A`: added `Canonical Path` and `Governed By` columns; removed `Adopts` column; `Reference` column corrected to RID-only; `Title` bolded; `Effective` corrected to ISO-8601/`—`. P-STD-001 body added. P-STD-001 status flipped to `accepted` (GATE-002 approval). P-STD-004 body updated for `Canonical Path` terminology. Source: `P-PH000-ST001-AC002-SES003-DEC007`, `DEC008`. |
| v0.2.2 | 2026-02-20 | Update | `P-STD-001` status updated to draft; canonical path and supersedes populated following full promotion from `T102-STD-004`. |
