---
artifact_type: 'DEV-REPORT'
initiative_id: '[ID]'
initiative_code: '[CODE]'
phase: '[#]'
stream_id: '[UID]'
activity_id: '[UID]'
task_id: '[<TASK-UID> | <TASK-UID>..<GATE-ID>]'
source_plan: '[repo-relative path to governing plan]'
implementation_reference: '[repo-relative path to governing IMPLEMENTATION artifact, if applicable]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Developer'
decision_owner_role: 'Client'
target_gate: '[gate UID if this slice hands off to a gate; omit otherwise]'
scope: '[bounded execution slice summary]'
consumers:
  - '[next artifact, review package, or owner; omit if not needed]'
consolidated_from:
  - '[source artifact path if this is consolidated or retroactive; omit otherwise]'
---

# DEV-REPORT: [Scope Title] (YYYY-MM-DD)

## 1. EXECUTIVE SUMMARY

Completed in this scope:
- [Implemented item]

Not completed in this scope:
- [Intentional out-of-scope or pending item]

Resulting posture:
- [What this implementation slice now enables]

## 2. IMPLEMENTATION LOG

### 2.1 [Task or grouped slice]

**Files updated**:
- `[repo-relative path]`

**Files created**:
- `[repo-relative path]`

**Applied changes**:
- [Concise change]

**Outputs produced**:
- `[artifact path or "None"]`

**Implementation result**:
- [What changed and why it matters]

### 2.2 [Next task or grouped slice]

**Files updated**:
- `[repo-relative path]`

**Applied changes**:
- [Concise change]

**Outputs produced**:
- `[artifact path or "None"]`

**Implementation result**:
- [Outcome]

## 3. VALIDATION EVIDENCE

### 3.1 Command Results

- `[command]` -> `[PASS | FAIL | expected non-zero]`

### 3.2 Evidence Interpretation

- [What the command/check proved]

## 4. TRACEABILITY MATRIX

| Work Item | Deliverable | Status | Reference |
|:--|:--|:--|:--|
| `[TASK/GATE ID or SPEC-###]` | `[deliverable/evidence]` | `[completed/in_progress/etc.]` | `[path or artifact reference]` |

## 5. HANDOFF

### 5.1 Objective

- [Immediate next review, handoff, or execution objective]

### 5.2 Recommended owner

- `[Role or person]`

### 5.3 Inputs

- `[repo-relative path]` ([why it matters])

### 5.4 Pending decision / next step

- [Blocking decision, follow-up task, or explicit “No external handoff in this slice.”]

<!-- OPTIONAL — include only when the report packages enough outputs that a dedicated index improves navigation -->
## 6. ARTIFACT INDEX

| Artifact | Path | Purpose |
|:--|:--|:--|
| `[name]` | `[repo-relative path]` | `[why it exists]` |

<!-- OPTIONAL — include only when bounded follow-up items or deferrals must be recorded -->
## 7. NOTES / DEFERRALS

- [Deferred or contextual note]

## 8. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | YYYY-MM-DD | Initial | [Initial bounded implementation slice delivery.] |
