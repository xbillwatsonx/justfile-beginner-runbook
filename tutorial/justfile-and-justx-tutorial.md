# Justfile & justx Tutorial

> **A longer guide to `just` and `justx` for developers and AI coding agents.**
>
> Learn how to replace scattered npm scripts, Makefiles, and shell scripts with a single, discoverable command runner that works across projects, and how to navigate it with `justx`, the interactive TUI launcher.

This is the longer tutorial. If you only want setup steps, start with `runbook/quick-start-card.md`.

---

## Table of Contents

1. [What is `just`?](#what-is-just)
2. [Why use a justfile?](#why-use-a-justfile)
3. [Installation](#installation)
4. [Your first justfile](#your-first-justfile)
5. [Recipes: the heart of just](#recipes-the-heart-of-just)
6. [Variables, parameters, and defaults](#variables-parameters-and-defaults)
7. [Dependencies between recipes](#dependencies-between-recipes)
8. [The `default` recipe and `--list`](#the-default-recipe-and---list)
9. [Settings block (`set ...`)](#settings-block-set-)
10. [Recipe attributes (`[group]`, `[doc]`, `[private]`, `[confirm]`)](#recipe-attributes-group-doc-private-confirm)
11. [Shebang recipes](#shebang-recipes)
12. [Aliases and abbreviations](#aliases-and-abbreviations)
13. [AI-agent-friendly justfile patterns](#ai-agent-friendly-justfile-patterns)
14. [justx: the interactive TUI launcher](#justx-the-interactive-tui-launcher)
15. [Hands-on: build a justfile from scratch](#hands-on-build-a-justfile-from-scratch)
16. [Real-world justfile examples](#real-world-justfile-examples)
17. [Cheatsheet](#cheatsheet)
18. [Further reading](#further-reading)

---

## What is `just`?

`just` is a **command runner** — a single, fast binary that reads a file called `justfile` and turns its contents into runnable commands called **recipes**.

Think of it as Make for humans: no `.PHONY`, no arcane syntax, no tab-vs-space wars. Just a clean file of named commands you can run from anywhere in your project.

```bash
# Instead of remembering:
npm run dev
npm run build
npm run test:watch
npx vitest run -t "spell"

# You type:
just dev
just build
just test-watch
just test-only spell
```

And if you forget what's available? Type `just --list` to see the available recipes.

---

## Why use a justfile?

| Problem | How `just` solves it |
|---|---|
| **"What commands does this project have?"** | `just --list` prints every recipe with a description |
| **"I have 15 npm scripts and can't remember half of them"** | Recipes are self-documenting with comments that appear in `--list` |
| **"My Makefile only works on Linux"** | `just` is easier to use across Linux, WSL, macOS, and Bash-compatible Windows setups |
| **"I need parameters with defaults"** | Recipes accept named parameters with default values |
| **"I want an AI agent to understand my project instantly"** | `just --list` is a one-line interface description any agent can parse |
| **"I have commands scattered across package.json, shell scripts, and my brain"** | One file. One tool. One menu. |

### Comparison with alternatives

| Need | npm scripts | Make | shell scripts | **just** |
|---|---|---|---|---|
| Works without Node.js | ❌ | ⚠️ | ✅ | ✅ |
| Cross-platform for beginners | ⚠️ | requires setup | ✅ | ✅ |
| Discoverable menu (`--list`) | ❌ | ⚠️ | ❌ | ✅ |
| Parameters with defaults | ❌ | ❌ | ⚠️ | ✅ |
| Documented recipes in `--list` | ❌ | ⚠️ | ❌ | ✅ |
| Built-in `--dry-run`, `--fmt` | ❌ | ⚠️ | ❌ | ✅ |
| AI agent can cold-start a project | ⚠️ | ⚠️ | ❌ | ✅ |

---

## Installation

`just` is a single binary. Pick your method:

```bash
# Debian / Ubuntu
# apt requires Debian 13+ or Ubuntu 24.04+. On older systems, use the official binary installer, cargo, uv, or pipx.
sudo apt install just

# macOS
brew install just

# Any Linux (static binary)
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin

# Verify
just --version
# just 1.49.0 (example output; your version may differ)
```

Make sure `~/.local/bin` is in your `$PATH`. Add this to `~/.bashrc` if needed:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

## Your first justfile

Create a file called `justfile` (no extension, all lowercase) in any project folder:

```just
hello:
    echo "Hello, world!"
```

Run it:

```bash
just hello
# echo "Hello, world!"
# Hello, world!
```

That's it. A recipe is a name followed by a colon, and the body is indented with **4 spaces** (tabs also work — `just` normalizes them).

### Key things to notice

- The file is named `justfile`, not `justfile.just` or `Justfile`.
- `just` printed the command before running it. We'll silence that with `@` shortly.
- You can have as many recipes as you want in one file.

---

## Recipes: the heart of just

A recipe is a named block of shell commands. Here's the anatomy:

```just
# This is a comment. It shows up in `just --list`.
recipe-name param1 param2="default":
    @echo "Running with {{param1}} and {{param2}}"
    some-command --flag
```

### The `@` prefix — silencing command echo

By default, `just` echoes every command line before running it. That's noisy. Prefix a line with `@` to suppress the echo:

```just
loud:
    echo "You'll see this command printed, then the output"

quiet:
    @echo "You'll only see the output, not the command"
```

**Rule of thumb:** use `@` for everything that isn't interesting debug output.

### Multi-line recipes

```just
deploy: build test
    @echo "Deploying..."
    @rsync -avz dist/ server:/var/www/
    @echo "Done!"
```

---

## Variables, parameters, and defaults

### Top-level variables

Variables defined at the top of the file are available everywhere:

```just
project := "my-app"
port    := "3000"

start:
    @echo "Starting {{project}} on port {{port}}"
    npm run dev -- --port {{port}}
```

Use `:=` for compile-time constants. These are evaluated when `just` parses the file, not at runtime.

### Recipe parameters

Recipes can accept arguments:

```just
greet person:
    @echo "Hello, {{person}}!"
```

```bash
just greet Alice
# Hello, Alice!
```

### Default values

Parameters can have defaults, making them optional:

```just
greet person="world":
    @echo "Hello, {{person}}!"
```

```bash
just greet          # Hello, world!
just greet Alice    # Hello, Alice!
```

### Variadic parameters (`+`)

Use `+` before a parameter name to accept multiple arguments:

```just
list-files +paths:
    ls -la {{paths}}
```

```bash
just list-files src public tests
# ls -la src public tests
```

`paths` becomes a single string with all arguments joined by spaces. Perfect for wrapping shell commands.

### Naming convention

Use lowercase, dash-separated names that read like English:

```bash
just run-tests
just deploy-staging
just build-release v2.0.0
```

---

## Dependencies between recipes

Recipes can depend on other recipes. Dependencies always run **before** the recipe that needs them:

```just
# install runs before build
build: install
    npm run build

install:
    @npm ci
```

```bash
just build
# → runs install, then build
```

### Multiple dependencies

```just
# All dependencies run first, in order
ci: install build test
    @echo "CI passed"

install:
    @npm ci

build:
    @npm run build

test:
    @npm test
```

### Parameterized dependencies

```just
release version: build test
    @echo "Releasing {{version}}..."
    @git tag "v{{version}}"
    @git push --tags
```

Each dependency runs at most once per invocation, even if multiple recipes depend on it.

---

## The `default` recipe and `--list`

### `just --list` — your project menu

This is the killer feature. Run it in any project with a justfile:

```bash
just --list
```

Output:

```
Available recipes:
    build        # Type-check and bundle for production
    clean        # Remove build artifacts
    dev          # Start the dev server with hot reload
    install      # Install dependencies
    test         # Run the full test suite
    test-watch   # Run tests in watch mode
```

Every recipe appears with the first line of its comment as a description. This is your project's **table of contents**.

### The `default` recipe

When you run `just` with no arguments, it runs the default recipe if one exists. A good beginner pattern is to make `default` print the recipe list:

```just
default:
    @just --list
```

Now typing `just` (with no arguments) prints the menu. **This is the recommended pattern** — cold start → full project map.

---

## Settings block (`set ...`)

`set` directives go at the very top of the justfile and change global behavior:

```just
# Use bash instead of sh (recommended)
set shell := ["bash", "-uc"]

# Enable unstable features (needed for top-level `export` and `--fmt`)
set unstable

# Explicitly load .env files (on by default in just 1.49+)
set dotenv-load

# Allow # comments inside recipe bodies
set ignore-comments

# Suppress the "Recipe ... failed" message on error
set no-exit-message
```

### Common advanced settings

```just
set shell := ["bash", "-uc"]
set unstable
```

- `set shell := ["bash", "-uc"]` — use bash with strict error handling (`-u` = error on unset variables, `-c` = read from string)
- `set unstable` — enables features marked unstable in your installed `just` version. Some examples may require it depending on your version. Check `just --help` or the official manual for your installed version.

The starter kit keeps things minimal on purpose. Add these settings as your justfile grows and you want stricter shell behavior or formatter support.

### Exporting variables to recipes

By default, top-level variables are **not** available to shell commands inside recipes. To export them, combine `set unstable` with `export`:

```just
set unstable

export DATABASE_URL := "postgres://localhost/dev"
export NODE_ENV    := "development"

db-ping:
    psql "$DATABASE_URL" -c "SELECT 1"
```

You can also export variables locally inside a single recipe:

```just
test:
    export NODE_ENV=test
    npm test
```

---

## Recipe attributes (`[group]`, `[doc]`, `[private]`, `[confirm]`)

Attributes go on the line **directly above** a recipe and change how it behaves:

### `[group('name')]` — organize your menu

```just
# Start the dev server
[group('dev')]
dev:
    @npm run dev

# Run the test suite
[group('test')]
test:
    @npm test
```

`just --list` now shows grouped output:

```
Available recipes:
    [dev]
    dev    # Start the dev server
    [test]
    test   # Run the test suite
```

### `[doc('text')]` — override the description

```just
[doc('Start the Vite dev server on port 5173')]
dev:
    @npm run dev
```

Use this when the auto-extracted comment isn't clear enough.

### `[private]` — hide from the menu

```just
[private]
_internal-helper:
    @echo "This won't appear in --list"
```

The recipe is still runnable — it just doesn't clutter the menu.

### `[confirm('message')]` — guard destructive actions

```just
[confirm('Delete all build artifacts and node_modules? (y/N)')]
nuke:
    rm -rf dist node_modules .vite
    @echo "Cleaned. Run 'just install' to restore."
```

`just` will prompt the user before running the recipe.

---

## Shebang recipes

For recipes that need a different interpreter (Python, Node, Ruby, etc.), use a shebang line:

```just
fetch-stats:
    #!/usr/bin/env python3
    import json, urllib.request
    data = json.loads(urllib.request.urlopen("https://api.example.com/stats").read())
    print(f"Users: {data['users']}")

generate-report:
    #!/usr/bin/env node
    const fs = require('fs');
    const report = { date: new Date().toISOString(), status: 'ok' };
    fs.writeFileSync('report.json', JSON.stringify(report, null, 2));
    console.log('Report written to report.json');
```

The shebang line becomes the interpreter for the entire recipe body. The body is written to a temp file and executed. This is the cleanest way to embed non-shell logic directly in your justfile.

---

## Aliases and abbreviations

### Aliases

Create shortcuts for frequently-used recipes:

```just
alias t  := test
alias tw := test-watch
alias b  := build
```

```bash
just t    # runs test
just tw   # runs test-watch
just b    # runs build
```

### Abbreviations

`just` also supports abbreviation matching — if you type a unique prefix, it resolves automatically:

```bash
just b    # runs build (if no other recipe starts with 'b')
just tes  # runs test (if unambiguous)
```

Aliases are explicit and documented. Abbreviations are convenient but fragile. Prefer aliases for muscle-memory shortcuts.

---

## AI-agent-friendly justfile patterns

This section is for developers who work with AI coding agents, code editors, CLI assistants, or local AI tools. A well-crafted justfile makes your project **instantly understandable** to any agent that lands in it.

### 1. Make `default` print the menu

```just
default:
    @just --list
```

One command, full project map. An agent types `just` and knows everything the project can do.

### 2. Use `[group]` to organize

Group recipes by concern so the menu tells a story:

```just
[group('dev')]      # Development lifecycle
[group('test')]     # Testing
[group('agent')]    # Agent handoff and context
[group('deploy')]   # Deployment
[group('maintenance')]  # Cleanup and utilities
```

### 3. Write imperative, specific comments

```just
# Run unit tests once
# Run unit tests in watch mode (usage: just test-watch)
# Type-check and bundle for production
```

An agent scanning `just --list` should be able to pick the right recipe **without reading the body**.

### 4. Add a `handoff` recipe

This is the killer recipe for agent-to-agent continuity. It writes a one-page brief any agent can ingest:

```just
# Drop a handoff brief for the next agent or session
[group('agent')]
handoff out="_handoff.md":
    @echo "# Handoff brief for {{justfile_directory()}}" > {{out}}
    @echo "" >> {{out}}
    @echo "## Available commands" >> {{out}}
    @just --list >> {{out}}
    @echo "" >> {{out}}
    @echo "## Last commits" >> {{out}}
    @git log --oneline -10 >> {{out}}
    @echo "Wrote {{out}}"
```

Run `just handoff` to drop a `_handoff.md` file. Hand it to a new agent (or paste it into a chat) and they have orientation in seconds.

### 5. Add an `agent-context` recipe

```just
# Show what files a new agent should read first
[group('agent')]
agent-context:
    @echo "1. justfile (this file)"
    @echo "2. AGENTS.md"
    @echo "3. README.md"
    @echo "4. docs/ARCHITECTURE.md (if present)"
```

### 6. Add agent workflow recipes

```just
# Preflight checks — run before starting work
[group('agent')]
agent-preflight:
    @echo "── Git Status ──"
    @git status --short
    @echo ""
    @echo "── Available Recipes ──"
    @just --list

# Verification after edits — confirm what changed
[group('agent')]
agent-verify:
    @echo "── Git Status ──"
    @git status --short
    @echo ""
    @echo "── Diff Summary ──"
    @git diff --stat

# Show current repo state
[group('agent')]
agent-status:
    @echo "── Branch ──"
    @git branch --show-current
    @echo ""
    @echo "── Recent Commits ──"
    @git log --oneline -5
    @echo ""
    @echo "── Working Tree ──"
    @git status --short
```

### 7. Don't put secrets in the justfile

The justfile is plain text and almost certainly committed to git. Use `.env` files for secrets and `export` for non-secret config.

### 8. Make destructive recipes `[confirm]`

```just
[confirm('Delete dist/, node_modules/, and cache? (y/N)')]
[group('maintenance')]
nuke:
    rm -rf dist node_modules .vite
    @echo "Run 'just install' to restore."
```

### 9. The standard justfile header

Every project justfile should start with the same header so agents recognize it:

```just
# project-name — one-line description
# Standard agent justfile convention — every repo feels the same.

set shell := ["bash", "-uc"]
set unstable

# ── Navigation ─────────────────────────────────────────────────────

# Show all commands
help:
    @just --list

# Open command menu (requires justx)
menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi
```

---

## justx: the interactive TUI launcher

`justx` is a companion tool that provides an **interactive terminal UI** for browsing and running just recipes. Instead of typing `just --list` and then `just <recipe>`, you get a navigable menu.

### Installation

```bash
# Recommended
uv tool install justx

# Alternate Python path
pip install justx

# Verify
justx --version
# justx 0.5.3 (example output; your version may differ)
```

### Key commands

| Command | What it does |
|---|---|
| `justx` | Open the interactive TUI menu (browse and run recipes) |
| `justx list` | List all recipes from all scopes |
| `justx list -l` | List local recipes only (project justfile) |
| `justx list -g` | List global recipes only (`~/.justx/user.just`) |
| `justx run <recipe>` | Run a recipe directly |
| `justx run -l <recipe>` | Run a local recipe |
| `justx run -g <source:recipe> <args>` | Run a global recipe |
| `justx check` | Verify `just` is installed and show discovered justfiles |
| `justx check -v` | Verbose check with detailed discovery info |
| `justx init` | Initialize `~/.justx/` with a sample `user.just` file |
| `justx init --download-examples` | Download example justfiles from the justx GitHub repo |

### Global vs. local recipes

`justx` understands two scopes:

- **Local** — the `justfile` in your current project directory
- **Global** — `~/.justx/user.just` — recipes available everywhere, in any directory

This means you can have personal recipes that follow you across all projects:

```just
# ~/.justx/user.just

# Greet someone by name
greet name:
    @echo "Hello, {{name}}! Welcome to justx."

# Show the current date and time
now:
    date
```

### Using justx in your justfile

Add a `menu` recipe to every project justfile so agents and users can launch the TUI:

```just
# Open command menu (requires justx)
menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi
```

### Why justx matters for AI agents

When an AI coding agent lands in a project:

1. It runs `just` → sees the menu
2. It runs `justx list` → sees all recipes with scopes
3. It runs `justx run <recipe>` → executes with scope awareness
4. It can use `justx check -v` to understand the full justfile discovery chain

The TUI (`justx` with no arguments) is also great for **humans** who want to browse recipes interactively without memorizing command names.

### justx workflow for agents

```bash
# 1. Discover what's available
justx list

# 2. Check the environment
justx check -v

# 3. Run a recipe
justx run -l build

# 4. Run a global recipe
justx run -g docker:shell my-image
```

Global recipes may need a source prefix when multiple global recipe files exist.

---

## Hands-on: build a justfile from scratch

Let's build a real justfile for a typical TypeScript/Vite project. Follow along.

### Step 1 — Create the file

```bash
touch justfile
```

### Step 2 — Add the header and settings

```just
# my-project — a TypeScript web app
# Standard agent justfile convention — every repo feels the same.

set shell := ["bash", "-uc"]
set unstable

# ── Navigation ─────────────────────────────────────────────────────

# Show all commands
help:
    @just --list

# Open command menu (requires justx)
menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi

default:
    @just --list
```

### Step 3 — Add dev lifecycle recipes

```just
# ── Dev Lifecycle ──────────────────────────────────────────────────

# Install dependencies (idempotent)
[group('dev')]
install:
    @npm install

# Start the dev server with hot reload
[group('dev')]
dev:
    @npm run dev

# Type-check and build for production
[group('dev')]
build:
    @npm run build

# Preview the production build locally
[group('dev')]
preview:
    @npm run preview
```

### Step 4 — Add test recipes

```just
# ── Testing ────────────────────────────────────────────────────────

# Run the full test suite once
[group('test')]
test:
    @npm test

# Run tests in watch mode
[group('test')]
test-watch:
    @npm run test:watch

# Run a single test by name (usage: just test-only "my test name")
[group('test')]
test-only name:
    npx vitest run -t "{{name}}"
```

### Step 5 — Add agent recipes

```just
# ── Agent Handoff ──────────────────────────────────────────────────

# Preflight checks — run before starting work
[group('agent')]
agent-preflight:
    @echo "── Git Status ──"
    @git status --short
    @echo ""
    @echo "── Available Recipes ──"
    @just --list

# Verify what changed after edits
[group('agent')]
agent-verify:
    @echo "── Git Status ──"
    @git status --short
    @echo ""
    @echo "── Diff Summary ──"
    @git diff --stat

# Show current repo state
[group('agent')]
agent-status:
    @echo "── Branch ──"
    @git branch --show-current
    @echo ""
    @echo "── Recent Commits ──"
    @git log --oneline -5
    @echo ""
    @echo "── Working Tree ──"
    @git status --short

# Drop a handoff brief for the next agent or session
[group('agent')]
handoff out="_handoff.md":
    @echo "# Handoff brief for {{justfile_directory()}}" > {{out}}
    @echo "" >> {{out}}
    @echo "## Available commands" >> {{out}}
    @just --list >> {{out}}
    @echo "" >> {{out}}
    @echo "## Last commits" >> {{out}}
    @git log --oneline -10 >> {{out}}
    @echo "Wrote {{out}}"

# Show what files a new agent should read first
[group('agent')]
agent-context:
    @echo "1. justfile (this file)"
    @echo "2. AGENTS.md"
    @echo "3. README.md"
    @echo "4. docs/ARCHITECTURE.md (if present)"
```

### Step 6 — Add maintenance recipes

```just
# ── Maintenance ─────────────────────────────────────────────────────

# Remove build artifacts
[group('maintenance')]
clean:
    rm -rf dist .vite

# Deep clean — removes node_modules too
[confirm('Delete dist/, node_modules/, and cache? (y/N)')]
[group('maintenance')]
nuke:
    rm -rf dist .vite node_modules
    @echo "Run 'just install' to restore dependencies."
```

### Step 7 — Test it

```bash
just                    # runs the default recipe if one exists
just --list             # organized menu with groups
just dev                # starts the dev server
just test-only "login"  # runs a specific test
just handoff            # writes _handoff.md
just agent-preflight    # shows git status + menu
justx                   # opens the interactive TUI (if installed)
```

### The complete file

```just
# my-project — a TypeScript web app
# Standard agent justfile convention — every repo feels the same.

set shell := ["bash", "-uc"]
set unstable

# ── Navigation ─────────────────────────────────────────────────────

# Show all commands
help:
    @just --list

# Open command menu (requires justx)
menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi

default:
    @just --list

# ── Dev Lifecycle ──────────────────────────────────────────────────

# Install dependencies (idempotent)
[group('dev')]
install:
    @npm install

# Start the dev server with hot reload
[group('dev')]
dev:
    @npm run dev

# Type-check and build for production
[group('dev')]
build:
    @npm run build

# Preview the production build locally
[group('dev')]
preview:
    @npm run preview

# ── Testing ────────────────────────────────────────────────────────

# Run the full test suite once
[group('test')]
test:
    @npm test

# Run tests in watch mode
[group('test')]
test-watch:
    @npm run test:watch

# Run a single test by name (usage: just test-only "my test name")
[group('test')]
test-only name:
    npx vitest run -t "{{name}}"

# ── Agent Handoff ──────────────────────────────────────────────────

# Preflight checks — run before starting work
[group('agent')]
agent-preflight:
    @echo "── Git Status ──"
    @git status --short
    @echo ""
    @echo "── Available Recipes ──"
    @just --list

# Verify what changed after edits
[group('agent')]
agent-verify:
    @echo "── Git Status ──"
    @git status --short
    @echo ""
    @echo "── Diff Summary ──"
    @git diff --stat

# Show current repo state
[group('agent')]
agent-status:
    @echo "── Branch ──"
    @git branch --show-current
    @echo ""
    @echo "── Recent Commits ──"
    @git log --oneline -5
    @echo ""
    @echo "── Working Tree ──"
    @git status --short

# Drop a handoff brief for the next agent or session
[group('agent')]
handoff out="_handoff.md":
    @echo "# Handoff brief for {{justfile_directory()}}" > {{out}}
    @echo "" >> {{out}}
    @echo "## Available commands" >> {{out}}
    @just --list >> {{out}}
    @echo "" >> {{out}}
    @echo "## Last commits" >> {{out}}
    @git log --oneline -10 >> {{out}}
    @echo "Wrote {{out}}"

# Show what files a new agent should read first
[group('agent')]
agent-context:
    @echo "1. justfile (this file)"
    @echo "2. AGENTS.md"
    @echo "3. README.md"
    @echo "4. docs/ARCHITECTURE.md (if present)"

# ── Maintenance ─────────────────────────────────────────────────────

# Remove build artifacts
[group('maintenance')]
clean:
    rm -rf dist .vite

# Deep clean — removes node_modules too
[confirm('Delete dist/, node_modules/, and cache? (y/N)')]
[group('maintenance')]
nuke:
    rm -rf dist .vite node_modules
    @echo "Run 'just install' to restore dependencies."
```

---

## Real-world justfile examples

Here are patterns from real projects to inspire your own justfiles.

### Pattern: Godot game project

```just
# godot-sandbox — Godot 4 learning sandbox
set shell := ["bash", "-uc"]

help:
    @just --list

menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi

# Open the project in the Godot editor
[group('godot')]
editor:
    godot --editor ~/projects/my-game/project.godot

# Run the main scene
[group('godot')]
run:
    godot ~/projects/my-game/project.godot

# Run a specific scene by number
[group('godot')]
run-scene number:
    godot ~/projects/my-game/project.godot res://scenes/{{number}}-*/main.tscn

# List all scenes
[group('maintenance')]
list-scenes:
    @ls -d ~/projects/my-game/scenes/*/
```

### Pattern: Game development workshop

```just
# game-dev-workshop
set shell := ["bash", "-uc"]

help:
    @just --list

menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi

# Search all research material for a keyword
[group('research')]
search-research query:
    @rg -l -i "{{query}}" ~/projects/my-research/

# Log a new entry to the work log
[group('maintenance')]
log message:
    @echo "[$(date '+%Y-%m-%d')] {{message}}" >> WORKLOG.md
    @echo "Logged to WORKLOG.md"

# Show recent work log entries
[group('maintenance')]
worklog:
    @tail -20 WORKLOG.md
```

### Pattern: AI agent workspace

```just
# Generic AI coding agent workspace
set shell := ["bash", "-uc"]

help:
    @just --list

menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi

# Start your agent CLI interactively
run:
    agent-cli

# Start your agent CLI and continue the last session
continue:
    agent-cli -c

# Start your agent CLI with a prompt (usage: just ask "List all .ts files")
ask prompt:
    agent-cli -p "{{prompt}}"

# Start your agent CLI read-only (no file mutation)
read-only prompt="":
    agent-cli --tools read,grep,find,ls -p "{{prompt}}"

# Create a new extension from template
new-ext name:
    @echo 'import type { ExtensionAPI } from "@example/agent-sdk";\n\nexport default function (agent: ExtensionAPI) {\n  agent.on("session_start", async (_event, ctx) => {\n    ctx.ui.notify("{{name}} loaded!", "info");\n  });\n}' > ~/projects/my-agent/extensions/{{name}}.ts
    @echo "Created ~/projects/my-agent/extensions/{{name}}.ts"
```

---

## Cheatsheet

### Installation & discovery

```bash
just --version           # Check version
just --list              # Menu of every recipe
just --explain <recipe>  # Print doc comment, then run
just --evaluate          # Show all variables after expansion
just --fmt               # Auto-format the justfile
just --fmt --check       # CI mode: exit 1 if not formatted
just --dry-run <recipe>  # Show what would run without running it
just --edit              # Open justfile in $EDITOR
just --init              # Initialize a new justfile in project root
just --dump              # Print the entire justfile
just --summary           # List recipe names only
just --variables         # List variable names
```

### Recipe syntax

```just
recipe:                        # Basic recipe (4-space indent)
    @command                   # @ = silent (no echo)

recipe a b:                    # Required parameters
    echo {{a}} {{b}}

recipe a="default":            # Optional parameter with default
    echo {{a}}

recipe +paths:                 # Variadic (space-joined)
    ls {{paths}}
```

### Dependencies

```just
test: install                  # install runs before test
ci: build test lint            # Multiple dependencies, in order
release version: build test    # Parameterized dependency
```

### Attributes

```just
[group('dev')]                 # Group heading in --list
[doc('Custom description')]   # Override --list description
[private]                      # Hide from --list
[confirm('Are you sure?')]     # Prompt before running
[no-cd]                        # Don't cd to justfile directory
```

### Settings (top of file)

```just
set shell := ["bash", "-uc"]   # Use bash with strict mode
set unstable                   # Enable unstable features for this just version
set dotenv-load                # Load .env files
set ignore-comments            # Allow # comments in recipe bodies
set no-exit-message            # Suppress error tail message
```

### Variables

```just
name := "value"                # Compile-time constant
export VAR := "value"          # Also export to shell (needs set unstable)
{{name}}                       # Interpolation in recipes
{{justfile()}}                 # Absolute path of justfile
{{justfile_directory()}}       # Directory containing justfile
```

### Shebang recipes

```just
my-script:
    #!/usr/bin/env python3
    print("Hello from Python")
```

### Aliases

```just
alias t := test                # Shortcut for test
alias b := build               # Shortcut for build
```

### justx commands

```bash
justx                          # Open interactive TUI menu
justx list                     # List all recipes (all scopes)
justx list -l                  # List local recipes only
justx list -g                  # List global recipes only
justx run <recipe>             # Run a recipe
justx run -l <recipe>          # Run a local recipe
justx run -g docker:shell img  # Run a global recipe
justx check                    # Verify just installation
justx check -v                 # Verbose discovery check
justx init                     # Initialize ~/.justx/user.just
justx init --download-examples # Download example justfiles
```

---

## Further reading

- **Official just site & docs:** [https://just.systems](https://just.systems)
- **just GitHub repo:** [https://github.com/casey/just](https://github.com/casey/just)
- **just cheatsheet:** [https://github.com/casey/just/blob/master/docs/cheatsheet.md](https://github.com/casey/just/blob/master/docs/cheatsheet.md)
- **justx GitHub repo:** [https://github.com/fpgmaas/justx](https://github.com/fpgmaas/justx)
- **AGENTS.md convention:** Create an `AGENTS.md` file in your project root to give AI agents additional context about your codebase, conventions, and architecture.

---

## Quick start checklist

- [ ] Install `just` using the best method for your platform
- [ ] Install `justx` (`uv tool install justx`)
- [ ] Create a `justfile` in your project root
- [ ] Add `set shell := ["bash", "-uc"]` and `set unstable` at the top
- [ ] Add a `default` recipe that runs `@just --list`
- [ ] Add a guarded `menu` recipe that runs `justx` when available
- [ ] Add your dev, test, build recipes with `[group]` attributes
- [ ] Add `agent-preflight`, `agent-verify`, `agent-status`, and `handoff` recipes
- [ ] Run `just --list` and verify the menu looks good
- [ ] Run `just --fmt` to auto-format
- [ ] Commit the justfile to your repo
- [ ] Tell your AI agent: "Run `just` to see available commands"
