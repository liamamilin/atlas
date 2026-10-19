# 品类认知与来源

固定的模型调研记录；来源访问日期与 Atlas 叶子原稿编写日期含义不同。叶子原稿的研究笔记链接属于原语料上下文，不表示本包附带该文件；本包来源以以下条目及未知项为准。

The pinned upstream tree at commit 539881b (github.com/lakhindarpal/bookmark-manager, materialized under source/) is a client-only bookmark manager built with Ripple TS, Vite, Tailwind/DaisyUI, Valibot, and Dexie/IndexedDB. A single Bookmark record type carries id, title, url, hostname, favicon Blob, description, flat tags[], isPinned, isArchived, visitCount, createdAt, visitedAt (source/src/includes/store.ts:3-16). The DB 'BookmarkDB' v1 has one table 'bookmarks' keyed by id with createdAt and visitCount indexes (source/src/includes/store.ts:41-47). The single component App.tsrx implements: an add/edit dialog with Valibot validation (URL http/https, title, description, 1-5 tags), a library grid with Home/Archived tabs, tag-filter sidebar with per-tag counts, title-only search, three sort modes with pinned-first, Visit (increments visitCount/visitedAt then window.open), Copy URL, Pin/Unpin, Edit, Archive/Unarchive, and a Delete action available only on archived items with a 5-second Undo toast. Metadata/favicons are fetched opportunistically from third-party services (api.microlink.io, images.weserv.nl, Google favicon) behind a 'sparkles' button and a fallback path, with failures only console.error'd. No test files, no import/export, no collections/folders, no sync, no preserved page copies, and no test script exist in the supplied manifest.

## S01 · Atlas confirmed input

inputs/scenario.json · scn_7756e0007f6a463a97316f3f49c15248@2

把偶然看到但当下不处理的外部网页链接留存，日后需要时能重新找到并回到原页面

Atlas scenario input; not a third-party code license



Pinned requirement input

## S02 · ev_ba200adf6e2c_05babdea64ba9858

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

New records are built with id `bm-${crypto.randomUUID()}`, hostname from getHostname(url), and defaults visitCount=0, visitedAt=null, isPinned=false, isArchived=false, createdAt=Date.now(); edits preserve the previous id, isPinned, isArchived, visitCount, createdAt, and visitedAt.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S03 · ev_ba200adf6e2c_06c81a165e03c96a

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

Pin/Unpin and Edit actions are rendered only when the item is not archived, and Edit loads the item's url/title/description/tags/favicon into the dialog.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S04 · ev_ba200adf6e2c_1596da4a90687ca5

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

The Valibot BookmarkFormSchema requires a non-empty URL matching /^https?:\/\/(?:[\w-]+\.)+[a-zA-Z]{2,}(?:\/\S*)?$/ and v.url, a non-empty title up to 100 chars, a non-empty description up to 280 chars, and 1-5 tags each up to 30 chars.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S05 · ev_ba200adf6e2c_2288b28e90cd8450

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

Tab, tag filters, sort, and search are held in component-local tracked state initialized to 'Home', [], 'Recently Added', and '' respectively, with no persistence to Dexie.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S06 · ev_ba200adf6e2c_35e41aab676021eb

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

saveBookmark sets the record in the in-memory map then awaits db.bookmarks.put(bm); deleteBookmark removes from the map then awaits db.bookmarks.delete(id).

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S07 · ev_ba200adf6e2c_4c56ef30a1785be1

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

A Delete action is rendered only for archived items; it calls deleteBookmark and shows an error-type toast with an Undo action that calls saveBookmark(item) to restore the record.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S08 · ev_ba200adf6e2c_5011700a24e503c7

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/includes/utils.ts · 539881bc67099d491e8ab6f85de0f443fa7de623

getHostname returns '' unless the URL matches an http/https regex with a dotted domain, otherwise returns new URL(url).hostname; getBlobUrl caches object URLs per Blob in a WeakMap; formatDate returns 'Never' for falsy timestamps else a locale date string.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S09 · ev_ba200adf6e2c_515aa5d072bd2ec4

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/includes/store.ts · 539881bc67099d491e8ab6f85de0f443fa7de623

A Dexie database named 'BookmarkDB' version 1 declares a single 'bookmarks' EntityTable keyed by id and indexed on createdAt and visitCount.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S10 · ev_ba200adf6e2c_5d51c18a989c01f8

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/index.html · 539881bc67099d491e8ab6f85de0f443fa7de623

index.html defines the #root div and loads /src/index.ts as a module for the Bookmark Manager SPA.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S11 · ev_ba200adf6e2c_6805376f7e2ee383

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/README.md · 539881bc67099d491e8ab6f85de0f443fa7de623

README describes the app as local-first with bookmarks stored in IndexedDB and featuring tagging, sorting by recently added/visited/most visited, and archiving/pinning.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S12 · ev_ba200adf6e2c_7150b0ac7a5678db

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

A Copy URL action writes item.url to the clipboard and shows a success toast.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S13 · ev_ba200adf6e2c_86ed2327f33a3ca8

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

An effect on component creation calls db.bookmarks.toArray() and inserts each returned bookmark into an in-memory RippleMap keyed by bookmark id.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S14 · ev_ba200adf6e2c_8e11efc61a4650ba

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

On submit, if no favicon exists and a hostname is derivable, the code fetches a Google s2 favicon proxied through images.weserv.nl inside a try/catch that only logs failure.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S15 · ev_ba200adf6e2c_93ff254508846f11

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

The Visit action builds an updated bookmark with visitedAt=Date.now() and visitCount+1, calls saveBookmark(updated), then opens the URL with window.open(item.url, '_blank', 'noopener,noreferrer').

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S16 · ev_ba200adf6e2c_9ab6b0e51811a16d

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

The displayed list filters by isArchived matching the active tab, requires every selected tag to be present in bookmark.tags, matches search only against bookmark.title.toLowerCase(), and sorts pinned-first then by the chosen sort mode with createdAt descending as fallback.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S17 · ev_ba200adf6e2c_9c7f6060878383fa

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/includes/store.ts · 539881bc67099d491e8ab6f85de0f443fa7de623

The Bookmark type stores id, title, url, hostname, favicon Blob, description, tags string array, isPinned, isArchived, visitCount, createdAt, and visitedAt.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S18 · ev_ba200adf6e2c_a2ebc864c5b6b3e7

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/index.ts · 539881bc67099d491e8ab6f85de0f443fa7de623

The entry point imports index.css, mounts the App component into #root via ripple's mount, and throws if the root element is missing.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S19 · ev_ba200adf6e2c_b1ca64cf2ad02998

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

The Archive/Unarchive action toggles isArchived and, when archiving, forces isPinned=false before saving.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S20 · ev_ba200adf6e2c_c4ad7e52e5713628

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

Tag counts are derived by iterating all in-memory bookmarks and counting each tag occurrence, then sorted alphabetically for the sidebar.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S21 · ev_ba200adf6e2c_ec303a2fd1afa287

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

fetchMeta calls https://api.microlink.io/?url=... and, on success with result.data, sets title/description and fetches the logo through https://images.weserv.nl/; errors are only console.error'd and the finally block resets loading.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## S22 · ev_ba200adf6e2c_f30eb4285ca66219

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/package.json · 539881bc67099d491e8ab6f85de0f443fa7de623

package.json scripts are start, dev, build, lint, typecheck, serve, format, and check; there is no test script and no test dependency.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Reviewed code observation; design adaptation is recorded separately; upstream not run.

## 待验证

- Runtime behavior was not observed; all claims are static reading of source files.
- Whether Dexie/IndexedDB persistence behaves correctly in real browsers at this commit is unverified.
- Whether the third-party metadata/favicon endpoints (api.microlink.io, images.weserv.nl, Google s2 favicons) are reachable, rate-limited, or CORS-permitted at runtime is unverified.
- The paired Research Notes referenced by leaf.md were not supplied, so product-level evidence beyond the pinned repository is unavailable.
- No automated tests exist in the manifest, so none of the described behaviors are test-confirmed.
- Behavior of Ripple TS reactivity primitives (track/effect/bindGroup/bindValue) at this pinned version was not validated.
- The full commit tree was inferred from the supplied source_manifest and the on-disk source/ directory; files outside it were not inspected.
- Host excluded unsupported evidence obs-no-test-files: observation cites an unknown source path: source/src
- Host excluded unsupported evidence inf-no-tests: Depends on a quarantined, unlocated observation


## 固定案例依据与设计取舍 / Fixed case basis and design

案例依据来自共享规范记录，完整版本见 inputs/case-basis.json。源码定位与独立审阅不代表上游运行通过。

[
  {
    "capability": "个人收藏库本地持久化：整个收藏集合写入浏览器 IndexedDB 单表，应用每次打开时全量载入，保存或删除立即落盘，关闭再打开后仍在。",
    "disposition": "adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_515aa5d072bd2ec4",
      "ev_ba200adf6e2c_35e41aab676021eb",
      "ev_ba200adf6e2c_86ed2327f33a3ca8",
      "ev_ba200adf6e2c_6805376f7e2ee383"
    ],
    "reason": "场景验收第1条要求“主动保存的链接在多次会话之间持久保留，形成不断增长的个人收藏”，上游 Dexie 单表 + 内存映射 + put/delete 落盘已直接满足，README 也定位为 local-first。差异仅在于记录结构增加归类字段，持久化机制原样沿用。"
  },
  {
    "capability": "记录以外部网页 URL 锚定：每条收藏持有 id、url、hostname（及可选标题/图标），点击记录在新标签打开原始网页。",
    "disposition": "adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_9c7f6060878383fa",
      "ev_ba200adf6e2c_93ff254508846f11",
      "ev_ba200adf6e2c_5011700a24e503c7"
    ],
    "reason": "场景验收第2条与流程第5步要求“打开记录即跳转到该页面，回到原始网页继续购买、阅读或参考”。上游 Visit 正是保存后以 window.open(noopener,noreferrer) 打开，hostname 由 URL 派生。差异是场景不需要访问计数与 visitedAt，只保留打开动作与域名派生。"
  },
  {
    "capability": "新增/编辑收藏的表单：填写 URL 与标题，URL 必须为合法 http/https 且含点域名，编辑时回填原字段并保留 id 与创建时间。",
    "disposition": "adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_05babdea64ba9858",
      "ev_ba200adf6e2c_06c81a165e03c96a",
      "ev_ba200adf6e2c_1596da4a90687ca5"
    ],
    "reason": "场景流程第1-2步是“浏览中看到想记住的页面便主动保存”，需要可信录入与校验。上游 Valibot 表单校验、编辑回填并保留 id/createdAt 的行为可复用；差异是把“1-5 个标签必填”改为“选择或新建一个归类”，描述字段按场景需要保留为可选。"
  },
  {
    "capability": "用单一“归类”字段取代多标签：每条记录只归属一个归类，侧栏按归类聚合条目数并支持按归类筛选浏览。",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_9c7f6060878383fa",
      "ev_ba200adf6e2c_9ab6b0e51811a16d",
      "ev_ba200adf6e2c_c4ad7e52e5713628"
    ],
    "reason": "场景明确“保存时选择一个简单归类”，是单归属分类而非多标签。上游是扁平 tags[] + 标签侧栏 + 计数 + 多标签交集筛选，需要把多值匹配改造为单选归属；计数与侧栏交互逻辑沿用，语义由“标签出现次数”变为“每归类条目数”。"
  },
  {
    "capability": "默认归类：未选择归类即保存的链接自动落入“未整理”默认归类，之后可被手动移动。",
    "disposition": "new_design",
    "evidence_ids": [],
    "reason": "场景流程第3步“未经整理的链接可先进入默认归类，之后再手动移动到更合适的位置”是上游完全没有的概念——上游只有 Home/Archived 两个视图，没有默认桶。快速保存不打断浏览依赖这一设计，属场景新增。"
  },
  {
    "capability": "归类管理：用户可新建归类（如“待购”“家居改造”“以后看看”），并把记录从一个归类移动到另一个归类，移动结果持久化。",
    "disposition": "new_design",
    "evidence_ids": [],
    "reason": "场景验收第3条要求“在归类之间移动记录或新建归类，操作结果在重新打开后仍然有效”。上游明确没有 collections/folders，也不持久化任何视图状态，因此新建归类与移动归类必须新设计并落库。"
  },
  {
    "capability": "归类浏览与关键字检索：先按归类列出，再在结果内用关键字匹配标题与域名（必要时含描述），默认按最近保存倒序。",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_9ab6b0e51811a16d",
      "ev_ba200adf6e2c_c4ad7e52e5713628"
    ],
    "reason": "场景验收第4条要求“通过归类浏览或关键字检索找到此前存入的特定链接”。上游检索只匹配 title.toLowerCase() 且带 pinned-first 排序，多值标签筛选也需并入归类。差异是扩大匹配字段到 hostname/描述，以覆盖“只记得是哪个网站”的找回场景。"
  },
  {
    "capability": "首次使用的起始归类集合：预置“待购”“家居改造”“以后看看”与默认“未整理”，用户可在此基础上增删。",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_05babdea64ba9858"
    ],
    "reason": "场景把这三类作为保存时的直接选项，属场景语境的默认数据。上游新建记录只写入 id/hostname/时间等默认字段，没有任何预置分类。这里借用其“新记录写入默认字段”的初始化思路，把预置归类作为应用初始数据而非记录字段。"
  },
  {
    "capability": "删除收藏并支持短时撤销：删除任意记录并弹出带“撤销”的操作提示，点击撤销即恢复。",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_4c56ef30a1785be1"
    ],
    "reason": "上游删除仅对归档项开放且配 5 秒 Undo 恢复。场景没有归档，用户会想直接清理误存链接。保留“删除 + 撤销恢复”的错误兜底机制，去掉“仅归档可删”的前置限制。"
  },
  {
    "capability": "不做置顶/归档：不引入 isPinned/isArchived，也不让编辑、删除出现“仅归档项可用”的分支。",
    "disposition": "not_adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_b1ca64cf2ad02998",
      "ev_ba200adf6e2c_06c81a165e03c96a"
    ],
    "reason": "场景是“先留存、稍后再处理”的收藏箱，没有归档-清空的工作流，置顶也不解决“待购/灵感”的浏览诉求；保留归档反而给编辑与删除加额外前置条件，与快速保存、快速清理相冲突。"
  },
  {
    "capability": "图标与元数据的轻量获取：保存时优先由域名派生 favicon 本地显示，第三方元数据（标题/描述/封面）仅作可选增强，失败静默降级。",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_8e11efc61a4650ba",
      "ev_ba200adf6e2c_ec303a2fd1afa287",
      "ev_ba200adf6e2c_5011700a24e503c7"
    ],
    "reason": "场景希望能一眼辨认“商品页/教程/灵感图”，但上游依赖 api.microlink.io、images.weserv.nl、Google s2 三个未经运行验证的第三方端点，失败只 console.error。差异是把可用性依赖降为本地域名派生，把外部抓取降级为增强，避免保存流程被第三方可达性阻塞。"
  },
  {
    "capability": "不做多排序模式与置顶优先：只保留“最近保存”倒序一种默认顺序。",
    "disposition": "not_adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_9ab6b0e51811a16d"
    ],
    "reason": "场景关注“找到此前存下的东西”，不涉及按访问次数排序或置顶。上游三种排序（最近添加/最近访问/访问最多）+ pinned-first 属书签阅读器语境，对收藏箱是冗余操作面。"
  },
  {
    "capability": "不做“复制 URL”动作：收藏箱的目标是回到原页而非分发链接。",
    "disposition": "not_adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_7150b0ac7a5678db"
    ],
    "reason": "上游 Copy URL 面向分享或复用链接；本场景流程终点是“从记录打开链接，回到原始网页继续购买、阅读或参考”，复制并非必需，去掉可减少每条记录的操作噪音。"
  },
  {
    "capability": "单页应用外壳：index.html 提供 #root，入口模块挂载应用并在根节点缺失时报错。",
    "disposition": "adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_5d51c18a989c01f8",
      "ev_ba200adf6e2c_a2ebc864c5b6b3e7"
    ],
    "reason": "场景是纯个人本地工具、无服务端需求，上游 SPA 挂载方式与本地优先定位一致，可直接沿用为运行外壳。差异仅在挂载的组件内部替换为收藏箱视图，属于结构性沿用。"
  },
  {
    "capability": "浏览视图状态（当前选中归类、搜索词）仅保留在会话内存中，不写入本地库。",
    "disposition": "adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_2288b28e90cd8450"
    ],
    "reason": "场景只要求“归类归属与移动结果在重开后仍然有效”，并未要求记住上次浏览位置。上游把 tab/标签筛选/排序/搜索放在组件本地状态而不落库，恰好划出“数据持久、视图不持久”的边界，避免浏览状态污染收藏数据。"
  }
]