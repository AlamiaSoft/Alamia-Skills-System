"""Integration checks for the generated static human/agent portal."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
MANIFEST = json.loads((ROOT / "catalog" / "collections.json").read_text(encoding="utf-8"))


class PortalBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_portal.py")], cwd=ROOT, check=True)
        cls.catalogue = json.loads((SITE / "data" / "catalog.json").read_text(encoding="utf-8"))

    def test_catalogue_matches_canonical_manifest(self):
        expected = sum(len(collection["skills"]) for collection in MANIFEST["collections"].values())
        self.assertEqual(len(self.catalogue["skills"]), expected)
        self.assertEqual(len({skill["id"] for skill in self.catalogue["skills"]}), expected)

    def test_every_skill_has_machine_and_human_resources(self):
        for skill in self.catalogue["skills"]:
            skill_id = skill["id"]
            self.assertTrue((SITE / skill["markdown"]).is_file(), skill_id)
            self.assertTrue((SITE / skill["metadata_url"]).is_file(), skill_id)
            self.assertTrue((SITE / skill["skill_page"] / "index.html").is_file(), skill_id)
            metadata = json.loads((SITE / skill["metadata_url"]).read_text(encoding="utf-8"))
            self.assertEqual(metadata["id"], skill_id)
            self.assertEqual(metadata["source"], skill["source"])
            self.assertEqual(metadata["collection"], skill["collection"])

    def test_agent_indexes_and_sitemap_include_all_skills(self):
        agents = json.loads((SITE / "agents.json").read_text(encoding="utf-8"))
        self.assertEqual(len(agents["collections"]), len(MANIFEST["collections"]))
        self.assertEqual(agents["skill_pages"], "skills/{skill_id}/")
        sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8")
        for skill in self.catalogue["skills"]:
            self.assertIn("skills/" + skill["id"] + "/", sitemap)
        self.assertTrue((SITE / "llms.txt").is_file())


if __name__ == "__main__":
    unittest.main()
