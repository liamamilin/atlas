# M1：OpenCode 执行失败与恢复验收

状态：已通过。该记录验证 provider/模型失败会进入明确的 `failed` 终态，保留诊断证据，不应用任何变更，并可安全清理隔离副本。

## 验收对象

- 项目：`prj_0862eec26e94462cbdf5d0414c478c8c`（AI agent harness）
- 迭代：`itr_927707ced8fb4c6096afd5c6d61a4f7a`《Agent Harness 失败恢复验收》
- 任务：`tsk_d22d2a5fc92e416cbe7206d98ce82a28`《失败验收：provider 执行失败》
- 执行：`exe_bbecc92c8acc4904a485e4ccd4781dc2`
- 接受基线：`snap_b183456b1de442189db24cb93945fda9`

## 固定边界

- 任务为只读分析，不允许写入项目文件。
- 使用不可用模型 `opencode-go/model-that-does-not-exist` 触发 provider 执行失败。
- 固定验证命令为 `python3 -m json.tool .atlas/harness.json`；由于 OpenCode 在验证前失败，本次不进入验证通过或应用阶段。

## 结果

- OpenCode CLI 以 `exitCode=1`、`status=failed`、`diagnosticCode=process_exit` 结束。
- Atlas 执行状态：`failed`；`engine_status=cli_failed`。
- 隔离副本文件变更为空，`scope_compliant=true`；源工作区没有写入。
- `application_status=not_applicable`，没有差异可应用。
- 清理状态：`cleaned`；`evidence_preserved=true`。证据目录保留 Atlas 记录、stdout/stderr 和失败诊断。
- 任务以 `waived` 记录，因为失败是本验收刻意制造的边界条件；这不把失败误报为产品成功。
- 迭代已完成，可基于同一接受基线继续新的独立任务。

## 仍未覆盖

应用后的回滚/撤销，以及并行任务、take-over、历史列表和多入口仍需单独范围与验收。
