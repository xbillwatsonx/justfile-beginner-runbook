# What Is a Justfile, And Why Should You Use One With Your AI Agents?

![A technical command hub connecting AI agents to repeatable project recipes](assets/justfile-ai-agents-header.png)

A justfile is a file that stores commands you use regularly. It gives your project a simple command menu, so you do not have to remember and type long commands every time you need them. And neither do your agents!

For example, imagine that checking your project requires this command:

```bash
python3 scripts/validate-project.py --check-config --check-dependencies
```

You could save that command in a justfile under a short name such as check. From then on, you would only need to run "`just check`". The long command still runs, but the justfile remembers it for you.

## What are just and justfile?

JUST is the program that runs your saved commands. The justfile is the file where those commands are stored.

Commands inside a justfile are called recipes. A recipe can contain one command or a series of commands that need to run together.

When you run `just --list`, just reads the project’s justfile and shows you all the available recipes. That list might include commands such as `just start`, `just test`, `just status`, `just build`, `just agent-preflight`, and `just agent-verify`.

You choose the recipe you need, and just runs the commands stored inside it.

## Why is this useful?

Most projects have important commands scattered across README files, package scripts, shell scripts, configuration files, old notes, and previous conversations with AI agents. This forces you to remember where everything is and how each command works.

A justfile puts the important commands in one place. You do not need to memorize every command or search through the entire project. You can run `just --list` and see the project’s command menu.

This is useful for beginners because you can give complicated commands simple names. You can also open the justfile and read exactly what each recipe will do before you run it.

## Why does this matter for AI agents?

AI agents face the same problem. When an agent enters a project, it must figure out how that project works. It may search through files, read documentation, inspect configuration, and try several commands before finding the correct procedure.

That takes time and uses AI tokens. It also creates opportunities for mistakes.

A justfile gives the agent a known starting point. The agent can run `just --list` and immediately see the project’s approved commands.

Instead of guessing how to run the tests, it can use `just test`. Instead of guessing how to inspect the project before making changes, it can use `just agent-preflight`. Instead of creating its own verification process, it can use `just agent-verify`.

Humans remember less, and agents guess less.

## What happened with Hermes?

I recently asked Hermes which AI model he was using. Our Hermes workspace already had a recipe designed to answer that question:

```bash
just model-current
```

Hermes did not use it. He manually opened his configuration file, searched through the settings, found the model, and reported the answer.

He got the correct answer, but he did unnecessary work. We had already created and tested the command he needed.

Alex and I updated Hermes’ instructions to add a justfile-first rule. We also added that rule to his durable memory so he would continue following it in future conversations.

For operational tasks, Hermes now checks `just help` or `just --list` first. If an existing recipe handles the task, he uses it. He only starts inspecting configuration files or assembling raw commands when no suitable recipe exists or when the recipe fails.

This does not prevent Hermes from investigating a problem. It simply gives him a reliable first place to look.

## How does this improve the system?

The first improvement is that it reduces guessing. The agent uses a known command instead of inventing a new procedure for a routine task.

It also reduces mistakes. The correct commands, file paths, options, and sequence of steps are already stored in the recipe. The agent does not have to reconstruct them from memory every time or reason through procedures that have already been solved. That leaves more of its reasoning budget available for work that actually requires judgment.

A justfile also creates consistency. The same recipe runs the same commands whether it is used by Hermes, OpenClaw, Codex, Claude, or any person working directly in the terminal.

This makes handoffs easier. A new agent can enter the project, run `just --list`, and quickly see how the project should be operated. Important procedures are no longer trapped in old conversations or dependent on one agent remembering them.

Troubleshooting becomes easier too. If a known recipe stops working, you have one procedure to inspect. Without a recipe, the agent might create a different command every time, which makes it harder to determine what changed or why something failed.

## What if there is no recipe?

A justfile does not replace the agent’s ability to reason. It gives the agent a reliable set of tools before asking it to improvise.

If the correct recipe does not exist, the agent can inspect the project and solve the problem. If an existing recipe fails, the agent can investigate the failure, repair the recipe, and test it again.

When a newly discovered procedure will be useful in the future, it can be added to the justfile. The next person or agent will not have to solve the same problem again.

The principle is simple: deterministic tools should handle repeatable work. AI reasoning should be used when the correct path is not already known.

## How do you get started?

We created the Justfile Beginner Runbook for people who have never used just or written a justfile. It explains what the tools are, how they work, and how to add a simple command menu to your own projects.

The runbook includes:

- A plain-language beginner guide
- A one-page quick-start card
- Copy-and-paste prompts for your AI agent
- A complete tutorial
- Example justfiles
- A starter justfile for your projects
- A dependency-free setup validator
- Instructions for Linux, WSL, macOS, and Bash-compatible Windows environments

You do not need Git to get started. You can download the release ZIP, extract it somewhere easy to find, and open the quick-start card. The included prompts can guide your AI agent through inspecting your system, explaining the correct installation method, and adding a justfile to your project.

JUST is the main tool that runs the recipes. JUSTX is an optional visual browser that makes the command menu easier to explore, but you do not need it for the justfile to work.

If you are tired of remembering long commands, or your AI agents keep rediscovering how your projects work, start with a justfile. Give the project a clear command menu, tell your agents to check it first, and add new recipes as repeated procedures come up.

Download the Justfile Beginner Runbook:
https://github.com/xbillwatsonx/justfile-beginner-runbook
