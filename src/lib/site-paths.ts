import { withBase } from './paths.mjs';
export const local = (path = ''): string => withBase(path, import.meta.env.BASE_URL);
