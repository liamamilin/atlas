# 决策与默认值

## D01 · 是否需要预约审批流，还是提交即确认？

默认提交即确认（无审批），保留 booking.status 字段；理由：确认掩盖场景直接预约可立即使用，且不引入未被要求的审批端点。

When to ask / 询问条件: 运营方要求某些设施需工作人员批准，或按设施类型自动批准时。

新增 pending 状态、管理员批准/拒绝端点与相应验收；改变 P0 可用性语义。

decided-default

## D02 · 重叠占用在应用层事务校验还是数据库排除约束？

默认 SQLite BEGIN IMMEDIATE 串行事务内先 SELECT 重叠再 INSERT，并以 UNIQUE(resource_id,start_epoch) 作同起点守卫；理由：CONTRACT 固定标准库+SQLite，无排除约束。

When to ask / 询问条件: 预期多进程/高并发写入，或迁往 PostgreSQL 时。

数据层实现与并发验收；PostgreSQL 可用 tstzrange + EXCLUDE 约束（S11）等价替换。

decided-default

## D03 · 时段如何表示与比较？

默认把带显式偏移的 ISO8601 解析为 UTC epoch 整数存储与比较，并按实例渲染规范化 ISO；区间为半开 [start,end)。

When to ask / 询问条件: 需要按本地墙钟时间做重复排期或处理夏令时语义时。

校验、排序与可用性计算。

decided-default

## D04 · 取消是软删除还是物理删除？

默认软取消：保留行、status=cancelled，重复取消幂等返回同一记录；理由：确认验收要求保留状态记录、不破坏历史。

When to ask / 询问条件: 存在法务保留期限或用户删除权要求时。

数据模型、可用性过滤与取消验收。

decided-default

## D05 · 认证与会话如何实现？

默认标准库哈希存储口令 + 服务端会话 Cookie，角色与 owner 仅取自会话；理由：角色不可由请求参数伪造是硬验收。

When to ask / 询问条件: 需要外部身份/SSO 时（本场景明确不支持公网身份）。

认证、授权中间件与全部越权验收。

decided-default

## D06 · 演示账号何时创建、是否重置？

默认 --init-demo 仅在空库创建 admin/alice/bob 三个合成账户，绝不重置既有账户或记录；理由：CONTRACT 要求且保证重启一致性。

When to ask / 询问条件: 运营方希望自带账户或自定义种子时。

启动流程与重启一致性验收。

decided-default

## D07 · UI 时间输入采用何种控件？

默认使用可输入显式时区偏移的 ISO8601 文本框；理由：CONTRACT 明确避免浏览器时区改写。

When to ask / 询问条件: 最终用户需要本地时区选择器或自动检测时。

UI 适配契约与端到端可用。

decided-default

## D08 · 成熟类别能力（审批、规则、通知、等待名单、审计、支付）是否本期引入？

默认全部推迟为 phase=null，仅预留状态/记录字段；理由：GUIDANCE 要求不为显得完整而加入未要求功能。

When to ask / 询问条件: 当社区政策明确需要审批、费用押金、通知或配额时逐个决策。

范围、数据模型与后续阶段划分。

decided-default
