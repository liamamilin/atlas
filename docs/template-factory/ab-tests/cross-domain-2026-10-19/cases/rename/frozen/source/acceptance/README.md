# 下载目录的预览式批量重命名与撤销：验收程序说明

本目录只有两个文件：`acceptance/run.py`（唯一验收程序）与本说明 `acceptance/README.md`。本实验是**未发布的认知模板/验收程序，不是下游应用、不是可交付产品**。`run.py` 是独立可运行的 REAL 目标检查器，只观察被测应用公开的 CLI 行为，不导入、不实现、不读取被测应用代码。

## 一、依赖与环境

- 仅使用 Python 3 标准库（argparse、hashlib、json、os、shutil、stat、subprocess、sys、tempfile、uuid）：无需安装、无网络、无凭据、无第三方依赖、无编码归档。
- 被测目标是一份由操作者**新隔离提供**的 `app.py`，入口契约固定为 `python3 app.py --root DIR COMMAND ...`。
- 需要操作系统支持创建符号链接（A01/A11 的夹具与越界用例依赖它）。若当前环境无法创建符号链接，`run.py` 按**基础设施不完整**显式失败（退出码 2），绝不静默跳过或记为通过。
- 不支持的环境/参数模式（缺少 `--app`、`--app` 不是可读文件、`--root` 不是已存在且可写目录等）一律作为基础设施不完整显式失败（退出码 2）。

## 二、准备一次性夹具与隔离应用

1. 准备一份新隔离的 `app.py`（仅由操作者提供，入口为 `python3 app.py --root DIR COMMAND ...`；禁止使用真实下载目录相关代码或应用源码目录）。
2. 准备夹具根：
   - 显式传入 `--root PATH` 时，`run.py` 只在 `PATH` 下新建唯一子目录 `atlas-accept-<随机十六进制>` 作为夹具父目录，结束时删除；**不触碰 `PATH` 内其它任何内容**。
   - 缺省不传 `--root` 时，`run.py` 在系统临时目录创建 `atlas-accept-<随机>` 并自清理。
3. 夹具内容全部在运行期随机生成，不硬编码文件名或结果：普通文件、子目录、符号链接（指向根内与根外）、预置的冲突目标、根外诱饵文件/目录。
4. 夹具内会再建立一个一次性 `home/`，并把被测子进程的 `HOME`、`USERPROFILE`、`XDG_CONFIG_HOME`、`XDG_CACHE_HOME`、`XDG_DATA_HOME` 全部指向它，同时设置 `PYTHONDONTWRITEBYTECODE=1`、`PYTHONIOENCODING=utf-8`。**绝不使用真实 HOME/Downloads 或应用源码目录，也绝不回退到任何真实目录。**

## 三、运行命令

```bash
python3 acceptance/run.py --app /path/to/app.py [--root /path/to/disposable-root]
```

- `--app` 必填，指向操作者提供的新隔离应用入口；缺失或不指向可读文件时退出码 2。
- `--root` 可选，指向一次性可写目录；缺省则在系统临时目录自建自清理。
- 每条用例打印一行 `ID PASS|FAIL - 说明`；任一断言失败则整体退出非零。

示例：

```bash
# 使用系统临时目录作为夹具父目录（自建自清理）
python3 acceptance/run.py --app /tmp/renamer-app/app.py

# 使用指定的一次性根目录（在该目录下新建子目录，结束后删除）
python3 acceptance/run.py --app /path/to/app.py --root /path/to/disposable-root
```

## 四、`run.py` 的适配契约（必经接口）

`run.py` 不导入被测应用代码，只通过公开 CLI 观察用户可见行为：

- 以 `shell=False` 的子进程调用：`python3 <app.py> --root <fixture_root> COMMAND ...`；工作目录为夹具根；单条命令超时 60 秒。
- 每条命令：stdout **必须恰好是一个 JSON 对象**；中文帮助/错误/日志可走 stderr；**操作失败必须非零退出并给出错误说明，且 stdout 不得输出假成功 JSON**。
- 命令与预期输出：
  - `list` → `{"files":[{"name":...,"size":...}]}`，仅含立即普通文件，排除 `.atlas-renamer` 状态目录、子目录与符号链接；`size` 与真实字节数一致；退出码 0。
  - `preview --find TEXT --replace TEXT --plan PATH` → `{"status":"preview","operations":[{"old":...,"new":...}],"plan":PATH}`；计划写入 `DIR/.atlas-renamer/` 内且 `PATH` 必须位于该状态目录内；operations 应为把文件名中**全部字面查找串**替换为替换串后的旧名到新名；计划含逐条 old→new 与可核对的原始身份证据（至少 `dev`/`ino`/`size`/`mtime_ns`/`sha256` 之一）；预览不改动原文件。
  - `apply --plan PATH --confirm` → `{"status":"applied","operations":[...],"receipt":PATH}`；缺 `--confirm` 拒绝；执行前整批冲突预检；已应用/陈旧计划被拒；回执写入状态目录内，供后续进程 `undo` 与重复 `apply` 检测。
  - `undo --receipt PATH --confirm` → `{"status":"undone"}`；缺 `--confirm` 拒绝；遇新冲突或数据被改动时拒绝且不覆盖、不删除现有数据。
- 路径安全：`plan`/`receipt` 解析后必须位于 `DIR/.atlas-renamer` 内，拒绝绝对路径越界、经 `..` 的穿越与经外部符号链接的写入。
- `run.py` 自身退出码：`0` 全部用例通过；`1` 存在断言失败；`2` 基础设施不完整（缺 `--app`、目标不可用、无法创建夹具等）。

## 五、A01–A12 用例清单与双向映射

| 用例 | 断言要点 | 覆盖能力 |
| --- | --- | --- |
| A01 | `list` 仅返回立即普通文件、`size` 与真实字节数一致，排除 `.atlas-renamer`/子目录/符号链接，且不改动任何条目；退出码 0 | F01 |
| A02 | `preview` 在 `.atlas-renamer` 内生成含 identity 证据的计划，operations 与预期 old→new 一致；预览后原文件字节与文件名未变 | F02 |
| A03 | 空查找文本、替换串含路径分隔符、替换串含 `..` 目录穿越、新名解析后不是单个文件名：均非零拒绝、stderr 报错、无改动、不留下计划 | F02 |
| A04 | 目标已存在、两个源指向同一新名、新名落在源集合内（含环）：整批拒绝且零改名 | F04 |
| A05 | `apply --confirm` 成功并写入状态目录内可读回执，磁盘名与新名一致、内容不变、未选文件不受影响 | F05 |
| A06 | `apply` 缺 `--confirm` 非零拒绝、无改动 | F05 |
| A07 | 对同一已应用计划再次 `apply`：不产生第二轮改名（非零拒绝，或返回 0 且 status 含 `already`） | F06 |
| A08 | 预览后源内容被改，或因删除/更换为目录导致身份改变：判定陈旧并拒绝，无部分改名、无误报成功 | F03, F06 |
| A09 | `undo --receipt --confirm` 恢复本批次全部旧名，stdout 为 `{"status":"undone"}`，文件名与内容与执行前一致，未参与文件不受影响 | F07 |
| A10 | `undo` 缺 `--confirm` 拒绝；撤销时旧名被占用或数据被改动时拒绝且不覆盖、不删除 | F07 |
| A11 | `plan`/`receipt` 越出 `.atlas-renamer`（绝对越界、`..` 穿越、经外部符号链接状态目录），或执行/撤销使用被复制到状态目录之外的计划/回执：均被拒绝且不在根外写入或改名 | F08 |
| A12 | 执行冲突、计划不存在、回执不存在等失败：非零退出、stderr 报错、stdout 无假成功 JSON，既有文件与内容不丢失 | F09 |

反向映射（能力 → 用例）：

- F01 → A01
- F02 → A02、A03
- F03 → A08
- F04 → A04
- F05 → A05、A06
- F06 → A07、A08
- F07 → A09、A10
- F08 → A11
- F09 → A12
- P0（F01–F09 全体）→ A01–A12（全覆盖，无遗漏、无额外 P0 义务）

F10–F19 为已声明的 later/not-applicable 成熟扩展（递归、正则、可选备份、多轮撤销、跨平台大小写/Unicode 等价、原子交换、计费、多租户、审计与 GUI 等，`phase=null`、`acceptance=[]`），本阶段不验收，也不作为实现要求。

## 六、路径、凭据与不支持模式

- 应用路径与夹具根**均可配置**；`run.py` 不附加任何全局头、凭据或环境秘密值到夹具、子进程或任何外部导航，也不记录任何秘密值。本目标是本地文件 CLI，**不涉及网络、外部 URL 或认证凭据**，因此不存在需要注入的认证适配器；不得为此发明目标并不需要的认证模式。
- 不支持的认证/环境模式必须显式作为**基础设施不完整**失败（退出码 2），不得静默跳过或记为通过。
- 本工具只作用于显式指定的一次性夹具根，绝不接触真实 Downloads/HOME 或应用源码目录；演示只使用测试创建的普通文件。

## 七、生成阶段状态

- 本说明与 `run.py` 均在**生成阶段编写：未执行、未安装、未运行任何程序**。
- 所有验收状态（A01–A12、P0）均为 `not_run`。
- 验收由**独立操作者在受控环境**自行执行，并据实际退出码与输出记录结果；本程序不提供测试专用端点，也不伪造任何通过报告。