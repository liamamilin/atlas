'use strict';

/*
 * acceptance/run.cjs — P0 薄聚合器与入口（仅编排与最终退出码）。
 *
 * 依赖：require ./common.cjs、./p0-save-classify.cjs、./p0-find-open.cjs、./p0-persistence.cjs。
 * 顺序：保存/归类 → 检索/浏览/打开 → 持久化，按序合并各模块导出的 cases，
 * 调用 common.runCases 顺序执行并汇总通过/失败/待操作员计数。
 *
 * 退出码契约（非零即视为未通过，绝不静默算通过）：
 * - failed > 0：断言失败，退出码 1；
 * - failed == 0 且 pending > 0：有待操作员未决项，退出码 2；
 * - 全部通过：退出码 0。
 *
 * 本文件不包含重复的用例逻辑、不启动被测应用、不 mock 目标响应，也不读取或打印目标凭据；
 * 凭据仅由 common.applyTargetCredentials 注入到显式配置的目标。
 */

const common = require('./common.cjs');
const saveClassifyModule = require('./p0-save-classify.cjs');
const findOpenModule = require('./p0-find-open.cjs');
const persistenceModule = require('./p0-persistence.cjs');

const runCases = common.runCases;
const loadConfig = common.loadConfig;
const InfrastructureError = common.InfrastructureError;

/* 固定顺序：保存/归类 → 检索/浏览/打开 → 持久化。 */
const GROUPS = [
  { label: '保存/归类（p0-save-classify）', module: saveClassifyModule },
  { label: '检索/浏览/打开（p0-find-open）', module: findOpenModule },
  { label: '持久化（p0-persistence）', module: persistenceModule },
];

function extractCases(group) {
  const exported = group.module;
  const cases = exported && Array.isArray(exported.cases) ? exported.cases : Array.isArray(exported) ? exported : null;
  if (!cases || cases.length === 0) {
    throw new InfrastructureError('[infrastructure] 行为组 ' + group.label + ' 未导出非空 cases 数组，无法聚合。');
  }
  for (let i = 0; i < cases.length; i += 1) {
    const item = cases[i];
    const id = item && (item.id || item.caseId);
    const run = item && (item.run || item.fn);
    if (!id || typeof run !== 'function') {
      throw new InfrastructureError('[infrastructure] 行为组 ' + group.label + ' 的第 ' + i + ' 条用例缺少 id 或可执行 run/fn。');
    }
  }
  return cases.slice();
}

function buildCases() {
  const merged = [];
  for (let i = 0; i < GROUPS.length; i += 1) {
    const groupCases = extractCases(GROUPS[i]);
    for (let j = 0; j < groupCases.length; j += 1) merged.push(groupCases[j]);
  }
  return merged;
}

function applyExitCode(summary) {
  const failed = summary && Number.isFinite(Number(summary.failed)) ? Number(summary.failed) : 0;
  const pending = summary && Number.isFinite(Number(summary.pending)) ? Number(summary.pending) : 0;
  if (failed > 0) {
    process.exitCode = 1;
    return 1;
  }
  if (pending > 0) {
    process.exitCode = 2;
    return 2;
  }
  process.exitCode = 0;
  return 0;
}

async function main() {
  let config;
  try {
    config = loadConfig();
  } catch (error) {
    console.error('[FAIL] 配置错误：' + (error && error.message ? error.message : String(error)));
    process.exitCode = 1;
    return 1;
  }

  let cases;
  try {
    cases = buildCases();
  } catch (error) {
    console.error('[FAIL] ' + (error && error.message ? error.message : String(error)));
    process.exitCode = 1;
    return 1;
  }

  console.log('[runner] P0 顺序：保存/归类 → 检索/浏览/打开 → 持久化；用例数 ' + cases.length + '。');

  let summary;
  try {
    summary = await runCases(cases, { config: config });
  } catch (error) {
    console.error('[FAIL] 运行失败：' + (error && error.stack ? error.stack : String(error)));
    process.exitCode = 1;
    return 1;
  }

  const code = applyExitCode(summary);
  if (code === 0) {
    console.log('[runner] 全部 ' + summary.total + ' 条用例通过；退出码 0。');
  } else if (code === 1) {
    console.error('[runner] 存在断言失败（failed=' + summary.failed + '）；退出码 1，不得视为通过。');
  } else {
    console.error('[runner] 存在待操作员未决项（pending=' + summary.pending + '）；退出码 2，未决项不得计为通过。');
  }
  return code;
}

if (require.main === module) {
  main().catch(function (error) {
    console.error('[FAIL] 未捕获错误：' + (error && error.stack ? error.stack : String(error)));
    process.exitCode = 1;
  });
}

module.exports = { main: main, buildCases: buildCases, applyExitCode: applyExitCode };
