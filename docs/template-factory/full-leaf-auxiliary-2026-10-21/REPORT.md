# 可靠 workflow 已通过真实资格验证，全量辅助生产已接续

八步workflow的小范围验证已由正式宿主门禁通过，当前 full / passed。精确源码 `74a678b9861b2833397e36e6e48f7b72425a6f16` 的 CI `39648165191` 全部 success，并已追加正式 host revision；此前 50b620b 的测试时序失败和修复证据保留。

原 launchd 单协调者实际启动了下一批20个叶子，群组消息、聊天室的研究会话已是 started，不只是排队或历史回执。初始实际PID90002；以后以launchctl和正式状态为准。每叶子顺序依赖、模型并发2、每批20自动接续，保留同一campaign、冻结范围、账本和原30天截止。当前只是全量执行中，尚未全量完成。

## 本次检查点

现场时间戳 1792605987.9720268，后续状态见正式 status / PROGRESS.json。

| 项目 | 数量 |
|---|---:|
| 冻结范围 | 1805 |
| 复用已有模板 | 18 |
| 本计划新增可用 | 2 |
| 已实际尝试叶子 | 8 |
| 已处理（含复用和失败） | 24 |
| 失败 | 4 |
| 待修订 | 0 |
| 来源不可用 | 0 |
| unsupported | 0 |
| 未开始 | 1779 |
| 执行中 | 2 |
| 暂停叶子 | 0 |
| 本计划新增CLI | 24 |
| 历史累计CLI | 123 |
| 活动CLI | 2 |
| 剩余本计划额度 | 7176 |

不同叶子的可用模板合计 20；辅助目录另有1条撤回待修订历史，不能计作覆盖。

## 真实验证结果

- 日历完成项真实重放0新增模型调用。支出失败项接续时不再领取已用过的协议恢复资格。
- 三个新验证叶子：字典失败、电子书失败、订阅阅读通过。失败隔离后队列自动继续；原始坏JSON和provider.invalid-output保留。
- 订阅阅读经历一次协议恢复、一次集中内容修订、新独立会话复审，合计6次CLI。修订后完整复审pass，8步均completed，真实重放0调用、0新增案例版本。
- 新制品 `tpl_a33b05ab19b948c490ed351cb4f7c112`，标准开发包SHA256 `799de98161dc16fbd29e9849f9f33b2192378fef3e1364df5a1439940d3fbc8a`。固定案例miniflux/v2 r3，commit `bdd8087d9cf7a20ca7e800948389e8a7e86445da`，研究与模板共用同一案例身份；r1/r2保留。
- 工厂页旧辅助目录缓存已修复：随视图、焦点和真实制品清单更新，不对不变4秒轮询重复拉目录。浏览器9项通过，关键测试重复3次通过，精确CI全部通过；真实界面已核验模型审阅、应用未运行、标准包和案例回查。
- 123个原文件（含六份应用数据库）、19个原案例版本摘要未改变。新增2个案例身份、5个版本；订阅阅读修订复用既有身份，重放不新增版本。原18份可用模板、六份示例及数据、冻结包和严格历史保留。

新模板均为“静态审阅通过、应用未运行”，本轮新增应用运行0。三个新样本只有1个可用，不能声称统计质量稳定；门禁通过证明完整成功路径与有限恢复/隔离机制，不代表所有叶子都会通过。订阅阅读的两项非阻断文档瑕疵和验收限制见FEED_KNOWN_LIMITS；不改冻结字节、不过度解读运行证据。独立接受研究回执中的template_passed=false表达该研究登记本身不授予模板验收，最终模板状态由MODEL_PRODUCTION和正式导入/下载记录表达。

## 正式证据和运行入口

[验证报告](../workflow-hardening-2026-10-21/WORKFLOW_VALIDATION.json)、[门禁回执](../workflow-hardening-2026-10-21/FULL_GATE_RECEIPT.json)、[实际启动](../workflow-hardening-2026-10-21/FULL_DISPATCH_STARTED.json)、[本次检查点](../workflow-hardening-2026-10-21/FULL_RESUMED_CHECKPOINT.json)、[新模板下载与案例](../workflow-hardening-2026-10-21/FEED_CATALOG_AND_DOWNLOAD.json)、[保护核验](../workflow-hardening-2026-10-21/VALIDATION_HISTORY_PRESERVED.json)、[操作命令](OPERATIONS.md)。

进度页 `http://127.0.0.1:5188/factory?view=workflow`，新制品 `http://127.0.0.1:5188/factory?view=artifacts&artifact_id=tpl_a33b05ab19b948c490ed351cb4f7c112`。后台每30秒写现场进度，小时跟进仅在重要变化/故障时介入。模型固定opencode-go/minimax-m3.1-flash-free；observed_model、内部请求及费用未获证实时为unknown。旧500、原99和严格G1/T08不扩权，本计划新增上限7200，不叠加旧401，恢复不重置首次启动后的30天窗口。源代码与已结束生产证据分开提交，绑定SHA的资格文件保持原字节。
