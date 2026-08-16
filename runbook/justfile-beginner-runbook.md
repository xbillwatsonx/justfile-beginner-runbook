# Justfile Beginner Runbook

Date: 2026-07-02

Use this runbook when you want an AI agent, command-line assistant, code assistant, or local AI harness to install `just`, set up `justx`, and add a useful project `justfile`.

This guide is platform-neutral. It can be used with any AI agent, command-line assistant, code assistant, desktop AI app, or local harness that can read and write project files.

## First 20 Minutes

If you are brand new, do not start by reading every file in this package.

Start with this path:

1. Open `runbook/quick-start-card.md`.
2. Give the first prompt to your agent.
3. Let the agent inspect your system.
4. Approve installation only after the agent explains what it found.
5. Confirm `just --version` works.
6. Confirm `justx --version` works if you chose to install `justx`.
7. Open your project folder.
8. Give the agent `prompts/add-standard-justfile-to-project.md`.
9. Confirm `just --list` shows recipes.
10. Confirm `just agent-preflight` runs.
11. Have the agent add the durable justfile-first rule to `AGENTS.md` or the appropriate existing agent instruction file.
12. Review what changed and confirm the workflow works before setup is called complete.

That is enough for the first day.

The longer tutorial is available at `tutorial/justfile-and-justx-tutorial.md` when you want to learn more.

## Supported Platforms

This runbook is intended for:

- Linux
- WSL on Windows
- macOS
- Windows with WSL, Git Bash, MSYS, or another Bash-compatible shell

`just` works across these platforms, which is one reason it is useful for humans and agents. Instead of each project having a different command style, the project can expose one familiar command list:

```bash
just --list
```

`justx` is optional. It gives users an interactive menu for recipes, but a project should still work with plain `just`.

The starter recipes in this package use Bash-style shell syntax. For Windows beginners, WSL is the recommended path. Native PowerShell or `cmd.exe` needs a Windows-specific starter justfile.

Before installing anything, the agent should detect the user's system and recommend the simplest install path for that system.

## 1. What `just` Is

`just` is a command runner.

That means you can put useful project commands in one plain text file named `justfile`, then run them by name.

For example, instead of remembering:

```bash
python3 -m pytest tests
```

you can create a recipe named `test` and run:

```bash
just test
```

For a beginner, the most important command is:

```bash
just --list
```

It shows the commands the project knows how to run.

## 2. What `justx` Is

`justx` is an optional terminal menu for `just`.

`just` runs recipes. `justx` is an optional menu that allows users to browse and run recipes interactively.

Official `justx` guidance says it is a TUI command launcher built on top of `just`, and that the `just` binary must already be available on your `PATH`.

In plain English: install `just` first. Install `justx` only if you want the optional interactive menu.

PATH is the list of folders your terminal searches when you type a command. If the program's folder is on PATH, you can type `just` without writing its full location. If it is not on PATH, the terminal says "command not found."

If you want a fuller lesson before changing a project, use:

- `prompts/teach-me-justfile-and-justx.md`
- `tutorial/justfile-and-justx-tutorial.md`

## 3. Why Agents Like Justfiles

AI agents often enter a project with no memory of how that project works.

A good `justfile` gives the agent a familiar menu:

- how to inspect the project
- how to run tests
- how to build
- how to lint
- how to verify edits
- how to report status

This keeps future work calmer because every project can answer the same first question:

```bash
just --list
```

## 4. Before Installing Anything

The agent should inspect first.

The agent should check:

- operating system
- shell
- whether `just` is installed
- whether `justx` is installed
- whether `uv`, `pipx`, `pip`, `brew`, `winget`, `scoop`, `apt`, or another package manager is available
- whether the install location is already on `PATH`

The agent should then explain the recommended install path before making changes.

## 5. Official Install Facts To Know

The official `just` manual says `just` can be installed with package managers, pre-built binaries, or from source with:

```bash
cargo install just
```

Common package-manager examples from the official package list include:

```bash
# Linux / WSL examples
# apt requires Debian 13+ or Ubuntu 24.04+. On older systems, use the official binary installer, cargo, uv, or pipx.
apt install just
dnf install just

# Windows examples
winget install --id Casey.Just --exact
scoop install just
choco install just

# macOS examples
brew install just
port install just

# Cross-platform examples
uv tool install rust-just
pipx install rust-just
npm install -g rust-just
```

The official `justx` repository currently recommends:

```bash
uv tool install justx
```

or:

```bash
pip install justx
```

Important: `justx` needs `just` available on `PATH`.

## 6. Friendly Agent Workflow

The agent should follow this order:

1. Inspect the system.
2. Report what is already installed.
3. Recommend the simplest install path.
4. Ask before installing if the action changes the system.
5. Install `just`.
6. Verify `just --version`.
7. Offer optional `justx` installation if the user wants an interactive menu.
8. If approved, install `justx` and verify `justx --version`. If skipped, continue with plain `just`.
9. Create or update a project `justfile`.
10. Run `just --list`.
11. Run `just agent-preflight` if that recipe exists.
12. Add the durable justfile-first rule to `AGENTS.md` or the appropriate existing agent/harness instruction file.
13. Preserve existing instructions and avoid duplicating an existing rule section.
14. Report exactly what changed and review it with the user.
15. Ask the user to confirm the workflow works.
16. Only then consider setup complete.

## 7. What Success Looks Like

A first setup is successful when:

- `just --version` prints a version.
- `just --list` shows recipes.
- the project has a `justfile`.
- `just agent-preflight` runs.
- `justx --version` prints a version, if `justx` was installed.
- the agent reports which recipes it added or changed.
- an appropriate project instruction file tells agents to check `just help` or `just --list` first.
- the user reviewed the changes and confirmed the workflow works.

If `justx` is not installed, that is not a failure. `justx` is helpful for browsing recipes, but plain `just` is the core tool.

## 8. Adding A Justfile To A Project

Before editing, the agent should inspect the project.

Look for:

- README instructions
- package scripts
- Makefile
- Taskfile
- scripts folder
- test commands
- build commands
- existing `justfile`, `Justfile`, `.justfile`, or `.Justfile`

If a justfile already exists, preserve it. Add recipes only after reviewing the current file.

### Coexistence With Existing Build Tools

Existing build tools should be preserved unless the user explicitly asks to replace or migrate them. A justfile can coexist with a Makefile, Taskfile, package scripts, and a `scripts/` folder because each tool uses its own command file. `make` reads `Makefile` and `just` reads `justfile`; they do not conflict.

Prefer thin just recipes that delegate to the project's existing authoritative commands rather than copying command implementations into two places. For example:

```just
# Run tests via existing Makefile
test:
    make test

# Build via existing npm scripts
build:
    npm run build
```

Before creating the justfile, report which command source is authoritative, what will remain unchanged, and which existing commands the proposed recipes will call. Review the proposed mapping with the user before editing.

If no justfile exists, start simple.

## 9. Standard Beginner Agent Recipes

These recipes are a good starting point:

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

The Git checks keep the recipes friendly when the folder is not a Git repo yet.

For a real project, add project-specific recipes such as:

```just
# Run tests
test:
    npm test

# Run linter
lint:
    npm run lint

# Build project
build:
    npm run build
```

Only add commands that actually work in that project.

## 10. Add The Durable Agent Rule

A justfile is the project command menu, but a future agent still needs a project rule telling it to look at that menu first.

After the justfile works, use `prompts/add-justfile-first-agent-rule.md`. The agent should inspect existing instruction files such as `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*`, or `.github/copilot-instructions.md`. It should preserve what is already there, use the most appropriate file, and avoid adding the same rule twice. If no suitable file exists, it should create `AGENTS.md` in the project root.

The finished rule should tell agents to:

- start operational work with `just help` or `just --list`
- use a matching recipe before raw commands, manual config inspection, or broad searches
- go manual when no recipe exists, a recipe fails, or the user asks for manual inspection
- propose a recipe when a repeated workflow is missing
- verify changes with `just --list` and `just agent-preflight` if available

The agent should report exactly which instruction file changed, review the setup with the user, and ask the user to confirm it works. Setup is not complete until the user confirms it.

## 11. Troubleshooting

### `just: command not found`

`just` is not installed, or it is installed somewhere your shell cannot find.

Ask the agent to check:

```bash
command -v just
echo "$PATH"
```

On Windows, ask it to check `winget`, `scoop`, or the terminal profile being used.

### `justx: command not found`

`justx` is not installed, or the Python tool install location is not on `PATH`.

Ask the agent to check:

```bash
command -v justx
uv tool list
python -m pip show justx
```

Use whichever commands are appropriate for your system.

### `justx` opens but no recipes show

You may not be inside a folder with a justfile.

Run:

```bash
ls
just --list
```

If `just --list` works, `justx` should be able to see local recipes when launched from that folder.

### `just --list` reports a parse error

The justfile itself has a syntax error. `just` reports the file and line number where parsing failed.

Ask the agent to:

1. read the reported line and the lines around it
2. identify the syntax issue (common causes: missing colon after a recipe name, wrong indentation, stray characters)
3. propose the smallest edit that fixes the syntax
4. ask for approval before editing
5. after editing, rerun `just --list` to confirm it parses
6. run the repaired recipe to confirm it works

Do not reinstall `just` or change PATH for a parse error. The problem is in the justfile, not the installation.

### A recipe fails

The recipe may call a command that is not installed, or the project may need setup first.

Ask the agent to:

1. run the command manually
2. inspect the error
3. update the recipe or add a setup note
4. rerun `just --list`

Ask for approval before making changes to the justfile.

## 12. Validation Script

This package includes a dependency-free validator script: `validate-justfile-setup.py`. It checks whether `just` is installed and on PATH, whether a justfile exists, whether the justfile parses, and whether recommended recipes are present.

### How to run it

From the repo root or any project directory:

```bash
python3 validate-justfile-setup.py /path/to/project
```

Add `--require-justx` only if `justx` is mandatory for your setup.

### Output and exit codes

- Exit code `0`: basic checks passed. The script prints `OK: basic justfile setup checks passed.`
- Exit code `1`: one or more errors were found. Errors are printed under an `Errors:` heading.
- Warnings are printed under a `Warnings:` heading but do not cause a nonzero exit code.

### What the validator checks

- The supplied project path exists and is a directory.
- A justfile exists (`justfile`, `Justfile`, `.justfile`, or `.Justfile`).
- The justfile is valid UTF-8.
- `just` is installed and available on PATH.
- `just --list` succeeds (the justfile parses without errors).
- Recommended recipes are present: `default`, `help`, `menu`, `agent-preflight`, `agent-verify`, `agent-status`.
- `justx` is on PATH (warning unless `--require-justx` is supplied).

### What the validator does not check

The validator does not run any recipe. A justfile may parse successfully and still contain recipes whose underlying commands fail. After running the validator, manually run safe recipes such as `just help` and `just agent-preflight` to confirm they work.

The validator also does not check:

- whether recipes produce correct output
- whether recipe commands exist on the system
- whether the justfile follows project conventions
- recipe body syntax beyond what `just --list` can parse

### Responding to validator findings

| Finding | What to do |
|---|---|
| `just is not installed or not on PATH` | Install `just` using the recommended method for your system, or fix PATH. See Section 5. |
| `No justfile found in ...` | Create a justfile in the project root. See Section 9. |
| `just --list failed` | The justfile has a syntax error. See Section 11, "`just --list` reports a parse error." |
| `Missing recommended recipes` | Add the missing recipes from the starter set in Section 9. |
| `justx is not installed` | Install `justx` only if you want the interactive menu. Otherwise, this warning is safe to ignore. |
| `File ... is not valid UTF-8` | The justfile has encoding problems. Re-save it as UTF-8 text. |

## 13. What Good Completion Looks Like

The agent's final report should include:

- whether `just` is installed
- `just --version` output
- whether `justx` is installed
- `justx --version` output
- justfile path
- agent instruction file path
- recipes added or changed
- `just --list` proof
- whether the user confirmed the workflow works
- any commands that still need manual review

## 14. Sources

- `just` installation manual: https://just.systems/man/en/installation.html
- `just` package list: https://just.systems/man/en/packages.html
- `just` pre-built binaries: https://just.systems/man/en/pre-built-binaries.html
- `justx` official repository: https://github.com/fpgmaas/justx
