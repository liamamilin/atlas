# M1：受控变更任务验收

状态：已通过。该记录覆盖一个最小、可回收的 `code` 变更任务，用来验证“隔离执行 → 固定验证 → 差异审阅 → 显式应用 → 独立产品验收 → 清理”的真实链路；不代表停止、取消、超时、回滚或通用 Harness 已完成。

## 验收对象

- 项目：`prj_0862eec26e94462cbdf5d0414c478c8c`（AI agent harness）
- 迭代：`itr_d2810e2a65974f25947fbd935509eb1c`《Agent Harness 变更任务验收》
- 任务：`tsk_990032f6aebc443f938b967ba54e0293`《变更验收：创建可回收标记文件》
- 执行：`exe_713507199bbc4546881577b10aefc432`
- 引擎：OpenCode CLI，模型 `opencode-go/mimo-v2.5`
- 接受基线：`snap_f27cb053d7b44844a4b04eb8b82cd03d`

## 固定边界

- 允许写入路径只有 `change-task.txt`。
- 预期内容只有一行：`Atlas change acceptance`。
- 固定验证命令：

  ```sh
  python3 -c "from pathlib import Path; assert Path('change-task.txt').read_text() == 'Atlas change acceptance\\n'"
  ```

- 执行在隔离副本中完成；源工作区在显式应用前不变。

## 结果

- OpenCode CLI 正常完成，退出码为 `0`，标准错误为空。
- 隔离副本范围检查通过：只新增 `change-task.txt`，没有修改或删除其他文件。
- 固定验证命令通过，任务步骤全部通过。
- 通过 Atlas 显式应用结果，应用状态为 `applied`；项目工作区中已核对文件内容与预期一致。
- 产品验收已独立记录为 `passed`，证据包含执行、应用和独立复核三项。
- 执行副本已清理，证据目录保留；清理结果为 `already_absent`（副本已在应用后完成清理）。
- 迭代已完成，状态为 `completed`。

## 结论与边界

这次验收证明 Atlas + OpenCode 的最小变更闭环可以真实运行，并且应用结果、验证结果、产品验收和副本清理彼此分离、可追溯。尚未覆盖的独立范围包括应用后自动回滚/撤销，以及并行任务、take-over、历史列表和多入口。
