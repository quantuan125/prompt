---
artifact_type: 'RESEARCH'
initiative_id: 'T800'
epic_id: 'T800C'
version: '1.0.0'
date: '2025-09-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: TradingView Pine Script Export of Horizontal Levels/Zones via Alerts

## I. EXECUTIVE SUMMARY

Commission targeted research on whether current TradingView + Pine Script v5 can export chart levels (horizontal lines, ranges/zones, session levels, POCs) and their human labels across multiple timeframes through alerts/webhooks in a way that our backend (tv_ingest) can parse into a structured YAML similar to the provided example. Identify hard limitations, viable patterns, and recommended approach(es).

## II. RESEARCH SCOPE & OBJECTIVES

### Primary Research Questions

1. Access to Drawn Objects
   - Can Pine v5 read properties (price, text/label/name, color, visibility, timeframe/visibility filters) of user-drawn objects (e.g., Horizontal Line, Ray, Box, Rectangle) placed manually on a chart?
   - If not directly, are there sanctioned workarounds (e.g., script-managed drawings only, input controls, alert-on-drawing with templated messages) that reliably surface the needed metadata to webhooks?

2. Alerts/Webhook Payload Capability
   - What information can be emitted from: (a) `alert()` in Pine; (b) alert created on a drawing tool; (c) strategy alerts? Are there limits on message length, rate, and frequency per alert?
   - Can a drawing’s user-entered “Text/Name” be programmatically included in an alert payload without manual duplication?
   - Are placeholders like `{{ticker}}`, `{{exchange}}`, `{{close}}`, or drawing-specific placeholders available for drawing alerts? Document official support.

3. Script-Managed Levels
   - For levels created by `line.new`, `hline`, `box.new`, can a script associate custom labels/tags and export them through `alert()` reliably? What getters exist (e.g., `line.get_price()`, `box.get_top()/get_bottom()`), and what are their constraints (history, repaint, last bar only)?
   - Is it feasible to model zones as `box.new` or as two `line` objects and serialize them to a compact payload per timeframe?

4. Multi-Timeframe Export Parity
   - Can a Pine script collect levels per multiple timeframes via `request.security()` while maintaining label integrity? What are known constraints when mixing drawings and MTF requests?
   - What are recommended patterns to enable/disable which timeframes to export (mirroring our existing `nmaq_exporter.pine` toggles)?

5. Labeling & Taxonomy
   - Feasibility of mapping TradingView-side labels to YAML categories: `major`, `sr`, `poc`, `zones`, `session`, `inactive`, `local`, `ALL`.
   - Robust conventions for auto-labeling (e.g., prefix `1D:SELL`, `1W:POC_1`, `ALL:ATH`), including collision handling and sanitation.

6. Data Volume & Reliability
   - Practical alert message size limits (bytes/characters) and safe batching strategy (multi-line payload vs multiple alerts). Include current official TradingView limits and any de facto safe thresholds.
   - Webhook delivery reliability, retries, and ordering guarantees; best practices to prevent duplication or loss.

7. Compliance & Terms
   - Confirm that the proposed approach conforms to TradingView Terms of Use and Pine Script policies (no scraping/private APIs). Identify any compliance risks.

### Secondary Research Objectives

8. Alternative Paths
   - If user-drawn object access is not possible, catalog alternative UX patterns: script-managed inputs; script-rendered objects with user-editable inputs; checklist pickers for categories; table UI with submit; using drawing alerts with a standardized manual template.
   - Evaluate pros/cons for trader workflow, error rates, and maintenance.

## III. RESEARCH DELIVERABLES

### A. Capability Matrix
- Matrix of object types (hline, ray, line, box/rectangle, label, text) vs: readable by Pine? editable? exportable via alert? label accessibility? MTF-aware?

### B. Alert/Webhook Constraints Report
- Official and observed limits for alert message length, frequency, webhook payload schema, and reliability considerations.

### C. Pattern Catalogue with Examples
- Code snippets demonstrating: extracting line/box prices; associating label metadata; serializing to compact lines; batching multi-timeframe payloads.
- Example of drawing-tool alert with templated message including a level label and value, if supported.

### D. Recommendation Brief
- Clear recommendation for the feasible path(s) to export levels/zones with labels across timeframes, with explicit callouts of what is not possible.
- Risk/mitigation table; impact on trader workflow.

## IV. CURRENT CONTEXT & CONSTRAINTS

- Existing exporter `components/tv_ingest/assets/pine/nmaq_exporter.pine` emits CSV-like rows over alerts for multiple timeframes.
- Backend `components/tv_ingest` ingests payloads and writes per-symbol aggregates (e.g., `data/BINANCE_BTCUSDT/master.csv`).
- Target output is a YAML structure authored today by traders; future goal is auto-generation from TradingView using level labels.

## V. RESEARCH METHODOLOGY

1. Primary sources: TradingView Pine Script v5 docs (objects, alerts, security/MTF, drawing tools), official forum posts, and staff responses.
2. Empirical tests: minimal Pine scripts to test getters on lines/boxes and alert payload size/behavior.
3. Constraint validation: verify Terms of Use regarding webhooks and automated exports.

## VI. SUCCESS CRITERIA

1. Definitive feasibility statement on user-drawn object access and label export.
2. Endorsed approach for exporting levels/zones with timeframe tags and labels.
3. Concrete examples sufficient for engineering spike.
4. Identified limitations and operational guidelines (message size, rate, batching).

## VII. SPECIFIC QUESTIONS FOR RESEARCHERS (ANSWER EXPLICITLY)

1. Can Pine read user-drawn Horizontal Line label text and price? If no, cite docs and propose the closest compliant workaround.
2. For script-created `hline`, `line.new`, `box.new` objects, what APIs retrieve their value(s) at the current bar? Provide code examples.
3. Can alerts created on drawing tools include the drawing’s label automatically in the webhook payload? What placeholders are supported?
4. What is the current maximum alert message size and safe practical limit? Provide source.
5. Are there known issues with multi-line alert payloads and TradingView webhooks? Any encoding quirks?
6. Can `request.security()` be used to gather level values from higher timeframes when the underlying objects are script-managed? Any repaint caveats?
7. Is there any supported API or export for chart “saved drawings”? If not, confirm.
8. Provide 2–3 reference implementations (public examples) closest to this use case.

## VIII. SAMPLE OUTPUTS REQUESTED

- Minimal Pine v5 snippets:
  - Create lines/boxes with custom labels; retrieve values; build alert payload lines in `key=value` or CSV form; multi-timeframe toggles mirroring `nmaq_exporter.pine`.
  - Example standardized alert message for drawing tools (if possible) including label and price.
- Backend payload examples compatible with our YAML transform (e.g., `TF=1D;TYPE=ZONE;LABEL=SELL;TOP=113200;BOT=111800`).

## IX. TIMELINE & CONTACTS

- Turnaround: 5 business days
- Point of Contact: LLM_Consultant (via repo comments/PR or shared channel)

---

Prepared by: LLM_Consultant
Approval Required: Client (Decision Owner)
Priority: High (blocks spec drafting for T800C)
Target Start: Upon approval
Expected Completion: 5 business days

