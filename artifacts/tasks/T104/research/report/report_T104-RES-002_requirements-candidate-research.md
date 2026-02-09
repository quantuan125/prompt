---
artifact_type: 'REPORT'
initiative_id: 'T104'
epic_id: 'T104'
research_id: 'T104-RES-002'
version: '1.0.0'
iteration: '1'
date: '2026-02-02'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
brief_reference: 'prompt/artifacts/tasks/T104/research/brief/brief_T104-RES-002_requirements-candidate-research.md'
report_template: 'prompt/templates/researcher/template_research_report.md'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
---

# RESEARCH REPORT: Requirements Candidate Research (T104-RES-002)

## I. EXECUTIVE SUMMARY

**Context**: SPS Section III.B.2–III.B.11 in `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` is structurally scaffolded but substantively empty (placeholders only). Without a structured candidate register grounded in internal decisions and aligned to T102 governance (ID spec, research index, issues/risks), the upcoming AC002 cross-category consultation risks being ad-hoc and incomplete.

**Verdict**: **CONDITIONAL GO** — proceed to AC002 consultation using the candidate register in Topic 8, but treat two governance conflicts as explicit consultation agenda items:
1) Initiative-scope `INT` token mismatch (template includes it; `T102-STD-005` disallows it at Initiative scope).
2) `T102-DEP-003 (Role Definitions)` is referenced but not defined in the inspected T102 SPS content, which blocks clean “adopt/align” mapping.

**Key Findings**:
* **Finding 1 (III.B is empty but not “unknown”)**: multiple confirmed decisions and plans imply concrete initiative-level candidates across `ASSUM/CON/QG/DEP/IF/STD/NOTE/RES` even though III.B is blank today. Evidence: `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md`, `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST000.md`, `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST001.md`, `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST002.md`.
* **Finding 2 (T104 must explicitly adopt T102 governance standards)**: T104 depends on T102’s governance stack (IDs, research indexing, decision record schemas, inheritance discipline). At minimum, `T102-STD-005` and `T102-STD-006` are hard constraints on how T104 authors IDs and research artifacts. Evidence: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`.
* **Finding 3 (External grounding supports the T104 artifact set)**: PRINCE2 and PMI/PMBOK describe a stable set of management products / process-group artifacts for initiation and planning that broadly correspond to T104’s tool surfaces (plan/roadmap, stage-gate approval packets, logs, issue/risk registers, communications approach). External references (web):
  - PRINCE2 management products overview and product descriptions: https://prince2.wiki/management-products/
  - PRINCE2 management products list (Project Brief, Stage Plan, Highlight Report, etc.): https://www.whatisprince2.net/prince2-products/
  - PMI process groups overview (Initiating / Planning etc.): https://www.pmi.org/learning/library/project-management-process-groups-brief-introduction-10384
  - PMI overview of a project charter (initiating artifact): https://www.pmi.org/learning/library/project-charter-what-is-6374
  - UK Design Council Double Diamond (Discover/Define framing): https://www.designcouncil.org.uk/our-work/skills-learning/tools-frameworks/the-double-diamond/
  - “Keep a Changelog” (delta-only changelog convention): https://keepachangelog.com/
* **Finding 4 (Agentic orchestration patterns reinforce T104 needs)**: Modern LLM-agent workflows consistently rely on (a) tool-calling/structured outputs, (b) explicit state/memory, (c) retrieval/traceability discipline, and (d) handoff protocols. These map directly to T104’s Roadmap/Plan/Notes/Research/Analysis surfaces and reinforce the need for deterministic schemas. External references (web):
  - ReAct (reason+act agent pattern): https://arxiv.org/abs/2210.03629
  - LangChain agents (tool-using agent orchestration patterns): https://python.langchain.com/docs/concepts/agents/
  - OpenAI Function calling / structured outputs (tool contracts): https://platform.openai.com/docs/guides/function-calling
  - OpenAI Structured Outputs (schema-constrained output): https://platform.openai.com/docs/guides/structured-outputs

**Candidate register summary (counts; all “candidate — to be validated in AC002”)**:
- ASSUM: 2
- CON: 4
- QG: 5
- DEP: 5
- IF: 5
- STD: 3
- IG: 2
- INT: 0 (see `T104-ISSUE-005`)
- RES: 2
- NOTE: 3
- ISSUE: 6 (incl. inherited)
- RISK: 5 (incl. inherited)

**Epic assessment verdict**:
- T104A KEEP; T104B KEEP; T104C KEEP; T104D KEEP; T104E KEEP (explicitly cross-cutting); T104F KEEP; T104G DEFER (until scoped).

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Followed brief Topics 1–8; repo-first evidence for internal claims; candidates are “to be validated” only; no SSOT modifications performed.

**Source of Truth Audit**:
* **Canonical ID and scope rules**:
  * `python3 prompt/skills/t102-std-005-id-spec/scripts/print_t102_adr_005.py`
* **Issues & risks schema**:
  * `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` (`T102-STD-007`)
* **T104 current state**:
  * `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`
  * `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001.md`
  * `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST001.md`
  * `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST002.md`
  * `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST001.md`
  * `prompt/artifacts/tasks/T104/raw/raw_T104-CWS_2026-02-02_p3.txt`
* **Prior research (informative)**:
  * `prompt/artifacts/tasks/T104/research/report/report_T104-RES-001_agentic-workspace-assessment.md`
  * `prompt/artifacts/tasks/T104/workspace/analysis/analysis_T104-RES-001_agentic-workspace-assessment.md`

**Limitations**:
* The commissioned brief file is dated `2026-02-03` while this report is authored `2026-02-02`; this report treats the brief as “latest available artifact in repo” and flags any timing-sensitive discrepancies.
* External research was conducted via public web sources; they provide grounding and terminology alignment, but do not override adopted project governance (T102 standards + ADRs).

---

## III. TOPIC FINDINGS

### Topic 1: SPS III.B.2–III.B.11 Gap Analysis (P1)
**Objective**: Systematically compare each SPS III.B category against internal evidence to identify implied candidates.

#### A. Evidence & Forensics
* **Source**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (III.B.2–III.B.11 are present but empty: `T104-ASSUM-001 —`, `T104-CON-001 —`, empty standards/research/issues tables).
* **Source**: `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md` (locked decisions: SSOT location, naming prefix policy, hierarchy semantics).
* **Source**: `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST001.md` (SES002 decisions: role boundaries merged into `T104-STD-001`, planner optionality, activity plan template deferral).

#### B. Analysis
**Gap matrix (initiative scope III.B)**:

| III.B Section | Current State | Source Evidence | Candidate Count |
|:--|:--|:--|--:|
| III.B.2 Assumptions (`ASSUM`) | Placeholder list only | SES002 DEC002 (planner optionality) | 2 |
| III.B.3 Constraints (`CON`) | Placeholder list only | Phase0 decisions + T102 CON inheritance | 4 |
| III.B.4 Quality Goals (`QG`) | Placeholder list only | T104 problem statement + T102 QGs + agentic drift risks | 5 |
| III.B.5 Dependencies (`DEP`) | Placeholder list only | T102 DEP set + research/consultation gating | 5 |
| III.B.6 Interfaces (`IF`) | Placeholder list only | T102 IF set + T104 gate/handoff needs | 5 |
| III.B.7 Project Standards (`STD`) | Empty STD table | ST002 plan names `T104-STD-001..003` | 3 |
| III.B.8 Development Guidances (`IG/INT`) | Placeholder only | IG needed; INT scope conflict | 2 (IG) / 0 (INT) |
| III.B.9 Research (`RES`) | Empty research table | RES-001 exists; RES-002 brief exists | 2 |
| III.B.10 Notes (`NOTE`) | Empty | Clarifiers needed: INT scope, deferrals, “thin roadmap” | 3 |
| III.B.11 Issues & Risks | Empty tables | Inherited issues/risks + new conflicts | 6 / 5 |

#### C. Governance Implication
* AC002 consultation can be structured as “validate and wordsmith candidates” rather than “discover categories from scratch”.
* The `INT` scope mismatch must be resolved before any initiative-level `T104-INT-*` IDs are created.

---

### Topic 2: T102 Cross-Integration Inventory (P1)
**Objective**: Identify T102 standards, interfaces, and dependencies T104 must reference/adopt/align with.

#### A. Evidence & Forensics
* **Source**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (T102 `STD`, `DEP`, `IF` declarations).
* **Source**: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` (`T102-STD-006` research index; `T102-STD-007` issues/risks index).

#### B. Analysis
**Cross-reference table (T102 → T104)**:

| T102 Item | T104 Impact | Dependency Type | Timing Risk |
|:--|:--|:--|:--|
| `T102-STD-005 (ID Governance Standard)` | Controls all candidate ID/token construction and reference semantics in T104 | adopts | Low |
| `T102-STD-006 (Research Workflow Standard)` | Controls how T104 research is indexed (SPS tables + Concept aggregation register) | adopts | Medium (T104 Concept register is scaffold today) |
| `T102-STD-005 (ID Specification & Rules)` | Canonical authority for scope/token rules, incl. `INT` scope limits | adopts | Low |
| `T102-STD-006 (Research Artifacts Index)` | Canonical spec for research index schema and placement | adopts | Medium |
| `T102-STD-007 (Issues & Risks Index)` | Canonical schema/enums for issues and risks tables | adopts | Low |
| `T102-IF-001..004` | Defines handoffs, client review, collaboration boundaries, co-authoring | aligns-with/extends | Medium |
| `T102-DEP-001 (Client Engagement)` | SLA expectations for decision-owner review cadence | adopts | Medium |
| `T102-DEP-002 (Planner Integration)` | Planner system integration constraint (even if planner optional today) | aligns-with | High |
| `T102-DEP-003 (Role Definitions)` | Referenced in T102 but not defined in inspected files | gap | High |

#### C. Governance Implication
* Where T104 templates diverge from `T102-STD-005` (initiative `INT`), treat it as an explicit issue (`T104-ISSUE-005`) and decision point in AC002.

---

### Topic 2b: Existing Decisions & Commitments Extraction (P1)
**Objective**: Mine consultation records for already-decided items that should become formal IID candidates.

#### A. Evidence & Forensics
* **Source**: `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md` (locked decisions: SSOT location, naming prefixes, hierarchy semantics).
* **Source**: `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST001.md` (SES002 DEC001–DEC007).

#### B. Analysis
**Extraction table (decision → implied candidate)**:

| Decision / OQ | Implied IID Category | Proposed Candidate ID | Evidence |
|:--|:--|:--|:--|
| SSOT location locked | CON | `T104-CON-002` | `notes_T104-CWS_phase0.md` |
| Notes prefix policy (`notes_...`, avoid `log_...`) | CON | `T104-CON-004` | `notes_T104-CWS_phase0.md` |
| Role boundaries merged into `T104-STD-001` | STD | `T104-STD-001` | `notes_T104-PH001-ST001.md` |
| LLM_Planner optionality | ASSUM | `T104-ASSUM-001` | `notes_T104-PH001-ST001.md` |
| Activity plan template deferred | NOTE | `T104-NOTE-002` | `notes_T104-PH001-ST001.md` |
| “Thin roadmap” discipline | NOTE/QG | `T104-NOTE-003`, `T104-QG-005` | `roadmap_T104-CWS.md` |

#### C. Governance Implication
* These candidates are already “implicitly decided”; AC002 should validate wording and promote into SPS as formal entries rather than re-deciding foundational decisions.

---

### Topic 3: Traditional PM Tools & Documents Mapping (P1)
**Objective**: Map T104 epics to industry-standard PM artifacts (PRINCE2, PMI/PMBOK) and discovery/define artifacts.

#### A. Evidence & Forensics
* **Source**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (T104A–T104G epics; intended artifact roles).
* **Source**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (T102 frames “Initiative Considerations” against industry standards).

#### B. External References (web)
* PRINCE2 management products (overview): https://prince2.wiki/management-products/
* PRINCE2 products list and descriptions: https://www.whatisprince2.net/prince2-products/
* PMI process groups overview: https://www.pmi.org/learning/library/project-management-process-groups-brief-introduction-10384
* PMI project charter overview: https://www.pmi.org/learning/library/project-charter-what-is-6374
* Design Council Double Diamond: https://www.designcouncil.org.uk/our-work/skills-learning/tools-frameworks/the-double-diamond/
* Keep a Changelog (convention): https://keepachangelog.com/

#### C. Analysis (mapping table)

| T104 Epic | Epic Code | PRINCE2 Equivalent(s) | PMI/PMBOK Equivalent(s) | Discovery/Define Equivalent(s) | Coverage Notes |
|:--|:--|:--|:--|:--|:--|
| T104A | ROADMAP | Project Plan / Stage Plan / Product-based planning (as a “spine”) | High-level roadmap + planning artifacts across Initiating/Planning | Discovery/Define orchestration surface | Strong fit if kept “thin pointer-based” |
| T104B | NOTES | Lessons Log / Daily Log / meeting minutes (non-normative) | Team comms records; decision capture supports governance | Session minutes / decision log | Strong fit if “promote decisions to SSOT” is enforced |
| T104C | PROPOSAL | Stage Boundary / exception handling packet; change proposal | Approvals at process-group boundaries; change request package | Define-phase approval packet | Strong fit for explicit gate checks |
| T104D | ANALYSIS | Business Case / options analysis inputs | Business analysis, alternatives, trade-offs feeding plans | Options analysis; recommendation memo | Strong fit; anchors “why” behind decisions |
| T104E | CHANGELOG | Configuration item history / change control records | Change control + baselined artifacts history | Artifact version delta log | Strong as cross-cutting; use “delta-only” convention (Keep a Changelog) |
| T104F | PLAN | Stage Plan / Work Package coordination | Project management plan + subsidiary plans (scope/schedule/risk/comms) | Execution coordination plan | Strong; complements thin roadmap |
| T104G | COMMUNICATION | Communication Management Approach/Strategy | Communications Management Plan / stakeholder engagement | Comms strategy | Currently underspecified; likely defer until scoped |

#### D. Recommendation (tied to candidates)
* Retain the 7-epic set but explicitly defer `T104G` unless/until a concrete “communication management approach” deliverable is specified (Topic 7).
* Add explicit initiative `IF`/`STD` candidates to cover status reporting and gate approval signals (Topic 8: `T104-IF-001`, `T104-IF-004`, `T104-STD-003`).

---

### Topic 4: LLM Agentic-Specific Workflow Tools (P1)
**Objective**: Survey emerging agentic workflow patterns and assess whether T104 covers them.

#### A. Evidence & Forensics
* **Source**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (multi-role workflow, deterministic retrieval as desired outcome).
* **Source**: `prompt/artifacts/tasks/T104/research/report/report_T104-RES-001_agentic-workspace-assessment.md` (drift/retrieval failure risks).

#### B. External References (web)
* ReAct: Synergizing reasoning and acting in language models: https://arxiv.org/abs/2210.03629
* LangChain agents (concepts): https://python.langchain.com/docs/concepts/agents/
* OpenAI function calling (tool contracts): https://platform.openai.com/docs/guides/function-calling
* OpenAI structured outputs (schema constrained): https://platform.openai.com/docs/guides/structured-outputs

#### C. Analysis (agentic pattern categories → T104 mapping)
1) **Tool contracts / structured outputs**
   - Pattern: agent outputs are constrained by schemas; tool calls encode “intent” and “payload”.
   - T104 relevance: drives need for deterministic table schemas and stable IDs so agents can reliably parse and route information.
   - Candidate linkage: `T104-QG-001`, `T104-QG-002`, `T104-IF-*`, `T104-IG-001`.

2) **State + memory discipline**
   - Pattern: agents rely on durable state surfaces (notes/logs/registers) to avoid context loss; without this, they re-derive and duplicate content.
   - T104 relevance: “Notes as session continuity” + “Research brief/report indexed” + “Roadmap as pointer spine” are determined state surfaces.
   - Candidate linkage: `T104-STD-001`, `T104-RES-001`, `T104-RES-002`, `T104-CON-001`.

3) **Retrieval-augmented navigation / link integrity**
   - Pattern: retrieval depends on stable filenames, prefixes, and links; broken links cause hallucinated locations and duplication.
   - T104 relevance: “deterministic retrieval” is a core desired outcome; link register policies become governance, not “nice-to-have”.
   - Candidate linkage: `T104-IG-001`, `T104-CON-004`, `T104-QG-001`, `T104-ISSUE-003`, `T104-RISK-003`.

4) **Handoff protocols**
   - Pattern: role-to-role handoffs need explicit boundary + acknowledgment to prevent ownership ambiguity and rework.
   - T104 relevance: role boundaries are already planned as `T104-STD-001` clauses; interfaces should be explicit at initiative scope.
   - Candidate linkage: `T104-IF-002`, `T104-IF-003`, `T104-DEP-004`.

#### D. Recommendation (tied to candidates)
* Add an explicit “status reporting” interface candidate (`T104-IF-004`) rather than relying on informal notes patterns; this aligns with PRINCE2 Highlight Report / PM status communications without creating a new epic.

---

### Topic 5: Interface, Dependency & Integration Patterns (P2)
**Objective**: Identify common interface/dependency patterns across PM + agentic workflows relevant to T104.

#### A. Evidence & Forensics
* **Source**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-IF-001..004`, `T102-DEP-001..002`).
* **Source**: `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS.md` (“thin roadmap” rule + Links Register).

#### B. Analysis (pattern catalogue)
* **Gate approval interface**: “decision owner approval signal” must be captured in a deterministic place (plan/SSOT sign-off areas) → `T104-IF-001`, `T104-STD-003`.
* **Research index interface**: brief/report must be indexable and linkable for auditability → `T104-DEP-002`, `T104-RES-001`, `T104-RES-002`.
* **Planner handoff interface**: must support optional planner today but preserve future integration path → `T104-IF-002`, `T104-DEP-004`.

#### C. Recommendation (tied to candidates)
* Treat “interfaces” as explicit initiative `IF` items rather than burying them in prose; this supports future machine validation.

---

### Topic 6: Issues & Risks Landscape (P2)
**Objective**: Update issues/risks beyond RES-001 given current project state.

#### A. Evidence & Forensics
* **Source**: inherited items listed in `brief_T104-RES-002_requirements-candidate-research.md` (T104-ISSUE-001..004, T104-RISK-001..003).
* **New evidence**:
  - `T102-STD-005` explicitly disallows initiative-scope `INT` (scope mismatch with SPS template).
  - `T102-DEP-003` referenced without definition in `sps_T102-CONSULTANT.md` (as inspected).

#### B. Recommendation
* Surface the new issues/risks as explicit consultation agenda items; do not silently “pick a side”.

---

### Topic 7: Epic Appropriateness Assessment (P1)
**Objective**: Keep/Defer/Merge/Remove recommendation per epic.

| Epic | Code | Recommendation | Rationale | Impact if Deferred | Dependencies |
|:--|:--|:--|:--|:--|:--|
| T104A | ROADMAP | KEEP | Core orchestration spine; prerequisite for deterministic navigation | High | `T104-IG-001`, `T104-STD-001` |
| T104B | NOTES | KEEP | Session continuity surface prevents SSOT pollution | Medium | `T104-STD-001` (role boundaries) |
| T104C | PROPOSAL | KEEP | Gate-check approval packet supports define-phase decisions | Low | `T104-STD-003` |
| T104D | ANALYSIS | KEEP | Synthesis bridge (research → proposal) is validated by RES-001 analysis artifact | Medium | `T104-DEP-002` |
| T104E | CHANGELOG | KEEP (cross-cutting) | Cross-cutting but essential for delta-only trace; do not force retroactive migrations | Low–Medium | `T104-CON-003` |
| T104F | PLAN | KEEP | Execution coordination prevents roadmap bloat; already part of Phase 1 | High | `T104-STD-001` |
| T104G | COMMUNICATION | DEFER | Underspecified purpose/scope; high scope-creep risk | Low | Needs concrete deliverables and interfaces |

---

### Topic 8: Candidate IID Register (P1)
**Objective**: Synthesize Topics 1–7 into a draft candidate IID register conforming to `T102-STD-005`.

#### III.B.2 — Project Assumptions (ASSUM)

**ASSUM Validation Lifecycle Summary (candidates)** (per `T102-STD-005-CLAUSE-005A`)

| ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
|:---|:--|:--|:--|:--|:--|:--|:--|
| `T104-ASSUM-001` | Planner Optionality | Pending | Validate via PH001 delivery: confirm ST001 + ST002 can be executed without mandatory planner role | PH001 | `LLM_Consultant` | Mitigation | `T104-CON-003` |
| `T104-ASSUM-002` | Forward-only Adoption | Pending | Validate via PH001: confirm standards adoption does not require bulk legacy migrations | PH001–PH002 | `LLM_Consultant` | Fallback | `T104-CON-003` |

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-ASSUM-001` | Planner Optionality | LLM_Planner involvement is optional by default and triggered only by complexity thresholds to be codified in `T104-STD-001`. | 2b | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST001.md` | candidate — to be validated in AC002 |
| `T104-ASSUM-002` | Forward-only Adoption | Standards and naming conventions can be adopted forward-only without immediate bulk migration. | 2b | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (T104E “define-only”) | candidate — to be validated in AC002 |

#### III.B.3 — Project Constraints (CON)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-CON-001` | Link Don’t Duplicate | Artifacts should link by ID/path rather than duplicating normative content across workflow tools and SSOT. | 1 | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` | candidate — to be validated in AC002 |
| `T104-CON-002` | Markdown Frontmatter | Artifacts remain Markdown with YAML frontmatter for toolability and review. | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-CON-001`) | candidate — to be validated in AC002 |
| `T104-CON-003` | No Retroactive Migration | Avoid retroactive bulk renames/migrations outside explicitly scoped refactor work; prefer forward-only conformance. | 2b | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (T104E scope) | candidate — to be validated in AC002 |
| `T104-CON-004` | Prefix Discipline | Enforce deterministic file prefixes for artifact types (e.g., `roadmap_`, `plan_`, `notes_`, `changelog_`, `handoff_brief_`) to reduce retrieval ambiguity. | 2b | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-CWS_phase0.md` | candidate — to be validated in AC002 |

#### III.B.4 — Quality Goals (QG)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-QG-001` | Deterministic Retrieval | Naming + placement enable deterministic agent/human retrieval with minimal ambiguity. | 1 | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` (desired outcome) | candidate — to be validated in AC002 |
| `T104-QG-002` | Traceability Integrity | Cross-artifact links and IDs support end-to-end traceability without duplication drift. | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-QG-002`) | candidate — to be validated in AC002 |
| `T104-QG-003` | Client Readability | Governance artifacts remain executive-readable and scannable. | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-QG-001`) | candidate — to be validated in AC002 |
| `T104-QG-004` | Low Disruption | Prefer adoption that minimizes author retraining and churn in early phases. | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-QG-003`) | candidate — to be validated in AC002 |
| `T104-QG-005` | Thin Spine | Roadmap remains pointer-based (“thin spine”), with execution detail living in plans/notes, to prevent bloat and drift. | 2b | `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS.md` | candidate — to be validated in AC002 |

#### III.B.5 — Dependencies (DEP)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-DEP-001` | T102 Standards Stack | T104 adopts explained T102 governance standards (IDs, ADRs, research indexing, issues/risks schemas). | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` | candidate — to be validated in AC002 |
| `T104-DEP-002` | Research Workflow | Formal research follows `T102-STD-006` indexing rules (brief+report gated and indexed). | 2 | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` (`T102-STD-006`) | candidate — to be validated in AC002 |
| `T104-DEP-003` | Client Engagement | Decision-owner review cadence is an initiative dependency at gates. | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-DEP-001`) | candidate — to be validated in AC002 |
| `T104-DEP-004` | Planner Integration | Maintain compatibility with future planner system consuming handoff schemas (even if planner optional today). | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-DEP-002`) | candidate — to be validated in AC002 |
| `T104-DEP-005` | Template Alignment | T104 SPS structure and token scopes remain aligned to canonical T102 ADRs (avoid local drift). | 2 | `python3 prompt/skills/t102-std-005-id-spec/scripts/print_t102_adr_005.py` | candidate — to be validated in AC002 |

#### III.B.6 — Interfaces (IF)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-IF-001` | Client Review | Gate approvals record decision-owner review signals consistently across plans/SSOT. | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-IF-002`) | candidate — to be validated in AC002 |
| `T104-IF-002` | Planner Handoff | Define a minimal handoff bundle interface between consultancy artifacts and downstream planning (incl. acknowledgment). | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-IF-001`) | candidate — to be validated in AC002 |
| `T104-IF-003` | Co-authoring Protocol | Define co-authoring rhythm and repo-as-SSOT behavior for consultant+client collaboration. | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-IF-004`) | candidate — to be validated in AC002 |
| `T104-IF-004` | Status Reporting | Define a minimal status/reporting surface (where status lives, cadence, and how it links to plans/roadmaps) to reduce ad-hoc “status in notes” drift. | 3/4 | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST000.md` (status reporting deferred), external grounding: PRINCE2 Highlight Report concept | candidate — to be validated in AC002 |
| `T104-IF-005` | Role Collaboration | Define collaboration boundary between Consultant/Planner/Developer for change ownership and clarification loops. | 2 | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (`T102-IF-003`) | candidate — to be validated in AC002 |

#### III.B.7 — Project Standards (STD)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-STD-001` | Planning Hierarchy | Adopt a normative planning hierarchy and role-boundary clauses for Consultant/Planner/Developer. | 2b | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST002.md` | candidate — to be validated in AC002 |
| `T104-STD-002` | UID Convention | Define timeline UID conventions and naming/link patterns supporting deterministic navigation. | 2b | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST002.md` | candidate — to be validated in AC002 |
| `T104-STD-003` | Gate Definition | Define phase gate schema (entry/exit criteria, evidence, approver) for baseline approvals. | 2b | `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001-ST002.md` | candidate — to be validated in AC002 |

#### III.B.8 — Development Guidances (IG / INT)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-IG-001` | Links Register | Define a minimum cross-link policy using the Roadmap Links Register as navigation spine. | 4 | `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS.md` | candidate — to be validated in AC002 |
| `T104-IG-002` | Research Linking | Provide a short “how to link research” guidance: Brief → Report → Analysis → consuming IDs (link-don’t-duplicate). | 2/5 | `prompt/artifacts/tasks/T104/workspace/analysis/analysis_T104-RES-001_agentic-workspace-assessment.md` | candidate — to be validated in AC002 |
| — | None Identified | Initiative-scope `INT` is not allowed per `T102-STD-005-CLAUSE-002` (allowed scopes: E/F/S). | 1 | `python3 prompt/skills/t102-std-005-id-spec/scripts/print_t102_adr_005.py` | candidate — to be validated in AC002 |

#### III.B.9 — Research (RES)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-RES-001` | Agentic Workspace Assessment | Formal research delivered; should be indexed in SPS III.B.9 with brief+report. | 1 | `prompt/artifacts/tasks/T104/research/report/report_T104-RES-001_agentic-workspace-assessment.md` | candidate — to be validated in AC002 |
| `T104-RES-002` | Requirements Candidate Research | Formal research commission; brief exists; report (this file) should be indexed in SPS III.B.9. | 1 | `prompt/artifacts/tasks/T104/research/brief/brief_T104-RES-002_requirements-candidate-research.md` | candidate — to be validated in AC002 |

#### III.B.10 — Notes (NOTE)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-NOTE-001` | INT Scope | Clarify that initiative-level “Integration Guidance” should not create `T104-INT-*` unless/until scope rules are reconciled; prefer `IG` at initiative scope. | 1 | `prompt/templates/consultant/sps/sps_structural_template.md`, `python3 prompt/skills/t102-std-005-id-spec/scripts/print_t102_adr_005.py` | candidate — to be validated in AC002 |
| `T104-NOTE-002` | Plan Deferral | Activity plan template formalization and step IDs are deferred to a future initiative alongside the LLM_Planner system; Phase 1 uses a skeleton only. | 2b | `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST001.md` | candidate — to be validated in AC002 |
| `T104-NOTE-003` | Changelog Discipline | Changelog entries are delta-only and should follow “keep a changelog” style to prevent narrative logs. | 3 | https://keepachangelog.com/ | candidate — to be validated in AC002 |

#### III.B.11 — Issues & Risks (ISSUE / RISK)

| Candidate ID | Title | Description | Source (Topic #) | Evidence | Validation Status |
|:--|:--|:--|:--|:--|:--|
| `T104-ISSUE-001` | Governance Rules Misalignment | Governance rules conflict with T104 semantics. | 6 | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` | candidate — to be validated in AC002 |
| `T104-ISSUE-002` | Notes Template Drift | Notes template semantics drift vs T104 NOTES usage. | 6 | `report_T104-RES-001_agentic-workspace-assessment.md` | candidate — to be validated in AC002 |
| `T104-ISSUE-003` | Naming Inconsistency | Case/suffix drift undermines deterministic retrieval. | 6 | `report_T104-RES-001_agentic-workspace-assessment.md` | candidate — to be validated in AC002 |
| `T104-ISSUE-004` | Missing Analysis Artifact | Analysis artifacts must exist for research commissions; enforce pattern. | 6 | `analysis_T104-RES-001_agentic-workspace-assessment.md` | candidate — to be validated in AC002 |
| `T104-ISSUE-005` | INT Scope Mismatch | Initiative `INT` scope mismatch (template vs `T102-STD-005`). | 6 | `python3 prompt/skills/t102-std-005-id-spec/scripts/print_t102_adr_005.py` | candidate — to be validated in AC002 |
| `T104-ISSUE-006` | T102 DEP-003 Undefined | `T102-DEP-003` referenced but not defined in inspected T102 SPS file. | 6 | `sps_T102-CONSULTANT.md` (references) | candidate — to be validated in AC002 |
| `T104-RISK-001` | Duplication Drift | Drift via duplication across artifacts. | 6 | inherited | candidate — to be validated in AC002 |
| `T104-RISK-002` | Hidden Gate Layer | Streams/subphases may be misused as hidden gates. | 6 | inherited | candidate — to be validated in AC002 |
| `T104-RISK-003` | Retrieval Failures | Naming inconsistency causes retrieval failures for agents. | 6 | inherited | candidate — to be validated in AC002 |
| `T104-RISK-004` | Category Drift | Invalid initiative `INT` IDs may enter SPS baseline. | 6 | derived from `T104-ISSUE-005` | candidate — to be validated in AC002 |
| `T104-RISK-005` | Consultation Overload | Too many unresolved governance conflicts may reduce decision quality. | 6 | `notes_T104-PH001-ST001.md` (OQ re additional STDs) | candidate — to be validated in AC002 |

---

## IV. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `HIGH, MEDIUM, LOW`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T104-ISSUE-001` | Governance Rules Misalignment | `workspace_documentation_rules.md` defines Plan/Proposal/Completion roles conflicting with T104 Roadmap/Notes/Changelog semantics | LLM_Consultant | `OPEN` | `HIGH` | 2026-01-18 | — | — |
| `T104-ISSUE-002` | Notes Template Drift | Notes template uses LOG/Subphase semantics inconsistent with T104 initiative NOTES usage | LLM_Consultant | `OPEN` | `HIGH` | 2026-01-18 | — | — |
| `T104-ISSUE-003` | Naming Inconsistency | Case and suffix drift across artifacts (toolability risk) | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-01-18 | — | — |
| `T104-ISSUE-004` | Missing Analysis Artifact | Analysis artifact coverage is incomplete across research commissions (RES-001 has analysis; ensure pattern for RES-002 onward) | LLM_Consultant | `IN-REVIEW` | `HIGH` | 2026-01-18 | `prompt/artifacts/tasks/T104/workspace/analysis/analysis_T104-RES-001_agentic-workspace-assessment.md` exists; confirm whether RES-002 requires companion analysis artifact and standardize expectation in `T104-IG-002` or `T104-STD-001` clauses | — |
| `T104-ISSUE-005` | INT Scope Mismatch | Initiative-scope `INT` appears in SPS template but is disallowed at initiative scope per `T102-STD-005-CLAUSE-002` | LLM_Consultant | `OPEN` | `HIGH` | 2026-02-02 | — | — |
| `T104-ISSUE-006` | T102 DEP-003 Undefined | `T102-DEP-003 (Role Definitions)` referenced in T102 SPS but no definition found in inspected T102 SPS content | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-02 | — | — |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `HIGH, MEDIUM, LOW`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T104-RISK-001` | Duplication Drift | Drift via duplication across workflow tool artifacts | LLM_Consultant | `OPEN` | `HIGH` | 2026-01-18 | — | — |
| `T104-RISK-002` | Hidden Gate Layer | Stream/Subphase reintroduced as hidden governance gate | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-01-18 | — | — |
| `T104-RISK-003` | Retrieval Failures | Tooling retrieval failures due to naming inconsistency | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-01-18 | — | — |
| `T104-RISK-004` | Category Drift | Invalid initiative `INT` IDs may be created and embedded into SPS baseline if scope conflict is not resolved | LLM_Consultant | `OPEN` | `HIGH` | 2026-02-02 | — | — |
| `T104-RISK-005` | Consultation Overload | Unresolved governance conflicts reduce AC002 decision quality and completeness | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-02 | — | — |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `sps_T104-CWS.md` | III.B.2–III.B.11 | Populate with validated candidates during AC002 (no silent placeholders) | Topic 8 tables |
| `sps_T104-CWS.md` | III.B.9 Research | Add rows for `T104-RES-001` and `T104-RES-002` with brief/report links | Topic 8 (RES) |
| `sps_T104-CWS.md` | III.B.11 Issues & Risks | Add inherited + new issues/risks using `T102-STD-007` schema/enums | Section IV |
| `concept_T104-CWS.md` | E.3 Research Artifacts Register | Populate later per `T102-STD-006` after adopting the pattern (dual-layer indexing) | Topic 2 / `T104-DEP-002` |

---

## VI. SOURCE MATERIAL

* **Brief Version Used**: `prompt/artifacts/tasks/T104/research/brief/brief_T104-RES-002_requirements-candidate-research.md` (version 1.0.0; dated 2026-02-03)
* **External sources (web)**:
  * https://prince2.wiki/management-products/
  * https://www.whatisprince2.net/prince2-products/
  * https://www.pmi.org/learning/library/project-management-process-groups-brief-introduction-10384
  * https://www.pmi.org/learning/library/project-charter-what-is-6374
  * https://www.designcouncil.org.uk/our-work/skills-learning/tools-frameworks/the-double-diamond/
  * https://keepachangelog.com/
  * https://arxiv.org/abs/2210.03629
  * https://python.langchain.com/docs/concepts/agents/
  * https://platform.openai.com/docs/guides/function-calling
  * https://platform.openai.com/docs/guides/structured-outputs
* **Internal files cited (key)**:
  * `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`
  * `prompt/artifacts/tasks/T104/workspace/roadmap/roadmap_T104-CWS.md`
  * `prompt/artifacts/tasks/T104/workspace/plan/plan_T104-PH001.md`
  * `prompt/artifacts/tasks/T104/workspace/notes/notes_T104-PH001-ST001.md`
  * `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md`
  * `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
  * `prompt/skills/t102-std-005-id-spec/scripts/print_t102_adr_005.py`
