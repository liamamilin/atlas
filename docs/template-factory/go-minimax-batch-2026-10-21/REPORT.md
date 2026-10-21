# OpenCode Go / MiniMax 三叶子辅助试产

本批实际执行三个不同叶子，完整静态生产成功 **1/3**。新增一份可用辅助模板、一个共享案例；未开发或运行应用，未推进严格 G1/T08。另两项失败保留，不能据此宣称 MiniMax 已能稳定无人值守生产。

## 固定输入与真实结果

请求、授权原文及摘要见 [BATCH_REQUEST.json](BATCH_REQUEST.json)、[AUTHORIZATION.md](AUTHORIZATION.md)、[REGISTRATION.json](REGISTRATION.json)。所有调用请求模型均为 `opencode-go/minimax-m3.1-flash-free`；实际读取模型目录确认此 ID 存在，未发起额外连通探针。CLI 未提供 observed_model，不把请求模型当作可独立核实的实际服务端模型。

| 叶子 / 具体场景 | 研究与固定源码 | 生成 / 独立审阅 / 入库 | 调用 |
| --- | --- | --- | --- |
| 看板任务板 / 个人小项目列与卡片管理 | Kanboard，MIT，`e4fb64e972b0ae255a92cf4b7b03489846ebbffc`，8份源码/文档，26条已接受观察 | 生成成功；新的独立会话完整静态审阅 pass，七维检查均真；辅助入库成功 | 3 |
| 支出跟踪 / 人民币日常支出及月度分类汇总 | ExpenseOwl，`4795569c754f77313ba3237aac5fddd7dc05d0c4`，8份固定源码/文档 | 原生成含3条 Atlas `leaf.md` 引用，违反只收上游固定文件观察的合同；宿主提前拒绝，未送审、未建案例、未入库 | 2 |
| 日历 / 固定 UTC+08:00 月网格与事件管理 | 研究提议 `t4t5/rencal`，但返回 JSON 无效，宿主尚未固定源码版本 | 字符串中的未转义双引号导致 JSON 解析失败；未生成、未审阅、未建案例、未入库 | 1 |

看板范围：个人命名看板、列、卡片、跨列移动与列内排序、列内完整清单/数量和持久化；无协作、账号、WIP与通知。支出范围不含预算、收入和银行同步，与原预算模板有不同核心机制。日历范围含跨日/月半开区间、月网格和事件增改删，不含任务、循环、同步和邀请。完整范围已在调用前固定。

来源：[Kanboard 固定版本](https://github.com/kanboard/kanboard/tree/e4fb64e972b0ae255a92cf4b7b03489846ebbffc)、[ExpenseOwl 固定版本](https://github.com/Tanq16/ExpenseOwl/tree/4795569c754f77313ba3237aac5fddd7dc05d0c4)。失败的日历研究提议不冒充已固定案例。

## 已入库模板与下载

- [Atlas 看板模板入口](http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_b21313b1dac44e3db298d0370cfbb75b)
- [标准开发包（实际下载已核对）](personal-kanban/atlas-development-package.zip)，SHA256 `9198d8aac5dd39e700478d29b21623e5c1978da7f461336b65ab3b2b65bdcfb0`。
- [固定源码证据](personal-kanban/upstream-evidence.zip)、[同一共享案例记录](personal-kanban/case-record.json)、[导入回执](personal-kanban/IMPORT_RECEIPT.json)、[独审原返回](personal-kanban/audit/blueprint-spec-review-aux/RESULT.json)。

制品 `tpl_b21313b1dac44e3db298d0370cfbb75b` 摘要 `ffaf9913f26d2266116ffa0746bdb85d2d2ba87b73e24884b81f4092cfe9c140`。共享案例 `case:auxiliary-batch-minimax-2026-10-21:personal-kanban` r1，摘要 `6c619352cee6c8a85ed501c8cc6b8618357a574a5489a555c0be654ac9cad222`；应用实证与模板共用此份规范记录。

新独审输入摘要 `06b0f967c38db8d30472bd793873c4b0f9b07c9d1937c223614b80e9f63cf302`，结果摘要 `7efb42970d3b88bb8861575f8708d5cfbe7df57919652e5fd4fa96e31e77e646`。完整阅读格式2及实际读取覆盖由宿主验证，未复用旧 pass。各阶段会话 ID 与 reservation 见 [USAGE.json](USAGE.json)。

包内 `HANDOFF.md`、`KNOWLEDGE.md`、`CURRENT_PHASE.json`、`ACCEPTANCE_CONTRACT.json`、`APP_DELIVERY.md`、`PROJECT_DECISIONS.json` 已核对；开发包的 template_digest、同份案例与 model-production 均与正式记录相符。新上下文从 HANDOFF.md 开始。本轮状态是**独立静态审阅通过、应用未运行**；生成验收程序仅 AST 解析及静态审阅，没有运行新应用或上游项目。未把包内声明当运行证据。

## 失败及可重复性

- [支出原失败](daily-expenses/FAILURE.json)、[引用分析](daily-expenses/SOURCE_BINDING_FAILURE_ANALYSIS.json)：第30–32项观察引用 leaf.md，不是固定上游文件。原始模型返回完整保留，未删除、转换或替换这些引用以取得 pass。该项包含未通过的原生成，不能下载为可用模板。
- [日历原失败](personal-calendar/FAILURE.json)、[协议分析](personal-calendar/PROTOCOL_FAILURE_ANALYSIS.json)：最后一条文本第13行第2167列存在未转义引号。CLI 进程 exit0 不等于有效交付；没有完整有效 JSON 可恢复。保留原始文本，不推测修复内容，不盲目重复启动。
- [同输入实际重放](REPLAY_RESULT.json)：新增 CLI **0**、新案例 **0**、新制品 **0**，成功项 export_reused/case_replayed；原两项 FAILURE 字节、CATALOG 字节和导入回执不变。日历保持已失败启动，拒绝重复收费调用。

这证明宿主流程能跨叶子复用、单项失败不阻断其余项、来源错误不能冒充案例、重复执行不创建身份；但本模型此轮首轮全链成功率仅1/3。日历研究约13.3分钟，明显长于另两项；暂不扩大批量规模。下一小轮应先以新提示版本明确分开 Atlas 场景依据与上游事实引用，并把研究输出收敛为短结构化字段，保留本轮失败身份与基线，再对失败原场景做受控复验。不能用这三个样本推出通用可靠性或评定应用质量。

## 宿主变更与验证

仅小范围复用：既有生产器新增模型参数及显式 `leaf-scenario-v1` 提示配置；历史默认 DeepSeek 提示字节不变。增加三项固定清单执行器，沿既有辅助 segment 持久登记9次上限与首次调用开始的8小时窗口，不重置原账本。无自动修订/重试。旧家庭保养修订的调用数改为按原 segment 统计，避免后续调用改变旧包来源声明。

- 生产工具回归 **30项通过**：[HOST_TESTS.log](HOST_TESTS.log)。覆盖模型绑定/防改标、固定请求、9次累计限额、失败隔离、旧检查点、旧修订计数、聚焦重放不清空其他项状态。
- 预算回归 **46项通过**：[BUDGET_TESTS.log](BUDGET_TESTS.log)。
- 完整后端 **773项，跳过8项，整体通过**：[BACKEND_TESTS.log](BACKEND_TESTS.log)。跳过项不冒充执行；真实新应用运行不在本轮范围。
- 修改宿主路径 Ruff 通过。正常远端 CI 按最终提交执行，精确运行结果随本次交付提供。
- [真实API、下载与保护结果](REAL_API_RESULTS.json)、[检查命令](VERIFY.py)：旧17份可用开发包实际下载 SHA 全相同；旧撤回候选仍409不可作为可用包；旧18个案例版本摘要不变；117个原冻结包/数据文件摘要无变化；新包正式下载与案例绑定通过。
- [历史修订真实复用](HISTORICAL_REUSE.json)验证旧家庭保养包在新批次开始后仍原样复用、0调用；[模型防改标检查](MODEL_BINDING_CHECK.json)拒绝将新 MiniMax 来源改标 DeepSeek。
- [真实UI读取](UI_ENTRY_CHECK.json)确认模型、案例、辅助状态和下载入口；页面保留正式工厂独审区的原有含义。

## 账本与收口

真实新增 **6次**，累计 **93→99/500**，活动调用0；失败调用照计。固定9次批次限额剩3次**未用，不自动补调**。耗时逐会话相加2187.38秒（约36.5分钟），11次 websearch、104次 webfetch；抓取不是搜索。CLI 逐步骤去重用量合计 input410800、output10803、reasoning49251、cache_read3962953，不能当作独立上下文长度或计费审计，详情见 USAGE.json。

目录现为 **19条：18份可用、1份待修订历史；6份已有核心运行示例、13条应用未运行**（含那份历史）。本轮新应用0、上游运行0、严格发布0。新增案例1、保留原18个案例版本（不是为失败项提前伪造案例）。严格书签业务修复、grant、旧时间窗口及失败历史均保持；G1依旧 blocked，T08未启动。

当前停止点：三项首轮试产和幂等核验已完成；两项各自在来源校验、研究协议阶段停止，未扩大任务或掩盖失败。后续内容修复需要新候选/提示绑定，不删除现有启动与失败证据。
