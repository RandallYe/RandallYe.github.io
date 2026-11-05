// Validate both hosting paths and restore a root build, including after preview failures.
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const cwd = fileURLToPath(new URL('../', import.meta.url));
const outputChecks = ['check:links', 'check:routes', 'check:history', 'check:demo', 'check:posts', 'check:talks', 'check:publications'];
const run = (script, base = '/') => {
  const result = spawnSync('npm', ['run', script], {
    cwd,
    stdio: 'inherit',
    env: { ...process.env, ASTRO_BASE: base },
  });
  if (result.error) throw result.error;
  if (result.status !== 0) throw new Error(`${script} failed at ${base} (exit ${result.status ?? result.signal})`);
};

let failure;
let previewAttempted = false;
try {
  run('check');
  run('test');
  run('build');
  outputChecks.forEach(script => run(script));
  previewAttempted = true;
  run('build', '/research-preview/');
  outputChecks.forEach(script => run(script, '/research-preview/'));
} catch (error) {
  failure = error;
} finally {
  if (previewAttempted) {
    try {
      run('build');
      run('check:links');
    } catch (error) {
      failure ??= error;
    }
  }
}
if (failure) {
  console.error(failure.message);
  process.exitCode = 1;
} else {
  console.log('Root and preview checks passed; root build restored. Browser, playback and external-resource review are separate.');
}
