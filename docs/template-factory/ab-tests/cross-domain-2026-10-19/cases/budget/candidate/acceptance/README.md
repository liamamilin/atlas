# 验收说明：个人月度预算与消费前剩余额度

本目录的 `acceptance/run.py` 是针对**真实目标**的独立验收检查器，覆盖固定范围 P0 的 A01–A14。它不是被检应用：不实现业务逻辑、不安装依赖、不使用 mock 目标响应、不执行任意用户命令。

> 生成阶段未运行任何程序：所有用例状态均为 `not_run`，实际执行由独立操作员在隔离的真实目标上完成（见文末「生成声明」）。

## 1. 环境要求

- Python 3，仅使用标准库（`argparse`/`csv`/`io`/`json`/`os`/`re`/`socket`/`subprocess`/`sys`/`time`/`uuid`/`datetime`/`decimal`/`urllib`）。
- 无需安装或构建，无第三方依赖，无外部资源/CDN。
- 被检应用需已启动，或可由 `--app-path` 指向其入口 `app.py`。
- 货币固定人民币（CNY），金额一律为两位小数字符串（如 `"0.10"`）。

## 2. 启动被检应用

被检应用是本范围的本地单机服务，仅绑定 `127.0.0.1`，全部持久化数据只写入 `--data-dir`：

```bash
python3 app.py --port 8000 --data-dir /path/to/data-dir
```

`GET /` 提供可用中文 UI，与 JSON API 共用同一真实状态。UI 必须提供契约中的 `data-testid` 控件：`month`、`category-name`、`category-budget`、`category-save`、`expense-date`、`expense-category`、`expense-amount`、`expense-note`、`expense-save`；分类选择项 `value` 等于 `category_id`。先设置 `month` 等待状态加载，`category-save` 建分类，`expense-save` 记账。

## 3. 运行验收程序

两种目标参数用法互斥，只能选择一种；`--month` 可选，默认当月。

### 3.1 Web 模式（`--target-url`）

```bash
python3 acceptance/run.py --target-url http://127.0.0.1:8000 --month 2026-10
```

- `--target-url` 必须是**精确 origin**（不含 path/query/fragment），scheme 仅 `http`，主机仅限 loopback（`127.0.0.1`/`localhost`/`::1`）。
- 携带内嵌凭据（`user:pass@`）的 URL 会在**发起任何请求前**以配置错误退出；该目标不需要认证，因此不引入任何可选认证适配层。
- 跨源重定向在**传输层**被拒绝：仅当重定向目标的 scheme/host/port 与给定目标完全一致时才继续，否则判为失败；同时显式禁用环境代理，避免请求被路由到目标 origin 之外。
- 所有请求只发往给定 origin；错误信息对 `//user:pass@` 形式做脱敏，不回显凭据。

### 3.2 CLI 模式（`--app-path` + `--data-root`）

```bash
python3 acceptance/run.py \
  --app-path /abs/path/to/app/app.py \
  --data-root /abs/path/to/owned-disposable-root \
  --month 2026-10
```

- `--app-path` 必须指向名为 `app.py` 的被检应用入口；`--data-root` 必须是**已存在**的、操作员自有的可弃用受控临时根目录，且不得是 `HOME` 或文件系统根，也不得包含被检应用目录。
- 检查器在 `127.0.0.1` 上取空闲端口，并以 `subprocess.Popen([sys.executable, app_path, "--port", PORT, "--data-dir", data_dir], shell=False)` 启动应用，`cwd` 为 `app.py` 所在目录，标准流置空。
- 该模式额外完整验证 A10：先做月份隔离断言，再在同一 `--data-dir` 上**重启**被检应用并核对当月状态保留，同时确认被检应用目录没有越界写入、`--data-root` 中确有持久化数据。
- 不执行安装，不调用任意命令，不使用真实 `HOME`/Downloads 等用户目录。

## 4. 用例 A01–A14

| 用例 | 类型 | 含义与预期可观察行为 |
| --- | --- | --- |
| A01 | 正例 | `GET /` 返回 200 `text/html` 中文界面，含全部 `data-testid` 控件且引用 `/api/state`；`GET /api/state?month` 返回该月实时状态，`totals` 与分类汇总自洽。 |
| A02 | 正例 | 通过 UI 控件与 `POST /api/categories` 建立分类与月预算；`state` 中该分类 `budget="100.00"`、`spent="0.00"`、`remaining` 等于预算。 |
| A03 | 负例 | 同一月份重复名称创建分类返回**非 2xx 且 JSON 含 error**，且不产生隐藏的第二条分类。 |
| A04 | 正例 | 记录含日期/分类/金额/备注的支出后，`state.transactions` 含该笔且字段精确；分类 `spent`/`remaining` 与整月 `totals` 一致重算。 |
| A05 | 负例 | 非正数（`0`、`0.00`、`-1.00`）或超过两位小数（`1.234`、`10.000`）以及非数字金额被拒绝（非 2xx JSON）；分类预算同样拒绝非法金额；既有数据与汇总保持原样，不静默取整或裁剪。 |
| A06 | 负例 | 交易日期与分类所属月份不一致时被拒绝（非 2xx JSON），既有数据不变。 |
| A07 | 正例 | 分类与整月 `budget`/`spent`/`remaining`/`totals` 计算正确；未使用分类仍可见（`spent="0.00"`）；超支显示负 `remaining`，且继续记账不被阻止、`spent` 继续累计。 |
| A08 | 正例 | `PUT`/`DELETE /api/transactions/{id}` 后，交易列表与分类/整月汇总即时一致地重算。 |
| A09 | 负例 | 对不存在或非法 `id` 的 `PUT`/`DELETE`（交易与分类）返回非 2xx JSON，原有记录保持不变。 |
| A10 | 正例 | 不同月份数据互相隔离（各月交易列表只含当月）；CLI 模式下同一 `--data-dir` 重启后数据保留，数据仅写入指定目录（应用目录无越界写入，`--data-root` 有持久化文件）。 |
| A11 | 正例 | `GET /api/export?month` 返回 200 UTF-8 CSV，含表头 `date,category,amount,note` 与当月行；中文、字段内引号与换行按 RFC 4180 往返可解析（重新序列化后仍可解析一致）。 |
| A12 | 正例 | `PUT /api/categories/{id}` 更新目标月预算，且不误改其他月份的同名分类。 |
| A13 | 正例 | UI 与 JSON API 共用同一真实状态：UI 读取 `/api/state`；新增支出后界面/内嵌状态数字与 API 一致，`remaining = budget − spent` 自洽。 |
| A14 | 负例 | API 校验失败返回非 2xx JSON 错误说明；UI 提供可理解的失败反馈区域，且不破坏旧数据。 |

## 5. 标准输出与退出码

标准输出：

- 首行：`目标模式：<http|file>；月份：<YYYY-MM>`。
- 每个用例一行：`Axx STATUS 描述`，`STATUS` 为 `PASS`/`SKIP`/`FAIL`/`ERROR`；`FAIL`/`ERROR` 追加 `| 详情`。
- 末行：`结果：通过 X / 跳过 Y / 失败 Z`。

退出码：

- `0`：无 `FAIL`/`ERROR`（全部通过；Web 模式下 A10 通过隔离断言后因无法验证重启/仅写指定目录而记为 `SKIP`，不计失败）。
- `1`：存在 `FAIL`/`ERROR`，或 CLI 模式下被检应用启动失败（`[启动失败]`）。
- `2`：配置错误（参数或目标不合法，在任何请求前退出，`[配置错误]` 打印到 stderr）。

## 6. 隔离与安全约束

- 仅合成本地演示数据：用例以随机运行标记生成唯一分类名与备注，不使用真实用户数据或凭据。
- 不记录任何敏感值：日志与错误信息不含凭据；`--target-url` 若含内嵌凭据会在请求前被拒绝，错误信息对凭据形式做脱敏。
- 仅 loopback：主机限 loopback、scheme 限 `http`；显式禁用环境代理；跨源重定向在传输层被拒；不豁免任意 loopback 来源或端口，只接受给定 origin。
- 仅受控目录：CLI 模式只接受显式 `--app-path` 与自有可弃用 `--data-root`，`shell=False`，不写入其他位置；被检应用数据只写入 `--data-dir`。
- 不安装依赖、不访问外部网络、不访问任意文件、不启动子进程（CLI 模式除外：仅显式启动被检 `app.py`）。

## 7. 生成声明

生成阶段未运行任何程序：`acceptance/run.py` 与本说明均未在真实或模拟目标上执行，未被安装，也未伪造通过结果。所有 P0 用例（A01–A14）状态均为 `not_run`；实际执行由独立操作员在隔离的真实目标上完成。