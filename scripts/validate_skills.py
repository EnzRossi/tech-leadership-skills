#!/usr/bin/env python3
"""Packaging and fixture checks, not behavioral evaluation.

Install scripts/requirements-validation.txt. Use --require-reference in CI.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parent.parent
FIELDS = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys rather than silently accepting the last value."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise ValueError('YAML keys must be unique strings')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def parse_frontmatter(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        return None, 'SKILL.md needs complete YAML frontmatter'
    try:
        data = yaml.load(match.group(1), Loader=UniqueLoader)
    except (yaml.YAMLError, ValueError, TypeError) as exc:
        return None, f'invalid YAML: {exc}'
    if not isinstance(data, dict):
        return None, 'frontmatter must be a mapping'
    return data, text[match.end():]


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def contained_file(base, value):
    if not nonempty(value) or Path(value).is_absolute():
        return False
    target = (base / value).resolve()
    return target.is_relative_to(base.resolve()) and target.is_file()


def load_json(path):
    try:
        return json.loads(path.read_text()), None
    except (OSError, ValueError) as exc:
        return None, f'{path.name}: {exc}'


def check_evals(skill_dir, name):
    data, error = load_json(skill_dir / 'evals/evals.json')
    if error:
        return [error]
    if not isinstance(data, dict):
        return ['evals.json must be an object']
    errors = []
    if data.get('skill_name') != name:
        errors.append('evals.json skill_name must match skill')
    cases = data.get('evals')
    if not isinstance(cases, list) or len(cases) < 3:
        return errors + ['evals.json needs at least 3 scenarios']
    ids, names = set(), set()
    for case in cases:
        if not isinstance(case, dict):
            errors.append('each eval must be an object')
            continue
        eid = case.get('id')
        if type(eid) is not int or eid < 1:
            errors.append('eval id must be a positive integer')
        elif eid in ids:
            errors.append(f'duplicate eval id {eid}')
        else:
            ids.add(eid)
        for field in ('name', 'prompt', 'expected_output'):
            if not nonempty(case.get(field)):
                errors.append(f'eval {eid}: {field} must be nonempty text')
        label = case.get('name')
        if nonempty(label):
            if label in names:
                errors.append(f'duplicate eval name {label}')
            names.add(label)
        assertions = case.get('assertions')
        if not isinstance(assertions, list) or not assertions or not all(nonempty(a) for a in assertions):
            errors.append(f'eval {eid}: assertions must be a nonempty list of text')
        files = case.get('files')
        if not isinstance(files, list):
            errors.append(f'eval {eid}: files must be a list')
        else:
            for file in files:
                if not contained_file(skill_dir, file):
                    errors.append(f'eval {eid}: missing or unsafe fixture path {file!r}')
    return errors


def check_trigger_evals(skill_dir):
    data, error = load_json(skill_dir / 'evals/trigger-evals.json')
    if error:
        return [error]
    if not isinstance(data, list):
        return ['trigger-evals.json must be an array']
    errors, queries, counts = [], set(), {True: 0, False: 0}
    for item in data:
        if not isinstance(item, dict) or not nonempty(item.get('query')) or type(item.get('should_trigger')) is not bool:
            errors.append('trigger items need nonempty query and boolean should_trigger')
            continue
        query = item['query'].strip().casefold()
        if query in queries:
            errors.append(f'duplicate trigger query: {item["query"]}')
        queries.add(query)
        counts[item['should_trigger']] += 1
    if min(counts.values()) < 5:
        errors.append('trigger fixtures need at least 5 positives and 5 negatives')
    return errors


def check_links(path, root=ROOT):
    """Check local inline Markdown destinations; remote URLs are a separate audit."""
    text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    errors = []
    for raw in re.findall(r'\]\(([^)]+)\)', text):
        target = raw.strip().strip('<>')
        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            continue
        if not parts.path:  # local heading anchors are not file references
            continue
        resolved = (path.parent / unquote(parts.path)).resolve()
        if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
            errors.append(f'{path.name}: missing or outside-repository link {target}')
    return errors


def check_skill(skill_dir):
    path = skill_dir / 'SKILL.md'
    if not path.is_file():
        return ['missing SKILL.md']
    text = path.read_text()
    fm, body = parse_frontmatter(text)
    if fm is None:
        return [body]
    errors = []
    if len(text.splitlines()) > 500:
        errors.append('SKILL.md exceeds repository 500-line limit')
    if not body.strip():
        errors.append('SKILL.md body is empty')
    if set(fm) - FIELDS:
        errors.append(f'unknown frontmatter fields: {sorted(set(fm) - FIELDS)}')
    name = fm.get('name')
    if not isinstance(name, str) or len(name) > 64 or not NAME_RE.fullmatch(name):
        errors.append('name must be 1–64 lowercase letters/digits with single hyphens')
    if name != skill_dir.name:
        errors.append('name must match skill directory')
    if not nonempty(fm.get('description')) or len(fm['description']) > 1024:
        errors.append('description must be 1–1024 characters')
    if 'metadata' in fm and (not isinstance(fm['metadata'], dict) or not all(isinstance(v, str) for v in fm['metadata'].values())):
        errors.append('metadata values must be strings')
    for field in ('license', 'compatibility', 'allowed-tools'):
        if field in fm and not nonempty(fm[field]):
            errors.append(f'{field} must be nonempty text')
    for required in ('references/methodology.md', 'references/sources.md', 'assets/output-template.md'):
        if not contained_file(skill_dir, required):
            errors.append(f'missing or unsafe {required}')
    for ref in re.findall(r'`((?:references|assets|scripts|evals)/[^`\s]+)`', body):
        if not contained_file(skill_dir, ref):
            errors.append(f'missing or unsafe reference {ref}')
    errors += check_evals(skill_dir, name)
    errors += check_trigger_evals(skill_dir)
    return errors


def run_reference_validator(skill_dirs, required=False):
    exe = shutil.which('skills-ref')
    if not exe:
        if required:
            return ['skills-ref not installed; official validation required']
        print('NOTE: official validation SKIPPED (skills-ref not installed)')
        return []
    errors = []
    for directory in skill_dirs:
        proc = subprocess.run([exe, 'validate', str(directory)], capture_output=True, text=True)
        if proc.returncode:
            errors.append(f'{directory.name}: skills-ref: {(proc.stdout + proc.stderr).strip()}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skills', nargs='*', type=Path)
    parser.add_argument('--require-reference', action='store_true')
    args = parser.parse_args()
    dirs = args.skills or sorted(p for p in (ROOT / 'skills').iterdir() if p.is_dir())
    errors = []
    if not dirs:
        errors.append('no skills found')
    for directory in dirs:
        found = check_skill(directory)
        errors.extend(f'{directory.name}: {e}' for e in found)
        print(f'{"FAIL" if found else "ok"} {directory.name}')
    # Repository Markdown only, excluding ignored local tooling and git internals.
    for base in [ROOT / 'docs', ROOT / 'skills', ROOT / 'templates']:
        for path in base.rglob('*.md'):
            errors += check_links(path)
    for path in ROOT.glob('*.md'):
        errors += check_links(path)
    errors += run_reference_validator(dirs, args.require_reference)
    for error in errors:
        print(f'  - {error}')
    print(f'{len(dirs)} skills checked, {len(errors)} problems. No model evaluations run.')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
