---
doc_type: "Epic Consultancy Procedural Guideline"
scope: "SPS Epic Authoring Process"
version: "1.0.0"
date: "2025-10-01"
status: "draft"
author: "LLM_Consultant"
---

# Epic Consultancy Procedural Guideline

Purpose: Provide a practical, process‑only guide for conducting a consultancy session to author or refine a single Epic in an SPS document with the client. This guide is free of artifact role definitions and policy/governance content; it focuses solely on how to run the process and co‑author the epic sections.

## 1. Principles
- Process only: capture how to work, not what the policies are.
- Collaborative drafting: co‑author every section with the client via short propose→confirm loops.
- Clarity over completeness: finish a thin, correct pass before deepening.
- Evidence first: base edits on the SPS template and current project materials the client provides.
- Traceable edits: record what changed and why in the epic changelog at the end.
- Minimal drift: avoid duplicating initiative‑wide content; include epic deltas only where applicable.

## 2. Session Overview
- Intake & Framing: align objectives, scope (this epic only), success criteria.
- Working Loops: iterate section by section with propose→confirm cycles.
- QA & Validation: run section‑level and global checks.
- Wrap‑up: summarize decisions, capture loose ends, and update changelog.

## 3. Preparation Checklist
- Locate the SPS document and the target epic section.
- Collect any prior notes, consultation transcripts, or draft text the client wants incorporated.
- Confirm the output format and any editing constraints (file paths, naming, review flow).
- Define success for the session (e.g., which sections must be completed today).
- Establish ground rules: no policy decisions; focus on wording and structure; capture open questions explicitly.

## 4. Consultation Flow (Facilitator Script)
1) Intake & Framing (2–5 minutes)
   - Purpose: restate the goal in one sentence; confirm scope is a single epic.
   - Ask: which sections are priority; any must‑keeps or must‑avoid points.
   - Output: a short plan of sections to cover in order.

2) Section Working Loop (repeat per section)
   - Select section: announce which section is in focus.
   - Elicit inputs: ask targeted prompts (see Section 5) to gather facts and intent.
   - Draft: propose a concise first pass (1–2 paragraphs or a small table/list).
   - Confirm: ask for accept/modify; capture edits immediately.
   - Lock: mark section as “provisionally complete”; log any follow‑ups.

3) QA & Validation Pass
   - Run the per‑section checklist.
   - Run the global checklist (Section 6) across the epic.

4) Wrap‑up
   - Read back what changed, what’s parked, and next actions.
   - Update the epic changelog with dated bullets.
   - Confirm the client is satisfied with today’s scope of completion.

## 5. Section Authoring Playbooks (Process‑Only)

The following playbooks guide the facilitation for each epic section. Avoid injecting policy details; capture the client’s intent in clear, minimal text.

### 5.1 Purpose
- Ask:
  - What outcome does this epic enable in plain business terms?
  - Who benefits and how is success recognized at a high level?
- Drafting rules: two short paragraphs max; avoid implementation details and identifiers.
- Accept when: it reads clearly to non‑technical stakeholders and is specific to this epic.

### 5.2 Scope (In / Out)
- Ask:
  - What is explicitly included in this epic’s responsibility?
  - What related work is explicitly excluded or handled elsewhere?
- Drafting rules: two bullet lists (In Scope, Out of Scope); keep items crisp and testable.
- Accept when: boundaries are unambiguous and non‑overlapping.

### 5.3 Governance (Control Items Table) — Process Handling Only
- Ask:
  - What control parameters does the client want listed for this epic?
  - What details belong elsewhere and should be referenced rather than restated?
- Drafting rules: create a concise two‑column table; do not define or change any policies.
- Accept when: entries are concise and defer details to their proper documents.

### 5.4 Inherited Considerations
- Ask:
  - Which initiative‑level rules materially constrain how this epic is authored?
  - Which are most critical to surface here (others remain implicitly inherited)?
- Drafting rules: include only a curated subset; cite by identifier and title if provided by the client; avoid restating full text.
- Accept when: the table is short, relevant, and non‑duplicative.

### 5.5 Epic Quality Goals
- Ask:
  - What measurable outcomes define “done well” for this epic?
  - How will we verify each outcome objectively?
- Drafting rules: atomic bullets with clear success tests; prefix with epic‑scoped IDs if provided.
- Accept when: each goal is testable and scoped to this epic.

### 5.6 Epic Dependencies & Interfaces
- Ask:
  - What this epic relies on to proceed (documents, approvals, inputs)?
  - What downstream artifacts or consumers rely on outputs from this epic?
- Drafting rules: list as compact bullets; include brief rationale.
- Accept when: upstream and downstream touchpoints are obvious and minimal.

### 5.7 Epic Assumptions (Optional)
- Ask:
  - Are there epic‑specific assumptions that differ from initiative‑level ones?
- Drafting rules: only record deltas; keep each assumption one line.
- Accept when: nothing repeats higher‑level assumptions.

### 5.8 Epic Constraints (Optional)
- Ask:
  - Are there epic‑specific constraints that differ from initiative‑level ones?
- Drafting rules: only record deltas; one line each.
- Accept when: constraints are specific and actionable.

### 5.9 Epic Notes & Parking Lot
- Ask:
  - What context or open questions should we track without blocking authoring?
- Drafting rules: one idea per bullet; tag items as Note or Parking‑Lot.
- Accept when: the list is short and directly useful for future sessions.

### 5.10 Epic GDR Index — Process Handling Only
- Ask:
  - Does the client want any epic‑level decisions recorded here at this time?
  - If yes, what minimal title and summary should be captured now?
- Drafting rules: scaffold entries (table row + brief body) only when explicitly requested; otherwise leave the index scaffolded but empty.
- Accept when: entries exist only as needed; no policy text is invented by the facilitator.

### 5.11 Feature Register
- Ask:
  - What features belong to this epic today, and what is their current status?
  - Where are their canonical descriptions maintained (paths or references)?
- Drafting rules: one row per feature with ID, short name, 1–2 line purpose, status, and canonical link.
- Accept when: only features are listed; no feature identifiers appear elsewhere in the epic text.

### 5.12 Epic Issues & Risks
- Ask:
  - What open issues or risks are specific to this epic?
  - For each, what is the current status and next action?
- Drafting rules: table with ID, description, owner/name, status; add brief “how to resolve” in the description where known.
- Accept when: each entry has a clear disposition (open with action, or closed with rationale).

### 5.13 Epic Changelog
- Ask:
  - What did we change today that should be recorded for traceability?
- Drafting rules: dated bullets with short summaries.
- Accept when: changes are auditable at a glance.

## 6. Validation Checklists

### 6.1 Per‑Section Checklist
- Clear, concise, and audience‑appropriate language.
- No unnecessary repetition of initiative‑level content.
- Section adheres to its structural expectations (paragraphs, bullets, or table as applicable).
- Open questions or follow‑ups are captured in Notes/Parking Lot.

### 6.2 Global Epic Checklist
- All required sections exist with at least a thin, correct pass.
- No feature identifiers appear outside the Feature Register.
- Section cross‑references are consistent and non‑contradictory.
- Issues/Risks have owners/names and actionable statuses.
- Changelog includes dated entries summarizing the session’s edits.

## 7. Collaboration Cadence
- Short cycles: propose→confirm edits in under five minutes per subsection.
- Socratic prompts: ask targeted, concrete questions; avoid leading the content.
- Read‑backs: summarize after each section; confirm acceptance explicitly.
- Parking discipline: defer unresolved topics to Notes/Parking Lot to protect flow.

## 8. Anti‑Patterns to Avoid
- Writing policy or defining authority in this guide or during drafting.
- Over‑specifying details not required by the section structure.
- Duplicating higher‑level content instead of referencing it briefly.
- Introducing feature identifiers outside the Feature Register.
- Leaving sections half‑drafted without capturing open questions.

## 9. Wrap‑Up & Handover
- Review the epic end‑to‑end for coherence and completeness.
- Confirm final wording changes live with the client.
- Update the epic changelog with today’s date and a succinct summary.
- List any follow‑ups, owners/names, and target timelines in Notes/Parking Lot or Issues.
- Share the updated file path for client review and archival.

## 10. Appendix — Question Bank (Examples)
- Purpose: “In one sentence, what success looks like for this epic?”
- Scope: “Name three items definitely in, and three definitely out.”
- Quality Goals: “How would we objectively verify this epic was done well?”
- Dependencies: “What inputs must exist before this epic can progress?”
- Issues/Risks: “What could block progress in the next two weeks?”
- Changelog: “What changed today that future readers should know?”

