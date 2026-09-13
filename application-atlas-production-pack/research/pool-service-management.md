# Research Notes — Pool Service Management

Research date: 2026-09-09
Leaf: Pool Service Management (DIRECTORY §F trade-services cluster, line 2108)
Slug: pool-service-management

## Research Goal

Understand what a Pool Service Management application actually is as an Application Type: the operator-side system of record for a swimming-pool service company. Establish its defining structure, the trade semantics that distinguish it from sibling field-service trades (pest control, lawn care) and from generic field service management, the canonical work shapes (recurring maintenance route stops vs one-time repairs/projects vs seasonal openings/closings), and the boundaries against adjacent Types.

This pass also carries two pre-hung joint-review flags from earlier sibling passes:

- lawn-care-business-management (processed 2026-09-08): "NEW flag for unprocessed pool-service-management (same route+chemical+recurring pattern; seam = water chemistry/pool equipment vs turf)"
- pest-control-management (processed 2026-09-09): "NEW FLAG for unprocessed pool-service-management (chemical-application sibling; same route+chemical+recurring pattern; seam = water chemistry/pool equipment vs pest treatment of structures; joint review recommended when that leaf processes)"

Both flags are discharged from this side (see Boundary Findings).

## Initial Boundary (hypothesis before research)

- Core hypothesis: same FSM family skeleton as the other §29 trade leaves — customer + serviced object → visit as unit of work → assigned technician → billing — with the serviced object being a swimming pool / body of water at the customer's property, and the visit's signature content being water-chemistry readings and treatment plus cleaning and equipment checks.
- Expected trade semantics: recurring weekly/biweekly maintenance cadence on routes; water chemistry (test readings → dosing); pool equipment (pumps, filters, heaters, salt cells) as tracked objects with maintenance cadences (filter cleans, salt cell cleans); seasonal work (openings/closings); monthly recurring billing.
- Likely confusion: pest-control-management and lawn-care-business-management (chemical-application siblings); generic field service management; appliance-repair (equipment-repair overlap); property maintenance management (owner side).
- Initial unknowns: (1) is water chemistry machinery definitional or standard? (2) do pool products carry a regulatory-reporting layer like pest control's pesticide usage reports? (3) is the "body of water" (pool vs spa vs multiple) a distinct structural object? (4) how do one-time repairs/jobs relate to recurring route stops? (5) how does seasonality shape the software?

## Research Questions

1. What is the serviced object — property, pool, or body of water — and how do products model it?
2. What is the unit of work, and what canonical shapes does it take (recurring route stop, one-time job, repair, opening/closing, filter clean)?
3. How does water chemistry enter the record: readings, dosing, cost tracking, customer-facing proof?
4. How does equipment enter the record, and does equipment state change the work?
5. How do routes work (assignment, frequency, optimization, skipped stops)?
6. How does billing work (monthly recurring, per-visit, repairs, chemical pass-through)?
7. What roles use the system (owner/office/technician/customer) and on what surfaces?
8. Is there any regulatory/compliance layer (licensing, chemical usage reports) comparable to pest control's?
9. How does seasonality manifest in the software?
10. Where are the boundaries vs pest control, lawn care, generic FSM, and adjacent Types?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

1. **Skimmer** — pool-dedicated, mobile-first, the self-described market leader by customer count ("trusted by 30,000+ pool pros"); tiered from solo operators to enterprise. Deep Tier-1 help center (help.getskimmer.com). Philosophy: all-in-one, tech-app-first, ease of use.
2. **Pool Brain** — pool-dedicated, web-dashboard + tech app, aimed at larger/growing companies ("the largest companies in the industry run on Pool Brain"); heavy automation philosophy (guided workflows, auto-dosing, auto-billing, alerts). Tier-1 help center (help.poolbrain.com) + rich feature pages.
3. **Pool Office Manager (POM)** — pool-dedicated, deliberately positioned against the "perfect repeating routes all year" model: built for seasonal service & repair companies, jobs that span visits, follow-ups, weather disruption. Philosophy: seasonal/repair-first realism. Product/feature pages (Tier-2).
4. **Kickserv** — horizontal field service management used by service trades; the generic-spine control sample (Tier-1 help center), same control role it played in the pest-control and lawn-care passes.

Rejected/adjusted candidates:

- **FieldRoutes** — checked for a pool-service line; its site documents pest control as the flagship industry and a generic "other field service industries" page (plumbing/HVAC/cleaning) with no pool-specific line at fetchable depth. Dropped from the pool sample (it remains the pest pass's sample product).
- **Jobber** — listed by Skimmer's comparison page as a competitor used by pool companies, but its industry pages returned HTTP 403 twice; abandoned per the source-access rule. Recorded as indirect evidence only.
- **PayThePoolman, ProValet, Pool Service Software (poolservicesoftware.com)** — named as competitors on Skimmer's comparison page; not fetched (sample already saturated; stop conditions met).

## Sources

Fetched 2026-09-09:

- Skimmer product root — https://getskimmer.com/ (also reached via https://www.skimmer.com/ redirect failure → getskimmer.com)
- Skimmer Help Center (Help Scout docs) — https://help.getskimmer.com/
  - Manage Work Orders category — https://help.getskimmer.com/category/62-work-orders
  - Record Chemical Readings and Dosages for a Work Order (App) — https://help.getskimmer.com/article/193-record-chemical-readings-and-dosages-for-a-work-order-app
  - Jobs FAQ — https://help.getskimmer.com/article/291-create-and-manage-jobs
  - Create, Edit, or Delete Automatically Recurring Work Orders (Web) — https://help.getskimmer.com/article/284-create-edit-or-delete-automatically-recurring-work-orders-web
  - Manage Routes category — https://help.getskimmer.com/category/14-manage-routes
  - Build a Pool Service Route Fast (Web) — https://help.getskimmer.com/article/96-build-a-route-web
  - Skipped Stops — Skip Tracking, Reasons, and Email Alerts — https://help.getskimmer.com/article/160-skipped-stops-skip-tracking-reasons-and-email-alerts
- Pool Brain product root — https://www.poolbrain.com/
- Pool Brain features page — https://www.poolbrain.com/features/
- Pool Brain Help Center (Intercom) — http://help.poolbrain.com/en/
  - Create & Edit Service Levels — https://help.poolbrain.com/en/articles/4420076-create-edit-service-levels
  - Automatic Chemical Dosing — https://help.poolbrain.com/en/articles/9114035-automatic-chemical-dosing
- Pool Office Manager product root — https://poolofficemanager.com/
- Kickserv Knowledge Center, Jobs article — https://kickserv.helpscoutdocs.com/article/32-jobs

Unreachable / dropped:

- Jobber industry page — HTTP 403 on both attempts (getjobber.com and www.getjobber.com); abandoned.
- Skimmer root via www.skimmer.com — transport error once; getskimmer.com succeeded (same site).

Evidence quality note: this pass is unusually strong — two pool-dedicated products documented at help-center level (Skimmer, Pool Brain), versus the pest and lawn-care passes where no trade-dedicated product had a reachable help center.

## Product A — Skimmer

### Key observations (evidence layer A unless noted)

Positioning: "All-in-one Pool Service Software for Routing, Scheduling & Billing"; "trusted by 30,000+ pool pros"; priced monthly per service location; tiers for "Getting Started / Scaling Up / Owning the Market (Enterprise)". Product surfaces: Back Office (web app), Technician (mobile app), Client features, Billing & Payments.

Core objects observed at help-center level:

- **Customer / service location** — routes are built from customer + location; customer profile holds gate codes, service history, equipment.
- **Route assignment (route stop)** — Route Builder binds tech + day of week + customer/location + frequency + start-on + stop-after (or "no end"). Stops reorderable by drag & drop; Optimize Route reorders automatically (documented limit: up to 25 routes per assignment; tier-gated to Scaling Up/Enterprise). Route Dashboard shows the day's stops; skipped stops highlighted orange.
- **Work order** — "a standard work order is a one-time job"; work order types carry defaults (work needed, tech pay, customer charge, estimated minutes). Recurring work orders repeat on a schedule "just like a route stop" (tier-gated: Scaling Up, Enterprise). Work order statuses include unscheduled/scheduled/finished (as seen in Jobs).
- **Jobs** — newer object for "continuity from quote to work to invoice to payment", aimed at "repairs, installs, or other one-time services". Created from an approved quote; carries line items, deposits (Not Collected → Collected → Applied), invoices, and work orders; statuses Not Started / Active / Work Complete / On Hold / Closed (+ Archived); tax rates dynamic until close, then snapshotted. "Items Needed" per work order: products, parts, chemicals; installed items can be added as invoice line items; uninstalled items sit "On Shopping List".
- **Chemical readings & dosages** — recorded on work orders and (canonically) on route stops; each body of water at a service location gets its own chemical tab (pool + spa example given by the docs); readings + dosages saved to the customer's service record; service emails to the customer include readings and dosages (configurable to omit). LSI and dosage calculator in the app (Orenda); readings importable from the LaMotte Spin Touch water tester.
- **Skipped stops** — a route stop can be skipped; optionally the tech must choose a reason (configurable reason templates); optional email to office and to customer; skipped stops visible on the Route Dashboard.
- **Billing** — invoices generate automatically from completed work; AutoPay for recurring service; "track chemicals and installed items so nothing goes unbilled"; QuickBooks Online sync; card surcharging; failed-payment alerts; customer portal and text-to-invoice.
- **Shopping List** — a first-class category (11 help articles): parts/chemicals needed in the field flow to a shopping list.
- **Reports** — 23 help articles; time tracking per stop.

Marketing metrics on the root page (miles saved, hours saved, growth multipliers) are vendor claims — excluded from all findings.

## Product B — Pool Brain

### Key observations (evidence layer A for help-center articles; A/B for feature pages)

Positioning: "Pool Company Software that optimizes everything"; "built by industry experts"; customers include large pool-service brands (franchisors and multi-route operators shown on the root page).

Core objects observed:

- **Route Stops vs Jobs** — "One Time Jobs and Route Stops are very different animals so we treat them differently throughout Pool Brain"; viewable/schedulable together or apart, clearly marked on web and app. This is the same seam Skimmer draws (route stop = recurring maintenance visit; job = one-time undertaking).
- **Service Levels** (help center) — control route-stop workflow requirements, assigned per body of water on a property: which checklist items are required, which chemical readings are required and under what circumstances, and system items like Backwash, Filter Clean, Salt Cell Clean. Common examples: "Complete Care", "Chemicals Only", "Full Service", "VIP Service", "Hot Tub Service". Service Levels control workflow; "Types" control technician pay and default billing prices. Estimated time per visit feeds route work-time totals; the service level appears as the line item on monthly invoices.
- **Bodies of water** — a property can carry multiple bodies of water (pool, spa, …); pricing, workflow, equipment, chem use/cost, tech pay, jobs, and alerts are all manageable per body of water; no documented limit on count. Techs are prompted to select which body of water they are servicing.
- **Chemical dosing & cost** (help center) — dosing amounts auto-entered from the readings the tech records for the visit; tech can edit or confirm; built-in Orenda calculator; dosing by LSI supported. Chem use and cost tracked automatically by customer, job, property, body of water, technician, and company total.
- **Equipment tracking** — equipment types, notes, and photos per property or body of water; **workflows change automatically based on equipment entered: "No salt cell? A salt reading won't be required. Cartridge filter? Backwash option is removed."**
- **Filter clean auto-scheduling** — filter and salt cell clean jobs auto-created on a chosen schedule; last-cleaned date auto-updated on completion; sorted into categories.
- **Custom alerts** — out-of-range chemical readings, flow (clogged impellers, backwash needed), leaks, time (late start, too long at a stop), cost (high chemical usage).
- **Guided workflows** — tasks can't be skipped, forgotten, or "cheated"; the app walks the tech through the configured steps.
- **Issue reports** — tech reports to office from the app with categories like "repair needed" or "system down", photos, notes; auto-associated with job and technician.
- **Job templates** — named examples: "pool openings/closings, pump prime issues, inspections, pool school, drains, acid washes".
- **Quotes → jobs → invoices** — quotes approved with a tap auto-create jobs; invoices auto-created when a job closes.
- **Automatic billing** — monthly invoices created, charged (credit card/ACH), and emailed automatically; retry on decline (documented: once per day); advance or arrears; flat rate or per visit; chemical usage charged automatically.
- **Proof of service** — service emails sent on route-stop completion with labeled photos (e.g., water level low, couldn't access property); 1-click customer feedback; customer portal with job/route-stop history (positioned for property-management companies reviewing many properties).
- **Technician pay & scorecards; route profit reports** — pay calculated per employee/property/body of water/service level; route profit shows good/low/negative profit per account.
- **Offline app** — works without signal or username/password; syncs when connected.
- **Integrations** — WaterGuru (remote water-chemistry monitoring), Pentair, Orenda (LSI), LaMotte Spin Touch (water tester), Heritage Pool Supply (distributor), QuickBooks Online.

## Product C — Pool Office Manager (POM)

### Key observations (evidence layer A for its own product pages; treat cross-product claims as B)

Positioning: "Pool Service Software Built for Seasonal Pool Service & Repair"; explicitly anti-route-perfectionism: "Most pool software was built for perfect, repeating routes all year. But real pool companies do not operate that way." Canonical work named on the root page: **Pool Openings + Closings, Pool Cleanings, Repairs + Projects, Rentals + Commercial Pools**. Pain points named: jobs that don't finish in one visit, repairs requiring follow-ups, weather delays, techs who forget to write things down, customers questioning service and invoices, chemicals/parts "disappearing".

Features (product pages):

- Route + scheduling that "change with the season"; drag/reschedule/add repairs; GPS tracking of techs and completed stops.
- Invoicing: custom or recurring invoices; "invoices are tied directly to completed work"; charges, notes, photos, approvals flow from field to office; QuickBooks 2-way sync (QBO) / 1-way (Desktop).
- CRM: calls → digital quotes by text/email → e-signature → stored contracts ("liability protection").
- Inventory: every part and chemical used in the field auto-updates inventory as jobs close; truck stock visibility; route preparation (trucks stocked with right parts/chemicals/customer notes).
- Pool chemical calculator: enter readings → instant chlorine/acid/shock requirements "for each pool".
- Reporting: average service time per technician, chemical costs per customer, profitability.
- Pricing per active user; users can be turned off in the off-season to reduce cost (seasonal staffing realized in the licensing model).

## Product D — Kickserv (generic control)

### Key observations (evidence layer A)

- Jobs are "the heart of the Kickserv workflow": Unscheduled → In Progress → (optional On Hold) → Completed; jobs start from opportunities/estimates or directly; scheduling assigns date/time/task type/technician; recurring series supported; invoice at the end.
- No pool semantics anywhere in the jobs workflow: no route stops, no bodies of water, no chemical readings, no equipment-driven workflows, no seasonal machinery. Confirms the generic spine (customer → job → schedule → tech → invoice) without trade depth — the same control result as the pest and lawn-care passes.

## Cross-product Comparison

| Dimension | Skimmer | Pool Brain | Pool Office Manager | Kickserv (control) |
|---|---|---|---|---|
| Customer + serviced pool record | customer + service location; equipment & gate codes on profile | customer + property + bodies of water (pool/spa/…) | customers + pools; rentals + commercial pools named | customer/contact only; no pool object |
| Recurring maintenance unit | route assignment (tech+day+frequency) | route stop under a service level per body of water | routes that "change with the season" | recurring job series (generic) |
| One-time work unit | work order; Jobs (quote→work→invoice→payment) | Jobs ("very different animals" from route stops) | repairs/projects with follow-ups | jobs (generic) |
| Water chemistry in the record | readings + dosages per body of water; LSI/dosage calculator; tester import | required readings per service level; auto-dosing; chem cost tracked at every grain | chemical calculator (chlorine/acid/shock) | none |
| Equipment | equipment on customer profile | equipment per property/body of water; workflow adapts to equipment (salt cell, filter type) | parts/chemicals inventory; truck stock | none |
| Equipment-maintenance cadence | — (not observed at fetched depth) | filter clean & salt cell clean auto-scheduling | route preparation incl. parts | none |
| Seasonality | stage-based marketing (start→scale→enterprise) | — (not explicit at fetched depth) | explicit: seasonal positioning, off-season user off-switch | none |
| Skipped stop / access failure | skip tracking with reasons; office & customer emails | "couldn't access property" photo in proof-of-service email | weather/emergency rescheduling narrative | generic job hold |
| Billing | auto-invoices from completed work; AutoPay; chem & installed items billed | automatic monthly billing; advance/arrears; per-visit/flat; chem usage charged | recurring + custom invoices tied to completed work | invoice after job |
| Customer-facing proof | service report emails with photos + readings/dosages | proof-of-service emails with labeled photos; portal; 1-click feedback | post-service reports emailed | — |
| Technician assignment | route assignment; work order assignee | techs assigned to routes/stops; pay per service level | crew routes; GPS | tech assignment on job event |
| Regulatory/compliance layer | none observed | none observed | none observed (contracts for "liability protection" only) | none |
| Deployment | SaaS, web + mobile, offline app | SaaS, web + mobile, offline app | SaaS (web), per-user pricing | SaaS |

## Canonical Abstraction Hierarchy

### Level 0 — Defining Invariant

Four jointly-held structures (family pattern of the §29 trade leaves; trade semantics live inside the objects):

1. **The customer with serviced pool(s)/body of water** — pool work is delivered at the customer's property on the pool itself, so the pool (and any additional bodies of water — spa, etc.) is a managed record bound to the customer, carrying water and equipment context. Remove → generic customer list / task tracker.
2. **The pool service visit as the unit of work** — a dated commitment bound to customer + pool + time, in two canonical shapes: the recurring maintenance visit (route stop on a standing frequency — the trade's dominant rhythm) and the one-time undertaking (repair, install, project, opening/closing) carried quote→work→invoice. The visit is the hub to which readings, treatments, cleaning/equipment checks, photos, and charges attach. Remove → address book / invoicing shell.
3. **The assigned technician** — office-managed assignment of the person who performs the work; routes organize the recurring visits per technician-day. Remove → self-service booking.
4. **Billing of the work** — completed visits and jobs resolve into money: recurring plan billing (monthly cadence documented in-sample), per-visit or flat-rate billing, repair invoices, chemical/parts pass-through. Remove → dispatch board.

Jointly-held is load-bearing: (1) alone = contact list; (2) without (1) = free-floating work orders; (1)+(2) without (3) = booking calendar; (1)+(2)+(3) without (4) = dispatch board.

### Level 1 — Common Mature Structure

- **Water chemistry machinery** — test readings captured per visit per body of water; dosing computed (auto-dosing with editable confirmation; LSI-based calculation; tester-device import); chemical usage and cost tracked (per customer/pool/tech/company); readings+dosages shown to the customer in service reports. The strongest trade signature — present in all three pool-dedicated products — but machinery depth varies and the visit remains a pool visit without it (a cleaning-only or equipment-only visit still fits the Type).
- **Equipment records** — pool equipment (pumps, filters, heaters, salt cells, automation) held per property/pool with photos/notes; in the deepest sample, workflow adapts to equipment state (no salt cell → no salt reading required; cartridge filter → no backwash option).
- **Equipment-maintenance cadence** — filter cleans / salt cell cleans auto-scheduled on their own cycle with last-cleaned tracking.
- **Route management** — route builder (tech + day + frequency), drag & drop resequencing, one-click optimization, map views, unscheduled bins, one-time moves to absorb disruption.
- **Technician mobile app** — the day's stops, guided workflows/checklists that can't be skipped, readings entry, photos, issue reports to the office, payments; offline operation.
- **Proof of service** — automatic service-report emails with photos (and readings/dosages), customer portal, 1-click feedback; review management.
- **Quotes → jobs → invoices** — digital quotes with e-signature, approval converting to a job, invoices tied to completed work, deposits.
- **Payments & collections** — card-on-file/autopay, automatic monthly billing with retry, surcharging, failed-payment alerts, QuickBooks sync.
- **Skipped-stop handling** — skip with required reason templates, office/customer notifications, dashboard visibility.
- **Reporting** — route profit per account, chemical cost per customer, tech time/scorecards, collections.
- **Inventory / shopping list** — parts and chemicals used in the field tracked against truck/warehouse stock; needed items flow to a shopping list.

### Level 2 — Variant / Optional Structure

- **Seasonal posture** — year-round sun-belt routes vs seasonal companies (openings/closings, off-season user off-switch, weather-driven rescheduling as a first-class concern).
- **Multiple bodies of water per property** — pool + spa + additional water features; priced and worked per body of water (deeply implemented in 2/3 pool-dedicated products; not observed as a distinct object at Kickserv).
- **Commercial / rental pools** — apartments, hotels, rentals; portal-based review for property managers (named by one product; depth unverified).
- **Sensor-fed chemistry** — remote water-chemistry monitors (in-water devices) feeding readings via integration, vs manual test-kit readings (integration-documented at one sampled product, via two integration partners; an emerging layer, not the baseline).
- **Technician pay machinery** — per-visit/per-service-level pay calculation and scorecards (depth varies).
- **Sales/CRM depth** — lead capture, e-signature contracts, review requests (depth varies).
- **Pricing model of the software itself** — per service location vs per user (vendor-commercial, not structural).

### Level 3 — Vendor-specific (research notes only)

- Skimmer: "Jobs" as a distinct object from work orders (2026-era feature); tier-gating of recurring work orders and route optimization (Scaling Up/Enterprise); documented optimize limit (25 routes per assignment); pricing per service location; LaMotte Spin Touch import; Sunbit consumer financing; AI Phone surface.
- Pool Brain: Service Levels vs Types split (workflow vs pay/pricing); default service levels ("Complete Care", "Chemicals Only"); daily card-decline retry; Orenda calculator integration; WaterGuru/Pentair/Heritage Pool Supply integrations; app runs without username/password offline.
- POM: per-user pricing with off-season off-switch; QuickBooks Desktop 1-way vs QBO 2-way sync; onboarding-time claims; named pain-point marketing.
- Kickserv: generic job statuses (Unscheduled/In Progress/On Hold/Completed); opportunity→estimate→job chain.

## Vendor-specific Findings

See Level 3. None of these entered the canonical model. The Skimmer Jobs-vs-work-order terminology and Pool Brain's Service-Level/Type split are product vocabularies for the same underlying seams (one-time vs recurring work; workflow config vs pricing config).

## Boundary Findings

### vs Pest Control Management (joint review DISCHARGED — keep-both RATIFIED)

The pest-control pass pre-hung this review: "chemical-application sibling; same route+chemical+recurring pattern; seam = water chemistry/pool equipment vs pest treatment of structures." Confirmed from this side:

- Both are route-based recurring-visit trades whose visits carry chemical content, with technician assignment and billing. The skeleton is shared (FSM family).
- The seam holds: pest control's serviced object is the structure/interior treated for pests under structural-pest-control regulation; pool service's serviced object is the body of water and its equipment. Pest's chemical records exist for **regulator reporting** (state pesticide usage reports, retention periods, WDO forms); pool products in this sample document **no regulatory reporting layer at all** — pool chemical records serve billing (chem cost tracking, chem pass-through billing) and customer proof (readings/dosages in service reports), not a regulator. Pest tracks monitored devices (bait stations); pool tracks water-quality equipment with maintenance cadences (filter/salt cell cleans) — different objects, different semantics.
- Neither leaf's defining core contains the other's trade semantics. Keep-both ratified; the lawn-care and pest-control flags are discharged.

### vs Lawn Care Business Management (flag from lawn-care pass discharged)

Seam as pre-hung: "water chemistry/pool equipment vs turf." Confirmed: lawn care's serviced object is turf/grass with treatment programs; pool service's is the pool with water balance and equipment. Same route+recurring skeleton, different trade content. Keep-both.

### vs Small Business Field Service Management (standing family flag carried)

Same question as all §29 trade passes: is a trade leaf just a Variant of generic FSM? The family position (established across nine prior sibling passes) is that the trade leaves share the generic skeleton but accumulate trade semantics inside their objects that generic products lack — confirmed here by the Kickserv control (no pool object, no chemistry, no equipment-driven workflow, no route-stop concept). The trade-Variant question remains deferred to the small-business-field-service-management leaf; the §29 trade-cluster consolidation recommendation (family-with-variants structure) now stands across TEN convergent sibling passes.

### vs adjacent Types

- **HVAC Service Management / Plumbing Business Management / Appliance Repair Management** — equipment-repair overlap; pool service's differentiator is the recurring water-care cadence on the pool itself (chemistry + cleaning), not break-fix dispatch on interior systems/appliances. A repairs-only pool company sits at the Type's edge, closer to the repair-trade pattern.
- **Property Maintenance Management** — owner/manager side; pool service is the procured trade's operator system. Pool Brain explicitly positions its portal for property-management companies — the two Types meet there but remain distinct.
- **Appointment-based Service Business Management** — clients book at a place of business; pool service is provider-travels-to-client on routes.
- **Home Services Marketplace / Local Service Marketplace** — demand-side discovery/booking; this Type is one company's operator-side system of record.
- **Water Quality Management (§21 environmental)** — different domain entirely: environmental water monitoring of natural/wastewater systems, not consumer pool water care.

### "去掉什么就变成另一个 Type" 判据

- Remove the pool/body-of-water as the serviced object → generic FSM (Kickserv pole).
- Remove the recurring route cadence (keep one-time jobs only) → repair-trade management (appliance-repair pattern) — the POM "repairs + projects" pole shows this is a variant within the Type, not a different Type, because the same objects (customer+pool, visit, tech, billing) carry it.
- Remove billing → dispatch board. Remove technician assignment → booking calendar.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit?

- **Paper-era pool service**: route cards / stop lists per tech-day, chemical test kits with handwritten log cards (per-pool reading/treatment history), equipment notes, monthly billing booklets — satisfies all four legs with no software: customer+pool record, dated visit with readings/treatment content, assigned tech, billing. The definition holds.
- **Pre-smartphone desktop era** (e.g., early-2000s pool-industry desktop packages): same objects on desktop; fits.
- **Regional markets**: pool service exists anywhere pools exist (sun-belt US, Australia, Mediterranean); nothing in the definition is US-specific. No regulatory forms are named in the core (unlike pest), so non-US regimes fit trivially.
- The definition names no smartphone app, no auto-dosing, no LSI, no GPS, no SaaS — all era machinery stays out of the core.

Historical check: **passed**.

## Uncertainties

1. **Regulatory/certification layer**: some jurisdictions regulate commercial pool operation (operator certifications, health-code inspections for public pools). No sampled product documents a compliance/inspection module; recorded as an uncertainty — not claimed present or absent in the Type. If such machinery exists in market products, it is likely Optional (L2), by analogy with pest's regulatory layer being trade-specific.
2. **Commercial pool route depth**: POM names "Rentals + Commercial Pools" but no sampled product documents commercial-pool-specific structure (health inspections, per-facility compliance) at fetched depth.
3. **Sensor-fed chemistry trajectory**: WaterGuru/Pentair integrations show remote monitors feeding readings; whether sensor-fed readings become the default input model is a market question, not resolvable from this sample.
4. **Skimmer "Jobs" maturity**: the Jobs object is new (2026-era release notes); its relationship to the older work-order object may consolidate; both were documented as fetched.
5. **Pool-brain "Types"** (pay/pricing config) documented only via the Service Levels article's explanation; not independently fetched.
6. **Jobber's pool-industry usage** — indirect only (Skimmer comparison page); Jobber pages unreachable (403 ×2).

## Final Synthesis

Pool Service Management is the pool-service company's operator-side system of record, and it is a **sibling trade variant of the §29 field-service family**: the same four-leg skeleton as pest control and lawn care (customer + serviced object → visit as unit of work → assigned technician → billing), with the serviced object being the customer's pool/body of water and the visit's canonical content being water care (readings → treatment), cleaning, and equipment checks.

The trade's signature is water chemistry: readings captured per visit per body of water, dosing computed (increasingly automatically), chemical cost tracked at every grain, and readings/dosages shown to the customer as proof of service. But chemistry machinery is standard-not-definitional — the defining core is the four jointly-held structures, with trade semantics living inside the objects (pool with water/equipment context; visit with readings/treatment/cleaning content; route-organized recurring cadence; monthly-cadence recurring billing plus repair invoicing).

Two structural notes distinguish pool service from its chemical-application siblings: (1) its chemical records serve billing and customer proof, not regulator reporting — no regulatory layer is documented anywhere in the sample; (2) equipment is a first-class record whose state shapes the work (equipment-driven workflow), with its own maintenance cadences (filter/salt cell cleans). Seasonality is the trade's economic rhythm (openings/closings, off-season contraction) and manifests as a variant axis rather than structure.

The market realizes the Type in three product shapes: route-first all-in-one platforms (Skimmer), automation-heavy operations platforms for larger operators (Pool Brain), and seasonal/repair-first realists (POM) — plus generic FSM products used by small pool companies without trade depth (Kickserv pole).

L0 one-liner: the pool-service company's operator-side system of record whose defining core is the customer with serviced pool(s)/body of water + the pool service visit (recurring route stop or one-time job) as unit of work + the assigned technician + billing of the work, with water chemistry, equipment, and seasonality as trade semantics inside those objects.
