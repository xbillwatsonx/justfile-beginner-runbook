# Prompt: Install `just` and `justx`

Copy this into your agent.

```text
Please help me install and verify just and justx on this system.

First inspect the system and tell me:
- operating system
- whether this is Linux, WSL, Windows, or macOS
- shell or terminal environment
- whether just is already installed
- whether justx is already installed
- whether uv, pipx, pip, brew, winget, scoop, apt, dnf, or another useful package manager is available
- whether any likely install path is missing from PATH

Do not install or change anything until you summarize what you found and recommend the simplest safe install path for this platform.

Use the platform's normal path when practical:
- Linux/WSL: system package manager, official binary installer, cargo, uv, or pipx
- Windows: winget, scoop, choco, cargo, uv, or pipx
- macOS: brew, MacPorts, cargo, uv, or pipx

After I approve the install step, install just first, verify `just --version`, then install justx and verify `justx --version`.

When done, report:
- commands you ran
- versions installed
- whether PATH changes were needed
- anything I need to restart or reopen
- the exact next command I should run to confirm it works
```
