# M1：停止执行与证据清理验收

状态：已通过。该记录验证活动执行被 Atlas 显式停止后，状态、取消摘要、范围检查、证据保留和隔离副本清理保持一致。

## 验收对象

- 项目：`prj_0862eec26e94462cbdf5d0414c478c8c`（AI agent harness）
- 迭代：`itr_07a0bb25be9645189600fe3ea328c660`《Agent Harness 停止清理最终复验》
- 任务：`tsk_a94598891bcd41b4a917847d06f56d8b`《停止清理最终复验》
- 执行：`exe_9384ae3aaf0c485db9f243ead2272233`
- 接受基线：`snap_d7848750f2e843688bf36a370954b66e`

## 固定边界

- 任务为只读分析，不允许写入项目文件。
- 固定验证命令是 30 秒等待，用于制造可停止的活动执行：

  ```sh
  python3 -c "import time; time.sleep(30)"
  ```

- 执行通过 Atlas HTTP 会话启动，随后立即调用停止入口。

## 结果

- 执行状态：`stopped`。
- OpenCode 状态：`abort_requested`；运行摘要 `status=cancelled`，`timedOut=false`。
- 停止后隔离副本没有新增、修改或删除文件，`scope_compliant=true`；源工作区没有写入。
- 产品验收以明确免验记录保存：停止任务不按“执行成功”计数，但其停止语义与安全结果已被独立记录。
- 清理状态：`cleaned`；`evidence_preserved=true`，证据目录保留 Atlas 生成的 `atlas.json`。
- 迭代 `itr_07a0bb25be9645189600fe3ea328c660` 已完成。

## 修复记录

首次停止复验发现 HTTP 会话没有 CLI 适配器的证据目录，清理回执错误地报告 `evidence_preserved=false`。Atlas 现会在清理前为这类会话物化最小 `atlas.json` 记录，再删除隔离副本；新增回归测试后后端 131 项测试全部通过，最终复验已确认保留结果。

## 仍未覆盖

失败恢复、应用后的回滚/撤销，以及并行任务、take-over、历史列表和多入口仍需单独范围与验收；任务级超时链路见 `m1-timeout-acceptance.md`。
