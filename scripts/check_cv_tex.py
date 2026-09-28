#!/usr/bin/env python3
"""Check that the one-page latex/cv.tex states its selected core facts."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
tex = (root / 'latex' / 'cv.tex').read_text()
# Undo the LaTeX escapes and spacing used in the source so plain strings can be compared.
plain = re.sub(r'\\([%&_#$])', r'\1', tex).replace('--', '-')
plain = re.sub(r'\s+', ' ', plain)


def scalars(path):
    """Collect `key: value` scalars from a simple YAML file without a YAML dependency."""
    values = []
    for line in (root / '_data' / path).read_text().splitlines():
        match = re.match(r'\s*-?\s*(\w+)\s*:\s*"?([^"#{][^"#]*?)"?\s*$', line)
        if match:
            values.append((match.group(1), match.group(2).strip()))
    return values


checks = {
    # The PDF keeps the stronger GPA/rank signal and omits the redundant weighted average.
    'education.yml': ['gpa', 'rank', 'degree'],
    'publications.yml': ['title', 'doi', 'journal'],
}
missing = []
for filename, keys in checks.items():
    for key, value in scalars(filename):
        if key in keys:
            needle = value.replace('https://doi.org/', '')
            if needle.lower() not in plain.lower():
                missing.append(f'{filename}: {key} "{value}"')
# The one-page CV intentionally lists representative coursework rather than every course.
required_one_page_facts = [
    'First-Class Single-Category Scholarship',
    'Provincial Third Prize, Ascend AI Track',
    'Third Prize, Sichuan Division',
    'Animal 3D Reconstruction Using Body-Shape Priors',
    '202611403381.7',
]
for fact in required_one_page_facts:
    if fact.lower() not in plain.lower():
        missing.append(f'one-page CV fact "{fact}"')

if missing:
    print('latex/cv.tex is out of sync with _data/:')
    print('\n'.join(f'  - {item}' for item in missing))
    sys.exit(1)
print('PASS: one-page latex/cv.tex matches selected education, publication, patent and honor facts.')
