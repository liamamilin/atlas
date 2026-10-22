# 两种产品形态的真实验证

本轮只验证 `product-reference-v1`。全量任务保持暂停，原台账、截止时间及严格 G1/T08 不变。模型固定 `open-design/deepseek-v4.1-flash`，两个样本共最多六次正常会话，不自动做内容修订或技术重试。

| 样本 | 已确认场景 | 研究依据 | 验证重点 |
| --- | --- | --- | --- |
| 书签管理 | 生活待购与灵感收藏夹 r2 | lakhindarpal/bookmark-manager，固定 539881bc67099d491e8ab6f85de0f443fa7de623 | 单人长期整理、保存到再次访问的旅程、组织和检索、错误恢复 |
| 投票应用 | 同机聚餐地点投票 r1 | nextcloud/polls，固定 65bf4627ee9a76c52034e796eda75ae5112ad7c3 | 主持人和参与者、单选及改票、准确汇总、结束禁投和重开 |

共复用两份共享案例，新增案例身份为零。原始来源记录没有独立验证固定版本的 SPDX 标识，不能以默认分支元数据补成固定版本证据；本轮保留原许可文本和该限制，不复制上游实现作为应用。本轮不运行上游或下游代码。

执行命令（从仓库根目录）：

```sh
PYTHONPATH=application-atlas-production-pack:examples/assisted-trials python3 examples/assisted-trials/produce_reference_pilot.py status
PYTHONPATH=application-atlas-production-pack:examples/assisted-trials python3 examples/assisted-trials/produce_reference_pilot.py run
```

`prepare` 仅复用固定来源、保存输入。`register` 要求已有精确提交 CI 成功及正式 host revision 回执，再使用原预算服务登记固定两样本。不得执行全量 `resume/start`。`run` 通过原正式 BudgetLedger 为研究、生成和独审分别计账；独审使用不同实际会话。普通样本失败保存原始返回与 `OUTCOME.json`，继续另一个样本；在途/不确定调用会暂停本试跑，不能盲目重复。

权威材料是每样本的 `INPUTS.json`、`SNAPSHOT.json`、`CASE_REUSE.json`；阶段输入、原始模型返回和读取证据保存在 `official-checkpoints` / `generation` 中。研究项目源码缓存位于用户指定外置目录，模板与验证证据位于本项目。

通过时交付 `generation/reference.zip` 和可阅读的 `PRODUCT_REFERENCE.md`，类型为产品认知参考包，静态审阅通过、应用未运行、未正式发布。它不是旧格式标准开发包，不把静态通过当作应用验证。未通过时不得导出合格包。

结果检查：角色与旅程是否完整；动作、规则、界面、断言及阶段切片是否相互一致；是否明确区分用户需求、上游观察、设计推断和未知；是否如实保留应用未运行。真实结果将在 `RESULTS.json` 和 `REPORT.md` 汇总，未完成的排队或模型交付不算通过。
