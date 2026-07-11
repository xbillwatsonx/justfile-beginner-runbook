import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "validate-justfile-setup.py"


class ValidatorCliTests(unittest.TestCase):
    def test_malformed_utf8_is_reported_without_traceback(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "justfile").write_bytes(b"default:\n    @echo ok\n\xff")

            result = subprocess.run(
                [sys.executable, str(VALIDATOR), str(project)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("not valid UTF-8", result.stdout)
        self.assertNotIn("Traceback", result.stdout)


class ReleaseConfigurationTests(unittest.TestCase):
    def test_run_scene_resolves_one_numbered_scene_before_calling_godot(self):
        tutorial = (
            REPO_ROOT / "tutorial" / "justfile-and-justx-tutorial.md"
        ).read_text(encoding="utf-8")
        blocks = re.findall(r"```just\n(.*?)```", tutorial, flags=re.DOTALL)
        godot_block = next(block for block in blocks if "# godot-sandbox" in block)

        with tempfile.TemporaryDirectory() as temporary_directory:
            project = Path(temporary_directory)
            (project / "justfile").write_text(godot_block, encoding="utf-8")
            (project / "project.godot").write_text("[application]\n", encoding="utf-8")
            scene = project / "scenes" / "12-test" / "main.tscn"
            scene.parent.mkdir(parents=True)
            scene.write_text("[gd_scene]\n", encoding="utf-8")
            binary_directory = project / "bin"
            binary_directory.mkdir()
            godot_log = project / "godot-args.txt"
            stub = binary_directory / "godot"
            stub.write_text(
                "#!/usr/bin/env bash\nprintf '%s\\n' \"$@\" > \"$GODOT_LOG\"\n",
                encoding="utf-8",
            )
            stub.chmod(0o755)
            environment = os.environ.copy()
            environment["PATH"] = f"{binary_directory}:{environment['PATH']}"
            environment["GODOT_LOG"] = str(godot_log)

            result = subprocess.run(
                ["just", "run-scene", "12"],
                cwd=project,
                env=environment,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            logged_arguments = godot_log.read_text(encoding="utf-8").splitlines()

        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(
            logged_arguments,
            ["project.godot", "res://scenes/12-test/main.tscn"],
        )

    def test_tutorial_quotes_user_controlled_recipe_parameters(self):
        tutorial = (
            REPO_ROOT / "tutorial" / "justfile-and-justx-tutorial.md"
        ).read_text(encoding="utf-8")

        unsafe_fragments = [
            '"Hello, {{name}}!',
            '"{{name}} loaded!',
            'extensions/{{name}}.ts',
            '> {{out}}',
            '-t "{{name}}"',
        ]
        for fragment in unsafe_fragments:
            with self.subTest(fragment=fragment):
                self.assertNotIn(fragment, tutorial)

    def test_package_recipe_uses_v017_and_explicit_manifest(self):
        justfile = (REPO_ROOT / "justfile").read_text(encoding="utf-8")

        self.assertIn("justfile-beginner-runbook-v0.1.7.zip", justfile)
        self.assertIn("distribution-manifest.txt", justfile)
        self.assertNotIn("zip -r", justfile)

    def test_justfile_first_prompt_has_required_durable_workflow(self):
        prompt_path = REPO_ROOT / "prompts" / "add-justfile-first-agent-rule.md"
        self.assertTrue(prompt_path.is_file())
        prompt = prompt_path.read_text(encoding="utf-8")

        required_text = [
            "AGENTS.md",
            "just --list",
            "just agent-preflight",
            "## Justfile-First Workflow",
            "Do not duplicate",
            "confirm",
        ]
        for text in required_text:
            with self.subTest(text=text):
                self.assertIn(text, prompt)

    def test_distribution_manifest_includes_article_header_and_agent_rule_prompt(self):
        manifest = (REPO_ROOT / "distribution-manifest.txt").read_text(
            encoding="utf-8"
        )

        self.assertIn("why-you-should-use-justfile-with-agents.md", manifest)
        self.assertIn("assets/justfile-ai-agents-header.png", manifest)
        self.assertIn("prompts/add-justfile-first-agent-rule.md", manifest)

    def test_v017_zip_matches_manifest_and_has_no_corrupt_member(self):
        manifest = [
            line
            for line in (REPO_ROOT / "distribution-manifest.txt")
            .read_text(encoding="utf-8")
            .splitlines()
            if line
        ]
        package = REPO_ROOT / "downloads" / "justfile-beginner-runbook-v0.1.7.zip"

        with ZipFile(package) as archive:
            self.assertEqual(archive.namelist(), manifest)
            self.assertIn("prompts/add-justfile-first-agent-rule.md", archive.namelist())
            self.assertIsNone(archive.testzip())


if __name__ == "__main__":
    unittest.main()
