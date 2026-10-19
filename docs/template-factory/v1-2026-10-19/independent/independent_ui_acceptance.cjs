// Host-side harness for an independent scenario adapter. It grants the browser
// access only to the app and owned loopback fixture, then requires explicit
// machine-readable assertion results from the adapter.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE);
const fs = require('node:fs');
const path = require('node:path');

async function main() {
  const appOrigin = new URL(process.env.APP_URL).origin;
  const fixtureOrigin = new URL(process.env.FIXTURE_BASE).origin;
  const required = JSON.parse(process.env.REQUIRED_ASSERTIONS_JSON);
  const browser = await chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_EXECUTABLE });
  const context = await browser.newContext({ acceptDownloads: false });
  const denied = [];
  await context.route('**/*', async route => {
    const url = route.request().url();
    let origin;
    try { origin = new URL(url).origin; } catch { origin = ''; }
    if (origin === appOrigin || origin === fixtureOrigin || url.startsWith('data:') || url.startsWith('blob:')) {
      await route.continue();
    } else {
      denied.push(url);
      await route.abort('blockedbyclient');
    }
  });
  const page = await context.newPage();
  const pageErrors = [];
  page.on('pageerror', error => pageErrors.push(String(error)));
  try {
    await page.goto(process.env.APP_URL, { waitUntil: 'domcontentloaded', timeout: 30000 });
    const adapterPath = path.resolve(process.env.ACCEPTANCE_ADAPTER);
    const stat = fs.lstatSync(adapterPath);
    if (!stat.isFile() || stat.isSymbolicLink()) throw new Error('adapter must be a regular file');
    const adapter = require(adapterPath);
    if (typeof adapter.run !== 'function') throw new Error('acceptance adapter must export async run({page, appUrl, fixtureBase, phase, scenarioId})');
    const result = await adapter.run({
      page,
      appUrl: process.env.APP_URL,
      fixtureBase: process.env.FIXTURE_BASE,
      phase: process.env.PHASE,
      scenarioId: process.env.SCENARIO_ID,
      runId: process.env.RUN_ID || null,
      initialMetadata: process.env.INITIAL_METADATA_JSON ? JSON.parse(process.env.INITIAL_METADATA_JSON) : null,
    });
    if (!result || !Array.isArray(result.assertions)) throw new Error('adapter result must contain assertions[]');
    const observed = new Set(result.assertions.map(item => item && item.id));
    if (process.env.PHASE === 'initial') {
      const prematureRestart = result.assertions
        .map(item => item && item.id)
        .filter(id => typeof id === 'string' && id.toLowerCase().includes('restart'));
      if (prematureRestart.length) throw new Error(`restart assertion cannot pass before container restart: ${prematureRestart.join(', ')}`);
    }
    const missing = required.filter(id => !observed.has(id));
    if (missing.length) throw new Error(`adapter omitted required assertions: ${missing.join(', ')}`);
    if (denied.length) throw new Error(`browser attempted off-origin requests: ${denied.join(', ')}`);
    if (pageErrors.length) throw new Error(`browser page errors: ${pageErrors.join(' | ')}`);
    process.stdout.write(JSON.stringify({
      phase: process.env.PHASE,
      assertions: result.assertions,
      denied_requests: denied,
      page_errors: pageErrors,
      adapter_metadata: result.metadata || {},
    }));
  } finally {
    await context.close();
    await browser.close();
  }
}

main().catch(error => {
  process.stderr.write(String(error && error.stack || error));
  process.exitCode = 1;
});
