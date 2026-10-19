const http = require('node:http');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE);
const { getCollections, getBookmarks, openOriginal, installXssObserver, classifyDuplicateOutcome, sameRecordSnapshots } = require('./bookmark_ui_acceptance.cjs');

function serve(handler) {
  const server = http.createServer(handler);
  return new Promise(resolve => server.listen(0, '127.0.0.1', () => resolve(server)));
}
(async () => {
  const fixture = await serve((req, res) => {
    const pathname = new URL(req.url, 'http://127.0.0.1').pathname;
    const label = pathname === '/original' ? 'Local original fixture page' : 'Local secondary fixture page';
    res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
    res.end(`<!doctype html><title>fixture</title><h1>${label}</h1>`);
  });
  const originalUrl = `http://127.0.0.1:${fixture.address().port}/original?token=synthetic-original`;
  const secondUrl = `http://127.0.0.1:${fixture.address().port}/second?token=synthetic-second`;
  const app = await serve((req, res) => {
    if (req.method === 'POST' && req.url === '/bookmarks') {
      req.resume();
      req.on('end', () => {
        res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
        res.end('<!doctype html><form method="get"><input name="q"></form><img src="/missing" onerror="window.__atlasXss=1"> Synthetic XSS fixture');
      });
      return;
    }
    if (req.url === '/missing') { res.writeHead(404); return res.end(); }
    if (req.url === '/go/42' || req.url === '/go/44') {
      res.writeHead(302, { location: req.url === '/go/42' ? originalUrl : secondUrl });
      return res.end();
    }
    res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
    res.end(`<form method="post" action="/bookmarks"><button type="submit">Save</button></form><ul><li class="collection" data-collection-id="7" data-default="1"><a href="/?collection=7">阅读收藏</a></li></ul><ul><li class="bookmark" data-bookmark-id="42"><a class="bookmark-title" href="/go/42">Go original</a></li><li class="bookmark" data-bookmark-id="43"><a class="bookmark-title" href="${originalUrl}">Direct original</a></li><li class="bookmark" data-bookmark-id="44"><a class="bookmark-title" href="/go/44">Go second</a></li><li class="bookmark" data-bookmark-id="45"><a class="bookmark-title" target="_blank" href="${secondUrl}">Direct second popup</a></li></ul>`);
  });
  const appUrl = `http://127.0.0.1:${app.address().port}/`;
  const evidenceDir = process.env.SYNTHETIC_EVIDENCE_DIR || fs.mkdtempSync(path.join(os.tmpdir(), 'bookmark-harness-dom-'));
  if (fs.existsSync(evidenceDir)) throw new Error(`refusing to overwrite synthetic evidence: ${evidenceDir}`);
  fs.mkdirSync(evidenceDir, { recursive: true });
  fs.mkdirSync(path.join(evidenceDir, 'screenshots'));
  process.env.APP_URL = appUrl;
  process.env.EVIDENCE_DIR = evidenceDir;
  const browser = await chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_EXECUTABLE });
  try {
    const context = await browser.newContext({ serviceWorkers: 'block' });
    await installXssObserver(context);
    const allowed = new Set([new URL(appUrl).origin, new URL(originalUrl).origin]);
    await context.route('**/*', route => allowed.has(new URL(route.request().url()).origin) ? route.continue() : route.abort('blockedbyclient'));
    const page = await context.newPage();
    await page.goto(appUrl);
    const postResponse = page.waitForResponse(response => response.request().method() === 'POST' && new URL(response.url()).pathname === '/bookmarks');
    await page.locator('form[action="/bookmarks"] button').click();
    await postResponse;
    await page.locator('img[src="/missing"]').waitFor();
    await page.waitForFunction(() => sessionStorage.getItem('__atlas_xss_observed') === '1', null, { timeout: 5000 });
    const firstResponseValue = await page.evaluate(() => sessionStorage.getItem('__atlas_xss_observed'));
    if (firstResponseValue !== '1') throw new Error(`first-response XSS execution not captured: ${firstResponseValue}`);
    await page.goto(appUrl);
    if (await page.evaluate(() => sessionStorage.getItem('__atlas_xss_observed')) !== '1') throw new Error('first-response XSS observation did not survive safe navigation');
    await page.evaluate(() => sessionStorage.removeItem('__atlas_xss_observed'));
    const collections = await getCollections(page);
    if (collections.length !== 1 || collections[0].text !== '阅读收藏') throw new Error(`collection DOM parse failed: ${JSON.stringify(collections)}`);
    const bookmarks = await getBookmarks(page);
    if (bookmarks.length !== 4 || bookmarks[0].id !== '42' || bookmarks[0].href !== '/go/42') throw new Error(`bookmark DOM parse failed: ${JSON.stringify(bookmarks)}`);
    const originalGo = await openOriginal(page, context, bookmarks[0], originalUrl, 'synthetic-original-go.png', '7');
    const originalDirect = await openOriginal(page, context, bookmarks[1], originalUrl, 'synthetic-original-direct.png', '7');
    const secondGo = await openOriginal(page, context, bookmarks[2], secondUrl, 'synthetic-second-go.png', '7');
    const secondDirect = await openOriginal(page, context, bookmarks[3], secondUrl, 'synthetic-second-direct.png', '7');
    const browseAfterClicks = await getCollections(page);
    if (!browseAfterClicks.some(collection => collection.id === '7')) throw new Error('could not browse collection after original-page clicks');
    const before = [{ id: '42', title: 'Original', href: '/go/42', expectedUrl: originalUrl }];
    const updated = [{ id: '42', title: 'Repeated', href: '/go/42', expectedUrl: originalUrl }];
    const created = [...before, { id: '43', title: 'Repeated', href: '/go/43', expectedUrl: originalUrl }];
    const duplicateOutcomes = {
      upsert: classifyDuplicateOutcome(before, updated, 303),
      create: classifyDuplicateOutcome(before, created, 303),
      reject: classifyDuplicateOutcome(before, before, 400),
      noChange: classifyDuplicateOutcome(before, before, 303),
      idempotencyReplay: { unchanged: sameRecordSnapshots(updated, updated), updated: sameRecordSnapshots(before, updated) },
    };
    if (duplicateOutcomes.upsert !== 'updated_existing_record' || duplicateOutcomes.create !== 'created_new_record'
      || duplicateOutcomes.reject !== 'rejected' || duplicateOutcomes.noChange !== 'accepted_without_observable_change'
      || duplicateOutcomes.idempotencyReplay.unchanged !== true || duplicateOutcomes.idempotencyReplay.updated !== false) {
      throw new Error(`duplicate outcome classification failed: ${JSON.stringify(duplicateOutcomes)}`);
    }
    const evidence = { status: 'passed', kind: 'synthetic harness-only test', firstResponseXssValue: firstResponseValue,
      firstResponseXssPersistedAcrossNavigation: true, collectionText: collections[0].text,
      navigation: { originalGo, originalDirect, secondGo, secondDirect, browseAfterClicks: true }, duplicateOutcomes, evidenceDir };
    fs.writeFileSync(path.join(evidenceDir, 'result.json'), JSON.stringify(evidence, null, 2) + '\n');
    process.stdout.write(JSON.stringify(evidence) + '\n');
    await context.close();
  } finally {
    await browser.close();
    await new Promise(resolve => app.close(resolve));
    await new Promise(resolve => fixture.close(resolve));
  }
})().catch(error => { console.error(error.stack || String(error)); process.exit(1); });
