/** @param {string} path @param {string} base @returns {string} */
export function withBase(path = '', base = '/') {
  if (/^(?:[a-z][a-z\d+.-]*:|\/\/|#)/i.test(path)) return path;
  return `${base.replace(/\/+$/, '')}/${path.replace(/^\/+/, '')}`;
}
