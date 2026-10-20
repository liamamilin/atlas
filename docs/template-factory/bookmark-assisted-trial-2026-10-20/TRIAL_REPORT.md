# 留存 · 书签辅助试用交付

已可真实试用：**http://127.0.0.1:5273/**。源码：`examples/bookmark-trial/`。独立源码包：`bookmark-trial-source.zip`（不含个人数据库）。

仓库根目录启动：`python3 examples/bookmark-trial/app/serve.py --port 5273 --demo`；解压后在 `bookmark-trial/` 执行 `python3 app/serve.py --port 5273 --demo`。Python 3.10+，本机实际3.10.13，标准库零安装。

## 七条真实浏览器旅程

全部由 Codex 使用桌面应用的真实 in-app browser 操作实际运行进程；不是API fixture代替。原始可访问性快照、截图与独立进程读回在 `evidence/`。

| 旅程 | 实际操作与结果 | 证据 |
|---|---|---|
| 1 启动并打开 | 127.0.0.1:5273 首页真实打开，保存表单、列表可用 | 01-start.ax.txt/png、final-home.png |
| 2 保存并读回 | 页面分别保存HTTP台灯、HTTPS木工教程；标题/描述不同；刷新仍在（2演示＋2新增＝4） | 02-save-refresh.ax.txt/png |
| 3 分类整理 | 页面创建“周末灵感”；把台灯从未整理移动过去；刷新仍归该分类，筛选只显示它 | 03-category-created、03-move-refresh |
| 4 搜索找回 | 分类＋标题“阅读角台灯”、域名127.0.0.1、描述amberdesk均找回目标；不匹配词显示0条/没有匹配的收藏 | 04-title/hostname/description-search、04-no-results |
| 5 打开原始链接 | 点击台灯标题产生真实新标签，精确目标 http://127.0.0.1:5273/demo-page?item=Lamp&color=warm%20white#details；路径、查询串、片段保留 | 05-open-target.ax.txt/png |
| 6 错误与恢复 | 页面提交not a url与javascript:alert(1)，均显示invalid_url，记录保持4条；改为合法HTTPS后成功且只增1条 | 06-invalid-url、06-non-http、06-recovered |
| 7 真实重启 | 停PID53560，确认端口拒绝连接；同源码同data-dir起PID53876。五条记录/五分类完整字段相等；真实页面刷新、组合搜索、点击新标签仍正常 | 07-before/after-restart.json、07-stopped.json、07-restart-search、07-restart-click-tabs |

随后保持运行最终源码：PID 54991，持续终端session9301，健康200。重新读回全部5条，并在真实页面完成回收站删除/恢复（extra-trash、extra-restored），保留用户可继续打开的标签。曾尝试以短命shell的nohup启动，执行器退出后进程未保留；已改为持续终端会话并重新打开验证。服务若随终端退出，使用上面的同一命令恢复。

## 输入与实际消费

- 叶子 bookmark-manager；“生活待购与灵感收藏夹” scn_7756e0007f6a463a97316f3f49c15248 r2。
- 案例 case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1；同一20条已接受场景事实。固定上游 LakhindarPal/bookmark-manager commit539881bc67099d491e8ab6f85de0f443fa7de623。本轮未重新研究、未运行上游。
- prepared plan：`8bf361dbaae383b02cb3fd48020cfa6d9a229edc2f08a00e5f92029fb8c3e3a4`。
- 原九文件先核SHA；四份R8修订、五份历史原字节复用。调用现有 research_from_accepted_facts → render_candidate → freeze_blueprint → export_development → verify_frozen，未导入/登记/发布正式tpl。
- 本地template digest：`6febed5fd5526e5955dbb25005ae1b45bcc876ea13ecc704b711d70f1f40bd8c`。local freeze仅固定输入，不是独审通过。标准包P0/P1规格、程序原样保留；另附TRIAL_SCOPE。
- 实际读取 HANDOFF.md、CURRENT_PHASE.json、ARCHITECTURE.md、DECISIONS.md、CATEGORY.md、ACCEPTANCE_CONTRACT.json；采用单用户扁平分类、未整理默认、标题/hostname/描述搜索、原URL和软删除语义，由当前Codex直接实现。本轮不是正式application-development队列消费；PROJECT_DECISIONS原包也不被伪改为正式确认。
- 来源标准包SHA256 `0b5eb5dae550ab2b4a5a0c7879878ba8289383520752f20dbd0c99b46078738f`；来源模板快照ZIP `9dfddd8a62ec46f31725918ae13500da461e04a74e3939a481ab3d4b7a810e31`。完整来源见packages/EXPORT_RECEIPT.json与应用SOURCE.json。
- 完整应用源码ZIP SHA256 `326ff434c4263badba31378d4bdcc4c4307a8bc0353789f104587c32effd52ea`。各文件SHA与大小见SOURCE_MANIFEST.json；最终进程与app/serve.py字节绑定见evidence/final-runtime.json。

## 检查与迭代

- 初版真实表单被Origin:null拒绝：Referrer-Policy:no-referrer令同源POST丢失来源信息；修为same-origin，仍拒绝跨源表单，真实重试成功。保留initial-origin-failure原始快照与图。
- 六项应用回归通过，涵盖URL原文、Unicode/大小写搜索、事务回滚、分类移动/迁移/软删恢复、初始化不复活改名预置、HTTP JSON错误、来源保护与HTML转义。`python3 -m unittest discover -s examples/bookmark-trial/tests -v`；原始regression.log。
- 复用原R8未改程序 A01/A02/A07/A08/A11，独立临时真实HTTP应用。首次4/5：A08未知/go目标错误体非JSON；修复该应用分支并只复测A08，通过。最终五个用例各有真实通过结果；原失败不删除，subset-results列出全部6次执行。不是完整严格P0、不是宿主phase proof。
- ruff针对应用、测试与导出脚本通过；来源包verify_frozen再次通过。
- 交付源码ZIP真实解压至临时目录，按README命令启动，首页200，首次2演示数据；不依赖仓库及第三方包。standalone-result.json、standalone-startup.log。
- 本轮初版＋两次应用缺陷修正，另完善连接关闭、来源核验与打包说明；应用工作副本迭代与严格工厂8/8分开。常规CI保留并加本例六项回归；不重复跑无关联的13组门禁。

## 已知缺口与原正式状态

- 未实现P1导入导出、去重、外部元数据；无账户/云同步/公网部署。无复杂多端设计，长列表仍为完整列表，无分页。默认仅本机127.0.0.1；不要暴露公网。
- 未完成完整32分支错误矩阵、严格P0全套、并发/压力、P1离线运行证明、分层独审和精确phase proof。辅助结果只证明核心七旅程可用。
- 源模板phase_acceptance原缺括号无有效检查点，原失败保留，不修成passed。严格G1仍blocked，T08 not_started；正式发布0、严格P0交付0。本轮新增辅助应用1、正式模板0、正式开发队列消费0。
- 工厂/外部OpenCode本轮新增0，factory86＋external1＝87/500，活动0；业务修复仍8/8。只读现场核对见formal-state-readonly.json。不称开发成本0；本轮消耗Codex开发、工具执行与人工试用时间。
- 原窗口、旧冻结字节、全部失败/grant/预算记录保留；本轮不恢复严格队列，也不新增恢复平台。

首份可用书签应用交付后，再以同一路线处理月度预算、多项目会议笔记；它们尚未在本轮开发，不冒充T08启动。
