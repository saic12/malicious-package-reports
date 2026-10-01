"""Check every report and campaign file before it is published.

Run locally (python scripts/validate.py) or in CI. Standard library only.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ECOSYSTEMS = {"pypi": "PyPI", "npm": "npm"}
CATEGORIES = {"malicious", "pentest"}
TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

errors: list[str] = []
reports: dict[tuple[str, str], pathlib.Path] = {}


def fail(path: pathlib.Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


for eco_dir, eco in ECOSYSTEMS.items():
    for path in sorted((ROOT / eco_dir).rglob("*.json")):
        rel = path.relative_to(ROOT / eco_dir).parts
        if len(rel) < 3 or rel[0] not in CATEGORIES or rel[1] != "osv":
            fail(path, "expected <ecosystem>/<malicious|pentest>/osv/<name>.json")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as error:
            fail(path, f"not JSON: {error}")
            continue
        for key in ("schema_version", "published", "modified", "details", "affected", "credits"):
            if key not in data:
                fail(path, f"missing {key}")
        if "id" in data:
            fail(path, "id is assigned by OSSF; leave it out")
        for key in ("published", "modified"):
            if key in data and not TIME.match(str(data[key])):
                fail(path, f"{key} must be UTC like 2026-10-01T00:00:00Z")
        details = str(data.get("details", ""))
        if not 20 <= len(details) <= 700:
            fail(path, f"details length {len(details)} outside 20..700")
        affected = data.get("affected") or []
        if len(affected) != 1:
            fail(path, "affected must hold exactly one package")
            continue
        package = affected[0].get("package") or {}
        name = package.get("name", "")
        if package.get("ecosystem") != eco:
            fail(path, f"ecosystem must be {eco}")
        expected = "/".join(rel[2:])[: -len(".json")]
        if name != expected:
            fail(path, f"package name {name!r} does not match file path {expected!r}")
        if not affected[0].get("versions") and not affected[0].get("ranges"):
            fail(path, "list the affected versions")
        if (eco, name) in reports:
            fail(path, f"duplicate of {reports[(eco, name)].relative_to(ROOT)}")
        reports[(eco, name)] = path

known = {name for _, name in reports}
for path in sorted((ROOT / "campaigns").glob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("name") != path.stem:
        fail(path, "name must match the file name")
    for member in data.get("packages", []):
        if member not in known:
            fail(path, f"campaign lists {member!r}, which has no report")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(reports)} reports")
