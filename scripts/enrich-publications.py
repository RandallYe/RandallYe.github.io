#!/usr/bin/env python3
"""Attach source-backed abstracts and archived bibliography versions to canonical records."""
from html.parser import HTMLParser
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]

# Select the archived record that matches the final canonical version, rather than
# picking a preprint/duplicate page by title alone.
ABSTRACT_SOURCES = {
    'reactive-relations-2018': 'foster-2018',
    'reactive-programs-calculation': 'foster-2021100681',
    'robostar-uncertainty': 'woodcock-2021',
    'circus-model-checking': 'ye-2017',
    'control-law-diagrams': 'ye-2020',
    'robochart-prism': 'ye-2021',
    'probabilistic-sequential-programs': 'ye-2021-a',
    'robochart-animation-icfem': 'ye-2022',
    'robochart-animation-jlamp': 'ye-2024100940',
}

BIB_SOURCES = {
    'agriculture-robot-light-treatment': [('10260395', 'cite.bib', 'Archived BibTeX')],
    'reactive-relations-2018': [('foster-2018', 'foster-2018.bib', 'Archived BibTeX'), ('foster-2018-a', 'foster-2018-a.bib', 'Archived BibTeX (earlier version)')],
    'reactive-programs-calculation': [('foster-2020-a', 'foster-2020-a.bib', 'Archived BibTeX (earlier version)'), ('foster-2021100681', 'cite.bib', 'Archived BibTeX')],
    'probabilistic-semantics-robochart': [('jim-2019', 'jim-2019.bib', 'Archived BibTeX')],
    'robostar-uncertainty': [('woodcock-2021', 'cite.bib', 'Archived BibTeX')],
    'circus-model-checking': [('ye-2017', 'ye-2017.bib', 'Archived BibTeX')],
    'control-law-diagrams': [('ye-2018', 'ye-2018.bib', '2018 working-report BibTeX'), ('ye-2020', 'ye-2020.bib', 'Archived BibTeX')],
    'probabilistic-sequential-programs': [('ye-2021-a', 'cite.bib', 'Archived BibTeX')],
    'robochart-animation-icfem': [('ye-2022', 'cite.bib', 'Archived BibTeX')],
    'robochart-animation-jlamp': [('ye-2023-formally', 'cite.bib', 'Archived BibTeX (preprint record)'), ('ye-2024100940', 'cite.bib', 'Archived BibTeX')],
    'proburel': [('ye-2023-probabilistic', 'cite.bib', 'Archived BibTeX (preprint record)')],
    'quantitative-activity-diagrams': [('ye-2024-quantitative', 'cite.bib', 'Archived BibTeX (preprint record)')],
    'state-rich-formalisms-thesis': [('ye-2016', 'ye-2016.bib', 'Archived BibTeX')],
}

PREPRINTS = {
    'security-protocol-animation': ('https://arxiv.org/abs/2410.00676', 'Preprint version'),
    'oran-energy-availability': ('https://arxiv.org/abs/2411.03943', 'Preprint version'),
}

class Abstract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.active = False
        self.depth = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'p' and 'pub-abstract' in values.get('class', '').split():
            self.active = True
            self.depth = 1
        elif self.active and tag not in {'br', 'img', 'hr', 'input'}:
            self.depth += 1

    def handle_endtag(self, tag):
        if self.active and tag not in {'br', 'img', 'hr', 'input'}:
            self.depth -= 1
            if self.depth <= 0:
                self.active = False

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_root', type=Path, help='Read-only old_entry export directory')
    source_root = parser.parse_args().source_root.resolve()
    data_path = ROOT / 'src/data/publications.json'
    records = json.loads(data_path.read_text())
    by_id = {record['id']: record for record in records}

    for canonical_id, old_slug in ABSTRACT_SOURCES.items():
        source = source_root / 'publication' / old_slug / 'index.html'
        raw = source.read_bytes()
        extracted = Abstract()
        extracted.feed(raw.decode('utf-8'))
        abstract = re.sub(r'\s+', ' ', ''.join(extracted.parts)).strip()
        if not abstract:
            raise SystemExit(f'No publication abstract found in {source}')
        # The archived conversion duplicated a TeX/Unicode CSP‖B expression.
        abstract = abstract.replace('$$CSP ∥ B$$CSP‖B', 'CSP‖B')
        record = by_id[canonical_id]
        record['abstract'] = abstract
        record['abstractSource'] = f'publication/{old_slug}/index.html'
        record['abstractSourceSha256'] = hashlib.sha256(raw).hexdigest()

    for canonical_id, versions in BIB_SOURCES.items():
        record = by_id[canonical_id]
        resources = record.setdefault('resources', [])
        known = {resource['url'] for resource in resources}
        for old_slug, filename, label in versions:
            url = f'/old_entry/publication/{old_slug}/{filename}'
            if url not in known:
                resources.append({'label': label, 'url': url})
                known.add(url)

    for canonical_id, (url, label) in PREPRINTS.items():
        record = by_id[canonical_id]
        resources = record.setdefault('resources', [])
        if not any(resource['url'] == url for resource in resources):
            resources.append({'label': label, 'url': url})

    records = [by_id[record['id']] for record in records]
    data_path.write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n')
    print(f'Enriched {len(ABSTRACT_SOURCES)} canonical abstracts, archived BibTeX links, and {len(PREPRINTS)} preprints.')

if __name__ == '__main__':
    main()
