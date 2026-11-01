import { expect, test } from "@playwright/test";

const pilot = "personal-knowledge-management-application";

test("overview returns coverage without full project cards and home stays bounded", async ({ page, request }) => {
  const response = await request.get("/api/oss/catalog?view=overview");
  const data = await response.json();
  expect(data.projects).toEqual([]);
  expect(data.stats.projects).toBeGreaterThan(7);
  expect(data.supported_leaves.every((l: { project_count: number }) => l.project_count > 0)).toBe(true);
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "继续探索", exact: true })).toBeVisible();
  expect(await page.locator('main a[href^="/types/"]').count()).toBeLessThanOrEqual(10);
  await expect(page).toHaveTitle("首页 · 应用图谱");
});

test("pagination keeps every project reachable, survives reload and resets on filters", async ({ page, request }) => {
  const first = await (await request.get("/api/oss/catalog?leaf=feed-reader&limit=24&sort=recommended")).json();
  const second = await (await request.get("/api/oss/catalog?leaf=feed-reader&limit=24&offset=24&sort=recommended")).json();
  expect(first.pagination.total).toBeGreaterThan(24);
  expect(second.scenarios).toEqual(first.scenarios);
  expect(first.projects.some((p: { repository_id: number }) => second.projects.some((s: { repository_id: number }) => s.repository_id === p.repository_id))).toBe(false);
  await page.goto("/discover?leaf=feed-reader");
  await expect(page.getByRole("article")).toHaveCount(24);
  await page.getByRole("button", { name: "下一页", exact: true }).click();
  await expect(page).toHaveURL(/page=2/);
  await expect(page.getByRole("article").first()).toHaveAccessibleName(second.projects[0].name);
  await page.reload();
  await expect(page.getByRole("article").first()).toHaveAccessibleName(second.projects[0].name);
  await page.getByRole("textbox", { name: "搜索项目、功能或场景", exact: true }).fill("miniflux/v2");
  await page.getByRole("button", { name: "搜索项目", exact: true }).click();
  await expect(page).not.toHaveURL(/page=/);
  await expect(page.getByRole("article")).toHaveCount(1);
  await page.getByRole("button", { name: "清除筛选", exact: true }).click();
  await expect(page).toHaveURL(/leaf=feed-reader$/);
  await expect(page.getByRole("article")).toHaveCount(24);
});

test("search stays editable while repositories wait and taxonomy appears independently", async ({ page }) => {
  let release!: () => void;
  const gate = new Promise<void>(resolve => { release = resolve; });
  await page.route("**/api/oss/catalog?**", async route => {
    if (new URL(route.request().url()).searchParams.get("q") === "密码") await gate;
    await route.continue();
  });
  await page.goto("/search?q=密码");
  await expect(page.locator('a[href="/types/password-manager"]').first()).toBeVisible();
  const input = page.getByRole("textbox", { name: "搜索类型、场景或项目", exact: true });
  await input.fill("Foam");
  await page.getByRole("button", { name: "开始搜索", exact: true }).click();
  await expect(page.getByRole("article", { name: "Foam", exact: true })).toBeVisible();
  release();
  await expect(input).toHaveValue("Foam");
  await expect(page).toHaveURL(/q=Foam$/);
});

test("service failures preserve navigation and have a working retry", async ({ page }) => {
  let offline = true;
  await page.route("**/api/health", route => offline ? route.fulfill({ status: 503, json: { error: "offline" } }) : route.continue());
  await page.route("**/api/oss/catalog?**", route => offline ? route.fulfill({ status: 503, json: { error: "offline" } }) : route.continue());
  await page.goto(`/discover?leaf=${pilot}`);
  await expect(page.getByText("本地服务暂时无法连接。分类资料仍可阅读；项目库、收藏和设置需要服务恢复。", { exact: true })).toBeVisible();
  await expect(page.getByRole("button", { name: "重新读取", exact: true })).toBeVisible();
  offline = false;
  await page.getByRole("button", { name: "重新检查", exact: true }).click();
  await expect(page.getByRole("button", { name: "重新检查", exact: true })).toHaveCount(0);
  await page.getByRole("button", { name: "重新读取", exact: true }).click();
  await expect(page.getByRole("article")).toHaveCount(7);
});

test("mobile navigation, favorites, guide and all main pages fit the viewport", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  const errors: string[] = []; page.on("pageerror", e => errors.push(e.message));
  for (const path of ["/", "/browse", "/discover", "/search", "/settings", "/guide", "/history", `/types/${pilot}`]) {
    await page.goto(path);
    await expect(page.locator("main h1").first()).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    const nav = page.getByRole("navigation", { name: "主导航", exact: true });
    for (const label of ["首页", "浏览类型", "发现项目", "我的收藏", "搜索"]) await expect(nav.getByRole("link", { name: label, exact: true })).toBeInViewport();
  }
  await page.getByRole("navigation", { name: "主导航", exact: true }).getByRole("link", { name: "我的收藏", exact: true }).click();
  await expect(page.getByRole("heading", { name: "我的收藏", exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: "我的收藏", exact: true }).first()).toHaveAttribute("aria-current", "page");
  expect(errors).toEqual([]);
});

test("invalid or blocked language storage does not crash the product", async ({ page }) => {
  await page.addInitScript(() => localStorage.setItem("atlas-lang", "invalid-language"));
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "想做一件事，先看看已有的可能性", exact: true })).toBeVisible();
  await page.getByRole("button", { name: "切换到英文", exact: true }).click();
  await expect(page).toHaveTitle("Home · Application Atlas");
  await page.addInitScript(() => {
    Storage.prototype.getItem = () => { throw new DOMException("Storage blocked", "SecurityError"); };
    Storage.prototype.setItem = () => { throw new DOMException("Storage blocked", "SecurityError"); };
  });
  await page.goto("/guide");
  await expect(page.getByRole("heading", { name: "从一个想法，找到值得了解的项目", exact: true })).toBeVisible();
  await page.getByRole("button", { name: "切换到英文", exact: true }).click();
  await expect(page.getByRole("heading", { name: "Find projects worth exploring", exact: true })).toBeVisible();
  await page.goto(`/types/${pilot}`);
  await expect(page.getByRole("heading", { name: "个人知识管理应用", exact: true })).toBeVisible();
  await expect(page.getByRole("article")).toHaveCount(7);
});

test("GitHub settings remain usable when model settings fail", async ({ page }) => {
  let failing = true;
  await page.route("**/api/settings/model", route => failing ? route.fulfill({ status: 503, json: { error: "Model configuration unavailable" } }) : route.continue());
  await page.goto("/settings");
  await expect(page.getByRole("textbox", { name: "GitHub 访问令牌", exact: true })).toBeVisible();
  await expect(page.getByText("加载失败", { exact: true })).toBeVisible();
  failing = false;
  await page.getByRole("button", { name: "重新加载", exact: true }).click();
  await expect(page.getByRole("heading", { name: "当前生效", exact: true })).toBeVisible();
});

test("desktop navigation starts a new page at its heading and exposes skip navigation", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("link", { name: "历史工作区与模板工厂", exact: true }).scrollIntoViewIfNeeded();
  await page.getByRole("link", { name: "历史工作区与模板工厂", exact: true }).click();
  await expect(page.getByRole("heading", { name: "历史工作区", exact: true })).toBeInViewport();
  await expect(page.locator("#main-content")).toBeFocused();
  await page.keyboard.press("Tab");
  await page.goto("/guide");
  await page.keyboard.press("Tab");
  await expect(page.getByRole("link", { name: "跳到主要内容", exact: true })).toBeFocused();
});

test("back navigation restores reading position after a lazy page remounts", async ({ page }) => {
  await page.goto("/browse");
  const target = page.locator('section[id="14"]');
  await target.scrollIntoViewIfNeeded();
  const before = await page.evaluate(() => window.scrollY);
  expect(before).toBeGreaterThan(1000);
  await page.getByRole("navigation", { name: "主导航", exact: true }).getByRole("link", { name: "发现项目", exact: true }).click();
  await expect(page.locator("main h1")).toBeInViewport();
  await page.goBack();
  await expect.poll(() => page.evaluate(() => window.scrollY)).toBeGreaterThan(before - 150);
});

test("capture the current product pages for visual review", async ({ page }) => {
  test.setTimeout(60_000);
  test.skip(!process.env.ATLAS_VISUAL_REVIEW, "Run with ATLAS_VISUAL_REVIEW=1 to update review screenshots");
  const views = [
    ["home", "/"], ["browse", "/browse"], ["discover", "/discover"],
    ["leaf", `/types/${pilot}`], ["search", "/search?q=Foam"],
    ["settings", "/settings"], ["guide", "/guide"], ["history", "/history"],
  ];
  for (const width of [1280, 390]) {
    await page.setViewportSize({ width, height: 900 });
    for (const [name, path] of views) {
      await page.goto(path);
      await expect(page.locator("main h1").first()).toBeVisible();
      if (name === "home") await expect(page.getByRole("heading", { name: "继续探索", exact: true })).toBeVisible();
      if (name === "discover") await expect(page.getByRole("article")).toHaveCount(24);
      if (name === "leaf") await expect(page.getByRole("article")).toHaveCount(7);
      if (name === "search") await expect(page.getByRole("article", { name: "Foam", exact: true })).toBeVisible();
      if (name === "settings") await expect(page.getByRole("heading", { name: "当前生效", exact: true })).toBeVisible();
      await page.screenshot({ path: `../docs/product-polish-2026-10-23/${name}-${width}.png` });
    }
  }
});
