# 架构与契约

默认技术栈：Python3 标准库 ThreadingHTTPServer + sqlite3 + 原生 HTML/CSS/JS，无第三方依赖；理由：CONTRACT 固定标准库与 SQLite、无安装、仅回环；替代方案：Flask/FastAPI 需安装（拒）；PostgreSQL 的 exclusion constraint（S11）可表达"不得重叠"，但引入外部数据库与部署（拒；若迁往 PostgreSQL 可用 tstzrange + EXCLUDE 约束等价替换）。进程为单进程多线程、SQLite 单写者，全部持久数据落在 --data-dir。

数据模型（DIR 内 SQLite）：users(id, username UNIQUE, password_hash, role ∈ {admin,resident})；sessions(token PRIMARY KEY, user_id, expires_at)；resources(id, name, active)；bookings(id, resource_id, owner_id, start_epoch INTEGER, end_epoch INTEGER, start_iso, end_iso, note, status ∈ {active,cancelled} 默认 active, created_at, cancelled_at)。索引：UNIQUE(resource_id,start_epoch) 作为同起点守卫，另建 (resource_id,status) 与 (owner_id,status)。时段按带偏移 ISO8601 解析为 UTC epoch 整数做真实时刻比较，语义为半开区间 [start,end)。

并发与重叠：每次写入使用 BEGIN IMMEDIATE 事务，顺序为校验→SELECT 重叠（status='active' AND start_epoch < :end AND end_epoch > :start）→INSERT；命中重叠返回 409。同一设施重叠最多一笔成功，不同设施互不阻塞。

API 契约（与 CONTRACT 完全一致）：POST /api/login、POST /api/logout；GET /api/me；GET /api/resources、POST /api/resources（admin）；GET /api/availability?resource_id=；POST /api/bookings；GET /api/bookings、GET /api/bookings/{id}；POST /api/bookings/{id}/cancel。错误契约：校验失败一律为非 2xx（400 参数非法、401 未登录、403 越权、404 不存在、409 重叠），响应体为 JSON 形如 {"error":"可读原因"}，绝不返回伪成功。状态机：booking 仅 active→cancelled 单向，重复取消幂等返回同一记录。

UI/适配契约：GET / 返回可用中文 UI，与 JSON API 共享同一真实状态；必需 data-testid=login-username,login-password,login-submit,resource-name,resource-save,booking-resource,booking-start,booking-end,booking-note,booking-save,logout；仅在登录/角色满足后显示相关控件；booking-start/end 为可输入显式时区偏移的 ISO8601 文本框以避免浏览器改写；select 的 option value 等于 resource_id。测试适配器据此以 HTTP（urllib + http.cookiejar）驱动真实登录与预约。

非功能要求：只绑定 127.0.0.1，无外部网络、遥测、子进程、任意文件访问或安装；口令用标准库哈希存储，会话由服务端持有，角色与 owner 只取自会话，客户端提交的 user_id/role 一律忽略；应用文件不超过 12 个，数据只在 DIR 内。

边界见 limits。
