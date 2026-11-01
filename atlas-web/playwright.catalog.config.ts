import { defineConfig } from "@playwright/test";
export default defineConfig({
  testDir: "./e2e/catalog-tests", workers: 1, fullyParallel: false, timeout: 30_000,
  outputDir: "./test-results-catalog",
  expect: { timeout: 10_000 }, reporter: [["list"]],
  use: { baseURL: "http://127.0.0.1:5228", screenshot: "only-on-failure", trace: "retain-on-failure" },
  webServer: [
    { command: "node e2e/catalog-start-api.mjs", url: "http://127.0.0.1:5229/api/health", reuseExistingServer: false, timeout: 30_000 },
    { command: "npm run dev -- --host 127.0.0.1 --port 5228 --strictPort", url: "http://127.0.0.1:5228", env: { ATLAS_API_TARGET: "http://127.0.0.1:5229" }, reuseExistingServer: false, timeout: 30_000 },
  ],
});
