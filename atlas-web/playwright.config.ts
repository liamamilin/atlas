import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e/tests",
  fullyParallel: false,
  workers: 1,
  timeout: 30_000,
  expect: { timeout: 7_500 },
  reporter: [["list"]],
  use: {
    baseURL: "http://127.0.0.1:5188",
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
  },
  webServer: [
    {
      command: "node e2e/start-api.mjs",
      url: "http://127.0.0.1:5199/api/health",
      reuseExistingServer: false,
      timeout: 30_000,
    },
    {
      command: "npm run dev -- --host 127.0.0.1",
      url: "http://127.0.0.1:5188",
      env: { ATLAS_API_TARGET: "http://127.0.0.1:5199" },
      reuseExistingServer: false,
      timeout: 30_000,
    },
  ],
});
