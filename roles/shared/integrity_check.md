Before executing any task, YOU MUST perform these checks on the provided task instructions and artifacts (e.g., manifest, TPG, TSG).

1.  **Verify Manifest:** Confirm that a manifest file is present and its component versions match the expected versions for this task.
2.  **Verify Component Existence:** Confirm that all file paths declared in the manifest exist and are accessible.
3.  **On Failure:** If any check fails, YOU MUST **HALT** immediately. Your only response must be: "**HALT: Integrity check failed.** [Specific Error, e.g., 'TPG version mismatch' or 'Examples file not found']. Please ask a human to investigate."