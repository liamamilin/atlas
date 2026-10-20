# Atlas G1 R6 实际交付与停止报告

**G1 blocked；T08 0/3 未启动；本轮正式新模板 0、真实 P0 交付/通过 0；案例新增 0、复用 1。CLI 71/500、活动 0；书签业务修复 6/6；旧协议 grant 1/1。**

真正停止点：`job_f3e32b56036b4ec7bea0c00d6a2a8dc4`、attempt1、`aggregate-semantic-review`。候选已构造，但独立聚合语义审阅 blocked，未冻结、未发布。已通过正式服务 pause 原计划，并执行宿主 `assess_g1`，结果 blocked。此结果不是“准备完成”，也不是 G1 通过。

## 实际执行

- 授权原件按原始字节保存；SHA256：`7c36e8048393bf7b3fd7eecc78c3af76e3189d462310d88955ce283dd4ce0168`。
- 正式准备请求摘要 `ac035cf6044801f86838ae43faef95b502f255ae8d42e7b2bd1404abe6a7bcd7`；新规格摘要 `6f806d9416cd1c5a724e980dece7330dac651c8a838d469db409d940a493f158`。21 处精确修订为 7 来源数组、13 依据解释和唯一架构来源句；其他作者业务字段、阶段、覆盖合同和九程序均未改变。
- 正式登记 V3 amendment `bamd_100a302fe8424d9493dafe62d6e43db9`；登记时未激活。正式 `resume-product v2` 在同一事务中激活窗口、记唯一业务第六轮、创建唯一后继、supersession 与收据。真实查询确认父批次暂停、后继 queued、原失败仍 attempt4；随后正式 resume 原计划。相同请求回放返回相同后继和截止，没有重复消费。
- 原截止 **2026-10-20 03:13:43.754534+08:00** 保留。本轮新窗口首次激活 **11:21:52.855422+08:00**，截止 **19:21:52.855422+08:00**（epoch `1792495312.855422`）；暂停和回放没有延期。
- 六项新设计预审全部通过，均有新 proposal/projection/实际输入身份。原六项审阅检查点保留；没有复制旧通过。
- 九份程序从正式 attempt4 检查点与交付文件继承：五份 R5 新交付及四份原复用。逐字节比较全部一致，新增 author/research/case-adaptation 模型调用均为 0。候选的全部作者字段与批准准备规格一致。
- 新增 7 次 CLI：六项新预审和一次聚合程序语义审阅，全部为正常首次调用；没有新增 retry、协议 grant 或第七轮业务修复。请求模型为 `opencode-go/deepseek-v4.1-flash`；真实内部模型身份、provider 请求次数与最终计费未获得权威观测，不推断。

## 真实阻断

独立聚合审阅及独立 Sol 静态复核均确认：

1. **A02**：单标签 hostname 的正向保存只走 HTML 表单。JSON POST 只测试非法 URL，没有验证 JSON 正向接受单标签 hostname；先前 JSON 边界断言的授权负转正未在同一入口保留。
2. **A07**：没有查询仅出现在原始 URL 路径/查询串或分类名中的词，不能区分“只查 title/hostname/description”与错误额外搜索 URL/分类名的实现。

这是**验收程序覆盖缺口**，不是已观察到的目标应用运行失败。修复需要修改已固定程序字节，超出 R6 来源/解释修订和 6/6 容量；没有修改它们、重跑同一输入换结论或提高上限。

审阅同时发现宿主把生成的 `acceptance/plan.json` 混入程序哈希清单却未提供对应材料。该宿主问题已完成限定修复：正式九程序清单单独绑定，生成元数据单列真实文件、前后哈希与差分并纳入聚合摘要。见 HOST_METADATA_FIX.md。**此修复未用于再次真实生产，也没有清除原报告；不能消除 A02/A07 阻断。**

## 检查与提交

真实生产源码为 `2b40dff20bc2761be649bc3ce43b825094bf075c`，完整13组检查通过，源码摘要未变化；远端 [CI 39363405866](https://github.com/liamamilin/atlas/actions/runs/39363405866) 的 check 和 docker-integration 均 success。

实际检查：后端630项（既定8项跳过）、Web单元9项、默认E2E17项、工厂E2E27项、严格Docker20项（零跳过）；Python依赖审计、ruff、Atlas导出、Web生成/数据核验、npm高危审计、typecheck和build均通过。独立执行器23项Python合同、Node合同与真实浏览器负例通过；最初沙盒浏览器启动受限记录与获准环境下的通过结果分开保存。

宿主元数据修复源码为 `7eb137cac6e2b21bbe3bb3dcf3493632a5e436cc`；94项定向测试、编译和diff检查通过。该新源码完整13组全部通过，源码摘要未变化；精确 [CI 39366847618](https://github.com/liamamilin/atlas/actions/runs/39366847618) 的 check 和 docker-integration 均 success。记录见 verification/metadata-fix/ 和 ci-metadata-fix.json。此修复未用于真实复产。

## 保全与未运行

原64次调用、5轮修复、旧两次普通追加加grant一次的3条非空retry记录、已消费grant、旧V1/V2时间行、原failed attempt4/snapshot/全部检查点均保留。案例r1、29条案例观察、20条场景事实（13代码+7推断）和14个原编号来源不变。实际新用量只追加在原campaign/plan/product身份。

未运行：新冻结、冻结后独立审阅、正式发布、标准交接实际消费、真实application-development P0、冻结套件运行、独立浏览器核心旅程、精确phase proof、G1通过及T08三场景生产/抽验。原固定书签、月度预算、多项目会议笔记样本未替换；G1未通过不能启动T08。

完整事实和恢复边界见 STOP_RECORD.json、RECOVERY.md；请求与收据见 actual-amendment-register.json、queue-request.json、actual-queue-receipt.json、actual-queue-replay.json。六新审阅、九程序零字节差、真实候选和原始CLI输出均已归档，candidate-attempt-1-not-frozen 仅为失败候选证据。

下一步需要明确授权针对 A02/A07 的程序修订范围及相应正式业务容量；本轮没有创建该授权或后继。仍须遵守原身份、500总额、旧grant已用完和本轮绝对截止。若截止已过，不能通过恢复、重启或改job重新取得时间。
