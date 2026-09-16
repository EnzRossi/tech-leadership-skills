"""Regression cases for malformed inputs previously accepted or crashing checks."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from validate_skills import (parse_frontmatter, check_evals, check_trigger_evals,
                             contained_file, check_links, run_reference_validator)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'evals').mkdir()

    def write(self, name, value):
        (self.root / 'evals' / name).write_text(json.dumps(value))

    def test_real_yaml_nested_metadata_and_block_description(self):
        fm, _ = parse_frontmatter('---\nname: x\ndescription: >-\n  first\n  second\nmetadata:\n  version: "0.2.0"\n---\nBody')
        self.assertEqual(fm['description'], 'first second')
        self.assertEqual(fm['metadata'], {'version': '0.2.0'})

    def test_duplicate_and_malformed_yaml(self):
        for text in ('---\nname: x\nname: y\n---\n', '---\nname: [\n---\n', '---\n- foo\n---\n'):
            self.assertIsNone(parse_frontmatter(text)[0])

    def test_eval_wrong_types_fail_without_crash(self):
        for value in ([], None, 'text', {'skill_name': 'x', 'evals': [None, [], 1]}):
            self.write('evals.json', value)
            self.assertTrue(check_evals(self.root, 'x'))

    def test_unhashable_ids_and_empty_assertions_fail(self):
        cases = [{'id': [], 'name': 'x', 'prompt': 'p', 'expected_output': 'e', 'files': [], 'assertions': []}] * 3
        self.write('evals.json', {'skill_name': 'x', 'evals': cases})
        self.assertTrue(check_evals(self.root, 'x'))

    def test_string_booleans_and_duplicates_fail(self):
        cases = [{'query': f'p{i}', 'should_trigger': True} for i in range(5)] + [{'query': f'n{i}', 'should_trigger': False} for i in range(5)]
        self.write('trigger-evals.json', cases)
        self.assertEqual(check_trigger_evals(self.root), [])
        self.write('trigger-evals.json', cases + [{'query': 'p0', 'should_trigger': 'false'}])
        self.assertTrue(check_trigger_evals(self.root))
        self.write('trigger-evals.json', cases + [cases[0]])
        self.assertTrue(check_trigger_evals(self.root))

    def test_paths_cannot_escape_or_follow_external_symlink(self):
        (self.root / 'inside.md').write_text('ok')
        (self.root / 'outside').symlink_to('/etc/hosts')
        self.assertTrue(contained_file(self.root, 'inside.md'))
        for value in ('/etc/hosts', '../missing', 'outside', {}, None):
            self.assertFalse(contained_file(self.root, value))

    def test_markdown_missing_local_link(self):
        path = self.root / 'doc.md'
        path.write_text('[missing](missing.md) [web](https://example.com)')
        self.assertEqual(len(check_links(path, self.root)), 1)

    def test_required_reference_cannot_silently_skip(self):
        with patch('validate_skills.shutil.which', return_value=None):
            self.assertTrue(run_reference_validator([], required=True))


if __name__ == '__main__':
    unittest.main()
