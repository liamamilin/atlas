# 一次性协议 grant 与同任务恢复合同

授权来源为 authorization/ 原始附件，SHA6592fdddfa743947cba4fcd685e3dc36d62e665203cac2c9a20ba029ee3f5829。不是预算amendment version3，不新增业务修复或时间。稳定完整登记请求见grant-request.json（schema atlas.protocol-retry-grant.v1）。

- POST /api/factory/v1/budget/protocol-grants：上述完整请求；服务事务内先幂等再首次56/5/2/active0校验，核对固定原失败reservation、原input/source/stdout/prompt与有效截止。返回pgrant_*和available状态。同键异请求或重复额外机会拒绝。
- GET /api/factory/v1/budget/protocol-grants/{id}：正式grant状态。预算报告含protocol_retry_grants和protocol_retry_grant_uses，使用记录与reservation关联。
- POST /api/factory/v1/jobs/job_7742b1c124be4c9ab3a0096da5cdd772/recover-protocol：{grant_id,idempotency_key:"atlas-g1-phase-protocol-resume-2026-10-19-v1"}。只允许固定paused_budget attempt2；事务归档旧state/error/stage/attempt/token/lease、snapshot及checkpoint摘要，再同job进入queued/attempt3；不改snapshot、原checkpoint或旧attempt目录；重放返回原恢复记录。
- 恢复不启动worker，关联批次必须保持paused。检查返回后，通过既有原plan resume恢复并启动worker。

实际预留仍由BudgetLedger.reserve同一写事务检查500/截止/并发/更低限制，再严格匹配原campaign/plan/product/job/operation/scope/model及五个实际上下文摘要。普通上限仍2；仅精确可用grant允许当前operation retry=1进入逻辑scope的第三次追加（不写retry=3）。grant与reservation/use同事务关联；预留占用，started/uncertain消耗，仅确定not_started可释放且保留关联历史。其他job/operation/campaign/产品/T08不适用。

pipeline预算前事件现为preparing；CLI Popen成功且mark_started完成后才发started，并在受保护清理区内。旧“started”日志不改写。严格拒绝原坏JSON，不补结构或提取嵌套passed。

## 实际消费与当前边界

原grant一次消费的phase_acceptance完整通过，未再放宽协议上限。后续宿主汇总恢复采用既有failed retry，同job进入attempt4，六项检查点原文保留。当前五文件交付后的来源结构门禁失败，计划正式暂停；recover-protocol幂等返回的attempt3历史receipt不代表当前job可继续。必须查询实际job/父计划/预算。

来源资格分别记录：case-level独立accepted不等于scenario-linked事实可用。本轮固定facts policy为accepted-linked-observations-only-v1，不得借增加来源目录、修改canonical链接或恢复legacy策略绕过该固定输入。下一修订须明确授权字段和依据范围；本次未获得第6轮业务修复、第二grant或延期。
