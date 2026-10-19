import { spawn } from "node:child_process";
import { copyFileSync, existsSync, mkdirSync, rmSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const webRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const packRoot = path.resolve(webRoot, "../application-atlas-production-pack");
const runtime = path.join(webRoot, ".e2e-runtime");
const sourceDatabase = path.join(packRoot, "atlas", "atlas.sqlite");

if (!existsSync(sourceDatabase)) {
  throw new Error("Missing atlas.sqlite; run export_atlas.py before Playwright tests");
}

rmSync(runtime, { recursive: true, force: true });
mkdirSync(path.join(runtime, "atlas"), { recursive: true });
mkdirSync(path.join(runtime, "drafts"), { recursive: true });
copyFileSync(sourceDatabase, path.join(runtime, "atlas", "atlas.sqlite"));
for (const name of ["mvp_apps.json", "mvp_apps_classified.json"]) {
  copyFileSync(path.join(packRoot, name), path.join(runtime, name));
}
writeFileSync(path.join(runtime, "drafts", "review.json"), "{}\n");
const draftFixture = `---
slug: e2e-draft
name: E2E Draft
name_zh: E2E 草稿
desc: Browser test draft
source: human
status: draft
created: 2026-09-24
engine: test
---
# E2E Draft

## Overview

This draft is created only inside the isolated Playwright runtime.

## How It Works

The browser test saves and deletes this local file.
`;
writeFileSync(path.join(runtime, "drafts", "e2e-draft.md"), draftFixture);
writeFileSync(path.join(runtime, "e2e-draft.fixture.md"), draftFixture);

const child = spawn(process.env.PYTHON || "python3", ["drafts_api.py", "--port", "5199"], {
  cwd: packRoot,
  env: {
    ...process.env,
    ATLAS_PACK: runtime,
    ATLAS_PROJECT_STORE: path.join(runtime, "projects", "atlas-projects.sqlite"),
  },
  stdio: "inherit",
});
let stopping = false;
function stop(signal = "SIGTERM") {
  if (stopping) return;
  stopping = true;
  child.kill(signal);
}
process.on("SIGINT", () => stop("SIGINT"));
process.on("SIGTERM", () => stop("SIGTERM"));
process.on("exit", () => rmSync(runtime, { recursive: true, force: true }));
child.on("exit", (code, signal) => {
  rmSync(runtime, { recursive: true, force: true });
  process.exit(code ?? (signal ? 1 : 0));
});
