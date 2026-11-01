import { defineConfig } from "@playwright/test";

// Read-only validation against the user's already running local services.
// This config deliberately never starts or replaces an API or test database.
export default defineConfig({
  testDir: "./e2e/live-tests",
  outputDir: "./test-results-live",
  workers: 1,
  fullyParallel: false,
  timeout: 30_000,
  expect: { timeout: 10_000 },
  reporter: [["list"], ["json", { outputFile: "../docs/product-polish-2026-10-23/live-validation/BROWSER_RESULTS.json" }]],
  use: { baseURL: "http://127.0.0.1:5188", screenshot: "only-on-failure", trace: "retain-on-failure" },
  projects: [
    { name: "desktop", use: { viewport: { width: 1280, height: 900 } } },
    { name: "mobile", use: { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true } },
  ],
});
