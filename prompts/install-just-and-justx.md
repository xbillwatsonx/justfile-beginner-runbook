# Prompt: Install `just` and Optional `justx`

Copy this into your agent.

```text
Please help me install and verify just on this system, and optionally set up justx if I approve it.

First inspect the system and tell me:
- operating system
- whether this is Linux, WSL, macOS, or Windows with a Bash-compatible shell
- shell or terminal environment
- whether just is already installed
- whether justx is already installed
- whether uv, pipx, pip, brew, winget, scoop, apt, dnf, or another useful package manager is available
- whether any likely install path is missing from PATH

Do not install or change anything until you summarize what you found and recommend the simplest safe install path for this platform.

Use the platform's normal path when practical:
- Linux/WSL: system package manager, official binary installer, cargo, uv, or pipx
- Windows with Bash-compatible shell: winget, scoop, choco, cargo, uv, or pipx, depending on the shell and PATH
- macOS: brew, MacPorts, cargo, uv, or pipx

After I approve the install step, install just first and verify `just --version`.

Then ask whether I want the optional justx interactive menu. If I approve, install justx and verify `justx --version`. If I skip justx, continue with plain just.

After tool installation is verified, continue with the project setup:
- use `prompts/add-standard-justfile-to-project.md` for the justfile step so you inspect the project, propose the recipes before editing, preserve an existing justfile, and verify each underlying command
- run `just --list` and `just agent-preflight` if available
- add the durable justfile-first rule to `AGENTS.md` or the appropriate existing agent/harness instruction file, using `prompts/add-justfile-first-agent-rule.md`
- preserve existing instructions and do not duplicate an existing rule section
- review all changes with me
- ask me to confirm the workflow works before calling setup complete

In the final report, include:
- commands you ran
- versions installed
- whether justx was installed or skipped
- whether PATH changes were needed
- anything I need to restart or reopen
- the exact next command I should run to confirm it works

Do not consider setup complete until I confirm the workflow works.
```
