"""Verify rendered canonical abstracts and bibliography resource links."""
from html.parser import HTMLParser
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1] / 'dist'
BASE = '/' + os.environ.get('ASTRO_BASE', '/').strip('/')
BASE = BASE.rstrip('/') + '/'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.abstracts = 0
        self.ids = set()
        self.links = []
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'summary': self._summary = True
        if attrs.get('id'): self.ids.add(attrs['id'])
        if tag == 'a': self.links.append(attrs.get('href', ''))
    def handle_data(self, data):
        if getattr(self, '_summary', False) and data.strip() == 'Abstract': self.abstracts += 1
    def handle_endtag(self, tag):
        if tag == 'summary': self._summary = False

path = ROOT / 'publications/index.html'
assert path.is_file()
page = Page(path)
assert page.abstracts == 9, page.abstracts
assert len([href for href in page.links if href.endswith('.bib')]) == 17
assert BASE + 'old_entry/publication/ye-2018/ye-2018.bib' in page.links
assert BASE + 'old_entry/publication/ye-2020/ye-2020.bib' in page.links
assert 'https://arxiv.org/abs/2410.00676' in page.links
assert 'https://arxiv.org/abs/2411.03943' in page.links
assert 'control-law-diagrams-technical-report' not in page.ids
print(f'Publication checks passed at {BASE}: nine source-backed abstracts, 17 BibTeX links, identified preprints and 2018 companion.')
