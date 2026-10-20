# R7 实施与真实生产结果

本轮已正式实施并执行，尚未完成 G1。六项全新设计预审取得五项 passed、一项 phase_acceptance blocked；已正式暂停原计划，未越过门禁进行聚合、发布或 P0 开发。T08 为 0/3，未换样本。

## 实际交付

- 原始附件已按原 UTF-8 字节归档并登记，SHA256 为 `5fb0792b769739f070f68af6ea196473671c791cd895989026ebf9520e282562`。
- 实现 failed-plan-revision.v3、prepared-program-revision.v1、bounded-revision authorization（内部 V4）、product-resume.v3。准备、登记、原子激活、唯一后继、重放、冲突、回滚和截止检查沿用正式服务，不改写旧版本语义。
- 精确修改 A02 的独立 JSON 正向、A07 的 path/query/分类名排除、A11 自己启动的同源码 fresh 实例检查及必要参数。九项交付四 replace、五 reuse；A01/A03/A08 原断言保留。确定补丁和全部 before/after SHA 见 `PROGRAM_REVISION_MANIFEST.json` 及 `prepared-programs/`。
- 限定 A12 六 save 分支映射、F02 首启、F11 fresh 说明、两项 target adaptation、file_plan 和文档同步；原 32 分支其余合同、案例 r1、20 条场景事实、14 个原来源不变。R6→R7 增量和历史 A→R7 累计分别绑定。
- 修复 R7 可选字段污染旧聚合缓存身份的问题，旧公式回归已验证。新聚合输入按九程序与单列生成 plan 元数据组织；本次真实生产尚未到达聚合，正向假 CLI 链接回归不冒充真实聚合。

## 正式执行

生产源码为 `e97431f323cad8a60ca5bee3ad19c37fd594d10b`，源码树摘要 `2181f5768db76d5fa54589a21e15af8a027d5a203d1ddd6b3b4b494a43bb8e2e`。精确远端 CI `39378796575` 的 check 和 docker-integration 均成功，见 `ci-source.json`。此后实际 prepare、登记、原子入队和 resume，未停在检查完成。

V4 授权 `bamd_f2054b5d9a9b4e80b6a4e379ed04a42a` 于 epoch `1792476987.017052` 激活，截止直接继承 `1792495312.855422`。唯一后继为 `job_3a658ba085e8417ea6faad5cb0cdd493`，attempt 1，batch `bat_6b4fc8bf5b4e42d79bc6a9069277e9f0`。请求原 key 重放返回同一后继和截止；随后真实查询确认 CLI71、修复7、active0、原任务/检查点不变、父计划仍暂停，再正式 resume。

| 新设计预审 | 真实结果 |
|---|---|
| scenario_scope | passed |
| product_completeness | passed |
| architecture_contract | passed |
| phase_acceptance | blocked |
| decisions_defaults | passed |
| runtime_protocol | passed |

六份新结果的原始输入、完整输出、建议、摘要与来源投影已归档在 `actual-production-raw/`、`actual-review-projections/` 和 `actual-six-new-review-proof.json`。所有建议逐项处置见 `R7_REVIEW_SUGGESTIONS.json`，旧 R6 意见处置见 `FINDINGS_DISPOSITION.json`。

## 准确停止点

阶段预审认为缺少分类实体跨重启证据。独立静态核查确认：绑定原 A05 已创建唯一分类、保存 ID、相同 instance_dir 重启后按原 ID 查实体，并验证名称归属及 HTML 记录。附件也明确将这项列为已有覆盖、A04 重命名跨重启列为非阻断建议。本次设计投影没有提供这些程序和处置材料，提示还说程序尚不存在，因此属于送审证据不足；这不证明目标应用通过，也不允许把模型 blocked 改成 passed。

生产在六预审汇总后失败，尚未消费后续程序交付检查点。最后记录 stage 是已通过的 runtime_protocol，真正阻断是 phase_acceptance。新模板 author 调用为 0。已通过正式计划服务暂停父批次及后继；旧 grant、原失败、调用、检查点均保存，见 `actual-stop-preservation.json`。

当前阶段无可用追加重试授权：旧 phase scope 的两次普通追加及一次 grant 均保留，旧 grant 只适用于旧 R5 job。改变投影会被现有 checkpoint_changed 拒绝；不会删除 CP、换操作名或新建任务绕过。因此本轮没有再调用模型寻找更宽松结论。恢复边界见 `RECOVERY.md`。

## 检查与证据性质

生产前完整 13 组检查通过，前后源码摘要一致：后端 664 tests（8 个预期 Docker opt-in skip）、Web unit 9、默认 E2E 17、工厂 E2E 27、严格 Docker 20（零 skip），其余审计、lint、导出、生成、数据核对、类型及构建均通过。日志见 `verification/full-final/checks.json`。受影响独立 Python、Node 合同及真实 Chromium 负控检查另存；这些属于执行器合同回归，不是实际 P0。

18 项受控 fixture 正负测试验证新断言能拒绝对应错误，包括 JSON 单标签拒绝、越界搜索、总空搜索、fresh 偷带记录、缺预置、缺空态、缺 flags、启动/清理失败。临时库/假 CLI 验证九材料、六新预审、author0、预算与幂等；不计正式模板或真实应用。

真实阻断后的宿主补证源码 `717ebf830cc231d25cb198795edec06741e7fb76` 也已单独完成 13/13 组检查：后端 668、Web unit 9、默认 E2E 17、工厂 E2E 27、严格 Docker 20/零 skip；前后源码摘要均为 `65ac7a04eebb78589fe5134524615f78240c0fd114456005a8bc932cbc5b5cf7`。6 项定向回归及独立代码审查同时通过。补证包只读准备完成，11 份 R7 检查点保持原值；没有再次进入真实预审。精确远端 CI 状态见 `ci-host-evidence-fix.json` 和 `FINAL_COMMITS.json`。

## 产品结果与预算

| 项目 | 本轮实际值 |
|---|---|
| 新正式模板 | 0 |
| 真实 P0 交付 / 通过 | 0 / 0 |
| 案例新增 / 复用 | 0 / 1 |
| 新应用实证研究版本 | 0；原共享 r1 仍可读取和复用 |
| G1 | blocked，正式宿主结果见 G1_ASSESSMENT-production-source.json 及最终 G1_ASSESSMENT.json |
| T08 | 0/3，G1 未通过故未启动 |
| CLI / active | 77/500；0 |
| 书签修复 | 7/7 |
| 旧 grant | 1/1 已消费，未新增 |
| 绝对截止 | 北京时间 2026-10-20 19:21:52.855422，不延期 |

旧冻结 A 是历史候选，不能计为本轮新发布。未运行项包括聚合、新候选冻结与冻结后审阅、发布、标准交接消费、首次 P0、冻结套件、独立浏览器、phase proof 及 T08。`STOP_RECORD.json` 保存观察时间、原始失败与正式暂停；源代码补证准备与最终提交/CI另见 `HOST_EVIDENCE_FIX.md` 和 `FINAL_COMMITS.json`。

宿主最新 G1 评估中的 artifact_id 是历史 A，并非本轮 R7 新候选；其未达正式目录资格、无标准开发交接与实际 P0/运行证据，因此仍 blocked。本地 API 和前端已恢复，原生产 root 的任务、预算及有效截止通过 HTTP 200 读回，见 `actual-final-http-state.json`；界面可用不等于生产恢复。
