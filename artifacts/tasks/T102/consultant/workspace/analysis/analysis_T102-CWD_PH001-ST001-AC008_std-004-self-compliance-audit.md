---
artifact_type: 'ANALYSIS'
planning_level: 'ACTIVITY'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST001'
activity_id: 'T102-PH001-ST001-AC008'
version: '0.3.0'
date: '2026-02-14'
status: 'gate_approved'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'STD-004 self-compliance audit (CLAUSE-001..017), derivative alignment verification (guideline + template), and remediation proposal for Client gate approval'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md'
source_dialogue: 'prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/notes_T102-PH001-SES001.md'
---

# ANALYSIS: Phase 1 / ST001 / AC008 — STD-004 Self-Compliance Audit & Exemplar Hardening

## I. EXECUTIVE SUMMARY

### A. Purpose (AC008)
This activity performs a CLAUSE-by-CLAUSE **self-compliance audit** of:
- `T102-STD-004 (Specification Standard & Guideline)` against its own 17 CLAUSEs, and
- the derivative artifacts governed by CLAUSE-017:
  - `prompt/templates/consultant/standards/guideline_standard_specs.md`
  - `prompt/templates/consultant/standards/template_standard_specs.md`

Deliverable intent: produce an audit report + remediation proposal suitable for `T102-PH001-ST001-AC008-GATE-001` (Client approval).

### B. Scope and constraints (Client-confirmed)
- **In scope**: STD-004 clause-by-clause audit + derivative alignment verification + remediation proposal.
- **Out of scope for this changeset**: applying any remediation edits (implementation occurs after gate approval).

### C. Summary of high-signal findings

**Primary issues (exemplar-hardening blockers)**:
1) **CLAUSE construction non-conformance (systemic)**:
   - Multiple CLAUSE bodies in `T102-STD-004` are not written as clearly singular normative statements and/or contain procedural imperatives that omit normative keywords (e.g., CLAUSE-003 “Add…” steps). This conflicts with `T102-STD-004-CLAUSE-005` and with the “Specification must be normative” intent in `T102-STD-004-CLAUSE-016`.
2) **Anchor derivation rule mismatch**:
   - `T102-STD-004-CLAUSE-007` states anchors derive from Title, but the deployed anchor scheme (post AC007) is derived from `ID + Title` (e.g., `t102-std-004-specification-standard-and-guideline`).
3) **Derivative traceability gap (CLAUSE-017 breach risk)**:
   - `guideline_standard_specs.md` contains normative rules (canonical directory + file naming/slug rules) claimed as governed by `T102-STD-004-CLAUSE-001/003`, but those rules are **not explicitly specified** in STD-004. This is “normative leakage” risk under the CLAUSE-017 constraint (“Derivatives MUST NOT introduce normative rules not traceable to a governing CLAUSE”).

### D. Recommendation
Adopt a remediation strategy that restores exemplar credibility by:
- bringing `T102-STD-004` into alignment with its own CLAUSE construction expectations (CLAUSE-005/016), and
- making the guideline’s canonical-location and naming rules explicitly governed by STD-004 (closing the CLAUSE-017 traceability gap), and
- amending CLAUSE-007 to reflect the actual anchor derivation rule used in Phase 1.

Two remediation options are provided in §VI; Option R2 is recommended for exemplar integrity.

### E. RES-007 Crosswalk Addendum (AC009 Gap Assessment)

This addendum integrates `T102-RES-007` (Standards Authoring Methodology Benchmarking) at the level required to support `T102-PH001-ST001-AC009` planning and Gate review.

**RES-007 integration readiness**:
- `T102-PH001-ST004-AC004-GATE-003` (Client sign-off on RES-007 integration recommendations) is **passed** on **2026-02-14**.

**Crosswalk: RES-007 gap matrix ↔ AC008 findings ↔ AC009 actions**

| RES-007 Gap | Severity | AC008 Audit Linkage | AC009 Action (Primary) | Status |
|:--|:--|:--|:--|:--|
| Clause granularity discipline (multi-obligation clauses need named subclauses) | Critical | Matches primary issue #1 (CLAUSE construction non-conformance) | Enhance `T102-STD-004-CLAUSE-005` subclause discipline (TK001 → proposal; TK004 → implement; TK005 → verify) | AC009-actionable |
| Normative/informative boundary hygiene (“normative leakage” prevention) | Critical | Partially overlaps derivative leakage; not explicitly governed inside STD-004 | Add `T102-STD-004-CLAUSE-018 (Boundary Hygiene)` and update derivatives to cite it (TK001/TK004/TK005) | AC009-actionable |
| Normative vocabulary consistency (controlled drafting vocabulary; avoid MUST/SHALL mixing) | Important | Not directly audited as a conformance item; observed as a system-level style risk | Add vocabulary guidance as a subclause under `T102-STD-004-CLAUSE-016` (TK001/TK004/TK005) | AC009-actionable (scope-approved) |
| Derivative traceability integrity (no untraced obligations in guideline/template) | Important | Matches primary issue #3 (CLAUSE-017 breach risk) | Govern directory + naming rules in STD-004 and fix derivative citations (TK001/TK004/TK005) | AC009-actionable |
| STD-004 / STD-009 modular boundary (do not merge; define interface) | Informational / Important | Out of scope for AC008 implementation; impacts downstream STD governance | Defer interface formalization to ST002 (STD-009 normalization scope) | ST002-deferred |

**AC009 scope boundary (actionable now vs deferred)**
- **AC009-actionable now**: boundary hygiene (new CLAUSE-018), CLAUSE-005 enhancement, vocabulary guidance, derivative traceability closure (directory/naming governance + citation fixes).
- **Deferred to ST002**: STD-009 normalization and any corpus-wide enforcement beyond the STD-004 exemplar + its immediate derivatives.

---

## II. INPUTS, METHOD, AND DEFINITIONS

### A. Inputs (audited artifacts)
1) Standard under audit:
   - `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_specification-standard-and-guideline.md`
2) Derivatives governed by CLAUSE-017:
   - `prompt/templates/consultant/standards/guideline_standard_specs.md`
   - `prompt/templates/consultant/standards/template_standard_specs.md`
3) Reference standard for ID/reference semantics:
   - `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`

### B. Severity scale (for this audit)
- **conformant**: satisfies all MUST/SHALL requirements that apply to the audited surface; no material ambiguity.
- **minor gap**: small ambiguity, incomplete traceability, or minor formatting drift that does not undermine intent.
- **non-conformant**: violates a MUST/SHALL requirement, contradicts other governed constraints, or materially undermines exemplar reliability.

### C. Applicability note (important)
Some CLAUSEs in STD-004 prescribe behavior for **other artifacts** (Concept/SPS indexes, downstream “combined files” generally).
For self-compliance, the audit treats each CLAUSE as requiring one of:
- (a) STD-004 as a combined file must comply directly, and/or
- (b) STD-004 must not contradict, and must remain accurate as the governing rule source for its governed surfaces.

---

## III. CLAUSE-BY-CLAUSE FINDINGS (TK001 / TK002)

### 1) `T102-STD-004-CLAUSE-001 (DR Index Schemas)` — **minor gap**

**What the clause requires (as written)**
- Defines an ADR Index schema and column definitions, including Canonical Path resolution expectations.

**Self-compliance check**
- STD-004 is not itself an ADR index table, so most of the clause is “governing for other artifacts”.
- However, the clause is used by derivatives (`guideline_standard_specs.md`) to justify canonical-path and naming rules.

**Finding rationale**
- The clause defines Canonical Path semantics but does **not** explicitly define:
  - the **designated standards directory** for the T102 consultant scope, or
  - a **file naming convention** for the standards directory.

This absence becomes material because derivatives currently assert these as normative rules “per CLAUSE-001/003”.

**Proposed remediation (see §VI)**
- Add explicit subclause(s) under CLAUSE-001 or CLAUSE-002 that define:
  - canonical directory for this scope, and
  - file naming convention + slug rules (or reference the authoritative location where those are governed).

---

### 2) `T102-STD-004-CLAUSE-002 (Placement Standards)` — **minor gap**

**What the clause requires (as written)**
- SPS has a `"<SCOPE> Governance Decisions"` section title.
- Concept has a `"<SCOPE> Architectural Decisions"` section title.
- SPS/Concept are index-only hubs referencing combined files by Canonical Path.

**Self-compliance check**
- STD-004 itself is a combined file and conforms to the “combined files” concept (it is extracted into a standards directory and referenced by Canonical Path in Concept).
- The exact section-title strings prescribed for SPS/Concept appear inconsistent with the current Concept surface (`concept_T102-CONSULTANT.md` uses `Decision System (ADR/STD Compendium)` and indexes).

**Finding rationale**
- This is an accuracy/coordination gap: the clause prescribes exact section titles that are not currently present in Concept (and may not be intended as literal titles post-migration).

**Proposed remediation (see §VI)**
- Clarify whether the section-title strings are:
  - normative exact headings, or
  - conceptual labels for “the governance decisions section”.
- If they are normative: propose follow-up hygiene work to align Concept/SPS headings (outside AC008 remediation scope unless explicitly commissioned).

---

### 3) `T102-STD-004-CLAUSE-003 (Entry Creation Workflow)` — **non-conformant**

**What the clause requires (as written)**
- A workflow for creating ADR index entries, including creating a combined file using the template and ensuring references follow `T102-STD-005`.

**Self-compliance check**
- This CLAUSE is itself part of the Specification section and is expected to be written as a normative specification clause (per CLAUSE-005 and CLAUSE-016).

**Finding rationale**
- The clause uses procedural imperatives (“Add… Assign… Create… Ensure… Populate…”) without explicitly encoding obligations using MUST/SHALL language.
- As a result, the CLAUSE reads like informative guidance rather than an enforceable specification clause, conflicting with:
  - `T102-STD-005-CLAUSE-005D` (“CLAUSE IDs represent enforceable Specification clauses and MUST be written as normative statements”), and
  - `T102-STD-004-CLAUSE-016` (“## Specification contains normative CLAUSE items”).

**Proposed remediation (see §VI)**
- Rewrite CLAUSE-003 into a single normative statement plus subclauses, or convert each step into explicitly normative requirements (`MUST`) while preserving the workflow shape.

---

### 4) `T102-STD-004-CLAUSE-004 (DR Body Template)` — **conformant**

**Self-compliance check**
- STD-004 contains one nested ADR body under `## Decision Record`:
  - `* **T102-STD-004-ADR-001 (Specification Standard & Guideline)** {#t102-std-004-adr-001-specification-standard-and-guideline}`
- Required subheadings exist: Context, Decision, Alternatives Considered, Consequences.
- Body text is on a new line and indented under headings; Consequences uses `(+)`, `(±)`, `(-)` bullets.

**No remediation proposed.**

---

### 5) `T102-STD-004-CLAUSE-005 (Specification Clauses)` — **non-conformant**

**What the clause requires (as written)**
- Specification is a list of clause items: `n) **<CLAUSE-ID> (<Title>)**`.
- Clauses are sequential.
- Clauses must conform to `T102-STD-005-CLAUSE-005D` (normative language).
- Each clause MUST be a single primary normative statement; additional detail SHOULD use subclauses.

**Self-compliance check**
- STD-004 satisfies: ordered clause list, sequential numbering (001..017), clause ID format.
- STD-004 does **not** satisfy the “single primary normative statement” discipline consistently, and several clauses contain multiple obligations without subclause IDs.
- Several clauses include informative/descriptive text and/or imperative steps without explicit normative keywords (see CLAUSE-003).

**Proposed remediation (see §VI)**
- Refactor the STD-004 specification section into a “single statement + subclause” pattern:
  - Keep top-level CLAUSE numbering stable (001..017),
  - Introduce subclauses (e.g., `T102-STD-004-CLAUSE-003A`, `…003B`) to carry detail,
  - Ensure each top-level CLAUSE contains a single normative “anchor” statement (MUST/SHALL/SHOULD/MAY).

---

### 6) `T102-STD-004-CLAUSE-006 (Cross-Artifact Linking Patterns)` — **conformant**

**Self-compliance check**
- STD-004 contains its decision record under `## Decision Record` (satisfies “STD internal DR pattern”).
- Nested ADR Context does not include a formal “Governed By” line; formal citations are in `## References`.

**No remediation proposed.**

---

### 7) `T102-STD-004-CLAUSE-007 (Anchor Title Stability)` — **non-conformant**

**What the clause requires (as written)**
- “Anchors MUST be lower-kebab derived from the Title.”

**Self-compliance check (as deployed)**
- The file’s anchors are of the form:
  - `t102-std-004-specification-standard-and-guideline`
  - `t102-std-004-adr-001-specification-standard-and-guideline`
These are derived from `ID + Title` (not Title-only).

**Finding rationale**
- The clause’s stated derivation rule does not match the actual canonical anchor construction used post-AC007.
- This is exemplar-critical because anchor stability and derivation rules are a dependency for reference hygiene and for any future automation.

**Proposed remediation (see §VI)**
- Amend CLAUSE-007 to explicitly define the Phase 1 anchor derivation rule:
  - anchor input is `<ID> + <Title>`,
  - normalization rules (spaces → `-`, `&` → `and`, strip punctuation, collapse repeats),
  - stability rule for title changes (migration requirement).

---

### 8) `T102-STD-004-CLAUSE-008 (Lifecycle Coherence)` — **conformant**

**Self-compliance check**
- Clause is conditional (“When a governing STD changes Status or is Superseded…”). No such event is in scope for this audit.

**No remediation proposed.**

---

### 9) `T102-STD-004-CLAUSE-009 (Status Management)` — **minor gap**

**What the clause requires (as written)**
- Lifecycle enum: `Proposed → Accepted → Deprecated`.
- Superseded IDs captured in **Supersedes** column.
- Points to CLAUSE-017 for specification lifecycle stages.

**Self-compliance check**
- Current Concept STD Index row for `T102-STD-004` uses Status `Proposed` and includes columns `Effective` and `Supersedes`, matching the intended schema.
- However, `T102-STD-004-CLAUSE-001` defines `Effective` as “ISO-8601 date `YYYY-MM-DD`” without specifying whether `—` is permitted; several Concept STD rows use `—` for Effective (including `T102-STD-004`).

**Proposed remediation (see §VI)**
- Clarify in CLAUSE-001 (or in a dedicated subclause) whether `Effective` permits `—` for “unknown / not yet set”, and if so under what conditions.

---

### 10) `T102-STD-004-CLAUSE-010 (Precedence Conflicts Hierarchy)` — **conformant**

**Self-compliance check**
- This clause is definitional and does not impose requirements on the STD-004 file structure.

**No remediation proposed.**

---

### 11) `T102-STD-004-CLAUSE-011 (Consequences Scope Requirements)` — **conformant**

**Self-compliance check**
- STD-004’s nested ADR Consequences section includes policy/authority boundary and automation impacts (linting/migration patterns), which are consistent with the clause’s guidance intent.

**No remediation proposed.**

---

### 12) `T102-STD-004-CLAUSE-012 (References & Provenance)` — **conformant**

**Self-compliance check**
- `## References` uses full formal reference style (`` `ID (Title)` ``) consistent with `T102-STD-005-CLAUSE-004`.
- `## Provenance` lists repo-relative paths (no raw URLs).

**No remediation proposed.**

---

### 13) `T102-STD-004-CLAUSE-013 (Variance ADR Contract)` — **conformant**

**Self-compliance check**
- Applies to downstream variance ADRs, not the STD-004 file itself.

**No remediation proposed.**

---

### 14) `T102-STD-004-CLAUSE-014 (Decision Promotion Workflow)` — **conformant**

**Self-compliance check**
- This clause provides guidance (SHOULD/MAY) and does not impose file-structure requirements on STD-004.

**No remediation proposed.**

---

### 15) `T102-STD-004-CLAUSE-015 (Automation & Linting Checks)` — **conformant**

**Self-compliance check**
- STD-004 satisfies the structural checks listed.
- Concept STD Index Canonical Path for `T102-STD-004` resolves to an existing file.

**No remediation proposed.**

---

### 16) `T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)` — **minor gap**

**What the clause requires (as written)**
- “Every combined file MUST contain exactly these sections in order…”

**Self-compliance check**
- STD-004 contains the required headings in the required order.
- The file includes an explicit anchor line `{#t102-std-004-specification-standard-and-guideline}` immediately after the `#` header.

**Finding rationale**
- If “exactly these sections” is interpreted as “exactly these headings”, STD-004 is conformant.
- If interpreted as “no other top-level structural lines permitted”, then explicit anchor lines would be disallowed; that interpretation would conflict with current repo practice (anchors are used widely for stable linking).

**Proposed remediation (see §VI)**
- Clarify in CLAUSE-016 whether explicit `{#...}` anchor lines are permitted as non-heading metadata under the `#` header and under nested ADR headers.

---

### 17) `T102-STD-004-CLAUSE-017 (Specification Lifecycle & Authority Chain)` — **minor gap**

**Self-compliance check**
- The derivative guideline and template exist and explicitly claim governance by STD-004.
- The guideline includes explicit “Conformance Coupling” language and “no untraced normative rules” language (aligns with CLAUSE-017 intent).

**Finding rationale**
- The guideline contains normative rules that are not currently explicitly traceable to a governing CLAUSE text in STD-004:
  - Canonical location (“all standard-spec files live under …”)
  - File naming convention + slug rules
While the guideline annotates these rules as “[per …]”, STD-004 does not state these requirements explicitly.

**Proposed remediation (see §VI)**
- Amend STD-004 to explicitly govern canonical directory and naming rules (preferably as subclauses under existing CLAUSE IDs to avoid renumbering).

---

## IV. DERIVATIVE ALIGNMENT VERIFICATION (TK004)

### A. `guideline_standard_specs.md` (PROCEDURAL_GUIDELINE) — alignment status: **minor gap**

**Observed derivative behavior**
- The guideline uses explicit “[per …]” citations to STD-004 CLAUSEs for most normative rules.
- It contains explicit coupling text:
  - “When `T102-STD-004` CLAUSEs are added, modified, or deprecated, this guideline and its template MUST be updated in the same changeset…”
  - “This guideline MUST NOT introduce normative rules… not traceable…”

**Primary misalignment**
- Canonical directory and file naming/slug rules are asserted as governed by `T102-STD-004-CLAUSE-002` and `T102-STD-004-CLAUSE-001/003`, but STD-004 does not explicitly define them.

**Result**
- The guideline is directionally aligned but requires STD-004 governance text to close the CLAUSE-017 traceability contract.

### B. `template_standard_specs.md` — alignment status: **conformant**

**Observed derivative behavior**
- Structural headings match CLAUSE-016.
- Nested DR pattern matches CLAUSE-004.
- Template does not introduce untraced normative obligations (it is a shape scaffold).

---

## V. AUDIT OUTPUTS (AC008 TK001–TK004 COMPLETE)

### A. Findings inventory (by severity)

| CLAUSE | Title | Finding | Severity |
|:--|:--|:--|:--|
| CLAUSE-001 | DR Index Schemas | Missing explicit governance for directory/naming used by derivatives | minor gap |
| CLAUSE-002 | Placement Standards | Prescribed exact section titles appear inconsistent with current Concept surface | minor gap |
| CLAUSE-003 | Entry Creation Workflow | Uses imperatives without normative keywords; reads as guidance, not specification | non-conformant |
| CLAUSE-004 | DR Body Template | Nested ADR conforms to required structure | conformant |
| CLAUSE-005 | Specification Clauses | Systemic mismatch: “single normative statement + subclauses” not consistently followed | non-conformant |
| CLAUSE-006 | Cross-Artifact Linking Patterns | Context/References boundary and internal DR pattern satisfied | conformant |
| CLAUSE-007 | Anchor Title Stability | Derivation rule contradicts deployed anchor scheme (ID+Title) | non-conformant |
| CLAUSE-008 | Lifecycle Coherence | Conditional; no triggered event | conformant |
| CLAUSE-009 | Status Management | Effective-date nullability ambiguous vs practice | minor gap |
| CLAUSE-010 | Precedence Conflicts Hierarchy | Definitional | conformant |
| CLAUSE-011 | Consequences Scope Requirements | Guidance satisfied by example | conformant |
| CLAUSE-012 | References & Provenance | Reference style + provenance satisfied | conformant |
| CLAUSE-013 | Variance ADR Contract | Out-of-surface | conformant |
| CLAUSE-014 | Decision Promotion Workflow | Out-of-surface | conformant |
| CLAUSE-015 | Automation & Linting Checks | Structural checks satisfied | conformant |
| CLAUSE-016 | Combined-File Canonical Structure | Anchor-line permissiveness not specified | minor gap |
| CLAUSE-017 | Specification Lifecycle & Authority Chain | Derivative traceability gap for directory/naming rules | minor gap |

### B. Remediation proposal coverage
See §VI for patch-ready remediation proposal options (no edits applied in this changeset).

---

## VI. REMEDIATION PROPOSAL (TK003) — FOR CLIENT GATE REVIEW

This section proposes two remediation options. Both options keep top-level CLAUSE numbering stable (001..017) and avoid any canonical-path renames.

### Option R1 (Minimal) — Fix exemplar contradictions + close derivative traceability gap

**Goal**: Make STD-004 internally consistent with deployed practice and remove the CLAUSE-017 “normative leakage” risk, with minimal restructuring.

**Proposed changes**
1) **Amend `T102-STD-004-CLAUSE-007`** to define the Phase 1 anchor derivation rule as `ID + Title` (and define normalization rules, including `& → and`).
2) **Amend `T102-STD-004` to explicitly govern canonical directory + naming convention**, either by:
   - adding subclauses under CLAUSE-002 (placement/canonical location), and under CLAUSE-001 or CLAUSE-003 (naming), or
   - adding a single new subclause under CLAUSE-001 that declares both directory + naming as required.
3) **Clarify `Effective` nullability** in CLAUSE-001/009 (explicitly allow `—` as “not set yet” OR require a date and fix the index rows in a separate hygiene activity).
4) **Clarify anchor-line permissiveness** in CLAUSE-016 (explicitly allow `{#...}` lines as non-heading metadata).

**Pros**
- Smaller changeset; lower blast radius.
- Immediately resolves the two highest-risk contradictions (anchors + derivative traceability).

**Cons**
- Does not fully satisfy the CLAUSE-005 “single normative statement + subclause” discipline; exemplar remains less machine-checkable.

### Option R2 (Strict exemplar) — Bring STD-004 into full self-conformance with CLAUSE-005/016 discipline

**Goal**: Make `T102-STD-004` a provably self-conformant exemplar by enforcing its own clause-construction rules.

**Proposed changes (superset of R1)**
1) Apply all R1 changes.
2) Refactor each CLAUSE body to follow a strict pattern:
   - Each top-level CLAUSE contains **one** normative anchor statement (MUST/SHALL/SHOULD/MAY).
   - All additional requirements are placed into explicitly labeled subclauses using `T102-STD-004-CLAUSE-###A/B/C...` (per `T102-STD-005-CLAUSE-005D`).
   - Procedural workflows (e.g., CLAUSE-003) are rewritten as normative requirements (MUST) while retaining a clear stepwise structure.

**Pros**
- Restores exemplar credibility; supports future linting/automation.
- Eliminates ambiguity about what is normative vs explanatory.

**Cons**
- Larger changeset; more review effort.
- Requires careful editing to avoid semantic drift while restructuring.

### Patch-ready change sketch (illustrative; not yet applied)

This sketch indicates the minimum governance text needed to close the derivative traceability gap without renumbering CLAUSEs. Exact final wording should be approved at gate.

#### A. Proposed exact edits (copy/paste-ready; not yet applied)

##### 1) STD-004: CLAUSE-001 — clarify `Effective` nullability

Target location:
- `T102-STD-004-CLAUSE-001 (DR Index Schemas)` → **Column Definitions** → item `5. Effective`

Proposed replacement text:
- Replace:
  - `5. \`Effective\`: ISO-8601 date \`YYYY-MM-DD\`.`
- With:
  - `5. \`Effective\`: ISO-8601 date \`YYYY-MM-DD\` or \`—\` if not yet set.`

Rationale:
- Aligns CLAUSE-001 with observed index practice and avoids “implicit exception” drift.

##### 2) STD-004: CLAUSE-002 — add explicit designated standards directory (closes guideline traceability gap)

Target location:
- `T102-STD-004-CLAUSE-002 (Placement Standards)` (append as final bullet)

Proposed insertion:
- `- **Designated Standards Directory (T102 Consultant)**: Combined standard-specification files for T102 consultant scope MUST live under \`prompt/artifacts/tasks/T102/consultant/standards/\`.`

Rationale:
- Makes the guideline’s canonical directory rule traceable to STD-004, satisfying CLAUSE-017.

##### 3) STD-004: CLAUSE-003 — make workflow explicitly normative

Target location:
- `T102-STD-004-CLAUSE-003 (Entry Creation Workflow)`

Proposed replacement (entire clause body; keep the clause heading as-is):
- Replace:
  - `To create a new ADR index entry:`
  - `1. Add ...`
  - `2. Assign ...`
  - `3. Create ...`
  - `4. Ensure ...`
  - `5. Populate ...`
- With:
  - `To create a new ADR index entry, authors MUST perform all of the following steps:`
  - `1. Add a new row to the appropriate index table using the required schema per \`T102-STD-004-CLAUSE-001\`.`
  - `2. Assign the next sequential ID for that scope.`
  - `3. Create a combined standard-specification file at the canonical path using the standard-specification template, applying CLAUSE entries under \`## Specification\` and DR body structure under \`## Decision Record\` per \`T102-STD-004-CLAUSE-004\`.`
  - `4. Ensure References follow \`T102-STD-005\`.`
  - `5. Populate the Canonical Path column in the index row with the full repo-relative path to the combined file.`

Rationale:
- Converts an “informative how-to” into an enforceable specification clause consistent with STD-005 CLAUSE semantics.

##### 4) STD-004: CLAUSE-007 — align derivation rule with deployed anchors (post-AC007)

Target location:
- `T102-STD-004-CLAUSE-007 (Anchor Title Stability)` (replace the four existing bullets)

Proposed replacement bullets:
- `- Anchors MUST be lower-kebab derived from \`<ID> + <Title>\` (e.g., \`t102-std-004-specification-standard-and-guideline\`).`
- `- Normalization MUST apply: spaces → \`-\`; \`&\` → \`and\`; strip punctuation; collapse repeated \`-\`.`
- `- Anchors MUST remain stable across file moves/splits.`
- `- If Title changes, keep the old anchor unless an explicit migration is performed.`
- `- Phase 1 stability contract: combined-file names and canonical paths SHOULD remain stable after migration completion. Anchors extracted from Concept remain stable within their combined file.`

Rationale:
- Restores internal consistency: the standard must describe the anchor rule the repo actually uses.

##### 5) STD-004: CLAUSE-016 — clarify that anchor lines are permitted metadata (avoid “exactly sections” ambiguity)

Target location:
- `T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)` (append as final bullet)

Proposed insertion:
- `- Non-heading metadata lines (e.g., explicit anchor lines in the form \`{#anchor}\`) MAY appear immediately after the \`# <STD-ID> — <Title>\` header and immediately after the nested ADR header line; this does not count as an additional required section.`

Rationale:
- Aligns the canonical-structure rule with current link-stability practice and prevents accidental prohibition of anchors.

##### 6) STD-004: directory + naming traceability → guideline citation fix (post-gate follow-up)

If changes (2) and (naming rule below) are accepted, update `guideline_standard_specs.md` citations so that:
- “Canonical location” cites `T102-STD-004-CLAUSE-002` (and/or the new designated-directory bullet).
- “File naming convention” cites the exact clause/subclause in STD-004 that governs naming.

##### 7) Missing governance: file naming convention + slug rules (recommended: add to STD-004; closes CLAUSE-017 “normative leakage”)

Target location (recommended):
- Append to `T102-STD-004-CLAUSE-003 (Entry Creation Workflow)` as an additional bullet OR introduce a `CLAUSE-003A` subclause in a strict (R2) refactor.

Proposed insertion (minimal, R1-compatible):
- `- **File Naming Convention**: Combined standard-specification filenames MUST follow \`<STD-ID>_<title-slug>.md\` where \`<title-slug>\` is lowercase, spaces → \`-\`, non-alphanumeric characters removed/replaced with \`-\`, and repeated \`-\` collapsed.`

Rationale:
- Makes the guideline’s naming rules traceable to STD-004, satisfying CLAUSE-017.

#### B. If Option R2 is selected: refactor pattern (example only; not fully enumerated here)

To satisfy the “single primary normative statement” requirement in CLAUSE-005 without renumbering, apply a consistent pattern:
- Keep `n) **T102-STD-004-CLAUSE-00N (...)**` as the top-level item.
- Make the first line under it a single anchor statement.
- Move all additional requirements into bullets prefixed with `T102-STD-004-CLAUSE-00N[A/B/C...]`.

Example (for CLAUSE-004, illustrative only):
- Top-level: `T102-STD-004-CLAUSE-004` becomes a single “DR body MUST conform to subclauses 004A..004D” anchor.
- Add subclauses:
  - `CLAUSE-004A` (Format)
  - `CLAUSE-004B` (Required headings)
  - `CLAUSE-004C` (Indentation/body rules)
  - `CLAUSE-004D` (Section placement boundary)

---

## VII. GATE PACKET CHECKLIST (`T102-PH001-ST001-AC008-GATE-001`)

Entry criteria satisfied by this artifact:
- [x] TK001: CLAUSE-by-CLAUSE audit performed for CLAUSE-001..017.
- [x] TK002: Findings recorded with severity + rationale.
- [x] TK003: Remediation proposal options provided (R1/R2) with patch-ready change sketch.
- [x] TK004: Guideline + template derivative alignment verified; traceability gaps identified.

Remaining gate action:
Gate action completed:
- [x] Client approval recorded (2026-02-11). R2 approved. Option B approved. Scope boundary confirmed.
- [x] Session evidence: `T102-PH001-ST001-AC008-SES001`

---

## VIII. GATE-001 DECISIONS (2026-02-11)

Gate entry criteria satisfied (TK001–TK004 complete). Client approval recorded below.

### A. Remediation option selected: R2 (Strict Exemplar)

Client approved full subclause refactor to make STD-004 provably self-conformant against CLAUSE-005 discipline. All 17 CLAUSEs will be restructured with subclauses where needed.

Decision: `T102-PH001-ST001-AC008-SES001-DEC001`

### B. STD-004 identity refocus: Option B (Combined File Authoring Standard)

STD-004 retains its role as the standard governing combined standard-specification file authoring. ADR-era CLAUSEs (001–004) are refocused to describe their function within the combined file model, not standalone ADR registration.

Key boundary:
- **STD-009** = STD registry handle (registration, indexing, body construction)
- **STD-004** = combined file internal authoring (CLAUSE construction, file structure, nested DR body, anchors, lifecycle, derivatives)

Decision: `T102-PH001-ST001-AC008-SES001-DEC002`

### C. Scope boundary

**In scope for AC008 TK005**:
- R2 subclause refactor of all 17 CLAUSEs
- Option B refocus (CLAUSE-001–004 rewritten for combined file context)
- CLAUSE-007 anchor derivation fix (ID + Title)
- CLAUSE-014 rewrite for STD-owns-ADR
- Explicit directory/naming governance (closes CLAUSE-017 gap)
- CLAUSE-016 anchor line clarification
- Guideline update (same changeset per CLAUSE-017)
- Template update if structural shape changes
- SPS MVC rewrite for refocused CLAUSE semantics

**Deferred to ST002**:
- STD-009 amendments (self-hosted STD exception, Concept index schema governance)
- SPS `Governed By` column gap (per STD-009-CLAUSE-004A)
- Concept STD Index schema governance formalization
- CLAUSE-014 potential migration to STD-009
- STD-004 `Adopts = —` exception formalization
- STD-004 retitle consideration

Decision: `T102-PH001-ST001-AC008-SES001-DEC003`

### D. CLAUSE-014 disposition

Rewrite for STD-owns-ADR model. The staged promotion concept (RES → IG → STD) remains valid; update framing so promotion target is STD (which contains nested ADR for rationale), not "STD/ADR" as alternatives. Flag as candidate for ST002 migration to STD-009.

Decision: `T102-PH001-ST001-AC008-SES001-DEC004`

### E. Additional directives

- STD-004 title kept as-is (`Specification Standard & Guideline`); retitle deferred to ST002. Decision: `DEC005`.
- STD-005 and STD-009 are first-class review targets in ST002-AC001. Decision: `DEC007`.
- Client preference: simplification of language and structured content over dense prose. Decision: `DEC001` (implicit in R2 approval).

---

## IX. APPROVED R2 REMEDIATION DIRECTION (Per-CLAUSE)

This section documents the approved refactoring direction for each CLAUSE. Detailed copy/paste-ready edits are provided in the companion proposal file:
`prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC008_r2-refactor-plan.md`

### A. Per-CLAUSE Refactoring Plan

| CLAUSE | Current Title | R2 Action | Key Change |
|:--|:--|:--|:--|
| 001 | DR Index Schemas | Refocus + subclauses | Retitle context to combined file indexes. Add subclauses for Effective nullability + designated directory. |
| 002 | Placement Standards | Refocus + narrow | Scope to `standards/` directory structure. Remove SPS/Concept section-title prescriptions (→ STD-009 domain). Add designated directory subclause. |
| 003 | Entry Creation Workflow | Rewrite normative + subclauses | Add MUST to lead-in. Add file naming convention subclause. |
| 004 | DR Body Template | Subclauses | Decompose into 004A (format), 004B (headings), 004C (body rules), 004D (placement). |
| 005 | Specification Clauses | Simplify + subclauses | Streamline overloaded text. Separate structural rule, referencing, non-duplication. |
| 006 | Cross-Artifact Linking | Subclauses | Each pattern bullet → named subclause (006A–006D). |
| 007 | Anchor Title Stability | Fix derivation | Amend to ID + Title. Add normalization subclauses. |
| 008 | Lifecycle Coherence | Minor | Single-statement already; add clarifying subclause if needed. |
| 009 | Status Management | Clarify | Cross-reference Effective nullability to 001. |
| 010 | Precedence Conflicts | No change | Single definitional statement. |
| 011 | Consequences Scope | No change | Already SHOULD-level guidance. |
| 012 | References & Provenance | Subclauses | Split into 012A (References) + 012B (Provenance). |
| 013 | Variance ADR Contract | No change | Already normative with MUST. |
| 014 | Decision Promotion Workflow | Rewrite | Retarget to STD (not "STD/ADR"). Flag for ST002 migration. |
| 015 | Automation & Linting | Minor update | Update check list for structural changes from other CLAUSEs. |
| 016 | Combined-File Canonical Structure | Clarify | Add MAY for `{#...}` anchor metadata lines. |
| 017 | Specification Lifecycle & Authority Chain | No structural change | Verify derivative gap closed by 002/003 amendments. |

### B. Derivative Updates (Same Changeset)

1. **Guideline** (`guideline_standard_specs.md`): Update all `[per ...]` citations to match refactored CLAUSE IDs/subclauses. Close traceability gap for canonical directory (→ CLAUSE-002 subclause) and naming convention (→ CLAUSE-003 subclause).
2. **Template** (`template_standard_specs.md`): Verify structural alignment with CLAUSE-016 (add anchor line allowance if template includes placeholder).
3. **SPS MVC** (`sps_T102-CONSULTANT.md`): Rewrite STD-004 body + MVC items to reflect refocused CLAUSE semantics. MVC should cite thematic CLAUSE groups, not enumerate every subclause.

---

## X. DEFERRED ITEMS REGISTER (→ ST002)

| # | Item | Why Deferred | Recommended Target |
|:--|:--|:--|:--|
| 1 | STD-009 amendments (self-hosted STD exception clause) | STD-009 changes require separate analysis + gate | ST002-AC001 |
| 2 | Concept STD Index schema governance (Authority STD + Canonical Path columns have no governing source) | Boundary decision between STD-004 and STD-009 | ST002-AC001 |
| 3 | SPS `Governed By` column gap (missing per STD-009-CLAUSE-004A) | SPS schema hygiene | ST002-AC003 |
| 4 | STD-004 `Adopts = —` exception formalization | Self-hosted STD needs explicit STD-009 exception | ST002-AC002 |
| 5 | CLAUSE-014 potential migration from STD-004 to STD-009 | Conceptually better fit in STD-009 (when to create an STD) | ST002 (post-baselining) |
| 6 | STD-004 retitle to reflect Option B identity | Avoid anchor/reference propagation in AC008 | ST002 |
| 7 | STD-005 and STD-009 first-class review using STD-004 as golden exemplar | Separate analysis scope | ST002-AC001 (DEC007) |

---

## XI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.0 | 2026-02-11 | Initial | Self-compliance audit (TK001–TK004): 17 CLAUSEs audited; 3 non-conformant, 5 minor gaps, 9 conformant; R1/R2 options proposed with patch-ready edits. |
| v0.2.0 | 2026-02-11 | Gate Closure | GATE-001 approved: R2 selected; Option B identity refocus approved; scope boundary locked; CLAUSE-014 rewrite approved; deferred items registered. Added §VIII–§X. |
