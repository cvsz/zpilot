from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import zpilot


class DotenvTests(unittest.TestCase):
    def test_parses_without_shell_expansion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / ".env"
            path.write_text("PLAIN=value\nQUOTED='two words'\nEXPANSION=$HOME\nexport ENABLED=yes # comment\n", encoding="utf-8")
            values = zpilot.dotenv(path)
            self.assertEqual(values["PLAIN"], "value")
            self.assertEqual(values["QUOTED"], "two words")
            self.assertEqual(values["EXPANSION"], "$HOME")
            self.assertEqual(values["ENABLED"], "yes")

    def test_rejects_invalid_key_and_unclosed_quote(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / ".env"
            path.write_text("BAD-KEY=value\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                zpilot.dotenv(path)
            path.write_text("VALUE='unterminated\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                zpilot.dotenv(path)


class AgentEnvironmentTests(unittest.TestCase):
    def test_agent_environment_drops_privileged_credentials(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = {
                "PATH": os.environ.get("PATH", ""),
                "HOME": directory,
                "GH_TOKEN": "github-secret",
                "GITHUB_TOKEN": "github-secret",
                "OPENAI_API_KEY": "provider-secret",
                "AWS_SECRET_ACCESS_KEY": "cloud-secret",
                "SSH_AUTH_SOCK": "/tmp/agent.sock",
            }
            with patch.dict(os.environ, source, clear=True):
                env = zpilot.agent_environment(Path(directory) / "isolated")
            self.assertIn("PATH", env)
            for key in ("GH_TOKEN", "GITHUB_TOKEN", "OPENAI_API_KEY", "AWS_SECRET_ACCESS_KEY", "SSH_AUTH_SOCK"):
                self.assertNotIn(key, env)
            self.assertTrue(Path(env["GH_CONFIG_DIR"]).is_dir())
            self.assertTrue(Path(env["GIT_CONFIG_GLOBAL"]).is_file())
            self.assertEqual(env["GIT_CONFIG_KEY_0"], "credential.helper")
            self.assertEqual(env["GIT_CONFIG_VALUE_0"], "")

    def test_output_redaction_masks_common_credentials(self) -> None:
        raw = "GH_TOKEN=github-secret Authorization: Bearer bearer-secret OPENAI_API_KEY=provider-secret"
        cleaned = zpilot.redact_output(raw)
        for secret in ("github-secret", "bearer-secret", "provider-secret"):
            self.assertNotIn(secret, cleaned)
        self.assertIn("[REDACTED]", cleaned)


class DiscoveryTests(unittest.TestCase):
    def test_discovers_nested_manifests_and_policy(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", "-b", "main"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "ZPilot Test"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "zpilot-test@example.invalid"], cwd=root, check=True)
            (root / "README.md").write_text("fixture\n", encoding="utf-8")
            (root / "zeaz.md").write_text("policy\n", encoding="utf-8")
            (root / "pyproject.toml").write_text("[project]\nname='fixture'\n", encoding="utf-8")
            nested = root / "services" / "api"
            nested.mkdir(parents=True)
            (nested / "go.mod").write_text("module example.invalid/api\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "fixture"], cwd=root, check=True)
            info = zpilot.discover(root)
            self.assertIn("Python", info["stacks"])
            self.assertIn("Go", info["stacks"])
            self.assertIn("zeaz.md", info["instructions"])
            self.assertTrue(info["clean"])

    def test_ignores_dependency_directories(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "node_modules").mkdir()
            (root / "node_modules" / "package.json").write_text("{}", encoding="utf-8")
            (root / "package.json").write_text(json.dumps({"scripts": {"test": "node test.js"}}), encoding="utf-8")
            names = {p.relative_to(root).as_posix() for p in zpilot.files_under(root)}
            self.assertIn("package.json", names)
            self.assertNotIn("node_modules/package.json", names)

    def test_selects_only_declared_package_scripts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "package.json").write_text(
                json.dumps({"scripts": {"test": "node test.js", "build": "node build.js"}}), encoding="utf-8")
            info = {"stacks": {"JavaScript/TypeScript": ["package.json"]}}
            with patch("zpilot.shutil.which", return_value="/usr/bin/npm"):
                plan = zpilot.validation_plan(root, info)
            names = [item[0] for item in plan]
            self.assertTrue(any(name.startswith("npm-test:") for name in names))
            self.assertTrue(any(name.startswith("npm-build:") for name in names))
            self.assertFalse(any("lint" in name or "typecheck" in name for name in names))


if __name__ == "__main__":
    unittest.main()
