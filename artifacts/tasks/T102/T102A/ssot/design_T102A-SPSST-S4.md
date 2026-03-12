---
iID: 'T102'
epic_id: 'T102A'
feature_id: 'T102A-SPSST'
story_id: 'T102A-SPSST-S4'
story_status: 'approved'        # draft|review|approved|rework|deprecated
stability: 'frozen'             # soft_lock|frozen
ready_to_plan: true
scg: 'B'                        # A=Authoring skeleton, B=Governance & Ops
---

# design_T102A-SPSST-S4 — Initiative Considerations 

> **Status:** Living design log (non‑final). Finalized decisions are recorded in the **Concept** artifact.
> **Scope:** Story `T102A‑SPSST‑S4` only (SPS §III‑B — Initiative Considerations).
> **Dates covered:** 20/08/2025 → 25/08/2025.

---

## III. CORE CONTENT

### A. Context & Intent

S4 defines the structure and authoring rules for SPS **§III‑B — Initiative Considerations**. This design log captures options explored, chosen architecture, and dated decision entries. It exists to:

* keep a **clear separation** between proposals and decisions;
* record **why** we chose the current structure; and
* provide **authoring guardrails** specific to S4 before the decision is frozen in the Concept artifact.

**Reference**
- **Request:** `request_T102A-SPSST_T102_v1.0.0.md` (S4 FRs, NFRs, Integration Notes)
- **Concept:** `Concept_T102A-SPSST` → Section **III.B.4** (S4 Story)
- **SPS Implementation:** `sps_T102-CONSULTANT.md` 

---

### B. Architecture Proposals 

#### 1. P1 — Minimal, merged “Global Considerations” (superseded)

A compact 3‑section model aimed at simplicity and minimal cognitive load.

```markdown
## C. Global Considerations

<!-- This section is for rules, assumptions, or notes that apply to ALL features above. -->
#### 1. Global Constraints & Assumptions

#### 2. Global Quality Goals (Optional)

*   *[If any, list them here as simple bullet points.]*

#### 3. Global Notes & Parking Lot
<details>
<summary>Click to expand contextual notes & out-of-scope items</summary>
<details>
```

**Pros:** smallest surface area; easier for newcomers.
**Cons:** merges **assumptions** with **constraints** (blurs governance boundaries); no explicit bucket for **dependencies & interfaces** or **implementation guidance**; weaker traceability to Request/Concept patterns.

---

#### 2. P2 — Standards-aligned, explicit six-bucket model (**current architecture**)

Six subsections mirror common project‑governance structures and reduce categorization ambiguity.

1. **Project Assumptions** — believed‑true, not yet verified.
2. **Project Constraints** — non‑negotiable limits (policy, tech, scope/time/cost).
3. **Success Criteria & Quality Goals (initiative)** — measurable “what good looks like” at initiative level; not story ACs.
4. **Dependencies & Interfaces** — external actors/systems/contracts and role handoffs.
5. **Implementation Guidance** — house rules for how we author/operate.
6. **Notes & Parking Lot** — expandable, non‑normative context & out‑of‑scope items.

**Pros:** crisp boundaries; strong traceability downstream; supports validator automation.
**Cons:** slightly larger surface area; requires lightweight author guidance.

---

### C. Decision Log Entries (chronological)

#### 1. Entry 1 — 20/08/2025 — Interim structure observed in working drafts

**Research Phase:** Comprehensive analysis of industry standards (PRINCE2 PID 2025, ISO/IEC/IEEE 29148:2018, BABOK v3) revealing better organizational patterns and clear definitional frameworks.

| Section | Purpose | Content Type | Industry Standard | Definition |
|---------|---------|--------------|------------------|------------|
| **1. Project Assumptions** | Unverified beliefs | Bullets | BABOK v3, ISO 29148 | Factors believed true but not yet confirmed; carry risk if proven false |
| **2. Project Constraints** | Non-negotiable limits | Bullets | ISO 29148, PRINCE2 | Restrictions/limitations that must be respected and cannot be changed within scope |
| **3. Success Criteria & Quality Goals** | Measurable targets | Bullets | ISO 29148 | Must be verifiable, singular, and complete with clear success/failure criteria |
| **4. Dependencies & Interfaces** | External factors | Bullets | PRINCE2 PID | Technical contracts, role definitions, integration points with other systems |
| **5. Implementation Guidance** | Technical notes | Bullets | Best Practice | Practical guidance for execution teams |

**What we had in practice:** **5 explicit subsections** used consistently, with **Notes & Parking Lot** treated as *optional*:

* Project Assumptions
* Project Constraints
* Success Criteria & Quality Goals 
* Dependencies & Interfaces
* Implementation Guidance
* *(optional)* Notes & Parking Lot

**Rationale at the time:**

* Introduced explicit **Dependencies & Interfaces** and **Implementation Guidance** to separate external contracts from internal authoring rules.
* Kept **Notes** optional to reduce required authoring.

**Integration Notes**
**Initiative Considerations** → feeds **Request Assumptions & Dependencies** 
- **Success Criteria & Quality Goals** → seed **Request NFRs** section
- **Dependencies & Interfaces** → inform **Request Interfaces & Data** section
- **Implementation Guidance** → provide **Concept implementation context**

**Observed issues:**

* Ambiguity on whether **Notes & Parking Lot** is required.
* Minor mis‑classification and ID prefix drift (e.g., interface items labeled as `DEP` but placed under **Implementation Guidance**).
* Occasional confusion between **initiative “Success Criteria”** vs **story‑level Acceptance Criteria**.

**Disposition:** Kept while we continued evaluation (P2 likely).

---

#### 2. Entry 2 — 25/08/2025 — Finalize S4 architecture to six mandatory subsections

**Decision:** 
- Adopt **P2** with **six mandatory subsections**, making **Notes & Parking Lot** mandatory as the sixth bucket. 
- Terminology simplifies to **“Quality Goals”** to align with verification language while clarifying it is **not** story‑level ACs.

**Why we chose this:**

* Clearer boundaries reduce rework during planning and review gates.
* Dedicated **Notes & Parking Lot** prevents leakage of tentative content into normative buckets and enables structured grooming.
* Consistency with governance patterns (assumptions vs constraints; dependencies/interfaces vs implementation guidance).

**Initiative Considerations Quick Reference:**

| **What am I writing about?** | **Which section?** | **ID Format** | **Language to use** |
|---|---|---|---|
| Something we believe is true but haven't confirmed yet | **Project Assumptions** | `T102-ASSUM-##` | "We assume..." or "It's likely that..." |
| Something that absolutely must be true - no flexibility | **Project Constraints** | `T102-CON-##` | "Must..." or "Cannot..." or "Required..." |
| How we'll measure success at the project level | **Quality Goals** | `T102-QG-##` | "≥90% of..." or "Within X days..." (measurable) |
| People, systems, or contracts outside our control | **Dependencies & Interfaces** | `T102-DEP-##` | "Client will..." or "System X provides..." |
| Rules for how we'll work or create things | **Implementation Guidance** | `T102-IG-##` | "We will..." or "Documents should..." |
| Ideas, context, questions, or things we won't do | **Notes & Parking Lot** | `T102-NOTE-##` | "Consider..." or "Out of scope..." or "Question:" |

**Quick decision test:**
- **Within our control + mandatory** = Constraint
- **Outside our control + needed** = Dependency  
- **Believed but unproven** = Assumption
- **How we measure success** = Quality Goal
- **How we work** = Implementation Guidance
- **Everything else** = Notes & Parking Lot

**Writing tips:**
- Keep each item to ≤25 words
- Be specific and testable where possible
- Add brief rationale in parentheses if helpful

**Authoring micro‑guide (drop‑in block)** — approved for S4 use:

```markdown
<!-- HOW TO ADD AN ITEM TO III-B (S4)
1) Pick the right subsection using the boundary rules:
   - Assumption = believed-true, not confirmed.
   - Constraint = non-negotiable limit.
   - Quality Goals = measurable “what good looks like” at initiative level.
   - Dependency & Interface = external actor/system/contract or handoff.
   - Implementation Guidance = our internal “how to author/operate” rules.
   - Notes & Parking Lot = contextual, exploratory, out-of-scope; do not delete.
2) Create an ID with the right prefix and 2-digit counter:
   - T102-ASSUM-## | T102-CON-## | T102-QG-## | T102-DEP-## | T102-IG-## | T102-NOTE-##
3) Write one line (≤ 25 words). Be atomic and testable where applicable.
4) Optionally add a short rationale in parentheses.
5) Constraint vs Dependency quick test:
   - If within our control and mandatory → Constraint.
   - If external commitment or contract → Dependency.
Examples:
- T102-CON-03 Review SLA ≤2 business days. (Keeps gates flowing)
- T102-ASSUM-05 Client will use Markdown/YAML editors.
- T102-QG-04 ≥90% sections pass validator on first pass.
- T102-DEP-03 Planner consumes Concept handoff schema v1.
- T102-IG-09 Approvals listed in document body, not YAML.
- T102-NOTE-02 Consider consolidating validation logs at epic level.
-->
```

**Disposition:** This entry supersedes Entry #1 where they conflict. Six buckets are **mandatory** for S4.

---

#### 3. Entry 3 — 07/09/2025 — Make “Initiative GDR Index” mandatory in SPS §III-B

**Decision:** Add a mandatory subsection **“7. Initiative GDR Index”** to SPS **§III-B — Initiative Considerations**.

**Why:** We need a single, auditable place for initiative-wide **governance decisions** (GDRs) that define how artifacts and gates work across all epics/features, without mixing technical ADRs into SPS. This aligns with PID governance practice and keeps technical decisions in Concept/Design.

**Scope & Rules**
- **Location:** SPS §III-B (after existing six buckets).  
- **Label:** “#### 7. Initiative GDR Index (governance decisions; links-only)”.  
- **GDR ID prefix:** `T102-GDR-####` (initiative). Epic-level deltas use `T102X-GDR-####` inside SPS §III-C (that Epic dossier).  
- **Table columns (required):**  
  `GDR ID | Title | Status | Scope | Owner | Effective | Supersedes | Anchor`  
- **Anchor naming:** lower-kebab, e.g., `{#t102-gdr-0001-solution-1}`.  
  
- **Body format (per row):** GDR subheading with **Context → Decision → Consequences → References** (ADR-lite style), but strictly **governance content only**.  
- **Validation (planner/tooling):**  
  1) Subsection exists;  
  2) Table present with required columns;  
  3) Each GDR has an anchor and body;  
  4) Each row lists at least one **Related Consideration** ID;  
  5) `Owner`, `Effective`, and `Status` are populated.

**Integration Notes**
- **Request** artifacts: do **not** embed ADR bodies; **A0** links to ADR(s).  
- **Concept**: Feature-level ADR index + per-story Design Logs remain the authoritative home for **technical** decisions.  
- **Traceability:** SPS GDR → Request A0 constraints (if relevant) → Concept ADR(s) (technical) → Design Logs → Tests/Code.

**Consequences**
- (+) Clear separation: **SPS=GDR (governance)**, **Concept/Design=ADR (technical)**.  
- (+) Consistent anchors & IDs; easier audits.  
- (±) Requires link discipline and a small validator rule set.

**References**
- PRINCE2 PID governance products; ISO/IEC/IEEE 42010 (architecture descriptions); ADR practice notes.


### D. Decision Record (Frozen Summary)
<!-- - A single **canonical summary** distilled from the latest *accepted* ADR(s).  
- Purpose: client-friendly “final decision at a glance” without reading the chronology. -->
#### 1. Decision Record
* **Title:** S4 — SPS §III‑B six‑bucket governance structure (mandatory Notes & Parking Lot)
* **Context:** Interim drafts used five explicit subsections with optional Notes; classification ambiguity persisted for interfaces vs guidance and for initiative goals vs story ACs.
* **Decision:** Adopt the six‑bucket model with **all subsections mandatory**; embed author micro‑guide and per‑bucket *[Instructions]* blocks; enforce ID prefixes and presence via validator in planning.
* **Consequences:**

  * (+) Crisper governance boundaries; fewer cross‑bucket corrections.
  * (+) Cleaner downstream traceability to Request NFRs and interface sections.
  * (±) Slightly more authoring overhead mitigated by micro‑guide and examples.
* **Alternatives considered:**

  * P1 Minimal 3‑section model (simplicity, but blurred boundaries & weaker traceability).
  * 5‑bucket variant with optional Notes (reduced consistency; exploratory items leaked into normative buckets).
* **References:** Request S4 FR‑01..04; Design log entries `20/08/2025` and `25/08/2025` (P1/P2, micro‑guide).

#### 2. Final Proposed Solution

```markdown
### B. Initiative Considerations

<!-- HOW TO ADD AN ITEM TO III‑B (S4)
1) Pick the right subsection using the boundary rules:
   - Assumption = believed-true, not confirmed.
   - Constraint = non-negotiable limit.
   - Quality Goal/Success Signal = measurable “what good looks like” at initiative level (NOT story ACs).
   - Dependency & Interface = external actor/system/contract or role handoff.
   - Implementation Guidance = internal “how we author/operate” rules.
   - Notes & Parking Lot = context/questions/out-of-scope; mandatory and groomed.
   - Initiative GDR Index = 
2) Create an ID with the right prefix and 2-digit counter:
   - [IID]-ASSUM-## | [IID]-CON-## | [IID]-QG-## | [IID]-DEP-## | [IID]-IG-## | [IID]-NOTE-##
3) One line (≤ 25 words). Be atomic; add a brief rationale if useful.
4) Constraint vs Dependency quick test: if within our control and mandatory → Constraint; if external commitment/contract → Dependency.
5) Initiative GDR Index
   - Use table columns exactly as listed (automation relies on them).
   - ID pattern: T102-GDR-#### (initiative); 
   - Anchor: lower-kebab, e.g., {#t102-gdr-0002-title}.
   - Body structure: Context → Decision → Consequences → References (governance only; no technical ADR content).
Examples:
- T102-CON-03 Review SLA ≤2 business days. (Keeps gates flowing)
- T102-ASSUM-05 Client will use Markdown/YAML editors.
- T102-QG-04 ≥90% sections pass validator on first pass.
- T102-DEP-03 Planner consumes Concept handoff schema v1.
- T102-IG-09 Approvals listed in document body, not YAML.
- T102-NOTE-02 Consider consolidating validation logs at epic level.
-->

#### 1. Project Assumptions
<!-- Believed‑true, not yet verified (BABOK). -->
*[One line per item (≤25 words); prefix `[IID]-ASSUM-##`.]*

#### 2. Project Constraints
<!-- Non‑negotiable limits (policy/tech/time/cost); ISO 29148 verifiability. -->
*[List constraints; prefix `[IID]-CON-##`.]*

#### 3. Quality Goals 
<!-- Measurable “what good looks like” at initiative level; NOT story Acceptance Criteria. -->
*[List measurable goals; prefix `[IID]-QG-##`.]*

#### 4. Dependencies & Interfaces
<!-- External actors/systems/contracts; role handoffs; interface/migration dependencies. -->
*[List dependencies & interfaces; prefix `[IID]-DEP-##`.]*

#### 5. Implementation Guidance
<!-- Internal authoring/operation rules (templates, ID patterns, approvals in body). -->
*[List house rules; prefix `[IID]-IG-##`.]*

#### 6. Notes & Parking Lot
<!-- Contextual notes, questions, out‑of‑scope; mandatory container; define grooming cadence. -->
*[Capture context/backlog notes; prefix `[IID]-NOTE-##`.]*

#### 7. Initiative GDR Index 
<!-- Provide a single, auditable index of initiative-level governance decisions that guide governance, artifacts, and gates across the initiative. -->
*[Assign IDs as [IID]-GDR-###; set Client as default owner; keep governance-only decisions (no technical ADRs); use lower-kebab anchors pointing to decision bodies]*

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|--------|-------|--------|-------|-----------|------------|--------|
| [IID]-GDR-001 | <Concise governance decision title> | `Proposed/Accepted/Deprecated` | Client | YYYY-MM-DD | <IDs or —> | #[iID-gdr-001-kebab-title] | 

* **`[IID]-GDR-001` — <Concise Title> — {#[iid-gdr-001-kebab-title]}**
  - **Context**: Brief rationale and background for the governance decision.
  - **Decision**: Single-sentence decision statement (what is adopted/mandated).
  - **Consequences**: Key impacts/tradeoffs; approvals or policy implications.
  - **References**: Related considerations & rules with links/IDs reference (e.g., `T102-CON-01 (Format Requirements)`) and external or internal scopes and standards if relevant (e.g: `T101`, `T102A-SPSST`, `T102D`)

```

### E. Integration, Dependency & Tracibility
#### 1. Integration Notes
* `T102A-SPSST-INT-05` — Terminology Clarification: *Global* = Program/Portfolio; *Initiative* = SPS scope.
* `T102A-SPSST-INT-06` — Standards Alignment: PRINCE2 PID, ISO 29148, BABOK v3.
* `T102A-SPSST-INT-07` — Documentation Pattern: explanatory markdown comments + *[Instructions]* under each subsection.

#### 2. Story-local Dependency
* `design_T102A-SPSST-S4.md` — proposals P1/P2, dated entries `20/08/2025` and `25/08/2025`.
* Standards references: PRINCE2 PID, ISO/IEC/IEEE 29148:2018, BABOK v3 (consolidated in project bibliography).
* S4 validator spec (presence/ID rules) — to be implemented by Planner/Tooling.

#### 3. Tracibility Matrix
<!-- **Req → ADR → Design artifacts → Tests/Code** mapping (you already have “Integration & Traceability”; keep and extend). -->
| ID                   | Title / Description                                  | Status | Evidence / Location                                | Notes |
| :------------------- | :--------------------------------------------------- | :----- | :------------------------------------------------- | :---- |
| `T102A-SPSST-S4-FR-01` | Rename to “Initiative Considerations”                | Met    | Final Proposed Solution → `section_title`          | —     |
| `T102A-SPSST-S4-FR-02` | Provide **six** industry-standard subsections        | Met    | Final Proposed Solution → `subsections` + skeleton | —     |
| `T102A-SPSST-S4-FR-03` | Markdown comments + clear definitions per subsection | Met    | Skeleton comments under each subsection            | —     |
| `T102A-SPSST-S4-FR-04` | *[Instructions]* under each subsection              | Met    | Skeleton includes explicit *[Instructions]* lines | —     |


### F. Ripple Test Notes
* Presence: all six subsection headings render; validator flags if any missing.
* ID hygiene: sample insertions use correct prefixes; cross‑bucket IDs are rejected by doc‑lint.
* Cognitive load: new authors can classify 10 sample items with ≥90% agreement.
* Separation of concerns: Quality Goals are not used as story ACs in downstream Requests.

### G. Open Questions & Risks 
#### 1. Risks Log
| ID | Description | Owner | Status | Target Date | Resolution Link |
|---|---|---|---|---|---|

#### 2. Questions Log
| Entry | QID | Question | Proposed Answer (if any) | Status | Owner | Target Date | Res. Link |
|:---:|---|---|---|---|---|---|---|

1. **SLA placement:** If the “≤2 business days” review SLA is policy (non‑negotiable), it belongs under **Constraints**; if it’s an external commitment, treat it as **Dependency**. Resolution owner?
2. **ID hygiene:** Some legacy items may have `DEP` prefixes but belong in **Implementation Guidance** (or vice versa). Create a small re‑tagging task list to avoid drift.
3. **Quality Goals vs Story ACs:** Ensure authoring guidance and validator messages prevent conflating initiative‑level quality targets with story‑level Acceptance Criteria.
4. **Validator coverage:** Do we require a doc‑lint to enforce presence of all **six** subsections and correct ID prefixes?
5. **Interface boundary:** Confirm whether role contracts (Consultant/Planner/Client) are modeled as **Interfaces** (preferred) rather than **Guidance**.
6. **Notes governance:** Since **Notes & Parking Lot** is mandatory, define grooming cadence to prevent unbounded growth.

---

### H. Next Steps for QA

* Add unit checks to the template validator: (a) six subsections present; (b) no cross‑bucket IDs; (c) each item ≤ 25 words; (d) mandatory comments present.
* Run a one‑page classification exercise on existing items and capture any re‑tag needs as a checklist under Notes (`T102-NOTE-##`).
