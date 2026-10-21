# 家物清单 · 家庭物品盘点

根据正式 Atlas P0 开发包独立实现的单用户本机应用。Python 3 标准库 + SQLite，无安装步骤、无外部请求。一行代表一件物品，支持位置登记、名称/备注搜索、整数分估值、编辑与位置调整、归档恢复。

## 启动

在本目录运行：

```sh
python3 app/serve.py --port 5276 --data-dir ./data
```

打开 http://127.0.0.1:5276 。默认数据目录是本应用的 `data/`；可用 `--data-dir` 指定独立目录。首次试用可加 `--demo`，只对尚未初始化的数据库填入演示数据；已有库重启不会追加演示数据。

只监听 127.0.0.1。原有书签、预算、会议应用及数据库不参与此应用。物品和位置存放在所选目录的 `inventory.sqlite3`，停止进程后使用同一目录启动即可继续盘点。

## 操作

左侧创建位置；右侧逐件录入物品并显式保存。顶部按位置、名称或备注以及活跃/归档状态筛选，数量和总估值仅统计当前列表。点击“编辑 / 调整位置”修改记录；归档物品可以在“已归档”视图恢复。备注按纯文本展示。

金额使用元字符串输入、整数分储存，范围 0–999999999.99，拒绝负数、NaN、指数和三位小数。无效提交零写入，页面保留输入原稿。多页编辑使用 revision 保护：旧版本不能覆盖新版本；冲突时保留原稿并提供最新记录入口。

## 验证

在仓库根目录运行：

```sh
python3 -m unittest discover -s examples/home-inventory-trial/tests -v
python3 examples/home-inventory-trial/tests/run_frozen_probe.py --output examples/home-inventory-trial/tests/results/frozen-http.json
```

回归覆盖非法写入、并发编辑、demo 初始化、HTML 转义，以及无效和冲突表单原稿。冻结探针直接读取正式 ZIP 中原始字节并核对 SHA，不改断言。A01–A03 各跑完整真实 HTTP 旅程；A04 启动、停止、同目录重启自有临时进程，并比较完整状态。测试仅使用临时目录，结束时清理进程。

源码包独立运行；在仓库外运行冻结探针时，提供 `--package /path/to/atlas-development-package.zip`。最近结果见 `tests/results/frozen-http.json` 和 `tests/results/regression.json`。HTTP 验证不代表浏览器旅程，浏览器证据由主开发上下文单独记录。

## 来源与边界

正式来源、模板摘要及辅助消费说明见 `SOURCE.json`；六份开发合同在应用创建前实际读取，SHA 和时间记录于 `CONSUMPTION.json`。沿用 D01/D02 的 assisted defaults，不宣称用户另行确认或严格 G1。未实现照片/附件、层级位置、导出或多人协作。估值仅为用户估计金额。

`source-package.zip` 按 `delivery.json` 精确列出源文件，不包含数据库、缓存、凭据或运行日志。未调用 OpenCode、额外模型或改动冻结模板。
