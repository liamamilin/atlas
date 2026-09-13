# Research Notes — Web Archive Viewer

Research date: 2026-09-09

## Research Goal

Understand the Application Type "Web Archive Viewer": an application whose purpose is to let a user locate, select, and view stored captures of web pages as they existed at past points in time. Produce a vendor-neutral Application Document that explains the defining core, standard capabilities, workflows, interfaces, rules, and variants of this Type, and its boundaries against neighboring Types (Web Browser, Read-it-later, Bookmark Manager, Search Engine caches, Digital Library Platform).

## Initial Boundary

Initial hypothesis before research:

- The core object is a **stored capture (snapshot) of a web resource**, addressed by the resource's original URL plus a capture datetime.
- The core user act is **time-addressed viewing**: pick a URL, see what captures exist, choose a point in time, view the page as captured.
- Closest neighbors: Web Browser (renders the live web), Read-it-later / Bookmark Manager (personal single copies), Search Engine (cached results as a byproduct), Digital Library Platform (curated document collections).
- Open questions going in: Is capture acquisition part of the Type? Is a hosted service required, or can the viewer be local? Is the time dimension definitional, or is a single snapshot enough? Where exactly is the line against a browser and against a mirror?

## Research Questions

1. What are the core objects? (capture/snapshot; relationship between original URL, capture time, and stored copy)
2. How does the user find captures for a URL? (URL entry, search, collection browsing)
3. How is the time dimension presented and resolved? (datetime negotiation, snapshot lists, nearest-match semantics)
4. How does replay/presentation work? (rendering the captured page, banners, link rewriting, missing-resource handling)
5. Where do captures come from, and is capture part of the definition? (crawlers, user-initiated capture, local archive files)
6. What search capabilities exist? (URL lookup vs full-text vs resource-level)
7. What rules and exceptions matter? (frozen-state promise, coverage gaps, live-web leaks, access restrictions/embargo)
8. What are the boundaries against Web Browser, Read-it-later, mirrors, search caches, and CMS/version-control versioning?

## Representative Products

Selected for market representativeness, documentation quality, and distinct product philosophies:

1. **Wayback Machine (Internet Archive)** — the dominant global public crawler-based web archive with a replay interface. (Direct surfaces unreachable this session; see Sources.)
2. **archive.today (archive.ph / archive.is)** — independent on-demand snapshot service. (Direct surfaces unreachable this session; see Sources.)
3. **ReplayWeb.page (Webrecorder)** — local-first, serverless "browser-based web archive viewer" over WARC/WACZ files.
4. **pywb (Webrecorder) + SolrWayback (Netarkivet.dk / Danish national archive)** — the institutional self-hosted replay software family used by national libraries and archives.
5. **Conifer (Rhizome)** — user-driven "collect and revisit" web archiving service with interactive capture and collection sharing.

Supporting framework source: **Memento (RFC 7089)** — the HTTP framework for time-based access to resource states, which supplies the canonical conceptual vocabulary for the whole Type.

## Sources

Directly fetched on 2026-09-09 (Layer A):

- RFC 7089 — HTTP Framework for Time-Based Access to Resource States -- Memento — https://datatracker.ietf.org/doc/html/rfc7089 (full text)
- Memento Guide — https://mementoweb.org/guide/ and https://mementoweb.org/guide/quick-intro/
- ReplayWeb.page — https://webrecorder.net/replaywebpage/ (product page), https://replayweb.page/docs/user-guide/ (user guide), https://replayweb.page/docs/user-guide/loading/, https://replayweb.page/docs/user-guide/locations/, https://replayweb.page/docs/user-guide/exploring/
- pywb documentation — https://pywb.readthedocs.io/en/latest/ (index) and https://pywb.readthedocs.io/en/latest/manual/configuring.html
- SolrWayback — https://github.com/netarchivesuite/solrwayback (README)
- IIPC — https://netpreserve.org/ and https://netpreserve.org/web-archiving/playback/
- Conifer — https://conifer.rhizome.org/

Unreachable on 2026-09-09 (each abandoned after repeated failures, per source-access rules):

- archive.org surfaces (help.archive.org, web.archive.org) — timed out ×2
- archive.today mirrors (archive.ph, archive.is) — timed out ×2
- UK Web Archive (webarchive.org.uk) — transport errors ×2
- Memento Time Travel aggregator UI (timetravel.mementoweb.org) — transport errors ×2
- Wikipedia (en.wikipedia.org) — timed out ×2; Wikiwand mirror — timed out ×2
- loc.gov — HTTP 403; Britannica — 404; arquivo.pt — timed out; docs.replayweb.page — transport error (alternate docs path used instead)

**Source-access limitation:** No direct evidence was obtained this session for Wayback Machine or archive.today product surfaces beyond the example Memento URLs quoted inside RFC 7089 itself (web.archive.org and archive.is Memento URLs with embedded capture datetimes). All product-specific claims about those two products are therefore held at the level the RFC examples support; no UI details, coverage numbers, or feature claims are asserted for them from model memory.

## Product Observations

### RFC 7089 — Memento framework (authoritative conceptual vocabulary) [Layer A]

- Defines the four canonical roles: **Original Resource** (URI-R: "a resource that exists or used to exist, and for which access to one of its prior states may be required"), **Memento** (URI-M: "a resource that encapsulates a prior state of the Original Resource… a frozen prior state"), **TimeGate** (URI-G: "capable of datetime negotiation to support access to prior states"), **TimeMap** (URI-T: "a resource from which a list of URIs of Mementos… is available").
- **Datetime negotiation**: the user agent expresses a preferred datetime (Accept-Datetime); the server selects the Memento that best matches; the selection algorithm is server discretion (e.g., nearest in time, nearest in past). "Due to the sparseness of Mementos in most systems, the value of the Memento-Datetime header returned by a server may differ (significantly) from the value conveyed by the user agent."
- **Memento-Datetime header** "constitutes a promise that the resource state reflected in the response will no longer change" — the frozen-state property is normative.
- A Memento's entity-body "may very well not be byte-to-byte the same" as the original response: reasons include **format migrations**, **URI-rewriting as applied by some Web archives**, and **the addition of banners as a means to brand Web archives**. (Direct RFC evidence that rewriting and banners are standard archive practices.)
- Mementos "exist in Web archives, content management systems, or revision control systems, among others" — i.e., the frozen-prior-state pattern is broader than web archives; the web-archive case is distinguished by holding prior states of **external web resources**.
- The framework is **distributed**: versions may reside on multiple servers; each server knows only its own versions; aggregators of TimeGates are an anticipated pattern.
- Example Memento URLs quoted in the RFC: `http://web.archive.org/web/19970107171109/http://www.ietf.org/`, `http://webarchive.nationalarchives.gov.uk/20080906200044/http://www.ietf.org/`, `http://archive.is/20120527002537/http://www.w3.org/TR/webarch/` — direct evidence that Wayback Machine, the UK National Archives web archive, and archive.is expose time-addressed captures with the capture datetime embedded in the URL, and that this pattern spans a global public archive, a national archive, and an independent snapshot service.

### ReplayWeb.page (Webrecorder) [Layer A]

- Self-labels on the product page: **"Browser-based Web Archive Viewer"**; tagline "Explore and replay interactive archived webpages directly in your browser"; described as "serverless playback of web archives". (Direct evidence for the leaf's own naming.)
- Loading model: load archived items from **local files** ("loaded directly in the browser and is *not* uploaded anywhere — your data never leaves your computer"), from **remote URLs** (downloaded fully or on-demand), **Google Drive** (`googledrive://`), **Amazon S3** (`s3://`), **IPFS** (`ipfs://`). "The goal is to support loading web archives from any source a web browser can connect to."
- Supported formats: **WACZ** (recommended; on-demand loading, no indexing required), **WARC** (entire file must be read to generate an index), **HAR**, **CDX**; WBN and ARC not supported.
- Homepage: "lists an index of all your loaded archived items. Items are searchable by their title or source, and can be filtered by the date they were loaded or their title."
- Navigation sidebar with three views: **Page** (lists all webpages stored in the item; searchable by title, URL, or extracted text; full-text search from pre-generated WACZ data or generated from WARC HTML), **Resources** (all content listed by URL and media type; search by exact URL, URL prefix, or contains; "for many archived items with no page or curatorial metadata available, this is the best way to explore the archived contents"), **Story** (curated pages with significance descriptions; only present if the archive carries a curated story, e.g., Conifer-exported WARCs).
- Additional features: full-text search; **Flash emulation via Ruffle** for older archives; **works offline** (desktop app or PWA); view page resources; Google Workspace plugin; on-demand loading via HTTP range requests; **embedding** ("archive receipts" embed mode to "display web archives like any other piece of media").
- No capture capability of its own — it is a pure viewer/replayer; capture is delegated to sibling tools (ArchiveWeb.page, Browsertrix).

### pywb (Webrecorder) [Layer A]

- Self-description: "a full-featured, advanced web archiving **capture and replay** framework… A subset of features provides the basic functionality of a 'Wayback Machine'."
- **Framed replay**: "the archived content is loaded into an iframe, and a top frame UI provides info and metadata." Top-frame URL pattern `/<coll>/<url>`, content served at `/<coll>/mp_/<url>`.
- **Frameless replay**: content served directly; bannerless by default since pywb 2.7 unless a custom banner template is added.
- **Banner purpose** (proxy mode): "insert a default banner… to make it clear to users that they are viewing replayed content."
- Security note: framed mode recommended "because a malicious site could tamper with the banner."
- **URL rewriting**: server-side rewriting plus a client-side rewriting system (**wombat.js**) that "intercepts network traffic and emulates the correct JS environment expected by a replayed page."
- **Proxy mode**: pywb acts as an HTTP/S proxy; "the user enters `http://example.com/` and is served content from the `my-coll` collection"; timestamp specified separately; "if the timestamp is omitted, proxy mode replay defaults to the latest capture."
- **Memento API** (TimeMap API, TimeGate API, URI-M headers) enabled by default.
- **Exact-timestamp redirects**: by default the canonical exact-timestamp URL is returned via `Content-Location` rather than a redirect; a classic redirect mode is available and "is consistent with previous behavior and other 'wayback machine' implementations."
- **Embargo and access control**: embargo before/after exact dates or by interval; access types allow/block/exclude; user-based access controls; per-collection ACL files.
- **Collections**: directory structure of archive (WARC/ARC files) + indexes (CDXJ) + acl + templates; auto "all" aggregate collection across collections; **remote Memento collections** (e.g., define a collection that accesses Internet Archive's Wayback Machine via `memento+https://web.archive.org/web/`).
- **Recording mode**: `/<coll>/record/<url>` records live-web content into the collection's WARCs (capture through the replay tool); live-web collection (`$live`) proxies the live web for testing.

### SolrWayback (Netarkivet.dk / Danish national archive) [Layer A]

- Self-description: "a web application for **browsing historical harvested ARC/WARC files** similar to the Internet Archive Wayback Machine. SolrWayback runs on a Solr server containing ARC/WARC files indexed using the warc-indexer."
- Features: free text search in all resources (HTML, PDFs, media metadata, URLs); interactive link graph; export of search results to WARC; image search; image geo/similarity search; n-gram visualization; domain statistics over time; word clouds; view all indexed fields and WARC headers for a record.
- **Playback**: "Solrwayback showing the playback of an archived webpage with playback toolbox overlay"; "Configure alternative playback engine to any playback engine using the playback-API such as OpenWayback or pywb" — the search interface and the playback engine are separable components.
- **URL API equivalence with Internet Archive**: "The API for linking to and browsing archived webpages is the same as for Internet Archive" — IA: `https://web.archive.org/web/20080213093319/http://…`; SolrWayback: `http://server/solrwayback/services/web/20140515140841/http://…`. (Direct cross-product evidence for the shared `web/<timestamp>/<original-url>` addressing pattern.)
- **Live-leak handling**: a root servlet / serviceworker setup catches "relative leaks (same domain)" and "redirected back into SolrWayback to the correct URL and correct crawl time"; "Absolute URL live-leaks… will not be caught and can leak to the open and live web. Open the network tab (F12)… or turn-off the internet connection to be sure there are no live leaks during playback." (Documented replay exception.)
- Harvesting context: WARC files from Heritrix, Webrecorder, Brozzler, Wget; indexing via the British Library's warc-indexer.

### IIPC — International Internet Preservation Consortium [Layer A]

- The professional body of national/university libraries and archives doing web archiving (members include Internet Archive, British Library, Library of Congress, national libraries across 35+ countries).
- Maintains a **Playback** tools page: "software used to **'play back' archived websites in the user's browser**. Key replay tools used by IIPC members include OpenWayback (OWB), Python Wayback (pywb) and SolrWayback."
- pywb is the IIPC-recommended replay solution; "Web archives currently using pywb for replay include Arquivo.pt, Vefsafn.is, the UK Web Archive and the Web Archive at UNT."
- SolrWayback "relies on real-time access to WARC files and a Solr index… has a built-in playback engine and can be integrated with pywb"; public use cases include the Hungarian Web Archive and IIPC collaborative collections hosted by Bibliotheca Alexandrina.
- (Confirms that the viewer function is a distinct, named software category — "playback/replay" — separate from crawling/harvesting and indexing, and that it is the standard access surface of institutional web archives.)

### Conifer (Rhizome) [Layer A]

- Self-description: "Collect and revisit web pages. Conifer is a web archiving service that creates an **interactive copy** of any web page that you browse, including content revealed by your interactions such as playing video and audio, scrolling, clicking buttons."
- Philosophy: user-driven capture ("Unlike conventional crawler-based web archiving methods…"); autopilot behaviors for popular platforms; login-and-capture; publish/share collections publicly or privately; "Own Your Data — download your web archives in the ISO standard WARC file format."
- Status note: "Creating and modifying collections was disabled before Conifer's discontinuation in June 2026." (Replay of existing collections remains the relevant evidence; product is end-of-life.)

### Wayback Machine (Internet Archive) [Layer A — minimal, degraded]

- Direct product surfaces unreachable this session. Evidence held: RFC 7089 quotes `http://web.archive.org/web/19970107171109/http://www.ietf.org/` as a Memento — direct evidence that the Wayback Machine serves time-addressed captures of arbitrary web resources with the capture datetime embedded in the URL, and (via SolrWayback's README) that its `/web/<timestamp>/<url>` API pattern is the de-facto reference that other replay systems imitate.
- IIPC lists Internet Archive as a member organization of the web-archiving community.
- No UI, coverage, or feature claims are made for the Wayback Machine in this pass beyond the above.

### archive.today (archive.ph / archive.is) [Layer A — minimal, degraded]

- Direct surfaces unreachable this session. Evidence held: RFC 7089 quotes `http://archive.is/20120527002537/http://www.w3.org/TR/webarch/` as a Memento — direct evidence that archive.is serves time-addressed captures with embedded datetimes.
- No further product-specific claims are made.

## Cross-product Comparison

| Dimension | Wayback Machine | archive.today | ReplayWeb.page | pywb / SolrWayback (institutional) | Conifer | Memento (framework) |
|---|---|---|---|---|---|---|
| Stored captures of web resources | yes (RFC example) | yes (RFC example) | yes (loads WARC/WACZ/HAR/CDX) | yes (WARC/ARC collections) | yes (WARC download) | yes (defining) |
| Time-addressed access (URL + capture datetime) | yes (`/web/<ts>/<url>`) | yes (`/<ts>/<url>`) | yes (per-page capture times in item index) | yes (same `/web/<ts>/<url>` pattern documented) | yes (collection + capture times) | yes (datetime negotiation, TimeMap) |
| Replay/presentation of the capture | yes | yes | yes ("replay interactive archived webpages") | yes ("playback of an archived webpage") | yes ("revisit") | yes (Memento dereference) |
| Capture acquisition bundled | crawler (background) | on-demand (user) | **no** (pure viewer) | external harvesters (Heritrix/wget); pywb record mode optional | user browsing capture | out of scope |
| Hosted service vs software vs local | hosted | hosted | local/serverless (PWA/desktop) | self-hosted server software | hosted | protocol |
| Banner / archived-status marking | (not directly evidenced) | (not directly evidenced) | (viewer chrome; not evidenced as banner) | yes (pywb banner "make it clear… viewing replayed content"; framed top-frame UI) | (not directly evidenced) | yes (banners documented as archive practice) |
| Link rewriting to stay inside archive | (implied by URL pattern) | (not directly evidenced) | yes (client-side replay engine) | yes (server + wombat.js; leak-catching root servlet) | yes (interactive replay) | yes (URI-rewriting documented) |
| Nearest-capture semantics | (implied by URL pattern) | (not directly evidenced) | n/a (explicit items) | yes (Memento API; exact-timestamp redirect option) | n/a | yes (normative) |
| Search | (not directly evidenced) | (not directly evidenced) | yes (pages by title/URL/full text; resources by URL) | yes (SolrWayback free text across all resources; pywb query templates) | (not directly evidenced) | TimeMap listing |
| Collection layer | (not directly evidenced) | (not directly evidenced) | yes (loaded items index) | yes (collections directories; aggregate "all") | yes (collections, public/private) | aggregation anticipated |
| Export/download | (not directly evidenced) | (not directly evidenced) | yes (sharing) | yes (SolrWayback WARC/CSV/zip export) | yes (WARC download) | n/a |
| Access control / embargo | (not directly evidenced) | (not directly evidenced) | no (local files) | yes (pywb embargo, allow/block/exclude, user-based) | yes (public/private collections) | n/a |
| Cross-archive aggregation | (not directly evidenced) | (not directly evidenced) | no (per-item) | yes (pywb remote Memento collections; aggregate "all") | no | yes (aggregators of TimeGates) |

Reading: the three rows that are "yes" across every column — stored captures, time-addressed access, replay presentation — are the Type's spine. Everything else varies by product philosophy.

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

Minimal structure without which the product is not a Web Archive Viewer:

1. **Stored captures of web resources** — the system holds persistent, frozen copies of web pages/resources that exist or existed on the live web. (Remove → live-web browser or proxy; nothing archived.)
2. **Time-addressed access** — each capture is identified by its original URL and its capture time, and the user selects among captures in the time dimension (a capture list, timeline, or datetime negotiation). (Remove → a single-copy mirror or a generic file viewer; the archive dimension is gone.)
3. **Replay presentation** — the selected capture is presented as a viewable page, with its archived identity (original URL + capture time) visible to the user. (Remove → a metadata index/catalog of captures with nothing to view.)

Jointly load-bearing: 1 alone = a mirror or file store; 2 without 1 = an empty timeline; 3 without 1+2 = a browser rendering something; 1+2 without 3 = a catalog, not a viewer; 1+3 without 2 = a single-snapshot display, not an archive viewer.

Anti-overfit notes (per the shared-implementation rule):

- **The `/web/<timestamp>/<url>` URL pattern is NOT definitional** — it is a dominant shared implementation (Internet Archive and SolrWayback documented; pywb's classic redirect mode "consistent with… other 'wayback machine' implementations"), but ReplayWeb.page addresses captures through loaded-item indexes and page lists without that URL grammar, and Memento's datetime negotiation is header-based. The invariant is time-addressing, not this URL shape.
- **Crawler-based mass harvesting is NOT definitional** — ReplayWeb.page is a pure viewer over files it did not create; Conifer and pywb record mode capture by user action; archive.today captures on demand. The invariant says nothing about how captures came to exist.
- **Hosted public service is NOT definitional** — self-hosted institutional software (pywb/SolrWayback) and local serverless viewers (ReplayWeb.page) satisfy the core.
- **Banner UI is NOT definitional** — pywb frameless mode is bannerless by default since 2.7; banners are a common marking mechanism, not the invariant. The invariant is only that the archived identity (original URL + capture time) is visible.
- **Full-text search is NOT definitional** — URL-addressed lookup suffices; full-text search is common-mature (SolrWayback, ReplayWeb.page) but not required.

### L1 — Common Mature Structure

- **Shareable archived URLs** embedding the capture time (the `web/<timestamp>/<url>` family; Memento URI-Ms).
- **Replay banner / top-frame chrome** marking that content is replayed and showing the capture datetime (pywb framed replay + banner; RFC documents banners as standard archive branding).
- **Link rewriting** (server-side and/or client-side) so navigation from a replayed page resolves to other captures instead of the live web (pywb wombat.js; SolrWayback root servlet; RFC documents URI-rewriting).
- **Nearest-capture resolution**: a requested datetime resolves to the nearest available capture; the served capture's datetime may differ significantly from the request (RFC normative; pywb exact-timestamp redirect option).
- **Search over the archive**: URL lookup at minimum; full-text search across pages/resources in mature products (SolrWayback free text in all resources; ReplayWeb.page full-text page search).
- **Collection/organization layer**: archives organize captures into collections or loaded items (pywb collections; ReplayWeb.page loaded-items index; Conifer collections).
- **Export/download of captures or search results** (SolrWayback WARC/zip/CSV export; Conifer WARC download; ReplayWeb.page sharing).

### L2 — Variant / Optional Structure

- **Capture acquisition model**: crawler harvest at scale (Internet Archive, national archives) / user-initiated on-demand capture (archive.today-style; Conifer; pywb record mode) / pre-made archive files supplied by the user (ReplayWeb.page).
- **Delivery form**: hosted public service / self-hosted institutional software / local desktop app or PWA / embeddable component (ReplayWeb.page "archive receipts").
- **Cross-archive aggregation**: federated lookup across multiple archives (Memento aggregators; pywb remote Memento collections and aggregate "all" collection).
- **Access governance**: embargo windows, allow/block/exclude rules, user-based access, public/private collections (pywb; Conifer) — typical of institutional/legal-deposit archives.
- **Research analytics over captures**: link graphs, n-gram trends, domain statistics, image/geo search, word clouds (SolrWayback).
- **Legacy-content emulation**: Flash playback via Ruffle (ReplayWeb.page); pywb flash video override (legacy, disabled by default).
- **Proxy-mode replay**: the viewer acts as an HTTP/S proxy so the user browses original URLs and receives archived content (pywb).
- **Curated narrative layers**: curated page lists with significance descriptions (Conifer stories; ReplayWeb.page story view).

### L3 — Vendor-specific (Research Notes only)

- pywb's URL prefix codes (`mp_`, `js_`, `if_`…), its 2.7 banner breaking change, its Redis-backed dedup policies, its wsgiprox certificate authority.
- SolrWayback's specific Solr/warc-indexer bundle, property files, headless-chrome page previews, Gephi link-graph export.
- ReplayWeb.page's Google Drive add-on, Ruffle integration, WACZ on-demand range loading, specific supported-format table.
- Conifer's autopilot behaviors, remote-browser capture fleet, 5GB free accounts, June 2026 discontinuation.
- Internet Archive's specific UI (calendar, save-page-now) — not evidenced this session, therefore not characterized at all.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model.

## Boundary Findings

- **vs Web Browser**: a browser renders the live web; the archive viewer renders stored past states. A browser can display an archived URL, but without a capture store and time selection it is not this Type. pywb proxy mode deliberately mimics browser UX ("the user enters http://example.com/ and is served content from the my-coll collection") — the seam is the content source (stored captures vs live web), not the interaction style. **Remove the archive → Web Browser.**
- **vs Read-it-later / Bookmark Manager**: those hold a personal copy of a page for later reading; there is no maintained, time-addressed capture set and no public/shared archive dimension. **Remove the time dimension and shared archive → personal saved copy (Read-it-later territory).**
- **vs Search Engine caches**: a cache is a transient byproduct of search, not a maintained archive with datetime-addressed, citable captures; the search engine's primary surface is discovery of the live web. **Remove the maintained capture store → cache byproduct, not this Type.**
- **vs Website mirror / static copy**: a mirror serves one copy as if it were live, with no original-URL + datetime addressing and no capture history. **Remove time-addressing → mirror.**
- **vs CMS / version control systems**: RFC 7089 notes these also expose Mementos (frozen prior states) — but of **their own resources**. The Web Archive Viewer's object is the **external web at large**, addressed by original public URL. **Change the archived object to the system's own content → versioning feature, not this Type.**
- **vs Digital Library Platform / Institutional Repository**: those curate document collections (books, articles, theses) with bibliographic identities; the web archive viewer's unit is the captured web resource addressed by URL + time. National web archives straddle: the institution curates, but the access surface is exactly this Type (IIPC's playback tools page is the institutional access layer).
- **Taxonomy note**: the professional community's name for the viewer function is **"playback" / "replay"** (IIPC: "software used to 'play back' archived websites in the user's browser"; ReplayWeb.page: "serverless playback of web archives"). The directory leaf "Web Archive Viewer" names the same function from the user's perspective; ReplayWeb.page itself self-labels "Browser-based Web Archive Viewer". No alias problem — the leaf is coherent — but the playback/replay vocabulary should be expected in sources.

## Uncertainties

- Wayback Machine and archive.today product surfaces were unreachable; their UI specifics (calendar/timeline widgets, save-page-now flows, coverage claims) are intentionally not characterized. Only their time-addressed Memento URL patterns (via RFC 7089 examples) are asserted.
- Whether the Wayback Machine's current replay uses framed or frameless presentation was not directly evidenced; pywb documents both modes as the two standard implementations, so the final document speaks of banner/top-frame marking as "common" rather than universal.
- The Memento Time Travel aggregator UI (timetravel.mementoweb.org) was unreachable; cross-archive aggregation is evidenced via RFC 7089's aggregator pattern and pywb's remote Memento collections, not via a fetched aggregator product page.
- UK Web Archive / national-archive UI specifics were not directly fetched; institutional-variant claims rest on pywb's access-control documentation plus IIPC's description of member archives using pywb/SolrWayback.
- Conifer is discontinued (June 2026) for new collections; its evidence describes the product as documented, not its current availability.

## Final Synthesis

The Web Archive Viewer is the **access surface of web archiving**: the pipeline is capture → index → replay, and this Type is the replay leg, whether bundled into a hosted archive service, shipped as self-hosted institutional software, or run locally over archive files.

The defining core is exactly three jointly-held structures: **stored captures of web resources** (frozen copies of pages that exist(ed) on the live web), **time-addressed access** (captures identified by original URL + capture time, selectable in the time dimension), and **replay presentation** (the selected capture rendered as a viewable page with its archived identity visible). The Memento framework (RFC 7089) supplies the canonical vocabulary — Original Resource, Memento, TimeGate, TimeMap — and its normative behaviors (frozen-state promise, nearest-match datetime negotiation, rewriting/banners as standard practices) describe the Type's rules directly.

Everything commonly associated with the dominant product — crawler harvesting at web scale, the `/web/<timestamp>/<url>` URL grammar, calendar UIs, save-page-now buttons, full-text search, analytics — is implementation or common-mature structure, not definition. The Type holds across a global public crawler archive, an on-demand snapshot service, national curated archives with embargo rules, self-hosted replay software, a local serverless viewer over WARC/WACZ files, and a user-driven capture-and-revisit service.
