# Research Notes — Proposal Management

Research date: 2026-09-06
Leaf: Proposal Management (DIRECTORY.md §07 Sales, Customer & Revenue)
Slug: proposal-management

---

## Research Goal

Understand what a Proposal Management application is as a Type: what a "proposal" is as a managed object, what the proposal lifecycle looks like, how content is created/governed/reused, how proposals are delivered and tracked, how acceptance is captured, and where the Type's boundary sits against CPQ, Sales Document Automation, Deal Desk, CLM, Sales Engagement, and buyer-side solicitation tools.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: seller-side software for creating, governing, sending, tracking, and closing sales proposals — offer documents sent to prospective buyers during a deal.
- Nearest neighbors: Configure Price Quote / CPQ (price computation), Sales Document Automation (generic document generation), Deal Desk / Commercial Approval Platform (commercial-term governance), Contract Lifecycle Management (post-acceptance contracting), Sales Engagement Platform (outreach cadences), E-sourcing / Construction Bidding (buyer-side solicitation), Opportunity/Pipeline Management (the deal record the proposal attaches to).
- Known ambiguity going in: "proposal management" also names the RFP-response discipline (responding to buyer solicitations — RFP/RFI/DDQ/security questionnaires), served by a distinct product family (RFPIO/Responsive, Loopio, Qvidian). The directory leaf sits in the sales section, so the sales-proposal pole is expected to be the center; the RFP-response pole must be examined and its status decided.

## Research Questions

1. What is a proposal as an object in these products — structure, sections, pricing, recipients, validity?
2. What is the proposal lifecycle (draft → internal review/approval → send → engagement → negotiation → decision)?
3. How is content created and reused (templates, content libraries, branding, merge fields, locking)?
4. How is pricing included (static tables, interactive tables, CPQ/catalog sync, CRM pull)?
5. How are proposals delivered, and what engagement tracking exists (opens, views, time per section, stakeholder identification)?
6. How is acceptance captured (e-signature, click-accept, payment)?
7. How do products integrate with CRM/sales stack (data pull, status sync, in-CRM operation)?
8. What internal collaboration/governance exists (roles, approvals, comments, workspaces, collaborator seats)?
9. What is the RFP-response pole, how does its machinery differ, and does it fit the same defining core?
10. Where are the boundaries vs CPQ, Sales Document Automation, Deal Desk, CLM, Sales Engagement, and buyer-side solicitation tools?

## Representative Products

Selected for market representativeness, documentation quality, distinct product philosophies, and customer-tier spread:

| Product | Pole / philosophy | Tier | Evidence level reached |
|---|---|---|---|
| PandaDoc | document-automation platform with proposals as flagship use case; e-sign + payments + API | SMB→enterprise | Tier-1 help-center index + Tier-2 product/use-case pages |
| Proposify | dedicated proposal software; design/template governance for sales+marketing teams | SMB/mid-market | Tier-2 product page + detailed plan matrix (KB unreachable) |
| Qwilr | web-native interactive proposals (proposal as web page, not PDF) | mid-market | Tier-2 product pages |
| GetAccept | digital-sales-room-centered deal execution (proposal inside a shared buyer space) | SMB→enterprise | Tier-2 product pages + detailed FAQ |
| Loopio | RFP-response management pole (enterprise response teams, content library + SME collaboration) | enterprise | Tier-2 product page + FAQ |

Rejected/adjusted during sampling:
- Responsive (formerly RFPIO) — primary RFP-pole candidate; site returned HTTP 403 ×1 → abandoned per network rules; Loopio substituted (Loopio's own comparison page confirms Responsive as its category peer).
- Proposify knowledge base (support.proposify.com) — timeout ×1 + transport error ×1 → abandoned; Proposify evidence rests on product page + pricing matrix.

## Sources

All fetched 2026-09-06.

- PandaDoc — https://www.pandadoc.com/ (product page); https://www.pandadoc.com/proposal-software/ (use-case page, incl. "What is proposal software?" definition, 3-step workflow, feature detail, FAQ); https://support.pandadoc.com/hc/en-us (help-center index: collections for Building templates / Creating documents / Sending & signing / Forms)
- Proposify — https://www.proposify.com/ (product page incl. plan matrix: templates, content library, interactive quoting, notifications & metrics, roles & permissions, approval workflows, workspaces, collaborator seats)
- Qwilr — https://qwilr.com/ (product page: editor, automation, quotes, analytics, QwilrPay, e-sign, Smart Proposal Engine, templates, use cases incl. digital sales rooms / mutual action plans)
- GetAccept — https://www.getaccept.com/ (product page); https://www.getaccept.com/product/proposal-software (proposal product page incl. FAQ defining proposal software, tracking detail, CPQ, approval roles, CRM send)
- Loopio — https://www.loopio.com/ (product page + FAQ: RFP/SQ/DDQ response management, content library, SME collaboration, milestones, analytics)

Evidence-layer legend used below:
- **A** = directly observed on an official page of a specific product
- **B** = cross-product commonality (observed across multiple sampled products)
- **C** = canonical inference (abstraction from comparison + boundary reasoning)

## Product Observations

### PandaDoc (A)

- Self-definition (proposal-software page): "an all-in-one solution that helps users create professional, customizable sales proposals… pre-built, fully customizable templates using text, multimedia, and specialized modules like e-signature blocks and pricing modules… Combined with approval workflows, a built-in content library, and secure document storage, sales teams can automate follow-ups, expedite sign-offs, and close deals."
- Documented 3-step workflow: (1) select a proposal template (or build from scratch); (2) add content, pricing, customer data, branding; (3) send to decision-makers and stakeholders — track views/engagement in real time, collect legally binding e-signatures in a single workflow.
- Templates: reusable; finished documents can be saved back as templates; content blocks, saved sections, branding controls; content library holds pre-approved content that can be **locked** — reps get "limited editorial access, ensuring that approved content is protected."
- Pricing tables: interactive — reps update/adjust quantities on the fly before sending, totals update instantly; with permissions, customers can select packages/quantities themselves.
- Approval workflow: "internal sign-offs before document delivery"; help center has an "Approval workflow" article under Building templates; "pre-send checks" article under Sending & signing.
- Tracking & analytics: notifications when documents are opened, viewed, or signed; analytics show where viewers spend time.
- e-signature: built into every plan; roles, recipients, signing order, switching signers (help-center article); audit trail; identity verification and QES as higher-end options (FAQ).
- Payments: payment gateways (Stripe, Square, PayPal, Authorize.net, QuickBooks) embedded in documents.
- CRM: native 2-way integrations with HubSpot, Salesforce, Pipedrive; "pull data from integration — CRM workflow step" is a documented help-center article; auto-fill proposal data from CRM.
- Adjacent surfaces: CPQ module, Deal Rooms ("collaborate and close deals in one personalized deal room"), Smart content (rules-based document adaptation), Workspaces, Forms with conditional logic, API/embedded editing, notary.
- Roles: sales & RevOps (create/send/track), marketing (brand consistency, locked pre-approved content), operations (workflow automation), customer success (post-sale docs).

### Proposify (A)

- Positioning: "proposal management platform"; "create, track, and sign winning proposals"; use cases: proposals, quotes, eSignatures, contracts.
- Templates: unlimited on all plans; content library — "create and share templates, sections, and images that can be pulled into documents."
- Editor: drag-and-drop; embed images/videos; custom domain so prospects see proposals.yourdomain.com.
- Interactive quoting: "allow prospects to alter the quantity or optional add-ons"; client input forms capture information from prospects inside documents.
- e-signatures on all plans; PDF export matching the digital version.
- Visibility: notifications & metrics — "get notified by email and see when prospects are viewing your document"; "detailed analytics on the time spent on each section"; reports (exportable table of all documents with filtering).
- Governance: custom fields & variables; roles & permissions ("lock down what users can and can't do by role"); approval workflows — "create conditions that if met will trigger an approval from a manager (by deal size and discount size)"; lock down proposal elements so reps can't edit them; CRM data pull to eliminate typos.
- Workspaces: "completely separate instances that admins can manage" for multi-unit businesses (franchises).
- Collaborator seats: users with access only to specific proposals, "can edit or approve, but not create or send."
- Integrations: HubSpot, Salesforce, Zoho, Pipedrive, Zapier, Stripe; Salesforce managed package with optional SSO ("reps work right within Salesforce").
- AI proposal generator exists as a marketing surface.

### Qwilr (A)

- Positioning: "Send interactive proposals, generate quotes, secure sign-off and payment"; "turns proposals into interactive buying experiences."
- Editor: drag-and-drop online editor; proposals are web pages (vs PDF — explicit "Qwilr vs. PDF" comparison page).
- Automation: "automate proposal generation and reduce manual CRM tasks"; Smart Proposal Engine — "generate personalized proposals, built with your rules, in minutes."
- Quotes: interactive quotes tailored per buyer.
- Analytics & notifications: track buyer interactions, real-time notifications when they engage; customer quote documents "track page views on live proposals"; revisit alerts ("someone revisiting a Qwilr page weeks later… signal to re-engage").
- Live link: "make changes on the fly and not have to resend a bunch of documents" — the sent proposal is a live surface, not a frozen file.
- Acceptance: e-sign & agreements (legally-binding e-signatures); QwilrPay — collect payments within proposals/quotes.
- Security surface: password protection of proposals.
- Templates: gallery across sales/marketing/CS; use cases extend to digital sales rooms, mutual action plans, customer onboarding.
- Integrations: HubSpot, Salesforce, Zoho, Pipedrive, QuickBooks, Stripe, Slack, Dynamics, Zapier; API.

### GetAccept (A)

- Positioning: "AI-Powered Digital Sales Rooms & Proposal Software"; the digital sales room is the center — "one shared room. Everyone on the same page… centralized hub… every stakeholder access to the latest content… never lose track of timelines, updates, or context."
- Proposals & quotes: "branded documents in seconds"; editor in all plans (mobile-responsive blocks); can also upload existing Word/PDF documents instead of using the editor.
- Personalization: video introductions, live chat conversation starters, video blocks (e.g., explaining the pricing table).
- Tracking: "map new stakeholders, understand opens and unique views all the way through to how much time a prospect has spent on each individual page"; FAQ adds: who viewed, how long per page, who they shared it with, stakeholder mapping, drop-off analysis.
- Pricing: CPQ module "ensures all reps have up-to-date and accurate pricing information, which can be automatically added to proposals."
- Governance: "approval roles… the right team members review and sign off on documents… faster transition to the contract stage."
- CRM: send proposals directly from the CRM; auto-populate CRM data into templates; integrations with Salesforce, HubSpot, Pipedrive, Dynamics, SuperOffice; 500+ automations; API.
- Adjacent: e-signatures (AdES/QES), contract management, mutual action plans, sales content management, sales engagement, notifications & reminders, AI (meeting summaries → content, business case builder, AI editor).
- Self-definition (FAQ): "Proposal software simplifies the creation, delivery, and tracking of sales proposals… build branded, interactive proposals using templates, track who's actually reading them through analytics, and manage everything from proposal to signed contract in one place."

### Loopio (A) — RFP-response pole

- Positioning: "AI RFP Software… Power your entire process, from RFPs to DDQs and security questionnaires"; also lists "Sales Proposals" as a use case.
- Object model: response **projects** — "import questions, organize them, and auto-fill accurate answers"; project milestones and proposal readiness at-a-glance.
- Content: centralized content library ("magic library") with content connectors into SharePoint, Google Drive, websites; automated review cycles prompt SMEs to update answers before they become outdated.
- Collaboration: smart assignments (assign questions/sections to SMEs), automated nudges, @mentions/comments, SMEs can answer inside Slack/Teams; review cycles.
- Analytics: response intelligence — win rates, readiness, project progress; "evaluate each proposal with AI-driven insights."
- Users: proposal & bid managers, sales teams, pre-sales, IT/InfoSec, investor relations, marketing.
- No buyer-facing engagement tracking, no embedded e-sign, no pricing tables in the observed material — the buyer interaction is the solicitation + submission, not a tracked web document.
- FAQ explicitly frames the category: "respond to RFPs, RFIs, DDQs, and security questionnaires… complete a first draft in minutes, collaborate efficiently, and ensure consistency across their RFP responses."

## Cross-product Comparison

| Capability | PandaDoc | Proposify | Qwilr | GetAccept | Loopio |
|---|---|---|---|---|---|
| Proposal as managed, persistent object | ✓ | ✓ | ✓ | ✓ | ✓ (response project) |
| In-app authoring/assembly | ✓ editor | ✓ editor | ✓ editor | ✓ editor (+ file upload) | ✓ question/answer assembly |
| Reusable templates | ✓ | ✓ unlimited | ✓ gallery | ✓ library | ✓ (response templates) |
| Shared content library / blocks | ✓ | ✓ | implied | ✓ (sales content mgmt) | ✓ (core of product) |
| Branding controls / locked content | ✓ | ✓ | ✓ (brand consistency claim) | ✓ | ✓ (brand voice) |
| Internal approval before send | ✓ | ✓ (deal-size/discount triggers) | ✓ (streamline approvals) | ✓ (approval roles) | ✓ (review cycles) |
| Delivery as link/web page | ✓ | ✓ (custom domain) | ✓ (live link) | ✓ (sales room) | submission-based |
| PDF export / file upload path | ✓ | ✓ | vs-PDF positioning | ✓ (upload Word/PDF) | document export |
| Engagement tracking (opens/views/time per section) | ✓ | ✓ | ✓ | ✓ (stakeholder mapping, drop-off) | ✗ (internal readiness instead) |
| Open/view notifications | ✓ | ✓ | ✓ (real-time) | ✓ | ✗ |
| Embedded e-signature | ✓ | ✓ | ✓ | ✓ (AdES/QES) | ✗ |
| Interactive pricing tables / quoting | ✓ | ✓ | ✓ | ✓ (CPQ-fed) | ✗ (RFQ content only) |
| Buyer-side editing (quantities/packages) | ✓ (permissions) | ✓ | ✓ | implied via CPQ | ✗ |
| Payment collection at acceptance | ✓ | (Stripe integration) | ✓ QwilrPay | (Chargebee integration) | ✗ |
| CRM integration (pull data / sync status) | ✓ 2-way | ✓ | ✓ | ✓ (send from CRM) | ✓ (content/CRM) |
| Deal room / shared buyer space | ✓ (Rooms) | ✗ | use case | ✓ (core) | ✗ |
| Mutual action plans | ✗ | ✗ | use case | ✓ | ✗ |
| AI drafting/generation | ✓ (smart content) | ✓ (generator) | ✓ (AI creator, Smart Proposal Engine) | ✓ (AI agents) | ✓ (response AI) |
| RFP/SQ/DDQ question import + SME assignment | ✗ | ✗ | ✗ | ✗ | ✓ (core) |

Reading of the table:
- The sales-proposal pole (PandaDoc, Proposify, Qwilr, GetAccept) is highly uniform: proposal object + assembly + governance + delivery + tracking + e-sign + CRM.
- Loopio shares the object/assembly/delivery/decision skeleton but replaces buyer-facing tracking and e-sign with internal response machinery (question import, SME assignment, review cycles, readiness). Same defining core, different center of gravity.

## Abstraction Levels

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **Proposal as a persistent managed record** — a distinct offer document object, addressed from the selling organization to a specific prospective buyer (typically bound to a deal/opportunity), held in the application's repository with an identity and status.
2. **Seller-side authoring/assembly inside the application** — the proposal is composed in (or ingested into) the application from reusable structure and deal data.
3. **Controlled delivery to the buyer** — the seller sends/publishes the proposal to the buyer as a presentation surface (document or web page/link) under the application's delivery mechanism.
4. **Lifecycle to a recorded decision** — the proposal advances through statuses (draft → sent → engaged → accepted/declined) and its outcome is recorded, closing the loop with the sales process.

Remove any one: without (1) it is a document editor; without (2) it is file storage; without (3) it is an internal drafting tool; without (4) it is document delivery, not proposal management.

### L1 — Common Mature Structure

Present across the sampled sales-pole products; expected in the market but not definitional:

- template library + shared content library (sections/blocks/images) with branding controls
- merge fields / variables populated from CRM or deal data
- internal review/approval gates before delivery (condition-triggered in some products)
- role/permission model incl. content locking (reps cannot alter approved content)
- delivery as a trackable web link (plus PDF export path)
- engagement tracking: opens, views, time per section/page, notifications
- embedded e-signature for acceptance (roles, signing order)
- interactive pricing tables / quote blocks (rep-adjustable; sometimes buyer-adjustable)
- CRM integration: data pull at creation, status sync at decision
- document repository with search/reporting over sent proposals

### L2 — Variant / Optional Structure

Depends on segment, philosophy, or deal shape:

- proposal form factor: paginated document vs web page vs shared deal room
- payment collection at acceptance (some products)
- buyer-side interactivity: quantity/package selection, client input forms, live chat, video blocks
- password protection / access control on the buyer-facing surface
- deal-room evolution: mutual action plans, stakeholder workspaces, meeting-recap content
- RFP-response machinery: solicitation question import, SME assignment, answer review cycles, response readiness analytics (the Loopio/Responsive pole)
- AI drafting/generation depth (from smart content to full auto-generation)
- multi-entity workspaces (franchise/multi-unit instances)
- industry template packs (agencies, construction, janitorial, consulting…)
- compliance posture: QES/AdES signature levels, HIPAA, eIDAS, SOC 2

### L3 — Vendor-specific Structure

(Research Notes only — not for the final document)

- PandaDoc: Deal Rooms, Smart content rules, Notary, embedded editing API, "pre-send checks," 2FA article, template workflow builder, QES/ID-verification upsell framing vs DocuSign/Proposify
- Proposify: collaborator-seat model (edit/approve but not create/send), Aspire integration, professional template design services, "State of Proposals" data report, custom domain mapping
- Qwilr: QwilrPay, Smart Proposal Engine, website-URL→proposal AI creator, "Qwilr vs. PDF" positioning
- GetAccept: digital sales room as product center, AdES/QES emphasis, meeting-transcript→content AI, Chargebee/HubSpot automation chains, stakeholder mapping/drop-off analytics vocabulary
- Loopio: "Response Intelligence," content connectors (Glean, 275+ sources claim), smart assignments/automated nudges vocabulary, Foundations/Enhanced/Enterprise tiers, 15–30 day implementation claim
- Vendor marketing figures (e.g., "17 minutes average creation," "43% won within 24 hours," "44% higher win rates," "415% ROI") are vendor claims — recorded here, not asserted in the final document.

## Vendor-specific Findings

See L3 above. The most consequential: GetAccept and PandaDoc both extend past the proposal into a shared buyer-facing workspace (digital sales room / deal room) — a drift toward a deal-execution surface that still contains the proposal core. Loopio/Responsive extend past the single proposal into a response-program platform (library + program analytics) — a drift toward knowledge/response operations.

## Boundary Findings

- **vs Configure Price Quote / CPQ (§07)**: CPQ's center is computing the priced configuration (rules, catalogs, price execution); proposal management's center is packaging the offer as a buyer-facing decision document. Overlap is real and bidirectional: proposal pricing tables can be CPQ-fed (GetAccept documents this), and CPQ outputs are often rendered inside proposals (PandaDoc sells both). Removal test: remove narrative/persuasion + buyer decision surface → CPQ; remove configuration/price computation → proposal management.
- **vs Sales Document Automation (§07)**: document automation centers template-driven production of many document types (contracts, NDAs, invoices, onboarding packs); proposal management centers the proposal-to-decision loop. PandaDoc legitimately straddles (self-describes as both); the proposal loop is the distinguishing center. Removal test: remove the deal-bound decision lifecycle → document automation.
- **vs Deal Desk / Commercial Approval Platform (§07)**: deal desk governs non-standard commercial terms against policy before quoting; proposal approvals are document-level gates inside the proposal workflow. Different object (commercial exception vs document).
- **vs Contract Lifecycle Management (§11)**: CLM begins at/near contracting (negotiation of the executed agreement, obligations, renewals); proposal management ends at acceptance/signature and hands off. Shared surface: e-signature. GetAccept's contract-management module is the visible seam.
- **vs Sales Engagement / Outreach Sequencing (§07)**: engagement platforms run multi-touch prospecting cadences; the proposal is a deal-stage artifact produced for an active opportunity, not a sequence step. Some engagement suites embed proposal-like sends — capability overlap, not Type identity.
- **vs Opportunity / Pipeline Management (§07)**: the CRM deal is the container; the proposal is one artifact within it. Proposal tools sync status back to the deal but do not own pipeline stages/forecasting.
- **vs buyer-side solicitation tools (E-sourcing §10, Construction Bidding §17, Government Procurement §24)**: those own the buyer's solicitation and bid collection; this Type owns the seller's response/offer. The RFP-response pole of proposal software is the seller-side mirror of e-sourcing.
- **vs Presentation Application (§03.04)**: decks present; proposals offer terms and capture a decision (pricing, acceptance). Form-factor similarity only.
- **RFP-response pole status**: Loopio/Responsive-class products fit the L0 core (offer record → assembly → submission → decision) but their center of gravity is response-program operations (library, SME workflow, readiness), not the buyer-facing proposal document. Flagged for joint review: they could justify a separate "RFP Response Management" leaf; under the current directory they are documented here as the solicited-response variant.

## Uncertainties

- Proposify's operational depth (help-center level) unverified — KB unreachable; its plan matrix is detailed but marketing-adjacent. Claims about Proposify kept at product-page strength.
- Responsive (RFPIO) not observed at all (403) — the RFP pole rests on Loopio alone plus Loopio's own category framing; pole characteristics (question import, SME assignment) are asserted as variant machinery with single-product evidence, marked accordingly.
- Help-center article-level behavior (exact state names, default settings, numeric limits) not fetched for any product — no precise operational parameters asserted anywhere in the final document.
- Whether buyer-side editing of pricing (quantity/package selection) is common or exceptional across the market: observed in PandaDoc/Proposify explicitly; treated as "some products" strength.
- The exact relationship between "quote" and "proposal" objects inside sampled products (separate object types vs document variants) was not verifiable at help-center depth; treated conceptually.

## Final Synthesis

A Proposal Management application is the seller-side system of record for the offer document in a deal: it holds each proposal as a persistent record bound to a prospective buyer, assembles it in-application from reusable content and deal data, governs it through internal review, delivers it to the buyer as a controlled presentation surface, observes the buyer's engagement, and carries it to a recorded decision (typically e-signed acceptance), with status synchronized back to the CRM deal.

The defining core is deliberately small (record + assembly + delivery + decision lifecycle). Everything else — templates, content libraries, engagement analytics, e-signature, pricing tables, approvals, CRM sync — is common mature structure that makes the Type commercially useful but does not define it. Two poles share the core: the seller-initiated sales proposal (the directory's center of gravity, §07) and the solicited RFP/bid response (enterprise response teams), which differs in trigger and machinery rather than in defining structure. Form-factor variants (paginated document, web page, shared deal room) are implementation philosophies, not separate Types.
