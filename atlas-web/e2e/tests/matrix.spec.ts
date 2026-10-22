import { expect, test, type APIRequestContext } from "@playwright/test";
import { copyFileSync, mkdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const e2eRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const runtimeRoot = path.join(e2eRoot, ".e2e-runtime");
const draftPath = path.join(runtimeRoot, "drafts", "e2e-draft.md");
const draftFixture = path.join(runtimeRoot, "e2e-draft.fixture.md");
const apiBase = `http://127.0.0.1:${process.env.ATLAS_E2E_API_PORT || "5199"}`;

function resetDraftFixture() {
  mkdirSync(path.dirname(draftPath), { recursive: true });
  copyFileSync(draftFixture, draftPath);
}

async function createProject(request: APIRequestContext, name: string) {
  const response = await request.post(`${apiBase}/api/projects`, {
    headers: { "Content-Type": "application/json" },
    data: { name, objective: "Exercise the route matrix", mode: "new" },
  });
  expect(response.status()).toBe(201);
  return (await response.json()).id as string;
}

async function deleteProject(request: APIRequestContext, projectId: string) {
  await request.delete(`${apiBase}/api/projects/${projectId}`, {
    headers: { "Content-Type": "application/json" },
    data: { confirm: projectId },
  });
}

function routesForProject(projectId: string) {
  return [
    "/",
    "/browse",
    "/types/business-messaging-application",
    "/search",
    "/apps",
    "/drafts",
    "/drafts/e2e-draft",
    "/projects",
    `/projects/${projectId}`,
    "/tutorial",
    "/ask",
    "/settings",
  ];
}

async function assertNormalPage(page: any, route: string) {
  await page.goto(route);
  await expect(page.locator("main h1").first()).toBeVisible();
  const width = await page.evaluate(() => ({
    body: document.body.scrollWidth,
    viewport: window.innerWidth,
    offenders: [...document.querySelectorAll<HTMLElement>("body *")]
      .map((element) => ({ element, rect: element.getBoundingClientRect() }))
      .filter(({ rect }) => rect.right > window.innerWidth + 1 || rect.left < -1)
      .slice(0, 8)
      .map(({ element, rect }) => ({
        tag: element.tagName,
        className: element.className,
        text: element.textContent?.trim().slice(0, 80),
        left: Math.round(rect.left),
        right: Math.round(rect.right),
      })),
  }));
  expect(width.body, `horizontal overflow at ${route}: ${JSON.stringify(width.offenders)}`).toBeLessThanOrEqual(width.viewport + 1);
}

test.setTimeout(90_000);

test("normal route matrix passes at 375px and 768px", async ({ page, request }) => {
  resetDraftFixture();
  const projectId = await createProject(request, `Matrix normal ${Date.now()}`);
  try {
    for (const viewport of [{ width: 375, height: 800 }, { width: 768, height: 900 }]) {
      await page.setViewportSize(viewport);
      for (const route of routesForProject(projectId)) {
        await assertNormalPage(page, route);
      }
    }
  } finally {
    await deleteProject(request, projectId);
    resetDraftFixture();
  }
});

test("language and accessible names hold across the route matrix", async ({ page, request }) => {
  resetDraftFixture();
  const projectId = await createProject(request, `Matrix language ${Date.now()}`);
  try {
    await page.setViewportSize({ width: 768, height: 900 });
    await page.goto("/");
    await page.getByRole("button", { name: "切换到英文" }).click();
    await expect(page.locator("html")).toHaveAttribute("lang", "en");
    for (const route of routesForProject(projectId)) {
      await page.goto(route);
      await expect(page.locator("html")).toHaveAttribute("lang", "en");
      await expect(page.locator("main h1").first()).toBeVisible();
      const unnamedButtons = await page.locator("button").evaluateAll((buttons) => buttons.filter((button) => {
        const element = button as HTMLButtonElement;
        return !element.getAttribute("aria-label")
          && !element.getAttribute("aria-labelledby")
          && !element.textContent?.trim()
          && !element.getAttribute("title");
      }).length);
      expect(unnamedButtons, `unnamed button at ${route}`).toBe(0);
      const unnamedControls = await page.locator("input, textarea, select").evaluateAll((controls) => controls.filter((control) => {
        const element = control as HTMLInputElement;
        return !element.getAttribute("aria-label")
          && !element.getAttribute("aria-labelledby")
          && !(element.labels && element.labels.length);
      }).length);
      expect(unnamedControls, `unnamed control at ${route}`).toBe(0);
    }
  } finally {
    await deleteProject(request, projectId);
    resetDraftFixture();
  }
});

test("route error matrix exposes a recoverable alert", async ({ page }) => {
  const cases = [
    { route: "/", pattern: "**/data/meta.json" },
    { route: "/browse", pattern: "**/data/meta.json" },
    { route: "/types/missing-matrix-leaf", pattern: "**/data/leaves/missing-matrix-leaf.json" },
    { route: "/search", pattern: "**/data/meta.json" },
    { route: "/apps", pattern: "**/data/apps.json" },
    { route: "/drafts", pattern: "**/api/drafts" },
    { route: "/drafts/e2e-draft", pattern: "**/api/drafts/e2e-draft" },
    { route: "/projects", pattern: "**/api/projects" },
    { route: "/projects/prj_missingmatrix", pattern: "**/api/projects/prj_missingmatrix/workspace" },
  ];
  for (const item of cases) {
    const handler = async (route: any) => route.fulfill({
      status: 503,
      contentType: "application/json",
      body: JSON.stringify({ error: "matrix outage" }),
    });
    await page.route(item.pattern, handler);
    await page.goto(item.route);
    await expect(page.getByRole("alert").first(), `error state for ${item.route}`).toBeVisible();
    await page.unroute(item.pattern, handler);
  }

  const tutorialHandler = async (route: any) => route.fulfill({
    status: 500,
    contentType: "text/plain",
    body: "matrix import failure",
  });
  await page.route("**/src/routes/tutorial.tsx*", tutorialHandler);
  await page.goto("/tutorial");
  await expect(page.getByRole("heading", { name: "页面加载失败", exact: true })).toBeVisible();
  await page.unroute("**/src/routes/tutorial.tsx*", tutorialHandler);
});

test("representative empty states remain explicit and navigable", async ({ page, request }) => {
  resetDraftFixture();
  const emptyMeta = {
    leafCount: 0,
    sectionCount: 0,
    l0Count: 0,
    appCount: 0,
    l0s: [],
    leafIndex: [],
  };
  const metaHandler = async (route: any) => route.fulfill({
    status: 200,
    contentType: "application/json",
    body: JSON.stringify(emptyMeta),
  });
  await page.route("**/data/meta.json", metaHandler);
  await page.goto("/");
  await expect(page.getByText("类型目录为空", { exact: true })).toBeVisible();
  await page.goto("/browse");
  await expect(page.getByText("类型目录为空", { exact: true })).toBeVisible();
  await page.unroute("**/data/meta.json", metaHandler);

  const appsHandler = async (route: any) => route.fulfill({
    status: 200,
    contentType: "application/json",
    body: "[]",
  });
  await page.route("**/data/apps.json", appsHandler);
  await page.goto("/apps");
  await expect(page.getByText("应用目录为空", { exact: true })).toBeVisible();
  await page.unroute("**/data/apps.json", appsHandler);

  const draftsHandler = async (route: any) => route.fulfill({
    status: 200,
    contentType: "application/json",
    body: "[]",
  });
  await page.route("**/api/drafts", draftsHandler);
  await page.goto("/drafts");
  await expect(page.getByText("暂无草稿", { exact: true })).toBeVisible();
  await page.unroute("**/api/drafts", draftsHandler);

  const projectsHandler = async (route: any) => route.fulfill({
    status: 200,
    contentType: "application/json",
    body: "[]",
  });
  await page.route("**/api/projects", projectsHandler);
  await page.goto("/projects");
  await expect(page.getByText("还没有项目", { exact: false })).toBeVisible();
  await page.unroute("**/api/projects", projectsHandler);

  await page.goto("/search?q=matrix-no-match-zzzz");
  await expect(page.getByText("没有匹配的类型或应用", { exact: true })).toBeVisible();

  const leaf = {
    slug: "empty-matrix-leaf",
    name: "Empty Matrix Leaf",
    name_zh: "空矩阵类型",
    aliases_zh: [],
    section_id: "",
    section_name: "",
    overview: "",
    dc: "",
    how: "",
    rules: "",
    variants: "",
    products: "",
    full_md: "",
    relations: [],
    apps: [],
  };
  const leafHandler = async (route: any) => route.fulfill({
    status: 200,
    contentType: "application/json",
    body: JSON.stringify(leaf),
  });
  const sourceHandler = async (route: any) => route.fulfill({
    status: 200,
    contentType: "application/json",
    body: JSON.stringify({ slug: "empty-matrix-leaf", sources: [] }),
  });
  await page.route("**/data/leaves/empty-matrix-leaf.json", leafHandler);
  await page.route("**/api/sources/empty-matrix-leaf", sourceHandler);
  await page.goto("/types/empty-matrix-leaf");
  await expect(page.getByRole("heading", { name: "空矩阵类型", exact: true })).toBeVisible();
  await expect(page.getByText("该类型暂无正式 Markdown 资料。", { exact: true })).toBeVisible();
  await page.unroute("**/data/leaves/empty-matrix-leaf.json", leafHandler);
  await page.unroute("**/api/sources/empty-matrix-leaf", sourceHandler);

  const projectId = await createProject(request, `Matrix empty ${Date.now()}`);
  try {
    await page.goto(`/projects/${projectId}`);
    await expect(page.getByText("当前没有活动迭代", { exact: false })).toBeVisible();
  } finally {
    await deleteProject(request, projectId);
    resetDraftFixture();
  }
});
