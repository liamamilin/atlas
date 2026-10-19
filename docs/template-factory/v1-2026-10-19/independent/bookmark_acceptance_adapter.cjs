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

// Semantic selectors frozen in the generated acceptance-suite UI contract.
// These are intentionally stable test hooks rather than presentation selectors.
const UI = Object.freeze({
  categoryManager: 'a[data-testid="category-manager"]',
  categoryCreate: 'form[data-testid="category-create-form"]',
  categoryRename: 'form[data-testid="category-rename-form"]',
  categoryDelete: 'form[data-testid="category-delete-form"]',
  categorySearch: 'form[data-testid="category-search-form"]',
  recordMove: 'form[data-testid="record-move-form"]',
  recordDelete: 'form[data-testid="record-delete-form"]',
  recordRestore: 'form[data-testid="record-restore-form"]',
  formError: '[data-testid="form-error"]',
  categoryCount: '[data-testid="category-count"]',
});

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
  for (const key of ['bookmarks', 'categories', 'items', 'data', 'records']) {
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

async function submitForm(form, submit = true) {
  if (submit) {
    await Promise.all([
      form.page().waitForLoadState('domcontentloaded').catch(() => {}),
      form.locator('button[type="submit"], input[type="submit"]').first().click(),
    ]);
  }
}

async function createCategoryViaUi(page, appUrl, name) {
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  await page.locator(UI.categoryManager).click();
  const form = page.locator(UI.categoryCreate);
  await form.locator('[name="name"]').fill(name);
  await submitForm(form);
  const created = await api(page, '/api/categories');
  if (created.status !== 200) throw new Error(`category readback returned ${created.status}`);
  const row = recordsFrom(created.data).find(item => item && item.name === name);
  if (!row || !row.id) throw new Error(`UI category creation did not persist ${name}`);
  return row;
}

function categoryTargetForm(page, selector, id) {
  const escaped = String(id).replaceAll('"', '\\"');
  return page.locator(`${selector}:has(input[name="category_id"][value="${escaped}"])`);
}

async function clickForm(form) {
  if (await form.count() !== 1) throw new Error(`expected one visible UI form, found ${await form.count()}`);
  await submitForm(form);
}

async function moveViaUi(page, appUrl, recordId, category) {
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const form = page.locator(`${UI.recordMove}:has(input[name="record_id"][value="${String(recordId)}"])`);
  if (await form.count() !== 1) throw new Error('record move control is missing or ambiguous');
  const categoryRow = recordsFrom((await api(page, '/api/categories')).data).find(row => row.name === category);
  if (!categoryRow) throw new Error(`move target category ${category} is absent`);
  await form.locator('select[name="category_id"]').selectOption(String(categoryRow.id));
  await clickForm(form);
}

async function searchViaUi(page, appUrl, category, q) {
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const categoryLink = page.locator('a').filter({ hasText: category }).first();
  const categoryHref = await categoryLink.getAttribute('href');
  if (!categoryHref || new URL(categoryHref, appUrl).searchParams.get('category') !== category) {
    throw new Error('selected category does not have a reachable category-page link');
  }
  await categoryLink.click();
  if (new URL(page.url()).searchParams.get('category') !== category) {
    throw new Error('clicking the category link did not open the selected category page');
  }
  const form = page.locator(UI.categorySearch);
  if (await form.count() !== 1) throw new Error('category search form is missing or ambiguous');
  const categoryField = form.locator('[name="category"]');
  const queryField = form.locator('[name="q"]');
  if (await categoryField.count() !== 1 || await queryField.count() !== 1) {
    throw new Error('category search form must expose category and q fields');
  }
  if (await categoryField.inputValue() !== category) throw new Error('category search form did not preserve selected category');
  await queryField.fill(q);
  await submitForm(form);
  const submitted = new URL(page.url());
  if (submitted.searchParams.get('category') !== category || submitted.searchParams.get('q') !== q) {
    throw new Error('submitted category search did not preserve category and q');
  }
}

async function requireMoveControl(page) {
  const controls = page.locator(UI.recordMove);
  if (await controls.count() < 1 || !(await controls.first().isVisible())) {
    throw new Error('record move control is missing from the rendered UI');
  }
}

async function validateUiContract(page, appUrl, category = 'Fixture Category') {
  await page.goto(checks.rootUrl(appUrl, { category }), { waitUntil: 'domcontentloaded' });
  await requireMoveControl(page);
  const form = page.locator(UI.categorySearch);
  if (await form.count() !== 1) throw new Error('category search form is missing or ambiguous');
  if (await form.locator('[name="category"]').inputValue() !== category) {
    throw new Error('category search form did not preserve selected category');
  }
  await form.locator('[name="q"]').fill('fixture-term');
  await submitForm(form);
  const url = new URL(page.url());
  if (url.searchParams.get('category') !== category || url.searchParams.get('q') !== 'fixture-term') {
    throw new Error('submitted category search did not preserve category and q');
  }
  return { move_control: true, category_search_preserved: true };
}

async function trashAndRestoreViaUi(page, appUrl, recordId) {
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const remove = page.locator(`${UI.recordDelete}:has(input[name="record_id"][value="${String(recordId)}"])`);
  if (await remove.count() !== 1) throw new Error('record delete control is missing or ambiguous');
  await clickForm(remove);
  const deleted = await api(page, `/api/bookmarks/${encodeURIComponent(String(recordId))}`);
  const deletedRecord = recordFrom(deleted.data);
  if (deleted.status !== 200 || !deletedRecord || !deletedRecord.trashed_at) {
    throw new Error('UI delete did not soft-delete the selected record');
  }
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const categoryResponse = await api(page, '/api/categories');
  const categoryName = deletedRecord.category ?? deletedRecord.category_name;
  const categoryLabel = typeof categoryName === 'string' ? categoryName : categoryName && categoryName.name;
  const categoryRecord = recordsFrom(categoryResponse.data).find(item => item.name === categoryLabel);
  if (!categoryRecord) throw new Error('soft-deleted record category could not be resolved for count check');
  await verifyVisibleCategoryCount(page, categoryRecord.id, 1);
  const restore = page.locator(`${UI.recordRestore}:has(input[name="record_id"][value="${String(recordId)}"])`);
  if (await restore.count() !== 1) throw new Error('undo/restore control is missing after soft delete');
  await clickForm(restore);
  const restored = await getById(page, recordId);
  if (restored.trashed_at) throw new Error('UI restore did not return the record to the active list');
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  await verifyVisibleCategoryCount(page, categoryRecord.id, 2);
}

async function verifyVisibleCategoryCount(page, categoryId, expected) {
  const count = page.locator(`${UI.categoryCount}[data-category-id="${String(categoryId)}"]`);
  const categories = recordsFrom((await api(page, '/api/categories')).data);
  const category = categories.find(item => String(item.id) === String(categoryId));
  if (!category) throw new Error(`category ${categoryId} is absent during visible count check`);
  const activeRows = await exactSearch(page, { category: category.name });
  if (activeRows.length !== expected || await count.count() !== 1 || Number((await count.innerText()).trim()) !== activeRows.length) {
    throw new Error(`visible active category count mismatch for ${categoryId}; expected ${expected}`);
  }
}

async function exerciseCategoryManagement(page, appUrl, token, category) {
  const activeChild = await createApiRecord(page, {
    url: `http://127.0.0.1/category-child/${token}`, title: `category-child-${token}`, category: category.name,
  });
  const trashedChild = await createApiRecord(page, {
    url: `http://127.0.0.1/category-trashed/${token}`, title: `category-trashed-${token}`, category: category.name,
  });
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const trashForm = page.locator(`${UI.recordDelete}:has(input[name="record_id"][value="${String(trashedChild.id)}"])`);
  if (await trashForm.count() !== 1) throw new Error('temporary category soft-delete control is missing');
  await clickForm(trashForm);
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  await page.locator(UI.categoryManager).click();
  const duplicate = page.locator(UI.categoryCreate);
  await duplicate.locator('[name="name"]').fill(category.name);
  await clickForm(duplicate);
  if (!(await page.locator(UI.formError).isVisible())) throw new Error('duplicate category submission has no visible HTML error');
  if (await duplicate.locator('[name="name"]').inputValue() !== category.name) {
    throw new Error('duplicate category error did not preserve submitted input for recovery');
  }
  if (await api(page, '/api/categories').then(r => recordsFrom(r.data).filter(x => x.name === category.name).length) !== 1) {
    throw new Error('duplicate category failure changed category state');
  }
  const rename = categoryTargetForm(page, UI.categoryRename, category.id);
  if (await rename.count() !== 1) throw new Error('category rename form is missing or ambiguous');
  const renamed = `${category.name} renamed`;
  await rename.locator('[name="name"]').fill(renamed);
  await clickForm(rename);
  const renameCheck = await api(page, '/api/categories');
  if (!recordsFrom(renameCheck.data).some(item => item.id === category.id && item.name === renamed)) {
    throw new Error('UI category rename did not persist');
  }
  const deleteForm = categoryTargetForm(page, UI.categoryDelete, category.id);
  if (await deleteForm.count() !== 1) throw new Error('category delete form is missing or ambiguous');
  await clickForm(deleteForm);
  const deleteCheck = await api(page, '/api/categories');
  if (recordsFrom(deleteCheck.data).some(item => item.id === category.id)) throw new Error('UI category delete did not persist');
  const movedActive = await getById(page, activeChild.id);
  const movedTrashed = await getById(page, trashedChild.id);
  for (const item of [movedActive, movedTrashed]) {
    const assigned = item.category ?? item.category_name;
    const name = typeof assigned === 'string' ? assigned : assigned && assigned.name;
    if (name !== '未整理') throw new Error('deleting a category did not move active and soft-deleted records to the default category');
  }
  const restore = page.locator(`${UI.recordRestore}:has(input[name="record_id"][value="${String(trashedChild.id)}"])`);
  if (await restore.count() !== 1) throw new Error('migrated soft-deleted record cannot be restored through the UI');
  await clickForm(restore);
  const restoredTrashed = await getById(page, trashedChild.id);
  const restoredCategory = restoredTrashed.category ?? restoredTrashed.category_name;
  const restoredName = typeof restoredCategory === 'string' ? restoredCategory : restoredCategory && restoredCategory.name;
  if (restoredTrashed.trashed_at || restoredName !== '未整理') {
    throw new Error('restored record became orphaned or did not return to the default category');
  }
}

async function verifyOpen(page, appUrl, record, originalUrl) {
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const row = page.locator(`tr[data-testid="record-row"][data-record-id="${String(record.id)}"]`);
  if (await row.count() !== 1) throw new Error('saved record row is missing or ambiguous');
  const link = row.locator('a[data-testid="record-open-link"]');
  const rel = (await link.getAttribute('rel') || '').split(/\s+/);
  if (await link.count() !== 1 || await link.getAttribute('href') !== originalUrl
      || await link.getAttribute('target') !== '_blank' || !rel.includes('noopener')) {
    throw new Error('record open link does not preserve the exact original URL and safe new-tab contract');
  }
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
  assertions.push(result('A01', true, 'bookmark was submitted through the HTML save form and exact content was read back'));

  const category = `Acceptance ${token} category`;
  const controlCategory = `Control ${token} category`;
  const categoryRecord = await createCategoryViaUi(page, appUrl, category);
  const controlCategoryRecord = await createCategoryViaUi(page, appUrl, controlCategory);
  const categoryControl = await createApiRecord(page, {
    url: `${fixtureBase}/second?control=category`, title: `Cross-category ${token} control`, category: controlCategory,
  });
  const keywordControl = await createApiRecord(page, {
    url: `${fixtureBase}/second?control=keyword`, title: 'Unrelated keyword control', category,
  });

  await moveViaUi(page, appUrl, record.id, category);
  const movedRecord = await getById(page, record.id);
  const newCategoryRows = await exactSearch(page, { category });
  const oldCategoryRows = await exactSearch(page, { category: '待购' });
  checks.assertMoveState({ record: movedRecord, recordId: record.id, newCategory: category, oldCategoryRows, newCategoryRows });
  assertions.push(result(CASE.move, true, 'record category field changed; new filter includes target and old filter excludes it'));
  assertions.push(result('A05', true, 'record was moved using its rendered move form and persisted under the selected category'));
  await verifyVisibleCategoryCount(page, categoryRecord.id, 2);
  assertions.push(result('A06', true, 'selected category page and visible sidebar count match the active API result'));

  const byCategory = await exactSearch(page, { category });
  const byCategoryAndKeyword = await exactSearch(page, { category, q: token });
  const byKeyword = await exactSearch(page, { q: token });
  const keywordMiss = await exactSearch(page, { category, q: `definitely-no-match-${token}` });
  checks.assertFindState({ recordId: record.id, categoryControlId: categoryControl.id, keywordControlId: keywordControl.id,
    byCategory, byCombined: byCategoryAndKeyword, byKeyword, keywordMiss });
  await searchViaUi(page, appUrl, category, token);
  const rendered = await page.locator('body').innerText();
  if (!rendered.includes(title) || rendered.includes(categoryControl.title) || rendered.includes(keywordControl.title)) {
    throw new Error('filtered Chromium UI did not isolate the target bookmark from the control record');
  }
  assertions.push(result(CASE.find, true, 'category, keyword, combined, negative match, and Chromium UI filters distinguish target from control'));
  assertions.push(result('A07', true, 'the real category search form submitted both category and keyword and distinguished controls'));

  const managedCategory = await createCategoryViaUi(page, appUrl, `Temporary ${token}`);
  await exerciseCategoryManagement(page, appUrl, token, managedCategory);
  assertions.push(result('manage category through browser forms', true,
    'category create, duplicate-name feedback with preserved input, rename, and delete were submitted through HTML forms'));
  assertions.push(result('A04', true, 'category create, duplicate feedback, rename and delete forms succeeded; active and trashed records migrated to the default category'));

  const opened = await verifyOpen(page, appUrl, record, originalUrl);
  if (!opened) throw new Error('open action did not reach the exact controlled fixture URL');
  assertions.push(result(CASE.open, true, `opened exact fixture URL ${originalUrl}`));
  assertions.push(result('A08', true, `the record open anchor href and actual Chromium navigation both matched ${originalUrl}`));

  const before = (await exactSearch(page, { q: `${token}-invalid` })).length;
  await page.goto(checks.rootUrl(appUrl), { waitUntil: 'domcontentloaded' });
  const invalidForm = page.locator('form[action="/bookmarks/new"]');
  const invalidFormUrl = 'ftp://example.test/unsupported-scheme';
  await invalidForm.locator('[name="url"]').fill(invalidFormUrl);
  await invalidForm.locator('[name="title"]').fill(`${token}-invalid`);
  await submitForm(invalidForm);
  if (!(await page.locator(UI.formError).isVisible()) || await invalidForm.locator('[name="url"]').inputValue() !== invalidFormUrl) {
    throw new Error('invalid URL form failure lacks visible feedback or retained recovery input');
  }
  await invalidForm.locator('[name="url"]').fill(`${fixtureBase}/recovered`);
  await submitForm(invalidForm);
  const recovered = (await exactSearch(page, { q: `${token}-invalid` })).find(item => item.title === `${token}-invalid`);
  if (!recovered || recovered.url !== `${fixtureBase}/recovered`) throw new Error('correcting the invalid form did not create the recovery record');
  for (const url of ['javascript:alert(1)', 'ftp://example.test/file']) {
    const rejected = await api(page, '/api/bookmarks', 'POST', { url, title: `${token}-invalid-api` });
    if (rejected.status !== 400) throw new Error(`invalid URL was not rejected with 400: ${url}`);
  }
  const after = (await exactSearch(page, { q: `${token}-invalid` })).length;
  if (after !== before + 1) throw new Error('invalid URL attempt wrote data or successful recovery did not persist exactly once');
  assertions.push(result(CASE.invalid, true, 'malformed URL showed HTML feedback and retained input; correction recovered; malformed/non-http(s) JSON inputs remained rejected'));
  assertions.push(result('A02', true, 'invalid URL was visibly rejected without a write, retained for correction, and recovered through the same form'));

  await trashAndRestoreViaUi(page, appUrl, record.id);
  assertions.push(result('soft-delete and undo through browser forms', true,
    'the UI soft-deleted the selected record and exposed an executable restore form that returned it to the active list'));
  assertions.push(result('A09', true, 'soft-delete and restore used rendered forms and active category counts were correct after each action'));

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

exports.validateUiContract = validateUiContract;
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
