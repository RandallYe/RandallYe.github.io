import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

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
