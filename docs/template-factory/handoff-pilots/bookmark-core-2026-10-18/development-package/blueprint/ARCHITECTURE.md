# 架构与契约

## 默认技术栈与理由

默认：Python 3 标准库（http.server + sqlite3）单进程本地应用，服务端渲染 HTML + 少量原生 JS 的中文界面。入口固定为 `python3 app.py --port PORT --data-dir DIR`，仅绑定 127.0.0.1，所有持久数据落在 DIR 下，应用自身无第三方依赖、无需应用依赖安装。这是本次试验环境的明确选择（见 GUIDANCE），不是类别约束，也不构成对旧 Node 方案的优劣判断。

替代方案：Node/Express（需 npm 依赖与额外构建链）；linkding（MIT，Django）/Linkwarden、Karakeep（AGPL-3.0）等成品（功能远超本场景，引入运维、许可与合规负担）。结论是自建薄应用，复用类别约定（单归属分类 + 未分类落点 + 软删除演进 + Netscape HTML 交换格式）而非复制第三方代码；本任务不复制任何第三方代码或上游代码。

## 数据模型（SQLite，例如 DIR/app.sqlite3）

- `category(id INTEGER PK, name TEXT NOT NULL UNIQUE, created_at TEXT NOT NULL)`
- `bookmark(id INTEGER PK, url TEXT NOT NULL, url_key TEXT NOT NULL, title TEXT NULL, note TEXT NULL, category_id INTEGER NULL REFERENCES category(id), created_at TEXT NOT NULL, updated_at TEXT NOT NULL)`
- `save_nonce(token TEXT PRIMARY KEY, created_at TEXT NOT NULL)`：用于同按钮重复提交的短窗口幂等。

URL 原样保存在 `url`（保留 query 与 fragment，打开时原样跳转）；`url_key` 为最小规范化比较键：trim、scheme/host 小写、去默认端口、去路径末尾多余斜杠，但保留 query 与 fragment。`category_id` 为 NULL 即界面显示“未分类/以后看看”，不预置可删除实体，保证未归类落点始终存在。时间以 ISO-8601 UTC 文本存储。

## 入口、状态与错误契约（以用户可见消息描述，不规定 HTTP 状态码或 API 路由）

- 启动：`python3 app.py --port PORT --data-dir DIR`；若 DIR 不存在则创建；仅回环监听。
- 空库提示与“检索无结果”提示必须是两条不同文案；
- 无效 URL 或非 http(s) 协议：显式错误、不落库、保留表单输入；
- 重复 URL：显式“已存在”提示 + 可供用户选择的“仍然保存”动作；
- 备注超限：显式错误且不落库，绝不静默截断；
- 分类名为空或重名：显式错误，不创建；
- 同按钮重复提交：仅产生一条记录。
- 生命周期（P0）：保存 → 未分类/指定分类 → 移动 → 按分类浏览或关键字检索 → 打开原页。删除/回收站不在 P0。

## UI/CLI 适配器契约（供验收，不规定 DOM 结构、路由或错误码）

验收通过真实浏览器驱动语义 UI，只依赖可访问角色与中文可见标签，不依赖模板专用 `data-testid`。适配器 `resolveControls(page, overrides)` 优先用角色/标签解析控件，并允许通过 `UI_SELECTORS`（JSON）覆盖映射，使语义等价的 UI 无需模板专用 testid 即可通过。下列为**默认建议选择器（仅建议，可覆盖，不是强制 DOM 契约）**：

- 保存表单：`save-url`、`save-title`、`save-note`、`save-category-select`、`save-category-new`、`save-submit`；用户可见错误容器 `form-error`。
- 分类：`category-list`、`category-item`（含分类标识与名称语义）。
- 记录：`record-list`（默认按添加时间倒序）、`record-card`（含 URL）、`record-open`（指向原始 URL、新标签打开）、`record-category`、`record-move-select`、`record-move-submit`。
- 检索：`search-input`、`search-submit`。
- 空状态：`empty-library` 与 `no-search-match` 必须是两条不同文案。

## 非功能需求

- 仅回环监听；不发起后台元数据抓取、遥测或任何非用户触发的对外请求。
- 唯一的对外导航是用户显式点击“打开原页”，指向记录保存时的原始 URL（含 query 与 fragment），在新标签页打开。
- 验收环境阻止对外部地址的真实连接：对外请求被拦截/中止，仅断言被尝试打开的 URL 与新标签行为，不产生真实外部流量。
- 认证（若配置）只作用于显式配置的目标，绝不附加到外部导航或夹具，且不记录凭据值；目标声明不支持的模式显式失败为基础设施/不完整，不静默跳过或伪装通过。
- 持久数据仅在 DIR 下，应用无网络依赖即可完整运行 P0 闭环。

## 重启与持久化验证契约

默认由操作员控制 before/after：用例先经 UI 保存记录与分类并输出停止并重启（`python3 app.py --port PORT --data-dir DIR`）的步骤，操作员完成后用例继续并经 UI 读回数据；未完成的操作员步骤不得记为通过。仅当用例自身以固定 argv（不启用 shell 插值）启动应用并安全持有该子进程时，控制器才可只终止自己启动的 PID 并重新启动；不得执行任意 shell 命令，不得终止无关进程。重启的证明是“新的自有进程 + 通过 UI 重新读回已持久数据”，不以文件存在或新建 SQLite 连接作为证明，也不要求应用暴露内部数据库连接状态。

## 限制

- 检索为大小写不敏感子串匹配（标题/URL/备注/分类名），不含正文全文索引。
- P0 不做服务端元数据抓取，标题仅来自用户输入或回退为 URL；P0 流程不发起外部网络请求（用户显式点击打开原页除外）。
- 无删除/回收站（记录只可保存与移动）；分类只可新建与选择，不可重命名或删除。
- 无导入/导出、无批量操作、无标签、无分页。
- 无认证，仅回环可达；不支持外部主机访问。
- 重复判定基于最小规范化键并保留 query/fragment，不做跟踪参数或 http/https 变体的自动合并。
- 不做网页快照/归档、失效链接扫描与正文全文检索。
- 不设任意性能/成本/延迟阈值；语义正确性与数据完整性优先于规模指标。
