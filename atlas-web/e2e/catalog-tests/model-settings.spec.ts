import { expect, test } from "@playwright/test";

for (const width of [1280, 390]) {
  test(`provider editing stays visible and saves changes at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 844 });
    const provider = (id: string, name = id) => ({
      id, name, preset: "", style: "openai", base_url: `https://${id}.example/v1`,
      models: ["fixture-model"], has_key: true, key_masked: "test••••only", updated_at: "",
    });
    const settings = {
      providers: [provider("one"), provider("two"), provider("three"), provider("four"), provider("opencode-go", "OpenCode Go")],
      default: { provider: "one", model: "fixture-model" },
      embedding: { provider: "", base_url: "", model: "" },
      presets: { custom: { name: "Another preset", style: "openai", base_url: "https://custom.example/v1", models: ["another-model"] } },
      resolved: { configured: false, reason: "Test fixture" }, embeddings: [],
    };
    const saved: Record<string, unknown>[] = [];
    await page.route("**/api/settings/github", route => route.fulfill({ json: { configured: false, source: "anonymous" } }));
    await page.route("**/api/settings/model", route => route.fulfill({ json: settings }));
    await page.route("**/api/settings/model/providers/opencode-go/test", route => route.fulfill({
      json: { id: "opencode-go", ok: false, error: "Old credential failed", code: "unauthorized", models: [], model_count: 0, latency_ms: 1 },
    }));
    await page.route("**/api/settings/model/providers", async route => {
      const input = route.request().postDataJSON();
      saved.push(input);
      const target = settings.providers.find(p => p.id === input.id)!;
      Object.assign(target, { name: input.name, base_url: input.base_url, models: input.models });
      await route.fulfill({ json: target });
    });
    await page.goto("/settings");
    const row = page.getByRole("article", { name: "OpenCode Go", exact: true });
    await row.getByRole("button", { name: "测试连接", exact: true }).click();
    await expect(row.getByText("Old credential failed")).toBeVisible();
    await row.getByRole("button", { name: "编辑", exact: true }).click();
    const form = page.getByRole("form", { name: "编辑服务 · OpenCode Go", exact: true });
    await expect(form.getByRole("heading")).toBeInViewport();
    await expect(form.getByLabel("显示名称", { exact: true })).toBeFocused();
    // The editor belongs to the selected row, rather than the top of a long list.
    await expect(row.locator("..").getByRole("form")).toHaveCount(1);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
    await expect(form.locator('input[type="password"]')).toHaveValue("");
    await form.getByLabel("接口地址（base URL）", { exact: true }).fill("https://updated.example/v1");
    await form.getByRole("textbox", { name: "模型（逗号或换行分隔）", exact: true }).fill("new-model, other-model");
    await form.getByRole("button", { name: "保存", exact: true }).click();
    await expect(form).toHaveCount(0);
    expect(saved[0]).toMatchObject({ id: "opencode-go", base_url: "https://updated.example/v1", models: ["new-model", "other-model"] });
    expect(saved[0]).not.toHaveProperty("api_key");
    await expect(row.getByText("Old credential failed")).toHaveCount(0);
    await row.getByRole("button", { name: "编辑", exact: true }).click();
    await expect(form.getByLabel("接口地址（base URL）", { exact: true })).toHaveValue("https://updated.example/v1");
    // Changing the preset of an existing provider must keep its identity.
    await form.getByRole("combobox", { name: "常用服务", exact: true }).selectOption("custom");
    await page.getByRole("form").locator('input[type="password"]').fill("e2e-provider-key-not-real");
    await page.getByRole("form").getByRole("button", { name: "保存", exact: true }).click();
    await expect(page.getByRole("form")).toHaveCount(0);
    expect(saved[1]).toMatchObject({ id: "opencode-go", api_key: "e2e-provider-key-not-real" });
    await page.getByRole("article", { name: "Another preset", exact: true }).getByRole("button", { name: "编辑", exact: true }).click();
    await expect(page.getByRole("form").locator('input[type="password"]')).toHaveValue("");
    await page.getByRole("form").getByRole("button", { name: "取消", exact: true }).click();
    await expect(page.getByRole("form")).toHaveCount(0);
    expect(saved).toHaveLength(2);
  });
}

test("quota fallback is visible and retrying the primary clears its active state", async ({ page }) => {
  const provider = (id: string, name: string) => ({ id, name, preset: id, style: "openai", base_url: `https://${id}.example/v1`, models: ["deepseek-v4.1-flash"], has_key: true, key_masked: "fixture••••only", updated_at: "" });
  const settings = {
    providers: [provider("open-design", "Open Design"), provider("opencode-go", "OpenCode Go")],
    default: { provider: "open-design", model: "deepseek-v4.1-flash" },
    fallback: { enabled: true, from_provider: "open-design", provider: "opencode-go", model: "deepseek-v4.1-flash", active: true },
    embedding: { provider: "", base_url: "", model: "" }, presets: {}, embeddings: [],
    resolved: { configured: true, provider: "opencode-go", provider_name: "OpenCode Go", model: "deepseek-v4.1-flash", source: "fallback", base_url: "https://go.example/v1" },
  };
  await page.route("**/api/settings/model", route => route.fulfill({ json: settings }));
  await page.route("**/api/settings/model/fallback", route => {
    expect(route.request().postDataJSON()).toEqual({ reset: true });
    settings.fallback.active = false;
    Object.assign(settings.resolved, { provider: "open-design", provider_name: "Open Design", source: "config" });
    return route.fulfill({ json: settings.fallback });
  });
  await page.goto("/settings");
  await expect(page.getByText("额度耗尽，已自动切换", { exact: true })).toBeVisible();
  await expect(page.getByLabel("额度耗尽备用服务")).toContainText("Open Design → OpenCode Go · deepseek-v4.1-flash");
  await page.getByRole("button", { name: "重试主服务", exact: true }).click();
  await expect(page.getByText("额度耗尽，已自动切换", { exact: true })).toHaveCount(0);
  await expect(page.getByRole("button", { name: "重试主服务", exact: true })).toHaveCount(0);
  await expect(page.getByRole("combobox", { name: "默认服务", exact: true })).toHaveValue("open-design");
});
