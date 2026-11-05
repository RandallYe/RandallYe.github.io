import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { routeGuardMiddleware } from '../node_modules/astro/dist/vite-plugin-astro-server/route-guard.js';
const root = new URL('../', import.meta.url);

test('CV download retains original bytes and passes the installed Astro browser-navigation guard', () => {
  assert.deepEqual(readFileSync(new URL('public/downloads/academic-cv.pdf', root)), readFileSync(new URL('CV/Academic_CV-Kangfeng_Ye.pdf', root)));
  assert.ok(!existsSync(new URL('downloads/academic-cv.pdf', root)), 'Avoid a project-root file collision');
  const guard = routeGuardMiddleware({ config: { root, publicDir: new URL('public/', root), srcDir: new URL('src/', root) } });
  let next = false;
  guard({ url: '/downloads/academic-cv.pdf', headers: { accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' } }, {
    writeHead(status) { assert.fail(`CV navigation blocked with ${status}`); },
  }, () => { next = true; });
  assert.ok(next);
});
