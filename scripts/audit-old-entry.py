from html.parser import HTMLParser
from pathlib import Path
import json,re
class Node:
 def __init__(self,tag='',attrs=()):self.tag=tag;self.attrs=dict(attrs);self.children=[]
 def text(self):return ' '.join(c.text() if isinstance(c,Node) else c for c in self.children if not isinstance(c,Node) or c.tag not in ['script','style'])
 def find(self,predicate):
  result=[self] if predicate(self) else []
  for c in self.children:
   if isinstance(c,Node):result+=c.find(predicate)
  return result
class Parse(HTMLParser):
 def __init__(self,text):super().__init__();self.root=Node();self.stack=[self.root];self.feed(text)
 def handle_starttag(self,t,a):
  n=Node(t,a);self.stack[-1].children.append(n)
  if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(n)
 def handle_endtag(self,t):
  for i in range(len(self.stack)-1,0,-1):
   if self.stack[i].tag==t:self.stack=self.stack[:i];break
 def handle_data(self,d):self.stack[-1].children.append(d)
def inspect(p):
 root=Parse(p.read_text(errors='replace')).root
 titles=root.find(lambda n:n.tag=='title');article=root.find(lambda n:'article-style' in n.attrs.get('class','').split())
 return {'title':titles[0].text() if titles else '', 'content':re.sub(r'\s+',' ',' '.join(n.text() for n in article)).strip(), 'links':[n.attrs for n in root.find(lambda n:n.tag in ['a','source','video','iframe','img','object'] and any(n.attrs.get(k) for k in ['href','src','srcset','poster','data']))], 'dates':[n.attrs for n in root.find(lambda n:n.tag=='time')], 'meta':[n.attrs for n in root.find(lambda n:n.tag=='meta' and n.attrs.get('name') in ['description','author'])]}

def audit(source, output):
 import hashlib
 from collections import Counter, defaultdict
 from datetime import datetime, timezone
 from urllib.parse import urljoin, urlsplit, unquote
 source = source.resolve()
 rows = json.loads((source / 'index.json').read_text())
 indexed = {row['relpermalink'].split('/old_entry/', 1)[-1].strip('/'): row for row in rows}
 files = []
 hashes = defaultdict(list)
 for path in sorted(source.rglob('*')):
  if not path.is_file(): continue
  digest = hashlib.sha256(path.read_bytes()).hexdigest()
  relative = path.relative_to(source).as_posix()
  files.append({'path': relative, 'bytes': path.stat().st_size, 'sha256': digest})
  hashes[digest].append(relative)
 sections = ['showcase', 'publication', 'talk', 'post', 'news', 'project', 'teaching']
 pages = []
 missing = []
 for section in sections:
  for path in sorted((source / section).glob('*/index.html')):
   relative = path.relative_to(source).as_posix()
   key = path.parent.relative_to(source).as_posix()
   row = indexed.get(key)
   detail = inspect(path)
   resources = []
   for link in detail.pop('links'):
    for attr in ('href', 'src', 'poster', 'data', 'srcset'):
     value = link.get(attr)
     if not value: continue
     urls = [part.strip().split()[0] for part in value.split(',') if part.strip()] if attr == 'srcset' else [value]
     for url in urls:
      resources.append({'attribute': attr, 'url': url})
      full = urlsplit(urljoin('https://www-users.york.ac.uk/~ky582/old_entry/' + relative, url))
      if full.netloc != 'www-users.york.ac.uk': continue
      prefix = next((p for p in ('/~ky582/old_entry/', '/ky582/old_entry/') if full.path.startswith(p)), None)
      if not prefix: continue
      target = source / unquote(full.path[len(prefix):])
      if target.is_dir(): target /= 'index.html'
      if not target.is_file(): missing.append({'page': relative, 'url': url, 'expectedPath': str(target.relative_to(source))})
   detail['contentExcerpt'] = detail.pop('content')[:700]
   pages.append({'path': relative, 'section': section, 'indexed': row is not None,
    'indexedDate': datetime.fromtimestamp(row['date'], timezone.utc).isoformat() if row else None,
    'sourceSummary': row.get('summary') if row else None, **detail, 'resources': resources})
 current_root = Path(__file__).resolve().parents[1]
 matches = []
 for path in sorted((current_root / 'public').rglob('*')):
  if path.is_file():
   digest = hashlib.sha256(path.read_bytes()).hexdigest()
   if digest in hashes: matches.append({'currentPath': path.relative_to(current_root).as_posix(), 'archivePaths': hashes[digest]})
 result = {'sourceRoot': str(source), 'auditDate': '2026-11-04',
  'summary': {'files': len(files), 'bytes': sum(f['bytes'] for f in files), 'extensions': dict(Counter(Path(f['path']).suffix.lower() for f in files)),
   'indexedRecords': len(rows), 'indexedSections': dict(Counter(r['section'] for r in rows)), 'contentPages': len(pages),
   'unindexedCandidatePages': [p['path'] for p in pages if not p['indexed']],
   'localMissingReferences': len({(x['page'], x['url']) for x in missing})},
  'files': files, 'contentPages': pages, 'missingLocalReferences': missing,
  'duplicateFileGroups': [paths for paths in hashes.values() if len(paths) > 1], 'identicalCurrentAssets': matches,
  'verificationLimits': ['HTML/search-index and local-byte inspection only; no external HTTP checks, media playback, codec checks or source-theory execution. Search-index exclusion alone is not proof that a page is a template.']}
 output.parent.mkdir(parents=True, exist_ok=True)
 output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
 print(json.dumps(result['summary'], indent=2))
 print(f'Exact byte matches with current public assets: {len(matches)}; report: {output}')

if __name__ == '__main__':
 import argparse
 parser = argparse.ArgumentParser(description='Read-only inventory of the supplied historical homepage export.')
 parser.add_argument('source', type=Path)
 parser.add_argument('--output', type=Path, default=Path('docs/old-entry-inventory.json'))
 args = parser.parse_args()
 audit(args.source, args.output)
