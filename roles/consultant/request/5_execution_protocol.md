# Execution Protocol: Request Artifact Task

## 1. Mission Context
Your purpose is to execute a specific phase of the request artifact workflow. The exact task you must perform is defined by the $ARGUMENT provided with this command.

## 2. Core Instruction Protocol
You MUST follow this sequence precisely:

1.  **Identify Your Task:** Your current task scope is defined by the $ARGUMENT.

2.  **Locate the Contract:** Open the TPG (`request_procedural_guideline.md`). Find the `<!-- BEGIN SCOPE: $SCOPE_ARGUMENT -->` block that matches your task. All subsequent instructions pertain to the metadata and steps within this block.

3.  **Verify Entry Gate (Pre-flight):**
    - Read the `prereq` list from the SCOPE block's metadata.
    - YOU MUST verify that **every condition** in that list is true before proceeding.
    - If any prerequisite is not met, YOU MUST **HALT** and report the specific failed condition.

4.  **Ingest Knowledge:**
    - Read the `knowledge` list from the SCOPE block's metadata.
    - You MUST ingest the full content of every document listed there to inform your work.

5.  **Execute Scoped Workflow:**
    - Execute the numbered steps contained within the body of the SCOPE block.
    - You MUST strictly adhere to the referenced `Core Principles` and `Hard Gates` (see TPG Appendix A).

6.  **Verify Exit Gate (Post-flight):**
    - Read the `success` list from the SCOPE block's metadata.
    - Your task is complete **ONLY when every condition** listed in the `success` list has been met.
    - This list is your primary checklist for your internal self-validation before concluding your response.

## 3. Shared Sub-Protocols
- **Pre-flight:** Before Step 1, you MUST execute the shared `integrity_check.md` protocol.
```
@prompt/roles/shared/integrity_check.md
```
- **Post-flight:** After Step 5 is successfully met, you MUST execute the shared `self_validation.md` protocol to perform a final quality review before generating your output.
```
@prompt/roles/shared/integrity_check.md
```