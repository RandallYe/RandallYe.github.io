import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
const root = new URL('../', import.meta.url);
const read = path => readFileSync(new URL(path, root), 'utf8');

test('posts contain the two selected archive articles and latest-site SEFM/DataMod report', () => {
  const posts = JSON.parse(read('src/data/posts.json'));
  assert.deepEqual(posts.map(post => post.id).sort(), ['sefm-datamod-report', 'steady-state-probabilities', 'temporal-logic']);
  const audit = JSON.parse(read('docs/old-entry-inventory.json'));
  for (const post of posts) {
    if (post.sourcePath.startsWith('post/')) {
      const source = audit.files.find(file => file.path === post.sourcePath);
      assert.equal(post.sourceSha256, source.sha256);
    } else {
      const source = readFileSync(new URL(`public/${post.sourcePath}`, root));
      assert.equal(post.sourceSha256, createHash('sha256').update(source).digest('hex'));
    }
    assert.ok(!post.body.includes('<script'));
    assert.ok(!post.body.includes('twitter.com/intent'));
    for (const match of post.body.matchAll(/src="(\/old_entry\/[^"#]+)"/g)) assert.ok(existsSync(new URL(`public${match[1]}`, root)), match[1]);
    for (const match of post.body.matchAll(/src="(\/posts\/SEFM_DataMod\/[^"#]+)"/g)) assert.ok(existsSync(new URL(`public${match[1]}`, root)), match[1]);
  }
  assert.ok(posts.find(post => post.id === 'temporal-logic').body.includes('plato.stanford.edu/entries/logic-temporal/'));
  assert.ok(posts.find(post => post.id === 'steady-state-probabilities').body.includes('expected-value-of-the-number-of-visits'));
  const report = posts.find(post => post.id === 'sefm-datamod-report');
  assert.equal((report.body.match(/<img\b/g) || []).length, 6);
  assert.ok(report.body.includes('/posts/SEFM_DataMod/workflow.png'));
  assert.ok(report.body.includes('https://arxiv.org/abs/2410.00676'));
  assert.ok(report.body.includes('https://arxiv.org/abs/2411.03943'));
});

test('all archived equations render to native MathML without changing HTML anchors', async () => {
  const { typesetArticle } = await import('../src/lib/article-math.ts');
  const post = JSON.parse(read('src/data/posts.json')).find(post => post.math);
  const result = typesetArticle(post.body);
  assert.ok((result.match(/<math /g) || []).length > 50);
  assert.ok(result.includes('<mtable'));
  assert.ok(result.includes('id="expected-value-of-the-number-of-visits"'));
  assert.ok(!result.includes('katex-error'));
});
