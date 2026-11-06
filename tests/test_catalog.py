"""Validate collection metadata, skill packages, profiles and workflow references."""
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=json.loads((ROOT/"catalog/collections.json").read_text(encoding="utf-8"))
class CatalogTests(unittest.TestCase):
 def test_all_skills_have_required_metadata_and_sections(self):
  seen=set()
  for domain,col in MANIFEST["collections"].items():
   for entry in col["skills"]:
    self.assertNotIn(entry["id"],seen);seen.add(entry["id"])
    source=ROOT/entry["source"];meta=json.loads((source/"skill.json").read_text(encoding="utf-8"));text=(source/"SKILL.md").read_text(encoding="utf-8")
    self.assertEqual(meta["id"],entry["id"]);self.assertEqual(meta["domain"],domain);self.assertRegex(meta["version"],r"^\d+\.\d+\.\d+$")
    if entry["source"].startswith("catalog/domains/"):\n     for section in ["## Inputs","## Procedure","## Outputs","## Quality checks","## Boundaries"]:self.assertIn(section,text)\n    else:self.assertIn("# ",text)
 def test_profiles_reference_known_collections(self):
  known=set(MANIFEST["collections"])
  for p in (ROOT/"profiles").glob("*/profile.json"):self.assertTrue(set(json.loads(p.read_text())["collections"]).issubset(known))
 def test_workflows_reference_known_skills(self):
  known={e["id"] for c in MANIFEST["collections"].values() for e in c["skills"]}
  for p in (ROOT/"workflows").glob("*/workflow.json"):
   for s in json.loads(p.read_text())["steps"]:self.assertIn(s["skill"],known)
if __name__=="__main__":unittest.main()
