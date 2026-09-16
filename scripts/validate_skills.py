#!/usr/bin/env python3
"""Repository-level checks for skills in ./skills.

Specification compliance (frontmatter fields, name rules, description length)
is delegated to the official reference validator, `skills-ref`, when it is
installed. This script adds the repository's own conventions on top:

  * SKILL.md exists and stays under the 500-line guidance
  * frontmatter parses and name matches the directory
  * every relative file referenced from SKILL.md exists
  * references/sources.md exists
  * evals/evals.json is valid and has >= 3 scenarios with assertions
  * evals/trigger-evals.json is valid and has both positive and negative cases

Usage:
    python scripts/validate_skills.py            # validate every skill
    python scripts/validate_skills.py skills/x   # validate one skill
Exit code 0 when everything passes, 1 otherwise.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
MAX_SKILL_MD_LINES = 500
MIN_EVALS = 3
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> tuple[dict, str] | tuple[None, str]:
    """Minimal YAML frontmatter parser (flat key: value pairs, block scalars)."""
    if not text.startswith("---\n"):
        return None, "SKILL.md must start with '---' frontmatter"
    end = text.find("\n---", 4)
    if end == -1:
        return None, "frontmatter is not closed with '---'"
    block = text[4:end]
    data: dict = {}
    key = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) and key is not None:
            data[key] = (data[key] + " " + line.strip()).strip()
            continue
        if ":" not in line:
            return None, f"cannot parse frontmatter line: {line!r}"
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value in (">", "|", ">-", "|-"):
            value = ""
        data[key] = value.strip('"').strip("'") if value else ""
    return data, text[end + 4 :]


def check_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    lines = text.count("\n") + 1
    if lines > MAX_SKILL_MD_LINES:
        errors.append(f"{skill_dir.name}: SKILL.md has {lines} lines (limit {MAX_SKILL_MD_LINES})")

    fm, body = parse_frontmatter(text)
    if fm is None:
        return errors + [f"{skill_dir.name}: {body}"]

    name = fm.get("name", "")
    if not NAME_RE.match(name or ""):
        errors.append(f"{skill_dir.name}: invalid name {name!r}")
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: name {name!r} does not match directory")
    desc = fm.get("description", "")
    if not desc:
        errors.append(f"{skill_dir.name}: description is empty")
    elif len(desc) > 1024:
        errors.append(f"{skill_dir.name}: description is {len(desc)} chars (limit 1024)")
    elif len(desc) < 120:
        errors.append(f"{skill_dir.name}: description is only {len(desc)} chars; too short to route reliably")

    # Every relative path referenced from SKILL.md should exist.
    for ref in re.findall(r"\(((?:references|assets|scripts|evals)/[^)\s#]+)\)", body):
        if not (skill_dir / ref).exists():
            errors.append(f"{skill_dir.name}: SKILL.md references missing file {ref}")
    for ref in re.findall(r"`((?:references|assets|scripts|evals)/[^`\s]+)`", body):
        if not (skill_dir / ref).exists():
            errors.append(f"{skill_dir.name}: SKILL.md references missing file {ref}")

    if not (skill_dir / "references" / "sources.md").exists():
        errors.append(f"{skill_dir.name}: missing references/sources.md")

    errors += check_evals(skill_dir, name)
    errors += check_trigger_evals(skill_dir)
    return errors


def check_evals(skill_dir: Path, name: str) -> list[str]:
    path = skill_dir / "evals" / "evals.json"
    if not path.exists():
        return [f"{skill_dir.name}: missing evals/evals.json"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{skill_dir.name}: evals.json is not valid JSON ({exc})"]
    errors = []
    if data.get("skill_name") != name:
        errors.append(f"{skill_dir.name}: evals.json skill_name must equal {name!r}")
    evals = data.get("evals")
    if not isinstance(evals, list) or len(evals) < MIN_EVALS:
        return errors + [f"{skill_dir.name}: evals.json needs at least {MIN_EVALS} evals"]
    ids = set()
    for ev in evals:
        eid = ev.get("id")
        if eid in ids:
            errors.append(f"{skill_dir.name}: duplicate eval id {eid}")
        ids.add(eid)
        for field in ("id", "prompt", "expected_output", "assertions"):
            if field not in ev:
                errors.append(f"{skill_dir.name}: eval {eid} missing {field!r}")
        if not ev.get("assertions"):
            errors.append(f"{skill_dir.name}: eval {eid} has no assertions")
        for f in ev.get("files", []) or []:
            if not (skill_dir / f).exists():
                errors.append(f"{skill_dir.name}: eval {eid} references missing file {f}")
    return errors


def check_trigger_evals(skill_dir: Path) -> list[str]:
    path = skill_dir / "evals" / "trigger-evals.json"
    if not path.exists():
        return [f"{skill_dir.name}: missing evals/trigger-evals.json"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{skill_dir.name}: trigger-evals.json is not valid JSON ({exc})"]
    if not isinstance(data, list):
        return [f"{skill_dir.name}: trigger-evals.json must be a JSON array"]
    errors = []
    pos = neg = 0
    for item in data:
        if not isinstance(item, dict) or "query" not in item or "should_trigger" not in item:
            errors.append(f"{skill_dir.name}: trigger eval items need 'query' and 'should_trigger'")
            continue
        if item["should_trigger"]:
            pos += 1
        else:
            neg += 1
    if pos < 5 or neg < 5:
        errors.append(
            f"{skill_dir.name}: trigger-evals.json needs >=5 positive and >=5 negative cases (has {pos}/{neg})"
        )
    return errors


def run_reference_validator(skill_dirs: list[Path]) -> list[str]:
    """Run the official skills-ref validator if it is on PATH."""
    exe = shutil.which("skills-ref")
    if not exe:
        print("note: skills-ref not installed; skipping official spec validation")
        return []
    errors = []
    for d in skill_dirs:
        proc = subprocess.run([exe, "validate", str(d)], capture_output=True, text=True)
        if proc.returncode != 0:
            errors.append(f"{d.name}: skills-ref: {(proc.stdout + proc.stderr).strip()}")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        skill_dirs = [Path(a).resolve() for a in argv[1:]]
    else:
        skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))
    all_errors: list[str] = []
    for d in skill_dirs:
        errs = check_skill(d)
        all_errors += errs
        print(f"{'FAIL' if errs else 'ok  '} {d.relative_to(ROOT) if d.is_relative_to(ROOT) else d}")
    all_errors += run_reference_validator(skill_dirs)
    for e in all_errors:
        print(f"  - {e}")
    print(f"\n{len(skill_dirs)} skill(s) checked, {len(all_errors)} problem(s).")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
