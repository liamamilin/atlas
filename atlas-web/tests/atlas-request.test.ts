import assert from "node:assert/strict";
import test from "node:test";
import {
  AtlasApiError,
  backfillLegacyAcceptance,
  getLegacyAcceptanceMigration,
  listProjectGenerations,
  reconcileProjectExecution,
} from "../src/lib/atlas.ts";

test("execution polling reconciles through an explicit JSON POST", async () => {
  const originalFetch = globalThis.fetch;
  let requestUrl = "";
  let requestInit: RequestInit | undefined;
  globalThis.fetch = async (input, init) => {
    requestUrl = String(input);
    requestInit = init;
    return new Response(JSON.stringify({
      id: "exe_test",
      task_id: "tsk_test",
      status: "completed",
    }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  };
  try {
    const execution = await reconcileProjectExecution("prj_test", "exe_test");
    assert.equal(execution.status, "completed");
    assert.equal(
      requestUrl,
      "/api/projects/prj_test/executions/exe_test/reconcile",
    );
    assert.equal(requestInit?.method, "POST");
    assert.deepEqual(requestInit?.headers, {
      "Content-Type": "application/json",
    });
    assert.equal(requestInit?.body, "{}");
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("legacy acceptance migration is read-only until explicit backfill", async () => {
  const originalFetch = globalThis.fetch;
  const requests: Array<{ url: string; init?: RequestInit }> = [];
  globalThis.fetch = async (input, init) => {
    requests.push({ url: String(input), init });
    return new Response(JSON.stringify({
      schema: 1,
      project_id: "prj_test",
      dry_run: true,
      generated_at: "2026-09-25T00:00:00Z",
      summary: {
        total_bindings: 1, complete: 0, not_backfilled: 1, backfilled: 0,
        needs_review: 0, no_conditions: 0, invalid: 0,
      },
      records: [],
      backfilled_task_ids: [],
    }), { status: 200, headers: { "Content-Type": "application/json" } });
  };
  try {
    const report = await getLegacyAcceptanceMigration("prj_test");
    assert.equal(report.summary.not_backfilled, 1);
    assert.equal(requests[0].url, "/api/projects/prj_test/acceptance-migration");
    const migrated = await backfillLegacyAcceptance("prj_test");
    assert.deepEqual(migrated.backfilled_task_ids, []);
    assert.equal(requests[1].url, "/api/projects/prj_test/acceptance-migration/backfill");
    assert.equal(requests[1].init?.method, "POST");
    assert.equal(requests[1].init?.body, JSON.stringify({
      confirm: "backfill_legacy_acceptance_metadata",
    }));
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("API errors expose stable code and retryability", async () => {
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async () => new Response(JSON.stringify({
    error: "provider is unavailable",
    code: "provider_unavailable",
    retryable: true,
    details: {},
  }), { status: 503, headers: { "Content-Type": "application/json" } });
  try {
    await assert.rejects(
      getLegacyAcceptanceMigration("prj_error"),
      (error: unknown) => error instanceof AtlasApiError
        && error.code === "provider_unavailable"
        && error.retryable === true,
    );
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("generation list bypasses the shared read cache", async () => {
  const originalFetch = globalThis.fetch;
  let requestInit: RequestInit | undefined;
  globalThis.fetch = async (_input, init) => {
    requestInit = init;
    return new Response(JSON.stringify([]), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  };
  try {
    await listProjectGenerations("prj_test");
    assert.equal(requestInit?.cache, "no-store");
  } finally {
    globalThis.fetch = originalFetch;
  }
});
