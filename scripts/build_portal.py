#!/usr/bin/env python3
"""Build a curated, static human/agent portal from the canonical Alamia catalogue."""
from __future__ import annotations
import json
import re
import shutil
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
MANIFEST = ROOT / "catalog" / "collections.json"
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main():
    manifest = read_json(MANIFEST)
    if manifest.get("schemaVersion") != 1 or not isinstance(manifest.get("collections"), dict):
        raise SystemExit("Unsupported or invalid collection manifest")
    SITE.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(SITE / "data", ignore_errors=True)
    (SITE / "assets").mkdir(parents=True, exist_ok=True)
    collections, skills, seen = [], [], set()
    for collection_id, collection in manifest["collections"].items():
        entries = []
        for item in collection.get("skills", []):
            skill_id, source = item.get("id"), item.get("source")
            if not isinstance(skill_id, str) or not ID_RE.fullmatch(skill_id) or skill_id in seen:
                raise SystemExit(f"Invalid or duplicate skill id: {skill_id!r}")
            seen.add(skill_id)
            source_path = (ROOT / source).resolve()
            if ROOT not in source_path.parents:
                raise SystemExit(f"Unsafe source path: {source!r}")
            metadata_path, skill_path = source_path / "skill.json", source_path / "SKILL.md"
            if not metadata_path.is_file() or not skill_path.is_file():
                raise SystemExit(f"Missing skill metadata or SKILL.md: {source}")
            metadata, markdown = read_json(metadata_path), skill_path.read_text(encoding="utf-8")
            if metadata.get("id") != skill_id:
                raise SystemExit(f"Metadata ID mismatch for {skill_id}")
            if metadata.get("domain") != collection_id:
                raise SystemExit(f"Domain/collection mismatch for {skill_id}: {metadata.get('domain')} != {collection_id}")
            md_url, json_url = f"data/skills/{skill_id}.md", f"data/skills/{skill_id}.json"
            write(SITE / md_url, markdown)
            public_metadata = {**metadata, "source": source, "collection": collection_id, "markdown": md_url, "metadata_url": json_url, "skill_page": f"skills/{skill_id}/"}
            write(SITE / json_url, json.dumps(public_metadata, indent=2, ensure_ascii=False) + "\n")
            item_data = public_metadata
            skills.append(item_data)
            entries.append(skill_id)
        collections.append({
            "id": collection_id,
            "title": collection.get("title", collection_id),
            "description": collection.get("description", ""),
            "skills": entries,
            "install": f"npx alamia-skills-install --{collection_id}",
        })
    profiles, workflows = [], []
    for path in sorted((ROOT / "profiles").glob("*/profile.json")):
        profiles.append(read_json(path))
    for path in sorted((ROOT / "workflows").glob("*/workflow.json")):
        workflows.append(read_json(path))
    catalogue = {"schemaVersion": 1, "name": manifest.get("name", "Alamia Skills"), "collections": collections, "skills": skills, "profiles": profiles, "workflows": workflows}
    write(SITE / "data/catalog.json", json.dumps(catalogue, indent=2, ensure_ascii=False) + "\n")
    skill_template = (SITE / "skill.html").read_text(encoding="utf-8")
    nested_template = skill_template.replace("<head>", "<head>\\n  <base href='../../'>", 1)
    for skill in skills:
        write(SITE / "skills" / skill["id"] / "index.html", nested_template)
    agents = {
        "name": "Alamia Skills System",
        "description": "Portable, reusable professional capabilities for compatible AI agents.",
        "catalog": "data/catalog.json",
        "collections": [{"id": c["id"], "title": c["title"], "skills": c["skills"]} for c in collections],
        "skill_resources": "data/skills/{skill_id}.md",
        "metadata_resources": "data/skills/{skill_id}.json",
        "skill_pages": "skills/{skill_id}/",
        "repository": "https://github.com/AlamiaSoft/Alamia-Skills-System",
        "install_prerequisites": "Node.js >=18; package publication status is documented in the repository README.",
    }
    write(SITE / "agents.json", json.dumps(agents, indent=2, ensure_ascii=False) + "\n")
    llms = [
        "# Alamia Skills System",
        "",
        "Portable, reusable professional capabilities for compatible AI agents.",
        "",
        "## Start here",
        "- Catalogue: data/catalog.json",
        "- Agent discovery: agents.json",
        "- Collections and skill resources are indexed in the catalogue.",
        "- Canonical source repository: https://github.com/AlamiaSoft/Alamia-Skills-System",
        "",
        "## Skill resource convention",
        "For each skill ID, read data/skills/{id}.json for metadata and data/skills/{id}.md for the complete agent-facing instructions.",
        "",
        "## Important semantics",
        "Skills describe capabilities. Collections group skills. Workflows compose skills as specifications; they are not an automated execution engine. Role profiles recommend collections and workflows.",
        "",
    ]
    write(SITE / "llms.txt", "\n".join(llms))
    base_url = "https://alamiasoft.github.io/Alamia-Skills-System/"
    urls = [base_url, base_url + "skill.html"] + [base_url + skill["skill_page"] for skill in skills]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{escape(u)}</loc></url>\n" for u in urls) + "</urlset>\n"
    write(SITE / "sitemap.xml", sitemap)
    write(SITE / ".nojekyll", "")
    print(f"Built portal for {len(skills)} skills across {len(collections)} collections.")

if __name__ == "__main__":
    main()
