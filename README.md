# Justfile Beginner Runbook

Beginner-friendly runbook for installing `just`, setting up `justx`, and giving AI agents a standard way to run project commands.

This package is standalone. It gives beginners and their agents a practical path for installing `just`, setting up `justx`, learning the basics, and adding a safe project command menu.

## What This Does

This guide helps a user hand a project to an AI agent and say:

> Please get `just` and `justx` working on this system, then add a simple project `justfile` so future agents know how to run common commands.

The agent should inspect the system first, explain what it found, install missing tools only with approval, preserve existing project files, and verify the result before calling it finished.

## Why This Matters

A `justfile` gives every project a simple command menu.

Without one, a person or agent has to hunt through README files, package scripts, shell scripts, Makefiles, notes, and old chat history to figure out how the project works. That slows everything down, especially when a new agent enters the project cold.

With a `justfile`, the first useful question becomes:

```bash
just --list
```

That one command can show how to inspect the project, run tests, build, start the app, verify edits, or prepare a handoff.

For humans, this means fewer commands to memorize. For agents, it means less guessing and fewer failed attempts. Instead of spending time rediscovering the project, the agent can follow a known path:

1. run `just --list`
2. run `just agent-preflight`
3. make the requested change
4. run `just agent-verify`
5. report what changed

This can also save inference costs. Agents burn tokens when they repeatedly search for commands, misread setup instructions, try the wrong test command, or explain avoidable errors. A good `justfile` turns common project actions into deterministic recipes, so the agent spends more of its reasoning budget on the actual work and less on rediscovery.

`justx` is optional, but it makes the same command menu easier to browse. `just` gives the project a reliable command interface. `justx` gives users a friendly way to navigate it.

## What Is Included

- `runbook/justfile-beginner-runbook.md` - Full beginner guide.
- `runbook/quick-start-card.md` - One-page starter card.
- `prompts/install-just-and-justx.md` - Copy-paste prompt for tool installation.
- `prompts/teach-me-justfile-and-justx.md` - Copy-paste prompt for learning how justfiles and `justx` work.
- `prompts/add-standard-justfile-to-project.md` - Copy-paste prompt for adding a project justfile.
- `prompts/repair-justfile-setup.md` - Copy-paste prompt for troubleshooting.
- `tutorial/justfile-and-justx-tutorial.md` - Longer tutorial for humans and agents.
- `examples/basic-justfile` - Small example for a new project.
- `examples/agent-standard-justfile` - Reference copy of the standard agent workflow justfile.
- `starter-kit/justfile` - Copy-ready version of the same standard justfile for users to place in a project.
- `validate-justfile-setup.py` - Dependency-free checker for common setup issues.

## Quick Start

If you are brand new, start here:

1. Open `runbook/quick-start-card.md`.
2. Copy the first prompt from the card into your agent.
3. Let the agent inspect your system and recommend an install path.
4. Approve the install only after the agent explains what it found.
5. If you want a lesson before changing a project, copy `prompts/teach-me-justfile-and-justx.md`.
6. After install verification, copy `prompts/add-standard-justfile-to-project.md`.
7. Ask the agent to run:

```bash
just --version
just --list
just agent-preflight
```

If `justx` is installed, also test:

```bash
justx --version
justx
```

## What Success Looks Like

You are done with the first setup when:

- `just --version` prints a version.
- `just --list` shows available recipes.
- the project has a `justfile`.
- `just agent-preflight` runs without a confusing error.
- `justx --version` prints a version, if you installed `justx`.

`justx` is helpful but optional. A project should still work with plain `just`.

## Supported Platforms

This package is intended for:

- Linux
- WSL on Windows
- Windows
- macOS

`just` is the core tool. `justx` is optional. The install prompt asks the agent to detect the user's system before recommending commands.

## Version

Status: v0.1.0 release candidate.

## Source Notes

Installation guidance was checked against:

- `just` official manual: https://just.systems/man/en/installation.html
- `just` package list: https://just.systems/man/en/packages.html
- `justx` official repository: https://github.com/fpgmaas/justx
