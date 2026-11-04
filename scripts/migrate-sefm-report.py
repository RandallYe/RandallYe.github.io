#!/usr/bin/env python3
"""Extract the latest-site SEFM/DataMod report into the validated Astro posts data."""
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'public/posts/SEFM_DataMod/SEFM_DataMod_2024.html'

class Extract(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.active = False
        self.depth = 0
        self.parts = []
        self.skip_title = False
        self.title_depth = 0
        self.title_removed = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if not self.active and tag == 'div' and 'markdown-preview' in values.get('class', '').split():
            self.active = True
            self.depth = 1
            return
        if not self.active:
            return
        if tag == 'div':
            self.depth += 1
        if tag == 'h2' and not self.title_removed:
            self.skip_title = True
            self.title_depth = 1
            self.title_removed = True
            return
        if self.skip_title:
            if tag == 'h2': self.title_depth += 1
            return
        allowed = {key: value for key, value in attrs if key in {'id', 'href', 'src', 'alt', 'title'} and value is not None}
        if tag == 'img' and allowed.get('src'):
            allowed['src'] = '/posts/SEFM_DataMod/' + Path(allowed['src']).name
        if re.fullmatch(r'h[3-6]', tag):
            tag = 'h' + str(int(tag[1]) - 1)
        self.parts.append('<' + tag + ''.join(f' {key}="{value.replace("&", "&amp;").replace(chr(34), "&quot;")}"' for key, value in allowed.items()) + '>')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if not self.active:
            return
        if self.skip_title:
            if tag == 'h2':
                self.title_depth -= 1
                if self.title_depth == 0:
                    self.skip_title = False
            return
        if re.fullmatch(r'h[3-6]', tag):
            tag = 'h' + str(int(tag[1]) - 1)
        if tag not in self.VOID:
            self.parts.append(f'</{tag}>')
        if tag == 'div':
            self.depth -= 1
            if self.depth == 0:
                self.active = False

    def handle_data(self, value):
        if self.active and not self.skip_title:
            self.parts.append(value)

    def handle_entityref(self, name):
        if self.active and not self.skip_title:
            self.parts.append(f'&{name};')

    def handle_charref(self, name):
        if self.active and not self.skip_title:
            self.parts.append(f'&#{name};')

source_bytes = SOURCE.read_bytes()
extractor = Extract()
extractor.feed(source_bytes.decode('utf-8'))
body = ''.join(extractor.parts)
if not body or len(re.findall(r'<img\b', body)) != 6:
    raise SystemExit('Could not extract the six expected original report figures')

posts_path = ROOT / 'src/data/posts.json'
posts = json.loads(posts_path.read_text())
posts = [post for post in posts if post['id'] != 'sefm-datamod-report']
posts.append({
    'id': 'sefm-datamod-report',
    'title': 'Application of formal verification in security protocols and O-RAN xApps',
    'date': '2024-11-04',
    'dateLabel': 'SEFM 2024 and DataMod 2024 · event week 4–8 November',
    'summary': 'A report from the SEFM and co-located DataMod 2024 events, covering work on sound animation for security protocols and quantitative verification for O-RAN xApps.',
    'math': False,
    'sourcePath': 'posts/SEFM_DataMod/SEFM_DataMod_2024.html',
    'sourceSha256': hashlib.sha256(source_bytes).hexdigest(),
    'body': body,
})
posts.sort(key=lambda post: post['date'], reverse=True)
posts_path.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + '\n')
