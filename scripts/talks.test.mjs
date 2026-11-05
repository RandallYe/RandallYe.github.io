import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const talks = JSON.parse(readFileSync(new URL('../src/data/talks.json', import.meta.url)));
const aliases = JSON.parse(readFileSync(new URL('../src/data/route-aliases.json', import.meta.url)));

test('talk records preserve all substantive archived talks and group rehearsals', () => {
  assert.equal(talks.length, 14);
  assert.equal(talks.filter(talk => talk.sourcePath).length, 11);
  assert.equal(talks.reduce((sum, talk) => sum + (talk.rehearsals ?? []).length, 0), 3);
  assert.equal(new Set(talks.map(talk => talk.id)).size, talks.length);
  const archiveTalks = talks.filter(talk => talk.sourcePath);
  assert.equal(archiveTalks.length, 11);
  for (const talk of archiveTalks) {
    assert.match(talk.date, /^\d{4}-\d{2}-\d{2}$/);
    assert.ok(aliases.some(alias => alias.path === talk.sourcePath.replace(/\/index\.html$/, '') && alias.destination === `talks/#${talk.id}`));
  }
  for (const talk of talks) {
    assert.ok(talk.thumbnailAlt && talk.thumbnailSource, talk.id);
    assert.ok(readFileSync(new URL(`../public${talk.thumbnail}`, import.meta.url)).length, talk.thumbnail);
    const sourcePath = talk.thumbnailSource.startsWith('talk/') ? `public/old_entry/${talk.thumbnailSource}` : `public/${talk.thumbnailSource}`;
    assert.ok(readFileSync(new URL(`../${sourcePath}`, import.meta.url)).length, talk.thumbnailSource);
  }
  for (const path of ['talk/ramics2021_rehearsal', 'talk/robostar_seminar_20221005', 'talk/robostar_seminar_20221119']) {
    assert.ok(aliases.some(alias => alias.path === path), `missing historical alias ${path}`);
  }
});

test('preserved recordings, slide files and frog-jumper models exist', () => {
  for (const path of [
    'public/old_entry/talk/20221026_icfem_2022/Animation_Movement.mp4',
    'public/old_entry/talk/20221027_models_2022/MODELS-2022_JF1_recording_Probabilistic-modelling-and-verification-using-RoboChart-and-PRISM_KangfengYe.mp4',
    'public/old_entry/talk/ramics2021/ramics2021.pdf',
    ...Array.from({ length: 5 }, (_, i) => `public/old_entry/files/PoS2019/frog-${i}.csp`),
  ]) assert.doesNotThrow(() => readFileSync(new URL(`../${path}`, import.meta.url)));
  assert.equal(talks.filter(talk => talk.recording).length, 2);
});

test('slide-cover thumbnail derivatives match their source PDFs and recorded hashes', () => {
  const manifest = JSON.parse(readFileSync(new URL('../docs/list-thumbnail-derivatives.json', import.meta.url))).derivatives;
  const sources = new Map(JSON.parse(readFileSync(new URL('../docs/legacy-assets.json', import.meta.url))).map(file => [file.path, file.sha256]));
  for (const item of manifest) {
    const thumbnail = readFileSync(new URL(`../public${item.thumbnail}`, import.meta.url));
    assert.equal(createHash('sha256').update(thumbnail).digest('hex'), item.thumbnailSha256);
    assert.equal(sources.get(item.sourcePath), item.sourceSha256);
  }
  assert.equal(manifest.length, 2);
});
