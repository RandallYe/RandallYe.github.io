"""Check research coverage, attribution, images and cross-links in either build base."""
from html.parser import HTMLParser
from pathlib import Path
import json
import os

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
BASE = '/' + os.environ.get('ASTRO_BASE', '/').strip('/')
BASE = BASE.rstrip('/') + '/'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = set()
        self.images = []
        self.selected = 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.add(attrs['href'])
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'article' and 'research-selected' in attrs.get('class', '').split():
            self.selected += 1

areas = json.loads((ROOT / 'src/data/research-areas.json').read_text())
publications = {paper['id'] for paper in json.loads((ROOT / 'src/data/publications.json').read_text())}
expected = {
    'semantics': {'proburel', 'probabilistic-designs', 'control-law-diagrams', 'abel-limit-theorem'},
    'probability': {'robochart-prism', 'activity-diagrams', 'oran'},
    'concurrency': {'circus', 'parser', 'interaction-trees', 'reactive-relations'},
    'security': {'protocol-animation', 'physical-layer-security'},
}
overview = Page(DIST / 'research/index.html')
home = Page(DIST / 'index.html')
assert overview.selected == 3
assert areas[0]['id'] == 'concurrency'
assert 'UTP &amp; Circus' in (DIST / 'research/index.html').read_text()
assert 'refinement checking' in (DIST / 'research/index.html').read_text()
assert 'refinement checking' in (DIST / 'index.html').read_text()
assert BASE + 'research/concurrency/#circus' in overview.links
assert 'projects' in overview.ids
covered = set()
contributions = 0
for area in areas:
    area_id = area['id']
    assert area_id in overview.ids, f'Lost existing research fragment: {area_id}'
    assert BASE + f'research/{area_id}/' in overview.links
    assert BASE + f'research/{area_id}/' in home.links
    assert {work['id'] for work in area['contributions']} == expected[area_id]
    page = Page(DIST / f'research/{area_id}/index.html')
    assert BASE + 'research/' in page.links
    for work in area['contributions']:
        contributions += 1
        assert work['id'] in page.ids
        assert BASE + f'research/{area_id}/#{work["id"]}' in overview.links
        for paper in work['relatedPublications']:
            covered.add(paper)
            assert BASE + f'publications/#{paper}' in page.links
        for demo in work['relatedDemos']:
            assert BASE + f'tools/{demo}/' in page.links
        for resource in work['resources']:
            url = resource['url']
            assert (BASE + url.lstrip('/') if url.startswith('/') else url) in page.links
    for project in area['relatedProjects']:
        assert BASE + f'research/projects/{project}/' in page.links
assert contributions == 13 and covered == publications
interests = Page(DIST / 'research/interests/index.html')
assert 'insresearch-interests-and-summaryins' in interests.ids, 'Lost the original research-interests fragment'
assert BASE + 'research/interests/' in overview.links
assert BASE + 'research/interests/' in home.links, 'Old research-interests fragment must reach the rebuilt page'
for area in areas:
    assert area['id'] in interests.ids
    for work in area['contributions']:
        assert BASE + f'research/{area["id"]}/#{work["id"]}' in interests.links
for path in ['pics/uvc_human.png', 'pics/PAL_use_case.png']:
    image = next(image for image in overview.images if image['src'] == BASE + path)
    assert image['alt'] and image['loading'] == 'lazy'
    assert BASE + path in overview.links, 'Technical diagram needs a full-size link'
concurrency = (DIST / 'research/concurrency/index.html').read_text()
assert 'only partly implemented' in concurrency
assert 'focused on verification of the reactive buffer' in concurrency
assert 'I do not claim authorship of the framework as a whole' in concurrency
security = (DIST / 'research/security/index.html').read_text()
assert 'animation soundness is separate' in security
print(f'Research output passes at {BASE}: four areas, 13 contributions, the research-interests summary, all 20 canonical works, original diagrams, demonstrations and scoped attribution.')
