# Research Notes — Deal Desk / Commercial Approval Platform

Directory leaf: §07 Sales, Customer & Revenue — "Deal Desk / Commercial Approval Platform"
Slug: `deal-desk-commercial-approval-platform`
Research date: 2026-09-08

## Research Goal

Understand what a **Deal Desk / Commercial Approval Platform** actually is as a class of software: who runs it, what objects exist inside it, how a non-standard deal moves through review to authorization, which rules govern it, and where the Type ends relative to CPQ (quote-time engine with embedded approval gates), Sales Pricing Application (standing price governance), Approval Workflow Platform (§10 generic routing), Opportunity Management / CRM (pipeline container), CLM (contract lifecycle), and the buyer-side "deal desk" used in procurement (Vendr/Tropic class).

This pass also **discharges two sibling flags from this side**:

1. The CPQ pass flag: *"CPQ embeds approval gates on discounts/terms; the Deal Desk leaf should own policy-making and the cross-functional approval process"* (research/configure-price-quote-cpq.md §Boundary Findings).
2. The Sales Pricing pass flag: *"vs Deal Desk (price-change/deviation approval here vs cross-functional commitment approval there — unprocessed sibling flag stands)"* (research/sales-pricing-application.md §Boundary Findings).

## Initial Boundary

Working hypothesis before research:

- Core use: a cross-functional function inside a selling organization (sales ops/RevOps, finance, legal, sometimes product) that reviews and authorizes **non-standard commercial deals** — deals whose price, terms, structure, or clauses depart from the organization's standing commercial policy.
- Users: deal desk managers/analysts (operators), sellers (requesters), finance/legal/sales leadership (reviewers/approvers), RevOps admins (policy configuration).
- Nearest neighbors: CPQ (embeds discount-approval gates; ends at the accepted quote), Sales Pricing (approves price changes/deviations, not whole deals), Approval Workflow Platform (generic request→routing→decision), CRM/Opportunity Management (holds the deal pipeline), CLM (contract lifecycle), buyer-side procurement "deal desk" (Vendr/Tropic — different operator).
- Unknowns going in: (a) does standalone "deal desk software" exist as a category, or is it only a capability of CPQ/CRM suites? (b) is "deal desk" the same thing on the buy side? (c) is the approval machinery definitional or just the generic approval skeleton applied to deals? (d) terminology hazard: "DealRoom"/"deal room" means something else in market usage.

## Research Questions

1. What is the central object — the deal? the exception request? the approval? the policy?
2. What triggers deal desk involvement (thresholds, complexity, value, non-standard terms)?
3. What does the approval structure look like (matrix, guardrails, sequential/parallel chains, approver groups, delegation)?
4. What do the cross-functional reviewers actually do, and what is recorded?
5. What happens after authorization (handoff to quote/contract/order; automatic quote updates)?
6. How is the desk itself measured (approval cycle time, win rate, deal size, margin)?
7. Is the Type standalone software, a suite capability, or a function without dedicated software?
8. Where is the buyer-side "deal desk," and is it the same Type?
9. Historical check: does the definition hold for pre-software deal review practice (committees, authority levels, deal logs)?

## Representative Products

Selected for market representativeness, documentation reachability, distinct product philosophies, and distinct customer tiers — plus two buyer-side boundary products:

| Product | Philosophy / pole | Evidence tier |
|---|---|---|
| **DealHub** (dealhub.io) | Quote-to-revenue suite (CPQ+CLM+DealRoom+billing) with deal desk as a named capability: Deal Desk Dashboard, automated approval workflows, pricing guardrails; deal desk customers at Intuit/Braze | Tier-2 product pages + glossary (root, /platform/cpq/, glossary/dealroom); deep docs login-gated |
| **Subskribe** (subskribe.com; acquired by DealHub) | Modern SaaS CPQ with **DealDesk AI** and a dedicated Approval Workflows capability: pre-established approval matrix, parallel approvals, approver groups, org-structure routing | Tier-2 product pages (/, /product/dealdesk-ai, /product/approval-workflows) |
| **RevOps** (revops.io; acquired by Maxio) | Self-described **"modern Deal Desk platform"** — the clearest standalone pole: approvals engine, guardrails, deviation-based approvals, legal exception review, centralized agreement repository | Tier-2 product pages + glossary (/, /approvals/overview, /glossary/deal-desk) |
| **HubSpot** (blog.hubspot.com/sales/deal-desk) | Function-definition + CRM-embedded software framing (deal desk as team/process; software = CRM deal tracking + automation recipes) | Tier-3 vendor educational article (Layer A quotes, marketing-adjacent — used with calibration) |
| **Vendr** (vendr.com; part of Vertice) | **Buyer-side boundary product**: AI pricing/negotiation agents for software procurement | Tier-2 homepage |
| **Tropic** (tropicapp.io) | **Buyer-side boundary product**: procurement intelligence + agentic execution (renewal/proposal agents, intake & orchestration) | Tier-2 homepage |

Unreachable (dropped per network rules after 1–2 failures): Salesforce (salesforce.com deal-desk URLs 404 ×2), Conga (403), DealHub deep product page (/product/dealroom 403) and knowledge base (docs.dealhub.io — JS/cookie login wall). The enterprise-suite pole (Salesforce/Conga/SAP/Oracle) is therefore covered only **structurally** (via Subskribe/DealHub positioning against Salesforce CPQ, and HubSpot's framing); no claims are made about specific suite internals.

## Sources

All fetched 2026-09-08.

- DealHub: https://dealhub.io/ ; https://dealhub.io/platform/cpq/ ; https://dealhub.io/glossary/dealroom/ ; (403: /product/dealroom, blog deal-desk article; login-walled: docs.dealhub.io)
- Subskribe: https://www.subskribe.com/ ; https://www.subskribe.com/product/dealdesk-ai ; https://www.subskribe.com/product/approval-workflows
- RevOps: https://www.revops.io/ ; https://www.revops.io/approvals/overview ; https://www.revops.io/glossary/deal-desk
- HubSpot: https://blog.hubspot.com/sales/deal-desk
- Vendr: https://www.vendr.com/
- Tropic: https://www.tropicapp.io/

## Product Observations

### DealHub (sell-side CPQ suite with deal desk capability) — evidence layer A

- Suite framing: "Bring quoting, approvals, contracts, subscriptions, billing, and buyer collaboration into a single revenue workflow… powered by AI and grounded in the controls teams need to scale."
- CPQ capability list includes: **Automated Approval Workflows** ("Speed up approvals with parallel workflows, real-time collaboration, and one-click approvals for faster deal execution") and **Deal Desk Dashboard** ("Gain complete deal visibility with real-time insights into quote progress, approval status, and sales momentum").
- Margin protection: "built-in pricing guardrails, smart discounting, and structured approvals that prevent revenue leakage."
- Guardrail semantics (glossary): "sales representatives are not able to offer certain discounts without managerial approval once CPQ guardrails are put into place"; "Sales leaders can let reps offer discounts up to a certain threshold without needing permissions."
- Approval→quote automation (glossary, discount approval workflows): "When a sales leader approves a discount, the sales rep does not need to update the quote… it is updated automatically."
- Named-function evidence: customer quotes from "Head of Deal Desk" (Intuit) — "Now sellers can see within their DealRoom exactly where approvals sit, improving SLAs and reducing friction" — and "VP, Global Deal Desk at Braze." Case-study stats: "Approval Cycles Cut from Days → 8hr", "Faster Approvals (<4h vs Days)", "70% Reduction in admin overhead on pricing & approvals", "90% Quote Accuracy. No DealDesk Needed."
- **Terminology hazard confirmed**: DealHub's "DealRoom" is a *digital sales room* (buyer-facing microsite with quote, contract, eSign, mutual action plans) — explicitly NOT the deal desk. The glossary positions Deal Desk teams as *users* of DealRoom: "DealRoom helps Deal Desk professionals ensure pricing, contract terms, and approvals are handled efficiently and accurately, without the usual email threads and document chaos."
- Operational docs (docs.dealhub.io) login-gated — internal approval-condition model not evidenced.

### Subskribe (sell-side CPQ, DealDesk AI + approval matrix) — evidence layer A

- "DealDesk AI: The Intelligent Deal Assistant… freeing your deal desk team from repetitive manual tasks so they can focus on strategic deal optimization." Customer quote (Director of Sales Ops): "approval processes flowing naturally — ultimately freeing up our deal desk team to focus on strategic initiatives instead of administrative tasks."
- Approval Workflows capability:
  - "Create approval workflows in minutes — use natural language to easily set up (and update) workflows."
  - "Enable parallel approvals driven by business logic — create dynamic approval rules, organize approver groups, and assign decision-makers."
  - **"Instant approvals: Build deals within your pre-established approval matrix for automatic approval – validated by deal desk and finance."**
  - "Keep approvals moving automatically — import your org structure so your CPQ knows who to send notifications to automatically. Preview for advance notice. And approvers can approve with a click."
  - "Never lose track of approvals — track every approval's status in real time. Ensure proper sign-off with complete visibility into the approval process."
- AI summarization aimed at approvers: "AI-generated summaries that make approval decisions quick and confident"; "critical deal terms automatically highlighted."
- Conversational assistant covers "product details, pricing policies, and approval processes."
- Seller-side quote (Enterprise AE): "It helps me build quotes, seek approvals from the right people, and easily ensure that order forms are accurate."

### RevOps (self-described "modern Deal Desk platform") — evidence layer A

- Identity: "DEAL DESK, APPROVALS, AND CPQ PLATFORM — Configure, Collaborate, Price, Quote, and Sign." "RevOps is the modern Deal Desk platform with a simple mission: enable businesses to build a scalable Deal Desk operation that helps their sales organizations close more deals faster, unify branding, reduce contract errors, and provide a centralized agreement repository."
- Approvals page: "multiple approval workflows within each agreement"; "sequential approvals"; "smart reassignment features — out of office / vacation reassignment, team-based approvers"; "re-usable agreement language to reduce legal escalations"; "scan for clauses using AI on any attachment"; "route approval discussions based on types of exhibits to any department"; "scalable and flexible approval rules engine. From no-code to yo-code."
- Workflows: "Admins can automate processes, **define deviations that will require approval**, and allow specific users to approve the changes."
- Guardrails: "you control what fields your team can edit on each template and deal."
- Collaboration: "Mention team members to receive clarification and assign manual approvals."
- Legal pole: "Reduce redlines with pre-approved terms and conditions. Quickly review reasoning for exceptions on NDAs, MSAs, and Order Form agreements. Scale approvals with delegating ownership of approval topics."
- Finance pole: "Built-in validation for all your commercial terms including dates, schedules, and entitlements"; ARR; ASC-606 data in CRM.
- Role spread on homepage: Sales, Finance, Operations, Legal, Customer Success — "Your entire company benefits."
- Release notes carry a "Deal Desk" category (Improved Search, Deal Expiration UI, Quantity Drawer, Dates Drawer) — the deal/agreement record is the product's working object.
- Glossary "Deal Desk": "A Deal Desk is a team that helps manage complex sales deals… a place where all relevant stakeholders – sales, finance, product, legal, success, and others – can discuss and work through deals, **usually non-standard ones**." Speed-up guidance: standardize processes/templates; implement deal desk software; clear roles; **"Set guidelines and approval thresholds: for discounts, customizations, and other deal-specific aspects"**; monitor "KPIs like deal cycle time, average deal size, and approval time." Industries: enterprise software, professional services, telecom, financial services, manufacturing.

### HubSpot (function definition + CRM-embedded framing) — evidence layer A (vendor educational; marketing-adjacent, used with calibration)

- Definition: "A deal desk is a centralized location (or team) that consolidates information about complex and high-value deals to ensure they go smoothly from end-to-end. Deal desks require representation from multiple departments… sales, product, legal, and finance."
- Scope triggers: "power users, atypical contracts, atypical use cases, detailed product/feature descriptions, pricing structures."
- Setup discipline: determine the desk's role; decide who staffs it; **define which deals it covers** ("how large, complex, or valuable a deal needs to be to warrant the team's attention"; where in the cycle the desk engages); create a process flow (workflows, documents, templates to standardize deals); analyze success.
- Metrics: profit, win rate, deal size, deal quality (margin, cost of deal terms, sales cycle time, contract length, profitability).
- Software framing: HubSpot deal tracking (CRM deals object), Workato "sales deal desk" recipe (Slack+Salesforce approval workflows, notifications, automated reporting — observed via HubSpot's article only, secondary), RevOps (guardrails, approval workflows; "quote → deal desk → deal room → sign").

### Vendr (buyer-side boundary product) — evidence layer A

- "AI PRICING AND NEGOTIATION AGENTS… part of Vertice." Pricing benchmarks "built on billions of dollars of real software spend"; negotiation insights "which terms move, which don't"; contract reviews; autonomous negotiations with human oversight. "Designed for your team — whether you have a procurement team or not." Renewals routed "from your procurement workflow." Entirely buyer-side; no sell-side deal desk semantics.

### Tropic (buyer-side boundary product) — evidence layer A

- "Procurement Software… intelligence and expertise procurement and finance teams need to prioritize savings opportunities, negotiate better, and optimize their tech spend." Agentic execution: Renewal Agent, Proposal Agent, **Intake & Orchestration** (procurement workflows). "Buyer-only model." FAQ: "Most procurement solutions focus on process — managing intake, approvals, and purchase orders." Confirms the buyer-side population's operator (procurement/finance), objects (purchases, renewals, supplier negotiations), and family (procurement).

## Cross-product Comparison

| Dimension | DealHub | Subskribe | RevOps | HubSpot framing | Vendr / Tropic (buyer side) |
|---|---|---|---|---|---|
| "Deal desk" is… | CPQ capability (dashboard + approval workflows) + named customer function | CPQ capability (DealDesk AI + approval matrix) + named function | The product's whole identity ("Deal Desk platform") | A team/process; software = CRM tracking + automation | Not used — procurement territory |
| Central object | Quote + approval status | Quote/deal + approval matrix | Agreement/deal + approval workflows | Deal record in CRM | Purchase/renewal request |
| Policy layer | Pricing guardrails; discount thresholds | Pre-established approval matrix (auto-approve within) | Guardrails (field editability); "deviations that require approval" | Coverage criteria (size/complexity/value) | n/a |
| Approval machinery | Parallel workflows, one-click approvals, status visible to sellers, SLAs | Parallel approvals, approver groups, org-structure routing, real-time status, previews | Sequential/parallel workflows, reassignment (OOO), team-based approvers, topic delegation | Approval workflows via automation platform | n/a |
| Cross-functional set | Deal desk head, sales ops, finance | Deal desk, finance | Sales, finance, ops, legal, CS | Sales, product, legal, finance | Procurement, finance |
| Non-standard trigger | Discounts beyond guardrails | Deals outside the matrix | Deviations from defaults; term exceptions | Atypical contracts/use cases; high value | n/a |
| After authorization | Quote updates automatically; DealRoom/eSign | Order form → signature | Agreement → signature → CRM sync | Deal proceeds in pipeline | n/a |
| Desk metrics | Approval cycle time, SLAs | Approval progress tracking | Deal cycle time, approval time, deal size | Profit, win rate, deal size, deal quality | Savings (different Type) |
| Packaging | Suite module | Suite module | Standalone platform | CRM + automation recipes | Standalone (procurement family) |

**Stable cross-product commonalities (Layer B):**
1. The desk exists for **non-standard deals** — exceptions to standing commercial terms (all sell-side sources).
2. A **policy layer** separates auto-proceed from review-worthy: guardrails/thresholds (DealHub), approval matrix (Subskribe), deviation definitions + guardrails (RevOps), coverage criteria (HubSpot).
3. **Cross-functional reviewer set** drawn from more than one function (all sell-side sources).
4. **Recorded, attributable decisions** with retained status/history and real-time visibility (all sell-side sources).
5. **Automatic propagation of approved terms** into the quote/agreement (DealHub, RevOps; implied by Subskribe's order-form flow).
6. **Cycle-time pressure** as the desk's core operational metric (all sell-side sources).
7. CRM integration as the deal's source context (all sell-side sources).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Deal Desk / Commercial Approval Platform:

1. **The deal exception of record** — a specific pending commercial commitment (quote, agreement, proposed terms) held as a persistent, reviewable record *because* it departs from the organization's standard commercial terms.
   - Remove → the records live only in CPQ/CRM as ordinary quotes/deals; nothing for a desk to review.
2. **The operationalized commercial policy** — the organization's standing rules for commercial terms (discount/price thresholds, pre-approved clauses and terms, coverage criteria by size/complexity) encoded so the system can distinguish in-policy deals (proceed without review) from exceptions (route to review).
   - Remove → approvals with no policy basis = a generic approval workflow platform; or guardrails with no review loop = CPQ's embedded gates.
3. **The cross-functional decision loop with retained authorization** — exceptions route to designated reviewers drawn from more than one function (sales leadership, finance, legal, ops); reviewers record attributable decisions (approve / reject / counter, with conditions); the retained record is the authorization on which the deal proceeds to downstream commitment on the excepted terms.
   - Remove the multi-function review → a single-manager discount signoff, not a deal desk. Remove retention → a meeting, not a platform.

**Jointly-held is load-bearing:**
- 1 alone = a deal/quote record (CPQ / CRM territory).
- 2 alone = policy/guardrail configuration (CPQ rules / Sales Pricing territory).
- 3 without 1+2 = generic Approval Workflow Platform (§10).
- 1+2 without 3 = guardrails that auto-block, with no review loop.
- 2+3 without 1 = policy documentation plus generic approvals, anchored to nothing commercial.
- 1+3 without 2 = an ad-hoc deal review committee; the *platform* framing requires the policy yardstick to be operationalized in the system.

### L1 — Common Mature Structure

Present in most mature products; not definitional:

- **Deal desk dashboard / queue** — real-time visibility into quote progress, approval status, and momentum (DealHub "Deal Desk Dashboard"; Subskribe real-time tracking; RevOps release-note category).
- **Parallel and sequential approval chains**, approver groups, org-structure-based routing, previews (Subskribe, RevOps).
- **Delegation and reassignment** — out-of-office/vacation reassignment, team-based approvers (RevOps).
- **Light-touch approval participation** — one-click approvals, notifications via Slack/email (Subskribe, RevOps, DealHub).
- **Exception intake from the seller's quote** — the rep requests an exception inside the quoting flow (DealHub, Subskribe, RevOps).
- **Collaboration on the deal record** — mentions, comments, internal discussion threads (RevOps; DealHub DealTalk).
- **Automatic quote/agreement updates on approval** (DealHub glossary; RevOps sync).
- **Desk metrics** — approval cycle time, deal cycle time, deal size, win rate, margin (HubSpot, RevOps glossary, DealHub case stats).
- **CRM integration** as the deal's source context (all sell-side products).
- **AI assistance** — approver-facing summaries, clause scanning, conversational quote building (Subskribe DealDesk AI, RevOps AI clause scan, DealHub AI). Era-current; not definitional.

### L2 — Variant / Optional Structure

- **Packaging spectrum**: standalone deal-desk platform (RevOps) ↔ CPQ-embedded capability (DealHub, Subskribe) ↔ CRM + generic automation recipes (HubSpot/Workato framing). The standalone pole is thin; suite-embedded is dominant.
- **Depth poles**: approval-centric (pure review/authorization) vs agreement/terms-centric (clause libraries, legal exception review — RevOps) vs quote-building-centric (RevOps blocks, Subskribe CPQ) — each shades toward a neighbor Type but keeps the L0.
- **Contract-terms depth**: pre-approved clause libraries, redline/exception review for NDAs/MSAs/order forms (RevOps) — shades toward CLM.
- **Buyer-side namesake**: procurement "deal desk" (Vendr, Tropic) — different operator, objects, and family; recorded as a boundary, not a variant of this Type.
- **Vertical tuning**: enterprise software, professional services, telecom, financial services, manufacturing (RevOps glossary).
- **AI agents** performing or summarizing reviews (era-current).

### L3 — Vendor-specific (Research Notes only)

- DealHub: DealRoom (digital sales room), DealTalk, DealStream, DealBox, "estimator" for consumption ACV.
- Subskribe: Zeppa business rules engine; "DealDesk AI" branding; G2 badge framing.
- RevOps: building blocks (Pricing Table, Term, Signature, Deal Expiration…), "no-code to yo-code," agreement templates.
- Consolidation observations: Subskribe acquired by DealHub; RevOps acquired by Maxio; Vendr part of Vertice.
- Customer-name stats (Intuit/Braze/Zapier quotes, "8hr approval cycles", "90% quote accuracy") — vendor-published, kept out of the canonical document.

## Rejected Findings

- **"Deal desk = discount approvals"** — rejected as too narrow: sampled products authorize whole commercial commitments (terms, clauses, entitlements, structure), with price/discount as one dimension (RevOps legal/finance poles; Subskribe "critical deal terms").
- **"The approval workflow is the whole Type"** — rejected: the generic request→routing→decision skeleton is shared with §10 Approval Workflow Platform; what makes this Type is the commercial policy layer + deal anchoring + cross-functional standing desk.
- **"Deal desk software is a standalone category"** — rejected as the dominant pattern: the standalone pole exists (RevOps) but is thin; CPQ-embedded capability is the dominant packaging. Held as a packaging variant, not a definitional claim.
- **"DealRoom/deal room = deal desk"** — rejected: market usage of "deal room" is a buyer-facing sales room (DealHub DealRoom) or an M&A data room; the deal desk is the internal approval function. Terminology hazard recorded.
- **"Buyer-side deal desk is the same Type"** — rejected: Vendr/Tropic serve the buying organization (procurement/finance) with pricing benchmarks and negotiation agents; operator, objects, and flows are procurement's. Same label, different Type.
- **"AI is definitional"** — rejected: the L0 loop (exception + policy + cross-functional decision + record) is complete without AI; AI is era-current assistance.

## Boundary Findings

- **vs Configure Price Quote / CPQ** — the flagged joint review, now resolved from this side. CPQ centers on rule-governed configuration, quote-time pricing, and the stateful quote record, ending at acceptance; it *embeds* approval gates on discounts/terms as a capability. Deal Desk centers on the **cross-functional review of exceptions against standing commercial policy** — the policy center and the review process, not the offer computation. When a CPQ suite adds a deal desk dashboard, an approval matrix, guardrail policy management, and cross-functional routing, it grows a Deal Desk capability (observed: DealHub, Subskribe). The leaves remain distinct Types. Seam: the quote is CPQ's object; the desk's object is the exception review; the desk consumes the quote and authorizes its non-standard terms.
- **vs Sales Pricing Application** — the flagged cross-check, now discharged from this side. Sales Pricing owns the standing governed price population and the price-setting/release discipline; its approvals attach to **price changes and deviations**. Deal Desk owns the cross-functional approval of **whole commercial commitments** — price is one dimension among terms, clauses, entitlements, and structure. The pricing application's unit is the price record; the desk's unit is the deal. Seam confirmed; leaves stand.
- **vs Approval Workflow Platform (§10)** — shares the skeleton (submitted request → routing → attributable decision → retained history) but is domain-specific: the request is a commercial commitment, the routing basis is commercial policy (thresholds, pre-approved terms), the reviewer set is the standing cross-functional desk, and the outcome authorizes commercial terms downstream. A generic approval platform can *implement* deal approvals (Workato recipe, observed via HubSpot's article) but carries no commercial policy layer or deal anchoring. Remove the commercial anchoring → generic approval workflow platform.
- **vs Opportunity Management / CRM** — CRM holds the pipeline container and the opportunity object; the deal desk operates on **exceptions to commercial policy** for specific deals, with its own record (the review/authorization), its own roles, and a policy layer CRM does not have. CRM-embedded packaging is common (HubSpot framing) but the defining objects are not CRM's.
- **vs Contract Lifecycle Management** — overlap on contract-terms review (pre-approved clauses, exception review — RevOps). CLM's center is the contract lifecycle (authoring → negotiation → signature → obligations); the desk's center is the commercial exception decision. Clause libraries are a desk capability; the full lifecycle is CLM's.
- **vs Proposal Management** — proposal tools present the offer and capture the buyer's decision; the desk authorizes non-standard terms internally before/while the offer is made. Distinct centers.
- **vs buyer-side procurement "deal desk"** — same market label, different Type: operator is the buying organization (procurement/finance), objects are purchases/renewals/supplier negotiations, family is procurement (§10 territory: Vendr, Tropic). Flag for directory-level attention so the label does not collapse the two.
- **Terminology hazard** — "Deal Room" in market usage = buyer-facing digital sales room (DealHub DealRoom) or M&A virtual data room; NOT the deal desk. Recorded to prevent future confusion in the directory.

## Historical / Market-Sample Check

Would older, thinner, or differently positioned products still fit the L0?

- **Pre-software practice**: a pricing/deal review committee (sales VP + finance + legal) convening on non-standard deals, with a deal log of exceptions, standing discount authority levels ("rep up to X%, manager to Y%, VP above"), and signed approvals. This satisfies the L0: exception record (deal log entry), operationalized policy (authority levels), cross-functional decision loop with retained authorization (minutes/signatures). The definition is not an artifact of the SaaS era.
- **Spreadsheet-era desk**: exception tracker + email approvals + shared drive of templates — satisfies the L0 without dashboards/AI/Slack.
- **Counter-shape**: a modern CPQ with only auto-block guardrails and no review loop does **not** satisfy the L0 — that is CPQ capability, not a deal desk. This counter-shape is what keeps the CPQ/Deal Desk seam honest.
- **Buyer-side namesake** fails the L0 deliberately (no sell-side commercial policy over the seller's own commitments) — confirming it as a different Type rather than a variant.

## Uncertainties

- Salesforce, Conga, SAP, Oracle deal desk surfaces unreachable this pass (404/403/JS walls) — the enterprise-suite pole is covered structurally (Subskribe/DealHub position against Salesforce CPQ; HubSpot's framing); no claims about specific suite internals are made.
- DealHub operational documentation login-gated — the exact approval-condition model (how conditions are expressed) is not evidenced; kept qualitative.
- Workato's "sales deal desk" recipe observed only through HubSpot's article (secondary source) — not independently verified.
- Whether a durable standalone "commercial approval platform" category exists independent of CPQ/deal-desk branding: evidence suggests the standalone pole is thin (RevOps is the clearest self-identified example, and it was acquired by a billing company — consolidation observation, not proof of category failure).
- Buyer-side deal desk products' internal approval machinery not researched (out of scope — boundary products only).
- No precise numeric thresholds (discount percentages, approval SLAs) are asserted anywhere: vendor-published customer stats exist but are marketing claims, not operational documentation.

## Final Synthesis

A Deal Desk / Commercial Approval Platform is the selling organization's **cross-functional commercial approval center**: the system of record where deals that depart from standing commercial policy are reviewed and authorized. Its defining structure is a triple — the **deal exception of record** (a pending commercial commitment held for review because it departs from policy), the **operationalized commercial policy** (guardrails, thresholds, pre-approved terms that separate auto-proceed from review-worthy), and the **cross-functional decision loop with retained authorization** (routing to reviewers from more than one function, attributable approve/reject/counter decisions, retained as the record that lets the deal proceed downstream on the excepted terms). Everything else — dashboards, parallel/sequential chains, delegation, collaboration surfaces, AI summaries, CRM integration, quote building, clause libraries — is the mature market's accumulated structure, packaging, or era-current assistance. The Type is real but its market packaging is predominantly a **capability of CPQ/revenue suites**; standalone deal-desk platforms exist but are few. The buyer-side "deal desk" is a different Type belonging to procurement. The two sibling flags (CPQ, Sales Pricing) are discharged from this side with both seams confirmed.
