import { expect, test } from "@playwright/test";
const leaf = "/types/personal-knowledge-management-application";

test("home leads to the real repository pilot and factory remains in history", async ({ page }) => {
  const errors: string[] = [];
  page.on("pageerror", error => errors.push(error.message));
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "想做一件事，先看看已有的可能性" })).toBeVisible();
  await expect(page.getByRole("navigation", { name: "主导航" }).getByRole("link", { name: "模板工厂" })).toHaveCount(0);
  await page.getByRole("link", { name: "探索场景与项目", exact: true }).click();
  await expect(page).toHaveURL(leaf);
  await expect(page.locator('article[aria-label]')).toHaveCount(7);
  await page.screenshot({ path: "../docs/oss-catalog-2026-10-23/pilot-desktop.png" });
  await expect(page.getByRole("heading", { name: "基于这个类型开发项目" })).toHaveCount(0);
  await page.getByRole("link", { name: "历史工作区与模板工厂" }).click();
  await expect(page.getByRole("link", { name: /^模板工厂/ })).toHaveAttribute("href", "/factory");
  expect(errors).toEqual([]);
});

test("scenario filters, evidence, license and upstream links are usable", async ({ page }) => {
  await page.goto(leaf);
  await page.getByRole("button", { name: "在文本文件与编辑器中积累知识 · 3", exact: true }).click();
  await expect(page.locator('article[aria-label]')).toHaveCount(3);
  await page.reload();
  await expect(page.locator('article[aria-label]')).toHaveCount(3);
  const foam = page.getByRole("article", { name: "Foam", exact: true });
  await expect(foam.getByRole("link", { name: "GitHub", exact: true })).toHaveAttribute("href", "https://github.com/foambubble/foam");
  await expect(foam.getByTitle("已核验开源许可证")).toBeVisible();
  await foam.getByRole("link", { name: "查看详情", exact: true }).click();
  await expect(page.getByRole("heading", { level: 1, name: "Foam" })).toBeVisible();
  await expect(page.getByRole("link", { name: "许可证原文", exact: true })).toHaveAttribute("href", /^https:\/\/github.com\/foambubble\/foam\//);
  await expect(page.getByRole("link", { name: "在 GitHub 查看", exact: true })).toHaveAttribute("href", "https://github.com/foambubble/foam");
  await page.getByText("展开介绍与关联的原文依据", { exact: true }).click();
  await expect(page.locator("blockquote").first()).toBeVisible();
  await expect(page.locator('blockquote a').first()).toHaveAttribute("href", /^https:\/\/api.github.com\/repos\/foambubble\/foam\/git\/blobs\//);
  await page.goBack();
  await expect(page.locator('article[aria-label]')).toHaveCount(3);
});

test("search includes repository facts and favorites survive reload", async ({ page }) => {
  await page.goto("/discover?q=Foam");
  await expect(page.locator('article[aria-label]')).toHaveCount(1);
  await page.getByRole("button", { name: "收藏 Foam", exact: true }).click();
  await expect(page.getByRole("button", { name: "取消收藏 Foam", exact: true })).toBeVisible();
  await page.reload();
  await expect(page.getByRole("button", { name: "取消收藏 Foam", exact: true })).toBeVisible();
  await page.getByRole("checkbox", { name: "只看收藏" }).check();
  await expect(page.getByRole("article", { name: "Foam", exact: true })).toBeVisible();
  await page.getByRole("button", { name: "取消收藏 Foam", exact: true }).click();
  await expect(page.getByText("没有符合当前筛选的项目。可以调整关键词、场景或许可状态。", { exact: true })).toBeVisible();
  await page.goto("/search?q=Foam");
  await expect(page.getByRole("article", { name: "Foam", exact: true })).toBeVisible();
  await page.goto("/discover?leaf=personal-knowledge-management-application&license=pending");
  await expect(page.locator('article[aria-label]')).toHaveCount(0);
  await page.getByRole("combobox", { name: "许可证", exact: true }).selectOption("open_source");
  await expect(page.locator('article[aria-label]')).toHaveCount(7);
});

test("API rejects cross-site writes and unsupported leaves", async ({ request }) => {
  const crossSite = await request.post("/api/oss/refresh", { headers: { Origin: "https://example.com" }, data: {} });
  expect(crossSite.status()).toBe(403);
  const invalid = await request.post("/api/oss/refresh", { data: { leaf: "unknown" } });
  expect(invalid.status()).toBe(404);
  const before = await (await request.get("/api/oss/catalog?leaf=personal-knowledge-management-application")).json();
  expect(before.projects).toHaveLength(7);
  const invalidFavorite = await request.post(`/api/oss/projects/${before.projects[0].repository_id}/favorite`, { data: { favorite: "true" } });
  expect(invalidFavorite.status()).toBe(400);
});

test("mobile layout has no horizontal overflow and an untouched leaf stays browsable", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(leaf);
  await expect(page.getByRole("article", { name: "Foam", exact: true })).toBeAttached();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  await page.screenshot({ path: "../docs/oss-catalog-2026-10-23/pilot-mobile.png" });
  await page.goto("/types/business-messaging-application");
  await expect(page.getByText("这个类型还没有已整理的项目。", { exact: true })).toBeVisible();
  await expect(page.getByRole("heading", { name: "正式资料阅读器", exact: true })).toBeVisible();
});
