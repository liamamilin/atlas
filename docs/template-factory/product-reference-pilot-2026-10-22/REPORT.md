# 两种产品形态：真实生成验证结果

## 结论

两项真实验证已经结束，**0/2 达到静态通过门槛**。两份都完成研究与生成，但被确定性检查拦下；工厂独立模型审阅、合格参考包冻结、目录登记均为 **0**，应用运行 **0**。全量任务仍为用户要求的暂停状态，没有自动开展第二轮。

本轮不能证明新模板已经有效，也不能据此断言 DeepSeek 的产品理解能力不足。已确认的共性是：发送给模型的输出合同没有完整表达宿主的枚举和图引用规则，同时生成内容确实存在规则、动作、断言和切片未闭合的问题。宿主成功阻止了不合格结果进入合格包。

## 两个实际样本

| 样本 | 场景／固定案例 | 真实结果 | 可阅读草稿 |
| --- | --- | --- | --- |
| 书签管理 | 生活待购与灵感收藏夹 r2；lakhindarpal/bookmark-manager `539881bc67099d491e8ab6f85de0f443fa7de623` | 研究 24 条观察；生成 1 角色、3 对象、10 动作、3 旅程、14 规则、16 断言、4 切片；结构校验失败 | [未通过候选](bookmark-manager/CANDIDATE.readable.json)、[实际失败](bookmark-manager/OUTCOME.json) |
| 同机聚餐投票 | 同机聚餐地点投票 r1；nextcloud/polls `65bf4627ee9a76c52034e796eda75ae5112ad7c3` | 研究 32 条观察；生成 2 角色、5 对象、6 动作、4 旅程、11 规则、14 断言、6 切片；来源保留检查失败 | [未通过候选](polling-application/CANDIDATE.readable.json)、[实际失败](polling-application/OUTCOME.json) |

这些数量用于描述草稿，不是质量评分或通过证据。候选没有合格 ZIP，不可作为已通过模板下载。

## 实际发现和修复

首轮两次研究使用 `readme/doc/license/source` 类型及阅读工具路径前缀，宿主只接受 `documentation/code_observation` 和固定相对路径。研究提示没有明确列出枚举。两次研究因此在 author 前终止，失败原文见 `OUTCOME.initial-protocol.json` 和 `RESULTS.initial-protocol.json`。

已实现并实际执行局部宿主修复：只接受固定类型别名及精确前缀移除；原文、文件摘要、顺序和行号不变。未知来源、越界和路径穿越继续拒绝。原研究、初始失败和原登记完整保留；通过正式 `align_host` 追加经 CI 验证的源码依据，然后复用研究继续。**恢复没有新建研究会话**。依据见 [逐条适配](PROTOCOL_ADAPTATION.json)、[正式恢复回执](HOST_ALIGNMENT_RECEIPT.json)、[真实恢复状态](RESUMED_AFTER_ALIGNMENT.json)。

## 后续确定性失败与只读诊断

以下诊断不是工厂独审，不代表通过，也没有改写生成内容。

### 书签

正式失败为 `surfaces.s_home.kind: unsupported surface kind`。模型填写的是“Primary list view / Modal capture form / Navigation panel / Detail overlay”，校验器期望平台枚举 `web/desktop/cli/api/library/other`，但发送合同未列出这些取值。

只读诊断在内存中假设平台均为 web 以定位后续问题，不保存为合格候选：

- 4 个 surface 的 navigation 共 14 项为说明文字，宿主期望已有 surface ID。合同只说字符串列表，没有明确引用目标。
- `as_save_to_named_collection` 引用 `r_single_collection`，但其动作 `a_save_bookmark` 未声明该规则。
- `as_open_external_page` 引用 `r_private_single_owner`，但 `a_open_record` 未声明该规则。
- `as_rename_collection_preserves_records` 引用 `r_organization_revisable`，但 `a_rename_collection` 未声明该规则。
- `r_deliberate_capture` 没有断言覆盖，四个切片均受影响。
- 核心、元数据和组织切片选中了默认排序规则，却只能找到依赖延后排序动作的断言，导致当前切片缺少独立覆盖。
- 语义风险：旅程用“保存动作”表达“打开空表单”，而保存动作要求已有合法 URL，并产生持久记录。需要拆清界面准备与业务提交，不应只改枚举后放行。

### 投票

正式失败为 `author observations must retain the researched pinned source tuples`。研究有 32 条观察，author 返回 28 条，保留的 28 条文字和行号完全相同，并非编造或篡改事实。它漏掉四条，并调整了一条顺序：

- `lib/Db/Poll.php` 313–314（投票限额）、462–466（匿名锁定）、230–255（克隆）；
- `lib/Db/Vote.php` 110–122（序列化）。

宿主要求全量原序复述，但 author 提示没有把这条等值约束明确说出。来源本就由宿主固定，不宜让生成端重复搬运整份观察数组。

原始 reference 还包含 `scope_options[3].extra_note` 未支持字段、4 个非平台枚举的 surface kind、说明文字形式的 navigation、未声明的 `absent` 生命周期状态，以及 `create_poll` 改变 tally 状态却未在 object_ids 中声明该对象。没有执行切片通过判定。

## 调用与状态

全部实际启动均请求 `open-design/deepseek-v4.1-flash`，由原正式预算机制计账；渠道未返回可独立核验的 observed_model 标识，不伪造该字段。

| 样本 | 阶段 | 会话用时 | 状态 |
| --- | --- | --- | --- |
| 书签 | research | 83.76 秒 | 已交付并复用 |
| 投票 | research | 123.80 秒 | 已交付并复用 |
| 书签 | author | 157.76 秒 | 已交付，确定性检查失败 |
| 投票 | author | 162.47 秒 | 已交付，确定性检查失败 |

本试跑 **4/6** 次，尚余 **2** 次，**并非额度耗尽**。原计划 **178/7200** 次新增，保留历史基线 99，累计 **277**；活动调用 **0**。原截止 `1795181744.123177` 未重置。未把旧剩余 401 叠加进来。完整会话、正式 reservation、原始返回摘要见 [最终调用台账](FINAL_CALL_LEDGER.json)。

本轮新增案例 **0**，复用案例 **2**；原 52 份案例版本及摘要不变。新增合格认知包 **0**、应用实证运行增量 **0**。原 123 个受保护文件（含六份应用及数据）、原目录摘要均未变，25 份旧开发包已在试跑前后实际下载核对，摘要一致。你提供的参考案例校验也全部通过。见 [保护检查](PRESERVATION_AFTER.json)、[结束后旧包下载](OLD_DOWNLOADS_AFTER.json)。

原全量统计保持：1805 范围，18 复用，7 ready_not_run，16 failed，11 source_unavailable，26 needs_revision，1 paused，1726 pending；本次小样本不冒充全量新增完成。严格 G1/T08 不变。

## 检查与下一轮

相关本地检查：145 项辅助回归、46 项预算回归、8 项试跑／恢复回归通过；Ruff 和差分检查通过。这些是宿主检查，不是模板应用运行。

实际源码提交及完整远端 CI：

- `331f5427c18868f17c7befd0dceb77995cda3a57`：[CI 39768811836](https://github.com/liamamilin/atlas/actions/runs/39768811836)，check / docker-integration 均 success；用于首次研究。
- `dbf7f32c570723baecfd94850ec75d772103af01`：[CI 39772197366](https://github.com/liamamilin/atlas/actions/runs/39772197366)，check / docker-integration 均 success；用于格式恢复及生成。

下一步应先完成[下一轮收敛清单](NEXT_ROUND_PLAN.md)：完整机器输出合同、宿主掌握来源、一次聚合图错误及受限集中修订。优先修一份候选，取得新的完整独审后再判断是否扩大；不把本轮失败仅归结为模型渠道，也不直接放开全量。
