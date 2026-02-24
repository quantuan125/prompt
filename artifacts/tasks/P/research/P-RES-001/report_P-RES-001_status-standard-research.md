---
artifact_type: 'RESEARCH_REPORT'
initiative_id: 'P'
research_id: 'P-RES-001'
version: '1.0.0'
iteration: '1'
date: '2026-02-23'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: Status Standard Research (`P-RES-001`)

## I. EXECUTIVE SUMMARY

**Context**: `P-STD-002` (Program Status Standard) is planned to govern program-wide status vocabulary, health assessment, dependency visibility, evidence linkage, update protocol, and status artifact specification. The current internal working model (seed) proposes a 7-state enum, a unified dependency schema, and evidence linkage requirements, but it is internally reasoned and lacks external benchmarking (`prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-research.md`).

**Verdict**: **GO (with amendments)** — the working model is directionally aligned with mature tooling patterns (customizable workflows under fixed meta-categories, explicit lifecycle categories, and traceable work-item linkages), but P-STD-002 should:
1) Treat the enum as a **state machine** with documented transitions and guard conditions (not just labels).
2) Treat “blocked/on-hold” as **distinct operational meanings**, but remain compatible with tools that model “blocked” as an attribute rather than a status.
3) Define health as **multi-dimensional** (time/cost/scope/quality/risk/benefits) with an explicit **hybrid RAG** threshold method.
4) Define dependency visibility as a **graph-first contract** (`depends_on`/`blocks`), with optional schedule semantics (`FS/SS/FF/SF`) when needed.
5) Define evidence linkage as a **deterministic evidence pointer contract** (link-don’t-duplicate), compatible with Jira/Azure work-item linking.

**Key Findings**:
1) **Tools separate meta-category from status**: Jira fixes three status categories (To Do / In Progress / Done) while allowing teams to create custom statuses and workflows. This supports a 7-state program enum as a governance overlay, provided it maps cleanly into tool meta-categories. [1][2]
2) **Enterprise workflows are explicitly stateful and traceable**: Azure DevOps distinguishes workflow “state categories” (Proposed/In Progress/Resolved/Completed/Removed) and supports rich link types and automation (e.g., PR-based completion), which is strong evidence for formal transition governance + evidence link patterns. [4][5]
3) **Health dimensions converge on tolerance targets**: PRINCE2’s management-by-exception model defines tolerances across time, cost, scope, quality, risk, and benefits; this supports a multi-dimensional health model and suggests RAG should be computed from tolerance bands rather than being purely subjective. [9]

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: This report stays within `brief_P-RES-001_status-standard-research.md` (11 topics; recommendations-only; no P-STD-002 clause drafting; no status artifact implementation).

**Source of Truth Audit**:
* **Program governance context (internal)**:
  * `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
  * `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
  * `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md`
  * `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md`
  * Seed (informative only): `prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-research.md`
* **External benchmarking**:
  * Jira Cloud administration and work item semantics. [1][2][16]
  * Azure DevOps Boards workflow categories, process workflows, linkability/automation. [4][5][11]
  * PRINCE2 tolerance dimensions (public summaries). [9]
  * Data/format standards and common front-matter patterns. [12][13][14][15]

**Limitations**:
* Some framework primary texts (PMI/PMBOK, PRINCE2 full manual, SAFe detailed kanban-state prescriptions) are paywalled or access-controlled. Where primary text was not accessible, this report uses public tool documentation as the strongest empirical proxy for “industry practice”, and labels framework coverage accordingly.
* Jira status sets are highly configurable; external evidence supports meta-category patterns more strongly than any fixed status list. [1][2]

---

## III. TOPIC FINDINGS

### Topic 1: Industry Status Enum Benchmarking (Critical)
**Objective**: Benchmark canonical status enum sets used in mature program/project management frameworks and tooling, and assess alignment with the proposed 7-state set.

#### A. Evidence & Forensics
* **Jira workflow meta-categories are fixed**:
  * **Source**: Jira status categories and constraints. [1]
  * **Observation**: Jira uses fixed status categories (To Do / In Progress / Done) that cannot be customized, while workflows and statuses are configurable. [1]
* **Jira statuses are categorized; cancelled can be “Done”**:
  * **Source**: Jira issue status categories. [2]
  * **Observation**: “Cancelled” can be treated as a “Done” status category (closed outcome, not necessarily “completed”). [2]
* **Azure DevOps uses lifecycle state categories**:
  * **Source**: Workflow state categories. [4]
  * **Observation**: Azure DevOps supports state categories such as Proposed, In Progress, Resolved, Completed, Removed, and uses those categories for reporting/behavior. [4]
* **Azure DevOps Scrum process has explicit default states**:
  * **Source**: Scrum process workflow. [5]
  * **Observation**: Example default workflow states include New → Active → Resolved → Closed, and the process supports link types (including “Found in build” and “Test result”) used as evidence. [5]
* **Jira Align illustrates additional operational statuses**:
  * **Source**: Jira Align status catalog. [7]
  * **Observation**: Enterprise portfolio tooling commonly includes statuses like “Paused” (hold) and “Canceled”, mapping to meta-categories rather than enforcing a universal enum across all orgs. [7]

#### B. Analysis
**What industry “canonical enums” actually look like**:
* The strongest cross-industry consensus is **not** a single fixed list of statuses; it is a **small set of meta-categories** (To Do / In Progress / Done; or Proposed/In Progress/Resolved/Completed/Removed) plus **custom statuses** within those categories. [1][2][4]
* Therefore, a program-level standard should define:
  1) A canonical **program status vocabulary** (for cross-initiative comparability), and
  2) A mandatory **mapping layer** from local tool statuses → program vocabulary / meta-categories.

**Gap analysis vs the proposed 7-state** (`planned`, `ready`, `in_progress`, `blocked`, `on_hold`, `completed`, `cancelled`):
* **Planned/Ready**: Aligns with common “To Do” splits (backlog vs ready/selected) seen in configurable workflows (often modeled via multiple To Do statuses rather than new categories). [1][7]
* **Blocked**: Many tools represent blocked-ness as a status or a flag/field; the standard must remain compatible with both patterns. [1][4]
* **On hold**: “Paused/On hold” is a common operational concept (distinct from blocked); enterprise tools often include it. [7]
* **Cancelled**: Tools commonly treat cancellation as a terminal “Done/Removed” outcome. [2][4]

#### C. Governance Implication
* `P-STD-002A` should define:
  - The 7-state vocabulary (or an equivalent), **plus** a required mapping to tool meta-categories (To Do/In Progress/Done; Proposed/In Progress/Resolved/Completed/Removed). [1][4]
  - A rule that local initiatives MAY have additional local states, but MUST map them to the program vocabulary for roll-ups.

**Scored comparison (Topic 1)** (rubric per brief Section III.D):

| Option | Description | Program Fit (5) | Industry Alignment (5) | Agentic Operability (3) | Adoption Overhead (3) | Extensibility (2) | Weighted Total (max 90) |
|:--|:--|:--:|:--:|:--:|:--:|:--:|--:|
| A | **3-state + attributes**: `todo/in_progress/done` with `blocked=true`, `hold_reason`, `done_reason={completed,cancelled}` | 4 | 5 | 4 | 5 | 3 | 78 |
| B | **7-state program enum** (working model) with required tool mapping | 5 | 4 | 5 | 4 | 4 | 80 |
| C | **Lifecycle-category-first**: align directly to Proposed/In Progress/Resolved/Completed/Removed; treat “ready/blocked/on_hold” as attributes | 4 | 4 | 4 | 3 | 5 | 71 |

**Recommendation**: Option **B** (7-state), **with** explicit mapping rules and an “attribute-compatible” interpretation for `blocked` (allowed as either a status or an attribute). [1][4]

---

### Topic 2: State Machine Transition Rules (Critical)
**Objective**: Recommend a transition matrix and guard-condition patterns consistent with mature tooling.

#### A. Evidence & Forensics
* **Azure DevOps models transitions, including “backward transitions”**:
  * **Source**: Workflow state categories documentation. [4]
  * **Observation**: Azure DevOps explicitly describes transition directionality (including backward transitions) and uses state categories for downstream behaviors (e.g., “completed” items visibility rules). [4]
* **Jira supports restricting transitions to user groups**:
  * **Source**: Jira Cloud administration docs on restricting workflows based on user groups. [3]
  * **Observation**: Jira supports guardrails at transition-time based on user/group, which maps to program role accountability patterns. [3]

#### B. Analysis
**Transition pattern recommendation (program-level)**:
* Use **initial** state: `planned`.
* Use **terminal** states: `completed`, `cancelled`.
* Allow controlled backflow only when explicitly justified and evidenced (e.g., `completed` → `in_progress` for rework).

**Proposed transition matrix (v1)**:
* `planned` → `ready` | guard: definition-of-ready satisfied (local; may be checklist).
* `ready` → `in_progress` | guard: owner assigned + start date (or “as_of”) recorded.
* `in_progress` → `blocked` | guard: blocker recorded (dependency ID or narrative).
* `blocked` → `in_progress` | guard: blocker resolved (evidence pointer).
* `in_progress` → `on_hold` | guard: explicit pause decision + next review date.
* `on_hold` → `ready` | guard: resume criteria set.
* `{planned,ready,in_progress,blocked,on_hold}` → `cancelled` | guard: cancellation reason + evidence pointer.
* `in_progress` → `completed` | guard: completion evidence pointer(s) + acceptance confirmation.
* `{completed,cancelled}` → `in_progress` (exception) | guard: “reopen” rationale + new work item/plan reference + evidence pointer.

Guard conditions map cleanly to tool controls:
* Restricting high-impact transitions (e.g., to terminal states) to specific roles or approval groups is consistent with Jira’s workflow restriction capabilities. [3]

#### C. Governance Implication
* `P-STD-002A` should include a required transition table (or equivalent) with:
  - initial and terminal state identification,
  - allowed transitions,
  - minimum guard conditions (especially for terminal transitions),
  - an explicit “reopen” exception contract.
* `P-STD-002D` should cross-reference evidence linkage requirements for terminal transitions (Topic 7).

---

### Topic 3: RAG Threshold Frameworks (High)
**Objective**: Recommend a threshold method for Red/Amber/Green health that reduces subjectivity.

#### A. Evidence & Forensics
* **PRINCE2 governs “tolerances” across key dimensions**:
  * **Source**: Public PRINCE2 tolerances summary (time, cost, scope, quality, risk, benefits). [9]
  * **Observation**: PRINCE2’s management-by-exception approach relies on pre-defined tolerances; status/exception handling triggers when tolerances are forecast to be exceeded. [9]

#### B. Analysis
RAG becomes subjective without defined thresholds. A program standard should specify:
1) What dimensions are assessed (Topic 4),
2) How each dimension maps to R/A/G,
3) How an overall RAG is derived from dimension-level RAG.

**Recommended threshold approach: Hybrid (tolerance bands + override rules)**
* For each dimension, define:
  - **Green**: within tolerance band
  - **Amber**: near tolerance limit (trend indicates risk of breach)
  - **Red**: tolerance breached or breach is highly likely absent intervention
* Aggregate using an override rule (example):
  - If any dimension is Red → overall Red
  - Else if 2+ dimensions are Amber → overall Amber
  - Else overall Green

#### C. Governance Implication
* `P-STD-002B` should define the required threshold method and aggregation rule, while allowing initiative-specific numeric values (tolerance amounts) to be configured locally.

**Scored comparison (Topic 3)**:

| Option | Description | Program Fit (5) | Industry Alignment (5) | Agentic Operability (3) | Adoption Overhead (3) | Extensibility (2) | Weighted Total |
|:--|:--|:--:|:--:|:--:|:--:|:--:|--:|
| A | Quantitative-only bands (fixed % thresholds everywhere) | 5 | 4 | 5 | 3 | 4 | 77 |
| B | Qualitative-only rules (narrative judgment; no numeric tolerances) | 4 | 4 | 3 | 5 | 3 | 70 |
| C | **Hybrid tolerances + override aggregation** (recommended) | 5 | 5 | 4 | 4 | 5 | 84 |

---

### Topic 4: Health Assessment Dimensions (High)
**Objective**: Recommend a standard set of health dimensions and aggregation.

#### A. Evidence & Forensics
* **PRINCE2 defines six tolerance areas**:
  * **Source**: PRINCE2 tolerances summary. [9]
  * **Observation**: Tolerances cover time, cost, scope, quality, risk, and benefits. [9]

#### B. Analysis
Health should be multi-dimensional at program scope, because a single RAG hides failure modes (e.g., “on schedule but failing quality”).

**Recommended standard dimensions (v1)**:
* `time` (schedule)
* `cost` (budget/capacity)
* `scope` (commitment changes)
* `quality` (verification/compliance completion)
* `risk` (known risk exposure)
* `benefits` (expected value / outcome realization)

**Aggregation**:
* Compute dimension-level RAG via the Topic 3 method.
* Compute overall RAG via override rules (Topic 3).

#### C. Governance Implication
* `P-STD-002B` should require these six dimensions at program reporting scope, while allowing optional additional dimensions (e.g., “dependencies”) provided they map to the same aggregation method.

---

### Topic 5: Dependency Typing Schemas (Critical)
**Objective**: Recommend a program-level dependency schema with typing and categorization.

#### A. Evidence & Forensics
* **Scheduling tools formalize dependency relationship types**:
  * **Source**: Microsoft Project dependency types (FS/SS/FF/SF). [8]
  * **Observation**: Dependency relationship types such as Finish-to-Start, Start-to-Start, Finish-to-Finish, and Start-to-Finish are standard representations in schedule tooling. [8]
* **PRINCE2 distinguishes internal vs external dependencies**:
  * **Source**: PRINCE2 dependency summary (internal/external). [17]
  * **Observation**: Dependencies can be categorized by whether they are within the project’s control (internal) or outside (external). [17]

#### B. Analysis
For program-wide orchestration, the **minimum useful** dependency contract is a directed graph with ownership and risk signals. Schedule semantics (FS/SS/FF/SF) are valuable but not required for every dependency.

**Recommended schema (v1, graph-first)**:
* Required fields per dependency edge:
  - `from_id` (blocker / upstream)
  - `to_id` (blocked / downstream)
  - `relationship`: `depends_on` (or `blocks`), with clear direction
  - `category`: `internal` | `external` (minimum); MAY extend (e.g., `cross_team`, `regulatory`, `resource`)
  - `criticality`: `critical` | `near_critical` | `non_critical` (or equivalent)
  - `owner` (who can resolve / coordinate)
  - `status`: `open` | `at_risk` | `resolved`
  - `evidence` (pointer(s) when status changes; see Topic 7)
* Optional schedule semantics:
  - `schedule_relation`: `FS` | `SS` | `FF` | `SF` (+ optional lag)

#### C. Governance Implication
* `P-STD-002C` should define the dependency contract as graph-first (supports LLM operability and tool interoperability), and treat FS/SS/FF/SF as optional enrichment. [8]

**Scored comparison (Topic 5)**:

| Option | Description | Program Fit (5) | Industry Alignment (5) | Agentic Operability (3) | Adoption Overhead (3) | Extensibility (2) | Weighted Total |
|:--|:--|:--:|:--:|:--:|:--:|:--:|--:|
| A | Schedule-first (always require `FS/SS/FF/SF` + lag) | 4 | 5 | 4 | 2 | 5 | 72 |
| B | **Graph-first + optional schedule semantics** (recommended) | 5 | 5 | 5 | 4 | 5 | 88 |
| C | Graph-only (no schedule semantics allowed) | 5 | 4 | 5 | 5 | 4 | 83 |

---

### Topic 6: Cross-Initiative Dependency Models (High)
**Objective**: Recommend whether to require a unified schema across initiatives or an interface-contract model.

#### A. Evidence & Forensics
* **Tools support cross-entity dependency visualization**:
  * **Source**: Azure DevOps “Delivery Plans” (dependency tracking) guidance. [18]
  * **Observation**: Enterprise tooling frequently provides cross-team/plan views specifically to surface dependencies across multiple backlogs/teams. [18]

#### B. Analysis
At program scope, the governing need is **visibility and comparability**, not forcing every initiative to use identical internal tooling or fields.

**Recommendation: Interface-contract model (program surface)**
* `P-STD-002C` defines a **program dependency interface** (minimum required fields, Topic 5).
* Each initiative MAY maintain richer local dependency models, but MUST surface the program interface for roll-ups.
* This approach is compatible with heterogeneous tools and reduces migration friction.

#### C. Governance Implication
* `P-STD-002C` should specify:
  - a minimum cross-initiative dependency interface,
  - a conformance rule (“local models must map to the interface”),
  - a roll-up view requirement for program reporting.

---

### Topic 7: Evidence Linkage Patterns (Critical)
**Objective**: Define evidence linkage patterns for transitions, especially terminal transitions.

#### A. Evidence & Forensics
* **Azure DevOps supports linking and evidence-like link types**:
  * **Source**: Scrum process workflow (Links tab). [5]
  * **Observation**: Work items can link to many artifacts; link relationships include examples like “Found in build” or “Test result”, which are evidence-like associations. [5]
* **Azure DevOps supports automation on work items via PRs**:
  * **Source**: Workflow and state categories doc (mentions PR completion). [4]
  * **Observation**: Work items can be auto-completed with pull requests, supporting deterministic evidence-driven terminal transitions. [4]
* **Jira supports issue linking as a first-class concept**:
  * **Source**: Atlassian support — link issues. [16]
  * **Observation**: Jira provides explicit issue link semantics (linking related issues) and is designed for cross-issue traceability. [16]

#### B. Analysis
**Evidence linkage contract requirements (program level)**:
* Evidence MUST be pointer-based (link-don’t-duplicate), and verifiable (path/URL resolves).
* Terminal transitions should require evidence pointers at minimum:
  - `completed`: verification/acceptance evidence (tests, review, sign-off note)
  - `cancelled`: cancellation rationale evidence (decision record, note)

**Recommended evidence pointer shape (v1)**:
* `evidence[]` array where each element has:
  - `type` (e.g., `note`, `pr`, `build`, `test_result`, `decision`)
  - `ref` (repo path or URL)
  - `date` (ISO-8601)
  - `by` (role/user)
  - `summary` (short)

This keeps P artifacts compatible with Jira/Azure linking patterns while staying repo-native. [4][5][16]

#### C. Governance Implication
* `P-STD-002D` should define:
  - which transitions require evidence (minimum: any → terminal),
  - evidence pointer schema (minimum keys),
  - validation rules (path resolution, ISO dates, attribution).

**Scored comparison (Topic 7)**:

| Option | Description | Program Fit (5) | Industry Alignment (5) | Agentic Operability (3) | Adoption Overhead (3) | Extensibility (2) | Weighted Total |
|:--|:--|:--:|:--:|:--:|:--:|:--:|--:|
| A | **Inline evidence pointers on each transition event** (recommended) | 5 | 4 | 5 | 3 | 4 | 77 |
| B | Separate evidence register artifact (evidence IDs referenced from status) | 4 | 4 | 5 | 2 | 5 | 71 |
| C | Tool-links only (no repo-native evidence contract) | 3 | 5 | 3 | 4 | 3 | 67 |

---

### Topic 8: Role Accountability Matrix (High)
**Objective**: Recommend an accountability model for who can update what, and how conflicts are resolved.

#### A. Evidence & Forensics
* **RACI is a standard role-accountability pattern**:
  * **Source**: Atlassian RACI guidance. [10]
  * **Observation**: RACI is commonly used to clarify who is Responsible, Accountable, Consulted, and Informed, reducing ambiguity in governance activities. [10]
* **Tools support role/group-based workflow restrictions**:
  * **Source**: Jira workflow restrictions by group. [3]
  * **Observation**: Transition restrictions can be enforced based on groups, reflecting practical enforcement mechanisms for accountability. [3]

#### B. Analysis
Two viable patterns:
1) **Role-restricted**: only certain roles can update certain fields / execute certain transitions.
2) **Role-attributed**: any role can update, but every change records `updated_by` and can be audited/rolled back.

**Recommendation (v1)**: Hybrid
* Use role-restricted controls for **terminal transitions** and **health downgrade** (high impact).
* Use role-attributed updates for routine progress updates (low friction), with required attribution and evidence when impact is high.

#### C. Governance Implication
* `P-STD-002D` should include a role-field and role-transition matrix (RACI-style) and define conflict resolution (e.g., last-write-wins + escalation path, or “Accountable role resolves conflicts”).

---

### Topic 9: Stale-State SLA Models (Medium, informational only)
**Objective**: Survey stale-state detection patterns for Phase 2; do not draft normative P-STD-002 v1 requirements.

#### A. Evidence & Forensics
* **Tools encode staleness behaviors**:
  * **Source**: Azure DevOps state categories doc. [4]
  * **Observation**: Some tool views de-emphasize or remove completed items after a fixed time window (example: completed work items may not show after a set period), reflecting an industry expectation that “old closed” becomes less operationally relevant. [4]

#### B. Analysis (survey)
Common stale-state detection models:
1) **Time-since-update** thresholds (e.g., warn if `in_progress` not updated in N days).
2) **Cadence enforcement** (must update at each checkpoint/cadence).
3) **Event-based triggers** (dependency resolution events require status refresh).
4) **Escalation paths** (notify owner/accountable role; require next-action refresh).

Applicability to P:
* Phase 0 / early program governance likely needs **simple time-since-update warnings** and a manual review cadence before automation.

#### C. Governance Implication
* `P-STD-002` v1 should reserve a section for stale-state governance as “Phase 2 / future work” and avoid locking numeric SLA thresholds until operational data exists.

---

### Topic 10: Artifact Format Options (High)
**Objective**: Evaluate YAML vs JSON vs Markdown-with-frontmatter vs hybrid formats for machine-readable status data.

#### A. Evidence & Forensics
* **JSON is standardized for interchange**:
  * **Source**: RFC 8259. [12]
  * **Observation**: JSON is a widely used, standardized text format for structured data interchange. [12]
* **YAML is a standard specification and common in config**:
  * **Source**: YAML 1.2 specification. [13]
  * **Observation**: YAML is a standardized human-readable data serialization format. [13]
* **YAML front matter is an established pattern for Markdown content systems**:
  * **Source**: GitHub Docs YAML frontmatter; Jekyll front matter. [14][15]
  * **Observation**: Many Markdown workflows support an initial YAML metadata block (“front matter”) without breaking Markdown rendering, enabling hybrid “structured + narrative” artifacts. [14][15]

#### B. Analysis
Format trade-offs for a Markdown-primary governance ecosystem:
* **YAML (standalone ledger)**: human-editable, supports comments; good for hierarchical data; can be error-prone without validation.
* **JSON**: strict, tool-friendly, less human-friendly for manual edits; no comments.
* **Markdown + YAML front matter**: keeps artifact Markdown-native; editors render it; structured payload can still be parsed; best when the payload stays moderately sized.

#### C. Governance Implication
* `P-STD-002E` should allow Markdown with YAML front matter as the default human+machine compromise, and explicitly permit a standalone YAML ledger when the canonical payload grows beyond “front-matter sized”. [14][15]

**Scored comparison (Topic 10)**:

| Option | Description | Program Fit (5) | Industry Alignment (5) | Agentic Operability (3) | Adoption Overhead (3) | Extensibility (2) | Weighted Total |
|:--|:--|:--:|:--:|:--:|:--:|:--:|--:|
| A | Standalone YAML ledger | 4 | 4 | 5 | 3 | 5 | 74 |
| B | Standalone JSON ledger | 3 | 4 | 5 | 3 | 5 | 69 |
| C | **Markdown + YAML front matter (canonical payload)** | 5 | 4 | 4 | 5 | 4 | 80 |

---

### Topic 11: Artifact Cardinality (High)
**Objective**: Recommend single vs multi-artifact models (structured + narrative + changelog).

#### A. Evidence & Forensics
* **Tooling generally separates structured data from narrative and history**:
  * **Source**: Jira workflow/status model and issue linking are distinct from narrative comments/pages; Azure DevOps links and automation are distinct from reporting views. [1][4][16]
  * **Observation**: Enterprise systems typically maintain structured records with separate narrative/context and separate history/audit, rather than collapsing all concerns into a single representation. [1][4][16]

#### B. Analysis
**Single artifact** (all-in-one Markdown) is simplest to operate, but becomes harder to validate and automate once the payload grows.

**Dual artifact** (structured ledger + narrative) cleanly separates concerns:
* Canonical source: structured ledger (YAML/JSON)
* Human digest: Markdown narrative

**Triple artifact** adds a changelog, improving auditability but increasing overhead.

#### C. Governance Implication
* `P-STD-002E` should define an authority hierarchy (what is canonical vs derived) and an update sequence (Topic 7/8) to avoid drift.

**Scored comparison (Topic 11)**:

| Option | Description | Program Fit (5) | Industry Alignment (5) | Agentic Operability (3) | Adoption Overhead (3) | Extensibility (2) | Weighted Total |
|:--|:--|:--:|:--:|:--:|:--:|:--:|--:|
| A | Single artifact (Markdown + front matter + narrative) | 5 | 4 | 4 | 5 | 4 | 80 |
| B | **Dual artifact (ledger + narrative; clear authority)** | 5 | 5 | 5 | 3 | 5 | 84 |
| C | Triple artifact (ledger + narrative + changelog) | 4 | 4 | 5 | 2 | 5 | 71 |

**Recommendation**: Option **B** (dual artifact) as the default; reserve a changelog as an optional add-on if audit needs grow.

---

## Issues & Risks

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-001-ISSUE-001` | Paywalled framework primaries | Some framework primary texts (PMI/PMBOK, PRINCE2 full manual, SAFe detailed state prescriptions) are not fully accessible; tool documentation is used as the strongest proxy. | LLM_Researcher | `OPEN` | `MEDIUM` | 2026-02-23 | — | — |
| `P-RES-001-ISSUE-002` | SAFe state-set visibility | SAFe kanban state naming conventions could not be fully validated from primary pages due to access control; status governance conclusions rely on tool patterns and limited SAFe public material. | LLM_Researcher | `OPEN` | `LOW` | 2026-02-23 | — | — |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-001-RISK-001` | Overfitting to one tool | Defining P-STD-002 too tightly to Jira/Azure patterns could reduce adoption for initiatives using other tooling. | LLM_Researcher | `MONITORED` | `MEDIUM` | 2026-02-23 | Mitigate by requiring a mapping layer (local statuses → program vocabulary) and keeping the program contract tool-agnostic. | — |
| `P-RES-001-RISK-002` | Drift between narrative and ledger | A multi-artifact model can drift if authority hierarchy and update sequence aren’t explicit. | LLM_Researcher | `MONITORED` | `HIGH` | 2026-02-23 | Mitigate by defining canonical source (ledger), derived views (narrative), and mandatory evidence pointers for terminal transitions. | — |

---

## V. ARTIFACT UPDATES (Integration Recommendations Package)

> Recommendations-only package for `P-PH000-ST001-AC003` consumption; no clause text drafting.

| P-STD-002 Domain | Research Inputs | Recommendations (summary) |
| :--- | :--- | :--- |
| `P-STD-002A` Status Vocabulary | Topics 1–2 | Adopt 7-state program vocabulary with mandatory mapping to tool meta-categories; publish explicit transition table + guard conditions; allow `blocked` as status or attribute-compatible. [1][4] |
| `P-STD-002B` Health Assessment | Topics 3–4 | Require multi-dimensional health (time/cost/scope/quality/risk/benefits) and hybrid tolerance-based RAG with override aggregation. [9] |
| `P-STD-002C` Dependency Visibility | Topics 5–6 | Define graph-first dependency interface (`depends_on`/`blocks`) with ownership + criticality + status; allow optional `FS/SS/FF/SF` enrichment; use interface-contract surfacing across initiatives. [8][18] |
| `P-STD-002D` Update Protocol | Topics 7–9 | Require evidence pointers for terminal transitions; define evidence schema + validation rules; use hybrid accountability (role-restricted for terminal + role-attributed for routine); reserve stale-state SLA details for Phase 2. [3][4][5] |
| `P-STD-002E` Status Artifact | Topics 10–11 | Prefer dual-artifact model (structured ledger + Markdown narrative) with explicit authority hierarchy; permit Markdown+front matter and/or standalone YAML ledger as governed by the standard. [14][15] |

**Cross-topic integration answers (per brief Section IV)**:
1) **Transitions × evidence**: All terminal transitions (→ `completed` / → `cancelled`, and exceptional reopen) should require evidence pointers; the transition table should mark these transitions as “evidence-required”. [4][5]
2) **Artifact format × dependencies**: Typed dependencies and evidence pointers are easiest to validate in a structured payload (YAML/JSON); Markdown narratives remain best for “what changed / why”. [12][13][14]
3) **Cardinality × update protocol**: If dual artifacts are used, update sequence must be canonical-ledger-first, narrative-derived-second, to avoid drift; role-accountability should enforce terminal-state updates (and their evidence) at the ledger layer. [3][14]

**Seed gap analysis (what is missing from the seed analysis to support all domains)**:
* Transition rules and guard conditions (Topic 2).
* Multi-dimensional health + explicit RAG method (Topics 3–4).
* A dependency contract that is explicitly graph-first with optional schedule semantics (Topics 5–6).
* A concrete evidence pointer schema and validation rules (Topic 7).
* A decided artifact model (single vs dual) with authority hierarchy (Topic 11).

---

## VI. SOURCE MATERIAL

* **Brief Version**: `prompt/artifacts/tasks/P/research/P-RES-001/brief_P-RES-001_status-standard-research.md` (v1.0.0, 2026-02-24)
* **Code Commit/Tag**: —
* **Internal files cited**:
  * `prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-research.md`
  * `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
  * `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

* **External sources**:
  * [1] Atlassian Support — What is a Jira workflow? https://support.atlassian.com/jira-cloud-administration/docs/what-is-a-jira-workflow/
  * [2] Atlassian Support — What are issue statuses? https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-statuses/
  * [3] Atlassian Support — Restrict workflows based on user groups https://support.atlassian.com/jira-cloud-administration/docs/restrict-workflows-based-on-user-groups/
  * [4] Microsoft Learn — Workflow states and state categories (Azure DevOps) https://learn.microsoft.com/en-us/azure/devops/boards/work-items/workflow-and-state-categories?view=azure-devops
  * [5] Microsoft Learn — Scrum process workflow (Azure DevOps) https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/scrum-process-workflow?view=azure-devops
  * [7] Atlassian Support — Jira Align statuses https://support.atlassian.com/jira-align/docs/statuses/
  * [8] Microsoft Support — Link tasks with dependencies in Project https://support.microsoft.com/en-us/office/link-tasks-in-a-project-b58d8d3b-091e-4f00-a971-0d2ed8408b3c
  * [9] Project-Management-Basics (PRINCE2 tolerances summary) https://www.project-management-basics.com/prince2-tolerance/
  * [10] Atlassian — RACI template https://www.atlassian.com/team-playbook/plays/raci
  * [11] Microsoft DevBlogs — Azure Boards + Pipelines traceability https://devblogs.microsoft.com/devops/linking-azure-boards-work-items-to-deployments/
  * [12] RFC 8259 — The JavaScript Object Notation (JSON) Data Interchange Format https://www.rfc-editor.org/rfc/rfc8259
  * [13] YAML 1.2 Specification https://yaml.org/spec/1.2.2/
  * [14] GitHub Docs — Using YAML frontmatter https://docs.github.com/enterprise-cloud@latest/contributing/syntax-and-versioning-for-github-docs/using-yaml-frontmatter
  * [15] Jekyll Docs — Front Matter https://jekyllrb.com/docs/front-matter/
  * [16] Atlassian Support — Link issues to other issues https://support.atlassian.com/jira-cloud-administration/docs/link-issues-to-other-issues/
  * [17] PRINCE2 dependency (internal/external) summary https://www.project-management-basics.com/project-dependency/
  * [18] Azure DevOps Labs — Track dependencies across teams (Delivery Plans) https://azuredevopslabs.com/labs/azuredevops/deliveryplans/
