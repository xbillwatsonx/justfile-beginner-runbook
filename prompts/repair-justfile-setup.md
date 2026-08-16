# Prompt: Repair A Justfile Setup

Copy this into your agent when `just`, `justx`, or a recipe is not working.

```text
Please troubleshoot my just/justx setup.

Start with read-only checks:
- operating system and shell
- current folder
- whether a justfile exists here
- `command -v just` or platform equivalent
- `just --version`
- `just --list`
- `command -v justx` or platform equivalent
- `justx --version`
- relevant PATH entries

Do not reinstall tools, overwrite files, or change PATH until you explain the likely cause, propose a fix, and ask for my approval. Wait for my approval before making any changes.

If the problem is a justfile recipe:
- inspect the recipe
- run the underlying command directly if safe
- explain the failure in plain English
- propose the smallest edit
- ask for my approval before making the change
- after approval, rerun `just --list` and the repaired recipe

Final report should include what was wrong, what changed, and proof that it works now.
```

