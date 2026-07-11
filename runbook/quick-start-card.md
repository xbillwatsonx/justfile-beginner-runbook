# Justfile Beginner Quick-Start Card

Use this card when you want an AI agent to install `just`, set up `justx`, add a safe starter `justfile`, and create a durable rule that tells future agents to use it first.

## Plain English

- `just` lets a project save useful commands in one file named `justfile`.
- A command inside a `justfile` is called a recipe.
- `just --list` shows the available recipes.
- `just agent-preflight` can give an agent a predictable first check.
- `justx` is an optional menu that allows users to browse and run recipes interactively.
- `AGENTS.md` or a similar instruction file can tell agents to check the project's recipes before going manual.

## Supported Platforms

This guide is meant for Linux, WSL, macOS, and Windows with WSL/Git Bash/MSYS or another Bash-compatible shell.

For Windows beginners, WSL is the recommended path. Native PowerShell or `cmd.exe` needs a Windows-specific starter justfile.

The best install command depends on your system, so ask your agent to inspect first.

## First 20 Minutes

1. Give the first prompt below to your agent.
2. Let the agent inspect your system.
3. Read the agent's proposed install path.
4. Approve the install only if it makes sense.
5. Verify `just --version`.
6. Verify `justx --version` if you installed `justx`.
7. Give the second prompt below from inside the project folder.
8. Ask the agent to prove `just --list` and `just agent-preflight` work.
9. Have the agent add the justfile-first rule to `AGENTS.md` or the appropriate existing instruction file.
10. Review the changes and confirm the workflow works before setup is called complete.

You do not need to understand every command on day one. The goal is simply to get a reliable project command menu working.

## Give This To Your Agent First

```text
Please help me set up just and optional justx for this system.

First inspect the system. Tell me:
- my operating system
- whether I am in Linux, WSL, macOS, or Windows with a Bash-compatible shell
- whether just is installed
- whether justx is installed
- which install method you recommend
- whether any PATH changes are needed

Do not install or change anything until you summarize what you found and propose the next step.
```

Before approving install commands, make sure the agent explains what each command does and why that install method fits your system.

## If You Want A Lesson First

Use `prompts/teach-me-justfile-and-justx.md` and ask your agent to teach from `tutorial/justfile-and-justx-tutorial.md`.

## After Install Works

```text
Please add a beginner-friendly justfile to this project.

Before editing:
- check whether a justfile already exists
- inspect existing project commands, such as README instructions, package scripts, Makefile, Taskfile, scripts folder, or test commands
- propose the recipes you plan to add

Do not replace an existing justfile without showing me the diff or proposal first.

After editing, run just --list and just agent-preflight if available.

Then inspect the project for AGENTS.md, CLAUDE.md, .cursor/rules/*, .github/copilot-instructions.md, or another obvious agent instruction file. Preserve existing instructions. Add the durable justfile-first rule from prompts/add-justfile-first-agent-rule.md without duplicating an existing section.

Report the justfile and instruction file changed, review the changes with me, and ask me to confirm the workflow works. Do not call setup complete until I confirm it.
```

## Minimum Good Starter Recipes

```just
# Show all commands when running plain `just`
default:
    @just --list

# Show all commands
help:
    @just --list

# Open command menu
menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi

# Agent preflight checks
agent-preflight:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; else echo "Not a Git repository."; fi
    just --list

# Agent verification after edits
agent-verify:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; git diff --stat; else echo "Not a Git repository."; fi

# Show current repo state
agent-status:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; git log --oneline -5; else echo "Not a Git repository."; fi
```

## Verification

Ask the agent to prove:

```bash
just --version
just --list
just agent-preflight
justx --version
```

For `justx`, a full menu test may need a real terminal because it is interactive.

## What Success Looks Like

- `just --version` prints a version.
- `just --list` shows recipes.
- `just agent-preflight` runs.
- `justx --version` prints a version, if `justx` was installed.
- Your agent can explain what recipes it added.
- Your project instructions tell agents to check `just help` or `just --list` before operational work.
- You reviewed the changes and confirmed the workflow works.
