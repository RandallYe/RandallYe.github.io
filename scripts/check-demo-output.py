"""Check real built demo markup, media loading and the security-page regression."""
from html.parser import HTMLParser
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1] / 'dist'
BASE = '/' + os.environ.get('ASTRO_BASE', '/').strip('/')
BASE = BASE.rstrip('/') + '/'

class Media(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

demos = {
    'probabilistic-relations': ('proburel', 'Reasoning about probabilistic programs in Isabelle/HOL'),
    'robochart-prism': ('robochart-prism', 'Probabilistic verification of RoboChart using PRISM'),
    'robochart-chemical-detector': ('robochart-animation-icfem', 'Animation of an autonomous chemical detector'),
    'robochart-patrol-robot': ('robochart-animation-jlamp', 'Animation of a patrol robot model'),
}
recordings = set()
for slug, (paper, title) in demos.items():
    page = ROOT / f'tools/{slug}/index.html'
    media = Media(page)
    videos = [attrs for tag, attrs in media.tags if tag == 'video']
    assert len(videos) == 1, slug
    video = videos[0]
    assert 'controls' in video and video['preload'] == 'none'
    assert 'autoplay' not in video
    assert video['poster'].startswith(BASE + 'old_entry/')
    assert (ROOT / video['poster'][len(BASE):]).is_file()
    sources = [attrs['src'] for tag, attrs in media.tags if tag == 'source']
    assert len(sources) == 1 and sources[0].startswith(BASE + 'old_entry/')
    assert (ROOT / sources[0][len(BASE):]).is_file()
    recordings.add(sources[0])
    links = [attrs.get('href', '') for tag, attrs in media.tags if tag == 'a']
    assert BASE + f'publications/#{paper}' in links
    assert 'Needham–Schroeder' not in page.read_text()
    for route in ['index.html', 'tools/index.html']:
        text = (ROOT / route).read_text()
        assert text.count(title) == 1, (route, slug)
        assert BASE + f'tools/{slug}/' in text
assert len(recordings) == 4
for slug, count in [('robochart-prism', 1), ('robochart-patrol-robot', 2)]:
    media = Media(ROOT / f'tools/{slug}/index.html')
    figures = [attrs for tag, attrs in media.tags if tag == 'img' and '/showcase/' in attrs.get('src', '')]
    assert len(figures) == count
    assert all(attrs.get('alt') for attrs in figures)
security = (ROOT / 'tools/security-protocol-animation/index.html').read_text()
assert 'Needham–Schroeder' in security and 'Diffie–Hellman' in security
assert 'youtube-nocookie.com/embed/8FO6KT6EMqM' in security
assert not any(tag == 'iframe' for tag, _ in Media(ROOT / 'tools/security-protocol-animation/index.html').tags)
print(f'Demo output checks passed at {BASE}: four distinct local videos, model diagrams, deferred loading, canonical links, no duplicate cards and security fallback retained.')
