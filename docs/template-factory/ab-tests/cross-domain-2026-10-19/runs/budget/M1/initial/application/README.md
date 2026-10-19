# 个人月度预算（本地应用）

单用户、纯本地的月度预算工具：按月建立用途分类与预算，记录、纠正支出，随时看到
计划 / 已花 / 剩余，并导出当月 CSV。不连接银行或支付服务，无网络、无遥测、无第三方依赖。

## 运行要求

- CPython 3.10（仅使用标准库：`http.server`、`sqlite3`、`csv`、`json`、`argparse`）。
- 无需安装、构建或联网。

## 启动

```
python3 app.py --port 8000 --data-dir ./data
```

- `--port`：监听端口（默认 8000）。服务只绑定 `127.0.0.1`，不对外网开放。
- `--data-dir`：所有持久化数据的目录（默认 `app/data`）；不存在时自动创建。
- 启动后浏览 `http://127.0.0.1:8000/`。
- `Ctrl+C` 停止。

## 存储

- 数据库文件：`<data-dir>/budget.sqlite3`（SQLite，WAL 关闭时默认日志模式）。
- 表：`categories(id, month, name, budget_cents)`，`UNIQUE(month, name)`；
  `transactions(id, date, category_id, amount_cents, note)`，外键指向分类。
- 金额以整数「分」存储，避免浮点误差；仅在 API/UI 边界格式化为两位小数字符串。
- 数据只写入该目录，正常重启后仍在，可回查历史月份。

## JSON API

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/api/state?month=YYYY-MM` | 返回 `{month,categories,transactions,totals}`，金额均为两位小数字符串 |
| POST | `/api/categories` | `{month,name,budget}` → `{id}`；同月同名返回 409 |
| PUT | `/api/categories/{id}` | `{budget}` → 更新后的分类条目 |
| POST | `/api/transactions` | `{date,category_id,amount,note}` → `{id}`；日期须属于分类月份 |
| PUT | `/api/transactions/{id}` | `{date,category_id,amount,note}` → 更新后的记录 |
| DELETE | `/api/transactions/{id}` | 删除记录，失败不改动原数据 |
| GET | `/api/export?month=YYYY-MM` | UTF-8 CSV，表头 `date,category,amount,note` |

校验失败返回非 2xx 且响应体为 JSON：`{"error":"<说明>"}`。

## 当前范围（已实现）

- 选择月份；该月分类与支出与其它月份完全隔离。
- 建立分类及预算；同月重名被拒绝；未使用分类仍显示（已花 0）。
- 记录支出（日期、分类、金额、备注）；金额须为正数、最多两位小数，不静默取整或裁剪。
- 分类汇总显示计划 / 已花 / 剩余，超支显示负剩余且不阻止继续记账。
- 修改分类预算、修改或删除支出，汇总与列表立即重算且保持一致。
- 重启后数据保留；导出当前月份 CSV，中文、逗号、引号、换行均按标准 CSV 引用往返。
- 浏览器 UI 提供明确的成功 / 失败反馈。

## 已知限制

- 单用户、单进程；无登录、无并发写入控制（SQLite 串行写入足够本地使用）。
- 分类不能改名或删除；月份不能整体复制到下一月。
- 导出为纯 UTF-8（无 BOM），面向标准 CSV 读取；不针对 Excel 公式做特殊处理。
- 备注长度与 UI 呈现未做上限约束（数据库层面无硬限制）。
- 日期不做时区/跨月提醒，仅做格式与「属于该分类月份」校验。

## 后续路线（候选，未实现）

1. 分类改名 / 删除（含其支出处理策略）。
2. 上月预算一键复制或滚动结转。
3. 本月收支对比与趋势视图。
4. 可选 CSV 导入与备份/还原。
5. 键盘快捷键与更完整的无障碍标注。
