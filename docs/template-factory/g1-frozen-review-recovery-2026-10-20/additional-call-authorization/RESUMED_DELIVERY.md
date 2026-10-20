# 追加独审与有效时间恢复：实际交付

旧启动时间限制已按用户后续指令解除，原 G1 任务确已正式恢复并完成一次 OpenCode Go 独审。本次真实停止原因是**冻结模板验收与合同冲突**，不是旧时间门禁或 provider 余额错误。原计划已正式暂停，活动调用 0；未擅自修改冻结交付、增加第八轮业务修复或再次调用模型。

## 已实现与验证

宿主源码提交 `da15a23a4007fa60158a87ee5a24e3d7b86852a7`，已推送 GitHub；[CI 39415837779](https://github.com/liamamilin/atlas/actions/runs/39415837779) completed/success，check 与 docker-integration 成功。代码包括追加单次资格、同任务 attempt 2→3 恢复、保留旧 grant/receipt 的版本迁移、额度失败剩余时间恢复、幂等非滚动激活、CLI 启动及执行期限复核、独立执行器的严格时间合同适配。

最终本地门禁见 TEST_RESULTS.md 与 verification/verified/checks.json：后端 729 项、原有跳过 8；前端单测 9、默认 E2E 17、工厂 E2E 27、严格 Docker 20/0 skip；其余审核、导出、数据检查、typecheck、build 均通过。独立执行器 fixture 27 项及 Chromium 负向 fixture 通过。**这些是宿主和 fixture 检查，不是生成应用的真实 P0 验收。**

## 正式恢复与真实结果

- 原 job：`job_b01427592b164863aab5bedf7b3863bb`，同 snapshot、input、case basis、artifact 与九份交付文件，实际 attempt 3。
- grant：`egrant_5168847ee98d4b7f980779bb9199f44f`，已消费；恢复 receipt：`frec_60a38757ec0c4363a193b922155df22a`。
- reservation：`bud_2b188bf21f09446c843877b9025c1841`，completed；请求模型 `opencode-go/deepseek-v4.1-flash`（CLI 未回传 observed_model，不把请求值冒充服务端观测值），exit 0，676.68 秒，实际调用仅 1 次，未追加引用修复。
- 宿主接受的真实结果：`acc_90be1c382dae42e4b3c2eba0344eeacf`，八维齐全，6 passed、1 uncertain、1 blocked，总体 blocked。原始返回、归一化结果、CLI 摘要和宿主 acceptance 分别保留在 actual-attempt-3/；摘要及严格来源绑定均校验。
- 有效时间：旧额度失败时剩余 4632.611294 秒在首次正式恢复原子激活，截止北京时间 **2026-10-20 20:59:23.965368**。重放未顺延；本次质量暂停也不自动再次停表或延长。

## 质量阻断与只读复核

独审指出两项会误判合规实现的问题，已直接核对冻结代码：

1. `acceptance/p0_library.py:980`，A03 对传入 base_url 无条件要求全部四个初始分类；F02 的后续启动语义允许用户改名、删除非默认分类。首启断言与已使用目标的断言需区分。
2. `acceptance/p1_maturity.py:335`，A13 要求首页出现 `/go/{record_id}`，而 `ARCHITECTURE.md:38` 明确 HTML 链接使用保存的原始 URL、`/go` 是独立 302 端点。
3. 独审还将架构标记 uncertain：A09 依赖软删除记录按 ID 读取成功，但 `ARCHITECTURE.md:37` 没有明确该状态下的 200/404 语义。README A11 argv 表与 runner 不一致继续如实保留。

错误合同当前明确命名为 `atlas.bookmark-error-contract.v2`，集中覆盖归类分支。独审建议补齐或解释其他错误码范围；该建议及空分类搜索/断网证明等建议均原样保留，尚未据此改动规格或断言，不将所有建议擅自当成已证实缺陷。

## 当前主线与用量

| 项目 | 实际状态 |
| --- | --- |
| 正式模板 | 0；历史冻结版本 2，当前候选仍 draft / blocked |
| 标准交接实际消费、真实 P0 交付/运行 | 0；未启动 |
| G1 | 宿主正式 assessment 为 blocked；见 operations/final-g1-assessment.json |
| T08 | 原书签、月度预算、多项目会议笔记 0/3，未启动，未替换样本 |
| 工厂 CLI | 82/500；另有此前授权独立诊断 1，保守合计 **83/500** |
| 书签业务修复 | **7/7**，不变；本轮 template author 调用 0 |
| 新资格 | 1/1 已消费；旧协议、补证和冻结恢复资格均保留 |
| 案例 | 本次新增 0，复用原案例 r1 1 份；原 campaign 累计新增案例修订 1、源码快照 1、关联实证应用 1 |
| 来源 | 原 commit、20 条场景事实、case basis 未变；应用最初创建归因仍按原报告标为 unknown |

正式 pause 请求及响应、实际父/子批次 paused、attempt 3 的 needs_review、台账 active=0 见 operations/。宿主 G1 的其余未满足项是未发布、无开发交付、无运行和交接；没有标记通过或用历史实验替代。

## 恢复边界

本次“恢复调用”已经真实完成，不能再使用该 grant 发起第四次独审。要继续推进，需要先审定上述内容修订的范围与额度，再通过正式修订服务产生新版本并取得相应审阅；当前不具备第八轮业务修复授权。本轮不实施此类内容修改，也不请求用户重复批准已完成的恢复操作。全部历史失败、额度与新调用证据保留。
