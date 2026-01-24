---
artifact_type: 'GUIDE'
scope: 'T810A2'
purpose: 'Document roles and handling rules for plan/proposal/completion artifacts'
status: 'draft'
owner: 'LLM_Consultant'
---

# Document Governance: Plan / Proposal / Completion (T810A2)

## 1) Roles (authoritative intent)
- **Plan (`plan_...`)**: Roadmap and phase gating; keeps activities, deliverables, gates, and short phase-level status. No per-activity execution logs; no F-RID bodies.
- **Proposal (`proposal_...`)**: Phase-specific collaboration and specification; carries IC table, F-RID bodies, traceability, clarifying questions, and a short phase completion summary. Normative during that phase until merged into the Request.
- **Completion (`completion_...`)**: Non-normative consultancy log; per-activity and per-phase completion notes and improvement guidance. Describes how we got there; never the source of truth for requirements.

## 2) Canonical sources
- **Normative truth for requirements/specs**: Request + current phase Proposal (while in draft/review).
- **Execution history**: Completion file only.
- **Roadmap**: Plan only.

## 3) Editing rules
- Do **not** paste F-RID or ADR bodies into Plan or Completion; reference by ID + section instead.
- Plan status blocks may link to Completion and Proposal/Request but should stay short (3–5 bullets per phase).
- Completion entries must be structured (see template below) and must point to canonical IDs/sections for any normative content.
- If normative wording changes, update Request/Proposal; add a note in Completion that the decision was updated, rather than copying the new text.

## 4) Usage pattern for LLM_Consultant (per activity)
1) Read the relevant Completion entry (prior activity) for context and improvement notes.
2) Read the Proposal/Request sections that contain the normative F-RIDs/decisions.
3) Perform the activity; write the new completion entry; update Proposal (if normative) and Plan phase status (if phase-level progress).

## 5) Completion entry structure (required)
- **Context & references**: Activity name/number, links to Plan section, Proposal/Request sections, relevant IDs.
- **Decisions made**: Bullets summarizing outcomes.
- **Improvement notes / next-activity guidance**: Bullets for what to do or avoid next.
- **Links to canonical specs**: IDs + sections (no inline spec text).

## 6) File naming and location
- Plan: `prompt/artifacts/tasks/T810/consultant/workspace/plan/T810A/T810A2/plan_T810A2-SCHEMA_phase0-4_vX.Y.Z.md`
- Proposal (per phase): `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A2/proposal_T810A2-SCHEMA_phaseN_vX.Y.Z.md`
- Completion (all phases): `prompt/artifacts/tasks/T810/consultant/workspace/completion/T810A/T810A2/completion_T810A2-SCHEMA_vX.Y.Z.md`

## 7) Cross-references to include
- Each Plan and Proposal should link to this guide and to the current Completion file in their introduction/resources section.
- Completion file should remind readers that normative text lives in Proposal/Request, not here.

## 8) Versioning guidance
- Bump Plan/Proposal versions when their role or scope changes (e.g., plan trimmed, new phase proposal).
- Keep Completion version aligned with major Plan/Proposal refactors; minor additions can stay within the same minor version if scope unchanged.

## 9) Anti-drift safeguards
- Never duplicate full specs across artifacts; always cite IDs.
- When decisions change, update normative source first (Proposal/Request), then add a note in Completion that records the change and points to the updated section.
- Keep Plan phase status concise; defer all detail to Completion/Proposal.

## 10) Markdown Structure 

### A. Plan Artifact Heading Hierarchy (plan_...)

- Plan artifacts SHOULD use the following heading hierarchy:
  - `##` Phase
  - `###` Subphase
  - `####` Planned Activities
  - `#####` ActivityTrend Line
- This hierarchy is in addition to the global Markdown header + numbering conventions table below.

| Level   | Markdown Header     | List Type           | Example             |
| ------- | ------------------- | ------------------- | ------------------- |
| Level 1 | `#`                 | *(none)*            | `CLIENT REQUEST`    |
| Level 2 | `##`                | Roman Numerals      | `I.`, `II.`, `III.` |
| Level 3 | `###`               | Capital Letters     | `A.`, `B.`, `C.`    |
| Level 4 | `####`              | Numbers             | `1.`, `2.`, `3.`    |
| Level 5 | `#####`             | Lowercase Roman     | `i.`, `ii.`, `iii.` |
| Level 6 | `######` (optional) | Lowercase Letters   | `a.`, `b.`, `c.`    |
| BELOW   |                     | Bullet Points (•)   | `*`                 |
| BELOW   |                     | Bullet Points (•)   | `-`, or `+`         |
