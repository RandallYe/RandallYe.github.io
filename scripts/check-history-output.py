"""Check migrated history is discoverable and aliases use the configured base."""
from pathlib import Path
from html.parser import HTMLParser
import json, os
root=Path(__file__).resolve().parents[1]
base='/' + os.environ.get('ASTRO_BASE','/').strip('/')
base=base.rstrip('/')+'/'
class Page(HTMLParser):
    def __init__(self,path):
        super().__init__();self.ids=set();self.links=set();self.feed(path.read_text())
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.add(attrs['id'])
        if 'href' in attrs:self.links.add(attrs['href'])
news=json.loads((root/'src/data/news.json').read_text())
projects=json.loads((root/'src/data/projects.json').read_text())
news_page=Page(root/'dist/news/index.html')
research=Page(root/'dist/research/index.html')
about=Page(root/'dist/about/index.html')
home=Page(root/'dist/index.html')
assert all(item['id'] in news_page.ids for item in news)
assert base+'news/' in home.links
assert base+'research/#projects' in about.links
assert 'teaching' in about.ids
assert base+'talks/#isabelle-utp-tutorial-2019' in about.links
for project in projects:
    assert base+f"research/projects/{project['id']}/" in research.links
    Page(root/f"dist/research/projects/{project['id']}/index.html")
for alias in json.loads((root/'src/data/route-aliases.json').read_text()):
    if not alias['path'].startswith(('project/','news/','teaching/')):continue
    page=Page(root/f"dist/old_entry/{alias['path']}/index.html")
    assert base+alias['destination'] in page.links,alias['path']
print(f'History output passes at {base}: {len(projects)} projects, {len(news)} news records, teaching and source redirects.')
