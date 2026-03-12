---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
epic_id: 'T102B'
feature_id: 'T102B1'
feature_code: 'RST'
version: '0.2.0'
date: '2026-02-08'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
source_request: 'prompt/artifacts/tasks/T102/T102B/ssot/request_T102B1-RST.md'
---

# PROPOSAL: RST (T102B1) — Non-Normative Notes & Analysis

## I. EXECUTIVE SUMMARY

This proposal contains **non-normative** content that was originally drafted during AC002 and has been intentionally moved out of the feature-level Request specification (`request_T102B1-RST.md`) to keep the Request focused on the canonical section structure and requirements per `T102B-STD-002`.

## II. MOVED CONTENT INDEX

Moved from `request_T102B1-RST.md` into this proposal:
- Requirements-with-Guidance Pattern (authoring pattern explanation)
- Industry Alignment Mapping (Conceptual)
- RLITE Derivation Feasibility Check (Informative)
- Appendix additions (Validation Checklist, Next Steps)

---

## III. REQUIREMENTS-WITH-GUIDANCE PATTERN (AUTHORING)

This Request follows **explicit ID referencing**: higher-precedence rules are implicitly inherited, but only the most critical inherited items are explicitly emphasized here (ID references only; no upstream text restatement).

RST uses the “requirements-with-guidance” pattern per `T102B-IG-002`:
- **Normative requirements** SHALL be stated using requirements language (e.g., SHALL/SHOULD) and written so the requirement is understandable without separate “Implementation Guidance” sections.
- **Inline authoring guidance** MUST be clearly marked as guidance (e.g., `Guidance:` prefix or HTML comment blocks) and MUST NOT introduce new obligations beyond the associated requirement statement.
- If guidance becomes enforceable policy, it SHOULD be promoted into a governing `STD/ADR` (or into an explicit `FR/NFR/CON`) rather than living indefinitely as free-form prose.

Applicability: This Request has `story_count = 4`, so Story Index is required per `T102B-STD-002-CLAUSE-004`.

Definition: `story_count` is the number of Story rows in the Story Index table (excluding the header row).

This section is navigation only and SHALL NOT include detailed story-level FR bodies or story-level acceptance criteria (deferred to `T102D (DESIGN)` per `T102B-STD-003`).

---

## IV. INDUSTRY ALIGNMENT MAPPING (CONCEPTUAL)

This mapping is intentionally conceptual (no clause-by-clause compliance matrix in Phase 1). Evidence is captured in `T102B-RES-001`.

| RST Section | ISO 29148 (conceptual) | BABOK v3 (conceptual) | SAFe (conceptual) | Evidence (internal) |
|:-----------|:------------------------|:----------------------|:------------------|:--------------------|
| I. Executive Summary | Purpose + overview | Business need framing | Feature intent + benefit framing | `T102B-RES-001` Topics 1–3 |
| A. Problem Definition | Problem/purpose context | Problem statement | “Just enough” feature context | `T102B-RES-001` Topic 3; W1–W7 |
| B. Scope | Scope definition | Scope definition | Feature boundaries | `T102B-RES-001` Topic 1 |
| C. Business Objectives | Success criteria | Goals/objectives/outcomes | Benefit hypothesis + success signals | `T102B-RES-001` Topic 3; Proposal P6 |
| D. Stakeholders | Stakeholder needs framing | Stakeholder analysis | Stakeholder alignment | `T102B-RES-001` Topic 2 |
| E. Inherited Considerations | Traceability emphasis | Governance trace to upstream constraints | Epic→Feature linkage | `T102-STD-003`, `T102-STD-005` |
| F. Feature Requirements | Requirements specification | Requirements definition | Feature-level requirements | `T102B-RES-001` Topics 1–3 |
| G. Governance Standards | Standards conformance indexing | Governance framework | Guardrails / governance standards | `T102B-RES-001` Topic 4 (S4); `T102-STD-009` |
| H. Feature Guidance & Notes | Informative annexes / guidance material | Supplementary information | Pragmatic enabler guidance | `T102B-RES-001` Topic 4; `T102-STD-005` |
| Removed (was H). Issues & Risks | Removed from Request; hosting deferred to `T102-RES-004` | Removed from Request; hosting deferred to `T102-RES-004` | Removed from Request; hosting deferred to `T102-RES-004` | `T102B-RES-001` Topic 5; `T102B-RES-002` Topic 4C |
| I. Research | Evidence linkage | Evidence/assumptions trace | Lightweight evidence pointers | `T102B-RES-001` methodology + sources |
| J. Story Index | Requirements allocation (navigation only) | Decomposition/navigation | Feature→Story navigation (no story FR bodies) | `T102B-RES-001` Topic 3; `T102B-STD-003` |
| K. Acceptance Criteria | Verification criteria | Success measures | Feature AC expectations | `T102B-RES-001` Topic 3 |
| IV. Approval Gate | Gate evidence + sign-off | Governance checkpoint | Feature-level “done” for Request stage | `T102B-STD-003`; `T102B-STD-002-CLAUSE-004` |

---

## V. RLITE DERIVATION FEASIBILITY CHECK (INFORMATIVE)

- RLITE is a governed subset of RST per `T102B-STD-004-CLAUSE-002` (mandatory sections only).
- Boundary target: RLITE artifacts remain <200 lines per `T102B-STD-004-CLAUSE-001`; if the mandatory subset cannot meet the boundary, escalate to Full Request per `T102B-STD-004-CLAUSE-005`.
- RST supports derivation by using `[M]` markers for mandatory sections and keeping optional sections fully omittable (no placeholder required).

---

## VI. REQUEST APPENDIX ADDITIONS (PROCESS / CHECKLISTS)

### A. Validation Checklist

- [x] Problem statement traces to T102B-RES-001 weaknesses (W1-W7)
- [x] Scope explicitly includes P1-P4 proposal implementation
- [x] Business objectives map to T102B quality goals
- [x] Inherited considerations emphasize Initiative + Epic rule IDs (no upstream text restatement)
- [x] Inherited considerations table schema follows `T102-STD-003-CLAUSE-001`
- [x] Feature requirements address structural changes
- [x] Story Index applicability rule documented (required-if `story_count > 1`)
- [ ] Issues & Risks removed from Request; items promoted to epic scope per D2
- [ ] Governance Standards section uses STD index schema per `T102-STD-009`
- [ ] Feature Guidance & Notes section has IG/INT/NOTE `####` subheadings
- [ ] RID tables use unified schema with Reference column
- [ ] Changelog section present with version history
- [ ] Acceptance Criteria relocated to `### K.` under Core Content
- [ ] Client approval obtained

### B. Next Steps

**Downstream Consumer**: Stream ST001 (AC002.1→AC003–AC005)

**Implementation Path**:
1. AC002.1: RST specification remediation — apply all structural corrections per this proposal
2. AC003: RST template formalization — author `prompt/templates/request/request_structural_template.md`
3. AC004: RST self-validation & retrofit — retrofit this Request toward v1.0 full conformance (includes INT population, marker removal, Problem Statement rewrite, `T102-RES-004` absorption)
4. AC005: Client approval gate — obtain approval statement and close ST001

---

## VII. AC002 RE-REVIEW DECISIONS & RATIONALES

### A. Decision Log (D1-D13)

#### D1 — Section G Redesign: Governance Decisions → Governance Standards
- **Context**: Section G used a `GDR` index schema (`| GDR ID | Title | Status | Owner | Effective | Reference |`). Per `T102-STD-009-CLAUSE-005`, no new GDR creation is permitted after migration cutoff. The GDR table is architecturally stale.
- **Options**: (A) Rename to "Governance Standards" with STD index schema per ADR-009. (B) Rename to "Decision Records" using ADR index per T102-STD-004. (C) Combined STD + ADR subsections.
- **Industry perspective**: ISO 29148 and BABOK v3 treat governance as standards conformance, not decision records. SAFe uses "guardrails" terminology.
- **Client direction**: Option A approved — STD schema.
- **Impact**: Request Section G table schema changes. ADR-002-CLAUSE-002 Section G entry updated. AC003-TK008 revised.

#### D2 — Section H Removal: Issues & Risks Removed from Request
- **Context**: LLM agents tend to log process-related issues (e.g., "Section X is empty") into Issues & Risks rather than specification-level risks. Current `T102-STD-007` has no content-type filtering mechanism.
- **Industry perspective**: ISO 29148 (SRS) does NOT include issue/risk registers. BABOK v3 manages risks at business analysis planning level. SAFe tracks risks at PI/ART level. Industry-standard spec documents do not embed issue/risk registers.
- **Research evidence**: `T102B-RES-001` (W5/W6) identified documentation weight. `T102B-RES-002` (Topic 4C) placed Issues/Risks at epic workspace level, not feature request level.
- **Options**: (A) Remove entirely — issues/risks at workspace/epic level. (B) Keep with restricted scope to spec-level risks only, requiring ADR-007 update.
- **Client direction**: Option A approved — remove entirely.
- **Impact**: Request Section H deleted. Existing T102B1-ISSUE-001/002 and T102B1-RISK-001 promoted to epic scope. ADR-002-CLAUSE-002 updated.

#### D3 — Unified RID Schema for Section F
- **Context**: Section F subsections used varying column schemas (Assumptions: `| ID | Assumption | Validation Method |`; Constraints: `| ID | Constraint | Rationale |`; FR: `| ID | Requirement | Addresses | Acceptance Check |`). No Reference column for traceability to governing CLAUSE specs.
- **Industry perspective**: ISO 29148 requires verification criteria per requirement. "Acceptance Check" renamed to "Verification" aligning with ISO 29148 terminology.
- **Decision**: Unified schema `| ID | Title | Description | Reference | Verification | Status | Note |` for CON/FR/NFR/IF. ASSUM keeps lifecycle schema per `T102-STD-005-CLAUSE-005A` with added Reference column.
- **Impact**: All Section F tables restructured. Reference column enables full traceability per `T102-STD-005-CLAUSE-004`.

#### D4 — INT Items Deferred to AC004
- **Context**: Request has zero `INT` items — no formal coordination with T102A or other features.
- **Decision**: Defer INT population to AC004 retrofit when template is available for reference.
- **Impact**: AC004 task register gains TK017 for INT items.

#### D5 — Feature Guidance & Notes Section
- **Context**: Client directed creation of a dedicated section for non-normative IID tokens (IG, INT, NOTE) rather than embedding under Feature Requirements (F).
- **Decision**: New `### H. Feature Guidance & Notes [O]` with `####` subheadings per token type (Implementation Guidance, Integration Guidance, Notes).
- **Impact**: ADR-002-CLAUSE-002 gains new section H. Previous Section H (Issues & Risks) removed; sections re-lettered.

#### D6 — Issues & Risks Research Elevated to T102-RES-004
- **Context**: The hosting architecture question (where should Issues & Risks live?) extends beyond T102B1 to the entire T102 governance model.
- **Client suggestion**: Investigate moving Issues & Risks from both SPS and Request to the Concept file.
- **Decision**: Elevate to `T102-RES-004` at initiative scope. Research topics: (1) Hosting options — SPS/Request/Concept/Workspace/Hybrid, (2) Content-type filtering rules, (3) Lifecycle management (RESOLVED/MITIGATED/DEFERRED/CANCELLED handling), (4) Scope-level tracking files vs SSOT embedding (GitHub Issues parallel), (5) ADR-007 spec update recommendations, (6) Cross-scope promotion rules.
- **Impact**: New `T102-PH001-ST004` research stream. AC004-TK018 absorbs findings when available.

#### D7 — Research Stream T102-PH001-ST004
- **Context**: `T102-RES-004` requires formal research commissioning per `T102-STD-006`.
- **Decision**: Register new `T102-PH001-ST004` in `plan_T102-PH001.md`. 4 activities: brief creation, client approval, report execution, report integration.
- **Impact**: Initiative plan amended. New stream plan file created.

#### D8 — Acceptance Criteria Relocation
- **Context**: `## IV. Acceptance Criteria` was a major section at same level as Executive Summary. Client argued it's a request-specific section that should be under Core Content.
- **Industry perspective**: BABOK v3 places acceptance criteria alongside requirements. SAFe embeds feature ACs within feature description.
- **Decision**: Move to `### K. Acceptance Criteria [M]` under Core Content. Amend ADR-002-CLAUSE-002 and CLAUSE-005.
- **Impact**: Major sections renumbered (Approval Gate IV→IV, Appendix V→V, new Changelog VI).

#### D9 — AC002.1 Subactivity
- **Context**: AC002 was already marked completed. Client wanted remediation without reopening.
- **Decision**: Create AC002.1 subactivity with 18 tasks. Blocks AC003.
- **Impact**: Stream plan amended with new activity block.

#### D10 — Proposal Authoring Rules for T102B2 Reuse
- **Context**: Proposal file serves as basis for developing T102B2. Need to capture authoring rules derived from decisions.
- **Decision**: Add Section VII to proposal with decision rationales and explicit authoring rules.
- **Impact**: Proposal file updated.

#### D11 — Deferred T102-RES-004 Absorption
- **Context**: Issues & Risks disposition cannot be finalized until T102-RES-004 completes.
- **Decision**: AC004-TK018 (deferred, blocked on ST004) absorbs report findings.
- **Impact**: AC004 task register updated with deferred task.

#### D12 — Canonical Section List A-K
- **Decision**: See Locked Decisions table above.

#### D13 — Major Section Restructure
- **Decision**: See Locked Decisions table above.

### B. Authoring Rules for T102B2 Reuse

Derived from D1-D13, these rules apply to all T102B Request-family artifacts:

1. **No `[M]`/`[O]` markers in authored requests**: Classification markers belong in the template only. Authored requests use plain section headings. (D4 deferred to AC004)
2. **Problem Statement format**: Use concise narrative paragraphs (3-5 sentences) with references to research artifacts. Avoid tabular extracts from research in Problem Statement. (Deferred to AC004)
3. **Non-normative content hosting**: IG, INT, and NOTE items are hosted in a dedicated "Feature Guidance & Notes" section (`### H.`) with `####` subheadings per IID token type. They do NOT belong in the Feature Requirements section (`### F.`) or scattered throughout other sections. (D5)
4. **Governance Standards section**: Uses STD index schema per `T102-STD-009-CLAUSE-004A`. Only populated when feature-level STDs are needed; otherwise contains placeholder row with dashes. (D1)
5. **Issues & Risks**: NOT hosted in Request artifacts (pending `T102-RES-004` resolution). Feature-level issues/risks promoted to epic scope per `T102-STD-007-CLAUSE-009`. (D2, D6)
6. **Acceptance Criteria**: Is a Core Content section (`### K.`), NOT a major `##` section. (D8)
7. **Changelog required**: Every Request artifact MUST include a `## VI. Changelog` section using the standard schema `| Version | Date | Type | Summary |`. (D13)
8. **RID table schema**: Feature Requirements subsections (CON/FR/NFR/IF) use unified schema: `| ID | Title | Description | Reference | Verification | Status | Note |`. ASSUM uses `T102-STD-005-CLAUSE-005A` lifecycle schema with added `Reference` column. (D3)
9. **NOTE formalization**: Non-normative references to companion documents use proper `T102-STD-005-CLAUSE-005E` NOTE format (e.g., `T102B1-NOTE-001`), not free-form paragraphs.
10. **Section F Reference column**: All RID tables include a `Reference` column with full formal references per `T102-STD-005-CLAUSE-004` linking to governing CLAUSE/RID specs. (D3)
