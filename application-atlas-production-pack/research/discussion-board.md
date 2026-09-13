# Research Notes — Discussion Board

Research date: 2026-09-07

## Research Goal

Understand the Application Type "Discussion Board" (directory leaf under 01.06 Community & Discussion) from real products: what its defining structure is, how discussion actually works, how it differs from neighboring Types (Online Forum, Q&A Community, Community Platform, chat/messaging), and whether the leaf is independent or an alias of Online Forum.

## Initial Boundary (hypothesis before research)

- Core use: asynchronous, persistent, topic-organized group discussion (a participant opens a topic; others reply over time; the thread remains readable).
- Likely users: interest-community members, course students/instructors, organization teams, product user communities.
- Nearest neighbors: Online Forum (most confusable — possibly the same market family), Q&A Community, Community Platform, Interest Community Platform, Group Messaging / Community Chat (real-time vs asynchronous).
- Known unknowns: (1) is "Discussion Board" separable from "Online Forum" at all; (2) how deep the LMS-embedded "discussion board" pole (grading, pedagogical rules) diverges; (3) whether mailing-list-style groups belong here.

## Research Questions

1. What are the core objects (board/space, topic/thread, post/reply, participant) and how do they relate?
2. What is the canonical discussion workflow (start topic → reply → … → terminal states)?
3. What topic/thread states and lifecycle rules exist (open/closed/pinned/locked/archived, draft/scheduled)?
4. How is the topic space organized (category trees vs tags vs course context)?
5. Who governs the space (moderators, permissions, trust systems) and what rules matter?
6. Which capabilities are defining vs common vs variant (Q&A machinery, grading, polls, email integration, chat)?
7. Where is the boundary with Online Forum, Q&A Community, Community Platform, and chat Types?

## Representative Products

Selected for market representability + documentation quality + different product philosophies + different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| Discourse | modern standalone/hosted discussion platform (open-source core + commercial hosting) | current market leader in open-source discussion software; self-described "community and forum software" |
| XenForo | classic commercial self-hosted forum software | direct descendant of the classic forum/bulletin-board lineage; rich admin manual |
| Canvas LMS (Discussions) | LMS-embedded discussion board (education) | the "discussion board" term is native to this pole; adds grading/pedagogy machinery |
| Flarum | minimal open-source forum, extension-driven | opposite philosophy to XenForo: minimal core, tags instead of category trees |

Rejected/abandoned samples (access failures, see Sources): phpBB (403), Google Groups (timeouts), Blackboard Learn help (dead URL), Moodle docs (403), vBulletin docs (403), MyBB docs (404 on structure pages).

## Sources

Fetched 2026-09-07:

- Discourse — https://www.discourse.org/ (positioning, features) ; https://www.discourse.org/about (mission, trust system, open source) ; https://docs.discourse.org/openapi.json (official API reference: topics, posts, categories, tags, groups, PMs, notifications, admin actions)
- XenForo — https://xenforo.com/docs/xf2/manual/ (admin manual index) ; raw docs repo: https://raw.githubusercontent.com/xenforo-ltd/docs/main/docs/manual/forums/discussions.mdx ; .../nodes-forums.mdx ; .../forum-thread-types.mdx ; .../questions.mdx
- Canvas LMS — https://canvas.instructure.com/doc/api/discussion_topics.html (official Discussion Topics API)
- Flarum — https://docs.flarum.org/ (About) ; https://docs.flarum.org/admin (Admin Dashboard)

Access limitations encountered (recorded per source-access rules):

- phpBB.com docs: HTTP 403 on two paths → abandoned; classic open-source pole covered instead by XenForo (commercial) + Flarum (open-source).
- support.google.com/groups: request timeouts on two URLs → abandoned; mailing-list-style groups pole NOT directly evidenced; treated structurally only, no product claims.
- help.blackboard.com legacy discussion-board URL: redirects to a multilingual search shell (content dead) → abandoned; LMS pole covered by Canvas API docs instead.
- docs.moodle.org: 403 twice → abandoned.
- vbulletin.com/docs: 403 → abandoned. docs.mybb.com structure pages: 404 → abandoned.
- Consequence: no precise numeric limits (post lengths, rate limits, trust-level thresholds, retention windows) are asserted anywhere; all such detail stays out of both files.

## Product A — Discourse (modern standalone/hosted discussion platform)

Evidence layer: A (official site + official API reference).

Key observations:

- Self-positioning: "the community platform powering more than 22,000 communities that create knowledge through conversation"; FAQ: mission is "delivering the best community and forum software"; founded 2013 to "bring thoughtful conversation back to the internet"; "If you want the conversation forgotten, put it on Slack. If it matters, put it on Discourse" (customer quote used in official marketing) — persistence-vs-chat is the vendor's own articulation of the Type's value.
- Object model (API): Topic (id, title, slug, category, tags) containing Posts (post_number within topic, reply_to_post_number, like actions, score, quote counts, incoming links); Categories with subcategories; Tags and tag groups; Groups; Private messages are topics addressed to users/groups ("Required for private message, comma separated"); Invites (link/email, expiry); Notifications; Search; Uploads.
- Topic lists: `/latest.json`, `/top.json`; ordering options include activity, views, posts, category, likes.
- Topic status machine: closed / archived / pinned / unpinned / visible (update-topic-status endpoint); topic timers ("Create topic timer", with based_on_last_post) — scheduled auto-actions on topics.
- Moderation/governance: admin user actions include silence, suspend, anonymize; posts have "reviewable" state (flagged-post review queue); trust system ("the community builds a natural immune system… the most engaged forum members can assist in the governance of their community"); badges (gold/silver/bronze types).
- Communication surfaces: open discussions (topics), built-in real-time chat, private messages/DMs, and email ("Connect with your community using open discussions, chat, private messages, or straight from email").
- Q&A support: "Community can upvote helpful posts/answers"; "Keep technical discussions organized with categories, tags, and accepted answers" (support-hub and developer-community use cases on the official site).
- Other: SSO/SAML enterprise auth; gamification features; SEO emphasis; AI plugin (topic/chat summarization, toxicity detection, message composition); themes/plugins; self-host or managed hosting; external_id/embed URL for using Discourse as a comments system for external blogs.

## Product B — XenForo (classic commercial self-hosted forum)

Evidence layer: A (official admin manual, raw docs repo).

Key observations:

- Terminology: the whole site is a "board" (admin option "Board active > Inactive board message"); structure units are "nodes" — "XenForo's equivalent to forums and categories in other forum software packages".
- Node tree: single tree, parents/children, arbitrary nesting, display order, drag-and-drop sorting. Node types: (1) Categories — containers for other nodes; (2) Forums — "contain threads and posts, the primary content type"; (3) Link forums/redirects; (4) Pages (static HTML in the tree). Recommended setup: categories at top, content forums beneath.
- Thread/post model: "The basic structure of a forum is a container for threads, those being a collection of posts". Discussion threads: original post first, replies sequential, pagination by post count ("if a forum is set to display 20 posts per page…"). Discussion forums list threads ordered by last-reply date.
- Forum and thread types (v2.2+): discussion threads (default), poll threads (multiple-choice vote attached to a thread), article threads (first post made prominent), question threads (any number of answers + one accepted solution), suggestion threads (idea + votes). Mixed-type forums allow several thread types. Thread-type-aware care when moving threads between forums.
- Question/solution mechanics: first post is the question, displayed at top of every page; replies are answers; permitted users vote on answers; thread is "unsolved" until one answer is selected as the solution (by thread author if permitted, else moderator/admin); solution displayed at top; solved icon in forum listing; question forums have filters (Unsolved, Your questions, Your answers).
- Permissions: per-node permissions per user or per group; inheritance from parent nodes; "if a user cannot view a parent node, they will never be able to view any children"; private nodes (staff-only example worked through in the manual); node-specific moderators (inherit to child nodes); paid-subscription forums ("create forums to which your users may pay to subscribe").
- Thread list filters: no-response threads, date ranges, etc.

## Product C — Canvas LMS Discussions (LMS-embedded pole)

Evidence layer: A (official Discussion Topics API documentation).

Key observations:

- Context-bound topics: discussion topics live in a course or a group ("API for accessing and participating in discussion topics in groups and courses"). There is no site-wide board tree; the container is the course (or group).
- Topic object: title, HTML message body, posted_at, last_reply_at, discussion_subentry_count, read_state, unread_count, subscribed.
- Reply structure: entries (top-level) + replies to entries; `discussion_type`: 'threaded' (fully threaded) vs 'side_comment'/'not_threaded' (one level of nesting only).
- Grading: `assignment_id` — "the unique identifier of the assignment if the topic is for grading"; graded discussions are assignments (create with assignment parameters, points possible); group discussions via `group_category_id` (each group gets its own copy of the topic; root_topic_id links back).
- Pedagogical rules: `require_initial_post` — "a user may not respond to other replies until that user has made an initial reply"; subscription holds explain why a user cannot subscribe ('initial_post_required', 'not_in_group_set', 'not_in_group', 'topic_is_announcement').
- Topic lifecycle: published (draft state; only teachers/TAs can create drafts), delayed_post_at (scheduled publish), lock_at (scheduled lock), locked ("closed for comments"), pinned (listed in "Pinned Discussion" section), reorder of pinned topics.
- Special types: `is_announcement` (announcements section; requires announcement-posting permission; can disable commenting); section-specific announcements.
- Read state: per-entry read/unread, forced_read_state (manually marked unread), unread counts, mark-topic-read endpoints.
- Ratings: allow_rating, only_graders_can_rate ("grade permissions are required to rate entries"), sort_by_rating (deprecated).
- Anonymity: entry author name "or null for anonymous topics when the author is not an instructor" — anonymous discussions exist; deletion clears user_id and message ("marked deleted").
- Attachments/media: file attachments on entries; podcast feeds for topics (podcast_url; optionally include student posts).
- Module integration: topics can be locked by module progression for students; topics can be duplicated; AI discussion summaries (generate/feedback with usage limits — era-common).

## Product D — Flarum (minimal open-source forum, extension-driven)

Evidence layer: A (official docs) — thinner than others; observations limited to what docs state.

Key observations:

- Self-positioning: "a delightfully simple discussion platform for your website… fast, free, and easy to use, with all the features you need to run a successful community. It's also extremely extensible." Successor of esoTalk and FluxBB (both classic lightweight forum software); MIT license; volunteer-governed.
- Philosophy: "No clutter, no bloat"; core is deliberately minimal; capabilities arrive as extensions ("manage your Extensions (including the flarum core extensions such as Tags)").
- Organization: the docs describe no category/forum tree in core; the organizing layer shipped with core is Tags (bundled extension). (Observation from the docs' own structure; treated as product-specific.)
- Governance: Admin Dashboard restricted to the "Admin" group; Permissions page configures "permissions for each user group… global and specific scopes"; Users list with administrative actions; basics (name/description/welcome banner), appearance, email config, maintenance mode, search drivers.
- Community site itself runs as a discussion board (discuss.flarum.org) with discussions referenced by numeric IDs (d/28869-style URLs).

## Cross-product Comparison

| Aspect | Discourse | XenForo | Canvas Discussions | Flarum |
|---|---|---|---|---|
| Unit of discussion | Topic (OP + posts) | Thread (OP + posts) | Discussion topic (OP + entries/replies) | Discussion (posts) |
| Standing space holding topics | Site with categories (+subcategories) & tags | Node tree (categories → forums) | Course or group context | Site with tags (bundled extension) |
| Reply structure | sequential posts + reply-to links | sequential posts, paginated | threaded OR one-level (side_comment) | sequential posts |
| Authorship | registered users (username identity) | registered users (groups) | enrolled users; anonymous topics supported | registered users (groups) |
| Persistence | permanent, searchable archive | permanent | permanent within course lifetime | permanent |
| Read/unread tracking | yes (new/latest/unread lists) | yes (new posts, filters) | per-entry read state, unread counts | yes |
| Notifications/subscriptions | topic watching/tracking, emails | watched threads, alerts | topic subscriptions (with holds) | notifications |
| Search | site search over topics/posts | search system | search_term on topic lists | search drivers (pluggable) |
| Moderation | staff tools, reviewables, silence/suspend, trust system | node moderators, staff, soft management | teacher/TA permissions, delete clears author | group permissions, admin actions |
| Topic states | closed/archived/pinned/visible + timers | sticky/locked/deleted (thread management) | draft/published, delayed post, lock_at, locked, pinned | sticky/locked/deleted (via core/extensions) |
| Organization layer | categories + tags | node tree (categories/forums) | course/group context (no board tree) | tags |
| Q&A machinery | upvotes + accepted answers (use-case documented) | question threads + solution (native) | absent | via extensions |
| Grading | absent | absent | native (assignment-linked, points, group discussions) | absent |
| Polls | plugin ecosystem | native poll threads | absent (separate Polls resource) | via extensions |
| Private 1:1/small-group messaging | private messages (topics addressed to users/groups) | conversations (starter docs) | separate Conversations resource | via extensions |
| Email integration | reply/participate "straight from email" | — (not observed in fetched pages) | notifications | mail configuration |
| Real-time chat | built-in chat channels | — | — | — |
| Paid access to boards | commercial hosting plans | paid-subscription forums | institutional licensing | free/open-source |
| AI assistance | Discourse AI (summaries, toxicity, composition) | — | discussion summaries (usage-limited) | — |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

A Discussion Board is a standing shared space where identified participants open topics and append asynchronous replies that remain persistently readable:

```text
Standing shared discussion space (holds many topics)
└── Topic opened by a participant (seed post)
    └── Asynchronous replies appended by participants over time
        └── Persistent readable thread (topic + replies survive sessions)
Posts carry displayed authorship (attributed participation)
```

Five properties. Remove any one and the Type collapses into something else:

- no standing multi-topic space → a single comment thread / guestbook, not a board
- no participant-opened topics → an announcement feed
- no asynchronous reply structure → a stream/chat
- no persistence → ephemeral live conversation
- no attribution → anonymous comment pool

Historical/market-sample check: Usenet newsgroups, mailing lists, BBS message areas, phpBB/vBulletin-era web forums, and 1990s LMS discussion boards all satisfy this core — none require category trees (a mailing list is one space), web UIs (Usenet was NNTP), central registration, moderation, or reputation. The core therefore survives the check; everything modern below is L1/L2.

### L1 — Common Mature Structure (very common, not defining)

- Organization layer for topics: category/forum trees (XenForo nodes, Discourse categories+subcategories) or tag systems (Flarum) — the shape varies, the layer is near-universal in mature products
- Member accounts, profiles, avatars; user groups/roles
- Topic lists with ordering and filters (latest, top, unread, unanswered); read/unread tracking
- Notifications and topic subscriptions/watching
- Search over topics and posts
- Moderation toolkit: edit/move/merge/split/close/pin/lock/delete (often soft-delete), flagged-content review queues
- Rich-text posts with attachments, images, quotes, reactions/likes
- Reputation/rank/trust systems and badges
- Polls attached to topics
- Private messaging between members (separate from public topics)
- Email integration (reply-by-email, digests, invites)

### L2 — Variant / Optional Structure

- Q&A machinery: question-type threads with accepted solutions and answer voting (native in XenForo; documented use-case capability in Discourse; absent in Canvas)
- Grading/pedagogy machinery: assignment-linked graded discussions, points, rubric/peer-review linkage, group discussions, require-initial-post rules, section scoping (Canvas; absent in forum products)
- Special topic types: announcements, article threads, suggestion/idea threads with votes
- Anonymous posting modes (Canvas anonymous topics)
- Access economics: paid-subscription forums (XenForo), commercial hosting tiers (Discourse), institutional licensing (Canvas)
- Real-time chat alongside topics (Discourse built-in chat)
- Mailing-list interoperability (reply-by-email as first-class participation; Google-Groups-style groups — NOT directly evidenced in the fetched sample; structural inference only)
- Deployment posture: self-hosted open source vs vendor-hosted SaaS vs LMS-embedded module
- AI assistance (summaries, toxicity detection, composition)
- Enterprise auth (SSO/SAML), gamification, SEO posture

### L3 — Vendor-specific (kept out of the final document)

- Discourse: trust levels, reviewables, topic timers, Discourse Hub app, "Civilized Discourse Construction Kit" naming, external_id/embed for blog comments
- XenForo: "node" terminology, link-forum/page node types, thread prefixes/fields/prompts, suggestion threads, RSS thread importer
- Canvas: module-progression locks, sections, podcast feeds, discussion-summary usage limits, masquerading
- Flarum: extension architecture details, bundled-extension list, console/queue drivers

## Vendor-specific Findings

See L3 above; none of these entered the canonical model. Notable drift signal: Discourse now markets itself as a "community platform" (support hub / workplace collaboration / product feedback / developer community use cases) while its FAQ still self-identifies as "community and forum software" — evidence that the standalone forum product family is being repositioned upward into the Community Platform neighborhood without changing its discussion core.

## Boundary Findings

1. **vs Online Forum — the load-bearing ambiguity.** The standalone products sampled (Discourse, XenForo, Flarum) are exactly the market family "Online Forum" would describe; in common usage "discussion board", "message board", "forum", and "bulletin board" are near-synonyms. The only defensible distinction found: Discussion Board names the *discussion surface/tool* (topic+reply machinery), which also exists embedded in host contexts without any public community venue — the LMS pole (Canvas) is a discussion board inside a course, with no site identity, no member community, no ranks. Online Forum names the *standing public community venue* built from boards (member base, public identity, moderation culture). Overlap is large: every standalone forum product instantiates both. → Recorded in STATUS.md as a boundary issue; recommend joint review / possible merge of the two leaves.
2. **vs Q&A Community.** Q&A makes the question/answer/accepted-answer structure the primary organizing principle (plus voting). In a Discussion Board, Q&A machinery is a thread-type variant (XenForo question threads; Discourse accepted answers). If a product's topics are predominantly questions with solutions and voting, it has crossed into Q&A Community.
3. **vs Community Platform.** Community platforms add member management, events, content/courses, monetization, and multi-surface engagement around the discussion core. Discourse's own repositioning illustrates the drift; the discussion core (topics+replies+persistence) remains the seam.
4. **vs Group Messaging / Community Chat.** Chat is real-time, stream-organized, and (in practice) ephemeral-in-attention; the board is asynchronous, topic-structured, and persistent-by-design. Discourse's own marketing articulates the seam ("if it matters, put it on Discourse"). Discourse shipping built-in chat shows the boundary is porous at the product level but structurally intact.
5. **vs Social Network / feed Types.** The board's unit is the topic in a shared space; the social network's unit is the person/profile with a follow graph and a feed. Boards may have profiles, but navigation is topic-first.
6. **vs comment sections / reviews.** Comments attach to a content item (article, product); a board is a standing venue that exists before and between any single content item.

## Uncertainties

- Mailing-list-style groups (Google Groups class) could not be fetched; their inclusion/exclusion in this Type is a structural inference (they satisfy L0), not product-evidenced. No claims made about their specific mechanics.
- phpBB/vBulletin/Blackboard/Moodle specifics unverified (access denied); the classic-forum pole rests on XenForo's manual, which explicitly positions itself in the same lineage ("forums and categories in other forum software packages").
- Flarum evidence is thinner (docs are admin/extend-oriented); its tags-vs-categories contrast is an observation from its documentation structure, marked product-specific.
- Exact numeric behaviors (post-length limits, rate limits, trust-level thresholds, pagination sizes, retention) were deliberately not asserted anywhere.
- Whether the directory intends "Discussion Board" and "Online Forum" as distinct Types could not be determined from products alone; escalated to STATUS.md.

## Final Synthesis

The Discussion Board is best understood as **the asynchronous, persistent, topic-structured group discussion application**: a standing space holds participant-opened topics; participants append attributed replies over time; threads remain readable and searchable. Around this minimal core, mature products add an organization layer (categories or tags), member accounts and groups, read-state and notifications, search, moderation tooling, reputation, polls, private messaging, and email participation. Two large variant families extend the core in different directions without changing it: **Q&A machinery** (question threads, solutions, voting) and **teaching machinery** (graded discussions, initial-post rules, group discussions). The Type's hardest boundary is terminological, not structural: standalone forum products are simultaneously "discussion boards" and "online forums"; the leaf distinction, if kept, must rest on discussion-tool-vs-community-venue emphasis, and the taxonomy question is escalated.
