# 一次性协议恢复：代码交付与真实外部停止

**G1 blocked；T08 not_started（0/3）。当前job_7742b1c124be4c9ab3a0096da5cdd772仍为attempt2 / paused_budget，stage为blueprint-spec-review-0-bbc43771a1bbbe99-phase_acceptance。CLI56/500、书签业务修复5/5、历史阶段追加2；本次一次性授权0/1（尚未登记或消费），活动调用0。正式模板0、真实P0通过0；案例新增0，原G1固定依据复用书签案例1。**

有效截止仍1792437223.754534：北京时间2026-10-20 03:13:43.754534（UTC2026-10-19 19:13:43.754534）。本轮停止记录采集时尚未到期；暂停不冻结时间。预算/会议笔记未启动、修复各0，原各上限2不变。

## 已实现和验证

原附件逐字节存authorization/，SHA256为6592fdddfa743947cba4fcd685e3dc36d62e665203cac2c9a20ba029ee3f5829。完整25字段固定请求见grant-request.json。

- 新ProtocolRetryGrantService及正式API/CLI：事务登记绑定原campaign/plan/product/job/失败reservation/operation/模型、input字节与canonical、projection/source/prompt/stdout摘要、原截止和max_extra_calls=1；先幂等后首次56/5/2校验。其他key不能重领。
- BudgetLedger.reserve在原写事务内精确占用grant并创建reservation/use关联，保持operation retry=1而不写逻辑第三次为retry3；正常上限仍2，其他scope/campaign/product/T08及更低限制不获例外。预留占用，started/uncertain消耗；仅确知not_started释放并保留历史关联。未新增amendment或record_repair。
- 新ProtocolRecoveryService及受限入口：只恢复原paused_budget attempt2，核对原协议失败、固定输入和三个已通过checkpoint、prepared plan与case适配；事务归档旧暂停原因/attempt/token/lease、snapshot/checkpoint摘要，再同job进入attempt3；重放不++；旧token失效，父批次继续paused。
- 预算前事件改为preparing；真实started在Popen成功和mark_started后、清理保护区内。旧日志保留。原不完整JSON仍被拒绝，未补括号或手写passed。

定向protocol11项通过，含完整临时V1联接：正式register→同job recover→parent resume→claim→实际Pipeline；复用prepared plan/案例适配/前三CP，只向phase_acceptance发送一次假CLI，五个实际计算摘要与原字节完全一致，账目57/5、重放不增，下一正常维度前终止。这个57仅是临时库测试，**真实生产仍56**。

CLI reliability14项通过，含拒绝不spawn、不发started、真实本地假CLI进程的启动顺序和异常清理、原坏JSON负例。独立Sol审查中发现的问题均已修复，最终无剩余明确缺陷。

本地既定13组全部通过且源树前后不变：后端612项（8项既有可选跳过）、web unit9、默认E2E17、工厂E2E27、严格Docker20项零跳过，其余审计/ruff/导出/数据/类型/构建通过。独立执行器Python/Node/Chromium正负fixture也通过，见verification。fixture不等于真实审阅或P0。

## 准确外部停止点

实现源码已推送5df220983c11387832b870c2990318f0708450c8，源/测试树af50d5df847208717f49a7ff1be3ba807691a65af84f1f350ca387a78d0cf18e。新API已加载该源码，**尚无本轮真实模型执行**；最近真实生产调用仍来源204d4e5beb7d6ce75a462ed342d01a9c03c43df2。最终证据提交HEAD另行报告。

必须的同SHA远端 [CI39282029202](https://github.com/liamamilin/atlas/actions/runs/39282029202) 两个job持续queued，没有通过或代码失败结论。GitHub [官方状态](https://www.githubstatus.com/) 同期报告Actions degraded_performance，事件“Degraded availability for GitHub Actions, GitHub Pages and Webhooks”仍在investigating。原始响应和采集时间见ci-external-wait.json、ci-source-latest.json。服务异常是外部状态佐证，不将其写成已证明的该次排队唯一原因。

因此遵守“远端CI通过后才正式授权/恢复”，保持计划正式pause，**没有登记grant、没有恢复attempt3、没有57次真实调用**。这不是额外协议重试失败，也不是新增业务语义失败。旧paused_budget/budget_retry_limit与其原始协议失败完整保留。

正式宿主assess_g1再次持久化blocked：队列未收敛、旧候选目录/审阅不合格、缺标准交接/实际开发/P0运行；它不被本地检查或CI排队报告覆盖。见G1_ASSESSMENT.json及STOP_RECORD.json。

## 保全、未运行与恢复

after-preservation-proof.json核对原56条reservation、5条repair、version1/version2、基础时间、原job整行和全部checkpoint均未变化；grant/recovery记录均空。原stdout/input/source证据字节未改；没有新candidate、campaign、计划或研究，没有模型/provider切换。provider内部请求、观察模型身份及实际费用仍unknown。

本轮真实phase_acceptance额外机会、decisions_defaults/runtime_protocol、五文件修订、程序语义审阅、冻结/冻结后审阅/发布、标准交接被实际消费、真实P0、冻结套件与独立浏览器、phase proof均**未运行**。T08三个样本未启动。当前正式模板数和P0数未以fixture或旧草案补足。

本次授权仍有效，无须重新索要同一范围许可。待5df2209的远端CI实际成功，重新核对未过绝对截止、仍56/5/2/active0及同输入后，按OPERATIONS的稳定请求正式登记grant、恢复同job、核对父暂停并resume。若已到期则停止新G1生产；本次没有延期授权。额外机会一旦真正启动即最多一次，再失败或完整语义结果需要业务第6轮时正式停，不能重领或换意见。

源码和证据均推送既有codex/stabilize-atlas；不合并主分支或部署其他外部服务。最终HEAD远端CI与实现SHA的CI分别报告，不把本地13组或旧CI写成新远端通过。
