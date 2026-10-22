import { expect, test } from "@playwright/test";

const apps = [
  { app_id: "app:alpha", name: "Alpha" },
  { app_id: "app:beta", name: "Beta" },
];
const cases = [
  { case_id: "case_alpha", revision: 2, app_id: "app:alpha", digest: "a".repeat(64), research: { summary: "Alpha pinned evidence" } },
  { case_id: "case_alpha_second", revision: 1, app_id: "app:alpha", digest: "c".repeat(64), research: { summary: "Second Alpha evidence" } },
  { case_id: "case_beta", revision: 4, app_id: "app:beta", digest: "b".repeat(64), research: { summary: "Beta pinned evidence" } },
];

test.beforeEach(async ({ page }) => {
  await page.route("**/data/apps.json", route => route.fulfill({ json: [] }));
  await page.route("**/api/factory/v1/applications", route => route.fulfill({ json: apps }));
  await page.route("**/api/factory/v1/cases?**", route => {
    const appId = new URL(route.request().url()).searchParams.get("app_id");
    return route.fulfill({ json: cases.filter(item => item.app_id === appId) });
  });
  await page.route("**/api/factory/v1/cases/*/revisions/*", route => {
    const id = new URL(route.request().url()).pathname.split("/").at(-3);
    const selected = cases.find(item => item.case_id === id);
    return selected ? route.fulfill({ json: { ...selected, source_snapshots: [], observations: [] } }) : route.fulfill({ status: 404, json: { error: "Missing case" } });
  });

});

test("shared case panel follows case deep links and browser history", async ({ page }) => {
  await page.goto("/apps?app_id=app%3Aalpha&case_id=case_alpha&case_revision=2");
  await expect(page.getByRole("heading", { name: "case_alpha · r2", exact: true })).toBeVisible();
  await page.getByLabel("共享案例应用").selectOption("app:beta");
  await expect(page).toHaveURL(/app_id=app%3Abeta/);
  await page.getByRole("button", { name: /case_beta · r4/ }).click();
  await expect(page.getByRole("heading", { name: "case_beta · r4", exact: true })).toBeVisible();
  await page.goBack();
  await expect(page.getByRole("heading", { name: "case_beta · r4", exact: true })).toBeVisible();
  await page.goBack();
  await expect(page.getByRole("heading", { name: "case_alpha · r2", exact: true })).toBeVisible();
  await page.goForward();
  await expect(page.getByRole("heading", { name: "case_beta · r4", exact: true })).toBeVisible();
  await page.goForward();
  await expect(page.getByRole("heading", { name: "case_beta · r4", exact: true })).toBeVisible();
});

test("case history restores defaults when URL parameters are removed", async ({ page }) => {
  await page.goto("/apps");
  await expect(page.getByRole("heading", { name: "case_alpha · r2", exact: true })).toBeVisible();
  await page.getByLabel("共享案例应用").selectOption("app:beta");
  await expect(page.getByRole("heading", { name: "case_beta · r4", exact: true })).toBeVisible();
  await page.goBack();
  await expect(page).toHaveURL(/\/apps$/);
  await expect(page.getByLabel("共享案例应用")).toHaveValue("app:alpha");
  await expect(page.getByRole("heading", { name: "case_alpha · r2", exact: true })).toBeVisible();
  await page.getByRole("button", { name: /case_alpha_second · r1/ }).click();
  await expect(page.getByRole("heading", { name: "case_alpha_second · r1", exact: true })).toBeVisible();
  await page.goBack();
  await expect(page.getByRole("heading", { name: "case_alpha · r2", exact: true })).toBeVisible();
});

test("factory opens the requested batches view and tab changes preserve browser history", async ({ page }) => {
  await page.route("**/data/meta.json", route => route.fulfill({ json: { leafIndex: [] } }));
  await page.route("**/api/factory/**", route => {
    const path = new URL(route.request().url()).pathname;
    if (path.endsWith("/status")) return route.fulfill({ json: { cli: { available: false, models: [] }, runtime: { available: false } } });
    if (path.endsWith("/assisted-templates")) return route.fulfill({ json: { items: [], unavailable: [], counts: { total: 0, core_verified: 0, not_run: 0 } } });
    return route.fulfill({ json: [] });
  });

  await page.goto("/factory?view=batches");
  await expect(page.getByRole("tab", { name: "任务批次" })).toHaveAttribute("aria-selected", "true");
  await expect(page.getByText("还没有任务批次")).toBeVisible();
  await page.getByRole("tab", { name: "模板制品" }).click();
  await expect(page).toHaveURL(/view=artifacts/);
  await expect(page.getByRole("tab", { name: "模板制品" })).toHaveAttribute("aria-selected", "true");
  await page.goBack();
  await expect(page.getByRole("tab", { name: "任务批次" })).toHaveAttribute("aria-selected", "true");
});


test("completed batches retain evidence without offering queue controls", async ({ page }) => {
  await page.route("**/api/factory/**", route => {
    const endpoint = new URL(route.request().url()).pathname;
    if (endpoint.endsWith("/batches")) return route.fulfill({ json: [{
      id: "bat_completed", state: "completed", created_at: "", jobs: [],
      config: { name: "Completed batch", kind: "scenarios", model: "", concurrency: 1 },
    }] });
    if (endpoint.endsWith("/status")) return route.fulfill({ json: { cli: { available: false, models: [] }, runtime: { available: false } } });
    return route.fulfill({ json: [] });
  });
  await page.setViewportSize({ width: 375, height: 800 });
  await page.goto("/factory?view=batches");
  await expect(page.getByRole("heading", { name: "Completed batch" })).toBeVisible();
  await expect(page.getByRole("button", { name: "暂停新任务", exact: true })).toHaveCount(0);
  await expect(page.getByRole("button", { name: "取消批次", exact: true })).toHaveCount(0);
  expect(await page.evaluate(() => document.body.scrollWidth)).toBeLessThanOrEqual(376);
});
