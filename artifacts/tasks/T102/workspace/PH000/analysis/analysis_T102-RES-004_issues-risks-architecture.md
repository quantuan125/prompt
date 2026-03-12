---
artifact_type: 'ANALYSIS'
initiative_id: 'T102'
research_id: 'T102-RES-004'
version: '1.1.0'
date: '2026-02-09'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Integration impact analysis for T102-RES-004 (Issues & Risks Architecture) — TK003 deliverable for T102-PH001-ST004-AC001'
source_report: 'prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md'
source_brief: 'prompt/artifacts/tasks/T102/research/T102-RES-004/brief_T102-RES-004_issues-risks-architecture.md'
---

# INTEGRATION ANALYSIS: T102-RES-004 — Issues & Risks Hosting Architecture

## I. EXECUTIVE SUMMARY

**Purpose**: Translate the accepted `T102-RES-004` research report findings into actionable integration recommendations for the T102 initiative. This analysis:

1. Presents the **key research findings** with governance implications highlighted
2. Produces the **`T102-STD-007` delta list** (clause-level amendment recommendations)
3. Assesses **impact on existing SSOT materials** (SPS, Request, Concept)
4. Maps **downstream effects** on T102B (REQUEST epic) development — specifically `T102B-PH001-ST001-AC002.1`
5. Provides a **T102B communication message** for the consultant owning that epic's development
6. Produces the **SSOT alignment checklist** required by TK003

**Report Verdict (accepted)**: PIVOT RECOMMENDED — adopt SPS-only hosting as **baseline** architecture; remove Feature-level I&R from Request by default; extend `T102-STD-007` with hosting, filtering, promotion, and staleness clauses. Pattern (c) — Concept aggregation — is preserved as a **conditional enhancement** pending `T102-RES-006` (ST004-AC003) viability verdict.

**Decision Ownership**: All recommendations in this analysis require Client approval (GATE-003) before downstream implementation.

---

## II. KEY RESEARCH FINDINGS — PRESENTATION & IMPLICATIONS

### Finding 1: Current Three-Tier Hosting Is Not Operating as Designed

**What the research found**: I&R tables exist at three scope levels (Initiative in SPS, Epic in SPS dossiers, Feature in Request Section H), but the system is not operating as a true three-tier architecture. Feature-level I&R is sparse (only `request_T102B1-RST.md` has it) and contains meta-authoring/process items rather than feature-specific requirements risks.

**Quantitative evidence**:

| Scope | Artifact | Issues (total/active) | Risks (total/active) | Avg Active Age (days) | Staleness Signal |
|:------|:---------|:---------------------|:---------------------|:---------------------|:-----------------|
| Initiative | SPS §III.B.10 | 7 / 7 | 4 / 4 | 98.4 | Yes (>90d OPEN) |
| Epic T102A | SPS §III.C.1.ix | 3 / 0 | 4 / 4 | 128.0 | Yes (>120d MONITORED) |
| Epic T102B | SPS §III.C.2.x | 8 / 4 | 4 / 3 | 23.0 | No (fresh) |
| Epic T102C | SPS §III.C.3.ix | 5 / 0 | 3 / 0 | — | No (closed/mitigated) |
| Feature T102B1 | Request §H | 2 / 2 | 1 / 1 | 3.0 | No (but misclassified) |

**Implication**: The Feature-level items (`T102B1-ISSUE-001`, `T102B1-ISSUE-002`, `T102B1-RISK-001`) are governance/template concerns that belong at Epic scope. This validates D2's original instinct to remove Feature-level I&R, but the research provides the evidence and architectural framework D2 lacked.

**Implication for initiative**: The staleness signal at Initiative (98.4d avg) and T102A Epic (128d avg) levels indicates a governance hygiene gap that will compound as the initiative scales. A staleness review policy is needed regardless of hosting architecture choice.

---

### Finding 2: `T102-STD-007` Governs Form, Not Architecture

**What the research found**: `T102-STD-007` has 9 strong clauses covering schemas, enums, ID rules, and closure coupling — but is **silent on 5 critical architectural questions**:

| Gap | Current Status | Impact |
|:----|:--------------|:-------|
| Default hosting placement (which artifacts carry I&R) | Unspecified | Cannot enforce "remove-by-default" without amendment |
| Feature-level I&R disposition | Unspecified | D2 cannot be implemented without normative backing |
| Content filtering (Issue/Risk vs ASSUM/CON/DEP/STD) | Partial (`T102-STD-005` implied) | Feature Requests become sinks for misclassified governance items |
| Feature→Epic promotion | Unspecified (only Epic→Initiative in CLAUSE-009) | No pathway to safely remove Feature I&R without losing concerns |
| Staleness detection | Unspecified | "Infinite MONITORED backlog" behavior at Initiative/Epic level |

**Implication**: `T102-STD-007` requires a targeted amendment to become decision-ready for the hosting architecture question. The amendment scope is bounded (4 delta categories) and does not require rewriting existing clauses — it extends them.

---

### Finding 3: Industry Benchmarking Supports Register-Based Pattern Over Per-Spec Embedding

**What the research found**: PRINCE2, BABOK, SAFe, and ISO 29148 public materials consistently describe Issues and Risks as managed via **registers/boards** with lifecycle processes, not as default sections inside each requirements specification.

**Key references** (public, qualified):
- PRINCE2: Issue Register and Risk Register as project management products
- BABOK: "Assess Risks" as business analysis work, not per-spec embedded section
- SAFe: PI Planning "risk board" with ROAM categories
- ISO 29148: Requirements engineering standard; public materials do not position I&R logs inside each spec

**Implication**: The "remove Feature-level I&R from Request by default" recommendation aligns with industry norms. Feature-level Requests are requirements specifications; Issues & Risks belong in project/initiative-level registers (SPS in our architecture).

---

### Finding 4: Recommended Default Architecture — SPS-Only with Hybrid Exception

**What the research found**: Five candidate hosting patterns were evaluated with equal-weight scoring across 5 criteria:

| Pattern | Score (max 25) | Verdict |
|:--------|:--------------:|:--------|
| **(a) SPS-only** (Initiative + Epic in SPS; no Feature I&R by default) | **19** | **GO (Recommended default)** |
| (b) SPS+Request (current three-tier) | 14 | NO-GO as default |
| (c) SPS+Concept (aggregated register) | 19 | PIVOT / Conditional (pending RES-007) |
| (d) Hybrid thresholds (Feature I&R only for complex/high-risk) | 18 | GO (secondary / exception path) |
| (e) Dedicated register (standalone artifact) | 19 | PIVOT / Optional |

**Recommended architecture**:
- **Default**: Pattern (a) — SPS-only hosting at Initiative + Epic scopes
- **Exception path**: Pattern (d) — Feature-level I&R permitted only for complex/high-risk features via explicit threshold criteria
- **Future enhancement**: Pattern (c) — Concept aggregated register, contingent on `T102-RES-007` viability verdict

**Implication**: This architecture simplifies governance (fewer surfaces to maintain), reduces LLM context noise in Request artifacts, and aligns with the "link-don't-duplicate" principle of `T102-STD-003`. The exception path preserves flexibility for genuinely high-risk features.

---

### Finding 5: Lifecycle and Promotion Rules Need Extension

**What the research found**: Current `T102-STD-007-CLAUSE-009` only covers Epic→Initiative promotion with SHOULD language. The research proposes:

- **Upward promotion** (Feature→Epic, Epic→Initiative): Create item at higher scope, close lower-scope item with reference
- **De-dup enforcement**: Highest-scope active item is canonical; lower-scope items closed or scoped as local deltas
- **Downward monitoring**: Initiative risk → Epic monitoring items (downstream references upstream; upstream MUST NOT reference downstream per `T102-STD-003`)
- **Staleness policy**: OPEN/MONITORED items >90 days trigger mandatory review touch

**Implication**: These rules are critical for making "remove-by-default at Feature scope" operational. Without Feature→Epic promotion rules, removing Feature I&R could cause concerns to be silently lost. The staleness policy directly addresses the 98-128 day stale items observed in SPS.

---

### Finding 6: Content Filtering Decision Tree

**What the research found**: A 6-step prescriptive decision tree distinguishes Issues/Risks from other governance categories (ASSUM, CON, DEP, STD, ADR, IG, NOTE):

1. Stable obligation/rule? → STD/RID/ADR (not Issue/Risk)
2. Current known problem blocking progress? → **Issue**
3. Potential negative event with uncertain occurrence? → **Risk**
4. Unvalidated belief? → **Assumption** (ASSUM)
5. External prerequisite? → **Dependency** (DEP)
6. Non-normative guidance? → IG/INT/NOTE

**Worked examples from current inventory**:
- `T102-ISSUE-001 (Planner Handoff Schema)`: Issue now → target state is Interface (IF) once defined
- `T102-ISSUE-004 (IDs Promotion Protocol)`: Issue now → target state is STD/ADR once formalized
- `T102B1-ISSUE-002 (Classification markers)`: Feature Issue → should be Epic Issue (promote to `T102B-ISSUE-###`)
- `T102A-RISK-003 (Document Bloat)` + `T102C-RISK-001 (Context Overload)`: Cross-epic risks → candidates for Initiative-level aggregation/linkage

**Implication**: This filtering tree provides the operational "how" for authors deciding where items belong. It also reveals that several current Initiative-level Issues are tracking gaps that should eventually become STD/IF/ADR artifacts — the Issue tracks the gap until the formal artifact is produced.

---

## III. `T102-STD-007` DELTA LIST (Recommendations-Only)

The following amendments are recommended for `T102-STD-007`. These are **recommendations-only** — actual clause drafting is downstream work.

### Delta 1: CLAUSE-001 Amendment — Default Hosting Architecture

**Current state**: "MUST be available for each scope and use the exact heading `Issues & Risks` across all artifacts."

**Recommended amendment**:
- Clarify that I&R sections are **mandatory at Initiative and Epic scopes** (in SPS)
- Clarify that I&R sections are **removed by default at Feature scope** (in Request artifacts)
- Define an **explicit exception mechanism**: Feature-level I&R MAY be included when a feature meets defined complexity/risk threshold criteria (hybrid exception per pattern d)
- When present at Feature scope, the section MUST conform to the same deterministic schema (existing CLAUSE-002 through CLAUSE-008)

**Rationale**: Research Finding 4 (options matrix), Finding 3 (industry benchmarking), Finding 1 (current state misclassification evidence).

### Delta 2: CLAUSE-009 Extension — Multi-Scope Promotion & De-Dup

**Current state**: Epic→Initiative promotion only; SHOULD language; no Feature→Epic pathway.

**Recommended amendment**:
- Add **Feature→Epic promotion rules**: If a Feature issue/risk impacts Epic success (multi-feature, template/standard compliance, or epic gates), create an Epic item and close the Feature item with reference
- Strengthen promotion from SHOULD to **MUST** when impact crosses scope boundaries
- Add **de-dup enforcement**: Highest-scope active item is canonical; lower-scope items MUST be either (a) closed with promoted ID reference, or (b) strictly scoped as local deltas
- Add **downward monitoring guidance**: When Initiative risk requires local monitoring, Epic-level items MAY be created that reference the Initiative item (downstream→upstream allowed; upstream MUST NOT reference downstream per `T102-STD-003`)

**Rationale**: Research Finding 5 (lifecycle rules), Finding 1 (no current de-dup enforcement).

### Delta 3: New Clause — Content Filtering Criteria

**Recommended new clause** (e.g., `T102-STD-007-CLAUSE-010`):
- Define prescriptive content filtering criteria distinguishing Issue/Risk from ASSUM, CON, DEP, STD, ADR, IG, INT, NOTE
- Include the 6-step decision tree from research Finding 6
- Mandate that Feature-level Items failing the filtering test MUST be promoted or reclassified before Feature Request approval gate
- Note that Issues/Risks tracking gaps that resolve into formal artifacts (STD/IF/ADR) SHOULD be closed with reference to the produced artifact

**Rationale**: Research Finding 6 (decision tree + worked examples), Finding 1 (misclassification evidence at Feature scope).

### Delta 4: New Clause — Staleness Detection Policy

**Recommended new clause** (e.g., `T102-STD-007-CLAUSE-011`):
- OPEN (Issues) or MONITORED (Risks) items older than **90 days** without status change MUST trigger a review touch
- Review touch options: update status, add/refresh resolution/mitigation notes, or explicitly DEFER/ACCEPT with rationale and governing IDs
- Staleness review cadence SHOULD align with initiative-level review cycles

**Rationale**: Research Finding 1 (98-128 day stale items in SPS), Finding 5 (staleness policy proposal).

---

## IV. IMPACT ASSESSMENT — EXISTING MATERIALS

### A. Impact on `T102-STD-007` (Issues & Risks Index)

| Impact Area | Severity | Action Required |
|:------------|:---------|:----------------|
| CLAUSE-001 amendment (hosting default) | HIGH | Amend to specify "remove-by-default at Feature scope" with exception mechanism |
| CLAUSE-009 extension (promotion rules) | HIGH | Extend to cover Feature→Epic, de-dup enforcement, downward monitoring |
| New CLAUSE-010 (content filtering) | MEDIUM | Author new clause with decision tree |
| New CLAUSE-011 (staleness policy) | MEDIUM | Author new clause with 90-day threshold |

**When**: Downstream of GATE-003 approval. Clause drafting is a separate activity (not in ST004 scope per DEC004).

### B. Impact on SPS (`sps_T102-CONSULTANT.md`)

| Impact Area | Severity | Action Required |
|:------------|:---------|:----------------|
| Initiative I&R (§III.B.10): 7 stale OPEN issues | MEDIUM | Trigger staleness review per proposed CLAUSE-011; update status or defer with rationale |
| T102A Epic I&R: 4 MONITORED risks >120 days | MEDIUM | Trigger staleness review; assess whether T102A risks are still active or should be ACCEPTED/CLOSED |
| T102B Epic I&R: Feature items to be promoted | HIGH | Promote `T102B1-ISSUE-001`, `T102B1-ISSUE-002`, `T102B1-RISK-001` to `T102B-ISSUE-###` / `T102B-RISK-###` (already planned in `T102B-PH001-ST001-AC002.1-TK014`) |
| Cross-epic de-dup: `T102A-RISK-003` (Document Bloat) + `T102C-RISK-001` (Context Overload) | LOW | Assess for Initiative-level aggregation or explicit linkage; not blocking |
| Research Register: `T102-RES-004` registration | MEDIUM | TK004 registers RES-004 in SPS Research table (pending) |

### C. Impact on Request Artifacts (`request_T102B1-RST.md`)

| Impact Area | Severity | Action Required |
|:------------|:---------|:----------------|
| Section H removal | HIGH | Remove Section H "Issues & Risks" from Request — **already planned in `T102B-PH001-ST001-AC002.1-TK005`** |
| Feature item promotion | HIGH | Promote T102B1 items to T102B Epic scope — **already planned in `T102B-PH001-ST001-AC002.1-TK014`** |
| Template implications | MEDIUM | RST template (AC003) MUST NOT include a default I&R section; may include instructional comment noting the exception mechanism |

**Key observation**: AC002.1 already planned TK005 (Section H removal) and TK014 (item promotion) based on D2/D8 decisions. RES-004 findings **validate and strengthen** these planned actions by providing evidence-based rationale and the architectural framework (promotion rules, filtering criteria) that D2 lacked.

### D. Impact on Concept Artifact (`concept_T102-CONSULTANT.md`)

| Impact Area | Severity | Action Required |
|:------------|:---------|:----------------|
| Concept as I&R aggregation surface (pattern c) | LOW | **Deferred** — contingent on `T102-RES-007` Concept viability verdict |
| No Concept-hosted I&R register exists today | — | No immediate action; RES-007 will determine if one should be created |

### E. Impact on `T102-STD-005` (ID Specification & Rules)

| Impact Area | Severity | Action Required |
|:------------|:---------|:----------------|
| Optional: Issue/Risk → target category promotion note | LOW | Consider adding non-normative guidance note to `T102-STD-005` for Issue/Risk → STD/ADR/RID promotion path |

### F. Impact on `T102-STD-003` (Explicit Inheritance Model)

| Impact Area | Severity | Action Required |
|:------------|:---------|:----------------|
| Directionality constraint confirmed | — | No amendment needed; research confirms downstream→upstream referencing is allowed, upstream→downstream is forbidden |

---

## V. DOWNSTREAM IMPACT — T102B EPIC DEVELOPMENT

### A. Impact on `T102B-PH001-ST001-AC002.1` (RST Specification Remediation)

AC002.1 is the most directly affected downstream activity. The following AC002.1 tasks are **unblocked or validated** by RES-004 findings:

| AC002.1 Task | RES-004 Impact | Status Change |
|:-------------|:---------------|:-------------|
| **T102B-PH001-ST001-AC002.1-TK005** (Remove Section H "Issues & Risks" from Request) | **VALIDATED** — RES-004 confirms remove-by-default architecture with industry evidence. D2/D8 decisions now have research backing. | Ready to execute |
| **T102B-PH001-ST001-AC002.1-TK006** (Insert new Section H "Feature Guidance & Notes") | **No change** — replacement section is independent of I&R hosting decision | Ready to execute |
| **T102B-PH001-ST001-AC002.1-TK014** (Promote T102B1 items to Epic scope in SPS) | **VALIDATED + ENHANCED** — RES-004 provides promotion rules (Finding 5) and filtering criteria (Finding 6) for how to classify promoted items. The promotion should apply the content filtering decision tree to determine if items remain as Issues/Risks at Epic scope or should be reclassified. | Ready to execute with enhanced guidance |
| **T102B-PH001-ST001-AC004-TK018** (Absorb T102-RES-004 report findings) | **UNBLOCKED** — Previously marked "DEFERRED — blocked on T102-PH001-ST004 completion". With GATE-002 passed and this analysis produced, the blocking condition is resolved. | Unblocked; can proceed when T102B-PH001-ST001-AC004 begins |

### B. Impact on `T102B-PH001-ST001-AC003` (RST Template Formalization)

| AC003 Task | RES-004 Impact |
|:-----------|:---------------|
| **T102B-PH001-ST001-AC003-TK009** (Author Section H "Feature Guidance & Notes") | **Confirmed** — template Section H should be "Feature Guidance & Notes" (IG/INT/NOTE), NOT "Issues & Risks". RES-004 validates this design decision. |
| **T102B-PH001-ST001-AC003 (Template-wide)** | The RST template MUST NOT include a default I&R section. An instructional comment MAY note the hybrid exception: "Feature I&R section MAY be included if feature meets complexity/risk threshold per `T102-STD-007`; otherwise, issues and risks are managed at Epic scope in SPS." |

### C. Impact on `T102B-PH001-ST001-AC004` (RST Self-Validation & Retrofit)

| AC004 Task | RES-004 Impact |
|:-----------|:---------------|
| **T102B-PH001-ST001-AC004-TK009** (Retrofit Section H — formerly "Issues & Risks") | **Scope change** — Section H is now "Feature Guidance & Notes", not I&R. Retrofit populates IG/INT/NOTE content. |
| **T102B-PH001-ST001-AC004-TK018** (Absorb RES-004 findings) | **Unblocked** — the blocking dependency is resolved. Absorption means: (1) confirm Section H removal is applied, (2) verify promoted items appear in SPS T102B dossier, (3) document the exception mechanism in template instructions. |

---

## VI. CROSS-RESEARCH DEPENDENCIES

| Research | Overlap Zone | Reconciliation Approach |
|:---------|:-------------|:-----------------------|
| **T102-RES-007** (Concept Role + Dynamic SSOT Registers) | Pattern (c) — Concept as I&R aggregation surface | RES-004 recommends pattern (c) as PIVOT/conditional. RES-007 will determine Concept viability. If RES-007 confirms Concept as a dynamic registers surface, pattern (c) may be adopted as an enhancement. If RES-007 finds Concept unsuitable, pattern (a) remains the sole default. |
| **T102-RES-005** (Inherited Considerations Viability) | SPS bloat reduction | RES-004's staleness policy and promotion/de-dup rules reduce I&R contribution to SPS bloat. RES-005 may recommend further SPS slimming through inheritance model changes. Findings are complementary. |
| **T102-RES-006** (Research Index Placement & Governance) | Register placement patterns | RES-004's recommendation of SPS-only hosting for I&R is analogous to Research register placement decisions. Consistent placement principles should emerge across both studies. |

### AC003 Brief Ingestion Directive (from RES-004)

The following I&R-specific evaluation topics MUST be included in the `T102-PH001-ST004-AC003` (RES-006) research brief, driven by RES-004 findings and the R3 conditional deferral:

1. **Pattern (c) viability assessment**: Evaluate whether Concept can serve as an I&R aggregation/dashboard surface — what would the structural design look like (cross-scope summary view, staleness indicators, promotion trails, cross-epic aggregation), what governance rules would apply, and what are the trade-offs vs SPS-only hosting (pattern a)?
2. **Register family scoping for I&R**: If Concept hosts dynamic registers, where does I&R sit relative to other register families (STD indexes, research registers, workscope registers)? Is I&R aggregation a separate Concept section or part of a unified register surface?
3. **STD-007 interaction clause**: If pattern (c) is adopted, what `T102-STD-007` amendment language is needed to define how Concept aggregation interacts with SPS canonical hosting? Specifically: how does a Concept aggregation layer satisfy the "must be available for each scope" reading without violating `T102-STD-003` directionality? (Ref: RES-004 Topic 2 governance implication — "I&R pointer/aggregation pattern" needed.)
4. **Staleness dashboard feasibility**: Can Concept provide the cross-scope staleness visibility that RES-004 identified as needed (Finding 1: 98-128 day stale items; Finding 5: staleness policy)? What is the maintenance cost of a Concept-hosted staleness dashboard vs a purely SPS-based staleness review cadence?

These topics ensure AC003's brief explicitly absorbs RES-004's open questions regarding pattern (c) rather than rediscovering them.

---

## VII. SSOT ALIGNMENT CHECKLIST

This checklist verifies alignment between RES-004 recommendations and existing SSOT state. All items must be addressed (either implemented or explicitly deferred) before GATE-003 sign-off.

| # | Check | Current State | Required State | Status | Owner |
|:--|:------|:-------------|:---------------|:-------|:------|
| 1 | `T102-STD-007` CLAUSE-001 specifies default hosting | Unspecified (implicit "all scopes") | Explicit "remove-by-default at Feature scope" | Pending STD amendment | LLM_Consultant |
| 2 | `T102-STD-007` CLAUSE-009 covers Feature→Epic promotion | Only Epic→Initiative | Extended to cover Feature→Epic + de-dup | Pending STD amendment | LLM_Consultant |
| 3 | Content filtering criteria exist | None (partial in STD-005) | New CLAUSE-010 with decision tree | Pending STD amendment | LLM_Consultant |
| 4 | Staleness policy exists | None | New CLAUSE-011 with 90-day threshold | Pending STD amendment | LLM_Consultant |
| 5 | `request_T102B1-RST.md` Section H removed | Section H present (`[O]`) | Section H removed; items promoted | Planned (T102B-PH001-ST001-AC002.1-TK005 / T102B-PH001-ST001-AC002.1-TK014) | T102B LLM_Consultant |
| 6 | RST template excludes default I&R section | Template not yet authored | Template Section H = "Feature Guidance & Notes" with instructional comment on exception | Planned (T102B-PH001-ST001-AC003) | T102B LLM_Consultant |
| 7 | T102B1 items promoted to Epic scope | Items in Request Section H | Items promoted to SPS T102B dossier | Planned (T102B-PH001-ST001-AC002.1-TK014) | T102B LLM_Consultant |
| 8 | RES-004 registered in SPS Research table | Not registered | Registered per `T102-STD-006` | Pending (TK004) | LLM_Consultant |
| 9 | RES-004 registered in Concept Research Register (E.3) | Not registered | Registered per `T102-STD-006` | Pending (TK004) | LLM_Consultant |
| 10 | Initiative I&R staleness review triggered | 7 OPEN issues avg 98d; 4 MONITORED risks | Staleness review performed | Deferred to post-CLAUSE-011 | LLM_Consultant |
| 11 | Cross-epic risk de-dup assessed | `T102A-RISK-003` / `T102C-RISK-001` unlinked | Assessed for aggregation/linkage | Deferred (non-blocking) | LLM_Consultant |

---

## VIII. T102B COMMUNICATION MESSAGE

The following communication is directed to the **T102B LLM_Consultant** who owns `T102B-PH001-ST001` (RST Development stream) execution.

---

### Communication: RES-004 Research Findings — Impact on T102B-PH001-ST001

**From**: T102 Initiative LLM_Consultant (ST004 research program)
**To**: T102B LLM_Consultant (ST001 RST development)
**Date**: 2026-02-09
**Subject**: T102-RES-004 Report Accepted — Unblocking AC002.1 and Informing AC003/AC004

**Summary**:

The `T102-RES-004 (Issues & Risks Architecture)` research report has been accepted (GATE-002 passed, 2026-02-09). The research validates and strengthens the D2/D8 decisions already captured in your AC002 re-review session. Below are the key impacts on your stream.

**1. AC002.1 — Validated Tasks**:

- **T102B-PH001-ST001-AC002.1-TK005 (Remove Section H)**: CONFIRMED. Research provides evidence-based rationale and industry benchmarking (PRINCE2, BABOK, SAFe, ISO 29148) supporting "remove-by-default at Feature scope." You may proceed with removal as planned.
- **T102B-PH001-ST001-AC002.1-TK014 (Promote Feature items to Epic scope)**: CONFIRMED WITH ENHANCEMENT. When promoting `T102B1-ISSUE-001`, `T102B1-ISSUE-002`, and `T102B1-RISK-001` to Epic scope, apply the RES-004 content filtering decision tree to determine whether each item should remain classified as Issue/Risk at Epic scope or be reclassified:
  - `T102B1-ISSUE-001 (Story Index schema alignment)`: Likely remains an Epic Issue (current gap blocking standard compliance)
  - `T102B1-ISSUE-002 (Classification marker standardization)`: Likely remains an Epic Issue (current gap); target state may be STD/ADR once standardized
  - `T102B1-RISK-001 (Request self-hosting drift)`: Remains a Risk (potential negative event with uncertain occurrence)

**2. AC003 — Template Implications**:

- The RST template (`template_request_structural.md`) MUST NOT include a default "Issues & Risks" section
- Section H should be "Feature Guidance & Notes" (IG/INT/NOTE) per your D9 decision
- An instructional comment MAY be included noting the hybrid exception: Feature I&R is permitted only when a feature meets complexity/risk threshold criteria per `T102-STD-007` (pending amendment)

**3. AC004 — Unblocked Task**:

- **T102B-PH001-ST001-AC004-TK018 (Absorb T102-RES-004 findings)**: Previously DEFERRED, now UNBLOCKED. Absorption scope:
  - Verify Section H removal is applied in the retrofitted Request
  - Verify promoted items appear in SPS T102B dossier with supersession notes
  - Document the exception mechanism in template instructions (if not already done in AC003)

**4. Reference Materials**:

- Research report: `prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md`
- This integration analysis: `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md`
- Governing notes: `prompt/artifacts/tasks/T102/workspace/PH001/ST004/AC001/notes_T102-PH001-ST004-AC001.md` (Session 4: GATE-001/GATE-002)

**5. No Action Required From You Now**:

The `T102-STD-007` amendment (Deltas 1-4) is downstream work managed at initiative scope. Your AC002.1 tasks (`T102B-PH001-ST001-AC002.1-TK005`, `T102B-PH001-ST001-AC002.1-TK014`) can proceed using the existing D2/D8 decisions with RES-004 as strengthening evidence. The STD amendment will formalize what your stream is already implementing.

---

## IX. RECOMMENDATIONS FOR CLIENT DECISION

The following recommendations are submitted for GATE-003 (Client sign-off on integration recommendations):

| # | Recommendation | Priority | Dependencies |
|:--|:---------------|:---------|:-------------|
| R1 | Adopt SPS-only (pattern a) as the **baseline** I&R hosting architecture for T102. Pattern (c) — Concept aggregation — is preserved as a conditional enhancement pending RES-006 (ST004-AC003). | HIGH | None |
| R2 | Adopt hybrid threshold (pattern d) as the defined exception path for complex/high-risk features | HIGH | R1 |
| R3 | Defer Concept aggregation (pattern c) pending `T102-RES-007` viability verdict | MEDIUM | `T102-RES-007` |
| R4 | Commission `T102-STD-007` amendment (Deltas 1-4) as downstream work — separate activity or incorporated into existing standards maintenance | HIGH | R1 approved |
| R5 | Unblock `T102B-PH001-ST001-AC002.1-TK005` / `T102B-PH001-ST001-AC002.1-TK014` for immediate execution using D2/D8 + RES-004 evidence | HIGH | R1 approved |
| R6 | Unblock `T102B-PH001-ST001-AC004-TK018` (remove DEFERRED status) | MEDIUM | R5, AC004 start |
| R7 | Schedule Initiative-level I&R staleness review after CLAUSE-011 is drafted | LOW | R4 |

---

## X. SOURCE MATERIAL

- **Research Report**: `prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md` v1.0.0
- **Research Brief**: `prompt/artifacts/tasks/T102/research/T102-RES-004/brief_T102-RES-004_issues-risks-architecture.md` v1.0.0
- **Activity Notes**: `prompt/artifacts/tasks/T102/workspace/PH001/ST004/AC001/notes_T102-PH001-ST004-AC001.md` v0.4.0
- **Stream Plan**: `prompt/artifacts/tasks/T102/workspace/PH001/ST004/plan_T102-PH001-ST004.md` v1.1.0
- **T102B Stream Plan**: `prompt/artifacts/tasks/T102/T102B/workspace/PH001/ST001/plan_T102B-PH001-ST001.md` v2.3.0
- **SPS**: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` v1.1.0
- **Standard**: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
