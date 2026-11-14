// Compile hand-written news notes into the validated news collection data.
// Frontmatter is a small YAML subset: `key: value` lines, plus `key:` followed
// by indented `- field: value` items for resource and provenance lists.
// The body after the closing `---` becomes `detail`.
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';

const dir = new URL('../src/content/news/', import.meta.url);
const file = new URL('../src/data/news.json', import.meta.url);
const key = line => line.match(/^\s*([A-Za-z0-9_]+):\s*(.*)$/);

const scalar = raw => {
  const text = raw.trim();
  if (!text || text === 'null') return null;
  return text.replace(/^(['"])(.*)\1$/, '$2');
};

function frontmatter(name, lines) {
  const data = {};
  let list = null;
  let item = null;
  for (const line of lines) {
    if (!line.trim() || /^\s*#/.test(line)) continue;
    const entry = line.match(/^\s*-\s+([A-Za-z0-9_]+):\s*(.*)$/);
    if (entry) {
      if (!list) throw new Error(`${name}: list item outside a list "${line}"`);
      item = { [entry[1]]: scalar(entry[2]) };
      data[list].push(item);
      continue;
    }
    const field = key(line);
    if (!field) throw new Error(`${name}: bad frontmatter line "${line}"`);
    if (item && /^\s/.test(line)) {
      item[field[1]] = scalar(field[2]);
      continue;
    }
    item = null;
    if (field[2].trim()) {
      data[field[1]] = scalar(field[2]);
      list = null;
    } else {
      data[field[1]] = [];
      list = field[1];
    }
  }
  return data;
}

function parse(name, source) {
  const parts = source.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!parts) throw new Error(`${name}: missing frontmatter`);
  const data = frontmatter(name, parts[1].split(/\r?\n/));
  for (const required of ['title', 'date', 'summary']) {
    if (!data[required]) throw new Error(`${name}: missing ${required}`);
  }
  const detail = parts[2].trim();
  return {
    id: name.replace(/\.md$/, ''),
    date: data.date,
    title: data.title,
    summary: data.summary,
    ...(detail && { detail }),
    resources: data.resources ?? [],
    provenance: data.provenance ?? [],
    eventDate: data.eventDate ?? null,
    eventEndDate: data.eventEndDate ?? null,
  };
}

export const buildNews = () => readdirSync(dir)
  .filter(name => name.endsWith('.md'))
  .sort()
  .map(name => parse(name, readFileSync(new URL(name, dir), 'utf8')));

if (import.meta.url === `file://${process.argv[1]}`) {
  const news = buildNews();
  writeFileSync(file, `${JSON.stringify(news, null, 2)}\n`);
  console.log(`Compiled ${news.length} news notes into src/data/news.json.`);
}
