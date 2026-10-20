# 实际停止与恢复边界

原计划已正式 pause；R6 后继 failed/attempt1，停止于 aggregate-semantic-review。不要直接 retry/resume 换一次语义结论，不要把 receipt replay 当作新生产资格。

先阅读 actual-aggregate-review.json、actual-six-new-review-proof.json、actual-nine-program-byte-proof.json 和 STOP_RECORD.json。六项新设计预审通过，但聚合审阅明确阻断 A02 JSON 单标签正向断言及 A07 搜索排除断言。独立静态核查确认它们是验收程序覆盖缺口；尚未生成目标应用，不是应用运行失败。

这两项必须修改本轮已固定的程序字节，超出 R6 来源/解释修订范围。书签修复6/6，不允许创建第七轮、不重置 campaign/job/repair/grant、不替换固定T08样本。需先取得明确的新业务修订范围及相应正式容量，再根据已有失败候选/程序检查点准备受限差分；本轮不创建该请求、不擅自提高额度。

宿主的生成 plan.json 元数据审阅材料修复只影响今后的证据组织，不清除原 blocked 报告，也不修复 A02/A07。本轮原始聚合输入、报告、候选和全部调用保持原样。所有新状态仍须通过正式服务/API/队列，不能改库。

旧截止 2026-10-20 03:13:43.754534+08:00 保留；本轮窗口 11:21:52.855422 至 19:21:52.855422+08:00 已一次激活。暂停/重放/重启不延长。额度与窗口的后续变更均需新明确授权。

后续仍按新规格审阅→新冻结→冻结后独立审阅→发布→标准交接真实消费→P0→冻结套件/独立浏览器→精确phase proof→宿主G1评估的顺序。仅G1正式passed才继续原T08三场景；所有未运行项见STOP_RECORD。
