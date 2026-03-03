---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST005'
activity_id: 'T104-PH001-ST005-AC008'
task_id: 'T104-PH001-ST005-AC008-TK001.1'
gate_id: 'T104-PH001-ST005-AC008-GATE-000'
version: '1.2.0'
date: '2026-03-03'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC008/analysis/analysis_T104-PH001-ST005-AC008-TK001_proposal-pattern-audit.md'
purpose: 'GATE-000 decision disposition package — recommended resolutions + rationale for all proposal-pattern-audit decisions (DEC001+), to enable Client acceptance and unblock TK002–TK004.'
consumers:
  - 'T104-PH001-ST005-AC008-GATE-000'
  - 'T104-PH001-ST005-AC008-TK002'
  - 'T104-PH001-ST005-AC008-TK003'
  - 'T104-PH001-ST005-AC008-TK004'
---

# PROPOSAL: GATE-000 Decision Disposition Package — T104-PH001-ST005-AC008

> **Purpose**: Provide a decision-ready disposition package for all design decisions raised by `T104-PH001-ST005-AC008-TK001` (“Proposal Pattern Audit”). Each decision (DEC###) includes clear options, a consultant recommendation (pre-selected), and a Client decision control. The finalized decisions in this proposal are the binding inputs for `T104-PH001-ST005-AC008-GATE-000` and for downstream execution in `TK002–TK004`.

---

## I. EXECUTIVE SUMMARY

**Context**: `analysis_T104-PH001-ST005-AC008-TK001_proposal-pattern-audit.md` identified structural divergence across proposal archetypes and multiple gaps/risks in the current `template_workspace_proposal.md` (which is E-ID workspace oriented and legacy-standard referenced).

**Goal at GATE-000**: The Client confirms or overrides each recommended design decision below. Once the Gate Decision Record (§VI) is set to `Client Decision = APPROVE` or `APPROVE WITH CONDITIONS`, downstream tasks `TK002–TK004` may proceed deterministically.

**Key planning constraint (already selected by Client)**: Proposal templating will follow a **multiple-template** posture (not a single template with conditional sections).

**Recommendation pre-selection**: For review speed, the consultant recommendation is **pre-checked** for each decision. This does not constitute approval; the authoritative approval signal is recorded in the Gate Decision Record (§VI).

---

## II. DISPOSITION SUMMARY (GIR-001…GIR-014)

| GIR ID | Gap(s) | Decision Area | Recommended Option | Execution Target | Blocking for TK002/TK003? | Client Decision |
|:--|:--|:--|:--|:--|:--|:--|
| GIR-001 | GAP-001 | Proposal archetype taxonomy (Draft 1) | (a) 4 archetypes | TK002 | Yes | (a) |
| GIR-002 | GAP-001 | Template posture | (b) Multiple templates | TK002 + TK003 | Yes | (b) |
| GIR-003 | GAP-002 | Frontmatter baseline | (a) Common keys + optional per-template keys | TK002 + TK003 | Yes | (a) |
| GIR-004 | GAP-003 | Decision gate semantics | (a) Allow proposal-embedded GDR for decision gates | TK002 | Yes | (a) |
| GIR-005 | GAP-005 | Authority references | (a) P-STD-* primary; legacy aliases informative only | TK002 + TK004 | Yes | (a) |
| GIR-006 | GAP-006 | Proposal lifecycle (Draft 1) | (a) Define lifecycle per archetype | TK002 | Yes | (a) |
| GIR-007 | GAP-001 | Template inventory set + naming | (a) Create one template per archetype | TK003 | Yes | (a) |
| GIR-008 | GAP-007 | TK004 cross-check targets | (a) Cross-check vs P-STD-004 + P-STD-005 + P-STD-001 + workspace guidelines | TK004 | No | (a) |
| GIR-009 | GAP-004 | Placement rule enforcement | (a) Enforce P-STD-004 scope-aligned placement in guideline | TK002 + TK004 | Yes | (a) |
| GIR-010 | GAP-001 | Legacy Template Disposition | (a) Deprecation notice + archive per P-STD-004 | TK003 | Yes | (a) |
| GIR-011 | N/A | Gate Review Package Formalization | (a) Formalize in TK002 with required sections | TK002 | Yes | (a) |
| GIR-012 | N/A | GIR Token Adoption | (a) Adopt `GIR-###` as standard | TK002 + analysis guideline | Yes | (a) |
| GIR-013 | GAP-004 | TK004 Cross-Check Target Augmentation | (a) Add `guideline_workspace_analysis.md` | TK004 | No | (a) |
| GIR-014 | N/A | Cross-Artifact Linkage in AC004 | (a) Expand AC004 scope | AC004 | No | (a) |

**Notes**:
- “Blocking” items MUST be resolved (Client confirms or overrides) before `TK002–TK004` proceed.
- GIR-002 is pre-selected per Client instruction: multiple templates are in scope for this activity.

---

## III. DESIGN DECISION REGISTER (DETAILED)

### GIR-001 — Proposal Archetype Taxonomy (Draft 1)

**Context**: Proposal exemplars used in current work fall into distinct structural archetypes: (1) E-ID development workspace, (2) gate decision disposition package, (3) promotion contract, (4) standards-input proposal.

**Decision prompt**: What is the canonical proposal archetype taxonomy for Draft 1?

| Option | Description |
|:--|:--|
| **(a) Adopt 4 archetypes (Recommended)** | `eid_workspace`, `gate_disposition`, `promotion_contract`, `standards_input` |
| (b) Broader buckets | Collapse into fewer types (e.g., `workspace` vs `contract`) |
| (c) Open-ended | No formal taxonomy; rely on free-form prose |

**Recommendation**: (a)

**Rationale**: Matches observed usage and enables deterministic template inventory and guideline structure.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-002 — Template Posture

**Context**: A single proposal template cannot represent all archetypes without heavy conditionality and loss of clarity.

**Decision prompt**: What templating posture governs AC008 deliverables?

| Option | Description |
|:--|:--|
| (a) Single template + conditional blocks | One `template_workspace_proposal.md` with type markers/conditional sections |
| **(b) Multiple templates (Recommended)** | One template per archetype; guideline inventory enumerates them |

**Recommendation**: (b)

**Rationale**: Prevents structural drift and aligns with evolved proposal usage patterns.

**Client Decision**: `[ ] (a)` / `[x] (b)` / `[ ] Override: _______________`

---

### GIR-003 — Frontmatter Baseline Policy

**Context**: Proposal artifacts are used at multiple scopes (stream/activity, program initiative, standards promotions). Current template assumes epic-scope keys.

**Decision prompt**: How should the guideline define proposal frontmatter requirements?

| Option | Description |
|:--|:--|
| **(a) Common baseline + optional keys per template (Recommended)** | Define required baseline keys common to all proposals; define optional keys per archetype/template. |
| (b) Template-specific only | Each template defines its own keys; no common baseline. |

**Recommendation**: (a)

**Rationale**: Maintains consistent traceability across proposal artifacts while preserving archetype-specific needs.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

### GIR-004 — Decision Gate Semantics (Proposal-Embedded GDR)

**Context**: Some gates are “quality verification” gates (best expressed as VERIFICATION artifacts) while others are “decision disposition” gates used to lock scope/decisions before implementation.

**Decision prompt**: For decision-only gates (like this GATE-000), where is the Client approval signal recorded?

| Option | Description |
|:--|:--|
| **(a) Proposal-embedded GDR for decision gates (Recommended)** | The disposition proposal contains `## Gate Decision Record` and is the authoritative client decision signal for GATE-000. |
| (b) Always require VERIFICATION | All gates must have a `verification_...gate-###.md` primary artifact with the GDR. |

**Recommendation**: (a)

**Rationale**: Keeps decision gates lightweight while still enforcing a single authoritative approval signal.

**Implementation note**: TK002 MUST define the “decision gate” vs “verification gate” distinction explicitly to avoid misuse.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

### GIR-005 — Authority References (P-STD-* Primary)

**Context**: Template and older artifacts reference legacy `T102-STD-*` identifiers. Program authorities now exist at `P-STD-001` (combined governance), `P-STD-004` (naming/placement), `P-STD-005` (IDs).

**Decision prompt**: What authority reference posture should the proposal guideline adopt?

| Option | Description |
|:--|:--|
| **(a) Cite P-STD-* as primary (Recommended)** | Use P-STD-* references as the canonical authority; allow legacy references as informative aliases only when necessary. |
| (b) Cite legacy only | Keep T102-STD-* as primary references in proposal guidance. |
| (c) Dual cite everywhere | Always cite both legacy and promoted IDs. |

**Recommendation**: (a)

**Rationale**: Prevents governance-scope confusion and matches current program standardization direction.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-006 — Proposal Lifecycle Definition (Draft 1)

**Context**: Proposal artifacts have different lifecycle semantics depending on archetype (e.g., promotion contract is deterministic; E-ID workspace proposals evolve over dialogue).

**Decision prompt**: Should the proposal guideline define lifecycle rules per archetype?

| Option | Description |
|:--|:--|
| **(a) Yes — define lifecycle per archetype (Recommended)** | Document creation triggers, in-progress editing posture, approval step, and SSOT promotion/archival rules per archetype. |
| (b) No — generic lifecycle only | Provide a single lifecycle narrative for all proposals. |

**Recommendation**: (a)

**Rationale**: Avoids misapplying E-ID “working index” workflow to promotion contracts and gate packages.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

### GIR-007 — Template Inventory Set + Naming

**Context**: Multiple templates require a deterministic inventory and naming scheme.

**Decision prompt**: What template set should TK003 produce and how should it be named?

| Option | Description |
|:--|:--|
| **(a) One template per archetype (Recommended)** | Create: `template_workspace_proposal_eid-workspace.md`, `template_workspace_proposal_gate-disposition.md`, `template_workspace_proposal_promotion-contract.md`, `template_workspace_proposal_standards-input.md`. |
| (b) Partial template set | Template only highest-frequency archetypes; keep others as guideline-only patterns. |

**Recommendation**: (a)

**Rationale**: Ensures template inventory completeness and reduces reliance on prose-only guidance.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

### GIR-008 — TK004 Cross-Check Target Set

**Context**: AC008-TK004 must prevent contradictions between proposal authoring rules and program authorities.

**Decision prompt**: What are the mandatory cross-check targets for TK004?

| Option | Description |
|:--|:--|
| **(a) P-STD authorities + workspace guidelines (Recommended)** | Cross-check vs: `P-STD-004`, `P-STD-005`, `P-STD-001`, `guideline_workspace_plan.md`, and `workspace_documentation_rules.md`. |
| (b) Legacy-only | Cross-check only vs legacy `T102-STD-004` / `T102-STD-005`. |
| (c) Minimal | Only check naming conventions; skip DR/ID governance. |

**Recommendation**: (a)

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-009 — Placement Rule Enforcement (P-STD-004)

**Context**: Proposal naming/placement must be consistent with P-STD-004 scope-aligned placement rules.

**Decision prompt**: Should the proposal guideline hard-require P-STD-004 scope-aligned placement for proposals?

| Option | Description |
|:--|:--|
| **(a) Yes — enforce scope-aligned placement (Recommended)** | Require `proposal_<scope-UID>_<kebab-topic>.md` placement to match whether `<scope-UID>` contains `AC###` per `P-STD-004-CLAUSE-003F`. |
| (b) Informative only | Mention placement guidance but allow drift for convenience. |

**Recommendation**: (a)

**Rationale**: Prevents placement drift and ensures compliance with naming authorities.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

### GIR-010 — Legacy Template Disposition

**Context**: Ensuring no usage drift occurs by properly handling the legacy `template_workspace_proposal.md`.

**Decision prompt**: What is the disposition for the legacy proposal template?

| Option | Description |
|:--|:--|
| **(a) Deprecation notice + archive per P-STD-004 (Recommended)** | Add a clear deprecation notice pointing to the new multi-template set and move to archive. |
| (b) Retain as-is | Keep the legacy template in the active inventory. |

**Recommendation**: (a)

**Rationale**: Aligns with AC003 precedent and prevents accidental usage of superseded patterns.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

### GIR-011 — Gate Review Package Formalization

**Context**: The `gate_disposition` archetype needs formal structural requirements to ensure consistency across gates.

**Decision prompt**: How should the `gate_disposition` archetype be formalized?

| Option | Description |
|:--|:--|
| **(a) Formalize in TK002 with required sections (Recommended)** | codify required sections: evidence index, disposition register, recommendation, and GDR. |
| (b) Keep informal | Allow free-form structure for gate disposition packages. |

**Recommendation**: (a)

**Rationale**: ensures quality and completeness of gate-ready packages.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

### GIR-012 — GIR Token Adoption

**Context**: P-STD-005-CLAUSE-008J session items use `DEC-###`. Using the same for analysis→proposal disposition items causes ID collision.

**Decision prompt**: What universal register token should be adopted for disposition items?

| Option | Description |
|:--|:--|
| **(a) Adopt `GIR-###` (Recommended)** | Adopt `GIR-###` (Gate Item/Itemized Resolution), matching P-AC004 precedent. |
| (b) Keep `DEC-###` | Continue using `DEC-###` despite collision risk. |
| (c) Use `DDR-###` | Use a new prefix (Design Decision Record). |

**Recommendation**: (a)

**Rationale**: Resolves token collision and remains consistent with evolved program-level practice.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-013 — TK004 Cross-Check Target Augmentation

**Context**: The analysis guideline provides handoff semantics that the proposal guideline should be consistent with.

**Decision prompt**: Should `guideline_workspace_analysis.md` be added to TK004 cross-check targets?

| Option | Description |
|:--|:--|
| **(a) Add (Recommended)** | Include the analysis guideline in the consistency check set. |
| (b) Defer to Draft 2 | Keep cross-check targets limited for Draft 1. |

**Recommendation**: (a)

**Rationale**: Prevents analysis→proposal handoff drift.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

### GIR-014 — Cross-Artifact Linkage in AC004

**Context**: Workflow consistency between roles requires clear field-level consistency contracts.

**Decision prompt**: Should AC004 scope be expanded to include cross-artifact linkage?

| Option | Description |
|:--|:--|
| **(a) Expand AC004 scope (Recommended)** | Include a section in `workspace_documentation_rules.md` defining the consultant workflow chain. |
| (b) New activity/stream | Defer to a separate planning activity. |

**Recommendation**: (a)

**Rationale**: Provides a central authority for artifact linkage rules.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

## IV. GATE ENFORCEMENT

`T104-PH001-ST005-AC008-TK002`, `TK003`, and `TK004` MUST NOT start until the Gate Decision Record (§VI) for GIR-001–GIR-014 is updated to:
- `Client Decision = APPROVE` or `APPROVE WITH CONDITIONS`
- `Decision Date` populated
- Any conditions enumerated (if applicable)

---

## V. REFERENCES

| Document | Path |
|:--|:--|
| ST005 Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md` |
| AC008 Pattern Audit Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC008/analysis/analysis_T104-PH001-ST005-AC008-TK001_proposal-pattern-audit.md` |
| Existing Proposal Template | `prompt/templates/consultant/workspace/template_workspace_proposal.md` |
| P-STD-004 | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| P-STD-005 | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| P-STD-001 | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |

---

## VI. GATE DECISION RECORD (GDR)

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `T104-PH001-ST005-AC008-GATE-000` |
| Reviewer Verdict | `PASS` |
| Client Decision | `APPROVE` |
| Conditions (if any) | — |
| Decided By | Client |
| Decision Date | `2026-03-03` |
| Decision Reference | Client approval signal in current session (`2026-03-03`). |

---

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.2.0 | 2026-03-03 | Update | Closed GATE-000 GDR with `Client Decision = APPROVE` and Decision Date. Updated GDR schema to align with verification guideline format; corrected GIR-007 template naming text. |
| v1.1.0 | 2026-03-02 | Update | Added GIR-010–GIR-014 from QA session (2026-03-02): legacy template disposition, gate review package formalization, GIR token adoption, TK004 cross-check augmentation, cross-artifact linkage in AC004. |
| v1.0.0 | 2026-03-01 | Initial | GATE-000 decision disposition package for AC008 proposal pattern audit decisions (GIR-001–GIR-009). Establishes multiple-template posture, authority reference policy, and gate enforcement rules to unblock TK002–TK004. |
