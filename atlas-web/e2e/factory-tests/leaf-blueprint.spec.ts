import { expect, test } from "@playwright/test";

const leaf = {
  slug: "task-management-application", name: "Task management", name_zh: "任务管理",
  aliases_zh: [], section_id: "productivity", section_name: "Productivity", overview: "Tasks", dc: "",
  how: "", rules: "", variants: "", products: "", relations: [], apps: [],
};
const scenario = {
  id: "scn_tasks", leaf: leaf.slug, leaf_name: leaf.name, name: "Task history", objective: "Retain task history",
  status: "ready", revision: 2,
};
const blueprint = {
  artifact_type: "product-blueprint", id: "bp_tasks", job_id: "job_blueprint", leaf: leaf.slug,
  scenario_name: scenario.name, scenario_revision: 2, digest: "d".repeat(64), level: "L1", state: "published",
  publication_status: "published", review_status: "passed",
  manifest: { name: "Task product blueprint", description: "A cognition blueprint", phases: [{ id: "MVP", title: "First release" }] },
  provenance: { case_basis: { case_refs: [{ case_id: "case_tasks", revision: 1 }] } },
  formal_checks: [], acceptances: [], reports: [],
};
const starter = {
  ...blueprint, artifact_type: "runnable-starter", id: "starter_tasks", manifest: { ...blueprint.manifest, name: "Task starter" },
};

async function openLeaf(page: import("@playwright/test").Page, artifacts: unknown[]) {
  await page.addInitScript(() => localStorage.setItem("atlas-lang", "en"));
  await page.route(`**/data/leaves/${leaf.slug}.json`, route => route.fulfill({ json: leaf }));
  await page.route(`**/api/factory/catalog?leaf=${leaf.slug}`, route => route.fulfill({ json: [scenario] }));
  await page.route(`**/api/factory/artifacts?leaf=${leaf.slug}&published=1`, route => route.fulfill({ json: artifacts }));
  await page.goto(`/types/${leaf.slug}`);
}

test("published product blueprint links to phase export and does not offer runnable instantiate", async ({ page }) => {
  await openLeaf(page, [blueprint]);
  await expect(page.getByRole("heading", { name: "Task product blueprint" })).toBeVisible();
  await expect(page.getByText("No target runtime reports; an unknown status stays unknown.")).toBeVisible();
  await expect(page.getByRole("button", { name: "Create application archive" })).toHaveCount(0);
  await expect(page.getByRole("link", { name: "Open blueprint and choose a phase package" })).toHaveAttribute("href", "/factory?view=artifacts&artifact_id=bp_tasks");
});

test("published runnable starter keeps its application archive flow", async ({ page }) => {
  await openLeaf(page, [starter]);
  await page.route("**/api/factory/artifacts/starter_tasks/instantiate", route => route.fulfill({ json: { download_url: "/downloads/task-app.zip" } }));
  await expect(page.getByRole("button", { name: "Create application archive" })).toBeVisible();
  await page.getByRole("button", { name: "Create application archive" }).click();
  await expect(page.getByRole("link", { name: "Download application" })).toHaveAttribute("href", "/downloads/task-app.zip");
});
