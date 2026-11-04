from pathlib import Path
import json,re
from html.parser import HTMLParser
root=Path(__file__).resolve().parents[1]
text=(root/'index.md').read_text()
section=text.split('# Publications\n',1)[1].split('# Talks and Presentations',1)[0]
section=re.sub(r'(^## [^\n]+)\n',r'\1\n\n',section,flags=re.M)
group=''; pubs=[]
for chunk in re.split(r'\n\s*\n',section):
    chunk=' '.join(chunk.split()).replace('\x12','')
    if chunk.startswith('## '):
        group=chunk[3:]
        continue
    if not re.match(r'\d+\.',chunk):continue
    citation=re.sub(r'^\d+\.\s*(?:\[==\*\*.*?\*\*==\]\s*)?','',chunk)
    urls=re.findall(r'https?://[^\s)]+',citation)
    url=urls[-1].rstrip('.,')
    if '“' in citation:
        authors,title_tail=citation.split('“',1)
        title,venue=title_tail.split('”',1)
        title=title.rstrip(',')
        venue=venue.lstrip(', ')
    else:
        # The two unquoted preprints have author lists ending before the title.
        marker='RoboCertProb:' if 'RoboCertProb:' in citation else 'Quantitative Assurance'
        authors,tail=citation.split(marker,1)
        title_tail=marker+tail
        title,venue=title_tail.split(', 2024.',1)
        venue='Preprint, 2024. '+venue
    year=int(re.search(r'\b(?:19|20)\d{2}\b',venue).group())
    venue=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',venue)
    venue=re.sub(r'https?://\S+','',venue).strip()
    pubs.append(dict(title=title.replace('$CSP\\,\\Vert \\,B$','CSP ∥ B'),authors=authors.rstrip(', '),venue=venue,year=year,url=url,group=group))
assert len(pubs)==20,len(pubs)
# Refresh source metadata while retaining canonical IDs and migrated resources.
existing_path = root / 'src/data/publications.json'
existing = {record['url']: record for record in json.loads(existing_path.read_text())} if existing_path.exists() else {}
pubs = [{**existing.get(record['url'], {}), **record} for record in pubs]
(root/'src/data/publications.json').write_text(json.dumps(pubs,indent=2,ensure_ascii=False)+'\n')
class Inventory(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.append(d['id'])
        for a in ('href','src'):
            if a in d:self.links.append(dict(tag=tag,attribute=a,url=d[a]))
p=Inventory();p.feed((root/'index.html').read_text())
(root/'docs/legacy-links.json').write_text(json.dumps(dict(sourceCommit='4544eec',ids=p.ids,links=p.links),indent=2)+'\n')
print(f'Extracted {len(pubs)} publications, {len(p.ids)} fragment IDs and {len(p.links)} link/asset references.')
