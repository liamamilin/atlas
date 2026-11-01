import { readFileSync } from "node:fs";
import path from "node:path";
import { expect, test } from "@playwright/test";

const snapshot = JSON.parse(readFileSync(path.resolve("../application-atlas-production-pack/oss_catalog_data/batch.snapshot.json"), "utf8"));
const leaves = ["feed-reader", "diagramming-application", "password-manager"];
function savedProjects(leaf: string) {
  const ids = new Set(snapshot.scenarios.filter((s: { leaf: string }) => s.leaf === leaf).map((s: { id: string }) => s.id));
  return snapshot.projects.filter((p: { leaves?: string[]; matches: { scenario_id: string }[] }) => p.leaves?.includes(leaf) || p.matches.some(m => ids.has(m.scenario_id)));
}

for (const leaf of leaves) {
  test(`${leaf}: real saved cards, scenario gaps and source links`, async ({ page, request }) => {
    const scenarios = snapshot.scenarios.filter((s: { leaf: string }) => s.leaf === leaf);
    const projects = savedProjects(leaf);
    const api = await (await request.get(`/api/oss/catalog?leaf=${leaf}`)).json();
    expect(api.scenarios).toHaveLength(scenarios.length);
    expect(api.scenarios.length).toBeGreaterThanOrEqual(3);
    expect(api.projects.map((p: { repository_id: number }) => p.repository_id)).toEqual(projects.map((p: { repository_id: number }) => p.repository_id));
    await page.goto(`/types/${leaf}`);
    await expect(page.locator("article[aria-label]")).toHaveCount(Math.min(24, projects.length));
    await expect(page.getByText(/自动发现：/)).toBeVisible();
    await expect(page.getByRole("button", { name: "更新项目资料", exact: true })).toBeVisible();
    const shown = await (await request.get(`/api/oss/catalog?leaf=${leaf}&limit=24&sort=recommended`)).json();
    const first = shown.projects.find((p: { generation_method?: string }) => p.generation_method === "live_search_and_grounded_extraction") || shown.projects[0];
    const card = page.getByRole("article", { name: first.name, exact: true });
    await expect(card.getByRole("link", { name: "GitHub", exact: true })).toHaveAttribute("href", first.github_url);
    await card.getByRole("link", { name: "查看详情", exact: true }).click();
    await expect(page).toHaveURL(new RegExp(`/repos/${first.repository_id}$`));
    if (first.license.source) await expect(page.getByRole("link", { name: "许可证原文", exact: true })).toHaveAttribute("href", first.license.source.url);
    await page.getByText("展开介绍与关联的原文依据", { exact: true }).click();
    await expect(page.locator("blockquote").first()).toBeVisible();
    await expect(page.locator('blockquote a[href*="/git/blobs/"]').first()).toHaveAttribute("href", /^https:\/\/api.github.com\/repos\/.+\/git\/blobs\//);
    await page.goBack();
    const empty = scenarios.find((s: { project_count: number }) => s.project_count === 0);
    if (empty) {
      await page.getByRole("button", { name: `${empty.name} · 0`, exact: true }).click();
      await expect(page.locator("article[aria-label]")).toHaveCount(0);
      await expect(page.getByText("没有符合当前筛选的项目。可以调整关键词、场景或许可状态。", { exact: true })).toBeVisible();
    }
  });
}

test("leaf selection, repository search and restricted licenses persist in URL", async ({ page }) => {
  await page.goto("/discover");
  await page.getByRole("combobox", { name: "软件类型", exact: true }).selectOption("feed-reader");
  await expect(page).toHaveURL(/leaf=feed-reader/);
  await expect(page.locator("article[aria-label]")).toHaveCount(Math.min(24, savedProjects("feed-reader").length));
  await page.getByRole("textbox", { name: "搜索项目、功能或场景", exact: true }).fill("miniflux/v2");
  await page.getByRole("button", { name: "搜索项目", exact: true }).click();
  await expect(page.locator("article[aria-label]")).toHaveCount(1);
  await page.reload();
  await expect(page.getByRole("article", { name: "v2", exact: true })).toBeVisible();
  await page.goto("/discover?leaf=diagramming-application&license=source_available");
  const card = page.getByRole("article", { name: "drawio", exact: true });
  await expect(card.getByTitle("源码可见 · 使用有限制")).toBeVisible();
  await card.getByRole("link", { name: "查看详情", exact: true }).click();
  await expect(page.getByText(/代码声明 Apache-2.0；README 对图标/)).toBeVisible();
  await page.getByText("展开介绍与关联的原文依据", { exact: true }).click();
  await expect(page.getByText("额外许可声明", { exact: true })).toBeVisible();
  await page.goBack();
  await page.getByRole("combobox", { name: "许可证", exact: true }).selectOption("open_source");
  await expect(page.locator("article[aria-label]")).toHaveCount(Math.min(24, savedProjects("diagramming-application").filter((p: { license: { status: string } }) => p.license.status === "open_source").length));
});

test("review exclusions stay unpublished and batch mobile cards fit the viewport", async ({ page, request }) => {
  const data = await (await request.get("/api/oss/catalog")).json();
  const sparse = data.projects.find((p: { full_name: string }) => p.full_name.toLowerCase() === "jaywcjlove/quick-rss");
  if (sparse) expect(sparse.completeness).toBe("partial");
  const bitwarden = data.projects.find((p: { full_name: string }) => p.full_name.toLowerCase() === "bitwarden/android");
  if (bitwarden && !bitwarden.matches.length) expect(bitwarden.completeness).toBe("partial");
  expect(new Set(data.projects.map((p: { repository_id: number }) => p.repository_id)).size).toBe(data.projects.length);
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/types/password-manager");
  await expect(page.locator("article[aria-label]")).toHaveCount(Math.min(24, savedProjects("password-manager").length));
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  await page.screenshot({ path: "../docs/oss-batch-2026-10-23/batch-mobile.png" });
});

test("conditional associations expose prerequisites and unread candidates stay visible", async ({ page, request }) => {
  const data = await (await request.get("/api/oss/catalog?leaf=feed-reader")).json();
  const project = data.projects.find((p: { matches: { applicability?: string }[] }) => p.matches.some(m => m.applicability === "conditional"));
  expect(project).toBeTruthy();
  await page.goto(`/repos/${project.repository_id}`);
  await expect(page.getByText("条件适用", { exact: true }).first()).toBeVisible();
  const match = project.matches.find((m: { applicability?: string }) => m.applicability === "conditional");
  await expect(page.getByText(`适用条件：${match.conditions[0]}`, { exact: true }).first()).toBeVisible();
  await page.goto(`/types/feed-reader?q=${encodeURIComponent(project.full_name)}`);
  const queue = page.getByLabel("候选读取队列", { exact: true });
  await queue.locator("summary").click();
  const expectedPending = snapshot.candidates.filter((c: { leaf: string; status: string }) => c.leaf === "feed-reader" && c.status === "pending").length;
  expect(data.discovery.counts.pending).toBe(expectedPending);
  await expect(queue.getByText(expectedPending ? "等待读取" : "已收录 · 资料待补充", { exact: true }).first()).toBeVisible();
  await page.screenshot({ path: "../docs/oss-batch-v3-2026-10-23/candidates-and-conditions.png" });
});
