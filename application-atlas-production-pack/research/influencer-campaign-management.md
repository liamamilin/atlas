# Research Notes — Influencer Campaign Management

## Research Goal

Understand what "Influencer Campaign Management" is as an Application Type: what software of this kind does, who operates it, what objects exist inside it, how a campaign actually moves from setup to results, and where its boundaries lie against the neighboring creator-economy Types (Influencer Marketing Platform, Brand-Creator Marketplace, UGC Creator Marketplace, Affiliate Management Platform, Social Media Management, Marketing Campaign Management).

## Initial Boundary

- Working hypothesis: this leaf is the **campaign-execution slice** of influencer marketing — the brand-side management of individual creator campaigns (brief → participants → deliverables → content review → publication → results), as distinct from the broader "Influencer Marketing Platform" leaf (creator database/discovery/relationship management/program measurement) listed as a sibling in §06.
- Directory context: §06 lists both "Influencer Marketing Platform" and "Influencer Campaign Management" as separate leaves, mirroring the directory's pattern of pairing a broad platform leaf with a campaign-execution leaf (e.g., Marketing Campaign Management Platform; Advertising Campaign Management vs Media Buying/DSP).
- Known risk recorded up front: in the real market, campaign execution is almost always sold as the core module of a broader influencer-marketing platform; a standalone campaign-only product category is thin (mainly UGC-campaign tools and agency tooling). This leaf may be a capability-level view of the same market as Influencer Marketing Platform — flagged for joint review rather than silently resolved.
- Nearest neighbors: Influencer Marketing Platform (sibling, unprocessed), Brand-Creator Marketplace (processed, left a joint-review flag addressed to this leaf), UGC Creator Marketplace (sibling, unprocessed), Affiliate Management Platform (processed, drew the campaign-vs-commission seam), Social Media Management Platform, Marketing Campaign Management Platform, Creator CRM.

## Research Questions

1. What is the central object — campaign, project, activation? What does it carry (goals, dates, budget, brief)?
2. How do creators enter a campaign (direct add, invitation, application) and what is the per-creator participation record?
3. How are deliverables specified (content types, platforms, hashtags/@mentions, due dates, disclosure)?
4. How does the content workflow work — draft submission, review/approval outcomes, revision loops, publication, content collection/binding?
5. How is compensation handled (cash, product gifting, commission/affiliate; pre- vs post-payment; budgets)?
6. What does the brand see for progress and results (per-participant status, published content, performance metrics)?
7. What does the creator see (portal, tasks, compensation, terms acceptance)?
8. Which capabilities are common mature structure vs definitional (recruitment pages, contracts, tracking links, paid amplification, AI)?
9. Where are the boundaries vs marketplace, affiliate, UGC, SMM, and the sibling platform leaf?

## Representative Products

Selection logic: market representation (enterprise + e-commerce mid-market poles), documentation completeness (Tier-1 help centers where possible), different product philosophies (enterprise workflow-governance vs e-commerce-native vs self-serve e-commerce vs enterprise AI-measurement), different customer tiers.

| Product | Pole | Customer tier | Evidence level |
|---|---|---|---|
| Later Influence (ex-Mavrck) | enterprise workflow-governance platform | enterprise brands | Tier 1 — dedicated help center (help-influence.later.com), campaign model fully documented |
| GRIN | e-commerce-native creator management | mid-market/large e-commerce | Tier 1 — help center (help.grin.co), campaign/activation docs |
| Aspire | self-serve e-commerce influencer platform | SMB/mid-market e-commerce | Tier 1 — help center (help.aspireiq.com), project workflow docs |
| CreatorIQ | enterprise AI-measurement platform | global enterprises/agencies | Tier 2 — official product pages (creatoriq.com), Campaign Execution page; help center unreachable |

Rejected/abandoned samples: Kolsquare (help center transport error ×2), Influencity (404 + transport error), IZEA (transport error ×2), HypeAuditor (timeout), Captiv8 (timeout), Traackr (transport error), Upfluence (403 in a prior pass — not retried). Per source-access rules these were abandoned after 1–2 failures; no claims about them are made.

## Sources

- Later Influence Help Center (Zendesk): https://help-influence.later.com/hc/en-us — categories "Creating Campaigns", "Running Campaigns", "Measuring Performance"; articles: Create a New Campaign; Campaign Brief; Overview of Campaign Workflow Stages & Logic; Navigating the Campaign Workflow Tab; Workflow Stages: Draft & Draft Review; Measuring Performance category. (Fetched 2026-09-07)
- GRIN Help Center (Intercom): https://help.grin.co/ — collections Running Programs / Activations / Campaigns; articles: Reviewing a Creator's Task Progress; What Creators See When They Are Invited to a Campaign. (Fetched 2026-09-07)
- Aspire Help Center (Intercom): https://help.aspireiq.com/ — collections Projects & Application Pages; Briefs & Contracts; Managing Collaborations; articles: Overview of project workflow stages; How does the Track Posts stage work?. (Fetched 2026-09-07)
- CreatorIQ official site: https://www.creatoriq.com/ and Campaign Execution page https://www.creatoriq.com/influencer-marketing-solution/influencer-campaign-management. (Fetched 2026-09-07)
- Prior-pass context (same production pack): research/brand-creator-marketplace.md (joint-review flag), research/affiliate-management-platform.md (campaign-vs-commission seam), STATUS.md boundary entries.

## Product A — Later Influence (enterprise pole)

### Key observations (Layer A — directly observed)

- **Campaign is the central object.** "Campaigns" is a top-level section; campaigns are created, named, described; a campaign has a **Setup** tab with seven sub-tabs: **Marketing Plan** (name, description, brand-suitability guidelines, **campaign-level budget field** tracking allocated/paid/remaining across incentives), **Deliverables** ("what creators are expected to produce — content types, due dates, required links or reference materials"), **Application** (required social accounts, contact fields, custom survey questions), **Brief** (creator-facing), **Incentives** (cash, gift cards, shipped product), **Workflow Stages**, **Message Templates**.
- **Campaign status: Draft → Live.** "You can adjust all setup before you set the campaign Live." Once Live, workflow editing becomes limited (can only disable empty stages; cannot add/reorder/rename).
- **Per-creator participation record carried through a workflow.** Default **12 stages in 4 phases**: Candidates (Candidates / Invited / Applied / Deliverables), Participants (Confirmation / Pre-Payment / Draft / Draft Review / Content Creation), Complete (Post Review / Post-Payment / Complete), Dropped. Content Creation, Complete, Dropped are always required; the rest optional. Custom stages can be added (examples given: Product Shipped, Legal Review, Event Participation).
- **Automatic vs manual promotion.** Automatic: into Applied (application submitted), out of Confirmation (creator confirms; opt-out → Dropped), out of Pre-/Post-Payment (incentives fulfilled via Stripe or Tango Card), into Draft Review (all required drafts submitted), out of Content Creation (all required content deliverables tracked). Manual: Candidates, Invited, Deliverables, Draft Review, Post Review, custom stages. "Automation will never move a creator backward."
- **Workflow tab = the campaign management hub.** Stage menu with per-stage creator counts; creator cards (profile image, demographics, connected social accounts); **Campaign Details** per creator with sub-tabs History / Drafts / Content / Incentives / Tracking Links. Bulk actions: Send Message, **Promote** (next stage), **Drop**, **Pay** ("available in payment stages only; marks all associated incentives as Fulfilled; a confirmation dialog always appears before any funds are sent"), Move to workflow stage, Assign Content Deliverable, Update due date, Update draft due date, Add to another campaign, Add to list. CSV export per stage.
- **Draft & Draft Review paired stages.** Creators submit drafts → team reviews → outcomes: **Approved / Approved with Corrections / Needs Work** (back to Draft for a new version). Version tracking per deliverable; only one draft per deliverable "In Review" at a time; drafts can be uploaded by creators, brand users, or internal users. **Shareable review links** let external stakeholders (clients, legal) review drafts without logging in — the team still owns approval.
- **Brief structure.** Two sections: **Public Campaign Summary** (visible pre-acceptance on the "Find Campaigns" page: content style, platforms, compensation overview, timeline) and **Full Campaign Brief** (post-confirmation: messaging scripts, visual concepts, requirements, linked documents). Default template: About the Brand & Product / Concept / Must-Hit Messaging / Inspiration / Draft Submission Guidelines. Platform-specific templates (Instagram post/Reels/Stories, TikTok, YouTube, Pinterest) specify counts, required hashtags, @brand-handle tagging "as a Branded Content Partner", filming/editing guidance, music licensing (TikTok Commercial Library / Meta Sound Collection), and **FTC disclosure guidelines** (#ad/#sponsored/#Gifted formats, verbal disclosure, language matching, placement at start of video).
- **Incentives/compensation.** Cash (Stripe), gift cards (Tango Card), shipped product; **Pre-Payment vs Post-Payment** stages; Incentive Advisor ("data-backed compensation estimates"); Shopify codes; incentive fulfillment tracked per creator; Budgets tab for incentive spending.
- **Recruitment into campaign.** Application questions with creator insights/filtering; Adding and Inviting Creators; Applicant Review; Confirming Participation; sharable applicant-review links for collaborators.
- **Measurement.** Clicks & Conversions overview; Conversion Tracking Setup; **content binding** to campaigns (with unbinding/moving content between campaigns); TikTok/Instagram/Pinterest metrics reference; **EMV & ROI**; Campaign Performance Report; paid media boosting (Meta Partnership Ads, TikTok paid media reporting).
- **Tasks** and **Later EdgeAI** as organizational/AI aids.

## Product B — GRIN (e-commerce-native pole)

### Key observations (Layer A)

- **Campaign/Activation as the organizing unit.** Help center collection "Running Programs": "Set up and manage successful brand activations, campaigns, and partnerships." **Naming migration documented**: accounts joined on/after January 23, 2023 have **Campaigns replaced by Activations** ("You can use Activations to manage and organize your creator marketing programs") — the same object renamed, evidence that campaign/project/activation are one concept family.
- **Campaign Work Room** with a **Progress** tab: "review task completion progress by your creators… monitor your creator's deliverable progress", latest content date, posted content, uploaded files; one-click **email reminder** to creators whose post-deadline is nearing.
- **Creator-facing proposal flow (Live URL portal).** Invited creators review the campaign proposal on their personal Live URL: **Overview** ("why you are implementing this campaign and why you have chosen them"), Proposal Steps, **Compensation** ("payment, commission, and/or products"), **Products** selection (when product compensation), **Review Tasks** ("all the media deliverable tasks… as well as #hashtags and @mentions that will need to be included in each post"), **Social Networks** sync, **Shipping Information**, **Personal Information**, **Content Rights** ("creators will agree to your terms and conditions… need to agree and accept the terms set for the campaign"), then submit the proposal. Brand reviews/manages proposals in the Work Room.
- Surrounding collections confirm the platform frame: Recruiting Creators, Managing Contacts, Sending Messages, Tracking Content (creator-generated content monitoring, missing-content troubleshooting, downloads), Reporting, Managing Your Brand, Help For Creators (39 articles).

## Product C — Aspire (self-serve e-commerce pole)

### Key observations (Layer A)

- **Project = the campaign unit**, with a **customizable workflow of stages**. Documented common stages: Send Welcome Email; **Briefs** ("outline exactly what kind of content you are looking for and when you'd like it completed by"); Member Information (shipping address); Sales Links + Promo Codes (mass-generate codes/links, email them); Product Fulfillment (Shopify-integrated gifting); Product Catalog (creator selects products, brand approves/edits/rejects orders); **Content** ("set up structured approval processes and allow creators to submit their work for review before they post"); Payment (PayPal). Optional stages: **Contract** (Dropbox Sign e-signature), **Track Posts** (mention listening on Instagram/TikTok), Product Request Form. **Custom stages** supported ("send a thank you note post-collab or ask for a product review").
- **Per-member progression.** Members move through stages; a **Completed** stage exists; "Restart Project" returns members to the first stage; Track Posts alternates members between "Wait for Live Posts" and "Review Posts" as they tag the brand, with posts **assigned to a project or group**.
- **Recruitment surfaces.** **Application Pages** (custom landing pages with editable questions to recruit campaign applicants); **Marketplace publishing** ("Publish your project in the Marketplace to receive hundreds of proposals from high-quality influencers"); unlisting; preventing paid creators from applying to unpaid (product-only) projects.
- **Applicant review.** Vetting (approve/reject), quick filters, **Group Applicant Review**, and an **Applicant Review Portal** for external reviewers with feedback/approvals.
- **Briefs & Contracts.** Briefs (Standard/Flexible) with **Content Guidelines** as the deliverables; sent individually or in bulk; creators review/edit/accept; additional T&Cs attachable; briefs editable/cancellable after sending; signed briefs reviewable. Contracts via e-signature templates (Dropbox Sign/Docusign), counter-signers, status tracking.
- **Content review.** "How do I review content?" — review a member's content **before it goes live**; manual completion marking; **Group Content Review** with multiple content approvers; **Content Hub** as the centralized content location.
- **Money.** Budget Tracking & Payments collection (payment methods, sending payments to members).
- **Reporting & Analytics** "Measure the performance of your projects, members, and content" (21 articles).

## Product D — CreatorIQ (enterprise AI-measurement pole, Tier 2)

### Key observations (Layer A — product pages only; operational detail not asserted)

- Dedicated **"Campaign Execution"** capability page (URL literally /influencer-campaign-management): "Campaign Management Made Simple — Streamline workflows, approvals, and reporting, all on one intuitive and centralized platform."
- **Instant campaign set-up**: "Input your campaign requirements, choose the modules your team needs, and follow a step-by-step flow to build campaigns."
- **Work with creators at scale**: "Communicate with creators en masse — invite them, share briefs, and approve their content — all without ever leaving your campaign page."
- **Centralized content review and approval system**: "Instantly view all organic and paid content authored by your community, alongside an array of performance metrics."
- **Intelligent content tracking**: "AI models automatically collect all posts by your selected creators that mention your brand during the campaign window, then layer in keywords for fine-tuning."
- **Integrated workflows for contracts and payments**; **real-time campaign performance reporting** (vendor claims metrics "refresh every eight hours" — vendor figure, not asserted in final doc); role-based team collaboration; FAQ confirms onboarding + content approvals + reporting centralization, contracts/compliance/payments automation, dashboards for reach/engagement/conversions/ROI.
- Platform menu separates **Creator Management** (CRM) from **Campaign Execution** — vendor-side confirmation that relationship management and campaign execution are distinct capability layers. Other modules: Discovery, Evaluation, Measurement, Recruit, Convert, Pay, BenchmarkIQ, SafeIQ, ExchangeIQ, Enterprise Governance.

## Cross-product Comparison

| Dimension | Later Influence | GRIN | Aspire | CreatorIQ |
|---|---|---|---|---|
| Campaign unit name | Campaign | Campaign → **Activation** (renamed 2023) | **Project** | Campaign |
| Campaign setup | 7 setup tabs (plan/budget, deliverables, application, brief, incentives, workflow, messages) | proposal config (compensation, tasks, rights) | project + workflow stages + application page | step-by-step flow, module selection |
| Participant record | creator in workflow stage w/ Campaign Details (history/drafts/content/incentives/tracking) | creator proposal + Progress in Work Room | member in project stage | creators in campaign |
| Deliverable spec | Deliverables tab + Brief templates (platform-specific, hashtags, @mentions, disclosure) | Review Tasks w/ hashtags & @mentions | Briefs w/ Content Guidelines | briefs shared en masse |
| Content review | Draft/Draft Review stages, 3 outcomes, versions, external review links | posted-content review in Progress | Content stage approval pre-posting; Group Content Review | centralized review & approval (organic + paid) |
| Content collection | binding to campaign; move/unbind | automatic tracking of creator content | Track Posts mention listening (IG/TikTok) | AI models collect brand-mentioning posts in campaign window |
| Compensation | incentives (cash/gift card/product), pre/post-payment stages, Pay action, budgets | compensation = payment/commission/products in proposal | Payment stage (PayPal), Budget Tracking & Payments | integrated payments (Pay module) |
| Recruitment into campaign | application + invite + applicant review | invite to campaign + proposal | application pages + marketplace publishing + invite | invite en masse |
| Creator portal | creator-facing campaign manager (Find Campaigns, tasks) | Live URL proposal portal | Creator Portal | (not asserted) |
| Results | Campaign Performance Report, EMV/ROI, conversions | Reporting collection | Reporting & Analytics (projects/members/content) | real-time dashboards (reach/engagement/conversions/ROI) |
| Contracts | (not observed in fetched pages) | content-rights acceptance in proposal | e-signature contracts | integrated contract workflows |
| Paid amplification | Meta Partnership Ads / TikTok paid media | (not observed) | Paid Ads collection (allowlisting, partnership ads, spark ads) | organic + paid content in one review view |

### Evidence layers

- **Layer A (directly observed, per product):** all bullet observations above, tied to fetched official pages.
- **Layer B (cross-product commonality):** campaign-as-unit; per-creator participation records in a stage workflow; brief/deliverable specification incl. hashtags/@mentions/disclosure; content review/approval loop; content collection bound to campaign; compensation machinery; recruitment surfaces; creator-facing portal; campaign-level reporting. Each supported by ≥3 of 4 products (contracts: 2–3; paid amplification: 3).
- **Layer C (canonical inference):** the Type is the brand-side execution system for creator campaigns; the campaign is a managed container that binds creators, obligations, content, money, and results into one progressing workflow.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

1. **Campaign as the managed unit** — a brand-defined, time-bounded creator-marketing effort (name, scope, timeline; commonly budget).
2. **Per-creator participation records bound to the campaign**, each carried through a managed participation workflow (onboarding/selection → obligations → delivery → completion or drop).
3. **Brief / deliverable specification** — the campaign defines what content creators must produce, on which platforms, by when (incl. required tags/mentions and disclosure expectations).
4. **Content bound to the campaign** — submitted drafts and/or published posts are collected and attached to the campaign and the responsible creator.
5. **Campaign-level progress and results** — the brand can see where each participant stands and what the campaign produced.

Removal tests: remove the campaign container → generic creator CRM/messaging; remove participation workflow → a brief document tool; remove deliverable spec → a contact list; remove content binding → outreach tool; remove progress/results → a spreadsheet. In every case the product stops being recognizable as influencer campaign management.

### L1 — Common Mature Structure

- Compensation machinery: incentive configuration (cash / product gifting / commission), payment stages or payment actions, campaign budgets, fulfillment tracking.
- Recruitment machinery: application pages/forms, invitations, applicant review/approval (incl. external reviewers).
- Creator-facing portal: campaign overview, tasks, compensation, shipping info, terms acceptance, proposal/draft submission.
- Content approval workflows: pre-publication draft review with approve/approve-with-corrections/revise outcomes; multiple approvers; external stakeholder review links.
- Automated content collection: mention listening and/or platform-API binding of published posts to the campaign.
- Contracts & terms: e-signature contracts, T&Cs, content-rights acceptance.
- Tracking links / promo codes for sales attribution inside campaigns.
- Message templates & workflow automation (stage-triggered emails, reminders).
- Product gifting/fulfillment coordination (catalogs, shipping).
- Campaign reporting: per-campaign performance, EMV/ROI, exports.
- Paid amplification of creator content (partnership ads, allowlisting, spark ads).
- Team roles/permissions; agency/multi-stakeholder collaboration; tasks; AI assistance.

### L2 — Variant / Optional Structure

- Unit naming: campaign vs project vs activation (same object family — GRIN's own rename is direct evidence).
- Workflow philosophy: fixed default stage set with toggles (Later) vs fully customizable stage lists (Aspire) vs less-documented flows (GRIN/CreatorIQ).
- Participation entry: open applications (public application link / marketplace listing) vs invitation-only vs direct assignment.
- Marketplace publishing of campaigns (Aspire Marketplace; Later "Find Campaigns") — seam toward Brand-Creator Marketplace.
- UGC-only campaigns (content as ad asset without audience posting) — seam toward UGC Creator Marketplace.
- Affiliate/commission campaigns inside the campaign tool — seam toward Affiliate Management Platform.
- Enterprise governance: multi-brand/multi-region workspaces, role-based access, brand-safety/suitability screening.
- Deployment/integration posture: SaaS with platform APIs, commerce integrations (Shopify), e-signature, payment rails.

### L3 — Vendor-specific (stays here)

- Later Influence: 12 default stages/4 phases; Draft Review outcomes (Approved / Approved with Corrections / Needs Work); "automation never moves backward"; Incentive Advisor; Tango Card/Stripe rails; Find Campaigns page; Public Campaign Summary; brand-suitability guidelines feeding AI; Later EdgeAI; drafts synced with Later Social.
- GRIN: Activations rename (Jan 23, 2023 cutoff); Live URL; Campaign Work Room; Progress tab with one-click reminder email; proposal step sequence (Overview → Compensation → Products → Review Tasks → Social Networks → Shipping → Personal Info → Content Rights).
- Aspire: Project Super Tables; Track Posts stage (IG/TikTok mention listening; Wait for Live Posts ↔ Review Posts); Product Catalog stage with order approval; Restart Project; Content Hub; Group Content Review; Applicant Review Portal; Standard vs Flexible Briefs.
- CreatorIQ: "refresh every eight hours" claim; Creator Graph; module names (Recruit/Convert/Pay/BenchmarkIQ/SafeIQ/ExchangeIQ); SafeIQ brand safety.

## Vendor-specific Findings

See L3. Generalization risks flagged: (1) GRIN's Campaigns→Activations rename shows unit naming is vendor vocabulary, not structure; (2) Later's 12-stage default is one product's workflow template, not the industry standard — Aspire's stage list differs materially; (3) CreatorIQ's 8-hour refresh is a vendor performance claim.

## Rejected Findings

- **"Campaign management = the whole influencer marketing platform"** — rejected as a definition (would erase the sibling leaf), but recorded as the central taxonomy tension: all four sampled products are broader platforms that *contain* campaign execution. The defining core above is the execution slice itself.
- **Payment execution as definitional** — rejected: compensation terms are universal in the sample, but payment *execution* is stage-optional (Later's pre/post-payment stages are optional; gifting-only campaigns exist — Aspire documents product-only campaigns). Compensation configuration is L1.
- **Creator discovery/database as definitional** — rejected: discovery belongs to the broader platform Type; campaigns can be staffed by direct assignment (Later Candidates optional; Aspire direct add/invite).
- **AI content tracking as definitional** — rejected: Aspire's manual Track Posts and GRIN's manual progress review satisfy the core; AI collection is today's dominant implementation of content binding (L1).
- **Creator portal as definitional** — rejected: participation can be managed via email + links; portals are the common modern implementation (L1).
- **Fixed stage vocabulary as definitional** — rejected: stage names/counts differ per product; the invariant is the managed progression, not the labels.

## Boundary Findings

1. **vs Influencer Marketing Platform (sibling leaf, unprocessed) — the central taxonomy tension.** All four sampled products self-describe as influencer/creator marketing platforms; campaign execution is their core module. No standalone campaign-only product was verified in this pass (UGC-campaign tools exist but lean toward the UGC marketplace leaf). Working seam proposed for joint review: **Influencer Marketing Platform = the brand-side program system of record** (creator database/discovery, relationship management, program-level measurement — with campaign execution as one module); **Influencer Campaign Management = the campaign-execution layer** (the campaign lifecycle as the defining object). Test: does the product's center of gravity sit on the campaign container (this leaf) or on the creator relationship/database across campaigns (platform leaf)? CreatorIQ's own menu separating "Creator Management" from "Campaign Execution" supports the two-layer reading. Candidate outcomes: two Types with this seam, or this leaf reclassified as a capability/variant of the platform leaf — taxonomy-owner decision; recorded, not silently resolved.
2. **vs Brand-Creator Marketplace (processed; their flag addressed here).** Marketplace = two-sided venue: creator supply as discoverable/transactable objects, creator-side portal where opportunities arrive, platform-executed compensation. Campaign management = brand-side execution tool: the campaign container is primary; creator portals exist to fulfill campaign obligations. Products straddle (Aspire publishes projects to its Marketplace; Later exposes a Find Campaigns page) — the marketplace module is an optional recruitment surface, not the defining core. Test adopted from the marketplace pass: genuine platform-side creator venue + platform-executed compensation = marketplace core present; campaign workflow as center of gravity = this Type.
3. **vs Affiliate Management Platform (processed).** Their recorded seam adopted: campaign/content relationship as primary object = this Type; attributed conversion + commission as primary object = affiliate. Later Influence ships "Affiliate Campaigns" as a deliverable type — commission mechanics appear as a campaign variant inside this Type without flipping the primary object.
4. **vs UGC Creator Marketplace (sibling, unprocessed).** UGC-only deliverables (ad-usable content, no audience posting) appear inside this Type as a content-format variant (Later brief template lists "UGC, posted" formats). Flag for joint review: if the deliverable is purely an ad asset and the venue is creator-facing, the product belongs to the UGC marketplace leaf.
5. **vs Social Media Management Platform.** SMM platforms schedule/publish the *brand's own* content; this Type coordinates *creators'* content. Vendor-side acknowledgment of the seam: CreatorIQ markets a Sprinklr integration for unified owned/earned/paid/creator measurement; Later Influence syncs drafts with Later Social (an SMM product) while keeping campaign workflow separate.
6. **vs Marketing Campaign Management Platform (§06 sibling).** Generic campaign management orchestrates channels/assets/audiences; this Type carries creator-specific semantics (per-creator participation, content deliverables, usage rights, disclosure, gifting). A generic campaign tool without creator-participation semantics is not this Type.
7. **vs Creator CRM.** Relationship records vs campaign execution. CreatorIQ's menu separates Creator Management from Campaign Execution — vendor-side confirmation. A creator CRM holds the relationship across campaigns; this Type runs the bounded effort.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products fit the L0? Pre-platform practice (blogger/seeded campaigns run on spreadsheets + email, late 2000s–early 2010s; marketplace-heritage products like IZEA's sponsored-post campaigns) implements the same core: a defined campaign effort, a per-blogger participation list, a brief (post requirements, links, disclosure), collected post URLs bound to the campaign, and progress tracking — without AI tracking, portals, or payment rails. Regional European products (Kolsquare-class, unreachable this pass) are structurally the same category. The L0 therefore survives the historical check; AI collection, portals, payment rails, and paid amplification are modern implementations, not definitional.

## Uncertainties

- CreatorIQ evidence is Tier-2 (product pages); its operational workflow (stage model, review mechanics) was not asserted — only its capability claims.
- GRIN's Activations article returned 401; Activations mechanics are inferred from the documented rename note + Campaign-era articles + collection descriptions. Kept qualitative.
- Contracts in Later Influence were not observed in fetched pages (may exist); contracts documented directly in Aspire and claimed in CreatorIQ — treated as common, not universal.
- Kolsquare/Influencity/IZEA/HypeAuditor/Captiv8/Traackr unreachable — European and marketplace-heritage poles rest on structural reasoning, not direct evidence.
- Exact numeric limits (participant counts, refresh intervals, fee rates) intentionally not asserted; CreatorIQ's "8 hours" is a vendor claim kept in research notes only.
- Whether any standalone (non-platform) influencer campaign-management product category exists at scale: unresolved; UGC-campaign tools are the nearest candidates but belong to a sibling leaf's review.

## Final Synthesis

Influencer Campaign Management is the brand-side execution application for creator campaigns. Its defining core is small: a campaign as the managed unit; per-creator participation records bound to that campaign and carried through a managed workflow; a brief/deliverable specification (what content, where, when, tagged how); content — drafts and published posts — collected and bound to the campaign; and a campaign-level view of progress and results. Around this core, mature products add compensation machinery (incentives, budgets, payment stages), recruitment surfaces (application pages, invitations, applicant review), creator portals, draft-review approval loops with external stakeholder links, automated content collection, contracts and terms acceptance, tracking links and promo codes, message automation, gifting coordination, reporting (EMV/ROI), paid amplification, and team/agency governance. The market realization is overwhelmingly as the execution core of broader influencer-marketing platforms — the sharpest taxonomy question of this pass, recorded for joint review with the sibling Influencer Marketing Platform leaf. Boundaries hold against the Brand-Creator Marketplace (two-sided venue vs brand-side execution), Affiliate Management (commission-per-conversion vs campaign/content object), UGC Creator Marketplace (ad-asset deliverables), Social Media Management (brand's own content), generic Marketing Campaign Management (no creator-participation semantics), and Creator CRM (relationship records vs bounded campaign execution).
