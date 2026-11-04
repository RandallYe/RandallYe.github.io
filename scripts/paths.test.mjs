import test from 'node:test';
import assert from 'node:assert/strict';
import { withBase } from '../src/lib/paths.mjs';

test('internal routes, files and fragments work at root and under a preview prefix', () => {
  for (const base of ['/', '/research-preview/', '/research-preview']) {
    const prefix = base === '/' ? '' : '/research-preview';
    assert.equal(withBase('', base), `${prefix}/`);
    assert.equal(withBase('/tools/security-protocol-animation/', base), `${prefix}/tools/security-protocol-animation/`);
    assert.equal(withBase('pics/me.jpg', base), `${prefix}/pics/me.jpg`);
    assert.equal(withBase('legacy/#publications', base), `${prefix}/legacy/#publications`);
  }
});

test('external resources and local fragment links are never prefixed', () => {
  for (const url of ['https://doi.org/10.1007/example', 'mailto:ye.randall@gmail.com', '#recording', '//example.org/video']) {
    assert.equal(withBase(url, '/preview/'), url);
  }
});
