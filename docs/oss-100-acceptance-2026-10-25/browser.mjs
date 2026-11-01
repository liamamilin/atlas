// Read-only acceptance against the existing production UI and API.
import { chromium, expect } from '../../atlas-web/node_modules/@playwright/test/index.mjs';
import { writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
const out = fileURLToPath(new URL('.', import.meta.url));
const browser = await chromium.launch({ headless: true });
const checks = [], writes = [], errors = [];
const origin = 'http://127.0.0.1:5188';
try {
  for (const viewport of [{ width: 1280, height: 900 }, { width: 390, height: 844 }]) {
    const context = await browser.newContext({ viewport });
    await context.route('**/api/**', route => {
      if (!['GET', 'HEAD'].includes(route.request().method())) {
        writes.push(route.request().method() + ' ' + new URL(route.request().url()).pathname);
        return route.abort();
      }
      return route.continue();
    });
    const page = await context.newPage();
    page.on('pageerror', error => errors.push(error.message));
    const api = async query => {
      const response = await context.request.get(origin + '/api/oss/catalog?' + query);
      expect(response.ok()).toBe(true);
      return response.json();
    };
    for (const [leaf, repo, label] of [
      ['web-browser', 'qutebrowser/qutebrowser', '许可证待核验'],
      ['electronic-health-record-ehr', 'atishay2411/MedPilot', '条件适用'],
      ['golf-course-management', 'aaronhorvat1/tee-time-booking-system', '待核实'],
      ['vector-retrieval-platform', '330205812/NexusRAG', '已核验开源许可证'],
      ['golf-course-management', '4jwilliams25/golf-course-management-app', '项目介绍待补充'],
    ]) {
      const query = new URLSearchParams({ leaf, q: repo }).toString();
      const data = await api(query);
      expect(data.projects).toHaveLength(1);
      await page.goto(origin + '/discover?' + query);
      const project = data.projects[0];
      const card = page.getByRole('article', { name: project.name, exact: true });
      await expect(card).toBeVisible();
      await expect(card.getByRole('link', { name: '查看 GitHub 项目', exact: true })).toHaveAttribute('href', project.github_url);
      await card.getByText('查看功能、适用范围与来源', { exact: true }).click();
      await expect(card).toContainText(label);
      if (repo === '330205812/NexusRAG') {
        await expect(card).toContainText('Pending merge');
        await expect(card.getByRole('link', { name: '许可证原文', exact: true })).toHaveAttribute('href', /github.com\/330205812\/NexusRAG/);
        await card.getByText('展开介绍与关联的原文依据', { exact: true }).click();
        await expect(card.locator('blockquote').first()).toBeVisible();
        await expect(card.locator('a[href*="/git/blobs/"]').first()).toBeVisible();
        await page.screenshot({ path: out + `acceptance-${viewport.width}.png`, fullPage: true });
      }
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
      checks.push({ viewport: viewport.width, leaf, repo, result: 'passed' });
    }
    await page.goto(origin + '/discover?leaf=web-browser');
    await page.getByRole('textbox', { name: '搜索项目、功能或场景', exact: true }).fill('qutebrowser/qutebrowser');
    await page.getByRole('button', { name: '搜索项目', exact: true }).click();
    await expect(page.getByRole('article')).toHaveCount(1);
    await expect(page).toHaveURL(/q=qutebrowser/);
    const leafData = await api('leaf=web-browser&limit=24');
    await page.goto(origin + '/discover?leaf=web-browser');
    await expect(page.getByRole('article')).toHaveCount(Math.min(24, leafData.pagination.total));
    await page.getByRole('button', { name: '下一页', exact: true }).click();
    await expect(page).toHaveURL(/page=2/);
    const second = await api('leaf=web-browser&limit=24&offset=24');
    await expect(page.getByRole('article').first()).toHaveAccessibleName(second.projects[0].name);
    expect(second.projects.every(p => !leafData.projects.some(q => q.repository_id === p.repository_id))).toBe(true);
    await page.goto(origin + '/discover?leaf=web-browser');
    const scenario = leafData.scenarios[0];
    await page.getByRole('button', { name: `${scenario.name} · ${scenario.project_count}`, exact: true }).click();
    await expect(page).toHaveURL(new RegExp(scenario.id));
    await expect(page.getByRole('button', { name: `${scenario.name} · ${scenario.project_count}`, exact: true })).toHaveAttribute('aria-pressed', 'true');
    await page.getByRole('combobox', { name: '许可证', exact: true }).selectOption('pending');
    const filtered = await api(new URLSearchParams({ leaf: 'web-browser', scenario: scenario.id, license: 'pending', limit: '24' }).toString());
    await expect(page.getByRole('article')).toHaveCount(Math.min(24, filtered.pagination.total));
    const favorites = await api('favorites=1&limit=24');
    await page.goto(origin + '/discover?favorites=1');
    await expect(page.getByRole('heading', { name: '我的收藏', exact: true })).toBeVisible();
    await expect(page.getByRole('article')).toHaveCount(Math.min(24, favorites.pagination.total));
    await expect(page.getByRole('checkbox', { name: '只看收藏', exact: true })).toBeChecked();
    await page.goto(origin + '/types/vector-retrieval-platform');
    await expect(page.getByRole('article')).toHaveCount(24);
    const batch = page.getByRole('region', { name: '批量采集', exact: true });
    await batch.getByText('批量采集 · 选择类型并自动续批', { exact: true }).click();
    await expect(batch.getByRole('status')).toContainText('21421/21421');
    await expect(batch.getByRole('status')).toContainText('部分项目失败');
    checks.push({ viewport: viewport.width, search: 'passed', pagination: 'passed', scenario_and_license_filter: 'passed', favorites_read_only: 'passed', completed_partial_progress: 'passed' });
    await context.close();
  }
  expect(writes).toEqual([]);
  expect(errors).toEqual([]);
  const result = { result: 'passed', checked_at: new Date().toISOString(), checks, writes, runtime_errors: errors };
  await writeFile(out + 'LIVE_BROWSER.json', JSON.stringify(result, null, 2) + '\n');
  console.log(JSON.stringify({ result: 'passed', checks: checks.length, writes: writes.length, runtime_errors: errors.length }));
} catch (error) {
  await writeFile(out + 'LIVE_BROWSER.json', JSON.stringify({ result: 'failed', checks, writes, runtime_errors: errors, error: String(error) }, null, 2));
  throw error;
} finally {
  await browser.close();
}
