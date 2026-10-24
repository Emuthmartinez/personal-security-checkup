"""Offline packaging checks. No network, accounts or scheduler access."""
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_relative_markdown_links_resolve_inside_package(self):
        checked = 0
        for source in ROOT.rglob('*.md'):
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', source.read_text()):
                if urlsplit(target).scheme or target.startswith('#'):
                    continue
                resolved = (source.parent / unquote(target.split('#')[0])).resolve()
                with self.subTest(source=str(source.relative_to(ROOT)), target=target):
                    self.assertTrue(resolved.is_relative_to(ROOT), 'link escapes package')
                    self.assertTrue(resolved.is_file(), 'missing packaged guide')
                checked += 1
        self.assertGreater(checked, 10, 'expected a linked portable skill package')

    def test_skill_metadata_is_available_to_loaders(self):
        text = (ROOT / 'SKILL.md').read_text()
        self.assertTrue(text.startswith('---\n'))
        header = text.split('---', 2)[1]
        fields = dict(line.split(': ', 1) for line in header.strip().splitlines())
        self.assertEqual(fields['name'], 'personal-security-checkup')
        self.assertTrue(fields['description'].strip())


if __name__ == '__main__':
    unittest.main()
