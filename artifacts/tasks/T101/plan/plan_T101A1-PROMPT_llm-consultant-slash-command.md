---
artifact_type: 'PLAN'
initiative_id: 'T101'
epic_id: 'T101A'
feature_id: 'T101A1'
feature_code: 'PROMPT'
version: '1.0.0'
date: '2025-12-10'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CONSULTANCY PLAN: T101A1-PROMPT LLM_Consultant Slash Command Integration (v1.0.0)

## I. EXECUTIVE SUMMARY

This plan defines how to introduce a reusable Codex CLI slash command (`/prompts:consult`) that initializes the **LLM_Consultant** persona using the client-provided system prompt and optional structured headers. The solution is designed as a general-purpose consultancy tool while remaining portable inside this repository and compatible with Codex CLI’s `~/.codex/prompts` convention.

The immediate goal for v1.0.0 is to:
- Persist the LLM_Consultant system prompt exactly as authored by the client (no content changes).
- Provide a simple, optional header scaffold (`CONTEXT`, `GOAL`, `TASK`, `QA`, `INSTRUCTION`, `NOTE`) that appears after the system prompt in that exact order.
- Implement a Codex CLI-compatible Markdown prompt under `.codex/prompts/consult.md` in this repo, and (where environment permits) mirror it to `~/.codex/prompts/consult.md`.
- Defer any additional gate-mechanic encoding or behavioral instrumentation to a later version while preserving the existing protocol description inside the system prompt.

## II. CONTEXT MATERIALS & PREREQUISITES

### A. Repository & Tooling Context

- Root AGENTS instructions: `AGENTS.md` at repo root (streamlit app, Codex CLI usage, apply_patch-only edits for files).
- Codex CLI behavior and custom prompts: `https://developers.openai.com/codex/guides/slash-commands#create-your-own-slash-commands-with-custom-prompts`.
- Existing plan structure exemplar:  
  - `prompt/artifacts/tasks/T810/consultant/workspace/plan/T810A/T810A1/plan_T810A1-PROMPT_frid-enhancement.md`.

**Constraint**: All file edits within this repo MUST use the standard file edit tooling (apply_patch) per `AGENTS.md`. Shell commands may create directories but must not be used to modify file contents.

### B. Behavioral & Design Constraints (from QA)

From the client’s QA comments:

1. **Command name**  
   - Required slash command trigger: **`/prompts:consult`**.  
   - The prompt file will therefore be named `consult.md`, and Codex will expose it via `/prompts:consult`.

2. **Header scaffold (optional usage)**  
   - v1.0.0 final behavior: After the LLM_Consultant system prompt body, include only a `# USER PROMPT` header followed by the user-supplied arguments (`$ARGUMENTS`) so the CLI-provided prompt appears immediately under that header.
   - The system prompt alone SHOULD remain sufficient for typical usage; `# USER PROMPT` exists to make appending ad-hoc user text frictionless.

3. **System prompt integrity**  
   - The system prompt content provided by the client MUST be preserved verbatim.  
   - No wording, ordering, or structural changes are allowed inside that system prompt block.  
   - Only additional content appended **after** the system prompt (e.g., the header scaffold) is permitted.

4. **Gate mechanics (deferred)**  
   - The step previously described as “Encode phase and gate mechanics explicitly in the prompt” is **out of scope for v1.0.0**.  
   - The prompt will not add extra mechanical gate phrases, formal trigger tokens, or additional enforcement logic beyond what is already described in the system prompt.  
   - Future versions MAY revisit explicit gate encoding as a controlled enhancement once v1.0.0 is stable.

5. **Placement locations**  
   - Target locations for the `consult` prompt:  
     - Repo-scoped: `.codex/prompts/consult.md` (under the app repo root).  
     - User Codex home: `~/.codex/prompts/consult.md` (for direct CLI consumption).  
   - Within this environment, `.codex/prompts/consult.md` will be implemented directly.  
   - Mirroring to `~/.codex/prompts/consult.md` will be attempted where filesystem permissions allow; otherwise, the client will be instructed how to copy/sync the file manually.

6. **Usage scope**  
   - The LLM_Consultant is intended as a **general-purpose** senior technical consultant and Socratic partner across initiatives, not bound to a single project domain.  
   - However, it must always use the exact client-authored system prompt, which already encodes its philosophy, phases, and guardrails.

## III. HIGH-LEVEL IMPLEMENTATION PLAN (v1.0.0)

This section defines the concrete steps to implement T101A1-PROMPT v1.0.0 in a way that respects the QA constraints above.

### Step 1 — Confirm structural exemplar & constraints

**Objective**: Align this plan with existing artifact conventions and Codex CLI requirements.

- Review `plan_T810A1-PROMPT_frid-enhancement.md` to mirror frontmatter and section structure for the T101 plan.  
- Confirm there are no additional `AGENTS.md` files under `prompt/` that would override repo-level instructions for this artifact family.  
- Validate Codex CLI expectations for custom prompts: location under `~/.codex/prompts`, YAML frontmatter with `description` and optional `argument-hint`, and Markdown body semantics.

### Step 2 — Capture QA constraints in this plan (COMPLETED IN THIS DOCUMENT)

**Objective**: Make QA decisions first-class constraints driving all implementation steps.

- Encode command name, header order, system prompt immutability, gate-mechanics deferral, and dual placement (`.codex` + `~/.codex`) explicitly in Section II.B.  
- Treat these QA items as non-negotiable acceptance criteria for v1.0.0.

### Step 3 — Design the `consult` prompt file structure

**Objective**: Define a stable, CLI-compatible structure for the new prompt file before creating it.

- Filename: `consult.md`.  
- Repo location: `.codex/prompts/consult.md` (new directory tree under app root if missing).  
- Frontmatter:  
  - `description:` short human-readable label (e.g., “Senior Socratic technical consultant (LLM_Consultant)”).  
  - `argument-hint:` keep minimal and flexible (e.g., `[<user_prompt>]`) to encourage freeform user input.
  - No additional metadata fields are required by Codex CLI for basic use.  
- Body:  
  - Start with the client-provided LLM_Consultant system prompt, unchanged.  
  - Append a clearly separated `# USER PROMPT` header followed immediately by `$ARGUMENTS` (no additional descriptive text), but **do not** alter or back-edit the system prompt content itself.

### Step 4 — Implement `.codex/prompts/consult.md` in the repo

**Objective**: Materialize the designed prompt file inside the repository.

- Create `.codex/` and `.codex/prompts/` directories at the app root if they do not already exist (via shell `mkdir -p`, not editing files).  
- Add `.codex/prompts/consult.md` via `apply_patch`, honoring:
  - The frontmatter structure from Step 3.  
  - The verbatim system prompt content as provided by the client.  
  - The ordered header scaffold and optional inline guidance text.  
- Ensure that the Markdown structure is compatible with Codex CLI expectations (frontmatter at top, separated by `---`).

### Step 5 — Mirror to `~/.codex/prompts/consult.md` (best-effort)

**Objective**: Make the prompt available to Codex CLI in the default home directory.

- Attempt to create `~/.codex/prompts/consult.md` using the same content as the repo version.  
- If the current environment restricts writing outside the workspace root:
  - Document this limitation in the final consultancy note.  
  - Provide a simple copy/sync instruction the client can run locally, e.g., `mkdir -p ~/.codex/prompts && cp .codex/prompts/consult.md ~/.codex/prompts/consult.md`.

### Step 6 — Usage guidance & validation checklist

**Objective**: Provide a light-weight validation path for the client.

- In the final consultancy response, include concise usage notes:  
  - How to invoke: `/prompts:consult`.  
  - How the optional headers can be used or ignored.  
  - Clarify that no additional gate-encoding has been added beyond what the system prompt already describes.  
- Suggest a few smoke-test scenarios (e.g., ambiguous idea vs. concrete technical task) to validate that:  
  - The system prompt text appears as expected.  
  - The header scaffold follows in the required order.  
  - The command is discoverable in the Codex slash popup with the planned description.

## IV. FUTURE ENHANCEMENTS (OUT OF SCOPE FOR v1.0.0)

These items are deliberately postponed but can be referenced when planning T101A1-PROMPT v1.1.0+:

1. **Explicit gate-token encoding**  
   - Introduce explicit, machine-parseable gate phrases (e.g., `GATE_A_APPROVED`, `GATE_B_APPROVED`) to improve consistency in phase transitions.  
   - Clarify how Codex CLI users should signal these approvals during consultations.

2. **Argument-driven initialization**  
   - More deeply integrate named placeholders such as `$CONTEXT`, `$GOAL`, `$TASK`, `$QA`, `$INSTRUCTION`, `$NOTE` into the prompt body so that slash command arguments pre-populate the scaffold.  
   - Confirm real-world Codex behavior when arguments are omitted (e.g., empty vs. literal placeholder text) before finalizing this pattern.

3. **Repository-wide prompt governance**  
   - Align T101 artifacts (PLAN, REQUEST, SPS, etc.) with the broader governance and ID rules already defined for T810 once those are generalized.  
   - Consider adding project-level documentation under `prompt/plans/` describing how all custom prompts and slash commands are versioned and shared.
