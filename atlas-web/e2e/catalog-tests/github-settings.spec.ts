import { expect, test } from "@playwright/test";

test("GitHub token is write-only, persists, clears and rejects cross-site writes", async ({ page, request }) => {
  await page.goto("/settings");
  const section = page.getByRole("region", { name: "GitHub Token", exact: true });
  await expect(section.getByText("未配置 · 使用公开匿名额度", { exact: true })).toBeVisible();
  const secret = "e2e-fixture-token-not-real";
  await section.getByLabel("GitHub 访问令牌", { exact: true }).fill(secret);
  await section.getByRole("button", { name: "保存 GitHub Token", exact: true }).click();
  await expect(section.getByText("已配置 · 本机保存", { exact: true })).toBeVisible();
  await expect(section.getByLabel("GitHub 访问令牌", { exact: true })).toHaveValue("");
  const saved = await (await request.get("/api/settings/github")).json();
  expect(saved).toEqual({ configured: true, source: "local" });
  expect(JSON.stringify(saved)).not.toContain(secret);
  await page.reload();
  await expect(section.getByText("已配置 · 本机保存", { exact: true })).toBeVisible();
  await section.getByRole("button", { name: "保存 GitHub Token", exact: true }).click();
  await expect(section.getByText("GitHub 设置已保存，后续采集立即使用。", { exact: true })).toBeVisible();
  const crossSite = await request.post("/api/settings/github", { headers: { Origin: "https://example.com" }, data: { token: "cross-site-fake-token" } });
  expect(crossSite.status()).toBe(403);
  const invalid = await request.post("/api/settings/github", { data: { token: "invalid\nsecret" } });
  expect(invalid.status()).toBe(400);
  expect(await invalid.text()).not.toContain("invalid\nsecret");
  await page.route("**/api/settings/github/test", route => route.fulfill({ json: { ok: true, configured: true, source: "local", limits: { core: { limit: 5000, remaining: 4999 }, search: { limit: 30, remaining: 29 } } } }));
  await section.getByRole("button", { name: "测试 GitHub 连接", exact: true }).click();
  await expect(section.getByText("连接成功 · REST 4999/5000 · Search 29/30", { exact: true })).toBeVisible();
  await section.getByRole("button", { name: "清除已保存 Token", exact: true }).click();
  await expect(section.getByText("未配置 · 使用公开匿名额度", { exact: true })).toBeVisible();
});
