# 同任务追加独审与外部阻塞时间恢复

授权来源：USER_AUTHORIZATION.txt（增加一次调用）及 TIMING_OVERRIDE_AUTHORIZATION.txt（明确忽略旧时间限制并恢复）；旧授权、停止记录、截止和全部失败原样保留。原始追加授权并不隐含无限重试或业务修复。

## 工作与验收对照

| 工作包 | 验收 | 证据 |
| --- | --- | --- |
| W01 授权隔离 | 两份用户原文SHA固定；原grant保持已消费 | 原文、prepare/proposal |
| W02 追加迁移 | 同job允许第二份明确授权；旧row/index/回执保留；旧key只回放 | 版本迁移回归、正式schema回执 |
| W03 时间恢复 | 原quota暂停点到旧截止剩余4632.611294秒；第一次恢复入队原子激活；不滚动延长 | time_resume行、重复请求回归 |
| W04 调用门禁 | 只允许原job attempt3一次goFlash；payload/source/prompt/九文件固定；1800秒上限；原额度不增 | 负向fixture、累计计账、CLI原始事件 |
| W05 合法交付 | 八维结果、原始响应/result/report与当前reservation/attempt严格绑定；旧结果不能顶替 | 交付回归、独立代码审阅 |
| W06 源码门禁 | 新源码必要完整检查、精确提交check/docker-integration通过 | verification、CI原文 |
| W07 正式执行 | prepare/register/recover/resume原任务；真实状态查询；最多一次新增调用 | operations请求/回执、实际CLI目录 |
| W08 后续主线 | 仅有效passed后发布→标准交接真实消费→P0→独立运行→宿主G1→原T08；否则正式暂停 | 最终交付/停止记录 |

## 时间与预算边界

只为这次外部quota中断接续剩余有效时间，不增加新的八小时窗口。暂停时间锚定真实unavailable acceptance（2026-10-20T10:04:40.244128+00:00）；原截止1792495312.855422保存不改。正式入队时固定effective_deadline=activated_at+4632.611294；重复恢复/新实例不能重置它。新时间行只影响原product/plan的G1；其他产品/阶段无延期。旧45分钟启动余量只对这份已激活授权豁免；单次1800秒和新有效截止继续强制执行。

工厂原81条调用记录保留；独立诊断1次单列，并保守计入500总上限，新独审成功启动后工厂82、独立诊断1、合计83。书签业务修复7/7；无第八轮、无模板author、无第二次新增冻结独审、无自动reference-repair。

本文件为工作定义，不代表检查或G1已通过。
