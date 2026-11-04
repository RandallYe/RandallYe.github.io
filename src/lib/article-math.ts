import katex from 'katex';

// Native MathML avoids client JavaScript, remote fonts and stylesheets.
export function typesetArticle(html: string): string {
  const decode = (value: string) => value.replaceAll('&hellip;', '\\ldots ').replace(/&(?:amp|lt|gt|quot|#39|nbsp);/g, entity => ({ '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'", '&nbsp;': ' ' })[entity] || entity);
  return html.split(/(<[^>]*>)/g).map(part => part.startsWith('<') ? part : part.replace(/\$\$([\s\S]*?)\$\$|(\\begin\{align\*\}[\s\S]*?\\end\{align\*\})|(?<!\$)\$(?!\$)([\s\S]*?)\$(?!\$)/g,
    (_match, block: string | undefined, align: string | undefined, inline: string | undefined) => katex.renderToString(decode(block ?? align ?? inline ?? ''), { output: 'mathml', displayMode: block !== undefined || align !== undefined, throwOnError: true, trust: false, strict: 'error', macros: { '\\mbox': '\\text' } })) ).join('');
}
