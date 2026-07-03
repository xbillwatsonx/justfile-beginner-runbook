#!/usr/bin/env python3
"""Basic checker for a project justfile.

This intentionally avoids dependencies so beginners and agents can run it
with a normal Python install.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


RECOMMENDED_RECIPES = {
    "default",
    "help",
    "menu",
    "agent-preflight",
    "agent-verify",
    "agent-status",
}

JUSTFILE_NAMES = ("justfile", "Justfile", ".justfile", ".Justfile")


def find_justfile(root: Path) -> Path | None:
    for name in JUSTFILE_NAMES:
        candidate = root / name
        if candidate.is_file():
            return candidate
    return None


def parse_recipe_names(text: str) -> set[str]:
    recipes: set[str] = set()
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.startswith((" ", "\t", "#", "@")):
            continue
        if ":" not in line:
            continue
        header = line.split(":", 1)[0].strip()
        name = header.split(None, 1)[0] if header else ""
        if not name or "=" in name:
            continue
        recipes.add(name)
    return recipes


def run_command(command: list[str], cwd: Path) -> tuple[int, str]:
    try:
        completed = subprocess.run(
            command,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    except FileNotFoundError:
        return 127, f"{command[0]} not found"
    return completed.returncode, completed.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a beginner justfile setup.")
    parser.add_argument("path", nargs="?", default=".", help="Project folder to check")
    parser.add_argument(
        "--require-justx",
        action="store_true",
        help="Fail if justx is not installed",
    )
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        errors.append(f"Path does not exist: {root}")
    elif not root.is_dir():
        errors.append(f"Path is not a directory: {root}")

    justfile = find_justfile(root) if not errors else None
    if justfile is None and not errors:
        errors.append(f"No justfile found in {root}")

    recipes: set[str] = set()
    if justfile is not None:
        recipes = parse_recipe_names(justfile.read_text(encoding="utf-8"))
        missing = sorted(RECOMMENDED_RECIPES - recipes)
        if missing:
            warnings.append("Missing recommended recipes: " + ", ".join(missing))

    if shutil.which("just") is None:
        errors.append("just is not installed or not on PATH")
    else:
        code, output = run_command(["just", "--list"], root)
        if code != 0:
            errors.append("just --list failed")
            warnings.append(output)

    if shutil.which("justx") is None:
        message = "justx is not installed or not on PATH"
        if args.require_justx:
            errors.append(message)
        else:
            warnings.append(message)

    print(f"Checked: {root}")
    if justfile is not None:
        print(f"Justfile: {justfile}")
        print("Recipes: " + (", ".join(sorted(recipes)) if recipes else "(none found)"))

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nOK: basic justfile setup checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
