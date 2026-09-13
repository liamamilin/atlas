# Research Notes — Farm Management Platform

Research date: 2026-09-08

## Research Goal

Understand what a Farm Management Platform actually is as an Application Type: what the operator's world looks like inside it, what is recorded, how a season is run through the software, which structures are defining versus merely common in the current market, and where its boundary sits against the many capability-slice Types that surround it in the directory (Crop Management, Field Management, Agronomy Management, Precision Agriculture Platform, Livestock Management, Dairy Farm Management, Agribusiness ERP, Farm Equipment Telematics, Farm Labor Management, Harvest Management, Grain Management).

## Initial Boundary Hypothesis

- A Farm Management Platform is the farmer/operator-side system for running a whole farming operation — land, crops and/or livestock, inputs, work, and money — as one managed business over time (seasons/cycles).
- It is NOT: a single-capability tool (spray log only, weather only, accounting only), a machine/sensor data platform, or a corporate ERP for a large agribusiness company.
- Nearest confusions: (a) capability slices (crop management, livestock management); (b) precision-agriculture / remote-sensing / IoT platforms (data-source-centric); (c) Agribusiness ERP (corporate resource scale, supply chain); (d) farm accounting software (money slice).

## Research Questions

1. How is the farm itself modeled (land structure, enterprises, livestock)?
2. What are the "production subjects" being managed (crop seasons/plantings, herds/mobs/animals)?
3. What gets recorded, with what attributes (date, place, input, operator, equipment), and where does the record go?
4. How do plans/budgets relate to actual records (plan vs actual loop)?
5. What role does compliance/reporting play (spray records, withholding periods, audits, banks)?
6. Is the financial layer definitional or optional?
7. Is livestock coverage definitional, or can the Type be crop-only?
8. What surfaces do users actually work in (map, mobile, dashboard, reports)?
9. Who participates besides the farmer (agronomists, contractors, retailers, banks)?

## Representative Products

| Product | Segment / philosophy | Evidence depth |
|---|---|---|
| Agworld | Mid-size/mixed growers, US+AU; collaborative crop records; agronomist/retailer/contractor ecosystem; "farm management information system" framing | A — official product pages (Essentials, Activity Management, Reporting & Compliance), homepage |
| Bushel Farm (formerly FarmLogs) | US row-crop owner-operators; field records + economics + grain marketing; self-serve SaaS | B — official farmer product page only; knowledge base unreachable (see Source-access Limitation) |
| AgriWebb | Commercial sheep/cattle stations, Australia (help-center evidence: AU audit article, AU biosecurity) with Brazilian-language support observed; UK presence not verified from fetched sources; mobile-first digital record keeping; mob- and individual-animal management | A — official help center (multiple collections) |
| Farmbrite | Small diversified farms worldwide (125+ countries); all-in-one: crops + livestock + inventory + accounting + sales | A — official help center (full documentation tree + getting-started guide) |
| Agrivi | Enterprise farms + agri-food value chain; agronomic + economic decisioning; moved upmarket toward AI advisory and supply-chain products | B — official site + case-study quotes only |

Selection rationale: two crop-led poles (Agworld collaboration-first, Bushel Farm economics-first), one livestock-led pole (AgriWebb), one mixed whole-farm SMB pole (Farmbrite), one enterprise/value-chain pole (Agrivi). Covers market representation, different product philosophies, different customer tiers.

## Sources

- https://www.agworld.com/ (homepage; fetched 2026-09-08)
- https://www.agworld.com/products/essentials (fetched 2026-09-08)
- https://www.agworld.com/products/activity-management (fetched 2026-09-08)
- https://www.agworld.com/products/reporting-compliance (fetched 2026-09-08)
- https://www.bushelfarm.com/ (farmer product page; fetched 2026-09-08)
- https://support.bushelpowered.com/hc/en-us (Bushel knowledge base — FAILED: 1 transport error + 1 timeout; abandoned per network rule)
- https://help.agriwebb.com/ (help center root; fetched 2026-09-08)
- https://help.agriwebb.com/en/collections/804640-getting-started (fetched 2026-09-08)
- https://help.agriwebb.com/en/collections/3870477-paddock-records-and-grazing-management (fetched 2026-09-08)
- https://help.agriwebb.com/en/collections/3870481-livestock-feed-and-chemical-inventory (fetched 2026-09-08)
- https://www.farmbrite.com/ (fetched 2026-09-08)
- https://help.farmbrite.com/help/quick-start (full help-center TOC + getting-started; fetched 2026-09-08)
- https://www.agrivi.com/ (fetched 2026-09-08)

## Product Observations

### Agworld (Evidence layer A for product-page claims)

Official self-positioning: "Farm Management Software — Plan your crop, mitigate your risks, improve your profitability"; footer brand: "Farm Management Information System"; "a collaborative farm data ecosystem for growers, agronomists, and others involved in the farming process." Solutions sold separately to growers, agronomists, ag retailers, contractors.

Key observations (official product pages):

- **Essentials (records)**: "capturing all field activities, observations and records in one place… designed to replace notebooks, spreadsheets and disconnected systems." Records spray applications, fertilizer use, seeding, harvest, field observations (pests, weeds, diseases; notes, photos, map annotations). Tracks operators and machinery per job ("who completed each job and what equipment was used"). Data "stored in a standardized format", by field and season; cloud-based; works offline on phone/tablet/desktop; "access your data anywhere".
- **Compliance posture**: homepage — "all your records are in one central location, ensuring that you're audit-ready at all times"; standardized structured database so any report (e.g., "how many units of N you've applied this year") is answerable.
- **Activity Management**: "Turn crop plans into clear, trackable field activities." Crop plans and agronomic recommendations convert into work orders and field activities; assigned to team members or contractors; tracked as planned / underway / completed; completed in the field via mobile app (works offline); "Agworld can automatically convert them into detailed spray or fertilizer records"; "complete operational history… for every field and season." Case-study quote (Loza Farms): recommendations arrive from the agronomist in Agworld and go out to workers as work orders in the same app.
- **Planning / Budgeting**: field plans "from a simple rotation all the way up to detailed, field by field, production plans"; forecast product requirements; budget ahead; "compare your plans to actual costs in-season"; financial performance analyzed "by crop, farm and field" (cost-to-date per input category shown per field).
- **Reporting & Compliance**: instant reports (spray records, input usage, crop performance, seasonal activity); plan-vs-actual comparisons across fields/crops/seasons; export/share with advisors, partners, financial institutions; label-rate validation of recommendations/applications against product labels; "end-to-end traceability from planning through to execution and reporting"; organic-certification audit use case (OMRI input report).
- **Data stance**: "You own your data… we do not sell data"; multi-country deployments (US, AU, NZ, ZA, CA, UK, EU).
- Precision module exists (separate product page) — data-source layer on top of records.

Coverage shape: crop-centric core; case studies include livestock and dairy operations but product documentation observed is crop-focused.

### Bushel Farm (Evidence layer B — marketing page only; operational docs unreachable)

Official page (farmer side): "Bushel's farm management software gives you a ground-level and big-picture view of your farm's operational and financial performance"; explicitly "(formerly FarmLogs, Bushel Farm)".

- Field activity records ("fertilizing record" screenshot; "a faster, easier way to keep farm records").
- Field-level profitability: "easily calculate incomes and expenses… profitability and position" (per-acre expense summary screenshot).
- Cost of production: "combines your machine data with grain contracts and input costs, allowing you to instantly calculate your cost of production, track revenues, and easily see your profit and loss."
- Grain contracts tracked in one place, imported from 3,500+ grain and ag retail facilities on the Bushel Network (vendor network claim — B layer).
- Weather/rainfall per field: rainfall notifications, compare with past seasons; market-price alerts.
- Integrations: John Deere Operations Center, Climate FieldView (machine/field data platforms).
- Adjacent (same vendor, not the FMP core): Bushel Business Account — embedded banking/payments product; agribusiness-side suite (CRM, portals, trade) targets grain buyers, not farmers.
- Philosophy: records + economics + marketing for the row-crop owner-operator; automation of data entry from machine and network sources.

### AgriWebb (Evidence layer A — official help center)

Official help-center structure = the product's world:

- **Getting started / record keeping framing**: "Everything you need to get setup and start digital record keeping." Mobile app first (app + web app pair documented); dashboard; paddock & livestock summary; "Farm Diary (Beta) — AI powered farm diary to automatically create draft livestock records" (era-current).
- **Farm map / paddocks**: Mapping collection — "Add infrastructure and landmarks to your digital farm map"; draw paddocks on web + mobile; paddock prefixes/descriptions; connect paddocks with gates; feedlotting setup.
- **Livestock records**: Mob Management (herd-level records, 30 articles) vs Individual Animal Management (IAM, 58 articles; EIDs/VIDs; CSV import; "live sessions" — induct animals at the crush/chute side); edit/undo records; livestock list.
- **Paddock records & grazing**: paddock list; **paddock history** ("full paddock history"); paddock treatment (spray and fertilise); **paddock withholding period** ("What happens once you apply a treatment with a withholding period to a paddock?"); cultivation records; sowing record; harvest record ("store your harvest on or off farm"); grazing planning and feed budgeting (feed on offer / forage availability; stocking rate vs carrying capacity; rotational grazing planner; managing planned livestock movements; cell grazing); grazing reports (grazing chart, paddock grazing intensity, AE/LSU/DSE load by paddock); cropping reports (cultivation/sowing/harvest).
- **Inventory**: "Livestock, Feed and Chemical Inventory — manage treatments, vaccines, semen, embryo, feed, fertiliser and spray inventory and track cost of production"; feed inventory management + feed planner + purchase/sales + reconciliation/wastage/feeder-status reports; animal treatment inventory; paddock treatment inventory; **biosecurity plans**; **audit and compliance in Australia** ("easily prepare for your upcoming audit"); paddock cost of production and gross margin report; paddock treatment history report.
- **Farm calendar & team**: "Create tasks, rainfall records and notes from your farm calendar."
- **Reports**: 37-article collection — "extract insights into how your operation is performing."
- **Account management**: users, subscription and farm settings. Marketplace/integrations; Sustainability Program Hub ("unites producers, technical assistants, and sustainability teams").

Coverage shape: livestock-led (sheep/cattle) with real cropping/paddock records; strong regional compliance orientation (AU audit, biosecurity); mob-level vs individual-animal packaging is a subscription split.

### Farmbrite (Evidence layer A — official help center, full documentation tree)

Official framing: "Farm Management Software for your whole farm… all-in-one"; customers quote "manage multiple enterprises with one product… livestock (chickens, goats, sheep and pigs) and vegetable production… CSA and farmers markets"; "consolidated all the different farm ventures we are in — dairy, beef, hogs, poultry, hay and grain."

Documentation tree (structure = world model):

- **Fundamentals**: dashboard (weather, upcoming tasks, orders, transactions); quick-add; import/export; custom fields; notes; photos/files; keywords.
- **Schedule & Tasks**: calendar, recurring events, reminders; tasks with creation/assignment, templates/series, statuses, missed/skipped, checklists, time tracking, GPS geolocation, and — significant — "associate events with livestock or fields."
- **Livestock**: animal records (types, details, EID/RFID, bulk import); groups (smart groups by attribute); breeding (eligible sires/dams, pregnancy checks, births, offspring, genealogy, coefficient of inbreeding); feedings (from inventory, group feedings by weight, repeated feedings, average daily gain); health & wellness (treatments + treatment templates, **withdrawal dates**, body condition score, wellness score); grazing (grazing locations, manage grazing); yields (e.g., lay rate; yield to inventory); accounting per animal (cost tracking, bill of sale).
- **Crops**: crop types; grow locations (fields, beds; grow-location accounting); planning (season start date, crop plan, yield calculator, seed-order estimate); plantings (bulk, succession, growth stages, transplanting, completing); treatments & care (templates, **nutrients & soil samples**, watering/tilling, **withdrawal dates on plantings/fields**); harvests (expected harvests, harvest units, harvest to inventory, crop loss, **traceability from harvest to sale**, yield averages).
- **Resources**: equipment (usage records, maintenance schedules, service notifications, statuses, QR codes); warehouses/bins; inventory (items, categories, lots, recipes, usage for treatments/maintenance, low-inventory notifications, movement, history).
- **Accounting**: chart of accounts, transactions, bank connection/import, receipt scanning, split transactions, credit/refunds; **accounting for items** ("see accounting transactions for fields, plantings, animals and equipment" — costs attach to production subjects); cost analysis / breakeven; P&L; spending by category; cash flow; balance sheet; budgets.
- **Market**: products, orders (online store, POS orders, CSA memberships, wholesale, picking from inventory, invoices, refunds), traceability from harvest to sale.
- **Farm map**: map fields, beds, animal pens; record notes/logs and tasks from the map; map filters.
- **Climate**: forecasts, on-site gauges/weather stations, climate logs, history and mapping.
- **Reports**: "over 100 pre-built… farm specific reports"; accounting/livestock/planting/harvest/resource/order reports; **audit trail report**.
- **Account**: users, roles & permissions, teams, **multi-farm user permissions**, subaccounts, MFA. Mobile app with **offline use**. API + Zapier + webhooks.

Coverage shape: whole-farm breadth (crops + livestock + money + sales) at small-operation depth; financial layer unusually complete (full accounting) for this Type.

### Agrivi (Evidence layer B — marketing site + case-study quotes)

- "AGRIVI 360 Farm Management Software — data-driven tools and real-time insights from the field to make precise agronomic and economic decisions"; targets enterprise farms and agribusiness.
- Case-study quotes (official site): "AGRIVI pulls everything in and calculates the cost every time you use the fertilizer… insight into how much you are spending during your season" (season cost loop); "no tools to help us gather it all in one place and assess productivity and efficiency… no accountability at the farm level. This is where AGRIVI came in" (single record + accountability); "accessible on either phone, tablet, or computer and not needing to go through multiple notebooks… data is there in a few clicks" (records replace notebooks).
- Product family extends beyond the FMP: AI Engage (white-labeled WhatsApp/Viber AI agronomic advisor for input companies), Food Traceability (for food/retail), Agriculture Supply Chain, Connect (weather station/soil sensor/machine integration). These are value-chain products adjacent to the farm-management core.
- Operational feature-level documentation not fetched (site is marketing-oriented); assertions kept weak.

## Cross-product Comparison

| Dimension | Agworld | Bushel Farm | AgriWebb | Farmbrite | Agrivi |
|---|---|---|---|---|---|
| Farm structure object | farms, fields, seasons (field-by-field plans) | fields per operation | farm map → paddocks (+ gates, infrastructure) | farms (multi-farm accounts) → fields/beds, animal pens | farms/fields (B) |
| Production subject | crop season on field | crops per field (+ grain position) | mobs / individual animals; paddock crops (sow→harvest) | plantings (crop) + animals/herds (livestock) | crops per season (B) |
| Record types observed | spray, fertilizer, seeding, harvest, observations (pest/weed/disease, photos, map notes) | field activities (fertilizing etc.) | treatments (animal + paddock), cultivation, sowing, harvest, grazing movements, rainfall, tasks | treatments, feedings, plantings, watering/tilling, harvests, grazing, equipment usage, climate logs | activities/inputs (B) |
| Record attribution | operator + machinery per job | automated from machine data (B) | user-entered, edit/undo trail, live sessions | per-record user; audit trail report | user-entered (B) |
| Mobile + offline | yes (A) | mobile app (B) | mobile-first (A) | mobile app with offline mode (A) | phone/tablet (B) |
| Plan vs actual / budget | plans → recommendations → activities; budget vs actual costs | cost of production, per-acre profitability | feed budgeting; stocking rate vs carrying capacity; cost of production reports | budgets, breakeven/cost analysis, accounting per subject | season cost tracking (B) |
| Input inventory | product-requirements forecast (A) | input costs (B) | treatments/vaccines/feed/fertiliser/spray/semen/embryo inventory with drawdown | inventory with lots, usage drawdown for treatments/feed | inputs (B) |
| Compliance / audit | audit-ready records; label-rate validation; organic audit use case | — (not observed) | withholding periods; AU audit prep; biosecurity plans | withdrawal dates; audit trail; traceability harvest-to-sale | traceability product (separate) |
| Financial layer | budgets + financial performance by field/crop (no full ledger observed) | P&L, cost of production, revenue tracking (B) | cost of production & gross margin reports | full accounting (chart of accounts, P&L, balance sheet) | season costs (B) |
| Multi-party participation | growers + agronomists + retailers + contractors (sold as separate solution faces) | farmer + Bushel Network (grain buyers) | producers + technical assistants (sustainability hub) | contacts, customers (direct-market) | value-chain partners (B) |
| Sales/commerce | — | grain contracts + marketing position | feed purchase/sales records | online store, POS, CSA, wholesale | — |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (deliberately minimal)

A Farm Management Platform is the operator-side system of record for a farming operation, holding three jointly-dependent structures:

1. **The farming operation as the managed entity of record** — the operator's whole operation held as a persistent structured unit: its land organization (farms → fields/paddocks/beds) and, where present, its livestock holding, plus the standing resources of the operation. The operator (owner/farm manager) is the system's principal user. *Remove → property/inventory tools or single-function apps; the "whole operation" scope is what separates the Type from capability slices.*
2. **Production subjects managed across their production cycle** — the operation's crops/plantings (a season from planning through growth to harvest) and/or herds/mobs/animals (through breeding, feeding, treatment, sale) held as managed subjects whose state is tracked over time. *Remove → a static farm map/register with nothing being run.*
3. **The operational record loop** — planned and completed work, input use, and observations captured as dated, attributed, location-bound entries against the subjects and structure, accumulating into a queryable operational history that feeds reporting (compliance and business). *Remove → a planner or spreadsheet with no running record; the "management" disappears.*

Jointly-held is load-bearing:

- 1 alone = a digital farm map / asset register.
- 2 alone = the capability slices (Crop Management / Livestock Management) scoped to one subject class.
- 3 alone = a generic notes/task tool with farm-flavored templates.
- 1+2 without 3 = farm structure + plans with no history (planning worksheet).
- 1+3 without 2 = record-keeping surface with no managed production.
- 2+3 without 1 = slice territory again — records about crops or animals, not about an operation.

### Historical / Market-Sample Check (§24)

- **Paper-era pre-history**: the farm record book — field register + field-by-field entries of operations, inputs, and yields; herd books; the farm account book; the diary. Satisfies all three legs (structure, subjects, record loop); the software Type digitizes exactly this. Nothing in the core requires cloud, GPS, sensors, or AI.
- **Early desktop era (1990s–2000s)**: farm record/accounting programs holding field/crop records and accounts satisfy the core.
- **Regional/regulatory forms**: Australian audit/biosecurity-driven livestock record keeping (AgriWebb) and EU-style compliance-driven record keeping satisfy the core without any specific regulation being definitional.
- Modern capabilities (machine-data integrations, satellite imagery, AI drafting, embedded banking) are era-current layers, correctly excluded from the core.

### L1 — Common Mature Structure (standard in current market, not definitional)

- Season/crop plans and budgets compared against actual records (plan vs actual).
- Input/inventory tracking with drawdown when used (feed, fertilizer, chemicals, seed) and purchase records.
- Task/work management with assignment to workers; scheduling/calendar; rainfall/weather records.
- Structured reporting: spray/application histories, input usage, production per field/paddock, cost of production, gross margin, audit/compliance exports.
- Mobile capture (commonly offline-capable) as the primary recording surface, with the map as an organizing/browsing surface.
- Multi-user accounts with roles/permissions; data ownership/export.
- Machinery/equipment records (usage, maintenance) and integrations with machine-data platforms (John Deere Operations Center / Climate FieldView-class).
- Financial-performance views (per-field/per-enterprise costs and returns). Note: full double-entry accounting is NOT at this level — see L2.

### L2 — Variant / Optional Structure

- Enterprise coverage mix: crop-led (Agworld, Bushel Farm), livestock-led (AgriWebb), mixed whole-farm (Farmbrite) — the Type spans the crop/livestock divide; a given product commonly leads with one.
- Full farm accounting (chart of accounts, bank feeds, P&L, balance sheet) vs financial views/reports only.
- Livestock granularity: mob/herd-level records vs individual-animal (EID) management (AgriWebb sells these as separate subscription tiers).
- Direct-market sales layer (online store, POS, CSA memberships) for small diversified farms (Farmbrite).
- Grain-marketing position tracking and contracts (Bushel Farm).
- Advisory-collaboration networks where agronomists/retailers/contractors are platform participants with their own solution faces (Agworld) vs single-farm accounts.
- Embedded banking/payments (Bushel Business Account) — adjacent, vendor-specific but packaged inside a farm app.
- Sustainability/carbon program participation (AgriWebb Sustainability Hub).
- AI assistance: draft records from voice/diary (AgriWebb Farm Diary), AI advisory (Agrivi AI Engage) — era-current.

### L3 — Vendor-specific (Research Notes only)

- Agworld: recommendation → work order → auto spray-record pipeline; label-rate validation; OMRI organic input report; sold as separate solution faces to agronomists/retailers/contractors; "Farm Management Information System" branding.
- Bushel Farm: Bushel Network grain-contract import from 3,500+ facilities; embedded FDIC-insured business account with debit card; agribusiness-side twin suite (CRM/portals/trade) sold to grain buyers.
- AgriWebb: mob vs IAM subscription split; live sessions at the crush; rotational grazing planner with planned livestock movements; AE/LSU/DSE load reports; feed trough/feeder status; AU audit & biosecurity content.
- Farmbrite: coefficient of inbreeding; wellness score; succession plantings; CSA membership products; subaccounts; multi-farm user permissions.
- Agrivi: white-label WhatsApp/Viber AI advisor for input manufacturers; food traceability and supply-chain products.

## Boundary Findings

- **vs Crop Management / Agronomy Management / Field Management** (directory siblings): those center a single subject class (the crop's agronomy, the field's lifecycle). Remove the whole-operation scope (multiple enterprises, resources, the operation as the unit) and a Farm Management Platform collapses into them. Confirmed from this side: crop-only sampled products (Agworld, Bushel Farm) still structure everything around the operation (farms, fields, inputs, labor, money, reporting), with crop management as one workspace.
- **vs Livestock Management / Dairy Farm Management**: same seam on the livestock side. A livestock-led FMP (AgriWebb) still holds paddocks, feed and chemical inventory, task calendar, reporting — the operation, not the animal, is the organizing frame.
- **vs Precision Agriculture Platform / Crop Remote Sensing Platform / Agricultural IoT Platform**: those are data-source-centric (sensors, satellite, machinery telemetry; the data layer is the product). In sampled FMPs, machine/sensor data arrives as optional integrations (Bushel Farm ↔ John Deere Operations Center/Climate FieldView; Agrivi Connect; Agworld Precision module) layered on the record core. Remove the record loop and keep sensors → those Types.
- **vs Agribusiness ERP**: ERP serves an agribusiness company's corporate resources (procurement, supply chain, finance at company scale); FMP serves the farming operation's own running record. Bushel illustrates the seam from one vendor: the farmer app vs the agribusiness suite are separate products.
- **vs Farm Equipment Telematics / Farm Labor Management / Harvest Management / Grain Management**: capability slices (machines, labor, post-harvest, grain) that FMPs commonly integrate or lightly cover; none of them carries the operation's whole record.
- **"去掉什么就变成另一个 Type"判据**：去掉 whole-operation scope → Crop/Livestock Management；去掉 record loop → farm map/plan worksheet；去掉 production subjects → generic task/notes tool；把数据源（传感器/卫星）放在中心 → Precision Agriculture / Remote Sensing。

## Uncertainties

- Bushel Farm operational documentation unreachable (2 failed fetches); its economics/marketing emphasis and integration behavior are marketing-page claims only (B). No precise workflow claims made for it.
- Agrivi's current farm-management feature set observed only at marketing depth (B); product family has moved upmarket (AI advisory, supply chain), so treating it as an enterprise-flavored FMP is an inference, kept weak.
- Whether Agworld supports livestock workflows in-product is unclear from observed pages (case studies include livestock customers); treated as variant coverage, not evidence about the Type.
- Subscription packaging (which capabilities sit in which tier) varies and was not systematically researched; no tier-level claims made.
- Full accounting within an FMP: Farmbrite proves the pole exists; other sampled products show reports-level finance only. Held as variant, not core.

## Final Synthesis

A Farm Management Platform is the farmer/operator's whole-operation system of record: it holds the operation's structure (land and livestock), manages its production subjects (crop seasons and/or herds/animals) across their cycles, and keeps the running, attributed record of planned and actual work, inputs, observations and outputs — a record kept structured enough to report for compliance and to steer the business (plan vs actual, cost of production). Everything else commonly seen — machine-data integration, satellite imagery, inventory depth, full accounting, direct-market sales, advisory networks, AI drafting — is market-era structure layered on that core. The Type's identity lives in the joint presence of operation-scope + managed subjects + record loop; removing any one collapses it into a neighbor (farm map, capability slice, or generic records tool).
