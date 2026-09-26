#!/usr/bin/env python3
"""Validate the built site's public surface, markup and local links (stdlib only)."""
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.sources, self.headings = [], [], [], []
        self.canonical, self.refresh = [], False
        self.nested_paragraph = False
        self.in_paragraph = False
        self.main_count = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in ('script', 'img') and attrs.get('src'):
            self.sources.append(attrs['src'])
        if tag == 'link' and attrs.get('href'):
            if attrs.get('rel') == 'canonical':
                self.canonical.append(attrs['href'])
            elif attrs.get('rel') != 'alternate':
                self.sources.append(attrs['href'])
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.refresh = True
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headings.append(int(tag[1]))
        if tag == 'main':
            self.main_count += 1
        if tag == 'p':
            self.nested_paragraph |= self.in_paragraph
            self.in_paragraph = True

    def handle_endtag(self, tag):
        if tag == 'p':
            self.in_paragraph = False


root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
assert (root / 'index.html').exists(), f'Build the site first: {root}'
pages = {p: Page(p.read_text()) for p in root.rglob('*.html')}
errors = []
hosts = {'hwzhangcs.github.io', 'localhost', '127.0.0.1'}
for path, page in pages.items():
    rel = path.relative_to(root).as_posix()
    route = '/' + rel.removesuffix('index.html')
    if not page.refresh:
        if page.main_count != 1 or page.headings.count(1) != 1:
            errors.append(f'{rel}: expected one main and one h1')
        if page.nested_paragraph:
            errors.append(f'{rel}: nested paragraph markup')
        if len(page.canonical) != 1:
            errors.append(f'{rel}: expected one canonical URL')
        for previous, current in zip(page.headings, page.headings[1:]):
            if current > previous + 1:
                errors.append(f'{rel}: heading skips h{previous} to h{current}')
    duplicates = [key for key, count in Counter(page.ids).items() if count > 1]
    if duplicates:
        errors.append(f'{rel}: duplicate IDs {duplicates}')
    for link in page.links + page.sources:
        parsed = urlsplit(urljoin('https://hwzhangcs.github.io' + route, link))
        if parsed.scheme not in ('http', 'https') or parsed.hostname not in hosts:
            continue
        target = root / unquote(parsed.path).lstrip('/')
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'{rel}: missing local resource {link}')
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f'{rel}: missing anchor {link}')

expected = {'index.html', 'cv/index.html', 'publications/index.html', 'portfolio/index.html',
            'research/bone-to-shape/index.html', 'sitemap/index.html', '404.html', 'about.html', 'about/index.html',
            'cv-json/index.html', 'resume.html', 'resume-json.html',
            'portfolio/paper-refiner/index.html', 'portfolio/bouncing-birds/index.html',
            'portfolio/smart-pos-system/index.html', 'portfolio/network-threat-detection/index.html'}
actual = {p.relative_to(root).as_posix() for p in pages}
if actual != expected:
    errors.append(f'Unexpected public routes: added={actual - expected}, missing={expected - actual}')
for filename in ['sitemap.xml', 'feed.xml']:
    path = root / filename
    if path.exists():
        xml = ET.fromstring(path.read_text())
        for text in xml.itertext():
            if any(marker in text for marker in ['Blog Post number', 'Paper Title Number', '/markdown/', '/posts/', '/teaching/', '/talks/', '2199-']):
                errors.append(f'{filename}: template content leaked into output')
for rel in ['index.html', 'cv/index.html', 'portfolio/index.html', 'publications/index.html']:
    source = (root / rel).read_text()
    if any(marker in source for marker in ['main.min.js', 'MathJax-script', 'mermaid.esm', 'plotly.min.js']):
        errors.append(f'{rel}: unnecessary heavy script loaded')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(pages)} HTML pages; local links, anchors, heading structure, canonical URLs, public routes and template exclusions.')
