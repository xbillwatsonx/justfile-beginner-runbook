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
    python3 validate-justfile-setup.py starter-kit --require-justx
    python3 -m py_compile validate-justfile-setup.py
    rm -rf __pycache__

# Build downloadable zip package
package:
    mkdir -p downloads
    rm -f downloads/justfile-beginner-runbook-v*.zip
    zip -r downloads/justfile-beginner-runbook-v0.1.2.zip . -x './.git/*' './downloads/*' './__pycache__/*'

# Agent preflight checks
agent-preflight:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; else echo "Not a Git repository."; fi
    just --list

# Agent verification after edits
agent-verify:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; git diff --stat; else echo "Not a Git repository."; fi
    just validate

# Show current repo state
agent-status:
    @if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git status; git log --oneline -5; else echo "Not a Git repository."; fi
