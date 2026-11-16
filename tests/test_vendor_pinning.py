"""Regression tests for immutable third-party vendor restoration."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "core"))
from reconciler import _clone_pinned_repository, _load_vendor_dependency


class VendorPinningTests(unittest.TestCase):
    def test_provenance_manifest_records_immutable_pins(self):
        manifest = json.loads((ROOT / "vendor" / "UPSTREAMS.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema_version"], 1)
        dependencies = {item["name"]: item for item in manifest["dependencies"]}
        self.assertEqual(set(dependencies), {"mattpocock-skills", "agent-pm"})
        for dependency in dependencies.values():
            self.assertRegex(dependency["commit_sha"], r"^[0-9a-f]{40}$")
            self.assertTrue(dependency["source"].startswith("https://github.com/"))
            self.assertEqual(dependency["license"], "MIT")

    def test_dependency_loader_returns_only_declared_pin(self):
        dependency = _load_vendor_dependency(ROOT, "agent-pm")
        self.assertEqual(dependency["commit_sha"], "76d1a82ac0401221a00ca218f4eda72e7d344c12")
        self.assertIsNone(_load_vendor_dependency(ROOT, "unlisted-dependency"))

    def test_clone_checks_out_exact_commit(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            target = root / "vendor" / "dependency"
            source.mkdir()
            subprocess.run(["git", "init", str(source)], check=True, capture_output=True, text=True)
            subprocess.run(["git", "-C", str(source), "config", "user.name", "Vendor Test"], check=True)
            subprocess.run(["git", "-C", str(source), "config", "user.email", "vendor-test@example.invalid"], check=True)
            (source / "README.md").write_text("pinned content\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(source), "add", "README.md"], check=True)
            subprocess.run(["git", "-C", str(source), "commit", "-m", "initial"], check=True, capture_output=True, text=True)
            expected = subprocess.run(
                ["git", "-C", str(source), "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

            _clone_pinned_repository(str(source), target, expected)

            actual = subprocess.run(
                ["git", "-C", str(target), "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            self.assertEqual(actual, expected)
            self.assertEqual((target / "README.md").read_text(encoding="utf-8"), "pinned content\n")

    def test_clone_refuses_non_immutable_revision(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(ValueError):
                _clone_pinned_repository("https://github.com/example/repo", Path(temporary) / "repo", "main")


if __name__ == "__main__":
    unittest.main()
