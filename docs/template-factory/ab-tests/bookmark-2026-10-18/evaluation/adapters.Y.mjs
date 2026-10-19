// UI-only SSR adapter; the same behavioral assertions are in runtime_test.mjs.
export function createAdapter(page, baseUrl) {
  async function navigate(action) {
    await Promise.all([page.waitForNavigation({ waitUntil: 'domcontentloaded' }), action()]);
  }
  async function homeIfNeeded() {
    if (!(await page.locator('[data-testid=bookmark-form]').count())) await navigate(() => page.locator('a.brand').click());
  }
  async function fill(record) {
    await homeIfNeeded();
    const form = page.locator('[data-testid=bookmark-form]');
    await form.locator('[name=url]').fill(record.url);
    await form.locator('[name=title]').fill(record.title ?? '');
    await form.locator('[name=note]').fill(record.note ?? '');
    if (record.category) await form.locator('select[name=categoryId]').selectOption({ label: record.category });
    else {
      const value = await form.locator('select[name=categoryId] option').first().getAttribute('value');
      await form.locator('select[name=categoryId]').selectOption(value);
    }
  }
  function row(record) {
    return page.locator('[data-testid=bookmark-item]').filter({ has: page.locator('[data-testid=bookmark-url]').filter({ hasText: new RegExp('^' + record.url.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }) }).first();
  }
  return {
    async ready() {
      await page.goto(baseUrl + '/');
      await page.locator('[data-testid=bookmark-form]').waitFor();
    },
    async save(record) {
      await fill(record);
      await navigate(() => page.locator('[data-testid=bookmark-submit]').click());
    },
    async createCategory(name) {
      const exists = await page.locator('[data-testid=category-link]').filter({ hasText: new RegExp('^' + name + '$') }).count();
      if (exists) return { category: name, observation: 'Already exists in product UI.' };
      const form = page.locator('[data-testid=category-form]');
      await form.locator('[name=name]').fill(name);
      await navigate(() => form.locator('button[type=submit]').click());
      return { category: name, observation: 'Created through UI.' };
    },
    async viewCategory(name) {
      if (name === 'all') await navigate(() => page.locator('a.brand').click());
      else {
        const text = name == null ? '未分类' : name;
        await navigate(() => page.locator('[data-testid=category-link]').filter({ hasText: new RegExp('^' + text + '$') }).click());
      }
    },
    async move(record, destination) {
      const form = row(record).locator('[data-testid=move-form]');
      await form.locator('select[name=categoryId]').selectOption({ label: destination });
      await navigate(() => form.locator('[data-testid=move-submit]').click());
    },
    async search(query) {
      await homeIfNeeded();
      const form = page.locator('[data-testid=search-form]');
      await form.locator('[name=q]').fill(query);
      await navigate(() => form.locator('[data-testid=search-submit]').click());
    },
    async records() {
      return page.locator('[data-testid=bookmark-item]').evaluateAll(nodes => nodes.map(n => ({
        url: n.querySelector('[data-testid=bookmark-url]').textContent,
        title: n.querySelector('[data-testid=bookmark-title]').textContent,
        note: n.querySelector('[data-testid=bookmark-edit-form] textarea[name=note]').value,
        text: n.innerText,
      })));
    },
    async openOriginal(record) {
      const link = row(record).locator('[data-testid=open-link]');
      const href = new URL(await link.getAttribute('href'), baseUrl).href;
      await Promise.all([page.waitForNavigation({ waitUntil: 'domcontentloaded' }).catch(error => ({ blockedNavigation: String(error) })), link.click().catch(error => ({ blockedNavigation: String(error) }))]);
      return href;
    },
    async submitEmptyUrl() {
      await homeIfNeeded();
      const form = page.locator('[data-testid=bookmark-form]');
      await form.locator('[name=url]').fill('');
      await form.locator('[name=title]').fill('');
      await form.locator('[name=note]').fill('');
      await navigate(() => form.locator('[data-testid=bookmark-submit]').click());
      return { errorText: await page.locator('[data-testid=form-error]').innerText() };
    },
    async doubleSave(record) {
      await fill(record);
      await navigate(() => page.locator('[data-testid=bookmark-submit]').dblclick());
      return { observation: 'Invoked one physical double-click on same save button; SSR navigation may replace the form. Request outcomes retained separately.' };
    },
  };
}
