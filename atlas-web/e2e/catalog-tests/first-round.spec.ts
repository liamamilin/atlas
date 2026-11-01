import { expect, test } from "@playwright/test";

test("pilot gate shows first-round scope, retained candidates and blocks duplicate starts", async ({ page }) => {
  const leaves = ["feed-reader", ...Array.from({ length: 1597 }, (_, i) => `remaining-type-${i}`)];
  const job = { id: "batch_" + "d".repeat(32), status: "awaiting_acceptance", leaves,
    prepared: leaves.slice(0, 20), completed_leaves: leaves.slice(0, 20), processed: 1200, total: 1200,
    targets: {}, errors: [], existing_only: false, scope: "first_round", first_round_limit: 60,
    deferred_total: 2400, pilot: { size: 20, status: "awaiting_acceptance" } };
  await page.route("**/api/oss/batches**", route => {
    expect(route.request().method()).toBe("GET");
    return route.fulfill({ json: { jobs: [job] } });
  });
  await page.goto("/discover?leaf=feed-reader");
  const batch = page.getByRole("region", { name: "批量采集", exact: true });
  await expect(batch.getByRole("status")).toContainText("试跑结束，等待实际验收");
  await expect(batch.getByRole("status")).toContainText("已选候选 1200/1200");
  await expect(batch.getByRole("status")).toContainText("首轮已结束 20/1598 个类型");
  await expect(batch.getByRole("status")).toContainText("2400 个候选保留待补");
  await expect(batch.getByRole("status")).toContainText("通过后自动续批，无需逐批确认");
  await batch.locator("summary").first().click();
  await expect(batch.getByRole("button", { name: "开始批量采集", exact: true })).toBeDisabled();
  await expect(batch.getByRole("button", { name: "继续批量任务", exact: true })).toHaveCount(0);
  expect((await batch.getByRole("status").innerText()).length).toBeLessThan(2200);
  await expect(batch.getByText("remaining-type-1590", { exact: false })).toHaveCount(0);
  await page.setViewportSize({ width: 390, height: 844 });
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
});

test("finished first round continues to show its deferred queue", async ({ page }) => {
  const job = { id: "batch_" + "e".repeat(32), status: "completed", leaves: ["feed-reader"], prepared: ["feed-reader"],
    completed_leaves: ["feed-reader"], processed: 60, total: 60, targets: {}, errors: [], existing_only: false,
    scope: "first_round", first_round_limit: 60, deferred_total: 122, pilot: { size: 0, status: "not_required" } };
  await page.route("**/api/oss/batches**", route => route.fulfill({ json: { jobs: [job] } }));
  await page.goto("/discover?leaf=feed-reader");
  const batch = page.getByRole("region", { name: "批量采集", exact: true });
  await expect(batch.getByRole("status")).toContainText("首轮处理完成");
  await expect(batch.getByRole("status")).toContainText("122 个候选保留待补");
  await expect(batch.getByRole("status")).toContainText("待补候选保留在候选池");
});
