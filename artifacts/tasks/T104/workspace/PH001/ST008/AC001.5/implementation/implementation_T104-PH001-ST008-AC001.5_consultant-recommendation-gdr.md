# Implementation Plan: AC001.5 — Consultant Recommendation Signal Codification in GDR

## Context & Trigger

During AC003 GATE-001 review, the client identified that the GDR lacks a consultant recommendation field, making it difficult to determine the consultant's gate-level advisory signal. The `Reviewer Verdict` field in the GDR is redundant with the verification artifact and violates `T104-CON-001` (Link Don't Duplicate). Cross-analysis confirmed a structural gap in the three-signal authority chain: Reviewer Verdict (verification) -> Consultant Recommendation (proposal) -> Client Decision (proposal GDR).

## Decisions Recorded

| # | Decision | Client Signal | Date |
|:--|:--|:--|:--|
| D1 | Route as `T104-PH001-ST008-AC001.5` | APPROVE | 2026-03-20 |
| D2 | Consultant Recommendation uses Client Decision taxonomy (`APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT`) | APPROVE | 2026-03-20 |
| D3 | Close AC003 GATE-001 under current schema (no dependency on AC001.5) | APPROVE | 2026-03-20 |
| D4 | Replace `Reviewer Verdict` with `Consultant Recommendation` in GDR (not simply add alongside) | APPROVE | 2026-03-20 |

## Retroactive Scope

Out of scope. Existing GDR instances in live proposals are NOT migrated. New proposals authored after AC001.5 completion will use the updated schema.

---

## File Change Register

| # | File | Path | Current Version | Change Type |
|:--|:--|:--|:--|:--|
| F1 | Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` | v1.5.0 | Schema amendment |
| F2 | Gate-Disposition Template | `prompt/templates/consultant/workspace/template_workspace_proposal_gate-disposition.md` | v1.3.0 | Template amendment |
| F3 | Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | v1.7.0 | Cross-reference clarification |
| F4 | Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` | v3.0.0 | Alignment patch |

---

## F1: `guideline_workspace_proposal.md` — Schema Amendment

### F1-C1: §V.B — Rename Section 5 in gate_disposition required structure

**Location**: §V.B (line ~107)

**Current**:
```markdown
5. Gate Recommendation
```

**Replace with**:
```markdown
5. Consultant Gate Recommendation
```

### F1-C2: §VII.A — Remove overloading rule from Decision gate semantics

**Location**: §VII.A (lines 205-211)

**Current**:
```markdown
### A. Decision gate (`gate_disposition` proposals)

- A decision gate is used to disposition design choices before downstream execution.
- The authoritative approval signal is the proposal-embedded `## Gate Decision Record` section.
- Decision-gate proposals MAY use a proposal-embedded GDR without a separate verification artifact.
- When a verification artifact also exists for the same gate, the proposal-embedded GDR is the authoritative decision record.
- **Plan-level positioning**: The gate-disposition proposal task SHOULD appear as part of the Gate-Readiness Stack — after the verification task for implementation-backed gates, or immediately before the gate row for consultation-only gates. The gate construct MUST include a `Gate-Disposition Proposal` field referencing the proposal path. For the full pattern, see `guideline_workspace_plan.md` §VI.L.
```

**Replace with**:
```markdown
### A. Decision gate (`gate_disposition` proposals)

- A decision gate is used to disposition design choices before downstream execution.
- The authoritative approval signal is the proposal-embedded `## Gate Decision Record` section.
- Decision-gate proposals MAY use a proposal-embedded GDR without a separate verification artifact.
- When a verification artifact also exists for the same gate, the proposal-embedded GDR is the authoritative decision record.
- The GDR carries two decision signals: the **Consultant Recommendation** (advisory) and the **Client Decision** (authoritative). The reviewer verdict is recorded only in the verification artifact and is NOT duplicated into the GDR.
- **Plan-level positioning**: The gate-disposition proposal task SHOULD appear as part of the Gate-Readiness Stack — after the verification task for implementation-backed gates, or immediately before the gate row for consultation-only gates. The gate construct MUST include a `Gate-Disposition Proposal` field referencing the proposal path. For the full pattern, see `guideline_workspace_plan.md` §VI.L.
```

### F1-C3: §VII.B — Update Verification gate semantics

**Location**: §VII.B (lines 213-219)

**Current**:
```markdown
### B. Verification gate

- Verification gates require reviewer-owned verification evidence and verdict taxonomy per `guideline_workspace_verification.md`.
- The verification artifact carries the reviewer verdict in its Gate Recommendation section (§VII of verification template).
- The `gate_disposition` proposal aggregates the reviewer verdict into its GDR alongside the client decision.
- Proposal artifacts MUST NOT substitute for verification artifacts when gate purpose is quality/compliance verification.
- When reviewer verdict or client decision is `RECYCLE`, the proposal MUST describe the same-gate reassessment loop and MUST NOT imply that downstream gate-dependent work may start before reassessment.
```

**Replace with**:
```markdown
### B. Verification gate

- Verification gates require reviewer-owned verification evidence and verdict taxonomy per `guideline_workspace_verification.md`.
- The verification artifact carries the reviewer verdict in its Gate Recommendation section (§VII of verification template). The reviewer verdict is NOT duplicated into the GDR.
- The `gate_disposition` proposal's Consultant Gate Recommendation section (§V) MUST state whether the consultant recommendation aligns with or departs from the reviewer's verdict, with a reference to the verification artifact.
- Proposal artifacts MUST NOT substitute for verification artifacts when gate purpose is quality/compliance verification.
- When consultant recommendation or client decision is `RECYCLE`, the proposal MUST describe the same-gate reassessment loop and MUST NOT imply that downstream gate-dependent work may start before reassessment.
```

### F1-C4: §VII.C — Replace GDR Field Specification

**Location**: §VII.C (lines 221-250)

**Current**:
```markdown
### C. GDR Field Specification

Every `gate_disposition` proposal MUST include a Gate Decision Record as the penultimate section (before Changelog):

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `<GATE-ID>` |
| Reviewer Verdict | [PASS / CONDITIONAL PASS / PASS WITH DEFERRALS / RECYCLE / FAIL / N/A — decision gate] |
| Client Decision | [APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT] |
| Gate Status After Decision | [completed / in_progress / failed / pending] |
| Conditions (if any) | [enumerated list or "—"] |
| Decided By | Client |
| Decision Date | YYYY-MM-DD |
| Decision Reference | [session notes path, inline statement, or "pending"] |

**Reviewer Verdict field rules**:
- When a verification artifact exists for the same gate: the Reviewer Verdict MUST match the verdict recorded in the verification artifact's Gate Recommendation section.
- When no verification artifact exists (pure decision gate): the Reviewer Verdict SHOULD be set to the consultant's recommendation verdict, or `N/A — decision gate` if no formal recommendation is applicable.

**Gate Status After Decision field rules**:
- `pending` is used only while the GDR is awaiting a client decision.
- `completed` is used when `Client Decision` is `APPROVE` or `APPROVE WITH CONDITIONS`.
- `in_progress` is used when `Client Decision` is `RECYCLE`; the gate remains open and the same gate ID is reassessed after remediation.
- `failed` is used when `Client Decision` is `REJECT`.

**RECYCLE-specific GDR rule**:
- When `Client Decision = RECYCLE`, `Conditions (if any)` MUST enumerate the remediation tasks/sub-tasks and the re-entry basis required before the same gate is reassessed.
```

**Replace with**:
```markdown
### C. GDR Field Specification

Every `gate_disposition` proposal MUST include a Gate Decision Record as the penultimate section (before Changelog):

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `<GATE-ID>` |
| Consultant Recommendation | [APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT] |
| Client Decision | [APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT] |
| Gate Status After Decision | [completed / in_progress / failed / pending] |
| Conditions (if any) | [enumerated list or "—"] |
| Decided By | Client |
| Decision Date | YYYY-MM-DD |
| Decision Reference | [session notes path, inline statement, or "pending"] |

**Consultant Recommendation field rules**:
- The Consultant Recommendation is the consultant's consolidated gate-level advisory signal, synthesizing all GIR item dispositions into a single recommendation using the Client Decision taxonomy (`APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT`).
- For implementation-backed gates (where a verification artifact exists): the Consultant Gate Recommendation section (§V) MUST state whether the recommendation aligns with or departs from the reviewer's verdict recorded in the verification artifact. The reviewer verdict is NOT duplicated into the GDR.
- For consultation-only gates (no verification artifact): the Consultant Recommendation is the sole advisory signal. No reviewer verdict exists to reference.

**Gate Status After Decision field rules**:
- `pending` is used only while the GDR is awaiting a client decision.
- `completed` is used when `Client Decision` is `APPROVE` or `APPROVE WITH CONDITIONS`.
- `in_progress` is used when `Client Decision` is `RECYCLE`; the gate remains open and the same gate ID is reassessed after remediation.
- `failed` is used when `Client Decision` is `REJECT`.

**RECYCLE-specific GDR rule**:
- When `Client Decision = RECYCLE`, `Conditions (if any)` MUST enumerate the remediation tasks/sub-tasks and the re-entry basis required before the same gate is reassessed.
```

### F1-C5: §VII.D — Update GDR Lifecycle initial state

**Location**: §VII.D, step 1 (line 253)

**Current**:
```markdown
1. Proposal artifact is authored with GDR section populated as: `Client Decision: pending`, `Gate Status After Decision: pending`, `Decision Date: —`, `Decision Reference: pending`.
```

**Replace with**:
```markdown
1. Proposal artifact is authored with GDR section populated as: `Consultant Recommendation: <consultant's recommendation>`, `Client Decision: pending`, `Gate Status After Decision: pending`, `Decision Date: —`, `Decision Reference: pending`. The Consultant Recommendation is populated at authoring time (not pending), as it represents the consultant's advisory signal that informs the client's decision.
```

### F1-C6: §XI Changelog — Add version entry

**Location**: §XI Changelog table, after the header row (before v1.5.0 entry, line ~323)

**Add new row at the top of the changelog table**:
```markdown
| v1.6.0 | 2026-03-20 | Amendment | §VII.C: Replaced `Reviewer Verdict` with `Consultant Recommendation` in GDR field specification. New field uses Client Decision taxonomy (`APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT`) as the consultant's consolidated gate-level advisory signal. Reviewer verdict remains only in the verification artifact per `T104-CON-001` (Link Don't Duplicate). §VII.A/B: Updated gate semantics to reflect three-signal model (reviewer verdict in verification, consultant recommendation in GDR, client decision in GDR). §V.B: Renamed Section 5 to "Consultant Gate Recommendation". §VII.D: Updated GDR lifecycle to populate consultant recommendation at authoring time. Source: T104-PH001-ST008-AC001.5. |
```

### F1-C7: Frontmatter version bump

**Location**: Frontmatter (lines 7-8)

**Current**:
```yaml
version: '1.5.0'
date: '2026-03-16'
```

**Replace with**:
```yaml
version: '1.6.0'
date: '2026-03-20'
```

---

## F2: `template_workspace_proposal_gate-disposition.md` — Template Amendment

### F2-C1: §V — Rename and restructure Gate Recommendation section

**Location**: §V (lines 85-99)

**Current**:
```markdown
## V. GATE RECOMMENDATION

Recommendation state:
- `PASS` / `CONDITIONAL PASS` / `PASS WITH DEFERRALS` / `RECYCLE` / `FAIL` / `N/A — decision gate`

Conditions and/or deferrals:
- [enumerate or use `-`]

Recycle reassessment path (`RECYCLE` only):
- `Same Gate Reassessed: [GATE-ID]`
- `Required Remediation Tasks: [TK### / TK###.n list]`
- `Downstream Tasks Still Blocked: [task list]`

Downstream enforcement:
- [what may start only after GDR closure]
```

**Replace with**:
```markdown
## V. CONSULTANT GATE RECOMMENDATION

Consultant recommendation:
- `APPROVE` / `APPROVE WITH CONDITIONS` / `RECYCLE` / `REJECT`

Reviewer verdict alignment (implementation-backed gates only):
- Reviewer verdict: `[verdict from verification artifact or "N/A — consultation-only gate"]`
- Verification artifact: `[path to verification artifact or "—"]`
- Alignment: `[Aligned / Departs — <rationale if departing>]`

Conditions and/or deferrals:
- [enumerate or use `—`]

Recycle reassessment path (`RECYCLE` only):
- `Same Gate Reassessed: [GATE-ID]`
- `Required Remediation Tasks: [TK### / TK###.n list]`
- `Downstream Tasks Still Blocked: [task list]`

Downstream enforcement:
- [what may start only after GDR closure]
```

### F2-C2: §VI — Replace GDR table and guidance notes

**Location**: §VI (lines 103-124)

**Current**:
```markdown
## VI. GATE DECISION RECORD (GDR)

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `[gate_id]` |
| Reviewer Verdict | `[PASS / CONDITIONAL PASS / PASS WITH DEFERRALS / RECYCLE / FAIL / N/A — decision gate]` |
| Client Decision | `[APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT / pending]` |
| Gate Status After Decision | `[completed / in_progress / failed / pending]` |
| Conditions (if any) | `[enumerated list or "-"]` |
| Decided By | `Client` |
| Decision Date | `YYYY-MM-DD` |
| Decision Reference | `[session notes path, inline statement, or pending]` |

If no verification artifact exists for the gate:
- `Reviewer Verdict` MAY be the consultant's recommendation verdict or `N/A — decision gate`

If `Client Decision = RECYCLE`:
- `Gate Status After Decision` MUST be `in_progress`
- `Conditions (if any)` MUST enumerate the remediation tasks and re-entry basis
- downstream `Depends On: GATE-###` tasks remain blocked until the same gate later records an approving decision
```

**Replace with**:
```markdown
## VI. GATE DECISION RECORD (GDR)

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `[gate_id]` |
| Consultant Recommendation | `[APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT]` |
| Client Decision | `[APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT / pending]` |
| Gate Status After Decision | `[completed / in_progress / failed / pending]` |
| Conditions (if any) | `[enumerated list or "-"]` |
| Decided By | `Client` |
| Decision Date | `YYYY-MM-DD` |
| Decision Reference | `[session notes path, inline statement, or pending]` |

The `Consultant Recommendation` is populated at authoring time (not pending). It represents the consultant's consolidated advisory signal synthesizing all GIR item dispositions. For implementation-backed gates, Section V documents the relationship to the reviewer's verdict (which remains only in the verification artifact).

If `Client Decision = RECYCLE`:
- `Gate Status After Decision` MUST be `in_progress`
- `Conditions (if any)` MUST enumerate the remediation tasks and re-entry basis
- downstream `Depends On: GATE-###` tasks remain blocked until the same gate later records an approving decision
```

### F2-C3: §VIII Changelog — Add version entry

**Location**: §VIII Changelog table (line ~144)

**Add new row at the top of the changelog table (before v1.3.0 entry)**:
```markdown
| v1.4.0 | 2026-03-20 | Amendment | §V: Renamed from "Gate Recommendation" to "Consultant Gate Recommendation". Taxonomy changed from reviewer verdict values (`PASS/FAIL`) to client decision taxonomy (`APPROVE/REJECT`). Added reviewer verdict alignment subsection for implementation-backed gates. §VI: Replaced `Reviewer Verdict` with `Consultant Recommendation` in GDR table. Updated guidance notes to reflect consultant-owned advisory signal. Source: T104-PH001-ST008-AC001.5. |
```

### F2-C4: Frontmatter version bump

**Location**: Frontmatter (line 10)

**Current**:
```yaml
version: '1.3.0'
```

**Replace with**:
```yaml
version: '1.4.0'
```

---

## F3: `guideline_workspace_verification.md` — Cross-Reference Clarification

### F3-C1: §VIII.B — Update Client Decisions heading and override rule

**Location**: §VIII.B (lines 195-204)

**Current**:
```markdown
### B. Client Decisions (in GDR)

| Decision | Definition |
|:--|:--|
| **APPROVE** | Accept PASS verdict. Gate closed. |
| **APPROVE WITH CONDITIONS** | Accept with conditions. Gate closed; conditions tracked. |
| **RECYCLE** | Agree rework needed. Gate stays open. |
| **REJECT** | Terminate gate. Work killed/redirected. |

**Rule**: Client MAY override reviewer verdict (e.g., REJECT a PASS if Client identifies concerns the reviewer missed). Override MUST be documented with rationale in the GDR.
```

**Replace with**:
```markdown
### B. Client Decisions (in GDR)

| Decision | Definition |
|:--|:--|
| **APPROVE** | Accept gate outcomes. Gate closed. |
| **APPROVE WITH CONDITIONS** | Accept with conditions. Gate closed; conditions tracked. |
| **RECYCLE** | Agree rework needed. Gate stays open. |
| **REJECT** | Terminate gate. Work killed/redirected. |

**Rule**: Client MAY override the consultant recommendation (e.g., REJECT when consultant recommends APPROVE, if Client identifies concerns missed by both reviewer and consultant). Override MUST be documented with rationale in the GDR.
```

### F3-C2: §X — Update GDR cross-reference to clarify three-signal model

**Location**: §X (lines 215-225)

**Current**:
```markdown
## X. GATE DECISION RECORD (GDR) — CROSS-REFERENCE

The Gate Decision Record (GDR) specification, lifecycle, and enforcement rules are defined in `guideline_workspace_proposal.md` §VII (Gate Semantics & Gate Decision Record).

The verification artifact's role at a gate is to provide evidence and a reviewer verdict (§VIII Verdict Taxonomy, §VII Gate Recommendation template section). The GDR — which records the client's decision — is hosted in the `gate_disposition` proposal artifact, not in the verification artifact.

**Cross-reference**: For GDR field specification, lifecycle, and enforcement rules, see `guideline_workspace_proposal.md` §VII.C–E.

**Historical note**: Prior to v1.1.0, this guideline contained the full GDR specification in §X. That specification has been migrated to the proposal guideline to consolidate GDR ownership in the consultant-owned gate package per T104-PH001-ST008-AC001 Option B approval.

**Task decomposition clarification**: Any verification-driven task rework that needs new tracked authority follows `guideline_workspace_plan.md §IV.E` (Task Decomposition Rules), not the Sub-Activity rules in `§VII`.
```

**Replace with**:
```markdown
## X. GATE DECISION RECORD (GDR) — CROSS-REFERENCE

The Gate Decision Record (GDR) specification, lifecycle, and enforcement rules are defined in `guideline_workspace_proposal.md` §VII (Gate Semantics & Gate Decision Record).

The gate decision flow produces three distinct signals:
1. **Reviewer Verdict** (in this artifact's Gate Recommendation section, §VIII): Evidence-based quality/compliance signal using verdict taxonomy (`PASS / CONDITIONAL PASS / PASS WITH DEFERRALS / RECYCLE / FAIL`). Recorded only in the verification artifact — NOT duplicated into the GDR.
2. **Consultant Recommendation** (in the proposal's GDR): Consolidated advisory signal synthesizing reviewer findings and GIR dispositions. Uses client decision taxonomy (`APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT`).
3. **Client Decision** (in the proposal's GDR): Authoritative closure signal. Client MAY override the consultant recommendation.

The verification artifact's role at a gate is to provide evidence and a reviewer verdict. The GDR — which records the consultant's recommendation and the client's decision — is hosted in the `gate_disposition` proposal artifact, not in the verification artifact.

**Cross-reference**: For GDR field specification, lifecycle, and enforcement rules, see `guideline_workspace_proposal.md` §VII.C–E.

**Historical note**: Prior to v1.1.0, this guideline contained the full GDR specification in §X. That specification has been migrated to the proposal guideline to consolidate GDR ownership in the consultant-owned gate package per T104-PH001-ST008-AC001 Option B approval.

**Task decomposition clarification**: Any verification-driven task rework that needs new tracked authority follows `guideline_workspace_plan.md §IV.E` (Task Decomposition Rules), not the Sub-Activity rules in `§VII`.
```

### F3-C3: §XIII Changelog — Add version entry

**Location**: §XIII Changelog table (before v1.7.0 entry)

**Add new row at the top of the changelog table**:
```markdown
| v1.8.0 | 2026-03-20 | Amendment | §VIII.B: Updated Client Decision definitions to remove reviewer-verdict coupling (e.g., "Accept PASS verdict" → "Accept gate outcomes"). Override rule now references consultant recommendation instead of reviewer verdict. §X: Expanded GDR cross-reference to document the three-signal model (reviewer verdict in verification, consultant recommendation in GDR, client decision in GDR). Clarified that the reviewer verdict is NOT duplicated into the GDR. Source: T104-PH001-ST008-AC001.5. |
```

### F3-C4: Frontmatter version bump

**Location**: Frontmatter (lines 7-8)

**Current**:
```yaml
version: '1.7.0'
date: '2026-03-16'
```

**Replace with**:
```yaml
version: '1.8.0'
date: '2026-03-20'
```

---

## F4: `workspace_documentation_rules.md` — Alignment Patch

### F4-C1: §7.A — Add three-signal note to workflow chain rules

**Location**: §7.A Rules list (lines 142-148), after the `VERIFICATION` rule and before the `PROPOSAL` rule

**Current**:
```markdown
- `VERIFICATION` produces independent reviewer evidence and a reviewer verdict for implementation-backed gates only.
- `PROPOSAL` packages decisions and hosts the authoritative Gate Decision Record (GDR) for `gate_disposition` proposals.
```

**Replace with**:
```markdown
- `VERIFICATION` produces independent reviewer evidence and a reviewer verdict for implementation-backed gates only. The reviewer verdict is recorded only in the verification artifact.
- `PROPOSAL` packages decisions and hosts the authoritative Gate Decision Record (GDR) for `gate_disposition` proposals. The GDR carries the consultant's recommendation (advisory) and the client's decision (authoritative). The reviewer verdict is not duplicated into the GDR.
```

### F4-C2: §7.C — Update VERIFICATION and PROPOSAL linkage rules

**Location**: §7.C Inter-Artifact Linkage Rules table (lines 156-165)

**Current**:
```markdown
| `VERIFICATION` holds reviewer verdict and findings; it does not host the GDR | Initiative-level |
| `PROPOSAL` hosts the authoritative GDR for `gate_disposition` proposals | Initiative-level |
```

**Replace with**:
```markdown
| `VERIFICATION` holds reviewer verdict and findings; it does not host the GDR. The reviewer verdict is not duplicated into the GDR | Initiative-level |
| `PROPOSAL` hosts the authoritative GDR containing the consultant recommendation (advisory) and client decision (authoritative) for `gate_disposition` proposals | Initiative-level |
```

### F4-C3: §10.C — Update execution history GDR note

**Location**: §10.C (line 217 area)

**Current**:
```markdown
- `gate_disposition` proposals host the authoritative Gate Decision Record (GDR) for gate closure decisions.
```

**Replace with**:
```markdown
- `gate_disposition` proposals host the authoritative Gate Decision Record (GDR), including the consultant's gate recommendation and the client's closure decision.
```

### F4-C4: §12 Changelog — Add version entry

**Location**: §12 Changelog table (before v3.0.0 entry)

**Add new row at the top of the changelog table**:
```markdown
| v3.1.0 | 2026-03-20 | Amendment | §7.A: Clarified that reviewer verdict stays in VERIFICATION only and PROPOSAL GDR carries consultant recommendation + client decision (three-signal model). §7.C: Updated VERIFICATION and PROPOSAL linkage rules to reflect GDR no longer duplicating reviewer verdict. §10.C: Updated GDR execution history note. Source: T104-PH001-ST008-AC001.5. |
```

### F4-C5: Frontmatter version bump

**Location**: Frontmatter (lines 5-6)

**Current**:
```yaml
version: '3.0.0'
date: '2026-03-20'
```

**Replace with**:
```yaml
version: '3.1.0'
date: '2026-03-20'
```

---

## Execution Checklist

- [ ] F1-C1: Rename §V.B Section 5 to "Consultant Gate Recommendation"
- [ ] F1-C2: Update §VII.A Decision gate semantics (add three-signal note)
- [ ] F1-C3: Update §VII.B Verification gate semantics (remove GDR aggregation, add §V bridge rule)
- [ ] F1-C4: Replace §VII.C GDR Field Specification (Reviewer Verdict -> Consultant Recommendation)
- [ ] F1-C5: Update §VII.D GDR Lifecycle step 1 (consultant recommendation populated at authoring time)
- [ ] F1-C6: Add §XI changelog entry (v1.6.0)
- [ ] F1-C7: Bump frontmatter to v1.6.0
- [ ] F2-C1: Rename and restructure §V Gate Recommendation -> Consultant Gate Recommendation
- [ ] F2-C2: Replace §VI GDR table and guidance notes
- [ ] F2-C3: Add §VIII changelog entry (v1.4.0)
- [ ] F2-C4: Bump frontmatter to v1.4.0
- [ ] F3-C1: Update §VIII.B Client Decisions override rule
- [ ] F3-C2: Update §X GDR cross-reference (three-signal model)
- [ ] F3-C3: Add §XIII changelog entry (v1.8.0)
- [ ] F3-C4: Bump frontmatter to v1.8.0
- [ ] F4-C1: Update §7.A workflow chain rules (three-signal note)
- [ ] F4-C2: Update §7.C linkage rules (VERIFICATION + PROPOSAL rows)
- [ ] F4-C3: Update §10.C execution history GDR note
- [ ] F4-C4: Add §12 changelog entry (v3.1.0)
- [ ] F4-C5: Bump frontmatter to v3.1.0

## Verification Criteria

After all changes are applied, verify:

1. **No `Reviewer Verdict` in GDR**: Grep all 4 files for "Reviewer Verdict" — should appear ONLY in:
   - `guideline_workspace_verification.md` §VIII.A (verdict taxonomy definition — this is correct)
   - Historical/cross-reference context (e.g., verification guideline §X explaining the three-signal model)
   - It MUST NOT appear as a GDR field in the proposal guideline or gate-disposition template

2. **Consultant Recommendation present in GDR**: Both `guideline_workspace_proposal.md` §VII.C and `template_workspace_proposal_gate-disposition.md` §VI contain `Consultant Recommendation` as a GDR field

3. **Section V renamed**: Both `guideline_workspace_proposal.md` §V.B and `template_workspace_proposal_gate-disposition.md` §V use "Consultant Gate Recommendation" heading

4. **Three-signal model documented**: `guideline_workspace_verification.md` §X and `workspace_documentation_rules.md` §7.A both describe the three-signal model

5. **No orphaned references**: No file references "Reviewer Verdict" as a GDR field or instructs authors to populate it in the GDR
