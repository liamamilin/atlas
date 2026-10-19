# 阶段与验收

## P0 · 单机本地月度预算核心旅程

使用者能在本地浏览器中选月、建立分类与预算、记录并纠正支出、核对计划/实际/剩余（含超支负剩余）、切换月份后重启仍可回查，并导出当月 CSV。

| 用例 | 类型 | 行为 | 执行器 |
| --- | --- | --- | --- |
| A01 | positive | 启动后 GET / 返回可用中文 UI；将 data-testid=month 设为某月后，JSON API 返回与该月一致的实时状态。 | acceptance/run.py |
| A02 | positive | 通过 UI 控件（category-name/category-budget/category-save）与 POST /api/categories 建立分类与预算，GET /api/state 返回该分类且 spent 为 "0.00"。 | acceptance/run.py |
| A03 | negative | 同一月份重复名称创建分类返回非 2xx JSON 错误，且不产生隐藏的第二个分类。 | acceptance/run.py |
| A04 | positive | 记录含日期、分类、金额与备注的支出后，GET /api/state 列表包含该笔且汇总与之一致。 | acceptance/run.py |
| A05 | negative | 非正数或超过两位小数的金额被拒绝（非 2xx JSON），存储值与汇总保持原样，不静默取整或裁剪。 | acceptance/run.py |
| A06 | negative | 交易日期与分类所属月份不一致时被拒绝，且既有数据不变。 | acceptance/run.py |
| A07 | positive | 分类与整月的 budget/spent/remaining/totals 计算正确；未使用分类仍出现；超支显示负 remaining 且不阻止后续记账。 | acceptance/run.py |
| A08 | positive | 修改或删除支出后，交易列表与汇总即时一致地重算。 | acceptance/run.py |
| A09 | negative | 对不存在或非法 id 的 PUT/DELETE 返回非 2xx，原记录保持不变。 | acceptance/run.py |
| A10 | positive | 不同月份数据互相隔离；以同一 --data-dir 重启后数据保留，且数据仅写入指定目录。 | acceptance/run.py |
| A11 | positive | GET /api/export?month 返回 UTF-8 CSV，含表头与当月行；中文、字段内引号与换行按 RFC 4180 往返可解析。 | acceptance/run.py |
| A12 | positive | PUT /api/categories/{id} 更新目标月预算，且不误改其他月份的同名分类。 | acceptance/run.py |
| A13 | positive | UI 控件反映与 JSON API 相同的真实状态（例如新增支出后界面汇总数字随之更新）。 | acceptance/run.py |
| A14 | negative | API 校验失败返回非 2xx JSON 错误说明；UI 对失败给出可理解反馈且不破坏旧数据。 | acceptance/run.py |
