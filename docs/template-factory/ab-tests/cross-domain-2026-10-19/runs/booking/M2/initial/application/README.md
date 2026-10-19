# 社区共享设施预约（trial-booking · P0）

回环本地演示应用：一个设施管理员与两名合成居民登录后，管理员创建可预约设施，
居民查看占用时段、按时段预约、查看与取消自己的预约；同一设施不能被重复占用，
权限完全由服务端会话与角色执行，数据在刷新与真实重启后保持一致。

技术栈：**CPython 3.10 标准库 `ThreadingHTTPServer` + `sqlite3` + 原生 HTML/CSS/JS**，
无第三方依赖、无安装构建、无外部网络与遥测。UI 为中文，且与 JSON API 共享同一真实状态。

## 启动

```bash
# 从 app/ 目录（app.py 所在目录）运行
python3 app.py --port 8000 --data-dir /path/to/data --init-demo
```

- `--port`：监听端口（默认 8000）。**只绑定 `127.0.0.1`**，不对外监听。
- `--data-dir`：全部持久数据目录（默认 `app.py` 同级的 `data/`），目录不存在会被创建。
- `--init-demo`：**仅在空库**创建合成演示账号；已有账户或记录时不做任何改动/重置。
  进程重启时不带该参数即可，数据不会重置。首次启动（web 模式）若库为空，需至少运行一次
  带 `--init-demo` 的启动来创建演示账号。

启动后访问：`http://127.0.0.1:8000/`（GET `/` 返回中文 UI）。

### 合成演示账号（本地测试数据，非真实凭据，切勿复用）

| 角色 | 用户名 | 口令 | 权限 |
| --- | --- | --- | --- |
| 设施管理员 | `admin` | `AtlasDemo-Admin-9!` | 创建设施；查看全部预约；取消任意预约 |
| 居民 | `alice` | `AtlasDemo-Alice-9!` | 查看设施/占用时段；提交、查看、取消**本人**预约 |
| 居民 | `bob` | `AtlasDemo-Bob-9!` | 同上（第二个居民，用于越权边界验证） |

## 存储

- 单个 SQLite 文件：`<DIR>/booking.sqlite3`，全部持久数据只在此文件内。
- 表：`users`、`sessions`、`resources`、`bookings`。
- 会话（`sessions.token`，30 天 TTL）与口令哈希均落库，因此重启后仍可继续登录。
- 时段时间以 **UTC epoch 整数**存储并按真实时刻比较；另存规范化 ISO8601 文本用于渲染。
  区间语义为**半开区间** `[start, end)`。
- 取消为**软取消**：保留记录并把 `status` 置为 `cancelled`，原时段随之释放。
- 索引：`(resource_id, status)`、`(owner_id, status)`，以及仅对 `status='active'` 生效的
  `UNIQUE(resource_id, start_epoch)` 同起点守卫。

## HTTP API（与 CONTRACT 一致）

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| POST | `/api/login` | `{username,password}` → `{user:{id,username,role}}`，下发会话 Cookie |
| POST | `/api/logout` | 结束会话（200） |
| GET | `/api/me` | 当前用户或 401 |
| GET | `/api/resources` | `{resources:[{id,name}]}`（需登录） |
| POST | `/api/resources` | `{name}` → `{id}`；**仅管理员** |
| GET | `/api/availability?resource_id=ID` | `{slots:[{start,end}]}`，仅 active、仅时段字段 |
| POST | `/api/bookings` | `{resource_id,start,end,note}` → `{id}`；owner 取自会话 |
| GET | `/api/bookings` | `{bookings:[…]}`，居民仅本人，管理员全部 |
| GET | `/api/bookings/{id}` | 单条；居民访问他人 403 |
| POST | `/api/bookings/{id}/cancel` | 幂等软取消，owner 或管理员 |

错误契约：校验失败一律为非 2xx 的 JSON `{"error":"可读原因"}`——`400` 参数/时间非法、
`401` 未登录、`403` 越权、`404` 不存在、`409` 时段重叠。**绝不返回伪成功。**
服务端始终忽略请求体中的 `user_id`/`owner_id`/`role`，角色与归属只取自会话。

UI 适配契约：`GET /` 暴露固定 `data-testid`（`login-username`、`login-password`、`login-submit`、
`resource-name`、`resource-save`、`booking-resource`、`booking-start`、`booking-end`、
`booking-note`、`booking-save`、`logout`），并按登录与角色显示；`booking-resource` 的
`option value` 等于 `resource_id`；`booking-start`/`booking-end` 为可输入显式时区偏移的
ISO8601 文本框，以避免浏览器改写时区。

## 本次交付范围（P0，已实现）

- F01 登录 / 登出 / 服务端会话（Cookie）
- F02 管理员创建可预约设施
- F03 查看设施与占用时段（可用性，不含他人个人细节）
- F04 提交预约：ISO8601 带时区、按真实时刻比较、结束 > 开始、半开相邻可预约
- F05 查看本人预约 / 管理员查看全部
- F06 取消预约：幂等、保留状态、释放时段
- F07 重叠唯一占用与并发隔离（同一设施最多一笔成功，不同设施互不阻塞）
- F08 持久化与真实重启一致
- F09 中文浏览器 UI 与 data-testid 适配契约
- F10 服务端权限执行（角色/owner 不可伪造）
- F11 失败与错误契约（非 2xx + JSON 原因，不伪报成功）

## 已知边界与限制

- 仅回环本地演示：不集成邮件、真实住户、支付/押金、公网身份或外部网络。
- 单进程 `ThreadingHTTPServer` + SQLite 单写者；并发保证基于 `BEGIN IMMEDIATE` 串行写事务，
  不构成跨主机或多副本的强一致保证。
- 仅三个合成账户、单社区，无多租户/组织层级。
- 无审批流、规则引擎、通知、等待名单、审计导出、账单；仅预留 `status` 与时间戳字段。
- 时区比较以 UTC 实例为准，不处理按本地墙钟的重复排期与夏令时特例。
- 取消为软取消，不提供物理删除或保留期策略。
- 本包内**未运行任何程序**；所有自检状态为 `not_run`，由独立操作员在真实目标上执行验收。

## 后续路线（非本次范围）

1. 审批流与按设施自动批准（复用 `bookings.status`）。
2. 设施规则：营业时间、客人上限、费用/押金（需产品决策）。
3. 通知与日历视图；管理员代订与重复排期。
4. 闭馆/封禁时段；配额、等待名单与信用（需社区政策决策）。
5. 审计轨迹、导出与保留期；多楼宇/区域分组。
6. 若转向 PostgreSQL，可用 `tstzrange + EXCLUDE` 等价替换重叠唯一约束。

<!-- 面向操作员的启动/存储说明如上；本文件与 DECISIONS.md 均为交付要求的一部分。 -->
