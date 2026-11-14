import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { buildNews } from './build-news.mjs';

test('compiled news data matches the markdown notes', () => {
  const compiled = JSON.parse(readFileSync(new URL('../src/data/news.json', import.meta.url), 'utf8'));
  assert.deepEqual(compiled, buildNews(), 'Run npm run build:news after editing src/content/news/');
  assert.equal(new Set(compiled.map(item => item.id)).size, compiled.length);
  assert.ok(compiled.every(item => /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(item.id)), 'Note filenames must be slugs');
});
