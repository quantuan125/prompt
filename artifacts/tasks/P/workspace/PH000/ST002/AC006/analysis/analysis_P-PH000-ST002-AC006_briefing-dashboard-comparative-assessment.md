---
artifact_type: 'ANALYSIS'
analysis_type: 'comparative_analysis'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-TK002'
version: '1.0.0'
date: '2026-03-30'
status: 'completed'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
purpose: 'Comparative analysis of briefing dashboard placement, derivation model, and V1 filtering boundary for AC006.'
options_compared: 'separate briefing file vs status_program section vs skill-generated ephemeral output'
evaluation_criteria: 'client usability, authority-hierarchy compliance, maintenance burden, handoff-pack traceability, assistant commissionability, future extensibility'
recommended_option: 'separate briefing_program.md derived manually from status_program.yaml with bounded supporting pointers'
---

# ANALYSIS: AC006 Briefing Dashboard Comparative Analysis

## I. EXECUTIVE SUMMARY

**Purpose**: Compare the viable architectural options for the AC006 briefing dashboard and select the V1.1 pattern that best supports client-facing continuity without contaminating the authoritative status surfaces.

**Scope**: Placement, derivation method, filtering model, and downstream implementation implications for the briefing dashboard only.

**Conclusion / Recommendation**: A separate derived briefing file at `prompt/artifacts/tasks/P/status/briefing_program.md` is the strongest option by a clear margin. It preserves `status_program.yaml` as the authoritative source, keeps `status_program.md` bounded as the narrative system-of-record, and gives the client a focused, prompt-assist-only surface for active work, recent movement, and dependency watch items.

### Client Summary

- The client-facing briefing should not be embedded into `status_program.md`; that file is already too broad and too large for continuity use.
- A separate `briefing_program.md` file gives the cleanest reading experience and the lowest governance risk.
- The briefing should be manually derived from `status_program.yaml`, with notes-register and session-note links used as supporting pointers rather than as authority sources.
- V1 should stay bounded to three sections: `Active Work Briefing`, `Recent Movement Watchlist`, and `Dependency Watchlist`.
- `Active Work Briefing` should include only `in_progress` activities.
- `Recent Movement Watchlist` should include a bounded set of recently updated non-terminal activities that matter for immediate continuity.
- Cross-scope prioritization should remain limited to a dependency watchlist in V1. Deeper prioritization logic belongs in the later future status-system initiative.
- Skill-generated ephemeral output is not recommended because it is the weakest option for auditability and stable client reuse.

## II. SCOPE & INPUTS

**In scope**:
- Compare briefing placement options
- Compare derivation models and maintenance posture
- Select a bounded V1 filtering model
- Define the recommendation that TK003 and TK005 will operationalize

**Out of scope**:
- Rewriting `status_program.md`
- Creating the briefing artifact itself
- Session-close skill architecture, which is already governed by AC004 authority
- Future automation or future initiative commissioning

**Inputs reviewed (repo-relative paths)**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_session-close-and-briefing-gap-audit.md`
- `prompt/artifacts/tasks/P/status/status_program.yaml`
- `prompt/artifacts/tasks/P/status/status_program.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md`
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`

## III. EVIDENCE / METHODOLOGY

**Method**:
1. Reused the completed TK001 audit as the requirements baseline for the briefing feature.
2. Reviewed the authoritative status ledger and derived status narrative to confirm the current data shape and current client pain points.
3. Compared three viable architectural options against weighted criteria that reflect client-readability, governance safety, and downstream execution clarity.
4. Selected the option that best preserves the authority hierarchy while remaining easy for an assistant to build and maintain later.

**Commands run (if any)**:
```bash
Get-Content prompt/artifacts/tasks/P/status/status_program.md | Select-Object -First 140
Get-Content prompt/artifacts/tasks/P/status/status_program.yaml | Select-Object -Skip 560 -First 100
```

**Evidence notes**:
- `status_program.md` already carries the authoritative narrative, health tables, evidence digest, and protocol guidance; embedding the briefing there would mix audiences.
- `status_program.yaml` already contains the canonical fields needed to seed a briefing surface: scope ID, name, status, last updated date, dependency edges, and evidence pointers.
- The TK001 audit already established that clients need a dedicated continuity surface and that the existing status narrative is too broad for that purpose.
- The notes register structure provides stable paths to the latest session-note files, which can be surfaced as bounded pointers inside the briefing.

## IV. FINDINGS / GAP REGISTER

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | structure | Embedded briefing would overload the narrative | Adding a client briefing section into `status_program.md` would further overload a narrative file that already serves as system-of-record plus protocol surface. | `resolved` | `P-PH000-ST002-AC006-TK003` | Resolved by selecting a separate file. |
| GAP-002 | workflow | Ephemeral skill output is too weak for auditability | A skill-generated-only output would be the hardest option to cite, review, and preserve as a stable continuity surface. | `resolved` | `P-PH000-ST002-AC006-TK003` | Rejected as the primary architecture. |
| GAP-003 | references | V1 needs a bounded source hierarchy | The briefing needs a simple authority model: ledger first, supporting pointers second, no new authority source. | `resolved` | `P-PH000-ST002-AC006-TK003` | Implemented in the recommendation. |
| GAP-004 | workflow | Cross-scope prioritization must stay bounded | The client needs some cross-scope visibility, but full prioritization logic exceeds AC006 V1.1. | `deferred_to_TK005` | `P-PH000-ST002-AC006-TK005` | Limit V1 to a dependency watchlist and defer richer prioritization. |

## V. COMPARATIVE ANALYSIS (TRADE STUDY)

### A. Options Under Comparison

| Option | Label | Description |
|:--|:--|:--|
| Option A | Separate Briefing File | Create `prompt/artifacts/tasks/P/status/briefing_program.md` as a prompt-assist-only derived client briefing surface. |
| Option B | Embedded Narrative Section | Add a dedicated briefing section inside `prompt/artifacts/tasks/P/status/status_program.md`. |
| Option C | Skill-Generated Ephemeral Output | Keep the briefing as a generated response pattern with no stable file artifact. |

### B. Evaluation Criteria & Weighting

| Criterion | Definition | Weight |
|:--|:--|:--|
| Client Usability | How quickly the client can answer “what is active and what changed?” | 25 |
| Authority-Hierarchy Compliance | How well the option preserves ledger authority and avoids surface contamination | 20 |
| Maintenance Burden | How easy the option is to update without duplicating too much state | 15 |
| Handoff-Pack Traceability | How clearly the option can point to latest session handoff packs | 15 |
| Assistant Commissionability | How easy it is for a downstream assistant to build from an implementation spec | 15 |
| Future Extensibility | How well the option can support later enhancements without rework | 10 |

### C. Comparative Assessment Matrix

| Criterion | Weight | Option A | Option B | Option C | Notes |
|:--|:--|:--|:--|:--|:--|
| Client Usability | 25 | 5 - dedicated reading surface with no narrative clutter | 2 - briefing is buried in an already-long narrative | 3 - focused in-session, but not stable for later reuse | The client needs a low-friction continuity view. |
| Authority-Hierarchy Compliance | 20 | 5 - ledger remains authoritative and briefing is clearly derived | 3 - derivation can still work, but audience boundaries blur | 2 - generated output risks becoming uncited de facto authority | AC006 must preserve the ledger/narrative hierarchy. |
| Maintenance Burden | 15 | 4 - one bounded derived file to update | 3 - fewer files, but heavier narrative maintenance | 2 - low file count, but repeated manual regeneration with no stable checkpoint | Maintenance must stay predictable for assistants. |
| Handoff-Pack Traceability | 15 | 5 - explicit handoff-pointer columns fit naturally | 3 - pointers compete with narrative density | 2 - pointers are transient unless manually recopied each time | Latest session handoff access is a core requirement. |
| Assistant Commissionability | 15 | 5 - deterministic target file, sections, and tables | 3 - assistant must splice into a large narrative without drift | 2 - no stable artifact target | TK005 needs a clean execution target. |
| Future Extensibility | 10 | 4 - can grow in place without mutating the narrative protocol | 2 - more growth further overloads `status_program.md` | 3 - flexible, but weakly governed | AC006 needs a bounded V1.1 that can expand later if approved. |

### D. Weighted Outcome

| Option | Weighted Outcome | Result |
|:--|:--|:--|
| Option A | 480 | Highest score and recommended |
| Option B | 275 | Too much audience and scope collision |
| Option C | 245 | Weakest auditability and weakest stable reuse |

### E. Recommendation

- Choose **Option A**.
- The approved V1.1 briefing pattern should be a separate Markdown artifact at `prompt/artifacts/tasks/P/status/briefing_program.md`.
- The artifact should be manually derived from `status_program.yaml` as the primary source. `status_program.md` and stream/activity notes are supporting reference surfaces only.
- V1.1 should contain exactly three sections:
  - `Active Work Briefing`: all `in_progress` activities
  - `Recent Movement Watchlist`: recently updated non-terminal activities relevant to immediate continuity
  - `Dependency Watchlist`: open critical dependencies touching activities listed in the first two sections
- The recommendation explicitly rejects embedding the briefing into `status_program.md` and rejects making ephemeral skill output the primary briefing surface.
- Richer prioritization logic beyond the dependency watchlist is deferred to the future status-system initiative.

## VIII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| `proposal` | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006_briefing-dashboard-standards-input.md` | Comparative analysis complete | `LLM_Consultant` | TK003 must convert the recommendation into explicit briefing conventions and client decision requests. |
| `implementation` | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/implementation/implementation_P-PH000-ST002-AC006_briefing-dashboard-task-specification.md` | TK003 disposition boundary defined | `LLM_Consultant` | TK005 should commission the separate `briefing_program.md` file and its bounded section/table model. |
| `proposal` | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` | TK003, TK004, and TK005 complete | `LLM_Consultant` | TK006 should treat this comparative analysis as primary evidence for the dashboard-placement decision. |

## IX. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Supporting Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_session-close-and-briefing-gap-audit.md` |
| Primary inputs | `prompt/artifacts/tasks/P/status/status_program.yaml`; `prompt/artifacts/tasks/P/status/status_program.md`; `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |

## X. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-30 | Initial | Compared separate-file, embedded-section, and skill-generated briefing architectures for AC006 and selected a separate `briefing_program.md` derived from the authoritative ledger as the recommended V1.1 pattern. |
