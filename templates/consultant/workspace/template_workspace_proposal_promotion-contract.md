---
artifact_type: 'PROPOSAL'
initiative_id: '[ID]'
initiative_code: '[CODE]'
phase: '[#]'
stream_id: '[SID-PH###-ST###]'
activity_id: '[SID-PH###-ST###-AC###]'
task_id: '[SID-PH###-ST###-AC###-TK###]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: '[path to governing plan]'
session_reference: '[path to decision session notes]'
source_standard: '[path to source standard/artifact]'
target_standard: '[path to target standard/artifact]'
purpose: 'Promotion contract with deterministic transfer rules and exact content blocks'
---

# PROPOSAL: Promotion Contract - [Source] to [Target]

## I. PURPOSE

- Promotion objective: [what is transferred]
- Delivery context: [task and gate linkage]
- Contract claim: implementation should require no additional design decisions

---

## II. SCOPE AND PRECONDITIONS

In scope:
- [items]

Out of scope:
- [items]

Preconditions:
- [required approvals, sources, baseline version]

---

## III. MAPPING TABLES

| Source Item | Target Item | Mapping Type | Notes |
|:--|:--|:--|:--|
| [T102-STD-XXX-CLAUSE-001] | [P-STD-XXX-CLAUSE-001] | 1:1 | [note] |

---

## IV. REPLACEMENT RULES (ORDERED)

1. [Rule 1]
2. [Rule 2]
3. [Rule 3]

Rule quality bar:
- deterministic
- executable
- no ambiguous replacement terms

---

## V. EXACT NEW CONTENT BLOCKS

### A. [Target section or clause]

```markdown
[exact text to insert]
```

### B. [Target section or clause]

```markdown
[exact text to insert]
```

---

## VI. IMPLEMENTATION EXECUTION NOTES

- Expected execution order: [ordered steps]
- Validation checkpoints: [what to verify]
- Rollback posture: [if applicable]

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `[plan_reference]` |
| Session Notes | `[session_reference]` |
| Source Standard | `[source_standard]` |
| Target Standard | `[target_standard]` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | YYYY-MM-DD | Initial | Initial template instantiation. |
