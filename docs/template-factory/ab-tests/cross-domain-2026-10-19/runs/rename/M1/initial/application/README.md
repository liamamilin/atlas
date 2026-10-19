# 下载目录的预览式批量重命名与撤销（单目录 CLI）

一个只依赖 Python 3.10 标准库的本地命令行工具：先在**单个明确指定的根目录**上预览
「文件名文字查找 → 替换」的结果，用户显式确认后整批改名，并能在之后用显式确认撤销这一次
改名。默认不递归、不处理目录与符号链接、不接触根目录之外的内容，任何冲突都拒绝整批而不是
覆盖或静默跳过。

## 运行环境

- CPython 3.10（实验统一解释器），仅标准库：`argparse`、`os`、`json`、`stat`、`time`。
- 无网络、无第三方依赖、无子进程、无凭据，也不需要安装任何东西。
- 入口：`python3 app.py --root DIR COMMAND ...`（在 `app/` 目录下运行）。

## 启动与用法

```bash
# 1) 列出根目录内的立即普通文件
python3 app.py --root /path/to/root list

# 2) 生成旧名到新名的计划（不改动原文件）；计划必须落在 ROOT/.atlas-renamer/ 内
python3 app.py --root /path/to/root preview \
    --find OLD --replace NEW \
    --plan /path/to/root/.atlas-renamer/plan-001.json

# 3) 显式确认后整批执行
python3 app.py --root /path/to/root apply \
    --plan /path/to/root/.atlas-renamer/plan-001.json --confirm

# 4) 再次 list 查看执行后的当前文件名
python3 app.py --root /path/to/root list

# 5) 显式确认后撤销这一次执行
python3 app.py --root /path/to/root undo \
    --receipt /path/to/root/.atlas-renamer/receipt-plan-001.json --confirm
```

成功时 stdout 恰好是一个 JSON 对象；帮助、错误与提示走 stderr；失败时以非零退出码结束，
且 stdout 不输出任何 JSON。退出码：`0` 成功，`1` 拒绝/操作失败，`2` 参数用法错误（argparse）。

## 存储布局

```
ROOT/
├── <用户文件…>                     # 仅操作这些立即普通文件
└── .atlas-renamer/                 # 内部状态目录，list 会排除它
    ├── plan-*.json                 # 不可变计划（创建后不覆盖）
    └── receipt-plan-*.json         # 执行回执，供后续进程 undo 与重复 apply 检测
```

计划 JSON 为多行可读文本，含 `version/created_at/root/find/replace` 与逐条
`{old,new,identity}`；`identity` 使用 `dev+ino+size+mtime_ns` 作为原始身份证据。
回执 JSON 复用同一份 operations，并记录 `status`（`applying`/`applied`/`undone`）与
已完成条目，因此可被独立的后续进程读取与撤销。

## 行为契约

- `list` → `{"files":[{"name":...,"size":...}]}`
  仅立即普通文件；排除子目录、符号链接与 `.atlas-renamer`；`size` 为真实字节数。
- `preview --find --replace --plan` → `{"status":"preview","operations":[{"old","new"}],"plan":...}`
  查找为非空字面文本（非正则），替换文件名中的**全部字面出现**；`--plan` 必须位于状态目录内；
  生成后原文件字节与文件名不变。
- `apply --plan --confirm` → `{"status":"applied","operations":[...],"receipt":...}`
  缺 `--confirm` 拒绝；执行前整批冲突预检并逐条核对源文件身份；重复执行同一已应用计划返回
  `{"status":"already-applied",...}` 且不再改名；陈旧计划（源内容或身份已变）被拒绝。
- `undo --receipt --confirm` → `{"status":"undone"}`
  缺 `--confirm` 拒绝；只恢复本批次；若旧名已被占用或文件数据已被改动，则拒绝且不覆盖、不删除；
  重复撤销被拒绝。

## 安全性质

- **不覆盖**：目标已存在、两个源指向同一新名、新名落在本批源集合内（含 a↔b 环）都在动手前整批拒绝。
- **不越界**：`--plan`/`--receipt` 解析后必须是 `ROOT/.atlas-renamer/` 的直接子项；拒绝绝对路径逃逸、
  经 `..` 的穿越，以及状态目录本身是外部符号链接的情形。
- **不假成功**：操作函数只在全批成功后返回；失败一律抛错，CLI 转为非零退出 + stderr，无 stdout JSON。
- **失败安全**：同文件系统内改名是元数据操作；执行/撤销中途系统调用失败时，尽力回滚本次已完成部分，
  并删除未完成的回执，避免把失败误记为成功。
- **不碰未选文件**：只对计划中列出的源文件改名；`list`/`preview` 不改动任何文件内容。

## 当前真实范围与限制

- 只处理**单个指定根目录**的**立即普通文件**；不递归、不处理目录与符号链接。
- 查找为字面文本，非正则；替换文本不得含路径分隔符；新名必须是单个合法文件名。
- 不实现 Linux 专有 `renameat2`（`RENAME_NOREPLACE`/`RENAME_EXCHANGE`）：执行期目标存在性预检与
  实际改名之间存在天然的极小 TOCTOU 窗口（已按 D03 用「整批预检 + 每步前再核查」缓解）。
- 换名环（如 a↔b）按计划内部冲突整体拒绝，不做临时名两阶段交换。
- 跨文件系统改名不支持（EXDEV 会失败并尽力回滚）；NFS/SMB 等网络文件系统上的失败语义不作保证。
- 陈旧判定默认只用 `dev/ino/size/mtime_ns`，不计算内容哈希（D01），存在极窄漏检窗口；
  计划/回执的 fsync 为尽力持久化，不承诺断电级精确恢复（D05）。
- 无 GUI、无删除/回收站、无多轮 undo/redo 链、无可选备份、无跨平台大小写/Unicode 等价冲突保证。

## 后续路线图（未实现）

1. 可选内容哈希与显式「允许覆盖」确认，缩小陈旧/TOCTOU 窗口。
2. 备份目录与多轮撤销/重做链。
3. 目录锁或平台原子替换能力，强化并发与免覆盖保证。
4. 大小写不敏感、Unicode NFC/NFD 等价与 `NAME_MAX` 校验。
5. 可选递归与正则模式（明确标注为超出当前单目录字面替换范围）。

## 自检状态

所有验收与自检均为 **not_run**。本包在生成阶段不执行任何程序；由独立操作者在其受控环境中
运行并记录结果。应用代码不提供任何测试专用端点，只通过上述公开 CLI 契约观察行为。
