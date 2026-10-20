# 会后有据：会议笔记辅助试用交付

地址 **http://127.0.0.1:5275/**。仓库根目录启动：`python3 examples/meetings-trial/app/serve.py --port 5275 --demo`。独立源码包 meetings-source.zip 不包含用户数据库。

## 开发来源与先后顺序

固定场景 scn_805c99ffe8da4532817592bb466a505e r1，原正式记录仍 draft。范围、来源研究、definition.json 和可执行验收程序先于应用完成；packages/EXPORT_RECEIPT.json 记录模板与标准包摘要，CONSUMPTION.json 在应用尚未开始时记录 Codex 实际读取的交接文件摘要。没有应用完成后倒填模板。

共享案例为 `case:assisted-meetings-joplin r2`，digest `010aea528378355df4fbe4cb895a261c3ceb72e1d1e64655c685343630faf4be`，固定 [Joplin commit cf57e593](https://github.com/laurent22/joplin/tree/cf57e5932584c0fbd894d8510f1a31a4d41f2251)。CaseLibrary.commit_research 服务保存，正式应用实证 API 原样读取同一记录；模板 inputs/shared-case-record.json 引用同一 r2。

静态证据：Folder.notes 的单一 parent_id 和软删除过滤，Note.new 的新笔记容器赋值，Note 的 anywherePattern 标题/正文搜索分支，REST API 文档的移动与正文语义。置顶、归档、本机 Python/SQLite、回收不自动过期为目标设计推断，不声称来自 Joplin 的已运行能力。根 LICENSE 为 AGPL-3.0-or-later，并含文件级例外与商标约束；未穷尽例外，仅参考研究，不复制上游实现或标志。upstream-evidence.zip 保存四份固定文件、许可证和摘要。

研究时发现 r1 把 Note.new 的定位误称为移动、把 anywherePattern 误标为 titlePattern。已在生成模板前经正式服务追加 r2 纠正，r1 请求/记录/回执保留；不是独立审阅通过。证据审阅 pending、上游运行 not_run，与下游应用的真实运行分开记录。

模板 digest `3a1dc2c414023091d3189cab0b5fe51cff318442b38a515d8fc2c3e0143a4c5a`；模板 ZIP SHA `90231160af1043ec48481c96edd93d2584a7fd75b1ad07fd8b860775685369cb`；标准开发包 ZIP SHA `42d624b768797aa9d265f0725726613b67d739c7dc4ba213c91d5d40dd48c433`。本地冻结仅固定输入，未登记正式模板或伪称正式队列消费。

## 真实浏览器旅程

| 核心旅程 | 实际结果 | evidence 原始记录 |
|---|---|---|
| 捕获与项目归属 | 空库创建“产品发布”“网站改版”；会议正文先入收件箱，再移入产品发布，网站项目不混入该笔记 | 01-start、02-project-a/b、03-saved-inbox/moved-project、05-project-b-isolation |
| 正文保存与编辑 | Markdown 表格原文保存；追加负责人和验收说明，保存与刷新后仍在 | 04-edit-open、04-edited-refresh |
| 置顶、归档与检索 | 置顶旧笔记在新笔记前；归档后默认活跃页不显示，大小写不同的正文词 mapledecision 仍能找到并打开；无结果有空状态 | 05-pinned-library/two-projects/pinned-title-sort、06-body-search/active-excludes-archive/archive-found-by-search/empty-search |
| 回收与恢复 | 回收站找到原笔记，恢复后保留项目、正文、置顶和归档标记 | 07-trash、07-restored-original-state |
| 真实进程重启 | 停 PID 61781、连接拒绝；同数据目录重启 PID 62169，三项目/两笔记全字段相同；浏览器重新检索并打开编辑后的完整正文 | 08-before-restart/stopped/after-restart、08-search-after-restart/body-after-restart |

最终页面 evidence/final-home.png 与 final-note.png；当前正文示例含“试用”，不是真实工作记录。数据仍在 examples/meetings-trial/data/meetings.sqlite3，未打包或提交 Git。

## 检查与交付

- 开发前冻结的 N01–N04 在各自隔离的真实 HTTP 进程通过，N04 包含停进程与原目录重启。测试程序未在应用完成后改写断言。HTTP 证明与浏览器旅程分别记录。
- 三项回归通过：正文原样与旧版本不能覆盖、项目/归档/检索/恢复、空正文零写入。ruff 检查通过；CI 新增会议应用回归入口。
- 独立解压源码 ZIP，仓库外运行 --demo 成功，自动创建示例项目与笔记，无仓库依赖。evidence/standalone-result.json、final-runtime.json 记录结果与实际运行源码 SHA。
- 源码 ZIP SHA `7083a6c61b1ccb3a60801f07fa371bfa345304c1024c259d94795d596689a8a4`，逐文件摘要见 SOURCE_MANIFEST.json。
- 无附件/富文本渲染/语音、导入导出、同步协作、项目删除/整项目归档、永久清理。显式保存，没有自动保存；使用者离开编辑页前需保存。完整并发专项、错误矩阵和严格独立运行评审后置。

本轮受控 OpenCode 新增 0，历史 87/500、书签业务修复 8/8 不变。G1 blocked、T08 not_started；本次为辅助试产，不替代严格验收。
