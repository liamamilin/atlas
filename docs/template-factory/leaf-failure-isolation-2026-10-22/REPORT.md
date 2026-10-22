# 单叶选源失败误停全量：原因与修复

本次停机是宿主故障隔离不完整，不是一个模型会话卡死。现场为计划新增142/7200、历史累计241、活动0，原1805范围不变。`live-video-chat-application`的研究返回`https://github.com/TokTok/c-toxcore`，共享案例保存`https://github.com/toktok/c-toxcore`；commit和六份文件完全相同。原代码严格比较URL字符串，随后把“没有匹配snapshot”错误发为全局`workflow_integrity`；因此整条计划暂停，并连带`dating-community-platform`尚未开始的独审阶段。

前一次小样本验证覆盖成功路径、协议恢复和部分失败隔离，但没有覆盖这类共享案例身份格式差异及其错误分类，是宿主实现及测试缺口。原暂停/失败时间和证据保留，未改成通过。

## 修复边界

- GitHub URL先经过现有公共仓库验证，再仅对owner/repo身份作casefold比较；原`RESEARCH.json`和模型返回不改写。文件路径大小写、完整文件集合、固定commit、内容摘要和案例版本仍严格匹配。
- 只有指定兼容案例、规范仓库和文件集合均匹配才复用固定snapshot，不重新解析HEAD；不存在的reuse ID、错仓库/文件、非法URL/路径、缺许可证选文、过大/非UTF8新源文件，明确记`source_selection_invalid`，该叶`failed/first_pass_done`并继续其他叶子，不在首轮自动追加内容修订。
- 真正404/410来源不可用单列；403/429/5xx/网络共享故障、固定字节或来源绑定损坏、未知宿主、数据库、预算/时间和不确定启动继续沿原全局安全机制处理。没有泛化吞异常、降低独审或把失败标成可用。

## 验证与执行

113项辅助工厂测试、ruff、语法及独立代码复核通过。真实失败研究只读匹配原案例r1和同一commit，原研究/原始返回摘要未变，检查新增模型调用0。队列回归覆盖单叶选源失败后继续后续叶子直至首轮结束，来源损坏负例仍暂停。fixture不是模板独审或应用运行证据。

修复提交`ebfb2816264d9892f2089dedd097b267be91efd1`。正式host revision、精确远端CI和同任务恢复结果单独记录；以`RESUMED.json`及正式status为实际运行依据，不以准备文件或历史start回执替代。

[故障快照](INCIDENT.json)、[原142次账本](CALLS_BEFORE.json)、[真实零调用匹配](REAL_SELECTION_ZERO_CALL_CHECK.json)、[检查](CHECKS.json)、[保护核验](PRESERVATION_BEFORE_FIX.json)。历史123文件含六应用数据、19案例版本未改。全量首轮仍按每批20、并发2、原7200/每叶6及30天截止执行，严格G1/T08与第二轮不启动。

## 真实恢复结果

精确源码`ebfb2816264d9892f2089dedd097b267be91efd1`的CI39732201044已completed/success，check和docker-integration均通过。正式host revision已追加；本次只变更协调者源码，API服务源码未变，健康核验通过，无需重启API或应用。

已通过原正式服务恢复同一full_first_round、同一launchd；`RESUMED.json`记录真实PID52480，计划新增144、历史累计243，活动2。live-video-chat已复用同案例r1、同commit和六份固定源码，未新增discovery，直接进入原author阶段；dating-community继续原独立审阅。新会话均为open-design/deepseek-v4.1-flash，已有process及tool_use/step_finish实际事件。

原142次账本记录逐项未改，原研究、原始返回及失败证据未改。暂停前123个受保护文件和19旧案例版本均未变；本次无应用开发、无内容修复额度增加、无时间重置。未声称当前两项模板已审阅通过；这是恢复运行证明。全量尚在首轮执行，继续交后台逐批接续，普通已知单项失败自动留档继续，首轮结束再汇总第二轮计划。
