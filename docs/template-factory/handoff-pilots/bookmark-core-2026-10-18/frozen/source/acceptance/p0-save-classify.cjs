'use strict';

/*
 * acceptance/p0-save-classify.cjs — P0 保存与归类行为组（require ./common.cjs）。
 *
 * 覆盖：A01 仅 URL 保存→未分类并出现（正）；A02 标题+备注重载完整（正）；A03 选择已有分类归入（正）；
 * A04 新建分类并归入后重载保持（正）；A11 重复 URL 显式提示且可显式继续保存为第二条（负）；
 * A12 双击 save-submit 只产生一条记录（负）；A13 超限备注显式报错且不落库、无静默截断（负）；
 * A14 无效 URL 与非 http(s) 协议显式报错且不落库（负）；A15 失败后表单保留输入、修正后重试成功（正）；
 * A16 中文与 emoji 标题/备注保存、显示、检索正确（正）。
 *
 * 约束：只与真实目标 UI 交互，不启动应用、不 mock、不用文件存在性代替用户行为；
 * 断言失败即抛出，runCases 汇总后进程退出码非零；不硬编码任何已知夹具值。
 */

const common = require('./common.cjs');

const openApp = common.openApp;
const saveBookmark = common.saveBookmark;
const search = common.search;
const readRecords = common.readRecords;
const resolveControls = common.resolveControls;
const doubleSubmit = common.doubleSubmit;
const expectAppText = common.expectAppText;
const expectErrorText = common.expectErrorText;
const waitFor = common.waitFor;
const assert = common.assert;
const matches = common.matches;
const runCases = common.runCases;
const loadConfig = common.loadConfig;

/* 未分类落点是规格声明的可见文案（category_id 为 NULL），不是某个夹具的私有值。 */
const UNCLASSIFIED_PATTERN = /未分类|以后看看|未归类|待整理|Unsorted|Uncategorized/i;
/* 重复 URL 必须出现显式“已存在”提示。 */
const DUPLICATE_PATTERN = /已存在|已经存在|可能已存在|重复保存|重复链接/;
/* 无效 URL / 非 http(s) 的错误语义；只在用户可见错误区匹配，避免命中静态帮助文案。 */
const STRICT_INVALID_PATTERN = /无效|不合法|非法|不是有效|仅支持|必须以|必须为|格式不正确|协议/;
/* 备注超限的错误语义；只在用户可见错误区匹配，避免命中静态“最多 N 字”提示。 */
const STRICT_NOTE_LIMIT_PATTERN = /备注.{0,8}(过长|超|上限)|超过.{0,8}(上限|长度)|不超过|最多.{0,8}(字|字符)|长度上限|太长|过多|过大|limit|字符数/i;

/* 无法从界面发现声明上限时的兜底超限长度（仍要求目标显式拒绝，不做静默截断）。 */
const NOTE_OVER_LIMIT_FALLBACK = 20000;

let sequence = 0;

function nonce(label) {
  sequence += 1;
  return String(label || 'case') + '-' + Date.now().toString(36) + '-' + sequence + '-' + Math.random().toString(36).slice(2, 8);
}

function uniqueUrl(label) {
  return 'https://bookmarks.example.com/' + nonce(label || 'item');
}

function findByUrl(records, url) {
  return records.find(function (record) { return record && record.url === url; }) || null;
}

async function countRecords(controls) {
  try {
    return await controls.recordCard.count();
  } catch (error) {
    return 0;
  }
}

async function waitForRecordByUrl(page, config, url, message) {
  return waitFor(async function () {
    const records = await readRecords(page, config);
    return findByUrl(records, url) || false;
  }, { message: message || ('记录列表应包含：' + url) });
}

function recordsForUrl(records, url) {
  return records.filter(function (record) { return record && record.url === url; });
}

async function readFormError(page, config) {
  const controls = resolveControls(page, config.uiSelectors);
  const locator = controls.formError;
  const count = await locator.count().catch(function () { return 0; });
  const texts = [];
  for (let i = 0; i < count; i += 1) {
    const text = (await locator.nth(i).innerText().catch(function () { return ''; })).trim();
    if (text) texts.push(text);
  }
  return texts.join(' ');
}

async function expectFormError(page, config, pattern, message) {
  return waitFor(async function () {
    const text = await readFormError(page, config);
    return text && matches(text, pattern) ? text : false;
  }, { message: message || ('应出现与 ' + String(pattern) + ' 匹配的用户可见错误') });
}

async function categoryOptionExists(page, config, name) {
  const controls = resolveControls(page, config.uiSelectors);
  const select = controls.saveCategorySelect;
  const count = await select.count().catch(function () { return 0; });
  if (count === 0) return false;
  const options = await select.first().locator('option').allTextContents().catch(function () { return []; });
  return options.some(function (text) { return text.trim() === String(name); });
}

async function detectNoteLimit(page, controls) {
  try {
    const raw = await controls.saveNote.getAttribute('maxlength');
    if (raw !== null && raw !== undefined && String(raw).trim() !== '') {
      const value = Number(raw);
      if (Number.isFinite(value) && value > 0) return value;
    }
  } catch (error) {
    /* 无 maxlength，继续从可见提示推断 */
  }
  let body = '';
  try {
    body = await page.locator('body').innerText({ timeout: 2000 });
  } catch (error) {
    body = '';
  }
  const patterns = [
    /备注.{0,40}?([0-9]{2,7})/,
    /(?:最多|上限|不超过|限制).{0,20}?([0-9]{2,7})/,
    /([0-9]{2,7})[ ]*(?:字|字符|个字符)/,
  ];
  for (let i = 0; i < patterns.length; i += 1) {
    const match = patterns[i].exec(body);
    if (match) {
      const value = Number(match[1]);
      if (Number.isFinite(value) && value >= 10) return value;
    }
  }
  return null;
}

const cases = [
  {
    id: 'A01',
    name: '仅 URL 保存后进入未分类并立即出现（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const url = uniqueUrl('a01');
      const result = await saveBookmark(page, { url: url }, config);
      assert(result.saved === true && result.duplicate !== true && !result.error, 'A01 仅 URL 保存应成功，实际 saved=' + result.saved + ' duplicate=' + result.duplicate + ' error=' + String(result.error));
      const record = await waitForRecordByUrl(page, config, url, 'A01 保存后记录应立即可见：' + url);
      const shown = (record.category || '') + ' ' + record.text;
      assert(UNCLASSIFIED_PATTERN.test(shown), 'A01 未选择分类时应落入未分类，实际可见文本：' + shown);
      assert(matches(shown, url) || (record.title && matches(record.title, url)), 'A01 缺省标题应回退为 URL 并可见，实际文本：' + shown);
    },
  },
  {
    id: 'A02',
    name: '标题与备注保存后重载仍完整（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const url = uniqueUrl('a02');
      const title = '教程收藏' + nonce('t');
      const note = '备注开头' + nonce('n') + '备注结尾';
      const result = await saveBookmark(page, { url: url, title: title, note: note }, config);
      assert(result.saved === true && !result.error, 'A02 带标题与备注保存应成功：' + String(result.error));
      await openApp(page, config);
      const record = await waitForRecordByUrl(page, config, url, 'A02 重载后记录应仍在：' + url);
      assert(record.text.indexOf(title) >= 0 || (record.title && record.title.indexOf(title) >= 0), 'A02 重载后标题应完整可见：' + title + '；实际：' + record.text);
      assert(record.text.indexOf(note) >= 0, 'A02 重载后备注应完整可见：' + note + '；实际：' + record.text);
    },
  },
  {
    id: 'A03',
    name: '选择已有分类保存后归入（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const category = '已有分类' + nonce('c');
      const seedUrl = uniqueUrl('a03-seed');
      const seed = await saveBookmark(page, { url: seedUrl, title: '建立分类', categoryName: category }, config);
      assert(seed.saved === true && !seed.error, 'A03 先用保存流程建立分类应成功：' + String(seed.error));
      await openApp(page, config);
      await waitFor(function () { return categoryOptionExists(page, config, category); }, { message: 'A03 分类应已存在并可在下拉中作为已有分类被选择：' + category });
      const url = uniqueUrl('a03');
      const result = await saveBookmark(page, { url: url, title: '选择已有分类', categoryName: category }, config);
      assert(result.saved === true && !result.error, 'A03 选择已有分类保存应成功：' + String(result.error));
      const record = await waitForRecordByUrl(page, config, url, 'A03 归入分类的记录应出现：' + url);
      const shown = (record.category || '') + ' ' + record.text;
      assert(shown.indexOf(category) >= 0, 'A03 记录应出现在所选分类中：' + category + '；实际：' + shown);
    },
  },
  {
    id: 'A04',
    name: '新建分类并归入后重载保持（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const category = '新分类' + nonce('c');
      const url = uniqueUrl('a04');
      const result = await saveBookmark(page, { url: url, title: '新建分类记录', categoryName: category }, config);
      assert(result.saved === true && !result.error, 'A04 新建分类并保存应成功：' + String(result.error));
      await openApp(page, config);
      const record = await waitForRecordByUrl(page, config, url, 'A04 重载后记录应仍在：' + url);
      const shown = (record.category || '') + ' ' + record.text;
      assert(shown.indexOf(category) >= 0, 'A04 重载后归属关系应保持：' + category + '；实际：' + shown);
      await expectAppText(page, category, 'A04 重载后新分类应仍存在：' + category);
    },
  },
  {
    id: 'A11',
    name: '重复 URL 显式提示且可显式继续保存为第二条（负）',
    type: 'negative',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const controls = resolveControls(page, config.uiSelectors);
      const url = uniqueUrl('a11');
      const first = await saveBookmark(page, { url: url, title: '重复来源' }, config);
      assert(first.saved === true && !first.error, 'A11 首次保存应成功：' + String(first.error));
      const before = await countRecords(controls);
      const duplicate = await saveBookmark(page, { url: url }, config);
      assert(duplicate.duplicate === true, 'A11 再次保存相同 URL 应出现显式“已存在”提示，而非静默处理');
      await expectErrorText(page, DUPLICATE_PATTERN, config);
      const afterDuplicate = await countRecords(controls);
      assert(afterDuplicate === before, 'A11 未确认时不得静默新增记录：before=' + before + ' after=' + afterDuplicate);
      const confirmed = await saveBookmark(page, { url: url, confirmDuplicate: true }, config);
      assert(confirmed.error === null || confirmed.error === undefined, 'A11 显式继续保存不应报错：' + String(confirmed.error));
      await waitFor(async function () {
        const records = await readRecords(page, config);
        return recordsForUrl(records, url).length === 2 ? true : false;
      }, { message: 'A11 显式继续后应存在两条相同 URL 记录：' + url });
    },
  },
  {
    id: 'A12',
    name: '双击保存提交只产生一条记录（负）',
    type: 'negative',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const controls = resolveControls(page, config.uiSelectors);
      const url = uniqueUrl('a12');
      await controls.saveUrl.fill(url);
      const titleInput = controls.saveTitle;
      if ((await titleInput.count().catch(function () { return 0; })) > 0) {
        await titleInput.fill('双击记录' + nonce('t'));
      }
      const outcome = await doubleSubmit(page, config);
      assert(outcome.delta === 1, 'A12 双击保存应只新增一条记录，实际新增 ' + outcome.delta);
      await waitFor(async function () {
        const records = await readRecords(page, config);
        return recordsForUrl(records, url).length === 1 ? true : false;
      }, { message: 'A12 该 URL 应恰好一条记录：' + url });
    },
  },
  {
    id: 'A13',
    name: '超限备注显式报错且不落库、无静默截断（负）',
    type: 'negative',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const controls = resolveControls(page, config.uiSelectors);
      const limit = await detectNoteLimit(page, controls);
      const overLimit = limit !== null ? limit + Math.max(1, Math.floor(limit * 0.02)) : NOTE_OVER_LIMIT_FALLBACK;
      const oversizedNote = '备'.repeat(overLimit);
      const url = uniqueUrl('a13');
      const before = await countRecords(controls);
      const result = await saveBookmark(page, { url: url, title: '超限备注', note: oversizedNote }, config);
      assert(result.saved !== true, 'A13 超限备注不应被接受保存（声明上限 ' + String(limit) + '，提交 ' + overLimit + ' 字）');
      await expectFormError(page, config, STRICT_NOTE_LIMIT_PATTERN, 'A13 超限备注应显式报错（声明上限 ' + String(limit) + '，提交 ' + overLimit + ' 字）');
      const after = await countRecords(controls);
      assert(after === before, 'A13 超限备注不得落库：before=' + before + ' after=' + after);
      const records = await readRecords(page, config);
      assert(!findByUrl(records, url), 'A13 超限备注的 URL 不应出现在库中：' + url);
    },
  },
  {
    id: 'A14',
    name: '无效 URL 与非 http(s) 协议显式报错且不落库（负）',
    type: 'negative',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const controls = resolveControls(page, config.uiSelectors);
      const invalidInputs = [
        { label: '无效文本', url: '这不是一个有效链接' + nonce('bad') },
        { label: 'ftp 协议', url: 'ftp://files.example.com/store/archive.txt' },
        { label: 'javascript 协议', url: 'javascript:alert(1)' },
      ];
      for (let i = 0; i < invalidInputs.length; i += 1) {
        const item = invalidInputs[i];
        const before = await countRecords(controls);
        const result = await saveBookmark(page, { url: item.url, title: '非法输入-' + item.label }, config);
        assert(result.saved !== true, 'A14 ' + item.label + ' 不应保存成功：' + item.url);
        await expectFormError(page, config, STRICT_INVALID_PATTERN, 'A14 ' + item.label + ' 应显式报错：' + item.url);
        const after = await countRecords(controls);
        assert(after === before, 'A14 ' + item.label + ' 不得落库：before=' + before + ' after=' + after);
      }
      const records = await readRecords(page, config);
      for (let i = 0; i < invalidInputs.length; i += 1) {
        assert(!findByUrl(records, invalidInputs[i].url), 'A14 非法 URL 不应出现在库中：' + invalidInputs[i].url);
      }
    },
  },
  {
    id: 'A15',
    name: '失败后表单保留输入、修正后重试成功（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const controls = resolveControls(page, config.uiSelectors);
      const badUrl = '待修正链接' + nonce('bad');
      const title = '待修正记录' + nonce('t');
      const failed = await saveBookmark(page, { url: badUrl, title: title }, config);
      assert(failed.saved !== true, 'A15 无效 URL 不应保存成功');
      await expectFormError(page, config, STRICT_INVALID_PATTERN, 'A15 无效 URL 应显式报错');
      const retainedUrl = await controls.saveUrl.inputValue().catch(function () { return null; });
      assert(retainedUrl === badUrl, 'A15 失败后链接输入应保留，实际：' + String(retainedUrl));
      if ((await controls.saveTitle.count().catch(function () { return 0; })) > 0) {
        const retainedTitle = await controls.saveTitle.inputValue().catch(function () { return null; });
        assert(retainedTitle === title, 'A15 失败后标题输入应保留，实际：' + String(retainedTitle));
      }
      const goodUrl = uniqueUrl('a15');
      const fixed = await saveBookmark(page, { url: goodUrl, title: title }, config);
      assert(fixed.saved === true && !fixed.error, 'A15 修正后重试应成功：' + String(fixed.error));
      const record = await waitForRecordByUrl(page, config, goodUrl, 'A15 修正后记录应出现：' + goodUrl);
      assert(record.text.indexOf(title) >= 0 || (record.title && record.title.indexOf(title) >= 0), 'A15 修正后标题应保留：' + title);
    },
  },
  {
    id: 'A16',
    name: '中文与 emoji 标题/备注保存、显示、检索正确（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      await openApp(page, config);
      const url = uniqueUrl('a16');
      const emoji = '🎉📌🧺';
      const title = '中文收藏' + emoji + nonce('t');
      const note = '中文备注' + nonce('n') + emoji;
      const result = await saveBookmark(page, { url: url, title: title, note: note }, config);
      assert(result.saved === true && !result.error, 'A16 中文与 emoji 记录应保存成功：' + String(result.error));
      const record = await waitForRecordByUrl(page, config, url, 'A16 记录应出现：' + url);
      assert(record.text.indexOf(title) >= 0 || (record.title && record.title.indexOf(title) >= 0), 'A16 标题中文与 emoji 应无乱码保留：' + title + '；实际：' + record.text);
      assert(record.text.indexOf(emoji) >= 0, 'A16 卡片应显示 emoji：' + emoji);
      await search(page, '中文收藏', config);
      const byChinese = await waitForRecordByUrl(page, config, url, 'A16 用中文检索应命中该记录：' + url);
      assert(byChinese.text.indexOf(emoji) >= 0 || (byChinese.title && byChinese.title.indexOf(emoji) >= 0), 'A16 中文检索结果应保留 emoji');
      await search(page, emoji, config);
      await waitForRecordByUrl(page, config, url, 'A16 用 emoji 检索应命中该记录：' + url);
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
