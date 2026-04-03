---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T002'
initiative_code: 'TECOM'
phase: '0'
stream_id: 'T002-PH000-ST000'
activity_id: 'T002-PH000-ST000-AC000'
task_id: 'T002-PH000-ST000-AC000-TK001'
version: '1.0.0'
date: '2026-04-03'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md'
execution_audience: 'assistant'
purpose: 'Detailed implementation specification for SES002 plan amendment — activity plan v2.0.0 (two-gate structure), stream notes register update, and hypothesis brief comparative matrix enhancement'
---

# IMPLEMENTATION (Task Specification): SES002 Plan Amendment & Hypothesis Brief Enhancement

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the exact file mutations required to implement the SES002 consultation decisions: (1) activity plan amendment to v2.0.0 with two-gate structure and full gate-readiness stack, (2) stream notes register update to register SES002, and (3) hypothesis brief enhancement with a formal comparative assessment matrix.
- **Authority chain**: Plan `plan_T002-PH000-ST000-AC000.md` (TK001) authorizes workspace establishment and plan authoring. This artifact specifies HOW the plan amendment, register update, and hypothesis brief enhancement are executed. Dev-report (or session notes) records execution evidence.
- **Audience**: `LLM_Assistant` — executing on behalf of `LLM_Consultant` per CONV-013 and CONV-018.
- **This artifact does NOT hold a GDR.** Gate decisions are recorded in gate-disposition proposals.

## II. TASK SCOPE

- **Governing plan task**: `T002-PH000-ST000-AC000-TK001` (Establish Consultation Workspace) — plan amendment is part of completing workspace establishment. TK000.1 (hypothesis brief enhancement) is also covered under the same design-decision boundary (SES002 plan amendment decisions).
- **Trigger**: Task complexity exceeds plan-step capacity — the plan amendment involves a complete task register restructuring (two-gate pattern, 7 new tasks/sub-tasks, resequenced dependencies) plus a parallel hypothesis brief enhancement with formal comparative assessment methodology.
- **Deliverable contract**: Three updated files (U1, U2, U3) as specified below.

**Design decisions governing this specification** (from SES002 consultation):
- Two-gate structure approved: GATE-001 (internal governance) + GATE-002 (external advisory release)
- Each gate follows consultation-only gate-readiness stack per `guideline_workspace_plan.md` §VI.L
- Hypothesis brief enhanced with comparative assessment matrix (weighted criteria + grading) — stays as `assessment` type, no new artifact
- SPS and Roadmap first draft produced together (TK002)
- Roadmap detail update deferred to post-discovery (TK006)
- Discovery session (TK005) strictly after GATE-002 (Option A: accept timeline risk)
- Codex GPT 5.4 adversarial review validated the two-gate separation and enhancement approach

---

## III. SPECIFICATION ITEMS

### SPEC-001 — Activity Plan Amendment (v1.0.0 → v2.0.0)

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 consultation decisions: two-gate structure, gate-readiness stack compliance, task resequencing |
| Target file(s) | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md` |
| Required end-state posture | Plan v2.0.0 with: (a) 14-row task register (TK000, TK001, TK000.1, TK002, TK002.1, TK002.2, GATE-001, TK003, TK004, TK004.1, TK004.2, GATE-002, TK005, TK006), (b) detailed task sections for all new/modified tasks, (c) updated Links Register, (d) changelog entry |
| Explicit non-target / do-not-change constraints | Do NOT modify the Executive Summary (Section I) purpose or non-goal statements. Do NOT alter TK000's detailed section body (already completed). Do NOT modify the raw transcript or hypothesis brief references in the Context block. |
| Validation check | (1) Task Register has exactly 14 rows (12 tasks/sub-tasks + 2 gates). (2) Every `Depends On` reference resolves to a valid task/gate ID in the register. (3) Gate-readiness stack tasks appear immediately before their governing gate row. (4) Detailed sections mirror Task Register dependency order per §VI.E. (5) Links Register includes all new deliverable paths. (6) Changelog records v2.0.0 amendment. |
| Blocking ambiguity rule | If any task's dependency chain creates a circular reference, STOP and escalate. If any deliverable path conflicts with an existing file, STOP and escalate. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter**

Replace the following frontmatter fields:
```yaml
version: '2.0.0'
date: '2026-04-03'
```
Keep all other frontmatter fields unchanged.

**Step 2: Replace the Task Register table in Section II (Activity Outline)**

Replace the entire Task Register table (the table after the `### Task Register` heading in Section II) with the following exact content:

```markdown
| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `T002-PH000-ST000-AC000-TK000` | Produce hypothesis brief | `completed` | LLM_Consultant | — | `analysis/` | `guideline_workspace_analysis.md` | Completed in separate branch. Assessed three architectural options; recommended hybrid (specialist + thin reporting layer). Formalized testable hypothesis. |
| TK001 | `T002-PH000-ST000-AC000-TK001` | Establish consultation workspace | `completed` | LLM_Consultant | — | `plan_T002-PH000-ST000-AC000.md`, `snotes/`, `notes_T002-PH000-ST000.md` | `guideline_workspace_plan.md`, `guideline_workspace_notes.md` | Workspace established. Plan amended to v2.0.0 in SES002 (two-gate structure, gate-readiness stack compliance). |
| TK000.1 | `T002-PH000-ST000-AC000-TK000.1` | Enhance hypothesis brief with comparative assessment matrix | `planned` | LLM_Consultant | TK000 | `analysis/` | `guideline_workspace_analysis.md` | — |
| TK002 | `T002-PH000-ST000-AC000-TK002` | Produce SPS at initiative level + thin-spine roadmap (first draft) | `planned` | LLM_Consultant | TK001 | `ssot/sps_T002-TECOM.md`, `ssot/roadmap_T002.md` | `guideline_ssot_sps.md`, `guideline_workspace_roadmap.md` | — |
| TK002.1 | `T002-PH000-ST000-AC000-TK002.1` | Gate-disposition proposal (GATE-001) | `planned` | LLM_Consultant | TK002, TK000.1 | `proposal/` | `guideline_workspace_proposal.md` | — |
| TK002.2 | `T002-PH000-ST000-AC000-TK002.2` | External review (GATE-001) | `planned` | LLM_Subconsultant | TK002.1 | `analysis/` | `guideline_workspace_analysis.md` | — |
| GATE-001 | `T002-PH000-ST000-AC000-GATE-001` | Internal governance package approval | `planned` | Client | TK002.2 | Pass/feedback | `guideline_workspace_plan.md` | — |
| TK003 | `T002-PH000-ST000-AC000-TK003` | Produce advisory note (English SSOT) | `planned` | LLM_Consultant | GATE-001 | `advisory_T002-PH000_agent-architecture-recommendation.md` | — | — |
| TK004 | `T002-PH000-ST000-AC000-TK004` | Produce advisory note (Vietnamese translation) | `planned` | LLM_Consultant | TK003 | `advisory_T002-PH000_agent-architecture-recommendation_vi.md` | — | — |
| TK004.1 | `T002-PH000-ST000-AC000-TK004.1` | Gate-disposition proposal (GATE-002) | `planned` | LLM_Consultant | TK004 | `proposal/` | `guideline_workspace_proposal.md` | — |
| TK004.2 | `T002-PH000-ST000-AC000-TK004.2` | External review (GATE-002) | `planned` | LLM_Subconsultant | TK004.1 | `analysis/` | `guideline_workspace_analysis.md` | — |
| GATE-002 | `T002-PH000-ST000-AC000-GATE-002` | Advisory note release approval | `planned` | Client | TK004.2 | Pass/feedback | `guideline_workspace_plan.md` | — |
| TK005 | `T002-PH000-ST000-AC000-TK005` | Conduct PH000 discovery session (workflow walkthrough) | `planned` | LLM_Consultant + TECOM | GATE-002 | Session notes (SES003+) | `guideline_workspace_notes.md` | — |
| TK006 | `T002-PH000-ST000-AC000-TK006` | Roadmap detail update | `planned` | LLM_Consultant | TK005 | `ssot/roadmap_T002.md` | `guideline_workspace_roadmap.md` | — |
```

**Step 3: Update TK001 detailed section in Section III**

Locate `### Task TK001: Establish Consultation Workspace` in Section III. Make the following changes:

3a. In the **Success Criteria** checklist at the bottom of TK001's section, change all `[ ]` to `[x]`:
```markdown
- [x] Activity plan exists with complete task register covering all planned deliverables
- [x] Session notes (SES001) capture sufficient context for a new session to resume without re-deriving
- [x] Stream notes register exists and indexes SES001
- [x] All directory paths for planned deliverables exist
```

**Step 4: Add TK000.1 detailed section after TK001 section**

Insert the following new section immediately after the TK001 section (before the `### Task TK002` section). Maintain the `---` separator between sections:

```markdown
---

### Task TK000.1: Enhance Hypothesis Brief with Comparative Assessment Matrix

**Task ID**: `T002-PH000-ST000-AC000-TK000.1`

**Purpose**: Add a formal comparative assessment matrix with weighted evaluation criteria and grading scale to the existing hypothesis brief (Section V), strengthening the analytical rigor of the architecture recommendation before it feeds the advisory note and internal governance gate.

**Deliverable**:
- Updated `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md` (version bump)

**Scope**:
- In scope:
  - Weighted evaluation criteria table (6 criteria with percentage-based weighting)
  - Comparative assessment matrix (3 options x 6 criteria, grading scale 1-5 with rationale)
  - Scoring-based recommendation update referencing matrix results
  - Dissenting consideration (where non-recommended options scored better)
- Out of scope:
  - Changing the `analysis_type` from `assessment` to `comparative_analysis` (stays as `assessment`)
  - Modifying existing Sections I-IV, VI-X content
  - Adding new evidence or research beyond what is already in the brief

**Implementation Reference**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/implementation/implementation_T002-PH000-ST000-AC000_ses002-plan-amendment-brief.md` — SPEC-003

**Steps**:
1. Add evaluation criteria and weighting subsection to Section V (between V.B and V.C)
2. Add comparative assessment matrix subsection
3. Update Section V.C recommendation to reference scoring rationale
4. Version bump and changelog entry

**Success Criteria**:
- [ ] Evaluation criteria table includes 6 weighted criteria with percentage-based weights summing to 100%
- [ ] Comparative assessment matrix grades all 3 options on all 6 criteria with 1-5 scale and brief rationale per cell
- [ ] Weighted scores calculated for all 3 options
- [ ] Recommendation references scoring outcome and addresses dissenting considerations
- [ ] No content drift from existing Sections I-IV, VI-X
```

**Step 5: Update TK002 detailed section**

Locate `### Task TK002: Produce SPS at Initiative Level + Thin-Spine Roadmap` in Section III. Make the following changes:

5a. Replace the **Purpose** paragraph:
```markdown
**Purpose**: Formalize NMAQ's understanding of the T002 initiative through a governance-level SPS document and establish the phase structure through a thin-spine roadmap (first draft). Both are internal NMAQ documents that record TECOM requirements and prepare for potential PH001 development. The roadmap first draft captures PH000 + PH001 phase headers; detailed roadmap integration occurs post-discovery (TK006).
```

5b. In the **Scope** section, add this bullet to "In scope":
```markdown
  - Roadmap first draft: PH000 + PH001 phase register headers, current delivery snapshot (compact), links register
```

5c. In the **Scope** section, add this bullet to "Out of scope":
```markdown
  - Detailed roadmap execution surface (stream/activity registers) — deferred to TK006 post-discovery
```

5d. In the **Steps** list, add after step 5:
```markdown
6. Author thin-spine roadmap with PH000 and PH001 phase headers, current delivery snapshot, and links register
7. Cross-validate roadmap links against SPS and activity plan paths
```

5e. In the **Success Criteria**, add:
```markdown
- [ ] Roadmap first draft exists with PH000 + PH001 phase register, current delivery snapshot, and links register
- [ ] Roadmap remains thin-spine (no stream/activity execution detail)
```

**Step 6: Add TK002.1 detailed section after TK002 section**

Insert immediately after the TK002 section:

```markdown
---

### Task TK002.1: Gate-Disposition Proposal (GATE-001)

**Task ID**: `T002-PH000-ST000-AC000-TK002.1`

**Purpose**: Package the internal governance artifacts (SPS, enhanced hypothesis brief, roadmap first draft) into a consultation-only gate-disposition proposal for GATE-001 client review and approval.

**Deliverable**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-001_gate-disposition.md`

**Scope**:
- In scope:
  - Gate Package Index listing all internal governance deliverables
  - Evidence Index referencing SPS, enhanced hypothesis brief, roadmap first draft
  - Consultant recommendation (advisory) for GATE-001 disposition
  - Gate Decision Record (GDR) shell for Client disposition
- Out of scope:
  - Advisory notes (those are GATE-002 scope)
  - DEV-REPORT or VERIFICATION (consultation-only gate — per §VI.L)
  - Implementation-backed evidence

**Inputs Required**:
- `prompt/artifacts/tasks/T002/ssot/sps_T002-TECOM.md` — SPS (TK002 deliverable)
- `prompt/artifacts/tasks/T002/ssot/roadmap_T002.md` — Roadmap first draft (TK002 deliverable)
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md` — Enhanced hypothesis brief (TK000.1 deliverable)

**Steps**:
1. Author proposal frontmatter per `guideline_workspace_proposal.md`
2. Compile Gate Package Index listing all internal governance deliverables
3. Compile Evidence Index with repo-relative paths
4. Author consultant recommendation section
5. Create GDR shell (Client Decision field left for Client disposition)

**Success Criteria**:
- [ ] Proposal exists with gate package index, evidence index, consultant recommendation, GDR shell
- [ ] All evidence index paths resolve to existing artifacts
- [ ] GDR shell includes required fields per `guideline_workspace_proposal.md` §VII
- [ ] No advisory notes referenced (those belong to GATE-002)
```

**Step 7: Add TK002.2 detailed section after TK002.1 section**

Insert immediately after the TK002.1 section:

```markdown
---

### Task TK002.2: External Review (GATE-001)

**Task ID**: `T002-PH000-ST000-AC000-TK002.2`

**Purpose**: Independent second-opinion quality audit of the GATE-001 internal governance package by LLM_Subconsultant, per consultation-only gate-readiness stack requirements.

**Deliverable**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_external-review-gate-001.md`

**Scope**:
- In scope:
  - Review of SPS completeness and traceability to hypothesis brief / session notes
  - Review of enhanced hypothesis brief comparative assessment methodology
  - Review of roadmap first draft structure and links validity
  - Assessment of evidence integrity, role-boundary compliance, and plan-guideline compliance
  - Assessment of downstream task readiness (TK003/TK004 advisory notes can proceed with approved package)
- Out of scope:
  - Advisory note content review (that belongs to GATE-002 external review)
  - Implementation-backed verification (consultation-only gate)
  - Overriding the gate-disposition proposal's GDR authority

**Inputs Required**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-001_gate-disposition.md` — Gate-disposition proposal (TK002.1 deliverable)
- All evidence artifacts referenced in the proposal's evidence index

**Steps**:
1. Review all evidence artifacts against consultation-only gate-readiness requirements
2. Assess evidence integrity and cross-link resolution
3. Assess plan-guideline compliance for internal governance package
4. Assess downstream task readiness (can advisory notes proceed?)
5. Author external review analysis per `guideline_workspace_analysis.md` §IV.B

**Success Criteria**:
- [ ] External review analysis exists with Strengths, Concerns/Risks, Recommendations sections
- [ ] All evidence artifacts in the gate package have been reviewed
- [ ] Downstream task readiness explicitly assessed
- [ ] Review is advisory; does not claim gate closure
```

**Step 8: Replace GATE-001 detailed section**

Locate the existing `### GATE-001: Client Feedback Checkpoint on Advisory Note` section. Replace the ENTIRE section (from the heading through the end of the Notes paragraph) with:

```markdown
### GATE-001: Internal Governance Package Approval

**Gate ID**: `T002-PH000-ST000-AC000-GATE-001`

**Entry Criteria**:
- TK000.1 (enhanced hypothesis brief with comparative assessment matrix) is completed
- TK002 (SPS + roadmap first draft) is completed
- TK002.1 (gate-disposition proposal) is completed
- TK002.2 (external review) is completed
- All deliverables are ready for Client review

**Reviewer**: Client

**Exit Criteria**:
- Client has reviewed the internal governance package (SPS, enhanced hypothesis brief, roadmap first draft)
- Client has reviewed the external review findings
- Client provides disposition: APPROVE, APPROVE WITH CONDITIONS, or RECYCLE
- Gate decision is recorded in the GDR within the gate-disposition proposal

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-001_gate-disposition.md`

**Notes**: This is a consultation-only gate following the reduced gate-readiness stack per `guideline_workspace_plan.md` §VI.L. No DEV-REPORT or VERIFICATION is required. The gate approves the internal governance foundation (NMAQ's formalized understanding of TECOM's requirements and architecture assessment) before advisory note production proceeds. The gate-disposition proposal hosts the authoritative GDR. The external review provides an independent second-opinion quality audit as advisory input.
```

**Step 9: Update TK003 detailed section**

Locate `### Task TK003: Produce Advisory Note (English SSOT)` in Section III. Make the following changes:

9a. In the **Scope** "In scope" list, add as the first bullet:
```markdown
  - Drawing from GATE-001-approved internal governance package (SPS problem definition, enhanced hypothesis brief comparative assessment, validated architecture recommendation)
```

9b. In the **Inputs Required** section, add:
```markdown
- `prompt/artifacts/tasks/T002/ssot/sps_T002-TECOM.md` — SPS Section III.A (Problem Definition) for framing
```

9c. In the **Steps** list, add as step 0 (before existing step 1):
```markdown
0. Review GATE-001-approved package to confirm architecture recommendation direction and evidence grounding
```

**Step 10: Add TK004.1 detailed section after TK004 section**

Insert immediately after the TK004 section:

```markdown
---

### Task TK004.1: Gate-Disposition Proposal (GATE-002)

**Task ID**: `T002-PH000-ST000-AC000-TK004.1`

**Purpose**: Package the external advisory deliverables (advisory notes EN/VI) into a consultation-only gate-disposition proposal for GATE-002 client review and release approval.

**Deliverable**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-002_gate-disposition.md`

**Scope**:
- In scope:
  - Gate Package Index listing advisory notes EN and VI
  - Evidence Index referencing advisory notes and their upstream sources (GATE-001-approved hypothesis brief, SPS)
  - Consultant recommendation for GATE-002 disposition (release to TECOM)
  - Gate Decision Record (GDR) shell for Client disposition
  - Release readiness assessment: advisory note quality, tone, completeness, Vietnamese translation fidelity
- Out of scope:
  - Re-reviewing internal governance artifacts (those were approved at GATE-001)
  - DEV-REPORT or VERIFICATION (consultation-only gate)

**Inputs Required**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/advisory_T002-PH000_agent-architecture-recommendation.md` — EN advisory note (TK003 deliverable)
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/advisory_T002-PH000_agent-architecture-recommendation_vi.md` — VI advisory note (TK004 deliverable)

**Steps**:
1. Author proposal frontmatter per `guideline_workspace_proposal.md`
2. Compile Gate Package Index listing both advisory notes
3. Compile Evidence Index with repo-relative paths and upstream traceability
4. Author release readiness assessment section
5. Author consultant recommendation section
6. Create GDR shell (Client Decision field left for Client disposition)

**Success Criteria**:
- [ ] Proposal exists with gate package index, evidence index, release readiness assessment, consultant recommendation, GDR shell
- [ ] All evidence index paths resolve to existing artifacts
- [ ] Upstream traceability to GATE-001-approved package is documented
- [ ] GDR shell includes required fields per `guideline_workspace_proposal.md` §VII
```

**Step 11: Add TK004.2 detailed section after TK004.1 section**

Insert immediately after the TK004.1 section:

```markdown
---

### Task TK004.2: External Review (GATE-002)

**Task ID**: `T002-PH000-ST000-AC000-TK004.2`

**Purpose**: Independent second-opinion quality audit of the GATE-002 advisory release package by LLM_Subconsultant, per consultation-only gate-readiness stack requirements.

**Deliverable**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_external-review-gate-002.md`

**Scope**:
- In scope:
  - Review of advisory note (EN) for: plain language quality, accuracy of architecture recommendation vs hypothesis brief, completeness of practical guidance, absence of NMAQ-internal jargon, appropriate tone (trusted peer, not sales document)
  - Review of advisory note (VI) for: translation fidelity to EN SSOT, natural Vietnamese technical terminology, correct register (informal "anh/em" matching raw transcript tone)
  - Assessment of evidence integrity between advisory notes and GATE-001-approved package
  - Assessment of downstream task readiness (discovery session can proceed after TECOM receives advisory)
- Out of scope:
  - Re-reviewing SPS or hypothesis brief (GATE-001 scope)
  - Implementation-backed verification
  - Overriding the gate-disposition proposal's GDR authority

**Inputs Required**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-002_gate-disposition.md` — Gate-disposition proposal (TK004.1 deliverable)
- All evidence artifacts referenced in the proposal's evidence index

**Steps**:
1. Review EN advisory note against quality criteria (plain language, accuracy, completeness, tone)
2. Review VI advisory note against translation quality criteria (fidelity, terminology, register)
3. Cross-check advisory content against GATE-001-approved hypothesis brief recommendation
4. Assess downstream readiness (TECOM can act on the advisory)
5. Author external review analysis per `guideline_workspace_analysis.md` §IV.B

**Success Criteria**:
- [ ] External review analysis exists with Strengths, Concerns/Risks, Recommendations sections
- [ ] Both advisory notes (EN + VI) reviewed against quality criteria
- [ ] Translation fidelity explicitly assessed
- [ ] Downstream readiness (TECOM actionability) assessed
- [ ] Review is advisory; does not claim gate closure
```

**Step 12: Add GATE-002 detailed section after TK004.2 section**

Insert immediately after the TK004.2 section:

```markdown
---

### GATE-002: Advisory Note Release Approval

**Gate ID**: `T002-PH000-ST000-AC000-GATE-002`

**Entry Criteria**:
- TK003 (advisory note EN SSOT) is completed
- TK004 (advisory note VI translation) is completed
- TK004.1 (gate-disposition proposal) is completed
- TK004.2 (external review) is completed
- All deliverables are ready for Client review

**Reviewer**: Client

**Exit Criteria**:
- Client has reviewed the advisory notes (EN and/or VI)
- Client has reviewed the external review findings
- Client provides disposition: APPROVE (authorize release to TECOM), APPROVE WITH CONDITIONS, or RECYCLE
- Gate decision is recorded in the GDR within the gate-disposition proposal

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-002_gate-disposition.md`

**Notes**: This is a consultation-only gate following the reduced gate-readiness stack per `guideline_workspace_plan.md` §VI.L. No DEV-REPORT or VERIFICATION is required. The gate authorizes release of the advisory notes to the TECOM CEO. Upon APPROVE, the advisory notes are delivered to TECOM and the discovery session (TK005) is unblocked. This gate is distinct from GATE-001 (internal governance): GATE-001 approves NMAQ's internal formalization; GATE-002 approves the external-facing communication.
```

**Step 13: Update TK005 detailed section**

Locate `### Task TK005: Conduct PH000 Discovery Session (Workflow Walkthrough)` in Section III. Make the following changes:

13a. In the **Inputs Required** section, replace:
```
- GATE-001 feedback (confirms direction before investing in deeper discovery)
```
with:
```
- GATE-002 approval (confirms advisory notes released to TECOM and direction accepted before investing in deeper discovery)
```

13b. In the **Deliverable** section, replace:
```
- Session notes (SES002+) capturing workflow map, tool inventory, review bottleneck analysis
```
with:
```
- Session notes (SES003+) capturing workflow map, tool inventory, review bottleneck analysis
```

13c. In the **Steps** list, step 1, replace "target: before 2026-04-10" with:
```
(target: before 2026-04-10 per raw transcript agreement — note: timeline risk exists due to GATE-001 + GATE-002 critical path; see plan changelog v2.0.0)
```

**Step 14: Add TK006 detailed section after TK005 section**

Insert immediately after the TK005 section:

```markdown
---

### Task TK006: Roadmap Detail Update

**Task ID**: `T002-PH000-ST000-AC000-TK006`

**Purpose**: Update the thin-spine roadmap with detailed integration based on PH000 discovery session findings. If discovery validates PH001 interest, expand the roadmap with stream/activity execution detail for PH001. If PH001 is not validated, record the outcome and close the roadmap at PH000 completion.

**Deliverable**:
- Updated `prompt/artifacts/tasks/T002/ssot/roadmap_T002.md` (version bump)

**Scope**:
- In scope:
  - Update Current Delivery Snapshot based on discovery findings
  - Update PH001 phase register entry based on go/no-go recommendation
  - Add Open Questions resolved during discovery
  - If PH001 validated: add stream register headers for PH001 execution planning
- Out of scope:
  - Full PH001 stream/activity/task breakdown (belongs in PH001 phase plan if approved)
  - Modifying SPS content (separate task if discovery changes requirements)

**Inputs Required**:
- `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES003.md` — Discovery session notes (TK005 deliverable)
- `prompt/artifacts/tasks/T002/ssot/roadmap_T002.md` — Existing roadmap first draft (TK002 deliverable)

**Steps**:
1. Review discovery session findings and go/no-go recommendation
2. Update Current Delivery Snapshot with discovery outcomes
3. Update PH001 phase register entry (status, intent refinement)
4. Resolve applicable Open Questions
5. If PH001 validated: add stream register headers
6. Version bump and changelog entry

**Success Criteria**:
- [ ] Roadmap reflects discovery session outcomes
- [ ] PH001 phase register entry updated with go/no-go status
- [ ] Open Questions register updated with discovery resolutions
- [ ] Roadmap remains thin-spine (no detailed execution planning in roadmap itself)
```

**Step 15: Update the Links Register (Section IV)**

Replace the entire Links Register table in Section IV with:

```markdown
| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | Activity Plan AC000 | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md` |
| Implementation | SES002 Plan Amendment Brief | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/implementation/implementation_T002-PH000-ST000-AC000_ses002-plan-amendment-brief.md` |
| Analysis | Hypothesis Brief | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md` |
| Notes Register | Stream Notes Register ST000 | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/notes_T002-PH000-ST000.md` |
| Notes | Session Notes SES001 | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES001.md` |
| Notes | Session Notes SES002 | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES002.md` |
| Raw Transcript | PH000 Raw Conversation | `prompt/artifacts/tasks/T002/raw_T002-PH000.txt` |
| External Reference | NMAQ Orchestration Spec | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/implementation/implementation_T103-PH000-ST000-AC001_orchestration-execution-patterns.md` |
| SPS | Initiative Governance | `prompt/artifacts/tasks/T002/ssot/sps_T002-TECOM.md` |
| Roadmap | Initiative Roadmap | `prompt/artifacts/tasks/T002/ssot/roadmap_T002.md` |
| Advisory Note (EN) | External Deliverable | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/advisory_T002-PH000_agent-architecture-recommendation.md` |
| Advisory Note (VI) | External Deliverable | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/advisory_T002-PH000_agent-architecture-recommendation_vi.md` |
| Proposal (GATE-001) | Gate-Disposition Proposal | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-001_gate-disposition.md` |
| Proposal (GATE-002) | Gate-Disposition Proposal | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-002_gate-disposition.md` |
| External Review (GATE-001) | Independent Quality Audit | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_external-review-gate-001.md` |
| External Review (GATE-002) | Independent Quality Audit | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_external-review-gate-002.md` |
```

**Step 16: Add Changelog entry (Section V)**

Add the following row to the Changelog table in Section V:

```markdown
| v2.0.0 | 2026-04-03 | Major amendment | Plan restructured per SES002 consultation decisions. Two-gate structure: GATE-001 (internal governance package approval) + GATE-002 (advisory note release approval). Each gate follows consultation-only gate-readiness stack (gate-disposition proposal + external review + gate). Added tasks: TK000.1 (hypothesis brief comparative matrix enhancement), TK002.1/TK002.2 (GATE-001 readiness stack), TK004.1/TK004.2 (GATE-002 readiness stack), TK006 (post-discovery roadmap detail update). TK001 marked completed. TK002 scope updated to include roadmap first draft. TK003 dependency updated (now depends on GATE-001). TK005 dependency updated (now depends on GATE-002), session target updated to SES003. GATE-001 redesigned from informal client feedback checkpoint to formal internal governance gate. Timeline risk flagged for April 10 discovery target. Codex GPT 5.4 adversarial review (SES002) validated two-gate separation and enhancement approach. |
```

---

### SPEC-002 — Stream Notes Register Update

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 occurred before previously planned SES002 (TECOM walkthrough); register must reflect actual session sequence |
| Target file(s) | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/notes_T002-PH000-ST000.md` |
| Required end-state posture | Register shows: SES001 (unchanged), SES002 (this session — plan amendment & SSOT planning), SES003 (TECOM walkthrough — relabeled from old SES002). Version bumped to v1.1.0. |
| Explicit non-target / do-not-change constraints | Do NOT modify the Purpose section, Stream Summary section, Activity Notes Register section, or Primary Links section. Only modify the Stream-Level Session Notes Register table and Changelog. |
| Validation check | (1) SES002 row exists with correct title, date, and notes file path. (2) Former SES002 (TECOM walkthrough) is now SES003. (3) Changelog records v1.1.0 amendment. |
| Blocking ambiguity rule | If the notes file path for SES002 does not match the expected pattern `snotes_T002-PH000-ST000-AC000-SES002.md`, STOP and escalate. |
| Status | `open` |

#### Implementation Detail

**Step 1: Replace the Stream-Level Session Notes Register table**

Replace the entire table under `## Stream-Level Session Notes Register` with:

```markdown
| Session | Session ID | Title | Date | Notes File | Status |
|:--------|:-----------|:------|:-----|:-----------|:-------|
| SES001 | `T002-PH000-ST000-SES001` | Kickoff & Architecture Advisory Session | 2026-04-03 | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES001.md` | `draft` |
| SES002 | `T002-PH000-ST000-SES002` | Plan Amendment & SSOT Planning Session | 2026-04-03 | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES002.md` | `draft` |
| SES003 | `T002-PH000-ST000-SES003` | PH000 Discovery: Workflow Walkthrough | — | — | `pending` |
```

**Step 2: Update frontmatter version**

Change `version: '1.0.0'` to `version: '1.1.0'` in the YAML frontmatter.

**Step 3: Add Changelog entry**

Add the following row to the Changelog table:

```markdown
| v1.1.0 | 2026-04-03 | Amendment | Registered SES002 (Plan Amendment & SSOT Planning Session, 2026-04-03). Relabeled former SES002 placeholder (TECOM workflow walkthrough) to SES003 to reflect actual session sequence. |
```

---

### SPEC-003 — Hypothesis Brief Comparative Assessment Matrix Enhancement

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 consultation — Client Comment 1 and Codex adversarial review both identified that the hypothesis brief's Section V options comparison lacks formal weighted evaluation criteria and grading |
| Target file(s) | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md` |
| Required end-state posture | Section V includes: (a) new subsection V.B2 "Evaluation Criteria & Weighting" with 6 weighted criteria, (b) new subsection V.B3 "Comparative Assessment Matrix" with 3 options graded 1-5 on each criterion with rationale and weighted scores, (c) updated V.C Recommendation referencing scoring results and dissenting considerations. Version bumped to v1.1.0. |
| Explicit non-target / do-not-change constraints | Do NOT modify Sections I-IV, VI-X. Do NOT modify existing Section V.A (Current State Summary) or V.B (Options) body text. Do NOT change the `analysis_type` frontmatter from `assessment` to `comparative_analysis`. Only ADD new subsections and UPDATE V.C. |
| Validation check | (1) Evaluation criteria weights sum to 100%. (2) All 3 options are graded on all 6 criteria. (3) Weighted scores are arithmetically correct. (4) Option C (Hybrid) has the highest weighted score. (5) Dissenting considerations address where non-recommended options scored better. (6) Changelog records v1.1.0. |
| Blocking ambiguity rule | If weighted scoring does NOT yield Option C as the highest scorer, STOP and escalate — the existing recommendation may need re-evaluation. Do NOT adjust weights to force Option C to win. |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter version**

Change `version: '1.0.0'` to `version: '1.1.0'` in the YAML frontmatter. Update `date: '2026-04-03'`.

**Step 2: Add Evaluation Criteria & Weighting subsection**

After the existing `### B. Options` section (after the Option C table ends, before `### C. Recommendation`), insert:

```markdown
### B2. Evaluation Criteria & Weighting

The following criteria are derived from TECOM's stated pain points (SES001 raw transcript), industry evidence (Microsoft orchestration patterns, Akka supervisor patterns, Lean Startup), and the Codex adversarial review. Weights reflect the relative importance to TECOM's specific context (4-person e-commerce company with manual CEO coordination bottleneck).

| Criterion | Definition | Weight |
|:--|:--|:--|
| CEO Coordination Reduction | Degree to which the architecture reduces manual CEO coordination overhead — the PRIMARY stated pain point | 30% |
| Time to First Value | How quickly the architecture delivers initial measurable value to TECOM operations | 20% |
| Complexity | Development and operational complexity appropriate for a 4-person team with no dedicated engineering staff | 15% |
| Build Effort | Initial development effort required relative to TECOM's capacity | 15% |
| Failure Resilience | Graceful degradation when individual components fail, minimizing blast radius | 10% |
| Scalability | Ability to add new domains/tools without rearchitecting the system | 10% |

**Weighting rationale**: CEO Coordination Reduction receives the highest weight (30%) because it is the explicit motivating question from the TECOM CEO ("Should I build one central manager agent...?"). Time to First Value receives 20% because TECOM is a small company that needs to see results quickly to justify continued investment. Complexity and Build Effort each receive 15% because TECOM's 4-person team cannot absorb high development overhead. Failure Resilience and Scalability each receive 10% as important but secondary considerations for the initial architecture decision.
```

**Step 3: Add Comparative Assessment Matrix subsection**

Immediately after the Evaluation Criteria & Weighting subsection, insert:

```markdown
### B3. Comparative Assessment Matrix

Grading scale: 1 (worst) to 5 (best) for TECOM's context. Each cell includes a grade and brief rationale.

| Criterion | Weight | Option A: Centralized Orchestrator | Option B: Independent Agents | Option C: Hybrid (Recommended) | Notes |
|:--|:--|:--|:--|:--|:--|
| CEO Coordination Reduction | 30% | **5** — If successful, single daily summary eliminates all manual coordination | **1** — Does not address the problem; CEO still manually synthesizes multiple independent reports | **4** — Reporting layer synthesizes specialist outputs into unified daily brief; substantial coordination reduction | This is the decisive criterion. Option B fails it entirely. |
| Time to First Value | 20% | **1** — Nothing works until the complete workflow is mapped and all sub-agents connected | **5** — First agent provides immediate standalone value on day one | **4** — First specialist provides standalone value; reporting layer follows as second step | Lean Startup: validate incrementally with smallest valuable slice |
| Complexity | 15% | **1** — Must understand all 10 tools and all business domains in a single system; high coupling | **5** — Each agent is simple, bounded, and independently understandable | **3** — Specialists are simple; reporting layer adds modest integration complexity via standardized status format | TECOM has no dedicated engineering staff; complexity must stay low |
| Build Effort | 15% | **1** — Requires complete workflow mapping before any value; large upfront investment | **5** — Minimal effort per agent; start immediately with one domain | **3** — Moderate: specialists + standardized status blocks + thin reporting layer | Proportionate to 4-person company capacity |
| Failure Resilience | 10% | **1** — Single point of failure; one orchestrator error cascades to all reporting | **5** — Fully isolated; one agent's failure has zero impact on others | **4** — Graceful degradation; if one specialist fails, others still report normally | Microsoft pattern guidance: minimize blast radius |
| Scalability | 10% | **2** — Every new domain increases orchestrator complexity; central bottleneck grows | **4** — Add agents independently, but no standardized interface for future reporting integration | **5** — New specialists plug in via standardized status format; reporting layer handles aggregation automatically | Akka: keep workers simple, interface via standard format |

**Weighted Scores**:

| Option | Calculation | Weighted Score |
|:--|:--|:--|
| **Option A: Centralized** | (5×30) + (1×20) + (1×15) + (1×15) + (1×10) + (2×10) = 150 + 20 + 15 + 15 + 10 + 20 | **230 / 500 (46%)** |
| **Option B: Independent** | (1×30) + (5×20) + (5×15) + (5×15) + (5×10) + (4×10) = 30 + 100 + 75 + 75 + 50 + 40 | **370 / 500 (74%)** |
| **Option C: Hybrid** | (4×30) + (4×20) + (3×15) + (3×15) + (4×10) + (5×10) = 120 + 80 + 45 + 45 + 40 + 50 | **380 / 500 (76%)** |

**Result**: Option C (Hybrid) scores highest at 76%, narrowly exceeding Option B (74%) and substantially exceeding Option A (46%).
```

**Step 4: Update Section V.C Recommendation**

Replace the existing `### C. Recommendation` section content (keep the heading) with:

```markdown
**Recommend Option C (Hybrid)** based on weighted comparative assessment scoring (76% vs Option B at 74%, Option A at 46%).

The scoring confirms the qualitative assessment: the hybrid architecture optimally balances TECOM's constraint profile across all evaluation dimensions.

**Key scoring drivers**:

1. **CEO Coordination Reduction (30% weight)**: This is the decisive criterion — it is the explicit reason TECOM CEO asked the question. Option A scores highest here (5/5) but is eliminated by catastrophic scores on Time to First Value, Complexity, Build Effort, and Failure Resilience. Option B scores lowest (1/5) because it does not address the coordination bottleneck at all. Option C scores well (4/5) via the thin reporting layer.

2. **Time to First Value (20% weight)**: Option C matches Option B's incremental delivery advantage — the first specialist provides standalone value immediately. The reporting layer is additive, not blocking.

3. **Complexity + Build Effort (15% + 15%)**: Option C trades Option B's perfect simplicity scores for moderate complexity that purchases the coordination reduction Option B cannot provide.

**Dissenting considerations**: Option B scored nearly as well (74% vs 76%) and offers superior simplicity. If TECOM's coordination bottleneck proves less severe than stated (e.g., discovery reveals the CEO's manual synthesis takes <10 minutes daily), Option B becomes the correct choice — the reporting layer overhead is not justified. This is precisely what GAP-004 (review bottleneck root cause) must validate in the PH000 discovery session.

**Recommended starting vertical**: Order tracking — highest daily urgency, most directly measurable, clearest data boundary.

**Where to start (practical sequence)**:
1. Map the order tracking workflow (data sources, handoff points, review checkpoints)
2. Build one specialist agent for order status reporting (delayed/delivered/pending)
3. Validate that the specialist's standardized output is useful to the CEO
4. Add a second specialist (email stats) and introduce the thin reporting layer
5. Expand incrementally based on validated learning
```

**Step 5: Add Changelog entry**

Add the following row to the Changelog table in Section X:

```markdown
| v1.1.0 | 2026-04-03 | Enhancement | Added formal comparative assessment methodology to Section V: evaluation criteria with percentage-based weighting (6 criteria), comparative assessment matrix (3 options graded 1-5 per criterion), weighted scoring calculation, and scoring-based recommendation with dissenting considerations. Enhancement driven by SES002 consultation (Client Comment 1) and validated by Codex GPT 5.4 adversarial review. Existing Sections I-IV, VI-X unchanged. Analysis type remains `assessment` (compliant per guideline_workspace_analysis.md line 77 for options tradeoffs). |
```

---

## IV. IMPLEMENTATION SEQUENCE

Recommended execution order for the LLM_Assistant:

1. **SPEC-002 first** (Stream Notes Register) — smallest change, no dependencies, quick validation
2. **SPEC-003 second** (Hypothesis Brief Enhancement) — self-contained content addition, no dependency on plan amendment
3. **SPEC-001 last** (Activity Plan Amendment) — largest change, references deliverables from SPEC-002 and SPEC-003

**Rationale**: SPEC-001 is the most complex mutation and benefits from SPEC-002 and SPEC-003 being completed first (the plan references the updated hypothesis brief and session notes). Starting with the smaller changes builds confidence and provides validation anchors.

**Post-execution validation**: After all three SPECs are complete, the executor SHOULD verify:
- All Links Register paths in the plan resolve to existing files or are marked as planned deliverables
- The Task Register dependency chain has no circular references
- The stream notes register SES002 file path matches the expected session notes location
- The hypothesis brief weighted scores are arithmetically correct

---

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md` |
| Hypothesis Brief | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md` |
| Stream Notes Register | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/notes_T002-PH000-ST000.md` |
| Session Notes SES001 | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES001.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| SPS Guideline | `prompt/templates/consultant/sps/guideline_ssot_sps.md` |
| Roadmap Guideline | `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-04-03 | Initial | Implementation specification created for SES002 plan amendment. Three SPEC items: SPEC-001 (activity plan v2.0.0 amendment with two-gate structure), SPEC-002 (stream notes register SES002 registration), SPEC-003 (hypothesis brief comparative assessment matrix enhancement). Execution audience: LLM_Assistant. Commissioned by LLM_Consultant per SES002 consultation decisions (Client-approved two-gate structure, hypothesis brief enhancement, roadmap timing). |
