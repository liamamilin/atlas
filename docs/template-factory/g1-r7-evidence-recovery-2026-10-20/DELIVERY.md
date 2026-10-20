# R7 补证恢复交付与真实停止报告

本轮已完成宿主补证恢复开发并实际恢复原任务：补证与新六项组合通过、聚合通过、产生一个真实冻结候选。冻结后的独立认知审阅在 600 秒超时，且该阶段历史追加重试 2/2 已耗尽；已正式暂停。**G1 未通过，模板生产主链仍未走通。**

## 本轮实际结果

| 项目 | 实际证据与状态 |
|---|---|
| 授权 | 原件 28,274 字节，SHA-256 `9194614646b37e52e8dbe026f8e383b65f91337925b674ca93940cd968fd7675`，原件与登记来源见 authorization/ |
| 宿主源码 | `a411f8f7991a00633a8843ce3bb998029bf67162`，source tree `61ce9eac8ce3c903831c20885a772f8862ecbe9394fbcda692bfa123530c03e0` |
| 精确源码 CI | [39390500949](https://github.com/liamamilin/atlas/actions/runs/39390500949)，check / docker-integration 均 completed/success；原始响应 ci-source.json |
| 恢复 | 原 job_3a658ba085e8417ea6faad5cb0cdd493，attempt 1 failed → 原子 attempt 2 queued → completed；未新建生产任务 |
| 新资格 | egrant_dd03245306034022bbc046e3b9428955，实际 reservation bud_9ad8e95b29224f249f9d48a654d22b9f，consumed 1/1，实际 call_attempt=2 |
| 审阅追加 | 原 phase blocked 与原六项 blocked 全保留；新 phase passed，新六项 passed，五项旧通过完整身份核验后复用 |
| 补证消费 | 新投影 23 份补证摘要全部匹配；日志记录读取其中 12 份文件；读取请求与偏移见 EVIDENCE_CONSUMPTION_PROOF.json，不声称所有文件均被完整逐字阅读 |
| 程序消费 | 九份 R7 文件 SHA 全部匹配；规格、案例 r1、20 条事实保持；模板 author 调用 0 |
| 聚合 | 独立 aggregate-semantic-review passed，原始输入、双基线来源、程序差分及报告在 actual-attempt-2/ |
| 冻结候选 | tpl_f7ecff8d8fef4deba828aa2a8ef82918，digest ec3f2fc668c20d24b78c22f15eed40779ed38b835c10b7b452aaba725dbb7105；实际下载包在 produced/ |
| 当前阻断 | job_b01427592b164863aab5bedf7b3863bb / attempt 1 / needs_review；队列 stage=acceptance，真正 CLI stage=cognitive-review，cli_timeout 600.48 秒；无完整有效结果 |
| 正式模板 / P0 | 本轮新增冻结候选 1；campaign 累计冻结版本 2；正式发布模板 0；真实 P0 开发、交付、独立运行均 0 |
| 案例 / 应用实证 | 本轮新增案例与应用实证增量 0，复用同一规范案例 r1 共 1 个；同一 case basis 摘要 a22ff1c0…，不是新建一份独立研究副本 |
| 用量 | 起点 77 → 80/500，新增为补证、聚合、冻结认知审阅各 1 次；活动调用 0；业务修复 7/7；旧协议 grant 1/1 原状，新补证 grant 1/1 |
| 窗口 | 北京时间 2026-10-20 19:21:52.855422 原绝对截止不变；本次停止时未到期，停止原因是后续阶段无追加重试资格 |
| G1 / T08 | 宿主正式 G1 blocked；T08 原书签、月度预算、多项目会议笔记未启动，未替换失败样本 |

## 已交付代码与回归

- evidence_views：只读重建完整提案、五维输入/提示/模型/配置/规则/文件树身份核验、23 项投影；不存在的路径仍拒绝。
- evidence_grants / BudgetLedger / CLI：持久一次性资格与预算原子占用、token/lease、Popen 前意图、启动不确定性保留占用、实际 call_attempt、幂等与期限。
- evidence_recovery / CLI / API：prepare、登记、同任务原子恢复；保存旧状态/错误/事件/检查点；父批次保持暂停直到真实状态核对后 resume。
- cognition：原单项及总览不覆盖，新结果与有效选择追加；共享同字节补证供总览严格验引用；已保存结果只复用。
- 宿主后处理恢复：新源码门禁追加、原已完成结果摘要绑定、完整输入不变，不产生新 CLI 资格；本轮现场未触发，仅做 temp-store 回归。

本轮完整 13 组最终通过：后端 687（8 项既定 skip）、web unit 9、默认 E2E 17、工厂 E2E 27、严格 Docker 20（0 skip），以及审计/ruff/数据导出生成校验/typecheck/build。检查前后源码摘要一致。初轮 CLI 兼容性失败和修复后日志分别保存，未删除失败。

定向 18 项、旧路径兼容 6 项、CLI 可靠性 15 项及 14 subtests；额外负控拒绝旧输入/CP/授权/程序变更，并发恢复同回执、并发占用只有一个成功、过期拒绝。跨 attempt 的启动前失败 → 实际 attempt 3 调用 → 新源码门禁 → attempt 4 零补调复用为隔离 fixture；不能把这些测试当作现场 P0 运行。

## 未执行与恢复

冻结后的有效独立审阅、正式发布、标准交接被应用开发消费、首次真实 P0、冻结套件与独立浏览器运行、phase proof、G1 passed 和 T08 均未完成。未用历史实验或 fixture 替代。

README §4.1 的 A11 参数遗漏仍在正式字节中，已知差分仅准备未应用。新 phase 将其列为建议；当前停止是冻结审阅超时，没有取得语义 blocker 结论，不能把两者混为一谈。见 README_A11_ERRATUM.json、README_A11_FORMAL_REVIEW_OBSERVATION.json 与 README-A11-NOT-APPLIED.diff。

准确停止点、实际暂停回执、G1 评估、冻结审阅恢复绑定及当前无合法继续请求的边界，分别见 STOP_RECORD.json、operations/pause.stdout.json、G1_ASSESSMENT.json、FROZEN_REVIEW_RECOVERY_BINDING.json、RECOVERY.md。后续批次保留原三场景与原有限额，见 T08_REPORT.json；不建议自动提高额度或重开窗口。

接口与实际请求在 CONTRACTS.md、OPERATIONS.md、operations/。requested model 为 opencode-go/deepseek-v4.1-flash；CLI 未报告 observed_model，保留原始空值，不宣称已观测到真实后端模型身份。
