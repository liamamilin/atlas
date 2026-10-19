const { chromium } = require(process.env.PLAYWRIGHT_MODULE);
(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: process.env.PLAYWRIGHT_EXECUTABLE,
  });
  try {
    const allowedOrigins = new Set([process.env.APP_URL, process.env.FIXTURE_URL].map(value => new URL(value).origin));
    const blockedRequests = [];
    const context = await browser.newContext({ serviceWorkers: 'block' });
    await context.route('**/*', async route => {
      const url = route.request().url();
      if (allowedOrigins.has(new URL(url).origin)) return route.continue();
      blockedRequests.push(url);
      return route.abort('blockedbyclient');
    });
    const page = await context.newPage();
    const response = await page.goto(process.env.APP_URL, { waitUntil: 'domcontentloaded', timeout: 15000 });
    if (response.status() !== 200 || await page.locator('h1').innerText() !== 'Synthetic bookmark probe') {
      throw new Error(`unexpected app page response=${response.status()}`);
    }
    await page.locator('#original').click();
    if (new URL(page.url()).origin !== new URL(process.env.FIXTURE_URL).origin ||
        await page.locator('h1').innerText() !== 'Local original fixture page') {
      throw new Error(`did not reach fixture page: ${page.url()}`);
    }
    const fixturePageUrl = page.url();
    await page.goBack();
    const post = await page.evaluate(async () => {
      const response = await fetch('/persist', { method: 'POST', body: 'chromium-persist-check' });
      return response.status;
    });
    if (post !== 201) throw new Error(`persist request status ${post}`);
    let externalBlocked = false;
    try {
      await page.goto('https://example.com/', { waitUntil: 'domcontentloaded', timeout: 3000 });
    } catch (error) {
      externalBlocked = blockedRequests.some(url => url.startsWith('https://example.com/'));
    }
    if (!externalBlocked) throw new Error('browser did not prove external request blocking');
    process.stdout.write(JSON.stringify({
      appStatus: response.status(),
      appUrl: process.env.APP_URL,
      fixtureUrl: fixturePageUrl,
      fixtureReached: true,
      postStatus: post,
      externalRequestBlocked: externalBlocked,
      blockedRequests,
      chromiumVersion: browser.version(),
    }));
    await context.close();
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exit(1); });
