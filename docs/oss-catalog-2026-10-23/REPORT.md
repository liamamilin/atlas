# 个人知识管理应用：第一版实际验收

验收日期：2026-10-23（Asia/Shanghai）。本轮交付范围是一个已有叶子的可用知识库切片。

## 真实数据

| 场景 | 项目 | 数量 |
|---|---|---:|
| 把零散笔记连接成知识网络 | Logseq、思源、Trilium Notes、Foam、Org-roam | 5 |
| 在文本文件与编辑器中积累知识 | Foam、Org-roam、SilverBullet | 3 |
| 搭建自己掌控的个人 Wiki | Trilium Notes、SilverBullet、TiddlyWiki、思源 | 4 |

全局共 7 个项目、12 条关联，没有按场景复制仓库。见 [数据检查](CATALOG_CHECK.json)、[最初联网采集凭据](INTAKE.json)与可复用的 [项目快照](../../application-atlas-production-pack/oss_catalog_data/pilot.snapshot.json)。

## 逐项目资料复核

下列介绍、功能、适用范围和关联均逐项对照官方 README；具体摘录和不可变 blob 身份保存在卡片内。

| 项目 | 本轮核对的核心依据 | 许可证原文核验 |
|---|---|---|
| [Logseq](https://github.com/logseq/logseq) | 知识管理、PDF 批注、任务管理与 DB graphs；保留 README 对数据库版 beta 和备份的说明，不泛化旧版文件存储描述 | AGPL-3.0 |
| [思源](https://github.com/siyuan-note/siyuan) | 块级引用、双向链接、Markdown 编辑与 Docker；卡片保留浏览器部署功能限制 | AGPL-3.0 |
| [Trilium Notes](https://github.com/TriliumNext/Trilium) | 分层个人知识库、关系/笔记链接图、自托管同步 | AGPL-3.0 |
| [SilverBullet](https://github.com/silverbulletmd/silverbullet) | Markdown Pages、双向 Wiki 链接、自托管、Lua 与查询 | MIT |
| [TiddlyWiki](https://github.com/TiddlyWiki/TiddlyWiki5) | 非线性个人网页笔记、单文件 HTML 与 Node.js 形态 | BSD-3-Clause；GitHub 字段 NOASSERTION，按原文核验 |
| [Foam](https://github.com/foambubble/foam) | VS Code、Markdown 文档、反向链接、Wiki 链接与关系图 | MIT；GitHub 字段 NOASSERTION，按原文核验 |
| [Org-roam](https://github.com/org-roam/org-roam) | 纯文本知识管理、离线个人 Wiki、反向链接与 Emacs / Org-mode | GPL-3.0 |

技术信息明确标为 GitHub 语言统计，不据此声称完整部署技术栈。采集器没有执行上游代码。

## 联网采集与更新

- 首次实际读取七个仓库的 repository、README、license 与 languages 资源，形成上述数据。
- 随后运行新采集器的第一次增量核验：新增 0、更新 1、未变 6、失败 0。
- 第二次增量核验：**新增 0、更新 0、未变 7、失败 0**，见 [联网更新原始结果](LIVE_REFRESH.json)。
- 单独绕过旧卡片缓存，对 Foam 执行了完整实时采集；许可证核验保持 MIT / open_source，见 [完整采集结果](FULL_FETCH.json)。
- 实际 GitHub 候选搜索返回 39 个匹配，读取前 15 个；结果保留为待复核候选，未自动发布，见 [搜索记录](DISCOVERY.json)。
- 在用户当前 5188 页面实际点击“更新项目资料”，经 5199 API 完成七个仓库的联网核验：新增 0、更新 0、未变 7、失败 0；随后从 Foam 卡片打开了真实 GitHub 仓库，页面错误为 0。见 [现场端到端凭据](LIVE_UI_UPDATE.json)与[更新完成截图](live-update.png)。

版本管理的数据快照不携带用户收藏；本地库保留收藏和每次更新记录。

## 自动化与真实浏览器验收

- Python 项目库合同检查 **12/12 通过**：首次/重复运行、身份去重、收藏与重开、关联替换及其他叶子保护、仓库改名、条件搜索、快照一次导入、事实依据缺失、未知/受限/变更许可证、未变来源复用、并发与中断恢复、事务回滚。
- 原工厂 API 文件类型回归 **2/2 通过**。
- 前端既有单元检查 **9/9 通过**，TypeScript 检查和生产构建通过。
- Chromium 真实浏览器 **5/5 路径通过**，连接隔离的真实本地 API 和 SQLite，没有伪造项目接口响应：
  1. 首页进入已有叶子，七张卡片可浏览；工厂不在主导航，历史入口仍存在。
  2. 场景筛选后刷新保持；展开卡片，查看许可证、来源摘录和原仓库链接。
  3. 搜索 Foam，收藏后重载仍存在，取消收藏可更新列表；统一搜索和许可筛选可用。
  4. 跨站写入、无效叶子和非布尔收藏参数被拒绝。
  5. 390px 手机布局无页面横向溢出；未覆盖叶子仍能浏览原资料，并明确显示暂无项目。

首轮浏览器发现收藏筛选的受控输入会因异步 URL 导航短暂回退，已修正并复测通过。截图：[桌面](pilot-desktop.png)、[手机](pilot-mobile.png)。

追加执行了全部常规页面 22 用例与历史工厂 43 用例。常规页面首轮 21 通过，发现新版首页遗漏分类为空的提示，补齐后该用例复测通过。工厂首轮 41 通过，另外两条因并行测试共用 trace 目录而失败；各套输出目录隔离后，两条均复测通过。历史模板页首次并发初始化数据库的竞争也已串行化，并补充可重试错误响应；相关历史路径复测没有再出现数据库锁错误。

## 历史与交付边界

首页与主导航以分类、场景和项目为中心；旧开发工作台、问答、分类草稿、案例和工厂通过 `/history` 保留原地址。旧叶子模板面板移到 `/history/types/<slug>`，新叶子页底部可进入。新模块不迁移、不删除旧工厂或 U17 数据。

本机 API 在确认无活动生成、发布和开发执行后，已重启加载新接口；默认 5199 API 返回 3 场景与 7 项目，现有 5188 前端可直接访问新版。

首批场景和介绍由本轮整理并对照来源核验。仓库采集和更新已自动化；全库自动生成与候选自动发布不属于本次已完成范围。资料复核由本轮实现过程完成，未把它标为用户人工终验或第三方项目部署实测。
