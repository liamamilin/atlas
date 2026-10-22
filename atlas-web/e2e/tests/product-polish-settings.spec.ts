import { expect, test } from "@playwright/test";

const provider = (id: string) => ({
  id, name: `Provider ${id}`, preset: "", style: "openai", base_url: `https://${id}.example/v1`,
  models: [`${id}-configured`], has_key: false, key_masked: "", updated_at: "",
});

const settings = {
  providers: [provider("alpha"), provider("beta")],
  default: { provider: "alpha", model: "alpha-configured" },
  embedding: { provider: "", base_url: "", model: "" },
  presets: {}, resolved: { configured: false, reason: "Test only; no credentials" }, embeddings: [],
};

test.beforeEach(async ({ page }) => {
  await page.route("**/api/settings/model", route => route.fulfill({ json: settings }));
});

test("model suggestions follow the provider even when the previous list returns late", async ({ page }) => {
  let releaseAlpha!: () => void;
  let alphaStarted!: () => void;
  const started = new Promise<void>(resolve => { alphaStarted = resolve; });
  const released = new Promise<void>(resolve => { releaseAlpha = resolve; });
  await page.route("**/api/settings/model/providers/alpha/models", async route => {
    alphaStarted();
    await released;
    await route.fulfill({ json: { id: "alpha", models: ["alpha-remote"] } });
  });
  await page.route("**/api/settings/model/providers/beta/models", route =>
    route.fulfill({ json: { id: "beta", models: ["beta-remote"] } }));

  await page.goto("/settings");
  await expect(page.getByLabel("默认模型", { exact: true })).toHaveValue("alpha-configured");
  await page.getByRole("button", { name: "查看全部模型", exact: true }).click();
  await started;
  await page.getByRole("combobox", { name: "默认服务", exact: true }).selectOption("beta");
  await expect(page.getByLabel("默认模型", { exact: true })).toHaveValue("beta-configured");
  await expect(page.locator("datalist option")).toHaveAttribute("value", "beta-configured");
  const completed = page.waitForResponse("**/api/settings/model/providers/alpha/models");
  releaseAlpha();
  await completed;
  await expect(page.locator("datalist option")).toHaveAttribute("value", "beta-configured");
  await page.getByRole("button", { name: "查看全部模型", exact: true }).click();
  await expect(page.locator("datalist option")).toHaveAttribute("value", "beta-remote");
});

test("failed model lookup shows an error and retains configured suggestions", async ({ page }) => {
  let fail = true;
  await page.route("**/api/settings/model/providers/alpha/models", route => fail
    ? route.fulfill({ status: 502, json: { error: "Model list temporarily unavailable" } })
    : route.fulfill({ json: { id: "alpha", models: ["alpha-recovered"] } }));
  await page.goto("/settings");
  const load = page.getByRole("button", { name: "查看全部模型", exact: true });
  await load.click();
  await expect(page.getByRole("alert")).toContainText("Model list temporarily unavailable");
  await expect(page.locator("datalist option")).toHaveAttribute("value", "alpha-configured");
  fail = false;
  await load.click();
  await expect(page.locator("datalist option")).toHaveAttribute("value", "alpha-recovered");
  await expect(page.getByRole("alert")).toHaveCount(0);
});
