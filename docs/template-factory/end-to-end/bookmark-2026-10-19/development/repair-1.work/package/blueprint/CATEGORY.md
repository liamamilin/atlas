# 品类认知与来源

固定的模型调研记录；来源访问日期与 Atlas 叶子原稿编写日期含义不同。叶子原稿的研究笔记链接属于原语料上下文，不表示本包附带该文件；本包来源以以下条目及未知项为准。

本报告区分“大类事实”（来自官方文档佐证）与“本场景特定建议”，并对权限、计费、管理、审计、导出与恢复逐项做适用性评估而非一律要求。

一类、被官方文档佐证的大类事实：
1) 记录是“指向”而非“持有”：Linkwarden 明确直说原因——只存地址等于赌页面还在，故另存多格式副本；Raindrop 与 Pinboard 的存档/失效链接/网页归档页同样把原内容放在应用之外。这印证叶子“记录指向、内容归 Web 所有”。
2) 主动捕获 + 持久累积库 + 用户可控组织/检索：Raindrop（collection/tag/收件箱 Unsorted/搜索匹配 title/description/URL/tags/notes）、linkding（标签+批量编辑+搜索）、Linkwarden（一链接一 collection + 多 tag）、Pinboard（标签+组合过滤）一致。
3) 组织形态是实现选择：Raindrop 用“collection 为主、一书签一 collection + 多 tag”，Linkwarden 同构（含默认 Unorganized），linkding/Pinboard 以标签为主、Pinboard 另有 bundles（标签分组）。叶子“形式不属定义”得到支持。
4) 成熟产品的常见增强（非定义）：自动元数据（linkding/Raindrop/Linkwarden）、去重（Raindrop Duplicate finder，属 Pro）、失效链接（Raindrop broken links）、内容存档（Raindrop web archive、linkding latest-plus、Linkwarden 多格式、Pinboard archive）、多设备/多浏览器、导入导出互操作、私有优先与可选分享、read-later（linkding unread、Linkwarden reader）。
5) 互操作约定：Netscape HTML 书签格式。linkding 明言以其导入导出；Raindrop 导出 HTML 即该格式且称“任何浏览器或书签管理器均可导入”；Linkwarden 从浏览器 HTML 导入并把文件夹映射为 collection、保留日期与 TAGS。这是本类目事实上的交换标准。

二类、按场景（生活待购与灵感收藏夹：单用户、简单归类、保存-检索-回跳）的取舍：
- 必做（直接对应验收）：以 URL 为锚的记录且打开即跳原页；主动保存（一键/表单/粘贴 URL）；持久化存储；简单归类（等价于“collection/文件夹”）的创建与移动，并在重开后保持；默认收件箱承接未整理项；按归类浏览 + 关键字检索；从记录打开原网页。
- 建议低成本纳入：删除的“回收站/可恢复”区（Raindrop 把删除项移入 Trash 并可拖出恢复，成本低、体验稳）；以 Netscape HTML 做导入/导出，既为一键迁移也为轻量备份（linkding/Raindrop/Linkwarden 均以此为互操作基线）。
- 可选/延后（成熟产品有、但本场景非必需）：网页存档、失效链接检测、重复检测、全文搜索、协作与权限、标注/阅读器、AI 归类、云备份、大文件上传。若做，应参照其真实约束：存档需 headless 浏览器与异步队列、内存与磁盘成本高，且登录/付费墙页面会保存成登录墙（Linkwarden/linkding/Pinboard 均有此局限）；全文搜索需额外搜索引擎（Linkwarden 依赖 Meilisearch）。

三类、权限/计费/管理/审计/导出与恢复的适用性评估：
- 权限：Linkwarden 有 Admin/Viewer/Contributor 角色、标注私有、collection 可分享而 tag 不可分享；linkding 支持多用户与向访客分享、OIDC/认证代理。本场景为单用户私人库，权限体系适用性低，唯一应默认的是“私有优先”（Pinboard 可默认全私有）。
- 计费：Raindrop Free（无限书签/collection/tag/设备）vs Pro 年付 US$28（全文搜索、存档、去重/失效链接、每日备份等）；Pinboard archive US$39/年。结论：核心保存-检索在成熟产品中普遍免费，付费点集中在存档/全文搜索/备份等增强；本场景无需照搬付费分层。
- 管理/审计：linkding 提供 Django admin 做用户与批量书签/标签管理、批量删除/归档，并记录 SSRF 拦截为警告；Linkwarden 有 Bulk Actions。此类企业取向能力对本场景适用性低，可省略；但 linkding 的 URL 校验与 SSRF 防护（默认拒绝加载内网主机）对任何“由服务端抓取 URL 元数据”的实现都值得在早期即考虑，属安全而非企业特性。
- 导出与恢复：Raindrop 全账户/单 collection/选中项导出 HTML/CSV/TXT，自动每日备份需 Pro；Linkwarden 导出 backup.json 仅元数据、不含已保存副本、不算完整实例备份、且导入不参与去重；Pinboard 可请求归档备份；linkding 以 Netscape HTML 导入导出。建议自建时把“导出为 Netscape HTML”+“内部可恢复删除”作为最低恢复基线，并明确“导出不含存档副本”。

四类、复用 vs 自建：
- 复用：linkding 为 MIT，宽松可参考/再分发；Linkwarden 为 AGPL-3.0，属网络 copyleft，基于其代码对外提供网络服务需向用户提供源码，若目标为闭源产品应谨慎；Raindrop、Pinboard 为专有 SaaS，无开源许可证，只能借鉴概念与交互，不能复制代码。
- 自建：鉴于叶子核心很小（URL 记录 + 归类 + 检索），且本场景仅需该核心子集，自建核心并用 Netscape HTML 保证可迁移，成本最低且契合验收；把存档、去重、失效检测等重量级能力列为可选，避免为“企业特性”付出不必要的复杂度与成本。
- 不确定性：上述许可结论均基于仓库 LICENSE 文本（linkding MIT、Linkwarden AGPL-3.0），但“是否可将某组件用于本项目”的最终判断需法务确认；本报告为模型报告来源证据，非独立运行时或法律核验。

五类、未知与弱证据：Raindrop 重复/失效链接的判定算法、Pinboard 当前运营与价格、Chrome 内置书签的完整正文、Delicious 的完整历史归属，均未从完整官方正文取得，已在 gaps 标注。

## S01 · Atlas confirmed input

inputs/scenario.json · scn_7756e0007f6a463a97316f3f49c15248@2

把偶然看到但当下不处理的外部网页链接留存，日后需要时能重新找到并回到原页面

Atlas scenario input; not a third-party code license



Pinned requirement input

## S02 · Raindrop.io Help Center — Bookmarks

https://help.raindrop.io/bookmarks · access date 2026-10-19（在线文档，未固定版本）

书签是产品核心对象，保存时选择 collection、可加 tag 与笔记并保存；一个书签只属于一个 collection；删除的书签移入 Trash collection，可像普通 collection 一样浏览，并通过拖出（或移到任意 collection）来恢复。

专有 SaaS，非代码；未提供开源许可证



build（仅借鉴概念约定，复用其交互约定而非代码）

## S03 · Raindrop.io Help Center — Collections

https://help.raindrop.io/collections · access date 2026-10-19（在线文档，未固定版本）

collection 类似文件夹用于分组；未选择 collection 就保存的书签落入内置收件箱 Unsorted，供日后整理；每个 collection 有独立图标与布局设置。

专有 SaaS，非代码；未提供开源许可证



build（采用“默认收件箱”概念；本场景验收要求含默认归类）

## S04 · Raindrop.io Help Center — Export & backup

https://help.raindrop.io/export · access date 2026-10-19（在线文档，未固定版本）

可导出整账户、单个 collection 或选中项，格式为 HTML、CSV、TXT；HTML 即浏览器书签通用的 Netscape 格式，任何浏览器或书签管理器均可导入；自动每日备份（云目的地如 Dropbox、Google Drive，另有 OneDrive 提及）需 Pro 订阅；导出与备份在网页端执行。

专有 SaaS，非代码；未提供开源许可证



reuse（采用 Netscape HTML 作为互操作导出格式）；备份/云同步为可选

## S05 · Raindrop.io Help Center — Limits（计划对比）

https://help.raindrop.io/limitations · access date 2026-10-19（在线文档，未固定版本）

免费版书签、collection、tag、每个 collection 的协作者数与同步设备数均无限；免费与 Pro 的差异集中在：文件上传 100MB/月 vs 10GB/月、单文件 100MB vs 300MB、提醒、标注、重复查找器（Duplicate finder）、自动备份；Pro 才含 Duplicate finder 与 Automatic backups。

专有 SaaS，非代码；未提供开源许可证



build（按场景取舍付费点：本场景不需要标注/提醒/大文件上传，重复与备份可自建为轻量能力）

## S06 · Raindrop.io — Pricing

https://raindrop.io/pro/buy · access date 2026-10-19（页面显示 Pro 年付 US$28；价格易变）

官方定价页：Free 版无限书签/collection/highlights/设备、导入导出、跨平台应用、可分享协作、100MB/月文件上传；Pro 年付 US$28，增加 AI 助手、全文搜索、Web archive（网页存档）、提醒、标注、Duplicate and broken links finder、每日备份、10GB/月上传。

专有 SaaS，非代码；未提供开源许可证



build（作为可选增值层参照；核心库功能免费，存档/全文搜索/去重等为本场景的非必需增强）

## S07 · Raindrop.io Help Center — Duplicates

https://help.raindrop.io/duplicates · access date 2026-10-19（在线文档，未固定版本；页面正文多半未取回）

Raindrop.io 可检测重复书签并在单一列表展示以便清理；Filters 页的 Library health 将 Duplicates 定义为“同一 URL 被保存多次”。（具体判定算法与是否自动合并未从完整正文核验。）

专有 SaaS，非代码；未提供开源许可证



build（库卫生为成熟产品的可选能力，非本场景定义性需求）

## S08 · Raindrop.io Help Center — Broken links

https://help.raindrop.io/broken-links · access date 2026-10-19（在线文档，未固定版本；正文受搜索摘要限制）

提供失效链接（broken links）清单能力；该页 FAQ 明确 Raindrop.io 会自动为每个书签保存 web archive 副本。（检测机制细节未从完整正文核验。）

专有 SaaS，非代码；未提供开源许可证



build（失效链接为“内容在应用之外”带来的结构性维护事项，可延后实现）

## S09 · Raindrop.io Help Center — Web archive（永久副本）

https://help.raindrop.io/web-archive · access date 2026-10-19（在线文档，未固定版本）

自动保存每个网页的副本；失败的页面会自动重试；可下载副本到本地并手动分享；据 Web 端变更日志（2025-05-19），对失效或离线的链接也使用 Wayback Machine 生成永久副本。

专有 SaaS，非代码；未提供开源许可证



build/optional（内容保存在原站之外，是否存档属可选增强，非书签管理器定义）

## S10 · linkding — 官方文档站（产品与功能）

https://linkding.link/ · access date 2026-10-19（在线文档，未固定版本）

自托管书签管理器，定位最小、快速、易部署；功能：标签组织、可开关的自定义、自动抓取标题/描述/图标/预览图、归档（本地 HTML 快照或 Internet Archive）、批量编辑、Netscape HTML 格式导入导出、多用户并可向他人或访客分享、Firefox/Chrome 扩展、REST API、单 Docker 容器 + SQLite 低维护。

开源（MIT，见其 GitHub 仓库）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

reuse（MIT 宽松许可，可借鉴其最小实现与导入导出契约；本任务不复制代码）

## S11 · linkding — Archiving 文档

https://linkding.link/archiving/ · access date 2026-10-19（在线文档，未固定版本）

服务器端归档仅在 latest-plus 镜像提供，用 singlefile-cli（headless Chromium）生成单 HTML 快照并加载 uBlock Origin Lite；直接指向 PDF 的 URL 会下载 PDF 存为资产；缺点：镜像显著变大、需约 1GB 内存、不支持 ARM v7、可能触发反爬、登录页内容不完整。替代路径：用 SingleFile 扩展上传到 /api/bookmarks/singlefile/，或 linkding 扩展“添加书签后运行 SingleFile”。

开源（MIT）；归档依赖 third-party 工具（singlefile-cli、Chromium），其各自许可未在本任务核验

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

build/optional（存档有实际资源与可靠性代价，适合作为可选层）

## S12 · linkding — REST API 文档

https://linkding.link/api/ · access date 2026-10-19（在线文档，未固定版本）

API 以 per-user token 认证；书签 CRUD、check 端点检查 URL 是否已保存并返回现有书签与抓取的 metadata 及 auto_tags；创建时若 URL 已存在会“静默更新现有书签而非新建”（文档提示未来可能改为报错）；分发时可按 modified_since/added_since 过滤；含 archived（归档）书签端点、assets（快照/上传）、bundles。

开源（MIT）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

build（“同 URL 一条记录”的收敛策略与 check 端点是可借鉴的契约设计）

## S13 · linkding — Options 文档（安全与运行选项）

https://linkding.link/options/ · access date 2026-10-19（在线文档，未固定版本）

默认拒绝加载指向内网主机的 URL 数据以防护 SSRF，可通过 LD_ALLOWED_INTERNAL_HOSTS 配置白名单或 * 关闭；LD_DISABLE_URL_VALIDATION 可禁用 URL 校验以存非 http(s) 或非全限定地址；支持 LD_ENABLE_OIDC（OIDC/SSO）与 LD_ENABLE_AUTH_PROXY（认证代理，会自动建用户）；数据库可选 SQLite（默认）或 PostgreSQL。

开源（MIT）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

build（单用户自托管可关闭这些企业向能力；但 URL 校验/SSRF 防护对任何抓取元数据的产品都值得早期考虑）

## S14 · linkding — Auto tagging 文档

https://linkding.link/auto-tagging/ · access date 2026-10-19（在线文档，未固定版本）

按 URL 模式（hostname/path/query/fragment）自动打标签；规则在创建或更新书签时应用；不匹配网站内容，不支持通配符；网页表单与浏览器扩展会预览将要添加的标签。

开源（MIT）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

build/optional（自动归类为可选增强，本场景用户手动选简单归类）

## S15 · linkding — Admin 文档

https://linkding.link/admin/ · access date 2026-10-19（在线文档，未固定版本）

内置 Django admin，含 linkding 定制；提供 UI 之外的能力：用户管理/自助、书签与标签管理（含批量操作）；批量书签动作有 Delete/Archive/Unarchive；标签可批量删除或删除未使用标签，删除标签不影响书签本身。

开源（MIT）

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

build（管理面/审计能力在本单用户场景中适用性低，可省略）

## S16 · linkding — GitHub 仓库（自述与许可证）

https://github.com/sissbruecker/linkding · master 分支，access date 2026-10-19（未固定分支；约 11.3k stars）

官方仓库确认：自托管、Docker 部署；功能含标签组织、批量编辑、Markdown 笔记、read-it-later、与他用户/访客分享、自动获取标题描述图标、归档、Netscape HTML 导入导出、PWA、Firefox/Chrome 扩展与 bookmarklet、OIDC/认证代理 SSO、REST API、admin 面板。仓库标注 MIT license。

MIT License，Copyright (c) 2019 Sascha Ißbrücker

https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt

reuse（MIT：宽松，可参考实现与再分发；本任务仅研究、不复制代码）

## S17 · Linkwarden — 官方文档 Welcome

https://docs.linkwarden.app/ · access date 2026-10-19（在线文档，未固定版本）

自托管、开源的协作式书签管理器：收集、阅读、标注并“完整保存”网页；明确以网页可能消失（link rot）为由为每个书签保存多格式副本；兼具 read-it-later 体验与 web archive 可靠性；面向协作，支持公开分享与多用户。

开源（AGPL-3.0，见其 GitHub LICENSE.md）

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

谨慎 reuse（AGPL-3.0 属 copyleft，网络服务修改后须向用户提供源码；如用于闭源产品需评估合规）

## S18 · Linkwarden — Preservation 文档

https://docs.linkwarden.app/usage/preservation · access date 2026-10-19（在线文档，未固定版本）

保存链接进入队列，后台 worker 用真实浏览器异步生成多种格式；格式含 Readable（正文）、Webpage（单文件 HTML，Monolith）、Screenshot（整页 JPEG）、PDF，以及提交给 Wayback Machine 的 Archive.org 快照（不由 Linkwarden 存储）；除 Archive.org 外新账户默认全开，可按全局或按 Tag 配置；刷新会先删除现有副本再从实时页面重新保存（页面已消失则失去旧副本）；每链接有超时与大小上限，生成失败标记为不可用；副本按 collection 存于磁盘或 S3，删除链接/collection 会连带删除文件；正文提取文本用于全文搜索（需 Meilisearch，自托管未必具备）。

开源（AGPL-3.0）

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

build/optional（内容存档是重量级可选能力，与书签“指向而非持有内容”的核心相反）

## S19 · Linkwarden — Import & Export 文档

https://docs.linkwarden.app/usage/import-and-export · access date 2026-10-19（在线文档，未固定版本）

导入不参与去重，同一文件重复导入会产生两份；导入的链接会进入归档队列；从浏览器 HTML 文件导入时：文件夹变为 collection、嵌套文件夹变为子 collection、无文件夹的书签进入名为 Imports 的 collection、保留原始添加日期、有 TAGS 属性时保留标签；导出为 backup.json，仅含元数据（账户设置、collections、links、tags、置顶链接、RSS 订阅），不含已保存的截图/PDF/快照，不能作为实例的完整备份；导入文件默认上限 10MB（IMPORT_LIMIT）。

开源（AGPL-3.0）

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

reuse（其“导入不去重”“导出仅元数据”的取舍值得作为自建时的边界提示）

## S20 · Linkwarden — Read and Annotate 文档（权限说明）

https://docs.linkwarden.app/usage/read-and-annotate · access date 2026-10-19（在线文档，未固定版本）

高亮与笔记对每个用户私有，共享 collection 中各成员独立标注彼此不可见；标注需要 collection 上的 Admin 角色或拥有权；Viewer/Contributor 可阅读但不能标注；公开 collection 的访客可读 Readable 但不能标注；删除链接会删除其标注。

开源（AGPL-3.0）

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

build（角色/权限属协作向能力，本单用户场景适用性低）

## S21 · Linkwarden — Links 文档（数据模型）

https://docs.linkwarden.app/usage/links · access date 2026-10-19（在线文档，未固定版本）

每个链接的数据：Address(URL) 必填、Collection 必填(默认 Unorganized)、Tags 可选、Name 可选、Description 可选(默认自动生成)、Is Pinned 可选、Screenshot/PDF 自动生成；一个链接只属一个 collection 但可有多个 tag；collection 可分享协作、tag 不可分享；Overview 说明每个用户的链接/标签/collection 数量不限。

开源（AGPL-3.0）

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

build（“一条记录=URL+一个主归类+多标签”与场景的“简单归类”高度吻合）

## S22 · Linkwarden — GitHub LICENSE.md

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md · main 分支 raw 文件，access date 2026-10-19（未固定分支）

文件正文为 GNU Affero General Public License Version 3（2007-11-19 文本，含第 13 条远程网络交互条款），标题为 AGPL v3 应用模板。

GNU AGPL-3.0

https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md

谨慎 reuse（copyleft：若基于其代码提供网络服务需向用户提供对应源码）

## S23 · Pinboard — 官方 FAQ

https://pinboard.in/faq/ · access date 2026-10-19（在线文档，未固定版本；价格与服务状态可能变动）

定位为“你见过的东西的互联网搜索引擎”——个人链接存档，可从任意电脑保存与搜索；archive 为付费功能，下载并存每个书签的本地副本并在原站下线/变更后仍可用，同时开启对书签页面全文的全文搜索；archive 价格 US$39/年（多年有折扣），7 天退款；每链接 32MB 大小上限；每链接只爬取一次，可手动 re-crawl；导入会保留标签与创建时间、隐私等元数据；标签最长 255 字符、不可含空白/逗号、不区分大小写；可用最多 4 个标签组合过滤；付费用户可请求下载归档备份（每书签一个文件夹+顶层 manifest HTML）。

专有 SaaS，非代码；未提供开源许可证



build（付费存档层与全文搜索是可选增值；单用户场景可省略）

## S24 · Pinboard — 官方 howto 页

https://pinboard.in/howto/ · access date 2026-10-19（在线文档，未固定版本）

书签可设为 public 或 private，仅自己可见 private；可将全部书签默认设为 private；以点号(.)开头的标签为私有标签；标签是主要组织方式，可按录入顺序或字母顺序显示，标签云约显示最常用的 200 个；Bundles 是“标签的命名集合”，用于把大量标签按类别分组，默认公开（点号前缀可私有）；导入会保留标签，原为私有的仍保持私有。

专有 SaaS，非代码；未提供开源许可证



build（私有优先与“标签分组”概念可借鉴；默认隐私符合叶子“private by default”规则）

## S25 · Pinboard — API v2 DRAFT 文档

https://idlewords.com/pinboard_api2_draft.htm · 草稿文档（DRAFT），access date 2026-10-19

草稿 API：书签含 archived 端点用于取回缓存副本 URL，仅归档用户可用；POST 请求重新爬取会覆盖原副本；标签为不含空白、大小写不敏感的自由标识；提供标签列表、批量改名与删除等端点；bundles 返回用户标签分组。

专有 SaaS 的 API 文档，非代码；未提供开源许可证



uncertainty（草稿接口易变；仅作参考，不依赖其契约）

## S26 · Delicious（社交书签历史）— Wikipedia 条目

https://en.wikipedia.org/wiki/Delicious_(website) · 条目版本 2026-09-22（access date 2026-10-19；百科非官方一手来源）

Delicious（del.icio.us）是成立于 2003 年的社交书签 Web 服务，用于存储、分享与发现网页书签，以标签为核心、早期公共可见并带社交/发现属性；后被 Yahoo 等收购（历史归属与关停细节未逐条核验）。

非代码（百科条目；Wikipedia 文本许可未在本任务核验版本）



build（作为“标签型社交书签”历史变体的旁证，佐证核心可脱离现代存档/协作能力而成立）

## S27 · Google Chrome 帮助 — 创建、查找与编辑书签（内置书签管理器）

https://support.google.com/chrome/answer/188842 · access date 2026-10-19（仅经搜索摘要，未取回完整正文）

Chrome 内置书签管理器：可添加/编辑书签与文件夹；导出会把书签写成 HTML 文件，可再导入到另一浏览器或新设备（导出/导入路径见配套帮助页 support.google.com/chrome/answer/96816）。仅凭搜索摘要，未核验完整正文细节。

专有产品文档，非代码；未提供开源许可证



build（浏览器内置形式与独立产品“同核不同范围”的对照旁证；作为叶子概念论断的弱证据）

## 待验证

- Chrome/Mozilla 等浏览器厂商的完整官方书签文档未取回（仅得搜索结果摘要），关于“浏览器内置书签”的陈述停留在概念层，未核验导出/导入步骤与去重行为细节。
- Raindrop.io 的 Duplicates 与 Broken links 帮助页正文多半未取回（受搜索摘要限制），重复判定算法、是否自动合并、失效链接检测机制均未核验。
- Raindrop.io Web archive 的具体限制（副本保留期、存储配额、失败重试上限）未从完整正文核验；仅确认“失败会自动重试”“可用 Wayback Machine 生成永久副本”。
- Raindrop.io 自动每日备份的还原点数量（如“30 个”）与 OneDrive 目的地来自第三方博客/论坛摘要，未在官方帮助正文中逐一确认，故正文未采信。
- Pinboard 的当前运营状态、实际价格与功能（如 archive US$39/年、32MB 上限）来自其官方 FAQ/howto 页面，但该页为长期静态文本、可能已过时；未从独立来源核验其现况。Delicious 的成立、收购与关停细节仅来自 Wikipedia 条目，未以一手官方来源核验。
- linkding 未固定版本号（文档与授权文件取自 master 分支，access date 2026-10-19）；linkding 是否提供“回收站/可恢复删除”未在本次所核验文档中确认，视为未知。
- linkding 归档依赖的 third-party 组件（singlefile-cli、Chromium、uBlock Origin Lite）各自许可证未在本任务核验；其“开源（MIT）”仅指 linkding 主仓库。
- Linkwarden 文档取自 main 分支在线站（access date 2026-10-19，未固定版本）；其存档资源的存储上限、超时、批大小等具体数值以环境变量配置，本报告未逐一取值核验。
- Netscape 书签 HTML 格式的正式规范来源未定位到权威标准文档；本报告仅依据 linkding 与 Raindrop 官方文档对其作为互操作格式的表述，未核验字段级规范与浏览器兼容边界。
- 各类产品的价格、免费额度与功能分层随版本变动，本报告仅在标注的访问日（2026-10-19）成立；本报告为模型报告的来源证据，非独立运行时验证，亦非法律意见。
