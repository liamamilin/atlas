# 冻结独审恢复：实际交付与停止点

**G1 仍为 blocked；T08 未开始（0/3）。正式发布模板 0，真实 P0 交付/通过 0/0。** 本轮完成宿主恢复开发和门禁，并实际启动了授权的唯一一次冻结独审；OpenCode Go 返回额度错误，未取得八维报告。

## 实际发生了什么

- 检查通过的源码为 `c5090772b364d9c3f75ce837f70cd2578d414a75`，源码树 `6d4ecacc74fbf419d175249ff949096b985144c75d31639a7484b71364dcfdb1`。
- 本地13组全部通过：后端719项，保留原8项跳过；前端单元9项；默认浏览器17项；工厂浏览器27项；严格Docker20项/0跳过。检查期间源码未变。[检查原文](verification/full-final/checks.json)
- 该精确提交的 GitHub CI [39404477135](https://github.com/liamamilin/atlas/actions/runs/39404477135) 为 completed/success，check与docker-integration均成功。[原始CI记录](ci-source.json)
- 正式 prepare、登记、recover 和 resume 均已执行，同一 `job_b01427592b164863aab5bedf7b3863bb` 从 attempt1→2。恢复后真实查询确认父/子批次仍暂停、snapshot/原空checkpoint集合/旧unavailable保持，随后才正式resume原计划。[实际请求与回执](operations/)
- 新资格 `egrant_c06325f363b84bd9bb1c8fa46f93f945`，新reservation `bud_c06f643f77bb4ce9a7bad57f30f161e1`。实际进程启动，资格已 consumed 1/1；启动时距绝对截止约4636.29秒，满足2700秒余量。授权timeout1800秒，实际生效上限1799.79秒，原snapshot仍600秒。
- 调用模型为 `opencode-go/deepseek-v4.1-flash`。约3.7秒后返回 HTTP429、`provider.quota`、`GoUsageLimitError: Go usage limit exceeded`，provider标注`5 hour`，没有提供reset时间。exit1，delivery_status=failed，observed_model不可见。[真实CLI汇总](actual-attempt-2/job_b01427592b164863aab5bedf7b3863bb/cli-summary.json)、[原始事件](actual-attempt-2/job_b01427592b164863aab5bedf7b3863bb/events.jsonl)
- 没有result.json/report.json，也没有八维审阅结论。新unavailable为`acc_c0cbb5e84d6f475dade4875d8af60174`，旧超时unavailable `acc_74476c79fca949a7a0bd4e4c043d31a6`完整保留。新acceptance通过job_attempt=2及正式recovery/grant/reservation表关联所有调用身份。[关联证明](LINEAGE_PROOF.json)

## 已实现的宿主能力

无损长字符串呈现、逐项源映射/摘要与严格只读ACL；原prompt逐字前缀与受限尾段；原始input字节和language敏感身份；严格类型的单次资格、幂等同任务恢复、累计预算/token/lease/启动意图与消费保护；启动前源码与材料复核；1800秒硬上限与2700秒余量；完整八维、真实冻结引用和原始响应→result→报告绑定；禁止本次自动reference-repair；合法已交付结果的无模型续交；latest-attempt优先和发布资格隔离。

这些能力由隔离fixture验证，包括实际服务→队列→Pipeline→假CLI的完整链。正常/blocked/uncertain/缺维度/非法引用/timeout、输入和模型篡改、越限、失效lease、源码变化、已知framing、checks篡改、宿主写入故障后的attempt3零CLI续交均纳入回归。**fixture通过不能替代本轮真实独审成功。**

## 保留与未运行

原冻结候选`tpl_f7ecff8d8fef4deba828aa2a8ef82918`及digest/归档、原input/source、案例r1、20条事实和九份程序均未改。派生材料16份原文、18个文件；实际不需要超长物理行分段。原外部历史判定未注入模型材料。本轮template author调用为0。

累计CLI为**81/500**（80+本次已启动1）；书签业务修复**7/7**；历史普通追加重试、旧protocol grant1/1与旧phase补证grant1/1均保留。活动调用0。[预算](BUDGET_FINAL.json)、[历史逐表保留验证](operations/final-state.json)

已通过正式plan pause将父/子批次暂停。宿主重新执行G1评估，保持blocked；其中queue_not_quiescent是“计划暂停即不可放行”的门禁原因，不表示仍有活动调用。[正式G1评估](G1_ASSESSMENT.json)、[停止记录](STOP_RECORD.json)

没有执行发布、标准开发交接消费、首次真实P0开发、冻结套件、独立浏览器运行或phase proof。T08原书签/月度预算/多项目会议笔记三个样本未替换、未启动。应用实证本轮新增案例0，复用原案例1；没有上游运行或新增实证成功声明。[精确计数](COUNTS.json)

API5199与前端5188已从该通过检查的源码重启，显式使用原生产根目录。没有为真实调用残留临时测试库路径。

后续边界和可执行诊断见[恢复说明](RECOVERY.md)。此次停止为真实provider额度阻塞，同时唯一资格已消费；不是“准备完成后未执行”。
