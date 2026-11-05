import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
const read = path => JSON.parse(readFileSync(new URL(`../${path}`, import.meta.url)));
const projects = read('src/data/projects.json');
const news = read('src/data/news.json');
const teaching = read('src/data/teaching.json');
const inventory = read('docs/old-entry-inventory.json');
const hashes = new Map(inventory.files.map(file => [file.path, file.sha256]));
const aliases = read('src/data/route-aliases.json');

test('every substantive archived project, news and teaching page has a hashed canonical record and alias', () => {
  const records = [...projects, ...news, ...teaching];
  const pages = inventory.contentPages.filter(page => page.indexed && ['project', 'news', 'teaching'].includes(page.section));
  assert.equal(pages.length, 29);
  for (const page of pages) {
    const matching = records.filter(record => record.provenance.some(source => source.source === 'old_entry' && source.path === page.path));
    assert.equal(matching.length, 1, page.path);
    assert.ok(aliases.some(alias => alias.path === page.path.replace('/index.html', '')), page.path);
  }
  const latestHash = createHash('sha256').update(readFileSync(new URL('../index.md', import.meta.url))).digest('hex');
  for (const record of records) {
    for (const source of record.provenance) {
      assert.equal(source.sha256, source.source === 'old_entry' ? hashes.get(source.path) : latestHash, source.path);
    }
  }
});

test('current project dates govern six canonical histories without obsolete Present claims', () => {
  assert.equal(projects.length, 6);
  const project = id => projects.find(project => project.id === id);
  assert.equal(project('cyphyassure').period, 'June 2021 – September 2021');
  assert.equal(project('into-cps').period, 'November 2016 – December 2017');
  assert.equal(project('cheddar').period, 'February 2024 – November 2025');
  const combined = project('robocalc-robotest');
  assert.equal(combined.period, 'April 2018 – June 2023');
  assert.equal(combined.provenance.filter(source => source.source === 'old_entry').length, 2);
  assert.ok(project('vetss').detail.includes('aircraft cabin pressure'));
  assert.ok(projects.every(project => !/Present|example/i.test(project.period + project.id)));
});

test('news preserves announcement dates, separates event dates and merges the JLAMP report', () => {
  assert.equal(new Set(news.map(item => item.id)).size, news.length);
  const exhibition = news.find(item => item.id === '20221011-robostar-industry-exhibition');
  assert.equal(exhibition.date, '2022-09-14');
  assert.equal(exhibition.eventDate, '2022-10-11');
  assert.equal(exhibition.eventEndDate, '2022-10-12');
  const jlamp = news.filter(item => item.provenance.some(source => source.path.includes('20231229_jlamp')));
  assert.equal(jlamp.length, 1);
  assert.equal(jlamp[0].date, '2023-12-19');
  assert.match(jlamp[0].detail, /29 December 2023/);
  assert.equal(jlamp[0].provenance.length, 2);
  assert.ok(news.every(item => !item.summary.includes('## ')));
});
