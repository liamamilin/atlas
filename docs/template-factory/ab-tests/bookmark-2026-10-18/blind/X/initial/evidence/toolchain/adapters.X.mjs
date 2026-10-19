// UI-only adapter. Selectors come from the anonymous app; no app/API mutation.
export function createAdapter(page, baseUrl) {
  const root = baseUrl + '/';
  async function refreshed(action) {
    const response = page.waitForResponse(r => new URL(r.url()).pathname === '/api/bookmarks' && r.request().method() === 'GET');
    await action();
    await (await response).finished();
    await page.waitForTimeout(70);
  }
  async function categoryValue(selector, name) {
    return page.locator(selector + ' option').evaluateAll((nodes, target) => {
      const found = nodes.find(n => target == null ? n.textContent.endsWith('（默认）') : n.textContent === target);
      if (!found) throw new Error('Category option not found: ' + target);
      return found.value;
    }, name ?? null);
  }
  function row(record) { return page.locator('#bookmark-list > li.bookmark').filter({ has: page.locator('.url').filter({ hasText: new RegExp('^' + record.url.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }) }).first(); }
  async function fill(record) {
    await page.locator('#url-input').fill(record.url);
    await page.locator('#title-input').fill(record.title ?? '');
    await page.locator('#note-input').fill(record.note ?? '');
    await page.locator('#category-select').selectOption(await categoryValue('#category-select', record.category));
  }
  return {
    async ready() {
      await page.goto(root);
      await page.locator('#category-select option').first().waitFor({ state: 'attached' });
      await page.locator('#list-hint').filter({ hasText: /共/ }).waitFor();
    },
    async save(record) {
      await fill(record);
      await refreshed(() => page.locator('#add-form button[type=submit]').click());
    },
    async createCategory(name) {
      const existing = await page.locator('#category-list .cat-name').filter({ hasText: new RegExp('^' + name + '$') }).count();
      if (existing) return { category: name, observation: 'Already present in initial UI; no new-category claim for this value.' };
      await page.locator('#category-name').fill(name);
      await refreshed(() => page.locator('#category-form button[type=submit]').click());
      return { category: name, observation: 'Created through UI.' };
    },
    async viewCategory(name) {
      const text = name === 'all' ? '全部记录' : name == null ? '未整理' : name;
      await refreshed(() => page.locator('#category-list .cat-name').filter({ hasText: new RegExp('^' + text + '$') }).click());
    },
    async move(record, destination) {
      await row(record).getByRole('button', { name: '编辑 / 移动', exact: true }).click();
      await page.locator('#edit-dialog').waitFor({ state: 'visible' });
      await page.locator('#edit-category').selectOption(await categoryValue('#edit-category', destination));
      await refreshed(() => page.locator('#edit-form button[type=submit]').click());
      await page.locator('#edit-dialog').waitFor({ state: 'hidden' });
    },
    async search(query) {
      if (!query) await refreshed(() => page.locator('#search-clear').click());
      else await refreshed(() => page.locator('#search-input').fill(query));
    },
    async records() {
      return page.locator('#bookmark-list > li.bookmark').evaluateAll(nodes => nodes.map(n => ({
        url: n.querySelector('.url').textContent,
        title: n.querySelector('a.title').textContent,
        note: n.querySelector('.note')?.textContent ?? '',
        text: n.innerText,
      })));
    },
    async openOriginal(record) {
      const link = row(record).locator('a.title');
      const href = new URL(await link.getAttribute('href'), baseUrl).href;
      const popupPromise = page.context().waitForEvent('page');
      await link.click();
      const popup = await popupPromise;
      await popup.waitForLoadState('domcontentloaded');
      return href;
    },
    async submitEmptyUrl() {
      await page.locator('#url-input').fill('');
      await page.locator('#title-input').fill('');
      await page.locator('#note-input').fill('');
      await page.locator('#add-form button[type=submit]').click();
      return page.locator('#url-input').evaluate(n => ({ value: n.value, validity: n.validity.valid, validationMessage: n.validationMessage }));
    },
    async doubleSave(record) {
      await fill(record);
      await page.locator('#add-form button[type=submit]').dblclick();
      await page.waitForTimeout(500);
      return { observation: 'Invoked one physical double-click on same save button. Request outcomes are in browser events.' };
    },
  };
}
