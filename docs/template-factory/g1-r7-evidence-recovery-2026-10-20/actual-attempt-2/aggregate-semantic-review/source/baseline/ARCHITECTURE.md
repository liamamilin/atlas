## 默认技术栈与理由

- **交付 profile：python-web。** 运行时为 Python 3.12 标准库（`http.server`、`sqlite3`、`urllib`、`json`、`html.parser`），零第三方依赖，满足 V1 指定的离线标准库约束。
- 备选方案（Flask/FastAPI、Node + IndexedDB）生态更丰富，但需要安装依赖或 npm/Playwright，与离线、可独立验收的要求冲突，故不采用。
- 前端为服务端渲染的少量 HTML 加原生 JS 渐进增强，无构建步骤；数据存取集中在服务层，HTML 表单与 JSON API 都是同一服务层的薄适配器。
- 理由：场景是单用户本地收藏箱，数据量小、访问单机，标准库加 SQLite 单文件即可覆盖持久化、检索、打开回跳与离线验收。

## 数据模型（SQLite，文件位于应用 `--data-dir/bookmarks.sqlite3`；验收时为每实例隔离子目录，绝不是测试者 data_dir 根目录）

- `schema_meta(version INTEGER)`：迁移版本。
- `categories(id TEXT PK, name TEXT NOT NULL UNIQUE COLLATE NOCASE, is_default INTEGER NOT NULL DEFAULT 0, position INTEGER NOT NULL, created_at INTEGER NOT NULL)`：首启预置「未整理」(is_default=1)、「待购」、「家居改造」、「以后看看」。
- `bookmarks(id TEXT PK, url TEXT NOT NULL, hostname TEXT NOT NULL, title TEXT NULL, description TEXT NULL, category_id TEXT NOT NULL REFERENCES categories(id), favicon_url TEXT NULL, created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL, trashed_at INTEGER NULL)`。
- 索引：`category_id`、`created_at`、`hostname`；不建立 `url` 唯一索引。重复 URL 的 409 判定（属 P1/F14）由服务层查询活动记录完成，`allow_duplicate=true` 时绕过；软删除记录不参与判定。
- 迁移：首次启动在单一事务内建表并写入预置归类；后续按技术决策 D12 演进版本。

## API 与错误合同（JSON）

- `GET /api/health` 返回 200 就绪信息与 schema 版本。
- `GET /api/categories` 返回归类数组，每项含 id、name、count、is_default。
- `POST /api/categories`（body: name）返回 201；重名 409 `duplicate_category`；空名或超过 120 字符 400 `invalid_name`。
- `PATCH /api/categories/{id}` 重命名，空名或超过 120 字符 400 `invalid_name`，与既有归类重名 409 `duplicate_category`，默认归类不可重命名（400 `protected_category`）；`DELETE /api/categories/{id}` 在事务内按 is_default 把其记录迁回默认归类，默认归类不可删（400 `protected_category`）。
- `GET /api/bookmarks?category=<name|id>&q=<str>&include_trashed=0` 返回记录数组（默认按 created_at 倒序，同值以 id 兜底）；`q` 对标题、hostname 与描述做大小写不敏感子串匹配，并与 category 叠加；未知归类过滤返回空集。
- `POST /api/bookmarks`（body: url 必填；title、description、category 可选；allow_duplicate 可选）返回 201；category 省略或为 null 时归入默认「未整理」，给出新名称时按 NOCASE 自动创建并复用既有归类，显式空字符串或超过 120 字符 400 `invalid_category`；非法 URL（非 http/https、hostname 为空）400 `invalid_url`；重复 URL 在 P1/F14 下返回 409 `duplicate_url` 并附 existing_id，`allow_duplicate=true` 时仍新增。
- `GET /api/bookmarks/{id}` 200 或 404 `not_found`；`PATCH` 更新字段，非法 URL 400 `invalid_url`、非法归类名 400 `invalid_category`、改为活动记录已用的 URL 409 `duplicate_url`；`POST /api/bookmarks/{id}/move`（body: category，省略/空名或超过 120 字符 400 `invalid_category`，新名称按 NOCASE 自动创建）迁移归属。
- `DELETE /api/bookmarks/{id}` 软删除返回 200；`POST /api/bookmarks/{id}/restore` 恢复；若同 URL 已有活动记录，恢复返回 409 `duplicate_url` 并附 existing_id，且不修改任何数据。
- `GET /api/export` 返回 200 `text/html` 的 Netscape 书签文件（含 `<!DOCTYPE NETSCAPE-Bookmark-file-1>` 头）；`POST /api/import` 接受同格式 HTML，返回 200 与 `{imported,skipped}` 计数，导入项可被检索到。
- `GET /go/{id}` 返回 302 且 `Location` 为保存时的 URL（`target=_blank rel=noopener` 由页面使用）；未知 id 404。
- 错误合同：所有校验失败返回 `{error:{code,message,field}}` 且状态码为 400/404/409；校验类错误绝不产生 5xx；响应体固定可解析。
- 状态合同：排序稳定、GET 幂等；归类与检索词为请求级参数，不写入数据库（沿用上游「视图状态不落盘」的边界，S05）。

## UI 适配器合同（HTML，供独立界面执行者）

- `GET /` 与 `GET /?category=<name>&q=<str>`：页面含录入表单 `<form method=post action=/bookmarks/new>`（字段 url、title、description、category 可输入文本框，默认值「未整理」并用 datalist 提供既有归类建议，允许输入新名称）、侧栏归类链接「/?category=…」、检索表单 `<form method=get action=/>`（字段 q）、记录列表容器。
- 每条记录：打开链接 `href=/go/{id} target=_blank rel=noopener`；移动表单 `action=/bookmarks/{id}/move`（category 可输入文本框并用 datalist 提供既有归类建议，默认当前归类）；删除表单 `action=/bookmarks/{id}/delete`；编辑入口；删除后出现撤销表单 `action=/bookmarks/{id}/restore`。
- 侧栏归类创建表单 `action=/categories/new`（字段 name）。
- 表单端点成功返回 303 重定向到列表页，失败返回 400 并显示错误信息；与 JSON API 共用服务层，语义一致。

## 验收适配器合同（供标准库验收程序）

- 已部署目标：`--base-url` 指向运行中的 python-web 实例，程序以标准库 HTTP 读写并断言行为；交付 start 为字面 argv 数组 ["python3","app/serve.py","--host","0.0.0.0","--port","8000","--data-dir","/state/app-data"]，仅暴露于隔离验收网络且不引入认证凭据。
- 重启与持久化：`--app-root` 为只读源码、`--data-dir` 为测试者草稿目录；`launch_app` 在 `{data_dir}/instances/<uuid>/` 创建每实例隔离 scratch 子目录，并以 argv 数组 [python3, <app_root>/app/serve.py, --host, 127.0.0.1, --port, <空闲端口>, --data-dir, <该实例子目录>] 启动同一冻结应用（由 launch_app 填入实际路径），轮询 `/api/health` 就绪，执行真实动作后终止进程，再以相同实例子目录重新启动并观察持久化行为。宿主 `{data_dir}` 根目录绝不是应用数据库；应用源码只读，凭据不外带到外部导航，验收不携带认证信息。

## 非功能需求

- 离线可用：保存不依赖任何外部服务；第三方增强失败静默降级，不阻塞保存。
- 单用户本机：无认证、无凭据文件；日常运行默认绑定 127.0.0.1，独立验收交付仅在隔离网络内监听测试者可路由的接口（0.0.0.0）。
- 确定性：排序与错误码稳定，GET 幂等，便于重复验收。
- 数据完整性：写操作事务化；删除归类在事务内迁移记录；软删除保证可恢复。
- 忠实性：验收只断言真实 HTTP 行为，不检查文件或标题存在性，不使用 mock 目标。
- 不设未经验证的时延或成本指标；仅要求请求可顺序处理。

## 边界与限制

- 不实现导入导出以外的同步、托管或协作；不实现浏览器扩展与移动分享目标。
- 不保存网页副本、不做正文全文检索、不做失效链接检测（外部网络在验收中禁用）。
- 不引入置顶/归档、多排序模式、复制 URL 与访问计数（见 F20、F23、F24）。
- 归类为扁平单选，不支持嵌套或多标签（见 F19、D01）。
- 第三方元数据抓取的实际可达性与 CORS 未验证，仅作可选增强并明确标注未验证。