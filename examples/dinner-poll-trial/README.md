# 同机聚餐地点投票

本目录是在新开发上下文中，消费 `atlas-development-package.zip` 后独立实现的 P0 应用。Python 3 标准库 HTTP + SQLite，无安装步骤、无第三方资源、无网络依赖。仅监听 `127.0.0.1`。

在仓库根目录启动（请使用专用的新数据目录）：

```sh
python3 examples/dinner-poll-trial/app/serve.py --port 5278 --data-dir /tmp/atlas-dinner-poll-my-trial --demo
```

访问 <http://127.0.0.1:5278/>。`--demo` 仅在数据库文件首次创建时填入虚构问题、地点与两张票；既有数据库不会追加示例。去掉 `--demo` 可从空白开始。同目录重启会恢复原有投票。按 Ctrl+C 停止；数据保存在指定目录的 `dinner-poll.sqlite3`。本实现及测试没有读取或修改任何既有用户数据库。

独立源码包 `source-package.zip` 解压后，进入 `dinner-poll-trial/` 目录运行：

```sh
python3 app/serve.py --port 5278 --data-dir /tmp/atlas-dinner-poll-independent
```

首页可创建问题和 2–8 个固定地点，每行一个。成员使用代号单选；同一投票内代号经首尾去空格及 `casefold()` 后相同，会替换原票。结果显示整数票数、参与人数、暂无投票或并列；不会擅自打破平票。结束投票会禁止新增与改票，重开保留已有结果。界面错误保留输入，所有用户文字经 HTML 转义。

## 数据与 API

问题 1–160 字，地点各 1–80 字，去空格/忽略大小写后不得重复，代号 1–40 字。使用 `polls`、`options`、`votes` 三表；数据库同时约束投票/选项归属及每个代号唯一票。关闭检查、选项检查、写票在同一锁定事务内完成。无永久删除功能。

接口与开发包契约一致：`GET /api/health`、`GET /api/polls`、`GET /api/polls/{id}`；`POST /api/polls` 接收 `{title,options:[文字]}`（201）；`POST /api/votes` 接收 `{poll_id,participant,option_id}`；`POST /api/polls/close` / `reopen` 接收 `{id}`。写入成功返回完整投票，关闭/重开幂等。错误采用 `{error:{code,message}}`：400 `invalid_title` / `invalid_options` / `invalid_participant` / `invalid_option`，404 `not_found`，409 `poll_closed`。计数从票记录派生。

## 消费与验证证据

`CONSUMPTION.json` 记录原始 ZIP SHA256、阅读文件逐项 SHA256 和时间；消费记录先于应用实现。原包原样保存于 `consumed-package/`。D01/D02 的普通可逆默认值已采纳并在消费记录中注明；原包待确认状态保留。未复制上游 Nextcloud 代码或资源。

以下命令均已实际执行：

```sh
python3 -m unittest discover -s examples/dinner-poll-trial/tests -v
python3 examples/dinner-poll-trial/consumed-package/blueprint/acceptance/probe.py --case A01 --app-root examples/dinner-poll-trial
python3 examples/dinner-poll-trial/consumed-package/blueprint/acceptance/probe.py --case A02 --app-root examples/dinner-poll-trial
python3 examples/dinner-poll-trial/consumed-package/blueprint/acceptance/probe.py --case A03 --app-root examples/dinner-poll-trial
python3 examples/dinner-poll-trial/consumed-package/blueprint/acceptance/probe.py --case A04 --app-root examples/dinner-poll-trial
```

10 项补充单测通过；A01–A04 全通过。每个冻结用例使用自己创建的临时数据库与真实 HTTP 进程，并实际停止、重启、比对列表/状态/全部选项票数。冻结程序 SHA256 为 `5a906ce5e0552c4cca5e26826746eb0d8278fb80ce79ccb5924a18e1283dbaff`，未经修改。首次 A01 在沙箱因禁止绑定本机端口中止，后获准在临时 localhost 端口运行，A01–A04 均成功；未把中止当通过。详细命令与输出见 `delivery.json`、`evidence/`。

补充测试覆盖 Unicode 同代号改票、并发同代号唯一票、状态门禁及不变性、跨投票选项、并列、无票、非法创建原子性、示例初始化边界、输入保留及 HTML 转义。浏览器实际操作由主开发上下文另记，不能以服务端渲染测试代替。

## 范围与缺口

这是辅助试产，非严格 G1/T08；没有调用 OpenCode，没有改动模板预算或严格门禁。P0 F01–F04 无已知功能缺口。开发包未提供冻结 `acceptance/runner.json` 绑定，因此此处是直接执行冻结 HTTP 套件的本机证据，没有声称已通过工厂离线 runner。原上游未安装运行、上游证据独立审阅 pending 的状态不变。

同机共享，代号不是身份认证。任何设备使用者均可冒用代号改票，也可结束/重开投票。本应用不提供远程分享、权限隔离、防恶意刷票或正式选举能力。源码 ZIP 不含数据库、凭据、缓存或虚拟环境。

## 本轮浏览器交付

主上下文已完成五组真实浏览器旅程，记录于 `evidence/browser-validation.json`，截图和逐步页面文本同目录保存。刷新与原进程停止、同数据目录重启均保留完整状态。仍只统计辅助试用，不改变严格G1/T08。

本轮长期试用数据位于 `examples/dinner-poll-trial/data`。从仓库根目录启动：

```sh
python3 examples/dinner-poll-trial/app/serve.py --port 5278 --data-dir examples/dinner-poll-trial/data
```

最终源码包采用共用 package_app.py 打包，解压后先进入 `dinner-poll-trial/`，再执行 `python3 app/serve.py --port 5278 --data-dir ./data`。不包含试用数据库。
