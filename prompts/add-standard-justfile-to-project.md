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
- report the justfile path, recipes added, validation output, and any commands that still need review
```

