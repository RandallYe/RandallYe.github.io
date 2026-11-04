"""Copy tracked legacy assets without changing the original source files."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIRS = ('CV', 'Cheddar', 'SEFM2024', 'pics', 'posts')
manifest = []
for folder in ASSET_DIRS:
    for source in sorted((ROOT / folder).rglob('*')):
        if not source.is_file():
            continue
        relative = source.relative_to(ROOT)
        target = ROOT / 'public' / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        manifest.append({'path': str(relative), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'bytes': source.stat().st_size})
(ROOT / 'public/legacy').mkdir(parents=True, exist_ok=True)
shutil.copyfile(ROOT / 'index.md', ROOT / 'public/legacy/index.md')
(ROOT / 'docs/legacy-assets.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(f'Preserved {len(manifest)} assets at their original paths.')
