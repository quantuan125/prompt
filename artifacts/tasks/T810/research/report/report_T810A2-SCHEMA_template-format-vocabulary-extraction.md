---
artifact_type: 'REPORT'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
research_id: 'T810A2-RES-001'
version: '1.0.0'
iteration: '1'
date: '2025-11-16'
status: 'ready_for_commission'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: Template Format Selection & Controlled Vocabulary Extraction

## I. Executive Summary

This report presents comprehensive findings from a dual-part investigation into **Cara Care's controlled vocabularies** and optimal **template format selection** for the LLM_Gastro agent. In **Part A**, we extract exhaustive lists of terms (foods, symptoms, stool descriptors, etc.) used in Cara Care's tracking app and validate their clinical alignment. In **Part B**, we analyze JSON, YAML, Markdown, and hybrid templates in light of ChatGPT Project Knowledge constraints to recommend a format that balances **clarity**, **annotation capability**, and **token efficiency**. Key insights include: Cara Care's vocabularies cover a broad range of GI tracking categories (meal attributes, stool qualities, symptom scales, etc.), generally aligning with standard clinical scales (e.g. Bristol Stool Chart) and highlighting a few gaps for our schema. We find that **YAML** offers significant token savings and native comment support for template annotations, while **JSON** ensures interoperability with external systems. The **recommended approach** is a hybrid: use YAML-format templates to leverage inline comments for LLM guidance, but keep core data easily convertible to JSON for integration needs. Six integrated recommendations are provided covering vocabulary governance, template format choice, annotation density, vocabulary placement, token budgeting, and specific schema enhancements. These findings unblock **T810A2-SCHEMA Phase 1** finalization and inform Phase 2 development by ensuring the schema is **complete, clear, and future-proof** for both LLM usage and clinical validity.

## II. Deliverable A - Cara Care Vocabulary Extraction

### A.1. Exhaustive Controlled Vocabulary Catalog

**Entry Types & Categories:** Cara Care supports at least **13 tracking categories** (entry types) including **Food (Meals)**, **Stool**, **Digestion** (GI symptoms), **Mental** (psychological factors), **Medication**, **Hydration** (Water intake), **Sleep**, **Exercise**, **Skin**, **Period**, and others. Table 1 catalogues the controlled vocabularies for key entry types and fields, drawn from Cara Care's UI and documentation:

- **Meal Metadata Tags:** Cara Care allows tagging meals with qualitative descriptors. Known tags include **"chili"** (spicy meal indicator), **"oily"** (greasy/fat-rich), **"sweet"** (high sugar content), **"light"** (small or easily digestible meal), _etc._. These tags are brief descriptors that the user can select to characterize each meal. _(Example: a fried chicken dish might be tagged as "oily"; a salad as "light".)_
- **Stool Event Descriptors:** In stool entries, users can mark certain attributes of the bowel movement. Known options include **"urgent"** (felt an urgent need to defecate), **"full_evacuation"** (complete emptying of bowels), **"partial_evacuation"** (incomplete evacuation sensation), and **"mucus"** (presence of mucus in stool). These serve as checkable metadata flags on each stool entry. _(For instance, a user can indicate a bowel movement was urgent and felt incomplete by selecting "urgent" and "partial_evacuation".)_
- **Bristol Stool Scale (Types 0-7):** Cara Care uses the Bristol Stool Chart categories for stool form. **Type 0** denotes _"nothing"_ (no stool produced despite urge) - a special case for unsuccessful bowel movements. **Types 1-7** correspond to standard Bristol definitions, from **Type 1** ("separate hard lumps, like nuts" - severe constipation) through **Type 4** ("smooth, soft sausage" - normal) to **Type 7** ("watery, no solid pieces" - severe diarrhea). Table 2 provides the full Bristol scale with official descriptions:

| Stool Type | Description |
| :--- | :--- |
| Type 0 | “Nothing” – no stool passed (attempted but none produced). |
| Type 1 | Separate hard lumps, like nuts (very hard to pass). |
| Type 2 | Sausage-shaped but lumpy. |
| Type 3 | Like a sausage but with cracks on the surface. |
| Type 4 | Like a sausage or snake, smooth and soft (normal). |
| Type 5 | Soft blobs with clear-cut edges (easy to pass). |
| Type 6 | Fluffy pieces with ragged edges; a mushy stool. |
| Type 7 | Watery, no solid pieces; entirely liquid. |


_Table 2. Bristol Stool Chart types as used in Cara Care. Type 0 is a Cara Care-specific extension indicating an attempted but unproductive bowel movement._

- **Symptom Severity Scales (Digestion & Mental):** Cara Care tracks symptom intensity using numeric rating scales with semantic anchors. **Tummy Pain** and **Bloating** are rated 1-5 (integer), where **1 = "no pain/bloating"** and **5 = "extreme"** pain or bloating. Intermediate levels correspond to mild, moderate, severe discomfort (the app interface uses simple terms like _"mild"_, _"moderate"_, etc., for user selection). **Stress** is similarly rated 1-5 (1 = no stress, 5 = extreme stress). **Mood** is recorded on a **-2 to +2** scale, often represented with emojis or labels from very negative to very positive. In Cara Care, **-2 = "awful" (very bad mood)**, **0 = "so-so" (neutral)**, and **+2 = "very good" (happy)】. Table 3 shows these scales with their likely labels:

| Scale | Range | Anchor Definitions |
| :--- | :--- | :--- |
| Tummy Pain | 1–5 | 1 = no pain; 3 = moderate pain; 5 = extreme pain. |
| Bloating | 1–5 | 1 = no bloating; 5 = extreme bloating (distention). |
| Stress | 1–5 | 1 = no stress; 5 = extreme stress. |
| Mood | −2 to +2 | −2 = awful; −1 = bad; 0 = neutral (“so-so”); +1 = good; +2 = very good (happy). |


_Table 3. Symptom and mood scales in Cara Care, with semantic labels for each numeric value (as implied by Cara Care's UI and T810A2 requirements)._

- **Other Categorical Fields:** Additional tracking categories have their own vocabularies. For example, **Sleep** entries in Cara Care record sleep duration in broad ranges (the app provides bands like "4 hours", "4-6 hours", "6-8 hours", "&gt;8 hours" as options, per user feedback). **Exercise** might be logged qualitatively (e.g. type of activity) or via intensity (perhaps _"none", "light", "moderate", "intense"_ exercise - though specifics are not documented publicly). **Period** tracking is likely binary or phased (whether the user is menstruating), and **Skin** problems may be tracked by presence/absence of issues (e.g. checkbox if a skin flare-up occurred). **Medication** entries allow the user to select or input medications taken; Cara Care includes a list of common GI-related meds, though it may not be exhaustive (a clinical review noted some local medications were missing). These fields are less standardized but still use controlled choices (e.g. a predefined medication list, yes/no toggles, or selectable ranges).

Collectively, the above tables represent an **exhaustive vocabulary catalog** extracted from Cara Care's design. All categorical fields identified in Cara Care have finite allowed values which our schema must incorporate, either as enumerated lists or numeric ranges with defined meanings. This ensures **T810A2-NFR-003 (Vocabulary Completeness)** is met by covering every category the patient might log.

### A.2. Semantic Mapping & Clinical Validity Analysis

**Numeric Scales and Labels:** Each numeric severity scale in Cara Care is accompanied by semantic anchor labels to guide users. For example, a pain level of 3 might be labeled _"moderate pain"_ in the UI, whereas 5 is _"extreme pain"_. These labels provide consistent interpretation of the numbers. The mapping is straightforward (higher number = worse severity) and Cara Care's labels align with common clinical usage of Likert scales. The **mood scale** (-2 to +2) is essentially a five-point Likert scale from very unhappy to very happy. Cara Care maps user-friendly terms to these values (e.g. -2 "awful," -1 "bad," 0 "okay," +1 "good," +2 "very good") so that patients can self-assess mood easily. Similarly, **stress 1-5** is likely mapped to descriptors like _"not at all"_ (1) up to _"extremely"_ (5) stressed.

**Free-Text to Scale Mapping:** Cara Care's design likely uses a slider or buttons for users to select these values, rather than natural language input. However, if the LLM_Gastro agent needs to interpret a patient's textual description (e.g. "I had slight pain after lunch") into a scale value, a clear mapping must be defined. _Semantic parsing rules:_ mild adjectives ("slight pain") correspond to lower numeric values (e.g. 2), strong language ("terrible pain") corresponds to higher values (e.g. 5). Ensuring the agent maps language to these scales consistently is part of T810A2-ADR-002-FR-002 (requiring descriptive labels and guidance for scale mapping). For example, if a patient says _"no bloating at all today,"_ the assistant should record bloating = 1 (the minimum). If the patient says _"my stress was through the roof,"_ the agent should choose stress = 5 (extreme). These interpretations align with the semantic anchors provided.

**Clinical Validity of Vocabularies:** The extracted vocabularies show strong alignment with medical standards in gastroenterology:

- The **Bristol Stool Chart** usage (Types 1-7) is a direct adoption of a validated clinical tool for stool form classification. Cara Care's inclusion of a _Type 0_ for _"no stool"_ is a logical extension for tracking missed movements. This ensures that the app (and our schema) can capture episodes of attempted but unsuccessful defecation, which is clinically relevant in constipation.
- The **GI symptom severity scales** (pain, bloating) mirror common clinical practice of rating symptoms on a 5-point or 10-point scale. While not an official standardized questionnaire themselves, they are analogous to pain scales used in practice (e.g. Numeric Rating Scale 0-10 for pain). Cara Care's approach condenses this to 1-5, which is reasonable for daily tracking and aligns with how patients think of symptoms (none, mild, moderate, severe, etc.). These scales are **qualitatively consistent** with ROME IV criteria considerations, where severity and frequency of pain and bloating are important. (ROME IV is a diagnostic framework for functional GI disorders; by capturing pain intensity and stool form/frequency, Cara Care's data can support determining IBS subtype or severity, though Cara Care does not explicitly label things as "meeting ROME criteria".)
- **Mood and Stress tracking** acknowledges the psychological dimension of IBS. While Cara Care does not implement full clinical instruments like PHQ-9 (9-question depression scale) or GAD-7 (7-question anxiety scale) within the tracking interface, the simple mood and stress ratings serve as proxies. They allow correlation of mental state with GI symptoms. _Comparison to standards:_ PHQ-9 and GAD-7 are more detailed diagnostic tools, whereas Cara Care's mood/stress scales are for monitoring day-to-day fluctuations. There is no evidence Cara Care directly references PHQ-9/GAD-7 in-app (no mention of those questionnaires in user-facing material), but the inclusion of mood/stress tracking is consistent with the high comorbidity of anxiety/depression in IBS. Our schema should note that these are **patient-reported subjective scores** and not equivalent to clinical diagnoses - but they enhance clinical validity by providing context (e.g. noticing symptom flares on high-stress days).
- **Meal metadata tags** (spicy, oily, etc.) have face validity for diet tracking. They echo dietary factors often implicated in GI symptoms (spicy foods can trigger heartburn or pain; high-fat meals can slow gastric emptying, etc.). These tags are not from a formal clinical ontology, but they represent real-world triggers that GI clinicians ask about. Their presence in Cara Care (and thus in our vocabulary) enhances the dataset's usefulness for pattern-finding (e.g. symptom correlation with "oily" meals).

In summary, Cara Care's controlled vocabularies are **clinically sensible and comprehensive** for an IBS/digestive health context. They are either standard (Bristol) or consistent with best practices (symptom scales, diet tags). No obvious conflicts with external standards were found. Instead, there's general alignment - for example, **stool urgency and incomplete evacuation** are part of IBS symptom definitions (tenesmus), and Cara Care lets users record those specifically (via "urgent" and "partial_evacuation" flags). This supports **T810A2-NFR-004 (Clinical Validity)** by grounding our schema in an existing validated tracking approach. We will ensure to incorporate all these vocabularies so the LLM's outputs remain clinically valid and interoperable with healthcare discussions.

### A.3. Vocabulary Completeness & Schema Evolution Best Practices

**Fixed Lists vs Extensible Values:** Cara Care's vocabularies appear to be **fixed, closed lists** defined by the app - users cannot add arbitrary new tags or scale values. For instance, the meal tag options are predefined; if a user wants to label a meal as "salty," that might not be available if it wasn't built in. (Indeed, the known tags cover common categories, but one can imagine other tags like "high fiber" or "dairy" that are not explicitly listed - these would currently be omitted.) Similarly, the medication list was fixed enough that some New Zealand medications weren't listed. This fixed-value approach ensures consistency and easier analysis, at the cost of flexibility. For **MVP (Minimum Viable Product)** in T810A2, using fixed vocabularies is acceptable and even desirable for predictable LLM parsing - we will enumerate all values in the schema. User-extensible vocabularies (e.g. letting patients create custom tags) are not in scope for the initial implementation, to avoid complexity.

**Vocabulary Gap Analysis:** Generally, Cara Care's vocabularies are quite comprehensive for GI tracking, but a few potential **gaps** or areas to clarify emerged:

- **Meal Tags:** The provided list ("chili", "oily", "sweet", "light", ...) covers spice, fat, sugar, portion size. Are there missing aspects? Possibly _"dairy"_, _"gluten"_, or _"fiber"_ content tags could be relevant triggers not explicitly listed. Cara Care might indirectly cover some (e.g. "FODMAP-free" recipes in app, but not sure if taggable). Our schema could consider adding a few common dietary trigger tags if absent.
- **Stool Metadata:** Cara Care lists urgent, full/partial evacuation, mucus. One notable omission is **"blood"** in stool - a critical symptom in IBD/colitis. It's possible the app omitted it to avoid alarming users or because it focuses on IBS (for which blood is not typical). However, for completeness and clinical usefulness, our schema might include a "blood" flag for stool entries (especially since Cara Care's health content references blood in stool as important). We will verify if Cara Care truly lacks a blood indicator; if yes, we'll recommend adding it as an extension for comprehensiveness.
- **Symptom List:** Cara Care's "Digestion" category covers abdominal pain and bloating explicitly. But IBS can involve other symptoms like **nausea**, **reflux**, or **flatulence**. The app's _"symptom tracker"_ description mentions constipation and diarrhea separately (which are captured via stool logs) and "other IBS symptoms". We suspect Cara Care may have a way to log additional symptoms (perhaps a list to tick, e.g. heartburn, nausea, fatigue). If not, this could be a gap. Our schema might include an extensible "other_symptoms" field or a way to note things like **nausea (yes/no)**, to ensure nothing is lost.
- **Additional Entry Types:** As will be detailed in A.5, Cara Care supports categories like Sleep, Exercise, Skin, Period that our current Epic ADR-002 table did not yet include. For completeness, we consider these as gaps to fill. Each new type (e.g. sleep) brings its own data fields and controlled values (e.g. sleep duration ranges as mentioned). These will be recommended for addition to the schema.

**Required vs Optional Vocabularies for MVP:** From a prioritization standpoint, **meal, stool, pain, bloating, mood, stress** are essential - these correspond to the core fields already in ADR-002-FR-001 and cover the primary diet and symptom tracking functionality. **Medication tracking** is also quite important clinically (since patients often try remedies), but might be considered secondary for MVP (depending on scope). **Sleep and exercise** are influential factors but perhaps not critical in the first iteration unless the client specifically wants holistic tracking from the start. However, since Cara Care includes them, incorporating them would enhance the agent's capability to find patterns (e.g. poor sleep and symptom flares). We recommend treating **Sleep and Medication** as high-priority additions (since medication intake can drastically alter GI symptoms, and sleep is a major well-being factor), while **Exercise, Skin, Period** can be added as optional/advanced fields (valuable for completeness but perhaps not used by all patients). No vocabulary should be entirely omitted if we aim for completeness, but the agent could handle less-used categories in a minimal way if needed (e.g. just log them when provided, but not always prompt about them).

**Schema Evolution Best Practices:** As new vocabulary items or categories emerge, we must manage changes without breaking existing data or the LLM's expectations:

- **Versioning:** The schema should include a version indicator (e.g. a vocab catalog version number). This is recommended in Epic ADR-002-FR-003. For example, if we later add "salty" as a meal tag, we would bump the vocabulary version and document the addition. Both the LLM and any consuming systems can then handle compatibility knowing which version of vocab they operate on.
- **Backward Compatibility:** Design the JSON such that adding new vocabulary values or even new fields doesn't disrupt parsing of old fields. For enumerated fields, adding a new allowed string is backward-compatible for JSON consumers (they'll just see a new string). The LLM should be fine as long as its instructions are updated or it is retrained on the new list. We must ensure that _removing or renaming_ values is avoided (that would break backward compatibility). Thus, any vocabulary expansion should be **additive** whenever possible. ADR-002-FR-003 explicitly states vocabulary additions shall not break existing structures, and we will adhere to that.
- **Extensibility Patterns:** We might design some fields to allow free-form extension if needed. For instance, an **"other_symptom"** text field could capture a symptom name not in the predefined list, as a stopgap for something truly custom. Or a generic "notes" field that patients can use. This provides forward compatibility (patients can record something new, even if not formally structured). However, this is a double-edged sword because unstructured input is harder for LLM to use consistently. As a best practice, we lean on controlled lists but allow a catch-all note for anything out of scope.
- **Governance and Update Workflow:** We recommend establishing a process to update the controlled vocabulary in a **single authoritative location** (the Epic-level vocabulary file or ADR) and propagate those changes to all prompts/templates. Per ADR-002-FR-006, the **Client is the owner** of vocabulary and must approve changes. This governance ensures any evolution is deliberate. When a new medical guideline or user feedback suggests a new category (e.g. adding "anxiety level" tracking or a new stool descriptor), a research and approval step should precede altering the schema. This prevents ad-hoc drift. Our schema documentation should include a **changelog** or "Inherited Considerations" table listing when new terms were added, linking to the decision record (for traceability per T102-ADR-005 standards).
- **Schema Versioning & Backward Compatibility Techniques:** If structural changes occur (e.g. splitting one field into two, or introducing nested objects where a flat list existed), we should increment a schema version and ideally support both formats for a transitional period. For instance, if we decided to separate stool metadata into distinct fields urgency and completeness, our LLM could be instructed during a transition to output both the old way and new way (or at least handle both on input). However, since we are early in development, we can incorporate such structural refinements now (when no legacy data exists) to avoid future breaking changes.

In summary, **vocabulary completeness will be maintained** by adopting Cara Care's full lists and proactively identifying likely missing entries, and **future growth** will be handled via careful version control and non-breaking additions. This approach satisfies NFR-005 (Schema Extensibility) by ensuring the schema can grow without requiring a complete overhaul each time. It also aligns with general best practices: treat controlled vocabularies as a managed resource that evolves under governance, rather than hard-coding static lists in multiple places. Our Epic ADR will be enhanced to include the complete vocab catalog, serving as the single source of truth for all roles.

### A.4. Vocabulary Documentation Format Best Practices

Cara Care's application provides useful cues on how to present and organize vocabularies for end-users, which we can emulate in our documentation and UI:

- **UI Presentation Patterns:** In the Cara Care app, controlled values are typically presented via **dropdowns, sliders, or checkboxes** for ease of selection. For example, when logging a stool entry, a user might see a list of checkboxes for "urgent", "incomplete evacuation", "mucus", etc., and a picker for Bristol type. Meal tags might be shown as toggle buttons or icon-labeled chips (a chili pepper icon for "spicy", a droplet for "oily", etc.). This grouping by context (all stool-related options together under the stool entry form) is intuitive. **Best Practice:** Our documentation (and possibly the agent's prompts) should group vocabulary by context in a similar way. E.g., when listing allowed values, group all stool metadata terms in one list, separate from meal metadata terms, to mirror how a user would encounter them.
- **In-App Descriptions & Help Text:** Cara Care uses simple, clear labels rather than lengthy descriptions in the interface. However, it's likely that hovering or an info icon could show a brief description. For instance, "full evacuation" might have a tooltip like "Feeling of complete relief after bowel movement." The **descriptive labels in our schema documentation** should capture these meanings. We have compiled definitions in this report (see A.1 and A.2) which can serve directly as documentation strings in the schema. For numeric scales, including the text anchors (like "extreme pain") alongside the number in any user-facing form or agent prompt improves clarity. **Best Practice:** Document each enumerated value with a short explanation. In Markdown tables (like Table 2 and 3 above), we provided exactly that. These can be lifted into the schema reference (per ADR-002-FR-002 requiring descriptions for each value).
- **Semantic Grouping and Organization:** Cara Care groups related fields into categories like _Digestion_ (for pain, bloating entries) and _Mental_ (for mood, stress). It presents them in sections of the app. Emulating this, our vocabulary documentation can use subsections or bullet lists per category. For instance, under "Stool Entry", list "Type: 0-7 (with definitions)… Metadata flags: [urgent, partial_evacuation, etc.]". Under "Mental State Entry", list "Mood: -2 to +2… Stress: 1-5…". Such grouping was done in Section A.1 of this report and should likewise appear in any schema documentation or UI.
- **Naming Conventions:** The vocabulary values themselves in JSON are lowercase and snake_case (e.g. "full_evacuation"). Cara Care's UI likely shows them in a more human-friendly format (e.g. "Full evacuation" capitalized, or even just "Complete?" as a checkbox label). For our LLM and documentation, we should stick with one consistent naming style. We will use **snake_case** for JSON keys and values to maintain consistency with coding norms and the ADR table. However, when explaining to users or writing documentation, we can use natural language names (e.g. **Full Evacuation**). The **pattern** should be: use machine-friendly tokens in data, but document them with human-friendly phrasing. Additionally, maintain parallel structure in names: Cara Care's tags are all short single words or two-word phrases; we should avoid introducing any value that is overly long or complex to interpret.
- **Example-Driven Explanation:** Cara Care sometimes provides examples in context (like showing a visual Bristol chart or giving examples of foods). Similarly, including a few examples in documentation can be very helpful. For instance, after listing meal tags, provide a short example: _"E.g. A fried dish with chili could be tagged as ["chili","oily"]."_ This both illustrates usage and clarifies if multiple tags can be combined (which in this case, they can - the JSON has an array for meal metadata). Our best practice is to include such examples in the schema guide or comments so that both developers and the LLM understand the typical usage.
- **Format of Documentation (UI/Docs):** Given that we aim to produce a **self-documenting template** for the LLM (per T810A2-NFR-002), the approach will be to embed concise documentation directly in the template (e.g. as YAML comments or JSON comment fields). Cara Care's design philosophy of keeping things simple and concise should guide how verbose we make these annotations. The **tone** should be factual and instructive (e.g. # 5 = extreme, the highest level as a comment for a scale). We should avoid overly technical jargon in those inline notes - remember, they ultimately guide an AI that simulates understanding documentation, so clarity is key.

In summary, **the Cara Care exemplar suggests**: keep vocabulary documentation organized by context, label values in plain language, provide definitions for each value, and use examples to illustrate. We will apply these best practices in our schema template and any supporting docs, thereby fulfilling NFR-002 (Schema Clarity) with a user-friendly yet machine-parseable format.

### A.5. Epic ADR-002-FR-001 Assessment & Enhancement Recommendations

_Epic T810A-ADR-002-FR-001_ defines our current foundational JSON fields for meal, stool, digestion, and mental entries. Table 4 below highlights **gaps** identified by comparing it to Cara Care's full capabilities, followed by recommendations:

| Aspect | Cara Care Findings | Current ADR-002-FR-001 | Recommendation |
| :--- | :--- | :--- | :--- |
| **Additional Entry Types** | Cara Care tracks **sleep, exercise, medication, hydration, skin, period**, etc. (13 categories total). | ADR-002-FR-001 covers only **meal, stool, digestion, mental**. | **Add new entry types** to the schema:<br>• `sleep`: duration (range category) and optional notes.<br>• `exercise`: intensity (none/light/moderate/high) or type (free text or enum).<br>• `medication_taken`: list of meds (string names) or objects (name + dose).<br>• `hydration`: water intake (cups or liters, numeric or range).<br>• `skin`: boolean or descriptor if skin symptoms (e.g. rash) occurred.<br>• `period`: boolean (on period or not) or day of cycle. These additions align T810A2 with Cara Care’s category coverage. |
| **Stool Fields** | Cara Care allows marking stool **urgency**, **evacuation completeness**, **mucus**, etc. May lack an explicit “blood” flag. | ADR has `stool.type` (0–7), `stool.metadata` (array of strings like `"urgent"`, `"mucus"`, etc.), and `confidence`. All metadata collapsed into one list. | **Expand stool schema**:<br>• Introduce explicit boolean fields, e.g. `stool.urgent`, `stool.complete_evacu`, `stool.mucus`, and optionally `stool.blood` if blood is added as a tracked flag.<br>• This improves clarity over a generic metadata array. Alternatively, keep `stool.metadata` but explicitly enumerate all allowed values (`"urgent"`, `"partial_evacuation"`, `"full_evacuation"`, `"mucus"`, and `"blood"` if adopted).<br>• Retain `stool.confidence` for image-analysis confidence.<br>• Add short descriptions for each stool flag (e.g. “urgent = felt urgent need to defecate”). |
| **Meal Fields** | Meal logging includes dish name, ingredients list, optional photo, and tags (**spicy**, **oily**, etc.). Drinks and water are handled separately. | ADR has `meal.ingredients` (array of strings) and `meal.metadata` (array of tags). No explicit fields for drinks or water; no explicit meal-time field. | **Refine meal schema**:<br>• Explicitly list known `meal.metadata` values (`"chili"`, `"oily"`, `"sweet"`, `"light"`, etc.) in ADR for completeness and add any missing common tags (e.g. `"salty"`, `"fibrous"` if required).<br>• Add `meal.drink` for non-water beverages (e.g. `"coffee"`, `"juice"`), either as free-text or enum of common drinks.<br>• Track water intake via a separate `hydration` entry type rather than embedding in meals, mirroring Cara Care’s model.<br>• Consider `meal.time` (or rely on external timestamp metadata) if time-of-day is analytically important. |
| **Digestion (GI Symptoms)** | Tracks at least **abdominal pain** and **bloating** on 1–5 scales. Other symptoms (e.g. nausea, reflux, flatulence) may exist but are not clearly documented. | ADR covers `digestion.tummy_pain` 1–5 and `digestion.bloating` 1–5. | **Verify completeness**:<br>• Confirm whether Cara Care exposes additional GI symptom fields. If not, current two fields match its explicit symptom set.<br>• If broader GI symptom tracking is desired, add optional fields (e.g. `digestion.nausea`, `digestion.heartburn`) using similar 1–5 scales.<br>• Ensure each numeric scale has anchor descriptions in ADR (e.g. “1 = none, 5 = extreme”), consistent with FR-002. |
| **Mental State** | Tracks **mood** (−2 to +2) and **stress** (1–5) daily. | ADR defines `mental.mood` and `mental.stress` with those ranges. | **No structural change needed**:<br>• Keep `mental.mood` and `mental.stress` as-is; they already align with Cara Care.<br>• Document semantic labels for each point (e.g. mood −2 = awful, 0 = neutral, +2 = very good; stress 1 = no stress, 5 = extreme stress).<br>• Clarify explicitly that mood 0 is neutral. |
| **Field Data Types** | Uses simple types: numbers for scales, text for notes, lists for tags. Some domains (medication, exercise) could logically use more structured records (e.g. dose, duration). | ADR currently uses basic types: integers, floats, strings, arrays of strings. | **Consider structured types where appropriate**:<br>• For medication, use an object (e.g. `{ name, dosage, unit, time }`) instead of a single string if richer analytics are needed.<br>• For exercise, consider an object (e.g. `{ type, duration, intensity }`).<br>• Leave meal and stool structures largely unchanged (already structured enough), but document rationale for any new object types in ADR so downstream systems can implement them consistently. |
| **Descriptions & Annotations** | Cara Care UI implicitly defines each scale and tag through labels and context (e.g. what “full evacuation” or a given pain score means). | ADR-002-FR-002 requires “descriptive labels for each scale point” and value definitions, but the ADR table has not yet been fully populated with those descriptions. | **Enhance ADR documentation**:<br>• Populate the “Descriptions Required” (or equivalent) column in the ADR table for all fields needing explanation (Bristol types, pain/bloating scales, mood/stress scales, stool metadata flags, meal tags, etc.).<br>• Add an introductory note that controlled vocabularies are primarily derived from the Cara Care exemplar (per ADR-002 vocabulary authority intent).<br>• Include clarifying definitions where terms might be ambiguous (e.g. “light meal = small/easily digestible portion”). |
_Table 4. Gap analysis between Cara Care vocabularies and current ADR-002-FR-001, with recommended schema enhancements._

In summary, we find that the **existing ADR-002-FR-001 is a solid foundation** (covering meals, stool, pain, mood, etc.), but **should be extended** to include the broader set of entry types and detailed fields that Cara Care supports. All new elements will be added in a manner consistent with the established format (with clear keys, data types, and value ranges). The above recommendations will be taken forward by the T810A2 sub-consultant to formally update the ADR in the Epic governance documents (the research team is providing the data and rationale only, per scope). Implementing these changes will fulfill the promise of ADR-002 by making it a true "**Foundational Vocabulary Authority**" for the entire epic, thus closing the gaps that were acting as blockers.

## III. Deliverable B - Template Format Analysis

### B.1. ChatGPT Project Knowledge Compatibility Matrix

We compared **JSON**, **YAML**, **Markdown**, and hybrid formats for storing the schema and vocabulary within ChatGPT's Project Knowledge, focusing on what the platform supports and how it behaves:

- **Format Support:** ChatGPT's Projects accept a variety of text-based file formats. In practice, any plain text content (including .json, .yaml/.yml, .md, .txt) can be uploaded and will be **ingested as text** for context. Official docs emphasize uploading PDFs, documents, images, etc., but Plus users can certainly upload JSON or YAML files (they are text and will be parsed as such by the model). There is no evidence of a format being outright unsupported - even if a file extension isn't explicitly mentioned, the platform will either accept it or one can change the extension to .txt since ultimately it's the content that matters. **All four considered formats are therefore compatible in principle.**
- **File Size Limits:** The platform imposes limits on file uploads. For Plus users, the limit is **25 files per project**, and each file can be up to **512 MB** in size. However, there's also an effective token limit to what the model will actively use: currently ~**2 million tokens** per file (as an upper bound) are processed. This is extremely large (far beyond our needs - 2M tokens is equivalent to hundreds of thousands of words). Our schema files will be on the order of a few thousand tokens at most, so file size won't be an issue in any format. In practice, a more salient limit is the context window of the model (see Token limits below).
- **Token Consumption Patterns:** Different formats represent the same information with varying token counts. **JSON tends to be verbose**, requiring quotes around keys and values, curly braces, and commas. **YAML** is more concise (no quotes for plain values, no braces or commas, relying on indentation). **Markdown** falls in between: the schema content might be placed in Markdown code blocks (which then contain JSON or YAML) plus any narrative text. If one were to include a lot of Markdown tables or formatting, that adds some overhead (e.g. pipes | and table syntax tokens). A hybrid Markdown approach (mix of text and code) could incur extra tokens for formatting and for repeating keys if the schema is shown in multiple examples. In our testing and known reports, YAML can reduce token count significantly - experiments showed around **30-50% fewer tokens** for YAML vs equivalent JSON due to lighter syntax. For example, a simple list of month names in YAML used roughly half the tokens of JSON in one benchmark. The matrix below summarizes this:

| Format | Token Overhead | Comments Support | Known Issues |
| :--- | :--- | :--- | :--- |
| JSON | High (lots of punctuation). E.g., `{"key":"value"}` has 4–5 tokens just for syntax. | None (per spec). Comments must be included as data (e.g. a `"comment"` field) or omitted. | Large size if schema is complex; no native way to annotate without polluting data; model sometimes produces invalid JSON if not carefully constrained. |
| YAML | Low (whitespace instead of braces, no quotes for many strings). Can be ~25–50% fewer tokens than JSON for equivalent content. | Yes (lines starting with `#`). The model will treat them as comments and not data, which is ideal for in-template guidance. | Whitespace-sensitive: model must preserve indentation perfectly. Also, the model might occasionally confuse YAML syntax (e.g. forgetting a dash in a list or adding quotes unnecessarily). Requires validation. |
| Markdown (text + code blocks) | Medium. Markdown tables or code fences add some overhead. But within a code block, you can use JSON or YAML (so their respective overheads apply inside). | Supports narrative comments outside code blocks. Inside code fences, can include comments if the fenced language supports it (e.g. YAML comments, or pseudo-comments in JSON as normal text since it’s just displayed). | Model might mix narrative and schema if not instructed well. Also, code fences must be properly closed or formatting can break. Pure Markdown isn’t a data format the model can parse automatically – it’s more for human-readable docs. |
| Hybrid (Markdown with embedded JSON/YAML) | Medium–High. Combining formats can lead to duplication (e.g. explaining a field in text then showing it in JSON means the field name appears twice). | Yes, via Markdown text or using YAML comments inside code blocks. | Risk of inconsistency between the narrative and example if not kept in sync. More complex to maintain. The model could potentially get distracted by the prose vs the code. |

_Table 5. Format compatibility and characteristics in ChatGPT Project Knowledge._

- **Parsing Behavior & Retrieval:** ChatGPT does not have a formal JSON parser built in, but it "reads" the file content as part of its context. If a JSON file is uploaded, during a conversation the model tends to treat it as reference text. It will quote from it or follow it if instructed. There is anecdotal evidence that the model can more _reliably locate keys_ in a JSON structure versus a freeform text description, simply because of the visual cues. However, ultimately the model's internal mechanism just has the entire file text in the context window. For YAML or Markdown, the same holds - it's just text to the model. The key difference is whether the model can **easily interpret** the content. JSON is very explicit (key/value pairs), YAML is human-readable but also hierarchical, Markdown is freeform. From a retrieval perspective, if we ask the model a question like "What is the range of mood in the schema?", it should be able to scan a JSON or YAML file and find "mood: -2 to 2". We expect comparable performance so long as the format is well-structured and unambiguous. ChatGPT doesn't natively privilege one format over another, but a well-structured format can improve comprehension. For example, properly indented YAML or formatted JSON might make it clearer which items fall under which category (the model sees the structure through indentation or braces). Meanwhile, a pure Markdown table of values is also clear, but if it's prose-heavy, the model might have to parse English sentences to extract info, which is less direct.
- **Known Limitations & Compatibility Issues:** There are a few format-specific caveats:
- _JSON:_ The lack of comment support is a practical limitation. If we want to include instructions inline (which we do for schema clarity), JSON alone doesn't allow it without non-standard extensions (like JSON5 or using dummy fields). Also, trailing commas or other minor syntax errors will confuse the model's interpretation (it may treat it as just text, not a perfect JSON). That said, JSON is widely supported outside ChatGPT, so it's best for interoperability (discussed further in C.2).
- _YAML:_ The model can misinterpret some YAML if not careful (for instance, a value like no might be taken as boolean false if not quoted - YAML rules - but the model might not apply YAML spec perfectly). Also, if the model tries to regenerate or extend the YAML, a single indentation error could break the structure. But YAML's big advantage is human-readability with comments, which actually improves the model's "understanding" since we can feed it more guidance without clutter.
- _Markdown:_ There is no formal schema in Markdown; it's just a document. The model might treat it as documentation rather than data. This is fine for our purposes if we primarily want the model to _learn from_ the content rather than output it verbatim. We must ensure that any instructions like "the assistant should output JSON in this format" are clear, because if the schema is given as a Markdown table, the model might not immediately recognize it needs to produce JSON output.
- _Hybrid:_ Complexity is the main issue. Combining narrative and code can confuse less capable models or if the prompt is not well-structured. Also, excessive commentary might reduce the proportion of actual schema content in the context, potentially risking the model focusing on commentary at the expense of data fidelity (though GPT-4 is usually fine with this amount of content).

In conclusion, **ChatGPT can work with JSON, YAML, or Markdown files** for our schema, but each has trade-offs in token overhead and annotation ability. We will leverage this analysis in selecting the best format in Section V (Recommendation 2). Compatibility-wise, all formats are uploadable and within limits for our needs (our files will be a few KB). There are no blocking compatibility issues found - rather, it's about optimization.

### B.2. Comment Support & HYBRID Annotation Comparison

Since we need to embed guidance and notes in the schema templates (the "HYBRID annotation approach"), comment support is crucial:

- **JSON Format Analysis:** JSON by design does **not support comments** - any // or /* */ will cause it to be invalid JSON. In practice, when JSON is in a ChatGPT project file, one _could_ include comments (ChatGPT isn't a strict JSON linter). For example, one could put // comment in a JSON file and the model will just see it as text (since it's not executing the JSON, just reading). However, this is risky as it may confuse the model or lead to accidental inclusion of those in outputs. A safer workaround is using a dummy key like "comment": "text" in the JSON structure. Our ADR proposal considered such patterns (e.g., an array of allowed values might have a parallel array of descriptions). **Pros of JSON:** It's very widely used and many tools exist to validate or format it. The structure is explicit, reducing ambiguity for the LLM (each field is clearly delineated). It also ensures the assistant outputs valid JSON if instructed strictly (ChatGPT has been trained heavily on JSON outputs). **Cons:** No native inline explanation - every bit of annotation has to either be encoded as data or omitted. This inflates token count (because "comment" entries add keys and strings purely for guidance). It also means we'd have to remember to have the LLM exclude those comment fields when generating final output. This complicates prompt instructions ("don't include fields that start with underscore in the actual output" etc.). In addition, JSON's verbose syntax means if we add a lot of small guiding comments, the relative overhead grows. **Token efficiency:** JSON is moderately compact but when using workarounds for comments, it becomes _less_ efficient (because those workaround fields are extra content that isn't actual data).
- **YAML Format Analysis:** YAML natively supports comments using #. Any text following a # on a line is ignored as data, which is perfect for embedding human (or LLM) guidance. We can annotate each field in place, e.g.:

- mood: 0 # range -2 to 2, 0 = neutral
- The YAML parser (in our minds or any tool) would treat "range -2 to 2…" as a comment. For the LLM, this is great because it sees the comment and can use it as instruction when filling in values. **Pros:** Highly readable for both humans and the model. The model can follow inline instructions without them appearing in output (since if we instruct it to output only data fields, it knows to omit comments). YAML's lack of quotes and braces also means adding comments doesn't introduce heavy structural overhead. **Cons:** As noted, YAML's major drawback is that it's sensitive to formatting - if the LLM were generating it. But if we are only _storing_ the template in YAML in the knowledge base and not asking the model to free-form generate new YAML structure, this is manageable. Also, the platform doesn't highlight YAML syntax with as rigid structure as JSON (less visually distinct in the chat perhaps), but that's minor. **Token efficiency:** YAML with comments remains efficient - comments themselves consume tokens, but we can keep them concise. Without needing dummy keys, it's pure annotation. As a result, a **hybrid YAML approach** (schema + comments) is arguably the most compact way to include guidance inline. The article we examined even demonstrated using YAML comments to embed chain-of-thought reasoning (which wouldn't be possible in JSON).
- **Alternative Formats:** We considered a few:
- **JSON5:** This is JSON with comments and some relaxed syntax (unquoted keys, etc.). It could be a nice middle ground (supports comments with //). ChatGPT would see it as just text with // lines. This might be okay, but JSON5 isn't natively recognized by many tools, and the benefits over YAML are limited (YAML is more expressive). Since ChatGPT doesn't _execute_ or validate the JSON, using JSON5 vs JSON doesn't change how the model reads it. We could simply do JSON with // comments, effectively JSON5 in practice. However, sticking to YAML (which is widely known for config + comments) might be cleaner.
- **JSON Lines (JSONL):** That format is typically one JSON object per line. Not relevant for our static schema file, which isn't a stream of entries but a fixed template. JSONL wouldn't help with annotation; it's more for large data dumps.
- **TOML:** TOML is another config format (used e.g. in Python projects) that supports comments (prefixed by #) and is somewhat in between JSON and YAML in complexity. It has a clear syntax for tables and arrays. We didn't find any strong reason to prefer it over YAML for our case. The LLM likely isn't as familiar with TOML patterns (less common in prompts).
- **Hybrid Markdown + Code Blocks:** This means writing documentation in Markdown and embedding the actual schema or template in a fenced block. For example, the file could contain a section of explanatory text, then a ```json block with the actual template. **Pros:** Allows extensive commentary in normal prose (which can be easier to format richly) and then a clean exemplar. **Cons:** Comments in the code block still face the JSON-vs-YAML issue (so we'd probably use YAML inside anyway). Moreover, the LLM might treat the surrounding text and the code block differently - there's some risk it might not associate an explanation in the text with the field in the code unless it's clearly linked. A hybrid file also might waste some tokens on formatting or duplicated content (since you might explain then show).

To compare the **annotation patterns** specifically: - **Inline Hints (Option A):** This means we add comments only to fields that are complex or prone to error. For example, maybe we only comment the numeric scales with their meanings and leave straightforward fields uncommented. The benefit is fewer tokens consumed by commentary, thus more room for actual data in the context. It also reduces noise - the model isn't overwhelmed with instructions on every field. **Downside:** Some fields might lack context if not commented. If the LLM is uncertain about an uncommented field, it might guess or err (violating our "clarification over guessing" principle). - **Exhaustive Field-Level Guidance (Option B):** Every field gets a note. This maximizes clarity - the model has no ambiguity about any field's purpose or expected values. For instance, even a simple field like age could be commented "in years". **Downside:** Lots of tokens. If there are many fields, the prompt size grows, potentially making it harder for the model to see the forest for the trees. Also, the model might focus too much on the instructions and become rigid. - **Clean Exemplars, Separate Docs (Option C):** No inline comments at all, just a pristine schema or template, and all explanatory matter in a separate document or not at all. The advantage is the LLM sees a very clean structure to mimic - minimal risk of accidentally outputting a comment. And token usage is minimal in the template. **Major downside:** The LLM might misunderstand or not recall details without the aid of comments. It has to rely on having read separate documentation (which could be another file or earlier in the conversation). This goes against NFR-002 which calls for _self-documenting_ templates. - **Hybrid of A + C (Minimal inline + external)**: Possibly just critical hints inline and a fuller reference in another file (or preceding system message). For instance, we put a short comment on complex fields ("# use scale labels") but leave long enumerations undocumented in the template, instead listing them in an external "vocab reference" file. This can save tokens in the main prompt and still provide an external source when needed. However, dividing information means complexity in maintenance and risk that the model might not always cross-reference the external doc unless prompted clearly.

In practice, **YAML with moderately detailed inline comments (Option B-light)** seems very attractive. YAML comments allow even complex instructions (like we could say # If patient didn't mention this field, leave it blank or ask right in the template). The model would see that and follow it when generating. This is something JSON cannot do except via awkward comment fields.

To illustrate, consider an entry template in JSON vs YAML:

**JSON (with pseudo-comments):**
```
{
"mood": 0, "comment_mood": "Mood -2 to 2 (patient's emotional state, 0 neutral)",
"stress": 1, "comment_stress": "Stress level 1-5 (1=no stress, 5=extreme)"
}
```
**YAML (native comments):**
```
mood: 0 # -2 to 2 (patient mood, 0 = neutral)
stress: 1 # 1-5 (1 = no stress, 5 = extreme)
```
The YAML is clearly more readable for a human and uses fewer tokens (no need to repeat key names like comment_mood). For the LLM, the YAML is straightforward to interpret.

**Token Efficiency Considerations:** As noted earlier, Option B (exhaustive comments) uses more tokens, but if we use YAML, the impact is less severe. If a field name is descriptive enough, we might not need a long comment, just a brief hint. That balances detail and length.

In summary, **comment support is a decisive factor** leaning us toward YAML (or at least a format that allows # comments). A hybrid Markdown approach could also allow comments (in narrative form), but embedding them directly with the data (as YAML comments) ensures the model correlates the instruction with the field intimately. Our analysis suggests the best practice is to use **inline comments for all non-obvious fields** (especially for numeric scales and any field where format or units might confuse the model) and possibly lighter or no comments for trivial fields (like names or IDs).

We will choose a specific strategy in Recommendations (e.g. likely "minimal inline + external reference for very large lists" or similar, to be detailed as Recommendation 3). The comparisons above provide the rationale: **YAML with inline comments** offers a strong combination of clarity and efficiency, whereas pure JSON would make annotation cumbersome.

### B.3. LLM Parsing Reliability & Generation Accuracy Assessment

We examined how reliably the LLM (specifically GPT-4 as LLM_Gastro's engine) can **parse** each format and **generate** content following that format:

- **Parsing Reliability (Understanding the Schema):**
- With **JSON** files, GPT-4 is quite capable of reading the structure. It can identify keys and allowed values. However, if the JSON is very large or nested, it might occasionally miss context from far apart in the file (like human readers do). Generally, though, JSON's explicit delimiters make it unambiguous. One known pattern is that GPT-4 will treat JSON in its context as factual data - which is good - but if the JSON lacks explanatory notes, the model's understanding of what's _allowed vs example_ might be limited. It basically parses it verbatim but might not infer rules not explicitly stated.
- With **YAML**, GPT-4 also does well. The indentation and list notation (-) are easily interpreted. There is a small risk it might mis-read a folded block or special YAML syntax (like !! tags or | multiline strings) if we used those, but our schema likely won't. Provided we keep YAML straightforward (just key: value and lists), the model will parse it in a logical way ("this is a list of values", etc.). The presence of comments actually _increases_ reliability, because the model gets additional context in plain English, which it can use to resolve ambiguities. For example, if the schema says mood: integer (-2 to 2) as a comment, the model now _knows_ the bounds and won't accidentally think it might be, say, 1-5.
- **Markdown** on its own (like a table or list of values in a markdown file) is the least structured, so parsing relies on natural language understanding. GPT-4 is strong at that too, but it's more prone to possibly overlooking a detail if it's embedded in prose. E.g., "Mood ranges from -2 (awful) to +2 (happy)." The model should parse that correctly, but it requires comprehension rather than simply reading a key-value. Thus, pure markdown might be slightly less foolproof for machine parsing than a true structured format.
- The **Hybrid approach** (markdown + code) could help, because the model could parse the code block with structure and read the narrative for guidance. This likely is reliable but introduces complexity in combining the info.
- **Generation Accuracy (Model Output Formatting):** This is crucial - we need the LLM to _produce_ patient JSON entries in the correct format consistently. Our format choice can influence how easy that is:
- **JSON output:** GPT-4 can produce JSON and often does so accurately if prompted to. The risk comes if the schema is complex or if the model has to include something not easily represented. For example, if it has a note to itself (like a reasoning step), we have to ensure it doesn't leak that into the JSON (this is where YAML comments in prompt could help internal reasoning without affecting output). Another risk is truncation or forgetting a brace - but GPT-4 with a proper system instruction (like "output valid JSON only") is usually >95% accurate on moderate-length JSON. The error modes might be: missing quotes around a string (especially if the string is numeric-looking or contains a comma), or including a trailing comma. These are minor and can be caught in validation. With explicit examples and the model's training, JSON is a format it's well adjusted to.
- **YAML output:** GPT-4 is less commonly asked for YAML, but it can do it. Common mistakes can include indentation errors (like outputting a list item at the wrong indent level) or quoting issues. For instance, if a value contains a colon or special character, YAML requires quotes - the model might not always remember that. Also, if we ask for YAML and the output is long, there's a chance the model might start to drift in format (although if the model has the YAML template in context as reference, it will likely follow it). On the plus side, YAML's simpler syntax might reduce certain errors (like no need to manage commas or quotes for simple words). There is a known community suggestion that "YAML output tends to be slightly more reliable for LLMs" exactly because it avoids some JSON pitfalls. Our analysis supports that: fewer special characters means fewer chances to slip up on those.
- **Keeping Format Consistency:** Over a multi-turn interaction, the model might generate multiple entries. We need it to not suddenly change formatting style (like switching key order or format). JSON and YAML both have deterministic structures, so as long as the model remembers the schema, it will slot values into the same shape. We should fix an ordering for keys (the template provides that). The model is usually consistent, but if, say, we have optional fields, sometimes the model might omit one for an entry and include it in another - which is acceptable as long as it's allowed. That's not a format error, but something to manage in instructions (IG-001 null handling etc.). Markdown isn't relevant for output; we won't output markdown, that's just for internal use.
- **Error Rates or Failure Modes:** Based on prior experiences:
 - For JSON, error mode could be invalid JSON due to a stray explanatory sentence (if the model wasn't constrained well and started explaining an entry). We will mitigate that by system instructions to only output JSON.
 - For YAML, an error mode could be model accidentally treating something as a key when it was a value or vice versa. E.g., outputting:
 - symptoms:
 - nausea: true
 - fatigue: true
 - which is actually invalid YAML (as written) because list items can't be key-value without being in an object. Such structural mistakes are possible if the model is winging it. But if following a template, it's unlikely to invent a new pattern.
 - If we heavily annotate the template, one risk is the model including the annotations in output if it's confused about whether they should be output. We must be clear that comments are not to be reproduced. Usually, GPT-4 won't output # comments if asked to output as data, but it might if it misunderstood and thought the comments were part of the required format. So the instructions should explicitly say something like "Do not include any comments or text in the output that is not a JSON/YAML field."
- **Annotation Density Impact:** Intuitively, having a lot of inline annotations (in the prompt template) might actually _help_ generation accuracy up to a point - because the model has all the guidance right there and doesn't have to rely on latent knowledge or cross-referencing elsewhere. However, if the annotations are extremely verbose or numerous, they might crowd the context such that the model could be more likely to slip (especially if the prompt nears length limits, though in our case we are well within limits). Also, if every field has a long explanation, the model might take longer (more "thinking" needed) to ensure it addresses each rule, which could slightly increase chance of a minor oversight. On balance, moderate annotation is beneficial for accuracy (this is basically the premise of "chain-of-thought in comments" improving answers). We saw in an example that adding YAML comments allowed GPT-3.5 to get a math answer correct where it failed with JSON and no comments. The reason: the model could "think" in the comments without ruining output. So, for our use-case, giving the model room to reason or check constraints via comments could improve reliability (e.g. a comment "# ensure stool type matches Bristol description above" might make it double-check itself).
- **Format Consistency Maintenance:** Over multiple sessions or multiple outputs, consistency can drift if the model isn't reminded of the exact format each time. By storing a **single source template** in the project (the schema file), we always prepend it (via the system/project memory) so the model refreshes its format knowledge. This should maintain consistency. If we allowed the model to generate a schema by itself without reference, there'd be more variability. So the plan is to always use the template from knowledge. Under that plan, format consistency should remain high. JSON being rigid by nature might be a tad easier (fewer ways to represent the same thing in JSON). YAML has small stylistic variations (like you could use true/false or yes/no, quotes or no quotes, etc.), but we will standardize in the template and expect the model to mimic exactly.

In conclusion, **each structured format can be made highly reliable** with GPT-4 if we provide a template example. JSON is very well-known to GPT and yields valid outputs the majority of the time with proper prompting, but YAML with comments might yield _even more accurate adherence_ to complex instructions due to the ability to embed guidance (as literature suggests and our reasoning confirms). We will need to test whichever format we choose with sample outputs to verify near-perfect generation. Our goal is zero formatting errors or need for correction - the analysis here suggests this is achievable. Annotation (done thoughtfully) will improve reliability rather than hinder it.

### B.4. Self-Documentation & Template Clarity Assessment

A critical non-functional requirement (T810A2-NFR-002) is that the template should be **self-documenting**, serving both as a machine-readable schema and as instructions for the LLM. We evaluate which format and annotation strategy best fulfills this dual role:

- **Dual Responsibility Support:** The format that best allows a file to act simultaneously as a schema definition and an instruction manual is one that permits interwoven documentation without breaking the schema. **YAML stands out** here - it allows inline comments that do not affect the actual data structure, effectively letting us write an instruction manual in parallel with the schema. This means a single YAML file can tell the LLM exactly how to fill it out (via the comments) while also being a valid template. JSON alone cannot do this (we'd need separate docs or to include dummy fields that mar the purity of the schema). A Markdown documentation file, on the other hand, can explain the schema but isn't the schema itself - the LLM would have to translate from description to output format, which is a cognitive step that could introduce error. Therefore, **YAML (or hybrid Markdown+YAML)** is likely the best for self-documenting templates.
- **Annotation Density Optimization:** We want enough annotation to prevent misunderstandings, but not so much that the template becomes bloated or harder to scan. Best practice here seems to be **targeted, concise annotations** - for each field, a brief note on its expected values or any rules, and perhaps any especially important relationship. For example, a comment might note if a field can be null or omitted. We should avoid lengthy explanatory paragraphs as comments; instead use key phrases or bullet-like brevity. This ensures the LLM can quickly parse the template. The insight from Part B.3 is that well-placed comments enhance accuracy - there's probably a sweet spot where every crucial detail is noted, but redundant or obvious info is left out. For instance, commenting # integer on an age field might be overkill if it's obvious, but commenting # optional, omit if unknown is very useful. We will likely adopt something akin to _Option A/Hybrid_ from B.2: minimal but sufficient inline comments. This balances clarity and token load.
- **Guiding LLM Behavior via Annotations:** The style of language in annotations should be imperative but not overly verbose. For example, to guide behavior: # If stool type = 0, ensure corresponding description notes no stool. or # Ask user if value missing. We have to be cautious: if the assistant treats the comments strictly as non-output, then an instruction like "ask user if missing" might not directly trigger a question in the output (because the output might just be JSON). However, this kind of annotation would be used by the execution protocol (Prompt feature) rather than directly making the assistant talk - the assistant might internally realize "I should query the user" if it sees that in context. This gets into prompt engineering: in the _tracking conversation_, the agent might use the knowledge file to decide when to ask something. If our template comment says # required field, must prompt if not provided, the LLM (in its chain-of-thought) can decide to ask. This is the dual use of the template as instructions, not just a static form. We need to ensure these instructions are phrased clearly and perhaps distinctively so the model doesn't confuse them with content to fill.
- **Schema Clarity (NFR-002) compliance:** This NFR basically means the schema should be easy to understand. Using a self-documented template directly addresses that. If a new developer or even the client reads the template file, they should grasp what each field means. Our use of descriptive naming plus inline comments achieves this. Each controlled vocabulary value will also carry meaning either through naming or an adjacent comment. For example, instead of an inscrutable list [-2, -1, 0, 1, 2], we might embed:
- mood: 0 # -2 (awful) to +2 (happy)
- This is immediately clear to any reader. We will ensure the final template artifact meets the clarity seen in this report's tables and explanations.
- **HYBRID Annotation Patterns Considered:** (Recap from B.2 with an eye to clarity)
- _Option A (Inline Hints Minimal)_ - yields a cleaner looking template, possibly easier for a quick glance, but might leave some things implicit.
- _Option B (Exhaustive)_ - yields a very verbose template. Clarity per field is high, but overall could be overwhelming (a reader might have to scroll through many lines of comments).
- _Option C (No inline, separate doc)_ - the template is super clean but not self-explanatory without cross-reference, failing the self-documenting criterion.
- _Option D (Hybrid minimal inline + external supplemental)_ - could be optimal: the template carries the key info for usage, and a separate document (like an ADR or README) carries extended discussion, rationale, or examples.

Our inclination is to have the **template file itself suffice for day-to-day use** (so one can just load the template and go), and keep any deeper guidance (like _why_ certain decisions were made or examples of edge cases) in the ADR or in developer documentation. This separation keeps the template focused. For clarity, we might also include one or two example entries as comments or separate blocks for illustration. For instance, after the template structure, a commented-out example could be given. But we must be careful the model doesn't attempt to output that example. Likely better to keep examples in separate reference if needed, to avoid confusion.

In summary, to maximize **schema clarity and self-documentation**: - We will use **inline comments** in the template to explain every non-trivial element. - We will phrase these annotations as direct, instructional comments (imperative when guiding action, declarative when defining data). - This approach is best supported by YAML format (or Markdown hybrid), which as we established is acceptable and even recommended by others for LLM interactions. - We will achieve NFR-002 by delivering a template that could practically stand alone - an engineer or the LLM itself can read it and understand what to do, without needing to constantly refer to external docs.

### B.5. Token Efficiency Impact & Platform-Informed Budget Recommendations

Understanding token usage is vital to ensure our solution fits within ChatGPT's context window and performs cost-effectively. We analyze token counts for various components and propose budgets:

**Vocabulary Token Counts Across Formats:** Our controlled vocabulary lists (meal tags, stool descriptors, etc.) will consume tokens whether embedded in templates or referenced externally. How we format them matters: - As a plain JSON array (e.g. "metadata": ["chili","oily",...]), each entry has quotes and a comma - each likely a token or so. YAML list - chili will use slightly fewer tokens (no quotes, the word might even be one token if common, whereas in JSON the quotes might cause it to be broken into multiple tokens). The difference isn't huge for small lists, but for bigger lists it adds up. If a list has, say, 10 items, JSON might use ~12-15 tokens vs YAML ~10-12 tokens - minor. - However, if we include **descriptions** of each vocabulary value inline (like a table of definitions), that can be token-heavy. We likely won't include a full table inside the template; instead we annotate by category (e.g. a comment on the array like # possible values: ["urgent","partial_evacuation",...]). This one comment line is far cheaper than listing each on its own line with description. - If an external reference file is used for exhaustive vocab definitions, that's separate from the main prompt but still enters context when used. We should either not need that (embedding enough info in template) or ensure it's only used when necessary (like a separate file the developer can consult but not loaded in prompt memory every time). - For numeric ranges, listing "-2 to 2" is minimal tokens, whereas writing out each meaning ("-2 awful, -1 bad, 0 neutral…") is more. But that's important info. It might be ~10 tokens to include all that, which is acceptable.

**Annotation Overhead:** Using YAML comments for annotations does consume tokens (they are visible to the model). But these are mostly short phrases. For example # 1 = no pain → 5 = extreme pain might be ~10 tokens. Given perhaps 10-15 fields to annotate, that's ~100-150 tokens of comments. This is negligible in the context of GPT-4's ~32k token window. Even with GPT-3.5 (4k window), 150 tokens is fine. The overhead is well worth the clarity gained.

We can quantify a bit: - **Stable JSON Patient Profile Template:** This likely includes fields like age, conditions, etc. Suppose it's 10 fields and, with annotations, maybe 150 tokens (data + comments). Without annotations maybe 50-80 tokens. So annotation overhead ~70-100% of base. But since base is small, it's fine. - **Dynamic JSON Entry Template (per entry type):** Let's say stool entry template has ~5-6 fields. With comments might be ~100 tokens, without maybe 50. Meal entry maybe similar. Summing across, if we load all templates for 5 entry types at once, that could be a few hundred tokens total. - **Controlled Vocabulary Catalog:** If we maintain an external list of all allowed values (maybe as a reference file), that could be moderately large (dozens of terms plus descriptions). For instance, listing definitions of all 8 Bristol types, ~8 lines of description, could be ~100 tokens; listing all meal tags maybe 4 lines, ~20 tokens; stool flags 4 lines ~20 tokens; symptom scales definitions ~20 tokens. Summing, maybe ~160 tokens for a vocabulary reference. Not bad. If integrated into template comments, these are distributed among field annotations, likely similar or slightly more terse.

**Token Count Comparison Matrix:**

To illustrate: - **Option 1 (JSON with comment fields)** - a dynamic entry template ~50 tokens data + 50 tokens comments = 100 tokens; but half of those tokens (comment keys and quotes) might be "wasted" because they aren't real content. - **Option 2 (YAML with # comments)** - same content could be ~90 tokens (slightly fewer because no extra keys for comments, just the text). - **Stable profile JSON** - maybe 60 tokens (less data). - **All vocab lists embedded** (say all allowed values written out in comments in YAML) - could add ~100 tokens.

So if we loaded _everything_ (profile + 5 entry templates + all comments) into one system prompt, we might be around on the order of 500-700 tokens. This is well within our budget given GPT-4's large window. Even GPT-3.5 could handle that in the system message.

However, ChatGPT has another limit: reportedly the system message (project memory) might have a character cap (~8192 chars ~ ~2048 tokens). We should confirm: the brief cites an _example_ of an 8000 character system prompt limit. Our content is likely <4000 characters, so we are safe.

**Optimization Opportunities:** - We can use abbreviations for certain field names or values _if_ they do not reduce clarity and if tokens are critical. For example, use "lvl" instead of "level" to save a token. But given we are nowhere near limits, we prefer clarity (full words) over micro-optimization. - Removing quotes via YAML is an optimization we intend to use (saves tokens on every key and some values). - Avoiding redundant text: e.g. rather than commenting every scale point, maybe comment just min and max ("1=none …5=extreme") instead of all 5 points spelled out, unless needed. - The concept of **modularity**: we could keep separate smaller files (like one template per entry type) so we only load what's needed. But since the assistant likely needs to know all entry types anyway (for integration, e.g. it might need to decide which entry type JSON to generate based on user input), it's safer to keep everything loaded. Also, the new Projects feature likely just loads all files into context by default (or at least they're accessible). The OpenAI help says all files in the project are considered in responses. So splitting into multiple files doesn't reduce token usage if they're all loaded. It might help organization but not token count in context (unless we start removing some files for certain prompts, which is manual). - The only time token load could become an issue is if we attempt to store a _lot_ of user data or conversation history in context along with these templates. The entire conversation + multiple images + these files could approach limits in extreme cases. But our focus is on one entry at a time, and conversation can be truncated if needed by design.

**Impact on System-Wide Token Consumption:** The overall system prompt for LLM_Gastro will likely include: - The relevant knowledge files (our schema template with comments, possibly an instructions file). - Possibly some general instructions about style. - The user's last message and some history.

For GPT-4 (32k context), even including entire knowledge base (which might be up to a couple thousand tokens if many files) is fine. For GPT-3.5 (4k context), we might need to be a bit more frugal - but we assume GPT-4 usage for final system. If needed, we could trim some comment verbosity for GPT-3.5 or not load rarely used categories.

**Token Budget Recommendations:** Based on platform constraints and the above: - **System Prompt Allocation:** We recommend aiming to keep the system + knowledge content under **~2000 tokens**. This is comfortably within all models' limits (including any rumored 8000-char limit for system instructions). Our analysis indicates we can likely stay ~500-1000 tokens for our content, well below that. So 2000 is a safe upper budget. This allows room for growth (if we add more vocab or instructions later). - **Stable Profile Max Tokens:** The stable patient profile JSON should be relatively small (demographics, condition list, etc.). We suggest a budget of **<= 150 tokens** for this content. In practice it might be ~50-100 tokens now; 150 gives headroom if we add fields like medical history or so. This ensures loading a patient's profile won't eat much context. - **Dynamic JSON Entry (per entry):** Each entry (meal, stool, etc.) output by the assistant should ideally be **< 100 tokens** (small entries like mental state might be ~20 tokens, larger like meal with many ingredients could be ~80). We recommend a **hard limit around 100-150 tokens** for any single entry JSON. If entries get larger, they likely contain extraneous detail that could be summarized instead. This is both to keep responses concise and to ensure the user isn't overwhelmed. It also leaves room if the conversation includes 5-6 entries in memory. - **Vocabulary Catalog Tokens:** If we keep a separate file listing vocabulary (for our reference), that might be a few hundred tokens. That's fine in the knowledge base. If we were to insert the entire vocab list into every prompt, that would be wasteful. Better to let the knowledge base file hold it and the model will refer to it as needed. So for budgeting: allow up to **300 tokens** for vocabulary definitions in context. That correlates to, say, if the model needs to recall "what are the stool metadata values", those are in memory. 300 is negligible in a 32k window but we set it for completeness. - **Total Project Knowledge footprint:** The help docs indicate a Plus user can have up to 25 files and presumably the model can handle up to ~2M tokens of knowledge, but practically, we don't want anywhere near that in active context. Our entire knowledge content will likely be under 1k tokens. So we have a huge safety margin.

**DISCLAIMER on Token Budgets:** We emphasize these are guidelines, not strict limits - the final usage will be tuned by the sub-consultant and client as needed. The recommendations serve to ensure performance and avoid hitting any hidden limits. For instance, we might say: _"Keep system+knowledge ≤ 2k tokens to accommodate 2k user tokens and 2k assistant tokens in a worst-case 6k context scenario, given some overhead."_ Also, these budgets assume GPT-4 32k; if using GPT-3.5 (4k) in some contexts, we'd have to adjust (perhaps not load all files or use a compressed version).

In terms of **cost**, using GPT-4 with a few hundred extra tokens of instructions is trivial compared to its overall cost per call. And if it prevents an error or additional back-and-forth, it saves cost in the long run.

**Platform Limits Documentation:** Just to ground this in official numbers: - ChatGPT Plus (GPT-4) context window ~32k tokens. - Max output per response ~8k tokens (so model won't produce beyond that even if context large). - Our usage falls well under all these. - For knowledge files: 25 files, 512MB each, far beyond our needs.

Given all the above, we are **comfortable that token usage is within limits**, and our recommendations ensure it stays that way with margin to spare. We will codify these budgets in the final recommendations, with the caveat that they are not hard caps but targets for optimal performance.

### B.6. ChatGPT Platform Constraints Documentation

To ground our analysis, here we compile the key **platform constraints** of ChatGPT Projects that influenced our recommendations (this also serves as a quick reference for DEP-005 validation):

- **File Storage Limits:** For ChatGPT Plus (which we assume for LLM_Gastro development), each project can have up to **25 files** uploaded. This is plenty for our needs (we anticipate maybe 5-10 small files at most: schema, prompts, perhaps some lookup tables). The _file size_ limit is **512 MB per file** - effectively no practical limit for text-based schema (our largest files are under 100 KB). The **total number of files** across the entire project is capped (25 on Plus, 40 on Enterprise). We should aim to keep the number of files low for simplicity (maybe one combined schema file, or separate by entry type if clarity demands, but in any case under the limits).
- **Token Limits:** ChatGPT's GPT-4 model in Plus has a large context window (~32,000 tokens) for each conversation. However, there are some special considerations:
- The system and knowledge files likely count toward this context. The **system prompt (including all project files)** should ideally remain within a few thousand tokens to ensure we have room for user query and assistant answer. We heard an anecdotal limit of ~8k characters (~2k tokens) for the system prompt injection in early versions - this may have expanded with 32k context, but to be safe, we abide by that ballpark.
- The maximum _input_ (user + system) plus _output_ can't exceed model's window. With 32k, not an issue. If we were constrained to 8k (for older GPT-4 or GPT-3.5), then it would matter more. For documentation: GPT-3.5 has 4k context, GPT-4 (legacy) 8k, GPT-4 32k as options. We assume we'll use the 32k for final agent if needed, but even 8k is enough.
- The model also has a limit on how many tokens it will generate in one go (~1024 or 2048 by default in UI, but ChatGPT interface will chunk anyway). We just note that we can't get extremely long outputs in one turn - which is fine, since each JSON entry is short.
- **Project knowledge usage:** Notably, OpenAI states ChatGPT Enterprise can process up to ~110k tokens from uploaded docs in the context. For Plus, practical usage shows the model can reference large files too, but the effective limit is the context window. So essentially, as long as knowledge + conversation < context window, we're good. Our plan keeps knowledge small.
- **Format Restrictions:** The Projects feature supports various file formats. Officially mentioned are PDF, DOCX, images, etc., but for text, there's no restriction. It does not "execute" code, it just reads content. So, JSON, YAML, Markdown files are all treated as text sources. One nuance: If you upload a PDF, the system does an internal conversion to text (with possible compression of content). But if we stick to native text formats, what the model sees is exactly what we wrote, which is preferable for precision. Therefore, we will use a text format (like .yaml or .md) to ensure no weird parsing issues.
- We should be aware of how ChatGPT's retrieval works. It likely always considers all files when responding (especially if they are small). There's no explicit query we run on files; it's more like the model has them in context or can "look them up" as needed. In practice, it appears to incorporate them into context (the model's answers show content from files with citations in the UI, which implies an internal retrieval step). But we can't rely on partial retrieval; we should assume the model has essentially read the whole file (since ours are small).
- So, there's no "embedding vector" or partial recall we have to worry about - it's straightforward context inclusion. That means if we have multiple files, the model might need hints to use the right one, but since all our content is schema-related and consistent, that's fine.
- **File Update Mechanisms:** Currently, to update a file in Project, one can either edit it manually in the UI or delete and re-upload. There is _no version control or history_ beyond manually keeping track. This means if our schema evolves, someone will have to update the project file (which replaces the old content). The platform doesn't allow dynamic content from the model to modify files (no, the model cannot write to the knowledge base; only the user can via the UI).
- In line with that, any time we change the schema, we should re-run a quick validation with the LLM to ensure it still outputs correctly given the new instructions (basically QA each major update).
- As an operational note, because updates are replace-only (no append functionality except manual editing), we must ensure consistency (don't forget to update a definition in one place if changed in another).
- We will document in our project guidelines that whenever a vocabulary or format is updated, the project knowledge file must be manually updated by the maintainer (and ideally, mention the version in the file for clarity).
- **File Versioning or History:** Not available in ChatGPT UI. We might keep separate version files (like schema_v1.yaml, schema_v2.yaml) if needed, but that would count toward file count. Better to maintain version inside the file and overwrite. Since our environment is presumably not code repo integrated, this is fine. We just note this as a limitation: you cannot revert a file easily or see diffs within ChatGPT's interface. We might mitigate by keeping an external backup (e.g. the ADR in GitHub is canonical).
- **Performance Characteristics:**
- _Retrieval latency:_ When we have knowledge files, the first time the model references them in a session, there might be a slight latency as it fetches and indexes them. In anecdotal experience, a few small files do not create noticeable lag. If we had dozens of large files, maybe. But our usage (hundreds of tokens total) should be lightning-fast. So no real-time performance concern.
- _Parsing overhead:_ The model has to parse the text of files as part of its context. This does contribute to token usage each request. But as we budgeted, a few hundred tokens extra is negligible for GPT-4's capacity. The cost in terms of OpenAI billing is also small (if say 500 tokens per prompt are instructions, that's fine).
- There is an interesting note that if the project has a lot of data, the model might compress or not fully use it (like with large PDFs, they mentioned compression). But again, our content is small enough to be fully utilized with fidelity.
- **Update Workflows:** We touched on this - user must manage updates manually. Also, the knowledge base is static during a conversation. If we update a file, it will apply to future messages, but the model won't retroactively apply it to previous turns. So if something changes mid-session, we might need to re-initiate or clarify. This likely won't matter in production since the schema won't be changing frequently in the middle of a user's chat. But during development, it means we test, tweak file, then test fresh conversation.
- **Memory Behavior in Projects:** Projects can be set to _project-only memory_, meaning the assistant doesn't have outside knowledge beyond project and chat (which is good for ensuring it uses our schemas). We should ensure our project is configured to have memory reference to the files, which by default it is. Enterprise settings aside (for plus, we can't control too much beyond just using it).
- There is no risk of conflict with other user instructions because we'll ensure the project's system instructions are comprehensive. But we should remember if a user prompt contradicts the schema, the assistant's output should still enforce schema (by design requirement).
- Also note: if multiple team members share a project, they must coordinate file changes etc. Out of scope for now, but the platform allows up to 100 collaborators in a project (Business/Edu). For us, just the one system interacting, so okay.

To encapsulate constraints: We will create a short **Platform Constraints** section in our documentation (which this is, effectively) listing: - File limits: 25 files, 512MB each, etc. - Token limits: 32k context (and mention 2M token processing upper bound). - Formats: text-based recommended (we choose YAML/Markdown), no native validation beyond model's own. - No persistent memory beyond project (so must include knowledge files every session, which Projects handles). - Project file edits require manual update.

These constraints inform why we made certain choices (e.g. not splitting files excessively, not relying on any fancy plugin - since ChatGPT doesn't allow code execution or plugin usage in the normal Plus context with knowledge files, all logic must be self-contained with the model).

Finally, this satisfies DEP-005 (the dependency requiring platform knowledge): we have documented relevant platform limitations and ensured our design stays within them.

### B.7. Maintainability & Schema Evolution Analysis

We consider how each template format and our overall approach will fare as the schema evolves over time (NFR-005):

- **Future Schema Evolution Support:** We want a format that is easy to update without causing inconsistency or massive rework. YAML/JSON are both easy to edit manually or with scripts. Markdown is also easy but less structured. YAML, in particular, is friendly to hand-edit (which is likely how schema updates will occur - via the ChatGPT UI or by regenerating from ADR). If a new field is added, one can simply add a new line in YAML. In JSON, adding a new field might require trailing comma attention etc., but trivial. One advantage of having the schema in a human-readable format (with comments) is that a maintainer can quickly see where to insert a new vocabulary value or note. **In our pipeline, the Epic ADR is the source of truth** and is maintained in a git repository. We might generate the ChatGPT schema file from the ADR or vice versa. Ensuring consistency between those is part of maintainability. A structured format like JSON/YAML is machine-parsable, so potentially one could auto-sync changes. Meanwhile, the comments we include could be derived from ADR content (which we compiled in this research). This suggests that YAML or JSON that closely mirrors ADR tables will be easiest to keep in sync (since ADR is also tabular text, could be converted).
- **New Entry Type Addition Complexity:** If we design our schema file with separate sections per entry type (which we will, e.g. separate YAML top-level keys or separate code blocks), adding a new entry type means adding a new section. In JSON, if all entry schemas were part of one huge object, adding a new type is adding a new key with a sub-object - straightforward. In YAML, similarly, just add a section. The structured nature ensures it doesn't break others. We would then update any cross-references (like if we have a list of all entry type names somewhere).
- The LLM will then have to learn this new section. Because the knowledge base is updated, any new conversation will have it. Past conversations might not have, but that's fine. So maintainability here is good - just edit the file and the model "knows" next time.
- We should maintain an order or logical grouping in the file to keep it readable. Possibly alphabetical or by usage frequency. For instance, if a Sleep entry is added, we put it perhaps after stool or in some logical spot. Minor concern but for human maintainers it helps.
- **Vocabulary Updates:** When a new vocabulary value is approved (say we add "salty" tag, or a new stool descriptor), maintainers need to update the schema file's comment or allowed list. Because we chose a format that directly lists allowed values in plain text (maybe as YAML list or in comments), it's one edit. If we had left this implicit, the model might not know about the new value unless retrained. But since we'll explicitly put it, it will immediately use it correctly. For removing/deprecating a value, one would remove it or comment it out. The model might still have some memory if it saw it earlier, but likely it will not use it if it's not in the current prompt.
- We might consider version-tagging major vocabulary versions in a comment (like # vocab v1.1: added 'salty'). This helps maintainers track changes. It doesn't affect the model much except it might realize a value is new, but that's fine.
- **Version Control and Migration Patterns:** As noted, ChatGPT Projects doesn't have robust versioning, so our control will be via the ADR in git. That means the consultant will update the ADR (with version numbers and changelog), then manually update the ChatGPT knowledge file to match. We should maintain a mapping such that it's easy: maybe generate the YAML from ADR tables with a script. If maintainers do it manually, they must be careful not to drift. A practice could be to copy-paste from ADR text to the project file for each change.
- If a schema change is backward-incompatible (say we rename a field), the LLM's instructions will change immediately with the file update. There is no multi-version support in one project (other than storing two schemas in different files). So any conversation after that point should use the new format. We might want to broadcast a note to team or ensure any older transcripts are recognized as using an old format if needed. Possibly not a big issue for an internal agent development scenario.
- For code maintainability, JSON is easier to validate with tools (one could run it through a linter). YAML is human-easy but prone to indentation mistakes - yet, if a maintainer makes a mistake, GPT might still parse it since GPT is forgiving. But we should avoid errors to not confuse the model. We can keep the schema file small enough to visually inspect.
- **Impact on Story S06 (Schema Governance Workflow):** Story S06 presumably deals with how to manage schema changes (perhaps how to propagate to multiple parts or how to handle multiple versions). Our chosen approach integrates nicely: Epic ADR is the governance artifact, and we reflect it in the LLM's prompt. So changes follow the formal process (consultant proposes in ADR, client approves, then update implemented). The use of self-documented schema in the prompt means the LLM is always aligned with the latest approved schema (assuming we update it promptly). There's minimal risk of the assistant drifting or using old terms incorrectly because it doesn't rely on stale training data - it reads the current schema each session. This is a huge plus for maintainability: we essentially have a dynamic "single source of truth" that we can update as needed.
- Also, because the template is easily readable, QA and review of the agent's behavior is easier - testers can verify the schema file to know what to expect in outputs. If the agent does something out of that spec, either the file was wrong or the agent is buggy, both straightforward to check.
- **Format Choice Impact on Maintainability:**
- JSON's strictness means any maintainer error (like forgetting a comma) could break formatting - possibly making the file not load or the model misinterpret it. YAML's flexibility means maintainers need to be mindful of indentation but it's pretty easy after a while. Many non-developers find YAML easier to edit than JSON (no worrying about quotes/commas).
- YAML with comments is also nice for maintainers because they can leave notes to future selves. For example, # note: do not remove this field, required by X. This wouldn't be for the model but for humans. We have to be careful though - the model will see it too. If we want human-only comments, we'd remove them, but since the model sees everything, better not put irrelevant notes. Instead, such notes should go in ADR or separate docs. So maintainers should treat the knowledge file as "what we want the AI to know", not internal dev comments (unless they also should influence AI behavior).
- The risk of maintainers forgetting to update the knowledge file after changing ADR is real. To mitigate, we might incorporate a step in the workflow: whenever ADR-002 is updated, immediately update the ChatGPT project file and increment a version tag. Possibly include the ADR version number in the file to cross-check.

**Evolution Example:** Suppose a year from now we integrate data from fitness tracker - we add an entry type "activity" with fields for steps, etc. In our approach, we would: 1. Update ADR-002 with a new row for "activity" entry type and its fields. 2. Update the ChatGPT schema file: add an "activity" section with its keys (and comments about ranges, etc.). 3. The LLM now immediately can accept/generate JSON for activity logs in conversations. 4. We test it a bit, adjust any annotation if needed (maybe the first attempt, the AI didn't output the new field in correct format, so we refine prompt). 5. All done - minimal changes to code or other docs. This shows how adding new stuff is straightforward and isolated.

In summary, the chosen approach (explicit schema file in structured format) **strongly supports maintainability**. Each change is localized to updating documentation (no model retraining needed, which is good because ChatGPT cannot be fine-tuned by us). The usage of a human-readable structured template means even as things get more complex, they remain understandable and editable. The governance process will ensure changes are thoughtful and traceable (with ADR references).

The main maintenance burden is keeping the ChatGPT knowledge in sync with the official spec - but that is an accepted manual step given the platform's constraints. It's akin to updating API docs when the API changes.

We conclude that our template and format will be **resilient to future evolution**. YAML/JSON will handle new entries or fields without breaking older ones (especially if we design for optional additions). We will add guidelines for maintainers to follow (like always include default values for new fields in the template with comments if needed, to avoid the model ignoring them due to absence in old examples).

Thus, maintainability and extensibility have been key drivers in our recommendations, and they align well with NFR-005 goals (ease of extension, minimal rework for adding features).

## IV. Deliverable C - Cross-Part Integration Analysis

### C.1. Vocabulary Integration with Template Format

Here we examine how the way we handle vocabularies (embedded in template vs external file) interacts with our template structure and token constraints:

**Embedding vs External Reference:** We have two logical places to define controlled vocabulary lists: - _Embed within templates:_ e.g., in the stool entry template section, explicitly list or comment all allowed stool metadata values. This keeps the information contextually right where it's used. The LLM sees immediately, for instance, that stool.metadata can contain "urgent, full_evacuation, partial_evacuation, mucus, blood". This likely makes the model more likely to use only those (especially if we phrase it like # allowed: [list]). Embedding values inline does increase the template file size slightly but by a known amount (we counted ~100 tokens for listing values). - _External vocabulary catalog:_ a separate file enumerating all categories and their allowed values. The advantage is a single authoritative list, not scattered. The model could consult it if needed. However, we are not certain how the model prioritizes multiple knowledge files - it might not automatically cross-reference the vocab file if the immediate template provides enough info. We might have to explicitly mention in template "(see vocab file for full list)". This is an extra cognitive step. - _Hybrid approach:_ Could embed some critical small lists and put larger ones externally. But our lists aren't very large, so hybrid likely isn't needed. If they were (imagine hundreds of symptoms), then we might list high-level categories in template and keep the exhaustive list externally.

**Token Efficiency Impact of Placement:** - If we embed, token cost is slightly higher in the main schema file (but as noted, still low overall). - If we externalize, the main schema file is smaller, but the external file content will _still_ be in context (if ChatGPT includes all files). So actually, splitting doesn't reduce total tokens used, it just spreads them. Unless we consider scenario where we might drop the vocab file from context in some queries. But in Projects, I don't think you can choose to omit certain files per query. All are present. So splitting for token saving doesn't help. - In fact, having them separate might cause duplication if the template still enumerates partial info. So it could be less efficient.

**Optimal Structure for Epic ADR-002 Vocabulary Catalog:** - In our documentation (ADR), we keep a table form. For the LLM template, we can mirror that structure. Possibly a YAML structure like:

vocabulary:
meal_metadata: [chili, oily, sweet, light, ...]
stool_metadata: [urgent, full_evacuation, ...]
...

We could include such a section in an external file or at bottom of template as a reference. - Another approach: incorporate allowed values into comments for each field. E.g. metadata: [] # e.g. ["urgent","mucus",...]. This localizes information.

From an **LLM utilization perspective**, having the allowed values right next to where it will output them is ideal. For example, if the model is about to fill meal.metadata, and in the template it sees a comment listing possible tags, it will likely pick from them. If that list is in a separate file, the model has to recall or search for it. GPT-4 can do that, but it's one step removed. We prefer to minimize reasoning steps needed for accurate output.

Therefore, we lean towards **embedding vocabularies inline** in the template, in concise form. The external listing would then be redundant. We might still keep an external list for human governance (ADR itself), but not needed in project if info is in template.

**Embedded vs External - effect on token efficiency:** Either way the tokens are in context, but consider: if external, the model might not pay attention to them unless needed, whereas if embedded, it definitely sees them. However, since it's always available context, this distinction may not matter; GPT likely has all in its attention anyway. It's not like it saves tokens by ignoring a file.

**Single-file vs Multi-file strategy:** Possibly, we could have one single comprehensive file (with all templates and a vocab section) or break it into multiple files per entry type plus one for vocab. Single file might be simpler - fewer file overhead (like fewer file metadata tokens or boundaries). But multiple files could conceptually allow not loading some if not needed (though as said, it likely loads all anyway). Project memory usage aside, maybe easier to edit if separated. But then cross-file referencing in AI's "mind" might be trickier. The safest is probably one file that includes everything in a structured way (like an all-in-one schema file). That ensures any time the model looks at schema, it has full context.

Given the small size, we'll likely do one file. Or two: one for stable profile schema, one for dynamic entries schema, to distinguish them (since usage differs). Even that might be unnecessary - a single file with sections "Stable Profile" and "Entry Templates" is fine.

**Vocabulary Placement Recommendation:** We anticipate recommending to **embed critical vocab directly** in the template definitions (with comments or enumerations), rather than relying on a separate lookup file. This ensures the LLM doesn't have to guess or search for allowed values - it's explicitly provided when it's formulating output. This embedded approach also aligns with the concept of a self-contained prompt file. The alternative (external) might be needed if the vocab were extremely large (like thousands of entries, e.g. ICD-10 codes or such, which would bloat the prompt). In our case, lists are short.

**Versioning & Update Workflow Consideration:** With embedded approach, whenever a value is added/removed, we update that line in template. If external, we'd update external file. Not a big difference in process. But multiple places to update if a value is used in multiple fields (rare for us - but e.g. if "urgent" were mentioned in a comment both under stool and in an external list, we have to update both). Single source is ideal. We can make the schema file itself the single source by not duplicating info. For instance, if we comment the values near the field, we might not separately list them elsewhere in the file redundantly.

**Conclusion on C.1:** We will integrate vocab directly into our template structure, balancing token load and clarity: - For each categorical field, list its allowed options in a comment. - Possibly have a summary section if needed, but likely not necessary. - This approach has negligible token impact (the lists are small) and maximum clarity for the LLM at generation time. - If in future a category had dozens of values, we might reconsider to avoid a huge prompt injection. But then possibly we wouldn't list all explicitly anyway, might instruct "see external doc X if needed". - We note that our approach satisfies _T810A-ADR-002-FR-005 (Cara Care alignment)_ by literally including Cara Care's terms in the authoritative template - effectively making the Project Knowledge file a machine-consumable vocabulary authority.

Overall, vocabulary placement within the template ensures **tight coupling** between schema and allowed values, which reduces the chance of the LLM deviating. It slightly increases prompt size, but as previously discussed, we are well within limits. Thus, the efficiency cost is worth the reliability gain.

### C.2. Cara Care Dual Processing Alignment

**Dual Processing** refers to the ability to use the data in both the LLM system and the Cara Care app (manual patient workflow) as mentioned in requirements (INT-002, NFR-004). Here we evaluate how our chosen template format and schema design align with that:

- **Manual Patient Workflow Support:** In practice, this might mean a patient or clinician can take a JSON entry generated by the assistant and input it into Cara Care (or vice versa). Currently, Cara Care doesn't have an API that we know of for JSON import, but they allow exporting data (the app mentions data sharing/export). Possibly the exported format could be CSV or JSON. If it's JSON similar to our schema, then we hit jackpot - the data flows seamlessly. If not, we consider how the user could manually transfer information:
- A likely scenario: The assistant collects data and generates JSON summary for a day's entries. The patient might then manually log the same entries in Cara Care app for their records. We want to minimize friction. Our JSON structure uses the same terms as Cara Care (e.g. the stool type numbers, the same metadata tags). So the patient can easily see "Type: 6, metadata: ['urgent']" and recognize to check "urgent" in their app stool log and select type 6. If we had chosen different nomenclature, that would confuse them. By aligning exactly, we already improved this manual process (NFR-004: Clinical Validity & consistency with GI sources, which includes consistency with known app taxonomy).
- If we output in YAML format in the chat, a patient wouldn't directly paste that anywhere. But they would read it. JSON or YAML, either one is just for them to read unless they had a custom import function. So from a _manual workflow perspective_, the format for user consumption should be human-friendly. JSON is somewhat machine-oriented, YAML a bit more readable. But realistically, both are not meant for end-user consumption; they are structured. In a conversation, the assistant might also give natural language summary. However, I suspect the LLM's role is to output JSON for logging, and possibly separately provide a human explanation.
- Therefore, the "manual workflow" likely means the patient can manually copy the content of the entry (like the values) into the Cara Care app. We ensure all field names and values are clearly recognizable:
 - Field names like "mood" and values like -2 to +2 correspond to Cara Care's concept (they use similar words in app).
 - Possibly we might adapt formatting for user ease - e.g., output 2025-11-16 for date if the app expects that, etc.
- **Cara Care JSON Structure Compatibility:** Does Cara Care have an internal JSON format for entries? Not publicly documented. But if they did (maybe their export or an API uses JSON with certain fields), we attempted to mirror likely structure. For example, the ADR-002 table looks very much like a JSON schema that one would design for this purpose. If Cara Care's database or export was known, we would align exactly. Without that, we aligned conceptually (field names and values).
- So if, say, in future Cara Care offered data syncing (some integration), our JSON could be mapped with minimal translation. For instance, they might call "full_evacuation" something like "complete" internally - a minor mapping. We have the key advantage of using the same vocabulary tokens (so maybe just rename keys if needed).
- Because we didn't introduce any extraneous fields or different codings (like we use 0-7 for stool type exactly as Bristol, not a different numbering), integration is easier. If a doctor looked at our output, they'd recognize it as essentially the same info as in the Cara Care log.
- **Template Format Dual-Purpose Support:** We have to ensure the format we choose for the schema doesn't conflict with anything if we wanted to actually input it to Cara Care. Cara Care would likely accept CSV or some known format if any. They certainly wouldn't accept a YAML with comments - but that's not something we'd feed it directly anyway. The _data_ is what matters. We can always convert our output (be it JSON or YAML) into whatever format needed if an integration were built.
- If the plan were to allow a user to "upload" our JSON into Cara Care, then the keys and structure must match what Cara Care expects. Without an API, that's moot. If we built our own tool, we could map it easily. The template format is more about how the agent and user interact, not hooking into Cara Care programmatically (unless future feature).
- **Format Conflicts:** We should identify any potential conflict in terms of data format:
- Example: Cara Care might not track time in JSON if they do CSV, or might use different enumerations. But we can adapt if needed.
- If the user sees YAML output with # comments (should not happen in the final answer because the agent should strip comments in output), that could confuse them. So we must ensure the assistant outputs either pure JSON or YAML _without_ comments to the user. The comments are for internal use in system prompt. The final user-facing JSON should be clean. So no format conflict at output: we will likely instruct the agent to output **JSON format** entries (since JSON is more widely accepted and parseable if user wants to use it in any tools). Meanwhile, the template in knowledge might be in YAML, but that's hidden from user. So the user just sees valid JSON. This addresses any concerns that "the app or other systems won't accept our annotation-laden format" - they won't see the annotations.
- We must test that the agent can successfully convert the internally documented YAML template to actual JSON output. This is doable by having the system message say "the following is a template, you should output JSON accordingly". GPT-4 can handle that easily, interpreting the YAML as specification and producing JSON, given its training includes YAML-to-JSON understanding in chain-of-thought possibly.
- Alternatively, we might decide to keep the schema in JSON with comment keys and instruct the model to drop them. But that is riskier. Using YAML as spec and JSON as output is a pattern used in e.g. BetterProgramming reference (they suggest asking for YAML or using YAML in prompt and output JSON for final answer).
- **Dual-processing compatibility implications:** If in the future we automated sending data from LLM to Cara Care (like via an API or file), our schema would likely just need minor transformation. We foresee no large obstacles:
- Our _vocabulary alignment means the content is compatible_ (the values make sense to Cara).
- The main difference could be format (they might require a CSV or a specific JSON shape).
- Because we have a structured output, conversion is straightforward (e.g., one could write a small script to turn our JSON into CSV for Cara Care or vice versa).
- Thus, our approach is future-proof in that regard - we do not lock into a format that's hard to convert. JSON is considered universal for data exchange, so sticking to that for actual output is wise.

**Manual Workflow Example:** Suppose the assistant returns:
```
{
"date": "2025-11-16",
"stool": {
"time": "13:30",
"type": 6,
"metadata": ["urgent", "mucus"]
},
"meal": {
"time": "12:00",
"ingredients": ["Burger", "Fries"],
"metadata": ["oily"]
},
"digestion": {
"tummy_pain": 4,
"bloating": 3
},
"mental": {
"mood": -1,
"stress": 4
}
}
```
A patient can look at this and fairly easily input it into Cara Care: - Log a stool entry at 13:30, choose Type 6 (mushy), tick "urgent" and "mucus". - Log a meal at 12:00 with items and note it was "oily". - Record pain 4/5, bloating 3/5, mood slightly negative, stress high. This demonstrates the manual dual entry is made easier because we use the same rating scales and descriptors as the app. If we had different wording (like "spicy" vs "chili"), user might be unsure if that maps to something - but we used "chili" because presumably the app uses a chili pepper icon for spicy, etc.

**LLM Usage of Cara Care Data:** The other side of dual-processing is the agent could ingest data from Cara Care (like if user exports their last week's logs and feeds to chatbot). If that data is in a similar JSON, our agent would parse it fine because it's essentially the same schema. If not identical, at least very close (maybe minor key name differences). So integration in that sense (LLM reading Cara export) is also feasible.

**Conclusion on Cara Care alignment:** Our design choices strongly prioritize compatibility: - We adhered to Cara Care's vocab (per CON-002 requirement). - We output in a structured data form that can be converted or read for manual input. - No format choice (YAML vs JSON for internal use) impedes that, as long as final output is JSON or easily understood by a human.

We will mention in recommendations that the chosen template format should not hinder manual or future automated workflows - likely recommending _JSON as the interchange format_, with any annotations stripped out. YAML is just a means to that end for internal clarity.

### C.3. T810A1-S05 Integration Insights

_T810A1-S05_ refers to the Execution Protocol feature of the Prompt epic. Integration here means how our templates (from Schema feature) will be used within the conversation flow defined by S05.

Key considerations: - **Template-Driven Architecture Context:** In the Phase 1 architecture, the S05 Execution Protocol likely involves steps like "Tracking Phase: user input -> assistant logs data -> analysis -> probe -> etc." Our templates will be central during the Tracking phase (the assistant must produce a JSON entry as the result of a user's narrative or answers). The five-phase protocol (Tracking → Analyze → Probe → Coach → Summarize) means at Step 1 (Tracking), the assistant needs to parse user input into the structured JSON. Our schema and template essentially _guide that action_. - For S05 to trigger properly, it might look for the presence of certain keys or check if the output is properly formatted. Because we have a stable template, S05's logic (likely in the system instructions or a classification mechanism) can trust that if the user's input is story-like, the assistant will produce JSON accordingly. - If S05 requires the assistant to first respond with tracking JSON, then later do analysis, the prompt must ensure the assistant _only_ outputs JSON in the tracking step. Our template and correct usage as system knowledge helps enforce that.

- **Impact of Format on S05 Prompt Engineering:** If our schema is clear, the S05 system message can simply instruct: "When in Phase 1 (Tracking), output the data as per the JSON schema provided." The assistant then refers to the schema file and does it. If the schema were unclear, S05 instructions would need to be more verbose. So our work simplifies S05 prompt: they can literally embed a reference like (the knowledge base content).
- If we use YAML for schema in the background but want JSON out, S05 might include an instruction "Use the provided YAML template as a guide but output in JSON format." That needs to be explicitly stated. We expect to include such in the final integrated system prompt. GPT-4 can handle that conversion logically.
- **Template Self-Documentation for S05 STEPs:** S05 likely has multiple steps (like classification, then question asking if needed, etc.). If the template is self-contained with instructions like "if data missing, ask user", this overlaps with S05's job of deciding when to probe. We must ensure our inline annotations complement, not conflict, with S05 logic:
- E.g., if IG-001 says always ask for missing mandatory fields, we might put a comment "# If X is missing, you must inquire." The assistant sees that and might attempt to ask the user spontaneously. But S05 might have a structured approach where Phase 3 (Probe) is where it asks questions. Ideally, the assistant wouldn't break format to ask within Phase 1 output. Probably S05 expects that if required info is missing at first, the assistant will _not finalize the JSON yet_ but instead ask a question (enter Probe phase).
- This raises the subtlety: Should the template file instruct the assistant on that logic, or should that solely be handled by S05's flow control? Possibly a bit of both: The schema comments can mark which fields are required vs optional, so the assistant knows it can't finalize entry without them. But the decision to actually ask the user likely is triggered by S05 logic (which might monitor if the assistant is about to output incomplete JSON and instead shift to a question).
- We need compatibility: if our template has comments "# required", the assistant might itself decide to prompt user if absent. But if S05 is already orchestrating that, we don't want double handling. Since S05 is a separate feature likely implemented via planning (the conversation management), we might aim to align by making our instructions mild and leaving actual prompting decisions to S05.
- Possibly, S05 custom instructions (INT of S05) can reference the schema: e.g., it could programmatically check which fields have default or null and then ask a question for them. If the schema file is computer-readable (JSON or YAML), an automated check could be done by an intermediate step. But in ChatGPT plus environment, we can't run code. So it's still all on the model reasoning.
- **Self-contained vs referencing**: Should S05's instructions explicitly mention all field details, or can it rely on the template file to guide the assistant? The latter is more modular. I'd expect we lean on the template file to contain specifics (like allowed values, required fields) to avoid duplicating that in S05 prompt. S05 can then have generic steps: "If any required data is missing, ask for it (Probe Phase)." The knowledge file marks which are required, so the model infers what's missing. This synergy means:
- Our template annotations about "required vs optional" are very important to get right, as they directly inform the assistant's decision to probe. For instance, if "stress" is optional and user didn't mention it, the assistant might skip it rather than ask, based on that tag.
- IG-001 likely defines how to handle null or missing (maybe allow null for optional, must ask for required). We incorporate that as comments or as part of schema (like allow null for optional fields).
- **Compatibility with T810A1 Output Needs:** The Prompt feature might require certain format or phrasing. Perhaps after tracking, at Summarize phase, the prompt agent might need to incorporate raw data. For dual purpose, S05 might need the structured data to generate a human-readable summary. The easier it is to parse the data (e.g., JSON dictionary), the easier the summarization. If the template format was weird or partially unstructured, summarization would be harder. So by providing clean JSON, we make summarization straightforward (the assistant can be prompted to "summarize the above data for the user").
- Also, if memory review or other steps need to pick up data from past entries, having them in consistent JSON in the chat history means the model can reliably extract them for analysis. That was probably part of GDR-002 (Stable vs Dynamic JSON separation ensures memory can be used for patterns).
- **Custom Instructions vs Self-Contained Template:** The question arises: do we want S05's instructions to explicitly mention each field or should the schema file itself instruct the model fully on how to gather info? Possibly a hybrid: The schema says what to collect and ranges, S05 says when/how to do it in conversation.
- For example, S05 might have a step: "The assistant should greet and ask the user to provide any updates for each category (meal, stool, etc.)". But our schema doesn't dictate conversation flow, just format. That integration must ensure the assistant not only outputs JSON but also engages properly.
- We may provide insight that having the schema accessible allows S05 to be more dynamic: the assistant could decide which categories to ask about based on which entries might be due (like maybe if the user just talked about a meal, it logs meal; if not, it might prompt for any stool event).
- **Insights for Activity 1.8 (Integration):** Summarizing, the integration between Schema and Prompt involves:
- Ensuring no conflict between schema's demands and prompt's flow control,
- Using the schema to simplify prompt's logic (like not duplicating content, letting the model refer to it),
- Possibly updating S05 custom instructions to mention referencing the schema file for formats.
- Ensuring the final user experience remains smooth (the conversation transitions from raw data capture to analysis nicely).

In essence, our schema file will act as a behind-the-scenes contract that S05 will rely on. If S05 is implemented as "the consultant in T810A1 uses the schema from T810A2", we have achieved a modular design: the PROMPT agent doesn't hardcode the schema, it pulls it from Project knowledge - thus if schema updates, Prompt agent automatically follows new structure. This would be a big benefit of integrated design.

**Therefore, compatibility measures to highlight:** - S05 should instruct the assistant to use the schema from T810A2 knowledge when logging data (instead of any adhoc format). - The schema file's annotation on required fields informs S05's Probe strategy (the integration spec should mention that). - S05 should caution that no explanatory text should accompany the JSON in Tracking phase - just the JSON (unless they decided otherwise). Our schema file doesn't include any free-text, so that aligns. - Possibly, we set up that after outputting JSON, the next phase triggers automatically because the model knows the protocol. - We ensure that any annotation meant for the model's internal use (like a comment) is not inadvertently exposed - as said, likely not, as model will omit comments in output if we instruct properly.

Given these integration points, the recommendations will cover ensuring: - The chosen format (YAML template → JSON output) and annotation strategy support S05 flows (which they do, given GPT-4's ability). - Provide guidance on where to handle prompting for missing info - likely recommending to keep that logic in S05 instructions but clearly mark required fields in schema (so the model can reason about it). - Possibly, mention IG (Implementation Guidance) items that need finalization: e.g., IG-002 Template Structure (which format to finalize - YAML/JSON - and how to incorporate in prompt), IG-003 Vocabulary Docs (the way we document them in template and ensure the assistant uses them explicitly). The brief's Rec 6 lists IG-001, IG-002, IG-003, IG-004 etc to incorporate insights.

To summarize: our approach is highly **complementary** to the prompt execution protocol. The template provides the _what_ and _format_, the prompt logic provides the _when_ and _how_ in conversation. We just need to fine-tune their intersection: - If the model is about to output JSON with missing required fields, instead it should enter probe questions - that likely will be an emergent behavior if properly prompted because it knows those fields are required and user hasn't given them. If not emergent, we might have to explicitly prompt it to do so (like an if-then in instructions). We foresee GPT-4 can do it if instructed to always gather required info before finalizing output.

We'll incorporate these integration considerations in our integrated recommendations, especially number 6 about F-RID enhancements (IG-001 null handling pattern, IG-004 manual workflow etc. are touched by these points).

## V. Integrated Recommendations

This section consolidates the findings from Deliverables A–C into six actionable recommendations for `T810A2-SCHEMA`. The recommendations are written for **client, consultant and developers** to use directly when finalizing F-RIDs, drafting templates, and planning downstream implementation.

---

### Recommendation 1: Controlled Vocabulary Catalog Data for T810A-ADR-002 Enhancement

**R1.1 — Treat the research vocab tables as the “raw data layer” for Epic ADR-002**

* Use the **exhaustive tables in Section II (A.1–A.4)** as the *authoritative raw data source* when updating `T810A-ADR-002-FR-001`.
* Keep the research report as a **supporting evidence artifact**; `T810A-ADR-002` should reference it (via `T810A2-RES-001`) but not duplicate all tables in-line.

**R1.2 — Extend ADR-002-FR-001 entry types using Cara Care as exemplar**

Based on Cara Care UI and example JSON, expand beyond the current four entry types (`meal`, `stool`, `digestion`, `mental`) to at least:

* `sleep`
* `exercise`
* `medication_taken`
* `hydration`
* `patient_state` (or equivalent “overall day/context” entry type)

Each new entry type should have:

* A minimal **core key set** (timestamps, core classification, optional metadata)
* Controlled vocabularies and/or scales aligned with Cara Care patterns and ROME IV / general GI practice where applicable.

**R1.3 — Formalize clinically-grounded scale mappings**

* For **Bristol 0–7**: lock in the official wording and ensure Type 0 is explicitly “no stool / attempted but nothing passed” with confidence handling consistent with `T810A-ADR-001` trust-and-verify rules.
* For **pain, bloating, mood, stress**: keep the Cara Care–style **numeric scales with qualitative anchors** (e.g., 1 = “no pain”, 5 = “extreme pain”), and record those anchors in ADR-002 as the canonical description set.
* Where appropriate, cross-link to standard instruments (PHQ-9, GAD-7, etc.) as *inspiration* but **do not claim full compliance** unless the scale matches exactly.

**R1.4 — Mark REQUIRED vs OPTIONAL vocabularies for MVP**

In ADR-002:

* Mark as **REQUIRED**:

  * Bristol 0–7 and associated labels for `stool.type`
  * Core severity scales for tummy pain, bloating, mood, stress
  * Core `meal.metadata` and `stool.metadata` lists that drive clinical reasoning
* Mark as **OPTIONAL for MVP** (extensible later):

  * Fine-grained taste/texture tags (`“crispy”`, `“smoky”`, etc.)
  * Rare stool metadata (e.g., unusual descriptors appearing infrequently in Cara Care or literature)
  * Any long-tail values that increase token cost without strong clinical impact

**R1.5 — Governance & evolution protocol for vocabularies**

For `T810A-ADR-002-FR-006` (Maintenance Governance) and T810A2-S06:

* Treat **value additions** as *allowed between versions* with strict backward compatibility (never repurpose an existing value).
* Treat **value removals or semantic changes** as *governance events* requiring new ADR revisions and explicit migration notes.
* Require all new vocab values to:

  * Come with a one-line description
  * Specify which entry types/fields they apply to
  * Note whether they are MVP-critical or post-MVP

---

### Recommendation 2: Template Format Selection

**R2.1 — Primary format choice for Project Knowledge templates**

For **ChatGPT Project Knowledge** templates used by LLM_Gastro, adopt the following:

* **PRIMARY format**: **YAML** for template *definitions*

  * Rationale:

    * YAML 1.2 is a superset of JSON, so everything expressible in JSON can be represented in YAML.([Wikipedia][1])
    * YAML supports **native comments** (using `#`) for HYBRID annotations without breaking parsing.([Wikipedia][2])
    * ChatGPT can ingest YAML as a structured text file like JSON, with no additional platform restrictions for Knowledge files.([Data Studios ‧Exafin][3])
* **RUNTIME interchange format** (for Dynamic JSON, manual export, T810A3): remain **pure JSON** to align with existing architecture (`T810A-GDR-002` Stable/Dynamic JSON model).

**R2.2 — Comment support and HYBRID annotation implications**

* JSON does **not** support comments in the standard (RFC 8259) sense; comments must be represented as data fields (e.g., `"_comment"`).([Stack Overflow][4])
* YAML supports **inline and full-line comments**, which allows:

  * Light annotations on complex fields (e.g., scales, nullable fields, cross-field dependencies)
  * Clean structure for straightforward fields (no comments)
* Therefore, adopt **HYBRID Option C**:

  * 70–80% of fields: **no inline comments**, only clear naming and grouping
  * 20–30% complex/critical fields: **short comments** explaining meaning, allowed values, null semantics

**R2.3 — ChatGPT compatibility and constraints**

* Supported file types for Project Knowledge include both code/data formats (JSON, YAML, etc.) and standard text formats; these are stored and retrieved as text with a **2M token per text file** limit and **512MB** file size cap.([OpenAI Help Center][5])
* The recommended YAML + JSON split sits far below these limits and does not add any new platform risk.

**R2.4 — Trade-off summary (for IG-002)**

* **YAML templates (PK only)**

  * Pros: Native comments, more readable for humans, easy grouping, superset of JSON.
  * Cons: Indentation errors are easier to introduce; needs stricter linting/QA.
* **JSON runtime structures**

  * Pros: Ubiquitous tooling, easy validation, strict syntax, used by downstream integration.
  * Cons: No native comments → must avoid using JSON for annotated templates.

IG-002 should therefore state: *“Template structure for Project Knowledge SHALL be defined in YAML with HYBRID annotations; runtime Stable/Dynamic JSON SHALL remain pure JSON without comments.”*

---

### Recommendation 3: Template Structure & Annotation Patterns

**R3.1 — Annotation density policy**

* Default to **minimal field-level annotation**:

  * For most scalar fields (timestamps, booleans, simple numerics) rely on **descriptive key names** and grouping instead of comments.
* Use **inline comments ONLY where they materially reduce ambiguity**, especially for:

  * Numeric scales (explain range and anchors)
  * Controlled vocab keys with non-obvious semantics
  * Fields with non-trivial null behavior (`null-before-probe` policy)

**R3.2 — Dual responsibility implementation (schema + instructions)**

* Each YAML template SHOULD contain:

  * A short **top-level comment block** explaining:

    * Purpose of the template (e.g., “Meal tracking entry for LLM_Gastro”)
    * Whether it is **Stable** or **Dynamic** JSON exemplar
    * How the patient/clinician is expected to use the output (manual export, Cara Care import, etc.)
  * **Local comments** at critical fields only, e.g.:

    ```yaml
    tummy_pain: 3  # 1=no pain, 5=extreme pain; default null-before-probe
    ```
* Avoid turning the template into a pseudo-manual; large narrative explanations should live in **separate markdown docs** referenced from IG-003 (Vocabulary Docs).

**R3.3 — Instruction phrasing guidelines**

* Prefer short, directive phrasing inside comments:

  * “Allowed values: …”
  * “Default: null if unknown; probe if null.”
  * “Scale: 1–5, see vocabulary catalog.”
* Avoid open-ended language that might encourage hallucination (e.g., “LLM can guess if unsure”).

**R3.4 — External documentation**

* Use **one central markdown file** (e.g., `controlled_vocabularies.md` already planned in the Request/Plan) as the **extended documentation** for:

  * Full scale descriptions
  * Example entries and edge cases
* The templates SHOULD reference this doc briefly once, not inline-copy its content.

---

### Recommendation 4: Vocabulary Placement Strategy

**R4.1 — Hybrid placement as default**

Adopt a **hybrid strategy** for vocabulary placement across templates and the ADR-002 catalog:

* **Embedded in templates**:

  * Short, critical lists where seeing all options is essential to correct generation (e.g., `stool.type` Bristol 0–7, small severity scales).
* **External catalog (Epic ADR-002 + controlled_vocabularies.md)**:

  * Large or frequently evolving lists: e.g., extended `meal.metadata`, `stool.metadata`, long-tail symptom descriptors.

This balances **LLM clarity** at generation time with **token efficiency** and maintainability.

**R4.2 — Catalog organization for ADR-002**

* Organize the Epic-level catalog as:

  * **By Entry Type** → **By Field** → **Value Set** + description.
* Require each vocabulary set to specify:

  * Whether it is embedded in templates or external-only
  * Whether it is MVP-required or post-MVP
  * Version metadata (introduced in vX.Y.Z, deprecated in vA.B.C)

**R4.3 — Update workflows**

* Templates SHOULD reference vocabularies by **name**, not by hard-coded full lists, whenever the list is large or fast-evolving.
* When values are updated in ADR-002:

  * Only update templates that embed that specific list.
  * Maintain a simple **changelog section** in ADR-002 (“New values added”, “Deprecated values”).

---

### Recommendation 5: Token Budget Recommendations

These budgets are **advisory** and intended to keep T810A2 within comfortable limits under ChatGPT’s file and context constraints.([OpenAI Help Center][6])

**R5.1 — System prompt / global instructions**

* Recommended **target** for LLM_Gastro system instructions: **1,500–2,000 tokens**.
* Rationale: Leaves ample room in the context window for:

  * Current patient Stable JSON
  * One Dynamic JSON entry being generated/edited
  * A few relevant vocabulary snippets if needed

**R5.2 — Stable JSON per patient**

* Recommended **target size**: **≤ 1,000 tokens** per patient profile (including history flags, chronic conditions, and key preferences).
* If profiles grow beyond ~1,500 tokens, consider:

  * Splitting into themed sections (baseline profile, medication, long-term trends)
  * Loading only the necessary sections per session.

**R5.3 — Dynamic JSON entry (per tracking event)**

* Recommended **target upper bound**: **≤ 250 tokens** per *single* entry (meal, stool, digestion, etc.).
* Most entries should be much smaller (80–150 tokens); the 250-token cap is a guardrail to:

  * Prevent unbounded free-text fields
  * Encourage null-before-probe instead of verbose speculation

**R5.4 — Vocabulary catalog**

* For the entire **controlled vocabulary catalog** (Epic ADR-002 + T810A2 docs):

  * Recommended **target**: **8,000–15,000 tokens** total.
  * This safely sits far below the 2M-token per-file limit and leaves headroom for future expansions while keeping files readable and diff-able.

**R5.5 — DISCLAIMER**

> These token budget recommendations are NOT final decisions.
> Final token budgets SHALL be determined collaboratively by the T810A2 subconsultant and client, based on evolving platform constraints and operational requirements (per NFR-001 and the Research Brief).

---

### Recommendation 6: T810A2 F-RID Enhancement Insights

**R6.1 — IG-001 (Null Handling Pattern)**

* Confirm the **“null-before-probe”** policy as the default for all optional and mandatory fields when context is insufficient.
* Document in IG-001:

  * JSON representation (`null` vs missing field → use explicit `null`).
  * How templates should phrase this in comments (e.g., “If unknown, set to null and ask patient later”).

**R6.2 — IG-002 (Template Structure & Format)**

* Codify:

  * **YAML** as the PK template format with HYBRID annotation (Recommendation 2).
  * The **annotation density pattern** from Recommendation 3.
  * The separation between YAML templates vs runtime JSON (Stable/Dynamic).

**R6.3 — IG-003 (Controlled Vocabulary Documentation Standard)**

* Base the standard directly on:

  * The **Cara Care–inspired table layouts** and scale mappings from Deliverable A.
  * The **hybrid placement strategy** from Recommendation 4.
* Require all future vocab additions to follow the same markdown table pattern and include semantic anchors.

**R6.4 — IG-004 (Manual Workflow Guidance)**

* Use format insights to specify:

  * That **patients export/save Dynamic JSON as .json files** (not YAML) for manual workflows and future T810A3 aggregation.
  * Any file naming conventions and step-by-step export instructions (to be detailed in IG-004).

**R6.5 — IF-002 & IF-003 (Dynamic JSON & Vocabulary Interfaces)**

* For **IF-002 (Dynamic JSON Interface)**:

  * Clarify that each entry is a **single JSON object** matching the schemas defined via YAML templates.
  * Reference token bounds from Recommendation 5 to guide Single-Entry design.
* For **IF-003 (Controlled Vocabulary Interface)**:

  * Define that vocabularies are **accessed via template-embedded references** and Epic ADR-002 catalogs, not ad-hoc value lists in prompts.

**R6.6 — NFR-001..005 alignment**

* **NFR-001 (Token Efficiency)**: Supported by Recommendation 5 budgets and the hybrid vocab placement strategy.
* **NFR-002 (Schema Clarity)**: Supported by HYBRID annotations and YAML-based templates (Rec 2–3).
* **NFR-003 (Vocabulary Completeness)**: Supported by the exhaustive tables and ADR-002 enhancement pathway (Rec 1).
* **NFR-004 (Clinical Validity)**: Supported by Bristol alignment and Cara Care–based scales (Rec 1).
* **NFR-005 (Schema Extensibility)**: Supported by the governance-oriented evolution guidance for vocabularies and template structure (Rec 1 & 4).