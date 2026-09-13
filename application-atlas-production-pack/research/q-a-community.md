# Research Notes — Q&A Community

## Research Goal

Understand the Application Type "Q&A Community" (DIRECTORY §01.06 Community & Discussion) from real products: what the defining structure is, how a question becomes a trusted answer, who the participants are, how quality is produced, and where the boundaries lie against the sibling Types already processed (Online Forum, Discussion Board, Community Platform, Interest Community Platform, Private Community Platform, Expert Q&A Platform) and adjacent Types (Answer Engine, Knowledge Question Answering Application, Help Center, Knowledge Base, Audience Response System).

## Initial Boundary

Working hypothesis before research:

- Core: a standing community whose participation is organized around question/answer pairs; open answering; community-produced answer authority (voting / acceptance / reputation); accumulation into a searchable answer archive.
- Nearest neighbors: Online Forum (venue-general — ALIAS-risk recorded by sibling passes), Discussion Board (tool), Community Platform (operated container — format-vs-container seam recorded), Expert Q&A Platform (vetted pool — seam already defined from that pass), Answer Engine / Knowledge QA (human vs algorithmic), Help Center / Knowledge Base (member-generated vs organization-authored), Interest-based Social Network (feed/follow-organized — Quora straddle risk), Audience Response System (session-bound).
- Open questions going in: Is voting/acceptance definitional or a common mechanism? Is a "venue of its own" required (forum seam), or is format enough? Where does Quora actually sit? Do enterprise-internal Q&A deployments stay in-type?

## Research Questions

1. What is the unit of record — question, thread, topic, or Q&A pair? How do answers attach?
2. Who may answer, and how is answer quality/authority produced (vetting vs voting vs acceptance vs ratings vs reputation)?
3. Is there a standing member base, and what identity/reputation machinery do members carry?
4. How do Q&A pairs accumulate and get rediscovered (search, tags/topics, feeds)? Is knowledge reuse a stated product value?
5. What participation lifecycle exists (ask → answer → vote/accept → rank → archive)?
6. Which community structures exist around the Q&A core (profiles, follows, feeds, comments, moderation, editing)?
7. What variants exist (topical scope, regional, enterprise-internal, institutional answerers, monetization, AI layers)?
8. Where exactly are the seams with forum Types, community platform, expert Q&A, answer engines, help centers/KBs, and social networks?

## Representative Products

Selected for market representation + different philosophies + different tiers:

1. **Stack Overflow / Stack Exchange network** — rigid knowledge-engineering pole: voting, accepted answers, reputation, strict topical scope, multi-site topical network. Community pages (stackoverflow.com, stackexchange.com) returned 403; official product/company pages (stackoverflow.co, stackoverflow.blog) were reachable and yielded direct positioning/stat facts.
2. **Baidu Zhidao (百度知道)** — mass-market casual pole (China): ask/answer/adopt loop, points economy, certified answerers, institutional (brand customer-service) answering. Homepage reachable (Tier 2).
3. **Zhihu (知乎)** — regional social-content hybrid pole (China): Q&A core with heavy content/community expansion (columns, ideas, hot lists, paid content). Root page + official Terms reachable (Tier 1–2).
4. **Quora** — social-feed pole (West): questions + answers with follow graph and personalized feed; upvotes, no canonical acceptance. NOT reachable (timeouts ×2) — named representative with reduced-strength claims only (per the precedent used by the expert-q-a-platform pass for JustAnswer/Experts Exchange).
5. **Brainly** — education/student pole: homework Q&A for K-12 with answer appreciation ("brainliest") and moderation ranks. NOT reachable (403 + transport error) — named representative with reduced-strength claims only.

Boundary reference product (not a member of the Type): **Discourse** (forum software whose official plugin directory documents Q&A machinery as optional plugins).

Historical anchor (memory-based, conceptual check only — no fetched source): **Yahoo! Answers** (2005–2021, closed).

## Sources

Reachable during this pass (research date 2026-09-08):

- Stack Overflow Business / company — https://stackoverflow.co/ (official stats: 83M questions and answers; a new question every ~21 seconds on average; knowledge reused 113 billion times; "cultivating dev communities since 2008"; 75% of developers still want to ask another person when they don't trust AI answers; 82% of devs visit multiple times per month)
- Stack Overflow for Teams → "Stack Internal" product page — https://stackoverflow.co/teams/ (enterprise variant; "your own version of our iconic green check mark"; capture/validate/organize/govern machinery)
- Stack Overflow Blog — https://stackoverflow.blog/ (network question links from workplace/travel/hsm/movies.stackexchange.com; badges e.g. "Populist"; "open-ended questions now available to all users"; "Stack Overflow for Agents" beta; Stack Data Licensing)
- Baidu Zhidao — https://zhidao.baidu.com/ (official homepage: tagline "总有一个人知道你问题的答案"; 搜索答案 / 我要提问 / 我来回答 primary actions; 获取采纳 (accepted answers); 财富值 points + 知道商城 + tasks; 认证用户/认证团队/合伙人; 权威机构 institutional answerers with answer/like counts; 优秀答主 leaderboards; AI-generated-content governance notice)
- Zhihu — https://www.zhihu.com/ (official root: tagline "有问题，就会有答案"; surfaces 关注/推荐/热榜/专栏/圈子; 机构号 institutional accounts) and https://www.zhihu.com/term/zhihu-terms (official Terms, effective 2025-03: self-description as online community "以问答产品或其他形式的内容产品"; user content types 回答/文章/想法/评论/专栏/播客; collaborative editing of 问题及补充说明/答案总结/话题描述; "知乎不能对用户发表的回答或评论的正确性进行保证"; 知乎直答 AI answer service described as non-human retrieval/generation over the community corpus; moderation measures 删除/屏蔽/折叠/标记)
- Discourse official plugin directory — https://www.discourse.org/plugins ("Solved — Great answer? Solved allows users to accept solutions to their topics."; "Post Voting — Upvote or downvote posts…"; Topic Voting; Gamification "points and leaderboards"; Category Experts)

Blocked / unreachable (attempted, then abandoned per network rules — recorded as a sourcing limitation):

- stackexchange.com/tour, stackoverflow.com/tour, stackoverflow.com/help/... — 403 ×3
- quora.com/about, help.quora.com — timeout ×2
- brainly.com, help.brainly.com — 403 / transport error
- en.wikipedia.org (HTML + REST API), web.archive.org — timeout ×4 / timeout
- answers.com — 403

Cross-pass recorded evidence (sibling research notes with their own fetched sources, cited as project-internal evidence):

- research/discussion-board.md — Q&A machinery exists inside forum products as a thread type (XenForo question threads native; Discourse accepted answers documented capability)
- research/online-forum.md — question-and-solution machinery = format capability inside a venue-general Type; a product becomes a Q&A community when question/answer/accepted-answer structure is the primary organizing principle of the whole venue
- research/community-platform.md — Q&A exists as a capability inside community platforms (Higher Logic "Q&A and discussions"; Discourse accepted-answers plugin)
- research/expert-q-a-platform.md — community-vs-expert seam: "anyone may answer; quality enforced by voting/reputation after the fact, not by vetting before it; no addressed transaction"

## Product A — Stack Overflow / Stack Exchange (rigid knowledge-engineering pole)

### Key observations (evidence layer A = fetched official pages; m = memory-based, kept general)

- **A**: The company describes the asset as "83 million questions and answers" — the Q&A pair is the accounting unit of the whole product; "a new question every ~21 seconds, on average"; "113 billion times knowledge has been reused" — reuse of the archive is the headline value, not conversation volume.
- **A**: The accepted answer is the product's "iconic green check mark" (official copy on the Stack Internal page: "your own version of our iconic green check mark") — i.e., the accepted-answer mark is the trust icon the vendor itself monetizes into the enterprise product.
- **A**: Quality machinery is badge-based ("community members earning the Populist badge") and question types evolve as product decisions ("open-ended questions now available to all users").
- **A**: The network is a family of topical sites (workplace.stackexchange.com, travel.stackexchange.com, hsm.stackexchange.com, movies.stackexchange.com shown on the blog) — one software platform, many scoped communities, each with question-URL records (/questions/<id>/...).
- **A**: Enterprise variant (Stack Overflow for Teams, now "Stack Internal") repackages the same trust machinery as an internal knowledge layer: capture, validate ("authorship, recency, usage, provenance" trust signals), organize, govern — plus AI-agent consumption ("Stack Overflow for Agents"; Stack Data Licensing of "decades of verified, technical knowledge").
- **m (general knowledge, kept general — help center 403)**: The public community runs voting (up/down), reputation accrual, privilege ladders, question closing/deduplication, tag taxonomies, and asker-selected accepted answers. No numeric thresholds, privilege names, or window details are asserted here because the help center was not reachable.
- Positioning drift note: the vendor's own current emphasis (Stack Internal, data licensing, agents) treats the public Q&A community as the trust-machinery origin, not the growth product.

## Product B — Baidu Zhidao 百度知道 (mass-market casual pole)

### Key observations (layer A = fetched homepage)

- **A**: Self-description: "全球领先中文互动问答平台" ("leading Chinese interactive Q&A platform"); tagline "总有一个人知道你问题的答案" ("someone always knows the answer to your question") — the premise is that the community contains the answer, and the archive surfaces it.
- **A**: Primary actions on the homepage are exactly the participation loop: 搜索答案 (search answers), 我要提问 (ask a question), 我来回答 (browse and answer). Search-first discovery of answers is the default entry.
- **A**: The adopted-answer mechanism is named in the newcomer help ("获取采纳" — "get adopted/accepted"), i.e., asker (or system) adoption of a best answer is a first-class product concept, parallel to Stack's check mark.
- **A**: A points economy wraps participation: 财富值 (wealth points) balance, 知道商城 (points shop), tasks/treasure boxes, cash withdrawal in-app — contribution is directly incentivized.
- **A**: Answerer quality structures: 认证用户 (certified users), 认证团队 (certified teams), 合伙人 (partner program), 优秀答主 (excellent answerers) leaderboards with displayed answer/like counts; institutional answerers (权威机构): brand customer-service accounts (banks, handset makers) answering at scale with per-account answer/like stats.
- **A**: Content governance notice about AI-generated content; question records live at /question/…/answer/… — question with answers attached, exactly the Q&A-pair record shape.

## Product C — Zhihu 知乎 (regional social-content hybrid pole)

### Key observations (layer A = fetched root page + official Terms)

- **A**: Positioning: "有问题，就会有答案" ("where there are questions, there are answers"). The Terms define the platform as an online community providing "问答产品或其他形式的内容产品" — Q&A products *plus other content forms* — the vendor itself names Q&A as the anchor product class.
- **A**: Content types are user-authored: 回答 (answers), 文章 (articles), 想法 (ideas), 评论 (comments), 专栏 (columns), 播客 (podcasts) — a content-community expansion on top of the Q&A core.
- **A**: Collaborative editing is explicitly contractual: "多人参与编辑的内容，包括但不限于问题及补充说明、答案总结、话题描述、话题结构" — questions, supplementary descriptions, answer summaries, and topic descriptions are community-editable (wiki-style) — and the resulting jointly-edited objects are owned by the platform, while individual posts (answers/articles) remain the user's copyright.
- **A**: The platform explicitly disclaims answer correctness: "知乎不能对用户发表的回答或评论的正确性进行保证" — answers are member-generated opinion, and the quality mechanism is community/market signal, not institutional guarantee. This is a clean Type-level marker distinguishing community Q&A from expert services.
- **A**: The same vendor operates an AI answer layer: 知乎直答 (Zhida), described in the Terms as *non-human* retrieval/generation over the community corpus, partner content, and public web content — official vendor confirmation that the human Q&A community and the algorithmic answer layer are two different things coexisting in one brand.
- **A**: Surfaces: 关注 (follow), 推荐 (recommend), 热榜 (hot list), 专栏 (columns), 圈子 (circles); 机构号 (institutional accounts) as an org participation form; moderation measures include 删除/屏蔽/折叠/标记 (delete/block/collapse/label).

## Boundary reference — Discourse (forum software; not the Type)

- **A**: The official plugin directory documents the Q&A format as optional capability: "Solved — Great answer? Solved allows users to accept solutions to their topics"; "Post Voting — Upvote or downvote posts within various topics"; Topic Voting; Gamification ("points and leaderboards"); Category Experts. A forum therefore *hosts* Q&A machinery; it does not *become* a Q&A community until the Q&A pair is the venue's primary organizing principle (consistent with the online-forum and discussion-board passes).

## Named representatives without reachable official docs (layer C claims only)

- **Quora**: question-organized knowledge community with strong social layer — member profiles, follow graph of people/topics, personalized answer feed, upvote-based ranking, no canonical accepted-answer mark. Claims kept general: no voting rules, monetization details (Quora+/Spaces), or numeric limits asserted — official docs unreachable (timeout ×2).
- **Brainly**: student homework Q&A community — questions answered by peers, appreciation mechanism ("brainliest"), moderation ranks for students, education-scoped. Claims kept general — official docs unreachable (403/transport error).

## Historical / Market-Sample Check

- **Yahoo! Answers (2005–2021; memory-based, conceptual only)**: question records + open answering + community voting with asker-selected best answer + persistent searchable archive, with none of: reputation privilege ladders, strict topical enforcement, tag discipline, wiki question editing, enterprise tiers. Satisfies the three defining structures → they hold across eras, not just the modern knowledge-engineering pattern. No precise mechanics asserted (no fetched source).
- **Usenet newsgroups / mailing lists**: carry Q&A-shaped traffic but fail the standing-community-with-attribution and community-produced-answer-authority legs (no venue-owned membership, no voting/acceptance) — correctly excluded, consistent with the online-forum pass's exclusion of Usenet as a venue ancestor.
- **Newspaper "ask the expert" columns / librarian reference desks**: no open member answering, no standing community — excluded (already the expert-q-a-platform pass's historical poles).
- **Ask Jeeves/Ask.com**: question-shaped front end but algorithmic answering, no community — excluded (Answer Engine territory).
- Conclusion: the defining core must NOT include reputation systems, tag taxonomies, strict topical scope, wiki editing, or gamification depth — all era- or product-features; and must NOT include voting/acceptance as *the* mechanism (Quora-style ranking without acceptance still qualifies) — the invariant is *community-produced* answer authority, whatever the mechanism.

## Cross-product Comparison

| Dimension | Stack Overflow/Stack Exchange | Baidu Zhidao | Zhihu | Quora (general) | Brainly (general) |
|---|---|---|---|---|---|
| Unit of record | question + answers (83M Q&A stated) | question + answers (/question/…/answer/…) | question + answers (+ articles/ideas around it) | question + answers | question + answers |
| Who answers | any member | any member; certified users/teams; brand service accounts | any member; 机构号 institutional accounts | any member | students/peers |
| Answer authority mechanism | voting + accepted answer + reputation + badges | adoption (采纳) + likes + points economy | 赞同 votes + algorithmic ranking + follower social proof | upvotes | appreciation ("brainliest") + peer signals |
| Community-produced authority? | yes (community voting/acceptance) | yes (adoption/likes) | yes (votes/social signals) | yes (upvotes) | yes (peer appreciation) |
| Archive & rediscovery | search + topical sites + tags; reuse stated (113B) | search-first; question archive | search + follow/recommend/hot-list feeds | search + feed | search + subject organization |
| Topical scope | per-site strict scope; network of sites | broad, general | broad + content expansion | broad | education/homework |
| Reputation/gamification | reputation, badges, privileges | wealth points, shop, tasks, leaderboards | creator metrics/standing | (kept general) | (kept general) |
| Collaborative question editing | (m: yes, kept general) | (not asserted) | yes (official Terms) | (not asserted) | (not asserted) |
| Enterprise/internal variant | Stack Internal (ex-Teams) | not observed | not observed | not observed | not observed |
| AI layer on corpus | Stack for Agents; data licensing | AI-content governance notice | 知乎直答 (non-human answer layer) | (not asserted) | (not asserted) |
| Institutional answerers | not observed as program | brand customer-service accounts (权威机构) | 机构号 | (not asserted) | (not asserted) |

## Canonical Model (drafted before final synthesis)

```text
Standing community of members
  └── Question (unit of record; carries the asker's specific need)
        └── Answers (open-member contributions, attributed)
              └── Community-produced answer authority
                  (vote / accept / rate / rank — mechanism is a variant)
        └── Accumulative, discoverable archive
            (Q&A pairs persist; search/topical organization; reuse is the value)
```

## L0 — Defining Invariant (minimal)

Exactly three jointly-held structures:

1. **The question as the unit of record** — a persistent, individually addressable question record posed by a member, carrying that member's specific need, to which answers attach. Remove → social feed / discussion surface / content platform.
2. **Open answering with community-produced answer authority** — any member may answer (answering is not restricted to a vetted pool, and answers are not machine-composed), and the authority/ranking of answers is produced by the community's own visible mechanisms — voting, acceptance, ratings, reputation — not conferred by vetting or computed by an algorithm. Remove → Expert Q&A Platform (vetted pool, addressed answers) or Answer Engine (algorithmic).
3. **The accumulative, discoverable answer archive** — Q&A pairs persist beyond the exchange and are organized for rediscovery (search, topical organization), so the record serves later visitors with the same need. Remove → ephemeral live Q&A / audience-response surface.

Jointly-held load-bearing:

- 1 alone = question-organized records without crowd answering → help center / FAQ (organization-authored) or a private expert exchange.
- 2 alone = crowd discussion without question-organized records → chat / community platform / social network.
- 3 alone = a searchable archive without living community answering → search engine / static KB.
- 1+2 without 3 = live AMA / audience-response Q&A → session-bound surfaces.
- 1+3 without 2 = question-shaped records without community answering → help center / knowledge base / answer engine.
- 2+3 without 1 = standing community with an archive but topic-organized → online forum / community platform with a Q&A capability (the format-vs-container seam).

Historical check: Yahoo! Answers-era products satisfy 1–3 with none of the modern machinery (see above); the definition is era-neutral.

## L1 — Common Mature Structure (very common, not definitional)

- voting / upvote–downvote on questions and answers (Stack-family, Zhihu 赞同, Quora upvotes, Discourse Post-Voting plugin)
- accepted-answer selection (asker- or community-selected best answer; Stack's "iconic green check mark"; Zhidao 采纳; Discourse Solved plugin) — present across most mature products but absent in at least one representative (Quora) → NOT definitional
- reputation / points / levels / badges (Stack reputation; Zhidao 财富值; gamification)
- member profiles with attributable contribution history (answer/like counts on Zhidao; profile pages)
- comments on questions and answers (side-channel clarification distinct from answers)
- question improvement: collaborative/wiki-style editing of question text and supplements (Zhihu official Terms; Stack-family editing kept general)
- topical organization: tags, topics, categories, per-site scoping (Stack network; Zhihu 话题; forum categories)
- search over the archive (all reachable samples place search prominently — Zhidao homepage action #1)
- feeds/recommendations/hot lists as discovery layers (Zhihu 推荐/热榜; Quora feed)
- ask-to-answer / answer solicitation and question-browsing entry points (我要提问/我来回答; (m) Stack-family ask flows)
- moderation toolkit: flag, close/duplicate handling, collapse/delete/label (Zhihu official Terms; Stack-family close/duplicate kept general; Discourse staff machinery)
- notifications and subscriptions (kept general)

## L2 — Variant / Optional Structure

- topical scope: single-domain (Stack Overflow), multi-site network (Stack Exchange), broad general (Zhidao, Zhihu, Quora), education-scoped (Brainly)
- deployment posture: public open communities vs enterprise-internal Q&A (Stack Internal — org-gated membership, same format + crowd answering + internal trust signals); Q&A machinery inside closed communities without being the Type remains community-platform territory (private-community-platform pass's flag, confirmed)
- institutional participation: brand/organization answerer accounts (Zhidao 权威机构 brand service accounts; Zhihu 机构号)
- monetization: advertising, points/reward economies incl. cash withdrawal (Zhidao), paid content subscriptions and creator monetization (Zhihu's content business kept general — 盐选-type paywalls are vendor-specific), bounties (Stack-family, kept general)
- adjacent content expansion: columns/articles/ideas/podcasts/hot lists around the Q&A core (Zhihu); the Q&A core remains the spine
- AI layers built ON the community record: corpus-grounded AI answer services (知乎直答), machine consumers (Stack Overflow for Agents), data licensing of the archive (Stack Data Licensing), AI-content governance rules (Zhidao) — the human Q&A community remains the underlying Type
- regional ecosystems and language scoping (Chinese poles; western poles)
- gamification intensity and economy depth (points shops, tasks, leaderboards)

## L3 — Vendor-specific (research notes only; excluded from the final document)

- Stack: exact reputation/privilege ladders, badge catalog (e.g. "Populist"), bounties, per-site area51 incubation process, CC-licensing posture of contributions, 83M/21s/113B stats, Stack Internal capture/validate/organize/govern architecture
- Baidu Zhidao: 财富值/商城/任务/提现 economy specifics, 认证团队/合伙人 program structures, 鸭家族 mascot/anniversary activations
- Zhihu: 盐选 member content business, 圆桌 roundtables, 直答 AI service terms, joint-editing IP assignment clause
- Quora/Brainly: any specifics — docs unreachable, nothing asserted

## Rejected Findings

- **"Voting + accepted answer + reputation is the definition"** — rejected: Quora (no acceptance) and Yahoo! Answers (no reputation ladders) still satisfy the Type; the invariant is community-produced authority, not a specific mechanism.
- **"Strict topical scope / expert culture is definitional"** — rejected: broad general communities (Zhidao/Zhihu/Quora) are equally canonical; Stack's strictness is a product philosophy (knowledge-engineering pole).
- **"Search-first discovery is definitional"** — rejected: feed/hot-list-first products (Zhihu/Quora) remain the Type; discovery layer is a variant.
- **"The venue must be a standalone public site"** — rejected: enterprise-internal Q&A (Stack Internal) satisfies all three defining structures behind an org gate; access posture is a variant. (A community platform with a Q&A *section* is still not this Type — the difference is what the product is primarily organized around.)
- **"Q&A Community = forum with question threads"** — rejected: in forum software, Q&A machinery is optional capability (Discourse Solved/Post Voting plugins; XenForo question threads); the Types differ in the primary organizing principle.

## Boundary Findings

1. **vs Online Forum** (§01.06, processed): venue-general vs format-organized. Discourse Solved/Post Voting prove Q&A machinery is a capability inside a forum; a product is this Type when question/answer/accepted-answer structure is the primary organizing principle of the whole venue. Remove the Q&A-pair spine → forum. (Discharges online-forum pass's note from this side.)
2. **vs Discussion Board** (§01.06, processed): tool vs community-format. The discussion-board pass already holds the seam: "If a product's topics are predominantly questions with solutions and voting, it has crossed into Q&A Community." Confirmed; no new flag.
3. **vs Community Platform** (§01.06, processed): format vs operated container. Q&A exists as a capability inside community platforms (Higher Logic "Q&A and discussions"; Discourse plugins). Remove the format → community platform remains. (Discharges community-platform pass's format-vs-container flag from this side.)
4. **vs Interest Community Platform** (§01.06, processed): format vs joinable-community-unit spine. Q&A communities organize *content* around questions, not *participation* around joined communities. Confirmed from this side.
5. **vs Private Community Platform** (§01.06, processed): closed-posture Q&A machinery inside private communities is not this Type unless the product is *primarily* Q&A-organized; enterprise-internal Q&A products (Stack Internal pole) are this Type in a deployment variant. Confirmed with the internal/enterprise variant note.
6. **vs Expert Q&A Platform** (§02.03, processed): vetted pool + addressed answers vs open crowd + community authority. Remove vetting → this Type. Confirmed from this side (that pass defined the seam; the "no addressed transaction" property holds — answers serve the archive, not a paid private exchange).
7. **vs Answer Engine / Knowledge Question Answering Application** (§02.03, processed): human member answers vs algorithmic composition. Vendor evidence sharpens the seam: the same vendors layer algorithmic answering on top of the human community corpus (知乎直答; Stack for Agents) while keeping them as distinct product layers.
8. **vs Help Center / Knowledge Base Application** (§02.06, processed): member-generated answers vs organization-authored record copy. Remove community answering → help center/KB.
9. **vs Interest-based Social Network** (§01.05, processed): the straddle pole is Quora (and content-expanded Zhihu). Seam: content binds to *questions* (Q&A) vs content binds to *profiles/streams* (social). In the reachable evidence (Zhidao, Zhihu Terms), questions remain the record spine even when feeds/follows are heavy; Quora kept general due to unreachable docs and flagged as the recognized straddler.
10. **vs Audience Response System** (§26, processed): session-bound live Q&A vs persistent discoverable archive. The archive leg (defining structure 3) is the discriminator.
11. **vs Tutoring Platform** (§23): answer-as-deliverable vs scheduled learning progression.

## Uncertainties

- Quora and Brainly official documentation unreachable: their structures are held at general-knowledge strength (layer C), marked as such; no mechanics asserted. If a later pass fetches them, the L1 list may gain acceptance/reputation variants.
- The public Stack community's help center (voting/reputation/closing specifics) unreachable: all Stack-family mechanics kept general; the fetched stats (83M Q&A, 21s, 113B reuse, badges, check mark) are cited as official positioning facts.
- Whether collaborative question editing is common across the Type: verified officially only for Zhihu (Terms) and known generally for Stack-family (memory) → held at L1 with mixed evidence strength.
- Institutional answering (brand service accounts) observed in both Chinese poles but not in Western samples' reachable pages → held as a variant with geographic skew noted.
- Yahoo! Answers historical check is memory-based (Wikipedia/archive unreachable) — conceptual fit only, no mechanical claims.

## Final Synthesis

A Q&A Community is a standing member community whose participation is organized around questions as persistent records: any member may answer, the community itself — through voting, acceptance, ratings, or reputation — makes some answers stand out as authoritative, and the accumulating question-and-answer archive is organized for rediscovery so that each answered question keeps serving later visitors. The three structures are jointly load-bearing, and every sampled product — rigid knowledge-engineering (Stack), points-driven mass-market (Zhidao), social-content hybrid (Zhihu), feed-social (Quora), education (Brainly), and the historical anchor (Yahoo! Answers) — satisfies them, while every adjacent Type fails exactly one of them. Voting, acceptance marks, reputation, tags, topical scope, feeds, institutional answerers, monetization, and AI layers are common or variant machinery; the archive-reuse premise ("someone always knows the answer", "113 billion times reused") is the Type's economic and social core.
