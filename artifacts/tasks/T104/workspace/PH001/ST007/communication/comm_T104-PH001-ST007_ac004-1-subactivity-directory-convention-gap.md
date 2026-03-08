---
artifact_type: 'COMMUNICATION'
from_initiative: 'T104'
from_stream: 'T104-PH001-ST007'
to_owner: 'Client'
date: '2026-03-05'
subject: 'AC004.1 Directory Split Implemented - Sub-Activity Directory Convention Gap for P-STD-004 Follow-Up'
priority: 'HIGH'
source_plan: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md'
source_sub_activity_plan: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004.1/plan_T104-PH001-ST007-AC004.1.md'
---

# COMMUNICATION: ST007 AC004.1 Sub-Activity Directory Convention Gap

## I. Purpose

Report the AC004.1 artifact relocation to a dedicated sub-activity directory and record the standards/tooling gap discovered during implementation.

## II. Implemented Change

The following AC004.1 artifacts were moved from the parent activity directory into a dedicated sub-activity directory:

- Plan: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004.1/plan_T104-PH001-ST007-AC004.1.md`
- Analysis: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004.1/analysis/analysis_T104-PH001-ST007-AC004.1-TK001_implementation-readiness.md`

All known references in ST007 stream/activity plans were updated to the new paths.

## III. Gap Identified

Current wording in `P-STD-004` and existing validator assumptions are parent-activity centric for sub-activity plan placement (for example, `AC004/plan_...-AC004.1.md`).

This implementation introduces a dedicated dotted directory (`AC004.1/`) for clearer separation of sub-activity artifacts. The current standards text does not explicitly define whether `AC###.N/` directories are prohibited, optional, or preferred for sub-activity artifacts.

## IV. Proposed Follow-Up (No Spec Change in This Changeset)

A future standards update should explicitly define sub-activity and sub-task directory policy under timeline workspace hierarchy, including:

- Whether `AC###.N/` directories are allowed.
- Whether parent-only placement under `AC###/` remains valid for backward compatibility.
- How validators should evaluate UID-scope placement for dotted sub-activity IDs.
- Whether any task-level directory pattern (if adopted in future) is allowed, and how it composes with `AC###` or `AC###.N` scope.

## V. Immediate Tooling Compatibility

To avoid breaking existing repositories that still use parent placement, validator behavior was updated to accept both:

- `AC###.N` artifacts under `AC###.N/`.
- `AC###.N` artifacts under parent `AC###/`.

This preserves backward compatibility while supporting the dedicated-directory model.
