# GUIDELINE: Workspace Notes (Registers + Session Notes)

**Purpose**: Define the authoring standard for Notes so they remain toolable, drift-resistant, and do not accumulate context rot.

**Key rule**: Notes are **session-scoped**. Phase/Stream/Activity "notes" files act as **registers** (indexes). Detailed records live in **one file per Session**.

**Register vs Notes file naming**:
- All files in this system use the `notes_` prefix.
- The role is differentiated by the tokens and the document title:
  - Register files include `PH###`, optionally `ST###`, optionally `AC###`, and MUST use a title containing `NOTES REGISTER`.
  - Session notes files include `-SES###` and MUST use a title containing `SESSION NOTES`.
- Future ideal (deferred): consider introducing a separate filename prefix for register files (e.g., `register_...`) in a later phase to make intent obvious at a glance.

---

## 1. Artifact Types

### 1.1 Phase Notes Register
A Phase Notes Register is the navigation surface for a phase.

- **File name**: `notes_<INIT>-PH###.md` (e.g., `notes_T104-PH001.md`)
- **Role**: index-only. It MUST NOT embed session bodies.
- **Minimum sections**:
  1) Purpose
  2) Phase-Level Session Notes Register (table)
  3) Stream Notes Register (table)
  4) Primary links
  5) Changelog

### 1.2 Stream Notes Register
A Stream Notes Register is the navigation surface for a stream.

- **File name**: `notes_<INIT>-PH###-ST###.md` (e.g., `notes_T104-PH001-ST001.md`)
- **Role**: index-only. It MUST NOT embed session bodies.
- **Minimum sections**:
  1) Stream Summary
  2) Stream-Level Session Notes Register (table)
  3) Activity Notes Register (table)
  4) Primary links
  5) Changelog

### 1.3 Activity Notes Register
An Activity Notes Register is the navigation surface for a single plan Activity.

- **File name**: `notes_<INIT>-PH###-ST###-AC###.md` (e.g., `notes_T104-PH001-ST001-AC002.md`)
- **Location**: `prompt/artifacts/tasks/<INIT>/workspace/notes/PH###/ST###/`
- **Role**: index-only. It MUST NOT embed session bodies.
- **Minimum sections**:
  1) Activity Summary
  2) Activity-Level Session Notes Register (table)
  3) Primary links
  4) Changelog

### 1.4 Phase Session Notes (Sessions)
Phase-level sessions capture meta-discussions that span multiple streams within a phase (e.g., authoring rule changes, phase readiness, cross-stream coordination). These sessions do not belong to any single Stream or Activity.

- **File name**: `notes_<INIT>-PH###-SES###.md` (e.g., `notes_T104-PH001-SES001.md`)
- **Location**: `prompt/artifacts/tasks/<INIT>/workspace/notes/PH###/`
- **ID prefix**: `<INIT>-PH###-SES###` (phase-scoped).
  - Example: `T104-PH001-SES001-DP001`, `T104-PH001-SES001-DEC001`
- **Constraint**: Phase-level sessions MUST NOT duplicate Stream-level or Activity-level decisions. They capture cross-stream coordination, meta-analysis, and phase-scoped planning only.

### 1.5 Stream Session Notes (Sessions)
Stream-level sessions capture meta-discussions that span multiple activities within a stream (e.g., readiness assessments, cross-activity dependency analysis, pre-execution planning). These sessions do not belong to any single Activity.

- **File name**: `notes_<INIT>-PH###-ST###-SES###.md` (e.g., `notes_T104-PH001-ST002-SES001.md`)
- **Location**: `prompt/artifacts/tasks/<INIT>/workspace/notes/PH###/ST###/`
- **ID prefix**: `<INIT>-PH###-ST###-SES###` (stream-scoped).
  - Example: `T104-PH001-ST002-SES001-DP001`, `T104-PH001-ST002-SES001-DEC001`
- **Constraint**: Stream-level sessions MUST NOT duplicate Activity-level decisions. They capture cross-activity coordination, meta-analysis, and stream-scoped planning only.

### 1.6 Activity Session Notes (Sessions)
Activity-level sessions capture work that belongs to a single Activity, but must be split across multiple meetings/sessions to prevent context rot.

- **File name**: `notes_<INIT>-PH###-ST###-AC###-SES###.md` (e.g., `notes_T104-PH001-ST001-AC002-SES001.md`)
- **Location**: `prompt/artifacts/tasks/<INIT>/workspace/notes/PH###/ST###/`
- **ID prefix**: `<INIT>-PH###-ST###-AC###-SES###` (activity-scoped).
  - Example: `T104-PH001-ST001-AC002-SES001-DP001`, `T104-PH001-ST001-AC002-SES001-DEC001`

**Forward-only rule**: Existing Activity Notes files that contain embedded session bodies MAY remain as-is. New authoring SHOULD follow the register + per-session file convention above.

---

## 2. ID Syntax Standards (Session-Scoped)

All structured items inside Session Notes MUST include the `SES###` token in the ID prefix to prevent collisions across sessions.

### 2.1 Session ID prefixes

- Phase session: `<INIT>-PH###-SES###`
- Stream session: `<INIT>-PH###-ST###-SES###`
- Activity session: `<INIT>-PH###-ST###-AC###-SES###`

Example: `T104-PH001-ST001-AC002-SES001`

### 2.2 Item ID format
`[Session-Prefix]-[TYPE][###]`

Examples:
- Discussion Point: `T104-PH001-ST002-SES001-DP001`
- Decision: `T104-PH001-ST002-SES001-DEC001`
- Action: `T104-PH001-ST002-SES001-ACT001`
- Open Question: `T104-PH001-ST002-SES001-OQ001`

**Reset rule**: sequences (`001`) reset per Session Notes file.

---

## 3. Status Enums

### 3.1 Decisions
- `Proposed`
- `Pending`
- `Confirmed`
- `Rejected`
- `Deferred`

### 3.2 Actions
- `pending`
- `in_progress`
- `completed`
- `deferred`

### 3.3 Open Questions
- `Open`
- `Resolved`
- `Deferred to [Phase/Stream]`

---

## 4. Data Schemas (Tables)

### 4.0 Session Notes Register (SES)
| Session | Session ID | Title | Date | Notes File |
|:--|:--|:--|:--|:--|

### 4.1 Discussion Points (DP)
| ID | Topic | Outcome | Rationale | Evidence |
|:---|:------|:--------|:----------|:---------|

### 4.2 Decisions (DEC)
| ID | Decision | Type | Status | Owner | Date | Rationale | Acceptance Signal | Evidence |
|:---|:---------|:-----|:-------|:------|:-----|:----------|:------------------|:---------|

### 4.3 Actions (ACT)
| ID | Action | Owner | Status |
|:---|:-------|:------|:-------|

### 4.4 Open Questions (OQ)
| ID | Topic | Question | Owner | Status | Needed By |
|:---|:------|:---------|:------|:-------|:----------|

---

## 5. Registration & Lifecycle Rules

### 5.1 Just-In-Time Registration

A register row SHALL be added only when its corresponding Notes file exists. Notes files MUST NOT be pre-registered purely because a Plan row exists.

**Rationale**: Activities are subject to consolidation, renumbering, or removal during plan amendments. Pre-registering notes file paths for `planned` activities creates drift when the plan changes, producing orphan references and inaccurate registers.

**Rule**:
- When a Session occurs, the author SHALL:
  1. Create the Session Notes file (`...-SES###.md`) at the standard path.
  2. Add a row to the appropriate Session Notes Register table linking to the new file.
- When an Activity is consolidated, renumbered, or removed, the author SHALL remove any corresponding Activity Notes Register row that no longer has a valid target.

### 5.2 Plan Amendment Sessions

When a consultation session concerns plan structure changes (activity consolidation, renumbering, scope adjustment) rather than new design/requirements work, the session SHALL be recorded as a Session Notes file with a title suffix `(Plan Amendment)`.

**Rationale**: Plan amendments arise from completed work revealing the need for structural changes. Recording the amendment decision trail at the narrowest matching scope preserves causal linkage without creating orphan notes files for activities that don't yet exist.

**Scope rule**: Record plan amendment sessions at the narrowest scope that matches the impact:
- Activity-only impact: Activity Session Notes (1.6) and index it from the Activity Notes Register (1.3).
- Cross-activity within a stream: Stream Session Notes (1.5) and index it from the Stream Notes Register (1.2).
- Cross-stream within a phase: Phase Session Notes (1.4) and index it from the Phase Notes Register (1.1).

**Legacy allowance (forward-only)**: If the affected Activity already uses a legacy "embedded sessions in one file" pattern, appending a plan amendment entry to that file is acceptable.

**Rule**:
- Plan amendment sessions use the standard session file structure (§6).
- Example title: `# STREAM SESSION NOTES: T104 — PH001 / ST002 / SES002 (Plan Amendment: Activity Consolidation)`
- The session's Discussion Points, Decisions, and Actions reference the affected plan file(s) and describe the structural changes.

---

## 6. Session Notes File Structure

Each Session Notes file is a standalone record and MUST contain these sections in order:

1) Agenda / Topics
2) Narrative Summary (Minutes-Style)
3) Discussion Points (DP Table)
4) Decisions Captured (DEC Table)
5) Actions / Carry-Forward (ACT Table)
6) Open Questions Register (OQ Table)
7) Session Handoff Pack

**Session file title format**:
- Phase: `# PHASE SESSION NOTES: <INIT> — PH### / SES### (<Title>)`
- Stream: `# STREAM SESSION NOTES: <INIT> — PH### / ST### / SES### (<Title>)`
- Activity: `# ACTIVITY SESSION NOTES: <INIT> — PH### / ST### / AC### / SES### (<Title>)`
