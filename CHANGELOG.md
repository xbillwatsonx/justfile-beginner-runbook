# Changelog

## 0.1.3 - 2026-07-03

- Changed the quick-start install prompt wording to say `optional justx`.
- Updated README and packaging references for the v0.1.3 zip.

## 0.1.2 - 2026-07-03

- Made the install prompt align with optional `justx` setup.
- Added `default:` to the quick-start card's minimum starter recipe block.
- Renamed the validator's starter recipe set from required to recommended and added `default`.
- Clarified that missing starter recipes are validator warnings unless core setup checks fail.
- Updated README and packaging references for the v0.1.2 zip.

## 0.1.1 - 2026-07-02

- Narrowed Windows wording to WSL/Git Bash/MSYS/Bash-compatible shell path.
- Made `justx` optional in the friendly agent workflow.
- Corrected `justx run -g` examples to use source-qualified global recipes.
- Softened `set unstable` wording.
- Fixed validator parsing for parameterized recipes.
- Added README path chooser, safety note, download-without-Git instructions, and validator usage examples.
- Added `default:` to starter justfiles and root repo justfile.
- Normalized runbook heading numbering.
- Cleaned `examples/basic-justfile` output behavior.

## 0.1.0 - 2026-07-02

- Created first standalone draft package.
- Added main runbook, quick-start card, prompts, examples, starter justfile, checker script, and internal review plan.
- Revised starter recipes so non-Git folders show a friendly message instead of a fatal Git error.
- Removed references to unrelated runbook projects from user-facing package text.
- Added teaching prompt and included Bill's tutorial at `tutorial/justfile-and-justx-tutorial.md`.
- Added supported-platforms guidance for Linux, WSL, Windows, and macOS.
- Added first-20-minutes and success-check guidance for brand-new users.
- Corrected tutorial `justx` install/repository details and clarified that the tutorial is optional deeper learning.
- Removed specific internal agent-tool examples from the main runbook wording.
- Completed disposable-folder smoke test for a fresh project using the starter justfile.
- Added README mini-article explaining why justfiles matter for users, agents, and inference cost.
- Added external review and repo-plus-zip packaging plan to internal review plan.
- Applied Hermes review corrections: guarded tutorial menu recipes, added apt caveat, removed public README review reference, updated release-candidate status, clarified duplicate starter/example files, labeled example version output, and made tutorial paths generic.
- Added public-repo `.gitignore`.
