# M1：任务级超时链路验收

状态：已通过。该记录验证任务级超时配置会终止超时验证命令、写入 `timed_out` 证据，并保留源工作区安全边界与清理证据。

## 验收对象

- 项目：`prj_0862eec26e94462cbdf5d0414c478c8c`（AI agent harness）
- 迭代：`itr_27255a757fe04b2da5ed216cb8e0e401`《Agent Harness 超时链路修复后验收》
- 任务：`tsk_e6b5fc5d7d054cf292848d6c17d0f6f2`《超时验收：任务级 30 秒边界》
- 执行：`exe_bc01ac9c5fcd4e67884a6140f3086a69`
- 接受基线：`snap_6c788690f025445e84ad3e9416ce19b5`

## 修复内容

任务模型新增可选 `timeout_seconds`，范围限制为 30–1800 秒；CLI 执行优先使用任务级值，否则回退到 `.atlas/harness.json` 的项目级 `policy.commandTimeoutSeconds`。任务输入快照会记录最终采用的任务级设置，便于复核。

## 固定边界

- 任务为只读分析，不允许写入项目文件。
- 任务级超时：`30` 秒。
- 固定验证命令：

  ```sh
  python3 -c "import time; time.sleep(31)"
  ```

- OpenCode CLI 在隔离副本中运行，源工作区不参与执行。

## 结果

- 验证步骤耗时：`30004ms`。
- 步骤状态：`timed_out`；退出码：`124`；`timedOut=true`。
- `verification.all_planned_passed=false`，因此超时不被视为通过。
- 源工作区：`changed=false`；文件变更为空；`scope_compliant=true`。
- 执行未进入应用阶段：`application_status=not_applicable`。
- 清理状态：`cleaned`；`evidence_preserved=true`；证据目录保留 `atlas.json`、OpenCode stdout/stderr 和结构化步骤记录。
- 迭代已完成；任务以 `waived` 记录，因为这是对超时安全语义的验收，而不是一项应当成功的业务变更。

## 之前暴露的缺口

修复前同一类 31 秒命令会使用项目默认 600 秒并被标记为 `completed`。修复后重新执行确认任务级 30 秒边界已生效；该缺口已补充回归测试。

## 仍未覆盖

应用后的回滚/撤销，以及并行任务、take-over、历史列表和多入口仍需单独范围与验收。
