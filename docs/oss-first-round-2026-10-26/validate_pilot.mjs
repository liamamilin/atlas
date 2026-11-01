// Actual read-only pilot acceptance against the already running production UI.
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import { readFile, writeFile, mkdir } from "node:fs/promises";
const require = createRequire(new URL("../../atlas-web/package.json", import.meta.url));
const { chromium, expect } = require("@playwright/test");
const base = new URL("./", import.meta.url);
const samples = JSON.parse(await readFile(new URL("PILOT_REVIEW_INPUT.json", base), "utf8"));
await mkdir(new URL("live-validation/", base), { recursive: true });
const browser = await chromium.launch({ headless: true });
const checks = [], writes = [], errors = [];
try {
  for (const [device, viewport, cases] of [
    ["desktop", { width: 1280, height: 900 }, samples],
    ["mobile", { width: 390, height: 844 }, samples.filter(x => ["cold-chain-transportation-monitoring", "population-health-management", "creator-tip-platform"].includes(x.leaf))],
  ]) {
    const context = await browser.newContext({ viewport });
    const page = await context.newPage();
    page.on("pageerror", error => errors.push(error.message));
    await page.route("**/api/**", route => {
      if (!["GET", "HEAD"].includes(route.request().method())) {
        writes.push(`${route.request().method()} ${new URL(route.request().url()).pathname}`);
        return route.abort("blockedbyclient");
      }
      return route.continue();
    });
    for (const sample of cases) {
      const query = new URLSearchParams({ leaf: sample.leaf, q: sample.repo });
      await page.goto(`http://127.0.0.1:5188/discover?${query}`);
      const card = page.getByRole("article").filter({ has: page.locator(`a[href="${sample.url}"]`) });
      await expect(card).toHaveCount(1);
      await expect(card).toBeVisible();
      const batch = page.getByRole("region", { name: "批量采集", exact: true });
      await expect(batch.getByRole("status")).toContainText("试跑结束，等待实际验收");
      await expect(batch.getByRole("status")).toContainText("20/1598");
      await expect(batch.getByRole("status")).toContainText("2388 个候选保留待补");
      await card.getByText("查看功能、适用范围与来源", { exact: true }).click();
      await expect(card.getByRole("heading", { name: "许可证核验", exact: true })).toBeVisible();
      await expect(card.getByRole("heading", { name: "资料来源", exact: true })).toBeVisible();
      await expect(card.getByRole("link", { name: "查看 GitHub 项目", exact: true })).toHaveAttribute("href", sample.url);
      await card.getByText("展开介绍与关联的原文依据", { exact: true }).click();
      await expect(card.locator("blockquote").first()).toBeVisible();
      const licenseResponse = page.waitForResponse(response => {
        const url = new URL(response.url());
        return url.pathname === "/api/oss/catalog" && url.searchParams.get("leaf") === sample.leaf
          && url.searchParams.get("q") === sample.repo && url.searchParams.get("license") === sample.license.status;
      });
      await page.getByRole("combobox", { name: "许可证", exact: true }).selectOption(sample.license.status);
      const filtered = await (await licenseResponse).json();
      expect(filtered.pagination.total).toBe(1);
      await expect(page.getByText("正在读取项目…", { exact: true })).toHaveCount(0);
      await expect(card).toBeVisible();
      if (sample.leaf === "cold-chain-transportation-monitoring") {
        await expect(card).toContainText("IoT 接入、邮件/SMS 告警尚属后续计划");
      }
      if (sample.leaf === "population-health-management") {
        await expect(card).toContainText("当前演示数据全部为本地生成的合成数据");
      }
      if (sample.leaf === "creator-tip-platform") {
        await expect(card).toContainText("当前不能端到端收款");
      }
      if (device === "mobile" || sample.leaf === "webmail-application") {
        await batch.getByRole("status").screenshot({ path: fileURLToPath(new URL(`live-validation/pilot-gate-${device}-${sample.leaf}.png`, base)) });
        await card.evaluate(element => { element.scrollIntoView({ block: "start" }); window.scrollBy(0, -120); });
        await page.screenshot({ path: fileURLToPath(new URL(`live-validation/pilot-card-${device}-${sample.leaf}.png`, base)) });
      }
      expect(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)).toBe(false);
      checks.push({ device, leaf: sample.leaf, repo: sample.repo, search: true, source: true, license: sample.license.status, github_link: true, gate_and_deferred: true, passed: true });
    }
    // A real scenario filter, beyond project-name/leaf/license filtering.
    await page.goto("http://127.0.0.1:5188/discover?leaf=profiler");
    const scenario = page.getByRole("button", { name: /^定位接口响应变慢的代码 · / });
    await expect(scenario).toBeVisible();
    await scenario.click();
    const selectedScenario = new URL(page.url()).searchParams.get("scenario");
    expect(selectedScenario).toBeTruthy();
    const response = await page.request.get(`http://127.0.0.1:5188/api/oss/catalog?leaf=profiler&scenario=${selectedScenario}&limit=24&offset=0`);
    const data = await response.json();
    await expect(page.getByRole("article")).toHaveCount(Math.min(24, data.pagination.total));
    checks.push({ device, scenario_filter: selectedScenario, projects: data.pagination.total, passed: true });
    await context.close();
  }
  expect(writes).toEqual([]);
  expect(errors).toEqual([]);
  const result = { checked_at: new Date().toISOString(), passed: true, cases: checks, writes, runtime_errors: errors };
  await writeFile(new URL("PILOT_BROWSER.json", base), JSON.stringify(result, null, 2) + "\n");
  console.log(JSON.stringify({ passed: true, checks: checks.length, writes: 0, runtime_errors: 0 }));
} finally {
  await browser.close();
}
