# R8 实际正式操作与恢复

生产源码：67d7da5d947c552fc32e794f34f46d6cc45b7259；远端 CI 39438435175 的 check/docker-integration completed/success，原始响应见 ci-source.json。所有命令显式使用原根目录，未使用临时测试库。

本轮已实际完成 prepare-revision、amendment-register、resume-product、相同请求重放和原计划 resume。真实请求/响应在 operations/，不可改稳定幂等键后再领取；这些入口的重放只返回原记录。

- amendment：bamd_be0c6137a6c64347855672b1ca51a5ad。
- 唯一 producer：job_dcb163d70a8e400fb07bc606570e2313，子批次 bat_110b70c765c04e57a76c168b1c33f83c。
- activated_at：2026-10-20T22:29:11.151877+08:00；绝对 deadline：2026-10-21T22:29:11.151877+08:00，恰好86400秒。
- 激活现场实际查询：新job queued/attempt1、子批次及原父计划paused、累计调用仍83、修复8/8；旧review行及旧acceptance原字节保留。activation-state.json 是事务后实际数据库只读查询与预算记录，不只是历史receipt。
- 随后正式resume原计划，新任务开始合法首次预审；旧job未做第四次同内容调用。API5199和Web5188已以相同源码重启，source-processes.json记录进程与显式ROOT。

以下命令均在仓库根目录执行。request.json为已实际使用的完整请求，没有待填参数：

```sh
export ATLAS_FACTORY_ROOT='/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack/atlas/template-factory'
export PYTHONPATH='/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack'
python3 -m template_factory.batch_cli --root "$ATLAS_FACTORY_ROOT" prepare-revision job_b01427592b164863aab5bedf7b3863bb --request docs/template-factory/g1-r8-contract-convergence-2026-10-20/prepare-request.json
python3 -m template_factory.batch_cli --root "$ATLAS_FACTORY_ROOT" amendment-register --request docs/template-factory/g1-r8-contract-convergence-2026-10-20/operations/amendment-request.json
python3 -m template_factory.batch_cli --root "$ATLAS_FACTORY_ROOT" resume-product plan_87059846caf345d2b2fe690657cf324f --request docs/template-factory/g1-r8-contract-convergence-2026-10-20/operations/resume-request.json
python3 -m template_factory.batch_cli --root "$ATLAS_FACTORY_ROOT" report plan_87059846caf345d2b2fe690657cf324f
```

准备入口要求原blocked基线仍是最新有效对应独审；新候选产生后不能重新准备旧内容。读取旧授权/恢复回执用相同请求的正式幂等入口，不替换基线或幂等键。resume-product不自动启动worker；本轮已核验实际状态后执行 `batch_cli resume plan_87059846caf345d2b2fe690657cf324f`。不要以该命令作为失败任务的无限重试。

失败或重启先读取当前job/checkpoints、budget reservation与receipt。活跃/不确定调用未排除前不补调。若同一规格合法结果已保存，按既有宿主检查点及确定性恢复规则接续；第九轮业务修复及额外grant不在授权内。所有后续发布、开发、运行和宿主G1评估须保留正式证据，不能因本页记载已激活而声称通过。T08目前尚未启动；必须等宿主G1正式通过后使用原固定三场景请求。

## 本轮正式停止状态

`job_dcb163d70a8e400fb07bc606570e2313` attempt1 的 phase_acceptance 于CLI exit0后因非法JSON交付失败，已有追加scope额度耗尽且旧grant不适用。随后本轮已执行正式 `batch_cli pause plan_87059846caf345d2b2fe690657cf324f`，operations/plan-pause-response.json与final-report.json记录实际parent paused、active0、86+external1=87、repair8/8及原截止未变。当前普通retry或resume-product回执重放不提供新的协议资格。完整停止诊断、历史逐行保护证明见STOP_RECORD.json，未授权的最小续作提议见MINIMUM_CONTINUATION.json；不能把它当grant-request直接登记。G1_ASSESSMENT.json为真实宿主blocked结果；T08未启动。
