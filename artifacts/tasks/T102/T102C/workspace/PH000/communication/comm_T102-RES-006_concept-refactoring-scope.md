---
artifact_type: 'COMMUNICATION'
from_initiative: 'T102'
from_stream: 'T102-PH001-ST004-AC003'
to_epic: 'T102C'
to_owner: 'T102C LLM_Consultant (sub-consultant)'
date: '2026-02-10'
subject: 'T102-RES-006 Research Complete — Concept Refactoring Scope & T102C-PH000 Initialization Guidance'
priority: 'HIGH'
source_analysis: 'prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md'
source_report: 'prompt/artifacts/tasks/T102/research/T102-RES-006/report_T102-RES-006_concept-role-dynamic-registers.md'
---

# COMMUNICATION: T102 Initiative → T102C Epic — Concept Refactoring Scope & Phase Initialization

## I. PURPOSE

This communication provides the **T102C sub-consultant** with the comprehensive research-backed Concept refactoring scope that emerged from `T102-RES-006` (Concept Role + Dynamic SSOT Registers). The T102C epic has not yet initialized its planning state. This communication serves as:

1. The **architectural input** that enables T102C planning initialization
2. A **concrete task/goal inventory** derived from three research commissions (RES-004, RES-005, RES-006)
3. **Suggested planning structure** for T102C-PH000 (Phase 0: Planning & Scope Definition)

---

## II. RESEARCH CONTEXT — WHAT WAS DECIDED

Three research commissions in `T102-PH001-ST004` produced a coherent recommendation chain:

| Research | Core Question | Answer | Key Impact on T102C |
|:--|:--|:--|:--|
| **RES-004** | Where does I&R live? | SPS-only default; Concept = conditional aggregation surface | Concept MAY host I&R aggregation dashboard (pointers-only) |
| **RES-005** | How does cross-scope coordination work? | Hybrid: embedded minimum viable + Concept audit surface + INT promotion | Concept is the "coordination audit surface" — registers, drift indicators, navigation hub |
| **RES-006** | What role does Concept play? | Hub-first with thresholds (Option e, scored 4.40/5.00) | **Comprehensive Concept role specification** — default + conditional register families, authority tiers, strict exclusions |

### The Approved Concept Architecture: Option (e) — Hub-First with Thresholds

**Concept Role (operational definition)**:
- **Initiative bridge / process manual** — single referenced operating rules surface
- **Coordination audit surface** — cross-scope registers with pointers-only discipline
- **Handoff authority surface** — package manifest + acceptance signals (per T102C-STD-001)

**Authority Tiers**:

| Tier | Content Type | Governance Level |
|:--|:--|:--|
| 1. Normative bodies | Standards + nested ADR rationale | Authoritative — Concept links to canonical STD files |
| 2. Authoritative snapshots | Handoff package manifest + acceptance signals | Authoritative — Concept owns this content |
| 3. Audit registers | Pointers-only surfaces (metadata + IDs + links) | Non-normative — Concept aggregates; canonical bodies live elsewhere |

**Strict Exclusions** (Concept MUST NOT host):
- Full requirements bodies (Request owns)
- Full design bodies (Design owns)
- Duplicated research bodies (Research reports own)
- Canonical I&R tables (SPS owns)

---

## III. CONCEPT REFACTORING TASK INVENTORY

The following is a concrete inventory of refactoring tasks derived from RES-006 findings, organized by priority and complexity. The T102C sub-consultant should use this as the basis for their Phase 0 planning.

### Priority 1: Immediate Hygiene (No Architectural Decisions Required)

These tasks can be executed independently and should be done first to establish a reliable baseline.

| # | Task | Current State | Target State | Complexity | Evidence |
|:--|:--|:--|:--|:--|:--|
| H1 | **Repair Research Register (E.3) broken links** | References versioned filenames (`*_v1.0.0.md`) that don't exist | All links use canonical unversioned filenames; all resolve to existing files | LOW | RES-006 Topic 1, Topic 6; RES-005 Finding 4 |
| H2 | **Update Research Register Source paths** | Source column references versioned SPS filename | Source column references canonical SPS filename `../sps/sps_T102-CONSULTANT.md` | LOW | RES-006 Topic 6 |
| H3 | **Register RES-004, RES-005, RES-006 in Concept E.3** | Not registered | All three research commissions registered per STD-006 | LOW | ST004 TK004 tasks |
| H4 | **Add "Last Verified" + "Link Status" columns to E.3** | No drift indicators | Each register entry includes `Last Verified` (date) and `Link Status` (`OK`/`BROKEN`) | LOW | RES-006 Delta C1 |

### Priority 2: Structural — Default Register Families (Always Present)

These tasks implement the "default surfaces" of Option (e).

| # | Task | Current State | Target State | Complexity | Evidence |
|:--|:--|:--|:--|:--|:--|
| S1 | **Populate §III.A: Identity & Operating Rules** | Placeholder comment block | Single referenced process manual: operating rules, authority tiers, "pointers-only" policy, maintenance protocol, gate-time link-integrity check procedure | MEDIUM | RES-006 Topic 1, Topic 3 |
| S2 | **Create Workscope Register** | Does not exist | Pointers-only inventory: `Scope / Scope ID / Type / Name / Owner / Status / Canonical Artifact(s) / Last Verified` — seeded from SPS WBS map | MEDIUM | RES-006 Topic 5 |
| S3 | **Create File Register** | Does not exist | Key artifact → role mapping: `Artifact / Role / Canonical Path / Owner / Update Trigger / Last Verified` | MEDIUM | RES-006 Topic 5 |
| S4 | **Annotate Design Register as "pointers-only"** | Active but no explicit posture | Add explicit "pointers-only" annotation; clarify that Design Register links to story-level design logs and does not duplicate bodies | LOW | RES-006 Topic 1 |
| S5 | **Implement Readiness Snapshot** | Placeholder | Lean structured surface per T102C-STD-001-CLAUSE-003: YAML roll-up table with Initiative/Epic/Feature states, Ready markers, Top 3 blockers | MEDIUM | T102C-STD-001, RES-006 Topic 10 |
| S6 | **Implement Handoff Snapshot** | Placeholder | Lean package manifest per T102C-STD-001-CLAUSE-002: immutable IDs/versions, acceptance signals, completeness checklist, links to SPS/Request/Design | MEDIUM | T102C-STD-001, RES-006 Topic 10 |
| S7 | **Populate §III.F: Integration & Interfaces** | Placeholder | "How registers interact" guidance — embedded vs centralized vs INT boundaries, with explicit interaction model | LOW | RES-006 Topic 3 |
| S8 | **Populate §III.G: Governance** | Placeholder | Change-control policy: who can update registers, gate-time link-integrity protocol, "Last Verified" update cadence | LOW | RES-006 Topic 1 |

### Priority 3: Structural — Conditional Register Families (Trigger-Gated)

These tasks implement conditional surfaces. The T102C sub-consultant should plan them but execute only when triggers are met.

| # | Task | Trigger Condition | Current Trigger Status | Complexity | Evidence |
|:--|:--|:--|:--|:--|:--|
| C1 | **Create I&R Aggregation Register** | 2+ epics have open I&R items, OR avg age >90 days, OR Client requests staleness visibility | **Triggers 1+2 MET** (T102A/B/C all have I&R; Initiative avg age 98.4d) | MEDIUM | RES-006 Topic 7, RES-004 pattern (c) |
| C2 | **Create Overview Assets section** | Recurring onboarding question not answerable by registers alone | Not yet met | LOW | RES-006 Topic 8 |
| C3 | **Create Plans & Roadmaps mini-index** | Navigation need for plans exceeds current discoverability | Informally met (multiple stream plans exist) | LOW | RES-006 Topic 9 |

### Priority 4: Tooling Decision (Cross-Initiative)

| # | Task | Options | Recommendation | Complexity | Evidence |
|:--|:--|:--|:--|:--|:--|
| T1 | **ADR extraction alignment** | Path A: Restore ADR anchors in Concept / Path B: Retarget `extract_adr.py` to standards files | **Path B recommended** (lower drift, aligns with "link-don't-duplicate") | MEDIUM | RES-006 Topic 4; separate T103 communication issued |

---

## IV. SUGGESTED T102C-PH000 PLANNING STRUCTURE

The T102C epic does not yet have an initialized plan. Based on the research findings and the task inventory above, the following planning structure is suggested. The T102C sub-consultant has full authority to adapt this structure.

### Suggested Phase 0: Planning & Scope Definition

**Objective**: Initialize T102C planning by absorbing research inputs, defining the implementation scope, and producing a phased execution plan.

| Suggested Activity | Purpose | Inputs | Key Output |
|:--|:--|:--|:--|
| AC001: Absorb Research Inputs | Review RES-004/005/006 reports and integration analyses; confirm research findings are understood and accepted as architectural inputs | This communication + source materials listed below | Research absorption notes + confirmed task inventory |
| AC002: Define Implementation Scope | Map task inventory (Section III above) to T102C execution phases; identify dependencies on T102 STD amendments (ST005); define sequencing | Task inventory + ST005 plan + STD amendment dependencies | Scoped phase plan (T102C-PH001 or similar) |
| AC003: Client Approval Gate | Present implementation plan to Client for approval | Phase plan from AC002 | Client-approved T102C execution plan |

### Dependencies on T102 Initiative Streams

| T102 Stream | T102C Dependency | Nature |
|:--|:--|:--|
| **ST005-AC004** (Amend STD-001) | T102C should align with STD-001 amendments that redefine Concept's role | Non-blocking — T102C can start hygiene + structural work before STD-001 is amended; STD-001 amendment formalizes what T102C implements |
| **ST005-AC001** (Amend STD-007) | If C1 (I&R Aggregation Register) is adopted, STD-007 interaction clause (Delta D1) should be in place | Soft dependency — T102C can create the register, but the governance clause should exist before the register is treated as a governed surface |
| **ST005-AC002** (Amend STD-005) | Directionality exception (Delta B1) for audit registers should be formalized | Soft dependency — T102C can proceed with "pointers-only" practice before the formal exception is drafted |
| **ST005-AC003** (Amend STD-006) | "Last Verified" + "Link Status" schema extension should be reflected in STD-006 | Soft dependency — T102C can add these columns as good practice; STD-006 amendment formalizes the schema |

### Sequencing Recommendation

```
Phase 0 (Planning)
  └─ AC001: Absorb research inputs
  └─ AC002: Define implementation scope
  └─ AC003: Client approval gate
     │
Phase 1 (Execution) — suggested ordering:
  ├─ Priority 1: Immediate hygiene (H1-H4) — can start immediately
  ├─ Priority 2: Structural defaults (S1-S8) — start after hygiene
  │   ├─ S1 (Operating Rules) — foundational; do first
  │   ├─ S2-S3 (Workscope/File Registers) — low dependency
  │   ├─ S4, S7, S8 (annotations + placeholders) — low effort
  │   └─ S5-S6 (Readiness/Handoff) — per T102C-STD-001
  └─ Priority 3: Conditional (C1-C3) — gated on triggers
      └─ C1 (I&R Aggregation) — triggers already met; may start with P2
```

---

## V. KEY ARCHITECTURAL CONSTRAINTS

The T102C sub-consultant must observe these constraints (derived from RES-006 + prior research):

1. **Pointers-only discipline**: All Concept registers aggregate metadata + IDs + links. Never duplicate canonical bodies.
2. **"Link-don't-duplicate" principle**: When information exists in a canonical artifact (SPS, Request, standards, research reports), Concept links to it rather than copying it.
3. **"Last Verified" on every register**: Each register row includes `Owner` + `Last Verified` (date) to enable manual drift detection.
4. **Gate-time link integrity**: Link integrity is checked at gates (manual checklist); this is a governance procedure, not an automation requirement.
5. **Authority tiers must be explicit**: Every Concept section should declare whether its content is normative, authoritative snapshot, or audit register (non-normative).
6. **Conditional surfaces require trigger evidence**: Before adding a conditional register family, document which trigger(s) are met and record the evidence.
7. **Gate construction**: All activities that include gates MUST follow the gate rules defined in `prompt/templates/consultant/workspace/guideline_workspace_plan.md` (Section VI: Gate Rules). Gates require explicit Entry Criteria, Reviewer, and Exit Criteria fields. Gates appear in the Task Register as special rows with `planned`/`completed`/`failed` status. Gates MUST NOT be used as tasks; tasks MUST NOT be used as gates.

---

## VI. SOURCE MATERIALS

The T102C sub-consultant should review the following materials as part of AC001 (Absorb Research Inputs):

**Primary (must-read)**:
- This communication
- RES-006 report: `prompt/artifacts/tasks/T102/research/T102-RES-006/report_T102-RES-006_concept-role-dynamic-registers.md` v1.0.0
- RES-006 integration analysis: `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md` v1.0.0

**Secondary (reference as needed)**:
- RES-004 report: `prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md`
- RES-004 integration analysis: `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md`
- RES-005 report: `prompt/artifacts/tasks/T102/research/T102-RES-005/report_T102-RES-005_cross-scope-coordination-architecture.md`
- RES-005 integration analysis: `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-005_cross-scope-coordination-architecture.md`

**Governance (authoritative constraints)**:
- T102C-STD-001: `prompt/artifacts/tasks/T102/T102C/standard/standard_T102C-STD-001_concept-architectural-framework.md`
- T102-STD-001 (pending amendment): `prompt/artifacts/tasks/T102/standard/standard_T102-STD-001_consultancy-operating-model.md`
- Current Concept: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`

---

## VII. CONTACT

For questions about the research findings, integration analysis, or STD amendment coordination, contact the **T102 Initiative LLM_Consultant** (ST004 research program owner).
