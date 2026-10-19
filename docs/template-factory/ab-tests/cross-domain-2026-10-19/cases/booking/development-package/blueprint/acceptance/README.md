# 验收说明（acceptance/README.md）

本目录只包含 P0 验收程序与其说明：acceptance/run.py 与 acceptance/README.md。
本文件仅文档化 run.py 的调用方式与用例编号；run.py 不导入本文件，二者无运行时依赖。

> 生成期状态：全部验收用例状态为 not_run。生成阶段不执行、不安装、不运行任何程序。
> 本程序由独立操作员在显式提供的真实目标上执行；在操作员实际运行并给出结果之前，
> 不得声称任一用例已运行或通过。

## 1. 前置条件

- Python 3 标准库运行环境（无需 pip，不需要安装任何第三方依赖）。
- 一个可运行的真实目标应用（本任务的下游应用），且其仅绑定 127.0.0.1。
- 目标使用 SQLite，全部持久数据落在其 --data-dir 指定的目录内。
- 无外部网络、无遥测；验收程序不会访问公网。

## 2. 目标启动（在运行验收前由操作员完成）

以回环方式启动目标，并仅在全新数据库上初始化合成演示账号：

    python3 app.py --port PORT --data-dir DIR --init-demo

- 目标必须只绑定 127.0.0.1，不得对外监听。
- --init-demo 仅在空库创建演示账号，绝不重置既有账户或记录。
- 启动后应能从 http://127.0.0.1:PORT 访问。

## 3. 合成演示账号（测试数据，非真实凭据）

| 角色 | 用户名 | 口令 |
| --- | --- | --- |
| 设施管理员（admin） | admin | AtlasDemo-Admin-9! |
| 居民（resident） | alice | AtlasDemo-Alice-9! |
| 第二居民（resident2） | bob | AtlasDemo-Bob-9! |

这些口令是显式合成的本地实验测试数据，不是真实凭据，不得复用到其他系统。
除非用 --admin-user 等参数显式覆盖，run.py 默认使用上表账号。

## 4. 运行验收

web 目标模式（连接已启动的目标）：

    python3 acceptance/run.py --base-url http://127.0.0.1:PORT

生命周期模式（由检查器以 shell=False 启动/重启目标，覆盖 A14 真实重启用例）：

    python3 acceptance/run.py --base-url http://127.0.0.1:PORT \
        --app app.py --data-dir DIR --port PORT

全部参数：

- --base-url（必需）：目标回环 origin，如 http://127.0.0.1:8000。仅接受 http 且主机为 127.0.0.1、localhost 或 ::1，且必须显式带端口；不得包含路径、查询、片段或内嵌凭据。
- --app：生命周期模式的目标 app.py 路径（须为存在的文件）。
- --data-dir：生命周期模式的一次性数据目录（须为已存在的自有临时目录；不得是 HOME 或 Downloads）。
- --port：生命周期模式目标监听端口（须与 --base-url 端口一致）。
- --admin-user / --admin-pass：管理员演示账号（须同时提供）。
- --resident-user / --resident-pass：居民演示账号（须同时提供）。
- --resident2-user / --resident2-pass：第二居民演示账号（须同时提供）。
- --timeout：单次请求超时秒数（默认 15）。

## 5. 运行模式

A) web 目标模式：只使用显式提供的回环 origin 与精确端口；重定向在传输层按 origin 校验，跨源跳转被阻断；Cookie 不跨源发送。不豁免全部回环端口。

B) 生命周期模式：当额外提供 --app、--data-dir、--port 时，检查器以 shell=False 启动目标（首次带 --init-demo），并在 A14 中执行一次真实重启（重启不带 --init-demo）以验证数据不被重置、状态保持一致。

## 6. 安全约束

- 只接受 http 回环 origin，且只信任该精确 host:port。
- base-url 不得内嵌凭据；除服务端 Cookie 会话外不支持其他认证模式，并在发起任何请求前显式失败。
- 重定向在传输层按 origin 校验；跨源跳转被阻断，Cookie 不跨源发送。
- 口令仅用于登录配置，绝不写入日志或 URL；失败摘要会脱敏口令。

## 7. 用例 A01..A16 的行为与期望

预期：每条用例均为正向或负向断言；任一断言不成立即计为失败。

- A01 登录/登出与会话：匿名 GET /api/me 返回 401；用 admin 与 alice 登录均返回 200，且 GET /api/me 的 role 与账号角色一致；POST /api/logout 返回 200/204；登出后 GET /api/me 再次返回 401。
- A02 未登录拒绝：未携带会话时 GET /api/bookings、GET /api/me、POST /api/bookings 均返回 401（非空成功、非数据泄露）。
- A03 角色不可伪造：居民 POST /api/resources 返回 403 且设施未被写入；居民提交预约时携带他方 user_id/owner_id/role 被忽略，GET /api/bookings/{id} 的 owner_id 必须等于该居民自身 id。
- A04 管理员建资源：管理员创建资源后，GET /api/resources 中出现该资源且名称一致。
- A05 可用性：GET /api/availability 仅返回 active 预约的时段，包含本人与他人的 active 时段，不含已取消时段；每个时段仅含 start 与 end，不泄露他人个人细节。
- A06 合法预约：使用带显式时区偏移（如 +08:00）的 ISO8601 提交成功并出现在本人列表；半开区间相邻的 [t0,t1) 与 [t1,t2) 均可预约；按真实时刻存储与比较。
- A07 时间校验：end 等于或早于 start、非法 ISO8601、缺少时区偏移均返回 400，且响应为非 2xx 的 JSON 且含可读原因。
- A08 重叠唯一：同一设施重叠时段返回 409，且未写入新记录（active 记录数不变）。
- A09 设施隔离：不同设施在同一时刻的预约互不阻塞，均可成功。
- A10 越权保护：居民查看他人预约详情返回 403、本人列表不含他人预约、取消他人预约返回 403 且原记录状态不变。
- A11 取消幂等：取消本人预约后 status=cancelled，原时段从可用性释放；重复取消返回同一条 cancelled 记录且不产生重复行。
- A12 管理员全局：管理员可查看全部预约并可取消任意（含他人）预约。
- A13 并发隔离：并发发起同一设施重叠预约时恰好 1 笔成功、其余为 409，最终 active 记录数一致。
- A14 刷新与重启一致：刷新后预约一致；在生命周期模式下真实重启进程后，预约 id 与状态、资源与管理员列表均保持一致。
- A15 中文 UI 与适配契约：GET / 返回 200 HTML、含中文内容、包含全部必需 data-testid（login-username、login-password、login-submit、resource-name、resource-save、booking-resource、booking-start、booking-end、booking-note、booking-save、logout），并引用真实接口 /api/login 与 /api/bookings；随后据此通过真实接口完成一次登录与预约并出现在本人列表。
- A16 失败契约：各类校验失败（401/403/404/409/400）均为非 2xx JSON 且含原因，不出现静默成功或伪成功。

用例使用固定未来锚点（2035-01-01Z）而非当前日期，避免依赖运行时刻。

## 8. 生命周期模式与一次性 DIR

- --data-dir 必须是操作员自有的、一次性的临时目录（不能是 HOME 或其 Downloads）。
- 首次启动带 --init-demo，在空库创建合成演示账号。
- A14 触发一次真实重启：先终止进程，再以相同 --data-dir、不带 --init-demo 重新启动。
- 重启后预约与资源必须与重启前一致，证明数据落在 DIR 且不会被重置。

## 9. 退出码与 JSON 摘要

退出码：

- 0：全部用例通过。
- 1：存在失败用例，或安装/生命周期准备阶段失败。
- 2：配置或用法错误（参数非法、origin 非法、账号参数不完整等）。

标准输出为一行的最小 JSON 摘要：

    {"ok": true, "mode": "web", "total": 16,
     "passed": N, "failed": M, "cases": {"A01": "pass", "A07": "fail"}}

存在失败时附加：

    "failures": [{"case": "A07", "reason": "脱敏后的原因"}]

配置错误输出 {"ok": false, "mode": "config", "error": "..."} 并返回 2；准备阶段错误输出 {"ok": false, "mode": "setup", "error": "..."} 并返回 1。摘要中的口令一律脱敏，绝不回显凭据或内嵌凭据的 URL。

## 10. 范围说明

本目录仅含验收程序与其说明，不含任何应用源码、凭据文件或归档。应用本身由下游工作交付；run.py 不是应用，也不作为应用运行。
