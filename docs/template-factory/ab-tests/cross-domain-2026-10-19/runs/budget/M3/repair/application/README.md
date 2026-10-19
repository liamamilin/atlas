# 个人月度预算与消费前剩余额度（P0）

单机本地应用：按月为用途设置预算，记录与纠正实际支出，在消费前看到准确的
计划 / 已花 / 剩余（含超支负剩余），切换月份、重启后仍可回查，并导出当月 CSV。
不连接银行或支付服务，无账户、无同步、无多租户。

## 启动

```bash
python3 app.py --port 8000 --data-dir /绝对路径/到/数据目录
```

- 仅使用 Python 3 标准库（在 CPython 3.10 上开发），无安装、无构建、无第三方依赖。
- 只绑定 `127.0.0.1`；`--data-dir` 为必填，所有持久化数据只写入该目录。
- 打开 `http://127.0.0.1:8000/` 即为中文界面，与 JSON API 共用同一真实状态。
- `--data-dir` 不存在时会自动创建（仅在指定目录内创建）。

## 存储

- 单个 SQLite 库：`<data-dir>/budget.sqlite3`，首次启动自动建表。
- 金额一律以整数“分”存储（`budget_cents` / `amount_cents`），响应渲染为两位小数字符串。
- 每次写入都在事务中提交；同一 `--data-dir` 重启后数据保留。
- 分类以 `(month, name)` 唯一；交易通过 `category_id` 关联分类，日期必须属于该分类所在月份。
- 应用目录只读运行，不会在其中写入任何数据文件。

## 当前范围（已实现）

- 选择月份并按月隔离分类、预算与支出。
- 建立分类与月预算；分类在当月内唯一。
- 调整分类月预算，仅作用于目标月份。
- 记录支出（日期 / 分类 / 正数金额 / 备注）。
- 查看分类与整月的计划、已花、剩余；未使用分类仍可见；超支显示负剩余且不阻止后续记账。
- 修改 / 删除支出后，列表与汇总即时一致地重算。
- 非法输入返回非 2xx JSON 错误且不破坏既有数据；UI 给出可理解反馈。
- 导出当月 CSV（UTF-8，RFC 4180 引号规则，CRLF，表头 `date,category,amount,note`）。

## JSON API

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/state?month=YYYY-MM` | `{month,categories,transactions,totals}`，金额均为两位小数字符串 |
| POST | `/api/categories` | `{month,name,budget}` → `{id}`；同月同名被拒绝 |
| PUT | `/api/categories/{id}` | `{budget}` → 更新后的条目；不改动其他月份 |
| POST | `/api/transactions` | `{date,category_id,amount,note}` → `{id}`；日期须属分类月份 |
| PUT | `/api/transactions/{id}` | 更新支出的四个字段 |
| DELETE | `/api/transactions/{id}` | 删除该支出；不存在时返回错误且不改变数据 |
| GET | `/api/export?month=YYYY-MM` | UTF-8 CSV 下载 |

校验失败一律返回非 2xx 且 JSON `{"error":"..."}`。

## UI 测试钩子（data-testid）

`month`、`category-name`、`category-budget`、`category-save`、`expense-date`、
`expense-category`、`expense-amount`、`expense-note`、`expense-save`。
分类下拉项 `value` 等于 `category_id`，选项随当前月状态加载。

## 明确限制

- 仅单个本地用户；无银行 / 支付连接，无认证、无多用户、无同步。
- 货币固定人民币（元，两位小数）；不支持多币种或自定义符号。
- P0 只展示当月计划 / 实际 / 剩余，不做跨月结余结转。
- P0 不支持删除 / 重命名 / 归档分类（未使用分类保留可见）。
- 不提供完整编辑历史 / 审计日志；当前以导出 CSV 作为最小审计与恢复起点。
- 金额超过两位小数或非正数直接拒绝，不做静默取整或裁剪。
- 本仓库不含任何自动化测试结果：全部自检状态为未运行，由独立操作员在真实实例上执行。

## 后续路线（尚未实现，按需推进）

1. 分类删除 / 归档与重命名（在保持历史一致的前提下）。
2. 跨月结余结转或“可用额度”语义（需用户确认规则）。
3. 完整编辑历史 / 审计日志（依赖 D04 的人类决定）。
4. 预算模板、复制上月预算、常用分类快捷项。
5. 备份轮换与导入 / 恢复（CSV 回灌或数据库快照）。
6. Web 端无障碍与移动端布局细化。
