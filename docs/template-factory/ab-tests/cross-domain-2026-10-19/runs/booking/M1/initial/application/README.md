# 社区共享设施的预约与取消（回环本地实验）

面向"一个设施管理员 + 封闭名单内两个居民"的本地预约与取消应用。
纯 Python 标准库实现（`ThreadingHTTPServer` + `sqlite3` + 原生 HTML/CSS/JS），
无第三方依赖、无构建步骤、无外部网络。

## 启动

```
python3 app.py --port PORT --data-dir DIR [--init-demo]
```

- 仅绑定 `127.0.0.1`，不对外监听。
- `--data-dir` 必须显式提供；所有持久数据都落在该目录内。
- `--init-demo` 仅用于本地实验：只在**缺少**演示账号时补建，绝不重置既有账户或记录。
  重复启动（不带 `--init-demo`）不会清空或改写任何数据。

示例（全新一次性目录）：

```
python3 app.py --port 8000 --data-dir /tmp/trial-booking-demo --init-demo
```

启动后浏览器访问 `http://127.0.0.1:8000` 即为可用中文界面。

### 演示账号（显式合成测试数据，非真实凭据）

| 角色 | 用户名 | 口令 |
| --- | --- | --- |
| 设施管理员 | admin | `AtlasDemo-Admin-9!` |
| 居民 | alice | `AtlasDemo-Alice-9!` |
| 居民 | bob | `AtlasDemo-Bob-9!` |

## 存储

- 唯一持久文件：`<data-dir>/trial-booking.sqlite3`（WAL 模式下可能同时出现
  `-wal` / `-shm` 附属文件，均在数据目录内）。
- 表：`users`、`sessions`、`resources`、`bookings`。
- 会话也存于数据库；进程真实重启后数据、状态与账户保持一致。
- 口令以 PBKDF2-HMAC-SHA256 加盐哈希存储；角色与 owner 只取自服务端会话。

## 当前范围（P0）

- F01 登录 / 登出 / 服务端会话。
- F02 管理员创建可预约设施。
- F03 查看设施与占用时段（可用性）。
- F04 提交预约（显式时区 ISO8601、半开区间、结束必须晚于开始）。
- F05 居民查看自己的预约；管理员查看全部。
- F06 取消预约（软取消、幂等、释放原时段）。
- F07 重叠唯一占用（同设施重叠 409）与并发隔离（`BEGIN IMMEDIATE`）。
- F08 持久化与真实重启一致。
- F09 中文浏览器 UI 与固定 `data-testid` 适配契约。
- F10 服务端权限执行（角色不可由请求参数伪造）。
- F11 失败与错误契约（非 2xx + JSON 原因，不伪报成功）。

### HTTP JSON API

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| POST | `/api/login` | `{username,password}` → `{user:{id,username,role}}`，下发会话 Cookie |
| POST | `/api/logout` | 结束会话 |
| GET | `/api/me` | 当前用户，未登录 401 |
| GET | `/api/resources` | `{resources:[{id,name}]}` |
| POST | `/api/resources` | `{name}` → `{id}`，仅管理员 |
| GET | `/api/availability?resource_id=ID` | `{slots:[{start,end}]}`，仅 active、不含他人隐私 |
| POST | `/api/bookings` | `{resource_id,start,end,note}` → `{id,booking}`；owner 取自会话 |
| GET | `/api/bookings` | 居民仅本人，管理员全部 |
| GET | `/api/bookings/{id}` | 单条；居民查看他人 403 |
| POST | `/api/bookings/{id}/cancel` | 软取消，幂等；owner 或管理员 |

错误码：`400` 参数非法、`401` 未登录、`403` 越权、`404` 不存在、`409` 时段重叠。
响应体统一为 `{"error":"可读原因"}`。

### 时段语义

- 输入必须是**带显式时区偏移**的 ISO8601（如 `2035-01-01T00:00:00+08:00`）。
- 内部按 UTC 实例（epoch 秒）存储与比较；对外渲染为规范化 UTC ISO8601。
- 区间为半开 `[start, end)`：相邻区间可预约，重叠区间返回 409。

## 文件结构

```
app.py           入口：参数解析、建库、启动回环服务器
db.py            SQLite 连接、建表、演示账号种子表结构
auth.py          口令哈希、会话、Cookie
isoutil.py       ISO8601 解析与规范化
store.py         设施 / 可用性 / 预约 / 取消（事务与重叠校验）
api.py           HTTP 路由、JSON 响应、静态资源、错误契约
static/index.html  中文 UI 与必需 data-testid
static/app.js      前端交互（真实调用 JSON API）
static/style.css   样式
README.md / DECISIONS.md  文档
```

## 限制

- 仅回环本地演示：不集成邮件、真实住户、支付/押金、公网身份或任何外部网络。
- 单进程 SQLite 单写者；并发保证限于本进程 + `BEGIN IMMEDIATE` 串行事务，
  不构成跨主机或多副本强保证。
- 仅 1 名管理员 + 2 名合成居民；无多租户、无组织层级。
- 无审批流、规则引擎、通知、等待名单、审计导出与账单（仅预留状态/时间戳字段）。
- 时区比较以 UTC 实例为准；不处理按本地墙钟的重复排期与夏令时特例。
- 取消为软取消，保留状态记录；不提供物理删除或保留期策略。
- 会话 Cookie 未设 `Secure`（本地 http 回环）；未实现 CSRF 令牌（单机本地演示）。
- 验收由独立操作员执行；本应用自身未在生成期运行任何测试。

## 后续路线（尚未实现）

- 审批流（`pending` → 批准/拒绝，按设施自动批准）。
- 按设施规则（营业时间、客人上限、费用/押金、材料要求）。
- 日历视图、管理员代订与重复排期、闭馆封禁时段。
- 配额 / 等待名单 / 信用额度（需先做产品决策）。
- 审计轨迹与导出、通知（明确不在本场景范围）。
