import { expect, test, type Page } from "@playwright/test";

// The model is not available in the isolated suite, so the assistant API is
// simulated; the backend loop and its safety rules have their own unit tests.
async function fakeAssistant(page: Page, opts: { destructive?: boolean } = {}) {
  const action = opts.destructive
    ? { id: "act_0123456789abcdef", method: "DELETE", path: "/api/projects/prj_demo", query: "", body: {}, summary: "删除项目在 Atlas 的记录（不删除本地源码）", risk: "destructive", confirm_text: "prj_demo" }
    : { id: "act_0123456789abcdef", method: "POST", path: "/api/oss/projects/7/favorite", query: "", body: { favorite: true }, summary: "收藏或取消收藏开源项目", risk: "write" };
  const thread = { id: "ast_" + "0".repeat(32), title: "", updated_at: "", running: false, pending: null as unknown, messages: [] as unknown[] };
  const decisions: unknown[] = [];
  await page.route("**/api/assistant/threads**", async route => {
    const request = route.request();
    const url = new URL(request.url());
    if (request.method() === "POST" && url.pathname.endsWith("/messages")) {
      const { content } = request.postDataJSON();
      thread.messages.push({ id: "m1", role: "user", content, created_at: "" });
      thread.messages.push({ id: "m2", role: "assistant", content: "准备好了，请确认。", created_at: "", status: "awaiting_confirmation", steps: [{ index: 1, tool: "call_api", summary: `${action.method} ${action.path} · 等待确认`, error: false }] });
      thread.pending = action;
      return route.fulfill({ status: 202, json: { status: "running" } });
    }
    if (request.method() === "POST" && url.pathname.includes("/actions/")) {
      const body = request.postDataJSON();
      decisions.push(body);
      thread.pending = null;
      thread.messages.push({ id: "m3", role: "action", created_at: "", action, decision: body.decision, outcome: { status: 200, ok: true, result: {} } });
      thread.messages.push({ id: "m4", role: "assistant", content: "已完成。", created_at: "", status: "completed", steps: [], navigate: "/settings" });
      return route.fulfill({ json: { status: "running", outcome: { status: 200, ok: true, result: {} } } });
    }
    if (request.method() === "POST") return route.fulfill({ status: 201, json: thread });
    return route.fulfill({ json: thread });
  });
  return decisions;
}

test("assistant proposes a change, waits for approval and opens the page it names", async ({ page }) => {
  const decisions = await fakeAssistant(page);
  await page.goto("/discover");
  await page.getByRole("button", { name: "打开应用助手" }).click();
  const panel = page.getByRole("dialog", { name: "应用助手" });
  await panel.getByRole("textbox", { name: "给助手的消息" }).fill("收藏第 7 个项目");
  await panel.getByRole("textbox", { name: "给助手的消息" }).press("Enter");
  const card = panel.getByRole("region", { name: "待确认的操作" });
  await expect(card).toContainText("POST /api/oss/projects/7/favorite");
  await card.getByRole("button", { name: "执行" }).click();
  await expect(panel).toContainText("已执行：收藏或取消收藏开源项目");
  expect(decisions).toEqual([{ decision: "approve" }]);
  await expect(page).toHaveURL(/\/settings$/);
  await page.keyboard.press("Escape");
  await expect(panel).toBeHidden();
});

test("destructive actions stay disabled until the confirmation text is typed", async ({ page }) => {
  const decisions = await fakeAssistant(page, { destructive: true });
  await page.goto("/");
  await page.keyboard.press("ControlOrMeta+k");
  const panel = page.getByRole("dialog", { name: "应用助手" });
  await panel.getByRole("textbox", { name: "给助手的消息" }).fill("删除 demo 项目");
  await panel.getByRole("button", { name: "发送" }).click();
  const card = panel.getByRole("region", { name: "待确认的操作" });
  const run = card.getByRole("button", { name: "执行" });
  await expect(run).toBeDisabled();
  await card.getByRole("textbox").fill("prj_wrong");
  await expect(run).toBeDisabled();
  await card.getByRole("textbox").fill("prj_demo");
  await run.click();
  expect(decisions).toEqual([{ decision: "approve", typed: "prj_demo" }]);
});
