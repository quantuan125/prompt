---
artifact_type: 'REPORT'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1'
research_id: 'T810A-RES-003'
version: '1.0.0'
iteration: '1'
date: '2025-10-14'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: LLM_Gastro Knowledge Taxonomy & Access Patterns

## I. Executive summary

This surface-level research enumerates ChatGPT-native knowledge types, how each is accessed, and where LLM_Gastro content should live for Story **T810A1-S04 (Knowledge Base)**. It also proposes a lean Block 4 structure to declare this to the agent. Scope is **platform-native only** (no custom RAG/tools) per constraints. 

---

## II. Knowledge type taxonomy (platform-validated)

**Naming for clarity** (maps to client’s System/Project/Internal/External):

1. **Internal Model Knowledge (“Internal”)**
   What: Model’s pretrained parameters + general world knowledge.
   Access: Always available implicitly.
   Notes: Not version-pinned; may differ from canon; must be bounded by KB sources. ([OpenAI Help Center][1])

2. **Knowledge Files & Project Files (“Project”)**
   What: Files you attach as **Knowledge** to a custom GPT or place inside a **Project**; used as a private KB.
   Access: Auto-indexed and retrieved by the GPT when relevant; configured by builder.
   Notes: Enterprise/Team projects introduce persistent “project memory/files.” ([OpenAI Help Center][2])

3. **Saved Memory & Chat History (”System”)**
   What: Cross-session **Saved Memories** plus **Chat History** reference; can auto-update; user-controllable.
   Access: Implicit; can be turned on/off and edited/deleted by user/admin.
   Notes: For S04, memory is acknowledged but **Stable JSON remains the authority** (see mapping). ([OpenAI Help Center][3])

4. **Web Search / Browsing (”External”)**
   What: Built-in web search capability for current info & source-backed answers; admin-toggleable.
   Access: **Tool-invoked** by model automatically or user-initiated; enabled per GPT/project settings.
   Notes: Use only when needed; S04 will include minimal trigger language. ([OpenAI Help Center][4])

5. **OTHERS (platform-native but out-of-scope for MVP)**
   Examples: Data Analysis/Code Interpreter, agents, connectors.
   Rationale: Not required for S04; list only to future-proof taxonomy. ([OpenAI Help Center][5])

**Governance anchor (clinical canon already defined):** Block 4 must recognize the **GI Knowledge Base Source Standard** (ROME IV, Bristol, ACG/AGA, alarm features) as the authoritative clinical content set for MVP.

---

## III. Access pattern matrix (how each type is used)

| Knowledge type                  | How it loads                 | Who controls       | Typical triggers                    | Key constraints (S04)                                                                                       |
| ------------------------------- | ---------------------------- | ------------------ | ----------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Internal model                  | Implicit/always              | OpenAI (model)     | Any prompt                          | May disagree with canon; treat as fallback, not authority. ([OpenAI Help Center][1])                        |
| Knowledge files / Project files | Auto-retrieved when relevant | Builder/Admin      | Question overlaps with file content | **Read-only to LLM_Gastro**; content curated/versioned; persists across sessions. ([OpenAI Help Center][2]) |
| Saved memory & chat history     | Implicit when enabled        | User/Admin         | Session start & throughout          | Memory is editable, can drift; **Stable JSON > Memory** precedence. ([OpenAI Help Center][3])               |
| Web search                      | Tool invocation              | Builder/Admin/User | Freshness gaps, citations needed    | Enterprise-toggleable; cite sources; use sparingly for clinical topics. ([OpenAI Help Center][4])           |
| Others (agents, analysis)       | Tool invocation              | Builder/Admin      | Specialized tasks                   | Not used in S04; keep listed only. ([OpenAI Help Center][5])                                                |

**Platform constraints to encode in S04:** read-only file access, no programmatic schema validation, default “helpful assistant” behavior must be overridden via prompt roles/protocols. 

---

## IV. Content → knowledge-type mapping (for LLM_Gastro)

1. **Clinical sources (ROME IV, Bristol, ACG/AGA, alarm features)**
   → **Project Knowledge** (Knowledge files / Project files). Treat as **canonical**; include version/date notes in Block 4. 

2. **Stable JSON (patient profile)**
   → **Project Knowledge** (Knowledge files), **read-only for the model**, manually maintained by patient outside chat; Block 4 states “details in T810A2.” 

3. **Dynamic JSON skeletons (entry templates/examples)**
   → **Project Knowledge** as **read-only exemplars** (KB), with generation rules deferred to S05; S04 references their existence only. 

4. **Session reports / prior day summaries**
   → **Saved Memory** (acknowledge existence) **and/or** **Project files** when explicitly stored. For MVP, refer to Memory Review Protocol (Step 0) to reconcile with profile. 

**Precedence statement for Block 4:** *When Project Knowledge conflicts with Model/Memory, **Project Knowledge wins**; when Memory conflicts with Stable JSON, **Stable JSON wins**.*

---

## V. Recommended Block 4 (Knowledge Base) structure (lean)

Keep it simple and declarative (no tool boilerplate). Suggested subsections:

1. **4.1 Knowledge Types (What I can use)**

* Internal Model (fallback)
* Project Knowledge (canonical: clinical sources; Stable JSON; Dynamic skeleton exemplars)
* Saved Memory (acknowledge; precedence rule)
* Web Search (when/why)
  *(One-line definition each; 3–4 bullets max.)* 

2. **4.2 Access Rules (How I use them)**

* Auto-available vs. read-only vs. tool-invoked
* Trigger cues (e.g., “if freshness/uncertainty, consider web search”)
* Authority & precedence (Stable JSON > Memory; Project Knowledge > Model).

3. **4.3 Content Inventory (What’s inside Project Knowledge)**

* Clinical canon list (ROME IV, Bristol, ACG/AGA, alarm features) w/ version/date placeholders
* File pointers/names (paths live in T810A2; S04 just lists categories). 

4. **4.4 Constraints (What I cannot do)**

* Cannot write to files; cannot validate schemas programmatically; must use prompt-level validation/exemplars. 

*(Notes: Memory behavior referenced, not re-explained; execution triggers and validation phrasing live in Block 5 & S05.)* 

---

## VI. Memory architecture clarification (for INT-005 references)

* **Step 0: Memory Review** before loading profile—identify discrepancies between Memory and Stable JSON; politely probe to resolve.
* **Precedence**: Stable JSON governs structured facts; log differences conversationally.
* **Scope**: Mention behavior only; do not duplicate INT-005 details in Block 4. 

---

## VII. S04 FR recommendations (ready for LLM_Consultant drafting)

* **FR-001 – Knowledge Type Enumeration**: Block 4 lists and defines Internal, Project, System (Memory), External (Web), Others (declared out-of-scope). 
* **FR-002 – Clinical Canon Placement**: Declare clinical sources live in **Project Knowledge** and are **authoritative** with version/date fields. 
* **FR-003 – Stable & Dynamic JSON Placement**: Stable JSON in **Project Knowledge (read-only)**; Dynamic JSON skeletons in **Project Knowledge (exemplars only)**, with generation rules deferred.
* **FR-004 – Access & Precedence Matrix**: Encode access modes (auto/manual/tool) and precedence rules (Project > Model; Stable JSON > Memory).
* **FR-005 – Constraints Banner**: Re-state platform constraints (read-only files; no schema validation; default behavior override lives in Block 5). 

---

## VIII. References (platform-native, authoritative)

* **Knowledge in GPTs** (how Knowledge files work). ([OpenAI Help Center][2])
* **Creating a GPT** (configure knowledge & web). ([OpenAI Help Center][6])
* **Memory FAQ** and **What is Memory?** (saved memory & chat history behaviors). ([OpenAI Help Center][3])
* **ChatGPT Capabilities Overview** (Search/Web). ([OpenAI Help Center][1])
* **ChatGPT Search for Enterprise** (admin toggle for web search). ([OpenAI Help Center][7])
* **Projects in ChatGPT** (project memory/files persistence). ([OpenAI Help Center][8])
* **GI Knowledge Base Source Standard** (ROME IV, Bristol, ACG/AGA, alarm features). 
* **Platform constraints & JSON split** (read-only, validation limits).

---

## IX. Appendices (context pointers)

* Research brief & deliverable scope (this effort).
* Request & governance anchors (S04 placeholder; INT-004/005; CON-008). 
* Implementation target (gastro_system.md Block 4 placeholder). 

---

## X. Minimal content inventory (to populate in S04)

### A. Required Documents

1. **Clinical Canon Summaries** (`.md`)

   * ROME IV, Bristol Chart, ACG/AGA, Alarm Features digests.
   * Contain *Version & Date* line; structured bullets.

2. **Bristol Stool Chart** (`.png` + `.md`)

   * Visual asset + textual mapping guide for classification consistency.

3. **Alarm Features Checklist** (`.md`)

   * List of red flags; labeled as *knowledge content only*.

4. **Stable JSON (Patient Profile)** (`.json`)

   * Authoritative patient state; manually updated; read-only.
   * Follows schema defined in T810A2.

5. **Dynamic JSON Skeleton (Entry Template)** (`.json`)

   * Defines per-entry structure for logs (stool, meal, sleep, etc.).
   * Read-only exemplar for Block 5; generation logic deferred.

6. **Daily Report Template** (`.md`)

   * Time-ordered structure for daily summaries; doubles as memory reference.

> **Authority Rule:** When Project Knowledge conflicts with Model or Memory, **Project Knowledge wins**; when Memory conflicts with Stable JSON, **Stable JSON wins**.

### B. Recommended Documents

7. **Operational Constants Cheat-Sheet** (`.md`)

   * Defines timezone, timestamp format (`DD-MM-YYYYTHH:MM:00+02:00`).

8. **Controlled Vocabulary Stubs** (`.yaml`)

   * Illustrative (non-authoritative) sample terms; refer to T810A2 for real sets.

9. **Knowledge Router Card** (`.md`)

   * Crosswalk: *When to consult which KB file* (e.g., stool → Bristol Chart).

10. **GI KB Source Standard Mirror** (`.md`)

* Condensed copy of GDR-005 clinical canon list with update policy.

### C. File Organization Example

```
kb/
  clinical/
    rome_iv_digest.md
    acg_aga_digests.md
    alarm_features.md
    bristol_stool_chart.md
    bristol_stool_chart.png
  patient/
    profile_stable.json
  templates/
    dynamic_entry_skeleton.json
    report_daily_template.md
  ops/
    operational_constants.md
    vocab_stubs.yaml
  governance/
    gi_kb_source_standard.md
```

**Metadata practice:** Include *Version & Date* line in body (not YAML header).
**All files read-only**; validation logic resides in Block 5.

---
