---
artifact_type: 'RESEARCH_REPORT'
initiative_id: 'T102'
research_id: 'T102-RES-004'
version: '1.0.0'
iteration: '1'
date: '2026-02-09'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: Issues & Risks Hosting Architecture (`T102-RES-004`)

## I. EXECUTIVE SUMMARY

**Context**: Feature-level Issues & Risks (I&R) in `request_T102B1-RST.md` Section H remains present (classified `[O]`) even though the Client’s AC002 re-review decision D2 recommended removal and promotion to Epic scope; the final disposition is blocked pending this research (`T102B-PH001-ST001-AC002-DEC002`, `...-DEC006`). The governing standard `T102-STD-007` defines I&R schemas/enums/ID rules but does not define the hosting architecture, content filtering rules, or multi-scope lifecycle beyond a limited Epic→Initiative promotion note.

**Verdict**: **PIVOT RECOMMENDED** (architecture + standard deltas). Multiple candidate hosting patterns are viable (“GO”), but the current three-tier default (SPS+Request) is **NO-GO as a default** due to synchronization burden and unclear feature-level filtering/promotion rules.

**Key Findings**:
1. **Current Hosting Is Three-Tier but Uneven**: Initiative and Epic I&R are meaningfully populated in SPS; Feature-level I&R exists only in one Request (T102B1) and contains meta-authoring/process items that are better scoped to the T102B Epic. (Topic 1)
2. **`T102-STD-007` Standardizes Form, Not Architecture**: `T102-STD-007` is strong on deterministic schema/enums and closure coupling, but weak/underspecified on placement (which artifacts should host), Feature-to-Epic promotion, de-dup enforcement, and content filtering criteria. (Topic 2)
3. **Industry Benchmarking Favors “Registers” Over “Per-Feature Spec Logs”**: Public sources for PRINCE2, BABOK, and SAFe describe issues/risks as managed via registers/boards and lifecycle processes, not as a default section inside each requirements specification; this supports D2’s “remove-by-default at feature scope” direction, with conditional exceptions for high-risk features. (Topic 3)
4. **Best Default Pattern**: **SPS-only hosting (Initiative + Epic I&R in SPS) with Feature-level “remove-by-default”** is the best default for T102, paired with (a) explicit Feature→Epic promotion rules and (b) content filtering criteria that prevent meta-template/process items from landing in feature Requests. (Topics 4–6)
5. **Concept Aggregation Is a Conditional Enhancement**: SPS+Concept (aggregated register in Concept) can further reduce duplication and improve rollups, but should be treated as **PIVOT / conditional** pending `T102-RES-007` (Concept role + dynamic registers viability). (Topic 4)

**Recommended `T102-STD-007` delta scope (recommendations-only)**:
- Clarify **default hosting architecture** (remove-by-default at Feature scope; define allowed exceptions).
- Extend **CLAUSE-009** to include Feature→Epic promotion, de-dup enforcement rules, and “downward monitoring” guidance (higher-scope risk spawning local monitoring actions without upstream referencing downstream).
- Add/clarify **content filtering criteria** (Issue/Risk vs ASSUM/CON/DEP/STD/ADR/IG/NOTE) aligned with `T102-STD-005`.
- Add a lightweight **staleness policy** (e.g., OPEN/MONITORED > 90 days triggers review).

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Research stayed within T102 governance artifacts and the commissioned brief topics. No implementation changes were made to SSOT artifacts (SPS/Request/Concept).

**Source of Truth Audit**:
- **SSOT Artifacts**:
  - `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
  - `prompt/artifacts/tasks/T102/T102B/ssot/request_T102B1-RST.md`
  - `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
- **Standards**:
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` (for register-architecture analogy)
- **Consultation Notes**:
  - `prompt/artifacts/tasks/T102/T102B/workspace/PH001/ST001/AC002/notes_T102B-PH001-ST001-AC002.md` (D2/D6)

**Limitations**:
- The repo ships ADR-extraction scripts for `T102-ADR-005` and `T102-ADR-007`, but they failed due to missing anchors in `concept_T102-CONSULTANT.md`. This report therefore treats the SSOT standards (`T102-STD-007`, `T102-STD-005`) as normative for I&R rules and explicitly records the extraction failure as an Issue in Section IV.
- Industry benchmarking is limited to public web sources (no paywalled ISO/BABOK/PRINCE2 text). Any “best practice” statements are therefore qualified and tied to the cited public materials.

---

## III. TOPIC FINDINGS

### Topic 1: I&R Hosting Inventory Across Scopes
**Objective**: Document current I&R hosting surfaces and quantify population density and staleness.

#### A. Evidence & Forensics
- **Initiative I&R** exists in SPS Section III.B.10:
  - Source: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` (Section “10. Issues & Risks”).
- **Epic I&R** exists in SPS epic dossiers:
  - T102A: `.../sps_T102-CONSULTANT.md` (“T102A … Epic Issues & Risks”).
  - T102B: `.../sps_T102-CONSULTANT.md` (“T102B … Epic Issues & Risks”).
  - T102C: `.../sps_T102-CONSULTANT.md` (“T102C … Epic Issues & Risks”).
- **Feature I&R** exists in only one Feature-level Request:
  - Source: `prompt/artifacts/tasks/T102/T102B/ssot/request_T102B1-RST.md` (Section “H. Issues & Risks”).
- **Concept artifact** does not currently host an I&R register/table:
  - Source: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md` (no “Issues & Risks” section/tables present).

#### B. Analysis (Inventory Table + Metrics)
As-of date for staleness metrics: **2026-02-09** (brief/report date).

| Scope Level | Scope ID | Hosting Artifact | I&R Surface | Issues (total / active / resolved / deferred) | Risks (total / active / mitigated+accepted+closed) | Avg active age (days) | Oldest active (days) | Notes |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| Initiative | `T102` | SPS | Section III.B.10 | 7 / 7 / 0 / 0 | 4 / 4 / 0 | 98.4 | 127 | Many initiative OPEN items are >90 days old (staleness signal). |
| Epic | `T102A` | SPS | Section III.C.1.ix | 3 / 0 / 3 / 0 | 4 / 4 / 0 | 128.0 | 128 | Epic issues fully resolved; risks MONITORED and >120 days old. |
| Epic | `T102B` | SPS | Section III.C.2.x | 8 / 4 / 4 / 0 | 4 / 3 / 1 | 23.0 | 23 | Active items are fresh (proposed 2026-01-17). |
| Epic | `T102C` | SPS | Section III.C.3.ix | 5 / 0 / 4 / 1 | 3 / 0 / 3 | — | — | Scope mostly closed/mitigated; one DEFERRED issue. |
| Feature | `T102B1` | Request | Section H | 2 / 2 / 0 / 0 | 1 / 1 / 0 | 3.0 | 4 | Items are process/template quality gaps, not feature requirements risks. |
| Initiative (register) | `T102` | Concept | N/A | 0 | 0 | — | — | No Concept-hosted I&R register today. |

**Duplication / overlap**:
- No exact title duplicates were found across scopes (by case-insensitive title matching).
- Semantic overlaps exist (e.g., “Document Bloat” / “Context Overload” risks) but are not currently linked/promotion-managed as a single canonical item.

#### C. Governance Implication
- The current “three-tier” architecture is **not operating as a true three-tier system** yet: Feature-level I&R is sparse and appears to capture meta-authoring work (classification/schema), suggesting misclassification and/or lack of filtering rules at Feature scope.
- A staleness policy is likely required for Initiative and long-lived MONITORED risks to preserve “scanability” and review cadence implied by `T102-STD-007`’s auditability intent.

---

### Topic 2: `T102-STD-007` Gap Analysis
**Objective**: Identify what `T102-STD-007` governs vs what remains unspecified for architecture decisions.

#### A. Evidence & Forensics
- Source: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
- Related constraints:
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
  - `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` (notably: Issues/Risks are OIDs; normative bodies must not reference ISSUE/RISK inline).

#### B. Analysis (Gap Matrix)
| Architectural Question | Standard Coverage | Status | Notes |
|:--|:--|:--|:--|
| Table schemas/enums/closure coupling | `T102-STD-007-CLAUSE-002..005,007,008` | Governed | Deterministic and strong. |
| ID patterns and stability | `T102-STD-007-CLAUSE-006` + `T102-STD-005` | Governed | Issue/Risk tokens are allowed at I/E/F scopes (`T102-STD-005`). |
| Hosting architecture (which artifacts host I&R by default) | `T102-STD-007-CLAUSE-001` | **Underspecified** | “Must be available for each scope” does not specify **artifact placement** nor “remove-by-default” exceptions. |
| Feature-level I&R disposition (default remove vs default include) | None | Unspecified | Conflicts with D2 intent; currently handled ad hoc via `[O]`. |
| Content filtering (Issue/Risk vs ASSUM/CON/DEP/STD/ADR/IG/NOTE) | None (partial in `T102-STD-005`) | **Partial** | `T102-STD-005` implies issues/risks are tracking surfaces and not normative, but does not provide an operational decision tree. |
| Cross-scope promotion and de-dup across I/E/F | `T102-STD-007-CLAUSE-009` | **Partial** | Limited to Epic→Initiative, SHOULD language, and does not address Feature→Epic. |
| “Downward monitoring” guidance (initiative risk driving local monitoring tasks) | None | Unspecified | Must respect `T102-STD-003` directionality (upstream must not reference downstream). |
| Staleness detection rules | None | Unspecified | Needed given current >90d OPEN/MONITORED items. |

#### C. Governance Implication
- `T102-STD-007` requires extension to become decision-ready for the hosting architecture question (placement defaults, filtering, and multi-scope lifecycle).
- Any architecture that centralizes I&R into Concept or a dedicated register requires either (a) relaxing CLAUSE-001’s implicit “in each artifact” reading, or (b) defining an “I&R pointer/aggregation” pattern that still satisfies deterministic schema obligations.

---

### Topic 3: Feature-Level I&R Utility Assessment
**Objective**: Evaluate whether Feature-level I&R in Request artifacts is useful or creates governance noise, using evidence and public industry benchmarking.

#### A. Evidence & Forensics
- Feature-level I&R exists in `prompt/artifacts/tasks/T102/T102B/ssot/request_T102B1-RST.md` Section H with 2 Issues and 1 Risk.
  - The I&R section is ~160 words and 12 non-empty lines out of ~2663 words total (~6%).
- AC002 re-review decisions:
  - D2: “Remove Issues & Risks from Request; promote feature-level items to epic scope” (industry norms; reduce clutter).
  - D6: commission initiative-scoped research to resolve hosting architecture.
  - Source: `prompt/artifacts/tasks/T102/T102B/workspace/PH001/ST001/AC002/notes_T102B-PH001-ST001-AC002.md`.
- The existing Feature-level items are meta-authoring concerns:
  - `T102B1-ISSUE-001` Story Index schema alignment to ADR clauses.
  - `T102B1-ISSUE-002` classification marker standardization.
  - `T102B1-RISK-001` request self-hosting drift risk.

#### B. Analysis (Utility vs Cost)
**Observed internal problems**:
- **Scope mismatch**: The Feature-level items are about template/standard alignment and process drift, which are Epic-wide governance concerns (T102B), not stable feature requirements concerns.
- **Filtering absence**: Without filtering criteria, feature Requests can become a sink for “governance hygiene” work items, increasing long-run noise even if any single section is small.
- **Scaling concern**: At projected scale (5–10 features per epic), even “small” sections compound; the primary cost is not raw word count but (a) authoring overhead of deciding whether to populate, and (b) LLM context selection errors where meta-process issues distract from stable requirements.

**Public benchmarking (qualified)**:
- PRINCE2 describes managing **issues** via an Issue Register (a project log/management product), and **risks** via a Risk Register; these are registers rather than default per-requirements-document sections.
- BABOK’s public task card for “Assess Risks” frames risk assessment as part of business analysis work, not as a default embedded section within each requirements specification.
- SAFe materials describe a PI Planning “risk board” and the ROAM categories (Resolved/Owned/Accepted/Mitigated), again consistent with managing risks via a board/register pattern rather than per-feature spec sections.
- ISO’s public page for ISO/IEC/IEEE 29148 positions it as a requirements engineering/process standard; public materials do not clearly support “issues/risk logs belong inside each requirement spec” as a default.

#### C. Governance Implication
- Feature-level I&R inside Requests is **not NO-GO in principle** (feature scope can legitimately have issues/risks per `T102-STD-005`), but it is **NO-GO as a default pattern** without filtering and promotion rules.
- This supports a **remove-by-default** posture for Feature Requests, with explicit exceptions for complex/high-risk features (hybrid threshold).

---

### Topic 4: Hosting Options Comparison Matrix
**Objective**: Evaluate the five candidate hosting patterns defined in the brief and provide a weighted score matrix.

#### A. Evidence & Forensics
- Current state is pattern (b) SPS+Request (three-tier) but sparsely realized at Feature scope (Topic 1).
- Constraints:
  - “link-don’t-duplicate” intent: `T102-STD-003`, `T102-STD-007-CLAUSE-009`.
  - Feature scope eligibility for I&R: `T102-STD-005` allows `ISSUE` / `RISK` at I/E/F scopes.

#### B. Analysis (Weighted Options Matrix)
Scoring rubric: 1 (worst) to 5 (best). Weights are **equal** per brief: (1) LLM context cost, (2) scanability/readability, (3) governance traceability, (4) maintenance burden, (5) cross-scope promotion clarity.

| Pattern | Description (hosting surface) | LLM cost | Scanability | Traceability | Maintenance | Promotion clarity | Total (max 25) | Option Verdict |
|:--|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--|
| (a) SPS-only | Initiative + Epic I&R in SPS; no Feature I&R by default | 4 | 4 | 4 | 3 | 4 | 19 | **GO (Recommended default)** |
| (b) SPS+Request | Initiative + Epic in SPS; Feature I&R in each Request (current) | 3 | 3 | 4 | 2 | 2 | 14 | **NO-GO as default** |
| (c) SPS+Concept | SPS (I+E) plus Concept aggregated register | 3 | 4 | 5 | 3 | 4 | 19 | **PIVOT / Conditional (RES-007)** |
| (d) Hybrid thresholds | SPS (I+E); Feature I&R only for complex/high-risk features | 4 | 4 | 4 | 3 | 3 | 18 | **GO (secondary / exception path)** |
| (e) Dedicated register | Standalone I&R register artifact; other artifacts link/reference | 5 | 3 | 4 | 3 | 4 | 19 | **PIVOT / Optional** |

**Recommendation synthesis**:
- Adopt (a) as the default hosting architecture, and treat (d) as a defined exception path.
- Keep (c) as an enhancement contingent on `T102-RES-007` confirming Concept’s viability as a dynamic SSOT registers surface.
- Avoid (b) as default because it scales poorly without filtering/promotion rules and creates synchronization risk across many Feature Requests.

#### C. Governance Implication
- This recommendation requires `T102-STD-007` updates to explicitly permit “remove-by-default at feature scope” while preserving deterministic schema when a Feature-level I&R section is present (hybrid threshold).
- If (c) is later adopted, `T102-STD-007` must be updated to define how Concept aggregation interacts with “must be available for each scope” without violating `T102-STD-003` directionality.

---

### Topic 5: Lifecycle & Cross-Scope Promotion Rules
**Objective**: Define lifecycle transitions and promotion/de-dup rules that scale beyond Epic→Initiative.

#### A. Evidence & Forensics
- Current promotion guidance exists only as Epic→Initiative SHOULD guidance: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` (CLAUSE-009).
- Directionality constraint: upstream scopes must not reference downstream rules: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`.
- Open/stale items exist at Initiative and long-lived MONITORED risks exist at T102A Epic (Topic 1).

#### B. Analysis (Proposed Lifecycle + Promotion Semantics)
**Lifecycle state diagram (text)**:

Issues (I/E/F):
```
OPEN -> IN-REVIEW -> RESOLVED
  \\-> BLOCKED
  \\-> DEFERRED
```

Risks (I/E/F):
```
OPEN -> MONITORED -> MITIGATED -> CLOSED
                 \\-> ACCEPTED -> CLOSED
```

**Promotion rules (recommendations-only)**:
1. **Upward promotion (canonical)**:
   - If a Feature issue/risk impacts Epic success (multi-feature, template/standard compliance, or epic gates), create an Epic item (`T102B-ISSUE-###` / `T102B-RISK-###`) and close the Feature item with notes referencing the promoted Epic ID.
   - If an Epic item becomes Initiative-impacting (multi-epic governance or operating model), follow existing `T102-STD-007-CLAUSE-009` guidance to create an Initiative item and close or re-scope the Epic item with back-ticked reference to the Initiative ID.
2. **De-dup enforcement**:
   - Treat the **highest-scope** active item as canonical; lower-scope items must be either (a) closed with a reference to the promoted ID, or (b) strictly scoped as local deltas (e.g., local manifestation details).
   - Avoid copying narratives across scopes; prefer references and delta-only notes (aligns with `T102-STD-003`).
3. **Downward monitoring (allowed, but no upstream referencing downstream)**:
   - When an Initiative risk requires local monitoring, create Epic-level “monitoring” risks/issues that reference the Initiative item (downstream referencing upstream is allowed). The Initiative item MUST NOT reference the spawned Epic items (directionality).

**Staleness policy (recommendations-only)**:
- OPEN (Issues) or MONITORED (Risks) older than **90 days** MUST trigger a review touch:
  - update status OR
  - add/refresh planned resolution/mitigation notes OR
  - explicitly DEFER/ACCEPT with rationale and governing IDs.

#### C. Governance Implication
- Extending `T102-STD-007-CLAUSE-009` to include Feature→Epic promotion and explicit de-dup rules is necessary to make remove-by-default at Feature scope operational without losing concerns.
- A staleness policy materially improves scanability for executive review and prevents “infinite MONITORED backlog” behavior observed in current SPS logs.

---

### Topic 6: Content Filtering Criteria
**Objective**: Define operational rules for what qualifies as Issue/Risk vs other governance surfaces, with worked examples from current inventory.

#### A. Evidence & Forensics
- `T102-STD-005` defines Issue/Risk as OID categories (tracking surfaces), and explicitly distinguishes them from normative RIDs/STD clauses.
- Current Feature-level items are meta-process items (Topic 3).
- Initiative items include “Planner Handoff Schema” and “IDs Promotion Protocol” that may be better expressed as Interfaces/Standards once decided (Topic 1).

#### B. Analysis (Decision Tree + Worked Examples)
**Decision tree (operational, prescriptive)**:
1. **Is this a stable obligation or enforceable rule?**
   - Yes -> create/update `STD` or `RID` (IF/CON/QG/DEP/FR/NFR) or an `ADR` clause; do **not** leave it as an Issue/Risk.
   - No -> continue.
2. **Is it a current, known problem/gap blocking progress?**
   - Yes -> **Issue**.
   - No -> continue.
3. **Is it a potential negative event with uncertain occurrence?**
   - Yes -> **Risk**.
   - No -> continue.
4. **Is the “risk” actually an unvalidated belief?**
   - Yes -> **Assumption (`ASSUM`)** with validation method/owner; create a Risk only if the consequence warrants explicit monitoring.
5. **Is it an external prerequisite or dependency (asset, approval, integration partner)?**
   - Yes -> **Dependency (`DEP`)**; create an Issue only if it is already failing or missing.
6. **Is it guidance/how-to (non-normative) rather than a gap/event?**
   - Yes -> `IG`/`INT`/`NOTE`.

**Worked examples (from current inventory)**:
- `T102-ISSUE-001 (Planner Handoff Schema)`:
  - Classification: **Issue now**, but target state should be **Interface (`IF`)** once the schema is defined (Issue tracks the “missing contract”; IF becomes the contract).
- `T102-ISSUE-004 (IDs Promotion Protocol)`:
  - Classification: **Issue now**, but target state should be **Standard (`STD`) or ADR** governing promotion semantics (Issue tracks the gap until formalized).
- `T102B1-ISSUE-002 (Classification markers)`:
  - Classification: **Epic Issue**, not Feature Issue (applies across T102B features). Promote to `T102B-ISSUE-###` and resolve by updating `T102B-STD-002` and/or `T102-STD-007` as appropriate.
- `T102A-RISK-003 (Document Bloat)` and `T102C-RISK-001 (Context Overload)`:
  - Classification: **Risks** (potential negative events affecting LLM/author performance). These are candidates for Initiative-level aggregation or explicit linkage (de-dup/promotion) because they are cross-epic concerns.

#### C. Governance Implication
- Without prescriptive filtering, Feature-level Requests are likely to accumulate meta-process issues that belong at Epic or Initiative scope, increasing maintenance burden and harming scanability.
- Filtering criteria also create a clear “promotion target” path from Issue/Risk → STD/ADR/RID when the item stabilizes into an obligation or reusable rule (aligns with `T102-STD-005` category precedence).

---

## IV. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-004-ISSUE-001` | ADR extraction anchors missing | ADR-005/ADR-007 print scripts fail because expected anchors are missing from `concept_T102-CONSULTANT.md`, blocking “print ADR block” workflow | LLM_Researcher | `OPEN` | `MEDIUM` | 2026-02-09 | — | — |
| `T102-RES-004-ISSUE-002` | Feature I&R filtering undefined | No normative content-filtering criteria exist to prevent feature Requests from hosting epic/initiative governance hygiene items | Client | `OPEN` | `HIGH` | 2026-02-09 | — | — |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-RES-004-RISK-001` | RES-007 dependency | Concept hosting candidate evaluation depends on RES-007 viability findings; if RES-007 is delayed, Concept-related recommendations may be provisional | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-09 | — | — |
| `T102-RES-004-RISK-002` | External sources are paywalled | Public-web-only constraint may prevent citing definitive ISO/BABOK/PRINCE2 clauses, weakening “industry norm” confidence | LLM_Researcher | `MONITORED` | `LOW` | 2026-02-09 | Use public official summaries; qualify claims; request excerpts if stronger evidence required | — |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `T102-STD-007` | CLAUSE-001, CLAUSE-009 | Amend to specify default hosting (remove-by-default at Feature), extend promotion (Feature→Epic), and add staleness + filtering guidance | Topics 2, 4, 5, 6 |
| `T102-STD-005` | (optional) | Consider adding an explicit “Issue/Risk → target category” promotion guidance note (non-normative) | Topic 6 |
| `T102B` Request template work | Request Section H | Implement D2 disposition using this report: remove-by-default, promote any feature I&R items to Epic, and enforce filtering rules | Topic 3, Topic 5, Topic 6 |
| `T102-RES-007` | Overlap reconciliation | Align Concept register recommendation (pattern c) with RES-007’s Concept viability verdict | Topic 4 |
| ADR skills system | ADR extraction scripts | Either add missing anchors to Concept or change scripts to extract from standards instead of Concept | Issue `T102-RES-004-ISSUE-001` |

---

## VI. SOURCE MATERIAL

**Brief Version**: `prompt/artifacts/tasks/T102/research/T102-RES-004/brief_T102-RES-004_issues-risks-architecture.md` (v1.0.0, 2026-02-09)

**Code Commit/Tag**: N/A (environment is not a git repository)

**Files Cited (repo)**:
- `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/T102B/ssot/request_T102B1-RST.md`
- `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md`
- `prompt/artifacts/tasks/T102/T102B/workspace/PH001/ST001/AC002/notes_T102B-PH001-ST001-AC002.md`

**External Sources (public web, best-effort)**:
- ISO: ISO/IEC/IEEE 29148 overview page: `https://www.iso.org/standard/45171.html`
- BABOK: IIBA task card “Assess Risks”: `https://www.iiba.org/globalassets/documents/certification/ecba/task-cards/ecba-task-cards-assess-risks.pdf`
- PRINCE2 summaries: Issue Register and Risk Register (public wiki):
  - `https://prince2.wiki/theme/risk/risk-register/`
  - `https://prince2.wiki/theme/progress/issue-register/`
- SAFe: PI Planning risk board slide deck (public):
  - `https://framework.scaledagile.com/2024/RTE/02_PI_Planning.pdf`

