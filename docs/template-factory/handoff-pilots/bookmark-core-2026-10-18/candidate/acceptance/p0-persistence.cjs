'use strict';

/*
 * acceptance/p0-persistence.cjs — P0 持久化行为组（require ./common.cjs）。
 *
 * 覆盖：A10 先经 UI 保存记录与分类；随后以真实进程重启为证明；再经 UI 读回数据仍在。
 *
 * 重启契约（与 common.cjs、ARCHITECTURE.md 一致）：
 * - 默认由操作员执行 before/after 步骤（operatorRestartSteps）：用例输出停止并以
 *   `python3 app.py --port PORT --data-dir DIR` 重启的步骤并等待其完成；未完成即抛
 *   OperatorPendingError，该用例状态为 operator-pending，绝不记为通过。
 * - 仅当用例自身以固定 argv（APP_ARGV，shell:false）安全启动并持有进程时，才终止自己
 *   启动的 PID 并重启，并断言新旧 PID 不同；绝不执行任意 shell、不终止无关进程。
 * - 刷新页面不是重启；数据文件存在或新建 SQLite 连接都不是重启证明；本用例不要求应用
 *   暴露内部数据库连接状态，只经真实 UI 读回数据。
 *
 * 约束：只与真实目标 UI 交互，不 mock、不用文件存在性代替用户行为、不硬编码已知夹具值；
 * 断言失败即抛出，runCases 汇总后进程退出码非零。
 */

const common = require('./common.cjs');

const openApp = common.openApp;
const saveBookmark = common.saveBookmark;
const readRecords = common.readRecords;
const resolveControls = common.resolveControls;
const waitFor = common.waitFor;
const assert = common.assert;
const InfrastructureError = common.InfrastructureError;
const RestartController = common.RestartController;
const operatorRestartSteps = common.operatorRestartSteps;
const waitForTargetReady = common.waitForTargetReady;
const runCases = common.runCases;
const loadConfig = common.loadConfig;

let sequence = 0;

function nonce(label) {
  sequence += 1;
  return String(label || 'case') + '-' + Date.now().toString(36) + '-' + sequence + '-' + Math.random().toString(36).slice(2, 8);
}

function uniqueUrl(label) {
  return 'https://bookmarks.example.com/' + nonce(label || 'item');
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

function findRecordByUrl(records, url) {
  for (let i = 0; i < records.length; i += 1) {
    if (sameUrl(records[i].url, url)) return records[i];
  }
  return null;
}

async function waitForRecordByUrl(page, config, url, message) {
  return waitFor(async function () {
    const records = await readRecords(page, config);
    return findRecordByUrl(records, url) || false;
  }, { timeout: config.timeout, message: message || ('记录应可经 UI 读回：' + url) });
}

/* 分类是否仍存在：优先分类列表/下拉选项，最终回退到页面文本。 */
async function categoryPresent(page, config, name) {
  const controls = resolveControls(page, config.uiSelectors);
  const target = String(name).trim();
  const items = controls.categoryItem;
  const itemCount = await items.count().catch(function () { return 0; });
  for (let i = 0; i < itemCount; i += 1) {
    const text = ((await items.nth(i).innerText().catch(function () { return ''; })) || '').trim();
    if (text === target || text.indexOf(target) >= 0) return true;
  }
  const select = controls.saveCategorySelect;
  if ((await select.count().catch(function () { return 0; })) > 0) {
    const options = await select.first().locator('option').allTextContents().catch(function () { return []; });
    if (options.some(function (text) { return text.trim() === target; })) return true;
  }
  const body = await page.locator('body').innerText().catch(function () { return ''; });
  return body.indexOf(target) >= 0;
}

async function assertRecordAndCategory(page, config, url, categoryName, phase) {
  const label = phase || '读回';
  const record = await waitForRecordByUrl(page, config, url, 'A10 ' + label + '应能经 UI 读回记录：' + url);
  const shown = [record.title, record.category, record.text].filter(function (item) { return item !== null && item !== undefined && String(item) !== ''; }).join(' ');
  assert(shown.indexOf(categoryName) >= 0, 'A10 ' + label + '记录应仍归属该分类：' + categoryName + '；实际：' + shown);
  await waitFor(function () { return categoryPresent(page, config, categoryName); }, { timeout: config.timeout, message: 'A10 ' + label + '分类应仍存在：' + categoryName });
  return record;
}

/* 目标是否已有进程在监听（用于判断能否安全地由本用例持有自有进程）。 */
async function targetAlreadyRunning(config) {
  return waitForTargetReady(config.targetUrl, 1200);
}

const cases = [
  {
    id: 'A10',
    name: '数据经真实进程重启后仍可经 UI 读回（正）',
    type: 'positive',
    async run(context) {
      const page = context.page;
      const config = context.config;
      const controller = new RestartController(config);
      const selfManaged = Array.isArray(config.appArgv) && config.appArgv.length > 0;

      /* 反证守卫：本用例绝不使用刷新、文件存在性或新建 SQLite 连接作为重启证明。 */
      const proofGuard = { refresh: false, fileExistence: false, sqliteConnection: false };

      let pidBefore = null;
      let restartProof = null;
      let operatorCommand = null;

      try {
        if (selfManaged) {
          if (await targetAlreadyRunning(config)) {
            throw new InfrastructureError('[infrastructure] 配置冲突：已提供 APP_ARGV（要求本用例以固定 argv 持有应用进程），但 ' + config.targetUrl + ' 已有进程在监听。请停止外部启动的进程，或移除 APP_ARGV 改用操作员 before/after 重启。');
          }
          try {
            pidBefore = await controller.start();
          } catch (error) {
            throw new InfrastructureError('[infrastructure] 无法以固定 argv 启动自有应用进程：' + (error && error.message ? error.message : String(error)));
          }
          assert(controller.canSelfRestart(), 'A10 应以固定 argv 安全持有自有应用进程');
          const started = await controller.waitUntilReady();
          assert(started, 'A10 自有应用进程应在回环地址就绪：' + config.targetUrl);
        }

        await openApp(page, config);
        const categoryName = '持久化分类' + nonce('c');
        const url = uniqueUrl('a10');
        const title = '持久化记录' + nonce('t');
        const note = '持久化备注' + nonce('n');
        const saved = await saveBookmark(page, { url: url, title: title, note: note, categoryName: categoryName }, config);
        assert(saved.saved === true && !saved.error, 'A10 重启前应能经 UI 保存记录与分类：' + String(saved.error));
        await assertRecordAndCategory(page, config, url, categoryName, '重启前');

        /* —— 真实进程重启 —— */
        if (selfManaged) {
          const heldPid = pidBefore;
          const restart = await controller.restart();
          assert(restart.oldPid === heldPid, 'A10 必须重启本用例持有的同一自有进程：oldPid=' + restart.oldPid + ' 期望=' + heldPid);
          assert(restart.newPid !== restart.oldPid, 'A10 重启后 PID 应与重启前不同，否则不算真实进程重启：' + restart.oldPid);
          const ready = await controller.waitUntilReady();
          assert(ready, 'A10 重启后的自有应用进程应重新在回环地址就绪：' + config.targetUrl);
          restartProof = { kind: 'self-pid-change', oldPid: restart.oldPid, newPid: restart.newPid };
        } else {
          const steps = operatorRestartSteps(config);
          operatorCommand = steps.command;
          const outcome = await controller.waitForOperator();
          assert(outcome && outcome.completed === true, 'A10 操作员必须完成真实的停止与重启；刷新页面不能替代进程重启。');
          const ready = await waitForTargetReady(config.targetUrl, config.timeout);
          assert(ready, 'A10 操作员重启后目标应重新就绪：' + config.targetUrl);
          restartProof = { kind: 'operator-confirmed', command: operatorCommand };
        }

        assert(restartProof !== null, 'A10 必须完成真实进程重启（自有 PID 变化或操作员确认停止并重启）；不得以页面刷新代替重启，也不得以数据文件存在或新建 SQLite 连接作为证明。');
        assert(restartProof.kind === 'self-pid-change' || restartProof.kind === 'operator-confirmed', 'A10 重启证明必须为自有 PID 变化或操作员确认的真实重启：' + restartProof.kind);
        assert(proofGuard.refresh === false && proofGuard.fileExistence === false && proofGuard.sqliteConnection === false, 'A10 断言：未使用刷新、文件存在性或新建 SQLite 连接作为重启证明。');

        /* —— 重启后经 UI 读回 —— */
        await openApp(page, config);
        await assertRecordAndCategory(page, config, url, categoryName, '重启后');

        return { status: 'passed', restartProof: restartProof, command: operatorCommand };
      } finally {
        if (selfManaged && controller.canSelfRestart()) {
          await controller.stop().catch(function () {});
        }
      }
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
