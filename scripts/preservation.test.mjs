import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
const root = new URL('../', import.meta.url);
const read = path => readFileSync(new URL(path, root));
const hash = value => createHash('sha256').update(value).digest('hex');

test('all inventoried legacy assets retain exact source bytes and original URLs', () => {
  const manifest = JSON.parse(read('docs/legacy-assets.json'));
  assert.equal(manifest.length, 17);
  for (const asset of manifest) {
    assert.equal(hash(read(asset.path)), asset.sha256, asset.path);
    assert.equal(hash(read(`public/${asset.path}`)), asset.sha256, `public/${asset.path}`);
  }
  assert.deepEqual(read('index.md'), read('public/legacy/index.md'));
});

test('bibliography preserves all source categories and co-authorship', () => {
  const publications = JSON.parse(read('src/data/publications.json'));
  const counts = Object.groupBy(publications, paper => paper.group);
  assert.deepEqual(Object.values(counts).map(group => group.length), [5, 8, 1, 3, 1, 2]);
  assert.equal(new Set(publications.map(paper => paper.url)).size, 20);
  assert.equal(publications.find(paper => paper.url.endsWith('77382-2_3')).authors, 'K. Ye, R. Metere, and P. Yadav');
  for (const paper of publications) {
    assert.ok(paper.title && paper.authors && paper.venue);
    assert.equal(new URL(paper.url).protocol, 'https:');
  }
});
