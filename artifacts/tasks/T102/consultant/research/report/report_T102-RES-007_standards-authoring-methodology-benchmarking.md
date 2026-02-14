---
artifact_type: 'RESEARCH_REPORT'
initiative_id: 'T102'
research_id: 'T102-RES-007'
version: '1.0.1'
iteration: '2'
date: '2026-02-14'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: Standards Authoring Methodology Benchmarking (`T102-RES-007`)

## I. EXECUTIVE SUMMARY

**Context**: This research was commissioned to benchmark the T102 standards authoring methodology (as implemented across `T102-STD-001..009`, with `T102-STD-004` and `T102-STD-009` as primary subjects) against established specification-authoring practices (ISO/IEC Directives Part 2, IETF BCP 14 / RFC 2119 / RFC 8174, IEEE standards style guidance, W3C process/style, and OASIS methodology), and to produce a decision-ready recommendation on whether `T102-STD-004` and `T102-STD-009` should merge or remain separate. Inputs include the AC008 self-compliance audit of `T102-STD-004` (R2 refactor approved) and the authority-chain constraints in `T102-STD-004-CLAUSE-017`.

**Verdict**: **GO** — proceed with `T102-STD-004` R2 formalization work in `T102-PH001-ST001-AC009`, but treat this report as an **enhancement lens**: (1) standardize normative keyword style and normative/informative boundary rules to match established guidance, (2) enforce clause granularity via named subclauses across the entire STD corpus (not just STD-004), and (3) **do not merge** `T102-STD-004` and `T102-STD-009` now; keep them separate but clarify their interface.

**Key Findings**:
1. **Clause granularity discipline is not consistently implemented across the STD corpus**: most T102 STDs use “multi-obligation bodies” inside a single `CLAUSE-###` without named subclauses; only `T102-STD-001`, `T102-STD-005`, and `T102-STD-009` materially use named subclauses. This validates AC008’s assessment that R2-style “anchor + subclauses” is needed for exemplar integrity (Topic 1).
2. **Industry drafting guidance converges on: explicit normative vocabulary + explicit normative/informative separation**. ISO/IEC Part 2 and IEEE-style guidance strongly emphasize controlled “verbal forms” (shall/should/may/can) and discourages “must” in formal standards drafting; IETF/W3C commonly use BCP 14 semantics via RFC 2119/8174. T102’s current mix of MUST/SHALL across STDs increases ambiguity and weakens mechanical conformance verification (Topics 2, 4–6). [1][2][3][4][5]
3. **T102’s combined-file model (normative spec + informative rationale in one file) is broadly industry-aligned in principle**, provided the informative portion is clearly labelled and does not contain normative requirements. ISO/W3C/OASIS patterns commonly co-locate normative and informative material in one publication while requiring clear marking and conformance boundaries; the T102 model maps cleanly to that approach (Topic 3, 4, 6). [1][4][6]
4. **Authority derivation chain + same-changeset conformance coupling is directionally aligned with change-control best practice**, but the current derivative artifacts demonstrate a real “normative leakage” anti-pattern (guideline declaring rules “per STD-004” that are not actually specified). This is precisely the class of drift that industry drafting governance tries to prevent (Topic 2, 3, 7). [1]
5. **Merge vs Separate (`STD-004` vs `STD-009`)**: industry bodies typically split “drafting/style rules” and “process/governance registry rules” into modular documents (e.g., ISO/IEC Directives Part 2 vs process directives; W3C Process vs style). Given T102’s deferred items register (AC008 §X), the best near-term move is **Separate-with-clarified-interfaces**: it resolves boundary ambiguity without expanding blast radius by merging (Topic 8). [1][4]

**Top Recommendations (preview)**:
1. **Keep `T102-STD-004` and `T102-STD-009` separate**, but add an explicit “interface contract” section: what each standard owns, what it MUST NOT own, and cross-references that are stable.
2. **Standardize normative keyword style across T102**: choose one primary drafting vocabulary (BCP 14 keywords or ISO/IEEE verbal forms) and ban mixing MUST/SHALL within a single standard unless explicitly justified by `T102-CON-009`.
3. **Generalize R2’s “anchor + named subclauses” pattern across the STD corpus** (or explicitly declare which STDs are exempt and why), so “CLAUSE == one testable obligation” becomes mechanically enforceable.

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Research stayed within the commissioned brief (`T102-RES-007`): no clause-level STD drafting and no SSOT/STD modifications. Output is recommendations-only.

**Source of Truth Audit**:
* **T102 standards (current state evidence)**:
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-001_consultancy-operating-model.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-002_canonical-yaml-header.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-003_explicit-inheritance-model.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_specification-standard-and-guideline.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-007_issues-risks-index.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-008_organisation-baseline-index.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md`
* **Commissioning/audit baseline**:
  * `prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102-RES-007_standards-authoring-methodology-benchmarking.md`
  * `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-CWD_PH001-ST001-AC008_std-004-self-compliance-audit.md`
  * `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC008_r2-refactor-plan.md`
* **Authority-chain derivatives**:
  * `prompt/templates/consultant/standards/guideline_standard_specs.md`
  * `prompt/templates/consultant/standards/template_standard_specs.md`
* **Normative keyword governing constraint (T102)**:
  * `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-CON-009`)

**External benchmark sources** (primary where accessible; otherwise explicitly treated as secondary): ISO/IEC Directives Part 2; IETF RFC 2119/8174; W3C Process + W3C Manual of Style; OASIS conformance/style guidance; IEEE Standards Style Manual (2009). [1][2][3][4][5][6][7][8]

**Limitations**:
* Industry documents evolve over time. This report uses the accessible published versions cited in §VI; if a newer edition supersedes a cited document, re-validation may change specific wording recommendations while preserving the high-level patterns.
* This report is time-locked to the cited editions/URLs in §VI (no attempt was made to chase newer editions beyond ensuring link accessibility).

---

## III. TOPIC FINDINGS

### Topic 1: CLAUSE Construction & Subclause Discipline (T102 corpus)
**Objective**: Inventory how T102 constructs `CLAUSE` items across `T102-STD-001..009` and characterize alignment with the “single primary normative statement + subclauses” discipline described in `T102-STD-004-CLAUSE-005`.

#### A. Evidence & Forensics
**CLAUSE construction inventory (defined clauses only; heuristic conformance to “single anchor + named subclauses”)**

**Heuristic scoring rubric (for reviewer reproducibility)**:
* **Parent CLAUSEs (defined)**: count of `T102-STD-###-CLAUSE-###` anchors (non-letter-suffixed) present as explicit headings/anchors in the STD.
* **Subclauses (defined)**: count of `...-CLAUSE-###A`, `...-CLAUSE-###B`, etc. (letter-suffixed) anchors explicitly present.
* **Conformance rate (heuristic)**: `conformant_parent_clauses / parent_clauses`, rounded to 2 decimals.
* **Conformant (heuristic)**: the parent CLAUSE reads as one testable obligation or definitional constraint, and uses named subclauses when multiple discrete obligations are present.
* **Pattern tags (heuristic)**:
  - `single_or_definitional`: a single obligation or definitional statement dominates the CLAUSE body.
  - `two_obligations`: two distinct obligations appear in one CLAUSE body without subclauses.
  - `multi_obligation`: 3+ distinct obligations appear in one CLAUSE body without subclauses.
  - `named_subclauses`: lettered subclauses are used to make obligations addressable.
  - `procedural_no_norm`: imperative workflow steps appear without explicit normative keywords.

| STD | Parent CLAUSEs (defined) | Subclauses (defined) | Sub/Parent | Conformance rate (heuristic) | Dominant clause-body patterns (heuristic) |
|:--|--:|--:|--:|--:|:--|
| `T102-STD-001` | 4 | 4 | 1.00 | 1.00 | `single_or_definitional`, `named_subclauses` |
| `T102-STD-002` | 2 | 0 | 0.00 | 0.50 | `single_or_definitional`, `two_obligations` |
| `T102-STD-003` | 4 | 0 | 0.00 | 0.25 | `multi_obligation` |
| `T102-STD-004` | 17 | 0 | 0.00 | 0.29 | `multi_obligation`, `two_obligations`, `procedural_no_norm` |
| `T102-STD-005` | 7 | 8 | 1.14 | 0.43 | `multi_obligation`, `named_subclauses` |
| `T102-STD-006` | 7 | 0 | 0.00 | 0.29 | `multi_obligation` |
| `T102-STD-007` | 11 | 0 | 0.00 | 0.00 | `multi_obligation` |
| `T102-STD-008` | 3 | 0 | 0.00 | 0.33 | `multi_obligation`, `two_obligations` |
| `T102-STD-009` | 5 | 5 | 1.00 | 0.20 | `multi_obligation`, `named_subclauses` |

**Observed cross-corpus patterns (examples; non-exhaustive)**:
* **“Multi-obligation clause bodies” are common** (many MUST/SHALL bullets inside a single `CLAUSE-###`) without named subclauses; this makes clause-level reference less precise (e.g., citing `CLAUSE-001` still leaves multiple obligations ambiguous).
* **Subclause patterns** when used are predominantly lettered suffixes (`CLAUSE-004A…E`) (e.g., `T102-STD-009-CLAUSE-004A..004E`), which is consistent with the R2 refactor direction selected in AC008 (§VIII–§IX in the audit analysis).
* **Procedural imperatives without normative keywords** appear as a failure mode specifically noted in AC008; in the current STD corpus, the clearest instance is `T102-STD-004-CLAUSE-003` (workflow steps written as “Add / Assign / Create / Ensure / Populate…” rather than MUST statements).

#### B. Analysis
**Synthesis**:
* The “anchor statement + named subclauses” pattern is not currently the dominant authoring method across the T102 STD corpus, and the lack of subclauses in core standards (notably `T102-STD-004`, `T102-STD-006`, `T102-STD-007`) is a structural contributor to ambiguity and audit burden.
* This materially strengthens the rationale for AC008 R2 refactor, and suggests the R2 approach should become **corpus-wide guidance**, not a one-off fix for STD-004.

**Implication for Topic 7**:
* A central gap dimension is “clause addressability”: industry standards strongly benefit from fine-grained, addressable requirements; T102 has the ID machinery, but clause bodies often contain multiple requirements that should become subclauses.

#### C. Governance Implication
* Treat “single anchor + named subclauses” as a **system-wide drafting constraint** (either as a rule in STD-004 or as a separate shared drafting standard), with explicit lintable rules.
* If exceptions are allowed (e.g., schema clauses that naturally enumerate multiple MUSTs), require explicit justification patterns and require subclauses anyway when referencing precision matters.

---

### Topic 2: Normative Keyword Semantics & Conformance Coupling
**Objective**: Assess how T102 uses normative keywords and evaluate the authority chain + conformance coupling model against industry practice.

#### A. Evidence & Forensics
* **T102 normative keyword constraint**: `T102-CON-009` states MUST/SHALL/SHOULD/MAY are interpreted per RFC 2119 and MUST be uppercase. (Source: `sps_T102-CONSULTANT.md`, “T102-CON-009 (Normative Keywords)”.)
* **Observed usage is mixed** across the STD corpus (e.g., some STDs are MUST-heavy; others use SHALL as primary). This is consistent with `T102-CON-009` semantics (RFC 2119 includes both MUST and SHALL), but weakens stylistic consistency and increases reviewer ambiguity.
* **Same-changeset conformance coupling** is specified in `T102-STD-004-CLAUSE-017` and repeated in the guideline (“When CLAUSEs change, guideline/template MUST update in the same changeset”). Evidence shows the guideline currently asserts canonical directory and naming rules “per STD-004” that are not explicitly governed in STD-004, violating the “no normative leakage” constraint in practice.

Industry evidence:
* **IETF** defines requirement-level keywords and warns about interpretation ambiguity; RFC 8174 clarifies uppercase vs lowercase applicability of RFC 2119 keywords. [2][3]
* **ISO/IEC Directives Part 2** defines controlled “verbal forms” for requirements/recommendations/permissions/possibilities (shall/should/may/can). [1]
* **IEEE style guidance** defines similar verbal forms and explicitly deprecates “must” as a drafting term in IEEE standards. [5]
* **W3C** uses RFC 2119 keywords as a normative vocabulary but explicitly distinguishes normative from informative parts and encourages clarity/consistency in conformance language. [4][6]

#### B. Analysis
**Keyword framework alignment**:
* T102’s choice to interpret keywords per RFC 2119 aligns well with IETF and with W3C’s long-running practice of using RFC 2119 semantics as a normative vocabulary for conformance language. [2][4]
* However, T102 currently mixes RFC-style (MUST/SHOULD/MAY) and ISO/IEEE-style (SHALL/SHOULD/MAY/CAN) within the same overall standards system. This creates an unnecessary “dialect surface” that complicates mechanical review and consistent author behavior.

**Authority chain + leakage**:
* Industry guidance consistently relies on a clear separation: normative requirements must live in the normative specification, while style/process guidelines must not add normative obligations “by accident”. This is functionally equivalent to T102’s “no normative leakage” rule and supports strengthening it (e.g., lint checks for derivative artifacts and for informative sections).

#### C. Governance Implication
* Make `T102-CON-009` decision-complete: select a **primary drafting vocabulary** and define:
  1) preferred keyword set (e.g., BCP 14 MUST/SHOULD/MAY as primary; SHALL permitted but discouraged), and
  2) explicit rule for informative sections (e.g., “informative sections MUST NOT use BCP 14 keywords unless explicitly flagged as normative”).
* Enforce `T102-STD-004-CLAUSE-017` with a compliance check that detects guideline/template obligations not traceable to a governing CLAUSE (and requires a remediation reference).

---

### Topic 3: Combined File Architecture & Specification Lifecycle
**Objective**: Evaluate T102’s combined standard-specification file model and lifecycle model against industry patterns.

#### A. Evidence & Forensics
* `T102-STD-004-CLAUSE-016` defines a combined-file canonical structure with `## Specification` (normative) and `## Decision Record` (informative) in the same file.
* `T102-STD-004-CLAUSE-017` defines lifecycle stages and an authority derivation chain (Specification → Guideline → Template) with same-changeset coupling.

Industry evidence:
* ISO/IEC Part 2 includes explicit rules for verbal forms and drafting, and the ISO/IEC publication model commonly includes both normative and informative elements in the same document while enforcing the boundary via labelling and drafting rules. [1]
* W3C process and style guidance distinguishes normative and non-normative content and treats conformance text as a first-class requirement in specs. [4][6]
* OASIS guidance emphasizes conformance statements and interoperability considerations as explicit parts of a specification set (often a suite), with clarity about what is required for conformance. [7][8]

#### B. Analysis
**Combined-file model**:
* T102’s combined-file approach is aligned with a broadly-used pattern: one canonical publication with clearly separated normative and informative parts. The key risk is not co-location; the key risk is **boundary contamination** (normative language in the rationale portion, or rationale treated as normative by readers).

**Lifecycle**:
* T102’s lifecycle stages are structurally plausible as an internal governance lifecycle (Draft → Proposed → Accepted → Amended → Deprecated), and can be mapped conceptually to W3C maturity stages (WD/CR/PR/REC) and other bodies’ states. [4]
* The main missing piece for industry alignment is not the list of states but the **change-control mechanics**: stable referencing, amendment/supersedes discipline, and how conformance applies across versions (which T102 partially addresses via `Supersedes` and coupling rules, but needs stronger interface definitions with `STD` registry semantics in STD-009).

#### C. Governance Implication
* Strengthen the combined-file model by adding explicit “normative/informative boundary” drafting constraints:
  - Informative sections MUST avoid BCP 14 keywords unless explicitly declared normative.
  - Conformance statements belong in the normative spec section (or in an explicit conformance clause/subclause).
* Tighten interface between lifecycle states in STD-004 and registry “Effective/Supersedes/Verification” semantics in STD-009 to prevent drift.

---

### Topic 4: ISO/IEC Directives Part 2 — Clause Construction & Document Structure
**Objective**: Benchmark T102 drafting and structure against ISO/IEC Directives Part 2.

#### A. Evidence & Forensics
* **Verbal forms**: ISO/IEC Directives Part 2 (2021) specifies “verbal forms” for expressing provisions; requirements use “shall” and “must” is explicitly disallowed in formal drafting. (Clause 7.2 and Table 3; see also Clause 7.2.1.) [1]
* **Numbering and subdivision discipline**: ISO/IEC Part 2 specifies how clauses/subclauses are numbered and subdivided (Clause 22.3.1 and Clause 22.3.2). [1]
* **Normative vs informative elements**: ISO/IEC Part 2 treats Foreword/Introduction as informative and specifies that the Scope should be factual and should not contain requirements (Clause 12.2 and Clause 14.5). [1]
* **Notes/examples are non-normative**: ISO/IEC Part 2 specifies that notes/footnotes/examples shall not contain requirements or recommendations (Clause 24.5 and Clause 25.1/25.5). [1]

#### B. Analysis
**Numbering and subclauses**:
* ISO/IEC typically uses hierarchical clause numbering (e.g., 5.1, 5.1.1) and defines subdivision rules, while T102 uses a flat `CLAUSE-###` plus lettered subclauses. This divergence is not inherently wrong; it is a representational choice. The risk is that lettered subclauses become optional or inconsistently applied (as observed in Topic 1). (ISO/IEC Part 2 Clause 22.3.1 and Clause 22.3.2.) [1]

**Verbal forms vs T102 keywords**:
* ISO/IEC Part 2’s controlled vocabulary differs stylistically from T102’s dominant MUST usage, but the drafting intent matches: one controlled vocabulary with defined semantics per “provision type” (requirements vs recommendations vs permissions). (ISO/IEC Part 2 Clause 7.2 and Table 3.) [1]
* For T102, the lowest-disruption posture remains: keep RFC 2119 semantics (per `T102-CON-009`), but enforce a single primary keyword style consistently, and strengthen boundary rules so informative sections do not carry normative force (consistent with ISO’s informative-element constraints). [1]

#### C. Governance Implication
* If T102 remains RFC-2119-based (per `T102-CON-009`), treat ISO/IEC Part 2 as structural guidance: emphasize granularity, explicit normative/informative separation, and consistent clause structure, rather than copying “shall” vocabulary wholesale.

---

### Topic 5: IETF RFC 2119/8174 & BCP 14 — Normative Keywords & Document Structure
**Objective**: Benchmark T102 normative keyword practice and document structure against IETF practices.

#### A. Evidence & Forensics
* RFC 2119 defines the semantics of requirement-level keywords, including MUST/MUST NOT/SHOULD/SHOULD NOT/MAY, and also includes SHALL/SHALL NOT as equivalents of MUST/MUST NOT. (RFC 2119, sections defining each keyword.) [2]
* RFC 8174 clarifies how RFC 2119 keywords are to be interpreted with respect to uppercase/lowercase ambiguity and applicability conventions (RFC 8174). [3]

#### B. Analysis
**Point-by-point semantic mapping (T102 ↔ IETF)**
* `MUST` / `SHALL`: Both represent “requirement level” obligations in RFC 2119; mixing both in the same corpus is permitted by RFC 2119 but can reduce stylistic consistency. T102 currently mixes both across STDs; choose a primary and treat the other as allowed-but-discouraged for uniformity. [2]
* `MUST NOT` / `SHALL NOT`: Same reasoning as above; standardize on one form for consistency. [2]
* `SHOULD` / `SHOULD NOT`: Recommendations with explicit rationale for deviation; this maps cleanly to T102 “recommended but not required” patterns and is well-suited for “authoring guidance inside normative specs” where hard enforcement is not intended. [2]
* `MAY`: Permission; T102 uses MAY appropriately for optional behaviors and exceptions, but should prefer named subclauses when MAY is used to define an exception contract (so it is addressable and auditable). [2]

**Uppercase convention**
* T102’s `T102-CON-009` (“MUST be written in UPPERCASE to carry normative meaning”) is consistent with the RFC 8174 posture and should remain the anchor for keyword interpretation in T102 governance. [3]

* The major improvement opportunity is operational rather than conceptual:
  - reduce “keyword sprawl” by ensuring each `CLAUSE`/subclause contains one testable obligation, and
  - ensure conformance-checkable language is in stable, addressable locations (subclauses), not in free-form narrative.

#### C. Governance Implication
* Evolve T102 keyword practice toward a “BCP 14 discipline” pattern:
  - require explicit conformance language in clause anchors,
  - discourage mixing MUST/SHALL to reduce confusion, and
  - require conformance section patterns for specs that can be tested.

---

### Topic 6: IEEE + W3C + OASIS — Consolidated Benchmark
**Objective**: Extract complementary drafting and conformance practices from IEEE/W3C/OASIS.

#### A. Evidence & Forensics
* IEEE drafting guidance defines the verbal forms and explicitly deprecates “must” as a term in IEEE standards drafting; “shall” indicates requirements, “should” recommendations, “may” permission, “can” possibility/capability. [5]
* W3C process/style guidance distinguishes normative/informative material and supports consistent conformance language (often via RFC 2119 keywords in specs). [4][6]
* OASIS guidance includes explicit attention to conformance and interoperability guidance as part of specification suites. [7][8]

**Consolidated comparison (summary; non-exhaustive)**

| Dimension | IEEE | W3C | OASIS | Relevance to T102 |
|:--|:--|:--|:--|:--|
| Controlled normative vocabulary | Prefers shall/should/may/can; “must” deprecated | Often uses RFC 2119 vocabulary; emphasis on normative/informative separation | Emphasis on conformance statements and interoperability guidance | Supports “pick a vocabulary and enforce it” |
| Normative vs informative | Clear separation; avoid ambiguity | Explicit separation; conformance is first-class | Specs often delivered as suites with conformance considerations | Supports T102 combined-file model with strict boundary rules |
| Conformance statements | Strong emphasis in standards drafting | Strong emphasis in specs; process maturity impacts review rigor | Conformance guidance is explicit | Supports adding conformance clause patterns in T102 |

#### B. Analysis
* IEEE and ISO are consistent with each other in “verbal forms” drafting (shall/should/may/can). W3C and IETF are consistent with each other in BCP 14 usage. The consistent pattern is **controlled vocabulary + explicit boundaries**, not which vocabulary is chosen.
* Given `T102-CON-009` already commits to RFC 2119 semantics, the lowest-disruption path is to keep BCP 14 semantics and enforce them more consistently (while documenting the difference from ISO/IEEE drafting vocab as a deliberate choice).

#### C. Governance Implication
* Add an explicit “Drafting vocabulary choice rationale” note to T102 governance (e.g., in `T102-CON-009` or a dedicated drafting standard) so reviewers do not attempt to “correct” MUST→SHALL inconsistently.

---

### Topic 7: T102 vs Industry Practice — Gap Analysis Matrix
**Objective**: Synthesize Topics 1–6 into a gap matrix with significance ratings.

#### A. Evidence & Forensics
See Topics 1–6 evidence; primary gaps are observable in clause inventory, derivative leakage examples, and keyword inconsistency, and are benchmarked against ISO/IEC, IETF, IEEE, W3C, and OASIS guidance. [1][2][3][4][5][6][7][8]

#### B. Analysis
**Gap analysis matrix (minimum dimensions; significance = Critical / Important / Minor / Informational)**

| Dimension | T102 current practice (observed) | Industry practice (benchmark) | Alignment | Significance | Implication |
|:--|:--|:--|:--|:--|:--|
| Clause granularity | Many `CLAUSE-###` contain multiple obligations with no named subclauses (Topic 1) | Fine-grained, addressable requirements (hierarchical numbering or structured clauses) [1] | Divergence | **Critical** | Adopt R2-style subclauses corpus-wide |
| Subclause discipline | Subclauses inconsistently used across STDs | Consistent hierarchical structuring patterns [1] | Divergence | **Important** | Standardize subclause pattern and require it for multi-obligation clauses |
| Normative vocabulary consistency | Mixed MUST/SHALL usage across STDs; `T102-CON-009` exists but not enforced as style | Controlled verbal forms (ISO/IEEE) or controlled BCP 14 keywords (IETF/W3C) [1][2][5] | Partial | **Important** | Decide and enforce a single primary vocabulary; reduce mixing |
| Normative vs informative boundary | Combined-file model exists, but derivative artifacts show “normative leakage” risk | Clear boundary between normative requirements and informative guidance; avoid accidental normativity [1][6] | Partial | **Critical** | Add lint/rules: informative sections + derivatives MUST NOT introduce obligations |
| Derivative authority chain | Authority chain declared; coupling rule declared; leakage exists in practice | Controlled change governance; derivatives cannot override specs [1] | Divergence | **Important** | Enforce traceability from guideline/template to governing clauses |
| Conformance statement patterns | Conformance intent exists but not standardized as a clause pattern across STDs | Conformance clauses/classes are first-class in many ecosystems [4][7] | Divergence | **Important** | Add a conformance clause pattern in STD-004 (or companion drafting STD) |
| Lifecycle + change control | Lifecycle stages exist; interface with STD registry semantics not fully formalized | Clear publication stages + supersession/amendment controls [4] | Partial | **Minor–Important** | Clarify mapping of “Accepted/Amended/Deprecated” to registry metadata and verification |
| “Standards about standards” modularity | Drafting rules (STD-004) separated from registry semantics (STD-009), but interface ambiguity remains | Typically modular docs: style/drafting vs process/governance [1][4] | Partial | **Important** | Keep separate; formalize interface contract |

#### C. Governance Implication
* Treat Topic 7 as the ordering function for AC009 work: resolve Critical gaps first (granularity + boundary), then Important (keyword standardization, conformance patterns, interface clarity).

---

### Topic 8: STD-004/STD-009 Merger Evaluation (first-class decision)
**Objective**: Decide whether to merge STD-004 and STD-009 or keep them separate with clarified interfaces.

#### A. Evidence & Forensics
**Current boundary (as implemented + AC008 decisions)**:
* **STD-004**: combined-file internal authoring rules (spec clause structure, file shape, nested ADR body, anchors, lifecycle, derivatives) — AC008 §VIII “Option B identity refocus”.
* **STD-009**: `STD` registry semantics (adoption contract, precedence/variance, index schema/body construction, migration tolerance) with subclauses `CLAUSE-004A..004E`.

**Deferred items register (AC008 §X) that stress the boundary**:
1. Self-hosted STD exception clause (STD-009 amendments)
2. Concept STD Index schema governance ambiguity (Authority STD + Canonical Path columns)
3. SPS `Governed By` column gap (STD-009-CLAUSE-004A compliance)
4. STD-004 `Adopts = —` exception formalization
5. Possible migration of STD-004 CLAUSE-014 into STD-009
6. STD-004 retitle consideration
7. First-class review of STD-005 and STD-009 using STD-004 as exemplar baseline

Industry benchmark:
* ISO/IEC and W3C demonstrate modular governance: drafting/style guidance is typically separated from process/governance registry rules (a strong prior in favor of separation). [1][4]

#### B. Analysis
**Options matrix (score 1–5; higher is better)**

| Criteria | Merge (`STD-004+STD-009`) | Separate-with-clarified-interfaces | Notes |
|:--|--:|--:|:--|
| Cohesion (single “meta-STD”) | 4 | 3 | Merge reduces doc hopping |
| Modularity / independent evolution | 2 | 5 | Separation mirrors industry modular governance |
| Blast radius of change | 2 | 4 | Merge increases change surface per revision |
| Cognitive load for authors/reviewers | 3 | 4 | Separation with explicit interface reduces confusion |
| Deferred items resolution clarity (AC008 §X) | 3 | 4 | Most deferred items are interface clarifications, not a need to merge |
| Scaling to 15–25 STDs | 2 | 5 | Modular docs generally scale better |

**Recommendation**: **Keep separate** (`STD-004` and `STD-009`), but formalize the interface:
1) Add an explicit “Boundary & Interfaces” section in each STD:
   - what it owns,
   - what it MUST NOT own,
   - which cross-references are stable and required.
2) Resolve the deferred items via targeted amendments (primarily in STD-009 for registry exceptions and in Concept/SPS hosting standards for index schemas), not by merging.

**Sensitivity analysis (growth)**:
* If T102 grows to 15–25 STDs, merging increases review surface area and makes “small registry changes” and “small drafting changes” co-evolve, increasing operational friction. Separation with explicit interfaces becomes more valuable as scale grows.
* A merge becomes more attractive only if empirical evidence shows that (a) interface clarifications do not reduce confusion, and (b) most changes always affect both docs together (highly coupled change frequency).

**Deferred-items mapping (resolution path)**

| AC008 §X item | Merge impact | Separate-with-interface impact | Recommendation |
|:--|:--|:--|:--|
| 1. Self-hosted STD exception | Would live in merged doc anyway | Add explicit STD-009 clause for self-hosted standards | Separate |
| 2. Concept STD index schema governance | Merge doesn’t decide hosting authority | Specify index schema authority explicitly (likely STD-009 + hosting rules) | Separate |
| 3. SPS `Governed By` gap | Still needs SPS change | Treat as downstream artifact conformance fix driven by STD-009 | Separate |
| 4. `Adopts = —` exception | Could be in merged doc | Add exception clause and migration posture in STD-009 | Separate |
| 5. CLAUSE-014 migration question | Merge sidesteps “migration” but not ownership | Decide ownership: lifecycle/promotion guidance likely fits registry/process side (STD-009) | Separate |
| 6. STD-004 retitle | Independent of merge | Apply once stable; consider anchor impact | Separate |
| 7. First-class review of STD-005/009 | Still required | Still required; use STD-004 as drafting exemplar | Separate |

#### C. Governance Implication
* Keep the modular split, but eliminate “boundary-by-narrative” by encoding the interface explicitly as normative text, with stable cross-references.

---

### Topic 9: Recommendations for Exemplar Strengthening
**Objective**: Produce prioritized recommendations compatible with the approved R2 baseline, marking each recommendation as validated/enhanced/new and assigning an implementation phase.

#### A. Evidence & Forensics
Recommendations are grounded in Topics 1–8 evidence, AC008 decisions (§VIII–§X), and external benchmarks emphasizing controlled vocabulary, boundary clarity, and conformance discipline. [1][2][3][4][5][6][7][8]

#### B. Analysis
**Prioritized recommendations**

1) **Enforce “anchor + named subclauses” for multi-obligation clauses across the entire T102 STD corpus**  
   - R2 alignment: **validated + enhanced** (expand beyond STD-004)  
   - Phase: **AC009 (STD-004) + ST002 follow-on (other STDs)**  
   - Impact: makes clause references precise and audit/test friendly.

2) **Standardize normative vocabulary style (reduce MUST/SHALL mixing)**  
   - R2 alignment: **new** (R2 focuses on clause structure, not vocabulary consistency)  
   - Phase: **ST002** (update `T102-CON-009` and enforce in STD templates)  
   - Industry basis: controlled verbal forms or controlled BCP 14 keywords are consistently emphasized. [1][2][5]

3) **Add an explicit “Normative vs Informative Boundary” rule set** (including “no BCP 14 keywords in informative sections”)  
   - R2 alignment: **enhanced** (supports combined-file model and prevents leakage)  
   - Phase: **AC009**  
   - Industry basis: boundary clarity is a repeated drafting principle (W3C/ISO style). [1][6]

4) **Formalize STD-004 ↔ STD-009 interface contract (keep separate)**  
   - R2 alignment: **new**  
   - Phase: **ST002**  
   - Impact: resolves deferred items #1–#5 without merging.

5) **Add a “Conformance clause pattern” (or required conformance subclause) to the combined-file authoring rules**  
   - R2 alignment: **new**  
   - Phase: **ST002**  
   - Industry basis: conformance is first-class in W3C/OASIS ecosystems. [4][7]

6) **Make derivative traceability mechanically checkable** (guideline/template must cite governing clause IDs that actually contain the rule)  
   - R2 alignment: **validated** (matches AC008 leakage diagnosis)  
   - Phase: **AC009** (close leak by moving naming/location rules into STD-004 or by correcting claims)  
   - Impact: prevents “derivative creates new law” anti-pattern.

7) **Clarify lifecycle-to-registry mapping** (Accepted/Amended/Deprecated ↔ Effective/Supersedes/Verification fields)  
   - R2 alignment: **enhanced**  
   - Phase: **ST002**  
   - Impact: improves review and drift control.

#### C. Governance Implication
* Treat recommendations 1–3 as exemplar hardening requirements (AC009). Treat 4–7 as system-wide standards governance improvements (ST002).

---

## IV. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-007-ISSUE-001` | Industry source accessibility | Some standards-body drafting manuals may be paywalled or superseded; claims must be qualified based on accessible versions and limitations | `LLM_Researcher` | `RESOLVED` | `MEDIUM` | 2026-02-12 | Accessible sources were located for ISO/IEC Directives Part 2 (ANSI share), IETF RFC 2119/8174, W3C Process/Style, OASIS guidance, and an accessible copy of the IEEE Standards Style Manual (2009). Remaining limitation: documents may have newer editions; this report is time-locked to the cited versions. | 2026-02-14 |
| `T102-RES-007-ISSUE-002` | STD-004/STD-009 boundary definition precision | Boundary was narrative; merger evaluation requires explicit boundary definition and criteria-before-scoring | `LLM_Researcher` | `RESOLVED` | `HIGH` | 2026-02-12 | Boundary and interface criteria defined in Topic 8 (evidence-based boundary + options matrix + deferred-items mapping). | 2026-02-13 |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-007-RISK-001` | Benchmark scope inflation | 5 bodies × many dimensions can expand beyond decision usefulness | `LLM_Researcher` | `MITIGATED` | `MEDIUM` | 2026-02-12 | ISO/IEC + IETF treated as primary; IEEE/W3C/OASIS used to validate core gaps and conformance boundary patterns only. | 2026-02-13 |
| `T102-RES-007-RISK-002` | R2 proposal obsolescence risk | Benchmarking could reveal issues beyond R2 scope | `LLM_Researcher` | `MONITORED` | `MEDIUM` | 2026-02-12 | Recommendations are framed as R2 enhancements, not a replacement; AC009 remains the integration surface for changes to STD-004. | — |
| `T102-RES-007-RISK-003` | Merger evaluation bias | Current separation could bias scoring | `LLM_Researcher` | `MITIGATED` | `LOW` | 2026-02-12 | Criteria defined before scoring; sensitivity analysis included; deferred items mapping forces concrete resolution paths for both options. | 2026-02-13 |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `T102-STD-004` | `## Specification` (all CLAUSE bodies) | Apply R2 “anchor + named subclauses” refactor; add explicit boundary + boundary hygiene rules (normative/informative separation) | Topics 1, 3, 7, 9 |
| `T102-CON-009` | Normative keyword style | Make drafting vocabulary decision explicit; define preferred keyword set; discourage mixing MUST/SHALL | Topic 2, 4–6, 7, 9 |
| `T102-STD-009` | Boundary & exceptions | Add self-hosted STD exception clause; formalize `Adopts = —` exception; clarify Concept index schema authority | Topic 8 + AC008 §X mapping |
| `guideline_standard_specs.md` | Locked rules section | Remove/replace claims “per STD-004” unless actually governed; or move governance into STD-004 to close leakage | Topic 2 |

---

## VI. SOURCE MATERIAL

* **Brief Version**: `prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102-RES-007_standards-authoring-methodology-benchmarking.md` (v1.0.0, 2026-02-12)
* **Code Commit/Tag**: —
* **Files Cited (T102 internal)**:
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-001_consultancy-operating-model.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-002_canonical-yaml-header.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-003_explicit-inheritance-model.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_specification-standard-and-guideline.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-007_issues-risks-index.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-008_organisation-baseline-index.md`
  * `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md`
  * `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (contains `T102-CON-009`)
  * `prompt/templates/consultant/standards/guideline_standard_specs.md`
  * `prompt/templates/consultant/standards/template_standard_specs.md`
  * `prompt/artifacts/tasks/T102/consultant/workspace/analysis/analysis_T102-CWD_PH001-ST001-AC008_std-004-self-compliance-audit.md`
  * `prompt/artifacts/tasks/T102/consultant/workspace/proposal/proposal_T102-CWD_PH001-ST001-AC008_r2-refactor-plan.md`
* **External Sources**:
  * [1] ISO/IEC Directives, Part 2 — Principles and rules for the structure and drafting of ISO and IEC documents (2021) — https://share.ansi.org/Shared%20Documents/Standards%20Activities/NCSCI/ISO_IEC_Directives_Part_2__2021.pdf
  * [2] RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels — https://www.rfc-editor.org/rfc/rfc2119
  * [3] RFC 8174 — Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words — https://www.rfc-editor.org/rfc/rfc8174
  * [4] W3C Process Document — https://www.w3.org/policies/process/
  * [5] IEEE Standards Style Manual (2009) — https://grouper.ieee.org/groups/nescom/msc/IEEE_Standards_Style_Manual_2009.pdf
  * [6] W3C Manual of Style — https://www.w3.org/2001/06/manual/
  * [7] OASIS Conformance Guidelines — https://docs.oasis-open.org/templates/TCHandbook/ConformanceGuidelines.html
  * [8] OASIS Interoperability Guidelines — https://www.oasis-open.org/policies-guidelines/interoperability-guidelines/
