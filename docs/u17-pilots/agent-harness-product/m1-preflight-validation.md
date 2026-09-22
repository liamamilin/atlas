# M1：启动前预检接入验证

状态：Atlas 侧接入与回归验证已完成；真实终端纵向切片已在授权环境完成 CLI、隔离副本、固定验证、权限门、获准只读工具调用、证据和清理复测。只读任务的完整 TUI 路径已通过；变更任务的停止和应用按钮不适用于本次分析任务，需另建变更任务时再验收。

状态：已完成启动前预检 API、Atlas 项目工作台展示、显式 CLI 执行分支、TUI 最小终端入口和运行摘要映射。

## 已交付

- `opencode_cli_adapter.py` 读取项目 `.atlas/harness.json`，校验精确兼容线，并以无 shell 的 argv 形式构造后续 `opencode run` 调用。
- `drafts_api.py` 提供 `GET /api/projects/:id/harness/preflight`。配置缺失时返回 `not_configured`；配置存在时返回版本、可执行文件、provider 名称、退出码和安全诊断，不返回 provider 原始输出或凭证。
- 创建执行入口在存在 `.atlas/harness.json` 时再次执行预检。预检失败会在创建隔离工作副本前返回可识别错误，因此不会留下半成品副本。
- 项目工作台执行区展示“OpenCode 启动前检查”，通过时显示版本、路径和 provider 检查状态；失败时隐藏启动按钮并显示修复提示。

## 实际验证

项目：`prj_0862eec26e94462cbdf5d0414c478c8c`（AI agent harness）

接口响应（2026-09-20）：

```json
{
  "status": "passed",
  "version": "1.18.31",
  "minimumVersion": "1.18.31",
  "executable": "/opt/homebrew/bin/opencode",
  "providerNames": ["OpenCode Go", "OpenAI", "OpenCode Zen", "commandcode"],
  "checks": {"version": {"passed": true, "exitCode": 0}, "providers": {"passed": true, "exitCode": 0}}
}
```

验证结果：后端 `130` 项单元测试通过；前端 typecheck 与 production build 通过；工作台刷新后显示“OpenCode 启动前检查 已通过：1.18.31”。provider 失败和超时均会被标记为失败，CLI 运行摘要只保留稳定传输字段、事件类型和安全诊断码，固定验证命令会在隔离副本中重新执行并映射为任务步骤，原始输出可写入独立证据目录，并可由 execution record 引用；显式清理只删除隔离副本并保留证据。测试不保留凭证或原始 provider 输出。

## 真实终端验收记录（2026-09-21）

任务：`tsk_4aa41e37e50448388589db2b2f9081c9`《M1：终端纵向切片真实只读验收》  
执行：`exe_7b6e4dd9e67446b1a88e4c6c325577d9`  
证据目录：`application-atlas-production-pack/projects/execution-evidence/prj_0862eec26e94462cbdf5d0414c478c8c/exe_7b6e4dd9e67446b1a88e4c6c325577d9`

- Atlas 启动前 preflight：通过（OpenCode `1.18.31`、provider 配置状态可读）。
- 隔离工作副本：已创建；源工作区在执行前后未发现变更。
- OpenCode CLI：进程退出码 `1`，没有产生 stdout；stderr 为 `Unexpected error / FileSystem.open (.../.local/share/opencode/log/opencode.log)`。
- Atlas 运行摘要现将该失败归一为 `diagnosticCode=log_access`，提示允许 OpenCode 创建或打开本机日志后重试；原始 stderr 仍只保留在证据目录。
- 固定验证：通过；任务级验证命令 `python3 -c "print('atlas terminal acceptance')"` 已在隔离副本中执行并记录。
- 应用状态：`not_applicable`；未执行应用、验收通过或清理，以保留失败证据供复核。

结论：这是本机运行环境的日志访问/并发阻塞，不是源项目改动或固定验证失败。提升权限重试会把任务上下文发送给外部 provider，需用户明确授权后才能进行；在此之前，真实终端纵向切片保持“待复测”，不能宣称端到端验收通过。

## 授权后的复测（2026-09-21）

用户明确授权后，使用同一任务进行了第二次真实 CLI 运行：`exe_4db1bd533d8e45259adefcb626da72d7`。

- OpenCode CLI 退出码 `0`，产生 4 个 JSON 事件（`step_start`、`tool_use`、`step_finish`）。
- 固定验证命令通过，隔离副本无文件变更，源工作区复核无新增、删除或修改。
- OpenCode 尝试执行 `bash` 检查时触发权限请求并被拒绝；因此验证了 ask-first 硬门，但没有证明一次获准工具调用的完整结果。
- 任务副本已显式清理，CLI 原始证据保留；项目证据包已导出到 `application-atlas-production-pack/projects/exports/prj_0862eec26e94462cbdf5d0414c478c8c/20260921T121435Z-1212e024.zip`。

结论：Atlas 的 CLI 启动、隔离、权限门、获准只读工具调用、固定验证、证据保存和清理链路已经有真实运行证据；该只读验收任务在后续 TUI 路径复核后已通过，变更任务的停止和应用仍未覆盖。

## TUI 启动/退出冒烟（2026-09-21）

命令：`python3 application-atlas-production-pack/atlas_cli.py --interactive --lang zh`。

- 在授权环境启动终端入口，界面正常绘制。
- 发送项目选择 `Enter` 进入任务视图，按 `v` 打开运行详情，再按任意键返回，最后按 `q` 退出；进程退出码为 `0`。
- 本次只验证项目选择、任务视图、运行详情返回和退出，不调用 OpenCode provider，也不修改项目文件。
- 复测前修复了两个 TUI 问题：标准 PTY 不支持 `curses.curs_set(0)` 时安全降级；进入任务视图时补充 `task_index` 闭包声明，避免 `UnboundLocalError`。

该结果收口终端入口的项目选择、任务查看和返回稳定性；只读任务的启动、执行、验收、导出和清理路径已在后续复测中通过。变更任务的停止和应用仍需另建任务验收。

## 获准只读工具复测（2026-09-21）

为补齐权限门证据，使用隔离副本再次执行同一只读任务：`exe_fd26826a648b47f98f7fde12cbb88e7c`。

- OpenCode 退出码 `0`，产生 27 个 JSON 事件。
- 实际工具类型为 `read`、`glob`、`grep`；没有调用 `bash` 或编辑工具。
- 固定验证通过，隔离副本没有文件变化，范围检查为 `scope_compliant=true`，源工作区没有变化。
- 权限配置写入临时目录并在进程结束后清理，没有进入隔离副本差异。
- 执行副本已清理，证据目录保留：`application-atlas-production-pack/projects/execution-evidence/prj_0862eec26e94462cbdf5d0414c478c8c/exe_fd26826a648b47f98f7fde12cbb88e7c`。

结论：一次明确获准的只读工具调用已通过；随后只读任务的 TUI 执行、查看、验收、导出和清理路径也已通过。该结果不能替代变更任务的停止和应用验收。

## 完整只读 TUI 路径（2026-09-21）

通过 TUI 选择 M1 未验收任务并完成：`j/j` 选择任务 → `Enter` 启动 → `y` 确认 → `v` 查看运行详情 → 返回 → `p` 输入验收证据并确认 → `x` 导出 → `c` 清理 → `q` 退出。

- 最新执行：`exe_fc680ac2fbe94ff491f5cab3a534dfb9`，状态 `completed`。
- 任务验收状态：`passed`。
- 应用状态：`not_applicable`（分析任务没有文件结果）。
- 导出包：`application-atlas-production-pack/projects/exports/prj_0862eec26e94462cbdf5d0414c478c8c/20260921T125016Z-8d23b93f.zip`。
- 清理已完成，证据保留；源工作区复核无变化。

这次完整路径覆盖了只读任务的执行、查看、验收、导出和清理。停止活动执行与应用变更结果需要通过单独的 `code` 或 `document` 任务验收，不能用分析任务冒充。

## 尚未覆盖

本次接入完成 Atlas 侧的 preflight 门、可视反馈、显式 CLI 执行、CLI 运行摘要归一化、固定验证步骤映射、独立证据目录写入、execution record 索引、显式清理入口、`evidence.run_summary` 统一字段和最小终端入口；只读任务的 TUI 执行、查看、验收、导出和清理路径已通过，但不代表 OpenCode TUI 已经由 Atlas 重实现。尚未覆盖的是变更任务的停止和应用按钮，需要单独创建 `code` 或 `document` 任务验收；若 provider 权限或本机配置仍阻塞，则把该访问条件记录为真实部署前置条件。

## 2026-09-22 兼容性修复

多类型需求案例的首个变更任务暴露了两处执行适配问题：运行时仍向当前 OpenCode 的 `serve` 子命令传递已移除的 `--pure` 参数；CLI 临时权限配置又将 `edit` 设为 `deny`，导致模型只能阅读资料，无法写入声明的输出路径。现已改为选择项目配置或 Homebrew 的 OpenCode 可执行文件、移除 `serve --pure`，并在隔离副本中允许 `edit`，同时继续由 Atlas 通过 `write_paths` 和快照差异执行范围控制。修复后 130 项后端测试通过，T1 文档任务重试成功并完成应用。
