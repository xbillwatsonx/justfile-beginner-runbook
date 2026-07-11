# Prompt: Add A Durable Justfile-First Agent Rule

Copy this into your agent from the root of the project you want to improve.

```text
Please add a durable justfile-first rule to this project's agent instructions.

Before editing:
- inspect the project for existing agent instruction files, especially `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*`, `.github/copilot-instructions.md`, and any obvious repo-specific harness instruction file
- use the most specific existing instruction file that applies to the whole project
- prefer `AGENTS.md` when no more specific existing instruction file is present
- create `AGENTS.md` in the project root if no suitable instruction file exists
- preserve all existing instructions
- check whether a section named `## Justfile-First Workflow` or an equivalent rule already exists

Do not duplicate an existing rule section. If the rule already exists, improve it only when needed and show me what changed.

Add this block, adapting only what is necessary for the existing instruction file:

## Justfile-First Workflow

For operational tasks in this project, start by checking the project command menu:

- Run `just help` or `just --list` from the project root.
- If a matching recipe exists, use that recipe before running raw shell commands, manually inspecting config files, or doing broad searches.
- Go manual only when no recipe exists, the recipe fails, or the user explicitly asks for manual inspection.
- When you discover a repeated workflow that is not covered by a recipe, propose adding it to the justfile.
- After changing the justfile or these instructions, run `just --list` and `just agent-preflight` if available, then report what changed.

After editing:
- run `just --list`
- run `just agent-preflight` if that recipe is available
- report the exact instruction file you created or changed
- summarize the rule added and any existing instructions you preserved
- ask me to confirm that the workflow works before calling setup complete

Do not consider setup complete until I confirm the workflow works.
```
