'use strict';

/*
 * acceptance/common.cjs — 共享配置、断言、UI 适配器、网络守卫与重启控制辅助（Node 18+ CommonJS）。
 *
 * 设计约束：
 * - 只依赖可访问角色与中文可见标签解析控件；UI_SELECTORS(JSON) 可覆盖默认建议选择器，
 *   语义等价的 UI 无需模板专用 data-testid 即可通过。
 * - 仅与显式配置的真实目标交互；缺少 TARGET_URL 时显式失败，绝不猜测地址。
 * - 网络守卫拦截并中止对非目标地址的真实连接；后台外发请求（元数据抓取/遥测）记录为违规供 A17 判定，
 *   用户显式点击打开原页导致的文档导航记录为 attemptedOpens 供 A09 判定。
 * - 认证只注入到显式配置的目标来源，绝不附加到外部导航或夹具，且不打印凭据值；
 *   不支持的模式在发起任何请求前显式抛基础设施/不完整错误。
 * - 重启以操作员 before/after 为默认；仅当用例以固定 argv 安全持有自有进程时才重启该 PID。
 */

const nodeHttp = require('node:http');
const nodeHttps = require('node:https');
const { spawn } = require('node:child_process');

const DEFAULT_TIMEOUT_MS = 15000;
const POLL_INTERVAL_MS = 100;
const NEWLINE = String.fromCharCode(10);
const DUPLICATE_PATTERN = /已存在|已经存在|可能已存在|重复保存/;

class ConfigError extends Error { constructor(m) { super(m); this.name = 'ConfigError'; } }
class AssertionError extends Error { constructor(m) { super(m); this.name = 'AssertionError'; } }
class InfrastructureError extends Error { constructor(m) { super(m); this.name = 'InfrastructureError'; } }
class OperatorPendingError extends Error { constructor(m) { super(m); this.name = 'OperatorPendingError'; } }

function sleep(ms) { return new Promise((resolve) => setTimeout(resolve, ms)); }

function isLoopbackHost(host) {
  const text = String(host || '');
  if (text === 'localhost' || text === '::1' || text === '[::1]') return true;
  return text.startsWith('127.');
}

function matches(text, matcher) {
  if (matcher === null || matcher === undefined) return false;
  if (matcher instanceof RegExp) return matcher.test(String(text));
  return String(text).includes(String(matcher));
}

function firstLine(value) {
  const text = String(value === null || value === undefined ? '' : value);
  const index = text.indexOf(NEWLINE);
  return index < 0 ? text : text.slice(0, index);
}

function assert(condition, message) {
  if (!condition) throw new AssertionError(message || '断言失败');
  return true;
}

let playwrightModule = null;

function getPlaywright() {
  if (!playwrightModule) {
    try {
      playwrightModule = require('playwright');
    } catch (error) {
      throw new InfrastructureError('[infrastructure] 未找到 Playwright：请在 acceptance/ 目录执行 npm install 安装浏览器验收依赖后重试。原始错误：' + error.message);
    }
  }
  return playwrightModule;
}

/* ------------------------------ 配置解析 ------------------------------ */

function parseJsonEnv(raw, label) {
  if (raw === null || raw === undefined || raw === '') return undefined;
  try {
    return JSON.parse(raw);
  } catch (error) {
    throw new ConfigError(label + ' 不是合法 JSON：' + error.message);
  }
}

function parseAppArgv(raw) {
  if (raw === null || raw === undefined || raw === '') return null;
  const value = parseJsonEnv(raw, 'APP_ARGV');
  if (!Array.isArray(value) || value.length === 0) throw new ConfigError('APP_ARGV 必须是至少含一个元素的 JSON 数组（按固定 argv 启动，不启用 shell）。');
  for (const item of value) {
    if (typeof item !== 'string' || item.length === 0) throw new ConfigError('APP_ARGV 的每个元素都必须是非空字符串（按固定 argv 启动，不启用 shell）。');
  }
  return value.slice();
}

function parseUiSelectors(raw) {
  if (raw === null || raw === undefined || raw === '') return {};
  const value = parseJsonEnv(raw, 'UI_SELECTORS');
  if (value === null || typeof value !== 'object' || Array.isArray(value)) throw new ConfigError('UI_SELECTORS 必须是 逻辑名到选择器 的 JSON 对象。');
  const out = {};
  for (const key of Object.keys(value)) {
    const selector = value[key];
    if (typeof selector !== 'string' || selector.trim() === '') throw new ConfigError('UI_SELECTORS 的 ' + key + ' 必须是非空选择器字符串。');
    out[key] = selector;
  }
  return out;
}

function parsePositiveInt(raw, fallback) {
  if (raw === null || raw === undefined || raw === '') return fallback;
  const value = Number(raw);
  if (!Number.isFinite(value) || value <= 0) throw new ConfigError('期望正整数配置，实际得到：' + raw);
  return Math.floor(value);
}

function parseAuth(env) {
  const user = env.AUTH_USER;
  const pass = env.AUTH_PASS;
  const hasUser = user !== null && user !== undefined && String(user) !== '';
  const hasPass = pass !== null && pass !== undefined && String(pass) !== '';
  if (hasUser !== hasPass) throw new ConfigError('[incomplete] AUTH_USER 与 AUTH_PASS 必须同时提供；当前仅提供其一，认证无法完成。');
  if (!hasUser) return null;
  const scheme = String(env.AUTH_SCHEME || env.AUTH_MODE || 'basic').trim();
  if (scheme.toLowerCase() !== 'basic') throw new InfrastructureError('[infrastructure] 不支持的认证模式 ' + scheme + '：本 P0 仅支持 basic；已在发起任何请求前显式拒绝，绝不静默跳过凭据。');
  return { user: String(user), pass: String(pass), scheme: scheme };
}

function loadConfig(env) {
  const source = env || process.env;
  const rawTarget = source.TARGET_URL;
  if (rawTarget === null || rawTarget === undefined || String(rawTarget).trim() === '') {
    throw new ConfigError('缺少必需环境变量 TARGET_URL：请提供被测应用的真实回环地址，例如 http://127.0.0.1:8080/。');
  }
  let target;
  try {
    target = new URL(String(rawTarget).trim());
  } catch (error) {
    throw new ConfigError('TARGET_URL 不是合法 URL（为安全起见不回显所提交的地址）');
  }
  if (target.username !== '' || target.password !== '') throw new ConfigError('[incomplete] TARGET_URL 不得包含用户信息（userinfo）；此 P0 不接受 URL 内嵌凭据，请改用受支持的显式认证配置（为安全起见不回显所提交的地址）');
  if (target.protocol !== 'http:') throw new InfrastructureError('[infrastructure] 本 P0 仅支持 http 目标传输；显式拒绝未支撑的 ' + target.protocol + ' 基础设施，而不是假装支持（为安全起见不回显所提交的地址）');
  const port = source.PORT !== null && source.PORT !== undefined && source.PORT !== '' ? parsePositiveInt(source.PORT, 0) : target.port ? Number(target.port) : null;
  const dataDir = source.DATA_DIR && String(source.DATA_DIR).trim() !== '' ? String(source.DATA_DIR).trim() : null;
  return Object.freeze({
    targetUrl: target.href,
    targetOrigin: target.origin,
    port: port,
    dataDir: dataDir,
    appArgv: parseAppArgv(source.APP_ARGV),
    uiSelectors: parseUiSelectors(source.UI_SELECTORS),
    auth: parseAuth(source),
    timeout: parsePositiveInt(source.UI_TIMEOUT_MS, DEFAULT_TIMEOUT_MS),
    headless: source.HEADLESS ? !(String(source.HEADLESS) === '0' || /^false$/i.test(String(source.HEADLESS))) : true,
  });
}

/* ------------------------------ UI 适配器 ------------------------------ */

const CONTROL_SPECS = {
  saveUrl: { kind: 'single', semantic: [(root) => root.getByRole('textbox', { name: /链接|网址|URL|link/i })], css: ['[data-testid=save-url]', '#save-url', 'input[name=url]', 'input[name=link]', 'input[type=url]'] },
  saveTitle: { kind: 'single', semantic: [(root) => root.getByRole('textbox', { name: /标题|title/i })], css: ['[data-testid=save-title]', '#save-title', 'input[name=title]'] },
  saveNote: { kind: 'single', semantic: [(root) => root.getByRole('textbox', { name: /备注|说明|note/i })], css: ['[data-testid=save-note]', '#save-note', 'textarea[name=note]', 'textarea[name=description]'] },
  saveCategorySelect: { kind: 'single', semantic: [(root) => root.getByRole('combobox', { name: /分类|category/i })], css: ['[data-testid=save-category-select]', '#save-category-select', 'select[name=category]', 'select[name=category_id]'] },
  saveCategoryNew: { kind: 'single', semantic: [(root) => root.getByRole('textbox', { name: /新建分类|新分类|分类名称|创建分类|category/i })], css: ['[data-testid=save-category-new]', '#save-category-new', 'input[name=new-category]', 'input[name=category-new-name]'] },
  saveSubmit: { kind: 'single', semantic: [(root) => root.getByRole('button', { name: /保存|添加|收藏|新增|提交|submit/i })], css: ['[data-testid=save-submit]', '#save-submit', 'button[type=submit]', 'button[name=save]'] },
  formError: { kind: 'list', semantic: [(root) => root.getByRole('alert')], css: ['[data-testid=form-error]', '#form-error', '.form-error', '[data-error]', '.error-message'] },
  categoryList: { kind: 'list', semantic: [], css: ['[data-testid=category-list]', '#category-list', '.category-list'] },
  categoryItem: { kind: 'list', semantic: [], css: ['[data-testid=category-item]', '.category-item', '[data-category-id]', '[data-category-name]', 'a[href*=category]'] },
  recordList: { kind: 'list', semantic: [], css: ['[data-testid=record-list]', '#record-list', '.record-list', 'main ol', 'main ul'] },
  recordCard: { kind: 'list', semantic: [], css: ['[data-testid=record-card]', '.record-card', 'article.record', 'li.record', 'main ol > li', 'main ul > li'] },
  recordOpen: { kind: 'list', semantic: [(root) => root.getByRole('link')], css: ['[data-testid=record-open]', '.record-open', 'a[data-url]', 'a[href]'] },
  recordCategory: { kind: 'list', semantic: [], css: ['[data-testid=record-category]', '.record-category', '[data-category-name]'] },
  recordMoveSelect: { kind: 'single', semantic: [(root) => root.getByRole('combobox', { name: /移动|分类|category|move/i })], css: ['[data-testid=record-move-select]', 'select[name=category]', 'select[name=move-to]', 'select.move-select', 'select'] },
  recordMoveSubmit: { kind: 'single', semantic: [(root) => root.getByRole('button', { name: /移动|保存|确定|更新|move|apply/i })], css: ['[data-testid=record-move-submit]', '.move-submit', 'button[name=move]', 'form button[type=submit]'] },
  searchInput: { kind: 'single', semantic: [(root) => root.getByRole('searchbox'), (root) => root.getByRole('textbox', { name: /搜索|检索|search|关键字|关键词/i })], css: ['[data-testid=search-input]', '#search-input', 'input[type=search]', 'input[name=q]', 'input[name=search]'] },
  searchSubmit: { kind: 'single', semantic: [(root) => root.getByRole('button', { name: /搜索|检索|search|查找/i })], css: ['[data-testid=search-submit]', '#search-submit', '.search-submit', 'button[name=search]'] },
  emptyLibrary: { kind: 'list', semantic: [], css: ['[data-testid=empty-library]', '#empty-library', '.empty-library', '[data-state=empty-library]'] },
  noSearchMatch: { kind: 'list', semantic: [], css: ['[data-testid=no-search-match]', '#no-search-match', '.no-search-match', '[data-state=no-search-match]'] },
  categoryCreateInput: { kind: 'single', semantic: [(root) => root.getByRole('textbox', { name: /新建分类|新分类|分类名称|创建分类/i })], css: ['[data-testid=category-create-input]', '#category-create-input', 'input[name=category-name]'] },
  categoryCreateSubmit: { kind: 'single', semantic: [(root) => root.getByRole('button', { name: /新建分类|创建分类|添加分类|新建|创建/i })], css: ['[data-testid=category-create-submit]', '#category-create-submit', '.category-create-submit'] },
  duplicateConfirm: { kind: 'single', semantic: [(root) => root.getByRole('button', { name: /仍然保存|仍要保存|仍保存|继续保存|保存为另一条|确认保存|仍然添加/i })], css: ['[data-testid=duplicate-confirm]', '#duplicate-confirm', '.duplicate-confirm', 'button[name=still-save]'] },
};

function camelToKebab(name) { return String(name).replace(/[A-Z]/g, (ch) => '-' + ch.toLowerCase()); }

const NAME_INDEX = (function () {
  const index = {};
  for (const name of Object.keys(CONTROL_SPECS)) {
    index[name.toLowerCase()] = name;
    index[camelToKebab(name)] = name;
  }
  return index;
})();

function normalizeOverrides(input) {
  if (input === null || input === undefined || input === '') return {};
  let value = input;
  if (typeof input === 'string') {
    try {
      value = JSON.parse(input);
    } catch (error) {
      throw new ConfigError('UI_SELECTORS 不是合法 JSON：' + error.message);
    }
  }
  if (value === null || typeof value !== 'object' || Array.isArray(value)) throw new ConfigError('UI_SELECTORS 必须是 逻辑名到选择器 的 JSON 对象。');
  const out = {};
  for (const key of Object.keys(value)) {
    const canonical = NAME_INDEX[String(key).trim().toLowerCase()];
    if (!canonical) throw new ConfigError('UI_SELECTORS 含未知控件名：' + key + '；可用名称为 ' + Object.keys(CONTROL_SPECS).join(', '));
    const selector = value[key];
    if (typeof selector !== 'string' || selector.trim() === '') throw new ConfigError('UI_SELECTORS 的 ' + key + ' 必须是非空选择器字符串。');
    out[canonical] = selector.trim();
  }
  return out;
}

function composeLocator(root, spec, override) {
  const builders = [];
  if (override) builders.push((scope) => scope.locator(override));
  for (const build of spec.semantic || []) builders.push(build);
  for (const selector of spec.css || []) builders.push((scope) => scope.locator(selector));
  let locator = null;
  for (const build of builders) {
    let next = null;
    try {
      next = build(root);
    } catch (error) {
      next = null;
    }
    if (!next) continue;
    if (!locator) {
      locator = next;
      continue;
    }
    try {
      locator = locator.or(next);
    } catch (error) {
      /* 保留已有 locator */
    }
  }
  if (!locator) locator = root.locator('xpath=//*[@data-atlas-unresolved]');
  return spec.kind === 'single' ? locator.first() : locator;
}

function resolveControls(page, overrides) {
  const normalized = normalizeOverrides(overrides);
  const out = {};
  for (const name of Object.keys(CONTROL_SPECS)) out[name] = composeLocator(page, CONTROL_SPECS[name], normalized[name]);
  return out;
}

function scopedLocator(root, name, overrides) {
  const spec = CONTROL_SPECS[name];
  if (!spec) throw new ConfigError('未知 UI 控件名：' + name);
  const normalized = normalizeOverrides(overrides);
  return composeLocator(root, spec, normalized[name]);
}

function configOf(page, explicit) {
  if (explicit) return explicit;
  const stored = page && page.__atlas && page.__atlas.config;
  if (stored) return stored;
  return { uiSelectors: {}, timeout: DEFAULT_TIMEOUT_MS, targetUrl: page && page.url ? page.url() : '' };
}

/* ------------------------------ 浏览器与打开 ------------------------------ */

function defaultPortFor(protocol) {
  if (protocol === 'https:' || protocol === 'wss:') return '443';
  if (protocol === 'http:' || protocol === 'ws:') return '80';
  return '';
}

function endpointKey(parsed) {
  if (!parsed) return '';
  let protocol = parsed.protocol;
  if (protocol === 'ws:') protocol = 'http:';
  else if (protocol === 'wss:') protocol = 'https:';
  const port = parsed.port || defaultPortFor(protocol);
  return protocol + '//' + parsed.hostname + (port ? ':' + port : '');
}

function getOriginGuardProxy(page) {
  try {
    const context = page && page.context ? page.context() : null;
    const browser = context && context.browser ? context.browser() : null;
    return (browser && browser.__atlasOriginGuardProxy) || null;
  } catch (error) {
    return null;
  }
}

function createOriginGuardProxy(config) {
  const target = new URL(config.targetUrl);
  if (target.protocol !== 'http:') throw new InfrastructureError('[infrastructure] 拒绝为未支撑的目标传输建立浏览器代理：' + target.protocol + '（HTTPS 基础设施需显式声明，绝不假装支持）。');
  const targetOrigin = config.targetOrigin || target.origin;
  const targetPort = target.port ? Number(target.port) : 80;
  const state = { attemptedOpens: [], violations: [], blocked: [] };

  function record(rawUrl, method, resourceType, isNavigation) {
    const entry = { url: rawUrl, method: method, resourceType: resourceType, navigation: isNavigation };
    state.blocked.push(entry);
    if (isNavigation) state.attemptedOpens.push(rawUrl);
    else state.violations.push(entry);
  }

  function looksLikeNavigation(req) {
    const dest = String(req.headers['sec-fetch-dest'] || '').toLowerCase();
    if (dest !== '') return dest === 'document' || dest === 'iframe' || dest === 'frame';
    const accept = String(req.headers.accept || '');
    return (req.method === 'GET' || req.method === 'HEAD') && accept.indexOf('text/html') >= 0;
  }

  const server = nodeHttp.createServer((clientReq, clientRes) => {
    const raw = clientReq.url || '';
    let parsed = null;
    try { parsed = new URL(raw); } catch (error) { parsed = null; }
    if (parsed && parsed.protocol === 'http:' && parsed.origin === targetOrigin) {
      const headers = Object.assign({}, clientReq.headers);
      delete headers['proxy-connection'];
      delete headers['proxy-authorization'];
      headers.host = target.host;
      const upstream = nodeHttp.request({
        protocol: 'http:',
        hostname: target.hostname,
        port: targetPort,
        method: clientReq.method,
        path: parsed.pathname + parsed.search,
        headers: headers,
      }, (upstreamRes) => {
        clientRes.writeHead(upstreamRes.statusCode || 502, upstreamRes.headers);
        upstreamRes.pipe(clientRes);
      });
      upstream.on('error', () => {
        if (!clientRes.headersSent) clientRes.writeHead(502, { 'content-type': 'text/plain; charset=utf-8' });
        try { clientRes.end('proxied target unavailable'); } catch (error) { /* 忽略 */ }
      });
      clientReq.on('error', () => { try { upstream.destroy(); } catch (error) { /* 忽略 */ } });
      clientReq.pipe(upstream);
      return;
    }
    const isNavigation = looksLikeNavigation(clientReq);
    const resourceType = isNavigation ? 'document' : String(clientReq.headers['sec-fetch-dest'] || 'proxy');
    record(raw, clientReq.method, resourceType, isNavigation);
    clientRes.writeHead(403, { 'content-type': 'text/plain; charset=utf-8' });
    clientRes.end('blocked by atlas deny-by-default origin guard proxy');
  });

  server.on('connect', (req, socket) => {
    record(req.url || '', 'CONNECT', 'connect', false);
    try { socket.destroy(); } catch (error) { /* 忽略 */ }
  });

  server.on('upgrade', (req, socket) => {
    record(req.url || '', req.method || 'GET', 'websocket', false);
    try { socket.destroy(); } catch (error) { /* 忽略 */ }
  });

  server.on('clientError', (error, socket) => {
    try { socket.destroy(); } catch (ignored) { /* 忽略 */ }
  });

  const listening = new Promise((resolve, reject) => {
    const onError = (error) => { server.removeListener('listening', onListening); reject(error); };
    const onListening = () => {
      server.removeListener('error', onError);
      const address = server.address();
      resolve(address && typeof address === 'object' ? address.port : 0);
    };
    server.once('error', onError);
    server.once('listening', onListening);
    server.listen(0, '127.0.0.1');
  });

  const proxy = {
    state: state,
    attemptedOpens: state.attemptedOpens,
    violations: state.violations,
    blocked: state.blocked,
    serverUrl: null,
    port: null,
    close: null,
  };
  proxy.close = () => new Promise((resolve) => {
    try {
      if (typeof server.closeAllConnections === 'function') server.closeAllConnections();
    } catch (error) { /* 忽略 */ }
    try {
      server.close(() => resolve());
    } catch (error) {
      resolve();
    }
  });
  return listening.then((port) => {
    proxy.port = port;
    proxy.serverUrl = 'http://127.0.0.1:' + port;
    if (typeof server.unref === 'function') server.unref();
    return proxy;
  });
}

async function launchBrowser(config) {
  const playwright = getPlaywright();
  const cfg = config || loadConfig();
  const headless = cfg.headless !== undefined ? cfg.headless : true;
  const proxy = await createOriginGuardProxy(cfg);
  let browser;
  try {
    browser = await playwright.chromium.launch({
      headless: headless,
      proxy: { server: proxy.serverUrl },
      args: ['--proxy-bypass-list=<-loopback>'],
    });
  } catch (error) {
    await proxy.close().catch(() => {});
    throw new InfrastructureError('[infrastructure] 浏览器启动失败，已关闭本次专用拒绝代理：' + (error && error.message ? error.message : String(error)));
  }
  try { browser.__atlasOriginGuardProxy = proxy; } catch (error) { /* 忽略 */ }
  try {
    browser.on('disconnected', () => { proxy.close().catch(() => {}); });
  } catch (error) { /* 忽略 */ }
  return browser;
}

async function waitForAny(page, locators, options) {
  const opts = options || {};
  const timeout = opts.timeout || DEFAULT_TIMEOUT_MS;
  return waitFor(async () => {
    for (const locator of locators) {
      try {
        if ((await locator.count()) > 0) return locator;
      } catch (error) {
        /* 继续尝试下一个候选 */
      }
    }
    return false;
  }, { timeout: timeout, message: opts.message || '任一控件出现' });
}

async function openApp(page, config) {
  const cfg = config || configOf(page);
  if (config) page.__atlas = { config: config };
  const controls = resolveControls(page, cfg.uiSelectors);
  const timeout = cfg.timeout || DEFAULT_TIMEOUT_MS;
  const response = await page.goto(cfg.targetUrl, { waitUntil: 'domcontentloaded', timeout: timeout });
  if (response && response.status() >= 500) throw new AssertionError('目标应用返回 HTTP ' + response.status() + '，判定不可用：' + cfg.targetUrl);
  await waitForAny(page, [controls.saveUrl, controls.searchInput, controls.recordList, controls.emptyLibrary, controls.noSearchMatch], { timeout: timeout, message: '应用可用界面锚点（保存表单/检索框/记录列表/空状态）' });
  return response;
}

/* ------------------------------ 断言 ------------------------------ */

async function waitFor(predicate, options) {
  const opts = options || {};
  const timeout = opts.timeout || DEFAULT_TIMEOUT_MS;
  const interval = opts.interval || POLL_INTERVAL_MS;
  const started = Date.now();
  let last;
  for (;;) {
    try {
      const value = await predicate();
      if (value) return value;
      last = value;
    } catch (error) {
      last = error;
    }
    if (Date.now() - started >= timeout) {
      const detail = last === undefined ? '' : last instanceof Error ? '；最后错误：' + last.message : '；最后观察：' + String(last);
      throw new AssertionError((opts.message || '条件未在限定时间内满足') + detail);
    }
    await sleep(interval);
  }
}

async function bodyText(page) {
  try {
    return (await page.locator('body').innerText({ timeout: 2000 })).trim();
  } catch (error) {
    return '';
  }
}

async function locatorText(locator) {
  try {
    if ((await locator.count()) === 0) return null;
    return (await locator.first().innerText({ timeout: 2000 })).trim();
  } catch (error) {
    return null;
  }
}

async function safeCount(locator) {
  try {
    return await locator.count();
  } catch (error) {
    return 0;
  }
}

async function expectVisible(locator, message) {
  return waitFor(async () => {
    try {
      if ((await locator.count()) === 0) return false;
      return await locator.first().isVisible();
    } catch (error) {
      return false;
    }
  }, { message: '期望可见：' + (message || '元素') });
}

async function expectCount(locator, expected, message) {
  return waitFor(async () => {
    try {
      return (await locator.count()) === expected;
    } catch (error) {
      return false;
    }
  }, { message: '期望数量为 ' + expected + '：' + (message || '元素') });
}

async function expectAppText(page, matcher, message) {
  return waitFor(async () => {
    const text = await bodyText(page);
    return matches(text, matcher) ? text : false;
  }, { message: message || '页面应包含文本 ' + String(matcher) });
}

async function expectAppTextAbsent(page, matcher, message) {
  return waitFor(async () => {
    const text = await bodyText(page);
    return matches(text, matcher) ? false : true;
  }, { message: message || '页面不应包含文本 ' + String(matcher) });
}

async function errorText(page, controls) {
  const locator = controls.formError;
  const count = await safeCount(locator);
  for (let i = 0; i < count; i += 1) {
    const text = (await locator.nth(i).innerText().catch(() => '')).trim();
    if (text) return text;
  }
  return null;
}

async function expectErrorText(page, matcher, configArg) {
  const cfg = configOf(page, configArg);
  const controls = resolveControls(page, cfg.uiSelectors);
  return waitFor(async () => {
    const fromForm = await errorText(page, controls);
    if (fromForm && matches(fromForm, matcher)) return fromForm;
    const body = await bodyText(page);
    if (matches(body, matcher)) return body;
    return false;
  }, { message: '期望出现用户可见错误：' + String(matcher) });
}

async function expectDistinctStateText(page, configArg) {
  const cfg = configOf(page, configArg);
  const controls = resolveControls(page, cfg.uiSelectors);
  const empty = await locatorText(controls.emptyLibrary);
  const miss = await locatorText(controls.noSearchMatch);
  if (empty === null || miss === null) throw new AssertionError('未能同时读取空库提示与检索无匹配提示：请提供 empty-library 与 no-search-match 的可解析标记。');
  if (empty === miss) throw new AssertionError('空库提示与检索无匹配提示文案相同，必须彼此不同：' + empty);
  return { emptyLibrary: empty, noSearchMatch: miss };
}

/* ------------------------------ 交互辅助 ------------------------------ */

async function clickAndSettle(page, locator, timeout) {
  const target = locator.first();
  await expectVisible(target, '可点击控件');
  await target.click({ noWaitAfter: true });
  await page.waitForLoadState('load', { timeout: timeout || DEFAULT_TIMEOUT_MS }).catch(() => {});
  await sleep(150);
}

async function optionExists(selectLocator, name) {
  try {
    if ((await selectLocator.count()) === 0) return false;
    const options = await selectLocator.first().locator('option').allTextContents();
    const wanted = String(name).trim();
    return options.some((text) => text.trim() === wanted);
  } catch (error) {
    return false;
  }
}

async function selectOptionByLabelOrValue(selectLocator, name) {
  const select = selectLocator.first();
  const wanted = String(name);
  try {
    await select.selectOption({ label: wanted });
    return true;
  } catch (error) {
    /* 继续尝试按 value */
  }
  try {
    await select.selectOption({ value: wanted });
    return true;
  } catch (error) {
    /* 继续按 option 文本匹配 */
  }
  const options = await select.locator('option').all();
  for (const option of options) {
    const text = ((await option.textContent()) || '').trim();
    if (text === wanted) {
      const value = await option.getAttribute('value');
      await select.selectOption(value === null ? { label: wanted } : value);
      return true;
    }
  }
  throw new AssertionError('无法在分类下拉中选择：' + wanted);
}

async function categoryVisible(page, name, controls) {
  const wanted = String(name).trim();
  const items = controls.categoryItem;
  const count = await safeCount(items);
  for (let i = 0; i < count; i += 1) {
    const text = (await items.nth(i).innerText().catch(() => '')).trim();
    if (text === wanted || text.includes(wanted)) return true;
  }
  return optionExists(controls.saveCategorySelect, wanted);
}

async function duplicatePresent(page, controls) {
  const text = await errorText(page, controls);
  if (text && DUPLICATE_PATTERN.test(text)) return true;
  const body = await bodyText(page);
  return DUPLICATE_PATTERN.test(body) && (await safeCount(controls.duplicateConfirm)) > 0;
}

async function saveBookmark(page, options, configArg) {
  const opts = options || {};
  const cfg = configOf(page, configArg);
  const controls = resolveControls(page, cfg.uiSelectors);
  const timeout = cfg.timeout || DEFAULT_TIMEOUT_MS;
  await expectVisible(controls.saveUrl, '保存表单链接输入框');
  await controls.saveUrl.fill(opts.url === null || opts.url === undefined ? '' : String(opts.url));
  if (typeof opts.title === 'string' && (await safeCount(controls.saveTitle)) > 0) await controls.saveTitle.fill(opts.title);
  if (typeof opts.note === 'string' && (await safeCount(controls.saveNote)) > 0) await controls.saveNote.fill(opts.note);
  if (opts.categoryName !== null && opts.categoryName !== undefined && String(opts.categoryName) !== '') {
    const name = String(opts.categoryName);
    if (await optionExists(controls.saveCategorySelect, name)) await selectOptionByLabelOrValue(controls.saveCategorySelect, name);
    else if ((await safeCount(controls.saveCategoryNew)) > 0) await controls.saveCategoryNew.fill(name);
  }
  const countBefore = await safeCount(controls.recordCard);
  await clickAndSettle(page, controls.saveSubmit, timeout);
  if (await duplicatePresent(page, controls)) {
    if (opts.confirmDuplicate) {
      await clickAndSettle(page, controls.duplicateConfirm, timeout);
    } else {
      return { saved: false, duplicate: true, error: await errorText(page, controls), countBefore: countBefore, countAfter: await safeCount(controls.recordCard) };
    }
  }
  const error = await errorText(page, controls);
  const countAfter = await safeCount(controls.recordCard);
  return { saved: error === null && !(await duplicatePresent(page, controls)), duplicate: false, error: error, countBefore: countBefore, countAfter: countAfter };
}

async function createCategory(page, name, configArg) {
  const cfg = configOf(page, configArg);
  const controls = resolveControls(page, cfg.uiSelectors);
  const timeout = cfg.timeout || DEFAULT_TIMEOUT_MS;
  const target = String(name).trim();
  if (target === '') throw new ConfigError('createCategory 需要非空分类名。');
  const hasDedicated = (await safeCount(controls.categoryCreateInput)) > 0 && (await safeCount(controls.categoryCreateSubmit)) > 0;
  if (hasDedicated) {
    await controls.categoryCreateInput.fill(target);
    await clickAndSettle(page, controls.categoryCreateSubmit, timeout);
  } else if ((await safeCount(controls.saveCategoryNew)) > 0) {
    await controls.saveCategoryNew.fill(target);
    if ((await safeCount(controls.categoryCreateSubmit)) > 0) {
      await clickAndSettle(page, controls.categoryCreateSubmit, timeout);
    } else {
      await controls.saveCategoryNew.press('Enter').catch(() => {});
      await page.waitForLoadState('load', { timeout: timeout }).catch(() => {});
      await sleep(150);
    }
  } else {
    throw new AssertionError('未找到分类创建入口：请通过 UI_SELECTORS 提供 category-create-input/category-create-submit 或 save-category-new 映射。');
  }
  await waitFor(async () => categoryVisible(page, target, controls), { timeout: timeout, message: '新建分类未出现：' + target });
  return target;
}

async function moveRecord(page, recordIndex, categoryName, configArg) {
  const cfg = configOf(page, configArg);
  const controls = resolveControls(page, cfg.uiSelectors);
  const timeout = cfg.timeout || DEFAULT_TIMEOUT_MS;
  const cards = controls.recordCard;
  const total = await safeCount(cards);
  if (recordIndex < 0 || recordIndex >= total) throw new AssertionError('recordIndex ' + recordIndex + ' 越界（当前记录数 ' + total + '）。');
  const card = cards.nth(recordIndex);
  await expectVisible(card, '待移动记录');
  const moveSelect = scopedLocator(card, 'recordMoveSelect', cfg.uiSelectors);
  await waitFor(async () => (await safeCount(moveSelect)) > 0, { timeout: timeout, message: '记录内未找到移动分类下拉' });
  await selectOptionByLabelOrValue(moveSelect, String(categoryName));
  const moveSubmit = scopedLocator(card, 'recordMoveSubmit', cfg.uiSelectors);
  if ((await safeCount(moveSubmit)) > 0) {
    await clickAndSettle(page, moveSubmit, timeout);
  } else {
    await moveSelect.first().press('Enter').catch(() => {});
    await page.waitForLoadState('load', { timeout: timeout }).catch(() => {});
    await sleep(150);
  }
  return true;
}

async function search(page, term, configArg) {
  const cfg = configOf(page, configArg);
  const controls = resolveControls(page, cfg.uiSelectors);
  const timeout = cfg.timeout || DEFAULT_TIMEOUT_MS;
  await expectVisible(controls.searchInput, '检索输入框');
  await controls.searchInput.fill(term === null || term === undefined ? '' : String(term));
  if ((await safeCount(controls.searchSubmit)) > 0) {
    await clickAndSettle(page, controls.searchSubmit, timeout);
  } else {
    await controls.searchInput.press('Enter').catch(() => {});
    await page.waitForLoadState('load', { timeout: timeout }).catch(() => {});
    await sleep(150);
  }
  return true;
}

async function readRecords(page, configArg) {
  const cfg = configOf(page, configArg);
  const controls = resolveControls(page, cfg.uiSelectors);
  const cards = controls.recordCard;
  const total = await safeCount(cards);
  const records = [];
  for (let i = 0; i < total; i += 1) {
    const card = cards.nth(i);
    const text = (await card.innerText().catch(() => '')).trim();
    let url = null;
    let title = null;
    const links = scopedLocator(card, 'recordOpen', cfg.uiSelectors);
    const linkCount = await safeCount(links);
    for (let j = 0; j < linkCount; j += 1) {
      const href = await links.nth(j).getAttribute('href').catch(() => null);
      if (href) {
        url = href;
        const linkText = (await links.nth(j).innerText().catch(() => '')).trim();
        if (linkText) title = linkText;
        break;
      }
    }
    if (!url) url = await card.getAttribute('data-url').catch(() => null);
    const category = await locatorText(scopedLocator(card, 'recordCategory', cfg.uiSelectors));
    records.push({ index: i, url: url || null, title: title, category: category, text: text });
  }
  return records;
}

async function doubleSubmit(page, configArg) {
  const cfg = configOf(page, configArg);
  const controls = resolveControls(page, cfg.uiSelectors);
  const timeout = cfg.timeout || DEFAULT_TIMEOUT_MS;
  const before = await safeCount(controls.recordCard);
  const button = controls.saveSubmit.first();
  await expectVisible(button, '保存按钮');
  await Promise.all([
    button.click({ noWaitAfter: true, force: true }).catch(() => {}),
    button.click({ noWaitAfter: true, force: true }).catch(() => {}),
  ]);
  await page.waitForLoadState('load', { timeout: timeout }).catch(() => {});
  await sleep(300);
  const after = await safeCount(controls.recordCard);
  return { before: before, after: after, delta: after - before };
}

/* ------------------------------ 网络守卫 ------------------------------ */

function installNetworkPolicy(page, config) {
  const context = page.context();
  const targetOrigin = config.targetOrigin || new URL(config.targetUrl).origin;
  const targetEndpoint = endpointKey(new URL(targetOrigin));
  const proxy = getOriginGuardProxy(page);
  const policy = {
    targetOrigin: targetOrigin,
    proxy: proxy,
    attemptedOpens: proxy ? proxy.attemptedOpens : [],
    violations: proxy ? proxy.violations : [],
    blocked: proxy ? proxy.blocked : [],
  };
  const handler = async (route) => {
    const request = route.request();
    const url = request.url();
    let parsed = null;
    try {
      parsed = new URL(url);
    } catch (error) {
      parsed = null;
    }
    if (!parsed || (parsed.protocol !== 'http:' && parsed.protocol !== 'https:')) {
      await route.continue().catch(() => {});
      return;
    }
    if (parsed.origin === targetOrigin) {
      await route.continue().catch(() => {});
      return;
    }
    const isNavigation = request.isNavigationRequest() && request.resourceType() === 'document';
    const entry = { url: url, method: request.method(), resourceType: request.resourceType(), navigation: isNavigation };
    policy.blocked.push(entry);
    try {
      await route.abort('blockedbyclient');
    } catch (error) {
      await route.abort().catch(() => {});
    }
    if (isNavigation) policy.attemptedOpens.push(url);
    else policy.violations.push(entry);
  };
  try {
    context.route('**/*', handler);
  } catch (error) {
    throw new InfrastructureError('[infrastructure] 无法安装网络守卫：' + error.message);
  }
  context.on('websocket', (socket) => {
    if (proxy) return;
    try {
      const parsed = new URL(socket.url());
      if (endpointKey(parsed) !== targetEndpoint) {
        const entry = { url: socket.url(), method: 'WS', resourceType: 'websocket', navigation: false };
        policy.blocked.push(entry);
        policy.violations.push(entry);
      }
    } catch (error) {
      /* 忽略非法 URL */
    }
  });
  policy.dispose = async () => {
    try {
      await context.unroute('**/*', handler);
    } catch (error) {
      /* 已卸载 */
    }
  };
  policy.assertNoBackgroundOutbound = () => {
    if (policy.violations.length > 0) throw new AssertionError('检测到后台外发请求（应被判失败）：' + policy.violations.map((item) => item.method + ' ' + item.url).join(' | '));
    return true;
  };
  policy.takeAttemptedOpens = () => policy.attemptedOpens.slice();
  policy.reset = () => {
    policy.attemptedOpens.length = 0;
    policy.violations.length = 0;
    policy.blocked.length = 0;
  };
  try {
    Object.defineProperty(page, '__atlasNetworkPolicy', { value: policy, writable: true, configurable: true, enumerable: false });
  } catch (error) {
    page.__atlasNetworkPolicy = policy;
  }
  try {
    context.__atlasNetworkPolicy = policy;
  } catch (error) {
    /* 忽略无法附加的上下文引用 */
  }
  return policy;
}

function getNetworkPolicy(page) {
  return page.__atlasNetworkPolicy || null;
}

function applyTargetCredentials(context, config) {
  const auth = config.auth;
  if (!auth) return { applied: false };
  const scheme = String(auth.scheme || 'basic').toLowerCase();
  if (scheme !== 'basic') throw new InfrastructureError('[infrastructure] 不支持的认证模式 ' + auth.scheme + '：仅支持 basic（HTTP Basic）。请在目标声明并实现受支持模式后再运行验收，不得静默跳过。');
  const targetOrigin = config.targetOrigin || new URL(config.targetUrl).origin;
  const pattern = targetOrigin + '/**';
  const header = 'Basic ' + Buffer.from(auth.user + ':' + auth.pass, 'utf8').toString('base64');
  const handler = async (route) => {
    const headers = Object.assign({}, route.request().headers(), { authorization: header });
    try {
      await route.fallback({ headers: headers });
    } catch (error) {
      await route.continue({ headers: headers }).catch(() => {});
    }
  };
  try {
    context.route(pattern, handler);
  } catch (error) {
    throw new InfrastructureError('[infrastructure] 无法注入目标认证：' + error.message);
  }
  return {
    applied: true,
    dispose: async () => {
      try {
        await context.unroute(pattern, handler);
      } catch (error) {
        /* 已卸载 */
      }
    },
  };
}

/* ------------------------------ 重启与持久化 ------------------------------ */

function buildAppArgv(config) {
  const base = config && Array.isArray(config.appArgv) && config.appArgv.length > 0 ? config.appArgv.slice() : ['python3', 'app.py'];
  if (config) {
    if (config.port && base.indexOf('--port') < 0) {
      base.push('--port');
      base.push(String(config.port));
    }
    if (config.dataDir && base.indexOf('--data-dir') < 0) {
      base.push('--data-dir');
      base.push(config.dataDir);
    }
  }
  return base;
}

function quoteArg(value) {
  const text = String(value);
  return /[^A-Za-z0-9_@%+=:,./-]/.test(text) ? JSON.stringify(text) : text;
}

function operatorRestartSteps(config) {
  const argv = buildAppArgv(config);
  const command = argv.map(quoteArg).join(' ');
  return {
    command: command,
    before: [
      '1. 确认记录与分类已通过 UI 保存（本用例随后会经 UI 读回这些数据）。',
      '2. 在运行被测应用的终端停止你启动的进程（仅停止 python3 app.py），不要终止无关进程。',
    ],
    after: [
      '3. 使用与之前相同的参数重新启动应用：' + command,
      '4. 等待应用在回环地址就绪后，回到本用例按提示继续。',
    ],
    notes: [
      '进程真实重启是持久化的唯一证明；刷新页面、文件存在或新建 SQLite 连接都不算重启。',
      '无法人工介入时，可设置 OPERATOR_CONFIRMED=1 声明已按上述步骤完成，或由用例以固定 argv 自行持有并仅重启自有 PID。',
    ],
  };
}

function probeHttp(url, timeoutMs) {
  const target = new URL(url);
  if (!isLoopbackHost(target.hostname)) throw new InfrastructureError('就绪探测仅允许回环目标：' + target.hostname);
  const transport = target.protocol === 'https:' ? nodeHttps : nodeHttp;
  const port = target.port ? Number(target.port) : target.protocol === 'https:' ? 443 : 80;
  return new Promise((resolve) => {
    const request = transport.request({ method: 'GET', hostname: target.hostname, port: port, path: target.pathname + target.search, timeout: timeoutMs || 1000 }, (response) => {
      response.resume();
      resolve(response.statusCode || 0);
    });
    request.on('error', () => resolve(0));
    request.on('timeout', () => {
      request.destroy();
      resolve(0);
    });
    request.end();
  });
}

async function waitForTargetReady(url, timeoutMs) {
  const timeout = timeoutMs || DEFAULT_TIMEOUT_MS;
  const started = Date.now();
  for (;;) {
    const status = await probeHttp(url, 1000);
    if (status >= 200 && status < 500) return true;
    if (Date.now() - started >= timeout) return false;
    await sleep(200);
  }
}

class RestartController {
  constructor(config) {
    if (!config) throw new ConfigError('RestartController 需要 loadConfig() 的配置。');
    this.config = config;
    this.child = null;
    this.ownsProcess = false;
  }

  operatorRestartSteps() {
    return operatorRestartSteps(this.config);
  }

  static operatorRestartSteps(config) {
    return operatorRestartSteps(config || loadConfig());
  }

  canSelfRestart() {
    return Boolean(this.ownsProcess && this.child && !this.child.killed && this.child.pid);
  }

  async start() {
    if (this.child) throw new InfrastructureError('应用已由本控制器启动，不能重复启动。');
    if (!this.config.appArgv) throw new InfrastructureError('[incomplete] 未提供 APP_ARGV：本用例不会以未声明方式启动应用；请改用操作员 before/after 步骤，或显式提供安全 argv。');
    const argv = buildAppArgv(this.config);
    const child = spawn(argv[0], argv.slice(1), { stdio: 'inherit', shell: false, env: Object.assign({}, process.env) });
    this.child = child;
    this.ownsProcess = true;
    await new Promise((resolve, reject) => {
      child.once('spawn', resolve);
      child.once('error', reject);
    });
    return child.pid;
  }

  async stop() {
    if (!this.canSelfRestart()) throw new InfrastructureError('仅可终止本用例以固定 argv 启动并持有的进程；当前没有可安全终止的自有进程。');
    const child = this.child;
    this.child = null;
    this.ownsProcess = false;
    await new Promise((resolve) => {
      let settled = false;
      const finish = () => {
        if (!settled) {
          settled = true;
          resolve();
        }
      };
      child.once('exit', finish);
      try {
        child.kill('SIGTERM');
      } catch (error) {
        finish();
      }
      setTimeout(() => {
        try {
          child.kill('SIGKILL');
        } catch (error) {
          /* 已退出 */
        }
        finish();
      }, 5000);
    });
    return true;
  }

  async restart() {
    if (!this.canSelfRestart()) throw new InfrastructureError('仅可重启本用例以固定 argv 启动并持有的进程；请改用操作员 before/after 步骤。');
    const oldPid = this.child.pid;
    await this.stop();
    const newPid = await this.start();
    if (newPid === oldPid) throw new AssertionError('重启后 PID 与重启前相同，不能作为真实进程重启的证明。');
    return { oldPid: oldPid, newPid: newPid };
  }

  async waitUntilReady(timeout) {
    return waitForTargetReady(this.config.targetUrl, timeout || this.config.timeout);
  }

  async waitForOperator(options) {
    const opts = options || {};
    const steps = this.operatorRestartSteps();
    const output = opts.stdout || process.stdout;
    output.write(NEWLINE + '[操作员步骤] 需要真实进程重启才能继续：' + NEWLINE);
    for (const line of steps.before) output.write('  ' + line + NEWLINE);
    for (const line of steps.after) output.write('  ' + line + NEWLINE);
    for (const line of steps.notes) output.write('  说明：' + line + NEWLINE);
    if (process.env.OPERATOR_CONFIRMED === '1' || opts.assumeConfirmed) {
      output.write('  已确认操作员已完成重启。' + NEWLINE);
      return { completed: true, command: steps.command };
    }
    const input = opts.stdin || process.stdin;
    if (input && input.isTTY && !opts.nonInteractive) {
      output.write('  完成上述步骤后，按回车继续。' + NEWLINE);
      await new Promise((resolve) => {
        input.resume();
        input.once('data', () => {
          input.pause();
          resolve();
        });
      });
      return { completed: true, command: steps.command };
    }
    throw new OperatorPendingError('等待操作员完成 before/after 真实重启；未完成的操作员步骤不得计为通过。');
  }
}

/* ------------------------------ 用例运行器 ------------------------------ */

async function runCases(cases, options) {
  const opts = options || {};
  const config = opts.config || loadConfig();
  const browser = opts.browser || (await launchBrowser(config));
  const results = [];
  try {
    for (const testCase of cases) {
      const id = testCase.id || testCase.caseId || 'unknown';
      const name = testCase.name || testCase.goal || id;
      const run = testCase.run || testCase.fn;
      const record = { id: id, name: name, type: testCase.type || null, status: 'passed', kind: null, error: null };
      if (typeof run !== 'function') {
        record.status = 'failed';
        record.kind = 'infrastructure';
        record.error = '用例缺少可执行的 run/fn';
        results.push(record);
        console.log('[FAIL] ' + id + ' ' + name + ' — 用例缺少可执行的 run/fn');
        continue;
      }
      const context = await browser.newContext({ ignoreHTTPSErrors: true, serviceWorkers: 'block' });
      const page = await context.newPage();
      page.__atlas = { config: config };
      try {
        installNetworkPolicy(page, config);
        applyTargetCredentials(context, config);
        const value = await run({ page: page, context: context, browser: browser, config: config, helpers: helpers });
        if (value && (value.status === 'operator-pending' || value.pending === true)) {
          record.status = 'operator-pending';
          record.kind = 'operator-pending';
          record.error = value.reason || value.message || null;
        }
      } catch (error) {
        if (error instanceof OperatorPendingError || (error && error.name === 'OperatorPendingError')) {
          record.status = 'operator-pending';
          record.kind = 'operator-pending';
          record.error = error.message;
        } else {
          record.status = 'failed';
          record.kind = error && error.name === 'InfrastructureError' ? 'infrastructure' : error && error.name === 'ConfigError' ? 'config' : 'assertion';
          record.error = error && error.stack ? error.stack : String(error);
        }
      } finally {
        await context.close().catch(() => {});
      }
      results.push(record);
      const mark = record.status === 'passed' ? 'PASS' : record.status === 'failed' ? 'FAIL' : 'OPERATOR-PENDING';
      console.log('[' + mark + '] ' + id + ' ' + name + (record.error ? ' — ' + firstLine(record.error) : ''));
    }
  } finally {
    if (!opts.browser) await browser.close().catch(() => {});
  }
  const passed = results.filter((item) => item.status === 'passed').length;
  const failed = results.filter((item) => item.status === 'failed').length;
  const pending = results.filter((item) => item.status === 'operator-pending').length;
  const summary = { total: results.length, passed: passed, failed: failed, pending: pending, results: results };
  console.log(JSON.stringify(summary, null, 2));
  if (failed > 0) process.exitCode = 1;
  else if (pending > 0) process.exitCode = 2;
  return summary;
}

/* ------------------------------ 导出 ------------------------------ */

const helpers = {};

Object.assign(helpers, {
  ConfigError: ConfigError,
  AssertionError: AssertionError,
  InfrastructureError: InfrastructureError,
  OperatorPendingError: OperatorPendingError,
  DEFAULT_TIMEOUT_MS: DEFAULT_TIMEOUT_MS,
  loadConfig: loadConfig,
  CONTROL_SPECS: CONTROL_SPECS,
  resolveControls: resolveControls,
  scopedLocator: scopedLocator,
  launchBrowser: launchBrowser,
  openApp: openApp,
  waitFor: waitFor,
  assert: assert,
  matches: matches,
  expectVisible: expectVisible,
  expectCount: expectCount,
  expectAppText: expectAppText,
  expectAppTextAbsent: expectAppTextAbsent,
  expectErrorText: expectErrorText,
  expectDistinctStateText: expectDistinctStateText,
  saveBookmark: saveBookmark,
  createCategory: createCategory,
  moveRecord: moveRecord,
  search: search,
  readRecords: readRecords,
  doubleSubmit: doubleSubmit,
  installNetworkPolicy: installNetworkPolicy,
  applyTargetCredentials: applyTargetCredentials,
  getNetworkPolicy: getNetworkPolicy,
  RestartController: RestartController,
  operatorRestartSteps: operatorRestartSteps,
  waitForTargetReady: waitForTargetReady,
  runCases: runCases,
});

module.exports = helpers;
module.exports.default = operatorRestartSteps;
