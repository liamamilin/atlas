# Atlas 55,651 项全量语义审核结果

审核 `atlas-semantic-55651-2026-10-29` 已完成冻结范围的处理，结论为**带限制完成，保留问题候选及明确失败**。Luna 主审有效结果 55,650 条、失败 1 条；DeepSeek 已完成 7,348 条复核、失败 59 条；主审及应复核队列均无待处理项。所有项目不作无条件通过声明。

启动：2026-10-29T05:44:21.544051+00:00；模型处理结束：2026-10-30T16:33:46.071113+00:00；墙钟耗时 34.82 小时，包含暂停和重试。固定 29 个主领域、55,651 个仓库 ID；原快照、语料摘要、提示词及模型身份核对通过。

主审包含复用的 100 条 Luna 试跑有效结果（legacy-v1 提示词版本单列），其余使用冻结的本轮提示词。历史 DeepSeek 50 次请求费用全计入预算，其中 28 个项目保留独立试跑意见；需要本轮聚焦疑点复核的项目仍另外处理。版本数量和真实回执见验收 JSON。

## 审核结果

下列项目级结果互斥；复核后项目未重复计入前两行。

|项目级结果|数量|
|---|---:|
|主审通过|1,534|
|主审通过但有覆盖限制|46,710|
|独立复核撤销全部线索|2,985|
|独立复核仍有确认线索的项目候选|3,955|
|独立复核含未决线索|380|
|独立复核失败|59|
|复用试跑独立复核意见|28|

主审失败 1 条未取得有效 Luna 结果，已进入独立复核；这不补记为主审成功。DeepSeek 明确失败的 59 项保留为复核缺口。`unreviewed_pending_primary=0` 仅指没有排队未处理项，不掩盖这些失败。逐项失败记录见 [FINAL_ACCEPTANCE.json](FINAL_ACCEPTANCE.json) 的 `failed_projects`。

## 线索与归档对照

双模型意见按 finding 统计，和上一表的项目数不同。以下为本轮聚焦复核，不把试跑独立意见混入同口径：

|聚焦复核意见|线索数|
|---|---:|
|模型确认|6,586|
|模型撤销|5,202|
|模型未决|436|

模型线索类别如下；这些数值不代表已确认错误数。主审原始线索包含复用试跑主审，聚焦复核还可能包含整体证据不足线索，两组分母不同。

|模型类别|主审原始线索|聚焦确认|聚焦撤销|聚焦未决|
|---|---:|---:|---:|---:|
|材料不足|968|384|576|36|
|场景关联疑点|1,869|497|1,338|28|
|许可表述/范围|327|302|18|3|
|前提/条件遗漏|2,212|1,018|1,074|105|
|计划/要求写成事实|950|712|201|34|
|无来源支持的主张|5,327|3,292|1,799|207|
|类型错位|600|381|196|23|

[ISSUES.jsonl](ISSUES.jsonl) 归档 7,372 个有原始线索、遗留意见或审核失败的项目，包含已撤销条目，不能把导出行数当作真实错误数。每项保留仓库链接、输入包和来源 provenance；`human_confirmed` 均为 false。

Codex 对 29 领域的 37 条新增全量审核线索进行了定向归档对照：**12 条得到来源支持、13 条撤销、12 条未决**。用户人工确认仍为 **0**。这是目的抽样，不能推算全库错误率。所支持的线索包括措辞与许可范围问题，并非全数为已证实功能错误。

完整案例表和原文证据链见 [SPOT_REVIEW.md](SPOT_REVIEW.md)、[SOURCE_SPOT_REVIEW.json](SOURCE_SPOT_REVIEW.json)。抽查涵盖 major/minor、模型撤销/未决、README/LICENSE 不一致、第三方许可范围、元数据资料及一仓库 14 个场景关联。相关原始归档文件 SHA-256 与 provenance 全部一致。

代表案例：

- [ha-jemenaoutlook](https://github.com/mvandersteen/ha-jemenaoutlook)：README 明确周/月数据尚未实现，卡片却列为现有能力；支持修正线索。
- [MySQL-Homework](https://github.com/spt3gntlmn/MySQL-Homework)：题目要求被写成已具备功能；应保留要求/目标语气。
- [AWS audit-manager frameworks](https://github.com/aws-samples/audit-manager-custom-security-frameworks)：README 的 MIT-0 与 LICENSE 的 Apache 2.0 表述不同；记录来源不一致并保留 pending。
- [Database-project](https://github.com/ayrustogaru/Database-project)：许可版权行指向 CodePen 表单，需查清文件授权适用范围；不由模型裁定整体授权。
- [ASCOMPlatform](https://github.com/ASCOMInitiative/ASCOMPlatform)：归档实际提供 SOFA 源码更新、库和测试工程步骤，撤销双模型的无来源支持判断。
- [imgAnnotation](https://github.com/alexklaeser/imgAnnotation)：README 的 GPL 声明不能证明存在独立 LICENSE 文件，撤销模型所称 pending 标签冲突。
- [Inventory-Order-Management-System](https://github.com/FaroukOyekunle/Inventory-Order-Management-System)：共享仓库的 CRM 关联已标 unverified 并列缺项，保留限定后的部分关联。

插件的 application/library 粗分类、First steps 是否表示未完成、局部 TODO 对整个功能的影响等保持未决，避免把标签规范或材料不足直接当作错误。

## 费用与预算

费用仅归属本审核请求，包含历史 Luna 100 条、DeepSeek 50 条及历史无用量回执的未知费用预留。未购买额外订阅、未提高预算、未修改计费路由。

|预算口径|美元|
|---|---:|
|按回执/费率核算并逐请求向上取整|$46.035060|
|预算扣账（Luna 保守上界 + Go 已报告费用）|$46.045201|
|未知费用全额预留|$0.216465|
|扣账与预留合计|$46.261666|
|原 $50 上限内剩余|$3.738334|

此前在保守预留接近 $50 时停付。按用户授权逐条对账后，7,525 个 Go balance 已结算回执 `usage.cost=list_cost` 合计 $7.71163261，替代了约 $12.04 的峰值预留；同时补正了 Luna 缓存写入费用估算，并校验长上下文倍数；Luna 原预算上界已经覆盖这些费用，本次保留该上界。旧账本、旧 MANIFEST、逐条金额变更和 17 项离线检查均已保留，随后才续跑。见 [COST_RECONCILIATION.json](COST_RECONCILIATION.json)、[对账检查](cost-reconciliation-20261030/CHECKS.json)。未知预留未释放。

Go 使用提供方已报告的请求费用；Luna 使用真实 token 用量按公开费率核算，并以更高输入上界控制预算。两者与提供方组织级最终账单分列，本次没有下载最终账单，也未声称组织总账余额等于此审核余额。

费率依据：[Luna 官方模型说明](https://developers.openai.com/api/docs/models/gpt-6-luna)、[缓存写入计费说明](https://developers.openai.com/api/docs/guides/prompt-caching)、[Go balance 用量说明](https://opencode.ai/v2/docs/console/go/)。Luna 缓存写入替代普通输入计费，超过 272K 输入的请求适用对应长上下文倍数。

## 回执、引用与覆盖限制

|提供方|有用量回执|真实返回模型|费用依据 / 美元|未知费用请求|
|---|---:|---|---|---:|
|openai|55,661|gpt-6-luna|用量按费率：38.224815490|42|
|opencode-go|7,611|deepseek-v4.1-flash|提供方请求报告：7.77793029|3|
|open-design|0|历史无回执|费用未知，保留预算|1|

已重算全部已结算回执的费用并核对返回模型；所有成功项目均有对应模型用量回执，所有输入包 hash 与审核检查点一致。主审带引用线索定位率：11,067/12,129（91.24%）；聚焦复核带引用意见定位率：11,668/12,196（95.67%）。没有引用的条目单列，未算入该分母。

聚焦复核中的模型确认线索均有可定位引文；266 条缺少有效引文的确认已降为未决。定位成功只证明文字在审核包中存在，业务推论、上下文和授权范围仍需判断。

- 仅元数据项目：7,407；包含截断来源的项目：2,580；存在未纳入文件的项目：15。
- 场景关联共 79,779 条，包内纳入 79,779 条；21,336 个项目关联多个场景。
- 主审每项目最多 60,000 来源字符，README/许可/其他文档分别有 40,000/15,000/12,000 字符上限；DeepSeek 只看相关片段及头尾，许可问题提供许可全文包内文本。截断或缺项保留为限制。
- 本次是资料语义审核及来源抽查，没有执行全部软件、逐行审计全部源码，未自动确认所有模型线索。

## 原首轮与资料缺项

原采集首轮结束时，冻结 1,598 叶子内有 **181,823 个未选中的叶子候选行**仍 pending，同一仓库可出现在多个叶子。它们不在本次 55,651 个已发布仓库的审核范围，未启动补采集。

本次冻结项目内，许可待核验 **44,080**、已记录开源许可核验 **11,571**；资料 complete **4,274**、partial **51,377**；类型 unknown **10,667**。这些既有缺项与新的语义错误候选分别统计。README 许可声明、独立 LICENSE 模板匹配、第三方文件许可适用范围也分别保留，不能互相代替。

## 生产保护与交付

生产库只读复查包括全库项目键、叶子归属、场景关系、收藏、OSS 任务及模型配置；另逐项比较冻结 55,651 张卡片数据摘要。结果见 [FINAL_ACCEPTANCE.json](FINAL_ACCEPTANCE.json) 的 `production_baseline`。
所有上述基线一致，未发现审核写回或需另列的用户变更。审核没有重启 API、恢复旧采集任务或修改生产卡片。

交付：[FINAL_ACCEPTANCE.json](FINAL_ACCEPTANCE.json)、[FINAL_MODEL_REVIEW.json](FINAL_MODEL_REVIEW.json)、[ISSUES.jsonl](ISSUES.jsonl)、[归档对照案例](SPOT_REVIEW.md)。原始快照、付费回执、未知预留、失败记录和恢复记录全部保留。后续若修正卡片，应另行确认具体变更，不扩展本次审核范围。
