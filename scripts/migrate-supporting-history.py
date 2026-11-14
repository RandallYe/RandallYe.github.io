"""Reconcile project/news/teaching history from the two read-only local sources."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, parse_qs, unquote
import argparse, hashlib, json, re

parser = argparse.ArgumentParser()
parser.add_argument('archive', type=Path)
parser.add_argument('latest', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
inventory = json.loads((root / 'docs/old-entry-inventory.json').read_text())
entries = {entry['path']: entry for entry in inventory['contentPages']}
latest_path = args.latest / 'index.md'
latest = latest_path.read_text()
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path, value): (root / path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')
def yaml_list(key, items):
    if not items: return ''
    lines=[f'{key}:']
    for item in items:
        first=True
        for name,value in item.items():
            lines.append(f"  {'- ' if first else '  '}{name}: {value}")
            first=False
    return '\n'.join(lines) + '\n'
def news_note(record):
    """One markdown note per announcement; build-news.mjs compiles them to JSON."""
    front = '\n'.join([f"title: {record['title']}", f"date: {record['date']}", f"summary: {record['summary']}"])
    for key in ('eventDate', 'eventEndDate'):
        if record.get(key): front += f"\n{key}: {record[key]}"
    front += '\n' + yaml_list('resources', record['resources']) + yaml_list('provenance', record['provenance'])
    body = record.get('detail', '')
    return f"---\n{front}---\n" + (f"\n{body}\n" if body else '')
def plain(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'https?://\S+', '', text)
    return ' '.join(text.replace('==', '').replace('**', '').replace('_', ' ').split())
def resources(text):
    result = []
    for label, url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text):
        url = url.split(' \"', 1)[0].removeprefix('./')
        if url.startswith(('Posts/SEFM_DataMod/', 'posts/SEFM_DataMod/')): url = '/posts/sefm-datamod-report/'
        elif not url.startswith(('http://', 'https://', '/')): url = '/' + url
        result.append(dict(label=plain(label), url=url))
    return result
class Body(HTMLParser):
    def __init__(self): super().__init__(); self.depth=0; self.text=[]; self.links=[]; self.link=None
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='div' and (self.depth or attrs.get('class')=='article-style'): self.depth+=1
        if self.depth and tag=='a': self.link=[attrs.get('href', ''), []]
    def handle_endtag(self, tag):
        if self.depth and tag=='a' and self.link:
            url, words=self.link; self.link=None
            if url.startswith('https://www.google.com/url?'): url=parse_qs(urlsplit(url).query).get('url', [url])[0]
            if url.startswith(('https://','http://')):
                self.links.append(dict(label=' '.join(words).strip() or urlsplit(url).netloc, url=url))
        if self.depth and tag=='div': self.depth-=1
    def handle_data(self, text):
        if self.depth:
            self.text.append(text)
            if self.link: self.link[1].append(text)
def source(path):
    file=args.archive/path
    return dict(source='old_entry', path=path, sha256=digest(file))
latest_source=dict(source='GitHub', path='index.md', sha256=digest(latest_path))
aliases=json.loads((root/'src/data/route-aliases.json').read_text())
def alias(path, destination, title): aliases.append(dict(path=path.removesuffix('/index.html'), destination=destination, title=title))
projects=[]
for slug, old, title, period, summary, url, related in [
 ('cheddar','cheddar','CHEDDAR','February 2024 – November 2025','The Communications Hub for Empowering Distributed Cloud Computing Applications and Research.','https://cheddarhub.org/',['security-protocol-animation']),
 ('sesame','sesame','SESAME','June 2023 – January 2024','Secure and Safe Multi-Robot Systems, a Horizon 2020 project associated with the Automated Software Engineering group. Historical work with Simos Gerasimou addressed safety and security analysis of multiple robotic systems using probabilistic model checking.','https://www.sesame-project.org/',[]),
 ('robocalc-robotest','robocalc','RoboCalc and RoboTest','April 2018 – June 2023','EPSRC projects in the RoboStar group, supporting research in modelling and verification of robotic software.','https://robostar.cs.york.ac.uk/',['robochart-prism','robochart-chemical-detector','robochart-patrol-robot']),
 ('cyphyassure','cyphyassure','CyPhyAssure','June 2021 – September 2021','An EPSRC-funded project associated with Simon Foster’s fellowship and the RoboStar group.','https://www.cs.york.ac.uk/circus/CyPhyAssure/',[]),
 ('vetss','vetss','Compositional Assume-Guarantee Reasoning of Control Law Diagrams using UTP','October 2017 – March 2018','A VeTSS-sponsored project on compositional reasoning for discrete-time control-law diagrams.','https://vetss.org.uk/',[]),
 ('into-cps','into-csp','INTO-CPS','November 2016 – December 2017','Integrated Tool Chain for Model-based Design of Cyber-Physical Systems, an EU Horizon 2020 project. The project itself ran from 2015 to 2017; the dates here describe Randall’s participation.','https://into-cps.org/',['line-following-robot']),
]:
    path=f'project/{old}/index.html'; p=Body(); p.feed((args.archive/path).read_text())
    evidence=[source(path),latest_source]
    if old=='robocalc': evidence.insert(1,source('project/robotest/index.html'))
    record=dict(id=slug,title=title,period=period,summary=summary,detail=' '.join(' '.join(p.text).split()),resources=[dict(label='Project website',url=url),*p.links],relatedDemos=related,provenance=evidence)
    projects.append(record)
    alias(path,f'research/projects/{slug}/',title)
    if old=='robocalc':alias('project/robotest/index.html',f'research/projects/{slug}/',title)
write('src/data/projects.json',projects)
news=[]
# Latest-source announcements. Keep acceptance, preprint and publication milestones distinct.
section=latest.split('# News\n',1)[1].split('# Awards',1)[0]
for index, match in enumerate(re.finditer(r'^(\d{4}-\d{2}-\d{2})([^\n]*)\n((?:(?!\d{4}-\d{2}-\d{2}|## ).*\n)*)',section,re.M)):
    date, heading, body=match.groups(); body=re.sub(r'^:\s*','',body,flags=re.M).strip()
    if not body: continue
    # This duplicate SEFM announcement has a conflicting July event date; use the explicit November event.
    if date=='2024-07-09' and 'SEFM2024' in body: continue
    title=plain(re.sub(r'^\s*to\s+(?:\d{4}-\d{2}-)?\d{2}\s*:?\s*', '', heading)).strip(' :') or plain(body).split('. ')[0]
    title=title.replace('availabel','available')
    title={
        '2024-09-01': 'A Tour Through the Programming Choices — Festschrift contribution',
        '2024-09-12': 'ProbURel paper accepted by Theoretical Computer Science',
        '2024-09-25': 'ProbURel paper available online',
        '2024-08-22': 'Security protocol animation paper accepted by SEFM2024',
        '2023-12-19': 'RoboChart animation journal paper accepted by JLAMP',
        '2024-06-05': 'CHEDDAR meetings at the University of Glasgow',
    }.get(date,title)
    if len(title)>150:title=title[:147]+'…'
    event= re.search(r'to\s+(\d{4}-\d{2}-\d{2}|\d{2})',heading)
    event_end=(event.group(1) if len(event.group(1))==10 else date[:8]+event.group(1)) if event else None
    news.append(dict(id=f'current-{date}-{index+1}',date=date,title=title,summary=plain(body),resources=resources(heading+' '+body),eventDate=date if event else None,eventEndDate=event_end,provenance=[latest_source]))
# Preserve all 21 historical announcements, merging the JLAMP report into the latest-source acceptance entry.
for path, entry in entries.items():
    if entry['section']!='news' or not entry['indexed']: continue
    p=Body(); p.feed((args.archive/path).read_text())
    title=entry['title'].split(' | ')[0]
    slug=path.split('/')[1].replace('_','-')
    summary=plain(entry['sourceSummary'])
    detail=' '.join(' '.join(p.text).split())
    if path=='news/20231229_jlamp_paper_accepted_online/index.html':
        record=next(n for n in news if n['date']=='2023-12-19')
        record['provenance'].append(source(path)); record['detail']=summary+' '+detail
        record['resources']+=p.links
        alias(path,'news/#'+record['id'],title)
        continue
    record=dict(id=slug,date=entry['indexedDate'][:10],title=title,summary=summary or title,detail=detail,resources=resources(entry['sourceSummary'])+p.links,provenance=[source(path)])
    if slug=='20221011-robostar-industry-exhibition':record.update(eventDate='2022-10-11',eventEndDate='2022-10-12')
    if slug=='robosoft':record.update(eventDate='2019-11-13',eventEndDate='2019-11-14')
    if slug=='swu-cq-first-visit':record.update(eventDate='2018-07-24',eventEndDate='2018-07-26')
    if slug=='2022-sosym-first-paper-award':record.update(title='2022 SoSyM Journal-first award',summary='The award concerns Probabilistic Modelling and Verification Using RoboChart and PRISM. Announced on 1 January 2023.',resources=[dict(label='Paper and co-authors',url='/publications/#robochart-prism'),dict(label='SoSyM Journal-first award (PDF)',url='/old_entry/news/2022_sosym-first-paper-award/featured.pdf')])
    news.append(record);alias(path,'news/#'+slug,title)
# Link short historical announcements to their canonical resources.
links={
 '20240201-new-project-cheddar': ('Project history','/research/projects/cheddar/'),
 '20230627-new-project-sesame': ('Project history','/research/projects/sesame/'),
 '20221026-icfem2022-presentation': ('Presentation and recording','/talks/#icfem-2022-robochart-animation'),
 '20221027-models2022-presentation': ('Presentation and recording','/talks/#models-2022-probabilistic-robochart'),
 'accepted-paper-icfem2022': ('Paper and co-authors','/publications/#robochart-animation-icfem'),
}
for record in news:
    if record['id'] in links:
        label,url=links[record['id']];record['resources'].append(dict(label=label,url=url))
    record['resources']=list({item['url']:item for item in record['resources']}.values())
news.sort(key=lambda n:(n['date'],n['id']),reverse=True)
(root / 'src/content/news').mkdir(parents=True, exist_ok=True)
for record in news:
    (root / f"src/content/news/{record['id']}.md").write_text(news_note(record))

# Retain the module description and teaching role, without carrying over a current-role claim.
path='teaching/csav2018/index.html';p=Body();p.feed((args.archive/path).read_text())
teaching=[dict(id='csav-2018',title='CSAV — Concurrent System Analysis and Verification',period='Spring term, 2018–2019',summary='Teaching assistant for Jim Woodcock’s practical classes at the University of York. The module covered CSP and Circus for modelling, validation, design and verification of concurrent reactive systems.',resources=p.links,provenance=[source(path)])]
write('src/data/teaching.json',teaching)
alias(path,'about/#teaching','CSAV teaching')
write('src/data/route-aliases.json',list({a['path']:a for a in aliases}.values()))
print(f'{len(projects)} canonical projects from seven archive pages; {len(news)} announcements; {len(teaching)} teaching record.')
