# R6 正式服务与执行顺序

生产根固定为 `application-atlas-production-pack/atlas/template-factory`，pack 固定为 `application-atlas-production-pack`。检查 `ATLAS_FACTORY_ROOT` 不含临时测试目录。所有命令从仓库根执行并显式传入绝对 root/pack；生产变更只经正式服务、API、队列。

1. `prepare-request.json` 使用 `atlas.failed-plan-revision.v2`，绑定原失败 attempt4、f190 proposal、原20条事实、r1案例、授权原件和九程序 manifest。`prepare-response.json` 是只读准备结果，不是入队或验收。
2. 完整13组检查及独立执行器门禁通过，提交推送后确认**同一源码 SHA** 的 `check`、`docker-integration` 均 success。保存门禁摘要与原始日志，然后重新查询正式64/5/active0、旧失败、grant1、原过期窗口。
3. 用 `amendment-request.json` 正式 `amendment-register --request <file>`；返回 V3 pending amendment。登记不激活窗口、不增加业务用量。
4. 从真实 amendment ID 生成 `queue-request.json`：`atlas.product-resume.v2`，原 job/artifact/digest、稳定 key `atlas-g1-r6-source-alignment-successor-2026-10-20-v1`、repair 中携带**原完整 prepare 请求**及准备结果的 cumulative scope，原模型/语言/timeout。执行 `resume-product plan_87059846caf345d2b2fe690657cf324f --request <file>`。同事务激活一次新窗口、记业务6、创建唯一后继与 receipt，父批次保持暂停。
5. 实际查询原失败和后继（不能以 receipt 代替），确认原 attempt4/错误/检查点和 grant1 不变；后继 queued、repair_attempts0、同身份/案例、业务6、CLI64、active0、新截止=activated_at+28800。相同请求重放不得增加后继、业务轮次或截止。
6. 正式 `resume plan_87059846caf345d2b2fe690657cf324f` 启动原计划。新六项设计预审使用新 proposal/projection；继承九份原程序，不重跑 author。之后聚合程序审阅、正式新冻结、冻结后独立审阅和目录发布。
7. 用标准 development 包创建实际 application-development，保存真实消费收据和 P0 交付。冻结套件及独立浏览器 machineplan 在同一精确应用上真实运行；注册精确绑定 phase proof，由正式 `assess_g1` 评估。
8. 仅 G1 正式 passed 后，继续原固定三场景 T08，书签按原规则复用 G1；不替换失败样本。

命令模板：

```sh
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli --root "$PWD/application-atlas-production-pack/atlas/template-factory" --pack "$PWD/application-atlas-production-pack" amendment-register --request docs/template-factory/g1-r6-source-alignment-2026-10-20/amendment-request.json
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli --root "$PWD/application-atlas-production-pack/atlas/template-factory" --pack "$PWD/application-atlas-production-pack" resume-product plan_87059846caf345d2b2fe690657cf324f --request docs/template-factory/g1-r6-source-alignment-2026-10-20/queue-request.json
PYTHONPATH=application-atlas-production-pack python3 -m template_factory.batch_cli --root "$PWD/application-atlas-production-pack/atlas/template-factory" --pack "$PWD/application-atlas-production-pack" resume plan_87059846caf345d2b2fe690657cf324f
```

新语义阻断需要超范围业务/程序修改、重试额度耗尽、外部服务阻断或新窗口到期时正式 pause、保存 raw/ledger/检查点并 assess_g1。总CLI500、业务6/6、旧grant1/1不再提高。真实未运行项不能标记通过。宿主缺陷在本次范围内修复后仍需规定源码检查和精确提交 CI，不能改业务输入重置预算。
