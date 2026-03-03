---
artifact_type: 'ANALYSIS'
analysis_type: 'pattern_audit'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST005'
activity_id: 'T104-PH001-ST005-AC008'
task_id: 'T104-PH001-ST005-AC008-TK001'
version: '1.1.0'
date: '2026-03-02'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
---

# ANALYSIS: Proposal Pattern Audit (T104-PH001-ST005-AC008-TK001)

## I. PURPOSE & SCOPE

**Purpose**: Audit existing proposal exemplars across Program (`P`) and Initiative (`T104`) workspaces, extract structural patterns, benchmark the current `template_workspace_proposal.md` against evolved usage, identify gaps/risks, and produce the decision inputs needed to author `guideline_workspace_proposal.md` (AC008-TK002) and update/replace proposal templates (AC008-TK003) deterministically.

**Scope**:
- **In scope**:
  - Proposal artifacts under `prompt/artifacts/tasks/P/` and `prompt/artifacts/tasks/T104/` (focus: gate disposition packages, promotion contracts, and standards-input proposals).
  - `prompt/templates/consultant/workspace/template_workspace_proposal.md` (existing template).
  - Naming/placement and ID authorities: `P-STD-004` and `P-STD-005`.
  - Planning context and precedent: AC007 (analysis pattern audit + GATE-000 decision disposition package pattern).
- **Out of scope**:
  - Authoring `guideline_workspace_proposal.md` (AC008-TK002 execution).
  - Editing/creating proposal templates (AC008-TK003 execution).
  - Formal Draft 2 alignment removals (AC008-TK901).
  - Any “external review” companion analysis for this activity (explicitly excluded from AC008 scope by Client instruction on 2026-03-01).

**Inputs reviewed**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (standards-input proposal; P-STD-004 seeding)
- `prompt/artifacts/tasks/T104/workspace/PH001/ST005/proposal/proposal_T104-PH001-ST005-AC007-TK001.1_gir-disposition-package.md` (gate disposition package pattern)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md` (gate disposition package pattern)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/proposal/proposal_P-PH000-ST001-AC002_promotion-contract-t102-std-004-to-p-std-001.md` (promotion contract pattern)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/proposal/proposal_P-PH000-ST001-AC006_promotion-contract-t102-std-005-to-p-std-005.md` (promotion contract pattern)
- `prompt/templates/consultant/workspace/template_workspace_proposal.md` (existing template baseline)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (naming/placement authority)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` (ID authority)

---

## II. EXEMPLAR INVENTORY

| # | Exemplar | Proposal archetype | Authoring posture | Key structural sections (high level) |
|:--|:--|:--|:--|:--|
| 1 | `T104-ST002-AC000_directory-naming-convention` | Standards-input proposal | Evidence + conventions + DR list | Purpose, Analysis (current state + patterns), Conventions (normative rules), Risks/DR register, Changelog |
| 2 | `T104-ST005-AC007_gir-disposition-package` | Gate disposition package | Decision register + GDR | Executive Summary, Disposition Summary, Detailed DEC register, Gate Decision Record (embedded), Changelog |
| 3 | `P-ST001-AC004_gir-disposition-package` | Gate disposition package | GIR register + client dispositions | Executive Summary, Disposition Summary, Detailed GIR register, Implementation notes, Changelog |
| 4 | `P-AC002_promotion-contract` | Promotion contract | Mechanical instructions | Purpose, Gap analysis, Re-ID mapping, Replacement rules, Exact new content, Index updates |
| 5 | `P-AC006_promotion-contract` | Promotion contract | Mechanical instructions + tiered reference plan | Purpose, Audit findings, Mapping, Replacement rules, Variances, Exact clause/ADR bodies |

**Observation**: These archetypes are structurally incompatible with the current template’s “E-ID workspace” orientation (Candidate Inventory → full bodies). Attempting to force them into one shape increases drift risk and reduces decision completeness.

---

## III. EXISTING TEMPLATE ASSESSMENT (`template_workspace_proposal.md`)

The current `prompt/templates/consultant/workspace/template_workspace_proposal.md` is optimized for:
- **E-ID development workspace** (Candidate Inventory “working index” + full bodies),
- **Epic-scoped** proposal framing (`epic_id`, `epic_code`, `target_document`, `target_section`),
- **T102-era governance references** (legacy `T102-STD-*` labels).

Key mismatches vs evolved usage:
1. **Archetype mismatch**: Gate disposition packages and promotion contracts do not have “Candidate Inventory + bodies” semantics.
2. **Scope mismatch**: Modern proposals are commonly **timeline UID scoped** (stream/activity), not epic scoped.
3. **Authority drift**: Program authority is now `P-STD-004` / `P-STD-005` (and `P-STD-001` for combined standard governance), which the template does not reflect.
4. **Gate semantics**: Some proposals embed a Gate Decision Record for decision gates (as in AC007); the template does not include this pattern.

---

## IV. PATTERN EXTRACTION

### A. Convergent patterns (stable across archetypes)

1. **Executive summary first**: Clear statement of what decision/outcome this proposal enables.
2. **Deterministic downstream**: When proposals are used to unblock implementation, they provide decision-complete instructions (not “ideas”).
3. **Decision/disposition register**: Gate-oriented proposals include structured decision items with explicit client disposition capture.
4. **Explicit authority references**: Proposals cite the governing plan and relevant standards/authorities for naming, IDs, and governance.
5. **Changelog discipline**: All mature exemplars include version/date/type/summary.

### B. Divergent patterns (archetype-specific)

| Archetype | Defining trait | Consequence for templating |
|:--|:--|:--|
| E-ID workspace | Candidate Inventory as master index | Needs inventory + full-body sections; not applicable to promotion contracts |
| Gate disposition package | Decision items + client checkboxing + GDR | Needs DEC/GIR register + embedded GDR + enforcement language |
| Promotion contract | Mechanical instructions + mapping tables | Needs deterministic mapping/replacement rules and exact text blocks |
| Standards-input proposal | Hybrid analysis + conventions + DR list | Needs conventions section, DR list, and risk register |

**Implication**: A multi-template posture is justified (and already chosen by the Client for AC008 planning).

---

## V. GAPS / RISKS REGISTER (AC008-TK001 OUTPUT)

| GAP ID | Category | Title | Description | Downstream target | Notes |
|:--|:--|:--|:--|:--|:--|
| GAP-001 | templates | Single-template assumption is invalid | Proposal archetypes require materially different structures; forcing one template increases drift and reduces clarity. | TK002 + TK003 | Client planning decision: adopt multiple templates. |
| GAP-002 | frontmatter | Frontmatter key set not standardized across archetypes | Some proposals are timeline-scoped; others are standard-scoped; template currently assumes epic-scoped keys. | TK002 + TK003 | Need baseline keys + allowed optional keys per template. |
| GAP-003 | gating | Gate decision recording is inconsistent | AC007 embeds a GDR in the proposal (decision gate). Verification guideline expects GDR in verification artifacts (gate reviews). Need explicit rule for proposal-gates vs verification-gates. | TK002 | AC008 will define “decision gate” semantics for GATE-000. |
| GAP-004 | naming_placement | Template and plan usage diverge on placement rules | `P-STD-004-CLAUSE-003F` requires scope-aligned placement for `proposal_`/`analysis_` (stream vs activity). Existing artifacts are mixed. | TK002 + TK004 | AC008 deliverables will be activity-scoped and placed under `AC008/`. |
| GAP-005 | governance | Legacy standard references risk confusion | Template cites `T102-STD-004` / `T102-STD-005`. Authority has promoted to `P-STD-001` / `P-STD-005`. | TK002 + TK004 | Use P-STD-* as primary; allow legacy aliases informatively. |
| GAP-006 | consistency | Proposal→SSOT promotion workflow is under-specified | Some proposals function as “promotion contracts”; others are “workspace deliberation”. Guideline must define lifecycle + promotion triggers. | TK002 | Include explicit lifecycle per archetype. |
| GAP-007 | crosschecks | Cross-check target set not enumerated | AC008-TK004 currently references legacy standards; must update to P-STD authorities and include P-STD-004 placement rules. | TK004 | Add concrete check list. |
| GAP-008 | governance | DEC token collision | `DEC` token collision with P-STD-005-CLAUSE-008J session items; resolved by adopting `GIR-###`. | TK001.1 | disposition: resolved |

---

## VI. GIR DISPOSITION REGISTER (PENDING AC008-TK001.1 / GATE-000)

The following decisions will be dispositioned in the GATE-000 proposal package produced by AC008-TK001.1.

| GIR ID | Decision area | Options | Recommendation (preliminary) | Gap(s) |
|:--|:--|:--|:--|:--|
| GIR-001 | Proposal archetype taxonomy | (a) 4 archetypes (E-ID workspace, gate disposition, promotion contract, standards-input); (b) broader buckets; (c) open-ended | (a) 4 archetypes for Draft 1 | GAP-001 |
| GIR-002 | Template posture | (a) Single template + `proposal_type`; (b) multiple templates | (b) Multiple templates (Client-selected) | GAP-001 |
| GIR-003 | Required frontmatter baseline | (a) common keys + optional per-template keys; (b) template-specific only | (a) Common baseline + per-template optional set | GAP-002 |
| GIR-004 | Decision gate vs verification gate semantics | (a) allow decision-gate proposals with embedded GDR; (b) force verification artifact for all gates | (a) Allow decision-gate proposals for GATE-000 when gate is “decision disposition” (not a quality gate) | GAP-003 |
| GIR-005 | Standards authority references | (a) cite P-STD-* primaries; (b) cite T102-STD-* only; (c) dual cite everywhere | (a) P-STD-* primary, with informative legacy alias notes only where needed | GAP-005 |
| GIR-006 | Template set naming | (a) `template_workspace_proposal_<type>.md` naming; (b) another scheme | (a) `template_workspace_proposal_<kebab-type>.md` | GAP-001 |
| GIR-007 | Cross-check target set for TK004 | (a) P-STD-004 + P-STD-005 + P-STD-001; (b) legacy T102 standards; (c) minimal checks | (a) P-STD authorities plus relevant workspace guidelines | GAP-007 |

---

## VII. CROSS-CHECK TARGETS (FOR AC008-TK004 UPDATE)

After TK002/TK003 delivery, AC008-TK004 should verify consistency against:
1. `standard_P-STD-004_file-naming-and-directory-convention.md` (proposal naming and placement)
2. `standard_P-STD-005_universal-id-specification.md` (ID patterns used in proposals)
3. `standard_P-STD-001_program-governance-standard.md` (Decision Record governance references, where applicable)
4. `guideline_workspace_plan.md` (gate dependency enforcement language)
5. `workspace_documentation_rules.md` (template/guideline inventories after delivery)

---

## VIII. REFERENCES

| Document | Path |
|:--|:--|
| ST005 Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| Existing Proposal Template | `prompt/templates/consultant/workspace/template_workspace_proposal.md` |
| P-STD-004 | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| P-STD-005 | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| AC007 GATE-000 Disposition Package | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/proposal/proposal_T104-PH001-ST005-AC007-TK001.1_gir-disposition-package.md` |
| P GATE-002 Disposition Package | `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC004-TK002.2_gir-disposition-package.md` |
| Promotion Contract (P-STD-001) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/proposal/proposal_P-PH000-ST001-AC002_promotion-contract-t102-std-004-to-p-std-001.md` |
| Promotion Contract (P-STD-005) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/proposal/proposal_P-PH000-ST001-AC006_promotion-contract-t102-std-005-to-p-std-005.md` |
| Standards-input Proposal (P-STD-004 seed) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` |

---

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| 1.1.0 | 2026-03-02 | Update | Renamed DEC register to GIR register per QA session GIR token adoption decision; added GAP-008 (DEC token collision). |
| 1.0.0 | 2026-03-01 | Initial | Draft 1 pattern audit of proposal exemplars vs existing proposal template. Identified archetype divergence, gaps/risks, and decision set required to author `guideline_workspace_proposal.md` and multi-template inventory deterministically. |

