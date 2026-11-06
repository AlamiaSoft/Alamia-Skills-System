"""Validate collection metadata, skill packages, profiles and workflow references."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "catalog" / "collections.json").read_text(encoding="utf-8"))


class CatalogTests(unittest.TestCase):
    def test_all_skills_have_required_metadata_and_sections(self):
        seen = set()
        for domain, collection in MANIFEST["collections"].items():
            for entry in collection["skills"]:
                self.assertNotIn(entry["id"], seen)
                seen.add(entry["id"])
                source = ROOT / entry["source"]
                metadata = json.loads((source / "skill.json").read_text(encoding="utf-8"))
                skill_text = (source / "SKILL.md").read_text(encoding="utf-8")
                self.assertEqual(metadata["id"], entry["id"])
                self.assertEqual(metadata["domain"], domain)
                self.assertRegex(metadata["version"], r"^\d+\.\d+\.\d+$")
                self.assertIn("# ", skill_text)
                if entry["source"].startswith("catalog/domains/"):
                    for section in ["## Inputs", "## Procedure", "## Outputs", "## Quality checks", "## Boundaries"]:
                        self.assertIn(section, skill_text, entry["id"])

    def test_profiles_reference_known_collections(self):
        known = set(MANIFEST["collections"])
        for profile_path in (ROOT / "profiles").glob("*/profile.json"):
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            self.assertTrue(set(profile["collections"]).issubset(known))

    def test_workflows_reference_known_skills(self):
        known = {
            entry["id"]
            for collection in MANIFEST["collections"].values()
            for entry in collection["skills"]
        }
        for workflow_path in (ROOT / "workflows").glob("*/workflow.json"):
            workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
            for step in workflow["steps"]:
                self.assertIn(step["skill"], known, workflow["id"])


if __name__ == "__main__":
    unittest.main()
