# 正式操作顺序

生产根application-atlas-production-pack/atlas/template-factory。先等待本轮源码SHA全部门禁和同SHA远端CI成功，再只读重查56/5/2、active0、pausedattempt2、原证据及绝对截止1792437223.754534。

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli protocol-grant-register --request docs/template-factory/g1-protocol-recovery-2026-10-19/grant-request.json
```

保存真实响应，用实际grant_id生成recover-request.json，稳定恢复key保持atlas-g1-phase-protocol-resume-2026-10-19-v1，然后：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli recover-protocol job_7742b1c124be4c9ab3a0096da5cdd772 --request docs/template-factory/g1-protocol-recovery-2026-10-19/recover-request.json
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli resume plan_87059846caf345d2b2fe690657cf324f
```

登记和恢复可用相同请求幂等重放，不能换key重排。核对同snapshot/原检查点/业务5、父暂停及新attempt3后再resume。GET上述job观察，仅phase_acceptance使用grant；完整交付通过后正常进入decisions_defaults/runtime_protocol、五文件生成、聚合审阅、冻结后审阅、发布/交接/P0/独立运行/phase proof/宿主G1。G1passed才启动原三样本T08。

额外调用失败、完整语义blocked/uncertain需业务修复、其他额度/外部阻塞或截止到期：正式pause原plan，保留原始失败与grant消费，执行assess_g1记录真实状态。不补第二次grant，不新建R6，不修改固定规格/五文件scope/machineplan，不借T08绕过。

## 本轮实际续作及宿主缺陷恢复

原 grant 已登记为 `pgrant_f3595368c14d4b23b6ab536f6d198007`，唯一消费 reservation 为 `bud_9a81a7a4adc14f49b46239ec68ee2fdb`，完整 phase_acceptance 结果通过。其后两个正常首次预审通过，累计 CLI59，业务修复5，grant1/1。不得再次消费该 grant。

attempt3 在宿主汇总严格引用校验时失败；最小修复见 HOST_AGGREGATION_FIX.md。新源码全部门禁及同 SHA CI 通过后，用现有 `POST /api/factory/jobs/job_7742b1c124be4c9ab3a0096da5cdd772/retry` 正式恢复失败任务，进入同 job attempt4。此入口不新增业务修复、grant、产品或固定输入。父计划仍暂停，必须实际 GET 核对59/5/0、相同snapshot和六个检查点、grant1后，调用 `POST /api/factory/v1/plans/plan_87059846caf345d2b2fe690657cf324f/resume`。不能重跑 protocol recovery 来增加 attempt。

## 当前停止点（attempt4）

五文件已交付，构造候选时正式失败：`cognition generation failed structural checks: invalid blueprint references: feature sources`。计划已正式pause，CLI64、业务5、grant1、active0；详见 STOP_RECORD 与 actual-source-eligibility-proof。当前不执行retry/resume、publish或develop：原功能引用与本次固定场景事实视图不一致，不能在保留固定输入的同时纯宿主修复。再次登记/恢复原协议grant只会返回历史记录，并不提供新生产资格。

后续先明确授权业务/依据修订范围，保留当前失败、五文件CP、原grant消费和全部历史；通过正式修订服务创建受授权的后继，不改库、不改旧视图、不把本轮CP挪用为新输入通过。需要重审的维度由新的实际输入身份决定。原截止不变，若已到期须停止G1生产；新业务授权本身不等于延期。T08仍须等真实G1通过。
