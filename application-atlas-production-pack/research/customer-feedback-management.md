# Research Notes — Customer Feedback Management

Research date: 2026-09-08
Slug: customer-feedback-management
Directory leaf: Customer Feedback Management (§07 Sales, Customer & Revenue)

## Research Goal

Understand what a Customer Feedback Management application actually is as an Application Type: its defining core, its typical users, its internal structures (feedback item, attribution, aggregation, prioritization, status), its main workflows (capture → organize → prioritize → act → close the loop), its interfaces (internal vs customer-facing), and its boundaries against adjacent Types (Voice of Customer Platform, Survey Platform, Product Management Platform, Help Desk, Review Platform, idea management).

## Initial Boundary

Initial hypothesis before research:

- Core use: consolidate scattered customer feedback (feature requests, ideas, problems, suggestions) into one managed, attributable body of records, aggregate demand across customers, prioritize, and act — usually with a loop closed back to customers.
- Users: product managers / product teams (operators); support, customer success, sales (contributors); customers (end users of a feedback portal).
- Nearest Types: Voice of Customer Platform (separate leaf directly above it in §07), Survey Platform (§03.11), Product Management Platform / Product Discovery Platform (§12), Help Desk (§07), Review Platform (§02.10), Customer Success Platform (§07).
- Key boundary risk: conflation with Voice of Customer (survey/metric programs). The directory holds these as two separate leaves; research must keep them separable.
- Unknowns: exact object models per product; how widely vote-machinery vs other aggregation is used; whether loop-closing is definitional or merely universal in the current market; how the UserVoice repositioning ("customer intelligence") affects the Type boundary.

## Research Questions

1. What is the unit of record? What kinds of feedback does it hold, and what fields?
2. How is feedback attributed to customers (user / company / account)? What role does attribution play?
3. How does the system aggregate related feedback across many customers (merge, dedup, votes, counts, themes)?
4. How is feedback organized and prioritized (taxonomies, boards, statuses, scoring)?
5. What is the status lifecycle of a feedback item, and who changes it?
6. How is the loop closed back to customers (portal status, changelog, notifications)?
7. What capture channels exist (portal, widget, integrations, import, internal contributors)?
8. How does the feedback item relate to planned product work (features/roadmap)? Where is the seam with Product Management?
9. Who uses which surface (internal team vs contributors vs end customers)?

## Representative Products

Selection principles applied: market representation, documentation completeness, different product philosophies, different customer tiers.

| Product | Tier / posture | Philosophy |
|---|---|---|
| Canny | SMB → mid-market | public voting portal first + structured internal pipeline (new 2026 "Ideas" layer) |
| UserVoice | enterprise B2B SaaS | multi-channel feedback capture aggregated and weighted by account/revenue ("customer intelligence" positioning) |
| Productboard | mid-market → enterprise | product-management workspace in which customer feedback is a first-class input linked to planned features |
| Feature Upvote | SMB | minimal lightweight voting board; deliberate simplicity |

(Other category members — Nolt, Frill, Upvoty, FeedBear, Beamer, Savio, Pendo Feedback — were noted but not sampled; stop conditions were reached before adding more.)

## Sources

### Canny (Tier 1 — official help center, directly fetched)

- Canny Help Center root — http://help.canny.io/ (collections: Getting Started, Canny Ideas, Canny Autopilot, Canny Integrations, Canny Feedback Portal, Canny Features, Canny Emails)
- "What's the difference between posts and ideas?" — http://help.canny.io/en/articles/12694558-what-s-the-difference-between-posts-and-ideas
- "Using Canny Ideas" — http://help.canny.io/en/articles/12015303-using-canny-ideas
- Canny Ideas collection listing (Insights, Themes, Scores and formulas, Idea groups, Status syncing, Recurring Revenue Tracking, Internal roadmap scoring, CSV import, portal fields)
- Canny Feedback Portal collection (Board settings)
- Ideas Integrations listing (Intercom, Zendesk, HubSpot, Salesforce, Zapier, Chrome Extension, Segment)

### UserVoice (Tier 2 — official product pages; help center unreachable)

- https://www.uservoice.com/ (root: positioning, integrations, FAQ)
- https://www.uservoice.com/customer-feedback-software (capture → understand → act machinery; dedup/merge/account linkage/revenue weighting; closed-loop replies)
- https://www.uservoice.com/customer-feedback-portal (branded portal: submit/vote/statuses "planned, in progress, shipped", duplicate merge, public/private, changelog)

Source-access limitation: https://www.uservoice.com/knowledgebase returned 404; https://help.uservoice.com/hc/en-us failed twice (transport error, then timeout) on 2026-09-08 and was abandoned per the network-restriction rule. All UserVoice claims below are therefore evidence layer A-at-Tier-2 (official product pages) at existence-level precision only. No precise operational details (numeric limits, exact status sets, plan-gating) are asserted for UserVoice.

### Productboard (Tier 1 — official support site, directly fetched)

- Productboard Support root — https://support.productboard.com/ (categories incl. Customer Insights and Engagement, Prioritization and Roadmapping)
- "Fundamentals of Productboard" — https://support.productboard.com/hc/en-us/articles/27858826222355 (data structures: products/components/features/subfeatures hierarchy; boards; "Features aren't feedback"; statuses)
- "Quick start guide: Feedback" — https://support.productboard.com/hc/en-us/articles/26907498937235 (feedback items, insights/linking, data fields incl. Customer=Company+User, owner, tags; processing states; contributor licensing; capture integrations)

### Feature Upvote (Tier 1 — official help center; category level)

- Help center root — https://help.featureupvote.com/ (9 categories)
- "How customers use your feedback board" — category listing: Adding a new suggestion; Upvoting a suggestion or adding a comment; Searching for suggestions
- "Using your feedback board as a moderator" — category listing: Editing and commenting; Moderating; **Merging and splitting suggestions**; Bulk importing; Pinning; **Voting on behalf of customers**; Moderating comments; Search; Exporting; **Tags and categories**; **Email notifications for customers**; Email log; Moving suggestions between boards; IP blocking; Activity log
- "Company Portals" — category listing: Creating a company portal

Evidence note: article bodies for Feature Upvote were not fetched (category listings only). Claims are existence-level: the documented feature set is confirmed by official help-center structure; fine mechanics are not asserted.

## Product Observations

### Canny (evidence layer A, Tier 1 help center)

- Two-layer object model as of 2026 ("Canny Ideas is live", teams onboarded to Ideas after 2026-05-19):
  - **Idea** — the internal record of a piece of feedback: "actionable work with clear deliverables". Internal-only. Carries fields (status, custom fields incl. number/date/text/formula/score types), insights, hierarchy position.
  - **Post** — the public-facing version of an idea, visible in the Feedback Portal (voting boards). End users submit posts; admins can also publish a post from an existing idea. Updates to the Idea do not affect the Post; both can exist independently.
  - **Insight** — an attribution record attached to an idea: "pieces of information that show additional interest or context around an idea". Created manually by admins or automatically (end-user votes/comments on the linked post become insights; Autopilot captures feedback from customer conversations/calls). Insights can be attributed to users and/or companies, and are internal-only.
- **Vote vs insight rule** (documented): a vote is public and tied to a specific end user and shows on the post ("this customer requested it"); an insight is internal-only and can capture context from non-public sources without affecting vote counts.
- **Aggregation**: merge ideas (explicitly irreversible — "Once merged, an idea cannot be un-merged"; linked posts merge too); while creating an idea, similar existing ideas surface to reduce duplicates; move ideas as sub-ideas; three-level group hierarchy and three-level idea/sub-idea hierarchy; default saved views: **Triage** (new, unactioned), **Backlog** (under consideration), **Roadmap** (actively prioritized or being worked on).
- **Prioritization**: scores and formulas, internal roadmap scoring, Recurring Revenue Tracking (ARR tied to accounts behind feedback), themes.
- **Status**: idea status (internal workflow) vs post status (external communication), optionally synced via admin-defined mappings.
- **Capture channels**: portal (public voting boards, public or access-controlled), integrations (Intercom, Zendesk, HubSpot, Salesforce, Segment, Zapier), Chrome extension, Autopilot (AI capture from customer conversations/calls), CSV import.
- **Close the loop**: post status visible in portal; dedicated "Canny Emails" help collection ("emails we send, to you and your users"); changelog/announcement features in the wider product.
- Attribution note: the originator user/company is what votes and insights attach to — customers are first-class records in the system.

### UserVoice (evidence layer A at Tier 2, existence-level precision)

- Positioning has drifted to "Customer Intelligence Platform" (2026 site), but the machinery described is classic customer feedback management: "Support tickets, reviews, surveys, sales calls — UserVoice pulls every piece of customer feedback into one place, tags it automatically, and shows your whole team what to act on first."
- Three-step machinery (official "how it works"):
  1. **Capture** — "every piece of feedback from support tickets, surveys, reviews, and your in-app widget lands in one inbox, tagged by source automatically."
  2. **Understand** — sentiment and themes surface automatically (AI analysis).
  3. **Act** — "Route each piece of feedback to the right team and follow up with the customer automatically once it's resolved"; many teams pair it with a public customer feedback portal.
- **Aggregation doctrine** (stated twice, on both pages): "When five customers send the same feedback, that's one signal — not five tickets. UserVoice links every piece of feedback to the account behind it, merges duplicates into one theme, and weights it by revenue." Worked example: three people at one account asking separately for SSO → linked by account → merged into one theme → counted once → prioritized with ARR attached ("$84k ARR, 3 people, 1 count").
- **Closed loop**: "Two-way, closed-loop replies. Reply to customers from the same thread you triage in, and notify them automatically once it's resolved."
- **Portal** (official page): branded, public or restricted to logged-in customers/specific accounts; customers submit ideas and upvote; "duplicates merged automatically, so vote counts reflect real demand"; "A public status for every idea keeps customers checking back" — statuses shown as planned / in progress / shipped-class; built-in changelog ("announce what shipped right where customers are already looking").
- **Audience spread**: support (escalation, one-off vs trend), product (de-duplicated requests into roadmap with customer's own words), success (at-risk accounts from sentiment), sales (feature gaps costing deals). Role-specific views of the same feedback body.
- Distinction from survey tools, stated by the vendor: "A survey tool captures answers to questions you ask. UserVoice also captures the feedback customers give you unprompted — in tickets, reviews, and conversations — and connects all of it to the same customer and account record."
- Historical note: UserVoice pioneered the suggest/vote board format (its own comparison pages position it against Canny/Productboard/Featurebase/Frill/Aha/Savio/Pendo — all the same market category).

### Productboard (evidence layer A, Tier 1 support site)

- Product-management workspace whose feedback handling is explicit and structural:
  - **Feedback** — "when you collect feedback from a stakeholder, that feedback is packaged into feedback". Displayed on **insights boards** ("specialize in collecting, organizing, analyzing, and processing feedback"); Productboard is positioned as "the central repository for feedback about your products".
  - **Insight (link)** — "we call the link itself an insight": a link from (part of) a feedback item to an entity in the product hierarchy; one feedback item can carry many insights to different entities. "Insights are important because they bind feedback to feature ideas and generate User Impact Score."
  - **Hierarchy** — Products → Components → Features → Subfeatures; features carry customizable statuses. Explicit doctrine: "**Features aren't feedback.** Features and subfeatures are meant to represent functional ideas that can be worked on and completed. They are not for tracking feedback from stakeholders." Also: "Subfeatures aren't bugs. Productboard isn't designed for tracking bugs" — boundary against ticketing stated by the vendor.
- **Feedback data fields** (documented, ordered by the vendor): Customer (split into Company and User subfields — with the rule "record the originator of the feedback, not the agent who reported it"), Owner (the maker responsible for processing it), Tags, Name. Feedback statuses: **Unprocessed → Processed → Archived** ("nothing special happens when feedback is archived; it still appears in insights boards and still contributes User Impact Score").
- **Processing workflow** (documented four-phase example): collect → check data fields → link insights → mark processed. Boards double as filtered inboxes (by status/owner/tags); bulk edit; insights automations (if/then triage rules).
- **Capture**: Chrome extension, email forwarding addresses, Slack/Teams/Zendesk/Intercom integrations, App Store review pull, CSV import, manual creation, feedback forms; **contributors** — non-product staff (AEs, CSMs) licensed to submit feedback; they "receive updates when their feedback is processed and when linked features get updated".
- **Prioritization**: User Impact Score (aggregates demand across linked feedback), grid prioritization boards.
- **Customer-facing surface**: portals — "flexible, interactive interfaces you can share with colleagues or customers to validate" (submit, vote, see status); roadmaps shareable externally. Portal evidence is Tier 1 (promoted support article) though its body was not fetched.

### Feature Upvote (evidence layer A at category level, existence-level precision)

- Minimal voting-board product; the whole system is "feedback boards" of **suggestions**:
  - Customer side: adding a new suggestion; upvoting a suggestion or adding a comment; searching.
  - Moderator side: editing/moderating suggestions; **merging and splitting suggestions**; **bulk importing** (CSV); pinning; **voting on behalf of customers** (moderator casts a vote in a customer's name — attribution without the customer being present); moderating comments; **tags/categories**; moving suggestions between boards; exporting; activity log; IP blocking.
  - **Email notifications for customers** — moderators' actions trigger customer-facing email (existence confirmed; mechanics not asserted).
  - **Company Portals** — per-customer-company private boards (existence confirmed; mechanics not asserted).
- Philosophy: deliberate minimalism ("The Feature Upvote way"; the sample's thin pole). No product-hierarchy, no scoring engine, no revenue weighting documented. Confirms that the pipeline machinery (hierarchy, scoring, multi-channel capture) is NOT required for the Type.

## Cross-product Comparison

| Structure | Canny | UserVoice | Productboard | Feature Upvote | Evidence strength |
|---|---|---|---|---|---|
| Feedback item of record | Idea (internal) + Post (public) | feedback item in one inbox | Feedback item | Suggestion | B — all 4 |
| Customer attribution (user + company/account) | votes/insights attributed to users & companies | "linked to the account behind it", ARR attached | Customer field = Company + User | voter identity; voting on behalf of customers | B — all 4 |
| Cross-customer aggregation (merge/dedup/linked demand) | merge ideas (irreversible), duplicate surfacing | auto-merge duplicates into one theme, counted once | insights link many feedback items to one feature; UIS aggregates | merge and split suggestions | B — all 4 |
| Demand quantification | votes on posts; scores/formulas | votes; revenue weighting | User Impact Score | raw upvotes | B — all 4 (votes universal; scoring varies) |
| Organization layer | groups/subgroups hierarchy, views, custom fields, themes | tags, themes, routing | product hierarchy, tags, owner, filtered boards | boards, tags, pinning | B — all 4 (shape varies: hierarchy vs flat) |
| Status lifecycle | idea status (internal) vs post status (external), optional sync | public status per idea (planned/in-progress/shipped-class) | feature statuses (customizable); feedback Unprocessed→Processed→Archived | moderator-managed suggestion statuses (mechanics not asserted) | B — all 4 have status; exact sets vary |
| Customer-facing surface | Feedback Portal (voting boards) | branded portal, public/private, changelog | portals (submit/vote/see status) | feedback board; per-company portals | B — all 4 |
| Close-the-loop notifications | user emails collection | automatic notify on resolve; two-way replies | contributors notified on processing/feature updates | email notifications to customers | B — all 4 |
| Capture breadth | portal + 7+ integrations + AI capture + import | widest: tickets/surveys/reviews/calls/widget | internal contributors + integrations + import + forms | board itself + bulk import + API | B — varies by product posture |
| Prioritization apparatus | scores/formulas, roadmap scoring, revenue tracking | revenue-weighted themes | UIS + impact/effort grids | none beyond votes | A/C — posture-dependent |
| Product-planning linkage | roadmap views within Ideas | "feature request management moves them through to shipped" | explicit: insights bind feedback to features in hierarchy | none/weak (export) | varies — strongest in Productboard |
| Multi-role access (contributors vs makers) | admins | role-specific views for support/product/success/sales | contributor licenses for AEs/CSMs | moderators only | B — 3 of 4 (Feature Upvote minimal) |

## Canonical Model — Four Abstraction Levels

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **The customer feedback item of record** — a persistent, individually identified record of one piece of customer feedback about the organization's product (a request, idea, problem, suggestion, or reaction), attributed to the customers who gave it (user and, in business contexts, their company/account). Remove attribution → internal idea management, not *customer* feedback management. Remove persistence → collection/inbox only.
2. **Cross-customer aggregation** — related feedback from many customers consolidated into one managed item (merge/dedup, linked contributions, or vote/contributor counts), so demand is held as one signal with a countable contributor base rather than many scattered remarks. Remove → support ticket queue where every piece stands alone.
3. **The managed feedback-to-decision pipeline** — items organized under a shared taxonomy (product areas, tags, boards), triaged and tracked through statuses toward the organization's product decisions, so the feedback body is managed over time rather than reacted to ad hoc. Remove → a suggestion box or comment feed.

Jointly-held is load-bearing: (1) alone = a feedback archive; (2)+(3) without customer attribution = internal idea management; (1)+(2) without the pipeline = collection with counting; (1)+(3) without aggregation = triage queue with no demand signal.

### Level 1 — Common Mature Structure

Present in essentially all mature current products (all 4 sampled), but not required to recognize the Type:

- **Customer-facing feedback surface** — a portal/board (public or customer-restricted) where customers submit, browse, vote, and comment.
- **Voting as demand quantification** — upvotes; votes linked to identified customers; proxy voting on behalf of customers.
- **Merge/duplicate machinery** — merging related items (sometimes irreversible), duplicate suppression at submission time.
- **Status model with external meaning** — statuses visible to customers (planned / in progress / shipped-class) alongside internal-only states; internal processing gates (unprocessed → processed).
- **Closed-loop communication** — status updates, changelog/announcement surfaces, automatic notifications to voters/contributors when an item progresses or ships.
- **Organization layer** — product areas/tags/boards; ownership assignment; saved filtered views as working inboxes.
- **Multi-channel capture** — integrations from support desks, chat, CRM, email forwarding, browser extensions, CSV import.
- **Prioritization apparatus** — scoring beyond raw votes (impact scores, formulas, revenue weighting).
- **Contributor roles** — non-product staff (support/success/sales) submitting feedback on behalf of customers.

### Level 2 — Variant / Optional Structure

- Portal openness: fully public vs logged-in customers vs per-account private boards ("company portals").
- Internal/external separation: split objects (internal idea vs public post) vs single item with visibility control vs internal-only feedback (no public surface at all).
- Hierarchy depth: flat boards (thin pole) vs multi-level product-area hierarchies.
- Demand weighting basis: raw votes vs impact scores vs revenue/ARR weighting (B2B pole).
- AI capture and analysis (conversation capture, auto-tagging, sentiment/themes) — era-current.
- Breadth of capture: portal-first vs multi-channel (tickets/surveys/reviews/calls) vs internal-contributor-first.
- Linkage to delivery tools (Jira/Azure DevOps) — handoff beyond the Type's core.
- Adjacent-layer coupling: NPS/micro-surveys, roadmap publication, in-app widgets.
- Moderation controls (comment moderation, IP blocking), import/export, APIs.

### Level 3 — Vendor-specific (Research Notes only)

- Canny: Autopilot AI capture; the May-2026 Ideas migration and post/idea status-sync mappings; Fibonacci/rating/range field types; documented character limits (400/5000/40/600/30/50); "Canny Emails" collection.
- Productboard: Spark AI agent and skills; teamspaces; "User Impact Score" name; contributor license model; the four-phase recommended workflow as vendor guidance.
- UserVoice: "customer intelligence" repositioning and revenue-weighted theme examples; the Acme/$84k ARR worked example; pricing posture claims.
- Feature Upvote: company portals naming; Help Scout-hosted docs; slide deck, "The Feature Upvote way".

## Vendor-specific Findings

See Level 3. Additionally:

- The internal-idea/public-post split is currently a Canny-specific object design (2026); UserVoice and Productboard realize the same conceptual separation (public status / internal processing) without a separate object. Treat the split object as an implementation, not a canonical structure.
- Revenue weighting is a B2B-enterprise posture (UserVoice explicitly, Canny and Productboard as features among others); Feature Upvote demonstrates the Type works without it.
- UserVoice's "customer intelligence" repositioning stretches the Type toward analytics; its own use-case taxonomy still names this category (feature request management, customer feedback portal, idea management software) — drift noted, not disqualifying.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (and the "remove-this" test) |
|---|---|---|
| Voice of Customer Platform | adjacent sibling leaf in §07; strongest seam | VoC is survey/metric-centered experience measurement (NPS/CSAT/CES programs, journeys, dashboards); CFM's unit of record is the individual item-level feedback record managed toward product decisions. Remove the item-of-record+pipeline and keep survey instruments/scores → VoC territory. Vendors blur this (UserVoice sells both use cases; UserVoice's own FAQ distinguishes survey tools from unprompted feedback capture). |
| Survey Platform (§03.11) | adjacent upstream | Survey platforms build structured question instruments and analyze responses; CFM aggregates unprompted and prompted free-form feedback into a persistent demand body. A survey response can become a captured feedback item, but surveys are not the system of record for demand. |
| Product Management Platform (§12) | downstream consumer of feedback; straddle risk | PM platform's central object is the planned feature/roadmap; CFM's is the customer feedback item. Productboard straddles (feedback pillar inside a PM workspace) but itself documents the seam: "Features aren't feedback." Remove the feedback-attraction machinery and keep planning → PM platform. |
| Product Discovery Platform (§12) | adjacent upstream | Discovery tools gather qualitative research (interviews/highlights) as evidence for decisions; CFM holds customer-attributed feedback items as a managed standing body with demand quantification and customer-facing loop. Overlap exists in insight-linking machinery. |
| Help Desk / Ticketing (§07) | capture source + neighbor | Ticket = one customer's issue, resolved and closed, service-level success; feedback item = demand signal aggregated across customers toward product change. Tickets are a capture channel into CFM. Remove aggregation-across-customers and keep per-case resolution → ticketing. |
| Review Platform (§02.10) | public-facing neighbor | Reviews are public consumer evaluations for other buyers; CFM is the vendor-internal management of customer voice. Some CFM tools import app-store reviews as a capture channel (Productboard), which is the seam, not an identity. |
| Community Platform (§01.06) | capture surface neighbor | Community discussion threads are conversations; CFM holds managed, stateful feedback items. Public feedback portals borrow community mechanics (votes, comments) but their purpose is demand management, not community. |
| Idea Management (internal) | not a directory leaf | Internal innovation idea management is the same machinery minus external-customer attribution; UserVoice sells both use cases. CFM is defined by the customer attribution leg. |
| Complaint & Escalation Management (§07) | sibling in §07; joint-review flag from that pass | Complaint/escalation tools govern one formal dissatisfaction case individually to resolution and remedy (regulated, case SLAs); CFM aggregates the customer voice into demand signals. The complaint-escalation pass recorded that 3 of 4 of its sampled products ship feedback/survey capture alongside complaints — capture feeds CFM while governed resolution stays there; products legitimately straddle. Discharged from this side; seam consistent. |

## Historical / Market-Sample Check

- Would older / thinner products still fit? Yes. A shared spreadsheet of customer feature requests — one row per request, columns for requester account, running count, owning PM, and status — satisfies all three Level-0 legs (item+attribution, count-based aggregation, managed status pipeline). Email-folder feature-request triage is thinner but passes legs 1 and 3 with count aggregation done mentally — the canonical abstraction deliberately does not require vote machinery, portals, or scoring engines.
- UserVoice itself (2008-era suggestion boards) passes the core without AI, revenue weighting, or multi-channel capture: items, customer attribution, vote counts, admin-changed statuses.
- Feature Upvote (the thinnest current pole) passes the core with boards + votes + merge + statuses.
- Therefore: portals, votes-as-UX, scoring engines, revenue weighting, AI capture, integrations are all held OUT of the defining core. The definition is not overfitted to the 2026 portal+AI generation.

## Uncertainties

1. UserVoice operational detail rests on Tier 2 product pages only (help center unreachable). Existence of machinery (capture/merge/status/portal/changelog/notifications) is confirmed; mechanics, defaults, and status sets are NOT asserted anywhere.
2. Feature Upvote article bodies not fetched; mechanics (e.g., exact notification triggers, status value sets) not asserted.
3. Productboard portal mechanics known only at the level of the promoted-article summary; portal body not fetched.
4. The exact historical boundary of the Type before ~2008 (pre-UserVoice) was reasoned, not document-verified: no archived primary source was consulted.
5. Whether loop-closing should be promoted into the defining core: all 4 sampled products ship it as a first-class capability, but the spreadsheet-era pass shows the Type is recognizable without any customer-facing loop. Held at Level 1 (strongest L1 candidate); flagged for future re-examination.
6. Possible taxonomy note: the directory's §07 holds "Voice of Customer Platform" and "Customer Feedback Management" as separate leaves — research supports keeping both, with the survey/metric-program vs item-level-demand seam. Some vendors (UserVoice; also Pendo-class suites) span both, which will strain future passes on neighboring leaves.

## Final Synthesis

A Customer Feedback Management application is the vendor-side system of record for the customer's voice about a product. Its defining core is three jointly-held structures: (1) the customer feedback item of record — a persistent identified record of one piece of feedback (request/idea/problem/suggestion), attributed to the customers who gave it; (2) cross-customer aggregation — related feedback consolidated into one managed item with a countable contributor base (merges, linked contributions, votes); (3) the managed feedback-to-decision pipeline — items organized under a shared taxonomy, triaged, and tracked through statuses toward product decisions. Around this core, mature products add the customer-facing portal (submit/vote/comment), voting, duplicate suppression, customer-visible statuses with closed-loop notifications and changelogs, multi-channel capture integrations, prioritization apparatus, and contributor roles. The Type sits between Voice of Customer (survey/metric programs — different unit of record) and Product Management (planned work — downstream consumer of feedback), with the item+attribution+aggregation+pipeline combination as its identity.
