# Show all commands when running plain `just`
default:
    @just --list

# Show all commands
help:
    @just --list

# Open command menu
menu:
    @if command -v justx >/dev/null 2>&1; then justx; else echo "justx is not installed or not on PATH."; fi

# Validate the starter kit and checker
validate:
    python3 validate-justfile-setup.py starter-kit
    python3 -m py_compile validate-justfile-setup.py
    python3 -m unittest discover -s tests -v
    rm -rf __pycache__ tests/__pycache__

# Validate the optional justx installation too
validate-justx:
    python3 validate-justfile-setup.py starter-kit --require-justx

# Build the v0.1.7 downloadable zip from the explicit distribution manifest
package:
    mkdir -p downloads
    rm -f downloads/justfile-beginner-runbook-v0.1.7.zip
    zip -q downloads/justfile-beginner-runbook-v0.1.7.zip -@ < distribution-manifest.txt
    unzip -t downloads/justfile-beginner-runbook-v0.1.7.zip

# Agent preflight checks
agent-preflight:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; else echo "Not a Git repository."; fi
    just --list

# Agent verification after edits
agent-verify:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; git diff --check; git diff --stat; else echo "Not a Git repository."; fi
    just validate
    JUST_UNSTABLE=1 just --justfile justfile --fmt --check
    JUST_UNSTABLE=1 just --justfile starter-kit/justfile --fmt --check
    JUST_UNSTABLE=1 just --justfile examples/basic-justfile --fmt --check
    JUST_UNSTABLE=1 just --justfile examples/agent-standard-justfile --fmt --check

# Show current repo state
agent-status:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; git log --oneline -5; else echo "Not a Git repository."; fi
