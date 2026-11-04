import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const resource = z.object({ label: z.string().min(1), url: z.url() });
const demos = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/demos' }),
  schema: z.object({
    slug: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/),
    title: z.string().min(1),
    subtitle: z.string(),
    summary: z.string(),
    researchArea: z.string(),
    status: z.enum(['recorded-demonstration', 'source-only', 'interactive']),
    problem: z.string(),
    method: z.string(),
    whatVisitorsSee: z.array(z.object({ title: z.string(), description: z.string() })),
    resultsOrLimitations: z.string(),
    thumbnail: z.string().optional(),
    thumbnailAlt: z.string(),
    mediaNote: z.string().optional(),
    videoUrl: z.url().optional(),
    videoPoster: z.string().optional(),
    interactiveUrl: z.url().optional(),
    paperLinks: z.array(resource),
    sourceLinks: z.array(resource),
    exampleLinks: z.array(resource),
    slidesLinks: z.array(resource),
    featured: z.boolean().default(false),
    order: z.number().default(0),
    updatedAt: z.coerce.date().optional(),
  }),
});

export const collections = { demos };
