# 品类认知与来源

固定的模型调研记录；来源访问日期与 Atlas 叶子原稿编写日期含义不同。叶子原稿的研究笔记链接属于原语料上下文，不表示本包附带该文件；本包来源以以下条目及未知项为准。

类别事实（多来源一致）：书签管理器的稳定内核是“用户主动保存的 URL 记录 + 持久累积的个人库 + 用户自定的组织方式 + 日后可检索并跳回原页”。组织模型在成熟产品中收敛为两种：单一归属的收藏夹/集合（Raindrop 每个书签只属于一个收藏夹；Linkwarden 每个 Link 恰好属于一个 Collection）与多标签（两者都支持），并普遍提供“未分类/Unsorted/Unorganized”作为保存时未归类的默认落点。元数据（标题、描述、图标、预览）通常自动抓取且可编辑，但抓取失败不能阻止记录落库。检索范围通常是标题、URL、描述、标签、备注；正文全文检索需要额外索引（Linkwarden 需 Meilisearch，Raindrop 将其列为 Pro 能力），不属于核心。重复处理分两档：保存时预防（Linkwarden 的“Prevent duplicate links”偏好）与事后筛查（Raindrop 的 Duplicates 筛选，需 Pro）；两者都提醒导入路径往往不去重（Linkwarden 明示同一文件导入两次即两份）。删除普遍是软删除（Raindrop 进 Trash 可拖出恢复）或明确不可撤销（Linkwarden 删除 Collection 连带子集合、全部链接与副本，且无法撤销；批量删除也无撤销）。导出普遍存在但不等于完整备份：Linkwarden 的 backup.json 不含截图/PDF/快照，linkding 的 UI 导出不含配置、快照与预览图。保存网页副本是可选重能力，成本与失败模式明确（无头浏览器、内存占用、反爬、登录墙、超时、体积上限；刷新会先删旧副本）。协作与权限只对共享库有意义，Linkwarden 用 Viewer/Contributor/Admin 三级并保留属主专属操作；单用户场景无需引入。

本场景（生活待购与灵感收藏夹，普通网络用户，单人对自己的链接库）的建议：首版只做四件事并逐条对齐验收——(1) 保存：URL 必填、标题可自动或手动补全、抓取失败也先落库；(2) 归类：单一归属的简单分类，保存时可选中或新建，未选则进“未分类/以后看看”，并支持之后移动到其他分类；(3) 检索：关键字匹配标题/URL/备注 + 按分类浏览，默认按添加时间倒序；(4) 打开：点击记录在新标签页打开原始 URL，库内不承载正文。数据生命周期建议为“保存 → 未分类 → 归类 → 检索 → 打开 → 删除 → 回收站 → 手动清空”，删除分类时必须明确二选一（把其中记录移入未分类，或级联删除并二次确认），不能让用户在没有提示的情况下丢失记录。边界情形应显式覆盖：同一 URL 重复保存（提示已存在并允许跳转，或允许重复但可合并）、URL 变体（跟踪参数、末尾斜杠、http/https、大小写域名）导致的“看似不同实则相同”、无效或非 http(s) 协议、保存时离线或无标题、超长标题与中文/emoji 检索、分类重命名与删除最后一个分类、空库与空分类的空状态、回收站中的记录不参与检索。建议提供简单的导出（JSON 或浏览器书签 HTML）与导入（至少能读浏览器导出的 HTML），因为这是防止锁定与换机迁移的最低成本；但不必做快照备份体系。明确不做：网页快照、失效链接扫描、全文索引、公开分享、多人协作与角色、审计日志、计费与配额、管理后台。若未来出现服务端抓取元数据，才需要引入 URL 校验与内网地址拦截（linkding 的 SSRF 防护是现成参照），并加超时与响应体积上限。合规与隐私上，个人收藏可能包含商品页、健康或家庭改造等敏感偏好，默认应私有、不公开、不默认上传第三方分析。

替代与复用：对本场景，现成方案分三类——SaaS（Raindrop，免费额度宽松、开箱即用，但重复/失效检查与全文检索在 Pro，数据在厂商侧）；自托管开源（linkding，MIT，单容器 + SQLite，功能已远超本场景，且快照能力还要 Chromium 与内存；Linkwarden/Karakeep，AGPL-3.0，快照/全文检索/协作齐备但明显偏重）；浏览器内置书签（零成本，但与单一浏览器配置绑定，缺少库级检索与迁移便利）。结论是“自建薄应用”优于“集成重型产品”，但应复用类别约定而非代码：单归属分类 + 未分类落点 + Netscape HTML 交换格式 + 软删除。若确需复用代码，linkding 的 MIT 许可最宽松（保留版权与许可声明即可）；Linkwarden 与 Karakeep 为 AGPL-3.0，作为独立服务通过网络提供时可能触发源码提供义务，须先做法务评估——本任务未复制任何第三方代码。

未知：未运行任何产品，以上均为文档所述行为；未验证万级书签下的检索性能、中文分词效果、URL 规范化的具体实现，以及各产品回收站保留期与导入去重的实际边界。

## S01 · Atlas confirmed input

inputs/scenario.json · scn_b92e41ce674f405fad0c87381f1dc5b7@1

把偶然看到但当下不处理的外部网页链接留存，日后需要时能重新找到并回到原页面

Atlas scenario input; not a third-party code license



Pinned requirement input

## S02 · linkding — GitHub 仓库 README（sissbruecker/linkding）

https://github.com/sissbruecker/linkding · master 分支，2026-10-17 访问（未固定提交）

自托管书签管理器，主打极简与 Docker 部署。功能包括：用标签组织书签、批量编辑、Markdown 备注、稍后读、与其他用户或访客分享、自动抓取标题/描述/图标、自动归档为本地 HTML 或 Internet Archive 快照、以 Netscape HTML 格式导入导出、PWA、Firefox/Chrome 扩展与 bookmarklet、OIDC/代理 SSO、REST API、带原始数据访问的用户管理后台。

MIT（仓库 LICENSE.txt，Copyright (c) 2019 Sascha Ißbrücker）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

可作为自托管替代方案评估或参考其数据模型；若复制代码须保留 MIT 版权与许可声明。本场景无需引入其全部能力。

## S03 · linkding 文档 — Archiving

https://linkding.link/archiving/ · 官方文档站，2026-10-17 访问（未固定版本）

仅 latest-plus 镜像支持服务端自动 HTML 快照，通过 singlefile-cli 驱动无头 Chromium 生成单文件 HTML，并尝试加载 uBlock Origin Lite 过滤广告；URL 直指 PDF 时改为下载 PDF 存为附件。文档明确列出代价：镜像显著变大、至少约 1 GB 内存、不支持 ARM v7；无头抓取可能触发反爬、需要登录的站点抓不到登录后内容。也支持从已登录浏览器用 SingleFile 扩展上传快照，已有同 URL 书签则把快照附加到该书签。

文档与代码同仓库，MIT（sissbruecker/linkding）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

参考其对“保存副本”成本与失败模式的说明；本场景不建议实现快照。

## S04 · linkding 文档 — Backups

https://linkding.link/backups/ · 官方文档站，2026-10-17 访问（未固定版本）

全部数据位于数据目录：SQLite 数据库、assets（HTML 快照）、favicons、previews。提供 full_backup CLI 生成包含数据库与各类资源的 zip，并在新实例挂载解压目录恢复；文档警告直接复制 SQLite 文件不具备事务安全性、可能损坏。UI 导出 HTML 的限制被明确写出：不导出用户配置、只导出本人书签、不含 Internet Archive 快照 URL、不含 HTML 快照本体（即使备份 assets 也无法重新关联）、不含图标与预览图。

MIT（sissbruecker/linkding）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

借鉴“UI 导出 ≠ 完整备份”的区分；本场景只需轻量导出，不必实现完整备份体系。

## S05 · linkding 文档 — Search

https://linkding.link/search/ · 官方文档站，2026-10-17 访问（未固定版本）

检索表达式覆盖单词（在标题、描述、备注、URL 中匹配）、引号短语、#标签，以及 and/or/not 布尔组合与括号分组；未写运算符时默认 and；全部大小写不敏感；标签需 # 前缀，开启 lax 模式后可省略。新版检索引擎自 v1.44.0 引入，可回退旧引擎。

MIT（sissbruecker/linkding）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

参考其检索范围（标题/描述/备注/URL/标签）作为最小检索设计；布尔语法对本场景属可选增强。

## S06 · linkding 文档 — Admin

https://linkding.link/admin/ · 官方文档站，2026-10-17 访问（未固定版本）

后台是定制过的 Django admin：可增删用户、改密码、授予 staff 权限；可按用户、归档状态、标签、文本过滤书签并批量删除/归档/取消归档；可批量删除标签或仅删除未使用标签，删除标签只解除关联、不删除书签。部分能力（标签清理等）只在后台提供，主界面没有。

MIT（sissbruecker/linkding）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

仅作为“多用户/运维后台”参照；单用户个人库场景不需要。

## S07 · linkding 文档 — Options（配置项）

https://linkding.link/options/ · 官方文档站，2026-10-17 访问（未固定版本）

默认拒绝从内网主机加载数据（元数据、预览图、PDF 快照），以防用户借实例发起 SSRF 访问内网服务或云元数据端点；可用 LD_ALLOWED_INTERNAL_HOSTS 按主机名/IP/CIDR 放行。可完全关闭 URL 校验以保存非 http/https 或非全限定地址。另有请求体大小上限、请求超时（大文件导入可能超时）、会话 Cookie 有效期（默认 1209600 秒，约两周）、CORS 白名单等。

MIT（sissbruecker/linkding）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

若实现服务端抓取元数据，必须借鉴其 SSRF 与超时/体积限制思路；若只存 URL 不抓取，则风险面显著缩小。

## S08 · Linkwarden — GitHub 仓库 README（linkwarden/linkwarden）

https://github.com/linkwarden/linkwarden · main 分支，2026-10-17 访问（未固定提交）

自托管、开源、面向协作的书签管理器，定位为“收集、阅读、标注并完整保存”。每个链接自动保存截图、PDF、单文件 HTML，可选提交 Wayback Machine；提供阅读视图与高亮标注、按收藏夹/子收藏夹/名称/描述/多标签组织、集合内协作与逐成员权限、公开分享、iOS/Android 原生应用、全文检索与筛选排序、浏览器扩展、Floccus 浏览器同步、SingleFile 上传、SSO（企业/自托管）、API key、批量操作、用户管理、RSS 订阅、图片与 PDF 上传。

AGPL-3.0（仓库 LICENSE.md）

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

只作行为与信息架构参考；AGPL 的网络服务源码义务需法律评估，本任务不复制其代码。

## S09 · Linkwarden 文档 — Overview

https://docs.linkwarden.app/usage/overview · 官方文档站（main 分支文档），2026-10-17 访问（未固定版本）

核心三类数据：Link（即书签/网页/URL）、Collection（可理解为文件夹，可共享给团队或公开）、Tags（附加的关键词分类层）。每个 Link 只能属于一个 Collection，但可有多个 Tag；Collection 可共享协作，Tag 不可共享。每个用户的 Link、Tag、Collection 数量不设上限。

文档仓库 MIT；所述产品为 AGPL-3.0

https://github.com/linkwarden/docs/blob/main/LICENSE

可直接借鉴“单一归属收藏夹 + 多标签”的双层模型；本场景只需前者。

## S10 · Linkwarden 文档 — Links

https://docs.linkwarden.app/usage/links · 官方文档站，2026-10-17 访问（未固定版本）

新增链接时 Address 必填；Collection 名义上必填，但未提供时会落到名为 Unorganized 的收藏夹（首次需要时自动创建）；Description 未填则按网页标题自动生成，Name 在卡片展示时覆盖 Description。记录字段含 URL、Collection、Tags、Name、Description、是否置顶，以及自动生成的截图与 PDF。

文档仓库 MIT；产品 AGPL-3.0

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

“URL 必填 + 缺省落入未整理区 + 标题可自动补全”是本场景应直接采用的最小规则。

## S11 · Linkwarden 文档 — Collections

https://docs.linkwarden.app/usage/collections · 官方文档站，2026-10-17 访问（未固定版本）

每个 Link 恰好属于一个 Collection；Collection 可嵌套、可共享、可公开。未指定收藏夹的链接进入 Unorganized。成员角色分 Viewer（只读）、Contributor（可新增）、Admin（可增删改任意链接并建子收藏夹）；改名、图标、成员管理、公开分享、移动与删除仅属主可做。删除 Collection 会连带删除子收藏夹、其中全部 Link 及保存副本，且不可撤销。公开 Collection 会暴露成员用户名；父收藏夹公开不会连带公开子收藏夹。

文档仓库 MIT；产品 AGPL-3.0

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

借鉴“删除分类的级联后果必须显式提示”；角色模型对本场景不适用。

## S12 · Linkwarden 文档 — Preservation

https://docs.linkwarden.app/usage/preservation · 官方文档站，2026-10-17 访问（未固定版本）

保存副本格式：Readable（正文抽取，供全文检索使用）、Webpage（单文件 HTML）、Screenshot（整页 JPEG）、PDF、Archive.org 快照（不存本地，仅提交地址）。保存后进入队列，由后台 worker 用真实浏览器逐条生成，非即时完成。失败原因包括：服务器以匿名访客访问、登录/付费墙/反爬、页面过慢超时、副本超出体积上限、地址从服务器不可达（含内网）。刷新副本会先删除旧副本再抓取，页面已消失则旧副本也一并丢失。无 Meilisearch 时检索只覆盖名称、地址、描述、标签而不含正文。

文档仓库 MIT；产品 AGPL-3.0

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

作为“保存副本是可选重能力”的证据；本场景应明确不做，以免继承其失败与运维成本。

## S13 · Linkwarden 文档 — Import & Export

https://docs.linkwarden.app/usage/import-and-export · 官方文档站，2026-10-17 访问（未固定版本）

从浏览器导入走标准书签 HTML 格式，兼容 Chrome、Brave、Edge、Firefox、Safari 等；文件夹映射为 Collection、嵌套文件夹映射为子 Collection，未归入文件夹的书签进入名为 Imports 的 Collection；保留原始添加日期，有则保留描述，仅当文件含 TAGS 属性时保留标签。导入不去重：同一文件导入两次会得到两份副本，“阻止重复链接”偏好不适用于导入；文件默认上限 10 MB；导入的链接会排队生成副本。导出的 backup.json 只含元数据（设置、收藏夹、链接、标签、置顶、RSS），不含截图/PDF/页面快照；跨实例导入会把嵌套收藏夹拍平，且往已有数据的账户导入会产生第二套收藏夹而非合并。

文档仓库 MIT；产品 AGPL-3.0

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

直接采用“HTML 作为导入交换格式、文件夹映射为分类”的约定；同时把“导入不去重”“导出不含附件”写入本场景的规则与提示。

## S14 · Linkwarden 文档 — Bulk Actions

https://docs.linkwarden.app/usage/bulk-actions · 官方文档站，2026-10-17 访问（未固定版本）

批量编辑仅在列表视图中开启；全选只覆盖当前已加载的条目，而非匹配查询的全部条目。可批量移动到 Collection（只能选已有集合，不能就地新建）、批量加标签或以新标签替换旧标签、批量重新保存副本、批量删除。批量删除无撤销，且要求对所选全部链接都有删除权限，否则整体失败。重新保存副本需删除权限，且会立即删除旧副本。标签可批量合并（合并后每条相关链接只保留新标签）或删除（仅解除关联，链接保留）。

文档仓库 MIT；产品 AGPL-3.0

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

参考其“全选=当前页”这一常见陷阱，以及“批量删除不可撤销”的确认设计。

## S15 · Linkwarden 文档 — Advanced Search

https://docs.linkwarden.app/usage/advanced-search · 官方文档站，2026-10-17 访问（未固定版本）

高级检索需 Linkwarden Cloud 或自托管 2.10+ 且配置 Meilisearch。支持按 name、url、tag、description、type、collection、public、pinned、before/after 日期检索，用 ! 取反并可组合；结果仍是普通链接列表，可继续套用批量操作。

文档仓库 MIT；产品 AGPL-3.0

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

仅作检索语法参考；本场景用简单关键字 + 分类过滤即可。

## S16 · Karakeep — GitHub 仓库 README（karakeep-app/karakeep，原 Hoarder）

https://github.com/karakeep-app/karakeep · main 分支，2026-10-17 访问（未固定提交）

自托管“收藏一切”应用：可存链接、简单笔记、图片与 PDF，并自动抓取标题/描述/图片；用列表（lists）分组，可多人协作同一列表；提供全文与语义检索、LLM 自动打标签与摘要（可接本地 ollama）、规则引擎、OCR、RSS 自动收集、REST API、批量操作、SSO。归档用 monolith 做整页保存，视频可用 yt-dlp 归档。可从 Chrome、Pocket、Linkwarden、Omnivore、Tab Session Manager 导入，并可用 floccus 与浏览器书签同步。README 自述其定位接近“稍后读 + 网络存档”，并列出与 Linkwarden、Wallabag、Shiori 的差异。

AGPL-3.0（仓库 LICENSE，版权归 Localhost Labs Ltd）

https://github.com/karakeep-app/karakeep/blob/main/LICENSE

证明“收藏一切”会迅速偏离纯书签管理；本场景应刻意收窄范围，不复制其代码。

## S17 · Raindrop.io 帮助中心 — Collections

https://help.raindrop.io/collections · 在线帮助文档，2026-10-17 访问（未固定版本；仅取得搜索结果摘要，正文未抓取）

每个书签只属于一个收藏夹；保存时可选择收藏夹，未选择则默认进入 Unsorted。收藏夹可嵌套。删除收藏夹时其中书签被移入 Trash 而非永久删除；删除父收藏夹会连带删除子收藏夹。

专有 SaaS，非开源代码；未取得代码许可



采用“单归属 + 默认未整理区”模型；不引入其产品。

## S18 · Raindrop.io 帮助中心 — Bookmarks

https://help.raindrop.io/bookmarks · 在线帮助文档，2026-10-17 访问（未固定版本；仅取得搜索结果摘要）

保存入口包括扩展弹窗与移动端分享面板，保存时可挑收藏夹、按需加标签。删除的书签进入 Trash 收藏夹，行为类似普通收藏夹：可浏览、可拖出恢复到任意收藏夹。

专有 SaaS，非开源代码；未取得代码许可



参考“软删除 + 可恢复到指定分类”的恢复路径。

## S19 · Raindrop.io 帮助中心 — Export & backup

https://help.raindrop.io/export · 在线帮助文档，2026-10-17 访问（未固定版本；仅取得搜索结果摘要）

可导出为 HTML、CSV、TXT；既可导出某个收藏夹，也可先选中若干书签再导出。对应地，导入页会先显示识别到的书签、文件夹、标签与高亮数量，供用户确认。

专有 SaaS，非开源代码；未取得代码许可



参考“导出前可选择范围 + 导入前先预览计数”的安全设计。

## S20 · Raindrop.io 帮助中心 — Filters

https://help.raindrop.io/filters · 在线帮助文档，2026-10-17 访问（未固定版本；仅取得搜索结果摘要）

筛选器包括“失效链接”（指向可能已无法访问页面的书签）与“重复项”（同一 URL 被保存多次）；帮助中心说明这两项需要 Pro。另有“无标签”筛选用于找出尚未打标签的书签。

专有 SaaS，非开源代码；未取得代码许可



说明重复与失效检查是成熟产品的付费增值项，属可选而非核心。

## S21 · Raindrop.io 帮助中心 — Limits / 订阅说明

https://help.raindrop.io/limitations · 在线帮助文档，2026-10-17 访问（未固定版本；仅取得搜索结果摘要）

官方称免费版对书签、收藏夹与设备数量不设限；Pro 订阅解锁额外存储、全文检索、页面归档以及重复项/失效链接等工具。

专有 SaaS，非开源代码；未取得代码许可



作为“免费核心 + 付费增强”的定价结构参照；本场景不涉及计费。

## S22 · Raindrop.io 帮助中心 — Tags

https://help.raindrop.io/tags · 在线帮助文档，2026-10-17 访问（未固定版本；仅取得搜索结果摘要）

标签可在保存书签时添加，也可之后随时编辑补充；输入时以逗号分隔多个标签。

专有 SaaS，非开源代码；未取得代码许可



若后续需要跨分类检索，可把标签作为二级维度；首版可不做。

## S23 · Google Chrome 帮助 — 导入/导出书签

https://support.google.com/chrome/answer/96816 · 在线帮助文档，2026-10-17 访问（未固定版本；仅取得搜索结果摘要）

Chrome 书签管理器可将书签导出为 HTML 文件，也可通过“整理 → 从 HTML 文件导入书签”把 HTML 文件导入；该 HTML 文件可用于导入到其他浏览器或工具。

专有软件与官方帮助文档，非开源代码



确认 Netscape 风格 HTML 是事实上的交换格式；本场景应支持导出/导入该格式或等价的简单 JSON。

## 待验证

- input.json 中不存在 research_date 字段，访问日期统一采用会话日期 2026-10-17；若需其他日期标签请以任务数据为准。
- Pinboard 官方 FAQ 与定价页多次抓取失败，未验证其标签制、默认隐私、归档层级与价格，故未列入来源，也未在结论中断言其行为。
- Raindrop.io 帮助中心正文页抓取被拒绝，仅能引用搜索结果摘要；具体 Pro 价格、Trash 保留期限、收藏夹数量上限与全文检索范围未核实。
- support.google.com 正文未抓取，Chrome 的导出/导入流程仅依据搜索摘要，未验证其书签检索、撤销与回收站能力细节。
- Linkwarden 文档站正文通过其 GitHub 文档仓库获取；未核对文档所述行为与具体发行版本号的一一对应关系。
- 未验证 Netscape 书签 HTML 的正式规范来源（该格式无权威标准文本），仅以多产品导入导出实现作为事实约定。
- 未做许可证法律审查；AGPL-3.0 的网络服务义务是否适用于特定部署形态未由法律顾问确认。
- 未验证大规模导入（数千至上万条）时的超时、去重与导出完整性，仅有文档层面的上限与警告。
- 未评估移动端分享入口、浏览器扩展在当前浏览器商店政策下的可用性与审核要求。
- 未进行可用性测试或用户研究；关于“简单分类优于标签”的建议属基于文档的设计判断，非实测结论。
