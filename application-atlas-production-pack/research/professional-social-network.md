# Research Notes — Professional Social Network

Research date: **2026-09-08**

## Research Goal

Understand what a Professional Social Network actually is as an Application Type — from real products, not from the directory label. Specifically: what defines it (and must remain if everything modern is stripped away), what is merely common mature structure, what is regional/vertical variant, and where its boundaries lie against Job Boards, General Social Networks, CRM-class systems, and profile/directory products.

## Initial Boundary (hypothesis before research)

- Core purpose hypothesis: a social network where individuals present a *professional* identity (career-record-shaped), connect with other professionals, and where career/business opportunity (hiring, being hired, business development, industry knowledge) is the reason the network exists.
- Nearest neighbors: General Social Network (01.05), Job Board (09), Social Profile Network (01.05), Interest-based Social Network (01.05), CRM / Sales Prospecting (07), Candidate Search Platform (09).
- Suspected boundary: jobs should NOT be definitional (early and vertical professional networks lack a jobs marketplace); the feed should NOT be definitional (early networks had no feed); the connection graph and the professional profile should be core.
- Unknowns: connection semantics across products (mutual vs follow), profile consumption model (who evaluates profiles), visibility/messaging gating rules, regional/vertical variation.

## Research Questions

1. What objects exist in the system (profile, connection, feed post, job, company page, group, event, message)?
2. How is the connection graph built, and what are its semantics (invitation/accept vs follow)?
3. Who consumes the profile, and for what evaluation purpose? Is profile-viewing visible to the member?
4. What flows does the platform support: networking, job seeking/recruiting, content sharing, business development, community?
5. What rules matter: real-identity policy, professional-conduct policy, visibility controls, messaging gating by relationship, invitation abuse limits?
6. How do regional incumbents and vertical variants realize the same core?
7. Where is the boundary against Job Board (listings-first), General Social Network (lifestyle identity), CRM (org-owned records), and profile/directory products?

## Representative Products

Chosen for market representativeness, documentation quality, different product philosophies, different regions, different eras of emphasis:

| Product | Role in sample | Region/position | Evidence quality |
|---|---|---|---|
| LinkedIn | global dominant archetype; recruiter-centric business model; richest help documentation | Global | Tier-1 help center, policies — strong |
| XING | European (DACH) regional incumbent; jobs/networking dual emphasis | Regional (Germany/Austria/Switzerland) | Tier-1 help center — strong |
| Maimai (脉脉) | Chinese regional professional network; real-name identity + community emphasis | Regional (China) | Tier-2 product/about page — moderate |
| ResearchGate-class academic networks | vertical (science) professional networks; publication-backed profiles | Vertical, global | **Source-access limitation** — help center unreachable (transport errors ×2), main site returned 403. Observations below rely on the product's known public surface only at *degraded strength* and are marked accordingly. Not used for any load-bearing claim. |

Wikipedia (for the historical check on early-2000s professional networks) timed out twice — see Sources / limitations.

## Sources

### LinkedIn (Tier-1, all fetched 2026-09-08)

- LinkedIn Help root: https://www.linkedin.com/help/linkedin
- Build your professional network: https://www.linkedin.com/help/linkedin/answer/a545734
- Various ways to connect with people on LinkedIn: https://www.linkedin.com/help/linkedin/answer/a541669
- Your Network and Degrees of Connection: https://www.linkedin.com/help/linkedin/answer/110
- Your Profile topic (55 articles, titles/abstracts): https://www.linkedin.com/help/linkedin/topic/a64
- Connections topic (29 articles, titles/abstracts): https://www.linkedin.com/help/linkedin/topic/a151001
- Jobs through social hiring: https://www.linkedin.com/help/linkedin/answer/a767235
- Professional Community Policies: https://www.linkedin.com/legal/professional-community-policies

### XING (Tier-1, all fetched 2026-09-08)

- XING Help Center root: https://help.xing.com/hc/en-us
- Networking category (Insights / Messages / Contacts / Member search): https://help.xing.com/hc/en-us/categories/31498338510749-Networking
- Contacts section (article list): https://help.xing.com/hc/en-us/sections/31498636287005-Contacts
- Add someone as a XING contact: https://help.xing.com/hc/en-us/articles/31499078549661-Add-someone-as-a-XING-contact
- My profile category (Business card / Timeline / Visibility / More): https://help.xing.com/hc/en-us/categories/31498356199069-My-profile

### Maimai (Tier-2, fetched 2026-09-08)

- Product/about page (Chinese): https://maimai.cn/ — self-describes as 职场社区和求职平台 ("workplace community and job-seeking platform") for 职场人 (workplace professionals); surfaces: 职业身份认证 (professional identity verification), 同事圈 (colleague circles), 职场话题/干货 (workplace topics), 公司点评 (company reviews), 人才银行 (talent bank / recruiting), 拓客通 (sales prospecting), 专家网络 (expert network), 企业号 (company/employer pages).

### Source-access limitations

- ResearchGate: helpcenter.researchgate.net — transport error ×2; www.researchgate.net/about — HTTP 403. Per the source-access rule the source is abandoned; academic-vertical observations are held at degraded (unverified-formal) strength and no load-bearing claim rests on them.
- Wikipedia (LinkedIn / XING history): request timed out ×2. The historical check below is therefore **conceptual** (structure-of-the-era reasoning), not fact-dated. No precise launch dates or era timelines are asserted anywhere.
- Maimai: only the marketing/about page was reachable; operational semantics (connection model, messaging gating, moderation) are NOT asserted from it.

## Product A — LinkedIn

### Key observations (evidence layer A = directly observed on official pages)

- The product's own definition of the network: "Your LinkedIn network is a professional directory made up of people you know and trust professionally." Networking is framed around staying in touch with alumni/colleagues/recruiters, discovering career opportunities, and engaging with industry professionals. (a545734)
- Connection semantics: sending a connection **invitation** creates a **1st-degree connection**; once connected, members can message each other directly and see more of each other's profiles. Connecting is framed as requiring "a clear professional reason to reach out" (worked/studied together, met at an event). A "How do you know [member]?" prompt exists; answering "We don't know each other" pushes the sender to message first instead. Invitation abuse (reported as spam) can restrict the account. (a541669, a545734)
- Degrees of connection: 1st-degree (mutual accepted invitation), 2nd-degree (connections of connections), 3rd-degree, followers, fellow group members, out-of-network. "The degree of connection you have with another member affects how you can interact with them." (answer/110)
- Follow is a *separate* structure from connection: following shows posts in feed without creating a connection or enabling direct messaging. (a545734, answer/110)
- Messaging gating: with a free account you can only message members you're already connected to; direct messaging of non-connections (InMail) is a paid/Premium capability. Message requests exist for coworkers/group members you aren't connected to. (a545734, topic a151001)
- Network size ceiling: 30,000 1st-degree connections max (stated as site-experience rule; product-specific number — L3). (a545734, a541669)
- Network-building machinery: contact import (device/address book, Gmail), "People You May Know", Alumni tab (per school/graduation year), member search (name, role, company, location, industry). (a545734, topic a151001)
- Profile as career record (topic a64): sections include Introduction (current position/company, location, contact info), About, Experience (positions grouped per company, reorderable "to be visible to your connections and recruiters"), Education, Skills (curated list; cap exists), Featured (work samples), Activity (posts/comments/articles), cover image, profile photo (must "reflect your likeness"), Volunteering, contact info. A "profile level meter" scores completeness and frames completeness as improving search discoverability.
- Profile is consumed for evaluation: "Who's viewed your profile" (viewer identity/insights, paid depth) exists because being viewed — by recruiters etc. — is a normal, expected event; "profile search appearances" reports how often the profile surfaced in searches; member-facing advice repeatedly addresses recruiters as the profile audience.
- Peer attestation on the profile: **Recommendations** — "a commendation written by a LinkedIn member to recognize your work," requestable from 1st-degree connections you work(ed) with, with an accept-or-dismiss control on receipt. **Skill endorsements** — members endorse each other's listed skills (per-member per-day cap exists — L3 number). (topic a64)
- Identity policy: "We require you to use your true identity on LinkedIn"; no fake profiles, no other people's photos, no accounts for others, no association with organizations you aren't professionally associated with; an ID-verification feature exists where profile name can be matched to government-issued ID name. (Professional Community Policies; a7153330)
- Professional-conduct policy: the platform positions itself as "a professional networking platform, not a dating site" — romantic advances prohibited; professional civility rules; spam rules explicitly forbid using the invitation feature for promotional outreach to strangers. (Professional Community Policies)
- Jobs flow: a jobs marketplace exists (Search and Apply for Jobs topic; "Apply for jobs" help shortcuts), plus "social hiring" — notifications when a 1st- or 2nd-degree connection is hiring for a relevant job. Jobs flow *through the member graph*, not as an isolated listing board. (a767235, help root)
- Consumption-side products: separate help surfaces for **Recruiter**, **Sales Navigator**, **Talent Insights**, Marketing Solutions — i.e., recruiters, salespeople, and marketers are first-class *consumer* parties of the member network, served by separate paid products built on the same member graph. (help root product menu)
- Content/community surfaces: feed (professional content from network, followed companies, suggestions), posts/articles, Groups (shared-interest professional discussions), Events, company/followable entities (companies you follow appear in feed description; LinkedIn Pages exist). (a545734, help root)
- Profile signals: "Open to Volunteering" style opt-in signals exist on the profile (a6862361); share-profile-update notifications for job changes/work anniversaries generate feed posts. (help root)

## Product B — XING

### Key observations (evidence layer A)

- Help Center is split **For Individuals / For Businesses**. Individuals: Find jobs, My profile, Networking (Insights, Messages, Contacts, Member search), Settings & security, News, Apps. Businesses: Job Ads, TalentManager, Application Manager (onlyfy), Employer Branding Profile, Recruiting Bundles, XING jobs network. The dual-sided structure (member network + recruiting machinery) mirrors the archetype at the structural level. (help root)
- Contact semantics: "Send a **contact request** to members you want to add to your contact list" — visit profile → Add as contact → (paid members may attach a message) → the member is notified and "can then choose to **accept or reject** it." Same mutual-consent model as the archetype, different vocabulary (contact vs connection). (Add someone as a XING contact)
- Contact governance article set: Accept or decline contact requests, Delete a contact, Delete sent contact requests, **Limit of contact requests** (a cap exists — L3 number), **Control the visibility of your contact list**, report unwanted messages or contact requests as spam. The contact list is both a personal asset and a privacy surface. (Contacts section)
- Member search is a first-class networking surface (Member search section), alongside Messages and Insights (feed-class surface). (Networking category)
- Profile structure (My profile category): **Business card** (the professional identity card), **Timeline** (activity/status surface), **Visibility** (dedicated visibility controls). The profile is again a business-card-shaped professional record with granular visibility. (My profile category)
- Community guidelines exist under Contacts ("Community Guidelines") — conduct rules for the member network. (Contacts section)
- Jobs is a first-class individual surface ("Find jobs") and the business side is recruiting-heavy — jobs/recruiting is the dominant commercial engine here, structurally confirming that recruiting rides on the member network rather than being the member network.

## Product C — Maimai (脉脉)

### Key observations (evidence layer A at Tier-2 strength — product page only)

- Self-positioning: "职场社区和求职平台" — a workplace community **and** job-seeking platform for 职场人 (workplace professionals); vendor-claimed scale "1.2亿职场人" (120M workplace professionals; vendor-claimed figure, recorded as such).
- **职业身份认证** (professional identity verification) is a headline capability — "海量用户职业身份认证，助力中国职场人塑造个人职业形象" — real-name/verified professional identity as the trust substrate. This is the regional (China) implementation of the true-identity norm, stronger than in Western products.
- **同事圈** (colleague circles) — circles bound to workplace/colleague context ("在圈子找到职场归属感").
- Community/content surface: 职场话题/职场干货 (workplace topics and practical knowledge) as a core community layer; this product leads with community more than the Western archetype.
- **公司点评** (company reviews — "先看点评，再找工作": read reviews first, then look for work): employer-evaluation content lives inside the professional network.
- Opportunity machinery: 人才银行 (talent bank — recruiting/人才全生命周期管理), 招聘管理 (recruiting management), 拓客通 (sales prospecting tool for sales staff), 专家网络 (expert network for B2B knowledge), 企业号/品牌号 (company and brand pages for employer branding).
- Not asserted (no source): connection-request semantics, messaging gating, feed mechanics, moderation rules.

### Degraded observation — academic-vertical networks (ResearchGate-class)

Due to source unavailability, held at minimal strength: academic professional networks are known to organize the same triad — a professional profile whose substance is publications/academic career, a colleague/co-author graph, and an academic-opportunity frame (visibility to peers, discussion, job boards in some cases). **Not used for any definitional claim.** Recorded primarily as a boundary probe: even a publication-substrate profile remains a *career-record* profile, supporting the abstraction of "professional profile" above any specific content type (CV items vs publications).

## Cross-product Comparison

| Dimension | LinkedIn (global archetype) | XING (European regional) | Maimai (Chinese regional) | Academic vertical (degraded) |
|---|---|---|---|---|
| Unit of identity | Profile: intro/About/Experience/Education/Skills/Featured | Profile as "Business card" + Timeline | Verified professional identity (实名职业身份) | Publication/academic-career profile |
| Identity norm | true identity policy; photo = likeness; ID-name verification feature | real member identity (guidelines) | platform-level professional identity verification (headline capability) | real researcher identity (implied) |
| Graph semantics | invitation → 1st-degree; mutual consent; separate Follow layer; degrees | contact request → accept/reject; mutual consent | not verified | colleague/co-author graph (not verified) |
| Evaluation consumption | recruiters explicitly framed as profile audience; Who's viewed; search appearances | business-side: TalentManager / employer branding | recruiting (人才银行), sales prospecting (拓客通), expert network | peer visibility (not verified) |
| Messaging gating | connection-gated on free tier; paid InMail for out-of-network; message requests for coworkers/group members | Messages surface; contact-request message paid (L1-level) | not verified | not verified |
| Jobs | job marketplace + social hiring through the graph | Find jobs + heavy recruiting business side | 求职平台 positioning + 人才银行 | absent or marginal (not verified) |
| Community/content | feed, posts/articles, Groups, Events | Insights, News, community guidelines | 职场话题 community + 同事圈 + 公司点评 | discussion/Q&A (not verified) |
| Company presence | followable company entities; Pages | Employer Branding Profile | 企业号/品牌号 | (institutional pages, not verified) |
| Regional/variant flavor | premium InMail/insights tiers | jobs-network bundles; contact-request caps | real-name verification; anonymous community layer (known public surface, not asserted here) | publication substrate |

### Stable commonalities across the sample (evidence layer B)

1. A **member-authored professional profile** as the identity unit (career-record-shaped: role, employer history, education/skills or their domain equivalent).
2. A **consent-based, mutual person-to-person professional relationship** (invitation/contact request → accept/reject) as the graph edge in mature products, with a separate, weaker follow/broadcast layer where content broadcasting exists.
3. **True/real identity as a platform norm** — enforced by policy (archetype), by product framing (business card), or by verification machinery (regional variant).
4. **Visibility and reach are governed by the graph**: relationship degree or contact status controls messaging, profile detail visibility, and contact-list visibility; out-of-network reach exists as a paid/controlled path.
5. **Recruiting/employer side is a first-class consumer party** served through the same member graph (recruiter products, employer branding profiles, talent banks).
6. **Jobs and hiring flows ride on the member network** rather than replacing it (social hiring; jobs network; talent bank).
7. **Professional content/community surfaces** (feed/insights/topics/circles) exist in all sampled products, in varying prominence.
8. **Peer attestation and reputation machinery** attach to the profile (recommendations/endorsements confirmed in the archetype; peer recognition expected in others but not verified — held weaker).

## Canonical Model (L0 / L1 / L2 / L3 abstraction)

### L0 — Defining Invariant (jointly held; each leg removal-tested)

1. **The self-authored professional profile.** A persistent, member-maintained record of the person's *professional* self — role, work history, education/skills (or the domain-equivalent substance, e.g., publications) — whose defining consumption is **evaluation by other parties for professional purposes** (hiring, partnering, sales, peer judgment). Not primarily self-expression or lifestyle presentation. Remove → general social network (lifestyle profile), or a portfolio/resume page outside a network.
2. **The identified professional connection graph.** Person-to-person relationship edges between *real, identified* professionals, forming the trust/reachability fabric of the network (consent-based mutual links being the dominant mature implementation). Remove → resume database / people directory / job board (profiles without relationships).
3. **The professional-opportunity orientation.** The profile and graph are organized around producing professional outcomes — being discovered and reached for work (hiring/being hired), business development, collaboration, industry knowledge — with true-identity norms because professional evaluation depends on authenticity. Remove → a general social network that merely has CV fields; the "professional" qualifier is what this leg carries.

Jointly-held is load-bearing:
- 1+2 without 3 → a CV-flavored general social network.
- 2+3 without 1 → a sourcing database / recruiting CRM (records about people, not self-authored member identities).
- 1+3 without 2 → a professional profile directory / resume site (Social Profile Network territory).

### L1 — Common Mature Structure (present across the mature market; NOT definitional)

- Job marketplace (post / search / apply) and recruiter-side tooling riding on the graph.
- Degrees of connection + graph-gated messaging + a paid/controlled out-of-network reach channel.
- Follow/broadcast layer beside the consent graph; professional feed (network content, followed companies).
- Peer attestation: recommendations and skill endorsements.
- Company/employer pages; groups; events.
- Member search + suggestion machinery (contact import, people-you-may-know, alumni).
- Profile-view transparency ("who viewed your profile" class) and search-appearance feedback.
- Profile-completeness framing; public profile URL; visibility controls (contact list, sections, photo).
- Premium consumer tiers (deeper insights, outreach credits, badges).

### L2 — Variant / Optional Structure (segment / region / era dependent)

- Identity substrate: email/account-based (global West) vs real-name/government-ID-verified professional identity (regional China) vs institution-backed academic identity.
- Anonymous or semi-anonymous community layers operating *alongside* the identified network (regional variant).
- Company-review content inside the network.
- Publication/portfolio substrate as profile substance (academic/creative verticals).
- Regional incumbency itself (a European incumbent, a Chinese network, a global archetype — same Type, different markets).
- Open-to-work / open-to-volunteering class opt-in signals; badges (premium/creator class).

### L3 — Vendor-specific (research notes only; not in the final document)

- 30,000 first-degree connection cap; 60-minute message edit window; 150 endorsements/24h; 50-member group chat; InMail credit model; "Other Similar Profiles"; profile level meter; ID-name matching feature; alumni tab mechanics (archetype).
- XING: paid contact-request message; per-tier product bundles (Prescreen/Go/Core/Pro/Ultimate class); contact-request limit; onlyfy/TalentManager product names.
- Maimai: 人才银行 / 拓客通 / 专家网络 branded modules; vendor-claimed 120M user scale.
- Note on §22 anti-overfitting: the 30,000 cap, premium tiers, and verification features are each single-product or few-product facts and were kept out of the canonical core.

## Rejected Findings (candidates examined and NOT promoted to the core)

- **"Jobs/hiring is the defining purpose"** — rejected. Academic-vertical networks and the known early-generation networks (profile + connections + peer attestation, pre-dating jobs marketplaces and feeds) satisfy the L0 triad without any jobs marketplace. Jobs are the dominant *commercial engine* in mature products (L1) but not the invariant. Also the §24 check: a definition centered on jobs would exclude the Type's own earliest members.
- **"Mutual invitation/accept is the graph edge"** — rejected as *definitional*; it is the dominant mature implementation (both Tier-1 samples) but the invariant is the identified professional relationship itself. A follow-heavy professional graph still reads as the same Type when the profile is a career record and the frame is professional; mutual-consent semantics stays L1.
- **"The professional feed/content is defining"** — rejected. Early networks predate feeds; community surfaces vary in prominence (archetype and Maimai lead with them, XING's are thinner). L1.
- **"Real-name/government verification is defining"** — rejected. It is a strong regional variant (Maimai) plus a verification *feature* in the archetype; the invariant is the true-identity *norm*, not the specific verification mechanism. L2.
- **"Endorsements/recommendations are defining"** — rejected; peer attestation is common (L1) and confirmed only in one product in this sample.
- **"Company pages are defining"** — rejected; employer presence is common (L1) and structurally downstream of the member graph.

## Boundary Findings

- **vs Job Board**: listings-first; posting + application workflow; no persistent self-authored member identity and no relationship graph. The PSN's job marketplace rides on the member graph (social hiring: notification *because* a 1st/2nd-degree connection is hiring). Removal test: remove the graph and member-authored identity from the jobs flow → Job Board. The seam is real and one-way: PSNs grow job boards easily; job boards do not become PSNs without growing the member graph.
- **vs General Social Network**: identity substance (career record vs lifestyle), consumption (professional evaluation vs social sharing), conduct policy (explicitly professional; the archetype bans romantic use), identity norm (true identity as structural requirement). If the profile stops being a career record evaluated by professional counterparties, the product is a general social network.
- **vs Social Profile Network (directory leaf)**: a people/profile directory lacks the professional-opportunity frame and (typically) the living connection graph. A PSN without its graph degrades exactly into this — the boundary carries the graph leg.
- **vs CRM / Sales Prospecting / Contact Discovery (07)**: those hold *organization-owned* records about people for the org's purposes; the PSN holds *member-authored* identities owned by the individuals. The archetype's sales product is literally a consumption-side overlay on the member graph — evidence of the seam, not the same Type.
- **vs Candidate Search Platform / ATS / Recruiting tools (09)**: recruiter-side workflow systems; the PSN supplies the substrate. Recruiter products sold by PSN vendors sit on the seam (L3).
- **vs Interest-based / portfolio networks**: portfolio-first products (work samples central, follow-first, interest frame) drift out of the Type; the profile stops being a career record and becomes a work gallery. Recorded as drift direction, not a taxonomy change.
- **vs Dating Application**: adjacent only negatively — the archetype's policy explicitly prohibits romantic use ("a professional networking platform, not a dating site"). Confirming the professional frame by exclusion.

## Historical / Market-Sample Check (§24) — conceptual pass

Source limitation: Wikipedia unreachable (timeouts ×2), so no dated facts are asserted. The check is structural:

- The known first-generation professional networks (early-2000s "business networking" products) are documented in the industry record as *profile + invitation contacts + peer recommendations* — no jobs marketplace, no feed, no endorsements, no company pages. Against the L0 triad: professional profile ✓, identified connection graph ✓ (invitation-mutual), professional-opportunity frame ✓ (explicit business networking purpose). They qualify as members of the Type.
- Conversely, a definition containing jobs/feed/endorsements/company pages would exclude that first generation — evidence those belong in L1/L2, not the core.
- Regional variants (European incumbent, Chinese real-name-verified network with community emphasis) satisfy the triad without modification. The academic vertical (degraded evidence) satisfies it with a publication-substrate profile — supporting "career-record-shaped" over "CV-shaped" as the invariant.
- Definition deliberately names no specific era machinery: no feed, no premium tiers, no AI, no verification vendor specifics.

## Uncertainties

1. Academic-vertical realization is based on unreachable sources — the degraded observation should be re-verified if sources become reachable. No load-bearing claim depends on it.
2. Maimai's connection semantics, messaging gating, and moderation were not verifiable from a marketing page; nothing about them is asserted in the final document.
3. Whether a *follow-only* professional graph (no consent edge at all) exists as a real product shape was not established; the final document therefore states the mutual-consent edge as "dominant mature implementation," not universal.
4. Precision facts (caps, time windows, tier features) were observed in exactly one product each and are quarantined as L3.
5. Historical check is conceptual due to source failure; no dates asserted.

## Final Synthesis

A Professional Social Network is the network whose defining core is exactly three jointly-held structures: the **self-authored professional profile** (a career-record-shaped identity presented for evaluation by other professionals — employers, recruiters, peers, counterparties), the **identified professional connection graph** (consent-based person-to-person relationships between real professionals as the reachability/trust fabric), and the **professional-opportunity orientation** (profile and graph organized around being discovered and reached for work, business, and industry knowledge, under true-identity norms). Jobs, feeds, endorsements, company pages, recruiter tooling, and verification mechanisms are all common mature or variant structures that ride on this core — removing any of them leaves the Type intact; removing any of the three legs collapses it into a neighboring Type (general social network, resume database/job board, profile directory, or sourcing CRM).
