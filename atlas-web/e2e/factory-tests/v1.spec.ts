import { expect, test } from "@playwright/test";

const scenario = {
  id: "scn_11111111111111111111111111111111", leaf: "task-management-application", leaf_name: "任务管理",
  name: "V1 task history", audience: "个人用户", objective: "保留任务记录", workflow: ["添加任务", "重新打开"], acceptance: ["记录仍存在"], updated_at: new Date().toISOString(), status: "ready", revision: 3,
  reviews: [{ current: true, outcome: "passed", scenario_revision: 3 }],
};
const legacyApp = { slug: "task-manager", name: "Task Manager", nameEn: "Task Manager", nameZh: "任务管理器", vendor: "Open source", tagline: "Manage personal tasks", taglineEn: "Manage personal tasks", tasks: ["Tasks"], taskLabels: { zh: ["任务"] }, leaf: "task-management-application", leafNameEn: "Task management", leafNameZh: "任务管理" };
const app = { app_id: "app:task-manager", legacy_slug: "task-manager", slug: "task-manager", name: "Task Manager", catalog_status: "researched" };
const sourceCase = {
  case_id: "case_task", revision: 2, app_id: app.app_id, digest: "d".repeat(64), evidence_digest: "e".repeat(64),
  research: { summary: "Pinned task lifecycle research", unknowns: ["Runtime behavior is unknown"] },
  source_snapshots: [{ repository: "https://github.com/example/tasks", commit_sha: "a".repeat(40), files: { "src/task.py": "b".repeat(64) }, file_manifest_digest: "c".repeat(64) }],
  observations: [{ evidence_id: "ev_code", kind: "code_observation", statement: "The task state is persisted.", location: { path: "src/task.py", commit_sha: "a".repeat(40), file_digest: "b".repeat(64) }, digest: "f".repeat(64), observation_status: "reviewed", reviews: [{ outcome: "accepted", reviewer: "human" }] }],
  scenario_links: [{ scenario_id: scenario.id, scenario_revision: 3, reason: "Supports task history", workflow_support: ["reload"], evidence_ids: ["ev_code"] }],
};

test("shared cases show fixed source, evidence, unknowns and keep legacy cards when the dynamic API is unavailable", async ({ page }) => {
  await page.route("**/data/apps.json", route => route.fulfill({ json: [legacyApp] }));
  await page.route("**/api/factory/v1/applications", route => route.fulfill({ status: 503, json: { error: "Case service unavailable" } }));
  await page.goto("/apps");
  await expect(page.getByRole("heading", { name: "应用目录", exact: true })).toBeVisible();
  await expect(page.getByRole("region", { name: "共享案例库" })).toBeVisible();
  await expect(page.getByText("Case service unavailable")).toBeVisible();
  await expect(page.locator("[id='task-manager']")).toBeVisible();
});

test("case revisions expose observed evidence separately from unknown runtime and link into factory", async ({ page }) => {
  await page.route("**/data/apps.json", route => route.fulfill({ json: [legacyApp] }));
  await page.route("**/api/factory/v1/applications", route => route.fulfill({ json: [app] }));
  await page.route(`**/api/factory/v1/cases?app_id=${encodeURIComponent(app.app_id)}`, route => route.fulfill({ json: [sourceCase] }));
  await page.route(`**/api/factory/v1/cases/${sourceCase.case_id}/revisions/2`, route => route.fulfill({ json: sourceCase }));
  await page.goto("/apps");
  await expect(page.getByRole("heading", { name: "case_task · r2", exact: true })).toBeVisible();
  await expect(page.getByText("Pinned task lifecycle research", { exact: true }).last()).toBeVisible();
  await page.locator("details").filter({ hasText: "ev_code" }).locator("summary").click();
  await expect(page.getByText("The task state is persisted.", { exact: true })).toBeVisible();
  await expect(page.getByText("Runtime behavior is unknown", { exact: true })).toBeVisible();
  await expect(page.getByText("aaaaaaaaaaaa", { exact: false }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: /打开模板目录与导出/ })).toHaveAttribute("href", /factory\?view=artifacts&case_id=case_task&case_revision=2/);
});

test("V1 plan survives run, pause, resume and reload with a stable idempotency key", async ({ page }) => {
  await page.route("**/api/factory/catalog", route => route.fulfill({ json: [scenario] }));
  await page.route("**/api/factory/batches", route => route.fulfill({ json: [] }));
  await page.route("**/api/factory/artifacts", route => route.fulfill({ json: [] }));
  await page.route("**/api/factory/status", route => route.fulfill({ json: { cli: { available: true, models: ["test/deepseek-flash", "opencode-go/deepseek-v4.1-flash"] }, runtime: { available: true } } }));
  await page.route("**/api/factory/v1/applications", route => route.fulfill({ json: [app] }));
  await page.route(`**/api/factory/v1/scenarios/${scenario.id}/basis`, route => route.fulfill({ json: { scenario_id: scenario.id, scenario_name: scenario.name, stage: "template_production", review_status: "passed", cases: [], evidence_scope: "No fixed evidence", blockers: ["case evidence pending"] } }));
  const digest = "1".repeat(64);
  const preview = { plan_id: "plan_v1", plan_digest: digest, state: "preview", seeds: [{ scenario_id: scenario.id, scenario_revision: 3, next_stage: "research", case_status: "missing" }], excluded: [], budget: { sessions_used: 4, sessions_limit: 500 } };
  let previewBody: Record<string, unknown> | undefined;
  const runBodies: Record<string, unknown>[] = [];
  let currentState = "preview";
  const currentPlan = () => ({ ...preview, state: currentState, batch: { id: "batch_v1", state: currentState } });
  await page.route("**/api/factory/v1/plans/preview", async route => { previewBody = route.request().postDataJSON(); await route.fulfill({ json: preview }); });
  let runCount = 0;
  await page.route("**/api/factory/v1/plans/plan_v1/run", async route => {
    runBodies.push(route.request().postDataJSON());
    runCount += 1;
    currentState = "running"; // Simulate accepted work whose first response was lost.
    if (runCount === 1) await route.fulfill({ status: 502, json: { error: "response lost" } });
    else await route.fulfill({ status: 202, json: { plan_id: "plan_v1", plan_digest: digest, batch: { id: "batch_v1", state: "running" } } });
  });
  await page.route("**/api/factory/v1/plans/plan_v1/pause", route => { currentState = "paused"; return route.fulfill({ json: { id: "batch_v1", state: "paused" } }); });
  await page.route("**/api/factory/v1/plans/plan_v1/resume", route => { currentState = "running"; return route.fulfill({ json: { id: "batch_v1", state: "running" } }); });
  await page.route("**/api/factory/v1/plans/plan_v1", route => route.fulfill({ json: currentPlan() }));
  await page.route("**/api/factory/v1/plans/plan_v1/report", route => route.fulfill({ json: { batch: { id: "batch_v1", state: currentState }, counts: {}, quality_result: currentState, budget: { cli_sessions_used: 1 } } }));
  await page.route("**/data/apps.json", route => route.fulfill({ json: [] }));
  await page.goto("/factory");
  await page.getByRole("tab", { name: "V1 计划与预算", exact: true }).click();
  await expect(page.getByRole("heading", { name: "V1 批次预览与执行", exact: true })).toBeVisible();
  await page.locator("label").filter({ hasText: scenario.name }).getByRole("checkbox").check();
  await page.getByRole("button", { name: "生成只读预览", exact: true }).click();
  await expect.poll(() => previewBody).toMatchObject({ scenario_ids: [scenario.id], model: "opencode-go/deepseek-v4.1-flash", admission_policy: "ready-only-v1", segment: "G1" });
  await expect(page.getByText("固定计划摘要", { exact: false })).toBeVisible();
  await page.getByRole("button", { name: "按固定摘要运行", exact: true }).click();
  await expect(page.getByRole("alert")).toContainText("response lost");
  await page.getByRole("button", { name: "按固定摘要运行", exact: true }).click();
  await expect.poll(() => runBodies.length).toBe(2);
  await expect(page).toHaveURL(/view=v1.*plan=plan_v1/);
  expect(runBodies[0]).toMatchObject({ expected_plan_digest: digest });
  expect(runBodies[1]).toEqual(runBodies[0]);
  expect(runBodies[0].idempotency_key).toBe(`run:plan_v1:${digest}`);
  await expect(page.getByRole("region", { name: "批次计划" }).getByText(/运行中/)).toBeVisible();
  await expect(page.getByText(scenario.id, { exact: false })).toBeVisible();
  await page.getByRole("button", { name: "暂停", exact: true }).click();
  await expect(page.getByRole("region", { name: "批次计划" }).getByText(/已暂停/)).toBeVisible();
  await page.getByRole("button", { name: "继续", exact: true }).click();
  await expect(page.getByRole("region", { name: "批次计划" }).getByText(/运行中/)).toBeVisible();
  await page.reload();
  await expect(page.getByText("plan_v1", { exact: false })).toBeVisible();
  await expect(page.getByText(scenario.id, { exact: false })).toBeVisible();
  await page.getByRole("button", { name: "暂停", exact: true }).click();
  expect(page.url()).toContain("/factory");
});

test("V1 catalog shows each blueprint runtime result per run and target, with no aggregate fallback", async ({ page }) => {
  const artifact = (id: string, acceptances: Record<string, unknown>[], runtime_status?: string) => ({
    id, artifact_type: "product-blueprint", digest: `${id}-digest`, state: "draft",
    runtime_status, review_status: "unavailable", evidence_status: "legacy_unverified",
    manifest: { name: id }, acceptances,
  });
  const runs = [
    { id: "run_passed_01", method: "blueprint-runtime", outcome: "passed", selected_phase: "P0", suite_status: "passed", phase_status: "passed", target_binding: { application_digest: "target-app-001" } },
    { id: "run_failed_02", method: "blueprint-runtime", outcome: "failed", selected_phase: "P1", suite_status: "failed", phase_status: "blocked", target_binding: { application_digest: "target-app-002" } },
  ];
  await page.route("**/api/factory/catalog", route => route.fulfill({ json: [] }));
  await page.route("**/api/factory/batches", route => route.fulfill({ json: [] }));
  await page.route("**/api/factory/artifacts", route => route.fulfill({ json: [
    artifact("artifact-with-runs", runs, "passed"), artifact("artifact-without-runs", [], "passed"),
  ] }));
  await page.route("**/api/factory/status", route => route.fulfill({ json: { cli: { available: true, models: [] }, runtime: { available: true } } }));
  await page.route("**/api/factory/v1/applications", route => route.fulfill({ json: [] }));
  await page.route("**/data/apps.json", route => route.fulfill({ json: [] }));

  await page.goto("/factory?view=v1");
  await expect(page.getByRole("heading", { name: "模板审阅、发布与撤回" })).toBeVisible();
  const withRuns = page.locator("article").filter({ hasText: "artifact-with-runs" });
  await expect(withRuns.getByText(/run_passed_01.*target-app-001.*P0.*suite_status: passed.*phase_status: passed/)).toBeVisible();
  await expect(withRuns.getByText(/run_failed_02.*target-app-002.*P1.*suite_status: failed.*phase_status: blocked/)).toBeVisible();
  await expect(withRuns.getByRole("link", { name: "查看运行断言" }).first()).toHaveAttribute("href", /view=artifacts&artifact_id=artifact-with-runs&runtime_run_id=run_passed_01/);
  await expect(page.locator("article").filter({ hasText: "artifact-without-runs" }).getByText("未运行", { exact: true })).toBeVisible();
});

test("fresh deep link restores a running plan, polls its report, pauses by plan ID, then stops at terminal state", async ({ page }) => {
  const planId = "plan_1234567890abcdef1234567890abcdef";
  const digest = "9".repeat(64);
  const batchId = "bat_abcdef1234567890abcdef1234567890";
  let state = "running";
  let reportRequests = 0;
  let planRequests = 0;
  let pauseRequestUrl = "";
  const plan = {
    id: planId, digest, campaign_id: "atlas-v1-first-production-2026-10-19", segment: "G1",
    seeds: [{ product_id: "product_1", scenario, runtime_sample: true, next_stage: "template" }],
    excluded: [], limits: { cli_sessions: 500, segment_seconds: 28800, production: 2, runtime: 1 },
  };
  await page.addInitScript(() => localStorage.clear());
  await page.route("**/api/factory/catalog", route => route.fulfill({ json: [scenario] }));
  await page.route("**/api/factory/batches", route => route.fulfill({ json: [] }));
  await page.route("**/api/factory/artifacts", route => route.fulfill({ json: [] }));
  await page.route("**/api/factory/status", route => route.fulfill({ json: { cli: { available: true, models: ["opencode-go/deepseek-v4.1-flash"] }, runtime: { available: true } } }));
  await page.route("**/api/factory/v1/applications", route => route.fulfill({ json: [app] }));
  await page.route(`**/api/factory/v1/scenarios/${scenario.id}/basis`, route => route.fulfill({ json: { scenario_id: scenario.id, stage: "template_production", blockers: [] } }));
  await page.route("**/data/apps.json", route => route.fulfill({ json: [] }));
  await page.route(`**/api/factory/v1/plans/${planId}`, route => {
    planRequests += 1;
    return route.fulfill({ json: { ...plan, state } });
  });
  await page.route(`**/api/factory/v1/plans/${planId}/report`, route => {
    reportRequests += 1;
    return route.fulfill({ json: {
      batch: { id: batchId, state, jobs: [] }, quality_result: "in_progress",
      budget: { cli_sessions_used: 37, cli_sessions_limit: 500, remaining_seconds: 28000 },
    } });
  });
  await page.route(`**/api/factory/v1/plans/${planId}/pause`, async route => {
    pauseRequestUrl = new URL(route.request().url()).pathname;
    state = "paused";
    await route.fulfill({ json: { id: batchId, state } });
  });
  await page.goto(`/factory?view=v1&plan=${planId}`);
  const planRegion = page.getByRole("region", { name: "批次计划" });
  await expect(planRegion.getByText(planId, { exact: false })).toBeVisible();
  await expect(planRegion).toContainText(digest);
  await expect(planRegion).toContainText("cli_sessions_used");
  await expect(planRegion).toContainText("37");
  await expect(page.getByRole("group", { name: "运行抽验场景" }).getByRole("checkbox")).toBeChecked();
  await expect.poll(() => reportRequests).toBeGreaterThan(1);
  await expect(page.getByRole("button", { name: "暂停", exact: true })).toBeEnabled();
  await page.getByRole("button", { name: "暂停", exact: true }).click();
  await expect(planRegion).toContainText(/已暂停|暂停/);
  expect(pauseRequestUrl).toBe(`/api/factory/v1/plans/${planId}/pause`);

  state = "completed";
  await page.getByRole("button", { name: "刷新计划", exact: true }).click();
  await expect(planRegion).toContainText(/已完成|completed/);
  const terminalReportCount = reportRequests;
  await page.waitForTimeout(4300);
  expect(reportRequests).toBe(terminalReportCount);
  expect(planRequests).toBeGreaterThan(0);
});
