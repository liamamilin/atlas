# 阶段与验收

## P0 · 核心可用

为聚餐问题预设地点选项，成员用代号单选并可改票，查看汇总，在结束后冻结投票，必要时重开。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A01 | positive | 创建2个不同投票，选择只属于当前投票；重复/空选项不能创建。 | acceptance/probe.py |
| A02 | positive | 小林选A、小周选B得到1/1总2；小林改B得到0/2，总数不增加。 | acceptance/probe.py |
| A03 | positive | 关闭后投票409poll_closed且汇总不变；重开允许小李选A变1/2总3；空代号与跨投票选项拒绝。 | acceptance/probe.py |
| A04 | positive | 相同数据目录重启后列表、状态、全部选项计数与代号票保留。 | acceptance/probe.py |
