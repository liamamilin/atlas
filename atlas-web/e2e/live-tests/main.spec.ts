import { expect, test, type Page, type TestInfo } from "@playwright/test";

const evidence = "../docs/product-polish-2026-10-23/live-validation";
let writes: string[];
let errors: string[];

test.beforeEach(async ({ page }) => {
  writes = []; errors = [];
  page.on("pageerror", e => errors.push(e.message));
  await page.route("**/api/**", route => {
    if (!["GET", "HEAD"].includes(route.request().method())) {
      writes.push(`${route.request().method()} ${new URL(route.request().url()).pathname}`);
      return route.abort("blockedbyclient");
    }
    return route.continue();
  });
});

test.afterEach(async ({ page }) => {
  expect(writes, "Live validation must not submit writes").toEqual([]);
  expect(errors, "Browser runtime errors").toEqual([]);
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), "Horizontal overflow").toBe(true);
});

async function screenshot(page: Page, testInfo: TestInfo, name: string) {
  await page.screenshot({ path: `${evidence}/${name}-${testInfo.project.name}.png` });
}

test("home uses the real lightweight coverage overview", async ({ page, request }, info) => {
  const overview = await (await request.get("/api/oss/catalog?view=overview")).json();
  expect(overview.projects).toEqual([]);
  expect(overview.stats.projects).toBeGreaterThan(0);
  const response = page.waitForResponse(r => r.url().includes("/api/oss/catalog?") && new URL(r.url()).searchParams.get("view") === "overview");
  await page.goto("/");
  const displayedOverview = await (await response).json();
  expect(displayedOverview.projects).toEqual([]);
  await expect(page.getByRole("heading", { name: "想做一件事，先看看已有的可能性", exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: `${displayedOverview.stats.projects.toLocaleString("zh-CN")} 已整理的真实项目`, exact: true })).toBeVisible();
  await expect(page.getByRole("heading", { name: "继续探索", exact: true })).toBeVisible();
  await expect(page).toHaveTitle("首页 · 应用图谱");
  await screenshot(page, info, "home");
});

test("taxonomy filters and opens a real type with a readable canonical source", async ({ page }, info) => {
  await page.goto("/browse");
  await page.getByRole("textbox", { name: "筛选领域与子域", exact: true }).fill("通讯");
  await expect(page.locator('section[id="01"]')).toBeVisible();
  await expect(page.locator('section[id="02"]')).toHaveCount(0);
  await page.getByRole("button").filter({ has: page.getByRole("heading", { name: "消息与聊天", exact: true }) }).click();
  await page.locator('a[href="/types/business-messaging-application"]').click();
  await expect(page.locator("main h1")).toHaveText("商业消息应用");
  await expect(page.getByRole("heading", { name: "正式资料阅读器", exact: true })).toBeVisible();
  await screenshot(page, info, "type-source");
});

test("real repository pagination stays bounded and survives reload", async ({ page, request }, info) => {
  // A completed type provides stable page membership while other types collect.
  const first = await (await request.get("/api/oss/catalog?leaf=feed-reader&limit=24&offset=0")).json();
  const second = await (await request.get("/api/oss/catalog?leaf=feed-reader&limit=24&offset=24")).json();
  expect(first.pagination.total).toBeGreaterThan(24);
  expect(second.projects).toHaveLength(24);
  expect(first.projects.some((p: { repository_id: number }) => second.projects.some((q: { repository_id: number }) => p.repository_id === q.repository_id))).toBe(false);
  await page.goto("/discover");
  await expect(page.getByRole("article")).toHaveCount(24);
  await screenshot(page, info, "discover");
  await page.getByRole("combobox", { name: "软件类型", exact: true }).selectOption("feed-reader");
  await expect(page.getByRole("article").first()).toHaveAccessibleName(first.projects[0].name);
  await page.getByRole("button", { name: "下一页", exact: true }).click();
  await expect(page).toHaveURL(/page=2/);
  await expect(page.getByRole("article").first()).toHaveAccessibleName(second.projects[0].name);
  await page.reload();
  await expect(page.getByRole("article").first()).toHaveAccessibleName(second.projects[0].name);
});

test("real project evidence, license and GitHub links expand correctly", async ({ page }, info) => {
  await page.goto("/discover?q=Foam");
  const card = page.getByRole("article", { name: "Foam", exact: true });
  await expect(page.getByRole("article")).toHaveCount(1);
  await card.getByText("查看功能、适用范围与来源", { exact: true }).click();
  await expect(card.getByRole("link", { name: "许可证原文", exact: true })).toHaveAttribute("href", /^https:\/\/github.com\/foambubble\/foam\//);
  await expect(card.getByRole("link", { name: "查看 GitHub 项目", exact: true })).toHaveAttribute("href", "https://github.com/foambubble/foam");
  await card.getByText("展开介绍与关联的原文依据", { exact: true }).click();
  await expect(card.locator("blockquote").first()).toBeVisible();
  await screenshot(page, info, "project-evidence");
});

test("real type, scenario and license filters match API counts", async ({ page, request }) => {
  const leaf = "feed-reader";
  const data = await (await request.get(`/api/oss/catalog?leaf=${leaf}&limit=24`)).json();
  await page.goto("/discover");
  await page.getByRole("combobox", { name: "软件类型", exact: true }).selectOption(leaf);
  await expect(page.getByRole("article")).toHaveCount(Math.min(24, data.pagination.total));
  const scenario = data.scenarios[0];
  await page.getByRole("button", { name: `${scenario.name} · ${scenario.project_count}`, exact: true }).click();
  const filtered = await (await request.get(`/api/oss/catalog?leaf=${leaf}&scenario=${scenario.id}&license=pending&limit=24`)).json();
  await page.getByRole("combobox", { name: "许可证", exact: true }).selectOption("pending");
  await expect(page.getByRole("article")).toHaveCount(Math.min(24, filtered.pagination.total));
  await page.getByRole("button", { name: "清除筛选", exact: true }).click();
  await expect(page).toHaveURL(/leaf=feed-reader$/);
  await expect(page.getByRole("article")).toHaveCount(Math.min(24, data.pagination.total));
});

test("favorites opens the existing personal state without changing it", async ({ page, request }, info) => {
  const favorites = await (await request.get("/api/oss/catalog?favorites=1&limit=24")).json();
  await page.goto("/discover?favorites=1");
  await expect(page.getByRole("heading", { name: "我的收藏", exact: true })).toBeVisible();
  await expect(page.getByRole("article")).toHaveCount(Math.min(24, favorites.pagination.total));
  await expect(page.getByRole("checkbox", { name: "只看收藏", exact: true })).toBeChecked();
  await screenshot(page, info, "favorites");
});

test("search finds a real repository and taxonomy aliases", async ({ page }, info) => {
  await page.goto("/search");
  await page.getByRole("textbox", { name: "搜索类型、场景或项目", exact: true }).fill("Foam");
  await page.getByRole("button", { name: "开始搜索", exact: true }).click();
  await expect(page.getByRole("article", { name: "Foam", exact: true })).toBeVisible();
  await screenshot(page, info, "search");
  await page.goto("/search?q=待办事项软件");
  await expect(page.locator('a[href="/types/task-management-application"]')).toBeVisible();
});

test("current collection progress and type data match their real API response", async ({ page }, info) => {
  const response = page.waitForResponse(r => new URL(r.url()).pathname === "/api/oss/batches");
  await page.goto("/types/instant-messaging-application");
  const job = (await (await response).json()).jobs[0];
  await expect(page.locator("main h1")).toHaveText("即时通讯应用");
  await expect(page.getByRole("article")).toHaveCount(24);
  const batch = page.getByRole("region", { name: "批量采集", exact: true });
  await expect(batch.getByRole("status")).toContainText(`${job.processed}/${job.total}`);
  if (["paused_model", "interrupted"].includes(job.status)) {
    await expect(batch.getByRole("button", { name: "继续批量任务", exact: true })).toBeVisible();
  } else if (job.status === "running") {
    await expect(batch.getByRole("status")).toContainText("批量采集中");
  }
  await screenshot(page, info, "type-collection");
});

test("settings renders real provider and GitHub status without submitting credentials", async ({ page }, info) => {
  await page.goto("/settings");
  await expect(page.getByRole("heading", { name: "当前生效", exact: true })).toBeVisible();
  await expect(page.getByRole("heading", { name: "GitHub Token", exact: true })).toBeVisible();
  await expect(page.getByRole("textbox", { name: "GitHub 访问令牌", exact: true })).toHaveValue("");
  await screenshot(page, info, "settings");
});

test("guide and historical entries remain navigable", async ({ page }, info) => {
  await page.goto("/guide");
  await expect(page.getByRole("heading", { name: "从一个想法，找到值得了解的项目", exact: true })).toBeVisible();
  await screenshot(page, info, "guide");
  await page.getByRole("link", { name: "打开历史工作区", exact: true }).click();
  await expect(page.getByRole("heading", { name: "历史工作区", exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: /^模板工厂/ })).toHaveAttribute("href", "/factory");
  await screenshot(page, info, "history");
});
