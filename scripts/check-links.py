"""Validate built internal routes, assets and fragment targets at either Astro base."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import os
import sys

ROOT = Path(__file__).resolve().parents[1] / 'dist'
BASE = '/' + os.environ.get('ASTRO_BASE', '/').strip('/')
BASE = BASE.rstrip('/') + '/'
if not ROOT.is_dir():
    sys.exit('No dist/ output. Run npm run build successfully before checking links.')

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

pages = {p: Page(p.read_text()) for p in ROOT.rglob('*.html')}
errors = []
warnings = []
checked = 0
for path, page in pages.items():
    relative = path.relative_to(ROOT).as_posix()
    archived = relative.startswith(('legacy/', 'posts/'))
    origin = 'https://local.invalid' + BASE + relative
    for link in page.links:
        parsed = urlsplit(urljoin(origin, link))
        if parsed.scheme not in ('https', 'http') or parsed.netloc != 'local.invalid':
            continue
        checked += 1
        if not parsed.path.startswith(BASE):
            message = f'{relative}: URL escapes configured base: {link}'
        else:
            target = ROOT / unquote(parsed.path[len(BASE):])
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                message = f'{relative}: missing target: {link}'
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                message = f'{relative}: missing fragment: {link}'
            else:
                continue
        (warnings if archived else errors).append(message)
for message in warnings:
    print('ARCHIVE WARNING:', message)
for message in errors:
    print('ERROR:', message)
print(f'Checked {len(pages)} HTML pages and {checked} internal references at {BASE}; {len(errors)} errors, {len(warnings)} legacy warnings.')
if errors:
    sys.exit(1)
