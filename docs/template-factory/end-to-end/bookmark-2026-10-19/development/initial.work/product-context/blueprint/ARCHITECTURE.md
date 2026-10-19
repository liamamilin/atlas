# 架构与契约

### 技术栈与理由
默认：Python 3 标准库 `http.server.ThreadingHTTPServer` + `sqlite3` + 服务端渲染 HTML 表单（无 JavaScript、无第三方依赖）。理由：目标运行环境无外网、无可安装依赖，标准库即可离线运行；单文件 SQLite 便于持久化与验收只读断言；服务端渲染表单让验收用标准库 HTTP 客户端驱动真实用户流程（GUIDANCE 推荐），无需浏览器。
备选与权衡：Flask/FastAPI/Django 需 pip 安装（离线不可靠）且模板或 ORM 增加体积；Node/Express 需 npm 且无内建 SQLite 驱动；前端 SPA + JSON API 需构建工具与真实浏览器才能验证界面，与离线约束冲突；纯静态站点无法满足本地持久化。采用标准库方案，同时把 HTTP 层与存储层分离，便于日后替换框架。

### 数据模型
P0：
- `collections(id INTEGER PK, name TEXT NOT NULL UNIQUE, is_default INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL)`；首次启动创建默认收件箱（is_default=1，名称“未整理”），不可删除。
- `bookmarks(id INTEGER PK, url TEXT NOT NULL, title TEXT NOT NULL DEFAULT '', note TEXT NOT NULL DEFAULT '', collection_id INTEGER NOT NULL REFERENCES collections(id), created_at TEXT NOT NULL, updated_at TEXT NOT NULL)`。
P1 增量：`bookmarks.deleted_at TEXT NULL`；`collections.parent_id INTEGER NULL`；`tags(id INTEGER PK, name TEXT NOT NULL UNIQUE)` 与 `bookmark_tags(bookmark_id, tag_id)`。
P2 增量：可选的 `fetch_status`、`archive_path` 字段；导入批次仅作日志，不改变主模型。
所有时间以 UTC ISO-8601 文本存储；P1 起对规范化 URL 建唯一索引以实现一地址一记录。

### HTTP / API 与错误契约
| 方法 | 路径 | 请求 | 成功 | 错误 |
| GET | `/`（含 `?collection=&q=`） | 无或查询参数 | 200 渲染列表与归类侧栏 | 未知 collection id → 404 |
| POST | `/bookmarks` | 表单 `url`(必填) `title` `collection_id`(可选) | 303 → `/?collection=<id或inbox>` | 非法/空 URL → 400 错误页并回显输入 |
| POST | `/collections` | 表单 `name` | 303 → `/` | 空或重名 → 400 |
| POST | `/bookmarks/<id>/move` | 表单 `collection_id` | 303 → 目标归类 | 未知 id 或未知归类 → 404 |
| GET | `/go/<id>` | 无 | 302 `Location: <保存的 URL>` | 未知 id → 404 |
| GET | `/?q=` | 查询 | 200 结果页（可为空） | 无 |
约定：GET 只读；所有 POST 变更后一律 303 重定向（PRG，避免刷新重复提交）；400 错误页保留用户输入并提供返回链接作为恢复；404 对不同实体统一格式。P1+ 沿用同一模式：`/trash`、`/bookmarks/<id>/restore`、`/bookmarks/<id>`(编辑)、`/tags`、`/export`、`/import`。未定义的公开或分享类路由一律 404。

### UI 适配契约（供验收用标准库驱动真实界面）
稳定字段与路由：
- 捕获表单 `<form method="post" action="/bookmarks">`，字段 `url`(required)、`title`、`collection_id`(可选 select)。
- 新建归类 `<form method="post" action="/collections">`，字段 `name`。
- 移动记录 `<form method="post" action="/bookmarks/<id>/move">`，字段 `collection_id`。
- 检索表单 `<form method="get" action="/">`，字段 `q`。
- 列表项 `<li class="bookmark" data-bookmark-id="..">`，标题链接 `<a class="bookmark-title" href="<保存的 URL>">`；归类项 `<li class="collection" data-collection-id=".." data-default="0|1">`。
- 打开原页入口 `GET /go/<id>`（302）。
无 JavaScript 依赖，所有交互在无脚本的可访问 HTML 中可用。

### 用户能力追踪（入口 → 动作 → 成功 → 错误 → 恢复）
| 能力 | 入口 | 动作 | 成功 | 错误 | 恢复 |
| F01 保存 | 首页捕获表单 | POST /bookmarks | 303 后列表出现记录 | 非法 URL 400 | 错误页回显输入，修正后重提 |
| F02 默认收件箱 | 捕获表单不选归类 | 提交 | 记录落入未整理 | — | 之后移动到合适归类 |
| F03 新建归类 | 侧栏新建表单 | POST /collections | 303 后侧栏出现归类 | 空名 400 | 重新输入名称 |
| F04 移动 | 记录上的移动表单 | POST /bookmarks/id/move | 目标归类出现记录 | 未知 id/归类 404 | 返回列表重新选择 |
| F05 按归类浏览 | 侧栏归类链接 | GET /?collection= | 只显示该归类记录 | 未知 id 404 | 返回默认收件箱 |
| F06 检索 | 顶部检索表单 | GET /?q= | 命中列表 | 无匹配→空结果 | 换关键词或清空 |
| F07 打开原页 | 记录标题链接或 /go/id | GET /go/id | 302 到真实 URL | 未知 id 404 | 返回库列表 |
| F08 持久化 | 任意写操作 | 事务提交 | 数据目录内 SQLite 落盘 | 磁盘错误→500 | 从数据目录备份恢复 |
| F09 私有优先 | 无公开路由 | 访问 /share、/public | — | 统一 404 | 仅本地访问 |

### 非功能要求
- 离线自包含：运行期不访问外网；唯一例外是用户点击打开原页的 302 目标，验收不跟随该跳转。
- 持久化：每次写操作提交 SQLite 事务；数据目录可整目录备份与恢复。
- 单用户私有：无认证、无公开分享路由；本产品无凭据，不记录也不输出任何敏感值。
- 安全：输出 HTML 全转义；URL 仅接受 http/https 绝对地址，拒绝 javascript:/data: 等 scheme；抓取启用时默认拒绝私网与回环地址。
- 可移植：应用源码只读，仅 --data-dir 可写。
- 可测：界面契约稳定（字段名、路由、data-* 属性），P0 全流程无需浏览器即可验收。

### 限制与假设
- 单进程本地服务，不做多实例并发写，SQLite 默认配置即可。
- P0 不抓取页面元数据、不检测失效链接、不保存副本；抓取与存档见 D05/D11，属 P2 可选且离线默认关闭。
- 进程重启的全流程验证由独立浏览器验收完成；本验收套件不重启服务，也不直接读取应用数据库，仅以保存后由全新无状态 HTTP 客户端读回记录作为套件内持久化佐证，进程重启耐久性标记为未验证，不声称已完成进程重启。
- 导入导出、标签、子归类、回收站均属 P1/P2，P0 用例不得依赖它们。
- 失效链接检测与元数据抓取在离线验收环境只能报告 unavailable，不得伪报通过。
