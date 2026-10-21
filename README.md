# Application Atlas

软件应用类型资料库及本地工作台。当前正式语料包含 1,805 个类型、29 个大域、270 个目录节点及 33 个产品实例。

- `application-atlas-production-pack/applications/`：正式英文档案，内容真相源。
- `application-atlas-production-pack/research/`：对应的研究笔记及边界依据。
- `application-atlas-production-pack/DIRECTORY.md`：分类目录。
- `application-atlas-production-pack/atlas/*.jsonl`：持久化翻译记录，纳入版本管理。
- `atlas-web/`：React + TypeScript + Vite 前端。
- `application-atlas-production-pack/drafts_api.py`：本地草稿 API（127.0.0.1:5199）。

## 模板工厂

可先试用 [留存 · 个人收藏夹](examples/bookmark-trial/README.md)：在仓库根目录运行 `python3 examples/bookmark-trial/app/serve.py --port 5273 --demo`，打开 http://127.0.0.1:5273/ 。这是从 R8 准备模板导出标准开发包后，由 Codex 直接实现的辅助试用应用；不代表严格 G1/T08 通过。来源包与七条真实浏览器旅程见 [试用报告](docs/template-factory/bookmark-assisted-trial-2026-10-20/TRIAL_REPORT.md)。

另有 [月有度 · 个人预算](examples/budget-trial/README.md)（5274）和 [会后有据 · 会议笔记](examples/meetings-trial/README.md)（5275）。均先固定共享案例、导出本场景模板与标准开发包，再由 Codex 实现并验证浏览器旅程；独立源码包不带试用数据库。[三场景对照与来源包](docs/template-factory/assisted-trials-2026-10-21/COMPARISON.md)记录实际结果、人工步骤与已知缺口。

[可重复辅助小批次](docs/template-factory/assisted-batch-2026-10-21/REPORT.md)将上述三份模板接入工厂，并新增家庭库存、专注计时、出行英语模板。工厂「模板制品」支持按名称查找、阅读、回查固定共享案例与导出标准开发包；辅助来源明确标注，不代表严格发布。代表应用 [家物清单](examples/home-inventory-trial/README.md) 使用5276，另两份新模板未运行应用。

[十模板辅助生产批次](docs/template-factory/assisted-batch-10-2026-10-21/REPORT.md)新增晚餐计划、聚餐投票、阅读、旅行、工时、训练、大纲、时间块、流程图和文件整理模板，均可在制品页查找及导出。代表应用 [一周晚餐](examples/meal-plan-trial/README.md)（5277）和 [聚餐投票](examples/dinner-poll-trial/README.md)（5278）已完成真实浏览器核心旅程及同目录重启；其余八份应用未运行。原有数据和严格 G1/T08 状态保留。

[Atlas 辅助模板工厂 V1 用户入口](docs/template-factory/assisted-v1-user-entry-2026-10-21/REPORT.md)已按 Codex 辅助生产范围收口：16份模板可沿「叶子 → 场景 → 模板」或「应用实证 → 固定案例 → 模板」找到。六份有历史核心运行示例，十份应用未运行；均可下载标准开发包，有示例者还可阅读说明、下载源码和回查证据。模板内提供可复制的 Codex 开始说明。辅助记录不等于严格验收或服务当前在线，正式发布区保留原门禁。

叶子类型与应用场景构成生产目录；OpenCode CLI 批量生产冻结候选，Harness 审阅及运行验收独立排队，已发布模板可确定性创建应用包。

- [模板工厂 V1 本轮交付与未通过项](docs/template-factory/v1-2026-10-19/DELIVERY.md)：代码门禁与真实 G1 分开；书签真实生产触及业务修复上限，G1 未通过、首批未启动。
- [开发计划与范围](docs/TEMPLATE_FACTORY_PLAN.md)
- [使用说明](docs/TEMPLATE_FACTORY_GUIDE.md)
- [验证记录](docs/TEMPLATE_FACTORY_VALIDATION.md)

## U17 设计与开发规划

U17 面向新想法和已有项目改进：搜索与阅读类型、应用资料，形成关联的开发文档，通过现有 agent 引擎执行并支持后续迭代。

长期架构：Atlas 独立管理项目知识、编排与验收状态，OpenCode 作为首个可替换的执行后端；允许长期复用，后续依据实际限制和收益决定自研范围。

- [产品设计](docs/U17_DESIGN.md)：用户流程、资料与文档体系、项目版本、agent 编排边界和验收场景。
- [开发规划](docs/U17_DEVELOPMENT_PLAN.md)：M0–M5 的验证任务、实现顺序和完成条件。
- [M5 完整试点计划](docs/U17_M5_PILOT_PLAN.md)：三个真实案例的执行顺序、普通生成对照、证据结构、缺陷分级和完成门槛。
- [剩余产品收口与发布打磨计划](docs/U17_REMAINING_PRODUCT_PLAN.md)：T025-T032 的开发顺序、外部条件、验证矩阵和发布边界。
- [核心主线验证](docs/U17_CORE_PATH_VALIDATION.md)：类型入口、真实工作区、基线、迭代前置条件和当前迭代状态的收口记录。
- [双场景样例](docs/u17-samples/)：新想法与已有项目改进的关联文档包。
- [文档索引](docs/README.md)：当前工作文档、试点材料与历史验证记录的统一入口。
- [发布候选说明](docs/U17_RELEASE_NOTES.md)：当前候选版本的范围、启动方式、验证结果与限制。
- [M0–M4 历史验证档案](docs/archive/u17/README.md)：已完成里程碑的实现与验证证据。
- [下游应用路线图](USAGE_ROADMAP.md)：U17 与其他功能的关系及历史记录。

截至 2026-09-22，U17 的 M0–M4、核心主线最小真实开发冒烟、M5 三个产品使用案例以及本轮产品化收口均已完成当前范围内的验证，形成发布候选。用户可从首页案例入口、搜索或类型叶子进入项目：类型叶子会自动固定完整类型正文并进入项目工作区，也可以把类型加入当前项目。项目路径明确包含工作区基线，活动迭代必须固定当前文档、已确认本版需求和已接受基线；已完成迭代不会被历史建议显示为当前阻塞。项目工作台支持带明确确认和活动任务保护的删除，并始终保留本地工作区和源码。网页可选择核心四件套、完整六件套或自定义文档集合；Atlas 要求目标完整、统一排序，并在逐份审阅保存时把下游草案绑定到本轮上游的不可变版本。开发执行继续由 OpenCode 在隔离工作副本中完成，Atlas 独立记录快照、文件/命令证据、需求覆盖、冲突安全写回和产品验收。多类型需求案例已完成 T1–T5 契约与只读分析验收，但尚未接入真实 provider 或模拟适配器；provider 抽象和前端性能优化留在后续路线。

当前剩余产品收口已进入 T025–T032 计划阶段，优先处理 provider 产物路径隔离和浏览器 backup/restore；`PROJECT_ACCEPTED` 仍需外部 provider、CI、签名/公证和安全审查证据。

U17 的本地 API 提供正式资料全文读取，并管理项目、固定资料、需求、决定、文档版本、项目基线、生成运行、迭代、执行任务、验收与导出。`project_generation.py` 负责固定输入分析和文档/改进方案候选；`execution_service.py` 与 `opencode_runtime.py` 负责短期 OpenCode 执行后端；项目、基线、任务、文件证据和验收仍由 Atlas 独立持久化。

## 启动

需要 Python 3.10+、Node.js 22，以及安装了 bge-m3 的 Ollama（向量检索时需要）。Python 依赖版本来自已验证的本地环境。

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd atlas-web
npm ci
npm run gen
npm run dev
```

另一终端在项目根目录启动草稿服务：

```sh
source .venv/bin/activate
python3 application-atlas-production-pack/drafts_api.py
```

打开 http://localhost:5188 。现有 macOS 启动器在 `apps/`，其中路径仍对应此电脑的工作区。

也可以使用轻量终端入口查看同一套项目状态。它默认只读，执行和清理必须显式传参；所有实际操作仍通过本地 API，沿用 Atlas 的 preflight、隔离副本、验证和证据记录：

```sh
python3 application-atlas-production-pack/atlas_cli.py --project <项目 ID>
python3 application-atlas-production-pack/atlas_cli.py --project <项目 ID> --task <任务 ID> --start --transport cli
python3 application-atlas-production-pack/atlas_cli.py --project <项目 ID> --execution <执行 ID> --cleanup
python3 application-atlas-production-pack/atlas_cli.py --project <项目 ID> --lang en
python3 application-atlas-production-pack/atlas_cli.py --interactive
```

终端入口是 M1 的最小纵向切片，不替代网页工作台；它覆盖项目/任务创建与选择、preflight、启动确认、运行摘要与验证步骤查看、活动 HTTP 执行停止、CLI 结果应用、产品验收记录、项目证据包导出和显式清理，失败摘要会给出 `log_access`、`provider_error`、`cli_protocol` 等安全诊断码，交互式接管和多任务并行仍留在后续阶段。

Vite 默认把 `/api` 代理到 `http://localhost:5199`。需要并行运行隔离 API 时，可在启动前设置 `ATLAS_API_TARGET=http://127.0.0.1:<port>`。

## 项目备份与恢复

项目列表中的“备份”会创建项目范围的 ZIP：包含项目 SQLite 状态、generation、证据和 Atlas 导出，不包含用户工作区源码或临时执行副本。也可以使用 CLI：

```sh
python3 application-atlas-production-pack/project_backup.py create <项目 ID>
python3 application-atlas-production-pack/project_backup.py inspect <备份.zip>
python3 application-atlas-production-pack/project_backup.py restore <备份.zip> <新的项目库路径>
```

恢复命令只允许写入不存在的项目库和产物目录，不覆盖当前库；恢复过程会先写 restore journal，进程中断后只报告并保留部分目标，需显式执行 `python3 project_backup.py restore-status <target>` 检查，再使用 `recover-restore <target> --confirm cleanup_partial_restore` 清理，Atlas 不会自动删除。恢复后请先检查报告，再把 API 的 `ATLAS_PROJECT_STORE` 指向新库。源码应由 Git 或独立备份负责。若 API 重启报告发现未完成 apply，Atlas 只保留 journal 并报告；需要显式调用 `recover-apply`（`action=restore_before` 且确认 execution ID）才尝试恢复 apply 前文件，不会自动重放。

初次克隆不包含派生数据库和网页数据，先运行：

```sh
python3 application-atlas-production-pack/export_atlas.py
ollama pull bge-m3
python3 application-atlas-production-pack/embed_leaves.py
cd atlas-web
npm run gen
```

导出会载入已保存的翻译。已有数据库中的向量仅在输入内容未变时保留；新增或修改的类型由 `embed_leaves.py` 补齐。导出遇到目录缺失、重复或孤立正文会失败，并保留旧数据库。

## 对话页（Ask）

`/ask` 是一个只读的对话页面：用自然语言查询类型知识，回答问题前先检索语料，回答里给出引用类型链接。

- **只读是结构性的**：可调用的工具只有 `search_atlas`、`get_leaf`、`get_neighbors`、`get_section_tree`、`read_atlas_source`、`get_atlas_source_manifest`，没有 shell、网络、写文件或子 agent。注册表里没有写工具，不是靠提示词约束。
- **有界**：每次提问最多 8 轮模型调用、180 秒、60000 tokens；触顶会以明确状态结束（`turn_limit` / `timeout` / `token_limit`），不会无限跑。
- **引用可核对**：只有模型在本次回答中引用、**且**工具确实返回过的 slug 才会渲染成链接，无法凭记忆编造类型。
- **语料视为数据**：检索结果在提示词中被标注为不可信内容，文档里的指令不会被执行。
- **不猜数字**：token 用量按 provider 返回值记录，provider 不返回时为未知，费用始终显示未知。

工具层在 `atlas_tools.py`，MCP 服务（`mcp_atlas.py`）与对话页共用同一份实现，避免两处语义漂移。对话存储默认在 `application-atlas-production-pack/atlas/ask/`，可用 `ATLAS_ASK_ROOT` 覆盖。

## 模型与凭据

阅读网页、导出、离线测试不需要模型凭据。语义检索需要本地 Ollama；分类、查重及翻译会使用外部模型 API。凭据按需从 `ATLAS_API_KEY` 环境变量读取，未设置时读取本机 OpenCode 的凭据。不要把凭据提交到仓库。

网页「设置」页（`/settings`）可以在界面里配置模型服务：从 18 个常用 provider 预设中选择（Open Design、OpenCode Go/Zen、Command Code、OpenAI、Anthropic、Google Gemini、DeepSeek、Moonshot、Zhipu、DashScope、SiliconFlow、OpenRouter、Groq、xAI、Mistral、Ollama、LM Studio），填入凭据，测试连通性，并设定默认服务与模型。也可以用「从 OpenCode 导入凭据」把本机已有凭据一次性导入；导入会同时读取 `auth.json` 和 `opencode.db`，因为 OpenCode 把新加入的 provider 只写进后者。

配置保存在 `application-atlas-production-pack/atlas/model-config.json`，权限 0600，已加入 `.gitignore`；凭据只写不读，读取接口只返回打码值，明文不会出现在页面数据里。可用 `ATLAS_MODEL_CONFIG` 指向其他配置文件。调用解析顺序为：显式参数 → 按任务角色选择的模型 → 设置页的默认值 → `ATLAS_MODEL_PROVIDER` / `ATLAS_MODEL` / `ATLAS_API_KEY` 环境变量 → 本机 OpenCode 凭据。

除 `opencode_cli_adapter`、`execution_service` 和 `project_generation` 通过 OpenCode CLI 执行外，其余模型调用统一走 `atlas_model.chat()` / `atlas_model.complete_text()` / `atlas_model.embed()`。除 Anthropic 使用原生 `/messages` 形状外，其余 provider 都按 OpenAI 兼容接口调用。

### 任务角色与模型

不同任务可以用不同模型，通过环境变量配置；**留空表示沿用默认模型**：

| 角色 | 环境变量 | 使用位置 |
|---|---|---|
| `adjudicator` | `ATLAS_ADJUDICATOR` | `classify.py` 分类裁决 |
| `dedupe` | `ATLAS_DEDUP_MODEL` | `dedupe_judge.py` 查重、草稿定名 |
| `translate` | `ATLAS_TRANSLATE_MODEL` | 正文 / 研究笔记 / 关系 / 子域翻译 |
| `identity` | `ATLAS_IDENTITY_MODEL` | 新建草稿时生成身份 |

角色只是提示：若角色指定的模型不在当前 provider 的模型列表里（例如 Go 时代的 `qwen3.8-flash`），Atlas 会忽略该角色并回退到默认模型，而不是把无效模型名发出去。provider 可用的模型列表来自设置页的配置或预设。

内部所有调用都会在发送前解析一次实际使用的 provider 与模型，取不到用量时如实记为未知，不推测成本。

分类模型通过 `ATLAS_ADJUDICATOR` 配置，默认 `qwen3.8-flash`；查重默认 `mimo-v2.5`。草稿生成和 U17 执行还需要 OpenCode CLI。草稿 agent 默认禁止 shell、web、外部目录和子 agent，只能写当前 slug 的三个输出文件；仅在受信任的人工研究中设置 `ATLAS_DRAFT_ALLOW_WEB=1`，将网络权限从 `deny` 调整为 `ask`。U17 默认使用 `opencode-go/mimo-v2.5`，可用 `ATLAS_EXECUTION_MODEL=provider/model` 覆盖。执行时 Atlas 默认启动只监听本机的 OpenCode V2 子进程，使用 standalone 项目服务；V1/V2 权限文件按已安装主版本生成，受管 V2 session 还会固定 Atlas 权限规则，隔离副本中的 shell、MCP、web、外部目录和子 agent 默认关闭。HTTP/V2 完成/失败终态的固定验证由 Atlas 在 agent 停止后独立执行，模型自报验证不会冒充 Atlas 证据；权限交互只支持“仅本次允许”或拒绝，不提供持久授权，禁止/未知动作只能拒绝。`ATLAS_OPENCODE_URL` 仅作为显式信任的未托管服务覆盖，并需额外设置 `ATLAS_ALLOW_UNMANAGED_OPENCODE=1`；若该 V2 服务启用了 Basic 认证，还需提供 `ATLAS_OPENCODE_USERNAME`/`ATLAS_OPENCODE_PASSWORD`。Atlas 无法验证该服务的真实策略时不提供此绕过。隔离副本默认存到项目数据库旁；若该目录位于源项目内则改用系统临时目录，可用 `ATLAS_EXECUTION_ROOT` 指定持久且位于项目外的目录。项目状态库本身不能位于待执行的源目录内；此类项目需用 `ATLAS_PROJECT_STORE` 把数据库放到项目外。

## 入库规则

1. 生成或编辑完整草稿并通过结构检查，新增类型必须有研究笔记。
2. 对当前正文执行查重。正文、身份、研究笔记或正式数据库变更后，旧裁决失效。
3. `new` 裁决才可新增；`same/variant` 只能合并到裁决指定的类型。
4. 入库在临时语料副本中执行导出、翻译、向量补齐、网页生成及固定样本回归。
5. 固定回归达到 90%、没有请求错误，且数据完整后才更新正式语料。失败保留原始草稿和正式数据。

一次只允许一个语料更新任务。数据库最后通过原子替换切换，分类器自动重新加载；草稿 ID 保持稳定，成功后提供正式类型链接。发布过程有回滚记录；若进程中断，重启 API 或再次导出会恢复未完成的切换。不要在更新过程中用其他脚本绕过锁直接写数据库。

中文译文是已有翻译资产，部分历史翻译在生成时已截短；此次修复不会凭空补齐译文。详情页保留完整英文各章节、来源及完整原始档案，供核对。

## 验证

不访问模型、不产生 API 费用：

```sh
python3 -m unittest discover -s application-atlas-production-pack/tests -v
python3 application-atlas-production-pack/gate_check.py --score-only application-atlas-production-pack/atlas/gate_regression.json
cd atlas-web
npm run typecheck
npm run build
```

`--score-only` 只重算现有结果，未达标返回非零。现有结果原始准确率为 44/52（84.6%），纳入路线图已明确接受的三个替代标签后为 46/52（88.5%）；这不是本轮修改后的在线分类成绩。

运行 `python3 application-atlas-production-pack/gate_check.py` 会重新调用分类 API，生成 `gate_regression.json` 和 `gate_summary.json`。正式入库必须执行本次临时库上的新回归，不接受旧报告替代。

GitHub Actions 在 push 和 pull request 上执行 Python/Node 依赖审计、离线回归、语料重新导出、网页数据生成与一致性校验、类型检查、生产构建和 Playwright 浏览器路径。纯静态构建只提供阅读功能，草稿页面需要本地 API 配合。当前本地单用户威胁模型和明确边界见 [`SECURITY.md`](SECURITY.md)。
