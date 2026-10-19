'use strict';
// Real UI happy-path probe. No API writes, DOM injection, seeded DB, or fake application.
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('/Users/milin/2026/软件开发/application-atlas/atlas-web/node_modules/@playwright/test');
const [caseName, rawTarget, output] = process.argv.slice(2);
const target = new URL(rawTarget);
if (!['budget', 'booking'].includes(caseName) || target.protocol !== 'http:' || target.hostname !== '127.0.0.1' || target.username || target.password) throw new Error('Explicit local HTTP target required');
const evidence = { case: caseName, kind: 'real_browser_happy_path', writes: 'UI controls only', checks: [], blocked: [], pageErrors: [], requests: [] };
let browser;
function check(value, message) { if (!value) throw new Error(message); }
const proxy = http.createServer((req, res) => {
  let url;
  try { url = new URL(req.url); } catch { /* blocked below */ }
  if (!url || url.origin !== target.origin || url.protocol !== 'http:') {
    evidence.blocked.push({ method: req.method, url: req.url });
    res.writeHead(403); res.end('Denied non-target origin'); return;
  }
  const headers = { ...req.headers, host: target.host };
  delete headers['proxy-authorization']; delete headers['proxy-connection'];
  const upstream = http.request({ hostname: '127.0.0.1', port: Number(target.port), method: req.method,
    path: url.pathname + url.search, headers }, incoming => { res.writeHead(incoming.statusCode, incoming.headers); incoming.pipe(res); });
  upstream.on('error', () => { if (!res.headersSent) res.writeHead(502); res.end('Target unavailable'); });
  req.on('error', () => upstream.destroy()); req.pipe(upstream);
});
proxy.on('connect', (req, socket) => { evidence.blocked.push({ method: 'CONNECT', url: req.url }); socket.destroy(); });
proxy.on('upgrade', (req, socket) => { evidence.blocked.push({ method: 'UPGRADE', url: req.url }); socket.destroy(); });
proxy.on('clientError', (_error, socket) => socket.destroy());
async function waitForValue(page, apiPath, predicate) {
  const deadline = Date.now() + 8000;
  let last;
  while (Date.now() < deadline) {
    last = await page.evaluate(async endpoint => { const response = await fetch(endpoint); return { status: response.status, body: await response.json() }; }, apiPath);
    if (last.status >= 200 && last.status < 300 && predicate(last.body)) return last.body;
    await page.waitForTimeout(100);
  }
  throw new Error('UI action not reflected in real API: ' + apiPath + ' ' + JSON.stringify(last));
}
(async () => {
  await new Promise((resolve, reject) => { proxy.once('error', reject); proxy.listen(0, '127.0.0.1', resolve); });
  try {
    browser = await chromium.launch({ headless: true, proxy: { server: 'http://127.0.0.1:' + proxy.address().port }, args: ['--proxy-bypass-list=<-loopback>'] });
    const context = await browser.newContext({ viewport: { width: 1280, height: 900 }, serviceWorkers: 'block' });
    const page = await context.newPage();
    page.on('pageerror', error => evidence.pageErrors.push(error.message));
    page.on('response', response => evidence.requests.push({ method: response.request().method(), url: response.url(), status: response.status() }));
    await page.goto(target.href, { waitUntil: 'domcontentloaded', timeout: 10000 });
    const control = name => page.getByTestId(name);
    if (caseName === 'budget') {
      await control('month').fill('2032-07');
      await control('month').dispatchEvent('change');
      await page.waitForTimeout(300);
      await control('category-name').fill('浏览器餐饮');
      await control('category-budget').fill('100.00');
      await control('category-save').click();
      const state = await waitForValue(page, '/api/state?month=2032-07', data => data.categories.some(row => row.name === '浏览器餐饮'));
      const category = state.categories.find(row => row.name === '浏览器餐饮');
      evidence.checks.push({ id: 'BU01', status: 'passed', detail: 'Created category through actual UI; real API readback matched' });
      await control('expense-date').fill('2032-07-12');
      await control('expense-category').selectOption(String(category.id));
      await control('expense-amount').fill('12.34');
      await control('expense-note').fill('浏览器真实输入');
      await control('expense-save').click();
      const after = await waitForValue(page, '/api/state?month=2032-07', data => data.transactions.some(row => row.note === '浏览器真实输入'));
      check(after.totals.spent === '12.34' && after.totals.remaining === '87.66', 'UI-created expense totals wrong');
      evidence.checks.push({ id: 'BU02', status: 'passed', detail: 'Created expense through actual UI; real API list and totals matched' });
    } else {
      async function login(name) {
        await control('login-username').fill(name);
        await control('login-password').fill('AtlasDemo-' + (name === 'admin' ? 'Admin' : 'Alice') + '-9!');
        await control('login-submit').click();
        await waitForValue(page, '/api/me', data => (data.user || data).username === name);
      }
      await login('admin');
      await control('resource-name').fill('浏览器活动室');
      await control('resource-save').click();
      const resources = await waitForValue(page, '/api/resources', data => data.resources.some(row => row.name === '浏览器活动室'));
      const resource = resources.resources.find(row => row.name === '浏览器活动室');
      evidence.checks.push({ id: 'KU01', status: 'passed', detail: 'Admin login and resource creation used actual UI controls' });
      await control('logout').click();
      await control('login-submit').waitFor({ state: 'visible' });
      await login('alice');
      await control('booking-resource').selectOption(String(resource.id));
      await control('booking-start').fill('2032-07-12T10:00:00+08:00');
      await control('booking-end').fill('2032-07-12T11:00:00+08:00');
      await control('booking-note').fill('浏览器居民预约');
      await control('booking-save').click();
      const after = await waitForValue(page, '/api/bookings', data => data.bookings.some(row => row.note === '浏览器居民预约'));
      const booking = after.bookings.find(row => row.note === '浏览器居民预约');
      check(String(booking.resource_id) === String(resource.id) && booking.status !== 'cancelled', 'UI-created booking wrong');
      evidence.checks.push({ id: 'KU02', status: 'passed', detail: 'Resident login and actual UI booking persisted; verified via real read-only API' });
    }
    await page.screenshot({ path: path.join(output, 'browser.png'), fullPage: true });
    evidence.screenshot = 'browser.png; capture only, not independently visually assessed';
    evidence.bodyText = await page.locator('body').innerText();
    evidence.status = 'passed';
  } catch (error) {
    evidence.status = 'failed_or_tool_error_unverified'; evidence.error = error.stack || String(error);
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => proxy.close(resolve));
    fs.writeFileSync(path.join(output, 'browser-result.json'), JSON.stringify(evidence, null, 2));
  }
  process.exitCode = evidence.status === 'passed' ? 0 : 1;
})().catch(error => { console.error(error.stack); process.exitCode = 1; });
