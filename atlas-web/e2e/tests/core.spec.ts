import { expect, test } from "@playwright/test";
import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const e2eRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const runtimeRoot = path.join(e2eRoot, ".e2e-runtime");
const draftPath = path.join(runtimeRoot, "drafts", "e2e-draft.md");
const draftFixture = path.join(runtimeRoot, "e2e-draft.fixture.md");

function resetDraftFixture() {
  mkdirSync(path.dirname(draftPath), { recursive: true });
  copyFileSync(draftFixture, draftPath);
}

function writeGeneratingDraftFixture() {
  const text = readFileSync(draftFixture, "utf8");
  const separator = text.indexOf("\n---\n", 4);
  if (separator < 0) throw new Error("draft fixture has no frontmatter terminator");
  const frontmatter = text.slice(0, separator + 5).replace("status: draft", "status: generating");
  writeFileSync(draftPath, `${frontmatter}\n`, "utf8");
}

test("browse opens a generated type leaf without browser errors", async ({ page }) => {
  const errors: string[] = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));

  await page.goto("/browse");
  const firstDomain = page.getByRole("button").filter({
    has: page.getByRole("heading", { level: 3 }),
  }).first();
  await expect(firstDomain).toBeVisible();
  await firstDomain.click();
  const leafLink = page.locator('a[href^="/types/"]').first();
  await expect(leafLink).toBeVisible();
  await leafLink.click();
  await expect(page).toHaveURL(/\/types\/[^/]+$/);
  await expect(page.locator("main h1")).toBeVisible();
  expect(errors).toEqual([]);
});

test("type page uses a stable source fallback without canonical API files", async ({ page }) => {
  const errors: string[] = [];
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto("/types/business-messaging-application");
  await expect(page.locator("main h1").first()).toBeVisible();
  await expect(page.getByRole("heading", { name: "正式资料阅读器", exact: true })).toBeVisible();
  await expect(page.getByText("静态资料", { exact: true })).toBeVisible();
  expect(errors).toEqual([]);
});

test("draft editor exposes dirty state and saves before deletion", async ({ page }) => {
  resetDraftFixture();
  await page.goto("/drafts/e2e-draft");
  const editor = page.getByRole("textbox");
  await expect(editor).toBeVisible();
  const original = await editor.inputValue();
  await editor.fill(`${original}\n\n## Browser Update\n\nSaved through the API.`);
  await expect(page.getByRole("button", { name: "查重", exact: true })).toBeDisabled();
  await expect(page.getByRole("button", { name: "生成中文对照", exact: true })).toBeDisabled();
  page.once("dialog", async (dialog) => {
    expect(dialog.message()).toContain("未保存");
    await dialog.dismiss();
  });
  await page.getByRole("link", { name: "草稿", exact: true }).click();
  await expect(page).toHaveURL(/\/drafts\/e2e-draft$/);

  const unsaved = page.getByText("未保存", { exact: true });
  await expect(unsaved).toBeVisible();
  const saveResponse = page.waitForResponse((response) =>
    response.request().method() === "PUT" && response.url().endsWith("/api/drafts/e2e-draft"));
  await page.getByRole("button", { name: "保存", exact: true }).click();
  expect((await saveResponse).ok()).toBeTruthy();
  await expect(page.getByText("已保存", { exact: true })).toBeVisible();
  await expect(unsaved).toBeHidden();
  await expect(editor).toHaveValue(/Browser Update/);

  page.once("dialog", (dialog) => dialog.accept());
  const deleteResponse = page.waitForResponse((response) =>
    response.request().method() === "DELETE" && response.url().endsWith("/api/drafts/e2e-draft"));
  await page.getByRole("button", { name: "删除", exact: true }).click();
  expect((await deleteResponse).ok()).toBeTruthy();
  await expect(page).toHaveURL(/\/drafts$/);
  await expect(page.getByText("E2E 草稿", { exact: true })).toHaveCount(0);
});

test("draft generation completion hydrates the editor", async ({ page }) => {
  writeGeneratingDraftFixture();
  await page.goto("/drafts/e2e-draft");
  const editor = page.getByRole("textbox");
  await expect(editor).toHaveValue(/^\s*$/);
  copyFileSync(draftFixture, draftPath);
  await expect(editor).toHaveValue(/This draft is created only inside the isolated Playwright runtime/, { timeout: 7000 });
});

test("draft polling exposes a stale state and retry affordance", async ({ page }) => {
  writeGeneratingDraftFixture();
  let fail = false;
  await page.route("**/api/drafts/e2e-draft", async (route) => {
    if (!fail) {
      await route.continue();
      return;
    }
    await route.fulfill({
      status: 503,
      contentType: "application/json",
      body: JSON.stringify({ error: "temporary outage" }),
    });
  });
  try {
    await page.goto("/drafts/e2e-draft");
    await expect(page.getByRole("textbox")).toBeVisible();
    fail = true;
    await expect(page.getByText("状态轮询中断，页面可能已过期。", { exact: true })).toBeVisible({ timeout: 7000 });
    await expect(page.getByRole("button", { name: "重试", exact: true })).toBeVisible();
  } finally {
    copyFileSync(draftFixture, draftPath);
  }
});

test("search matches type and application aliases", async ({ page }) => {
  await page.goto("/search");
  const search = page.getByRole("textbox", { name: "搜索类型或应用" });
  await search.fill("TickTick");
  await page.getByRole("button", { name: "开始搜索", exact: true }).click();
  await expect(page).toHaveURL(/q=TickTick/);
  await expect(page.locator('a[href="/types/to-do-list-application"]')).toBeVisible();
  await page.goto("/search?q=待办事项软件");
  await expect(page.locator('a[href="/types/task-management-application"]')).toBeVisible();
});

test("unknown routes render a real not-found page", async ({ page }) => {
  const errors: string[] = [];
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto("/route-that-does-not-exist");
  await expect(page.getByRole("heading", { name: "页面不存在", exact: true })).toBeVisible();
  await expect(page.getByText("404", { exact: true })).toBeVisible();
  expect(errors).toEqual([]);
});

test("apps hash links focus the target and invalid hashes explain recovery", async ({ page }) => {
  await page.goto("/apps#todoist");
  const target = page.locator("#todoist");
  await expect(target).toBeVisible();
  await expect(target).toBeFocused();
  await page.goto("/apps#missing-app");
  await expect(page.getByText("链接的应用不存在，请返回应用目录重新选择。", { exact: true })).toBeVisible();
});

test("mobile pages avoid horizontal overflow and name the draft editor", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 800 });
  for (const path of ["/browse", "/types/business-messaging-application"]) {
    await page.goto(path);
    const width = await page.evaluate(() => ({ body: document.body.scrollWidth, viewport: window.innerWidth }));
    expect(width.body).toBeLessThanOrEqual(width.viewport + 1);
  }
  resetDraftFixture();
  await page.goto("/drafts/e2e-draft");
  await expect(page.getByRole("textbox", { name: "草稿正文" })).toBeVisible();
  const width = await page.evaluate(() => ({ body: document.body.scrollWidth, viewport: window.innerWidth }));
  expect(width.body).toBeLessThanOrEqual(width.viewport + 1);
});

test("public catalog exposes bilingual labels and navigable canonical links", async ({ page }) => {
  await page.goto("/apps");
  await page.getByRole("button", { name: "切换到英文" }).click();
  await expect(page.getByText("Task Management Application", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("View classification evidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("Todoist is cataloged for Tasks, Projects and Calendar.", { exact: true })).toBeVisible();

  await page.goto("/types/human-resource-information-system-hris");
  const canonicalLink = page.locator('a[href="/types/human-capital-management-hcm"]').first();
  await expect(canonicalLink).toBeVisible();
  await canonicalLink.click();
  await expect(page).toHaveURL(/\/types\/human-capital-management-hcm$/);
  await expect(page.locator("main h1").first()).toBeVisible();
  await expect(page.getByRole("heading", { name: "Adjacent", exact: true }).first()).toBeVisible();
});

test("project detail state follows the selected project", async ({ page, request }) => {
  const created: string[] = [];
  try {
    for (const name of ["Project switch A", "Project switch B"]) {
      const response = await request.post("http://127.0.0.1:5199/api/projects", {
        headers: { "Content-Type": "application/json" },
        data: { name, objective: "Verify project identity", mode: "new" },
      });
      expect(response.status()).toBe(201);
      created.push((await response.json()).id);
    }
    await page.goto("/projects");
    await page.locator(`a[href="/projects/${created[0]}"]`).first().click();
    await expect(page.locator("main h1")).toHaveText("Project switch A");
    await page.goBack();
    await page.locator(`a[href="/projects/${created[1]}"]`).first().click();
    await expect(page.locator("main h1")).toHaveText("Project switch B");
  } finally {
    for (const id of created) {
      await request.delete(`http://127.0.0.1:5199/api/projects/${id}`);
    }
  }
});

test("English tutorial does not fall back to the long Chinese source", async ({ page }) => {
  await page.goto("/tutorial");
  await page.getByRole("button", { name: "切换到英文" }).click();
  await expect(page.getByRole("heading", { name: "Atlas Tutorial", exact: true })).toBeVisible();
  await expect(page.getByText("中文", { exact: false })).toHaveCount(0);
});

test("local API initializes recovery, backup download, and controlled restore", async ({ page, request }, testInfo) => {
  const health = await request.get("http://127.0.0.1:5199/api/health");
  expect(health.ok()).toBeTruthy();
  expect((await health.json()).recovery.status).toBe("completed");
  const readiness = await request.get("http://127.0.0.1:5199/api/ready");
  expect(readiness.status()).toBe(200);
  expect((await readiness.json()).ready).toBe(true);

  const response = await request.post("http://127.0.0.1:5199/api/projects", {
    headers: {
      "Content-Type": "application/json",
      "Origin": "https://attacker.example",
    },
    data: { name: "Blocked", objective: "Must not be created", mode: "new" },
  });
  expect(response.status()).toBe(403);
  expect((await response.json()).error).toContain("origin");

  const fixtureName = `Backup fixture ${testInfo.repeatEachIndex}-${Date.now()}`;
  let projectId: string | undefined;
  try {
    const created = await request.post("http://127.0.0.1:5199/api/projects", {
      headers: { "Content-Type": "application/json" },
      data: { name: fixtureName, objective: "Verify backup download", mode: "new" },
    });
    expect(created.status()).toBe(201);
    const project = await created.json();
    projectId = project.id;
    const backup = await request.post(
      `http://127.0.0.1:5199/api/projects/${project.id}/backup`,
      { headers: { "Content-Type": "application/json" }, data: {} },
    );
    expect(backup.status()).toBe(201);
    const backupResult = await backup.json();
    const download = await request.get(
      `http://127.0.0.1:5199${backupResult.download_url}`,
    );
    expect(download.status()).toBe(200);
    expect(download.headers()["content-disposition"]).toContain("attachment");
    expect((await download.body()).byteLength).toBeGreaterThan(100);

    await page.goto("/projects");
    const projectCard = page.locator("article").filter({ hasText: fixtureName });
    const uiDownload = page.waitForEvent("download");
    await projectCard.getByRole("button", { name: "备份", exact: true }).click();
    expect((await uiDownload).suggestedFilename()).toMatch(/\.zip$/);

    await projectCard.getByRole("button", { name: "管理备份", exact: true }).click();
    const backupPanel = page.locator("#backup-restore");
    await expect(backupPanel.getByText("备份与恢复", { exact: true })).toBeVisible();
    await expect(backupPanel.getByText("校验通过", { exact: true }).first()).toBeVisible();
    await backupPanel.getByRole("button", { name: "准备恢复", exact: true }).first().click();
    await expect(backupPanel.getByText("恢复到新的空项目库", { exact: true })).toBeVisible();
    page.once("dialog", async (dialog) => {
      expect(dialog.message()).toContain("新的空项目库");
      expect(dialog.message()).toContain("不会覆盖当前项目库");
      await dialog.accept();
    });
    await backupPanel.getByRole("button", { name: "确认恢复到新空库", exact: true }).click();
    await expect(backupPanel.getByText("恢复完成", { exact: false })).toBeVisible();
    page.once("dialog", async (dialog) => {
      expect(dialog.message()).toContain("删除备份");
      expect(dialog.message()).toContain("用户源码");
      await dialog.accept();
    });
    await backupPanel.getByRole("button", { name: "删除归档", exact: true }).first().click();
    await expect(backupPanel.getByText("备份归档已删除", { exact: false })).toBeVisible();
     await expect(backupPanel.getByRole("button", { name: "删除归档", exact: true })).toHaveCount(1);
  } finally {
    if (projectId) {
      await request.delete(`http://127.0.0.1:5199/api/projects/${projectId}`, {
        headers: { "Content-Type": "application/json" },
        data: { confirm: projectId },
      });
    }
  }
});
