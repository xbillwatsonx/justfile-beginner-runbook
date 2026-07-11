# Justfile Beginner Runbook

Beginner-friendly runbook for installing `just`, setting up `justx`, and giving AI agents a standard way to find and run project commands.

This package is standalone. It gives beginners and their agents a practical path for installing `just`, setting up `justx`, learning the basics, and adding a safe project command menu.

## What This Does

This guide helps a user hand a project to an AI agent and say:

> Please get `just` and `justx` working on this system, then add a simple project `justfile` so future agents know how to run common commands.

The agent should inspect the system first, explain what it found, install missing tools only with approval, preserve existing project files, and verify the result. It should also add a durable justfile-first rule to the project's agent instructions and get the user's confirmation before calling setup finished.

## Why This Matters

A `justfile` gives every project a simple command menu.

For a fuller explanation of why this matters for both people and AI agents, read [What Is a Justfile, and Why Should You Use One With AI Agents?](why-you-should-use-justfile-with-agents.md). You can also read and share the [published X article](https://x.com/xbillwatsonx/status/2076010273698152580).

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

## Two Layers That Work Together

The v0.1.6 setup has two simple layers:

1. The project `justfile` contains the recipes. It is the project command menu.
2. `AGENTS.md` or another agent/harness instruction file tells the agent to check that menu first.

Both matter. A command can exist without an agent knowing it should use that command first. That was the exact problem seen in real Hermes use: the recipe existed, but the durable project instructions did not yet tell the agent to start there. The justfile-first rule closes that gap for Hermes, OpenClaw, and other agent harnesses.

## What Is Included

- `runbook/justfile-beginner-runbook.md` - Full beginner guide.
- `runbook/quick-start-card.md` - One-page starter card.
- `prompts/install-just-and-justx.md` - Copy-paste prompt for tool installation.
- `prompts/teach-me-justfile-and-justx.md` - Copy-paste prompt for learning how justfiles and `justx` work.
- `prompts/add-standard-justfile-to-project.md` - Copy-paste prompt for adding a project justfile.
- `prompts/add-justfile-first-agent-rule.md` - Copy-paste prompt for adding the durable agent/harness rule.
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
7. Have the agent run:

```bash
just --version
just --list
just agent-preflight
```

8. Have the agent add the durable rule from `prompts/add-justfile-first-agent-rule.md` to `AGENTS.md` or the appropriate existing instruction file.
9. Review what changed and confirm the workflow works. Only then is setup complete.

If `justx` is installed, also test:

```bash
justx --version
justx
```

## Which Path Should I Use?

- New to command line? Start with the Linux, WSL, or macOS path if available. For Windows beginners, WSL is the recommended path.
- Already inside a project? Use `prompts/add-standard-justfile-to-project.md`.
- Only want to learn first? Use `prompts/teach-me-justfile-and-justx.md`.
- Something is broken? Use `prompts/repair-justfile-setup.md`.

Before approving install commands, make sure the agent explains what each command does and why that install method fits your system.

## Download Without Git

You do not need Git to use this package.

1. While v0.1.6 is a release candidate, use the repository files or the locally built `downloads/justfile-beginner-runbook-v0.1.6.zip`.
2. After v0.1.6 is approved and published, download `justfile-beginner-runbook-v0.1.6.zip` from the v0.1.6 release page.
3. Unzip it somewhere simple, such as your Desktop or Documents folder.
4. Open `runbook/quick-start-card.md` first.
5. Give the prompts to your agent from the unzipped folder.

Do not copy this repo's `starter-kit/justfile` into this runbook repo. Copy it into the project you want to improve.

## What Success Looks Like

You are done with the first setup when:

- `just --version` prints a version.
- `just --list` shows available recipes.
- the project has a `justfile`.
- `just agent-preflight` runs without a confusing error.
- `AGENTS.md` or the appropriate agent instruction file contains the justfile-first rule.
- you reviewed the changes and confirmed the workflow works.
- `justx --version` prints a version, if you installed `justx`.

`justx` is helpful but optional. A project should still work with plain `just`.

## Supported Platforms

This package is intended for:

- Linux
- WSL on Windows
- macOS
- Windows with WSL, Git Bash, MSYS, or another Bash-compatible shell

`just` itself can be installed on Windows, but the starter justfile recipes use Bash-style shell syntax. For native PowerShell or `cmd.exe`, use WSL/Git Bash or create a Windows-specific starter justfile.

`just` is the core tool. `justx` is optional. The install prompt asks the agent to detect the user's system before recommending commands.

## Validator Usage

Check a project folder:

```bash
python3 validate-justfile-setup.py /path/to/project
```

Require `justx` too:

```bash
python3 validate-justfile-setup.py /path/to/project --require-justx
```

Missing starter recipes are warnings unless `just --list` fails, `just` is missing, or the project has no justfile.

## Version

Status: v0.1.6 release candidate.

## Source Notes

Installation guidance was checked against:

- `just` official manual: https://just.systems/man/en/installation.html
- `just` package list: https://just.systems/man/en/packages.html
- `justx` official repository: https://github.com/fpgmaas/justx
