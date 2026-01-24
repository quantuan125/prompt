---
artifact_type: 'CONCEPT'
initiative_id: 'T810'
initiative_code: 'GASTRO'
version: '1.0.0'
date: '2025-12-15'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

## III. CORE CONTENT

### A. Identity & Operating Rules
<!-- 
- Canonical header + links to governing GDRs/ADRs (inheritance table: “link-don’t-duplicate”).  <!-- T102-GDR-002/003/004/005 
- Scope & boundaries (what lives in SPS vs Request vs Design); change log.
--> 

### B.  Decision System (ADR Compendium)

#### 1. Initiative Architectural Decisions

| ADR ID | Title | Status | Effective | Supersedes | Anchor |
|--------|-------|--------|-----------|------------|--------|

#### 2. Epic Architectural Decisions

##### i. `T810A` Epic: `SYSTEM` - Gastroentologist Agent System

| ADR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| `T810A-ADR-001` | Trust-and-Verify Confidence Policy | Accepted | Client | 2025-10-27 | — | #t810a-adr-001-confidence-policy |
| `T810A-ADR-002` | Foundational Vocabulary Authority | Proposed | Client | TBD | — | #t810a-adr-002-vocabulary-authority |
| `T810A-ADR-003` | Dual-Purpose Reporting Policy | Accepted | Client | 2025-10-27 | — | #t810a-adr-003-dual-purpose-reporting |
| `T810A-ADR-004` | GI Knowledge Sources Catalog | Accepted | Client | 2025-10-27 | — | #t810a-adr-004-gi-sources-catalog |
| `T810A-ADR-005` | Tracking Payload Envelope | Accepted | Client | 2025-12-15 | — | #t810a-adr-005-tracking-payload-envelope |
| `T810A1-ADR-001` | 9-Block Architecture Assignment | Proposed | Client | 2025-12-09 | — | #t810a1-adr-001-9-block-architecture-assignment |

* **T810A-ADR-001 (Trust-and-Verify Confidence Policy) — {#t810a-adr-001-confidence-policy}** 

  **Context:** Per `T810A-GDR-001`, features must communicate confidence qualitatively while maintaining mandatory numeric thresholds for backend/JSON tracking. Research (`T810A-RES-001` Deliverable B; `T810A-RES-002`) revealed numeric confidence in JSON without qualitative user-facing communication, creating machine/human disconnect. This ADR extracts implementation details from Epic governance for feature-specific adaptation.

  **Decision:** Establish Trust-and-Verify Confidence Policy defining qualitative tiers, mandatory internal numeric ranges for backend/JSON (0-1 scale), modality-specific examples, and explicit prohibition of numeric values in user-facing prose.

  **Specification:**

  **T810A-ADR-001-FR-001 (Qualitative Confidence Tiers)**
  - **High Confidence**: "fairly confident," "this appears to be," "likely" — State classification with brief rationale; validation optional
  - **Moderate Confidence**: "moderate confidence," "appears to be, though [ambiguity]," "suggest" — State with detailed rationale + encourage validation
  - **Low Confidence**: "uncertain," "difficult to classify definitively," "unclear" — State uncertainty explicitly + mandatory validation request

  **T810A-ADR-001-FR-002 (Mandatory Internal Numeric Ranges)**
  - **MANDATORY for backend/JSON tracking** (tracking payload generation, pattern analysis, validation logic):
    - High: >0.9 (0.9-1.0 range)
    - Moderate: 0.7-0.9
    - Low: <0.7 (0.0-0.7 range)
  - **PROHIBITION**: Numeric confidence values SHALL NOT appear in user-facing communication
  - **Use Case**: Backend generation tasks (tracking payload `"confidence": 0.85`), A3 pattern analysis, validation intensity logic
  - Features SHALL implement numeric→qualitative mapping per FR-001 for all user-facing text

  **T810A-ADR-001-FR-003 (Image Classification Examples)**
  - **Bristol Stool Chart** (Types 0-7):
    - **Type 0**: "nothing" (no poop produced despite attempted BM)
      - Tracking: Always confidence=1.0 in tracking payload (`"stool_type": 0, "confidence": 1.0`)
      - User-facing: Intelligent communication required: "I understand you attempted a bowel movement but didn't produce anything. That's important tracking information."
    - **Type 1-7** (standard Bristol scale):
      - High (>0.9): Clear Type 4 → "This appears to be Bristol Type 4 based on smooth texture and shape"
      - Moderate (0.7-0.9): Type 5-6 ambiguity → "I see this as Bristol Type 5, though lighting makes it somewhat ambiguous. Does that match?"
      - Low (<0.7): Poor quality → "Image quality makes definitive classification difficult. What did you observe?"
  - **Meal Analysis**:
    - High: Clear items → "This appears to be a vegetable stir-fry with rice"
    - Moderate: Partial visibility → "This looks like pasta, though some ingredients are partially visible. Can you confirm?"

  **T810A-ADR-001-FR-004 (Cross-Modality Applicability)**
  - **Text Analysis**: Apply tiers to symptom severity assessments, pattern identification
  - **Structured Data**: Apply to controlled vocabulary matching, clinical criteria alignment
  - **Pattern Recognition**: Apply to longitudinal trend analysis, correlation identification

  **T810A-ADR-001-FR-005 (Validation Intensity Mapping)**
  - High (>0.9) → Validation optional ("Does that sound right?")
  - Moderate (0.7-0.9) → Validation encouraged ("Can you confirm?")
  - Low (<0.7) → Validation mandatory ("What did you observe?")
  - Validation SHALL NOT block conversational flow per `T810A-GDR-001`

  **Consequences:**
  - (+) Standardized confidence behavior across features with mandatory backend numeric for A3 pattern analysis
  - (+) Bristol Type 0 handled correctly (confidence=1.0 tracking, intelligent user communication)
  - (±) Features must maintain numeric→qualitative mapping discipline
  - (±) Numeric ranges mandatory for backend; features adapt user-facing phrasing
  - (-) No programmatic validation per `T810A-CON-004`

  **Alternatives Considered:**
  - **Option A**: Optional numeric guidance — Rejected: Backend/JSON tracking requires mandatory numeric for A3 aggregation and validation logic
  - **Option B**: Numeric in user-facing with disclaimer — Rejected: False precision perception
  - **Option C**: Separate tiers per modality — Rejected: Unnecessary complexity

  **References:**
  `T810A-GDR-001 (Trust-and-Verify Workflow Standard)`,
  `T810A-QG-007 (Confidence Communication)`,
  `T810A-IG-003 (Explicit Classification)`,
  `T810A-CON-004 (ChatGPT Architectural Constraints)`

  **Provenance:**
  `analysis_T810A-SYSTEM_gdr-scope-assessment.md`,
  `request_T810A1-PROMPT.md`



* **T810A-ADR-002 (Foundational Vocabulary Authority) — {#t810a-adr-002-vocabulary-authority}**

  **Context:** Per `T810A-GDR-002`, a schema split architecture requires controlled vocabularies for categorical fields across the patient profile schema (stable patient context) and tracking entry schemas (dynamic tracking entries). Without authoritative cross-feature vocabulary governance, features risk inconsistent terminology, aggregation incompatibility per `T810A-DEP-002`, and Cara Care dual-processing misalignment per `T810A-CON-002`. Research (`T810A-RES-001` Deliverable E) confirms Cara Care application as primary exemplar for GI tracking vocabulary patterns.

  **Decision:** Establish Foundational Vocabulary Authority defining authoritative controlled vocabularies for Epic features requiring patient tracking JSON structures. Vocabulary catalog governs meal/stool metadata, numeric scale semantics, and cross-feature consistency. Cara Care application serves as primary exemplar per `T810A-GDR-004` vocabulary authority model. Adopt `T810A-ADR-002`, defining foundational JSON requirements table as Epic governance.

  **Specification:**

   1) **T810A-ADR-002-FR-001 (Foundational JSON Requirements Table)** — Enhanced per `T810A2-RES-001` Deliverable A.5 gap analysis and client directive (Activity 1.9 QA)

      | Entry Type | Classification | Key | Data Type | Range/Values | Descriptions Required |
      |:-----------|:--------------|:----|:----------|:-------------|:----------------------|
      | **meal** | **REQUIRED** | `ingredients` | array | list of ingredient strings | Meal components |
      | **meal** | **REQUIRED** | `metadata` | array | ["chili", "oily", "sweet", "light", "salty", "fibrous"] | Descriptive tags (explicitly enumerate ALL per `T810A2-RES-001` R1.2) |
      | **stool** | **REQUIRED** | `type` | integer | 0-7 | Bristol scale descriptions for each (Type 0 = "nothing" per `T810A2-RES-001` A.1) |
      | **stool** | **REQUIRED** | `metadata` | array | ["urgent", "full_evacuation", "partial_evacuation", "mucus", **"blood"**] | Event descriptors (**"blood" added** per `T810A2-RES-001` A.5 clinical validity) |
      | **stool** | **REQUIRED** | `confidence` | float | 0.0-1.0 | LLM image analysis confidence |
      | **digestion** | **REQUIRED** | `tummy_pain` | integer | 1-5 | 1=no pain → 5=extreme; predefined descriptions per `T810A2-RES-001` R1.3 |
      | **digestion** | **REQUIRED** | `bloating` | integer | 1-5 | 1=no bloating → 5=extreme; predefined descriptions per `T810A2-RES-001` R1.3 |
      | **mental** | **REQUIRED** | `mood` | integer | -2 to 2 | -2=awful, 0=neutral (so-so), 2=very good (happy) per `T810A2-RES-001` R1.3 |
      | **mental** | **REQUIRED** | `stress` | integer | 1-5 | 1=no stress → 5=extreme stress per `T810A2-RES-001` R1.3 |
      | **sleep** | **OPTIONAL** | `duration` | string/enum | ["<4h", "4-6h", "6-8h", ">8h"] OR integer (hours) | Sleep duration ranges |
      | **sleep** | **OPTIONAL** | `notes` | string (optional) | free text | Sleep quality notes |
      | **medication** | **OPTIONAL** | `medications` | array of strings | Simple: ["Imodium", "Probiotics"] | Medication entries (structured objects deferred to post-MVP per `T810A2-RES-001` R1.2) |
      | **hydration** | **OPTIONAL** | `water_intake` | float/enum | cups OR liters OR range category | Water consumption |

      **MVP Scope Boundary**:
      - **REQUIRED Entry Types** (MVP Core): meal, stool, digestion, mental 
      - **OPTIONAL Entry Types** (MVP Extended): sleep, medication, hydration
      - **DEFERRED Entry Types** (Post-MVP): exercise, skin, period, patient_state, others per `T810A2-RES-001` A.1

      **Enhancement Rationale**:
      - **"blood" in stool.metadata**: Clinically critical for IBD/colitis differentiation (alarm symptom per `T810A2-RES-001` A.5)
      - **"salty", "fibrous" in meal.metadata**: Common dietary triggers per `T810A2-RES-001` R1.2
      - **Semantic anchor labels**: All scales populated per `T810A2-RES-001` R1.3 (Bristol 0-7, pain/bloating/mood/stress)
      - **OPTIONAL entry types**: Enable holistic GI tracking (sleep quality, medication effects, hydration patterns correlate with symptoms) while controlling MVP scope


   2) **T810A-ADR-002-FR-002 (Critical Requirements)**
      - Value set definitions: What each numeric level means  
      - Descriptive labels for each scale point  
      - Guidance for LLM_Gastro on scale mapping from natural language input

   3) **T810A-ADR-002-FR-003 (Vocabulary Governance)**
       - **Vocabulary Versioning**: Track vocabulary catalog version (e.g., "v1.0.0")
       - **Controlled Expansion**: New vocabulary values approved via Epic consultant coordination
       - **Cross-Feature Notification**: Features notified of vocabulary additions/deprecations
       - **Backward Compatibility**: Vocabulary additions SHALL NOT break existing JSON structures

   4) **T810A-ADR-002-FR-004 (Cross-Feature Consistency)**
      - **T810A1 (PROMPT)**: System prompt references vocabulary catalog for tracking payload generation
      - **T810A2 (PATIENT)**: Schema specifications implement vocabulary as authoritative source
      - **T810A3 (REPORT)**: Aggregation logic depends on vocabulary consistency for pattern analysis
      - **Enforcement**: Features SHALL NOT deviate from catalog without Epic ADR amendment

   5) **T810A-ADR-002-FR-005 (Cara Care Alignment)**
      - **Primary Exemplar**: Cara Care application UX patterns and terminology
      - **Supplementary Research**: Clinical vocabularies from `T810A-ADR-004` (ROME IV, ACG/AGA guidelines) for medical terminology
      - **Patient Familiarity**: Vocabulary assumes patient familiarity with Cara Care-aligned tracking terms per `T810A2-ASSUM-005`
      - **Vocabulary Extraction**: Systematic extraction via research commission (`T810A2-RES-001` Part 1: Cara Care Vocabulary Extraction)

   6) **T810A-ADR-002-FR-006 (Maintenance Governance)**
      - **Owner**: Client (vocabulary adoption/expansion authority)
      - **Updates**: LLM_Consultant proposes, Client approves
      - **Update Triggers**: Cara Care application updates, clinical guideline changes, patient feedback
      - **Documentation**: ADR body maintains vocabulary catalog with version history
      - **Traceability**: Link to research IDs (`T810A-RES-001`, `T810A2-RES-001`), Cara Care resources, clinical standards


  **Consequences:**
  - (+) Centralized vocabulary authority; cross-feature aggregation compatibility per `T810A-DEP-002`; Cara Care dual-processing alignment per `T810A-CON-002`
  - (+) Systematic vocabulary governance prevents drift; Epic-level updates avoid feature-level inconsistencies
  - (±) Cara Care exemplar assumes patient UX familiarity; vocabulary expansion requires Epic coordination overhead
  - (±) Research commission required for exhaustive vocabulary extraction (`T810A2-RES-001` Part 1)
  - (-) English-only MVP scope per `T810A2-ASSUM-006`; multilingual vocabularies deferred

  **Alternatives Considered:**
  - **Option A**: Feature-distributed vocabularies — Rejected: Cross-feature inconsistency; aggregation incompatibility; maintenance burden
  - **Option B**: Embed in GDR-002 — Rejected: GDR updates for every vocabulary addition create governance overhead
  - **Option C**: External vocabulary file — Rejected: Lacks traceability; governance unclear
  - **Option D**: No controlled vocabularies — Rejected: Violates `T810A2-NFR-003` (Vocabulary Completeness); pattern analysis unreliable

  **References:**
  `T810A-GDR-002 (Schema Split Architecture)`,
  `T810A-GDR-004 (GI Knowledge Base Sources)`,
  `T810A-ADR-001 (Trust-and-Verify Confidence Policy)`,
  `T810A-ADR-003 (Dual-Purpose Reporting Policy)`,
  `T810A-ADR-004 (GI Knowledge Sources Catalog)`,
  `T810A-DEP-002 (Long-term Analysis)`,
  `T810A-CON-002 (Platform Compatibility)`,
  `T810A-QG-006 (Patient Usability)`,
  `T810A-RES-001 (System Architecture & Clinical Validation)`,

  **Provenance:**
  `handoff_brief_T810A2-SCHEMA.md`,
  `plan_T810A2-SCHEMA_phase0-4.md` 

* **T810A-ADR-003 (Dual-Purpose Reporting Policy) — {#t810a-adr-003-dual-purpose-reporting}** 

  **Context:** Per `T810A-GDR-003`, features must produce unified reports serving both clinician handoff and LLM memory. Research (`T810A-RES-001` Deliverable F) confirms chronological timeline in first-person patient perspective as optimal for dual-purpose use. This ADR extracts format specifics, voice mandates, length guidance, triggers, and validation from Epic governance for feature adaptation.

  **Decision:** Establish Dual-Purpose Reporting Policy defining voice, structure, triggers, validation, and export patterns for session-end clinical reporting.

  **Specification:**

  **T810A-ADR-003-FR-001 (Narrative Voice Mandate)**
  - **First-Person Patient Perspective**: "I experienced..." (NOT "Patient experienced..." or "You experienced...")
  - **Rationale**: Patient narrative ownership; natural for patient-authored documentation
  - **Example**: "I had breakfast at 8:30 AM with scrambled eggs and toast. Mid-morning I experienced mild bloating..."

  **T810A-ADR-003-FR-002 (Length Targets)**
  - **Target Range**: 100-200 tokens per daily report
  - **Guidance**: Efficiency target for token-constrained LLM memory (not strict limit)
  - Features MAY exceed 200 tokens if clinical nuance requires; SHALL NOT sacrifice critical detail

  **T810A-ADR-003-FR-003 (Content Pattern)**
  - **Template**: Time → Event → Symptom/Meal/Stool → Analysis Summary
  - **Example**: "8:30 AM — Breakfast: scrambled eggs, toast, coffee | 10:00 AM — Mild bloating (severity 3/10) | 12:00 PM — BM (Bristol Type 4, no urgency) | Analysis: Post-breakfast bloating suggests possible egg sensitivity; normal stool consistency indicates no acute GI distress"
  - **Chronological Ordering**: Events in time sequence

  **T810A-ADR-003-FR-004 (Trigger Mechanisms)**
  - **Session-End Auto**: Agent offers report at natural conversation conclusion
  - **Patient Request**: "/report", "can you summarize today?", "generate my daily report"
  - **Mid-Session**: Agent MAY generate interim reports if patient requests

  **T810A-ADR-003-FR-005 (Validation Loop)**
  - **Draft Presentation**: Conversational tone per `T810A-QG-002`
  - **Patient Review**: Reviews for accuracy/completeness
  - **Correction Protocol**: Patient corrects → Agent adjusts → Patient confirms
  - **Phrasing**: "Does this summary capture your day accurately?" (NOT blocking)
  - **Authority**: Patient has final authority

  **T810A-ADR-003-FR-006 (JSON Export Schema)**
  - **Dual Output**: (1) Markdown narrative (clinician-shareable); (2) Structured JSON (exported alongside the tracking log per `T810A-IG-004`)
  - **JSON Structure**: `{"session_date": "YYYY-MM-DD", "report_markdown": "<text>", "entries_count": N, "validation_status": "confirmed"}`

  **T810A-ADR-003-FR-007 (A1/A3 Coordination)**
  - **T810A1**: Generate session-end report
  - **T810A3**: Aggregate multi-session reports per `T810A-DEP-002`
  - **Handoff**: A1 exports markdown+JSON → A3 consumes per `T810A-IG-006`
  - **Stability**: Core structure remains stable for aggregation

  **Consequences:**
  - (+) Standardized format across features; dual-purpose utility eliminates proliferation
  - (±) First-person voice unconventional; length guidance requires summarization discipline
  - (±) A1/A3 coordination requires format stability
  - (-) Formal handoff features deferred to T810A3

  **Alternatives Considered:**
  - **Option A**: Third-person voice — Rejected: Disconnects patient authorship
  - **Option B**: Separate formats — Rejected: Proliferation; maintenance burden
  - **Option C**: Strict 200-token limit — Rejected: Clinical nuance may require exceeding target

  **References:**
  `T810A-GDR-003 (Dual-Purpose Clinical Reporting)`,
  `T810A-IG-006 (Session Context Injection & Handoff)`,
  `T810A-IG-004 (Tracking Payload Per-Turn Delta)`,
  `T810A-QG-002 (Persona & Tone)`,
  `T810A-DEP-002 (Long-term Analysis)`

  **Provenance:**
  `analysis_T810A-SYSTEM_gdr-scope-assessment.md`,
  `request_T810A1-PROMPT.md`

* **T810A-ADR-004 (GI Knowledge Sources Catalog) — {#t810a-adr-004-gi-sources-catalog}** 

  **Context:** Per `T810A-GDR-004`, features must ground clinical GI reasoning in authoritative sources. Research (`T810A-RES-001` Deliverable D) identifies ROME IV, Bristol Chart, ACG/AGA guidelines, and alarm features as essential for diagnostic reasoning and safety escalation. This ADR centralizes catalog, versioning, update cadence, and maintenance governance for ADR-level updates without GDR changes.

  **Decision:** Establish GI Knowledge Sources Catalog as centralized, versioned reference for all Epic features requiring clinical GI knowledge.

  **Specification:**

  **T810A-ADR-004-FR-001 (Diagnostic Frameworks)**
  - **ROME IV Criteria**: Functional GI disorder classification (IBS, functional dyspepsia/constipation); Version ROME IV (2016), monitored for ROME V
  - **Bristol Stool Chart**: Types 0-7 (Type 0="nothing" per ADR-001-FR-003; Types 1-2 constipation, 3-4 normal, 5-7 diarrhea); Application: multimodal analysis per `T810A-IG-003`, patient self-reporting

  **T810A-ADR-004-FR-002 (Clinical Practice Guidelines)**
  - **ACG**: IBS management, functional dyspepsia treatment, colorectal cancer screening
  - **AGA**: Clinical practice updates for functional GI disorders, diagnostic testing
  - **International**: WHO/ISO standards (metric units, 24-hour time), global dietary terminology

  **T810A-ADR-004-FR-003 (Safety Escalation)**
  - **Alarm Features**: Unexplained weight loss (>10 lbs), persistent vomiting (>24h), blood in stool, severe abdominal pain, nocturnal diarrhea, rectal bleeding, family history colorectal cancer/IBD
  - **Thresholds**: "Discuss with gastroenterologist urgently" triggers
  - **Stance**: Frame as "working theories for clinician discussion" per `T810A-CON-003`

  **T810A-ADR-004-FR-004 (Versioning)**
  - **Tracking**: Version/publication year (e.g., "ROME IV (2016)", "ACG IBS Guidelines (2021)")
  - **Effective Dates**: Track adoption into knowledge base
  - **Deprecation**: Note replacement source and migration date

  **T810A-ADR-004-FR-005 (Update Cadence)**
  - **Annual Review**: Catalog reviewed annually
  - **Triggered Updates**: Upon major guideline publication (ROME V, ACG/AGA revisions)
  - **Safety-Critical**: Immediate alarm features updates
  - **Notification**: Features notified of breaking changes

  **T810A-ADR-004-FR-006 (Deprecation Procedures)**
  1. Monitor professional society publications
  2. Evaluate A1/A2/A3 impact
  3. Document replacement strategy
  4. Changelog entry with effective date
  5. Brief subconsultants

  **T810A-ADR-004-FR-007 (Maintenance Governance)**
  - **Owner**: Client (source adoption/deprecation authority)
  - **Updates**: LLM_Consultant proposes, Client approves
  - **Approval Gates**: Clinical source changes require explicit Client approval
  - **Documentation**: ADR body version history
  - **Traceability**: Link to research IDs, guideline publications, clinical advisories

  **Consequences:**
  - (+) Centralized catalog; easier maintenance; versioning enables evolution tracking
  - (±) Annual review discipline required; US-centric guidelines; A1/A2/A3 coordination
  - (-) Comprehensive safety deferred per `T810A-CON-003`

  **Alternatives Considered:**
  - **Option A**: Distributed references — Rejected: Maintenance burden, version drift
  - **Option B**: Embed in GDR — Rejected: GDR updates for every guideline change
  - **Option C**: External file — Rejected: Lacks traceability

  **References:**
  `T810A-GDR-004 (GI Knowledge Base Sources)`,
  `T810A-QG-004 (Holistic Analysis)`,
  `T810A-IG-003 (Explicit Classification)`,
  `T810A-CON-002 (Platform Compatibility)`,
  `T810A-CON-003 (Clinical Compliance Deferral)`,
  `T810A-DEP-005 (Clinical Safety Framework)`

  **Provenance:**
  `analysis_T810A-SYSTEM_gdr-scope-assessment.md`,
  `request_T810A1-PROMPT.md`

* **T810A-ADR-005 (Tracking Payload Envelope) — {#t810a-adr-005-tracking-payload-envelope}**

  **Context:** Per `T810A-GDR-002`, the schema split architecture requires a consistent per-turn tracking payload contract across features. Analysis identified a mismatch: the legacy “exactly one entry per interaction” rule cannot represent multi-event turns (e.g., multiple stool images + concurrent symptoms) without data loss or schema drift.

  **Decision:** Adopt Pattern A (mixed chronological array) as the MVP per-turn tracking payload envelope: when tracking is required, `LLM_Gastro` outputs a single fenced `json` codeblock containing a **delta array** of **1+ entry objects** inferred from the user’s current message; prior entries are not re-stated.

  **Specification:**

  **T810A-ADR-005-FR-001 (Single Codeblock Output)**
  - When tracking is required, output MUST include exactly one fenced `json` codeblock containing the tracking payload.
  - The codeblock payload MUST be valid JSON (no trailing commas, comments, or markdown inside the JSON).

  **T810A-ADR-005-FR-002 (Envelope Pattern A)**
  - The tracking payload MUST be a JSON array of entry objects (Pattern A).
  - Each entry object MUST include `entry_type` as the first-class discriminator for downstream grouping/filtering.

  **T810A-ADR-005-FR-003 (Per-Turn Delta Only)**
  - The array MUST contain only entries implied by the current user input (delta-only).
  - The assistant MUST NOT regenerate, copy forward, or summarize prior entries inside the tracking codeblock (avoids cumulative drift and token bloat).

  **T810A-ADR-005-FR-004 (Multi-Event Turn Handling)**
  - A single user message MAY produce 1+ entries in the same array (e.g., 4 stool images + current bloating → 5 entries).
  - When multiple images correspond to distinct times/events, the assistant SHOULD emit one stool entry per image unless the user explicitly states they represent the same event.

  **T810A-ADR-005-FR-005 (Chronology Semantics)**
  - If timestamps are known, entries SHOULD be ordered chronologically by timestamp.
  - If timestamps are partially known/unknown, entries SHOULD be ordered by best-effort occurrence (or, failing that, by appearance order in the user’s message) and use `null` for unknown timestamps.

  **T810A-ADR-005-FR-006 (ID Policy)**
  - Entry-level `id` fields are OPTIONAL and SHOULD NOT be required for MVP tracking output.
  - When an identifier is needed downstream, prefer stable derivation from timestamp + array order during post-processing rather than requiring the LLM to generate IDs.

  **Consequences:**
  - (+) Multi-entry turns become representable without collapsing events into a lossy single object.
  - (+) Lowest-drift contract under “no validation” constraints: no index maintenance, no variable container semantics.
  - (±) Pattern B remains viable as a derived aggregation view for reporting/export workflows, but is not the per-turn delta contract.
  - (-) Consumers must filter/group by `entry_type` (trivial, but explicit) rather than relying on per-type top-level arrays.

  **Alternatives Considered:**
  - **Option 0 (Status Quo / Single-Entry Object)** — Rejected: cannot represent multi-event turns without data loss.
  - **Option B (Per-Type Arrays Container)** — Rejected for MVP per-turn contract: either variable top-level shape per turn or token-heavy empty arrays.
  - **Option C (Entries + Type Index)** — Rejected: index maintenance is brittle without programmatic validation.

  **References:**
  `T810A-GDR-002 (Schema Split Architecture)`,
  `T810A-IG-004 (Tracking Payload Per-Turn Delta)`,
  `T810A-ADR-002 (Foundational Vocabulary Authority)`,
  `T810A-CON-004 (ChatGPT Architectural Constraints)`

  **Provenance:**
  `analysis_T810A-SYSTEM_dynamic-json-envelope-decision.md`

#### 3. Feature Architectural Decisions

##### i. `T810A1` Epic: `PROMPT` - Gastroentologist System Prompt

| ADR ID | Title | Status | Effective | Supersedes | Anchor |
|--------|-------|--------|-----------|------------|--------|
| T810A1-ADR-001 | 9-Block Architecture Assignment | Proposed | Client | 2025-12-09 | — | t810a1-adr-001-9-block-architecture-assignment |

* **T810A1-ADR-001 (9-Block Architecture Assignment)** {#t810a1-adr-001-9-block-architecture-assignment}

  **Context:** T810A1-PROMPT requires development of a 9-block modular system prompt per `T810A1-NFR-003 (Prompt Maintainability)`. Each block corresponds to a specific Story (S01-S09) that specifies functional requirements for that block. Clear Story-to-Block assignment ensures modular development, traceability, and maintenance consistency per `T810A-QG-005 (Architecture Maintainability)`. Existing content in `gastro_system.md` v0.x provides baseline for Blocks 1-3. Without canonical block assignment, Phase 2 development risks scope drift and Story-Block misalignment.

  **Decision:** Adopt canonical 9-block architecture with explicit Story assignments and F-RID governance per block. Each block receives dedicated Story ID, development scope, and governing F-RID references as follows:

  **Block 1 — Project Context (Story: T810A1-S01)**
  - **Scope**: Diagnostic stance, privacy policy, operational constants (timezone, timestamp format)
  - **Development Status**: Baseline exists in `gastro_system.md` v0.x; review and align with Phase 1 F-RIDs
  - **Governing F-RIDs**: `T810A1-IF-001` (Input Interface), `T810A1-IF-002` (Output Interface), `T810A1-IG-006` (Session Initialization operational constants reference)
  - **Story S10 Integration**: S10 (Metadata Header) FRs merge into S01 as YAML frontmatter specification; no separate block

  **Block 2 — Role Identity & Competencies (Story: T810A1-S02)**
  - **Scope**: Role mandate, key competencies, communication style per protocol phase (Engage, Analyze, Probe, Coach, Summarize)
  - **Development Status**: Baseline exists in `gastro_system.md` v0.x; review for T810A1-IG-002/T810A1-IG-003 alignment
  - **Governing F-RIDs**: `T810A1-NFR-002` (Persona & Tone), `T810A1-IG-002` (OARS Dialogue collaborative framing), `T810A1-IG-003` (Epistemic Hedging confidence language), `T810A1-GDR-001` (protocol phase tones)

  **Block 3 — Toolbox Declaration (Story: T810A1-S03)**
  - **Scope**: Tool declarations (ChatGPT native tools, external APIs)
  - **Development Status**: Deferred per `T810A1-CON-003`; preserve placeholder
  - **Governing F-RIDs**: `T810A1-CON-003` (Tooling Deferral to post-MVP)

  **Block 4 — Knowledge Base (Story: T810A1-S04)**
  - **Scope**: Knowledge type taxonomy (Internal Model, Custom Instructions, Project Knowledge, Memory, Web Search), authority hierarchy, schema references
  - **Development Status**: Requires full development; no baseline
  - **Governing F-RIDs**: `T810A1-IF-005` (Session Context Injection), `T810A1-IG-006` (Session Initialization schema loading), `T810A1-IG-007` (Tracking Payload Generation Pattern), `T810A1-INT-006` (Schema Loading Integration with T810A2 artifacts)

  **Block 5 — Execution Protocol (Story: T810A1-S05)**
  - **Scope**: 5-phase protocol (Tracking → Analyze → Probe → Coach → Summarize), protocol triggering (input-type detection), phase execution steps, gate enforcement, session initialization sequence
  - **Development Status**: Requires full development; highest complexity and F-RID consumption
  - **Governing F-RIDs**: `T810A1-NFR-001` (Protocol Reliability), `T810A1-NFR-004` (Protocol Triggering), `T810A1-NFR-005` (Probe Enforcement), `T810A1-GDR-001` (Tracking-First Protocol), `T810A1-GDR-002` (Session Workflow Architecture), `T810A1-IG-001` (Phase Gating), `T810A1-IG-002` (OARS Dialogue), `T810A1-IG-003` (Epistemic Hedging), `T810A1-IG-004` (Protocol Triggering Logic), `T810A1-IG-005` (Anti-Pattern detection awareness), `T810A1-IG-006` (Session Initialization), `T810A1-IG-007` (Tracking Payload Generation Pattern), `T810A1-INT-001` (Probe Triggering Integration)

  **Block 6 — Behavioral Guardrails (Story: T810A1-S06)**
  - **Scope**: Anti-pattern prohibitions, constraint enforcement (T810A1-CON-001 to T810A1-CON-004), gate compliance checks, safety boundaries
  - **Development Status**: Requires full development; no baseline
  - **Governing F-RIDs**: `T810A1-CON-001` (Risk Acceptance), `T810A1-CON-002` (Open Knowledge Base), `T810A1-CON-003` (Tooling Deferral), `T810A1-CON-004` (Fixed Keys), `T810A1-IG-001` (Phase Gating enforcement rules), `T810A1-IG-005` (Anti-Pattern Prohibitions primary home)

  **Block 7 — Quality & Success Criteria (Story: T810A1-S07)**
  - **Scope**: Verification checkpoints aggregated from E-QGs and IG-derived quality criteria, session quality checklist, output quality standards
  - **Development Status**: Requires full development; no baseline
  - **Governing F-RIDs**: E-QG inherited (`T810A-QG-001` to `T810A-QG-008`), IG-derived checkpoints from `T810A1-IG-001` to `T810A1-IG-007`

  **Block 8 — Exemplars (Story: T810A1-S08)**
  - **Scope**: Positive and negative dialogue examples demonstrating OARS dialogue, epistemic hedging, anti-pattern violations, gate phrasing, JSON generation
  - **Development Status**: Requires full development; no baseline
  - **Governing F-RIDs**: `T810A1-IG-002` (OARS Dialogue demonstrations), `T810A1-IG-003` (Epistemic Hedging phrasing demonstrations), `T810A1-IG-005` (Anti-Pattern violation demonstrations)

  **Block 9 — I/O Specification (Story: T810A1-S09)**
  - **Scope**: Input interface (text + image parsing), output interface (Markdown primary), explicit classification confidence indicators, reporting trigger (/report command), tracking payload output format, session report dual-format
  - **Development Status**: Requires full development; no baseline
  - **Governing F-RIDs**: `T810A1-IF-001` to `T810A1-IF-006` (all interface specifications), `T810A1-IG-003` (confidence in output), `T810A1-IG-007` (JSON output format), `T810A1-INT-005` (Session Report dual-format), `T810A1-INT-007` (Controlled Vocabulary Integration)

  **IG Coverage Matrix** (per Client QA Requirement — every Story must have ≥1 governing IG):
  - S01: `T810A1-IG-006` | S02: `T810A1-IG-002`, `T810A1-IG-003` | S03: *None (deferred)* | S04: `T810A1-IG-006`, `T810A1-IG-007` | S05: `T810A1-IG-001` to `T810A1-IG-007` (all) | S06: `T810A1-IG-001`, `T810A1-IG-005` | S07: *Derived from all IGs* | S08: `T810A1-IG-002`, `T810A1-IG-003`, `T810A1-IG-005` | S09: `T810A1-IG-003`, `T810A1-IG-007`

  **Consequences:**
  - (+) Clear modular boundaries per `T810A1-NFR-003`; enables isolated Story-level refinement post-Phase 2
  - (+) Traceability: Each Story maps to exactly one Block; each Block maps to exactly one Story (1:1 correspondence)
  - (+) Maintenance: Block-level edits localized per `T810A-QG-005`; reduces merge conflicts in multi-developer scenarios
  - (+) IG coverage verified: Every Story (except deferred S03) governed by ≥1 IG, ensuring implementation guidance completeness
  - (+) Phase 2 scope clarity: Blocks 1-3 baseline exists; Blocks 4-9 require full development
  - (±) S10 (Metadata Header) merged into S01; reduces block count from 10 to 9, simplifies architecture but merges two Story scopes
  - (-) High interdependency between Block 5 (S05) and Blocks 4, 6, 8, 9: S05 references S04 schema authority, S06 enforces S05 gates, S08 demonstrates S05 patterns, S09 aligns with S05 outputs; requires careful cross-block coordination in Phase 2
  - (-) Block 5 highest complexity: Consumes all T810A1-IG-001 to T810A1-IG-007 patterns; risk of bloat if not carefully scoped

  **References:**
  `T810A1-NFR-003 (Prompt Maintainability)`,
  `T810A-QG-005 (Architecture Maintainability)`,
  `T810A1-GDR-001 (Tracking-First Clinical Protocol)`,
  `T810A1-GDR-002 (Session Workflow Architecture)`,
  `T810A1-CON-003 (Tooling Deferral)`,
  `T102-ADR-004 (Decision Records Index)`


### C. Readiness Snapshot (Lean, manual)
<!-- 
- **A. Roll-up Table** (Initiative/Epics/Features: State | Ready? | Top blockers | Next gate | Updated_at)
- **B. DoR Checklists (brief)** per tier (links to Request/Design for evidence)
- **C. Notes & Overrides** (Client approvals recorded with ID)
-->

### D. Handoff Snapshot (Authoritative)
<!-- 
- **A. Package Manifest** (immutable IDs, doc versions/SHAs)
- **B. Acceptance Signals** (Client sign-off, gate approvals)
- **C. Completeness Checklist** (ADR accepted; FRs approved; risks linked)
- **D. Links** (SPS/Request/Design anchors; no copy-paste)
-->

### E. Registers 
<!-- 
- Risks/Assumptions/Dependencies registers (pointer-based; no duplication)
-->
#### 1. Feature Register

#### 2. Design Register
| Epic ID | Feature ID | Story ID | Design Log | Status | Notes |
| :------ | :--------- | :------- | :--------- | :----- | :---- |



### F. Integration & Interfaces
<!-- 
- Planner consumption notes (schema, payload outline), cross-traceability rules.
-->


### G. Governance

<!-- 
- Local GDRs for Concept (e.g., T102C-GDR-003/005 once accepted) + change control.
-->
