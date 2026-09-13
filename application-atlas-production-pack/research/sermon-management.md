# Research Notes — Sermon Management

## Research Goal

Understand what "Sermon Management" software is as an Application Type: what the sermon is as a managed object, what the core workflow is (preparation → record → library → availability), how products package this (standalone platforms, prep apps, ChMS modules, app/site surfaces), and where the boundaries sit against Podcast Platform, Media Asset Management, Church Website Builder, Worship Planning, Worship Presentation Software, Scripture Study Application, ChMS, and live streaming.

## Initial Boundary

- Leaf: Sermon Management (§25 Nonprofit, Membership & Religious Organizations), slug `sermon-management`.
- Working hypothesis: the church's system for managing its sermons as records — capturing/collecting sermon content, cataloging it with sermon-specific metadata, accumulating a sermon library, and making the message available beyond the live service (website library, podcast, app; historically physical media). A second pole (sermon preparation/writing) shares the sermon record.
- Nearest neighbors: Podcast Platform (§27), Media Asset Management (§27), Church Website Builder (§25, processed — seam already held: "site display object vs record workflow"), Worship Planning (§25, unprocessed), Worship Presentation Software (§25, unprocessed), Scripture Study Application (§25, processed), Church Management System / ChMS (§25, processed), Video Streaming Platform (§26).
- Known unknowns at start: whether prep-side products belong to this Type or a separate one; whether publication is definitional or common; whether the Type survives without recordings (manuscript-only).

## Research Questions

1. What is a "sermon" as an object in these systems — what metadata and what content forms?
2. What is the lifecycle: how does a sermon enter the system, and what happens to it after the service?
3. What does the "library" look like (organization, retrieval, series/speaker/scripture)?
4. What distribution/publication channels exist, and are they definitional or variant?
5. Is sermon preparation (writing the message) part of this Type or a different one?
6. How do ChMS products, church apps, church website builders, and streaming products each carry a slice of this?
7. What rules/behaviors matter (ownership posture, content forms, access, trim/segment)?
8. Where exactly are the boundaries with the neighboring Types listed above?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer tiers:

| Product | Pole | Status this pass |
|---|---|---|
| sermon.net | standalone sermon broadcast/archive platform (sermon-first media hosting) | REACHABLE — root + outreach-tools pages (Tier-2) |
| Sermonary (by Ministry Pass) | sermon preparation/writing application | REACHABLE — root + editor + multiply pages (Tier-2) |
| One Church Software | ChMS with a named "Sermon Archive" feature (module pole) | REACHABLE — root + features + vs-Subsplash comparison (Tier-2) |
| Tithe.ly (Church App / Sites) | sermon surfaces inside church app/website products | REACHABLE — root + church-app product page (Tier-2) |
| BoxCast | live-streaming platform (boundary anchor: streaming-first, VOD archive as byproduct) | REACHABLE — root (Tier-2) |

Market anchors observed but NOT usable for operational claims this pass:

- SermonAudio — sermonaudio.com + support.sermonaudio.com returned 403 ×3 (abandoned per source-access rule). Existence as a major sermon platform is market context only; no operational claims drawn.
- Subsplash — subsplash.com + help.subsplash.com timed out ×2 (abandoned). Its media-platform positioning is documented only second-hand via One Church Software's own comparison page ("known for its church apps and multimedia… Media, apps, streaming, and giving first").
- Faithlife / Logos Sermons / Proclaim — sermons.logos.com, faithlife.com/sermons, proclaimonline.com all unreachable (timeouts/transport error ×2). Prep+publish pole partially covered by Sermonary instead.
- WordPress "Sermon Manager" plugin (wpforchurch, published 2011) — plugin page reachable; plugin closed Dec 2025 (security issue); readme/Trac 429+403. Used only as evidence that a self-hosted CMS-plugin realization of the sermon archive existed, not for feature claims.
- Sharefaith (Ministry Brands) — reachable root: church websites "engage members with sermons", streaming product "schedule, edit, & archive" — thin sermon-management evidence, used as packaging context.
- Elvanto (Tithe.ly ChMS) — help center search for "sermon" returns only service-planning usages (sermon as a section of a service plan) and app push notifications for "new sermon uploads" — evidence that at this vendor the sermon record lives on the app/media side, not the ChMS core.

## Sources

Fetched 2026-09-09:

- sermon.net — https://www.sermon.net/ (root: positioning, FAQ, plans) ; https://www.sermon.net/outreach-tools-apps (network app, custom-branded apps, Roku channel)
- Sermonary — https://sermonary.com/ (root) ; https://sermonary.com/editor/ (blocks editor, slide export, AI assistant) ; https://sermonary.com/multiply/ (derivative content)
- One Church Software — https://onechurchsoftware.com/ (root) ; https://onechurchsoftware.com/features/ (Sermon Archive feature) ; https://onechurchsoftware.com/one-church-software-vs-subsplash/ (Subsplash positioning, second-hand)
- Tithe.ly — https://get.tithe.ly/ (root/product nav) ; https://get.tithe.ly/product/church-app (sermon streaming/archives/downloads FAQ)
- BoxCast — https://www.boxcast.com/ (root)
- Sharefaith — https://www.sharefaith.com/ (root)
- Elvanto — https://www.elvanto.com/ (root) ; https://help.elvanto.com/hc/en-us/search?query=sermon (3 results)
- WordPress.org — https://wordpress.org/plugins/sermon-manager-for-wordpress/ (plugin closed notice, reviews, metadata)

Unreachable (recorded limitations): sermonaudio.com (403 ×3), subsplash.com + help.subsplash.com (timeout ×2), sermons.logos.com + faithlife.com/sermons (timeout ×2), proclaimonline.com (transport error), wpforchurch.com (domain squatted — spam site), sermondrop.com (timeout), plugins.svn.wordpress.org (429) + plugins.trac.wordpress.org (403).

Evidence quality note: all reachable sources are Tier-2 (official product/marketing pages). No Tier-1 help-center article bodies were fetched for any sampled product (help centers either unreachable or not attempted after root pages proved rich). All operational claims below are calibrated accordingly; no precise numeric limits, retention windows, or default settings are asserted anywhere.

## Product A — sermon.net (standalone broadcast/archive pole)

Key observations (Layer A, official product pages):

- Self-positioning: "Stream, Share, and Store Your Sermons Without Concern… Stream live, store forever, and share everywhere—without ads or restrictions… your church owns its content, ensuring sermons remain accessible anytime, anywhere." Tagline: "Moving the Messages to Millions since 2005."
- The church-side console is called "Sermon Studio" (login at sermonstudio.net) — the broadcaster account.
- Content forms archived: "Live Stream and archive your Audio, Video, & PDF files" (plan feature line). Storage-quota plans (25/100/300 GB tiers with overage pricing) — pricing detail kept out of the final document.
- Recording pipeline: "Record your live streams and archive them in various formats, trimming them to show only the message portion, for example" — the service recording is trimmed down to the sermon.
- "Reshare archived content to give viewers access to past sermons and events at their convenience."
- Distribution surfaces: podcast feeds ("Your sermons can automatically publish to Apple Podcasts, Google Podcasts, Spotify, and Roku"), website/landing page under the church's own domain, mobile apps (a free shared "Sermon Network App" every ministry is included in, plus paid custom-branded apps), Roku/TV channel, and simulcast to Facebook/YouTube.
- Consumer side: "Looking for Your Church or Pastor? Watch or listen to any ministry using sermon.net - for free! No account needed." — a platform-level directory of ministries; viewers follow/subscribe and get "We're Live" notifications.
- Ownership posture is the pitch: ad-free, no third-party ads/algorithms/censorship, "own your platform" (branded "Sermon Shield").
- Account-lifecycle policy (FAQ): if the church stops paying, media becomes inaccessible and inactive accounts are eventually purged; export-on-request offered for a fee. Vendor-specific policy — research notes only.

## Product B — Sermonary (prep/writing pole)

Key observations (Layer A, official product pages):

- Self-positioning: "The Simple Sermon Builder — An all-in-one sermon app that makes preparing and preaching a sermon easier than ever before." "Created by pastors, for pastors."
- The sermon is a structured document: "Drag and Drop Sermon Editor" with typed content blocks — Bible Verses ("your favorite Bible translations built into our editor"), Sermon Points, Illustrations, Application, Media, Custom blocks (savable as templates).
- "Build your sermons from ideas to distribution."
- Delivery support: "Podium Mode — Preach without distractions… deliver your message seamlessly" (preaching from the notes in-product).
- Slide bridge: "One-click slide creation — mark your content as slides as you go. Exporting your selected presentation slides… Powerpoint… ProPresenter" — the sermon document feeds worship-presentation software.
- Research support: Research Suite (commentaries, cross-references, notes), Illustrations library, Template Library (Traditional 3-point, Funeral, Apologetics, Verse-by-verse, Wedding ceremony…).
- Aftermath/repurposing: "Multiply — Turn One Sermon Into a Week of Discipleship… generate ready-to-share devotionals, group questions, posts, and more directly from your sermon": 5 small-group questions, 5 daily devotionals, a ~200-word blog/newsletter recap, social posts, a summary. Framing: "Preach Once. Impact All Week." / "Your Sermon Isn't Meant To Last One Day."
- AI assistant: clarity editing, illustration suggestions, "Repurpose With Ease — Transform your sermon into a blog, devotional, or other impactful content."
- Sharing/collaboration feature exists (sharing page in nav); offline editing on desktop claimed ("works without internet on any desktop or laptop").

## Product C — One Church Software (ChMS module pole)

Key observations (Layer A, official features page):

- Named feature: **"Sermon Archive — Store all your sermons in one place. Keep your audio and video Bible teaching organized and make it accessible for others to enjoy."**
- "We integrate with YouTube and Vimeo for video hosting" — the hosting substrate can be third-party platforms; the sermon record stays in the ChMS.
- "Add teaching aids to your message" — attachments beyond the recording.
- "Members can save their notes from each sermon" — per-sermon member notes.
- "Easily embed messages on your church website" — website library as an output surface.
- The rest of the product is a full ChMS (people, giving, check-in, groups, accounting, service planning with "Detailed Orders of Service") — the sermon archive is one feature among many, not the center.

## Product D — Tithe.ly (church app/sites surfaces)

Key observations (Layer A, official product pages):

- Church App feature list: "Sermon Streaming and Archives — Allow members to watch live sermons or catch up on past messages anytime."
- App FAQ: the app can be "packed with… sermon audio and video, blogs, daily devotional, events, Sunday bulletins, newsletters, online giving, and more."
- Offline consumption: "Can people download sermons to their phone? Yes, your audience can download sermons and other media directly to their smartphone or tablet and play them without needing an internet connection."
- The app newsfeed "aggregates much of your church content such as events… blog posts, sermons and media, and push notifications."
- Sites product page lists "Sermon media player" as a website capability.
- Notably, the current product nav has no standalone "Media" product; sermon surfaces live inside Church App and Sites. Elvanto (Tithe.ly's ChMS) help center has no sermon-archive documentation — only sermon as a service-plan section and "new sermon uploads" as an app push-notification trigger. At this vendor the sermon record is app/media-side, not ChMS-core.

## Product E — BoxCast (streaming boundary anchor)

Key observations (Layer A, official root page):

- Center is live streaming ("The Platform That Powers Live Production… Stream brilliantly"), with OTT apps, encoders, audio mixing, and a website builder.
- House of Worship is one vertical among several (sports, government, business) — not sermon-shaped.
- Content sharing exists ("Instantly clip, share, and amplify your broadcasts") and broadcasts are recorded, but the object model is the broadcast/event, not the sermon record with sermon metadata.
- Used only as a boundary anchor: streaming-first products drift toward Video Streaming territory; the sermon library is what makes a product sermon management.

## Cross-product Comparison

| Dimension | sermon.net | Sermonary | One Church Software | Tithe.ly (App/Sites) | BoxCast |
|---|---|---|---|---|---|
| Sermon as unit of record | yes — archived message (audio/video/PDF) with trim-to-message | yes — sermon document (blocks: scripture, points, illustrations) | yes — "Sermon Archive" entries (audio/video + teaching aids) | yes — sermons as app/site content | no — broadcast/event is the record |
| Sermon-specific metadata | implied (title/ministry; directory listing) | scripture, points, sermon type via templates | audio/video Bible teaching; teaching aids | sermon audio/video items | none (event metadata) |
| Library/archive | "store forever", reshare archived content | pastor's sermons + template library | "store all your sermons in one place" | archives in app | VOD archive of broadcasts |
| Availability beyond the service | podcast feeds, website, network app, custom apps, Roku, FB/YT simulcast | Multiply (devotionals, group questions, recap, social), sharing | website embed, member access | app streaming + offline downloads, site player | clip/share of broadcasts |
| Live capture | live stream → record → trim → archive | n/a (prep-side) | n/a (upload/integrate) | "watch live sermons" in app | live streaming is the center |
| Prep support | none observed | full (editor, research, templates, podium) | none observed | none observed | none |
| Packaging | standalone platform | standalone app | ChMS feature | app/site product surfaces | streaming platform |
| Consumer access | free, no account, directory + follow | pastor-side (content handed to congregation via outputs) | members + website visitors | app users + site visitors | viewers |

Layer B (cross-product commonality) readings:

- The sermon as a persistent, individually identified record with sermon-specific identity is present in every sermon-centered sample member (4/4 sermon-centered products; BoxCast excluded as boundary anchor).
- An accumulating library/archive is present in all sermon-centered products ("store forever", "store all your sermons in one place", app "archives", pastor's sermon list).
- Availability beyond the live service is present in all sermon-centered products, realized through different channel sets (podcast/app/website/TV vs derivative content).
- Content forms vary: audio, video, PDF, manuscript/notes — no single form is universal.
- Series organization: NOT directly evidenced in any fetched page this pass (no fetched page shows a series object). Held as market-common from general category knowledge but UNVERIFIED this pass — kept out of definitional claims; noted as uncertainty.
- Podcast feed generation: directly evidenced at sermon.net only; strongly implied by the category. Held common-mature, not definitional (channel set varies; OCS embeds website; Tithe.ly uses app; historical pole predates podcasting).
- Member notes per sermon: single-product (OCS) — optional.
- Teaching aids attached to messages: single-product (OCS) — optional.
- Derivative-content generation: single-product (Sermonary Multiply) — optional/era-current.
- Analytics/play counts: NOT evidenced on any fetched page — unverified this pass, not claimed.

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The sermon as the unit of record** — a persistent, individually identified record of one sermon (a specific message prepared and/or preached in the church's life), carrying sermon-specific metadata — title, speaker, date/service occasion, typically the scripture passage, commonly series membership — and the message's content (a recording — audio/video — and/or notes/manuscript, commonly with attached materials).
   - Remove → a generic media library, a file store, or a plain writing tool; nothing sermon-shaped remains.
2. **The sermon library as the church's archive of record** — sermon records accumulate into an organized, retrievable collection (browsable by date, speaker, scripture, series) that is the church's preaching record over time.
   - Remove → one-off uploads with no memory; the archive-of-record value dies.
3. **The message carried beyond the service** — the sermon record (or its content) is made available outside the live preaching moment: published through distribution channels the product operates or feeds (website library, podcast feed, church app, TV apps; historically physical media such as duplicated tapes/CDs and mailed copies), and/or transformed into derivative content for the congregation (devotionals, group questions, recaps, social posts).
   - Remove → a private archive nobody can reach, or a writing tool with no afterlife; the Type's purpose ("the message keeps working after Sunday") dies.

Jointly-held load-bearing analysis:

- 1 alone = a media file with metadata / a sermon document — a catalog entry, not management.
- 2 without 1 = a folder of recordings / a pile of manuscripts.
- 3 without 1+2 = a podcast host or generic publishing platform.
- 1+2 without 3 = a private archive — conceivable as a degenerate posture but not productized by the market; recorded as a note, not a claimed impossibility.
- 1+3 without 2 = one-off uploads with no library memory.
- 2+3 without 1 = a generic media/content library with no sermon shape.

### L1 — Common Mature Structure

- Podcast feed generation (RSS) as the dominant distribution realization (directly evidenced at sermon.net; category-standard).
- Website sermon library/player/embed as an output surface (OCS "embed messages on your church website"; Tithe.ly Sites "Sermon media player"; sermon.net website under own domain).
- Church app sermon surface: stream live, catch up on past messages, offline downloads (Tithe.ly).
- Audio/video hosting with player; multiple content forms per record (audio/video/PDF at sermon.net; audio/video + teaching aids at OCS; manuscript blocks at Sermonary).
- Trim/segment of captured service recordings down to the message (sermon.net).
- Search/browse over the library by sermon metadata.
- Speaker attribution and date/service occasion on records.
- Scripture passage as record metadata (directly evidenced at Sermonary blocks; implied by "Bible teaching" at OCS).
- Delivery support at the prep pole: podium/presenter mode, slide export to presentation software (Sermonary).
- Consumer access without accounts (sermon.net "No account needed"; Tithe.ly app downloads).

### L2 — Variant / Optional Structure

- Content-form emphasis: audio-only vs video vs manuscript-first (prep pole) vs PDF notes.
- Capture path: live-stream auto-archive vs manual upload vs in-product authoring.
- Distribution channel set: podcast feeds, website embed, church app, custom-branded apps, TV/Roku apps, social platforms — any subset.
- Hosting substrate: product-operated hosting vs third-party platforms (YouTube/Vimeo integration at OCS; simulcast to Facebook/YouTube at sermon.net).
- Ownership posture: ad-free self-owned platform pitch (sermon.net) vs riding third-party platforms.
- Packaging: standalone broadcast platform / standalone prep app / ChMS module / church-app & site surfaces / CMS plugin (WordPress Sermon Manager) / streaming-platform adjacency.
- Consumer-side discovery: platform-level directory with follow/subscribe (sermon.net network) vs private church-only surfaces.
- Prep-side depth: research suite (commentaries, cross-references), template/illustration libraries (Sermonary).
- Derivative-content generation, AI assistance (Sermonary Multiply/AI) — era-current, optional.
- Member notes per sermon, teaching aids (OCS) — optional.
- Storage-quota pricing models — commercial variant.

### L3 — Vendor-specific (research notes only)

- sermon.net: Sermon Studio console name; Sermon Network App + directory; Fellowship TV; Sermon Shield branding; reseller program; storage tiers (25/100/300 GB, $0.60/GB overage); inactivity-purge + paid export policy; custom-app pricing ($350/$600 setup lines).
- Sermonary: "Drag and Drop Sermon Editor™", Podium Mode, Multiply, Ministry Pass relationship, 14-day trial.
- One Church Software: "Sermon Archive" feature name; YouTube/Vimeo integration; My One Church member app.
- Tithe.ly: Automatic App Builder (AI), newsfeed aggregation, All-Access bundling.
- BoxCast: BoxCast Flow protocol, Spark encoder, Mixing Station, OTT apps.
- Sharefaith/Ministry Brands: suite packaging (Media = graphics library, not sermon management); streaming product's "schedule, edit, & archive".

## Vendor-specific Findings

See L3 above. Additional posture findings:

- sermon.net's entire pitch is ownership/control versus third-party platforms (ads, algorithms, censorship) — a positioning axis, not a Type structure.
- One Church Software's comparison page positions Subsplash as "media, apps, streaming, and giving first" with "newer, lighter" ChMS — second-hand evidence (Layer A for OCS's claim about the market, Layer C at best for Subsplash itself).
- Elvanto's help center shows the ChMS↔media split at one vendor: sermon as service-plan section (planning) + "new sermon uploads" push trigger (app side), no ChMS-core sermon archive docs.

## Boundary Findings

1. **vs Podcast Platform (§27)** — the podcast platform centers the show/episode catalog and the listener's subscription; Sermon Management centers the church's sermon record and library. The podcast feed is one output channel of the sermon record (sermon.net: sermons "automatically publish to Apple Podcasts, Google Podcasts, Spotify"). Remove the sermon library/sermon metadata → a podcast host; remove the feed → still sermon management (website/app/channels remain; historical pole predates podcasting). FORWARD FLAG for the podcast-platform pass: sermon-podcast products sit on this seam; expected keep-both on the record-center seam.
2. **vs Media Asset Management (§27)** — MAM holds generic media assets for media organizations; Sermon Management holds sermon-shaped records (speaker, scripture, series, service occasion) for a church. Remove the sermon shape → MAM/file store.
3. **vs Church Website Builder (§25, processed)** — RATIFIED from this side: the church-website-builder pass held the seam as "site display object vs record workflow"; this pass confirms it — website builders embed/consume a sermon library ("Sermon media player", "engage members with sermons"), while Sermon Management produces and operates the record behind it (capture → catalog → publish). Keep-both.
4. **vs Worship Planning (§25, unprocessed)** — worship planning organizes the service occasion (order of service, songs, people); Sermon Management organizes the message as a record. They meet at the service plan's sermon slot (Elvanto docs show "the sermon" as a section of a service plan) and at the prep pole (a prepared sermon feeds the plan). FORWARD FLAG for the worship-planning pass: confirm the occasion-vs-message-record seam; expected keep-both.
5. **vs Worship Presentation Software (§25, unprocessed)** — presentation software displays content live in the service (lyrics, scripture, slides); Sermon Management keeps the message as a record that outlives the service. They meet at slide export (Sermonary → PowerPoint/ProPresenter) and at record-while-presenting products (Faithlife Proclaim — unreachable this pass). FORWARD FLAG for the worship-presentation-software pass: confirm the live-display-vs-record seam.
6. **vs Scripture Study Application (§25, processed)** — scripture study centers the canonical corpus addressed by reference and personal study; Sermon Management centers the church's sermon records. Prep tools borrow study machinery (Sermonary's commentaries/Bibles) as support — the scripture-study pass itself already noted "sermon editors" as optional outputs on its side. Seam holds.
7. **vs Church Management System / ChMS (§25, processed)** — ChMS centers the people/records core (members, households, giving, groups); the sermon archive ships as a module (OCS "Sermon Archive") or lives on the app/media side (Tithe.ly/Elvanto split). Standalone sermon products (sermon.net, Sermonary) prove the independent center. Keep-both on the module↔standalone spectrum.
8. **vs Video Streaming Platform (§26) / live streaming** — streaming centers the live broadcast event; Sermon Management centers the accumulating sermon library. Streaming products auto-archive into sermon libraries (sermon.net does both; BoxCast stays streaming-first with VOD as byproduct). Seam: live event vs the sermon record.
9. **vs Content Management System (§02.07)** — sermon records are content, and the archive can be realized as a CMS content type (WordPress Sermon Manager plugin). The sermon shape (speaker/scripture/series/service metadata + podcast/app distribution machinery + church context) is what makes the Type; CMS-plugin realization is a variant, not a different Type.

## Historical / Market-Sample Check (§24 workflow reference — conceptual)

- **Tape-ministry generation**: churches cataloging sermon recordings (cassettes) labeled with speaker/date/title/series in a tape library, duplicated and mailed to shut-ins, missionaries, and sold/given at the door — satisfies all three L0 legs (sermon record with metadata + content; accumulating library; distribution via physical media) with no podcast/app/website/AI. Conceptual check: passed.
- **Printed-sermon ancestor**: churches printing and distributing sermon transcripts/pamphlets (newsletter inserts, mailed sermon periodicals) — the manuscript-form realization of the availability leg. Conceptual check: passed.
- **Prep-side lineage**: the pastor's sermon manuscript file (filing cabinet of past sermons with date/passenger notes, reused and handed out) — the prep pole's library without software. Conceptual check: passed.
- The definition therefore names no channel set, no media form, no packaging, no AI — all era machinery stays out of the core.

## Uncertainties

1. **Series organization** — universally expected in the category but not directly evidenced on any fetched page this pass; held common-not-definitional, flagged unverified.
2. **Analytics/engagement metrics** (plays, views) — expected in the category but not evidenced on fetched pages; not claimed anywhere.
3. **SermonAudio / Subsplash / Faithlife (Logos) Sermons** — the three biggest sermon-native brands were all unreachable; the media-platform pole is documented only via sermon.net (direct) and OCS's comparison page (second-hand). If a future pass reaches them, re-verify: series objects, podcast machinery depth, transcript features, prep+publish integration (Proclaim → SermonAudio/Faithlife upload loop).
4. **Whether a no-distribution private archive exists as a productized posture** — assumed degenerate, not verified.
5. **Permissions/roles** (who may publish sermons) — not evidenced on fetched pages; not claimed.
6. **Transcription** — expected in the current market but not evidenced this pass; not claimed.

## Final Synthesis

Sermon Management is the church's sermon-record system: the sermon (a specific message, prepared and/or preached) is the unit of record, carrying sermon-specific identity (speaker, date/occasion, scripture, commonly series) and content (recording and/or manuscript); records accumulate into the church's sermon library of record; and the message is carried beyond the live service — published through channels (website library, podcast, app, TV; historically physical media) and/or transformed into derivative content (devotionals, group guides, recaps). The market realizes one Type in two centers of gravity — the archive/broadcast pole (standalone platforms, ChMS modules, app/site surfaces) and the preparation pole (sermon-writing apps whose records flow into delivery and derivative content) — with packaging (standalone vs module vs CMS plugin vs app surface) as a variant axis, not a Type split. The strongest seams are against Podcast Platform (feed as output channel vs show-centered catalog), Church Website Builder (record workflow vs display object — ratified from both sides), Worship Planning (message record vs service occasion), and Worship Presentation Software (record vs live display).
