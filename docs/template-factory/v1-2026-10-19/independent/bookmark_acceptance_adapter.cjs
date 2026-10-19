// Independent Chromium adapter for the frozen bookmark-manager contract.
// It uses only the template's declared HTML form/API contract. No app source is imported.
const CASE = {
  save: 'save bookmark with title and URL',
  move: 'assign category then move it to another category',
  find: 'find by category and by keyword',
  open: 'open and verify exact original URL using a controlled local fixture',
  restart: 'restart the same app container with the same persistent state and verify records remain',
  invalid: 'reject malformed/non-http(s) URL without creating a record',
  concurrent: 'run concurrent independent saves and verify every acknowledged write is present exactly once',
};
const checks = require('./bookmark_contract_checks.cjs');

function result(id, passed, detail) { return { id, passed: passed === true, detail }; }

function recordFrom(payload) {
  if (payload && typeof payload === 'object' && !Array.isArray(payload)) {
    for (const key of ['bookmark', 'record', 'data', 'item']) {
      if (payload[key] && typeof payload[key] === 'object' && !Array.isArray(payload[key])) return payload[key];
    }
    return payload;
  }
  return null;
}

function recordsFrom(payload) {
  if (Array.isArray(payload)) return payload;
  for (const key of ['bookmarks', 'items', 'data', 'records']) {
    if (payload && Array.isArray(payload[key])) return payload[key];
  }
  return [];
}

async function api(page, path, method = 'GET', body) {
  return page.evaluate(async ({ path, method, body }) => {
    const response = await fetch(path, {
      method,
      headers: body === undefined ? {} : { 'Content-Type': 'application/json' },
      body: body === undefined ? undefined : JSON.stringify(body),
      redirect: 'manual',
    });
    const text = await response.text();
    let data;
    try { data = JSON.parse(text); } catch { data = text; }
    return { status: response.status, data, location: response.headers.get('location') };
  }, { path, method, body });
}

function apiBase(path, search = {}) {
  const url = new URL(path, 'http://app.invalid');
  for (const [key, value] of Object.entries(search)) url.searchParams.set(key, value);
  return `${url.pathname}${url.search}`;
}

async function getById(page, id) {
  const response = await api(page, `/api/bookmarks/${encodeURIComponent(String(id))}`);
  if (response.status !== 200) throw new Error(`bookmark ${id} read returned ${response.status}`);
  return recordFrom(response.data);
}

async function exactSearch(page, query) {
  const response = await api(page, apiBase('/api/bookmarks', query));
  if (response.status !== 200) throw new Error(`bookmark search returned ${response.status}`);
  return recordsFrom(response.data);
}

async function submitViaUi(page, appUrl, token, fixtureBase) {
  const originalUrl = `${fixtureBase}/original`;
  const title = `Acceptance ${token}`;
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const form = page.locator('form[action="/bookmarks/new"]');
  await form.locator('[name="url"]').fill(originalUrl);
  await form.locator('[name="title"]').fill(title);
  const categoryField = form.locator('[name="category"]');
  if (await categoryField.count()) await categoryField.fill('待购');
  await Promise.all([
    page.waitForLoadState('domcontentloaded').catch(() => {}),
    form.locator('button[type="submit"], input[type="submit"]').first().click(),
  ]);
  const candidates = await exactSearch(page, { q: token });
  const record = candidates.find(item => item && item.title === title && item.url === originalUrl);
  if (!record || !record.id) throw new Error('UI save did not produce exactly the requested title and original URL');
  return { record, originalUrl, title };
}

async function verifyOpen(page, appUrl, record, originalUrl) {
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const href = `/go/${encodeURIComponent(String(record.id))}`;
  const link = page.locator(`a[href="${href}"]`).first();
  const [popup] = await Promise.all([page.waitForEvent('popup'), link.click()]);
  await popup.waitForLoadState('domcontentloaded');
  const exact = popup.url() === originalUrl;
  await popup.close();
  return exact;
}

async function createApiRecord(page, { url, title, category }) {
  const saved = await api(page, '/api/bookmarks', 'POST', { url, title, category });
  if (saved.status !== 201) throw new Error(`control bookmark save returned ${saved.status}`);
  const record = recordFrom(saved.data);
  if (!record || !record.id || record.url !== url || record.title !== title) {
    throw new Error('control bookmark acknowledgement omitted exact record identity/content');
  }
  return record;
}

async function runJourney({ page, appUrl, fixtureBase, token }) {
  const assertions = [];
  const { record, originalUrl, title } = await submitViaUi(page, appUrl, token, fixtureBase);
  const initialRecord = await getById(page, record.id);
  checks.assertExactRecord(initialRecord, { id: record.id, title, url: originalUrl, category: '待购' });

  const category = `Acceptance ${token} category`;
  const controlCategory = `Control ${token} category`;
  for (const name of [category, controlCategory]) {
    const created = await api(page, '/api/categories', 'POST', { name });
    if (created.status !== 201) throw new Error(`category create returned ${created.status}: ${name}`);
  }
  const categoryControl = await createApiRecord(page, {
    url: `${fixtureBase}/second?control=category`, title: 'Unrelated category control', category: controlCategory,
  });
  const keywordControl = await createApiRecord(page, {
    url: `${fixtureBase}/second?control=keyword`, title: 'Unrelated keyword control', category,
  });

  const moved = await api(page, `/api/bookmarks/${encodeURIComponent(record.id)}/move`, 'POST', { category });
  if (moved.status !== 200) throw new Error(`bookmark move returned ${moved.status}`);
  const movedRecord = await getById(page, record.id);
  const newCategoryRows = await exactSearch(page, { category });
  const oldCategoryRows = await exactSearch(page, { category: '待购' });
  checks.assertMoveState({ record: movedRecord, recordId: record.id, newCategory: category, oldCategoryRows, newCategoryRows });
  assertions.push(result(CASE.move, true, 'record category field changed; new filter includes target and old filter excludes it'));

  const byCategory = await exactSearch(page, { category });
  const byCategoryAndKeyword = await exactSearch(page, { category, q: token });
  const byKeyword = await exactSearch(page, { q: token });
  const keywordMiss = await exactSearch(page, { category, q: `definitely-no-match-${token}` });
  checks.assertFindState({ recordId: record.id, categoryControlId: categoryControl.id, keywordControlId: keywordControl.id,
    byCategory, byCombined: byCategoryAndKeyword, byKeyword, keywordMiss });
  await page.goto(checks.rootUrl(appUrl, { category, q: token }), { waitUntil: 'domcontentloaded' });
  const rendered = await page.locator('body').innerText();
  if (!rendered.includes(title) || rendered.includes('Unrelated category control') || rendered.includes('Unrelated keyword control')) {
    throw new Error('filtered Chromium UI did not isolate the target bookmark from the control record');
  }
  assertions.push(result(CASE.find, true, 'category, keyword, combined, negative match, and Chromium UI filters distinguish target from control'));

  const opened = await verifyOpen(page, appUrl, record, originalUrl);
  if (!opened) throw new Error('open action did not reach the exact controlled fixture URL');
  assertions.push(result(CASE.open, true, `opened exact fixture URL ${originalUrl}`));

  const before = (await exactSearch(page, { q: `${token}-invalid` })).length;
  for (const url of ['not a URL', 'javascript:alert(1)', 'ftp://example.test/file']) {
    const rejected = await api(page, '/api/bookmarks', 'POST', { url, title: `${token}-invalid` });
    if (rejected.status !== 400) throw new Error(`invalid URL was not rejected with 400: ${url}`);
  }
  const after = (await exactSearch(page, { q: `${token}-invalid` })).length;
  if (after !== before) throw new Error('invalid URL attempt created a bookmark');
  assertions.push(result(CASE.invalid, true, 'malformed and non-http(s) URLs returned 400 without a record'));

  const requested = Array.from({ length: 5 }, (_, index) => ({
    url: `https://${token}-${index}.atlas-acceptance.example/${token}-${index}`,
    title: `${token}-parallel-${index}`,
  }));
  const writes = await Promise.all(requested.map(item => api(page, '/api/bookmarks', 'POST', item)));
  if (writes.some(item => item.status !== 201)) throw new Error(`concurrent save status mismatch: ${writes.map(item => item.status).join(',')}`);
  const acknowledged = writes.map((write, index) => {
    const item = recordFrom(write.data);
    if (!item || !item.id || item.title !== requested[index].title || item.url !== requested[index].url) {
      throw new Error(`concurrent acknowledgement ${index} omitted exact ID/title/URL`);
    }
    return { id: String(item.id), title: item.title, url: item.url };
  });
  for (const item of acknowledged) {
    const rows = await exactSearch(page, { q: item.title });
    checks.assertAcknowledgedRecords(rows, [item]);
  }
  assertions.push(result(CASE.save, true, 'UI save retained exact title/URL and was assigned then moved'));
  assertions.push(result(CASE.concurrent, true, 'five concurrent acknowledgements each have a stable ID and appear exactly once'));
  return {
    assertions, token,
    primary: { id: String(record.id), title, url: originalUrl, category },
    categoryControl: { id: String(categoryControl.id), title: categoryControl.title, url: categoryControl.url, category: controlCategory },
    keywordControl: { id: String(keywordControl.id), title: keywordControl.title, url: keywordControl.url, category },
    concurrent: acknowledged,
  };
}

async function verifyPersisted(page, metadata) {
  if (!metadata || !metadata.primary || !metadata.categoryControl || !metadata.keywordControl || !Array.isArray(metadata.concurrent)) {
    throw new Error('initial phase metadata lacks primary/control/concurrent acknowledged records');
  }
  const primary = await getById(page, metadata.primary.id);
  checks.assertExactRecord(primary, metadata.primary);
  const categoryControl = await getById(page, metadata.categoryControl.id);
  checks.assertExactRecord(categoryControl, metadata.categoryControl);
  const keywordControl = await getById(page, metadata.keywordControl.id);
  checks.assertExactRecord(keywordControl, metadata.keywordControl);
  const categoryRows = await exactSearch(page, { category: metadata.primary.category });
  const oldCategoryRows = await exactSearch(page, { category: '待购' });
  const keywordRows = await exactSearch(page, { q: metadata.primary.title });
  if (!categoryRows.some(row => String(row.id) === metadata.primary.id)
      || categoryRows.some(row => String(row.id) === metadata.categoryControl.id)
      || !categoryRows.some(row => String(row.id) === metadata.keywordControl.id)
      || keywordRows.some(row => String(row.id) === metadata.keywordControl.id)
      || oldCategoryRows.some(row => String(row.id) === metadata.primary.id)
      || !keywordRows.some(row => String(row.id) === metadata.primary.id)) {
    throw new Error('original category/search filters did not preserve target inclusion and control exclusion');
  }
  for (const acknowledged of metadata.concurrent) {
    const rows = await exactSearch(page, { q: acknowledged.title });
    checks.assertAcknowledgedRecords(rows, [acknowledged]);
  }
}

exports.run = async ({ page, appUrl, fixtureBase, phase, runId, initialMetadata }) => {
  const token = `independent-${String(runId || 'missing-run-id').replace(/[^a-zA-Z0-9-]/g, '')}`;
  if (!runId) throw new Error('runner must preserve RUN_ID across the container restart');
  if (phase === 'initial') {
    const journey = await runJourney({ page, appUrl, fixtureBase, token });
    return { assertions: journey.assertions, metadata: journey };
  }
  if (phase !== 'after-restart') throw new Error(`unexpected phase ${phase}`);
  if (process.env.RESTART_LIFECYCLE_CONFIRMED !== '1') throw new Error('runner has not confirmed a real Docker container restart');
  await verifyPersisted(page, initialMetadata);
  const replay = await runJourney({ page, appUrl, fixtureBase, token: `${token}-post` });
  replay.assertions.push(result(CASE.restart, true,
    'same container ID was running before and after a changed StartedAt; original ID/title/URL/category and all concurrent acknowledged records persisted exactly'));
  return { assertions: replay.assertions, metadata: { ...replay, verified_original_record_id: initialMetadata.primary.id } };
};
