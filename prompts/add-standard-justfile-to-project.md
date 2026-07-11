# Prompt: Add A Standard Project Justfile

Copy this into your agent from the root of the project you want to improve.

```text
Please add a beginner-friendly justfile to this project.

Before editing:
- check whether a justfile already exists
- inspect README instructions
- inspect package scripts, Makefile, Taskfile, scripts folder, or common test/build commands if present
- propose the recipes you plan to add

Preserve any existing justfile. Do not delete or replace it without showing me the proposed change first.

The starter recipes I want when practical are:
- help
- menu
- agent-preflight
- agent-verify
- agent-status

Add project-specific recipes only when you can verify the underlying command exists.

After editing:
- run `just --list`
- run `just agent-preflight` if available
- add the durable justfile-first rule to `AGENTS.md` or the appropriate existing agent/harness instruction file, using `prompts/add-justfile-first-agent-rule.md`
- preserve existing instructions and do not duplicate an existing rule section
- report the justfile path, instruction file path, recipes added, validation output, and any commands that still need review
- review the changes with me
- ask me to confirm the workflow works before calling setup complete

Do not consider setup complete until I confirm the workflow works.
```

