---
artifact_type: 'ANALYSIS'
planning_level: 'ACTIVITY'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST001'
activity_id: 'T102-PH001-ST001-AC009'
sub_activity_id: 'T102-PH001-ST001-AC009.1'
version: '0.1.0'
date: '2026-02-15'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Second-opinion gap/risk review of AC009.1 redesign proposal (STD-004 comprehensive redesign + STD-009 merge) to improve GATE-001 approval readiness and reduce downstream implementation risk.'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
source_plan: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md'
source_session_notes: 'prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC009-SES002.md'
source_proposal: 'prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md'
current_target_std: 'prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_specification-standard-and-guideline.md'
current_target_sps: 'prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md'
---

# ANALYSIS: AC009.1 (STD-004 Redesign) — GATE-001 Second-Opinion Review (Gaps, Risks, and Recommendations)

## I. EXECUTIVE SUMMARY

This analysis provides a second-opinion review of the AC009.1 redesign proposal (`proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md`) commissioned after AC009-GATE-001 QA findings (`notes_T102-PH001-ST001-AC009-SES002.md`). It focuses on **approval readiness** (AC009.1-GATE-001), plus **downstream implementation risk** for AC009.1-TK002 (formalization into `T102-STD-004`, guideline, template, SPS).

**Top blocking gaps (approval/implementation-risk):**
1. **STD Index schema mismatch vs SPS reality**: Proposal makes `Governed By` normative, but SPS STD Index currently omits it.
2. **Adoption contract ambiguity**: `Adopts` semantics + the “self-contained” problem for `T102-STD-004` are unresolved, risking a gate stall and/or post-merge conformance confusion.
3. **Normative vocabulary consistency is internally inconsistent** (BCP 14 preference vs examples using SHALL), risking repeat drift and reviewer disputes.
4. **Resequencing blast radius is under-scoped**: proposal addresses guideline/template/SPS, but does not define “key surfaces” nor a controlled update mechanism for high-signal references outside those files.
5. **Substandard semantics ambiguity**: Even if “heading-only” is intended, the `T102-STD-004A/B/C/D` shape looks like a token; stronger “non-token” guardrails are needed to avoid accidental governance expansion.

**Recommendation posture:** Proceed with the current architecture direction (STD-009 merge + substandard headings + full resequencing), but add **explicit decisions** and **tight wording updates** to eliminate the above ambiguity before requesting AC009.1-GATE-001 approval.

---

## II. INPUTS REVIEWED (GROUNDING)

### A. AC009.1 proposal + decision evidence
- Proposal: `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md`
- Session notes (18 decisions): `prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC009-SES002.md`
- Stream plan (AC009.1 scope/gates): `prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md`

### B. Current governing surfaces affected by AC009.1 formalization
- Current STD-004: `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_specification-standard-and-guideline.md`
- Current STD-009 (to be absorbed): `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md`
- Current guideline/template: `prompt/templates/consultant/standards/guideline_standard_specs.md`, `prompt/templates/consultant/standards/template_standard_specs.md`
- Current SPS (STD Index + derivatives): `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
- Related standards referenced by proposal: `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`, `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-007_issues-risks-index.md`

### C. Client QA inputs (dialogue in this thread, 2026-02-15)
1. Self-adoption is not intuitive; `Adopts` may be redundant vs Canonical Path; desire to use the column to express “spec exists vs registry-only”.
2. Leaning “heading-only” substandards; concern that `T102-STD-004A` looks like an STD token instance.
3. Prefer updating “key surfaces only” but uncertainty about what those are; desire for script support because semantics changed materially.

---

## III. FINDINGS (GAPS + RISKS) WITH RECOMMENDATIONS

### Finding 1 — STD Index schema mismatch (proposal vs SPS reality)

**What’s happening**
- Proposal’s merged `CLAUSE-012A` defines STD Index schema including `Governed By` (`| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Governed By | Reference |`).
- Current SPS STD Index uses schema without `Governed By` (9 columns): `| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |`.

**Why it’s a gate risk**
- AC009.1-TK002 necessarily touches SPS (proposal explicitly lists SPS as a target file).
- If the gate approves the proposal as-written, AC009.1 implementation must introduce a schema-breaking change to SPS without explicit acceptance criteria, increasing rejection probability or rework.

**Recommendation**
- Treat this as a **first-class decision** to close before AC009.1-GATE-001:
  - Either (A) add `Governed By` to SPS STD Index and define its semantics clearly (what belongs there vs `Reference`), or
  - (B) explicitly remove `Governed By` from the STD Index schema and re-home those semantics (but this is a higher-risk change because it conflicts with absorbed STD-009 guidance).

**External alignment note (registry practice)**
- Registries typically require clear “specification” references for entries and explicit change-control guidance, not ambiguous/duplicated metadata surfaces. RFC 8126’s “Specification Required” notion is a useful mental model: a stable, public, sufficiently detailed specification should exist and be referenced when defining/operating a registry. [SRC-4]

---

### Finding 2 — Adoption contract ambiguity (`Adopts`) and the “self-contained standard” problem

**What’s happening**
- Proposal absorbs the adoption contract: “exactly one `Adopts` reference” (as `CLAUSE-010A`).
- Client feedback indicates self-adoption for `T102-STD-004` feels circular and undermines the column’s value.

**Core ambiguity to resolve**
What is the *primary purpose* of `Adopts` in the STD Index?
1) A **pointer to canonical normative text** (“where the actual rules live”), or
2) A **governance signal** (“this registry entry’s rules are defined elsewhere vs in-row / in-file”), or
3) Both (which risks redundancy/confusion without strict definitions).

**Recommendation (options with tradeoffs)**

**Option 1 (lowest churn; most consistent with current proposal text)**: Keep `Adopts` as the canonical “spec pointer”, and explicitly allow “self-contained” adoption.
- Define: `Adopts` is the canonical normative specification reference for that STD entry. If the STD’s canonical spec lives in the same combined file, `Adopts` MAY reference itself (i.e., “this file is the adopted spec”).
- Add a short explanation in the absorbed adoption-contract clause to prevent reviewer confusion: “Self-reference is not a no-op; it is an explicit declaration that the STD’s canonical text is this file.”
- Risk: still feels weird to humans; mitigate by adding a “self-contained” note and ensuring `Adopts` is never used as a proxy for “external spec exists”.

**Option 2 (human-first clarity; larger blast radius)**: Replace/rename `Adopts` to a “Canonical Spec” concept that can be either a path or a formal reference, and allow `—` explicitly for self-contained standards.
- Define: if `Adopts = —`, then the STD is self-contained (its canonical spec is in the same file), and the STD body becomes authoritative without an external pointer.
- Risk: requires rewriting absorbed STD-009 semantics (and corresponding proposal clauses) and likely needs more ST002 coordination.

**Option 3 (most explicit; adds column(s))**: Keep `Adopts` as the formal reference and add a separate *operational* locator (e.g., `Canonical Path`) for repo tooling.
- Formal `Adopts`: backticked `ID (Title)`.
- Operational locator: repo-relative path.
- Risk: schema expansion + more upkeep; benefit: removes the “why self-adopt” confusion by giving each column a distinct job.

**External alignment note (normative references + stability)**
- ISO drafting guidance strongly discourages relying on unstable external web references and emphasizes clarity about how content is normatively referenced/used. For this repo, stable repo-relative references are closer to that spirit than ungoverned URLs. [SRC-5]

---

### Finding 3 — Normative vocabulary consistency is not decision-complete

**What’s happening**
- Proposal states BCP 14 keywords are “preferred primary vocabulary” (e.g., `MUST`, `SHOULD`, `MAY`) but also uses “SHALL” in proposed obligation text snippets.

**Why it matters**
- Industry practice distinguishes:
  - IETF BCP 14 (RFC 2119 + RFC 8174): controlled requirement keywords; uppercase-only semantics clarification. [SRC-1], [SRC-2], [SRC-3]
  - ISO house style: “shall” as requirement, “must” as external constraint; avoid undefined verbal forms; avoid ambiguity across translations. [SRC-5]
- T102 currently cites RFC semantics via `T102-CON-009`, but the drafting style decision (primary vocabulary) must be made explicit to prevent ongoing “keyword correction churn”.

**Recommendation**
- Force a single explicit decision for Phase 1, with a “compatibility” rule:
  - If you want BCP 14 as primary: avoid SHALL in new normative obligations (unless explicitly permitted as equivalent under your governance).
  - If you want ISO-style as primary: update the BCP 14 reference posture so reviewers don’t treat SHALL usage as an error.
- Ensure the proposal’s own examples adhere to the chosen posture (otherwise the gate will approve drift-by-example).

---

### Finding 4 — Full resequencing blast radius is under-defined (“key surfaces” unclear)

**What’s happening**
- Proposal acknowledges that resequencing breaks existing `T102-STD-004-CLAUSE-*` references and that STD-009 is deprecated/superseded.
- Proposal includes derivative updates for guideline/template/SPS, but does not define “key surfaces” nor a controlled approach to update the highest-signal remaining references (e.g., active standards, validators/tests, non-archived governance docs).

**Why it’s a risk**
- Leaving old references in active, high-signal places recreates the exact “agentic drift” failure mode that motivated the merge.

**Recommendation**
Define (and explicitly scope) “key surfaces” for the migration posture. A recommended definition:
1. **SSOT surfaces**: SPS + Concept (anything used as day-to-day governance entrypoints).
2. **Normative standards**: `prompt/artifacts/tasks/T102/consultant/standards/` (excluding deprecated archives only if clearly labeled).
3. **Derivatives**: guideline + template.
4. **Automation/verification surfaces**: `prompt/scripts/`, `prompt/tests/` (where outdated references cause false validations or misleading outputs).

Then state explicitly what is **not** a key surface (e.g., historical reports under `prompt/scripts/output/`, superseded proposals, archived artifacts), to prevent scope creep.

**Recommendation (script posture)**
If script support is desired, align it to “key surfaces only” and require it to be mapping-driven (no heuristic rewriting). Specifically:
- A mapping table for:
  - `STD-009` clause IDs → new `STD-004` clause IDs
  - old `STD-004` clause IDs → new resequenced IDs
- Then update references only in the key-surface set, leaving historical artifacts untouched.

---

### Finding 5 — Substandards should be “heading-only”, but need stronger guardrails to prevent token confusion

**What’s happening**
- Client preference: heading-only.
- Risk: `T102-STD-004A` looks like a legitimate `STD` RID token to both humans and tools.

**Recommendation**
Reinforce the “heading-only” contract with unambiguous constraints:
- Substandards are *structural headings only*; they must never appear in registries/taxonomy tables as tokens.
- Substandards must never be used inside backticked formal reference contexts (where they could be interpreted as RIDs).
- All formal referencing should cite the parent STD and the relevant `CLAUSE` IDs (which already stay under `T102-STD-004-CLAUSE-###`).

This recommendation aligns with the intent that “rules live in the standard; headings are navigation aids” and prevents accidental STD-005 taxonomy expansion (which the proposal already flags as an integration issue).

---

### Finding 6 — Status casing “applies across all status fields” likely needs scoping clarification

**What’s happening**
- AC009 notes record a decision: “Status enums MUST be lowercase wrapped in backticks … applies across all status fields.”
- Meanwhile, the Issues/Risks standard (`T102-STD-007`) explicitly requires uppercase backticked status enums for Issues and Risks.

**Why it matters**
If interpreted literally, the “all status fields” phrasing conflicts with the adopted Issues/Risks standard and will drive repeated reviewer contradictions.

**Recommendation**
Before gate approval, clarify that the lowercase status rule applies to:
- STD/ADR/CLAUSE lifecycle statuses (e.g., `proposed`, `accepted`, `deprecated`, `superseded`),
and does **not** override Issue/Risk lifecycle enums governed by `T102-STD-007`.

---

## IV. RECOMMENDED “GATE-001 READINESS” DELTAS (MINIMUM SET)

This is not an implementation plan; it is the minimal set of proposal clarifications needed to reduce GATE-001 stall risk:

1. Add an explicit decision/statement about **SPS STD Index schema** and whether `Governed By` will be added (and how it is used).
2. Make an explicit decision about **`Adopts` semantics** for self-contained standards (especially `T102-STD-004`).
3. Make the **normative vocabulary posture** decision complete (BCP 14 primary vs ISO-style primary) and align proposal examples.
4. Define **“key surfaces”** for resequencing migration and state whether a mapping-driven script will be used.
5. Strengthen “heading-only substandards” guardrails to prevent accidental tokenization.
6. Clarify status-casing scope so it does not conflict with `T102-STD-007`.

---

## V. EXTERNAL REFERENCES (INDUSTRY SOURCES)

These sources are included to ground “industry standard” comparisons used in this analysis.

## Sources
- [SRC-1] RFC Editor — RFC 2119: Key words for use in RFCs to Indicate Requirement Levels: https://www.rfc-editor.org/info/rfc2119
- [SRC-2] RFC Editor — RFC 8174: Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words: https://www.rfc-editor.org/info/rfc8174
- [SRC-3] RFC Editor — BCP 14 (RFC 2119 + RFC 8174 bundle): https://www.rfc-editor.org/info/bcp14
- [SRC-4] RFC Editor — RFC 8126: Guidelines for Writing an IANA Considerations Section in RFCs (registry + specification-required posture): https://www.rfc-editor.org/rfc/rfc8126.html
- [SRC-5] ISO — ISO House Style (drafting guidance; normative/informative labeling; verbal forms): https://www.iso.org/ISO-house-style.html
- [SRC-6] Cognitect (Michael Nygard) — Documenting Architecture Decisions (immutability + superseded posture): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions

## Changelog
| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.0 | 2026-02-15 | Initial | Second-opinion analysis for AC009.1: identified approval blockers and implementation risks; provided decision-focused recommendations to improve GATE-001 readiness. |

