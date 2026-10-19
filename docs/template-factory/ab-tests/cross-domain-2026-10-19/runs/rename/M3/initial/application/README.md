# 单目录预览式批量重命名与撤销（本地 CLI）

一个只整理**一个明确指定的本地根目录**的命令行工具：先预览字面文本替换生成的
旧名→新名计划，显式确认后执行，并能安全撤销这一批改名。仅使用 Python 标准库，
无网络、无依赖安装、应用自身不调用 shell/子进程。

## 启动方式

运行时已固定为 **CPython 3.10**，只用标准库：

```bash
python3 app.py --root DIR list
python3 app.py --root DIR preview --find TEXT --replace TEXT --plan PATH [--hash]
python3 app.py --root DIR apply   --plan PATH --confirm
python3 app.py --root DIR undo    --receipt PATH --confirm
```

- `--root DIR` 必须位于子命令之前，且是已存在的目录；应用只操作该目录的**立即普通文件**。
- 成功后 stdout 恰好输出一个 JSON 对象；拒绝或失败时非零退出，错误信息在 stderr，
  stdout **绝不输出假成功 JSON**。
- 可选 `--hash` 让 `preview` 额外记录 sha256 内容证据（默认只记元数据，见 DECISIONS.md D01）。

## 存储

所有持久状态都放在根目录内的状态目录 `DIR/.atlas-renamer/`：

- 计划文件：由 `preview --plan` 指定，路径必须位于状态目录内。写入后不再改动
  （独占创建，已存在即拒绝）。JSON 为多行可读文本，含：
  `plan_id / find / replace / root / operations[{old,new,identity{dev,ino,size,mtime_ns,...}}]`。
- 回执文件：由 `apply` 生成，名为 `receipt-<plan_id>.json`，逐条记录 `old/new/identity`
  以及 `applied/completed/undone` 等标记，供后续独立进程执行 `undo` 与重复执行检测。
- 写入采用 `flush + fsync`，回执用临时文件 + 原子替换更新；这只是崩溃可见性的尽力而为，
  不是断电级恢复承诺（见 DECISIONS.md D05）。

## 行为契约

| 命令 | 成功输出 | 说明 |
| --- | --- | --- |
| `list` | `{"files":[{"name","size"}]}` | 仅立即普通文件；排除子目录、符号链接与 `.atlas-renamer` |
| `preview` | `{"status":"preview","operations":[{"old","new"}],"plan":PATH}` | 替换文件名中**全部**字面出现；不修改原文件；整批冲突在预览阶段整体拒绝 |
| `apply` | `{"status":"applied","operations":[...],"receipt":PATH}` | 需 `--confirm`；整批预检通过后逐条改名；回执供 undo |
| `undo` | `{"status":"undone"}` | 需 `--confirm`；只恢复本批次；遇新冲突或数据被改动即拒且不破坏 |

退出码：`0` 成功；非零表示拒绝或失败（错误说明在 stderr）。

## 安全不变式

- **不覆盖**：目标已存在、两个源指向同一新名、或新名落在本批次源文件名内（含 a↔b 环）
  时整体拒绝，零改动。
- **防过期**：计划携带源文件身份证据；预览与执行之间源文件被改动（内容/身份）即拒绝，
  且不产生部分改名。
- **防重复**：同一已执行计划再次 `apply` 不会产生第二轮改名。
- **撤销保护**：撤销时旧名被占用或已改名文件数据被改动即拒绝，绝不覆盖或删除现有数据。
- **边界**：`plan`/`receipt` 解析后必须位于 `DIR/.atlas-renamer` 内；拒绝绝对路径越界、
  `..` 穿越，以及经外部符号链接的状态目录或状态文件。

## 当前范围（P0，已实现）

字面查找/替换的 `list → preview → apply → undo` 完整闭环，含整批冲突预检、身份证据的
防过期与防重复、显式 `--confirm`、逐条回执，以及根目录/状态目录的路径边界。

## 已知限制

- 仅单个根目录的立即普通文件；不递归，不处理目录与符号链接，不接触根目录外文件。
- 查找为**非空字面文本**（非正则）；新名必须是单个文件名，禁止路径分隔符与目录穿越。
- 未使用 Linux 专有的 `renameat2`（`RENAME_NOREPLACE`/`RENAME_EXCHANGE`）：目标存在性
  预检与实际改名之间存在天然 TOCTOU 极小窗口（D03）。
- 换名环（a↔b）作为计划内部冲突整体拒绝，不做临时名两阶段交换（D04）。
- 跨文件系统改名不支持（EXDEV 拒绝）；NFS/SMB 等网络文件系统上“失败即未改名”不作保证（D02）。
- 无多轮 undo/redo 链、无可选备份、无大小写不敏感与 Unicode(NFC/NFD) 等价冲突的强保证。
- 状态文件的 fsync 与崩溃恢复为尽力而为，不承诺断电精确恢复（D05）。
- 无 GUI、无删除/回收站、无云、无多用户权限模型。
- 所有自检/验收状态为 `not_run`；生成阶段不执行任何程序，由独立操作者在受控环境运行。

## 后续路线（不在本次范围）

1. 可选唯一备份（`.bk`），不覆盖既有备份。
2. 显式开关支持递归、目录/符号链接/隐藏文件过滤。
3. 正则/模式驱动改名，与现有字面语义并存但默认关闭。
4. 多轮 undo/redo 链（由持久 journal 驱动）。
5. 跨平台大小写不敏感与 Unicode 规范化等价冲突检测。
6. 原子交换/换名环支持（平台特性可用时）。
7. 可选的 `--hash` 强制内容证据策略与更低时间戳分辨率文件系统适配。
