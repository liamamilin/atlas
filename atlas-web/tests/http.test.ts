import assert from "node:assert/strict";
import test from "node:test";
import { fetchWithTimeout } from "../src/lib/http.ts";

test("stalled requests time out and do not retry writes", async () => {
  const original = globalThis.fetch;
  let calls = 0;
  globalThis.fetch = async (_url, init) => {
    calls++;
    return new Promise((_resolve, reject) => init?.signal?.addEventListener("abort", () => reject(new DOMException("Aborted", "AbortError"))));
  };
  try {
    await assert.rejects(fetchWithTimeout("/api/test", { method: "POST" }, 5), /Request timed out/);
    assert.equal(calls, 1);
  } finally { globalThis.fetch = original; }
});

test("a proxy HTML error produces an actionable response error", async () => {
  const original = globalThis.fetch;
  globalThis.fetch = async () => new Response("<html>Bad gateway</html>", { status: 502 });
  try { await assert.rejects(fetchWithTimeout("/api/test"), /Invalid service response \(502\)/); }
  finally { globalThis.fetch = original; }
});

test("service errors retain the server's explanation", async () => {
  const original = globalThis.fetch;
  globalThis.fetch = async () => Response.json({ error: "Saved progress retained" }, { status: 503 });
  try { await assert.rejects(fetchWithTimeout("/api/test"), /Saved progress retained/); }
  finally { globalThis.fetch = original; }
});
