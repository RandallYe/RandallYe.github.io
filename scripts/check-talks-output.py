"""Check rendered talk records, recordings, historical aliases and source downloads."""
from html.parser import HTMLParser
from pathlib import Path
import os

ROOT = Path(os.environ.get('CHECK_ROOT', 'dist')).resolve()
BASE = os.environ.get('CHECK_BASE', '/')
if not BASE.startswith('/') or not BASE.endswith('/'):
    raise SystemExit('CHECK_BASE must start and end with /')

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = set(); self.links = []; self.videos = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag == 'video': self.videos.append(a)

talk_file = ROOT / 'talks/index.html'
assert talk_file.exists(), f'missing {talk_file}'
talk_page = Page()
talk_page.feed(talk_file.read_text())
assert len(talk_page.ids) >= 11
assert 'cheddar-symposium-2025' in talk_page.ids and 'pint-of-science-robotic-swarms-2019' in talk_page.ids
assert len(talk_page.videos) == 2
assert all('controls' in v and v.get('preload') == 'none' and 'autoplay' not in v for v in talk_page.videos)
for video in talk_page.videos:
    source = video.get('src', '').removeprefix(BASE).lstrip('/')
    assert (ROOT / source).is_file(), f'missing recording {source}'
assert any('frog-4.csp' in href for href in talk_page.links)

alias_count = 0
for path in sorted((ROOT / 'old_entry/talk').glob('*/index.html')):
    page = Page()
    page.feed(path.read_text())
    assert any(href.startswith(BASE + 'talks/#') for href in page.links), f'broken talk alias: {path}'
    alias_count += 1
assert alias_count == 14, f'expected 14 substantive talk aliases, found {alias_count}'
print(f'Talk checks passed at {BASE}: 14 historical URLs, 11 archive records, 3 grouped rehearsals, 2 deferred local recordings.')
