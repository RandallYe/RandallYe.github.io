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

test('available abstracts, BibTeX files and preprints are attached to their canonical works', () => {
  const records = json('src/data/publications.json');
  const manifest = json('docs/old-entry-assets.json').files.filter(file => file.path.endsWith('.bib'));
  const linkedBib = new Set();
  for (const record of records) {
    if (record.abstract) {
      assert.ok(record.abstractSource, record.id);
      assert.match(record.abstractSourceSha256, /^[a-f0-9]{64}$/, record.id);
      assert.ok(record.abstract.length > 100, record.id);
    }
    for (const resource of record.resources || []) {
      if (resource.url.endsWith('.bib')) linkedBib.add(resource.url.replace(/^\/old_entry\//, ''));
    }
  }
  assert.equal(records.filter(record => record.abstract).length, 9);
  for (const file of manifest) assert.ok(linkedBib.has(file.path), `unlinked BibTeX source: ${file.path}`);
  assert.ok(records.find(record => record.id === 'security-protocol-animation').resources.some(resource => resource.url === 'https://arxiv.org/abs/2410.00676'));
  assert.ok(records.find(record => record.id === 'oran-energy-availability').resources.some(resource => resource.url === 'https://arxiv.org/abs/2411.03943'));
});
