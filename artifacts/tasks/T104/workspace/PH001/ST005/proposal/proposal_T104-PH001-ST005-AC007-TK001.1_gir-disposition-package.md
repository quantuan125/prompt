---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST005'
activity_id: 'T104-PH001-ST005-AC007'
task_id: 'T104-PH001-ST005-AC007-TK001.1'
gate_id: 'T104-PH001-ST005-AC007-GATE-000'
version: '1.1.1'
date: '2026-03-01'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/analysis/analysis_T104-PH001-ST005-AC007_analysis-pattern-audit.md'
external_review_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC007/analysis/analysis_T104-PH001-ST005-AC007-GATE-000_external-review-disposition.md'
purpose: 'GATE-000 decision disposition package — recommended resolutions + rationale for all TK001.1 design decisions (DEC001+), to enable Client acceptance and unblock TK002–TK004.'
consumers:
  - 'T104-PH001-ST005-AC007-GATE-000'
  - 'T104-PH001-ST005-AC007-TK002'
  - 'T104-PH001-ST005-AC007-TK003'
  - 'T104-PH001-ST005-AC007-TK004'
---

# PROPOSAL: GATE-000 Decision Disposition Package — T104-PH001-ST005-AC007

> **Purpose**: Provide a decision-ready disposition package for the design decisions raised by `T104-PH001-ST005-AC007-TK001` (“Analysis Pattern Audit”). Each decision (DEC###) includes clear options, a consultant recommendation (pre-selected), and a Client decision control. The finalized decisions in this proposal are the binding inputs for `T104-PH001-ST005-AC007-GATE-000` and for downstream execution in `TK002–TK004`.

---

## I. EXECUTIVE SUMMARY

**Context**: `analysis_T104-PH001-ST005-AC007_analysis-pattern-audit.md` identified 10 gaps (GAP-001…GAP-010), with GAP-002 already resolved (“LLM_Consultant is ALWAYS the author of analysis artifacts”). The remaining gaps require explicit design decisions (DEC001+) before authoring `guideline_workspace_analysis.md` (TK002) and updating `template_workspace_analysis.md` (TK003).

**Goal at GATE-000**: The Client confirms or overrides each recommended design decision below. Once the Gate Decision Record (§V) is set to `Client Decision = APPROVE` or `APPROVE WITH CONDITIONS`, downstream tasks `TK002–TK004` may proceed deterministically.

**External review evidence**: An independent external review of this disposition package concluded **APPROVE** (no overrides required) and raised four implementation-level flags for downstream execution. These are dispositioned here as additional decisions (DEC010–DEC013) to ensure GATE-000 closes with full awareness and deterministic downstream scope. (Reference: `analysis_T104-PH001-ST005-AC007-GATE-000_external-review-disposition.md`.)

**Recommendation pre-selection**: For review speed, the consultant recommendation is **pre-checked** for each decision. This does not constitute approval; the authoritative approval signal is recorded in the Gate Decision Record (§V).

---

## II. DISPOSITION SUMMARY (DEC001…DEC013)

| DEC ID | Gap(s) | Decision Area | Recommended Option | Execution Target | Blocking for TK002/TK003? | Client Decision |
|:--|:--|:--|:--|:--|:--|:--|
| DEC001 | GAP-001, GAP-004 | Analysis type taxonomy + `analysis_type` enum | (a) Include `pattern_audit` + 4 core types | TK002 + TK003 | Yes | (a) |
| DEC002 | GAP-003 | Template approach | (a) Single template with conditional sections | TK002 + TK003 | Yes | (a) |
| DEC003 | GAP-004 | Frontmatter key policy | (a) Common keys + optional type-specific keys | TK002 + TK003 | Yes | (a) |
| DEC004 | GAP-005 | Conditional marker convention | (a) HTML comment markers | TK003 | Yes | (a) |
| DEC005 | GAP-006 | Evidence section placement | (a) Universal near top | TK002 + TK003 | Yes | (a) |
| DEC006 | GAP-008 | Findings/gap register schema | (b) Lightweight GAP-style (non-gate-blocking) | TK002 + TK003 | Yes | (b) |
| DEC007 | GAP-009 | Integration Roadmap handling | (a) Research-synthesis-only with marker | TK002 + TK003 | Yes | (a) |
| DEC008 | GAP-010 | Linking chain scoping | (a) Scope T104-IG-002 to research synthesis only | TK002 | Yes | (a) |
| DEC009 | GAP-007 | Scope & Inputs placement | (a) Universal `Scope & Inputs` section near top | TK002 + TK003 | Yes | (a) |
| DEC010 | ER-GAP-003 | TK004 cross-check targets | (a) Add proposal template cross-check | TK004 | No | (a) |
| DEC011 | ER-GAP-001 | Per-type lifecycle positions | (a) Define lifecycle positions for all 5 types (Draft 1 preliminary) | TK002 | Yes | (a) |
| DEC012 | ER-GAP-002 | GAP register `Disposition` enum | (a) Enumerate bounded values (recommended set) | TK002 + TK003 | Yes | (a) |
| DEC013 | ER-GAP-004 | Generic “Downstream Actions” section | (a) Define required fields + per-type guidance | TK002 + TK003 | Yes | (a) |

**Notes**:
- GAP-002 (role boundary) is already resolved and is not included as a decision item in this proposal.
- All “Blocking” items MUST be resolved (Client confirms or overrides) before `TK002–TK004` proceed.
- `ER-GAP-###` items originate from the independent external review. They are renamed here (with an `ER-` prefix) to avoid collision with TK001’s GAP-001…GAP-010 numbering.

---

## III. DESIGN DECISION REGISTER (DETAILED)

### DEC001 — Analysis Type Taxonomy + `analysis_type` Enum (GAP-001, GAP-004)

**Context**: Exemplars reflect multiple analysis shapes (research synthesis, compliance audit, assessment/hardening, external review). Existing ST005 analysis artifacts already use `analysis_type: 'pattern_audit'` for pattern audit analyses, creating an immediate enum/taxonomy decision requirement.

**Decision prompt**: What is the canonical analysis type taxonomy for Draft 1, and what is the allowed `analysis_type` enum in frontmatter?

| Option | Description |
|:--|:--|
| **(a) Adopt 5-type enum (Recommended)** | `pattern_audit`, `research_synthesis`, `compliance_audit`, `assessment`, `external_review`. `analysis_type` is REQUIRED for all analysis artifacts. |
| (b) Adopt 4-type enum only | `research_synthesis`, `compliance_audit`, `assessment`, `external_review`. Pattern audits must be reclassified under one of these types and avoid `pattern_audit`. |
| (c) Open-ended string | `analysis_type` is required but may be any kebab-case value; guideline defines constraints and requires justification. |

**Recommendation**: (a)

**Rationale**: Avoids invalidating already-authored ST005 pattern audits and provides a bounded taxonomy that still covers observed exemplar diversity.

**Implementation note**:
- `TK002` registers the enum and describes lifecycle/section requirements per type.
- `TK003` adds `analysis_type` to `template_workspace_analysis.md` and introduces conditional markers tied to type where applicable.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC002 — Template Approach (GAP-003)

**Context**: The current `template_workspace_analysis.md` is research-synthesis oriented; other analysis types use different structures. A single template can still work if conditional sections are clearly marked and guideline rules define what to include per type.

**Decision prompt**: Should Draft 1 use a single analysis template with conditional sections, or multiple type-specific templates?

| Option | Description |
|:--|:--|
| **(a) Single template with conditional sections (Recommended)** | Keep one `template_workspace_analysis.md`, mark type-specific sections as conditional, and codify inclusion rules per `analysis_type` in the guideline. |
| (b) Multiple templates | Create one template per analysis type (e.g., `template_workspace_analysis_assessment.md`, etc.). |
| (c) Hybrid | Single base template + optional add-on appendices per type. |

**Recommendation**: (a)

**Rationale**: Minimizes template sprawl while still supporting multiple analysis shapes via explicit conditionality and guideline rules.

**Implementation note**:
- `TK002` defines required sections per type.
- `TK003` updates the existing template to be type-aware (conditional markers + registers).

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC003 — Frontmatter Key Policy (GAP-004)

**Context**: Existing template frontmatter is research-synthesis specific (`research_id`, `research_brief`, `research_report`, `target_proposal`). Exemplars use other keys (e.g., `target_standard`, `source_plan`). A stable Draft 1 posture is: (1) a common baseline key set for all analysis artifacts; (2) optional, type-specific keys registered in the guideline.

**Decision prompt**: What is the canonical frontmatter policy for analysis artifacts?

| Option | Description |
|:--|:--|
| **(a) Common keys + optional type-specific keys (Recommended)** | Require a common baseline (incl. `analysis_type`), and register optional keys per `analysis_type` (including: `target_standard`, `target_artifact`, `source_plan`, `reference_standard`). |
| (b) Type-specific key sets only | Define a separate full key set per type; template branches heavily by type. |
| (c) Minimal keys | Only require `artifact_type`, initiative identifiers, and `analysis_type`; all other keys are discouraged. |

**Recommendation**: (a)

**Rationale**: Prevents frontmatter drift while keeping the template usable across multiple types without forcing irrelevant keys.

**Implementation note**:
- `TK002` defines baseline + optional keys and when each applies.
- `TK003` updates frontmatter accordingly (remove/relegate research-only keys; add optional placeholders).

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC004 — Conditional Marker Convention (GAP-005)

**Context**: Research-synthesis-only sections (notably E-ID candidate mapping and integration roadmap content) must be clearly excluded for other analysis types.

**Decision prompt**: How should the template mark sections that are only applicable to a subset of analysis types?

| Option | Description |
|:--|:--|
| **(a) Use HTML comments in-template (Recommended)** | Example: `<!-- RESEARCH SYNTHESIS ONLY — omit for other analysis types -->` placed at section headers. |
| (b) Guideline-only rule | No markers in template; guideline dictates what to omit. |
| (c) Separate subsection labels | Add a subsection header per type (more verbose), no HTML comments. |

**Recommendation**: (a)

**Rationale**: Fast, unambiguous, and matches existing template conventions for in-template author guidance.

**Implementation note**: `TK003` applies markers to all type-conditional sections.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC005 — Evidence/Methodology Placement (GAP-006)

**Context**: Mature exemplars ground claims in explicit evidence (file paths, commands, etc.). The current template lacks a dedicated evidence/methodology section.

**Decision prompt**: Where should the Evidence/Methodology section live in the standard analysis structure?

| Option | Description |
|:--|:--|
| **(a) Universal near top (Recommended)** | Add a required Evidence/Methodology section immediately after Scope & Inputs, for all analysis types. |
| (b) Type-specific placement | Evidence placement varies per type; guideline defines placement per type. |
| (c) Embedded-only | No standalone section; evidence must be embedded within each section. |

**Recommendation**: (a)

**Rationale**: Makes evidence rules hard to miss and keeps analysis artifacts auditable and toolable across all types.

**Implementation note**:
- `TK002` codifies evidence requirements.
- `TK003` adds the section to the template.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC006 — Findings/Gap Register Schema (GAP-008)

**Context**: Analysis artifacts use registers to track issues/gaps, but analysis findings are not gate-blocking in the same way verification findings are. A lighter-weight schema reduces semantic confusion with verification.

**Decision prompt**: What schema should analysis findings/gaps use in Draft 1?

| Option | Description |
|:--|:--|
| (a) Mirror verification findings schema | Use `FINDING-###` plus severity + Situation A/B semantics as in verification. |
| **(b) Lightweight GAP-style schema (Recommended)** | Use `GAP-###` (or `AN-GAP-###` if desired), with fields: `ID`, `Category`, `Title`, `Description`, `Disposition`, `Downstream Target`, `Notes`. No gate-blocking semantics. |
| (c) No register | Findings remain free-form narrative only. |

**Recommendation**: (b)

**Rationale**: Preserves structured tracking while preventing analysis from inheriting verification’s gate authority semantics.

**Implementation note**:
- `TK002` defines the register schema and how it differs from verification.
- `TK003` adds a Findings/Gap Register section/table to the template.
- Per DEC012, `Disposition` values are enumerated (bounded set) to preserve structured tracking.

**Client Decision**: `[ ] (a)` / `[x] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC007 — Integration Roadmap Handling (GAP-009)

**Context**: The existing template’s “Integration Roadmap” is deeply tied to research-synthesis proposal seeding and does not apply to other analysis types.

**Decision prompt**: How should downstream actions be represented in the template across types?

| Option | Description |
|:--|:--|
| **(a) Keep research-synthesis roadmap; mark as conditional (Recommended)** | Retain the current integration roadmap content, but mark it as `research_synthesis` only via conditional marker. Other types use a generic “Downstream Actions” section. |
| (b) Replace with a single generic “Downstream Actions” section | Remove the research-synthesis roadmap content; all types use the same generic section. |
| (c) Type-specific downstream sections | Provide dedicated downstream section variants per type. |

**Recommendation**: (a)

**Rationale**: Minimizes disruption to existing research-synthesis workflow while avoiding misapplication to other types.

**Implementation note**: `TK002/TK003` align guideline rules and template sections accordingly.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC008 — Linking Chain Scoping (GAP-010)

**Context**: The T104-IG-002 Brief→Report→Analysis→Proposal linking chain applies to research synthesis, but not to compliance audits, assessments, external reviews, or pattern audits.

**Decision prompt**: How should the guideline scope the linking chain to prevent misapplication?

| Option | Description |
|:--|:--|
| **(a) Explicitly scope IG-002 to research synthesis only (Recommended)** | Guideline states: IG-002 lifecycle and cross-artifact rules apply only when `analysis_type = research_synthesis`. Other types define their own lifecycle positions and handoffs. |
| (b) Treat IG-002 as global | IG-002 is referenced without scoping; authors infer applicability. |
| (c) Omit IG-002 entirely from analysis guideline | Keep linking chain out of analysis guidance and rely on separate artifacts. |

**Recommendation**: (a)

**Rationale**: Prevents category errors and preserves the intent of IG-002 without over-generalizing.

**Implementation note**: `TK002` includes an explicit scoping sentence and per-type lifecycle notes (see also DEC011 for non-research lifecycle positions).

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC009 — Scope & Inputs Placement (GAP-007)

**Context**: All examined exemplars place “Scope & Inputs” near the top. The current analysis template opens with “Source Material Summary,” which is research-synthesis specific and not a universal replacement for scope framing.

**Decision prompt**: Where should “Scope & Inputs” appear in the standard analysis structure?

| Option | Description |
|:--|:--|
| **(a) Universal section near top (Recommended)** | Add a required “Scope & Inputs” section immediately after the Executive Summary for all analysis types. |
| (b) Embed into Executive Summary | Do not add a dedicated section; scope framing must be included in the executive summary. |
| (c) Type-specific placement | Scope placement varies by type. |

**Recommendation**: (a)

**Rationale**: Makes scope unmissable and normalizes a stable structure across analysis types while still allowing type-specific content elsewhere.

**Implementation note**:
- `TK002` makes “Scope & Inputs” a universal required section.
- `TK003` inserts the section and refactors “Source Material Summary” to be research-synthesis-only if retained.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC010 — Add Proposal Template Cross-Check to TK004 Targets (ER-GAP-003)

**Context**: The analysis template (research synthesis) is designed to feed proposal seeding workflows. TK004 currently cross-checks the ANALYSIS guideline vs workflow/governance references, but does not include `template_workspace_proposal.md` as a target. This increases the risk of analysis→proposal handoff drift (Draft 1).

**Decision prompt**: Should TK004 include `template_workspace_proposal.md` in the cross-check target list to reduce handoff drift risk?

| Option | Description |
|:--|:--|
| **(a) Add proposal template cross-check to TK004 (Recommended)** | Expand TK004 scope to include `prompt/templates/consultant/workspace/template_workspace_proposal.md` as an additional target. |
| (b) Defer to Draft 2 | Keep TK004 unchanged; accept residual drift risk through Draft 1 and address in TK901. |
| (c) Defer to AC008 only | Do not expand TK004; rely on AC008 (proposal guideline/template alignment) to correct any drift later. |

**Recommendation**: (a)

**Rationale**: Minimal incremental work in TK004 and highest leverage to reduce analysis→proposal friction.

**Implementation note**: If (a) is chosen, update TK004 target list in the AC007 plan and execute the cross-check during TK004.

**Client Decision**: `[] (a)` / `[x] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC011 — Lifecycle Positions for Non-Research Analysis Types (ER-GAP-001)

**Context**: DEC008 scopes the T104-IG-002 linking chain to `research_synthesis`. Draft 1 still needs lifecycle positioning guidance for the other `analysis_type` values (`pattern_audit`, `compliance_audit`, `assessment`, `external_review`) to avoid “orphan” analyses with unclear upstream/downstream handoffs.

**Decision prompt**: Should TK002 define preliminary lifecycle positions for all 5 analysis types in Draft 1?

| Option | Description |
|:--|:--|
| **(a) Define preliminary lifecycle positions for all 5 types (Recommended)** | TK002 defines lifecycle positions for all `analysis_type` values, clearly marking non-research positions as “Draft 1 preliminary — revise as exemplars accumulate.” |
| (b) Research-only lifecycle (Draft 1) | TK002 defines lifecycle only for `research_synthesis`; non-research types remain lifecycle-undefined until more exemplars exist. |
| (c) Create a follow-on task | Keep TK002 focused; define non-research lifecycle positions in a separate task after Draft 1. |

**Recommendation**: (a)

**Rationale**: Prevents ambiguity for non-research authors while maintaining appropriate humility (“preliminary”) given limited exemplars.

**Implementation note**: `TK002` adds a lifecycle table/section per analysis type with explicit Draft 1 caveats for non-research types.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC012 — Enumerate `Disposition` Values for the GAP Register (ER-GAP-002)

**Context**: DEC006 adopts a lightweight GAP register schema with a `Disposition` field. If the field is free-text, cross-artifact tracking and automation become unreliable.

**Decision prompt**: Should the analysis GAP register define a bounded `Disposition` value set in Draft 1?

| Option | Description |
|:--|:--|
| **(a) Bounded enum (Recommended)** | Define a bounded set, recommended: `pending_decision`, `resolved`, `deferred_to_<task>`, `superseded`, `accepted_as_is`. |
| (b) Free-text disposition | Allow any text in `Disposition`. |
| (c) Split into multiple fields | Replace `Disposition` with multiple fields (e.g., `Status`, `Owner`, `Target`, `Due Date`) — higher structure but higher burden. |

**Recommendation**: (a)

**Rationale**: Keeps the schema lightweight while still preserving toolable structure.

**Implementation note**:
- `TK002` defines the enum and naming convention for `deferred_to_<task>` (e.g., `deferred_to_TK004`).
- `TK003` reflects the bounded set in template instructions/examples.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### DEC013 — Define Generic “Downstream Actions” Section Requirements (ER-GAP-004)

**Context**: DEC007 retains the research-synthesis Integration Roadmap and introduces a generic “Downstream Actions” section for non-research types. Without a minimal field spec, TK002 may under-specify this section and create inconsistent handoffs.

**Decision prompt**: Should TK002 define required fields and per-type guidance for the generic “Downstream Actions” section in Draft 1?

| Option | Description |
|:--|:--|
| **(a) Define required fields + per-type guidance (Recommended)** | TK002 defines a minimal required field set and short per-type guidance. Suggested minimum fields: `downstream_artifact_type`, `target_reference`, `trigger_condition`, `responsible_role`, `notes`. |
| (b) Narrative-only | No required fields; authors write free-form downstream notes. |
| (c) Per-type bespoke sections | Define distinct downstream section variants per analysis type — more explicit but more template complexity. |

**Recommendation**: (a)

**Rationale**: Provides determinism without over-engineering the template.

**Implementation note**:
- `TK002` defines the section schema/fields and per-type guidance.
- `TK003` adds the section to `template_workspace_analysis.md` as a non-research conditional section.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

## IV. EXECUTION INSTRUCTIONS (POST GATE-000)

**Gate enforcement**: `T104-PH001-ST005-AC007-TK002`, `TK003`, and `TK004` MUST NOT start until the Gate Decision Record (§V) is updated to:
- `Client Decision = APPROVE`, or
- `Client Decision = APPROVE WITH CONDITIONS` (conditions enumerated and tracked).

**Deterministic downstream execution mapping**:
- `TK002 (Guideline)`: codify the decisions as normative guidance (5-type taxonomy, lifecycle per type per DEC011, required sections, evidence rules, findings schema + bounded `Disposition` values per DEC012, frontmatter conventions, naming, template inventory, and generic “Downstream Actions” section spec per DEC013).
- `TK003 (Template)`: update `template_workspace_analysis.md` to implement the conditional structure, frontmatter keys, universal sections, findings/gap register (including DEC012 guidance), evidence methodology section, downstream actions section (DEC013), and references/links register.
- `TK004 (Cross-check)`: verify no contradictions vs `T102-STD-006`, `T104-IG-002`, `guideline_workspace_verification.md`, `workspace_documentation_rules.md`, and `guideline_workspace_plan.md`. If DEC010 is approved, also cross-check against `template_workspace_proposal.md` (analysis→proposal handoff alignment).

---

## V. GATE DECISION RECORD (GDR)

This section is extracted from `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (§X) and adapted for proposal acceptance. For this proposal gate, “Reviewer Verdict” is the consultant assessment that this disposition package is complete and decision-ready.

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `T104-PH001-ST005-AC007-GATE-000` |
| Reviewer Verdict | PASS |
| Client Decision | APPROVE |
| Conditions (if any) | — |
| Decided By | Client |
| Decision Date | 2026-03-01 |
| Decision Reference | Client approval recorded inline in this GDR (instruction on 2026-03-01). |

---

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-01 | Initial | Created GATE-000 decision disposition proposal (DEC scheme) grounded in AC007 TK001 analysis pattern audit. |
| v1.1.0 | 2026-03-01 | Update | Incorporated independent external review flags as additional decision items (DEC010–DEC013) to ensure deterministic downstream scope (TK002–TK004) before Client gate approval. |
| v1.1.1 | 2026-03-01 | Update | GATE-000 decision recorded: Client Decision set to APPROVE in GDR. |
