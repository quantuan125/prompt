# GUIDELINE: Workspace Notes (Registers + Activity Notes)

**Purpose**: Define the authoring standard for Notes so they remain toolable, drift-resistant, and do not accumulate context rot.

**Key rule**: Notes are **activity-scoped**. Stream notes act as **registers** (indexes). Detailed records live in **one file per Activity**.

---

## 1. Artifact Types

### 1.1 Stream Notes Register
A Stream Notes Register is the navigation surface for a stream.

- **File name**: `notes_<INIT>-PH###-ST###.md` (e.g., `notes_T104-PH001-ST001.md`)
- **Role**: register + optional stream-level sessions. Register section MUST NOT embed Activity-level long-form records. Stream-level sessions (§1.3) are the exception for meta/cross-activity content.
- **Minimum sections**:
  1) Stream Summary
  2) Activity Notes Register (table)
  3) Primary links

### 1.2 Activity Notes
An Activity Notes file contains the detailed records for a single plan Activity.

- **File name**: `notes_<INIT>-PH###-ST###-AC###.md` (e.g., `notes_T104-PH001-ST001-AC002.md`)
- **Recommended location**: `prompt/artifacts/tasks/<INIT>/workspace/notes/PH###/ST###/`
- **Role**: the authoritative history/evidence surface for consultation outcomes tied to that Activity.

### 1.3 Stream-Level Notes (Sessions)
Stream-level sessions capture meta-discussions that span multiple activities within a stream (e.g., readiness assessments, cross-activity dependency analysis, pre-execution planning). These sessions do not belong to any single Activity.

- **Location**: Embedded within the Stream Notes Register file (`notes_<INIT>-PH###-ST###.md`) under a dedicated `## III. STREAM-LEVEL SESSIONS` section, placed after the Activity Notes Register table.
- **ID prefix**: `<INIT>-PH###-ST###` (stream-scoped, no AC component).
  - Example: `T104-PH001-ST002-DP001`, `T104-PH001-ST002-DEC001`
- **Session entry format**: Same structure as §6 (Agenda, Narrative, DP, DEC, ACT, OQ, Handoff).
- **Constraint**: Stream-level sessions MUST NOT duplicate Activity-level decisions. They capture cross-activity coordination, meta-analysis, and stream-scoped planning only.
- **When to use**: When a consultation session concerns the stream as a whole (readiness reviews, scope alignment, cross-activity planning) rather than a specific Activity's deliverables.

---

## 2. ID Syntax Standards (Activity-Scoped)

All structured items inside Activity Notes MUST use the Activity ID as the prefix.

### 2.1 Activity ID prefix
`[Initiative]-[Phase]-[Stream]-AC[###]`

Example: `T104-PH001-ST001-AC002`

### 2.2 Item ID format
`[Activity-ID]-[TYPE][###]`

Examples:
- Discussion Point: `T104-PH001-ST001-AC002-DP001`
- Decision: `T104-PH001-ST001-AC002-DEC001`
- Action: `T104-PH001-ST001-AC002-ACT001`
- Open Question: `T104-PH001-ST001-AC002-OQ001`

**Reset rule**: sequences (`001`) reset per Activity Notes file (not per meeting).

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

A Stream Notes Register row SHALL be added only when its corresponding Activity transitions to `in_progress`. Notes files for `planned` activities MUST NOT be pre-registered in the Stream Notes Register.

**Rationale**: Activities are subject to consolidation, renumbering, or removal during plan amendments. Pre-registering notes file paths for `planned` activities creates drift when the plan changes, producing orphan references and inaccurate registers.

**Rule**:
- When an Activity status changes to `in_progress`, the author SHALL:
  1. Create the Activity Notes file at the standard path.
  2. Add a row to the Stream Notes Register linking to the new file.
- When an Activity is consolidated, renumbered, or removed, the author SHALL remove any corresponding row from the Stream Notes Register.

### 5.2 Plan Amendment Sessions

When a consultation session concerns plan structure changes (activity consolidation, renumbering, scope adjustment) rather than new design/requirements work, the session SHALL be appended to the most recent completed Activity's notes file as a **Plan Amendment** session entry.

**Rationale**: Plan amendments arise from completed work revealing the need for structural changes. Recording the amendment decision trail in the most recent completed Activity's notes preserves causal linkage without creating orphan notes files for activities that don't yet exist.

**Stream-level alternative**: If the plan amendment concerns a stream that has no completed Activities (all `planned`), the session MAY be recorded as a stream-level session (§1.3) in the Stream Notes Register file instead.

**Rule**:
- Plan amendment sessions use the standard session entry structure (§6) with the heading suffix `(Plan Amendment)`.
- Example: `### Session — 2026-02-05 (Plan Amendment: Activity Consolidation)`
- The session's Discussion Points, Decisions, and Actions reference the affected plan file(s) and describe the structural changes.

---

## 6. Session Entry Structure (within an Activity Notes file)

If an Activity requires multiple meetings, append multiple session entries in the same Activity Notes file.

Each session entry MUST contain these sections in order:

A. Agenda / Topics
B. Narrative Summary (Minutes-Style)
C. Discussion Points (DP Table)
D. Decisions Captured (DEC Table)
E. Actions / Carry-Forward (ACT Table)
F. Open Questions Register (OQ Table)
G. Session Handoff Pack

**Session entry heading format (no separate session ID)**:
- `### Session — YYYY-MM-DD (Title)`

