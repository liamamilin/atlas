# 架构与契约

## 默认技术栈与理由

- 交付 profile：python-web。Python 3.12 标准库（http.server、sqlite3、urllib、json、html.parser），零第三方依赖；服务端渲染 HTML 表单，JSON API 与 HTML 适配器共用同一服务层。
- 备选 Flask/FastAPI 需安装依赖；Node + IndexedDB/SPA 需 npm/浏览器工具且把数据放在浏览器 profile。二者与离线、可独立验收、单用户本地库的约束冲突，故不采用。
- 数据文件位于应用 `--data-dir/bookmarks.sqlite3`；验收的每实例隔离目录由测试适配器创建，测试者 `--data-dir` 根目录不是应用数据库。
- 单用户、本地优先；无认证、无云同步。日常绑定 127.0.0.1；仅隔离验收网络使用 0.0.0.0。

## 数据模型（SQLite）

- `schema_meta(version INTEGER)`：迁移版本单行。启动时在一个事务内创建/升级 schema，v1 建表并写入预置归类；版本演进只通过事务化迁移，不回退、不依赖客户端存储。
- `categories(id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE COLLATE NOCASE, is_default INTEGER NOT NULL DEFAULT 0, position INTEGER NOT NULL, created_at INTEGER NOT NULL)`：首启预置「未整理」(is_default=1)、「待购」、「家居改造」、「以后看看」。
- `bookmarks(id TEXT PRIMARY KEY, url TEXT NOT NULL, hostname TEXT NOT NULL, title TEXT NULL, description TEXT NULL, category_id TEXT NOT NULL REFERENCES categories(id), favicon_url TEXT NULL, created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL, trashed_at INTEGER NULL)`。
- 索引：category_id、created_at、hostname；url 不设唯一索引。P1/F14 的重复检测由服务层查询活动记录完成；P0 不启用重复拒绝。
- trashed_at 为 NULL 表示活动记录；非 NULL 为软删除。默认列表与计数只统计 trashed_at IS NULL；恢复清空 trashed_at。删除归类在单一事务内把该归类下的活动记录与软删除记录都改到默认归类，因此恢复不会产生无归类记录。
- 排序固定为 created_at DESC、id ASC；category 与 q 只作请求参数，不落库。

## URL 策略

- 记录 URL 必须是绝对、可解析的 HTTP(S) URL，且 hostname 有效且非空。单标签主机（如 http://localhost）与 IP 字面量均有效；不做 DNS 查询、可达性检查或目标页抓取。
- 保存与打开都保留用户提交的原始字符串（不补斜杠、不改大小写、不重写路径）；hostname 由解析结果派生。若 PATCH 更新 URL，必须用新 URL 重新派生 hostname。
- 拒绝：缺少 scheme、非 http/https、缺少/非法 hostname、无法解析的字符串；返回 400 invalid_url 且不写入。
- 上游 S04 的点域名正则与 S08 getHostname 是源观察，映射为 adjusted：点不是通用 URL 有效性要求；target 采用上述解析策略。
- 保存、打开、抓取三者分离：P0 保存与列表均不请求目标页；打开只产生浏览器导航或 /go 302。

## API、错误与状态合同

- `GET /api/health` → 200 JSON，含就绪与 schema 版本。
- `GET /api/categories` → 200 数组，每项 id、name、count、is_default；count 只计活动记录。
- `POST /api/categories` name → 201；重名 409 duplicate_category；空名或超过 120 字符 400 invalid_name。
- `PATCH /api/categories/{id}` name → 200；同上校验；默认归类 400 protected_category。`DELETE /api/categories/{id}` → 200；默认归类 400 protected_category；否则事务内把活动与软删记录迁到默认归类。
- `GET /api/bookmarks?category=<name|id>&q=<str>&include_trashed=0|1` → 200 数组；默认排序 created_at DESC、id ASC；q 对标题、hostname、描述做大小写不敏感子串匹配并与 category 叠加；未知归类返回空数组。
- `POST /api/bookmarks` url 必填，title、description、category 可选，allow_duplicate 为 P1；201；category 省略/null 时归入默认「未整理」；显式空字符串或超过 120 字符 400 invalid_category；新名称按 NOCASE 自动创建并复用；非法 URL 400 invalid_url；P1 重复 409 duplicate_url 且附 existing_id。
- `GET /api/bookmarks/{id}` 200 或 404 not_found；`PATCH` 更新字段；URL 变化时重算 hostname；非法 URL 400 invalid_url，非法归类 400 invalid_category；P1 重复 409 duplicate_url。`POST /api/bookmarks/{id}/move` body category 必填；省略/空/超长 400 invalid_category；新名称自动创建。`DELETE /api/bookmarks/{id}` 软删除 200；`POST /api/bookmarks/{id}/restore` 恢复；P1 同 URL 活动冲突 409 duplicate_url 且不改数据。
- `GET /go/{id}` 302，Location 为保存时原始 URL；未知 id 404 not_found。HTML 打开链接使用原始 URL，target=_blank、rel=noopener。
- P1：`GET /api/export` Netscape HTML；`POST /api/import` 同格式，返回 imported/skipped。
- 错误合同：JSON 失败返回 `{error:{code,message,field}}`；通用 bad_request（畸形/不可解析 JSON，400）、invalid_url、invalid_category、invalid_name、not_found、duplicate_category、protected_category、duplicate_url。校验错误不产生 5xx，不产生部分写入；畸形 JSON 一律 bad_request 且不写。
- 状态合同：GET 幂等；写操作事务化；校验失败保持提交前状态；分类与 q 为视图状态；删除与恢复改变 trashed_at 但不删除行。

## UI/HTML 适配器合同（供真实表单验收与独立浏览器执行者）

- `GET /`：保存表单 `form[action=/bookmarks/new]`（method=post，字段 url/title/description/category；category 预填「未整理」）；`a[data-testid=category-manager]` 指向 /categories；`form[data-testid=category-search-form]` 为 GET /，含 select 或 input name=category（归类名）与 input name=q；记录行 `tr[data-testid=record-row][data-record-id]`；打开链接 `a[data-testid=record-open-link]` 的 href 必须等于保存时原始 URL，target=_blank，rel 含 noopener；每行含 `form[data-testid=record-move-form]`（input record_id、select name=category_id，值为 API 归类 ID）、`form[data-testid=record-delete-form]`（input record_id）；回收站或 `GET /?trash=1` 的软删记录行含 `form[data-testid=record-restore-form]`（input record_id）。
- `GET /categories`：`form[data-testid=category-create-form]`（input name）、`form[data-testid=category-rename-form]`（input category_id、name）、`form[data-testid=category-delete-form]`（input category_id）；每个归类行/侧栏计数为 `[data-testid=category-count][data-category-id=...]`，只显示活动记录数；归类名/计数与 JSON 一致。
- 表单成功：save 303 到 /?category=...；move 303 到目标归类；delete 303 到 /?trash=1；restore 303 到恢复后归类；category create/rename/delete 303 到 /categories。失败：400/409 渲染当前页，含 `[data-testid=form-error]` 可读消息，保留 url/title/description/category/name/category_id/record_id 中已提交的值，并保留可重新提交的表单；不得 5xx 或写入。
- 归类搜索：提交 category 与 q，成功后 URL 与表单同时保留两者；页面显示所选归类、保留的查询和匹配行；同一关键字在两个归类分别得到各自结果；某归类无匹配时显示明确空结果，不是错误。
- 记录移动由 HTML 适配器把 category_id 翻译成归类名，再调用现有 move 服务；归类删除仍按 API 事务迁移活动与软删记录。默认归类不可重命名/删除。
- P0 不提供孤立的记录编辑界面；仅保留 PATCH /api/bookmarks/{id} 的现有 URL 更新合同（URL 变化重算 hostname）。打开链接的实际导航目标由 href 与 /go 302 双重验证，不抓取目标页。

## 验收适配器合同

- 全部程序使用 `--base-url` 指向真实 python-web 目标；A01/A05/A09 另需 `--app-root` 与 `--data-dir`，A14 需 `--data-dir`。
- `--app-root` 只读；`--data-dir` 是测试者草稿根。重启用例通过 common.launch_app 在同一 `--data-dir/instances/<id>` 上启动 `app/serve.py`，真实写入、SIGTERM、同一目录重启并读回；健康检查不是重启证据。
- HTML 用例以标准库 urllib 提交 application/x-www-form-urlencoded 表单并解析响应 HTML 的 data-testid、表单字段、链接与文本；不以 API 调用代替声明的 HTML 表单，不驱动 JS/DOM。独立浏览器执行者可复用同一契约。
- 所有请求限定在 base_url 精确 origin；/go 不跟随重定向；不请求保存的外链、元数据或 favicon；不附加凭据；目标要求认证时显式报告基础设施未就绪。
- 结果：stdout 单个 atlas.acceptance-result.v1 JSON；断言失败或基础设施错误 exit nonzero；不声称已运行。

## 非功能需求

- 离线可用：保存/浏览/检索不依赖外部服务；不设置外部抓取为 P0 要求。
- 数据完整性：写事务化；归类删除与恢复保持引用完整；校验失败零写入。
- 确定性：排序、错误码、重定向稳定；GET 幂等。
- 可访问/可测试：语义化 HTML、表单 label 或 aria、稳定 data-testid；服务端输出 UTF-8。
- 单用户本机：无认证；日常 127.0.0.1，0.0.0.0 仅隔离验收网络。
- 不设未经验证的时延/吞吐/成本目标；只要求请求可顺序处理。

## 边界与限制

- 不实现云同步、多设备、协作、分享、浏览器扩展/移动分享目标。
- 不保存网页副本、不抓取正文、不做失效链接检测（F17/F18）。
- 不引入置顶/归档/多排序/复制 URL/访问计数（F20/F23/F24）。
- 归类为扁平单选；嵌套/标签属后期（F19/D12）。
- P0 不做重复拒绝；F14/A15 保持 P1。
- 第三方元数据/图标仅 P1 可选增强，失败不影响保存；离线验收不验证其可达性。