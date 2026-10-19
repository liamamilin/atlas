# 认知模板工厂改造

日期：2026-10-19。范围：用户确认的“完整认知库＋当前阶段执行包＋独立验收”，以及跨品类对照发现的交付协议、stdin 和执行可靠性问题。本轮实现、独立审查与检查已完成；实际结果在文末。旧 A/B、原失败及未运行的书签验收不作追改。

## 交付结构

同一冻结规范派生三个视图，不另外生成一套相互独立的答案。

| 视图 | 入口 | 职责 |
| --- | --- | --- |
| 完整认知库 | `KNOWLEDGE.md` → `blueprint/` | 保留全部品类、产品、架构、路线图、决策、程序和来源；原包字节不变 |
| 当前阶段执行包 | `HANDOFF.md`、`CURRENT_PHASE.json`、`PROJECT_DECISIONS.json` | 当前阶段及必要前期能力、正负向目标、完整场景、限制与决策触发条件；已有阶段需核实，默认建议不等于人工确认 |
| 独立验收 | `ACCEPTANCE_CONTRACT.json` | 当前与前期用例清单、实现文件哈希、冻结套件摘要；导出状态始终为未运行 |

`HANDOFF_MANIFEST.json` 固定交接入口和原包文件摘要。`APP_DELIVERY.md` 告诉下游 agent 如何交回源码和运行元数据，不把应用源码混入认知模板。开发包不自动实现应用、安装依赖或执行测试。

## 开发与检查顺序

- [x] 冻结原始证据，确定兼容边界；完整知识与阶段视图来自同一版本。
- [x] 实现三部分导出、默认决策状态、入口摘要以及双语页面。
- [x] 修复 CLI stdin 继承、失败摘要、退出/协议证据分离及整个进程组清理。
- [x] 实现严格应用交付清单、有限路径归一化、不可变输入与独立运行任务。
- [x] 新生产生成逐例调用/结果协议，修订保留协议；旧包缺适配器明确不可用。
- [x] 检查完整队列、API 和页面，真实容器验证启动/正负向/异常/超时/清理，独立审查并修复。
- [x] 完成回归、文档和结果记录；不自动发布、晋级或把合成目标验证替换为历史应用验收。

## 运行协议

新页面的认知生产请求包含 `acceptance_protocol: "atlas.acceptance-runner.v1"`。旧 API 请求可不带该字段，保留原行为。运行能力取决于冻结包是否包含合法的 `acceptance/runner.json`，不靠文件名猜命令。

```json
{
  "schema": "atlas.acceptance-runner.v1",
  "result_schema": "atlas.acceptance-result.v1",
  "cases": {
    "A01": {"args": ["--case", "{case_id}", "--base-url", "{base_url}"]}
  }
}
```

必须覆盖规范全部验收 ID，执行程序由规范的 `implementation` 字段确定。支持 Python、Node 程序；参数只能是字面值和独立的 `{case_id}`、`{base_url}`、`{app_root}`、`{data_dir}`。禁止自选宿主命令。选择阶段时执行该阶段及前期回归，不能只跑启动就宣称阶段通过。

每次调用 stdout 只输出一个结果 JSON，stderr 可输出诊断：

```json
{
  "schema": "atlas.acceptance-result.v1",
  "case_id": "A01",
  "status": "passed",
  "assertions": [{"id": "saved-value", "passed": true, "detail": "实际动作和观察"}]
}
```

需要非空、实际行为断言。通过还需进程退出零；合法失败结果配合非零退出记录为失败，不混成协议不可用。结果 stdout 限 64000 字符，超限明确未核实；展示可截短，但不能从截断尾部解析通过。每次调用 stdout/stderr 总量上限 8 MB，退出后同样检查。缺少、重复或错误结构不能变成通过。结构符合协议仍不证明语义正确；独立静态审阅要检查真实交互、负向断言和目标适配，运行验收再连接实际应用。

## 应用提交与隔离

在制品“独立运行验收”选择阶段，上传源码 ZIP，确认本地隔离执行后提交。API 为现有制品 accept 入口，`method: "blueprint-runtime"`，同时带 `expected_digest`、`phase`、`source_archive_base64`、`execution_confirmed: true` 和超时。

ZIP 根目录需有 `delivery.json`：

```json
{
  "schema": "atlas.application-delivery.v1",
  "root": ".",
  "files": ["app.py"],
  "runtime": {
    "profile": "python-web",
    "install": [],
    "build": [],
    "start": ["python3", "app.py", "--port", "8080", "--data-dir", "/state"],
    "port": 8080,
    "readiness_path": "/"
  }
}
```

示例命令需要应用实际实现对应参数。其他支持 `node-web`、`static-web`，以及 Python `cli` 的 `smoke` 命令；CLI 不填 web start/port。源文件可统一置于 `app/` 并设 root 为 app，files 相对该代码根。清单必须与实际文件逐项一致，允许一次无歧义的 app 前缀归一化并记录，不反复剥前缀、猜根目录或改源码。ZIP 压缩上限 1 MiB、展开上限 8 MiB。

任务固定模板摘要、阶段、源码原始 ZIP、展开文件哈希、交付收据和输入摘要。运行前复核版本与完整性；同一制品不重复排入活跃运行任务。运行占独立验证队列，不调用模型。

应用及冻结用例在 Docker 中运行，使用固定支持的 Python/Node 镜像并记录解析后的镜像 ID；缺镜像时准备镜像可能联网，应用/测试执行网络关闭。应用使用一次性副本；原始提交保持不变。测试源码只读挂载、无宿主凭据、Docker socket 或宿主命令执行。测试容器与应用仅共享本次网络空间，必要语言用单独镜像，不能假设 Node 镜像自带 Python。可写数据置于容器 `/state`。

先运行安装/构建及真实启动就绪检查，再逐项执行冻结用例。离线依赖无法满足、浏览器等环境未支持时如实不可用，不临时开放外网或伪造 UI 结果。startup/stdout/stderr、用例与断言、版本、镜像、原始源码是否改变和清理结果分别保存。环境错误保留部分证据并新增未完成记录，不能让历史通过掩盖本次失败。取消或所有权丢失不生成通过记录。

CLI 输入固定为 DEVNULL，避免继承控制脚本；CLI 完成、JSON 交付合法、应用启动、阶段行为验收是不同状态。失败摘要尽量保留原错误，清理失败不能返回成功；TERM 无法终止的整个自有进程组会升级清理。

## 验证与限制

首轮 150 项工厂相关后端检查通过；最终全后端检查 434 项，其中 426 通过、8 项容器检查按设计默认跳过。需要显式启用的 8 项已另行真实执行：独立执行器 7/7、完整提交队列链路 1/1。以下不同证据不能混为应用质量结论。

| 检查 | 实际结果与范围 |
| --- | --- |
| `PYTHONPATH=application-atlas-production-pack python3 -m unittest discover -s application-atlas-production-pack/tests -p 'test_*.py'` | 434 项、38.565 秒，426 通过 / 8 默认跳过；含新协议生成、修订继承、旧包兼容、固定输入、重复提交、环境失败记录、进程组和输出传输 |
| `ATLAS_RUN_DOCKER_INTEGRATION=1 python -m unittest tests.test_blueprint_runtime_docker -v`（在 production-pack 下） | 7/7，50.352 秒；独立实现者运行，覆盖 Python/Node Web、真实 CLI 正负向、启动退出 traceback、非零失败结果、超时及自有容器清理，详见[记录](runtime-validation.md) |
| `ATLAS_RUN_DOCKER_INTEGRATION=1 PYTHONPATH=application-atlas-production-pack python3 -m unittest application-atlas-production-pack.tests.test_blueprint_runtime_jobs.RuntimeJobTests.test_real_docker_through_api_queue_and_pinned_frozen_source -v` | 1/1，4.182 秒；合成源码 ZIP 经 API 校验、队列、冻结测试、真实 HTTP 正负向与验收落库；摘要绑定、源码不变、不晋级 |
| 工厂 Playwright：`npx playwright test --config playwright.factory.config.ts` | 20 个用例最终均有通过记录。全量回归发现旧包范围提醒丢失，已恢复；最后一次全量 18/20，剩余 2 项展示文案断言修正后定向 2/2 通过。包括本地 API 的导入/阅读/导出与 mock 运行结果显示；页面检查不调用模型或实际容器 |
| 前端及静态检查 | `npm test` 9/9；`npm run typecheck`、`npm run build`、工厂 Python compileall、`git diff --check` 通过 |

Sol 独立 reviewer 最终只读复查无剩余阻断；其结论仅为源码/契约审查，不冒充 Docker 或用户产品实测。审查发现并修复：stderr 混入结果、非零失败误分类、部分容器创建漏清理、环境失败缺验收记录、活跃任务缺 UI 状态、修订丢适配协议、成功/失败后遗留抗 TERM 子进程、截断 stdout 伪通过、交付示例与显示字段不一致。真实子进程检查覆盖超过输出上限的快速进程，不能只依赖轮询时发现超限。

合成测试证明本轮基础设施与协议路径可用，不证明任何生成程序的语义自动正确；真实品类应用、第三方依赖、浏览器验收环境、镜像拉取及网络出口探测不在这些容器检查的证明范围。单个程序可伪造断言，因此仍需独立认知/程序审阅及必要负向目标，不能只凭 JSON 状态认证产品。

本轮不新跑付费模型生产，不改全局 provider/model，继续兼容 OpenCode CLI 的配置。没有认知模板自动发布或 L1 晋级。旧书签 A01–A33 与新书签 17 项整套程序仍是独立待验收事项；新运行器不会把它们自动改为已通过。
