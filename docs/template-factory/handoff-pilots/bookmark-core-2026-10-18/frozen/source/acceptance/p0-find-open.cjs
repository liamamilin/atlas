'use strict';

/*
 * acceptance/p0-find-open.cjs — P0 检索、浏览、打开与本地私有行为组（require ./common.cjs）。
 *
 * 覆盖：
 * A05 记录跨分类移动后重载归属更新（正）；
 * A06 分类浏览仅含该分类且按添加时间倒序（正）；
 * A07 关键字命中标题/URL/备注/分类名且无无关结果（正）；
 * A08 空库提示与检索无匹配提示互不相同（负）；
 * A09 点击 record-open 在新标签打开原始 URL 且保留 query 与 fragment（正，经 installNetworkPolicy 拦截外连）；
 * A17 仅回环可达、除显式点击打开原页外无后台外发、认证仅作用于显式目标且不支持模式显式失败（负）。
 *
 * 约束：只与真实目标 UI 交互，不启动应用、不 mock、不用文件存在性或内部 API 代替用户行为；
 * 断言失败即抛出，runCases 汇总后进程退出码非零；不硬编码任何已知夹具值。
 */

const nodeNet = require('node:net');
const nodeOs = require('node:os');

const common = require('./common.cjs');

const openApp = common.openApp;
const saveBookmark = common.saveBookmark;
const createCategory = common.createCategory;
const moveRecord = common.moveRecord;
const search = common.search;
const readRecords = common.readRecords;
const resolveControls = common.resolveControls;
const scopedLocator = common.scopedLocator;
const expectVisible = common.expectVisible;
const waitFor = common.waitFor;
const assert = common.assert;
const AssertionError = common.AssertionError;
const getNetworkPolicy = common.getNetworkPolicy;
const applyTargetCredentials = common.applyTargetCredentials;
const runCases = common.runCases;
const loadConfig = common.loadConfig;

let sequence = 0;

function nonce(label) {
  sequence += 1;
  return String(label || 'case') + '-' + Date.now().toString(36) + '-' + sequence + '-' + Math.random().toString(36).slice(2, 8);
}

function delay(ms) {
  return new Promise(function (resolve) { setTimeout(resolve, ms); });
}

function uniqueUrl(label) {
  return 'https://bookmarks.example.com/' + nonce(label || 'item');
}

function isLoopbackHost(host) {
  const text = String(host || '');
  if (text === 'localhost' || text === '::1' || text === '[::1]') return true;
  return text.startsWith('127.');
}

function normalizeUrl(value) {
  try {
    const parsed = new URL(String(value));
    return parsed.origin + parsed.pathname + parsed.search + parsed.hash;
  } catch (error) {
    return null;
  }
}

function sameUrl(a, b) {
  const left = normalizeUrl(a);
  const right = normalizeUrl(b);
  return left !== null && left === right;
}

/* 网络请求 URL 不含 fragment（浏览器不发送），因此比较 origin/path/query。 */
function sameRequestTarget(a, b) {
  try {
    const left = new URL(String(a));
    const right = new URL(String(b));
    return left.origin === right.origin && left.pathname === right.pathname && left.search === right.search;
  } catch (error) {
    return false;
  }
}

async function safeCount(locator) {
  try {
    return await locator.count();
  } catch (error) {
    return 0;
  }
}

/* 读取状态标记文案：优先可见文本，隐藏容器用 textContent 兜底；都无法解析时返回 null。 */
async function readStateMarker(locator) {
  const count = await safeCount(locator);
  for (let i = 0; i < count; i += 1) {
    const node = locator.nth(i);
    const inner = (await node.innerText().catch(function () { return ''; })).trim();
    if (inner) return inner;
    const content = (await node.textContent().catch(function () { return ''; })).trim();
    if (content) return content;
  }
  return null;
}

function recordBlob(record) {
  return [record && record.title, record && record.url, record && record.category, record && record.text]
    .filter(function (item) { return item !== null && item !== undefined && String(item) !== ''; })
    .join(' ');
}

function findRecordIndex(records, url) {
  for (let i = 0; i < records.length; i += 1) {
    if (sameUrl(records[i].url, url)) return i;
  }
  return -1;
}

function hasRecord(records, url) {
  return findRecordIndex(records, url) >= 0;
}

async function categoryVisible(controls, name) {
  const target = String(name).trim();
  const items = controls.categoryItem;
  const count = await safeCount(items);
  for (let i = 0; i < count; i += 1) {
    const text = ((await items.nth(i).innerText().catch(function () { return ''; })) || '').trim();
    if (text === target || text.indexOf(target) >= 0) return true;
  }
  const select = controls.saveCategorySelect;
  if ((await safeCount(select)) > 0) {
    const options = await select.first().locator('option').allTextContents().catch(function () { return []; });
    if (options.some(function (text) { return text.trim() === target; })) return true;
  }
  return false;
}

/* 确保分类存在：优先专用分类创建入口；否则经保存流程的“新建分类”入口创建（不新增 mock）。 */
async function ensureCategory(page, config, name) {
  const controls = resolveControls(page, config.uiSelectors);
  const target = String(name).trim();
  const hasDedicated = (await safeCount(controls.categoryCreateInput)) > 0 && (await safeCount(controls.categoryCreateSubmit)) > 0;
  if (hasDedicated) {
    await createCategory(page, target, config);
    await waitFor(function () { return categoryVisible(controls, target); }, { timeout: config.timeout, message: '分类应出现：' + target });
    return { name: target, seedUrl: null };
  }
  const seedUrl = uniqueUrl('seed');
  const seed = await saveBookmark(page, { url: seedUrl, title: '建立分类' + nonce('s'), categoryName: target }, config);
  assert(seed.saved === true && !seed.error, '通过保存流程创建分类应成功：' + target + '；' + String(seed.error));
  await waitFor(function () { return categoryVisible(controls, target); }, { timeout: config.timeout, message: '分类应出现：' + target });
  return { name: target, seedUrl: seedUrl };
}

/* 点击分类项进入该分类浏览（语义控件 category-item，不依赖模板专用 testid）。 */
async function browseCategory(page, config, name) {
  const controls = resolveControls(page, config.uiSelectors);
  const items = controls.categoryItem;
  const target = String(name).trim();
  await waitFor(async function () {
    const count = await safeCount(items);
    for (let i = 0; i < count; i += 1) {
      const text = ((await items.nth(i).innerText().catch(function () { return ''; })) || '').trim();
      if (text === target || text.indexOf(target) >= 0) return true;
    }
    return false;
  }, { timeout: config.timeout, message: '分类列表应包含可用于浏览的分类：' + target });
  const count = await safeCount(items);
  for (let i = 0; i < count; i += 1) {
    const item = items.nth(i);
    const text = ((await item.innerText().catch(function () { return ''; })) || '').trim();
    if (text === target || text.indexOf(target) >= 0) {
      await expectVisible(item, '分类浏览入口：' + target);
      await item.click({ noWaitAfter: true });
      await page.waitForLoadState('load', { timeout: config.timeout }).catch(function () {});
      return i;
    }
  }
  throw new AssertionError('分类列表中未找到分类用于浏览：' + target);
}

async function waitForIndexByUrl(page, config, url, message) {
  return waitFor(async function () {
    const records = await readRecords(page, config);
    const index = findRecordIndex(records, url);
    return index >= 0 ? { index: index } : false;
  }, { timeout: config.timeout, message: message || ('记录应出现：' + url) });
}

async function findCardByUrl(page, config, url) {
  const controls = resolveControls(page, config.uiSelectors);
  const cards = controls.recordCard;
  const total = await safeCount(cards);
  for (let i = 0; i < total; i += 1) {
    const card = cards.nth(i);
    const links = scopedLocator(card, 'recordOpen', config.uiSelectors);
    const linkCount = await safeCount(links);
    for (let j = 0; j < linkCount; j += 1) {
      const href = await links.nth(j).getAttribute('href').catch(function () { return null; });
      if (href && sameUrl(href, url)) return { card: card, link: links.nth(j) };
    }
    const dataUrl = await card.getAttribute('data-url').catch(function () { return null; });
    if (dataUrl && sameUrl(dataUrl, url)) return { card: card, link: null };
  }
  return null;
}

/* 检索后只允许出现 allowedUrls 命中的记录，且绝不出现 decoyUrl。 */
async function assertSearchOnly(page, config, term, allowedUrls, decoyUrl) {
  await search(page, term, config);
  await waitFor(async function () {
    const records = await readRecords(page, config);
    return records.some(function (record) {
      return allowedUrls.some(function (url) { return sameUrl(record.url, url); });
    }) ? true : false;
  }, { timeout: config.timeout, message: '检索应命中：' + term });
  const records = await readRecords(page, config);
  for (let i = 0; i < records.length; i += 1) {
    const record = records[i];
    const allowed = allowedUrls.some(function (url) { return sameUrl(record.url, url); });
    assert(allowed, '检索“' + term + '”返回了无关记录：' + recordBlob(record));
  }
  assert(!records.some(function (record) { return sameUrl(record.url, decoyUrl); }), '检索“' + term + '”不应命中无关记录：' + decoyUrl);
}

function nonLoopbackIpv4() {
  const out = [];
  const interfaces = nodeOs.networkInterfaces();
  for (const name of Object.keys(interfaces)) {
    const entries = interfaces[name] || [];
    for (const info of entries) {
      if (info && info.family === 'IPv4' && !info.internal && !isLoopbackHost(info.address)) out.push(info.address);
    }
  }
  return out;
}

/* 仅用于判定“是否在非回环地址可达”：正确绑定回环时连接应被拒绝。 */
function canConnect(address, port, timeoutMs) {
  return new Promise(function (resolve) {
    const socket = nodeNet.connect({ host: address, port: port });
    let settled = false;
    const finish = function (value) {
      if (settled) return;
      settled = true;
      socket.destroy();
      resolve(value);
    };
    socket.setTimeout(timeoutMs || 1000);
    socket.once('connect', function () { finish(true); });
    socket.once('timeout', function () { finish(false); });
    socket.once('error', function () { finish(false); });
  });
}

const cases = [
  {
    id: 'A05',
    name: '记录跨分类移动后重载归属更新（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const catA = '移动源' + nonce('c');
      const catB = '移动目标' + nonce('c');
      await ensureCategory(page, config, catA);
      await ensureCategory(page, config, catB);
      await openApp(page, config);
      const url = uniqueUrl('a05');
      const saved = await saveBookmark(page, { url: url, title: '待移动记录' + nonce('t'), categoryName: catA }, config);
      assert(saved.saved === true && !saved.error, 'A05 保存到源分类应成功：' + String(saved.error));
      await browseCategory(page, config, catA);
      const found = await waitForIndexByUrl(page, config, url, 'A05 源分类中应出现该记录：' + url);
      await moveRecord(page, found.index, catB, config);
      await openApp(page, config);
      await browseCategory(page, config, catB);
      await waitForIndexByUrl(page, config, url, 'A05 重载后目标分类应包含该记录：' + url);
      await browseCategory(page, config, catA);
      await waitFor(async function () {
        const records = await readRecords(page, config);
        return hasRecord(records, url) ? false : true;
      }, { timeout: config.timeout, message: 'A05 重载后原分类不应再包含该记录：' + url });
    },
  },
  {
    id: 'A06',
    name: '分类浏览仅含该分类且按添加时间倒序（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const catA = '浏览分类' + nonce('c');
      const catB = '其他分类' + nonce('c');
      await ensureCategory(page, config, catA);
      await ensureCategory(page, config, catB);
      await openApp(page, config);
      const url1 = uniqueUrl('a06-first');
      const url2 = uniqueUrl('a06-second');
      const urlOther1 = uniqueUrl('a06-other1');
      const urlOther2 = uniqueUrl('a06-other2');
      let result = await saveBookmark(page, { url: url1, title: '较早记录' + nonce('t'), categoryName: catA }, config);
      assert(result.saved === true && !result.error, 'A06 保存第一条应成功：' + String(result.error));
      await delay(1100);
      result = await saveBookmark(page, { url: url2, title: '较新记录' + nonce('t'), categoryName: catA }, config);
      assert(result.saved === true && !result.error, 'A06 保存第二条应成功：' + String(result.error));
      result = await saveBookmark(page, { url: urlOther1, title: '别的分类' + nonce('t'), categoryName: catB }, config);
      assert(result.saved === true && !result.error, 'A06 保存其他分类第一条应成功：' + String(result.error));
      result = await saveBookmark(page, { url: urlOther2, title: '别的分类' + nonce('t'), categoryName: catB }, config);
      assert(result.saved === true && !result.error, 'A06 保存其他分类第二条应成功：' + String(result.error));
      await browseCategory(page, config, catA);
      await waitForIndexByUrl(page, config, url1, 'A06 分类浏览应包含第一条：' + url1);
      await waitForIndexByUrl(page, config, url2, 'A06 分类浏览应包含第二条：' + url2);
      const records = await readRecords(page, config);
      assert(!hasRecord(records, urlOther1) && !hasRecord(records, urlOther2), 'A06 分类浏览不得包含其他分类的记录');
      const indexNew = findRecordIndex(records, url2);
      const indexOld = findRecordIndex(records, url1);
      assert(indexNew >= 0 && indexOld >= 0, 'A06 两条目标记录都应出现在分类浏览中');
      assert(indexNew < indexOld, 'A06 默认应按添加时间倒序（新在前）：新记录 index=' + indexNew + ' 应小于旧记录 index=' + indexOld);
    },
  },
  {
    id: 'A07',
    name: '关键字命中标题/URL/备注/分类名且无无关结果（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const base = 'fd' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
      const titleToken = base + 'T';
      const urlToken = base + 'U';
      const noteToken = base + 'N';
      const catToken = base + 'C';
      const decoyToken = base + 'X';
      const titleUrl = uniqueUrl('a07-title');
      const urlUrl = 'https://bookmarks.example.com/' + urlToken;
      const noteUrl = uniqueUrl('a07-note');
      const catUrl = uniqueUrl('a07-cat');
      const decoyUrl = uniqueUrl('a07-decoy');
      const catName = '检索分类' + catToken;
      const cat = await ensureCategory(page, config, catName);
      await openApp(page, config);
      let result = await saveBookmark(page, { url: titleUrl, title: '标题命中' + titleToken }, config);
      assert(result.saved === true && !result.error, 'A07 保存标题命中记录应成功：' + String(result.error));
      result = await saveBookmark(page, { url: urlUrl, title: 'URL命中记录' + nonce('t') }, config);
      assert(result.saved === true && !result.error, 'A07 保存 URL 命中记录应成功：' + String(result.error));
      result = await saveBookmark(page, { url: noteUrl, title: '备注命中记录' + nonce('t'), note: '备注内容' + noteToken }, config);
      assert(result.saved === true && !result.error, 'A07 保存备注命中记录应成功：' + String(result.error));
      result = await saveBookmark(page, { url: catUrl, title: '分类命中记录' + nonce('t'), categoryName: catName }, config);
      assert(result.saved === true && !result.error, 'A07 保存分类命中记录应成功：' + String(result.error));
      result = await saveBookmark(page, { url: decoyUrl, title: '无关记录' + decoyToken }, config);
      assert(result.saved === true && !result.error, 'A07 保存无关记录应成功：' + String(result.error));
      const catAllowed = [catUrl];
      if (cat.seedUrl) catAllowed.push(cat.seedUrl);
      await assertSearchOnly(page, config, titleToken, [titleUrl], decoyUrl);
      await assertSearchOnly(page, config, urlToken, [urlUrl], decoyUrl);
      await assertSearchOnly(page, config, noteToken, [noteUrl], decoyUrl);
      await assertSearchOnly(page, config, catToken, catAllowed, decoyUrl);
    },
  },
  {
    id: 'A08',
    name: '空库提示与检索无匹配提示互不相同（负）',
    type: 'negative',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const controls = resolveControls(page, config.uiSelectors);
      const emptyText = await readStateMarker(controls.emptyLibrary);
      assert(emptyText !== null, '[incomplete] 未能解析空库提示（empty-library）；请提供可解析标记用于与检索无匹配提示对比。');
      const restMatch = await readStateMarker(controls.noSearchMatch);
      if (restMatch !== null) {
        assert(restMatch !== emptyText, 'A08 空库提示与检索无匹配提示必须互为不同文案，实际相同：' + emptyText);
      }
      const seed = await saveBookmark(page, { url: uniqueUrl('a08'), title: '建立非空库' + nonce('t') }, config);
      assert(seed.saved === true && !seed.error, 'A08 建立非空库应成功：' + String(seed.error));
      const term = '无匹配检索' + nonce('q');
      await search(page, term, config);
      const shown = await waitFor(async function () {
        const text = await readStateMarker(controls.noSearchMatch);
        return text ? text : false;
      }, { timeout: config.timeout, message: 'A08 检索无匹配时应显示对应提示：' + term });
      assert(shown !== emptyText, 'A08 检索无匹配时不得复用空库提示文案，实际：' + shown);
      const emptyAfter = await readStateMarker(controls.emptyLibrary);
      if (emptyAfter !== null) {
        assert(emptyAfter !== shown, 'A08 空库提示与检索无匹配提示不得混为一谈：' + shown);
      }
    },
  },
  {
    id: 'A09',
    name: '点击记录在新标签打开原始 URL 且保留 query 与 fragment（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const browserContext = context.context;
      const config = context.config;
      await openApp(page, config);
      const policy = getNetworkPolicy(page);
      assert(policy, '[incomplete] 需要 installNetworkPolicy 网络守卫以拦截外连并捕获被尝试打开的 URL。');
      const token = nonce('a09');
      const url = 'https://bookmarks.example.com/page/' + token + '?q=' + token + '&ref=atlas#frag-' + token;
      const saved = await saveBookmark(page, { url: url, title: '打开原页' + nonce('t') }, config);
      assert(saved.saved === true && !saved.error, 'A09 保存记录应成功：' + String(saved.error));
      const found = await waitFor(async function () {
        return (await findCardByUrl(page, config, url)) || false;
      }, { timeout: config.timeout, message: 'A09 记录应出现：' + url });
      const openLink = found.link || scopedLocator(found.card, 'recordOpen', config.uiSelectors).first();
      await expectVisible(openLink, 'A09 记录打开链接');
      const href = await openLink.getAttribute('href');
      assert(href !== null && href !== undefined && String(href) !== '', 'A09 record-open 应包含指向原始 URL 的 href');
      assert(sameUrl(href, url), 'A09 record-open 的 href 必须保留原始 URL（含 query 与 fragment）：' + href + ' 期望 ' + url);
      const targetAttr = await openLink.getAttribute('target');
      policy.reset();
      const popupPromise = browserContext.waitForEvent('page', { timeout: config.timeout }).catch(function () { return null; });
      await openLink.click({ noWaitAfter: true });
      const popup = await popupPromise;
      assert(popup, 'A09 点击记录应在新标签/新页面打开原始 URL');
      await waitFor(function () {
        return policy.attemptedOpens.some(function (candidate) { return sameRequestTarget(candidate, url); }) ? true : false;
      }, { timeout: config.timeout, message: 'A09 应尝试打开原始 URL（含 query）：' + url });
      const attempted = policy.takeAttemptedOpens();
      assert(attempted.some(function (candidate) { return sameRequestTarget(candidate, url); }), 'A09 被尝试打开的 URL 应匹配原始 URL 的 origin/path/query');
      policy.assertNoBackgroundOutbound();
      assert(targetAttr === null || targetAttr === undefined || String(targetAttr).toLowerCase() === '_blank' || Boolean(popup), 'A09 记录应在新的标签页打开原页');
      await popup.close().catch(function () {});
    },
  },
  {
    id: 'A17',
    name: '仅回环可达、无后台外发且认证仅作用于显式目标（负）',
    type: 'negative',
    async run(context) {
      const page = context.page;
      const browserContext = context.context;
      const config = context.config;
      const policy = getNetworkPolicy(page);
      assert(policy, '[incomplete] 需要 installNetworkPolicy 网络守卫。');
      const target = new URL(config.targetUrl);
      assert(isLoopbackHost(target.hostname), 'A17 目标必须通过回环地址访问，实际主机：' + target.hostname);
      await openApp(page, config);
      assert(isLoopbackHost(new URL(page.url()).hostname), 'A17 应用页面必须位于回环地址，实际：' + page.url());
      const port = target.port ? Number(target.port) : target.protocol === 'https:' ? 443 : 80;
      const addresses = nonLoopbackIpv4();
      const reachable = [];
      for (let i = 0; i < addresses.length; i += 1) {
        if (await canConnect(addresses[i], port, 1200)) reachable.push(addresses[i]);
      }
      assert(reachable.length === 0, 'A17 应用只能绑定回环地址，却在非回环地址可达：' + reachable.join(', '));
      const token = nonce('a17');
      const url = 'https://bookmarks.example.com/' + token;
      const saved = await saveBookmark(page, { url: url, title: '本地私有' + token, note: '私有备注' + token }, config);
      assert(saved.saved === true && !saved.error, 'A17 保存应成功：' + String(saved.error));
      await search(page, token, config);
      await openApp(page, config);
      policy.assertNoBackgroundOutbound();
      let failure = null;
      try {
        applyTargetCredentials(browserContext, { auth: { user: 'probe-user', pass: 'probe-secret', scheme: 'digest' }, targetOrigin: config.targetOrigin, targetUrl: config.targetUrl });
      } catch (error) {
        failure = error;
      }
      assert(failure !== null && failure !== undefined && failure.name === 'InfrastructureError', 'A17 不支持的认证模式必须显式失败为基础设施/不完整，实际：' + String(failure && failure.name));
      if (config.auth) {
        const body = await page.locator('body').innerText().catch(function () { return ''; });
        assert(body.indexOf(config.auth.pass) < 0, 'A17 凭据值不得出现在页面内容中');
        assert(body.indexOf(config.auth.user) < 0, 'A17 凭据用户名不得出现在页面内容中');
      }
      const attempted = policy.takeAttemptedOpens();
      for (let i = 0; i < attempted.length; i += 1) {
        let parsed = null;
        try { parsed = new URL(attempted[i]); } catch (error) { parsed = null; }
        if (parsed) assert(parsed.username === '' && parsed.password === '', 'A17 不得把凭据附加到外部导航：' + attempted[i]);
      }
      policy.assertNoBackgroundOutbound();
    },
  },
];

async function main() {
  let config;
  try {
    config = loadConfig();
  } catch (error) {
    console.error('[FAIL] 配置错误：' + (error && error.message ? error.message : String(error)));
    process.exitCode = 1;
    return;
  }
  try {
    await runCases(cases, { config: config });
  } catch (error) {
    console.error('[FAIL] 运行失败：' + (error && error.stack ? error.stack : String(error)));
    process.exitCode = 1;
  }
}

if (require.main === module) {
  main();
}

module.exports = { cases: cases };
module.exports.cases = cases;
