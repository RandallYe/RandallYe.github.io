import { defineConfig } from 'astro/config';
import { writeFileSync } from 'node:fs';
import { buildNews } from './scripts/build-news.mjs';

// Keep the compiled news data in step with the notes while `astro dev` runs.
const newsNotes = {
  name: 'news-notes',
  configureServer(server) {
    server.watcher.add('src/content/news');
    server.watcher.on('all', (_event, file) => {
      if (!file.replaceAll('\\', '/').includes('src/content/news/') || !file.endsWith('.md')) return;
      try {
        writeFileSync(new URL('./src/data/news.json', import.meta.url), `${JSON.stringify(buildNews(), null, 2)}\n`);
      } catch (error) {
        console.error('[news-notes]', error.message);
      }
    });
  },
};

export default defineConfig({
  site: 'https://randallye.github.io',
  base: process.env.ASTRO_BASE || '/',
  output: 'static',
  trailingSlash: 'always',
  vite: { plugins: [newsNotes] },
});
