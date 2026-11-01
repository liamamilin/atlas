import { expect, test } from "@playwright/test";

test("choose existing non-pilot leaves, start a batch and resume saved progress", async ({ page, request }) => {
  const catalog = await (await request.get("/api/oss/catalog?leaf=feed-reader")).json();
  expect(catalog.supported_leaves.some((l: { slug: string }) => l.slug === "bookmark-manager")).toBe(true);
  expect(catalog.supported_leaves.length).toBeGreaterThan(100);
  let jobs: unknown[] = [];
  let submitted: { leaves: string[]; existing_only: boolean } | null = null;
  const job = { id: "batch_" + "a".repeat(32), status: "running", leaves: ["feed-reader", "bookmark-manager"], prepared: ["feed-reader", "bookmark-manager"], processed: 1, total: 5, targets: {}, errors: [], existing_only: true };
  await page.route("**/api/oss/batches**", async route => {
    if (route.request().method() === "GET") return route.fulfill({ json: { jobs } });
    if (route.request().url().endsWith("/resume")) {
      jobs = [{ ...job, status: "completed", processed: 5 }];
      return route.fulfill({ status: 202, json: jobs[0] });
    }
    submitted = route.request().postDataJSON(); jobs = [job];
    return route.fulfill({ status: 202, json: job });
  });
  await page.goto("/discover?leaf=feed-reader");
  const batch = page.getByRole("region", { name: "批量采集", exact: true });
  await batch.locator("summary").first().click();
  await batch.getByRole("combobox", { name: "加入软件类型", exact: true }).selectOption("bookmark-manager");
  await batch.getByRole("button", { name: "加入", exact: true }).click();
  await batch.getByRole("checkbox", { name: "仅处理已有候选，本次不扩大搜索", exact: true }).check();
  await batch.getByRole("button", { name: "开始批量采集", exact: true }).click();
  await expect(batch.getByRole("status")).toContainText("1/5");
  expect(submitted).toEqual({ leaves: ["feed-reader", "bookmark-manager"], existing_only: true, first_round_limit: 60 });
  jobs = [{ ...job, status: "interrupted", processed: 3 }];
  await page.reload();
  await batch.getByRole("button", { name: "继续批量任务", exact: true }).click();
  await expect(batch.getByRole("status")).toContainText("批量采集完成 · 5/5");
});

test("partial projects remain browsable without scenario links or quotes", async ({ page }) => {
  let sparse: Record<string, unknown> = {};
  await page.route("**/api/oss/projects/*", route => route.fulfill({ json: { project: sparse, scenarios: [], leaves: [{ slug: "feed-reader", name: "Feed Reader" }] } }));
  await page.route("**/api/oss/catalog?**", async route => {
    const response = await route.fetch(); const data = await response.json();
    const proof = { source_url: "https://api.github.com/repos/test/sparse", immutable_url: "", source_sha256: "a".repeat(64), excerpt: "", verification: "source_based" };
    data.projects = [{ ...data.projects[0], name: "Sparse project", full_name: "test/sparse", positioning: "候选项目 · 定位待补充", summary: "来自仓库元数据的初步介绍", scope: "适用范围待补充", matches: [], features: [], completeness: "partial", missing_fields: ["features", "scenario_associations", "license_verification"], summary_evidence: proof, scope_evidence: proof, positioning_evidence: proof, generation_method: "live_search_coverage_first", license: { status: "pending", spdx: null, note: "许可证未核验", source: null }, collection_notes: ["README 暂不可读"] }];
    sparse = data.projects[0];
    return route.fulfill({ json: data });
  });
  await page.goto("/discover?leaf=feed-reader");
  const card = page.getByRole("article", { name: "Sparse project", exact: true });
  await expect(card.getByText("资料待补充", { exact: true })).toBeVisible();
  await card.getByRole("link", { name: "查看详情", exact: true }).click();
  await expect(page.getByRole("heading", { level: 1, name: "Sparse project" })).toBeVisible();
  await expect(page.getByText("尚未建立场景关联；仍可按类型浏览。", { exact: true })).toBeVisible();
  await expect(page.getByText("功能说明待补充", { exact: true })).toBeVisible();
  await expect(page.getByText("README 暂不可读", { exact: true })).toBeVisible();
  await page.getByText("展开介绍与关联的原文依据", { exact: true }).click();
  await expect(page.getByText("依据下方资料概述，未附逐字引文。", { exact: true }).first()).toBeVisible();
  await page.setViewportSize({ width: 390, height: 844 });
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
});

test("model-paused batches expose a reason and resume the same saved job", async ({ page }) => {
  let job = { id: "batch_" + "b".repeat(32), status: "paused_model", leaves: ["feed-reader"], prepared: ["feed-reader"], processed: 2, total: 5, targets: {}, errors: [], existing_only: true, pause_reason: "资料整理模型不可用：quota_exhausted；请检查模型设置后继续" };
  await page.route("**/api/oss/batches**", route => {
    if (route.request().method() === "GET") return route.fulfill({ json: { jobs: [job] } });
    expect(route.request().url()).toContain(`${job.id}/resume`);
    job = { ...job, status: "completed", processed: 5, pause_reason: "" };
    return route.fulfill({ status: 202, json: job });
  });
  await page.goto("/discover?leaf=feed-reader");
  const batch = page.getByRole("region", { name: "批量采集", exact: true });
  await expect(batch.getByRole("status")).toContainText("服务配置需处理，批量任务已暂停 · 2/5");
  await expect(batch.getByText(/quota_exhausted/)).toBeVisible();
  await batch.getByRole("button", { name: "继续批量任务", exact: true }).click();
  await expect(batch.getByRole("status")).toContainText("批量采集完成 · 5/5");
});

test("temporary outages show persisted automatic retry time and allow waking the existing worker", async ({ page }) => {
  let job = { id: "batch_" + "c".repeat(32), status: "retry_wait", leaves: ["feed-reader"], prepared: ["feed-reader"], processed: 2, total: 16, targets: {}, errors: [], existing_only: true, auto_recovery: true, pause_reason: "", recovery: { next_retry_at: "2026-10-24T04:10:00+00:00", cycles: 2, last_error: "HTTP 520 · 临时网关故障" } };
  let resumes = 0;
  await page.route("**/api/oss/batches**", route => {
    if (route.request().method() === "GET") return route.fulfill({ json: { jobs: [job] } });
    expect(route.request().url()).toContain(`${job.id}/resume`);
    resumes += 1;
    job = { ...job, status: "running", pause_reason: "" };
    return route.fulfill({ status: 202, json: job });
  });
  await page.goto("/discover?leaf=feed-reader");
  const batch = page.getByRole("region", { name: "批量采集", exact: true });
  await expect(batch.getByRole("status")).toContainText("临时故障，等待自动恢复 · 2/16");
  await expect(batch.getByText("HTTP 520 · 临时网关故障", { exact: true })).toBeVisible();
  await expect(batch.getByText(/自动重试，无需手动继续/)).toBeVisible();
  await batch.locator("summary").first().click();
  await expect(batch.getByRole("button", { name: "开始批量采集", exact: true })).toBeDisabled();
  await batch.getByRole("button", { name: "立即重试", exact: true }).click();
  await expect(batch.getByRole("status")).toContainText("批量采集中 · 2/16");
  expect(resumes).toBe(1);
});
