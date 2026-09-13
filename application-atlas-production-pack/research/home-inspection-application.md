# Research Notes — Home Inspection Application

## Research Goal

Understand what software for the **Home Inspection Application** leaf actually is, from real products: what world it models, who uses it, how a home inspection business runs inside it, and where its boundary sits against neighboring leaves (Property Inspection Application, Small Business Field Service Management, Appointment Scheduling Application, Building Condition Assessment, Real Estate Transaction Management, Government Inspection Management).

Directory context: the leaf sits in "29 Home, Family, Personal & Local Services", surrounded by trade-business leaves (HVAC Service Management, Plumbing Business Management, Moving Company Management…). The neighborhood framing is "software for a local service trade's business" — but the leaf name says "Application", so the research must decide what the market actually sells: a report-writing tool, a scheduling hub, or one blended Type.

## Initial Boundary (working hypothesis before research)

- Hypothesis: software used by home inspectors / home inspection companies to run client-commissioned home inspections — bookings, the on-site inspection, the inspection report as the deliverable, payment.
- Most confusable neighbors: **Property Inspection Application** (§17 sibling — still unprocessed; two carried joint-review flags point at it), **Small Business Field Service Management**, **Appointment Scheduling Application**, **Building Condition Assessment** (processed; carried a flag asserting that transaction-driven single-property inspection "belongs to the sibling" Property Inspection Application), **Real Estate Transaction Management**.
- Carried flags to discharge or confirm: building-condition-assessment (§17 processed) vs property-inspection-application; government-inspection-management (§24 processed) name-proximity flag for property-inspection-application. Both flags intersect this leaf because the "inspection company inspecting for transactions" pole is exactly what home inspection software serves.

## Research Questions

1. What is the central object of this software? (inspection? order? report? job?)
2. What does that object carry (property, client, agent, services, fee, agreement)?
3. How does the report get produced — from templates? field capture? AI? What states does it have?
4. How does money flow (fee computation, invoicing, who pays, pay-at-close, refunds)?
5. Who books inspections, and what role do real-estate agents play structurally?
6. What roles exist internally (solo inspector, multi-inspector firm, office admin, franchise)?
7. What is the lifecycle of an inspection order from booking to archive, including exceptions (reschedule, cancel, duplicate, re-inspection)?
8. What ancillary services attach (radon, WDO/termite, mold) and how?
9. What varies by region/country (forms, report culture, language)?
10. Where are the Type boundaries — especially vs Property Inspection Application (§17)?

## Representative Products

| Product | Shape | Why selected |
|---|---|---|
| Spectora | Modern all-in-one SaaS (report writing + scheduling + payments + communication); solo→enterprise segments | Market-leading modern pole; exceptionally deep official help center |
| HomeGauge | Incumbent since 2001; desktop report writer + companion apps + business tools; now part of Spectora family (SHGI Corp) | Established desktop pole; buyer/agent-facing surfaces documented |
| ISN (Inspection Support Network) | Office-hub platform (25+ years): scheduling, orders, payments, agent ecosystem, own report writer; usage-based pricing | Multi-inspector/franchise pole; order-form evidence richest |
| Home Inspector Pro (HIP) | Cross-platform report-first tool (Windows/Mac/iOS/Android; 20+ countries, 10 languages) + HIP Office | International pole; desktop/mobile field-capture philosophy |

Different philosophies, different customer tiers (new inspector → enterprise/franchise), and (with the HomeGauge–Spectora family relationship noted) three independent vendor lineages.

## Sources

Research date: 2026-09-08. All evidence fetched live from official vendor surfaces.

- Spectora — product home: https://www.spectora.com/ ; features: https://www.spectora.com/features/ ; Info Center (help): https://support.spectora.com/en/ ; Inspection Details Page collection: http://support.spectora.com/en/collections/2144911-inspection-details-page ; Payments collection: http://support.spectora.com/en/collections/2144777-payments
- HomeGauge — product home: https://www.homegauge.com/ ; software page: https://www.homegauge.com/one/home-inspection-software/ ; Support Center: https://support.homegauge.com/
- ISN — product home: https://www.inspectionsupport.com/ ; Help Center: https://help.inspectionsupport.com/en/ ; Features collection: https://help.inspectionsupport.com/en/collections/99439-isn-features
- Home Inspector Pro — product home: https://homeinspectorpro.com/ (features, support, tutorials linked from site)

Access limitations: none material; all four vendor surfaces and three help centers fetched successfully. Deep per-article bodies were not fetched (collection titles + product pages carried the evidence); precise per-product state vocabularies, limits, and pricing mechanics therefore stay unverified and are not asserted below beyond what the fetched text states.

---

## Product A — Spectora (Evidence Layer A unless noted)

**Positioning** (Tier 2): "AI-powered home inspection software… report writing, scheduling, payments, and client communication" in one platform; segments: New Inspector / Experienced Solo / Multi-Inspector / Enterprise; 12,000+ inspectors claimed.

**Report writing**: mobile app (iOS/Android) + web editor + template editor; AI comment generation on all devices; voice-driven AI report writing (early access); photos and video; "offline reporting with automatic syncing"; web-based interactive reports plus PDF; commercial and residential templates; Repair Request Builder gives agents "exactly what they need to move the transaction forward".

**Scheduling**: online booking widget for any website; automated confirmations and reminders; Google Calendar integration; AI Scheduling Agent (early access) answers inbound calls, checks availability, books inspections.

**Business operations**: digital agreements + e-signatures; integrated payments (Apple Pay / Google Pay); instant payouts; **"The report doesn't unlock until you're paid and the contract is signed"** (report-lock rule); automated follow-ups to collect reviews.

**Payment depth (help center, Tier 1)**: Payments collection (50 articles): Multi-Party Payments; Instant Payouts; **Pay at Close**; payment links; split payment without Spectora Payments; "How to Have an Agent or 3rd Party Pay for an Inspection"; payment over the phone; options collections: Credit & Debit, ACH/Bank Transfers, Manual Payments, Buy Now Pay Later, Pay At Close, **Collect Payment After Publishing**; payouts management (Stripe infrastructure named in help); Refunds & Disputes (full/partial refunds, disputes, 1099-K); Invoices (add info, download PDF, edit fees on a scheduled inspection).

**Inspection object (help center, Tier 1)**: "Inspection Details Page" collection (43 articles) — change inspection address; **assign inspectors to inspections**; Reports sub-collection: update inspection with latest template, add a new report to an existing inspection, **Publishing the Report**, Publish All vs Quick Publish, **Report View Log**, **How to Unlock a Report**; Fees & Payments: payment marked "Paid in Full", **recalculate modifiers on inspections**, add/remove services and add-ons from an existing inspection; Agreements: print/add/remove/update the inspection agreement; Internal: order ID/order numbers; Emails & Texts: share report or inspection details with anyone, resend confirmation to **client or agent**, email-open tracking, SMS consent (TCPA); More: inspection change log, reorder/copy an inspection, **Client View URL**, print a work order, reschedule, cancel.

**Agent surface**: dedicated "Real Estate Agent/Realtor Resources" help collection; "Find a Home Inspector" public directory; Fixle protection-products collection (L3).

## Product B — HomeGauge (Evidence Layer A unless noted)

**Positioning** (Tier 2): "Home Inspection Software and Websites for Inspectors"; "Trusted… since 2001"; founded by a home inspector; "Now, as part of Spectora" — logo reads "HomeGauge – a SPECTORA Company"; trademark of SHGI Corp. (Family relationship recorded as market observation.)

**Product structure**: Spectora Report Writer (cloud, mobile-first) vs **HomeGauge Desktop Report Writer** ("Collect in the field, edit on desktop" via Companion app; "Use your own templates & comment libraries"; "Multiple formats (Narrative, Grid & more)").

**Business tools** (software page): streamlined credit card processing; inspection scheduling software; **buyer/inspector dashboard**; schedule appointments directly from your website; **online signatures for inspection agreements**; deliver cloud-based reports securely; **lock reports until payment is received**; automate follow-up emails; inspection guarantees; forms library "NPMA-33, Florida Wind Mitigation" and other common inspector forms (WDO); **CRL/Repair Request** — "buyers and agents create a repair list from the inspection report and attach to their repair addendum form"; custom websites; RV inspections vertical.

**Support center taxonomy (Tier 1)**: Initial Setup; **Business Management** (53 articles); Desktop Report Writer (76); Companion Apps (17); Websites; **State-Specific Requirements & Franchises** (6); HomeGauge Information (113); **Customers — "User guides for inspection customers"** (11); **Real Estate Professionals — "User guides for Real Estate Professionals"** (5). The last two confirm consumer-side surfaces for buyers and agents, not just the inspector.

**Audiences** (site footer): Home Inspectors / Home Buyers / Real Estate Agents.

## Product C — ISN, Inspection Support Network (Evidence Layer A unless noted)

**Positioning** (Tier 2): "Home inspection software for fast, professional report writing" + "the most complete home inspection software solution"; report writer + scheduling + payments + business reporting + marketing in one platform; 25+ years; "ISN powers over 2 million inspections a year"; "top franchises"; usage-based pricing per inspection processed (per-inspection price tiers displayed on pricing page); migration pitch aimed at Spectora switchers.

**Report writer**: HTML reports on phone/tablet/laptop with real-time sync; AI tools to "analyze inspection photos for defects" and write comments; photos/videos/360° images; multiple layouts; interactive HTML or printable PDF.

**Scheduling & jobs**: online scheduling **for clients and agents**; **Smart Scheduling suggests the right inspector**; "track jobs, upsells, mileage, payroll settings, notes"; agent dashboard for post-inspection follow-ups; 1-to-1 and mass email marketing; text/email reminders.

**Payments**: cards or ACH, onsite or by invoice; "FlexFund, an optional payment method allowing clients to pay for inspections at closing"; invoice system; payment requests; VA Loan Termite Invoice (WDI) invoicing; post-sale payment processing.

**Inspection order model (help center, Tier 1 — the richest evidence)**:
- "Order Form Features" (OFV1/OFV2 = order form versions): default controls — **Subject Property Address, Client, Buyer's Agent, Seller's Agent, Escrow Officer, Escrow Fields, Closing Date, Sales Price, Inspection Type, Fees, Date/Time/Duration, Inspector List, Year Built, Square Feet, Alarm and Alarm Code**; custom controls — Water Quality, New Construction, Foundation Type, Policy Holder/Number, Transferee, Relocation Contact, Report Number, Seller's/Buyer's Agency, fee-bearing dropdowns, packages control with package pricing.
- Order machinery: "View Order History"; Client/Agent/**Unscheduled** Order Grids; **Duplicate Inspection Check**; **Duplicate Inspection Notification Emails**; **"Set an Inspection Order to No Date or Time"**; Multiple Inspectors on Inspection Order; Inspection Notes Macros; auto-populating property information; "This Client/Agent May Already Exist Notice" (dedup on people too); **Daily Sequence Number (DSN)** order numbering; RLSD-Released column.
- Inspection features: **Re Inspection**; Duplicate and Re-Inspection Flags; **Multiple Public Reports**; QR Code for Report; Reschedule Email/SMS; Map Upcoming Inspections.
- Fees: Fee History; Searching Fees; "benefit of using **Services** instead of just Inspection Types"; mileage calculator; property age calculator (fee drivers); **Inspection Type Upgrades 2.0** (upsells); **Radon Setup**; Escrow Features; Inspection Estimates.
- People: Clients, Agents and Contacts grids; Multiple Clients on an Order (multiple clients → separate payment requests/invoices/FlexFund/SMS/email events); **Multiple Phone Numbers for Clients, Agents, and Contacts**; "Agent's First Inspection Banner"; Call Logging; **Agency Relationship Manager (ARM)**; **Real Estate Professional Dashboard (RED)** — agent login, zip-code filtering, "Introduction for Agents"; AgentHub; Agent Acquire (mobile).
- Report sharing: "See if Emails or Reports have been viewed"; **Repair Request List ("Formerly Known as The Reference Addendum")**; Sample Report Feature; Quality Assurance; Task List; Time Clock tool; Cost Centers; InterNACHI BuyBack System Alerts; InspectionBooking.ai; ISN Evergreen revenue program (offer clients insurance/security/warranties; site claims "up to $474 per inspection").

## Product D — Home Inspector Pro / HIP (Evidence Layer A unless noted)

**Positioning** (Tier 2): "Flexible, Interactive & Easy to Read Inspection Reports"; "used… by more than 10,000 home inspectors"; **"Runs on Windows, Mac, iPhone, iPad & Android devices in more than 20 countries and 10 languages."**

**Field-first report writing**: "inspectors are able to write reports onsite using their mobile device during the inspection, and can review and deliver reports from their home or office computer"; voice recognition for narratives; HIP Camera rapid photos with instant annotation; photos, video, 360° images in reports; **Team Inspections — "collaborate with multiple inspectors live on site or use multiple devices on the same job"**; automatic saves.

**Report culture**: PDF **and** HTML reports; digital stationery and cover-page designer; pop-up glossary for clients; **summary** ("allows the client to jump directly to issues"); Multiple Summaries categories; automatic AI translation into 6 languages; template editor "allows inspectors in more than 20 countries and 10 different languages to use our… software on any type of inspection" (residential and commercial); "Create a repair request list for agents to use in negotiations on clients' behalf".

**Office & ecosystem**: HIP Office/Lite web office; "Sync all data to HIP or Inspection Support Network" (ISN interop); separate credit-card-processing service (inspectionpayments.com); website hosting arm; desktop tutorials, mobile tutorials, help desk; review-on-site with clients via photo/video slideshow + summary comments.

---

## Cross-product Comparison

| Aspect | Spectora | HomeGauge | ISN | HIP | Evidence |
|---|---|---|---|---|---|
| Central object | Inspection (with order ID) | Inspection | **Inspection Order** | Inspection job | A (all 4) |
| Property as subject | inspection address | subject property | Subject Property Address control + sq ft, year built | per-report property | A |
| Client of record | client (payer) | buyer/inspector dashboard | Client control; **multiple clients per order** | client | A |
| Agent structurally present | confirmations to client **or agent**; agent help collection; Repair Request Builder | agent guides; CRL for buyers+agents | Buyer's/Seller's Agent controls; RED agent dashboard; AgentHub | repair request list for agents | A |
| Fee on the order | services + add-ons + **modifiers** | fees; card processing | Fees control; fee history; mileage/age calculators | (payment service external) | A (3 of 4 explicit; HIP payment separate) |
| Payment machinery | Spectora Payments: cards/ACH/BNPL/manual, payment links, payouts, refunds/disputes | card processing; report lock until paid | invoice system; payment requests; cards/ACH; FlexFund pay-at-close | separate card processing service | A (4/4) |
| Report lock/pay rule | report locked until paid + signed | lock reports until payment received | not observed | not observed | A (2/4) — common-mature, not universal |
| Agreement | e-signature agreements on inspection | online signatures for pre-inspection agreements | agreements sendable from order (sq-ft warning) | not observed | A (3/4) |
| Templates | template editor/center; import; update inspection with latest template | own templates & comment libraries; Narrative/Grid | Templates & Containers Library | flexible template editor, multi-language, "inspect anything" | A (4/4) |
| Field capture | mobile app, offline sync, photos/video | Companion app → desktop editor | ISN mobile + report writer real-time sync | mobile + desktop + team inspections | A (4/4) |
| Report publish/deliver | **Publishing the Report**; Publish All vs Quick Publish; Client View URL; view log | cloud delivery; buyer dashboard | Multiple Public Reports; QR code; viewed tracking | PDF/HTML delivery; glossary; summaries | A (4/4) |
| Ancillary services | services/add-ons on inspection | WDO/NPMA-33/wind-mit forms; RV vertical | Radon setup; WDI/termite invoices; Inspection Type Upgrades | (template-flexible) | A (3/4 explicit) |
| Scheduling | booking widget; confirmations; calendar; reschedule/cancel | online scheduler on website | smart scheduling; premium time slots; no-date orders; unscheduled grid | HIP Office (depth not observed) | A (3 explicit; HIP moderate) |
| Multi-inspector | assign inspectors; Advanced add-on for multi-inspector companies | franchises | multiple inspectors per order; smart assignment | **Team Inspections live on site** | A (4/4) |
| Exceptions | reschedule; cancel; copy/reorder; unlock report; change log | (not detailed) | re-inspection; duplicate check; no-date orders; reschedule | (not detailed) | A (2 detailed) |
| Business analytics | (metrics imagery; Advanced) | business management collection | volume, agent activity, average fees, custom reports; time clock; cost centers | (not observed) | A (ISN deepest) |
| AI | comment assist; message assist; report assist; scheduling agent | (via Spectora writer) | photo-defect analysis; comment helper; InspectionBooking.ai | translation; voice recognition | A (era-current) |

**Stable commonalities (B — cross-product)**: inspection order bound to property + client + fee; template-driven examination record; report as the deliverable with publish/deliver states; payment against the order; agent as a structurally recognized third party; mobile field capture; scheduling; multi-inspector support; ancillary add-on services; a repair-request artifact derived from the report (present in all 4 under four different branded names — strong B-layer finding).

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The client-commissioned inspection order** — a dated engagement for one specific property, commissioned by an identified client, carrying the fee for the inspection service(s) booked. Remove → generic scheduling/invoicing tooling with no inspection subject.
2. **The recorded on-site examination** — structured observations captured during the property walk-through against the inspector's template: per-area/system checklist items, comments, photos/video. Remove → booking-and-billing with no inspection substance.
3. **The inspection report as the sold deliverable** — a client-facing document assembled from the examination record, published and delivered to the client (commonly also shared with agents). Remove → field data capture with no product (property-inspection territory).

Jointly-held is load-bearing:
- 1 alone = booking calendar / order grid
- 2 + 3 without 1 = bare template report writer (thin pole; the order survives there as report-header fields — client, address, date, fee)
- 1 + 2 without 3 = inspection data capture, no deliverable
- 1 + 3 without 2 = document generator

### L1 — Common Mature Structure (universal-in-sample or near)

- Scheduling machinery: calendars, online booking widgets, confirmations/reminders (email/SMS), reschedule/cancel, inspector assignment
- Template system: areas/systems → items → comments; comment libraries; import/share; regional and statutory forms (e.g., NPMA-33 termite, state wind-mitigation — named in HomeGauge's own copy)
- Field capture: mobile apps with offline support, photo capture/annotation, video/360°, voice input, multi-device/team inspection
- Report assembly & delivery: summary sections, PDF and/or HTML/web-interactive output, publish states, client view links, report view tracking
- Fee & payment machinery: fee computed from services/add-ons plus modifiers (square footage, property age, mileage); invoices; payment links; cards/ACH; refunds; report-lock-until-paid (2/4 sampled); pay-at-close products
- E-signed pre-inspection agreements attached to the order (3/4 sampled)
- Client & agent communication automation; email/SMS open/view tracking
- Agent surfaces: agent portals/dashboards, repair-request lists generated from the report, agent-as-payer options
- Multi-inspector support: assignment, team inspection, franchise/state-requirement packaging
- Ancillary services (radon, WDO/termite, etc.) modeled as add-on services with their own forms
- Business analytics: volume, fees, agent activity
- Era-current: AI comment/photo/translation/scheduling assistance (all 4 sampled; treated as era-current, not structural)

### L2 — Variant / Optional Structure

- Firm scale: solo inspector vs multi-inspector vs franchise/enterprise (all 4 sell to these tiers explicitly)
- Platform posture: desktop writer + companion apps vs cloud/mobile-first
- Report culture: narrative vs grid styles; PDF vs interactive HTML/web (both named across products)
- Payment posture: at booking vs on delivery vs pay-at-close (real-estate-embedded)
- Regional regimes: state-specific requirements (HomeGauge collection), statutory forms, jurisdiction-defined inspection types; international multi-language templates (HIP: 20+ countries)
- Adjacent verticals run on the same tooling: RV inspections (HomeGauge), commercial property inspections (Spectora/HIP templates)
- Integration posture: standalone all-in-one vs hub + third-party report writers (ISN's integrations collection; HIP's sync to ISN)

### L3 — Vendor-specific (research notes only)

- Spectora: Repair Request Builder; Pay at Close; Instant Payouts; Stripe-based payouts; Advanced add-on; Fixle protection products; "Find a Home Inspector" directory; Spectora University
- HomeGauge: Create Request List™ (trademarked); Homebuyer PLUS perks; Companion app; narrative/grid style names; inspection guarantees
- ISN: FlexFund; RED (Real Estate Professional Dashboard); AgentHub; Agent Acquire; Agency Relationship Manager; Evergreen revenue program; Porch offerings; InterNACHI BuyBack alerts; DSN order numbering; OFV1/OFV2 order-form versioning; Cost Centers; Time Clock; InspectionBooking.ai; CloudInspect (purpose unverified)
- HIP: HIP Camera; pop-up glossary; digital stationery; HIP Office/Lite; inspectionpayments.com; sync-to-ISN interop
- Market observation: HomeGauge branded "a Spectora Company" (SHGI Corp) — consolidation noted, mechanics not researched

### Rejected Findings (not promoted)

- "Report writing is the whole Type" — rejected: 4/4 products carry order/scheduling/payment machinery around the report; ISN historically an office hub. But symmetric rejection: "it's just field-service software" — rejected: the report-as-deliverable is the signature no FSM shares.
- Agent/escrow machinery as definitional — rejected: ISN's order form carries buyer's/seller's agents, escrow officer, closing date, sales price, but that is US-resale-transaction embedding; HIP's international multi-language footprint and template flexibility show the core holds without it. Transaction fields = common (US) implementation of "commissioning context", not invariant.
- Report-lock-until-paid as definitional — rejected: 2/4 products; a payment-policy implementation.
- AI features as structural — rejected: era-current.
- "Homeowner-facing DIY inspection app" reading of the leaf name — rejected: no sampled product (or market surface) is a homeowner self-inspection tool; all four sell to inspection businesses. The directory neighborhood (trade-business leaves) corroborates the operator-side reading.

---

## Boundary Findings

1. **vs Property Inspection Application (§17 sibling, unprocessed)** — the load-bearing boundary for this leaf. The two carried flags (building-condition-assessment; government-inspection-management) assumed "inspection companies inspecting for owners or transactions" sit in §17. This pass's evidence shows the **client-commissioned, fee-per-engagement, report-as-product** pole — overwhelmingly the pre-purchase home inspection tied to real-estate transactions — is exactly what all four sampled products serve; it is this leaf's center. The coherent split: §17 Property Inspection Application = **owner/property-manager-side inspections of their own or managed portfolio** (recurring condition inspections of standing inventory, findings feeding maintenance; no per-job external client and no sold report), while this leaf = **the home-inspection trade serving external clients per engagement**. Note: building-condition-assessment's carried line "transaction-driven single-property inspection (buyer/lender due-diligence report) belongs to the sibling" is contradicted by this evidence for the buyer-side home-inspection pole; recommend the property-inspection-application pass adopt the operator/customer test above and discharge or correct that flag jointly.
2. **vs Small Business Field Service Management** — FSM's job is performing service work (parts, labor, recurring agreements); here the job's output is a condition report about a property and the report is the sold product. Scheduling exists here as a capability, not the spine.
3. **vs Appointment Scheduling Application** — booking is one capability of the order; the Type's center is the engagement + examination + report, not the slot.
4. **vs Building Condition Assessment** — portfolio-scale condition surveys translated into capital plans vs per-engagement client deliverables.
5. **vs Real Estate Transaction Management** — the transaction is that Type's container; here transaction fields (agents, escrow, closing date) merely attach to the inspection order (ISN evidence); the inspection order remains the container.
6. **vs Government Inspection Management** — regulatory authority inspecting against its own criteria, no fee-for-report vs private commercial engagement producing a paid deliverable.
7. **vs Vehicle Inspection / Diagnostic Application** — different object (vehicles vs real property).
8. **"Remove what to become another Type" tests**: remove the external paying client + report deliverable → property/owner-side inspection (§17); remove the property and report → field service; remove the examination record → document/booking tools; make the agency a government authority → government inspection management.

## Historical / Market-Sample Check (§24)

Paper-era practice: appointment book entry (client, address, date, fee) + clipboard checklist form filled during the walk-through + typed/handwritten report delivered to the client + check payment. This satisfies all three L0 structures — nothing cloud/mobile/AI/agent-portal is required. Regional check: HIP documents the same core across 20+ countries and 10 languages with fully flexible templates, i.e., without US agent/escrow/pay-at-close machinery. Older/regionally different products fit the definition. **Pass.**

## Uncertainties

- Exact lifecycle state vocabularies per product were not verified article-by-article (e.g., Spectora's publish/unlock semantics known only from titles; ISN's RLSD "Released" column unexplored). The document therefore describes states generically.
- HIP's scheduling depth (HIP Office scheduler) was not directly observed; marked moderate.
- Whether a pure report-writer-only thin pole still sells standalone today was not directly sampled; the desktop writers' standalone history supports its existence, so scheduling/payments were kept out of L0.
- ISN "CloudInspect" (20-article help collection) purpose unverified; excluded from all claims.
- HomeGauge–Spectora corporate relationship recorded from their own sites only; corporate mechanics not researched.

## Final Synthesis

A Home Inspection Application is the home-inspection business's engagement system of record: it holds **client-commissioned inspection orders** (dated engagements for specific properties, carrying fees), equips the inspector to **record the on-site examination** against templates, and **produces and delivers the inspection report** — the sold deliverable — to the client, with agents as structurally recognized third parties. Around this core, mature products add scheduling, payments (often with pay-at-close), e-signed agreements, agent portals and repair-request artifacts, multi-inspector coordination, ancillary-service add-ons, and business analytics. The Type is operator-side (the inspection company), per-engagement (external client, fee per job), and report-centric; it is distinguished from owner-side property inspection by the commercial engagement structure, and from field service by the report being the product.
