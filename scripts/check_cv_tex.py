#!/usr/bin/env python3
"""Check that latex/cv.tex still states the key facts kept in _data/ (stdlib + PyYAML-free)."""
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
    'education.yml': ['gpa', 'weighted_average', 'rank', 'degree', 'program'],
    'honors.yml': ['title'],
    'publications.yml': ['title', 'doi', 'journal'],
    'ip.yml': ['title', 'number'],
}
missing = []
for filename, keys in checks.items():
    for key, value in scalars(filename):
        if key in keys:
            needle = value.replace('https://doi.org/', '')
            if needle.lower() not in plain.lower():
                missing.append(f'{filename}: {key} "{value}"')
for course in re.findall(r'name: ([^,}]+), score: (\d+)', (root / '_data' / 'education.yml').read_text()):
    if f'{course[0].strip()} ({course[1]})' not in plain:
        missing.append(f'education.yml: course "{course[0].strip()} ({course[1]})"')

if missing:
    print('latex/cv.tex is out of sync with _data/:')
    print('\n'.join(f'  - {item}' for item in missing))
    sys.exit(1)
print('PASS: latex/cv.tex matches education, honors, publications and IP data.')
