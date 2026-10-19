// Real Chromium negative fixtures for the independent user-action adapter.
// The fixture server exposes working JSON/API query paths; only the UI is defective.
const assert = require('node:assert/strict');
const http = require('node:http');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || path.resolve(__dirname, '../../../../atlas-web/node_modules/playwright'));
const adapter = require('./bookmark_acceptance_adapter.cjs');

function fixtureHtml({ missingMove = false, dropsCategory = false } = {}) {
  return `<!doctype html><html><body>
    <a data-testid="category-manager" href="/categories">Categories</a>
    ${missingMove ? '' : '<form data-testid="record-move-form" method="post" action="/bookmarks/demo/move"><input name="record_id" value="demo"><select name="category_id"><option value="1">Fixture Category</option></select><button>Move</button></form>'}
    <form data-testid="category-search-form" method="get" action="/">
      <select name="category"${dropsCategory ? ' disabled' : ''}><option selected>Fixture Category</option></select>
      <input name="q" value=""><button type="submit">Search</button>
    </form>
    </body></html>`;
}

async function withFixture(options, run) {
  const server = http.createServer((request, response) => {
    const url = new URL(request.url, 'http://127.0.0.1');
    if (url.pathname === '/api/bookmarks' && request.method === 'GET') {
      const good = url.searchParams.get('category') === 'Fixture Category' && url.searchParams.get('q') === 'fixture-term';
      response.writeHead(200, { 'content-type': 'application/json' });
      response.end(JSON.stringify(good ? [{ id: 'demo', title: 'fixture-term', category: 'Fixture Category' }] : []));
      return;
    }
    if (url.pathname === '/api/bookmarks/demo/move' && request.method === 'POST') {
      response.writeHead(200, { 'content-type': 'application/json' });
      response.end(JSON.stringify({ id: 'demo', category: 'Fixture Category' }));
      return;
    }
    response.writeHead(200, { 'content-type': 'text/html' });
    response.end(fixtureHtml(options));
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  try { await run(base); } finally {
    server.closeAllConnections();
    await new Promise(resolve => server.close(resolve));
  }
}

async function apiStillWorks(page, base) {
  const result = await page.evaluate(async () => {
    const response = await fetch('/api/bookmarks?category=Fixture%20Category&q=fixture-term');
    return { status: response.status, rows: await response.json() };
  });
  assert.equal(result.status, 200);
  assert.equal(result.rows.length, 1);
}

(async () => {
  const browser = await chromium.launch({ headless: true, ...(process.env.PLAYWRIGHT_EXECUTABLE ? { executablePath: process.env.PLAYWRIGHT_EXECUTABLE } : {}) });
  try {
    await withFixture({ missingMove: true }, async base => {
      const page = await browser.newPage();
      await page.goto(base);
      await apiStillWorks(page, base);
      await assert.rejects(adapter.validateUiContract(page, base), /move control is missing/);
      await page.close();
    });
    await withFixture({ dropsCategory: true }, async base => {
      const page = await browser.newPage();
      await page.goto(base);
      await apiStillWorks(page, base);
      await assert.rejects(adapter.validateUiContract(page, base), /did not preserve category and q/);
      await page.close();
    });
  } finally {
    await browser.close();
  }
  process.stdout.write('real Chromium detected missing move control and category-dropping search form while fixture APIs remained functional\n');
})().catch(error => { process.stderr.write(String(error.stack || error)); process.exitCode = 1; });
