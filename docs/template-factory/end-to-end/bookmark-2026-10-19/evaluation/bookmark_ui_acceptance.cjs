const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE);
const check = (ok, msg) => { if (!ok) throw new Error(msg); };
const out = name => path.join(process.env.EVIDENCE_DIR, 'screenshots', name);
const stateFile = () => path.join(process.env.EVIDENCE_DIR, 'browser-state.json');

async function submit(page, selector, values, expected = 303) {
  const form = page.locator(selector).first();
  check(await form.count(), `missing form ${selector}`);
  for (const [name, value] of Object.entries(values)) {
    const field = form.locator(`[name="${name}"]`).first();
    check(await field.count(), `missing field ${name}`);
    const tag = await field.evaluate(el => el.tagName.toLowerCase());
    if (tag === 'select') await field.selectOption(String(value)); else await field.fill(String(value));
  }
  const action = await form.getAttribute('action');
  const post = page.waitForResponse(r => r.request().method() === 'POST' && new URL(r.url()).pathname === action);
  const nav = page.waitForNavigation({ waitUntil: 'domcontentloaded' });
  const button = form.locator('button[type="submit"], input[type="submit"], button:not([type])').first();
  check(await button.count(), `missing submit button in ${selector}`);
  await button.click();
  const [, response] = await Promise.all([nav, post]);
  return response.status();
}

async function send(page, selector, values, expected = 303) {
  const status = await submit(page, selector, values, expected);
  check(expected === null || status === expected, `${selector} returned ${status}, expected ${expected}`);
  return status;
}

async function invalid(page, selector, values) {
  const form = page.locator(selector).first();
  check(await form.count(), `missing form ${selector}`);
  await form.evaluate(el => { el.noValidate = true; });
  for (const [name, value] of Object.entries(values)) {
    const field = form.locator(`[name="${name}"]`).first();
    check(await field.count(), `missing field ${name}`);
    const tag = await field.evaluate(el => el.tagName.toLowerCase());
    if (tag === 'select') await field.selectOption(String(value)); else await field.fill(String(value));
  }
  const action = await form.getAttribute('action');
  const post = page.waitForResponse(r => r.request().method() === 'POST' && new URL(r.url()).pathname === action);
  const nav = page.waitForNavigation({ waitUntil: 'domcontentloaded' });
  const button = form.locator('button[type="submit"], input[type="submit"], button:not([type])').first();
  check(await button.count(), `missing submit button in ${selector}`);
  await button.click();
  const [, response] = await Promise.all([nav, post]);
  return response.status();
}

const getCollections = page => page.locator('li.collection[data-collection-id]').evaluateAll(xs => xs.map(x => ({
  id: x.getAttribute('data-collection-id'), default: x.getAttribute('data-default'), text: x.innerText.trim(),
})));
const getBookmarks = page => page.locator('li.bookmark[data-bookmark-id]').evaluateAll(xs => xs.map(x => {
  const a = x.querySelector('a.bookmark-title');
  return { id: x.getAttribute('data-bookmark-id'), title: a?.textContent?.trim() || '', href: a?.getAttribute('href') || '', absoluteHref: a?.href || '', visibleText: x.innerText.trim() };
}));
async function browse(page, id) {
  const link = page.locator(`li.collection[data-collection-id="${id}"] a`).first();
  check(await link.count(), `missing collection browse link ${id}`);
  const nav = page.waitForNavigation({ waitUntil: 'domcontentloaded' });
  await Promise.all([nav, link.click()]);
}
async function query(page, q) {
  const form = page.locator('form[method="get"][action="/"]').first();
  check(await form.count(), 'missing search form');
  const input = form.locator('[name="q"]');
  check(await input.count(), 'missing q input');
  await input.fill(q);
  const nav = page.waitForNavigation({ waitUntil: 'domcontentloaded' });
  await Promise.all([nav, input.press('Enter')]);
  return getBookmarks(page);
}
function contextFor(browser) {
  return browser.newContext({ serviceWorkers: 'block' }).then(async context => {
    const allow = new Set([process.env.APP_URL, process.env.FIXTURE_BASE].map(x => new URL(x).origin));
    const blocked = [];
    await context.route('**/*', async route => {
      const url = route.request().url();
      if (allow.has(new URL(url).origin)) return route.continue();
      blocked.push(url);
      return route.abort('blockedbyclient');
    });
    return { context, blocked };
  });
}
async function installXssObserver(context) {
  await context.addInitScript(() => {
    let observed = window.__atlasXss;
    Object.defineProperty(window, '__atlasXss', {
      configurable: true,
      get() { return observed; },
      set(value) { observed = value; try { sessionStorage.setItem('__atlas_xss_observed', String(value)); } catch (_) {} },
    });
  });
}
async function openOriginal(page, context, record, url, screenshot, returnCollectionId = null) {
  const link = page.locator(`li.bookmark[data-bookmark-id="${record.id}"] a.bookmark-title`);
  check(await link.count(), `missing title link for ${record.id}`);
  const href = await link.getAttribute('href');
  const appOrigin = new URL(process.env.APP_URL).origin;
  const target = new URL(href, process.env.APP_URL);
  const isDirect = target.href === url;
  const isGoRedirect = target.origin === appOrigin && /^\/go\/[^/]+$/.test(target.pathname);
  check(isDirect || isGoRedirect, `title link is neither the original URL nor an app /go/<id> route: ${href}`);
  const popupWait = context.waitForEvent('page', { timeout: 1500 }).catch(() => null);
  await link.click();
  const popup = await popupWait;
  const destination = popup || page;
  await destination.waitForLoadState('domcontentloaded');
  check(destination.url() === url, `opened ${destination.url()}, expected ${url}`);
  const pathName = new URL(url).pathname;
  const expectedHeading = pathName === '/original' ? 'Local original fixture page'
    : pathName === '/second' ? 'Local secondary fixture page' : null;
  check(expectedHeading, `no local fixture heading is defined for ${pathName}`);
  check(await destination.locator('h1').innerText() === expectedHeading,
    `fixture page content mismatch for ${pathName}; expected ${expectedHeading}`);
  const finalUrl = destination.url();
  await destination.screenshot({ path: out(screenshot), fullPage: true });
  if (popup) await popup.close();
  const appResponse = await page.goto(process.env.APP_URL, { waitUntil: 'domcontentloaded' });
  check(appResponse?.status() === 200, 'could not restore app after opening original page');
  if (returnCollectionId !== null) await browse(page, returnCollectionId);
  return { finalUrl, navigation: isGoRedirect ? 'app-go-redirect' : 'direct-original-link', usedPopup: Boolean(popup), restoredApp: true, returnCollectionId };
}

async function captureTargetSnapshots(page, context, records, url, searchTerm, prefix) {
  const snapshots = [];
  for (const record of records) {
    const clicked = await openOriginal(page, context, record, url, `${prefix}-${record.id}.png`);
    snapshots.push({ id: record.id, title: record.title, href: record.href, visibleText: record.visibleText,
      expectedUrl: url, clickedUrl: clicked.finalUrl, navigation: clicked.navigation });
    await query(page, searchTerm);
  }
  return snapshots;
}

function classifyDuplicateOutcome(beforeRecords, afterRecords, postStatus) {
  const beforeById = new Map(beforeRecords.map(item => [item.id, item]));
  const sameIds = beforeRecords.length === afterRecords.length && afterRecords.every(item => beforeById.has(item.id));
  const fieldsChanged = sameIds && afterRecords.some(item => beforeById.get(item.id).title !== item.title
    || beforeById.get(item.id).href !== item.href || beforeById.get(item.id).expectedUrl !== item.expectedUrl);
  return postStatus >= 400 ? 'rejected'
    : afterRecords.length > beforeRecords.length ? 'created_new_record'
    : fieldsChanged ? 'updated_existing_record'
    : sameIds ? 'accepted_without_observable_change' : 'record_set_changed';
}
const sameRecordSnapshots = (left, right) => JSON.stringify([...left].sort((a, b) => a.id.localeCompare(b.id)))
  === JSON.stringify([...right].sort((a, b) => a.id.localeCompare(b.id)));

async function firstRun(browser) {
  const { context, blocked } = await contextFor(browser);
  await installXssObserver(context);
  const page = await context.newPage();
  const dialogs = [];
  page.on('dialog', async d => { dialogs.push(d.type()); await d.dismiss(); });
  const runId = process.env.RUN_ID;
  const makeUrl = pathName => new URL(`/${pathName}?token=${runId}_${pathName}`, process.env.FIXTURE_BASE).toString();
  const urls = { first: makeUrl('original'), second: makeUrl('second'), xss: makeUrl('xss') };
  const titles = { first: `Cobalt chair ${runId}`, second: `Green lamp ${runId}`, xss: `<img src=x onerror="window.__atlasXss=1"> XSS-${runId}` };
  const report = { phase: 'initial', runId, checks: [], urls, titles, duplicateSave: {} };
  const pass = (id, detail = '') => report.checks.push({ id, status: 'pass', detail });
  check((await page.goto(process.env.APP_URL)).status() === 200, 'initial app GET failed');
  let cats = await getCollections(page);
  const defaults = cats.filter(c => c.default === '1');
  check(defaults.length === 1, `expected one default collection, saw ${defaults.length}`);
  check(cats.length === 1 && (await getBookmarks(page)).length === 0, 'isolated library was not empty at start');
  const defaultCat = defaults[0];
  report.defaultCollection = { id: defaultCat.id, text: defaultCat.text };
  await browse(page, defaultCat.id);
  await send(page, 'form[method="post"][action="/bookmarks"]', { url: urls.first, title: titles.first });
  let records = await getBookmarks(page);
  const first = records.find(r => r.title === titles.first);
  check(first, 'default save not visible');
  report.bookmarks = { first: { id: first.id, url: urls.first, title: titles.first } };
  pass('save-to-default-without-category');
  await page.screenshot({ path: out('01-default-saved.png'), fullPage: true });

  const categoryName = `待购-${runId}`;
  await send(page, 'form[method="post"][action="/collections"]', { name: categoryName });
  cats = await getCollections(page);
  const newCat = cats.find(c => c.text.includes(categoryName));
  check(newCat, 'new collection missing from sidebar');
  report.createdCollection = { id: newCat.id, name: categoryName };
  pass('create-collection');
  await send(page, 'form[method="post"][action="/bookmarks"]', { url: urls.second, title: titles.second, collection_id: newCat.id });
  records = await getBookmarks(page);
  const second = records.find(r => r.title === titles.second);
  check(second, 'save in new category not visible');
  report.bookmarks.second = { id: second.id, url: urls.second, title: titles.second };
  await openOriginal(page, context, report.bookmarks.second, urls.second, '02-second-original.png', newCat.id);
  pass('save-in-new-collection');

  await browse(page, defaultCat.id);
  const moveSelector = `form[method="post"][action="/bookmarks/${first.id}/move"]`;
  await send(page, moveSelector, { collection_id: newCat.id });
  await browse(page, newCat.id);
  records = await getBookmarks(page);
  check(records.some(r => r.id === first.id) && records.some(r => r.id === second.id), 'destination browse missing moved or saved record');
  await browse(page, defaultCat.id);
  records = await getBookmarks(page);
  check(!records.some(r => r.id === first.id), 'moved record remains in default collection');
  pass('move-and-browse-by-category');

  records = await query(page, `${runId}_original`);
  check(records.some(r => r.id === first.id) && !records.some(r => r.id === second.id), 'URL keyword search result incorrect');
  records = await query(page, titles.second);
  check(records.some(r => r.id === second.id) && !records.some(r => r.id === first.id), 'title keyword search result incorrect');
  pass('keyword-search');
  await browse(page, newCat.id);
  await openOriginal(page, context, report.bookmarks.first, urls.first, '02-original-page.png', newCat.id);
  pass('open-original-page');
  await page.goto(process.env.APP_URL);

  // Exercise the same user action as the core default-category check: omit
  // collection_id and let the UI's default assignment apply.
  await send(page, 'form[method="post"][action="/bookmarks"]', { url: urls.xss, title: titles.xss });
  const xssOnSaveResponse = await page.evaluate(() => sessionStorage.getItem('__atlas_xss_observed'));
  records = await query(page, `${runId}_xss`);
  const xss = records.find(r => r.title === titles.xss);
  check(xss, 'XSS sentinel record missing');
  report.bookmarks.xss = { id: xss.id, url: urls.xss, title: titles.xss };
  const xssItem = page.locator(`li.bookmark[data-bookmark-id="${xss.id}"]`);
  check(await xssItem.locator('a.bookmark-title').innerText() === titles.xss, 'HTML title not preserved as literal text');
  check(await xssItem.locator('img[src="x"]').count() === 0, 'HTML title created an img element');
  check(xssOnSaveResponse === null && await page.evaluate(() => sessionStorage.getItem('__atlas_xss_observed')) === null
    && await page.evaluate(() => window.__atlasXss) === undefined && dialogs.length === 0,
    'HTML title executed script or opened a dialog during save response/search');
  report.htmlSafety = { xssObservedDuringSaveResponse: xssOnSaveResponse, xssObservedAfterSearch: await page.evaluate(() => sessionStorage.getItem('__atlas_xss_observed')), dialogs: [...dialogs] };
  await page.screenshot({ path: out('03-html-safety.png'), fullPage: true });
  pass('html-output-safety');

  const catCount = (await getCollections(page)).length;
  const idsBeforeInvalid = (await query(page, runId)).map(r => r.id).sort();
  report.invalidInputs = [];
  for (const item of [
    ['empty-url', ''], ['malformed-url', 'https://'],
    ['javascript-scheme', 'javascript:window.__atlasXss=2'],
    ['data-scheme', 'data:text/html,<script>window.__atlasXss=3</script>'],
  ]) {
    const status = await invalid(page, 'form[method="post"][action="/bookmarks"]', { url: item[1], title: `invalid-${item[0]}-${runId}` });
    check(status === 400, `${item[0]} returned ${status}, expected 400`);
    await page.goto(process.env.APP_URL);
    const ids = (await query(page, runId)).map(r => r.id).sort();
    check(JSON.stringify(ids) === JSON.stringify(idsBeforeInvalid), `${item[0]} dirtied bookmark inventory`);
    report.invalidInputs.push({ name: item[0], status, inventoryUnchanged: true });
  }
  for (const [name, value] of [['blank-category', '   '], ['duplicate-category', categoryName]]) {
    const status = await invalid(page, 'form[method="post"][action="/collections"]', { name: value });
    check(status === 400, `${name} returned ${status}, expected 400`);
    await page.goto(process.env.APP_URL);
    check((await getCollections(page)).length === catCount, `${name} dirtied category inventory`);
    const ids = (await query(page, runId)).map(r => r.id).sort();
    check(JSON.stringify(ids) === JSON.stringify(idsBeforeInvalid), `${name} changed bookmark inventory`);
    report.invalidInputs.push({ name, status, inventoryUnchanged: true });
  }
  pass('invalid-inputs-no-dirty-data');

  const dupeObs = report.duplicateSave;
  const duplicateSearch = `${runId}_second`;
  const before = await query(page, duplicateSearch);
  dupeObs.beforeRecords = await captureTargetSnapshots(page, context, before, urls.second, duplicateSearch, 'duplicate-before');
  dupeObs.beforeCount = dupeObs.beforeRecords.length;
  dupeObs.postStatus = await send(page, 'form[method="post"][action="/bookmarks"]', {
    url: urls.second, title: `Repeated ${runId}`, collection_id: newCat.id,
  }, null);
  await page.goto(process.env.APP_URL);
  const after = await query(page, duplicateSearch);
  dupeObs.afterRecords = await captureTargetSnapshots(page, context, after, urls.second, duplicateSearch, 'duplicate-after');
  dupeObs.afterCount = dupeObs.afterRecords.length;
  dupeObs.outcome = classifyDuplicateOutcome(dupeObs.beforeRecords, dupeObs.afterRecords, dupeObs.postStatus);
  dupeObs.contract = 'risk observation only; fail only if frozen contract promises uniqueness/idempotency';
  const duplicateContract = process.env.DUPLICATE_URL_CONTRACT || 'observe';
  if (duplicateContract === 'idempotent') {
    const beforeReplay = dupeObs.afterRecords;
    const replayStatus = await send(page, 'form[method="post"][action="/bookmarks"]', {
      url: urls.second, title: `Repeated ${runId}`, collection_id: newCat.id,
    }, null);
    await page.goto(process.env.APP_URL);
    const replayRows = await query(page, duplicateSearch);
    const afterReplay = await captureTargetSnapshots(page, context, replayRows, urls.second, duplicateSearch, 'idempotency-replay');
    dupeObs.idempotencyReplay = { postStatus: replayStatus, beforeRecords: beforeReplay, afterRecords: afterReplay,
      unchanged: replayStatus < 400 && sameRecordSnapshots(beforeReplay, afterReplay) };
    dupeObs.afterRecords = afterReplay;
    dupeObs.afterCount = afterReplay.length;
    dupeObs.contractResult = dupeObs.idempotencyReplay.unchanged ? 'pass' : 'fail';
  } else if (duplicateContract === 'unique-url') {
    dupeObs.contractResult = dupeObs.afterCount === 1 ? 'pass' : 'fail';
  } else {
    dupeObs.contractResult = 'observation-only';
  }
  if (dupeObs.contractResult === 'fail') {
    report.status = 'failed';
    report.duplicateSave = dupeObs;
    report.failure = { contract: duplicateContract, outcome: dupeObs.outcome, recordCount: dupeObs.afterCount };
    fs.writeFileSync(stateFile(), JSON.stringify(report, null, 2) + '\n');
    throw new Error(`frozen ${duplicateContract} contract violated by repeated save behavior`);
  }
  report.expectedAfterRestart = { secondUrlRecords: dupeObs.afterRecords };
  const latestSecond = dupeObs.afterRecords.find(r => r.title === `Repeated ${runId}`) || dupeObs.afterRecords[0];
  if (latestSecond) report.bookmarks.second = { id: latestSecond.id, url: urls.second, title: latestSecond.title };
  report.bookmarks.secondUrlRecordIds = dupeObs.afterRecords.map(r => r.id).sort();
  report.duplicateSave = dupeObs;
  report.checks.push({ id: 'duplicate-save-risk-observation', status: duplicateContract === 'observe' ? 'observed' : 'pass', detail: `${dupeObs.outcome}; ${dupeObs.beforeCount} -> ${dupeObs.afterCount}; ${dupeObs.contractResult}` });
  await browse(page, newCat.id);
  await page.screenshot({ path: out('04-before-restart.png'), fullPage: true });
  try { await page.goto('https://example.com/', { timeout: 3000 }); } catch (_) {}
  check(blocked.some(url => url.startsWith('https://example.com/')), 'external browser request was not blocked');
  report.blockedRequests = blocked;
  report.dialogs = dialogs;
  report.status = 'passed';
  fs.writeFileSync(stateFile(), JSON.stringify(report, null, 2) + '\n');
  await context.close();
  return report;
}

async function restarted(browser) {
  const state = JSON.parse(fs.readFileSync(stateFile(), 'utf8'));
  const { context } = await contextFor(browser);
  await installXssObserver(context);
  const page = await context.newPage();
  const response = await page.goto(process.env.APP_URL, { waitUntil: 'domcontentloaded' });
  check(response.status() === 200, 'post-restart app GET failed');
  const cats = await getCollections(page);
  check(cats.some(c => c.id === state.defaultCollection.id && c.default === '1'), 'default collection lost on restart');
  check(cats.some(c => c.id === state.createdCollection.id && c.text.includes(state.createdCollection.name)), 'new collection lost on restart');
  await browse(page, state.createdCollection.id);
  let records = await getBookmarks(page);
  check(records.some(r => r.id === state.bookmarks.first.id && r.title === state.bookmarks.first.title), 'moved record lost on restart');
  check(records.some(r => r.id === state.bookmarks.second.id && r.title === state.bookmarks.second.title), 'second record lost on restart');
  check(!records.some(r => r.id === state.bookmarks.xss.id), 'default record appeared in separate category');
  const duplicateSearch = `${state.runId}_second`;
  const urlB = await query(page, duplicateSearch);
  const persistedSecondTargets = await captureTargetSnapshots(page, context, urlB, state.urls.second, duplicateSearch, 'after-restart-second');
  const persistedById = new Map(persistedSecondTargets.map(item => [item.id, item]));
  for (const expected of state.expectedAfterRestart.secondUrlRecords) {
    const actual = persistedById.get(expected.id);
    check(actual && actual.title === expected.title && actual.href === expected.href
      && actual.visibleText === expected.visibleText && actual.expectedUrl === expected.expectedUrl
      && actual.clickedUrl === expected.clickedUrl && actual.navigation === expected.navigation,
      `observed duplicate-save state did not persist for record ${expected.id}`);
  }
  check(persistedSecondTargets.length === state.expectedAfterRestart.secondUrlRecords.length,
    'duplicate-save record count changed after restart');
  check((await query(page, `no-match-${state.runId}`)).length === 0, 'no-match search returned a record after restart');
  await browse(page, state.defaultCollection.id);
  records = await getBookmarks(page);
  check(records.some(r => r.id === state.bookmarks.xss.id), 'default record lost on restart');
  const item = page.locator(`li.bookmark[data-bookmark-id="${state.bookmarks.xss.id}"]`);
  check(await item.locator('a.bookmark-title').innerText() === state.titles.xss, 'escaped title changed after restart');
  check(await item.locator('img[src="x"]').count() === 0, 'HTML injected after restart');
  check(await page.evaluate(() => window.__atlasXss) === undefined
    && await page.evaluate(() => sessionStorage.getItem('__atlas_xss_observed')) === null,
    'HTML-shaped title executed after restart');
  await page.screenshot({ path: out('05-after-restart.png'), fullPage: true });
  await browse(page, state.createdCollection.id);
  await openOriginal(page, context, state.bookmarks.first, state.bookmarks.first.url, '06-after-restart-original.png', state.createdCollection.id);
  const result = { phase: 'after-restart', status: 'passed', actualContainerRestart: true,
    checks: ['collections', 'bookmarks-and-moves', 'search', 'first-and-second-original-targets', 'duplicate-save-observed-state', 'html-safety'],
    secondTargetSnapshots: persistedSecondTargets };
  fs.writeFileSync(path.join(process.env.EVIDENCE_DIR, 'after-restart.json'), JSON.stringify(result, null, 2) + '\n');
  await context.close();
  return result;
}

if (require.main === module) (async () => {
  const browser = await chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_EXECUTABLE });
  try {
    const report = process.env.PHASE === 'initial' ? await firstRun(browser) : await restarted(browser);
    process.stdout.write(JSON.stringify(report));
  } finally { await browser.close(); }
})().catch(error => { console.error(error.stack || String(error)); process.exit(1); });

module.exports = { getCollections, getBookmarks, openOriginal, installXssObserver, classifyDuplicateOutcome, sameRecordSnapshots };
