# 生活待购与灵感收藏夹 — 验收运行说明

本目录是一套独立、冻结的验收套件，用真实 HTTP 目标验证 python-web 应用。它不包含应用实现，不导入应用代码，也不读取应用自己的测试判定；本文档只是运行说明，不代表任何用例已经执行或通过。**本套件未执行，任何人不得据此声称测试通过。**

## 1. 目标适配器

| 参数 | 适用范围 | 用途 |
| --- | --- | --- |
| `--base-url` | A01–A15（全部） | 已部署 python-web 实例的 http/https 根 URL；所有 base_url 行为断言都发往该 origin。 |
| `--app-root` | A01、A03、A05、A09、A11 | 只读应用源码根；必须包含 `app/serve.py`，用于启动同一冻结应用的隔离实例。 |
| `--data-dir` | A01、A03、A05、A09、A11、A14 | 测试者可变草稿根；重启适配器在其 `instances/` 下创建每实例目录；A14 在此生成导入 HTML。 |

### 1.1 `--base-url`

- 示例：`http://127.0.0.1:8000`。必须是 http 或 https；不得包含用户名、口令、查询串或片段。
- 验收目标声明无认证；套件不会把凭据放入 URL、请求头、日志或 fixtures。`HttpClient` 拒绝 `Authorization`/`Proxy-Authorization`；若目标要求 Basic/Bearer/session 等认证，或健康检查返回 401/403，程序在业务请求前显式失败并报告基础设施未就绪，不支持认证适配器，也不跳过或伪造通过。
- 每个请求都绑定到该精确 origin（scheme、hostname、port）；重定向逐跳校验，跨源立即失败。不会放行任意 loopback 主机或端口，也不默认信任所有 localhost 端口。

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
- 目标不需要认证，也不实现任何登录/令牌适配器。`HttpClient` 不附加全局凭据头，并拒绝 `Authorization`/`Proxy-Authorization`；目标若返回 401/403 或在健康检查阶段要求认证，程序在发送业务请求前显式失败，按基础设施未就绪处理，不跳过、不伪造通过。错误输出对 URL 中的用户名/口令及敏感查询参数做脱敏，凭据不进入 fixtures、日志或断言 detail。
- 套件只与 `--base-url` 精确 origin 或自己启动的隔离实例通信；外部网络禁用，不抓取已保存 URL、元数据或 favicon。

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

`acceptance/runner.json` 的唯一作用是为 Atlas 提供每个用例的 argv；实现程序由固定 spec 选择。所有用例都必须带 `--base-url`，A01/A03/A05/A09/A11 还必须带 `--app-root` 与 `--data-dir`，A14 还必须带 `--data-dir`。未知或缺失参数由参数解析器显式报错并非零退出。

### 4.1 与 runner.json 一致的 args

| 用例 | 程序 | args |
| --- | --- | --- |
| A01 | `p0_library.py` | `["--case","A01","--base-url","{base_url}","--app-root","{app_root}","--data-dir","{data_dir}"]` |
| A02 | `p0_library.py` | `["--case","A02","--base-url","{base_url}"]` |
| A03 | `p0_library.py` | `["--case","A03","--base-url","{base_url}","--app-root","{app_root}","--data-dir","{data_dir}"]` |
| A11 | `p0_library.py` | `["--case","A11","--base-url","{base_url}","--app-root","{app_root}","--data-dir","{data_dir}"]` |
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
python3 /suite/acceptance/p0_library.py --case A03 --base-url "$BASE_URL" --app-root "$APP_ROOT" --data-dir "$DATA_DIR"
python3 /suite/acceptance/p0_library.py --case A11 --base-url "$BASE_URL" --app-root "$APP_ROOT" --data-dir "$DATA_DIR"
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
| A01 | 对 base_url 做健康检查，经真实保存表单提交唯一 URL/标题/描述并跟随 303，断言 HTML 记录行与 JSON 读回；再用 `--app-root`/`--data-dir` 启动隔离实例，经真实表单保存，停止后以同一实例子目录重启，断言 id、原始 URL、标题与描述稳定。 |
| A02 | 用保存表单提交单标签主机 URL（如 `http://atlas-a02-<token>`）作为显式正向边界：断言 303、原始字符串持久化且行内 href 精确；同一表单与 JSON 分别提交缺协议、`javascript:`、`ftp://`、`http://` 空主机、含空格/非法 hostname 的值，断言 400 `invalid_url`、`form-error` 可读、相对计数不新增且被拒 URL 不出现在列表。另用独立唯一单标签 hostname URL 经 JSON POST 保存，断言 201、新 id、独立 GET/列表中同一 id 与原始 URL；非法输入的 before 快照在两条合法创建后取得。单标签主机是接受策略，不要求点域名。 |
| A03 | 在给定 base_url 按持久化后的用户分类状态验证省略 category 保存进入未整理、有效新分类名自动创建、读回及 HTML/API 分类筛选；同一 app_root 的独立 fresh 实例在首次业务写入前验证四个预置分类在 API 与 HTML 均可见。不得要求已用目标恢复已删除或重命名的非默认预置分类。缺少 app_root/data_dir、启动/来源/清理错误均失败；fresh 数据位于测试者 data_dir/instances 下，不清空或重置 base_url。 |
| A04 | 从首页 `a[data-testid=category-manager]` 进入 `/categories`；用 `category-create-form` 的真实 `name` 新建（303 后可见且计数正确）；用重名及大小写变体提交 create/rename 表单，断言 409 `duplicate_category`、`form-error`、输入保留且集合不变；用 `category-rename-form` 提交 `category_id`+`name` 重命名，记录跟随；用 `category-delete-form` 删除归类，断言活动与软删记录都迁回未整理、软删记录在 `/?trash=1` 可恢复；对默认归类做 rename/delete，断言 400 `protected_category` 且不变；JSON API 保留已有非法名称、重复名称及默认分类保护断言；不宣称成功 JSON rename/delete 已覆盖。create/rename 分别提交省略 name、空字符串、纯空白、121 字符名（JSON 另含显式 null），均断言 400 `invalid_name`、`form-error`、提交值保留、分类与记录集合及归属不变。 |
| A05 | 用 `record-move-form` 的真实 `record_id` 与 `select name=category_id` 移动，303 到目标归类后旧归类消失、新归类可见、JSON 读回归类正确；再用 `--app-root`/`--data-dir` 启动隔离实例，经真实表单移动，停止后同目录重启读回归属。 |
| A06 | 两个归类各两条记录，读取 HTML `[data-testid=category-count][data-category-id]` 与记录行，并与 `/api/categories` 的 count 和 `/api/bookmarks` 列表比对；通过真实移动、删除、恢复表单改变状态，逐步断言 count 只计活动记录且与列表一致，软删记录仍在 `include_trashed=1` 中。 |
| A07 | 用真实 `category-search-form` 提交 `category` 与 `q`，断言 200、表单的 category 与 q 值均保留、页面显示所选归类/查询/匹配行；用同一关键字分别在两个归类提交，断言各自只命中本归类记录；在某归类提交无匹配 q，断言显示明确空结果且无记录行；同时保留 JSON 断言：标题、hostname、描述的子串大小写不敏感命中，category+q 叠加，无匹配返回 200 空数组；仅存在 URL path、URL query 或分类名的唯一 token 经 JSON 与实际 HTML 搜索表单查询不得命中目标记录，以 id/行集合判断而非页面回显，保留允许字段的正向控制。 |
| A08 | 经真实保存表单创建带 query 的原始 URL，解析 `tr[data-record-id]` 内 `a[data-testid=record-open-link]`，断言 href 精确等于保存值、`target=_blank`、`rel` 含 `noopener`，并以 `urljoin` 验证它是实际导航目标；再 `GET /go/{id}` 不跟随重定向，断言 302 Location 精确等于原始 URL；未知 id 404 `not_found`；读回记录 URL 未被改写。P0 不请求目标外链。 |
| A09 | 经真实保存表单创建记录，用 `record-delete-form` 软删除并跟随 303，断言默认列表/计数排除、`/api/bookmarks?include_trashed=1` 仍存在、`/?trash=1` 显示 `record-restore-form`；用该表单恢复，断言 URL/标题/描述/归类回归且重新可见；再创建归类与记录、软删除记录后用 `category-delete-form` 删除归类，断言软删记录迁到未整理且仍可在回收站恢复，恢复后无孤儿；最后用 `--app-root`/`--data-dir` 启动隔离实例，真实删除后停止、同目录重启，断言删除状态与回收站内容保持，并可恢复。 |
| A10 | JSON 路径保留未知 id 的 GET/PATCH/DELETE/move 均 404 `not_found`，三类畸形 JSON 均 400 `bad_request`，无 5xx、记录集合与锚点字段不变；HTML 路径用保存表单提交非法 URL，断言 400、`form-error`、url/title 输入保留、无新增记录，再用同一表单提交修正 URL 断言 303 且只新增一条；用归类表单提交非法 name，断言 `form-error` 且无写入。 |
| A11 | `/api/health` 返回 200 JSON；`GET /` 返回 200 text/html，含 `action=/bookmarks/new` 表单、`name=url`、`category-manager` 链接与列表容器；用不存在的归类过滤得到明确空状态（a11-base-*，仅当前部署入口）。另必须使用同一冻结 app_root 与 data_dir 创建 fresh=True 的新隔离实例，业务写入前证明 health、未过滤全库含软删除均为空、四预置分类合法唯一 ID/count=0、未过滤首页表单/URL/分类入口/列表/明确空态且无记录行（a11-fresh-*）；finally 关闭 client 并停止拥有的进程、确认退出，缺参数/启动失败/清理失败不得通过。这不证明 base_url 被清空或同容器重启。 |
| A12 | 只处理书签保存/移动，不使用分类创建或重命名表单。HTML 保存 `category`（名称）显式空/纯空白/121 字符为 400 `invalid_category`，省略则默认未整理；HTML 移动 `category_id`（ID）省略/空/未知为 400 `invalid_category`；JSON 保存 `category`（名称）省略/null 默认未整理，显式空/纯空白/121 字符为 400 `invalid_category`；JSON move `category`（名称）省略/null/空/纯空白/121 字符为 400 `invalid_category`。有效新名称可自动创建；HTML 未知 ID 不得变为新名称；JSON 不新增 `category_id` 字段。每个负向 HTML 为 400/`form-error`/输入保留，JSON 为 400/`error.code=invalid_category`，分类集合/记录集合/锚点归属均不变；修正有效值可恢复。 |
| A13 | 仅凭 URL 保存 201；hostname 由 URL 派生，title 允许缺失或字符串降级，favicon 缺失/内联/同源；本次记录行内的打开链接 href 精确等于保存的原始 URL（HTML entity 解码后）、target=_blank、rel 含 noopener；HTML 资源引用不含外部 URL。程序断言不能单独证明运行环境禁用了外网。 |
| A14 | `GET /api/export` 返回 200 text/html，含 Netscape 书签头与两条已存 URL；在 data_dir 生成导入 HTML，POST `/api/import` 返回 imported=2/skipped=0，导入 URL 可检索。 |
| A15 | 重复 URL 返回 409 `duplicate_url` 且含 existing_id，总数不变；`allow_duplicate=true` 时 201、新 id、总数加一、同 URL 两条。 |

### 5.1 HTML 表单验收契约

所有 HTML 断言都用标准库 urllib 提交 `application/x-www-form-urlencoded` 并解析服务端返回的 HTML；不驱动浏览器、不执行 JavaScript。数据由唯一 token 构造，断言针对本次 token 的相对计数或集合变化，不依赖固定样本。

- `GET /`：保存表单 `form[action=/bookmarks/new]`（method=post；字段 `url`、`title`、`description`、`category`）；`a[data-testid=category-manager]` 指向 `/categories`；`form[data-testid=category-search-form]` 为 GET `/`，含 `category`（归类名）与 `q`；记录行 `tr[data-testid=record-row][data-record-id]`；打开链接 `a[data-testid=record-open-link]`；每行 `form[data-testid=record-move-form]`（`record_id`、`select name=category_id`，值为 API 归类 ID）与 `form[data-testid=record-delete-form]`（`record_id`）。
- `GET /?trash=1`：软删记录行含 `form[data-testid=record-restore-form]`（`record_id`）。
- `GET /categories`：`form[data-testid=category-create-form]`（`name`）、`form[data-testid=category-rename-form]`（`category_id`、`name`）、`form[data-testid=category-delete-form]`（`category_id`）；每个归类的计数元素为 `[data-testid=category-count][data-category-id=...]`，只显示活动记录数，并与 `/api/categories` 的 count 一致。
- 成功导航：save 303 到 `/?category=<归类>` 或 `/`；move 303 到目标归类；delete 303 到 `/?trash=1`；restore 303 到恢复后归类；category create/rename/delete 303 到 `/categories`。
- 失败契约：400/409 渲染当前表单页，含可读 `[data-testid=form-error]`，保留已提交的 `url`/`title`/`description`/`category`/`name`/`category_id`/`record_id` 值并保留可重新提交的表单；不得 5xx、不得部分写入。
- `category` 在保存表单中是归类名称；`category_id` 在移动与归类管理表单中是 API 归类 ID。HTML 没有 JSON null，字面字符串 `null` 不作为 JSON null 测试。

## 6. 启动证据与行为证据

- 启动证据只回答“进程是否起来并暴露健康接口”：`/api/health` 返回 200 JSON；启动日志可用于诊断。它不证明保存、检索、重启或错误合同。
- 行为证据来自真实 HTTP 请求：唯一 token、精确状态码、结构化错误码、读回字段、相对计数、隔离实例的前后对比。A14 的导入 HTML 只是请求输入，不是 mock 响应。
- 重启证据来自同一实例子目录上的真实动作、停止、再启动与读回；健康检查本身不算重启证明。A01/A05/A09 的隔离实例只证明从 `--app-root` 启动的冻结应用可持久化，不证明 `--base-url` 指向的部署实例可重启；外部只读目标的重启行为必须保持未验证。
- P0 的保存、列表、搜索与打开检查都不抓取已保存 URL、元数据或 favicon。`GET /go/{id}` 明确不跟随重定向，只读取 302 的 Location；HTML 打开链接只断言 href/target/rel 与 urljoin 目标，不实际导航到外部站点。
- `GET /` 的 HTML 检查是对服务端响应文本的检查，不是浏览器 DOM/JavaScript 渲染；套件不驱动浏览器。
- 不以 `--help`、进程退出码 0、日志文字或作者声明作为通过依据；仅使用 stdout 的结果 JSON。

## 7. 结果 schema 与退出码

stdout 只输出一个 `atlas.acceptance-result.v1` JSON 对象；诊断和逐条断言日志走 stderr。示例：

```json
{"schema":"atlas.acceptance-result.v1","case_id":"A01","status":"passed","assertions":[{"id":"a01-health-status","passed":true,"detail":"GET /api/health -> HTTP 200"}]}
```

- `status` 为 `passed`、`failed` 或 `unverified`；只有非空断言全部通过才是 `passed`。`assertions` 必须是真实执行观察，不得为空或由固定样本直接复制。
- 退出码：`0` 当且仅当 `status=passed`；任一断言失败、基础设施错误或未验证均非零。不要只读取退出码或 stderr 来判断成功。
- stdout 只输出一个完整结果 JSON，总长度不超过 64000 字符（UTF-8 字节数）；`common.emit_result` 会压缩过长的 detail 并保持在 60000 字节以内，runner 不应截断 stdout。结果被截断即视为失败。
- 缺少/未知 `--case`、缺少必需 flags、非法 `--base-url` 会显式非零退出；把有效 case 传给未实现该 case 的程序会产生 `dispatch` 失败结果并非零退出。

## 8. 离线限制与未验证能力

- 验收环境外部网络禁用；套件只访问 `--base-url` 的精确 origin 或自己启动的隔离实例。不会抓取已保存 URL、元数据或 favicon。`GET /go/{id}` 明确不跟随重定向，只读取 302 的 Location。
- 传输边界关闭代理，并对重定向逐跳校验 origin；跨源重定向直接失败，不会回退为任意 loopback 放行或豁免所有本机端口。A14 使用 `.atlas-acceptance.example` 合成 URL，套件不会请求这些 URL。
- 目标要求认证时（例如 401/403），程序在业务请求前显式失败，不支持 Basic/Bearer/session 等模式，不实现登录适配器、不跳过、不伪造通过；凭据不写入请求、fixtures、日志或结果 detail。
- A13 程序的无外部资源断言仅覆盖 HTML 子项；它不能证明应用进程在外网被禁用时仍可保存。要报告 A13 完整离线通过，运行者必须在现有执行环境禁用应用外网，并保留与同一 app_root、应用/执行容器身份及实际运行 receipt 绑定的网络配置和运行证据。缺少该环境证据时离线结论未证明，程序行为子项通过不得汇总为完整离线通过；不能使用用户手填 `offline=true` 自证。若本次未实际运行，状态仍为 not_run。套件本身不会抓取外部元数据/图标；它不验证真实 favicon 图像、第三方抓取、视觉准确度或 CORS。
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
- `0.0.0.0` 仅用于隔离验收网络；日常本机运行可绑定 `127.0.0.1`，但交付示例保持上述字面值。该示例只描述交付合同，不代表应用已实现、已启动或已通过验收。

A03 与 A11 分别使用 common.launch_app(app_root, data_dir, 0, fresh=True)，且各自管理并清理自己创建的 instances/<uuid>：每次新建 instances/<uuid>，不传旧 instance_dir、不删除已有数据；每个用例的首启证据只属于该用例自己，不互相借用 receipt。实际 G1 必须绑定交付应用源码，准备 fixture 不能替代真实 P0。
