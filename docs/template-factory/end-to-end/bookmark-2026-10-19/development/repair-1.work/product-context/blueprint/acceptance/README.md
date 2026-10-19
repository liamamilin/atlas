# 验收套件运行说明（acceptance/README.md）

本目录是「生活待购与灵感收藏夹」的**独立验收套件**，按 `atlas.acceptance-runner.v1` 协议对**真实 HTTP 目标**逐例执行行为断言。**本套件不实现应用**；前提是应用已按 `source/SPECIFICATION.json` 的架构与 HTTP/UI 契约实现并正在运行，其监听地址由 `--base-url` 提供。上传的元数据不提供测试命令。

## 1. 目标适配器与运行环境

- **目标适配器**：唯一目标是由 `--base-url` 指定的真实 HTTP(S) 服务，例如 `--base-url http://127.0.0.1:8000`。所有用例经标准库 `http.client` + `http.cookiejar`（`acceptance/common.py` 的 `HttpTarget`）发送真实请求、提交真实表单并解析真实 HTML 响应。
- **绝不使用 mock**：不内置假响应、不 stub 目标、不以固定 fixture 替代行为；断言只依据目标的真实响应。
- **运行环境**：仅 Python 3 标准库（`http.client`、`http.cookiejar`、`html.parser`、`json`、`urllib` 等），**无第三方依赖**，因此**不提供 requirements 清单**，运行期也不得安装任何包。
- **无外网**：运行期不访问互联网；用例只与 `--base-url` 通信。A08 只断言 `GET /go/<id>` 的 302 `Location` 指向所存 URL，**不跟随**该外部跳转。
- **不假设浏览器**：不依赖 Playwright 或任何浏览器；全部 Web 用例由标准库 HTTP 客户端驱动服务端渲染 HTML 表单完成。若某能力确实需要浏览器，用例必须显式报告 unavailable，绝不伪造 UI 成功。

## 2. 套件文件

| 文件 | 作用 |
| --- | --- |
| `acceptance/common.py` | 共享库与目标适配器：`HttpTarget`、`parse_forms`、`parse_list`、`Assertions`、`Ctx`、`main`、`fail_explicit`。导入无副作用，不联网、不打开任何应用数据库。 |
| `acceptance/p0_core.py` | P0 捕获与归类用例（A01–A05）。 |
| `acceptance/p0_find.py` | P0 检索、打开与持久化用例（A06–A10）。 |
| `acceptance/p0.py` | P0 薄聚合器与可执行入口（A01–A10）。 |
| `acceptance/p1.py` | P1 整理与维护用例（A11–A18）。 |
| `acceptance/p2.py` | P2 互操作与可选增强用例（A19–A25）。 |
| `acceptance/runner.json` | 冻结的 Atlas runner 绑定（最后生成，内容精确，不含任何结论或覆盖信息）。 |

每个阶段脚本都以 `__file__` 定位套件根并 `sys.path.insert(0, <suite_root>)`，因此即使工作目录不是 `/suite`，`python /suite/acceptance/p0.py` 也能正确导入 `acceptance.common`。

## 3. 精确命令与标志

通用标志：

| 标志 | 必填 | 说明 |
| --- | --- | --- |
| `--case` | 是 | 用例 ID（A01–A25 之一）。未知或缺失时显式非零失败。 |
| `--base-url` | 是 | 目标真实 HTTP(S) 基址，例如 `http://127.0.0.1:8000`。带凭据的 URL 不受支持。 |
| `--data-dir` | 否 | tester 的可写草稿目录（见 §5），缺省时使用临时目录。 |
| `--app-root` | 否 | 只读应用源码目录；本套件不重启进程，故一般无需提供。 |

逐例命令（`{base_url}` 与 `{data_dir}` 由 Atlas runner 注入到对应位置）：

```bash
# P0：A01–A10
for c in A01 A02 A03 A04 A05 A06 A07 A08 A09 A10; do
  python /suite/acceptance/p0.py --case "$c" --base-url http://127.0.0.1:8000 --data-dir /state
done

# P1：A11–A18
for c in A11 A12 A13 A14 A15 A16 A17 A18; do
  python /suite/acceptance/p1.py --case "$c" --base-url http://127.0.0.1:8000 --data-dir /state
done

# P2：A19–A25
for c in A19 A20 A21 A22 A23 A24 A25; do
  python /suite/acceptance/p2.py --case "$c" --base-url http://127.0.0.1:8000 --data-dir /state
done
```

单个用例即一次独立进程：stdout **恰一个** `atlas.acceptance-result.v1` JSON 对象，诊断写 stderr。退出码约定：`0` 全部断言通过；`1` 存在失败断言；`2` 基础设施/装配失败（缺少或未知标志、无法连接目标等）。完整结果必须保持在 64000 字符以内，超限被截断的结果不能判通过。

结果示例：

```json
{"schema":"atlas.acceptance-result.v1","case_id":"A01","status":"passed","assertions":[{"id":"behavior-1","passed":true,"detail":"POST /bookmarks 303 后 GET /?collection=<id> 列表出现该记录，标题/URL/归类与提交值一致"}]}
```

## 4. 启动证据与行为证据

- **启动证据**：目标在 `--base-url` 可达（能建立连接并取回 HTML）。这只证明服务在运行。
- **行为证据**：每个用例提交真实请求/表单，并根据响应断言具体可观察行为（记录出现、归类隔离、关键字命中/不命中、`/go/<id>` 302 `Location`、400/404 负例、导入导出内容等）。只有行为断言全部通过才判 `passed`。
- 本套件**不把“服务可连接”当作“功能已实现”**，也不做标题/文件存在性检查充当行为验证。

## 5. data_dir 与持久化的边界

- `--data-dir` 仅是 tester 在 `/state` 下的可写草稿目录（用于导入导出等临时文件）；**绝不**把它当作应用数据库，**绝不**打开或读取应用的 SQLite。
- 本套件**不重启进程**。A09 只以“保存记录后由一个全新、无会话 HTTP 客户端读回该记录”作为服务端已持久保存的佐证，它**不证明进程重启**。
- **进程重启耐久性标记为未验证**，由独立浏览器验收覆盖；本套件不得声称已完成重启，也不得为此判 `passed`。
- 不重启的原因来自宿主隔离契约：Web 验收程序只与目标共享网络访问，不能假定能启动或停止应用进程。

## 6. 离线限制与“不可用即显式报告”

- 运行期无外网。需要外部网络的增强能力在离线环境下必须显式报告 unavailable/未验证，**绝不伪报通过**：
  - A22：元数据抓取默认关闭，保存不触发外发请求；即使启用，指向私网或回环地址的抓取也以安全错误（4xx）拒绝。
  - A23：无外网下失效链接检查明确报告 unavailable/未验证，且不改动记录本身。
  - A24：未配置存档能力时请求网页副本，返回明确的未实现/不可用，不伪造也不返回空的存档内容。
- 无法连接目标、缺少必需标志、出现未知 case 等一律显式非零失败，绝不静默跳过或判定通过。

## 7. runner.json 与 Atlas 执行方式

`acceptance/runner.json`（`schema` 为 `atlas.acceptance-runner.v1`，`result_schema` 为 `atlas.acceptance-result.v1`）为每个规范用例 A01–A25 **恰好绑定一次**：

```json
{"schema":"atlas.acceptance-runner.v1","result_schema":"atlas.acceptance-result.v1","cases":{"A01":{"args":["--case","{case_id}","--base-url","{base_url}","--data-dir","{data_dir}"]}}}
```

其余每个条目结构相同，均形如 `{"args":["--case","{case_id}","--base-url","{base_url}","--data-dir","{data_dir}"]}`。实现文件由 `SPECIFICATION.json` 的 `acceptance[].implementation` 决定：A01–A10 → `acceptance/p0.py`，A11–A18 → `acceptance/p1.py`，A19–A25 → `acceptance/p2.py`。绑定只含字面量与 `{base_url}`、`{data_dir}`、`{case_id}` 占位符，不含任何结论或覆盖信息。

Atlas 按 `runner.json` 逐例调用：为每个 case 注入真实 `{base_url}` 与可写 `{data_dir}`，执行一次独立进程，读取 stdout 的单个 `atlas.acceptance-result.v1` JSON，并以退出码判定通过与否。

## 8. 应用交付示例（根 delivery.json）

前提是应用已按 `SPECIFICATION.json` 实现（本任务不实现应用）。下面的 `delivery.json` 放在应用仓库根，供 Atlas 启动真实目标；`runtime.profile` 必须取支持的合法值之一（`python-web`、`node-web`、`static-web`、`cli`），本应用为 `python-web`。启动命令是**字面量 argv 数组**，其中的 `--port`、`--data-dir` 不会被占位符插值。

```json
{
  "schema": "atlas.application-delivery.v1",
  "root": ".",
  "runtime": {
    "profile": "python-web",
    "install": [],
    "build": [],
    "start": ["python3", "-m", "app", "--port", "8000", "--data-dir", "./state"],
    "port": 8000
  },
  "source_files": [
    "app/__init__.py",
    "app/__main__.py",
    "app/server.py",
    "app/storage.py",
    "app/views.py"
  ]
}
```

说明：

- `install` 与 `build` 均为空数组，因为应用只用 Python 3 标准库，无第三方依赖、无构建步骤。
- `start` 是字面量 argv，由宿主直接执行；运行期不访问外网。`--data-dir ./state` 为固定的交付示例值，实际部署须保证启动工作目录下 `./state` 可写且为**应用的持久数据目录**（可整目录备份），它不是 tester 的 `{data_dir}`。
- `source_files` 为应用自身交付清单中声明的源码文件；本验收任务不生成也不修改其中任何一个。
- 应用源码保持只读，只有数据目录可写；服务只监听本地端口，不暴露到公网。

## 9. 前提与范围

- 本套件**不实现应用**，不复制以往书签应用的实现或测试代码，也不导入被验收应用的任何测试结论。
- 断言严格基于 `SPECIFICATION.json` 冻结的路由、表单字段、错误契约与 `data-*` 适配属性：捕获表单 `POST /bookmarks`（`url`/`title`/`collection_id`）、新建归类 `POST /collections`（`name`）、移动 `POST /bookmarks/<id>/move`、打开原页 `/go/<id>`（302）、按归类/关键字浏览 `GET /?collection=&q=`，列表项 `li.bookmark[data-bookmark-id]` 与归类项 `li.collection[data-collection-id]`。
- 目标无认证需求，套件不发明任何认证适配器，也不接受或记录任何凭据；诊断信息中的 URL 授权段会被移除。
- 验收程序在冻结后独立于下游应用，且不会修改本套件。
