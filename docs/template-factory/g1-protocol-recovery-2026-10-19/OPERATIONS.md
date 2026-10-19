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
