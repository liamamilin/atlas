# 阶段与验收

## P0 · 回环本地最小可用预约与取消

管理员创建设施，居民登录后查看占用时段并按时段预约、查看与取消自己的预约；权限由服务端执行，重启后一致。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A01 | positive | 使用合成演示账号可登录并建立服务端会话，GET /api/me 返回当前用户与角色，登出后会话失效。 | acceptance/run.py |
| A02 | negative | 未携带会话访问 GET /api/bookings 返回 401，而非空成功或数据泄露。 | acceptance/run.py |
| A03 | negative | 居民请求创建资源返回 403；居民提交预约时携带他方 user_id/role 一律忽略，owner 取自会话。 | acceptance/run.py |
| A04 | positive | 管理员创建资源后，GET /api/resources 中出现该资源且可供预约。 | acceptance/run.py |
| A05 | positive | GET /api/availability 只返回 active 预约的时段，且不含他人个人细节。 | acceptance/run.py |
| A06 | positive | 居民提交带显式偏移的 ISO8601 预约成功并出现在自己的列表中；相邻半开区间 [t0,t1) 与 [t1,t2) 均可预约。 | acceptance/run.py |
| A07 | negative | 结束不晚于开始或非法/缺时区 ISO8601 返回 400，且响应为非 2xx JSON 且含可读原因。 | acceptance/run.py |
| A08 | negative | 同一设施重叠时段预约返回 409，且未写入新记录、不伪报成功。 | acceptance/run.py |
| A09 | positive | 不同设施在同一时刻的预约互不阻塞，均可成功。 | acceptance/run.py |
| A10 | negative | 居民不能查看他人预约详情、列他不在自己列表、取消他人预约被拒且原记录不变。 | acceptance/run.py |
| A11 | positive | 取消自己的预约后 status=cancelled、原时段在可用性中释放；重复取消返回同一 cancelled 结果且不产生重复记录。 | acceptance/run.py |
| A12 | positive | 管理员可查看全部预约并可取消任意预约。 | acceptance/run.py |
| A13 | positive | 并发发起同一设施重叠预约时最多一笔成功（2xx），其余为 409，最终 active 记录数一致。 | acceptance/run.py |
| A14 | positive | 刷新后资源与预约一致；在提供 app.py 与一次性 DIR 时真实重启进程后数据与状态保持一致。 | acceptance/run.py |
| A15 | positive | GET / 返回可用中文 UI，包含必需 data-testid 控件，按角色显示，并据此完成一次真实登录与预约。 | acceptance/run.py |
| A16 | negative | 各类校验失败均为非 2xx JSON 且含原因说明，不出现静默成功或伪成功。 | acceptance/run.py |
