// Real Chromium negative fixtures for the independent user-action adapter.
// The fixture server exposes working JSON/API query paths; only the UI is defective.
const assert = require('node:assert/strict');
const http = require('node:http');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || path.resolve(__dirname, '../../../../atlas-web/node_modules/playwright'));
const adapter = require('./bookmark_acceptance_adapter.cjs');

function restoreFixtureHtml({ trash = false, missingRestore = false, invalidRestore = false } = {}) {
  if (!trash || missingRestore) return '<!doctype html><html><body><h1>Active records</h1></body></html>';
  const ids = ['demo', 'migrated'];
  return `<!doctype html><html><body><h1>Trash</h1>${ids.map(id => `
    <form data-testid="record-restore-form" method="post" action="/bookmarks/${invalidRestore ? 'wrong' : id}/restore">
      <input type="hidden" name="record_id" value="${id}"><button type="submit">Restore ${id}</button>
    </form>`).join('')}</body></html>`;
}

async function withRestoreFixture(options, run) {
  const records = {
    demo: { id: 'demo', title: 'Demo', url: 'https://example.test/demo', category: '未整理', trashed_at: '2026-10-19T00:00:00Z' },
    migrated: { id: 'migrated', title: 'Migrated', url: 'https://example.test/migrated', category: '未整理', trashed_at: '2026-10-19T00:00:00Z' },
  };
  const formPosts = [];
  const apiRestoreCalls = [];
  const server = http.createServer(async (request, response) => {
    const url = new URL(request.url, 'http://127.0.0.1');
    const recordMatch = url.pathname.match(/^\/api\/bookmarks\/([^/]+)$/);
    if (recordMatch && request.method === 'GET') {
      const item = records[decodeURIComponent(recordMatch[1])];
      response.writeHead(item ? 200 : 404, { 'content-type': 'application/json' });
      response.end(JSON.stringify(item || { error: 'not found' }));
      return;
    }
    if (url.pathname.startsWith('/api/bookmarks/') && url.pathname.endsWith('/restore')) {
      apiRestoreCalls.push(url.pathname);
      response.writeHead(404, { 'content-type': 'application/json' });
      response.end(JSON.stringify({ error: 'API restore is not available' }));
      return;
    }
    if (request.method === 'POST' && url.pathname.startsWith('/bookmarks/')) {
      const chunks = [];
      for await (const chunk of request) chunks.push(chunk);
      const body = new URLSearchParams(Buffer.concat(chunks).toString());
      const recordId = body.get('record_id');
      formPosts.push({ action: url.pathname, record_id: recordId });
      const expectedAction = `/bookmarks/${recordId}/restore`;
      if (url.pathname === expectedAction && records[recordId]) delete records[recordId].trashed_at;
      response.writeHead(303, { location: '/?trash=1' });
      response.end();
      return;
    }
    response.writeHead(200, { 'content-type': 'text/html' });
    response.end(restoreFixtureHtml({ ...options, trash: url.searchParams.get('trash') === '1' }));
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  try { await run({ base, records, formPosts, apiRestoreCalls }); } finally {
    server.closeAllConnections();
    await new Promise(resolve => server.close(resolve));
  }
}

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
    await withRestoreFixture({}, async ({ base, records, formPosts, apiRestoreCalls }) => {
      const page = await browser.newPage();
      for (const path of ['/', '/categories']) {
        await page.goto(new URL(path, base).toString());
        assert.equal(await page.locator('form[data-testid="record-restore-form"]').count(), 0,
          `${path} must not expose restore controls outside the trash view`);
      }
      for (const id of ['demo', 'migrated']) {
        const restored = await adapter.__test.restoreViaTrashPage(page, base, id);
        assert.equal(restored.trashed_at, undefined);
      }
      assert.deepEqual(formPosts.map(item => item.record_id), ['demo', 'migrated']);
      assert.equal(apiRestoreCalls.length, 0, 'restore must use the rendered trash form, not an API shortcut');
      assert.equal(records.demo.trashed_at, undefined);
      assert.equal(records.migrated.trashed_at, undefined);
      await page.close();
    });
    for (const options of [{ missingRestore: true }, { invalidRestore: true }]) {
      await withRestoreFixture(options, async ({ base }) => {
        const page = await browser.newPage();
        await assert.rejects(adapter.__test.restoreViaTrashPage(page, base, 'demo'), /restore/);
        await page.close();
      });
    }
  } finally {
    await browser.close();
  }
  process.stdout.write('real Chromium detected missing move/search/restore controls and verified trash-only form restoration while fixture APIs remained functional\n');
})().catch(error => { process.stderr.write(String(error.stack || error)); process.exitCode = 1; });
