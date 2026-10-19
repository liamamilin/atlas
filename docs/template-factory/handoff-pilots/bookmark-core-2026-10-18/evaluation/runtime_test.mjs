import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import http from 'node:http';

const require = createRequire(import.meta.url);
const { chromium } = require('/Users/milin/2026/软件开发/application-atlas/atlas-web/node_modules/@playwright/test');
const args = Object.fromEntries(process.argv.slice(2).reduce((a, x, i, xs) => i % 2 ? a : [...a, [x.slice(2), xs[i + 1]]], []));
const root = args.evidence;
const events = [], actions = [], checks = [];
let sequence = 0, currentCheck = 'setup', controlSequence = 0, browser, context, page, adapter, denyProxy;
const A = { id: 'A', url: 'https://example.com/item/lamp?source=collection&variant=warm#details' };
const B = { id: 'B', url: 'https://example.com/item/bookshelf', title: '折叠书架', note: '小户型，周末量尺寸', category: '待购' };
const C = { id: 'C', url: 'https://example.com/tutorial/bread', title: '酸面包教程', note: '周日尝试' };
const fixtures = [A, B, C];
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const write = (name, data) => fs.writeFile(path.join(root, name), typeof data === 'string' ? data : JSON.stringify(data, null, 2));
class ProductAssertion extends Error {}
function assert(value, message, observed) { if (!value) throw new ProductAssertion(`${message}\nObserved: ${JSON.stringify(observed)}`); }
function url(value) { return new URL(value).href; }
function urls(records) { return records.map(r => url(r.url)).sort(); }
async function act(name, fn) {
  const item = { at: new Date().toISOString(), check: currentCheck, name };
  actions.push(item);
  try { const value = await fn(); item.result = value ?? 'completed'; return value; }
  catch (error) { item.error = String(error.stack || error); throw error; }
}
async function shot(name) {
  const base = `${String(++sequence).padStart(3, '0')}-${currentCheck}-${name}`;
  const body = await page.locator('body').innerText().catch(e => `BODY UNAVAILABLE: ${e}`);
  await write(`${base}.txt`, body);
  await page.screenshot({ path: path.join(root, `${base}.png`), fullPage: true }).catch(e => events.push({ type: 'screenshot-error', error: String(e) }));
  let records;
  try { records = await adapter.records(); } catch (e) { records = { adapterError: String(e) }; }
  await write(`${base}.json`, { url: page.url(), body, records });
  return base;
}
async function check(id, area, fn, exploratory = false) {
  currentCheck = id;
  const result = { id, area, kind: exploratory ? 'exploration' : 'required', startedAt: new Date().toISOString() };
  checks.push(result);
  try { result.observation = await fn(); result.status = 'runtime_assertions_passed'; }
  catch (error) {
    result.status = error instanceof ProductAssertion ? 'assertion_failed_needs_review' : 'tool_or_environment_error_unverified';
    result.error = String(error.stack || error);
  }
  result.evidence = await shot(result.status).catch(e => `SNAPSHOT FAILED: ${e}`);
  result.finishedAt = new Date().toISOString();
  await write('runtime-results.json', { label: args.label, fixtures, checks, actions, events });
}
async function control(action) {
  const id = String(++controlSequence).padStart(3, '0');
  await fs.writeFile(path.join(args.control, `request-${id}.json`), JSON.stringify({ action }));
  const deadline = Date.now() + 25000;
  while (Date.now() < deadline) {
    try {
      const response = JSON.parse(await fs.readFile(path.join(args.control, `response-${id}.json`), 'utf8'));
      if (!response.ok) throw new Error(response.error);
      return response;
    } catch (error) { if (error.code !== 'ENOENT') throw error; }
    await sleep(50);
  }
  throw new Error(`Supervisor control timeout: ${action}`);
}
async function expectRecords(expected, options = {}) {
  const records = await adapter.records();
  assert(JSON.stringify(urls(records)) === JSON.stringify(expected.map(r => url(r.url)).sort()), 'Visible record URLs must match expected records without duplicates.', records);
  for (const fixture of expected) {
    const record = records.find(r => url(r.url) === url(fixture.url));
    if (fixture.title) assert(record.title === fixture.title, `Exact title retained for ${fixture.id}.`, record);
    if (fixture.note) assert(record.note === fixture.note, `Exact note retained for ${fixture.id}.`, record);
  }
  return records;
}
async function all() { await adapter.viewCategory('all'); await adapter.search(''); }
async function persistence() {
  await all(); await expectRecords(fixtures);
  await adapter.viewCategory('学习'); await expectRecords([B, C]);
  await adapter.viewCategory('待购'); await expectRecords([]);
  await adapter.viewCategory(null); await expectRecords([A]);
  await all(); await adapter.search('书架'); await expectRecords([B]);
  await adapter.search('面包'); await expectRecords([C]);
  await adapter.search(''); await expectRecords(fixtures);
}
function attachPage(p) {
  p.on('response', response => {
    const request = response.request();
    if (!['GET', 'HEAD'].includes(request.method())) events.push({ check: currentCheck, type: 'write-response', method: request.method(), url: response.url(), status: response.status(), submittedBody: request.postData() });
  });
  p.on('framenavigated', frame => {
    if (frame === p.mainFrame() && /^https?:/.test(frame.url())) {
      const target = new URL(frame.url());
      if (!['127.0.0.1', 'localhost'].includes(target.hostname)) events.push({ check: currentCheck, type: 'external-navigation', url: frame.url() });
    }
  });
  p.on('console', msg => events.push({ check: currentCheck, type: 'console', level: msg.type(), text: msg.text() }));
  p.on('pageerror', error => events.push({ check: currentCheck, type: 'pageerror', text: String(error) }));
  p.on('dialog', dialog => { events.push({ check: currentCheck, type: 'dialog', text: dialog.message() }); dialog.dismiss().catch(() => {}); });
  p.on('requestfailed', request => events.push({ check: currentCheck, type: 'requestfailed', url: request.url(), failure: request.failure() }));
}

try {
  // Redirect chains may bypass Playwright routing. A local deny-only proxy
  // prevents every external network connection, including redirected requests.
  denyProxy = http.createServer((req, res) => { res.writeHead(502); res.end('External network disabled by test operator'); });
  denyProxy.on('connect', (req, socket) => {
    events.push({ check: currentCheck, type: 'proxy-denied-external', target: req.url });
    socket.end('HTTP/1.1 502 Bad Gateway\r\nConnection: close\r\n\r\n');
  });
  await new Promise(resolve => denyProxy.listen(0, '127.0.0.1', resolve));
  browser = await chromium.launch({ headless: true, proxy: { server: `http://127.0.0.1:${denyProxy.address().port}`, bypass: '127.0.0.1,localhost' } });
  context = await browser.newContext({ viewport: { width: 1440, height: 1050 }, locale: 'zh-CN' });
  context.on('page', attachPage);
  context.on('request', request => {
    const target = new URL(request.url());
    if (request.isNavigationRequest() && /^https?:/.test(target.protocol) && !['127.0.0.1', 'localhost'].includes(target.hostname)) events.push({ check: currentCheck, type: 'external-navigation-request', url: request.url() });
  });
  context.on('response', async response => {
    if (response.status() >= 300 && response.status() < 400) {
      const location = (await response.allHeaders()).location;
      if (location) events.push({ check: currentCheck, type: 'server-redirect', url: response.url(), status: response.status(), location, resolvedTarget: new URL(location, response.url()).href });
    }
  });
  await context.route('**/*', async route => {
    const request = route.request();
    const target = new URL(request.url());
    if (!['127.0.0.1', 'localhost'].includes(target.hostname) && !['data:', 'about:'].includes(target.protocol)) {
      events.push({ check: currentCheck, type: 'blocked-external-request', url: request.url(), navigation: request.isNavigationRequest() });
      if (request.isNavigationRequest()) await route.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: '<!doctype html><meta charset="utf-8"><title>合成外链验证页</title><p>本页面由本地测试拦截器提供，没有访问外站。</p>' });
      else await route.abort('blockedbyclient');
    } else await route.continue();
  });
  page = await context.newPage();
  const module = await import(pathToFileURL(args.adapter).href);
  adapter = module.createAdapter(page, args['base-url']);

  await check('R01', '运行交付', async () => {
    await act('Load Chinese app through assigned loopback port.', () => adapter.ready());
    const body = await page.locator('body').innerText();
    assert(/[\u4e00-\u9fff]/.test(body), 'Chinese text is present in usable initial UI.', body);
    await expectRecords([]);
    return { body, note: 'Source dependency review and supervisor process evidence supplement this browser check.' };
  });
  await check('R02', '保存', async () => {
    await act('Save A with URL only.', () => adapter.save(A)); await shot('saved-A');
    await act('Save C with title and note, no category.', () => adapter.save(C)); await shot('saved-C');
    await act('Refresh.', () => page.reload()); await all();
    return await expectRecords([A, C]);
  });
  await check('R03', '未分类', async () => {
    await act('Open unclassified view.', () => adapter.viewCategory(null));
    return await expectRecords([A, C]);
  });
  await check('R04', '创建及选择归类', async () => {
    await act('Create 待购.', () => adapter.createCategory('待购')); await shot('created-待购');
    await act('Create 学习.', () => adapter.createCategory('学习')); await shot('created-学习');
    await act('Save B with category 待购.', () => adapter.save(B));
    await act('Browse 待购.', () => adapter.viewCategory('待购'));
    return await expectRecords([B]);
  });
  await check('R05', '移动', async () => {
    await adapter.viewCategory(null);
    await act('Move C from unclassified to 学习.', () => adapter.move(C, '学习')); await shot('moved-C');
    await adapter.viewCategory('待购');
    await act('Move B from 待购 to 学习.', () => adapter.move(B, '学习')); await shot('moved-B');
    await page.reload();
    await adapter.viewCategory('学习'); const destination = await expectRecords([B, C]); await shot('destination');
    await adapter.viewCategory(null); await expectRecords([A]); await shot('unclassified-after-move');
    await adapter.viewCategory('待购'); await expectRecords([]); await shot('source-after-move');
    await all(); await expectRecords(fixtures);
    return { destination };
  });
  await check('R06', '搜索', async () => {
    await all();
    await act('Search 书架 over all records.', () => adapter.search('书架')); await expectRecords([B]); await shot('书架');
    await act('Search 面包 over all records.', () => adapter.search('面包')); await expectRecords([C]); await shot('面包');
    await act('Search nonexistent term.', () => adapter.search('不存在的词零匹配')); await expectRecords([]);
    const emptyBody = await page.locator('body').innerText(); await shot('empty-search');
    await act('Clear search.', () => adapter.search('')); await expectRecords(fixtures);
    return { emptyBody, scope: 'all records selected through product UI' };
  });
  await check('R07', '打开原网页', async () => {
    const opened = [];
    for (const fixture of fixtures) {
      if (!page.url().startsWith(args['base-url'])) await adapter.ready();
      await all();
      const before = events.length;
      const href = await act(`Open original URL for ${fixture.id}.`, () => adapter.openOriginal(fixture));
      await sleep(250);
      const external = events.slice(before).filter(e => e.type === 'external-navigation-request');
      const navigations = events.slice(before).filter(e => e.type === 'external-navigation');
      const redirects = events.slice(before).filter(e => e.type === 'server-redirect');
      const exactWitness = url(href) === url(fixture.url) || navigations.some(e => url(e.url) === url(fixture.url)) || redirects.some(e => url(e.resolvedTarget) === url(fixture.url));
      assert(exactWitness, 'Full original target including fragment is witnessed in actual href, server Location, or browser URL; internal redirect links are accepted.', { href, expected: fixture.url, navigations, redirects });
      assert(external.some(e => { const a = new URL(e.url), b = new URL(fixture.url); return a.origin === b.origin && a.pathname === b.pathname && a.search === b.search; }), 'Actual browser navigation to original URL was intercepted.', external);
      opened.push({ id: fixture.id, href, interceptedNavigation: external, redirects, browserUrls: navigations });
      for (const popup of context.pages()) if (popup !== page) await popup.close();
      if (!page.url().startsWith(args['base-url'])) await adapter.ready();
    }
    return opened;
  });
  await check('R08', '持久化', async () => {
    await page.goto(args['base-url']); await persistence(); await shot('refresh-persisted');
    const restart = await act('Normally stop and restart with same data directory.', () => control('restart'));
    await adapter.ready(); await persistence(); await shot('normal-restart-persisted');
    const isolated = await act('Start with separate new empty data directory.', () => control('isolate'));
    await adapter.ready(); await all(); await expectRecords([]); await shot('fresh-directory-empty');
    await act('Restore core test data instance.', () => control('restore'));
    await adapter.ready(); await persistence();
    return { restart, isolated };
  });
  await check('R09', '反馈及失败后的数据安全', async () => {
    await all(); const before = await expectRecords(fixtures);
    await act('Attempt empty URL save with existing data.', () => adapter.submitEmptyUrl());
    const feedback = await page.locator('body').innerText(); await shot('empty-url-feedback');
    await page.reload(); await all(); const after = await expectRecords(fixtures);
    return { before, after, feedback, note: 'Successful operation feedback is also captured in R02/R04/R05 screenshots.' };
  });

  await check('M01', '恢复及状态', async () => {
    const crash = await control('crash_restart'); await adapter.ready(); await persistence(); await shot('crash-recovered');
    await control('explore'); await adapter.ready();
    const otherPage = await context.newPage(); const other = module.createAdapter(otherPage, args['base-url']); await other.ready();
    const d = { id: 'D', url: 'https://example.com/explore/tab-one', title: '多页签一', note: '第一张页面先保存' };
    const e = { id: 'E', url: 'https://example.com/explore/tab-two', title: '多页签二', note: '第二张页面随后保存' };
    await adapter.save(d); await other.save(e); await page.reload(); await all(); await expectRecords([d, e]);
    await otherPage.close();
    let repeatedSave = { status: 'unverified', reason: 'Adapter does not implement duplicate submit.' };
    if (adapter.doubleSave) {
      const f = { url: 'https://example.com/explore/double-save', title: '重复点击保存', note: '同一表单双击' };
      repeatedSave = await adapter.doubleSave(f); await page.reload(); await all();
      repeatedSave = { interaction: repeatedSave, records: await adapter.records() };
    }
    return { crash, multiTabSequential: 'both records present', repeatedSave };
  }, true);
  await check('M02', '真实输入边界', async () => {
    const boundary = { url: 'https://example.com/explore/boundary?one=two&quoted=%22%E4%B8%AD%E6%96%87%22#section', title: `中文 空格 '双引号" ${'长标题'.repeat(80)}`, note: `备注 \" ' & 中文\n${'长备注内容 '.repeat(160)}` };
    await adapter.save(boundary); await page.reload(); await all();
    let records = await adapter.records(); let found = records.find(r => url(r.url) === url(boundary.url));
    assert(found && found.title === boundary.title && found.note === boundary.note, 'Long Chinese, spaces, quotes, note, and URL round trip exactly.', found);
    await adapter.save(boundary); await page.reload(); await all(); records = await adapter.records();
    return { duplicateUrlCount: records.filter(r => url(r.url) === url(boundary.url)).length, records };
  }, true);
  await check('M03', '失败处理', async () => {
    const probes = await control('probe_start_failures');
    await page.reload(); await all();
    return { ...probes, afterFailureRecords: await adapter.records(), persistenceWriteFailure: 'unverified; no artificial storage fault injected' };
  }, true);
  await check('M04', '内容安全', async () => {
    const probe = { url: 'https://example.com/explore/safe-content-probe', title: `中文 ' \" & <b>标题</b>`, note: `<svg onload=\"window.__atlasLocalHarmlessProbe=1\"></svg> & ' \"` };
    await adapter.save(probe); await page.reload(); await all();
    const executed = await page.evaluate(() => window.__atlasLocalHarmlessProbe ?? null);
    const record = (await adapter.records()).find(r => url(r.url) === url(probe.url));
    assert(executed === null, 'Harmless local script marker must not execute.', { executed, record });
    assert(record?.title === probe.title && record?.note === probe.note, 'HTML special characters remain literal content.', record);
    return { executed, record };
  }, true);
  await check('M05', '上手及浏览', async () => ({ observation: 'Initial empty state, save/category/unclassified/search/open entry points, and empty search were captured in R01-R07. Adapter source documents actual UI routes; human reviewer assesses obstacles without aesthetic scoring.' }), true);
} catch (error) {
  await write('runtime-fatal.json', { error: String(error.stack || error), checks, actions, events });
  process.exitCode = 1;
} finally {
  await write('runtime-results.json', { label: args.label, fixtures, checks, actions, events });
  if (browser) await browser.close();
  if (denyProxy) await new Promise(resolve => denyProxy.close(resolve));
}
