# 品类认知与来源

固定的模型调研记录；来源访问日期与 Atlas 叶子原稿编写日期含义不同。叶子原稿的研究笔记链接属于原语料上下文，不表示本包附带该文件；本包来源以以下条目及未知项为准。

ev_ba200adf6e2c_05babdea64ba9858 [code_observation]: New records are built with id `bm-${crypto.randomUUID()}`, hostname from getHostname(url), and defaults visitCount=0, visitedAt=null, isPinned=false, isArchived=false, createdAt=Date.now(); edits preserve the previous id, isPinned, isArchived, visitCount, createdAt, and visitedAt.

ev_ba200adf6e2c_06c81a165e03c96a [code_observation]: Pin/Unpin and Edit actions are rendered only when the item is not archived, and Edit loads the item's url/title/description/tags/favicon into the dialog.

ev_ba200adf6e2c_1596da4a90687ca5 [code_observation]: The Valibot BookmarkFormSchema requires a non-empty URL matching /^https?:\/\/(?:[\w-]+\.)+[a-zA-Z]{2,}(?:\/\S*)?$/ and v.url, a non-empty title up to 100 chars, a non-empty description up to 280 chars, and 1-5 tags each up to 30 chars.

ev_ba200adf6e2c_3168bcd465b6a043 [inference]: The scenario's user-controlled 'category' (归类) is realized only as up to five free-text tags on each record; there are no creatable, renameable, or nestable collections, and no separate move operation beyond editing tags.

ev_ba200adf6e2c_35e41aab676021eb [code_observation]: saveBookmark sets the record in the in-memory map then awaits db.bookmarks.put(bm); deleteBookmark removes from the map then awaits db.bookmarks.delete(id).

ev_ba200adf6e2c_4c56ef30a1785be1 [code_observation]: A Delete action is rendered only for archived items; it calls deleteBookmark and shows an error-type toast with an Undo action that calls saveBookmark(item) to restore the record.

ev_ba200adf6e2c_6bbd7a588896fe31 [inference]: The scenario step of letting unclassified links land in a default category is not supported, because the form schema rejects saves with zero tags.

ev_ba200adf6e2c_7150b0ac7a5678db [code_observation]: A Copy URL action writes item.url to the clipboard and shows a success toast.

ev_ba200adf6e2c_7d47d725a2e9b759 [inference]: Metadata and favicon enrichment is best-effort and dependent on third-party HTTP services; failures degrade silently to console errors while the bookmark still saves with whatever fields the user entered or omitted defaults for.

ev_ba200adf6e2c_86ed2327f33a3ca8 [code_observation]: An effect on component creation calls db.bookmarks.toArray() and inserts each returned bookmark into an in-memory RippleMap keyed by bookmark id.

ev_ba200adf6e2c_8e11efc61a4650ba [code_observation]: On submit, if no favicon exists and a hostname is derivable, the code fetches a Google s2 favicon proxied through images.weserv.nl inside a try/catch that only logs failure.

ev_ba200adf6e2c_922f1dbc84912d99 [inference]: Persistence is local to one browser profile/device via IndexedDB with no sync layer, so the scenario's cross-session growth holds only on the same browser, and the leaf's multi-device context is unmet.

ev_ba200adf6e2c_93ef917a193a45ab [inference]: Deletion is limited to archived records and recovery is only the transient Undo action on the toast; there is no trash view, and non-archived records cannot be deleted at all through the UI.

ev_ba200adf6e2c_93ff254508846f11 [code_observation]: The Visit action builds an updated bookmark with visitedAt=Date.now() and visitCount+1, calls saveBookmark(updated), then opens the URL with window.open(item.url, '_blank', 'noopener,noreferrer').

ev_ba200adf6e2c_9ab6b0e51811a16d [code_observation]: The displayed list filters by isArchived matching the active tab, requires every selected tag to be present in bookmark.tags, matches search only against bookmark.title.toLowerCase(), and sorts pinned-first then by the chosen sort mode with createdAt descending as fallback.

ev_ba200adf6e2c_b1ca64cf2ad02998 [code_observation]: The Archive/Unarchive action toggles isArchived and, when archiving, forces isPinned=false before saving.

ev_ba200adf6e2c_c4ad7e52e5713628 [code_observation]: Tag counts are derived by iterating all in-memory bookmarks and counting each tag occurrence, then sorted alphabetically for the sidebar.

ev_ba200adf6e2c_e62ae7e0a2c68ba1 [inference]: Retrieval by keyword covers only bookmark titles, not URLs, descriptions, or tag names, so the scenario's 'find by a remembered word' workflow is partially supported.

ev_ba200adf6e2c_e7dd8d32c05c39f9 [inference]: The app supports the scenario's save-now/find-later loop: a deliberate add dialog writes a URL-anchored record into durable IndexedDB, and the record can later be browsed, tag-filtered, title-searched, and opened back to the live URL.

ev_ba200adf6e2c_ec303a2fd1afa287 [code_observation]: fetchMeta calls https://api.microlink.io/?url=... and, on success with result.data, sets title/description and fetches the logo through https://images.weserv.nl/; errors are only console.error'd and the finally block resets loading.

## S01 · Atlas confirmed input

inputs/scenario.json · scn_7756e0007f6a463a97316f3f49c15248@2

把偶然看到但当下不处理的外部网页链接留存，日后需要时能重新找到并回到原页面

Atlas scenario input; not a third-party code license



Pinned requirement input

## S02 · ev_ba200adf6e2c_05babdea64ba9858

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

New records are built with id `bm-${crypto.randomUUID()}`, hostname from getHostname(url), and defaults visitCount=0, visitedAt=null, isPinned=false, isArchived=false, createdAt=Date.now(); edits preserve the previous id, isPinned, isArchived, visitCount, createdAt, and visitedAt.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S03 · ev_ba200adf6e2c_06c81a165e03c96a

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

Pin/Unpin and Edit actions are rendered only when the item is not archived, and Edit loads the item's url/title/description/tags/favicon into the dialog.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S04 · ev_ba200adf6e2c_1596da4a90687ca5

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

The Valibot BookmarkFormSchema requires a non-empty URL matching /^https?:\/\/(?:[\w-]+\.)+[a-zA-Z]{2,}(?:\/\S*)?$/ and v.url, a non-empty title up to 100 chars, a non-empty description up to 280 chars, and 1-5 tags each up to 30 chars.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S06 · ev_ba200adf6e2c_35e41aab676021eb

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

saveBookmark sets the record in the in-memory map then awaits db.bookmarks.put(bm); deleteBookmark removes from the map then awaits db.bookmarks.delete(id).

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S07 · ev_ba200adf6e2c_4c56ef30a1785be1

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

A Delete action is rendered only for archived items; it calls deleteBookmark and shows an error-type toast with an Undo action that calls saveBookmark(item) to restore the record.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S12 · ev_ba200adf6e2c_7150b0ac7a5678db

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

A Copy URL action writes item.url to the clipboard and shows a success toast.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S13 · ev_ba200adf6e2c_86ed2327f33a3ca8

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

An effect on component creation calls db.bookmarks.toArray() and inserts each returned bookmark into an in-memory RippleMap keyed by bookmark id.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S14 · ev_ba200adf6e2c_8e11efc61a4650ba

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

On submit, if no favicon exists and a hostname is derivable, the code fetches a Google s2 favicon proxied through images.weserv.nl inside a try/catch that only logs failure.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S15 · ev_ba200adf6e2c_93ff254508846f11

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

The Visit action builds an updated bookmark with visitedAt=Date.now() and visitCount+1, calls saveBookmark(updated), then opens the URL with window.open(item.url, '_blank', 'noopener,noreferrer').

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S16 · ev_ba200adf6e2c_9ab6b0e51811a16d

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

The displayed list filters by isArchived matching the active tab, requires every selected tag to be present in bookmark.tags, matches search only against bookmark.title.toLowerCase(), and sorts pinned-first then by the chosen sort mode with createdAt descending as fallback.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S19 · ev_ba200adf6e2c_b1ca64cf2ad02998

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

The Archive/Unarchive action toggles isArchived and, when archiving, forces isPinned=false before saving.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S20 · ev_ba200adf6e2c_c4ad7e52e5713628

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

Tag counts are derived by iterating all in-memory bookmarks and counting each tag occurrence, then sorted alphabetically for the sidebar.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## S21 · ev_ba200adf6e2c_ec303a2fd1afa287

https://github.com/lakhindarpal/bookmark-manager/blob/539881bc67099d491e8ab6f85de0f443fa7de623/src/App.tsrx · 539881bc67099d491e8ab6f85de0f443fa7de623

fetchMeta calls https://api.microlink.io/?url=... and, on success with result.data, sets title/description and fetches the logo through https://images.weserv.nl/; errors are only console.error'd and the finally block resets loading.

Fixed source license/NOTICE hashes in inputs/case-basis.json; legal reuse review not performed.



Independently accepted code_observation; design adaptation is recorded separately; upstream not run.

## 待验证

- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- Behavior of Ripple TS reactivity primitives (track/effect/bindGroup/bindValue) at this pinned version was not validated.
- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- Host excluded unsupported evidence inf-no-tests: Depends on a quarantined, unlocated observation
- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- Host excluded unsupported evidence obs-no-test-files: observation cites an unknown source path: source/src
- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- No automated tests exist in the manifest, so none of the described behaviors are test-confirmed.
- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- Runtime behavior was not observed; all claims are static reading of source files.
- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- The full commit tree was inferred from the supplied source_manifest and the on-disk source/ directory; files outside it were not inspected.
- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- The paired Research Notes referenced by leaf.md were not supplied, so product-level evidence beyond the pinned repository is unavailable.
- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- Whether Dexie/IndexedDB persistence behaves correctly in real browsers at this commit is unverified.
- Unverified case limitation (case:product-c42848f63251507bd9d911a5:faa52e6b1414 r1); not accepted evidence:
- Whether the third-party metadata/favicon endpoints (api.microlink.io, images.weserv.nl, Google s2 favicons) are reachable, rate-limited, or CORS-permitted at runtime is unverified.


## 固定案例依据与设计取舍 / Fixed case basis and design

案例依据来自共享规范记录，完整版本见 inputs/case-basis.json。源码定位与独立审阅不代表上游运行通过。

[
  {
    "capability": "F08: a single-user personal library persisted in SQLite that survives browser sessions and server restarts, with records queried from the database for every request rather than held in a browser store.",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_35e41aab676021eb",
      "ev_ba200adf6e2c_86ed2327f33a3ca8",
      "ev_ba200adf6e2c_922f1dbc84912d99",
      "ev_ba200adf6e2c_e7dd8d32c05c39f9"
    ],
    "reason": "The evidence shows Dexie writes on save/delete and a one-time db.bookmarks.toArray() hydration into an in-memory RippleMap, scoped to one browser profile with no sync. The target adopts local, single-user, cross-session retention but replaces IndexedDB/Dexie and in-memory hydration with SQLite on the Python server; it does not claim browser-profile persistence, multi-device sync, or the source map as target design."
  },
  {
    "capability": "F11: the library is delivered as Python server-rendered HTML pages and forms using POST/redirect/GET for saving records, managing categories, moving records between categories, and soft-delete/restore, including a ready empty-library view. P0 has no standalone record-editing page; record URL updates retain only the existing PATCH /api/bookmarks/{id} contract.",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_06c81a165e03c96a",
      "ev_ba200adf6e2c_86ed2327f33a3ca8",
      "ev_ba200adf6e2c_e7dd8d32c05c39f9"
    ],
    "reason": "The evidence describes a client-mounted SPA: Edit is an in-page dialog populated from item fields, and component creation loads Dexie rows into a client RippleMap. The target implements the already-declared P0 save, category-management, move and soft-delete/restore journeys as Python 3.12 HTML responses. Source SPA mounting, client-side dialog state and Dexie hydration are not carried over. The source Edit dialog does not imply a target record-editing UI; the existing PATCH API retains URL updates and recomputes hostname when the URL changes. The save-now/find-later loop and ready empty state remain the target intent."
  },
  {
    "capability": "A deliberate save creates a URL-anchored record with a stable id, a locally derived hostname, creation time and initial active state. Later changes preserve the record id and creation time; updating the URL recomputes hostname from the new URL. The adopted capability is this identity and creation lifecycle; visitCount and visitedAt are not target fields or P0 obligations.",
    "disposition": "adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_05babdea64ba9858"
    ],
    "reason": "The accepted observation records the source's bm-prefixed UUID identity, hostname derivation, createdAt, initial flags and visit fields, and preservation of identity and creation/visit fields on edit. These remain source observations. The target adopts stable record identity and creation time, represented by its existing id/created_at model and made durable by SQLite; it does not import the source's visitCount/visitedAt fields, which F24 excludes. URL updates follow the existing PATCH contract and derive hostname again. The source's tag constraints and other state fields are not silently imported into the category or target data model."
  },
  {
    "capability": "URL validation accepts only absolute, parseable HTTP(S) URLs with a nonempty valid hostname, allows single-label hosts such as http://localhost, preserves the original URL text, and rejects malformed, non-HTTP(S) or empty-host input without writing; no DNS or online-reachability check is performed.",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_1596da4a90687ca5"
    ],
    "reason": "The upstream Valibot rule is a dotted-host regex that requires a dot-separated domain and an alphabetic top-level suffix, so it rejects localhost. That regex is retained as a source fact and mapped as adjusted, not reused as the target rule: the target parses the URL, checks the http/https scheme, absolute form and hostname presence, permits single-label hosts, and stores the entered string unchanged."
  },
  {
    "capability": "Create, rename and delete named categories with validation and with protection or reassignment when a category still contains records, assign one at save time, move records between categories, and default uncategorized saves into an Inbox category.",
    "disposition": "new_design",
    "evidence_ids": [
      "ev_ba200adf6e2c_3168bcd465b6a043",
      "ev_ba200adf6e2c_6bbd7a588896fe31"
    ],
    "reason": "Evidence shows the source has no category entity: classification is only up to five free-text tags, there is no collection CRUD or separate move, and the form rejects saves with zero tags. The target therefore designs first-class categories, an inbox default for unclassified capture and an explicit move action; these are new target concepts, not source-derived tag behavior."
  },
  {
    "capability": "Browse one category and see only its active records, with a category count that agrees with the listed records after adds, moves and restores.",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_c4ad7e52e5713628",
      "ev_ba200adf6e2c_9ab6b0e51811a16d"
    ],
    "reason": "Source facts derive tag counts by scanning all in-memory bookmarks and filter records by requiring every selected tag. The target computes category counts and category-scoped lists in SQL over active, non-deleted rows so the count and the list stay consistent; the source tag-sidebar algorithm is not the target implementation."
  },
  {
    "capability": "Search the selected category by keyword across title, hostname and description using case-insensitive substring matching, retaining category and query and rendering matching or explicit empty results.",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_9ab6b0e51811a16d",
      "ev_ba200adf6e2c_e62ae7e0a2c68ba1"
    ],
    "reason": "Source search lowercases and compares only bookmark.title; the fixed target F06/A07 contract adjusts it to title, derived hostname and description, combined with the selected category. Raw URL text, category names and tags are not additional keyword fields. This clarifies target design only; accepted observations, evidence IDs, source revision and disposition remain unchanged."
  },
  {
    "capability": "Open a saved record as a navigation to its stored original URL, preserving the URL text and never fetching, proxying or prefetching the destination during save, listing or open preparation.",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_93ff254508846f11"
    ],
    "reason": "Source opens the URL with window.open(url, '_blank', 'noopener,noreferrer') after updating visit state. The target renders the record URL as an ordinary HTTP(S) link or server redirect with the same new-tab/no-referrer intent; opening is a user navigation distinct from saving, and the Python server does not request the target page."
  },
  {
    "capability": "Do not enrich saved records with third-party metadata or favicon services and do not prefetch saved target pages; stored title, description and URL come from the user or local derivation.",
    "disposition": "not_adopted",
    "evidence_ids": [
      "ev_ba200adf6e2c_7d47d725a2e9b759",
      "ev_ba200adf6e2c_8e11efc61a4650ba",
      "ev_ba200adf6e2c_ec303a2fd1afa287"
    ],
    "reason": "The source calls api.microlink.io and images.weserv.nl/Google s2 favicons on save and treats failures as silent. The target P0 deliberately omits these outbound calls because saving and opening must remain distinct from fetching; no target-page response, metadata or icon is retrieved, and no source enrichment behavior is presented as target design."
  },
  {
    "capability": "Soft-delete an active record into a recoverable trash and restore it later, instead of allowing deletion only on archived items with a transient toast undo.",
    "disposition": "adjusted",
    "evidence_ids": [
      "ev_ba200adf6e2c_4c56ef30a1785be1",
      "ev_ba200adf6e2c_93ef917a193a45ab"
    ],
    "reason": "Source facts limit Delete to archived items and provide recovery only through an Undo action on the toast, with no trash view and no deletion path for active records. The target uses an explicit soft-delete/restore lifecycle exposed in HTML so records remain recoverable; this changes the source's archived-only and transient-recovery model."
  }
]