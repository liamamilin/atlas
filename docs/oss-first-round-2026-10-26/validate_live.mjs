// Read-only browser checks against the existing services. Never starts a server.
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import { mkdir, writeFile } from "node:fs/promises";
const require = createRequire(new URL("../../atlas-web/package.json", import.meta.url));
const { chromium, expect } = require("@playwright/test");
const evidence = new URL("./live-validation/", import.meta.url);
await mkdir(evidence, { recursive: true });
const browser = await chromium.launch({ headless: true });
const results = [];
try {
  for (const [device, viewport] of [["desktop", { width: 1280, height: 900 }], ["mobile", { width: 390, height: 844 }]]) {
    const context = await browser.newContext({ viewport });
    const page = await context.newPage();
    const writes = [], errors = [];
    page.on("pageerror", e => errors.push(e.message));
    await page.route("**/api/**", route => {
      if (!["GET", "HEAD"].includes(route.request().method())) {
        writes.push(`${route.request().method()} ${new URL(route.request().url()).pathname}`);
        return route.abort("blockedbyclient");
      }
      return route.continue();
    });
    await page.goto("http://127.0.0.1:5188/discover?leaf=webmail-application");
    const batch = page.getByRole("region", { name: "批量采集", exact: true });
    await expect(batch.getByRole("status")).toContainText("已选候选");
    await expect(batch.getByRole("status")).toContainText("1598");
    await expect(batch.getByRole("status")).toContainText("候选保留待补");
    await expect(page.getByRole("article").first()).toBeVisible();
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth);
    expect(overflow).toBe(false);
    await page.screenshot({ path: fileURLToPath(new URL(`./first-round-${device}.png`, evidence)) });
    // Search a real, newly collected repository. Membership does not depend on
    // changing live pagination or on a prearranged project list.
    const project = await page.getByRole("article").first().getAttribute("aria-label");
    await page.goto(`http://127.0.0.1:5188/discover?leaf=webmail-application&q=${encodeURIComponent(project)}`);
    const card = page.getByRole("article", { name: project, exact: true });
    await expect(card).toBeVisible();
    await card.getByText("查看功能、适用范围与来源", { exact: true }).click();
    const github = await card.getByRole("link", { name: "查看 GitHub 项目", exact: true }).getAttribute("href");
    expect(github).toMatch(/^https:\/\/github.com\/[^/]+\/[^/]+$/);
    await expect(card.getByRole("heading", { name: "许可证核验", exact: true })).toBeVisible();
    await expect(card.getByRole("heading", { name: "资料来源", exact: true })).toBeVisible();
    await card.getByText("展开介绍与关联的原文依据", { exact: true }).click();
    await expect(card.locator("blockquote").first()).toBeVisible();
    expect(writes).toEqual([]);
    expect(errors).toEqual([]);
    results.push({ device, passed: true, project, github, overflow, writes, runtime_errors: errors });
    await page.screenshot({ path: fileURLToPath(new URL(`./project-evidence-${device}.png`, evidence)) });
    await context.close();
  }
  await writeFile(new URL("./BROWSER_START.json", import.meta.url), JSON.stringify({ checked_at: new Date().toISOString(), results }, null, 2) + "\n");
  console.log(JSON.stringify({ passed: true, checks: results.length, writes: 0 }));
} finally {
  await browser.close();
}
