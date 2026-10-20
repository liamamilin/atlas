# R7 实际停止与恢复边界

原计划已通过正式 `BatchService.action(..., "pause")` 暂停。R7 唯一后继 `job_3a658ba085e8417ea6faad5cb0cdd493` 为 failed / attempt 1；父计划与后继批次均 paused。`actual-plan-pause.json` 是实际响应，`actual-stop-preservation.json` 是暂停后的实际查询。campaign 控制表并未被设置为 budget pause；这里是计划级暂停，不能混称 paused_budget。

六项真实新预审中，scenario_scope、product_completeness、architecture_contract、decisions_defaults、runtime_protocol 通过，phase_acceptance 为 blocked。其原始结果和失败检查点保持原样。任务最后登记的 stage 是第六项 runtime_protocol，因为该项在阶段阻断汇总前完成；真正阻断来自 phase_acceptance，不能把它报告成 runtime_protocol 失败。

独立静态核查确认，绑定的 A05 已创建唯一分类、保存 ID，并在相同 instance_dir 重启后按原 ID 读取分类实体，再检查记录名称归属与 HTML 列表。详见 `independent-real-blocker-review.json`。本次设计预审只收到计划投影及六份文档，没有这些既有程序和附件对 A05/A04 的处置材料。因此目前证据支持宿主送审材料缺口，不能据此新增 A04 验收、修改五份复用程序、删除原 blocker，或宣称实际应用已通过持久化验收。

允许完成的宿主补证准备：校验原绑定 manifest / R6 检查点 / 程序字节，将既有程序与授权处置作为静态材料纳入未来 phase_acceptance 投影，并绑定新摘要。规格和程序不因此改变；完整检查及精确 SHA CI 记录另存。该准备不产生新审阅结果，不替换已存在的检查点。

继续真实重审目前没有合法入口与可用资格：

- 普通同任务重试会读取原 blocked 检查点；改变投影会被 `checkpoint_changed` 拒绝。
- 原 phase scope 的两次普通追加及一次 grant 历史均保留；grant 仅绑定旧 R5 job，已消费 1/1，不能用于本 R7。
- 不能删除检查点、换 operation 冒充首次调用，或以新 job / product / campaign 绕过资格。
- 当前 CLI 77/500、书签修复 7/7、active 0；总 CLI 余额不等于该阶段重试授权。

后续如决定补证重审，需要明确绑定本 R7 job、phase_acceptance 操作、原 proposal、新证据投影、原失败检查点与累计历史的授权，以及正式受限恢复入口。当前旧 `recover-protocol` 不能直接使用，也未虚构可执行的新恢复请求。不能在现有授权下登记新的 grant 或第八轮业务修订。原绝对截止仍为 2026-10-20 19:21:52.855422+08:00；暂停不延长它。

安全的只读现场查询（从仓库根执行，明确原生产 root）：

```sh
PYTHONPATH="$PWD/application-atlas-production-pack" python3 -m template_factory.batch_cli \
  --root "$PWD/application-atlas-production-pack/atlas/template-factory" \
  --pack "$PWD/application-atlas-production-pack" \
  report plan_87059846caf345d2b2fe690657cf324f
```

恢复后仍须按真实预审 → 程序消费 → 聚合 → 冻结 → 冻结后审阅 → 发布 → 标准交接消费 → 首次 P0 → 冻结套件和独立浏览器 → 精确 phase proof → 宿主 G1 的顺序执行。只有 G1 正式 passed 才运行原 T08 三样本；目前不启动。
