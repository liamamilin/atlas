# 一周晚餐 · 本机辅助试用

从标准开发包独立实现的 P0 应用。Python 3.10+ 标准库即可运行，无需安装依赖。

在仓库根目录启动：

```sh
python3 examples/meal-plan-trial/app/serve.py --port 5277 --data-dir /private/tmp/atlas-meal-plan-trial --demo
```

浏览器打开 `http://127.0.0.1:5277`。`--data-dir` 是专用数据目录，只创建其中的 `meal-plan.sqlite3`；请勿指向既有应用的数据目录。`--demo` 只为全新数据库生成番茄炒蛋和本周两天计划；已有数据库即使为空也不会重新写入演示数据。去掉 `--demo` 可从空库开始。再次用同一目录启动可继续使用。使用 `Ctrl+C` 停止。

解压源码包后，进入 `meal-plan-trial/` 目录运行：

```sh
python3 app/serve.py --port 5277 --data-dir ./data --demo
```

## 使用

1. 登记菜谱名称、基准人数；食材每行填写 `名称|单位|数量`，例如 `番茄|g|300` 和 `鸡蛋|个|2`。
2. 选择日期、菜谱及用餐人数，点击“保存晚餐”。每日期只有一份晚餐；选择范围外日期会跳至该日期所在周。
3. 修改人数后点“保存人数”，清单立即重算；“暂停计划”保留原计划并排除采购贡献，“恢复计划”重新计入。
4. 可选择 1–7 天的起止范围，或前后移动 7 天；其他日期的计划不会进入当前清单。

人数是 1–20 的整数，食材数量是大于零、最多两位小数的十进制字符串。每顿贡献按菜谱人数换算，使用 ROUND_HALF_UP 四舍五入到百分之一，再按去除首尾空格及 casefold 后的名称和精确单位合并。仅支持 g、ml、个，不自动换算。暂停日期也禁止重复新增。所有表单显式提交；错误保留输入且不写入数据。

## 接口

- `GET /api/health`
- `GET /api/state?start=2026-11-02&end=2026-11-08`：`recipes`、范围内 `plans`（含暂停）、`shopping`
- `GET /api/shopping?start=2026-11-02&end=2026-11-08`：`items` 与有效 `plan_count`
- `POST /api/recipes`：`{name,base_servings,ingredients:[{name,unit,quantity}]}`
- `POST /api/plans`：`{date,recipe_id,servings}`
- `POST /api/plans/update`：`{id,servings}`
- `POST /api/plans/toggle`：`{id}`

POST 接受 JSON；数量 `quantity` 为字符串，人数和 ID 为 JSON 整数。错误返回 `{error:{code,message}}`。`quantity_minor` 是百分之一单位的整数。

## 验证

冻结套件直接复制自开发包，SHA 记录于 `CONSUMPTION.json`；未改写断言。每个用例使用独立临时目录，真实启动、停止并重启进程：

```sh
python3 examples/meal-plan-trial/acceptance/probe.py --case A01 --app-root examples/meal-plan-trial
python3 examples/meal-plan-trial/acceptance/probe.py --case A02 --app-root examples/meal-plan-trial
python3 examples/meal-plan-trial/acceptance/probe.py --case A03 --app-root examples/meal-plan-trial
python3 examples/meal-plan-trial/acceptance/probe.py --case A04 --app-root examples/meal-plan-trial
python3 -m unittest discover -s examples/meal-plan-trial/tests -v
```

A01–A04 均通过，补充 11 项测试均通过（精度、大小写/单位、暂停日期冲突、零写入、范围边界、周隔离、GET 无写入、演示数据保护、真实 HTTP 表单保留输入/转义/跨周跳转、404 错误形状）。实际命令、输出和时间见 `delivery.json`。受限执行环境需允许测试绑定本机随机端口。解压源码包后将 `examples/meal-plan-trial/` 前缀删去，并以 `--app-root .` 运行。

## 已知范围与缺口

仅单用户本机晚餐计划，菜谱保存后不可修改。无账户、云同步、营养建议、附件、食谱抓取、采购下单、单位自动换算、删除或导入导出界面。数量为份数估算，不是真实订单或营养建议。

此子开发上下文完成 HTTP、重启和表单测试；实际浏览器视觉/交互验收由主上下文另行记录。模板包没有 `blueprint/acceptance/runner.json`，这里直接执行冻结 `probe.py`，不冒称工厂离线运行验收已接通。静态来源独立审阅 pending，上游应用未运行；本次仅辅助试用，不代表严格 G1/T08 通过，也未调用 OpenCode 或改动预算。未读取任何既有用户数据库。

## 本轮浏览器交付

主上下文已完成五组真实浏览器旅程，记录于 `evidence/browser-validation.json`，截图和逐步页面文本同目录保存。刷新与原进程停止、同数据目录重启均保留完整状态。仍只统计辅助试用，不改变严格G1/T08。

本轮长期试用数据位于 `examples/meal-plan-trial/data`。从仓库根目录启动：

```sh
python3 examples/meal-plan-trial/app/serve.py --port 5277 --data-dir examples/meal-plan-trial/data
```

最终源码包采用共用 package_app.py 打包，解压后先进入 `meal-plan-trial/`，再执行 `python3 app/serve.py --port 5277 --data-dir ./data`。不包含试用数据库。
