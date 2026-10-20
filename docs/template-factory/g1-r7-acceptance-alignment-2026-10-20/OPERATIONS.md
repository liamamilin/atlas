# R7 正式操作合同

生产 root 固定为 `application-atlas-production-pack/atlas/template-factory`，pack 固定为 `application-atlas-production-pack`，命令从仓库根执行并传绝对路径。`ATLAS_FACTORY_ROOT` 不得残留临时路径。任何状态变化通过正式服务/CLI/API；禁止直接改库。

1. 先验证完整13组检查前后源码摘要一致、独立执行器合同及独立审查；提交推送后确认精确提交的 `check` / `docker-integration` 都 completed/success。未通过时不执行后续生产。
2. 正式 `prepare-revision job_f3e32b56036b4ec7bea0c00d6a2a8dc4 --request prepare-request.json`。返回新 proposal、choices、九文件 manifest，四replace五reuse；准备不消费修复、不启动模型。
3. 用 `budget.build_r7_authorization_request(store, prepared_request, summary=..., reason=...)` 生成 `amendment-request.json`；正式 `amendment-register --request ...`，保存 pending V4 真响应。授权原件和稳定key不替换。
4. 使用真实返回 amendment ID 调用 `product_recovery.build_r7_product_resume_request(store, prepared_request, amendment_id)`，保存 `queue-request.json`。正式 `resume-product plan_87059846caf345d2b2fe690657cf324f --request ...`。该事务唯一激活6→7、唯一后继入队，继承绝对截止1792495312.855422，不启动worker。
5. 再查询真实任务/预算/父批次：CLI71、修复7、active0、后继queued attempt1、父paused、旧job failed attempt1、全部旧CP/记录不变；稳定请求回放返回同后继且不重复计数。receipt不能代替实际状态。
6. 正式 `resume plan_87059846caf345d2b2fe690657cf324f`。执行六项新设计预审，宿主确定补丁供四程序且五程序R6原字节；模板author0；双基线及授权/实际生成元数据经新聚合审阅，之后冻结及冻结后独立审阅。
7. 仅符合目录资格的精确摘要才正式publish。标准application-development生成并消费P0交接包，归档包摘要/消费CP；首次P0正常模型调用计原campaign。失败需要业务修复时7/7已用完，禁止重建initial P0绕过。
8. 实际交付冻结套件验证，A11 app_root绑定该真实应用；按原冻结machineplan完成独立浏览器、同容器重启/非法输入/并发写入/清理，注册精确phase proof后正式assess_g1。
9. 只有宿主G1 passed才启动原T08书签、月度预算、多项目会议笔记三个固定样本。保留原500总额及其他产品2轮、独立T08首次窗口/并发规则。

绝对截止、追加重试额度、有效语义门禁、外部服务或范围门禁阻断时，正式pause并保留真实报告/原始返回/台账。不会自行增加第八轮、第二次grant、延长窗口或替换失败样本。

本文件描述真实已实现接口与执行顺序；具体是否已运行，以本目录实际响应、STOP_RECORD、G1_ASSESSMENT为准，不以操作文档当作通过证明。
