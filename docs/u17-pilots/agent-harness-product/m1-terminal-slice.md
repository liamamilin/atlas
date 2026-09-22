# M1：终端入口纵向切片

状态：已实现并完成当前范围验收；真实 CLI、获准只读工具调用、固定验证、证据保存、清理和完整只读 TUI 路径均已通过；单文件变更任务的执行、显式应用、独立验收和清理也已通过。停止和任务级超时链路已通过；失败恢复和回滚仍需另建任务验收。

`application-atlas-production-pack/atlas_cli.py` 是 Atlas 工作台的最小终端入口。它复用本地 API，不直接调用 OpenCode，因此执行边界与网页工作台一致：Atlas 负责项目状态、preflight、隔离工作副本、固定验证、差异审阅、应用和证据。

## 使用方式

```sh
# 查看项目；多个项目时会先列出可选 ID
python3 application-atlas-production-pack/atlas_cli.py --project <项目 ID>

# 显式启动一个 CLI 任务
python3 application-atlas-production-pack/atlas_cli.py \
  --project <项目 ID> --task <任务 ID> --start --transport cli

# 查看某次执行的摘要
python3 application-atlas-production-pack/atlas_cli.py \
  --project <项目 ID> --execution <执行 ID>

# 显式清理已结束的隔离工作副本；证据目录会保留
python3 application-atlas-production-pack/atlas_cli.py \
  --project <项目 ID> --execution <执行 ID> --cleanup

# 切换英文输出
python3 application-atlas-production-pack/atlas_cli.py --project <项目 ID> --lang en

# 打开键盘优先的交互界面
python3 application-atlas-production-pack/atlas_cli.py --interactive
```

默认调用只读取项目、工作区、任务、执行和 preflight，并明确提示只读模式。`--start` 和 `--cleanup` 是两个独立的变更开关；没有目标任务或执行 ID 时直接返回错误，不猜测用户意图。

交互模式中，方向键或 `j/k` 选择，`n` 新建任务，Enter 进入项目或启动确认，`y/n` 确认或拒绝，`v` 查看最新执行摘要与验证命令，`a` 应用最新的已完成结果，`s` 停止活动 HTTP 执行，`p/f/w` 分别记录通过、失败或豁免验收，`x` 导出当前项目证据包，`c` 清理选中任务的最新执行副本，`r` 刷新，`b` 返回项目列表，`q` 退出。启动、停止、应用、验收、导出和清理前都会再次显示确认提示；应用前后仍由后端核对基线和范围。

## 本轮范围

- 已覆盖：项目/任务创建与选择、OpenCode preflight、CLI 运行摘要、退出码和超时、证据目录、固定验证结果、验证步骤查看、活动 HTTP 执行停止、显式应用、产品验收记录、项目证据包导出、显式清理，以及键盘优先的任务确认。
- 已覆盖：中文默认、英文切换，以及不依赖网页的脚本化调用。
- 暂不覆盖：实时事件流、暂停后 take-over、多任务并行、CLI 会话续接。

## 验收证据

- `tests/test_reliability.py` 中的 `AtlasCliTests` 验证默认只读，以及启动/清理必须显式请求。
- 完整后端回归为 130 项；前端类型检查和生产构建保持通过。
- 真实验收任务 `tsk_4aa41e37e50448388589db2b2f9081c9` 已验证 preflight 和固定验证；OpenCode CLI 因受限环境无法打开本机日志而退出码 1，证据与失败验收记录已保留，不能据此宣称端到端通过。
- 随后的授权复测 `exe_4db1bd533d8e45259adefcb626da72d7` 已验证 CLI 退出码 0、权限门、固定验证、证据保存和清理；OpenCode 的 bash 检查因未获允许而被拒绝，因此仍不宣称工具调用完整成功。
- `atlas_cli.py --interactive --lang zh` 已复核项目选择、任务启动确认、运行详情、产品验收、导出、清理和退出（退出码 0）；标准 PTY 不支持 `curses.curs_set(0)` 时已安全降级，并修复任务视图 `task_index` 闭包错误。变更任务的停止链路已通过；失败恢复和回滚路径另列为后续验收范围。
- CLI 任务仍由后端执行 `opencode --version`、`providers list`、隔离副本和固定验证命令，终端入口本身不保存或处理 provider 原始输出。
