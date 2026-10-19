# Atlas 模板工厂 V1 交付与真实验收

状态：当前源码完整门禁通过；本轮真实G1被设计缺陷及业务修复上限阻断，已正式暂停。T08未启动，不能宣称V1完整验收完成。

## 可审查实现

- 实际起点 `d0a206dd749e866619379e152b26a880d1d3c104`，没有重置工作区。
- 第一阶段提交 `4ea4a5922aa67d20f914b67ea7683374efbf50c9`；完整检查后的修复阶段提交 `419074b9d9601f50e9ae088514929095868500d2`，后续宿主审计验证修复提交 `d1a1b8c`；均已推送 `origin/codex/stabilize-atlas`。
- [T01–T08工作包与验收对照](IMPLEMENTATION.md)、[迁移、共享数据、接口与证据合同](CONTRACTS.md)、[正式操作与恢复步骤](OPERATIONS.md)。
- U17只增加固定案例引用和必要消费兼容；没有将深度平台化当作本轮前置。

## 实际检查

[完整检查](verification/FINAL_CHECKS.md)与[机器原始记录](verification/final/checks.json)：后端545项（537执行通过、8已知可选Docker skip），网页单元9项、默认端到端17项、工厂端到端27项；严格Docker专项20项、0 skip。严格专项包含8条实际Docker路径与12条fixture/协议检查，不能描述为20个真实生成应用。生成/导出/数据校验、类型检查、构建、Ruff、pip-audit、npm高危检查通过；保留2个moderate npm依赖告警。

完整运行前后源码摘要一致：`ab3fe454ce8533dec733de9c8d3ec182fdc97550f32bb79195cfea7ec5a71fb8`。[提交绑定](verification/COMMIT_BINDING.json)将此摘要绑定到已推送代码。失败、中断及并发浏览器干扰的旧检查单独归档，未冒充当前通过。

## 本轮真实样例

- 固定 G1 plan `plan_87059846caf345d2b2fe690657cf324f`；同一campaign `atlas-v1-first-production-2026-10-19`。
- 书签场景 r2：生活待购与灵感收藏夹。真实上游 `lakhindarpal/bookmark-manager` 固定commit `539881bc67099d491e8ab6f85de0f443fa7de623`。
- [共享案例规范记录](g1-real-sample/case-record.json)、[固定引用](g1-real-sample/fixed-reference.json)。研究已独立审阅入库，应用实证和模板复用同一记录；29条观察分别为20条代码、8条推断、1条文档。没有执行上游应用，因此不声称上游运行通过。旧33个应用身份和旧引用语义保留。
- 候选A `tpl_7f4c17e834c342e7b462e6bb8b6379e4` / `8d9229d3895b…` 已冻结。[完整内容](g1-real-sample/template-8d9229d3895b/manifest.json)、[独立审阅](g1-real-sample/candidate-reviews.json)返回 uncertain：URL与畸形JSON错误合同待澄清；未发布、未运行。
- 该候选的[真实页面阶段包导出检查](g1-real-sample/candidate-handoff-inspection/HANDOFF.md)只是候选导出检查，不替代真正下游开发作业使用的标准包和G1证据。
- 第二轮规范修订通过正式repair请求执行，只允许architecture_markdown和D04.impact；[检查点比较](g1-real-sample/spec-revision-observation.json)显示其他作者字段未变，全部程序复用。本轮后续设计检查发现产品/UI合同仍不完整，准备继续业务修订时被2轮硬上限阻断；新版本没有冻结，故不存在新程序字节比较或新独立通过，A仍未通过。
- 独立验收[预定计划](independent/PLAN.md)在结果前固定；书签真实核心旅程含浏览器保存、分类移动、搜索、精确打开原URL、同容器重启、非法URL无写入、并发写入不丢失。执行器准备测试是fixture，尚不代表实际应用通过。

## 首批与硬边界

G1没有通过前，T08不启动。[首批请求](t08-request.json)和[事先固定的3场景抽验](SAMPLING_PLAN.json)为书签、月度预算、多项目会议笔记。首批最多10产品，本轮先3个、包含G1复用；失败不能换样本。

G1与T08共用500次CLI会话，生产/静态审阅并发2、运行并发1；单产品业务修复2轮、逻辑阶段追加重试2次。G1固定起点1792389754.633465，截止1792418554.633465；恢复、暂停和修订不重置。书签业务修复已用2/2，认知独立审阅累计追加重试已用2/2；新修订可有合法首次审阅，但不能取得新追加额度。provider内部请求、搜索次数、实际费用与未观测模型身份保持未知。

## 未完成与恢复

当前正式状态见[G1报告](G1_REPORT.md)、[宿主评估](G1_ASSESSMENT.json)和[首批未启动报告](T08_REPORT.json)。缺少合格修订模板、正式发布、真实P0交付及精确目标运行证明；业务修复已用2/2，不会因全局剩余458调用而自动续跑。后续只走正式API/服务/队列；不直接写库补通过，不修改冻结断言，不扩大限额。资源/外部错误的原始日志和正式job检查点保存在本地业务根目录；[恢复入口](OPERATIONS.md)可执行。

[下一批候选与限额建议](NEXT_BATCH.md)与当前固定抽验分开；没有自动排队新候选。

## 真实页面停止点

[页面观察记录](g1-real-sample/g1-ui-observation.json)确认计划已暂停、修复额度耗尽、模板未发布及P0未运行；未点击恢复、重试或发布。

![本轮G1真实停止状态](g1-real-sample/g1-paused-boundary.png)

## 独立执行器最终专项（单列，不是P0）

正式V1 submission/receipt、actual app_root摘要与runtime binding、初始/重启后断言、移动/筛选负控、所有原始并发写入持久化和清理合同已修正。16项Python synthetic回归、Node合约fixture与语法检查通过，详见[准备记录](independent/verification/preparation-2026-10-19.md)；这些不包含在后端545项中，也不是实际应用通过。

实际Docker合成技术探针验证network none、零端口发布、仅宿主loopback中继到固定容器127.0.0.1、GET200、POST302原Location、同容器真实重启后仍可访问；容器和relay清理均证明完成。[探针原记录](independent/verification/network-none-relay-probe.json)明确synthetic。没有运行真实书签P0或Chromium应用旅程，没有phase proof。

[Sol最终独立静态复核](independent/verification/final-review.md)保留旧版网络P1，确认最终runner `c37db3a4aaf013fe80c43fbdcd19dcd90430e12c367c893309e21d37488df817` 的该阻断已关闭。冻结machineplan仍为 `5e352e1cdbad18d5dbf827e37e9e0f394f0e7fbf919b0dd18713f7affb6ebb3a`。执行器就绪不解除生产修复2/2和G1未通过。
