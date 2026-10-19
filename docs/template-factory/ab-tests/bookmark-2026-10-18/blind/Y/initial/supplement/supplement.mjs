import fs from 'node:fs/promises';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
import http from 'node:http';
const require = createRequire(import.meta.url);
const { chromium } = require('/Users/milin/2026/软件开发/application-atlas/atlas-web/node_modules/@playwright/test');
const args = Object.fromEntries(process.argv.slice(2).reduce((a, x, i, xs) => i % 2 ? a : [...a, [x.slice(2), xs[i + 1]]], []));
const fixture = { url: 'https://example.com/supplement/long-note', title: '长备注完整性核对', note: `生活收藏备注：中文 空格 ' " &\n`.repeat(180) };
const requests = [], events = [];
let browser, proxy;
try {
  proxy = http.createServer((req, res) => { res.writeHead(502); res.end(); });
  proxy.on('connect', (req, socket) => socket.end('HTTP/1.1 502 Bad Gateway\r\nConnection: close\r\n\r\n'));
  await new Promise(resolve => proxy.listen(0, '127.0.0.1', resolve));
  browser = await chromium.launch({ headless: true, proxy: { server: `http://127.0.0.1:${proxy.address().port}`, bypass: '127.0.0.1,localhost' } });
  const context = await browser.newContext({ viewport: { width: 1440, height: 1050 }, locale: 'zh-CN' });
  await context.route('**/*', route => new URL(route.request().url()).origin === args['base-url'] ? route.continue() : route.abort());
  const page = await context.newPage();
  page.on('response', response => {
    const r = response.request();
    if (r.method() !== 'GET') {
      const raw = r.postData();
      let data;
      let encoding;
      try { data = JSON.parse(raw); encoding = 'json'; } catch { data = Object.fromEntries(new URLSearchParams(raw)); encoding = 'form-urlencoded'; }
      // HTML textarea form submission uses CRLF on the wire. Compare the logical
      // LF textarea value, preserve the raw submitted text as evidence as well.
      const logicalNote = encoding === 'form-urlencoded' ? data.note?.replace(/\r\n/g, '\n') : data.note;
      requests.push({ method: r.method(), url: r.url(), status: response.status(), encoding, submittedNote: data.note, logicalSubmittedNote: logicalNote, submittedNoteCodePoints: Array.from(data.note ?? '').length, logicalSubmittedNoteCodePoints: Array.from(logicalNote ?? '').length });
    }
  });
  page.on('pageerror', e => events.push(String(e)));
  const { createAdapter } = await import(pathToFileURL(args.adapter).href);
  const adapter = createAdapter(page, args['base-url']);
  await adapter.ready();
  await adapter.save(fixture);
  await page.reload();
  await adapter.viewCategory('all'); await adapter.search('');
  const records = await adapter.records();
  const found = records.find(r => r.url === fixture.url);
  const sent = requests.find(r => r.logicalSubmittedNote === fixture.note);
  const result = {
    label: args.label, id: 'M02b', kind: 'post-review supplementary exploration, not a new core requirement',
    submitted_full_note_verified: !!sent, expected_note_code_points: Array.from(fixture.note).length,
    actual_note_code_points: found ? Array.from(found.note).length : null,
    outcome: !sent ? 'submission_not_verified' : !found ? 'not_saved_inspect_feedback' : found.note === fixture.note ? 'exact_round_trip' : 'accepted_text_changed',
    fixture, record: found, requests, events, body: await page.locator('body').innerText(),
  };
  await page.screenshot({ path: `${args.evidence}/long-note.png`, fullPage: true });
  await fs.writeFile(`${args.evidence}/result.json`, JSON.stringify(result, null, 2));
  console.log(JSON.stringify({ label: args.label, outcome: result.outcome, submitted: result.expected_note_code_points, readback: result.actual_note_code_points, actual_submission_verified: result.submitted_full_note_verified }));
} finally {
  if (browser) await browser.close();
  if (proxy) await new Promise(resolve => proxy.close(resolve));
}
