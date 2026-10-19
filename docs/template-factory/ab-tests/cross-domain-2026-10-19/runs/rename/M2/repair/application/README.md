# 预览式批量重命名与撤销（单目录 CLI）

一个仅使用 Python 标准库的本地命令行工具：对**一个明确指定的目录**中的普通文件做
字面文本查找/替换，先预览不落盘改名，显式确认后执行，并能撤销这一次批量改名。

## 启动

需要 CPython 3.10（无第三方依赖）。

```bash
cd app
python3 app.py --root /path/to/assigned/dir list
```

`--root` 必须显式给出，且为该次操作的唯一边界；绝不会处理该目录之外的文件。
命令执行时的工作目录应是 `app/`（入口与模块同目录）。

## 命令与输出契约

- **stdout 只输出 JSON**；帮助、中文提示与错误走 stderr。
- 任何操作性失败都以非零退出码结束，并只输出错误，不产生“假成功”。

### list
```bash
python3 app.py --root DIR list
# {"files":[{"name":"a.txt","size":12}, ...]}
```
只列出**直接普通文件**，排除内部状态目录 `.atlas-renamer`、子目录与符号链接。

### preview
```bash
python3 app.py --root DIR preview \
  --find "IMG" --replace "照片" \
  --plan DIR/.atlas-renamer/plan-1.json
# {"status":"preview","operations":[{"old":"IMG1.jpg","new":"照片1.jpg"}],"plan":"..."}
```
- `--find` 为非空**字面**文本（不是正则）；`--replace` 可为空字符串（表示删除）。
- 只对文件名中包含 `--find` 的普通文件生成改名操作；不修改原文件。
- 计划路径必须位于 `DIR/.atlas-renamer/` 内；同名计划已存在时拒绝覆盖。
- 结果名不是合法单文件名（含 `/`、`\`、为空、`.`/`..`）、或与其他文件重名、
  或目标名已被占用时，**整份计划拒绝生成**。
- 计划以 UTF-8、`indent=2` 的多行 JSON 落盘，包含每个源文件的身份证据
  （`size`、`mtime_ns`、`sha256`），用于在 apply 时拒绝过期计划。

### apply
```bash
python3 app.py --root DIR apply --plan DIR/.atlas-renamer/plan-1.json --confirm
# {"status":"applied","operations":[{"old":"IMG1.jpg","new":"照片1.jpg"}],"receipt":".../receipts/<id>.json"}
```
- 缺少 `--confirm` 直接拒绝。
- 执行前逐项复核：源文件仍是普通文件、内容 `sha256` 与 `size` 与计划一致；
  任一目标名已存在则**整批拒绝且不做任何改动**；否则才逐项改名。
- 计划顶层的 `id` 会变成回执文件名，因此必须是安全单段令牌（生成值为十六进制）。
  被篡改为绝对路径、含 `/` 或 `..` 的 `id` 会在**任何改名之前**被拒绝，
  避免经不受信任字段把回执写到指定根目录之外。
- 中途失败会把已改的部分回滚，旧数据不丢失。
- 成功后写入回执（`DIR/.atlas-renamer/receipts/<plan-id>.json`），供后续进程撤销。
- 同一计划重复执行会被拒绝（回执已存在，或文件系统状态表明已执行）。

### undo
```bash
python3 app.py --root DIR undo --receipt DIR/.atlas-renamer/receipts/<id>.json --confirm
# {"status":"undone"}
```
- 缺少 `--confirm` 直接拒绝。
- 只恢复该回执记录的这一次批量改名，内容不动。
- 若恢复目标名现在已被占用，或当前文件内容/状态与回执不符，**拒绝且不覆盖任何已存在文件**。
- 已撤销过的回执再次撤销会被拒绝。

## 存储

运行期持久状态只在 `DIR/.atlas-renamer/` 下：

- `DIR/.atlas-renamer/<name>.json`：preview 生成的计划（不可覆盖）。
- `DIR/.atlas-renamer/receipts/<plan-id>.json`：apply 生成的回执（不可覆盖）。

计划/回执路径会校验落在状态目录内，并拒绝经由符号链接指向目录之外的路径。
`receipts/` 子目录同样要求是普通目录（非符号链接）并解析后仍位于根目录内；
所有由计划内容推导出的文件名（如计划 `id`）都按安全单段令牌校验。
任何写入都只会发生在指定根目录的 `.atlas-renamer/` 之下。

## 当前范围

- 单目录、默认不递归。
- 只处理普通文件；不处理目录与符号链接。
- 字面文本替换（非正则）。
- 一次执行对应一次撤销。

## 已知限制 / 不做的事

- 不做递归、批量多目录、删除/回收站、通配符或正则。
- 不做图形界面、云盘、并发锁与多用户协作。
- 不做大小写敏感的改名特例：为兼容本机（默认大小写不敏感）文件系统，
  结果名之间及与现有文件之间按大小写折叠判重，可能拒绝仅在大小写上不同的改名。
- 不做权限/所有者保留之外的特殊元数据处理（改名不改内容）。

## 后续路线（尚未实现）

- 可选递归深度与 `--glob` 过滤（需重新定义冲突与回滚范围）。
- 支持在一次会话中撤销多批（历史栈）。
- 支持正则模式作为显式子命令，与字面模式并存。
- 结构化 `--dry-run` 与机器可读的错误对象（当前失败仅 stderr 文本 + 非零码）。
