# TRACKING PAYLOAD WORKFLOW — PATIENT INSTRUCTIONS (DRAFT)

## I. Export From Conversation

1. Copy each tracking payload `json` code block the assistant shows you during the day.
2. Paste the JSON into a plain-text editor (for example, Notepad).

## II. Build a Chronological JSON Array

1. Create one “master” JSON array file: start with `[` and end with `]`.
2. For each copied code block (each one is an array), move its entry objects into the master array (append/merge).
3. Order entries by `timestamp` (oldest first, when available).
4. Ensure each entry object is separated by a comma and the JSON is valid.

## III. Save the File

1. Save the file with a `.json` extension, for example: `gastro_2025-01-01_session.json`.
2. Keep one file per day or per tracking period so that entries remain easy to review.

## IV. Upload to Project Knowledge (Future Use)

1. When instructed, upload the JSON file to the Project Knowledge area for LLM_Gastro.
2. Keep your original files as your own backup for future reference.
