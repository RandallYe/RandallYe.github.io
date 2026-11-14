import { defineCollection, reference } from 'astro:content';
import { file, glob } from 'astro/loaders';
import { z } from 'astro/zod';

const slug = z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/);
const resourceUrl = z.url().or(z.string().regex(/^\/(?!\/)/));
const resource = z.object({
  label: z.string().min(1),
  url: resourceUrl,
  description: z.string().optional(),
});
const publications = defineCollection({
  loader: file('./src/data/publications.json'),
  schema: z.object({
    id: slug,
    title: z.string().min(1),
    authors: z.string().min(1),
    venue: z.string().min(1),
    year: z.number().int().min(1900),
    url: z.url(),
    group: z.string(),
    abstract: z.string().optional(),
    abstractSource: z.string().optional(),
    abstractSourceSha256: z.string().regex(/^[a-f0-9]{64}$/).optional(),
    resources: z.array(resource).default([]),
    relatedDemos: z.array(reference('demos')).default([]),
  }),
});
const demos = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/demos' }),
  schema: z.object({
    slug,
    title: z.string().min(1),
    subtitle: z.string(),
    summary: z.string(),
    researchArea: z.string(),
    category: z.enum(['research-demo', 'engineering-case-study']).default('research-demo'),
    status: z.enum(['recorded-demonstration', 'source-only', 'interactive']),
    problem: z.string(),
    method: z.string(),
    whatVisitorsSee: z.array(z.object({ title: z.string(), description: z.string() })),
    resultsOrLimitations: z.string(),
    thumbnail: resourceUrl.optional(),
    thumbnailAlt: z.string(),
    mediaNote: z.string().optional(),
    videoUrl: z.url().optional(),
    videoPoster: resourceUrl.optional(),
    media: z.array(z.object({
      kind: z.enum(['video', 'image', 'poster', 'download']),
      src: resourceUrl,
      title: z.string(),
      caption: z.string(),
      alt: z.string().optional(),
      poster: resourceUrl.optional(),
      mimeType: z.string().optional(),
      sourcePath: z.string(),
      sha256: z.string().regex(/^[a-f0-9]{64}$/),
      verificationStatus: z.enum(['preserved', 'headers-checked', 'playback-checked']).default('preserved'),
    })).default([]),
    provenance: z.object({
      sourcePage: z.string(),
      originalDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    }).optional(),
    relatedPublications: z.array(reference('publications')).default([]),
    interactiveUrl: z.url().optional(),
    paperLinks: z.array(resource),
    sourceLinks: z.array(resource),
    exampleLinks: z.array(resource),
    examplesHeading: z.string().default('Examples'),
    slidesLinks: z.array(resource),
    featured: z.boolean().default(false),
    order: z.number().default(0),
    updatedAt: z.coerce.date().optional(),
  }),
});

const posts = defineCollection({
  loader: file('./src/data/posts.json'),
  schema: z.object({ id: slug, title: z.string(), date: z.string(), dateLabel: z.string().optional(), summary: z.string(), math: z.boolean(), sourcePath: z.string(), sourceSha256: z.string(), thumbnail: resourceUrl, thumbnailAlt: z.string().min(1), thumbnailSource: z.string().min(1), body: z.string() }),
});
const talks = defineCollection({
  loader: file('./src/data/talks.json'),
  schema: z.object({
    id: slug,
    title: z.string().min(1),
    date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    event: z.string().min(1),
    description: z.string().min(1),
    resources: z.array(resource).default([]),
    rehearsals: z.array(z.object({ date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/), title: z.string(), label: z.string() })).default([]),
    sourcePath: z.string().optional(),
    recording: z.string().optional(),
    recordingTitle: z.string().optional(),
    thumbnail: resourceUrl,
    thumbnailAlt: z.string().min(1),
    thumbnailSource: z.string().min(1),
  }),
});
const source = z.object({
  source: z.enum(['GitHub', 'old_entry']),
  path: z.string(),
  sha256: z.string().regex(/^[a-f0-9]{64}$/),
});
const provenance = z.array(source).min(1);
const projects = defineCollection({
  loader: file('./src/data/projects.json'),
  schema: z.object({ id: slug, title: z.string(), period: z.string(), summary: z.string(), detail: z.string(), resources: z.array(resource), relatedDemos: z.array(reference('demos')), provenance }),
});
const news = defineCollection({
  // Compiled from the notes in src/content/news/ by scripts/build-news.mjs.
  loader: file('./src/data/news.json'),
  schema: z.object({ id: slug, title: z.string(), date: z.iso.date(), summary: z.string(), detail: z.string().optional(), eventDate: z.iso.date().nullish(), eventEndDate: z.iso.date().nullish(), resources: z.array(resource), provenance: z.array(source).default([]) }),
});
const teaching = defineCollection({
  loader: file('./src/data/teaching.json'),
  schema: z.object({ id: slug, title: z.string(), period: z.string(), summary: z.string(), resources: z.array(resource), provenance }),
});
const researchAreas = defineCollection({
  loader: file('./src/data/research-areas.json'),
  schema: z.object({
    id: slug,
    title: z.string().min(1),
    shortTitle: z.string().min(1),
    notation: z.string(),
    question: z.string().min(1),
    summary: z.string().min(1),
    approach: z.string().min(1),
    order: z.number().int(),
    relatedProjects: z.array(reference('projects')),
    contributions: z.array(z.object({
      id: slug,
      title: z.string().min(1),
      summary: z.string().min(1),
      method: z.string().min(1),
      relatedPublications: z.array(reference('publications')),
      relatedDemos: z.array(reference('demos')),
      resources: z.array(resource),
      examples: z.array(z.string()),
      role: z.string().optional(),
    })).min(1),
  }),
});
export const collections = { demos, publications, posts, talks, projects, news, teaching, researchAreas };
