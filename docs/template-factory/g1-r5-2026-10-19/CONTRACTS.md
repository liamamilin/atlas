# R5 授权、预算和队列合同

本轮原始授权来源为 `authorization/ATLAS_G1_R5_EXECUTION_CODEX_INSTRUCTIONS.txt`，原始字节 SHA-256 `4d642929aeccdea2a5b0afb5d92157bc54f7e47871f2a3425b05a35268cc9b73`。`authorization/source.json` 记录来源路径、归档路径和字节数；不修改源文件，不把实现报告当成授权。

## 登记（不生效、不记第五轮）

`POST /api/factory/v1/budget/amendments`，body 为 `authorization-request.json`。等价 CLI：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli \
  amendment-register --request docs/template-factory/g1-r5-2026-10-19/authorization-request.json
```

schema 为 `atlas.g1-r5-authorization.v1`；稳定 key `atlas-g1-r5-user-authorization-2026-10-19-v1`。固定 campaign/product/G1 plan、失败 job、plan-1 result、prepared request/effective plan/patch/formal repair 摘要、已激活 version1 前驱和本次实际授权文件。首次事务登记要求 52 次已计入 CLI、4 次业务修复、0 活动预留。完整请求和摘要追加到 `tf_budget_amendment_binding`；旧记录、预算基础值、segment 与授权原文件不修改。

先查稳定幂等请求，再检查首次基准；合法后续消耗到 53/5 时同请求仍返回同一记录。同键异请求、更换 key、错来源/前驱/绑定及重复 version2 均拒绝。

## 生效与正式修订（同一事务）

`POST /api/factory/v1/plans/plan_87059846caf345d2b2fe690657cf324f/queue-r5`。等价 CLI：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli \
  queue-r5 plan_87059846caf345d2b2fe690657cf324f \
  --request docs/template-factory/g1-r5-2026-10-19/queue-request.json
```

`queue-request.json` 在实际登记返回 amendment ID 后写入，四个字段：`amendment_id`、固定 `idempotency_key=atlas-g1-r5-prepared-2026-10-19-v1`、原 `artifact_id`、原样 `repair`（准备目录 formal-repair-request-NOT-EXECUTED.json）。原业务请求摘要 `72991407589cc5cfe950178a7f7ea1dbd0011dad4cd93ca05d77a1956d9a6089`，不随机修改 note/model/timeout。

协调服务复用现有 `queue_repair` 的 caller-owned transaction/ledger：version2 生效、记第5轮、创建 prepared successor 和来源关系一次提交；任一失败全部回滚。父计划暂停时新子批次暂停，不调用 ensure_worker；核对后另走原 plan resume。重放返回同一 batch/job，不重复记账。旧 a53 保持 failed、原 error/attempt/checkpoints 不变，supersession 仅记录正式后继关系。

version2 仅把该 G1 plan 的修复上限 4→5。基础 started `1792389754.633465` / deadline `1792418554.633465` 与 version1 所有字段保留；version2 的 new_deadline 固定继承 `1792437223.754534`，不用 `max(now+window)`。pending 不生效，active 才由统一选择器消费；到期拒绝新调用/预留。其他产品与 T08 不继承这项 G1 例外。CLI 500、并发2/1、更低限制和所有重试历史保留。

## 回归与执行边界

临时库联接回归装载归档完整29观察、实际分离的冻结来源/失败job、五文件scope与52/4，运行真实登记/queue/父暂停领取/resume/Pipeline，到架构预审 spy。模型边界为假CLI；不声称真实预审或应用通过。错误分支、source篡改、inner/outer恢复继续验证。真实生产必须等待本轮新 SHA 的完整门禁与远端CI，实际请求/响应随后分别保存。

## 实际响应与保留边界

实际登记、生效、重放和队列响应均已归档；请求字段详见authorization-request.json与queue-request.json。此次schema/接口不支持额外phase retry或第六轮；不能通过改model/note/request key获得额度。当前正式host assessment见G1_ASSESSMENT.json，原始协议错误/重试预算门禁分开见STOP_RECORD及protocol-recovery-proof。
