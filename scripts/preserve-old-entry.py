"""Preserve selected authored resources, verifying audit hashes before copying."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PREVIEWS = {'showcase/demonstration_of_probabilistic_relation/featured_hu7888d7cc804f4e8e895bb066cdd171ef_1109337_720x2500_fit_q75_h2_lanczos_3.webp'}
PREVIEWS.update({'showcase/animation_of_autonomous_chemical_detector/Featured_hud9be3fd51e9ded56112bb3323c9633e2_1004789_720x2500_fit_q75_h2_lanczos_3.webp', 'showcase/animation_of_patrol_robot/Featured_hu022584ec861fb5fb603cb43189fc6f04_1083944_720x2500_fit_q75_h2_lanczos_3.webp', 'showcase/animation_of_patrol_robot/PatrolMod_hu38db1eb6168b86b42bf1b461bf10a67e_2104495_1200x1200_fit_q75_h2_lanczos_3.webp', 'showcase/probabilistic_verification_of_robochart_using_prism/featured_hub5a9c5ab00d6cfe3a815a9fd2a1eab28_1167549_720x2500_fit_q75_h2_lanczos_3.webp', 'showcase/animation_of_patrol_robot/Corridor_sections_hu9c767e2eb6e7fe0b4aefa2a101f579ca_248902_1200x1200_fit_q75_h2_lanczos_3.webp'})
EXTENSIONS = {'.mp4', '.pdf', '.bib', '.csp', '.zip', '.png', '.jpg', '.jpeg', '.svg', '.webp'}


def preserve(source):
    audit = json.loads((ROOT / 'docs/old-entry-inventory.json').read_text())
    authored = [page for page in audit['contentPages'] if page['indexed']]
    prefixes = {str(Path(page['path']).parent) + '/' for page in authored}
    destinations = dict(re.findall(r'^\| `([^`]+)`.*? \| `([^`]+)`', (ROOT / 'docs/old-entry-merge-map.md').read_text(), re.M))
    selected = []
    for entry in audit['files']:
        path = entry['path']
        scope = any(path.startswith(prefix) for prefix in prefixes)
        scope |= path.startswith(('files/', 'uploads/', 'publication/ye-2016/'))
        if not scope or Path(path).suffix.lower() not in EXTENSIONS:
            continue
        if re.search(r'_hu[0-9a-f]', Path(path).name) and path not in PREVIEWS:
            continue
        consumers = set()
        for page in authored:
            if path.startswith(str(Path(page['path']).parent) + '/'):
                consumers.add(page['path'])
            for resource in page['resources']:
                url = urlsplit(urljoin('https://www-users.york.ac.uk/~ky582/old_entry/' + page['path'], resource['url']))
                if url.netloc == 'www-users.york.ac.uk':
                    relative = re.sub(r'^/(?:~?ky582)/old_entry/', '', unquote(url.path))
                    if relative == path:
                        consumers.add(page['path'])
        selected.append({**entry, 'publicPath': 'old_entry/' + path,
                         'consumers': [{'sourcePage': page, 'plannedDestination': destinations[page]} for page in sorted(consumers)],
                         'mediaPlayback': 'not-checked' if path.endswith('.mp4') else None})

    # Check every source and existing destination before making any copies.
    for entry in selected:
        original = source / entry['path']
        digest = hashlib.sha256(original.read_bytes()).hexdigest()
        if digest != entry['sha256']:
            raise ValueError(f'Source changed since audit: {entry["path"]}')
        target = ROOT / 'public' / entry['publicPath']
        if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            raise ValueError(f'Refusing to overwrite a different file: {target}')
    for entry in selected:
        target = ROOT / 'public' / entry['publicPath']
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copyfile(source / entry['path'], target)
    manifest = {'source': 'old_entry', 'audit': 'docs/old-entry-inventory.json', 'files': selected,
                'policy': 'Authored original media/downloads plus an explicitly selected genuine preview; unselected generated derivatives, stock samples and theme infrastructure excluded. The historical CV is retained under old_entry/uploads and does not replace the current CV.'}
    (ROOT / 'docs/old-entry-assets.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    print(f'Preserved {len(selected)} resources ({sum(f["bytes"] for f in selected):,} bytes), with source hashes and page dependencies.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    args = parser.parse_args()
    preserve(args.source.resolve())
