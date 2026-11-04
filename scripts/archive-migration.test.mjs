import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
const root = new URL('../', import.meta.url);
const read = path => readFileSync(new URL(path, root));
const json = path => JSON.parse(read(path));

test('recovered resources match the audited originals without importing template assets', () => {
  const audit = new Map(json('docs/old-entry-inventory.json').files.map(file => [file.path, file]));
  const manifest = json('docs/old-entry-assets.json').files;
  assert.equal(manifest.filter(file => file.path.endsWith('.mp4')).length, 9);
  for (const file of manifest) {
    assert.equal(file.sha256, audit.get(file.path).sha256, file.path);
    assert.equal(createHash('sha256').update(read(`public/${file.publicPath}`)).digest('hex'), file.sha256, file.publicPath);
    assert.ok(!/\/(?:conference-paper|journal-article|preprint|example|external-project|getting-started|jupyter|writing-technical-content)\//.test(file.path), file.path);
  }
});

test('old publication aliases consolidate into unique current records', () => {
  const records = json('src/data/publications.json');
  const ids = new Set(records.map(record => record.id));
  assert.equal(ids.size, 20);
  const map = json('docs/canonical-content-map.json');
  for (const id of [...Object.values(map.publicationAliases), ...Object.values(map.companionReports)]) assert.ok(ids.has(id), id);
  assert.equal(map.publicationAliases['ye-2023-probabilistic'], 'proburel');
  assert.equal(map.publicationAliases['ye-2023-formally'], map.publicationAliases['ye-2024100940']);
  assert.notEqual(map.publicationAliases['ye-2022'], map.publicationAliases['ye-2024100940']);
  for (const record of records) {
    for (const resource of record.resources || []) {
      assert.ok(!resource.url.includes('doi.org/https://'));
      if (resource.url.startsWith('/')) assert.ok(read(`public${resource.url}`).length);
    }
  }
});
