"""Account for all audited archive pages; verify exact-case static aliases and targets.

--write refreshes publication/poster aliases and the documentation report.
Without --write, validate the report and a build at ASTRO_BASE (no files changed).
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import json
import os

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = {
    'publication/conference-paper', 'publication/journal-article', 'publication/preprint',
    'talk/example-talk', 'post/getting-started', 'post/jupyter',
    'post/writing-technical-content', 'project/example', 'project/external-project',
}
EXCLUDED_POSTS = {
    'post/bdi_model', 'post/quantum_superposition', 'post/robosoft_evolving_robot',
    'post/robosoft_testing_robotic_systems', 'post/stochastic',
}
POSTERS = {
    'poster_animation_robochart_interaction_trees': 'tools/robochart-chemical-detector/#resources',
    'poster_probabilistic_modelling_and_verificaton': 'tools/robochart-prism/#resources',
    'poster_robostar_industry_exhibition_202210': 'tools/robochart-prism/#resources',
}

def read(path):
    return json.loads((ROOT / path).read_text())

def write(path, value):
    (ROOT / path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = set()
        self.refresh = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.add(attrs['href'])
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.refresh = attrs.get('content')

def report_and_aliases():
    inventory = read('docs/old-entry-inventory.json')
    hashes = {file['path']: file['sha256'] for file in inventory['files']}
    canonical = read('docs/canonical-content-map.json')
    aliases = read('src/data/route-aliases.json')
    assert len({entry['path'] for entry in aliases}) == len(aliases), 'Duplicate alias paths'
    mapped = {entry['path']: entry for entry in aliases}
    rows = []
    for page in inventory['contentPages']:
        path = page['path'].removesuffix('/index.html')
        title = page['title'].split(' | ')[0]
        if path in TEMPLATES:
            decision, reason = 'excluded-template', 'Stock theme example.'
        elif path in EXCLUDED_POSTS:
            decision, reason = 'excluded-by-user', 'Outside the two selected old-entry posts.'
        else:
            decision, reason = 'canonical', 'Migrated or merged into a canonical page.'
            section, slug = path.split('/', 1)
            if section == 'publication':
                work = canonical['publicationAliases'].get(slug) or canonical['companionReports'].get(slug)
                assert work, f'No canonical publication mapping: {path}'
                destination = f'publications/#{work}'
                if slug in canonical['companionReports']:
                    reason = 'Companion working report linked from the canonical chapter; not a separate publication.'
            elif section == 'showcase' and slug in POSTERS:
                destination = POSTERS[slug]
                reason = 'Poster edition linked from the related demonstration resources.'
            else:
                assert path in mapped, f'Unaccounted archive page: {path}'
                destination = mapped[path]['destination']
            expected = dict(path=path, destination=destination, title=title)
            if path in mapped:
                assert mapped[path]['destination'] == destination, f'Conflicting alias: {path}'
            else:
                aliases.append(expected)
                mapped[path] = expected
        excluded = decision != 'canonical'
        if excluded:
            assert path not in mapped, f'Excluded page has an alias: {path}'
        rows.append(dict(
            sourcePath=page['path'], sourceSha256=hashes[page['path']], title=title,
            directoryUrl=f'/old_entry/{path}/', exactFileUrl=f'/old_entry/{page["path"]}',
            decision=decision, destination=None if excluded else '/' + destination, reason=reason,
        ))
    summary = dict(Counter(row['decision'] for row in rows))
    assert len(rows) == 84 and summary == {'canonical': 70, 'excluded-template': 9, 'excluded-by-user': 5}, summary
    report = dict(
        inventory='docs/old-entry-inventory.json',
        scope='New-host aliases only; no claim of redirects on the historical external host.',
        summary=summary, pages=rows,
    )
    return report, aliases

def verify_build(report):
    base = '/' + os.environ.get('ASTRO_BASE', '/').strip('/')
    base = base.rstrip('/') + '/'
    dist = ROOT / 'dist'
    assert dist.is_dir(), 'Build first with the same ASTRO_BASE.'
    targets = {}
    for row in report['pages']:
        alias_file = dist / row['exactFileUrl'].lstrip('/')
        if row['decision'] != 'canonical':
            assert not alias_file.exists(), f'Excluded route was emitted: {alias_file}'
            continue
        assert alias_file.is_file(), f'Missing exact-case alias file: {alias_file}'
        alias = Page(alias_file)
        destination = base + row['destination'].lstrip('/')
        assert destination in alias.links, f'Missing fallback link: {alias_file}'
        assert alias.refresh == '0;url=' + destination, f'Wrong refresh target: {alias_file}'
        target = urlsplit(row['destination'])
        target_file = dist / target.path.lstrip('/')
        if target_file.is_dir():
            target_file /= 'index.html'
        assert target_file.is_file(), f'Missing canonical target: {target_file}'
        if target.fragment:
            if target_file not in targets:
                targets[target_file] = Page(target_file)
            assert unquote(target.fragment) in targets[target_file].ids, f'Missing target fragment: {destination}'
    # Check that preserved downloads are reachable from pages, not merely copied.
    links = set()
    for path in dist.rglob('*.html'):
        links.update(Page(path).links)
    downloads = 0
    for file in read('docs/old-entry-assets.json')['files']:
        if Path(file['path']).suffix not in {'.pdf', '.mp4', '.bib', '.zip', '.csp'}:
            continue
        if file['path'] == 'uploads/CV-KangfengYe.pdf':
            continue  # Preservation only; About promotes the current CV.
        assert base + file['publicPath'] in links, f'Unlinked preserved download: {file["path"]}'
        downloads += 1
    print(f'Route coverage passes at {base}: 70 canonical aliases, 9 excluded examples, 5 excluded posts; all 84 pages accounted for.')
    print(f'{downloads} preserved downloads are linked; the superseded CV is retained for preservation only.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    report, aliases = report_and_aliases()
    if args.write:
        write('src/data/route-aliases.json', aliases)
        write('docs/route-coverage.json', report)
        print('Updated aliases and docs/route-coverage.json:', report['summary'])
    else:
        assert aliases == read('src/data/route-aliases.json'), 'Alias data is stale; run npm run audit:routes.'
        assert report == read('docs/route-coverage.json'), 'Route report is stale; run npm run audit:routes.'
        verify_build(report)
