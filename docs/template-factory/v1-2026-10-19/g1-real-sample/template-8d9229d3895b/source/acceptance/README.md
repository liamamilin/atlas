# 生活待购与灵感收藏夹 — 验收运行说明

本目录是一套独立、冻结的验收套件，用真实 HTTP 目标验证 python-web 应用。它不包含应用实现，不导入应用代码，也不读取应用自己的测试判定；本文档只是运行说明，不代表任何用例已经执行或通过。

## 1. 目标适配器

| 参数 | 适用范围 | 用途 |
| --- | --- | --- |
| `--base-url` | A01–A15（全部） | 已部署 python-web 实例的 http/https 根 URL；所有 base_url 行为断言都发往该 origin。 |
| `--app-root` | A01、A05、A09 | 只读应用源码根；必须包含 `app/serve.py`，用于启动同一冻结应用的隔离实例。 |
| `--data-dir` | A01、A05、A09、A14 | 测试者可变草稿根；重启适配器在其 `instances/` 下创建每实例目录；A14 在此生成导入 HTML。 |

### 1.1 `--base-url`

- 示例：`http://127.0.0.1:8000`。必须是 http 或 https；不要包含用户名、口令、查询串或片段。
- 验收目标声明无认证；套件不会把凭据放入 URL、请求头、日志或 fixtures。
- 每个请求都绑定到该精确 origin（scheme、hostname、port），不会放行任意 loopback 主机或端口。

### 1.2 `--app-root`、`--data-dir` 与每实例隔离

- `--app-root` 是只读源码，必须存在 `<app_root>/app/serve.py`。套件只读取和启动它，不修改它，也不读取应用的自测判定。
- `--data-dir` 只是测试者的草稿根目录，必须可写，且不得等于 `--app-root` 或 `/`。
- `launch_app` 在 `<data_dir>/instances/` 下创建 `<uuid>/`，并把该子目录作为应用 `--data-dir`。应用数据库（如 `bookmarks.sqlite3`）位于实例子目录内；宿主 `<data_dir>` 根目录绝不作为应用数据库。
- 需要重启的用例复用第一次的实例子目录；日志写到 `<data_dir>/instances/<uuid>/logs/app-*.log`。
- A14 在 `<data_dir>` 根写入 `import-<token>.html`，仅作为 `/api/import` 的输入；它不是数据库，也不代表目标响应。

### 1.3 重启持久化适配器

A01、A05、A09 使用以下真实进程适配器（cwd 为 `app_root`）：

`[当前 Python 解释器 (sys.executable), "<app_root>/app/serve.py", "--host", "127.0.0.1", "--port", "<free_port()>", "--data-dir", "<data_dir>/instances/<uuid>"]`

- 启动时移除代理环境变量，stdout/stderr 写入实例日志；轮询 `GET /api/health`，仅当返回 200 且 JSON 对象时视为就绪（默认 30 秒）。
- 对隔离实例执行真实创建/移动/删除等动作，然后 `stop_app`（SIGTERM，超时后 SIGKILL），再以相同实例子目录启动同一冻结应用，读回并断言行为。
- 该重启证据只证明从 `app_root` 启动的隔离实例可持久化，不证明 `--base-url` 指向的已部署实例可重启。若外部目标只读且不可重启，重启部分必须显式报告未验证或失败，不能以健康检查或新进程替代。

## 2. 运行时要求与依赖

- 交付 profile：`python-web`。
- Python 3.12；仅使用标准库（`http.server`、`sqlite3`、`urllib`、`json`、`html.parser` 等）。
- `install` 为空：不执行 `pip`，不访问包索引；`requirements.txt` 声明无第三方包。
- `build` 为空：无 npm、Node、Playwright、浏览器库、前端构建或截图步骤。
- 每个程序用 `os.path.dirname(os.path.abspath(__file__))` 自举 `sys.path`，不依赖工作目录。下面的示例假定套件位于 `/suite/acceptance`；若实际路径不同，只替换路径，不要改变参数。
- 目标不需要认证；`HttpClient` 不附加全局凭据头，并拒绝 `Authorization`/`Proxy-Authorization`。若目标要求认证（例如健康检查 401/403），程序按基础设施未就绪显式失败，不实现登录适配器，不跳过或伪造通过；错误输出会对 URL 中的凭据和敏感查询参数做脱敏。

## 3. 文件与用例分组

| 文件 | 内容 |
| --- | --- |
| `acceptance/common.py` | 共享参数解析、同源 HTTP 客户端、断言记录、结果输出、健康轮询、隔离实例启动/停止与重启适配器。 |
| `acceptance/p0_library.py` | A01、A02、A03、A11。 |
| `acceptance/p0_organize.py` | A04、A05、A06、A12。 |
| `acceptance/p0_find_open.py` | A07、A08。 |
| `acceptance/p0_recovery.py` | A09、A10。 |
| `acceptance/p1_maturity.py` | A13、A14、A15。 |
| `acceptance/requirements.txt` | 无第三方依赖的声明；安装步骤为空。 |
| `acceptance/runner.json` | `atlas.acceptance-runner.v1` 独立绑定，列出 A01–A15 各一次。 |

## 4. 逐用例精确参数与调用示例

`acceptance/runner.json` 的唯一作用是为 Atlas 提供每个用例的 argv；实现程序由固定 spec 选择。所有用例都必须带 `--base-url`，A01/A05/A09 还必须带 `--app-root` 与 `--data-dir`，A14 还必须带 `--data-dir`。未知或缺失参数由参数解析器显式报错并非零退出。

### 4.1 与 runner.json 一致的 args

| 用例 | 程序 | args |
| --- | --- | --- |
| A01 | `p0_library.py` | `["--case","A01","--base-url","{base_url}","--app-root","{app_root}","--data-dir","{data_dir}"]` |
| A02 | `p0_library.py` | `["--case","A02","--base-url","{base_url}"]` |
| A03 | `p0_library.py` | `["--case","A03","--base-url","{base_url}"]` |
| A11 | `p0_library.py` | `["--case","A11","--base-url","{base_url}"]` |
| A04 | `p0_organize.py` | `["--case","A04","--base-url","{base_url}"]` |
| A05 | `p0_organize.py` | `["--case","A05","--base-url","{base_url}","--app-root","{app_root}","--data-dir","{data_dir}"]` |
| A06 | `p0_organize.py` | `["--case","A06","--base-url","{base_url}"]` |
| A12 | `p0_organize.py` | `["--case","A12","--base-url","{base_url}"]` |
| A07 | `p0_find_open.py` | `["--case","A07","--base-url","{base_url}"]` |
| A08 | `p0_find_open.py` | `["--case","A08","--base-url","{base_url}"]` |
| A09 | `p0_recovery.py` | `["--case","A09","--base-url","{base_url}","--app-root","{app_root}","--data-dir","{data_dir}"]` |
| A10 | `p0_recovery.py` | `["--case","A10","--base-url","{base_url}"]` |
| A13 | `p1_maturity.py` | `["--case","A13","--base-url","{base_url}"]` |
| A14 | `p1_maturity.py` | `["--case","A14","--base-url","{base_url}","--data-dir","{data_dir}"]` |
| A15 | `p1_maturity.py` | `["--case","A15","--base-url","{base_url}"]` |

### 4.2 调用示例

变量仅为占位，实际值由 Atlas 注入；`python3` 必须是 Python 3.12。

```sh
BASE_URL="http://127.0.0.1:8000"
APP_ROOT="/path/to/frozen/app"
DATA_DIR="/state/acceptance-data"

python3 /suite/acceptance/p0_library.py --case A01 --base-url "$BASE_URL" --app-root "$APP_ROOT" --data-dir "$DATA_DIR"
python3 /suite/acceptance/p0_library.py --case A02 --base-url "$BASE_URL"
python3 /suite/acceptance/p0_library.py --case A03 --base-url "$BASE_URL"
python3 /suite/acceptance/p0_library.py --case A11 --base-url "$BASE_URL"
python3 /suite/acceptance/p0_organize.py --case A04 --base-url "$BASE_URL"
python3 /suite/acceptance/p0_organize.py --case A05 --base-url "$BASE_URL" --app-root "$APP_ROOT" --data-dir "$DATA_DIR"
python3 /suite/acceptance/p0_organize.py --case A06 --base-url "$BASE_URL"
python3 /suite/acceptance/p0_organize.py --case A12 --base-url "$BASE_URL"
python3 /suite/acceptance/p0_find_open.py --case A07 --base-url "$BASE_URL"
python3 /suite/acceptance/p0_find_open.py --case A08 --base-url "$BASE_URL"
python3 /suite/acceptance/p0_recovery.py --case A09 --base-url "$BASE_URL" --app-root "$APP_ROOT" --data-dir "$DATA_DIR"
python3 /suite/acceptance/p0_recovery.py --case A10 --base-url "$BASE_URL"
python3 /suite/acceptance/p1_maturity.py --case A13 --base-url "$BASE_URL"
python3 /suite/acceptance/p1_maturity.py --case A14 --base-url "$BASE_URL" --data-dir "$DATA_DIR"
python3 /suite/acceptance/p1_maturity.py --case A15 --base-url "$BASE_URL"
```

## 5. 每个用例断言的行为

| 用例 | 行为证据 |
| --- | --- |
| A01 | 先对 base_url 健康检查、保存并读回；再从 app_root 启动隔离实例，保存后停止、以同一实例子目录重启，断言 id 与 url 不变。 |
| A02 | 缺协议、`javascript:`、`ftp://`、无点域名四类 URL 均返回 400 `invalid_url`；以本用例唯一 URL 标记的相对计数断言列表未新增。 |
| A03 | 预置归类（未整理、待购、家居改造、以后看看）可见；缺省 category 落入未整理；新归类名保存后自动创建且可按该归类检索。 |
| A04 | 新建 201/可见、同名及大小写变体 409 `duplicate_category`、PATCH 重命名、DELETE 归类后记录回到未整理；默认归类重命名/删除返回 400 `protected_category`。 |
| A05 | base_url 上移动后仅新归类可见；隔离实例中移动、停止、同子目录重启后归属仍保留。 |
| A06 | 两个归类各两条记录，按归类过滤的结果精确等于本归类集合，且 `/api/categories` 的 count 与实际条数一致。 |
| A07 | 标题、hostname、description 的子串分别命中且大小写不敏感；category 与 q 叠加；无匹配返回 200 空数组。 |
| A08 | `GET /go/{id}` 不跟随重定向，302 的 Location 等于保存 URL；未知 id 返回 404 `not_found`；读回 URL 未被改写。 |
| A09 | base_url 删除后默认列表排除、`include_trashed=1` 可见、restore 后 url/title/description/category 恢复；隔离实例删除跨重启保持。 |
| A10 | 未知 id 的 GET/PATCH/DELETE/move 均 404 `not_found`；三类畸形 JSON 均 400 `bad_request`；无 5xx，记录集合与锚点字段不变。 |
| A11 | `/api/health` 返回 200 JSON；`GET /` 返回 200 text/html，含 `action=/bookmarks/new` 表单、`name=url` 字段与列表容器。 |
| A12 | 空名与 121 字符归类名的保存/移动均 400 `invalid_category`；归类集合、记录集合与锚点归属不变。 |
| A13 | 仅凭 URL 保存 201；hostname 由 URL 派生，title 允许缺失或字符串降级，favicon 缺失/内联/同源；首页可渲染记录且 HTML 资源引用不含外部 URL。 |
| A14 | `GET /api/export` 返回 200 text/html，含 Netscape 书签头与两条已存 URL；在 data_dir 生成导入 HTML，POST `/api/import` 返回 imported=2/skipped=0，导入 URL 可检索。 |
| A15 | 重复 URL 返回 409 `duplicate_url` 且含 existing_id，总数不变；`allow_duplicate=true` 时 201、新 id、总数加一、同 URL 两条。 |

## 6. 启动证据与行为证据

- 启动证据只回答“进程是否起来并暴露健康接口”：`/api/health` 返回 200 JSON；启动日志可用于诊断。它不证明保存、检索、重启或错误合同。
- 行为证据来自真实 HTTP 请求：唯一 token、精确状态码、结构化错误码、读回字段、相对计数、隔离实例的前后对比。A14 的导入 HTML 只是请求输入，不是 mock 响应。
- 重启证据来自同一实例子目录上的真实动作、停止、再启动与读回；健康检查本身不算重启证明。
- `GET /` 的 HTML 检查是对服务端响应文本的检查，不是浏览器 DOM/JavaScript 渲染；套件不驱动浏览器。
- 不以 `--help`、进程退出码 0、日志文字或作者声明作为通过依据；仅使用 stdout 的结果 JSON。

## 7. 结果 schema 与退出码

stdout 只输出一个 `atlas.acceptance-result.v1` JSON 对象；诊断和逐条断言日志走 stderr。示例：

```json
{"schema":"atlas.acceptance-result.v1","case_id":"A01","status":"passed","assertions":[{"id":"a01-health-status","passed":true,"detail":"GET /api/health -> HTTP 200"}]}
```

- `status` 为 `passed`、`failed` 或 `unverified`；只有非空断言全部通过才是 `passed`。
- 退出码：`0` 当且仅当 `status=passed`；任一断言失败、基础设施错误或未验证均非零。不要只读取退出码或 stderr 来判断成功。
- 结果总长度保持在 64000 字符以内；`common.emit_result` 会压缩过长的 detail，runner 不应截断 stdout。
- 缺少/未知 `--case`、缺少必需 flags、非法 `--base-url` 会显式非零退出；把有效 case 传给未实现该 case 的程序会产生 `dispatch` 失败结果并非零退出。

## 8. 离线限制与未验证能力

- 验收环境外部网络禁用；套件只访问 `--base-url` 的精确 origin 或自己启动的隔离实例。不会抓取已保存 URL、元数据或 favicon。`GET /go/{id}` 明确不跟随重定向，只读取 302 的 Location。
- 传输边界关闭代理，并对重定向逐跳校验 origin；跨源重定向直接失败，不会回退为任意 loopback 放行。A14 使用 `.atlas-acceptance.example` 合成 URL，套件不会请求这些 URL。
- A13 只在离线条件下验证保存成功、hostname 派生、title 的缺失/字符串降级、favicon 缺失/内联/同源，以及服务端 HTML 不引用外部资源；不验证真实 favicon 图像、第三方抓取、视觉准确度或 CORS。
- 第三方元数据/图标增强端点的实际可达性未经本套件验证；不得把 A13 解释为这些端点可用。
- 不驱动浏览器库，不做 DOM/JS 渲染、截图或图标准确性检查。任何浏览器专属前提不可用时，执行者应报告 `unverified` 或 `failed`，绝不伪造 UI 通过。
- 不设未经验证的时延、吞吐或成本目标。

## 9. 根 `delivery.json` 示例

将 `delivery.json` 放在交付源码根（`root` 为 `.`，启动路径相对该根）：

```json
{
  "schema": "atlas.application-delivery.v1",
  "root": ".",
  "runtime": {
    "profile": "python-web",
    "install": [],
    "build": [],
    "start": ["python3", "app/serve.py", "--host", "0.0.0.0", "--port", "8000", "--data-dir", "/state/app-data"],
    "port": 8000
  }
}
```

- `profile` 固定为 `python-web`；`install`、`build` 均为空，表示不运行 pip/npm 或构建步骤。
- `start` 是字面 argv 数组，占位符如 `{port}`、`{data_dir}` 不会在参数内插值；上例等价启动命令为 `python3 app/serve.py --host 0.0.0.0 --port 8000 --data-dir /state/app-data`。
- `port` 必须与 start 中显式端口 `8000` 一致。
- `/state/app-data` 是交付进程自己的持久化目录；验收调用中的 `--data-dir` 是测试者草稿根，二者角色不同，不要混用。
- `0.0.0.0` 仅用于隔离验收网络；日常本机运行可绑定 `127.0.0.1`，但交付示例保持上述字面值。
