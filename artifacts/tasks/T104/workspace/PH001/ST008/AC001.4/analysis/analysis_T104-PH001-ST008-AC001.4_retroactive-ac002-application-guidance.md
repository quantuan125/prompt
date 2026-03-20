---
artifact_type: 'ANALYSIS'
analysis_type: 'assessment'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.4'
task_id: 'T104-PH001-ST008-AC001.4-TK009'
gate_id: 'T104-PH001-ST008-AC001.4-GATE-001'
version: '1.0.0'
date: '2026-03-20'
status: 'active'
author: 'LLM_Developer'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/plan_T104-PH001-ST008-AC001.4.md'
assessment_scope: 'Retroactive application of GATE-001-approved governance model to P-PH000-ST002-AC002 gate package'
purpose: 'File-by-file application guidance for restructuring the AC002 gate package from same-gate RECYCLE to gate supersession under the approved external-impact governance model'
---

# ANALYSIS: Retroactive AC002 Application Guidance (T104-PH001-ST008-AC001.4)

> **APPLICATION GUIDANCE ONLY**: This artifact provides instructions for how the AC002 gate package should be restructured. It does NOT restructure the AC002 package itself. The actual restructure is a downstream consumer action performed after this guidance is reviewed.

## I. EXECUTIVE SUMMARY

**Purpose**: Provide a file-by-file change list for restructuring `P-PH000-ST002-AC002` from a same-gate RECYCLE treatment to the approved gate supersession model, following GATE-001 approval of the external-impact governance framework.

**Scope**: All AC002 artifacts affected by the gate supersession: the activity plan, the gate-disposition proposal, the analysis artifacts (deprecation), and the session notes addendum.

**Conclusion / Recommendation**: The AC002 gate package requires a structured forward amendment across six artifact surfaces. The approved three-layer deprecation model applies to the superseded analysis artifacts. The remediation work completed in TK001.3–TK001.7 carries forward into the GATE-002 package — no work is lost. The restructure is mechanical and follows the mechanics approved in GATE-001.

### Client Summary

- GATE-001 approved the governance model that classifies the `P-STD-002 v1.2.0` amendment as a decision-boundary external impact on `P-PH000-ST002-AC002-GATE-001`.
- The correct treatment is gate supersession: close GATE-001 with `Client Decision: SUPERSEDE`, create GATE-002 with the v1.2.0 baseline, renumber the existing GATE-002 (implementation acceptance) to GATE-003.
- All remediation work from TK001.3–TK001.7 carries forward into the GATE-002 package — no rework is needed.
- Analysis artifacts produced for the prior (v1.1.0) baseline are deprecated using the approved three-layer model (frontmatter + Evidence Index + Links Register).
- A new clean GATE-002 gate-disposition proposal is authored with the v1.2.0 Evidence Index and a GDR in `pending` state.
- The session notes addendum (§I of SES001) is updated to reference the completed governance model.
- This guidance document is the instruction set; actual restructure is performed by the downstream executor.

---

## II. SCOPE & INPUTS

**In scope**:
- File-by-file change instructions for the AC002 gate supersession restructure
- Three-layer deprecation guidance for superseded analysis artifacts
- New GATE-002 proposal creation instructions
- Plan amendment instructions (gate register, recycle re-entry block, links register)
- Session notes addendum update instructions

**Out of scope**:
- Actually performing the AC002 restructure (this is application guidance only)
- Creating the GATE-002 proposal content in full (that is a downstream task for LLM_Consultant)
- Restructuring any artifacts outside the AC002 package
- Amending the stream plan `plan_P-PH000-ST002.md` (stream-level gate numbering may require a separate plan amendment, but it is not addressed here — the AC002 activity plan is the primary restructure surface)

**Inputs reviewed (repo-relative paths)**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_gate-impact-classification-assessment.md` (§V.B, §V.F) — authoritative governance model
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md` (v1.3.0) — live AC002 plan with same-gate RECYCLE and HOLD annotation
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-001_design-decision-disposition.md` (v1.2.0) — live GDR in RECYCLE state
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/snotes/snotes_P-PH000-ST002-AC002-SES001.md` (v1.1.0) — plan amendment addendum with HOLD annotation
- Assessment §V.F (retroactive application mechanics)

---

## III. EVIDENCE / METHODOLOGY

**Method**:
- Read assessment §V.F for the approved retroactive application mechanics
- Read all three AC002 live artifact files to understand current state
- Map each approved mechanic to the specific files and fields that must change
- Produce a file-by-file change list with exact field values and deprecation notice text

**Evidence notes**:
- The AC002 plan (v1.3.0) confirms GATE-001 is `in_progress` with a HOLD on the Reassessment Rule
- The AC002 proposal (v1.2.0) confirms GDR `Client Decision: RECYCLE` and `Gate Status After Decision: in_progress`
- The SES001 addendum (§I) documents DEC005–DEC007 establishing the hold pending T104 governance resolution
- Assessment §V.F identifies the supersession as Scenario #1 (pending gate + external impact) compounded with Scenario #3 (gate already in recycle when external impact occurred)

---

## IV. FINDINGS / GAP REGISTER

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | lifecycle | GATE-001 uses incorrect disposition | GDR records `RECYCLE` but the trigger was an external decision-boundary change — correct disposition is `SUPERSEDE` | `resolved` | §V.A (plan amendment) | Resolved by applying the approved governance model |
| GAP-002 | lifecycle | Analysis artifacts not deprecated | Analysis artifacts produced against the v1.1.0 baseline are not yet deprecated; Evidence Index does not segregate historical evidence | `resolved` | §V.C (three-layer deprecation) | Resolved by applying the three-layer deprecation model |
| GAP-003 | lifecycle | No successor gate exists | GATE-002 for the v1.2.0 baseline does not exist; existing GATE-002 (implementation acceptance) will become GATE-003 | `resolved` | §V.B (gate creation + renumbering) | Resolved by gate restructure instructions |
| GAP-004 | references | Recycle Re-entry Block still present | The GATE-001 Recycle Re-entry Block in the plan becomes obsolete after supersession | `resolved` | §V.A (plan amendment) | Replaced by supersession structure |
| GAP-005 | references | SES001 addendum references pending governance | The §I addendum says governance "is under review" — now resolved | `resolved` | §V.E (session notes update) | Updated to reference completed governance model |

---

## V. ASSESSMENT (RESTRUCTURE GUIDANCE)

### A. Plan Amendment: `plan_P-PH000-ST002-AC002.md`

**File**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md`
**Current version**: v1.3.0
**Target version**: v1.4.0 (minor version bump for forward amendment)

**Change 1 — Frontmatter version bump**:
- Update `version` from `1.3.0` to `1.4.0`
- Update `date` to `2026-03-20`

**Change 2 — Executive Summary update**:
- Replace the statement "This activity is currently in a same-gate recycle loop at `P-PH000-ST002-AC002-GATE-001` after the earlier gate package was found stale against the March 18, 2026 standard amendment."
- With: "GATE-001 (v1.1.0 baseline design decision approval) has been superseded by the external-impact governance model approved at T104-PH001-ST008-AC001.4-GATE-001 on 2026-03-20. The external baseline change (`P-STD-002 v1.2.0` amendment, 2026-03-18) changed the decision boundary; the correct treatment is gate supersession. GATE-002 is the design decision approval gate for the `P-STD-002 v1.2.0` baseline. GATE-003 (renamed from GATE-002) remains the implementation acceptance gate."

**Change 3 — Task Register: GATE-001 row**:
- Current: `| GATE-001 | ... | 'in_progress' | ... | Plan guideline §VI.K | RECYCLE recorded on 2026-03-19; same-gate reassessment loop active. |`
- Replace with:
  ```
  | GATE-001 | `P-PH000-ST002-AC002-GATE-001` | Design Decision Approval (v1.1.0 baseline) | `superseded` | Client | TK001.2 | GDR in gate_disposition proposal | Plan guideline §VI.M | `SUPERSEDE` recorded on 2026-03-20; gate superseded due to external baseline change (P-STD-002 v1.2.0). Succeeded by GATE-002. |
  ```

**Change 4 — Task Register: GATE-002 row (NEW — insert after TK001.7 row, before TK002)**:
- Add a new GATE-002 row for the v1.2.0 baseline design decision approval:
  ```
  | GATE-002 | `P-PH000-ST002-AC002-GATE-002` | Design Decision Approval (v1.2.0 baseline) | `planned` | Client | TK001.7 | GDR in gate_disposition proposal (to be authored) | Plan guideline §VI.M, §VI.L | Successor gate to superseded GATE-001. Entry criteria reference P-STD-002 v1.2.0 baseline. |
  ```

**Change 5 — Task Register: Rename existing GATE-002 to GATE-003**:
- The current GATE-002 (Client acceptance of artifact set skeleton) becomes GATE-003.
- Update all occurrences of `GATE-002` in the implementation acceptance gate row to `GATE-003`.
- Row: `| GATE-003 | P-PH000-ST002-AC002-GATE-003 | Client acceptance of artifact set skeleton | planned | Client | TK004 | ... |`

**Change 6 — Task Register: Update downstream dependency references**:
- TK002 row: Change `Depends On: GATE-001` to `Depends On: GATE-002`
- TK003 row: Change `Depends On: GATE-001` to `Depends On: GATE-002`
- TK004 row: Keep `Depends On: TK002, TK003` (no gate dependency to update)
- GATE-003 row: Keep `Depends On: TK004`

**Change 7 — GATE-001 Detailed Section**:
- Remove the `Recycle Re-entry Block` from the GATE-001 detailed section.
- Replace with a `Supersession Block`:
  ```
  **Supersession Block**:
  - **Gate Status**: `superseded`
  - **Supersession Trigger**: External baseline change — `P-STD-002 v1.2.0` amendment (2026-03-18) changed the normative baseline against which design decisions were being evaluated. Classified as a decision-boundary external impact per T104-PH001-ST008-AC001.4-GATE-001 governance model.
  - **Prior Assessment**: Historically valid for the v1.1.0 baseline. Preserved per the three-layer deprecation model.
  - **Successor Gate**: `P-PH000-ST002-AC002-GATE-002` — design decision approval for the v1.2.0 baseline.
  - **GDR Reference**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-001_design-decision-disposition.md` (records `Client Decision: SUPERSEDE`)
  - **Governance Authority**: `T104-PH001-ST008-AC001.4-GATE-001` approval, 2026-03-20; `guideline_workspace_plan.md` §VI.M
  ```

**Change 8 — Add GATE-002 Detailed Section** (after GATE-001 section, before GATE-003 section):
  ```
  ### GATE-002: Design Decision Approval (v1.2.0 Baseline)

  **Gate ID**: `P-PH000-ST002-AC002-GATE-002`

  **Type**: Consultation-only decision gate (successor to superseded GATE-001)

  **Normative Baseline**: `P-STD-002 v1.2.0` (8-state lifecycle model, deferred-state governance, CLAUSE-056)

  **Entry Criteria**:
  - New gate-disposition proposal authored with clean Evidence Index for v1.2.0 baseline
  - Design decisions GIR-001 through GIR-003 refreshed against v1.2.0 requirements
  - Rebaselined implementation requirements analysis (TK001.5) confirmed as current

  **Reviewer**: LLM_Consultant (recommendation); Client (decision owner)

  **Exit Criteria**: GDR in the gate-disposition proposal records `Client Decision: APPROVE` or `APPROVE WITH CONDITIONS`

  **Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md` (to be authored)

  **Depends On**: TK001.7 (all v1.2.0 remediation work complete)

  **Note**: All remediation work from TK001.3–TK001.7 carries forward into this gate package. No additional remediation is required before GATE-002 can be assessed.
  ```

**Change 9 — Rename GATE-002 Detailed Section to GATE-003**:
- The existing "GATE-002: Client Acceptance of Artifact Set Skeleton" section header becomes "GATE-003".
- Update `Gate ID` field from `P-PH000-ST002-AC002-GATE-002` to `P-PH000-ST002-AC002-GATE-003`.
- Update `Downstream enforcement` text from "GATE-002" to "GATE-003".

**Change 10 — Links Register additions**:
- Add: `| Proposal | GATE-002 Disposition (to be authored) | prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md |`
- Add: `| Governance Authority | T104-PH001-ST008-AC001.4 Activity Plan | prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/plan_T104-PH001-ST008-AC001.4.md |`
- Add: `| Application Guidance | AC002 Retroactive Application Guidance | prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_retroactive-ac002-application-guidance.md | superseded annotation |`

**Change 11 — Changelog entry**:
- Add: `| v1.4.0 | 2026-03-20 | Amendment | Retroactive gate supersession per T104-PH001-ST008-AC001.4-GATE-001 approved governance model. GATE-001 closed with `SUPERSEDE` (external decision-boundary change — P-STD-002 v1.2.0). GATE-002 created as design decision approval gate for v1.2.0 baseline. Previous GATE-002 (implementation acceptance) renumbered to GATE-003. All Depends On references updated. Recycle Re-entry Block replaced by Supersession Block. Source: T104-PH001-ST008-AC001.4 GATE-001 (2026-03-20). |`

---

### B. Gate Creation: New `proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md`

**File**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md`
**Action**: CREATE (new file)
**Executor**: LLM_Consultant (this is consultant-authored proposal work)

**Frontmatter requirements**:
```yaml
artifact_type: 'PROPOSAL'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC002'
gate_id: 'P-PH000-ST002-AC002-GATE-002'
version: '1.0.0'
date: '2026-03-20'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md'
analysis_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002-GATE-001_current-state-assessment.md'
external_review_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002-GATE-001_external-review-reassessment.md'
supersedes: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-001_design-decision-disposition.md'
purpose: 'Gate disposition package for GATE-002 — design decision approval for P-STD-002 v1.2.0 baseline (successor to superseded GATE-001)'
consumers:
  - 'P-PH000-ST002-AC002-GATE-002'
```

**Evidence Index requirements (clean — v1.2.0 baseline only)**:
- The new GATE-002 Evidence Index MUST contain only artifacts assessed against the `P-STD-002 v1.2.0` baseline.
- Include a `Historical Evidence` subsection that references the superseded GATE-001 artifacts with a note that they are preserved for historical traceability.

**Evidence Index — Primary Evidence (v1.2.0 baseline)**:
| Evidence Type | Artifact | Path | Notes |
| Analysis | Gate-001 Current-State Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002-GATE-001_current-state-assessment.md` | Rebaselined assessment for v1.2.0 (TK001.4) — carries forward into GATE-002 |
| Analysis | Rebaselined Implementation Requirements Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/analysis/analysis_P-PH000-ST002_status-system-implementation-requirements.md` | v1.2.0 requirements (TK001.5) — carries forward into GATE-002 |
| Analysis | Refreshed Reassessment External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002-GATE-001_external-review-reassessment.md` | v1.2.0 external review (TK001.6) — carries forward into GATE-002 |
| Session | AC002 SES001 (incl. Plan Amendment Addendum) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/snotes/snotes_P-PH000-ST002-AC002-SES001.md` | Documents DEC005–DEC007 (HOLD) and the governance resolution reference |
| Standard | P-STD-002 v1.2.0 | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` | Current normative authority |
| Governance | T104-PH001-ST008-AC001.4 GATE-001 Application Guidance | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_retroactive-ac002-application-guidance.md` | Authorized restructure instructions |

**Evidence Index — Historical Evidence (v1.1.0 baseline, superseded)**:
| Evidence Type | Artifact | Path | Notes |
| Analysis (superseded) | Prior External Review (v1.1.0 baseline) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002_implementation-recommendations-review.md` | SUPERSEDED — assessed against v1.1.0 baseline. Preserved for historical traceability. |
| Proposal (superseded) | GATE-001 Gate-Disposition Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-001_design-decision-disposition.md` | SUPERSEDED — GDR records `Client Decision: SUPERSEDE`. Preserved as historical record. |

**GDR initial state (pending)**:
```
| Gate ID | `P-PH000-ST002-AC002-GATE-002` |
| Consultant Recommendation | [to be populated when package is ready for review] |
| Client Decision | `pending` |
| Gate Status After Decision | `pending` |
| Conditions (if any) | — |
| Decided By | Client |
| Decision Date | — |
| Decision Reference | pending |
```

---

### C. Three-Layer Deprecation: Superseded Analysis Artifacts

The following artifacts were produced against the `P-STD-002 v1.1.0` baseline and must be deprecated using the approved three-layer model.

#### C.1 Layer 1 — Frontmatter + Deprecation Notice

**Artifact**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002_implementation-recommendations-review.md`

Apply the following changes to this artifact's frontmatter and body:

**Frontmatter changes**:
```yaml
status: 'superseded'
superseded_by: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002-GATE-001_external-review-reassessment.md'
```

**Deprecation notice (first line of body, after frontmatter)**:
```
> **SUPERSEDED**: This artifact was produced against the `P-STD-002 v1.1.0` baseline. It has been superseded by `analysis_P-PH000-ST002-AC002-GATE-001_external-review-reassessment.md` which assesses against the `P-STD-002 v1.2.0` baseline. This artifact is preserved for historical traceability only.
```

**Version bump**: Bump to next minor version; add changelog entry recording the supersession.

**Note on other artifacts**: The current-state assessment (`analysis_P-PH000-ST002-AC002-GATE-001_current-state-assessment.md`) and the rebaselined requirements analysis (`analysis_P-PH000-ST002_status-system-implementation-requirements.md`) and the reassessment external review (`analysis_P-PH000-ST002-AC002-GATE-001_external-review-reassessment.md`) are all v1.2.0-baseline artifacts and carry forward as-is into the GATE-002 package. They do NOT require deprecation.

#### C.2 Layer 2 — Evidence Index

**Where**: In the new GATE-002 gate-disposition proposal (§V.B above).
- Primary Evidence section: Contains only v1.2.0-baseline artifacts.
- Historical Evidence subsection: Contains superseded v1.1.0-baseline artifacts with `SUPERSEDED` annotation.

**Where also**: In the superseded GATE-001 gate-disposition proposal:
- The Evidence Index already contains the superseded artifacts. No change needed (the entire GATE-001 proposal becomes a historical artifact; the GDR `Client Decision: SUPERSEDE` marks it as such).

#### C.3 Layer 3 — Links Register (Plan)

**Where**: In `plan_P-PH000-ST002-AC002.md` Links Register section.

Add an entry:
```
| Analysis (superseded) | Prior Implementation Recommendations Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002_implementation-recommendations-review.md` | superseded — v1.1.0 baseline; succeeded by reassessment external review |
```

---

### D. GATE-001 Proposal Update: Record SUPERSEDE Decision

**File**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-001_design-decision-disposition.md`
**Current version**: v1.2.0
**Target version**: v1.3.0

**Change 1 — Frontmatter**:
```yaml
version: '1.3.0'
date: '2026-03-20'
status: 'superseded'
superseded_by: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md'
```

**Change 2 — Deprecation notice (first line after frontmatter)**:
```
> **SUPERSEDED**: This gate-disposition proposal was produced against the `P-STD-002 v1.1.0` baseline. GATE-001 has been closed with `Client Decision: SUPERSEDE` due to an external decision-boundary change (`P-STD-002 v1.2.0` amendment, 2026-03-18). This proposal is preserved as the historical GATE-001 record. The successor gate package is at `proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md`.
```

**Change 3 — GDR update (replace the GDR table)**:
```
| Gate ID | `P-PH000-ST002-AC002-GATE-001` |
| Consultant Recommendation | `SUPERSEDE` |
| Client Decision | `SUPERSEDE` |
| Gate Status After Decision | `superseded` |
| Conditions (if any) | Successor gate: `P-PH000-ST002-AC002-GATE-002`. External event: `P-STD-002 v1.2.0` amendment (2026-03-18) changed the decision boundary. Prior assessment preserved as historically valid for the v1.1.0 baseline. |
| Decided By | Client |
| Decision Date | `2026-03-20` |
| Decision Reference | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_retroactive-ac002-application-guidance.md` |
```

**Change 4 — Changelog entry**:
```
| v1.3.0 | 2026-03-20 | Amendment | GDR updated to record `Client Decision: SUPERSEDE` and `Gate Status After Decision: superseded`. Frontmatter marked `status: superseded` with `superseded_by` reference to GATE-002 proposal. Deprecation notice added. Source: T104-PH001-ST008-AC001.4-GATE-001 governance model approval and retroactive application guidance (TK009). |
```

---

### E. Session Notes Update: `snotes_P-PH000-ST002-AC002-SES001.md`

**File**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/snotes/snotes_P-PH000-ST002-AC002-SES001.md`
**Current version**: v1.1.0
**Target version**: v1.2.0

**Change 1 — Frontmatter version bump**:
- `version: '1.2.0'`
- `date: '2026-03-20'`

**Change 2 — Plan Amendment Addendum §I update**:
- The existing §I Plan Amendment Addendum documents DEC005–DEC007 with the note that governance is "under review" and the restructure is "held pending T104-PH001-ST008-AC001.4-GATE-001 governance resolution."
- Append the following to the §I addendum (as a new sub-section or an inline resolution note):

```
### Resolution (2026-03-20)

The external-impact governance model was approved at `T104-PH001-ST008-AC001.4-GATE-001` on 2026-03-20. The HOLD on GATE-001 reassessment (DEC007) is now lifted.

Classification confirmed: The `P-STD-002 v1.2.0` amendment is an **external, decision-boundary impact** under the approved governance model. Gate supersession is the correct treatment.

Retroactive application: GATE-001 is closed with `Client Decision: SUPERSEDE`. GATE-002 is created as the design decision approval gate for the v1.2.0 baseline. The original GATE-002 (implementation acceptance) is renumbered to GATE-003.

Application authority: `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_retroactive-ac002-application-guidance.md` (TK009)

Status of remediation work: TK001.3–TK001.7 are all completed and their outputs carry forward into the GATE-002 package. No additional remediation is required.
```

**Change 3 — Changelog entry**:
```
| v1.2.0 | 2026-03-20 | Amendment | Added resolution note to §I Plan Amendment Addendum. T104-PH001-ST008-AC001.4-GATE-001 approved the external-impact governance model on 2026-03-20. HOLD lifted; gate supersession confirmed and applied. GATE-001 → SUPERSEDE; GATE-002 created; prior GATE-002 renumbered GATE-003. Source: T104-PH001-ST008-AC001.4 TK009 retroactive application guidance. |
```

---

## VI. RESTRUCTURE SEQUENCE RECOMMENDATION

To maintain internal consistency during the AC002 restructure, apply changes in the following order:

1. **Update GATE-001 proposal** (§V.D) — Record `SUPERSEDE` in the GDR first, so the GATE-001 record is closed before the plan references it as superseded.
2. **Deprecate superseded analysis** (§V.C, Layer 1) — Mark `analysis_P-PH000-ST002-AC002_implementation-recommendations-review.md` with `status: 'superseded'`.
3. **Create GATE-002 proposal** (§V.B) — Author the new gate-disposition proposal with clean Evidence Index and pending GDR.
4. **Update the AC002 plan** (§V.A) — Apply gate register changes, GATE-001 Supersession Block, new GATE-002 section, GATE-003 rename, dependency updates, and Links Register additions.
5. **Update session notes** (§V.E) — Append the resolution note to the §I addendum.

---

## VII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| PLAN | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md` | This guidance approved | LLM_Consultant | Apply §V.A changes |
| PROPOSAL (new) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-002_design-decision-disposition.md` | This guidance approved | LLM_Consultant | Create per §V.B |
| PROPOSAL (update) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-001_design-decision-disposition.md` | This guidance approved | LLM_Consultant | Apply §V.D changes (SUPERSEDE GDR) |
| ANALYSIS (deprecate) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/analysis/analysis_P-PH000-ST002-AC002_implementation-recommendations-review.md` | This guidance approved | LLM_Consultant | Apply §V.C Layer 1 (frontmatter + deprecation notice) |
| NOTES | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/snotes/snotes_P-PH000-ST002-AC002-SES001.md` | This guidance approved | LLM_Consultant | Apply §V.E changes |

---

## VIII. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/plan_T104-PH001-ST008-AC001.4.md` |
| Governance Model (primary design source) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/analysis/analysis_T104-PH001-ST008-AC001.4_gate-impact-classification-assessment.md` §V.B, §V.F |
| GATE-001 Proposal (GIR details) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.4/proposal/proposal_T104-PH001-ST008-AC001.4-GATE-001_gir-disposition-package.md` GIR-009 |
| AC002 Plan (live exemplar) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/plan_P-PH000-ST002-AC002.md` (v1.3.0) |
| AC002 Proposal (live GDR) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/proposal/proposal_P-PH000-ST002-AC002-GATE-001_design-decision-disposition.md` (v1.2.0) |
| AC002 Session Notes (live addendum) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC002/snotes/snotes_P-PH000-ST002-AC002-SES001.md` (v1.1.0) |
| Plan Guideline (§VI.M) | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Proposal Guideline (§VII.C–D) | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |

---

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-20 | Initial | Retroactive AC002 application guidance artifact. Covers: five-file restructure sequence (plan amendment with gate supersession structure, new GATE-002 proposal creation, GATE-001 proposal SUPERSEDE GDR update, three-layer deprecation of v1.1.0 analysis, session notes resolution addendum). Authorized by T104-PH001-ST008-AC001.4-GATE-001 GATE-001 approval (GIR-009). Source: Assessment §V.F retroactive application mechanics. |
