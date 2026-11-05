from pathlib import Path
from html.parser import HTMLParser
import json, re, hashlib
import argparse
parser = argparse.ArgumentParser(description='Recover only the two user-selected historical posts.')
parser.add_argument('source', type=Path)
source = parser.parse_args().source.resolve()
root = Path(__file__).resolve().parents[1]
class Extract(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=False);self.depth=0;self.parts=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if not self.depth:
   if t=='div' and d.get('class')=='article-style':self.depth=1
   return
  if t=='div':self.depth+=1
  if t=='img':
   name='temporal-logic.png' if 'temporal-logic' in d.get('src','') else 'two-states.png' if 'two-states' in d.get('src','') else 'summary-steady-state_prob.png'
   folder='temporal-logic' if name=='temporal-logic.png' else 'steady_state_probabilities'
   self.parts.append(f'<a href="/old_entry/post/{folder}/{name}"><img src="/old_entry/post/{folder}/{name}" alt="{d.get("alt",name)}" loading="lazy" /></a>');return
  allowed={k:v for k,v in a if k in ['id','href','alt']}
  if t=='a':allowed.pop('target',None)
  if t.startswith('h') and len(t)==2 and t[1].isdigit():t='h'+str(min(int(t[1])+1,6))
  self.parts.append('<'+t+''.join(' '+k+'="'+v.replace('"','&quot;')+'"' for k,v in allowed.items() if v is not None)+'>')
 def handle_endtag(self,t):
  if not self.depth:return
  if t=='div':
   self.depth-=1
   if not self.depth:return
  if t.startswith('h') and len(t)==2 and t[1].isdigit():t='h'+str(min(int(t[1])+1,6))
  self.parts.append('</'+t+'>')
 def handle_data(self,s):
  if self.depth:self.parts.append(s)
 def handle_entityref(self,s):
  if self.depth:self.parts.append('&'+s+';')
 def handle_charref(self,s):
  if self.depth:self.parts.append('&#'+s+';')
posts=[]
for slug,old,title,date,summary,math in [
 ('temporal-logic','temporal-logic','Temporal Logic — history and semantics','2022-11-18','A timeline of temporal logics, from tense logic to branching-time and probabilistic logics.',False),
 ('steady-state-probabilities','steady_state_probabilities','Steady state probabilities of Markov chains','2022-11-23','Notes on recurrence, stationary distributions and limiting behaviour of Markov chains.',True)]:
 path=source/'post'/old/'index.html';p=Extract();p.feed(path.read_text());body=''.join(p.parts)
 thumb,alt={'temporal-logic':('old_entry/post/temporal-logic/temporal-logic.png','Timeline of temporal logics'),'steady-state-probabilities':('old_entry/post/steady_state_probabilities/summary-steady-state_prob.png','Diagram summarising steady-state probabilities')}[slug]
 posts.append(dict(id=slug,title=title,date=date,summary=summary,math=math,sourcePath='post/'+old+'/index.html',sourceSha256=hashlib.sha256(path.read_bytes()).hexdigest(),thumbnail='/'+thumb,thumbnailAlt=alt,thumbnailSource='post/'+old+'/'+Path(thumb).name,body=body))
data_path=root/'src/data/posts.json'
existing={post['id']:post for post in json.loads(data_path.read_text())} if data_path.exists() else {}
for post in posts: existing[post['id']]=post
all_posts=sorted(existing.values(),key=lambda post:post['date'],reverse=True)
data_path.write_text(json.dumps(all_posts,indent=2,ensure_ascii=False)+'\n')
p=root/'src/data/route-aliases.json';a=json.loads(p.read_text());a.extend(dict(path='post/'+post['sourcePath'].split('/')[1],destination='posts/'+post['id']+'/',title=post['title']) for post in posts);a=list({entry['path']:entry for entry in a}.values());p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n')
