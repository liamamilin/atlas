import { expect, test } from "@playwright/test";

test("a late history response cannot replace the conversation selected later", async ({ page }) => {
  let markAStarted!: () => void;
  const aStarted = new Promise<void>((resolve) => { markAStarted = resolve; });
  let releaseA!: () => void;
  const aGate = new Promise<void>((resolve) => { releaseA = resolve; });

  await page.route("**/api/ask/threads", async (route) => {
    if (route.request().method() !== "GET") {
      await route.fulfill({ status: 405, body: "Not used by this test" });
      return;
    }
    await route.fulfill({
      contentType: "application/json",
      body: JSON.stringify([
        { id: "thread-a", title: "Older conversation A", created_at: "", updated_at: "", message_count: 1, running: false, excerpt: "" },
        { id: "thread-b", title: "Selected conversation B", created_at: "", updated_at: "", message_count: 1, running: false, excerpt: "" },
      ]),
    });
  });
  await page.route("**/api/ask/threads/*", async (route) => {
    const id = new URL(route.request().url()).pathname.split("/").at(-1);
    if (id === "thread-a") {
      markAStarted();
      await aGate;
    }
    const title = id === "thread-a" ? "Older conversation A" : "Selected conversation B";
    await route.fulfill({
      contentType: "application/json",
      body: JSON.stringify({
        id,
        title,
        created_at: "",
        updated_at: "",
        running: false,
        model: { configured: true, provider: null, model: null, reason: null },
        messages: [{ id: `message-${id}`, role: "assistant", content: title, created_at: "", status: "completed" }],
      }),
    });
  });

  await page.goto("/ask");
  await expect(page.getByRole("button", { name: /历史/ })).toBeVisible();
  await page.getByRole("button", { name: /历史/ }).click();
  await expect(page.getByRole("button", { name: /Older conversation A/ })).toBeVisible();
  await page.getByRole("button", { name: /Older conversation A/ }).click();
  await aStarted;
  await page.getByRole("button", { name: /历史/ }).click();
  await page.getByRole("button", { name: /Selected conversation B/ }).click();

  await expect(page.getByText("Selected conversation B", { exact: true })).toBeVisible();
  const lateAResponse = page.waitForResponse((response) =>
    response.url().endsWith("/api/ask/threads/thread-a"));
  releaseA();
  await lateAResponse;
  await expect(page.getByText("Selected conversation B", { exact: true })).toBeVisible();
  await expect(page.getByText("Older conversation A", { exact: true })).toHaveCount(0);
});

for (const action of ["reopen", "failed-new"] as const) {
  test(`running conversation keeps polling after ${action}`, async ({ page }) => {
    let complete = false;
    const summary = { id: "running-thread", title: "In progress", created_at: "", updated_at: "", message_count: 1, running: true, excerpt: "" };
    await page.route("**/api/ask/threads", route => route.request().method() === "POST"
      ? route.fulfill({ status: 503, json: { error: "New conversation unavailable" } })
      : route.fulfill({ json: [summary] }));
    await page.route("**/api/ask/threads/running-thread", route => route.fulfill({ json: {
      ...summary, running: !complete,
      model: { configured: true, provider: null, model: null, reason: null },
      messages: [{ id: "answer", role: "assistant", content: complete ? "Completed answer" : "Still working", created_at: "", status: complete ? "completed" : "pending" }],
    } }));
    await page.goto("/ask");
    await page.getByRole("button", { name: /历史/ }).click();
    await page.getByRole("button", { name: /In progress/ }).click();
    await expect(page.getByText("Still working", { exact: true })).toBeVisible();
    if (action === "reopen") {
      await page.getByRole("button", { name: /历史/ }).click();
      await page.getByRole("button", { name: /In progress/ }).click();
    } else {
      await page.getByRole("button", { name: "新对话", exact: true }).click();
      await expect(page.getByRole("alert")).toContainText("New conversation unavailable");
    }
    complete = true;
    await expect(page.getByText("Completed answer", { exact: true })).toBeVisible();
    await expect(page.getByText("Still working", { exact: true })).toHaveCount(0);
  });
}
