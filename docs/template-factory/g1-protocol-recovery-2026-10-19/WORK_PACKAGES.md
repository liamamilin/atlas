# 一次性协议恢复工作包与验收对照

基线e430635，原任务attempt2/paused_budget、56次CLI、5轮业务修复、phase_acceptance历史追加2次、active0。附件原始字节归档authorization/，SHA6592fdddfa743947cba4fcd685e3dc36d62e665203cac2c9a20ba029ee3f5829。绝对截止1792437223.754534不变；授权只增加本operation一次协议机会，不新增业务修复。

|工作包|验收|状态/证据|
|---|---|---|
|基线/来源|原附件和固定输入/projection/stdout/56/5/2逐项核对，保护历史|已核对；source、fixed-input-recheck、baseline-records|
|grant|事务登记精确一次、幂等、并发/跨身份拒绝、预留占用与not_started释放保留关联|已实现；定向11项含身份/并发/回滚/释放/低限额与完整联接通过|
|同任务恢复|原paused_budget受限恢复、状态归档、snapshot/CP不变、重放不++、父暂停不抢跑|已实现；同任务恢复/幂等/篡改拒绝、真实Pipeline临时库联接通过|
|观测|预算前preparing；Popen+mark_started后才started；严格坏JSON仍拒绝|已实现；CLI reliability14项含顺序/拒绝不spawn/清理通过|
|检查|定向回归、独立审查、既定13组、本轮源码SHA远端CI|本地13组全部通过，源树未变化；5df2209已推送，远端39282029202排队，官方Actions异常|
|真实恢复|正式登记grant、同jobattempt3、恢复父plan、只消费一次额外协议调用|blocked_external：远端CI未获runner；grant0/1、同任务仍attempt2|
|G1|全维度、五文件、语义审阅、冻结/冻结后审阅、发布、实际交接/P0/独立运行/phase proof/宿主|未运行：真实恢复前被CI外部门禁阻断|
|T08|G1通过后固定原书签/月预算/会议笔记三样本|未启动|

CLI500、生产/静态2、运行1、业务5/5、其他阶段重试2均不扩大。失败、完整语义阻断或截止到期须正式暂停，不补JSON/换意见/换候选。
