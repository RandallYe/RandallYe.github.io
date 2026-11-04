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
  schema: z.object({ id: slug, title: z.string(), date: z.string(), summary: z.string(), math: z.boolean(), sourcePath: z.string(), sourceSha256: z.string(), body: z.string() }),
});
export const collections = { demos, publications, posts };
