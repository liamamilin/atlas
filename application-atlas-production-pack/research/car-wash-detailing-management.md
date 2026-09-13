# Research Notes — Car Wash / Detailing Management

## Research Goal

Understand what "Car Wash / Detailing Management" is as an Application Type: the operator-side business software used by car washes (express tunnel, in-bay automatic, self-serve, full-serve/flex) and auto detailing / reconditioning businesses. Identify the core objects (vehicle, service package, ticket/transaction, membership plan, detail job), the main workflows (wash transaction, membership lifecycle, detailing job), who operates the system and from which surfaces, which structures are car-wash-specific (vehicle identification, gate redemption, unlimited wash plans, car counts), and where the boundary lies against Auto Repair Shop Management, Appointment-based Service Business Management, Retail POS, Loyalty Program Management, and Field Service Management.

## Initial Boundary

- Nearest directory siblings (§29 vehicle services): Auto Repair Shop Management (processed — its research notes already flag this leaf as "appearance services with package pricing and quick turnover; no diagnostic labor-and-parts composition"), Collision Repair Management, Vehicle Inspection / Diagnostic Application.
- Nearest cross-section siblings: Appointment-based Service Business Management, Small Business Field Service Management (§29), Retail POS (§05.10), Loyalty Program Management (§05.15).
- Hypothesis to test: the defining core is the vehicle-bound appearance-service transaction (package catalog + ticket + payment), with membership machinery and vehicle identification as the industry's dominant commercial pattern but not definitional.

## Research Questions

1. What is the central record: ticket, vehicle, or membership?
2. How are services modeled (wash tiers, detail packages, à la carte services)?
3. How does an express-wash transaction flow (entry → identification → eligibility → gate → tunnel → record)?
4. How do unlimited wash memberships work (enrollment, recurring billing, card updater, decline handling, churn saving, cancellation)?
5. How does a detailing job flow (estimate → schedule → check-in → stages → checklist → QC → payment → delivery)?
6. What vehicle data is kept and why (plate, RFID tag, VIN, make/model, service history)?
7. What surfaces exist (tunnel POS, pay station, detail bay tablet, member app, back office, owner app)?
8. What reporting is standard (car counts, revenue per car, membership metrics, labor productivity)?
9. Where is the boundary vs adjacent Types, and is "wash POS" vs "detailing shop software" one Type or two?

## Representative Products

| Product | Posture | Why selected |
|---|---|---|
| Rinsed | Car-wash-specific CRM / membership growth layer that integrates with existing POS | Modern SaaS philosophy; membership-centric; multi-site operators; shows the CRM/membership pole |
| Washify (DRB) | Entry-level cloud car wash POS for single-site / small washes | Wash-side operational pole at SMB tier; includes detail scheduling module |
| DRB SiteWatch | Enterprise tunnel POS / site controller | Enterprise tier; "introduced the market to unlimited plans"; multi-profit-center chains; vehicle identification machinery |
| Mobile Tech RX | Auto reconditioning / detailing business software (app-first) | Detailing-shop pole; technician/job-centric; individual-detailer customer tier |

Rejected/abandoned: Sonny's Wash Connect (washconnect.com transport error; sonnysdirect.com 403 ×1 each — abandoned per network rule). Rinsed Help Center (support.rinsed.com) timed out — product pages only.

## Sources

- Rinsed — https://www.rinsed.com/ (home) and https://www.rinsed.com/the-car-wash-crm (product page) — fetched 2026-09-06
- Washify — https://www.washify.com/ (product page on drb.com) — fetched 2026-09-06
- DRB SiteWatch — https://www.drb.com/tunnel_solutions/point-of-sale/sitewatch — fetched 2026-09-06
- DRB Vehicle Identification — https://www.drb.com/tunnel_solutions/point-of-sale/sitewatch/car_wash_vehicle_identification — fetched 2026-09-06
- Mobile Tech RX — https://www.mobiletechrx.com/ (home) and https://www.mobiletechrx.com/workflow/ — fetched 2026-09-06

Evidence layers used below: **A** = directly observed on an official product page; **B** = observed across multiple products; **C** = canonical inference from cross-product comparison.

## Product Observations

### Rinsed (Car Wash CRM)

Key observations (Layer A unless noted):

- Positioning: "Car Wash Customer Relationship Management Software… specifically built for car wash owners and operators to grow and manage their memberships." Integrates directly with the operator's POS and website; is not itself a POS.
- Claims 3,000+ car washes as customers and "10,000,000+ active members" managed (marketing figures — treat as vendor claims).
- Product surface: The Car Wash CRM, Salespath (driveway sales conversion: "visibility into each sales moment", records audio of every sales pitch, gamification, real-time sales stats), Support Agent (AI phone support, 24/7, 16+ languages).
- CRM capabilities: automated credit-card decline messages ("dunning") so payment issues don't cost members; customized downsell offers at cancellation ("combat churn"); self-serve membership management; retail & loyalty tools; analytics with actionable insights; e-commerce ("simple online forms that make it easy to sell memberships online").
- Before/after framing: without CRM, the POS lacks data visibility, has lengthy checkout forms, cannot send CC decline notifications, suffers high member churn and limited member communication; with CRM: automated churn reduction, one-page checkout, easy reporting, integrated email/text, data in one place.
- Interpretation: the membership book (recurring plan subscribers) is the managed asset; the CRM layer exists because the POS alone does not adequately manage membership lifecycle (billing failures, churn, win-back).

### Washify (DRB)

Key observations (Layer A):

- Positioning: "entry-level point-of-sale solution for single-site or small car wash"; cloud-based; "automate your wash, reduce overhead, increase recurring sales."
- Unlimited wash plan management: "a healthy unlimited wash plan is a virtual necessity for a successful car wash today"; easy/fast enrollment; automates monthly renewal (auto-charges member cards); self-serve enrollment via website, mobile app, POS, or pay station.
- Vehicle identification: RFID tags affixed to member vehicles "automatically allow them through the gate to redeem washes"; LPR recognizes member vehicles by license plate — suited to washes without staff to affix tags; also a marketing tool ("gather information on members and non-members alike… targeted marketing based on purchase history").
- Automatic credit card updater: checks the card database every three days; contacts issuing bank on expiry (vendor-specific cadence — L3).
- Marketing tools: branded Android/iPhone app (customer signs up for monthly plan in-app; all in-app interactions recorded into POS real-time reporting), e-commerce plugins (memberships, gift cards, wash books), SMS/MMS (receipts, confirmations, promo codes), email marketing (purchase-triggered + blasts, template library), marketing automation (campaigns via email/text/push).
- Detail management module (full-serve/flex-serve): virtual scheduling — customers book/change detail appointments through the wash's app; confirmations, reminders, pick-up reminders; online booking calendar used to determine staffing needs.
- Labor tracking: built-in time & attendance; to-the-second tracking; per-detailing-assignment and per-service-type labor hours; overtime alerts; connects productivity with hours worked.
- CRM: centralized customer transactions/interactions, service-issue documentation, loyalty program management.
- Fleet account management: per-client discounts, add-ons, methods.
- Gas pump integration: sell washes at own or partner gas stations.
- Inventory management: automatic tracking, real-time data.
- Owner's mobile app: staffing, real-time data, kiosk/POS management, alerts.
- Reporting/analytics: hourly car count, marketing data, customer behavior insights; customizable; accessible anywhere.

### DRB SiteWatch (enterprise tunnel POS)

Key observations (Layer A):

- Positioning: Windows-based car wash POS; "trusted by more top 50 car wash chains than any car wash POS"; "introduced the market to unlimited plans"; supports up to 64 stations per site; single-site to multi-profit-center chain; express to full-service.
- Unlimited monthly wash plans framed as "secure weather-proof revenue" — monthly income regardless of car counts.
- Core features: labor management (employee time clock for any position, labor hours/cost, precise control of employee access to functions); inventory management (barcode reader); alerts & bulletins (sales/labor/warning); web reporting (exportable, sorting/filtering); StatWatch (key stats via browser or phone app).
- Payments: EMV processing (vendor claims ≤5s, P2PE — L3); Card Account Updater checks daily (vendor cadence — L3); framed as preventing "involuntary churn."
- Add-on modules:
  - Xpress Pay Terminal (XPT) — self-pay terminal/pay station.
  - ARM (Automatic Recharge Module) — renews plans by auto-charging cards monthly; "prevents pass sharing by tying each monthly pass to a specific vehicle license plate or tamper-resistant RFID tag."
  - Vehicle Identification — FastID AI-LPR and FastPass RFID (TotalID = both). RFID flow: tag on vehicle → reader at XPT scans → SiteWatch "assures that the car is eligible and determines the type of service the car is to receive" → gate up → car queued for the tunnel. LPR adds personalized marketing (e.g., "10th wash free, free birthday wash"), frequent-customer identification, targeted plan offers at the pay terminal, self-serve plan sign-up by entering plate number; smart/aggressive whitelisting for misreads; regional availability restrictions (AR/ME/NH — L3).
  - Multi-Site Replication — central management; plans and prepaids redeemable chain-wide.
  - Website Connect / Mobile Connect — e-commerce site component + consumer mobile app; purchases transfer directly into SiteWatch.
  - SmartCodes — barcodes/QR for coupons/prepaids sent via email/social.
  - WashCAP — sell washes at gas pumps (own or partner).
  - Loyalty Promotion Module — tracks and rewards frequent visitors.
  - Prepaids and Washbooks Control — activate, reload, track; redeemable at any location.
  - Quick Lube Pro — manage a quick-lube chain from the same system (multi-profit-center); suggestive selling, receipt messaging, Chek-Chart diagrams.
  - QuickBooks interface — GL and house accounts.
- Framing: SiteWatch is "the spinal cord of your whole business" — centrally manage car washes, quick lubes and other profit centers; share sales, labor and customer history across sites.

### Mobile Tech RX (detailing / auto reconditioning)

Key observations (Layer A):

- Positioning: "Auto Reconditioning Software" for detailing and adjacent recon verticals (detailing, PDR, glass repair, interior repair, paint touch up, wheel & rim repair, window tint, PPF & vinyl, ADAS calibration). App-first; admin portal + technician app.
- Workflow: task management; "check in cars with VIN scanning"; pricing tools ("create high-value prices", built-in pricing calculators — vendor claims data-backed pricing, L3); custom checklists; "go from scheduling an appointment to collecting payment in one app."
- Workflow management (Pro subscription): drag-and-drop board; vehicles move through color-coded stages (no limit on stage creation — vendor detail, L3); real-time view of repair progress, technician status, workload; identifies operational gaps; average repair times by tech and vehicle type.
- Service checklists: itemized; techs "consistently repair and service vehicles the same way, every time."
- Time tracking: start/stop timer per service; average repair times reporting.
- Customer experience: time-stamped before photos ("protect your business"); organized customer records; client portal — customers see their vehicle's stage in real time.
- Marketing: CRM; automated repeat-business messages.
- Finance: payment processing; paying people; taxes.
- Reports/analytics: real-time business data.
- Customer tier: individual detailers / small recon businesses ("thousands of business owners around the world"; vendor revenue figure $1.9B — L3 marketing claim).

## Cross-product Comparison

| Structure | Rinsed | Washify | DRB SiteWatch | Mobile Tech RX | Layer |
|---|---|---|---|---|---|
| Service package / price catalog | — (POS-side) | yes (POS services) | yes (wash packages, plan tiers) | yes (packages + pricing calculators) | B |
| Per-vehicle service transaction/ticket | — (reads POS data) | yes | yes | yes (job per vehicle) | B |
| Vehicle record / identification | via POS data | RFID + LPR | FastPass RFID + FastID AI-LPR; plate-tied passes | VIN scan at check-in | B |
| Unlimited / recurring wash plans | core focus (growth + churn) | core (auto-renew, self-serve enroll) | core (ARM auto-recharge; "introduced" the model) | — (not observed) | B (wash-side) |
| Membership redemption at gate | — | RFID/LPR gate | eligibility check → gate → tunnel queue | — | B (wash-side) |
| Card-on-file maintenance | decline messages (dunning) | card updater (3-day cadence) | card updater (daily cadence) | — | B |
| Churn management | downsells at cancel, win-back | — | "involuntary churn" prevention framing | — | B (partial) |
| Customer CRM | core | yes | yes (customer history shared across sites) | yes | B |
| Marketing (email/SMS/app/push) | core | yes | coupons/SmartCodes, loyalty promos | automated repeat messages | B |
| E-commerce / consumer app | membership sales forms | branded app + plugins | Website/Mobile Connect | — (client portal instead) | B |
| Detail scheduling | — | detail module (booking, reminders, pickup) | — (full-serve supported; module not detailed on page) | scheduling feature | B (partial) |
| Job/stage board for detailing work | — | — | — | drag-and-drop stages + checklists | A (single product) |
| Labor / time tracking | — | per-assignment, per-service-type | time clock per position, labor cost | per-service timers, per-tech averages | B |
| Photo documentation | — | — | — | time-stamped before photos | A (single product) |
| Client-facing job status | — | — | — | client portal (stage visibility) | A (single product) |
| Car-count / revenue reporting | analytics layer over POS | hourly car count | web reports + StatWatch dashboards | business reports | B |
| Multi-site management | multi-site operators | — | multi-site replication, chain-wide redemption | — | B |
| Fleet/commercial accounts | — | fleet accounts | house accounts | — | B (partial) |
| Adjacent profit centers (quick lube, gas pumps) | — | gas pump integration | Quick Lube Pro, WashCAP | — | B (partial) |
| Equipment/tunnel control | — | — | TunnelWatch, NoPileups, CarPics (separate products) | — | A (single vendor) |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as car wash / detailing management:

```text
Operator-configured vehicle-appearance service catalog (packages/tiers with prices)
└── Service transaction binding service(s) to a vehicle (the ticket)
    └── Payment / settlement (retail, prepaid, or plan redemption)
        └── Operator-side management of the service operation (record, count, report)
```

Four properties:

1. **Vehicle-appearance service catalog** — the operator configures what it sells (wash tiers, detail packages, à la carte services) with prices. Without it, it is not a service-business system.
2. **Vehicle-bound service transaction** — the unit of sale is a service applied to a vehicle; the ticket binds service(s) to the vehicle being serviced. The vehicle is the service subject even when anonymous.
3. **Payment/settlement** — retail payment, prepaid redemption, or plan redemption closes the transaction.
4. **Operator-side management** — the system records transactions and exposes the operation's state (counts, revenue, labor) to the business.

Historical check: pre-membership tunnel POS (package menu + per-wash ticket + car counts + cash management) and paper-era detailing shops (package ticket + checklist) both satisfy this core without vehicle records, memberships, LPR, or apps. Self-serve bay controllers satisfy the minimal transaction core. The L0 holds across eras and formats.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Vehicle identification & records** — RFID tag, license plate recognition, or VIN scan ties a vehicle (and its history) to the customer account; enables gate redemption and personalized marketing.
- **Unlimited / recurring wash plans** — the dominant wash-side commercial model: self-serve enrollment (web/app/POS/pay station), automatic monthly renewal, card-on-file maintenance (updater + decline messaging), churn management (downsells, win-back), plan tied to a specific vehicle to prevent pass sharing.
- **Gate redemption flow** — identification at entry → eligibility check → service determination → gate → queue/fulfillment.
- **Customer CRM** — contact records, transaction/interaction history, service-issue documentation, loyalty.
- **Marketing machinery** — email/SMS/push, purchase-triggered messages, campaigns, coupons/codes, win-back.
- **E-commerce & consumer app** — buy plans/prepaids/gift cards online; in-app plan management; purchases flow into the POS.
- **Labor / time tracking** — time clock; labor hours by position, service type, or detail assignment; productivity vs hours.
- **Detail scheduling** — appointment booking (customer self-serve or staff), confirmations/reminders/pick-up reminders, calendar-driven staffing.
- **Reporting & dashboards** — car counts (hourly), revenue, plan metrics, labor; site and corporate roll-ups.
- **Multi-site management** — central configuration, chain-wide plan/prepaid redemption, cross-site data sharing.
- **Commercial accounts** — fleet accounts and house accounts with per-client pricing.
- **Prepaids / washbooks / gift cards / coupons** — alternative instruments alongside retail and plans.

### L2 — Variant / Optional Structure

- **Wash format specialization** — express conveyor tunnel vs in-bay automatic vs self-serve vs full-serve/flex (hand work) vs detailing-only shop vs mobile detailing; the ticket's fulfillment cadence ranges from seconds (gate→tunnel) to hours (bay job).
- **Membership model depth** — unlimited plans vs per-wash loyalty points vs punch/washbooks; some operators run retail-only.
- **Detailing job machinery** — stage boards, itemized service checklists, per-service timers, before/after photo documentation, client-facing status portal; depth varies (single-product observations in sample).
- **Equipment / tunnel control integration** — tunnel controllers, queuing cameras, collision-avoidance, motor control; sold as companion products by equipment-side vendors.
- **Multi-profit-center operation** — quick lube, gas-pump wash sales, convenience retail alongside the wash.
- **Pricing tooling** — data-backed pricing calculators (detailing), precision pricing analytics (chains).
- **Payment hardware** — self-pay terminals/pay stations, EMV readers, kiosk management.
- **Accounting integration** — GL export / QuickBooks interfaces.
- **AI assistance** — AI phone support, AI marketing automation.
- **Regional/segment posture** — US express-wash membership boom shapes the current market center of gravity; full-serve/flex and international formats weight scheduling and hand labor more heavily.

### L3 — Vendor-specific (Research Notes only)

- Rinsed: Salespath (driveway sales audio recording, gamification, conversion stats), Support Agent (AI phone support, 16+ languages), dunning/downsell productization, "10M+ members managed" and % uplift figures.
- DRB SiteWatch: 64-station ceiling, ARM module name, FastID/FastPass/TotalID naming, SmartCodes, WashCAP, Quick Lube Pro, Chek-Chart, StatWatch, XPT, EMV ≤5s claim, daily card-updater cadence, LPR state restrictions (AR/ME/NH), 99.9%/99% accuracy claims, whitelisting modes (smart/aggressive), CarPics/TunnelWatch/NoPileups companion products, "introduced unlimited plans" claim.
- Washify: 3-day card-updater cadence, X Station / Xelerator hardware, owner's app scope, gas-pump integration at partner stations.
- Mobile Tech RX: unlimited color stages, admin-portal vs app split, Pro-subscription gating, pricing-calculator "data and science" claims, $1.9B processed figure, recon-vertical breadth (PDR/glass/tint/PPF/wheels/ADAS).

## Vendor-specific Findings

See L3 above. Notable posture differences:

- **Rinsed is not a POS** — it is a membership/CRM layer that presupposes a POS; its existence demonstrates that membership lifecycle management (billing hygiene, churn, driveway conversion) is a distinct concern from transaction processing in this industry.
- **DRB spans equipment and software** — tunnel control, collision avoidance, and pay stations are companion products; the POS is the "spinal cord" integrating them.
- **Mobile Tech RX is job-centric, not membership-centric** — no wash-plan machinery observed; economics come from per-job pricing (calculators) and technician productivity.

## Boundary Findings

1. **vs Auto Repair Shop Management** (§29 sibling, processed): repair management centers on diagnostic labor-and-parts composition (repair order with parts lines, labor guides, parts inventory, cores, DVI inspections). Car wash/detailing centers on appearance-service packages with quick turnover and no parts composition. Some vendors serve both markets; the RO economics differ enough to keep separate Types. Seam confirmed from the sibling's own research notes.
2. **vs Collision Repair Management**: collision work is insurance-claim-driven estimate/audit workflow; detailing is consumer-paid appearance service. No claim/adjuster machinery in this Type's sample.
3. **vs Appointment-based Service Business Management** (§29 generic sibling): the generic type centers on appointment booking for services. Car wash/detailing adds the vehicle-bound service subject, vehicle identification/gate redemption, membership plans, car-count reporting. Booking exists here (detailing) but is one workflow among three, not the defining one.
4. **vs Retail POS** (§05.10): a car wash POS sells configured vehicle services with gate/bay fulfillment and plan redemption; retail POS sells goods. The wash ticket is closer to a service ticket than a product sale; car-count and plan-redemption reporting have no retail analog.
5. **vs Loyalty Program Management** (§05.15): loyalty/points machinery appears here as a module (Loyalty Promotion Module, loyalty tools); the Type's core is operational (sell → fulfill → settle), not program administration.
6. **vs Small Business Field Service Management** (§29): mobile detailing travels to the vehicle, superficially FSM-like; but the job model (vehicle check-in → package → checklist → payment) is the same as shop detailing, and the wash side has no field dimension at all. FSM is a generic multi-industry Type; this leaf is the vehicle-appearance-service-specific business system.
7. **vs Fleet Management System** (§18): fleet software manages vehicles owned by the operator; here vehicles are customers' property being serviced.
8. **Internal seam — wash pole vs detailing pole**: the sample shows two fulfillment philosophies inside one Type: (a) wash-transaction pole — seconds-scale anonymous-or-identified transactions, membership redemption at the gate, car counts as the vital metric; (b) detailing-job pole — hours-scale scheduled jobs, stage boards, checklists, per-job pricing. They share the L0 core (vehicle + package + ticket + payment + operator management) and vendors span both (Washify sells both; DRB serves express and full-serve). Treated as one Type with two poles; a detailing-only product without any wash machinery (Mobile Tech RX) still satisfies the L0, as does a wash-only product without job machinery (SiteWatch without detail module).

## Uncertainties

- Rinsed Help Center unreachable (timeout) — Rinsed's operational mechanics (how POS data syncs, member-portal specifics) are known only at product-page level; no precise integration behavior asserted.
- Sonny's Wash Connect unreachable (transport error + 403) — cross-validation of the wash-POS pole rests on Washify + SiteWatch only; both are DRB-family products, so wash-side POS commonality is supported by two products of one vendor family plus Rinsed's POS-integration framing. This is a sample-depth limitation, not a contradiction; claims kept at "commonly" strength.
- Detail-side sample is single-product for stage boards, photo documentation, and client portals — kept product-specific/optional.
- No numeric limits (plan counts, station counts beyond vendor-stated, stage counts) asserted in the final document beyond vendor-stated figures kept in Research Notes.
- Regional breadth: sample is US-centric (express-wash membership market). Full-serve/flex and international formats inferred from Washify's full/flex-serve framing and DRB's "express to full-service" claim; not independently documented.

## Final Synthesis

Car Wash / Detailing Management is the operator-side business system for selling and fulfilling vehicle appearance services. Its defining core is small: an operator-configured service package catalog, a vehicle-bound service transaction (ticket), payment/settlement, and operator-side management of the operation. On top of this, mature products add the industry's characteristic structures: vehicle identification (RFID/LPR/VIN) and records, unlimited wash plans with automated recurring billing and churn management, gate redemption, CRM + marketing + e-commerce, labor tracking, detail scheduling and job machinery, car-count/revenue reporting, and multi-site management. The Type has two fulfillment poles — the seconds-scale wash transaction (membership-centric, car-count-driven) and the hours-scale detailing job (estimate → schedule → stages → checklist → payment) — sharing one core model. It is distinguished from auto repair management by the absence of diagnostic parts-and-labor composition, from generic appointment-based service management by the vehicle-bound subject and membership/gate machinery, and from retail POS by service fulfillment and plan redemption.
