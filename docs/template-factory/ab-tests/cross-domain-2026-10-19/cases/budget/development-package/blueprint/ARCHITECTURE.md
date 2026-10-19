# 架构与契约

## 默认技术栈与理由
- Python 3 标准库 + SQLite（CONTRACT 固定）：无安装、无第三方依赖，适合本地单机；sqlite3 提供事务与集中持久化。
- HTTP 层用标准库 http.server（ThreadingHTTPServer + 轻量路由），只绑定 127.0.0.1，贴合“本地单用户、无外部网络”。
- 前端为随应用提供的原生 HTML/CSS/JS，与 JSON API 共用同一真实状态，不引入 CDN 或外部资源。
- 被否方案：Flask/FastAPI（需第三方依赖，违反零安装约束）；直接复用 Actual Budget(NodeJS，规模不匹配)或 Firefly III(AGPL-3.0，强 copyleft，不宜复制)（S08,S09）。

## 数据模型（保持小规模）
- categories(id INTEGER PK, month TEXT 'YYYY-MM', name TEXT, budget_cents INTEGER)，唯一约束 (month,name)。
- transactions(id INTEGER PK, date TEXT 'YYYY-MM-DD', category_id INTEGER, amount_cents INTEGER, note TEXT)。
- 金额一律以整数“分”存储，响应渲染为两位小数字符串；亦可用 decimal.quantize 实现（S12）。
- spent 由按 category 聚合推导，remaining = budget − spent；totals 为整月 budget/spent/remaining 聚合。

## API/错误/状态契约（与 CONTRACT.md 一致）
- GET /api/state?month=YYYY-MM；POST /api/categories；PUT /api/categories/{id}；POST /api/transactions；PUT /api/transactions/{id}；DELETE /api/transactions/{id}；GET /api/export?month=YYYY-MM。
- 所有金额为两位小数字符串；校验失败（非正数、超过两位小数、日期与分类月不符、同月同名、未知 id）返回非 2xx 且 JSON {"error":"..."}，同时不改变既有数据。
- 月份是隔离键：写入与查询必须匹配目标月，跨月误改必须拒绝。

## UI/CLI 适配契约（供测试）
- UI 必须提供 data-testid=month,category-name,category-budget,category-save,expense-date,expense-category,expense-amount,expense-note,expense-save；分类选择项 value 等于 category_id。
- 先填 month 等待状态加载；category-save 建分类；expense-save 记账。其余界面可自由设计。
- 启动：python3 app.py --port PORT --data-dir DIR，仅 127.0.0.1。
- 验收程序 acceptance/run.py 以显式目标参数连接真实实例（Web 模式仅允许给定的 loopback origin/port，禁止跨源重定向）；本地 CLI 模式仅允许显式 --app-path 与受控 --data-root，shell=False。

## 非功能需求
- 全离线：无遥测、无外部网络、无任意文件访问、无子进程；数据仅写入 --data-dir。
- 金额确定性：整数“分”或 decimal，避免二进制浮点误差。
- 持久化：事务/原子写入，正常重启后可回查。
- 反馈：UI 对失败给出可理解提示，API 返回结构化错误。

## 复用与来源
- S10（RFC 4180）与 S11/S12（Python csv/decimal 标准库）作为格式与精度依据；未复制任何第三方代码。
