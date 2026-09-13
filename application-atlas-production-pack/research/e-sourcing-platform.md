# Research Notes — E-sourcing Platform

## Research Goal

Understand what an E-sourcing Platform really is from real products: the central object(s), the buyer-side and supplier-side workflows, the event lifecycle, the rules that govern competitive bidding, and the boundaries against Strategic Sourcing Platform (unprocessed sibling), Government Procurement Platform, Online Auction Platform, Proposal Management, Supplier Portal, Procurement Management / Procure-to-pay, and CLM.

## Initial Boundary

Initial hypothesis: a buyer-side application for running competitive sourcing events (RFI/RFP/RFQ/tender/eAuction) with invited external suppliers responding online in structured form, followed by comparison/scoring and an award decision.

Nearest neighbors: Strategic Sourcing Platform (§10 sibling, unprocessed), Procurement Management Platform, Procure-to-pay Platform, Purchase Order Management, Supplier Management Platform, Supplier Portal, Spend Analysis, Government Procurement Platform (§24, processed), Online Auction Platform / Auction Management System (§05.18, processed), Proposal Management (§07, processed), Construction Bidding Platform (§17), Contract Lifecycle Management (§11, processed).

## Research Questions

1. What is the central object — "event", "project", "solicitation"? What is its lifecycle?
2. What event types exist (RFI/RFP/RFQ/ITT/eAuction) and how do they differ structurally?
3. How is an event structured (lots, line items, questionnaires, pricing tables, attachments)?
4. How do suppliers participate (invitation vs public broadcast; registration; response portal; bidding)?
5. What rules govern responses (deadlines, revisions, sealed bids, Q&A, bid visibility, partial bidding)?
6. How does comparison/evaluation work (bid tables, scorecards, weighted multi-scoring, tabulation)?
7. Where does the platform end — award recommendation? contract/PO creation?
8. What roles exist (sourcing manager/host, evaluators/collaborators, suppliers, approvers)?
9. Historical check: what did pre-SaaS / regional / public-portal e-sourcing look like?
10. Boundaries with the neighbors above.

## Representative Products

| Product | Pole | Philosophy |
|---|---|---|
| SAP Ariba Sourcing (SAP S2C / Strategic Procurement) | enterprise suite | sourcing events inside the largest S2P suite, tied to contracts/supplier management/ERP |
| JAGGAER One · Sourcing | source-to-contract suite | "one workflow from single-line RFQ to 10,000-line BOM auction", auction- and optimization-rich |
| Market Dojo Sourcing | lightweight on-demand | self-service, pay-per-event, host/supplier vocabulary, sandpit, transparent pricing |
| Euna Sourcing (ex-Bonfire) | public-sector SaaS | solicitations built→issued→evaluated→awarded for government agencies, supplier-network broadcast |

Coupa Sourcing attempted and abandoned: coupa.com 403 (recorded by earlier sibling passes), compass.coupa.com product page Okta sign-in gated — recorded as source-access limitation, not sampled.

## Sources

Research date: 2026-09-08. Tier 1 = official operational documentation; Tier 2 = official product pages.

- JAGGAER — Sourcing solution page (official product page, Tier 2): https://www.jaggaer.com/solutions/sourcing/ — includes vendor FAQ defining sourcing software and S2C positioning.
- Market Dojo — Sourcing product page incl. full plan-feature matrix (official product page, Tier 2): https://marketdojo.com/sourcing/ and https://marketdojo.com/
- Euna Solutions (Bonfire et al. merged) — Euna Procurement + Euna Sourcing pages (official product pages, Tier 2): https://eunasolutions.com/solutions/procurement/ and https://eunasolutions.com/solutions/procurement/sourcing/
- SAP — Source-to-contract solutions page covering SAP Ariba sourcing (official product page, Tier 2): https://www.sap.com/products/spend-management/strategic-sourcing-and-contracts.html ; spend-management overview https://www.sap.com/products/spend-management/sourcing.html (404 on direct path, redirected)
- Coupa — compass.coupa.com product documentation: unreachable (Okta login gate). Recorded as limitation.

Source-access limitation: no product's help-center-level operational documentation (per-screen guides) was reachable in this environment; SAP help portal is a JS-only shell (consistent with sibling-pass records) and Coupa is login-gated. All operational claims below are therefore calibrated to official product-page evidence; precise defaults, numeric limits, and per-screen workflows are deliberately not asserted.

## Product A — JAGGAER One · Sourcing

### Key observations (evidence layer A)

- Positions "One strategic sourcing platform. Every category and event." — "From a single-line RFQ to a 10,000-line BOM auction with multi-round optimization. One workflow handles it all."
- Event types: "RFI / RFP / RFQ with re-usable category templates"; "RFx and event templates … Multi-round negotiations with stage-gated approvals."
- Auctions: "Reverse, forward, Dutch, Japanese and ranked auctions with live transparency and audit trail."
- Evaluation: "Weighted scorecards — score price, quality, lead time, ESG and risk. Configurable weights per category and event type"; "Multi-criteria evaluation & BAFO rounds"; "Commercial & technical bid envelopes."
- Award: "Award optimization (ASO) — mathematical optimization … optimized award with rule-based allocation"; "Line-level awarding with split allocation"; "Realized savings tracking post-award."
- Direct-material variant: "Hierarchical multi-line BOM RFQ", "Engineering data: drawings, specs & quality", "Should-cost modelling", "PLM, ERP and quality system integration."
- Tail-spend variant: "3-bid-and-buy comparison view", "Quick-quote events with lightweight forms", "Self-service portal for occasional buyers."
- Platform position: "Sourcing in JAGGAER One feeds Contracts, Procure-to-Pay and Supplier Intelligence on the same data layer."
- Vendor FAQ (evidence A, definitional wording): "Sourcing software is a platform that helps procurement teams manage the end-to-end sourcing process — from RFx creation and supplier engagement to bid analysis, auction management and contract award." And: "Sourcing … covers everything from market analysis and RFx events to supplier selection, negotiation and contract award. Sourcing typically sits at the start of the source-to-contract (S2C) process."
- Public-sector vertical: "Solicitation management and public bid publishing … Full audit trail and public-records compliance."
- Customer evidence: "From a 10-line RFQ to a multi-thousand-line BOM auction. Our category teams move faster, and our suppliers see one consistent experience" (TK Elevator quote).

## Product B — Market Dojo Sourcing

### Key observations (evidence layer A)

- Flagship module named "SourcingRFX & eAuctions": "Run multistage RFQs, RFPs, and eAuctions to secure the best price and fit, while ensuring transparency, compliance, and supplier resilience."
- "Perform all tender activities in one simple-to-use platform. Run RFIs, RFPs and RFQs, event weighting, document uploads and advanced pricing tables. Capture everything you would have done in a traditional spreadsheet and more."
- Auctions: "from simple lots to entire bill of materials, run Open, Ranked or Japanese forward and reverse auctions."
- Rounds/visibility: "Multi-stage RFx & Multiscoring — easy to configure participant inclusion and bid deadlines for every round, with optional visibility for real-time bid ranking. Run complex weighted events with multi scoring … allow users and groups to score."
- Questionnaires: "Create weighted questionnaires with different question types, tables and document uploads … automatic and manual scoring."
- Reuse: "Event cloning & templates — the simple template system avoids lengthy set-up times"; template libraries.
- Excel integration for event creation and participant bidding; export "post-event reports".
- Roles vocabulary: host vs supplier ("building events as a host, to experiencing them as a supplier" in the free sandpit); collaborators (multi-scoring, suppliers) as plan features.
- Plan feature matrix confirms the feature set as commercial tiers: RFx management & scheduling (RFI, RFP, RFQ); forward & reverse auctions management; event scoring; weighted events; multi-scoring collaborators; "Sealed results"; "Advanced lots", "Advanced lot partial bidding", "Advanced lot hidden columns"; multi-round tenders/multi-stage RFQs; multi-currency events; SSO; API.
- On-demand business model: "pay for and adopt the solution one sourcing event at a time"; serves public sector (G-Cloud page) and consultancies; tail-spend "Quick Quotes".

## Product C — Euna Sourcing (ex-Bonfire)

### Key observations (evidence layer A)

- Brand history: "Bonfire, IonWave, EqualLevel, and DemandStar have come together as Euna Procurement — a full-cycle platform." Bonfire was the public-sector strategic-sourcing/e-sourcing product.
- "Whether you're issuing price-only bids or complicated, multi-faceted solicitations, Euna Sourcing … is your one-stop shop for creating, issuing, evaluating, and awarding bids."
- Three-stage flow: BUILD → SOLICIT → AWARD:
  - Build: "Receive and triage procurement requests from internal stakeholders"; templates or peers' projects; "Control who works in each section, with a full audit trail"; AI advisor "before publishing to prevent against supplier questions and addendums."
  - Solicit: "Broadcast to 1.25M+ suppliers in the network; distribute updates, publish addendums, and manage Q&A online; guide suppliers through a structured, verified submission experience."
  - Award: "Use digital scorecards to capture scores, comments, and notes; run price comparison scenarios to quickly identify best value; filter, rank, and sort supplier data to support your final decision; easily export all audit trails."
- Vendor FAQ: "Euna Sourcing is an advanced procurement software designed to optimize the source-to-contract process … brings buyers, suppliers, and bid evaluators together in a single location to streamline the drafting, distributing, evaluation, and award of various solicitations."
- Supplier side: "self-register, select commodity codes, ask clarifying questions in-app, and submit bids through a simple online portal"; guided Submission Builder; self-service registration collecting documents, diversity classifications, commodity codes.
- Compliance posture (public sector): "proactive sourcing guardrails like sealed bidding, error checkers, and automated workflows"; "FOIA-ready audit trails"; "public transparency tools built-in."
- Downstream: "Generate contracts directly from awarded sourcing projects"; evaluator consensus tools; contract workflows from award.
- Evaluators: "Score and compare supplier proposals in a shared digital workspace with customizable scorecards, automated tabulation, and consensus tools."

## Product D — SAP Ariba Sourcing (via SAP Source-to-Contract pages)

### Key observations (evidence layer A, product-page level)

- "Guided sourcing — improve creation, monitoring, and awarding of request for information (RFI) and RFP sourcing events with streamlined processes."
- "Support for multiple RFx types — create 'request for' events and competitive bidding environments to save time, compare choices, and make informed decisions."
- "Process and workflow management … speed up sourcing cycles"; "Savings pipeline and tracking — optional, integrated app for tracking and reporting savings."
- "Sourcing project management and automated negotiation — create, manage, and execute projects and events for materials, including multiple renegotiation rounds and support for flexible pricing."
- "Automated project initiation — enable demand and sourcing projects to be triggered by purchase requisitions acquired from multiple back-end systems."
- "Access to material masters — ensure that the automated creation of sourcing award documents, such as contracts and POs, complies with terms and conditions."
- "Supplier management and collaboration — manage supplier lists to receive bids from the right suppliers and integrate with supplier portals to ease collaboration."
- Sourcing Assistant: "Orchestrate sourcing workstreams and tasks from supplier discovery to award … analyze bids with supplier risk and market inputs, and generate counter offers at scale."
- FAQ: SAP Ariba "supports the full source-to-contract process by integrating sourcing, supplier management, and contract creation in one cloud-based platform … enables strategic sourcing events, automates supplier onboarding, streamlines contract authoring … integrating with ERP systems."

## Cross-product Comparison

| Dimension | JAGGAER | Market Dojo | Euna (ex-Bonfire) | SAP Ariba |
|---|---|---|---|---|
| Central object | sourcing event (RFx → award); "one workflow handles it all" | event/tender (RFx & eAuctions), host-built | solicitation (BUILD → SOLICIT → AWARD) | sourcing event/project ("creation … and awarding of … events") |
| Event types | RFI/RFP/RFQ; reverse/forward/Dutch/Japanese/ranked auctions | RFI/RFP/RFQ; open/ranked/Japanese forward & reverse auctions | bids & "competitive solicitations" (price-only to multi-faceted); sealed bidding | RFI/RFP + multiple RFx types, "competitive bidding environments" |
| Event structure | lots, line items, 10k-line BOM, category templates | lots, advanced lots, partial bidding, pricing tables, questionnaires, doc uploads | requirements + structured submission builder | events + projects; materials, flexible pricing |
| Supplier participation | invited; "suppliers see one consistent experience" | invited suppliers participate via portal; sandpit simulates both sides | broadcast to 1.25M network; self-register; in-app Q&A; guided submission | "supplier lists to receive bids from the right suppliers"; supplier-portal integration |
| Rounds/negotiation | multi-round negotiations, BAFO rounds, stage-gated approvals | multi-stage RFx, per-round deadlines & participant inclusion | addenda & Q&A before submission | multiple renegotiation rounds; AI counter-offers |
| Secrecy/sealing | commercial & technical bid envelopes; live transparency option for auctions | "Sealed results" plan feature; optional real-time bid ranking visibility | sealed bidding as compliance guardrail | not observed at page level |
| Evaluation | weighted scorecards (price/quality/lead time/ESG/risk); multi-criteria | event scoring; weighted events; multi-scoring by users & groups | digital scorecards; automated tabulation; consensus tools; price comparison scenarios | bid analysis; AI bid analysis with risk inputs |
| Award | optimized award, rule-based allocation, line-level award with split allocation | post-event reports; host decision | award recorded; contracts generated from awarded projects | award documents = contracts and POs created from events |
| Reuse machinery | re-usable category templates | templates, libraries, event cloning, Excel | templates, peers' projects, approved language | projects/events; guided creation |
| Downstream | feeds Contracts, P2P, Supplier Intelligence | best-of-breed modules (contract mgmt, AP) | contracts from award; ERP integration | contracts + POs from award; ERP/material masters |
| Post-award | realized savings tracking | savings tracking add-on | savings reporting | savings pipeline & tracking app |

Common (cross-product, evidence layer B): the event as bounded competition; RFx typing (RFI/RFP/RFQ) with auctions as an additional event type; structured supplier responses (questionnaire + itemized pricing + documents) under deadline; rounds/multi-stage negotiation; evaluation via scoring/weighted criteria and side-by-side comparison; the award decision as the event's end; templates/cloning; audit trail; supplier-side portal participation; handoff to contract/PO.

Variant (evidence layer A per product, not promoted): public-sector broadcast/publication posture (Euna, also JAGGAER public-sector vertical and Market Dojo G-Cloud); direct-material BOM sourcing with ERP/PLM ties (JAGGAER, SAP); tail-spend quick-quote mode (JAGGAER, Market Dojo); auction-specific mechanics (Dutch/Japanese/ranked, partial bidding, hidden columns); forward auctions (both suites — selling side inside a buying tool, niche); on-demand per-event pricing (Market Dojo).

Vendor-specific (evidence layer A, not promoted): JAGGAER ASO multi-million-variable solver, JAI AI, "3-bid-and-buy", commercial/technical bid envelopes; Market Dojo sandpit, transparent per-event pricing, plan matrix names; Euna's 1.25M supplier network, 100K+ templates, Bonfire/IonWave/EqualLevel/DemandStar merger, FOIA framing; SAP Guided Sourcing branding, Joule Sourcing Assistant, Icertis partnership, material masters.

## Canonical Abstraction

### L0 — Defining Invariant (kept deliberately minimal)

The buyer-side system of record for competitive sourcing, defined by three jointly-held structures:

1. **The sourcing event as the bounded competition of record** — a persistent, identified event configured by the buyer: what is being bought (scope; commonly lots/line items), what suppliers must answer and price (requirements/questionnaire + priced lines), the competition rules (visibility/sealing, rounds), and the calendar (open → close). Remove → RFP documents and email threads with nothing to manage (RFP-authoring territory, not this Type).
2. **Structured external supplier responses captured through the platform** — invited suppliers respond inside the event's structure: answers to required content, itemized pricing against the buyer's lines, attachments; deadline-enforced, revisable before close, optionally sealed from competitors. Remove → an email inbox/attachment drop — the pre-digital tender inbox the digitized act replaces.
3. **Side-by-side comparison/scoring feeding the recorded award decision** — the platform arranges responses for comparison (bid tables, weighted scorecards, rankings) and the event ends in an awarded decision recorded against the event, handed onward (to contract/PO machinery). Remove → submission collection with no selection act; the "sourcing" is gone.

Jointly-held is load-bearing: 1 alone = RFP document tooling; 2 without 1 = form/attachment collection; 3 without 1+2 = generic bid-comparison spreadsheet; 1+2 without 3 = submission warehouse; 2+3 without 1 = unanchored analysis.

What is deliberately NOT definitional: auctions and auction mechanics (RFP/RFQ-only events are first-class in every sample); public posting/publication (corporate default is invitation); cloud/AI/optimization; savings tracking; supplier networks; templates; integrations; numeric limits of any kind.

### L1 — Common Mature Structure

- Event typing as RFx (RFI/RFP/RFQ) + eAuction as an additional competition mode
- Lots/line-item structure for pricing; weighted questionnaires with multiple question types and document uploads
- Multi-round events (staged RFQs, BAFO/renegotiation rounds) with per-round deadlines and participant control
- Q&A/clarification channel and addenda before close
- Weighted scorecards / multi-scoring by multiple evaluators; price tabulation and comparison views
- Templates, template libraries, event cloning; Excel import/export
- Supplier-facing response portal (invited accounts); real-time bid ranking visibility options; sealed vs open bid postures
- Audit trail across the event; post-event reporting/export
- Handoff of the award to contract/PO machinery; savings tracking as an attached app/module in suites

### L2 — Variant / Optional Structure

- Public-sector posture: public broadcast to a large registered supplier network, public notices/addenda, publication and public-records duties (shared machinery with Government Procurement Platform — the public/ruled axis)
- Direct-material/BOM sourcing: hierarchical multi-line RFQs, engineering data, should-cost, ERP/PLM integration
- Tail-spend/quick-quote mode: lightweight forms, self-service for occasional buyers, preferred-supplier routing
- Optimization-based award (rule-based allocation, split awards, what-if scenarios)
- Indexed/rate-card pricing; multi-currency events; forward auctions inside the buying tool; on-demand per-event commercial model

### L3 — Vendor-specific

JAGGAER ASO/JAI/bid envelopes/3-bid-and-buy; Market Dojo sandpit/plan names/Synergy AI; Euna supplier-network scale figures/Bonfire lineage/FOIA framing; SAP Guided Sourcing/Joule assistants/material masters/Icertis. These remain here only.

### Historical / Market-Sample Check

- Analog pre-history: paper sealed-bid tendering — the buyer issues an invitation-to-tender to a set of suppliers; suppliers return sealed, deadline-bound priced responses; the buyer tabulates bids on a comparison sheet (often with weighted criteria) and awards; the award letter opens the contract. This satisfies all three L0 legs at analog level, confirming the L0 does not overfit digital implementation.
- 2000s generation: early web e-sourcing (FreeMarkets-style industrial reverse-auction services, first Ariba/Emptoris-era modules) and public e-tendering portals — event + invited/registered suppliers + structured bids + award, without cloud, AI, supplier networks, optimization suites, or savings apps. Fits.
- Regional check: UK G-Cloud-listed on-demand eSourcing (Market Dojo), North-American public-sector sourcing (Euna/Bonfire lineage), EU public e-tendering portals — the public/ruled layer differs but the event/response/award core is identical.
- Conclusion: the defining core is era- and geography-stable; auctions, networks, and optimization are market eras/positions, not the Type.

## Boundary Findings

1. **vs Strategic Sourcing Platform (§10 sibling, UNPROCESSED — forward flag for joint review).** The market uses "strategic sourcing" and "e-sourcing/sourcing" interchangeably; suites brand the same event machinery under both names (JAGGAER sells "Strategic Sourcing" whose page is all RFx/eAuction events; Coupa's docs call the module "Strategic Sourcing"; SAP calls the same functions "strategic sourcing events" inside Guided Sourcing). Proposed seam: e-sourcing = executing the competitive event (solicitation → structured response → comparison → award); strategic sourcing = the analytic/planning discipline around it (spend/opportunity analysis, category strategy, savings pipeline, supplier discovery feeding events). JAGGAER's own FAQ supports the seam: "sourcing … typically sits at the start of the source-to-contract (S2C) process" while "strategic sourcing management is the ongoing discipline of planning, executing and optimising sourcing activity across spend categories." Joint review recommended; probable outcome = keep both with center-of-gravity split, but the alias risk is real and must be decided with the sibling's evidence.
2. **DISCHARGES procure-to-pay-platform pass flag (§10, 2026-09-08):** "Strategic Sourcing / E-sourcing (upstream events ending at contract; JAGGAER's own FAQ draws the S2C/P2P line)." Confirmed from this side with first-hand evidence: JAGGAER's FAQ draws the S2C line exactly; SAP creates "sourcing award documents, such as contracts and POs" from events (upstream of, not inside, the P2P chain); every sampled suite positions sourcing events as the S2C opening act ending at award/contract.
3. **vs Government Procurement Platform (§24, processed) — RATIFIED from this side.** That pass's seam (public/ruled axis: public solicitation → controlled response → recorded+published award) holds: corporate e-sourcing is invitation-based by default (JAGGAER, Market Dojo), and the public posture (broadcast to a registered network, addenda/Q&A, publication duties) appears as a sector configuration — even inside the same products (JAGGAER public-sector vertical; Market Dojo G-Cloud). Euna/Bonfire shows the public-sector pole can be a product's whole center. Keep both Types.
4. **vs Online Auction Platform / Auction Management System (§05.18, processed) — CONFIRMED from this side.** Same bidding mechanics, reverse direction: the buyer solicits competitive offers from suppliers and awards a contract; users are buyer teams and invited supplier bidders, not bidders/sellers in a venue; the auction is one optional event mode, not the venue.
5. **vs Proposal Management (§07, processed) — mirror image.** Proposal management is the seller side of the same RFx (responding to a buyer's RFP with content, pricing, acceptance); e-sourcing owns the buyer side (issuing, collecting, comparing, awarding).
6. **vs Supplier Portal / Supplier Management Platform (§10, processed).** Supplier participation here is event-bounded (respond to this event); the portal is the standing supplier-facing surface (orders, invoices, profiles, documents); supplier management owns the standing supplier record. Suites integrate all three; the event is the e-sourcing Type's object.
7. **vs Procurement Management Platform / Procure-to-pay (§10, processed).** Sourcing events end at award (S2C opening); PMP owns the procurement operation (governed demand, managed supplier base, purchase) and P2P the transactional chain (PO → receipt → invoice). This pass confirms the prior passes' "events→contract" seam.
8. **vs Construction Bidding Platform (§17).** Industry-shaped RFx (bid packages, bid leveling, subcontractor bids) — adjacent specialization, not this Type.
9. **vs CLM (§11, processed).** The award feeds contract creation; the contract as managed record is CLM's object. E-sourcing stops at the awarded decision (+ optional draft award documents in suites).

## Uncertainties

- Sealed-bid enforcement mechanics (when bids unseal, who sees what when) are asserted by vendors as features ("sealed results", "bid envelopes") but the operational detail was not verifiable from Tier-1 docs — kept generic in the final document.
- Supplier-side surfaces: in suites, the response UI may be part of the supplier portal rather than a standalone e-sourcing login — implementation packaging, recorded as variant, not invariant.
- Request-intake (requisition→sourcing project) evidenced strongly in SAP/Euna; likely common in suites but not evidenced for the lighter pole — kept as common-in-suites, not core.
- Precise numeric claims (network size "1.25M+", template counts, savings percentages) are vendor marketing figures — recorded here only, not in the final document.
- Coupa Sourcing not sampled (login-gated docs); market ubiquity of Coupa's Sourcing module accepted as background but no product-specific claims made.
- Whether "E-sourcing Platform" vs "Strategic Sourcing Platform" should be merged remains open until the sibling pass runs.

## Final Synthesis

An E-sourcing Platform is the buying organization's system for running competitive sourcing events: a buyer configures a bounded event (what's needed, how suppliers respond, the rules and the calendar); invited suppliers answer and price through the platform in structured form under deadline; the platform arranges the responses for side-by-side comparison and scoring; and the event ends in a recorded award decision handed to contract/PO machinery. Auctions are one optional event mode; public-sector tendering is a governed variant posture; strategy/analysis, purchase chains, standing supplier records, portals, and contracts are neighboring Types the event touches but does not own.
