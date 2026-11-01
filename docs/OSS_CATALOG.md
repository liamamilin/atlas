# Atlas：按场景发现真实项目

当前主线为 **Leaf → Scenario ↔ Project**。沿用 Atlas 已有分类，真实项目提供事实基础；历史模板工厂保留在 `/history`，不再作为新版主入口。

## 当前工作方式

所有现有叶子都可指定采集，没有试点白名单。搜索不设 Stars 门槛，可配置分页。场景先保留，允许重复；项目不要求资料完整或凑满某个数量才展示。

核心底线：仓库身份真实且公开、介绍有实际官方资料来源、推断及缺项明确标注、许可证未知或受限时不误标开源。GitHub Token 只用于 GitHub 请求授权，不进入模型输入、快照或审计。

- 场景来自已有叶子的定义；生成失败时保留既有场景，必要时使用标明“初步”的分类场景。
- 搜索发现的真实候选持久保存。模型不能添加搜索或候选队列之外的仓库。
- 读取仓库公开元数据、README、许可证与仓库内官方文字文档。README 缺失、许可证不明、模型返回的资料格式不完整时，先依据已核实的公开元数据生成初步卡片，并标明待补充。共享服务暂时不可用时保存进度、自动等待并恢复；认证和配置错误明确暂停。
- 项目与叶子的归属独立于场景关联；还没有场景关联的项目也能浏览、搜索和收藏。
- 卡片区分原文引文、资料概述、条件适用和待核实推断；不再强制每个字段有逐字引文。提供的引文若不存在于原文，则丢弃，不会冒充证据。
- 支持应用、库、资源集合等真实项目并标明类型。明确无关的候选排除后保留原因。
- 许可证独立读取；核验不完整可以入库，标记为待核验。标准开源、受限源码与未知状态分开展示。

## 批量执行

`oss_batch.py` 是持续批量入口。叶子清单来自现有分类，指定哪些叶子就处理哪些，不默认扩展到全库。

```sh
# 仓库根目录：发现候选并自动处理；每叶子搜索后固定本次候选集
python3 application-atlas-production-pack/oss_batch.py start \
  --leaves feed-reader diagramming-application password-manager \
  --search-pages 2 --batch-size 16 --output /tmp/atlas-batch-result.json

# 只消化已有队列；开始时冻结目标，不在本次任务中追加搜索结果
python3 application-atlas-production-pack/oss_batch.py start \
  --leaves feed-reader diagramming-application password-manager --existing-only

# 查看和恢复同一个任务，job ID 来自输出、API 或本机 batches 记录
python3 application-atlas-production-pack/oss_batch.py status --job batch_<id>
python3 application-atlas-production-pack/oss_batch.py resume --job batch_<id>
```

批次大小只是执行单元，不是采集完成数量上限。任务自动接续后续批次；每个目标在同一任务中处理一次，单项读取失败保存原因后跳过，不无限重试。临时故障在短重试后进入持久的 `retry_wait`，按 1、2、4、8 分钟退避，最高每 15 分钟再试，不因冷却轮次数耗尽停止；更长的服务端等待时间会被遵守。模型和 GitHub 共享网络/限流故障都适用。已完成目标保留，只继续尚未完成的目标。API 自带每 15 秒巡检，服务重启后会自动接回启用恢复的任务，不依赖浏览器。永久凭据或配置问题仍明确暂停。已结束任务的 `resume` 不会重新发起采集；可新建任务补充或重试。

`oss_discovery.py batch --leaves ...` 也委托给同一个批量执行器。`oss_discovery.py export --db <path>` 导出当前浏览快照，覆盖所有已采集叶子，不再限定三个试点。

资料读取沿用 4 路并发，模型提取默认 4 路并发，每个请求仍整理 4 个项目；结果由同一协调线程逐项写入并保存检查点。模型组分别记录调用次数、回执及重试状态，避免并发更新相互覆盖。某组服务暂时失败时，已完成的其他组仍先保存；未完成组自动等待后继续。`ATLAS_OSS_MODEL_CONCURRENCY=1` 可退回串行，允许范围为 1–4；默认每批 16 个候选时有 4 个提取组。叶子仍按任务清单顺序推进。

每个任务把叶子、候选 ID、单项状态、当前批次、运行记录和异常保存到 SQLite，并保存本机 JSON 进度。整个任务持有更新锁，避免并发更新覆盖事实；浏览与搜索继续可用。来源变化、单项失败和重复仓库按 numeric repository ID 增量处理，收藏不被覆盖，稀疏结果不覆盖已有完整事实。

## 页面

- 首页使用轻量覆盖概览，只展示已有项目的类型；“我的收藏”可从主导航直接进入。新版使用指南位于 `/guide`，包含资料说明与本地服务排查。
- [项目库](http://127.0.0.1:5188/discover)：选择任意现有叶子；展开“批量采集”可加入多个叶子、启动任务并观察进度。
- 项目每页最多 24 个，可按名称或最近核验排序；页码、关键词及筛选保存在地址中，刷新与浏览器前进后退可恢复。清除筛选会保留当前类型。场景数量按全部筛选结果统计，不受分页影响。
- 批量面板提供“仅处理已有候选”选项，进程中断和模型暂停时显示原因及继续按钮；查询参数保留搜索及筛选。
- 单叶子“更新项目资料”仍执行一次更新；持续处理使用批量入口。
- [设置](http://127.0.0.1:5188/settings)：保存、测试或清除 GitHub Token；留空保留，保存后立即使用，接口不回传明文，本机文件权限 0600。
- [历史入口](http://127.0.0.1:5188/history)：旧模板与历史执行保留。

## API

| 接口 | 用途 |
|---|---|
| `GET /api/oss/catalog` | 按 `leaf/q/scenario/license/favorites` 浏览；返回所有现有可用叶子与候选状态 |
| `POST /api/oss/refresh` | `{leaf}`，单叶子一次更新；个人知识管理保留原编辑整理的更新方式 |
| `GET /api/oss/runs/<id>` | 单次更新进度 |
| `POST /api/oss/batches` | `{leaves:[...],existing_only:false,batch_size:8,search_pages:1}`，异步持续批量 |
| `GET /api/oss/batches` | 最近批量任务 |
| `GET /api/oss/batches/<id>` | 持久进度；发现进程已退出时标记中断 |
| `POST /api/oss/batches/<id>/resume` | `{}`，继续未完成目标 |
| `POST /api/oss/projects/<id>/favorite` | `{favorite:boolean}` |
| `GET/POST /api/settings/github` | 查看凭据状态、保存或清除 |
| `POST /api/settings/github/test` | 测试连接并返回公开额度 |
| `POST /api/settings/model/fallback` | 保存额度耗尽备用规则；`{reset:true}` 清除已激活状态并重试主服务 |

写接口沿用本机 Host、Origin 和 JSON 请求边界。叶子需存在于 Atlas 分类中；路径穿越、虚构仓库 ID、私有资料及凭据外传不属于放宽范围。

浏览接口可传 `limit=1..100`、`offset=0..` 与 `sort=name|recent`；`pagination.total` 是分页前的匹配项目数。未传 `limit` 保留原来的完整读取行为，供导出与已有脚本使用。`view=overview` 只返回覆盖统计、场景及已有项目的类型，不返回项目正文或候选队列，供首页使用。

前端兼容尚未重启的旧 API，以本地分页保持可用；响应体缩减需新 API 生效。已有采集任务运行期间不要为了界面更新中断任务，待任务结束后再重启 API。

## 数据与限制

- `atlas/oss-catalog.sqlite`：场景、全局仓库、叶子归属、多对多关联、收藏、候选、运行和批量进度。
- `atlas/oss-discovery/`：公开来源与模型结果缓存、逐批审计及任务 JSON；运行数据不入 Git。
- 部分读取失败时，已经成功读到的许可证和文档仍保存在 `atlas/oss-discovery/evidence/`；失败项后续继续重试，不将失败缓存为永久缺失。
- `oss_catalog_data/pilot.snapshot.json` 与 `batch.snapshot.json`：可版本管理的浏览快照，包含来源及许可证状态，不包含凭据和收藏。
- `license-reviews.json` 与 `discovery-reviews.json`：来源摘要绑定的已有人工复核，保持纠正过的许可及关联说明。

分页遵守 GitHub Search 的接口范围；默认每查询取一页，每页至多 100 条，可设 1–10 页。默认非 fork、非归档；排序仍可按 Stars，但不设置最低 Stars。不会宣称穷尽所有项目。

当前只读取仓库内官方资料，尚未自动爬取站外帮助中心。资料概述与推断不代表部署、安全或功能实测。初步卡片与待核验许可会明确显示。

批量提取沿用现有模型配置。对于当前 DeepSeek 模型，资料整理使用已实测的非思考模式，避免推理占满 JSON 输出；其他流程保持原行为。参数依据 [DeepSeek 官方文档](https://api-docs.deepseek.com/guides/thinking_mode/)。

## 模型额度与自动切换

本机已配置 **Open Design → OpenCode Go / `deepseek-v4.1-flash`**。确认余额或配额耗尽后，同一请求在 Go 重试一次；后续请求及重启后的任务继续使用 Go。原默认服务仍保留，充值后可在设置点击“重试主服务”恢复。普通 HTTP 429 限流、认证失败、网络故障不会被当作余额耗尽，也不会自行切换其他模型。

Go 使用官方 OpenAI 兼容入口，并携带 Atlas 自身的 User-Agent 与批次会话 ID，参考 [OpenCode Go 接入要求](https://opencode.ai/v2/docs/console/go/#where-can-i-use-it)。公开模型列表不验证密钥，所以 Go 的“测试连接”还执行一次极小模型请求。DeepSeek V4.1 Flash 使用 Go 订阅额度；先前将 Step 5 Preview 称作免费模型的说法已更正，官方也将其列为订阅额度模型。

持续批量对 HTTP 408、425、429、全部 5xx 服务端及网关错误（包含 520、522、524），以及超时、临时网络失败和连接中断，最多尝试 3 次（含首次），默认等待 2 秒、4 秒。`Retry-After` 要求更长等待时遵守它；要求超过 60 秒时交批量执行器持久等待，不提前重试。认证、地址及永久请求错误不重试，也不冒充额度耗尽。每次失败记录实际 provider、model、上游 HTTP 状态、脱敏错误摘要、重试次数及时间，保存在运行记录的 `model_errors` / `model_retry` 中；不保存请求头或凭据。

临时故障的短重试仍失败时，批量状态为 `retry_wait`，自动等待后续跑；仅凭据、配置或主备额度均不可用等需要处理的问题为 `paused_model`。已经读到的来源缓存及已完成项目保留，未整理项目保持未完成。处理好凭据或额度后点击继续，从保存位置恢复。模型返回无效 JSON 则仍按有界格式重试和资料不足标注处理。

备用配置不包含密钥；激活状态单独存入本机 `atlas/model-config.fallback-state.json`，权限 0600，并由 Git 忽略。模型缓存与逐批回执记录实际使用的 provider、model、切换原因及时间；Go 结果不会缓存成 Open Design 的响应。

## 验收记录

- [新版 API 重启与真实数据页面验收](product-polish-2026-10-23/live-validation/SUMMARY.json)：重启前后完整性校验、真实 HTTP 响应体积、桌面与手机只读浏览器检查，以及采集并行运行时的一致性快照分页核验。
- [个人知识管理首轮](oss-catalog-2026-10-23/REPORT.md)
- [三个叶子首次发现](oss-batch-2026-10-23/REPORT.md)
- [分批与 Token 设置复验](oss-batch-v3-2026-10-23/REPORT.md)
- [开放批量与剩余队列验收](oss-open-batch-2026-10-23/REPORT.md)
- [模型额度自动切换验收](oss-provider-fallback-2026-10-23/REPORT.md)
- [模型临时错误自动重试验收](oss-model-recovery-2026-10-23/REPORT.md)
- [模型并发与断点恢复验收](oss-concurrency-2026-10-23/REPORT.md)
- [520 网关错误恢复修复](oss-recovery-520-2026-10-24/REPORT.md)
- [持续自动恢复、主动巡检与四路并发](oss-unattended-2026-10-24/REPORT.md)
- [新增三个叶子验收与下一批 100 个叶子](oss-expansion-2026-10-23/REPORT.md)

```sh
python3 -m unittest discover -s application-atlas-production-pack/tests -p 'test_oss*.py' -v
python3 -m unittest discover -s application-atlas-production-pack/tests -p test_github_settings.py -v
cd atlas-web
npm run typecheck
npm test
npm run build
npm run test:e2e:catalog
# 对已运行的真实 API 与前端做只读检查，不会启动或替换测试数据库
npm run test:e2e:live
```
