"""Verify selected posts, original figures, internal anchors and server-rendered maths."""
from pathlib import Path
from html.parser import HTMLParser
import os

ROOT = Path(__file__).resolve().parents[1] / 'dist'
BASE = '/' + os.environ.get('ASTRO_BASE', '/').strip('/')
BASE = BASE.rstrip('/') + '/'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.math = 0
        self.images = []
        self.links = []
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'math': self.math += 1
        if tag == 'img' and '/post/' in attrs.get('src', ''): self.images.append(attrs)
        if tag == 'a': self.links.append(attrs.get('href', ''))

index = ROOT / 'posts/index.html'
assert index.is_file()
listing = Page(index)
for slug in ['temporal-logic', 'steady-state-probabilities']:
    assert BASE + f'posts/{slug}/' in listing.links
    path = ROOT / f'posts/{slug}/index.html'
    page = Page(path)
    assert page.images and all(image.get('alt') for image in page.images)
    assert all(image['src'].startswith(BASE + 'old_entry/') for image in page.images)
    if slug == 'steady-state-probabilities':
        assert page.math > 50, page.math
        assert 'Historical working notes' in path.read_text()
        assert 'katex-error' not in path.read_text()
    else:
        assert page.math == 0
        assert 'https://plato.stanford.edu/entries/logic-temporal/' in page.links
for excluded in ['quantum-superposition', 'stochastic', 'bdi-model', 'robosoft-evolving-robot', 'robosoft-testing-robotic-systems']:
    assert not (ROOT / f'posts/{excluded}/index.html').exists()
print(f'Two-post output checks passed at {BASE}: original figures/references, native MathML and requested scope.')
