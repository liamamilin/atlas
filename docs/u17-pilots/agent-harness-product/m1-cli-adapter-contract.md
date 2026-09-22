# M1：CLI 适配层契约（第一步）

状态：适配器基础、显式 CLI 执行分支、启动前 preflight、运行证据索引、工作副本清理、结果应用和键盘优先的最小终端纵向切片已实现；接管和实时事件流待扩展。

## 已实现

`application-atlas-production-pack/opencode_cli_adapter.py` 将 Atlas 项目契约与 OpenCode CLI 隔开：

- 从项目 `.atlas/harness.json` 读取 OpenCode 二进制路径、最低兼容版本、provider 名称和命令超时；缺失或非法配置会明确失败。
- 用数字版本比较校验当前 CLI 不低于最低兼容版本。版本不满足时不会构造执行命令。
- 运行 `opencode --version` 和 `opencode providers list`，只返回版本、退出码、provider 名称和“是否有输出”等安全诊断，不保存命令原始输出或凭证值。
- 通过 argv 数组构造 `opencode run --format json [--model ...] <prompt> --dir <workdir>`，不经过 shell；工作目录必须已存在。
- 用 `summarize_run` 把完成、失败、超时、退出码、输出字节数和 JSON 顶层事件类型归一为稳定摘要；失败会额外归一为安全的 `diagnosticCode`/`diagnosticHint`（例如 `log_access`、`provider_error`、`cli_protocol`），不把 provider 原始错误写入摘要。`run_prompt` 同时返回原始 stdout/stderr 和摘要，`write_run_evidence` 可将它们写入独立的 `run.json`、`stdout.txt`、`stderr.txt` 目录；`record_cli_run_evidence` 会把目录索引写入 Atlas execution record。CLI 完成后，Atlas 在同一隔离副本中重新运行任务声明的固定验证命令，并把每条命令映射为步骤状态、退出码、耗时和输出摘要。`POST /api/projects/:id/executions/:execution-id/cleanup` 提供显式清理入口，只删除已结束且已应用/无需应用的隔离工作副本，保留证据目录。文件隔离、差异审阅、应用和验收仍由 Atlas 负责。
- `application-atlas-production-pack/atlas_cli.py` 提供最小终端入口：默认只读展示项目、任务、执行、preflight 和 CLI 摘要；`--start` 才启动任务，`--cleanup` 才清理工作副本，`--lang en` 切换英文。它只调用 Atlas API，不绕过后端边界。
- `--interactive` 打开键盘优先的终端界面：方向键或 `j/k` 选择，`n` 新建任务，Enter 启动确认，`y/n` 确认或拒绝，`v` 查看运行摘要和验证命令，`a` 应用最新结果，`s` 停止活动 HTTP 执行，`p/f/w` 记录通过/失败/豁免验收，`x` 导出项目证据包，`c` 清理，`r` 刷新，`b` 返回项目列表，`q` 退出。

## 边界

这一层不替换既有 HTTP 会话执行链，CLI 通过执行请求中的显式 `transport: "cli"` 进入同步适配分支；默认 HTTP 路径保持不变，项目工作台在启动任务时提供执行方式选择。Atlas 已提供项目级 `GET /api/projects/:id/harness/preflight`，工作台和终端入口都展示版本、可执行文件和 provider 检查结果；启动执行前后端再次执行同一预检，失败时不创建隔离副本，并返回可操作的版本、provider 或路径诊断。CLI 执行结束时 Atlas 统一写入 `evidence.run_summary`、独立 `cli_run` 证据、固定验证步骤和清理索引；CLI 记录不提供 HTTP 会话续接。当前终端切片覆盖状态查看、项目/任务选择、启动确认、运行摘要与验证步骤查看、活动 HTTP 执行停止、结果应用、产品验收记录、项目证据包导出和显式清理；CLI 实时事件流、暂停接管和多任务并行仍不纳入本轮。

## 验证

适配器测试覆盖：

1. 通过版本和 provider 检查时仅生成安全证据；
2. 低于兼容线时返回 `version_incompatible`；
3. prompt 中含 shell 字符时仍按单一 argv 传递，并固定 `--dir`。

完整回归命令：`python3 -m unittest discover -s tests -p 'test_*.py'`（130 tests）。前端 `npm run typecheck` 与 `npm run build` 通过；启动前 API 已在实际项目工作区通过 OpenCode 1.18.31 复核；provider 失败、超时、运行摘要归一化、失败诊断码、CLI 隔离执行、固定验证步骤映射、证据落盘、execution record 索引、显式清理路径和终端入口的只读/显式变更边界也有回归覆盖。真实终端复测已验证 CLI 退出码 0、权限门、固定验证和清理；获准只读复测进一步验证了 `read`/`glob`/`grep` 工具调用、零文件变化和范围合规。TUI 启动/退出及项目/任务查看路径已通过，但仍不能替代完整端到端键盘路径。
