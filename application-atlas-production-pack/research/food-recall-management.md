# Research Notes — Food Recall Management

Research date: 2026-09-08
Directory leaf: Food Recall Management (§20 Agriculture, Food & Natural Resources)
Slug: food-recall-management

---

## Research Goal

Understand what a Food Recall Management application actually is as an application type: what object sits at its center (the hypothesis: the recall *event*, not the lot record and not the food-safety program), what workflows define it (initiate/declare → determine affected scope → notify → collect responses → verify → close), how it relates to the standing traceability record and to the food-safety program machinery it sits beside, and where its boundaries sit against Food Traceability Platform, Food Safety Management, HACCP Management, Food Manufacturing ERP, WMS, and complaint-handling neighbors.

## Initial Boundary (hypothesis before research)

- Food Recall Management = the application whose center of gravity is the **recall event as a managed record**: a discrete, identified event that binds to affected product identity (lot/batch/date-code level), resolves to affected parties (distribution points, locations, customers), drives a notification → response → verification loop, and closes with documentation sufficient for regulators and auditors.
- It has two operational faces: the **initiator side** (manufacturer/producer declares the recall and pushes it down the chain) and the **recipient side** (retailer/foodservice/distributor receives the notice, matches against its own inventory/locations, acts, and reports back). Dedicated products often support both sides of the same event.
- Nearest neighbors: Food Traceability Platform (§20 sibling, unprocessed — the standing lot-movement record), Food Safety Management / HACCP Management (§20 siblings, unprocessed — the standing program machinery), Food Manufacturing ERP (§20, processed 2026-09-08 — recall execution as an L1 routine on its own lot data), WMS (recall traceability as an inventory control context), Complaint & Escalation Management (§07 — complaints may trigger recalls), Medical Device Post-market Surveillance (§22, processed — recall inside device regulation; cross-industry parallel).
- Prior-pass context honored: the food-manufacturing-erp pass recorded "recall execution as routine (trace/block/notify)" as its L1 and hung the seam that dedicated recall Types exist; the food-cold-chain pass noted "some food vendors bundle" condition monitoring with traceability/recall and recommended the dedicated passes hold the seam by object.
- Suspected boundary test: remove the event workflow → a traceability database remains; remove the affected-scope determination from the event → a mass-notification blast tool remains; remove the standing program machinery → an FSMS remains (the recall event workflow persists as a procedure).

## Research Questions

1. What is the central object of the system — event, lot, complaint, or program?
2. How is the affected scope of a recall determined and expressed (product × lot × location)?
3. What does the notification→response→verification loop look like, and who are the counterparties (trading partners, regulators, consumers)?
4. How does the event close, and what documentation does closure produce?
5. What standing readiness machinery exists (contacts, templates, mock recalls, plans) and is it definitional?
6. How do initiator-side and recipient-side products differ, and are they one Type or two?
7. How does the event workflow relate to traceability data, FSMS programs, and ERP lot data in real products?

## Sample Selection

Chosen for market representativeness, different product philosophies, and different customer tiers:

| Product | Vendor | Segment / tier | Philosophy | Evidence access |
|---|---|---|---|---|
| Recall InfoLink | Recall InfoLink (Boise, ID, US) | Dedicated recall event platform; manufacturers, distributors, points of sale; food-first (also pharma, pet & animal, medical device) | Cross-industry, standards-based recall event management as the whole product | Root page + Features page (Tier 1/2 marketing with detailed process timeline) |
| FoodLogiQ Recall | Trustwell (formerly FoodLogiQ; merged with ESHA Research 2023) | Supply-chain platform module; restaurants/foodservice chains, grocers/retailers, manufacturers/CPG, wholesale distributors | Recall as one module of a supply-chain traceability/compliance platform, with deep traceability integration | FoodLogiQ Recall product page (Tier 2, detailed capability list) |
| Ideagen Safefood 360° | Ideagen | Food-safety management suite for manufacturers (GFSI-oriented); 35+ modules | Recall as one module inside the standing FSMS program machinery | Root page only (module-level naming; dedicated module page redirected to homepage) |

Boundary / context samples:

- **ReposiTrak (Park City Group / Leavitt Partners)** — fetched a 2013 partnership press release describing Recall InfoLink ("standardized messages, automated communications, inventory tracking and reporting") and observed its own positioning: a traceability network marketed as "Prepare For Faster, More Precise Recalls" — i.e., the traceability side sells *readiness*, leaving *execution* to the recall platform. Context evidence only; not a representative.
- **iFoodDS** — fetched root page; current positioning is FSMA-204 traceability exchange (Trace Exchange™); no recall product surfaced on the fetched page. Not usable as a recall sample; noted as a market observation.
- **Food Manufacturing ERP pass evidence (2026-09-08)** — Foodware 365 Track & Trace ("In the event of a recall, the remaining batches of the product in question are blocked automatically and the Track & Trace procedure can start… inform the customers and suppliers concerned"), Aptean US edition ("One-Click Recall Management"), BatchMaster ("Lot Traceability & Recall" module), ParityFactory WMS/MES ("perform a recall within minutes") — used as boundary evidence for the ERP/WMS seam.

Rejected: Riser (a frequently cited dedicated manufacturer-side recall SaaS) — URL could not be confirmed (search engine timed out); not used. FDA regulatory pages — 404 on fetch; regulatory frame kept generic (see Uncertainties).

## Sources

Tier 1/2 official product pages (no paywalled help-center articles were reachable; evidence depth is product/module marketing pages with process detail):

- Recall InfoLink — https://www.recallinfolink.com/ and https://www.recallinfolink.com/features (researched 2026-09-08)
- Trustwell / FoodLogiQ Recall — https://www.foodlogiq.com/ (redirect) and https://www.trustwell.com/products/foodlogiq/recall/ (researched 2026-09-08)
- Ideagen Safefood 360° — https://safefood360.com/ (researched 2026-09-08; dedicated recall module page redirected to homepage)
- ReposiTrak — https://www.repositrak.com/recall-management/ (2013 partnership press release; fetched as context) and site nav ("Prepare For Faster, More Precise Recalls" under Traceability Network)
- iFoodDS — https://www.ifoodds.com/ (fetched; traceability positioning only)
- FDA — https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts returned HTTP 404 on 2026-09-08; no regulatory page fetched.

Evidence layer A (direct product observation) applies to all product-specific claims. The pages are marketing/product surfaces rather than step-by-step user guides, so precise numeric limits, escalation windows, report formats, and GS1 message internals are NOT asserted anywhere from memory.

---

## Product Observations

### Product A — Recall InfoLink

Observations (evidence layer A):

- Self-describes as "a fully automated, industry-leading product recall management system"; CEO quote frames the goal: "A well performed product recall protects your brand, instills confidence, and builds trust along the value chain."
- **Two-pole posture, stated on the homepage**: "Plan & Practice — Prepare your team and your supply chain with realistic mock recall simulations… ready for any recall event" and "Respond & Report — Automate recall notifications, response verification, and documentation to ensure recipients take the necessary actions."
- **A typical recall timeline, step by step** (homepage): 1) Enter Recall Details — "structured fields to ensure accuracy and compliance"; 2) Import Contacts — "upload contact info or distribution lists and designated affected parties"; 3) Automate Notifications — "email, text, phone calls, and fax with guaranteed delivery"; 4) Track Progress — "monitor real-time responses as action is taken while auto-reminders are sent to unresponsive contacts at scheduled intervals"; 5) Status Reports sent to inbox; 6) Confirm Actions Taken — "receive verification that affected products have been removed, disposed of, or corrected as necessary"; 7) Optional Re-Notification — "scheduled re-notifications to unresponsive contacts sent before finalizing the recall"; 8) Download Reports — "detailed reports for regulatory compliance and internal review"; 9) Wrap Up — "complete the recall."
- **Features page, Connect pillar**: "Send and receive notifications automatically" (both initiator and responder sides in one platform); "Utilize GS1 Product Recall Standards for consistency"; "Route notifications to preferred communication channels"; support "all product types, including food, medical devices, pharmaceuticals, and consumer goods"; "Comply with traceability and recall requirements"; **"Manage recall lifecycles, including amendments and cancellations"**; "Streamline responses from trading partners with a universal web portal"; "Optimize B2C relations, including loyalty customer notifications."
- **Integrate pillar**: "API for system integration"; "Full audit trail to meet regulatory standards."
- **Execute pillar**: "Create unique communication schedules, notification templates, and escalation policies"; "Define custom properties for incidents, events, products, and distribution points"; "Supervise recalls across segmented locations, with custom contact groups"; "Simplify contact information management."
- Supply-chain roles named: Manufacturers, Distributors, Points of Sale, Consumers. Industries named: Food, Pharmaceutical, Pet & Animal, Medical Device (food first). Customers named on page: grocers (Sprouts, URM Stores, Associated Grocers, Affiliated Foods Midwest), suppliers (Simplot, North Bay Produce).
- US Patents #8145574, #9697523 cited in footer.

### Product B — FoodLogiQ Recall (Trustwell)

Observations (evidence layer A):

- Product page title: "All-In-One Food Product Recall Management Software"; positioning: "Ensure swift food product recalls with real-time alerts and tracking"; tagline verbs: "initiate, execute, and verify recalls and stock withdrawals."
- Capability list:
  - "Instantaneously communicate product recalls and withdrawals to contacts and locations across your supply chain via email, phone, and text."
  - "Standardize Withdrawal Notifications — Create and define templatized phone, text, and email messages to ensure maximum efficiency and accuracy in a recall or stock withdrawal."
  - "Automate Escalation Actions — Create automatic escalation processes if no action is taken by a particular location or contact within a specified timeframe."
  - "Real-Time Recall Data — Monitor recall acknowledgements, responses, and resolutions across all your locations in real-time via a centralized, live dashboard."
  - "Execute Targeted Actions — Leverage FoodLogiQ's Traceability solution to identify affected products at the batch-lot level and launch a targeted removal, hold, or withdrawal on specific products or impacted locations across your supply chain."
  - "Prepare with Mock Withdrawals — Ensure your entire team is prepared for future recalls, understands standard protocols, and is ready to take action by initiating mock recalls and withdrawals across your locations."
- Process bullets: "Identify products quickly and efficiently"; "Create customizable workflows that align with your recall process"; "Monitor the recall process in real-time, with status updates and alerts"; "Create custom communication with customers, stakeholders, and regulatory agencies"; "Access documentation and audit trails for each recall"; "Check statuses and scan recalled items from mobile devices"; "Integrate with other business systems seamlessly to manage the entire process."
- Recall explicitly paired with **withdrawal/stock withdrawal** throughout — the event vocabulary includes both.
- Traceability is a separate sibling module in the same product family (FoodLogiQ Traceability; "Expedite Recalls" is a platform use-case page) — recall consumes traceability output ("batch-lot level" targeting) rather than being the traceability record itself.
- Audience pages named: Restaurants; Grocers + Retailers; Food Manufacturers + CPG; Wholesale Food Distributors; Supplement Manufacturers; Growers, Packers + Shippers. Customer logos include grocery chains and restaurant chains — i.e., heavy recipient-side (multi-location operator) usage.
- Marketing claim: "Reduce the time required to address issues and recall products by up to 70%" (vendor figure, kept here only).

### Product C — Ideagen Safefood 360°

Observations (evidence layer A, thin by design):

- Self-describes as an integrated food safety and supplier quality management platform with "over 35 modules" for GFSI-recognized standards (cloud, audit-ready working environment).
- The **Management System** feature block names recalls as one of the suite's key processes: "Take control of your key management processes, including CAPA and deviation management, auditing, management review, **recalls** and more."
- The suite's center is the standing program machinery (HACCP/PCP plans, PRPs, monitoring, supplier management, document control); recall appears as a workflow class inside that management system, listed alongside CAPA and deviation management.
- Dedicated recall module page was not reachable (URL redirected to homepage); no deeper recall-workflow claims asserted for this product.

### Context samples (evidence layer A, boundary only)

**ReposiTrak**:

- 2013 partnership press release describes Recall InfoLink as "processing recalls faster and easier… The solution's standardized messages, automated communications, inventory tracking and reporting simplify compliance efforts"; the joint pitch was "quickly and effectively get products off the shelf and out of the distribution center."
- Current site nav markets its traceability network as "Prepare For Faster, More Precise Recalls" — traceability as the readiness layer, distinct from the recall execution platform it partners with. This is the cleanest available articulation of the traceability-vs-recall-management seam from a vendor that sells both concepts separately.

**iFoodDS**: root page is now entirely FSMA-204 traceability exchange (Trace Exchange™, Key Data Elements); no recall product presented. Market observation: traceability-first vendors foreground traceability; recall execution is a separate sale.

**Food Manufacturing ERP pass (2026-09-08, sibling pass evidence)**:

- Foodware 365 Quality & Food Safety: "In the event of a recall, the remaining batches of the product in question are blocked automatically and the Track & Trace procedure can start… trace the product both up and down the line, after which you can inform the customers and suppliers concerned."
- Aptean US edition comparison chart: "One-Click Recall Management" among the food-ERP deltas; BatchMaster module: "Lot Traceability & Recall"; ParityFactory (food WMS/MES): "perform a recall within minutes."
- Reading: ERP/WMS products execute recall actions (block, trace, notify) on their own internal lot data as a routine; the dedicated recall platforms center the *event* and the *cross-organization notification/response loop* with closure documentation. The ERP recall is one node's action; the recall platform manages the event across parties.

---

## Cross-product Comparison

| Structure | Recall InfoLink | FoodLogiQ Recall | Safefood 360° (suite) | Strength |
|---|---|---|---|---|
| Recall event as the managed unit (initiate → manage → finalize) | ✓ (timeline: enter details → wrap up; lifecycle incl. amendments/cancellations) | ✓ ("initiate, execute, and verify"; "documentation and audit trails for each recall") | ✓ (recalls named as a Management System process) | Core (3/3) |
| Affected scope at product × lot level | ✓ (structured fields; "custom properties for… products, and distribution points") | ✓ ("identify affected products at the batch-lot level… specific products or impacted locations") | (not evidenced on fetched pages) | Core (2/3 deep; B) |
| Multi-channel outbound notification | ✓ (email, text, phone, fax; "guaranteed delivery") | ✓ (email, phone, text; templatized) | (not evidenced) | Core (2/3 deep; B) |
| Per-recipient response tracking + escalation on non-response | ✓ (real-time responses; auto-reminders at scheduled intervals; re-notification; escalation policies) | ✓ (acknowledgements/responses/resolutions dashboard; automatic escalation if no action within timeframe) | (not evidenced) | Core (2/3 deep; B) |
| Recipient action verification ("removed, disposed of, or corrected") | ✓ ("Confirm Actions Taken") | ✓ ("verify"; mobile scanning of recalled items) | (not evidenced) | Core (2/3 deep; B) |
| Closure documentation / audit trail for regulators | ✓ ("detailed reports for regulatory compliance and internal review"; full audit trail) | ✓ ("documentation and audit trails for each recall"; custom communication with regulatory agencies) | (suite-wide audit posture; recall-specific not evidenced) | Core (2/3 deep; B) |
| Both initiator and responder sides of the event | ✓ (send and receive notifications; universal web portal for trading-partner responses) | ✓ (initiator orgs and "all your locations" as responders; restaurant/grocer/manufacturer/distributor audiences) | (initiator/facility side only, in-suite) | Core/Common (2/3; A) |
| Standing readiness: contacts/distribution lists | ✓ (import contacts, custom contact groups, contact management) | ✓ ("contacts and locations across your supply chain") | (implied by suite) | Core/Common (2/3; A) |
| Standing readiness: mock recalls / simulations | ✓ ("Plan & Practice"; mock recall simulations) | ✓ ("Prepare with Mock Withdrawals"; mock recalls across locations) | (not evidenced on fetched pages) | Common (2/3 deep; A) |
| Notification templates + escalation policies as configuration | ✓ | ✓ | (not evidenced) | Common (2/3; A) |
| Traceability integration as scope-determination source | ✓ ("comply with traceability and recall requirements"; integration via API) | ✓ (explicit leverage of sibling Traceability module for batch-lot targeting) | (suite holds its own records) | Common (2/3; A) |
| Recall vs withdrawal vocabulary | (recall-centric) | ✓ (recalls and stock withdrawals throughout) | (not evidenced) | Variant |
| Event lifecycle transitions incl. amendments/cancellations | ✓ (explicit) | (not named on fetched page) | (not evidenced) | Common (1/3; A) |
| B2C/consumer notification | ✓ (loyalty customer notifications) | (consumer survey content; not a capability claim) | — | Optional (1/3; A) |
| Cross-industry scope (pharma, medical device, pet) | ✓ (named industries) | (food/supplement focus) | (food focus) | Variant (1/3; A) |
| GS1 Product Recall Standards alignment | ✓ (named) | (FSMA/GS1 context via traceability pages; recall page silent) | (GFSI standards framing) | Common (1/3 explicit; A) |
| Suite membership | standalone | module of supply-chain platform | module of FSMS suite | Variant (packaging) |

Reading: every deep sample centers the recall **event** with a structured record, an affected-scope resolution (product × lot × location), a tracked multi-channel notification→response loop with escalation, verification of recipient actions, and closure documentation. Standing readiness (contacts, templates, mock recalls) is universal in the dedicated products but sits on top of the event workflow. Traceability integration is the common scope-determination source but is consumed, not owned. Suite products (FSMS) embed the same workflow as one process among many. Cross-industry reach, B2C notification, and lifecycle-transition depth vary → variants.

## Canonical Model (with abstraction levels)

### L0 — Defining Invariant (minimal)

The type stands on three jointly-held properties. Removing any one stops it from being a recall management application:

1. **The recall event as managed record of record** — a discrete, individually identified event (a recall or market withdrawal of a product) carrying structured content (affected product identity, reason/severity context, instructions), a lifecycle that includes declaration, tracked progress, optional amendments/cancellation, and closure, and accumulating an attributed audit trail. This is what makes it *event* management rather than a standing registry. (Remove → a traceability database or a shelf of contact lists.)
2. **Affected-scope determination from product identity** — the event binds to the affected product at lot/batch/date-code granularity and resolves that scope to the parties and locations that hold or received the affected product (initiator side: distribution points/customers; recipient side: match against own inventory/locations). This is what makes the event *product-specific and addressable* rather than a broadcast. (Remove → a mass-notification blast tool.)
3. **The notification → response → verification loop through closure** — notices dispatched to affected parties over multiple channels, each recipient's acknowledgment and action tracked individually (with escalation on non-response), recipients' reported actions (removed / disposed / corrected) verified, and the event closed with documentation retained for regulatory and internal review. This is what makes it *management* rather than alerting. (Remove → one-way alerting.)

Jointly-held is load-bearing: (1) alone = a case file; (2) alone = a lot-matching database, i.e. traceability territory; (3) alone = mass-notification tooling; (1)+(3) without (2) = emergency broadcast; (2)+(3) without (1) = ad-hoc messaging with no event spine; (1)+(2) without (3) = a notice with no response management.

Historical check (§24-style): the paper-era recall drill satisfies all three properties at analog level — a recall binder with a product/lot list and distribution records (scope), typed/mailed notification letters plus a phone tree with a response log (loop), a recovered-stock tally and a filed regulatory report closing the file (event record). The recipient-side analog — a store manager receiving the notice, checking shelves and back room, logging disposal, phoning back completion — satisfies the same three from the other side. A 2000s email+spreadsheet recall (distribution spreadsheet, mailed PDF notice, response tracking sheet) satisfies all three. Nothing in L0 requires cloud, GS1 message standards, B2C notification, or mock-recall machinery.

### L1 — Common Mature Structure

Very common in current products, not definitional:

- standing readiness machinery: contact/distribution-list registry, notification templates, escalation policies and schedules, recall plans
- mock recall / mock withdrawal execution as a rehearsal mode of the same event workflow
- real-time event dashboard (acknowledgment/response/resolution progress across locations)
- multi-channel dispatch (email, text/SMS, phone, fax) with delivery guarantees
- configurable event fields and per-event/per-product/per-distribution-point properties
- closure reports and downloadable documentation packs (regulatory + internal)
- audit trail as a system property (who was told what, when, who confirmed what)
- API/system integration so scope and inventory data flow in from ERP/WMS/traceability systems
- recall-lifecycle transitions including amendments and cancellations
- alignment to recall message standards (GS1 Product Recall Standards explicitly named by one product) and regulatory-reporting expectations

### L2 — Variant / Optional Structure

- **Operational pole**: initiator-side (manufacturer/producer declares and pushes), recipient-side (retailer/foodservice/distributor receives, matches, acts, responds), or both in one platform (Recall InfoLink and FoodLogiQ evidence both; grocers and restaurant chains are the heavy recipient population)
- **Packaging**: standalone dedicated platform vs module of a supply-chain/traceability platform vs module of an FSMS suite (Safefood 360° pole) vs capability inside ERP/WMS (the sibling Types' seam)
- **Industry scope**: food-bound (this leaf's directory placement) vs cross-industry recall event platforms (pharma, medical device, pet & animal, consumer goods — one sampled product names all)
- **Regulatory regime**: jurisdiction-dependent expectations and message standards (US FDA/FSIS/FSMA-era; EU regime; GS1 standards) — products reference compliance by geography; the specific regime is customer-configuration, not the Type
- **Scope extension**: B2C/consumer notifications (loyalty lists), regulator-facing communication, outbreak-investigation adjacency
- **Data-source depth**: event defined from notice-level data only (standalone) vs computed from integrated traceability graphs (batch-lot targeting via platform traceability)
- **Deployment & scale**: multi-site/multi-location hierarchies, segmented location supervision, multi-language support

### L3 — Vendor-specific (kept out of the final document)

- Recall InfoLink: the 9-step homepage timeline as a branded process; "guaranteed delivery" phrasing; patented platform claims (US Patents #8145574, #9697523); "Recall Ready" branding; Recall Experts Guide lead magnet; CEO named quotes; cross-industry industry list as marketing segmentation.
- Trustwell/FoodLogiQ: "reduce recall time by up to 70%" marketing figure; "$2-$10 million average direct recall cost" marketing figure; 2500+ brands claim; consumer-sentiment survey product line; "Expedite Recalls" use-case page naming; the Traceability module's FSMA-204 positioning; Whole Foods named testimonial.
- Ideagen: 35+ module count; Azure backing; GFSI audit-ready framing; Ideagen F&B compliance division messaging.
- ReposiTrak: 2013 joint-marketing agreement details; scan-based trading framing.

---

## Vendor-specific Findings

See L3 above. Additional A-level semantics worth recording:

- Recall InfoLink's timeline is the strongest direct evidence that the event has a *structured declaration* step ("structured fields to ensure accuracy and compliance") before any communication is sent — the event record precedes the loop.
- Recall InfoLink's features page is the strongest direct evidence for lifecycle transitions beyond open/close: "Manage recall lifecycles, including amendments and cancellations."
- FoodLogiQ's capability list is the strongest direct evidence for the recipient-side loop: per-location acknowledgment tracking ("Monitor recall acknowledgements, responses, and resolutions across all your locations"), automatic escalation on inaction "within a specified timeframe," and mobile verification ("scan recalled items from mobile devices").
- FoodLogiQ's phrasing "launch a targeted removal, hold, or withdrawal on specific products or impacted locations" is the strongest direct evidence that the *action repertoire* on the event is discrete and scoped (remove / hold / withdraw), not free-form.
- FoodLogiQ's consistent "recalls and stock withdrawals" pairing is direct evidence that the event vocabulary spans recalls and (non-regulatory) commercial withdrawals — one workflow, two event classes.
- Safefood 360°'s Management System block ("CAPA and deviation management, auditing, management review, recalls and more") is direct evidence that recalls sit as a workflow class *beside* CAPA/deviation handling inside FSMS suites — the same event workflow, suite-embedded.
- ReposiTrak's traceability-network marketing ("Prepare For Faster, More Precise Recalls") plus its 2013 partnership with Recall InfoLink is direct vendor-side evidence that traceability-readiness and recall-execution are separable sales — the seam vendors themselves maintain.

## Boundary Findings

1. **vs Food Traceability Platform (§20 sibling, unprocessed)**: the standing traceability record is the *continuous* lot-movement ledger across trading partners ("where did this lot go / where did it come from"); recall management is the *episodic* event workflow executed on top of such records when a lot is implicated. Evidence: FoodLogiQ ships Traceability and Recall as separate modules, with Recall explicitly *consuming* traceability output ("leverage FoodLogiQ's Traceability solution to identify affected products at the batch-lot level"); Recall InfoLink manages events from notice-level data without owning the chain; ReposiTrak sells traceability as recall *readiness*, partnering with a recall-execution vendor for execution; the food-manufacturing-erp pass separately recorded ERP traceability as "one node's operational record." Test: remove the event workflow → a traceability platform remains; remove the standing lot ledger → a recall event platform remains (fed by imports). JOINT REVIEW recommended with the food-traceability-platform pass; this pass expects keep-both with the seam held on continuous-record vs episodic-event.
2. **vs Food Safety Management / HACCP Management (§20 siblings, unprocessed)**: FSMS/HACCP center the standing *program* machinery (hazard analysis, CCPs/PCPs, monitoring, verification, CAPA, audits); the recall is the *emergency-response event* the program prepares for. Safefood 360° embeds recalls as one process inside its 35+-module suite — the module exists precisely because the event workflow is distinct from program machinery. Expected seam for those passes: remove the event workflow → the FSMS remains; remove the program machinery → the recall event workflow remains. Consistent with the food-cold-chain pass's recommendation pattern.
3. **vs Food Manufacturing ERP (§20, processed 2026-09-08)**: the ERP supports recall *execution as routine on its own lot data* (trace, block, notify internally — that pass's L1) and remains the inventory/financial system of record; the dedicated recall type centers the *event record* and the *cross-organization notification/response loop* (trading partners, locations, consumers, regulators) with closure documentation the ERP does not own. Consistent with that pass's boundary finding #6. The two coexist: the ERP is typically the data source; the recall platform is the event manager.
4. **vs WMS (§10, processed) and food WMS/MES (ParityFactory, boundary sample of the ERP pass)**: warehouse execution products carry "recall traceability" as an inventory-control context and can "perform a recall" on stock they hold; the recall-management type is not the warehouse system — its event spans the whole chain and its users are food-safety/quality/compliance functions, not warehouse operators.
5. **vs Complaint & Escalation Management (§07)**: complaints are the standing intake for individual customer grievances; a complaint (or test result, or inspection finding) may *trigger* a recall event, but the objects differ (complaint case vs recall event) and the recall event then drives a chain-wide, regulator-facing workflow the complaint machinery does not model.
6. **Cross-industry parallel (no directory change)**: recall event machinery exists for pharmaceuticals, medical devices, pet products, consumer goods (Recall InfoLink names all four). The medical-device-lifecycle-management pass (§22, 2026-09-08) centered the device lifecycle record chain, with recalls as post-market actions — same event pattern, different regulatory/regime home. The directory binds this leaf to food (§20); the generalization is noted for taxonomy maintainers only.
7. **vs bulk-notification / emergency-notification tooling (not a directory leaf)**: mass-notification services dispatch messages and track delivery but lack the product/lot scope determination and the action-verification semantics (removed/disposed/corrected) that define the recall loop. The recall loop's *response* is an operational action against stock, not a message receipt.

Taxonomy note: no alias or variant problem for this leaf. The recall event workflow is stable and nameable across independent vendors and is sold both standalone and embedded; the leaf is kept as a separate Type with the episodic-event center of gravity.

## Uncertainties

1. No sample exposes a public step-by-step user guide or help center; all claims rest on product/feature marketing pages (with unusually detailed process content in the two dedicated samples). Precise operational details (escalation windows, report formats, GS1 message internals, delivery mechanics) are therefore not asserted in the final document.
2. Safefood 360°'s dedicated recall module page was unreachable (redirect to homepage); the suite's recall evidence is module-naming depth only. Used as placement evidence (suite-embedded variant), not for workflow claims.
3. Riser (dedicated manufacturer-side recall SaaS frequently cited in the market) could not be confirmed or fetched; the manufacturer-side dedicated pole is evidenced through Recall InfoLink's initiator capabilities and FoodLogiQ's manufacturer audience pages rather than a pure-play manufacturer tool.
4. FDA regulatory pages were unreachable (404); the regulatory frame (reporting expectations, classification practice) is grounded only in vendors' references to regulatory compliance, regulatory-agency communication, and GS1 standards. No specific regulatory rules are asserted in either document.
5. iFoodDS — a vendor historically associated with retailer/foodservice recall management — now presents as traceability-first; whether it still sells a recall product could not be confirmed from fetched pages. No claims made.
6. The exact split of initiator vs responder usage per product (e.g., whether grocers use Recall InfoLink primarily to receive or to push) cannot be verified from marketing pages; the both-sides capability is evidenced, the usage mix is not.

## Final Synthesis

A Food Recall Management application is the food supply chain's event-management system for recalls and withdrawals: its defining core is the recall event as a managed record (structured declaration, lifecycle through closure, audit trail), the affected-scope determination that binds the event to product at lot/batch granularity and resolves it to the parties and locations that hold the product, and the notification → response → verification loop that pushes instructions down (or up) the chain, tracks each recipient's acknowledgment and action with escalation, verifies that affected stock was removed/disposed/corrected, and closes the event with documentation retained for regulators and auditors. Around that core, mature products add standing readiness machinery (contact registries, templates, escalation policies, mock recalls), real-time event dashboards, integration to the traceability/ERP/WMS systems that hold the lot and inventory data, and standards/regulatory alignment. The type is one workflow serving two poles — the initiator that declares the event and the recipient organizations that act on it — realized as standalone dedicated platforms, supply-chain-platform modules, FSMS-suite modules, and ERP/WMS capabilities, with the dedicated platforms distinguished by owning the event and the loop rather than the standing lot record (traceability) or the program machinery (FSMS).
