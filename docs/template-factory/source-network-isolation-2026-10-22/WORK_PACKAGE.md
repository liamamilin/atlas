# 首轮来源网络隔离与有限续作

实际metasearch-engine在固定commit源码下载出现URLError，宿主误发full_provider_unavailable，暂停全量并连带vertical-search独审。164原CLI、旧provider退避和失败记录保留。本轮只修宿主source/model/API故障域，不改模板内容、案例版本、prompt/profile、每叶6/7200/并发2/原30天/G1历史。

使用现有公共源码GET，在每叶工作目录持久化URL/limit绑定、已启动尝试、有限退避和结果摘要。每请求最多3次、2/8秒退避，重启不清计数；真实请求成功与缓存重放区分。SOURCE_PIN与已下载源hash仍严格。共享pin函数默认行为兼容，仅新增可注入fetch。

一次来源网络问题不全局暂停：耗尽后该叶paused/first_pass_done/deferred_reason，保留检查点，继续下一项并在首轮报告单列；不是产品失败或成功。原事件表记录source_health，连续3不同叶耗尽且中间无真实源网络成功才暂停全局。源码明确认证/限流也可全局暂停，但不消耗模型provider恢复资格。已耗尽叶不因进程重启无限回队列；未知启动、输入/来源真实性损坏、数据库/预算和真实持续公共故障的边界保留。

验证覆盖临时失败后成功、耗尽后下一叶、重启/并发journal、真实网络成功才重置source健康、3不同叶才全局停、API故障不冒充模型provider、历史额度/退避不变与原源码hash负例。必要精确提交CI通过后正式host激活并恢复同一首轮/launchd，不能仅交付代码准备。
