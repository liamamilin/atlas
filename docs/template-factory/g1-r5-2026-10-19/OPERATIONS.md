# R5 正式执行入口

生产根：`application-atlas-production-pack/atlas/template-factory`。原 campaign、G1 plan、产品、场景r2、failed job、上游SHA与所有历史保持，原授权字节见 authorization/。G1有效绝对截止 `1792437223.754534` 不延期。

必须先核对生产源码SHA、本轮完整门禁和同SHA远端CI全部通过、当前52/4/active0与固定依据一致。登记命令见 CONTRACTS.md；保存 authorization-response.json 和 pending 预算，再用实际 amendment ID 构造 queue-request.json。正文 repair 必须是准备目录已冻结原请求，不修改 note/model/timeout。

正式 `queue-r5` 在同一事务激活 version2、记第五轮和调用原 queue_repair，父暂停时子批次仍暂停。保存 queue-response、实际新job及其snapshot，核对 prepared摘要、五文件scope、v1/case_basis、repair_attempts=0、继承截止，再恢复计划：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli \
  resume plan_87059846caf345d2b2fe690657cf324f
```

这一步通过现有正式服务恢复父/子批次并启动 worker；不 retry 旧 a53，不调用旧 resume-product，不手拼生产目录。观察用 status/report；暂停用相同 plan 的 pause。

新artifact必须经过本轮全维度预审、五文件实际生成、精确差分语义审阅、正式冻结及冻结后独立审阅。通过目录门禁后才发布。标准 development-package 导出与实际 application-development 接收必须绑定同一版本、case、P0及导出摘要；不另给应用一份私下规格。

实际交付后通过 verify-delivery 入正式运行队列。冻结套件与当前固定 machineplan/独立 Chromium 执行器对同一 app 取证；记录实际 runner、suite、target binding、archive、case basis、phase 与预算响应摘要。phase proof 用宿主 register_phase_evidence 流程，不改报告 passed 字段。宿主 assess_g1 以本轮真实证据评估。

G1通过后，原 v1-2026-10-19/t08-request.json 经正式 preview固定自己的T08 plan/digest并run；固定书签、月度预算、多项目会议笔记三分母，不自动扩到十个。T08自身最多8小时，但共用原500总账，G1的5轮例外不扩散。

遇到真实语义阻断或需要第六轮、调用/截止耗尽、外部服务阻塞：保存raw输入/输出、失败、budget与job/checkpoints，正式pause相关plan，完成不受阻文档、检查和提交。不重试换意见，不将协议错误当业务修复，也不将业务失败当协议重试。

## 本轮已实际执行及停止

登记/生效/排队与幂等重放已执行，见 authorization-response、queue-response、*-replay-response。版本2为bamd_ad804106fd7049b1b67b914b8e494300；successor job_7742b1c124be4c9ab3a0096da5cdd772。原 formal-repair-request-NOT-EXECUTED.json 是历史文件名，其精确正文已由本轮queue-request消费，不能重复作为新修订排队。

当前原plan已正式pause，job attempt2为paused_budget，累计56/500、5/5、active0，G1blocked，T08not_started。当前逻辑阶段历史两次追加重试均已耗尽；当前授权不允许直接重试、重新排队或增额。协议失败的正式恢复只复用了前三checkpoint，没有新增CLI，见protocol-recovery-proof。

只读检查仍可执行batch_cli status/report，或GET /api/factory/jobs/job_7742b1c124be4c9ab3a0096da5cdd772。不要将status响应中的旧base deadline当作有效截止；读匹配G1/plan/product的已激活version2，其绝对截止仍1792437223.754534。到期不能用暂停或恢复延期。下一步需要明确、受限且经正式服务登记的额外重试授权/机制；目前没有该授权，因此不提供会绕过限制的恢复命令。若之后有业务修复或已到期，分别需要对应明确授权。
