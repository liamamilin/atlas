# Research Notes — Shop Floor Management

## Research Goal

Determine what "Shop Floor Management" is as a distinct Application Type: what objects and structures define it, who uses it, how the floor's day is actually managed through it, and where its boundaries lie against the dense §16 cluster — Manufacturing Execution System / MES, Factory Operations Management, OEE Management Platform, Production Planning / APS, Manufacturing ERP — plus generic task management / meeting tooling.

This pass also inherits four pre-hung forward flags that explicitly defer to it:

- factory-operations-management (processed 2026-09-08): JOINT REVIEW — "the event-and-response leg is shared territory (dispatch/andon/visual management); this leaf's delta = the live production-operations picture + the operational performance record". That pass framed this leaf's center as "the floor's daily management system (issues, visual management, escalation)".
- manufacturing-execution-system-mes (processed 2026-09-09): "shop-floor-management pass should ratify the event-response vs order-execution seam".
- production-planning (processed 2026-09-09): "shop-floor-management pass should confirm the plan-pipeline vs event-response seam from its side".
- manufacturing-erp (processed 2026-09-09): "shop-floor-management pass should confirm the execution-recording seam".

## Initial Boundary

Working hypothesis before research: "shop floor management" is a polysemic label. Candidate readings:

1. **Lean daily management (SFM as a named practice)** — tiered meetings, SQCDP-class visual boards, escalation, leader standard work, gemba walks; a distinct software family exists for this.
2. **Shop-floor execution/dispatch** — the MRP-II "shop floor control" lineage: dispatch lists, labor/production reporting, abnormality management; products doing this self-label "shop floor execution" (L2L) or MES (ShopVue) — likely Factory Operations Management / MES territory, not this leaf.
3. **Label-only usage** — the phrase attached to unrelated page names or benefit copy (Tulip's station-administration page).

Nearest neighbors if reading 1 holds: FOM (live production state + event-response + performance record), MES (order execution + as-built), OEE platform (effectiveness measure), Production Planning/APS (schedule generation), generic work management (tasks/meetings without floor binding).

## Research Questions

1. What objects does a shop-floor-management product hold? (boards, meetings, issues, actions, routines?)
2. Who uses it — operators, supervisors, managers, support functions?
3. What is the recurring loop — what happens daily/weekly, in what structure?
4. Does the product own production orders, machine state, or the as-built record? (expected: no)
5. Where does the escalation run — to functions (maintenance/quality) or through management tiers?
6. Where does the performance content on the boards come from (entry, integrations, connectivity)?
7. Is the practice manufacturing-exclusive? (Tervene serves healthcare — check breadth)
8. What is the paper-era ancestor — does the definition survive the historical check?

## Representative Products

| Product | Role in sample | Posture | Customer tier |
|---|---|---|---|
| Tervene | in-type, explicit "Shop Floor Management System (SFM)" self-label | routine/form-first daily-management suite | mid-market to global manufacturers; also healthcare/nursing homes |
| iObeya | in-type, second management-side pole | visual-canvas-first (digital Obeya rooms), enterprise OpEx platform | large enterprises (pharma, aerospace, automotive, energy) |
| L2L (Shop Floor Execution) | boundary pole — execution/dispatch self-label | connected operations platform | mid-size to enterprise plants |
| ShopVue (CAI Software) | boundary pole — MES self-label | discrete-manufacturing MES | mid-size discrete manufacturers |
| Tulip | label-only usage | composable frontline operations platform | enterprise plants |

Selection rationale: two in-type products with different product philosophies (routine-first vs canvas-first) and tiers; three boundary products spanning the execution neighborhood to ratify the seams the sibling passes deferred.

## Sources

Research date: 2026-09-09. All fetches via WebFetch (markdown).

**Reached (Tier 1/2):**

- Tervene — home: https://tervene.com/
- Tervene — "Digital Shop Floor Management Software": https://tervene.com/solution/shop-floor-management-software/
- iObeya — home (incl. Lean Manufacturing use case copy, FAQ, customer reviews): https://www.iobeya.com/
- L2L — "Shop Floor Execution": https://www.l2l.com/platform/shop-floor-execution
- ShopVue — "ShopVue MES Software" product page: https://caisoft.com/products/shopvue-mes/ (reached via https://www.shopvue.com/ redirect)
- Tulip — "Shop floor management" support doc: https://support.tulip.co/docs/shop-floor-management

**Unreachable (per source-abandonment rule):**

- Factory Operating System (fos) — https://www.factory-operating-system.com/ and https://factory-operating-system.com/ — transport error ×2. Third management-side sample missing; market-breadth claims calibrated accordingly.
- Katana Shop Floor App — https://katanamrp.com/shop-floor-app/ and https://www.katanamrp.com/shop-floor-app/ — 404 ×2; https://help.katanamrp.com/ — transport error ×1. Small-shop execution pole not directly evidenced; covered structurally via ShopVue/L2L.

**Also consulted (prior passes, same environment):** research/factory-operations-management.md, research/manufacturing-execution-system-mes.md, research/oee-management-platform.md, research/production-planning.md, research/manufacturing-erp.md, research/advanced-planning-scheduling-aps.md (sibling seam framings; Tulip "A Tour of the shop floor" and L2L platform/production pages were fetched by those passes).

---

## Product Observations

### Tervene — "Digital Shop Floor Management Software" (evidence layer A)

Positioning: "Tervene helps you implement a successful **Shop Floor Management System (SFM)**"; "Equip managers and supervisors with SFM tools to consistently meet performance targets." The software is explicitly for **frontline managers and operational leaders** ("the must-have software for frontline managers and operational leaders").

SFM tool inventory (the page's own enumeration):

- **Leader Standard Work** — "Standardize managers' schedules with daily, weekly, and monthly routines"; "Manage schedules for recurring tasks, including daily checks, data logs, audits, LPAs, team meetings, shift handovers, and performance reviews"; reminders for standard-work adherence.
- **Daily Routines** — "Structure daily routines for every supervisor."
- **Gemba Walks** — "Define Gemba Walk checklists to identify issues, capture photos, and spot improvement opportunities"; structured manager walkthroughs; identify deviations early.
- **Rounds & Inspections** — "digital checklists for safety, equipment, quality, and maintenance checks."
- **5S Audits / Audits and Inspections** — tailored forms, scheduled in calendars, answers can require photos/notes/corrective actions, audit reports.
- **Huddles & Meetings** — "Run more efficient meetings with predefined agendas, structured discussions, and action tracking."
- **Tiered Meetings** — "Standardize information flow to **escalate issues** and make decisions at the right management level"; "a series of meetings structured by tiers (**Tier 1, Tier 2, Tier 3**)"; "Establish an escalation process to quickly address issues and make decisions at the right organizational level."
- **Shift Handovers** — "Share critical information between shifts."
- **Problem-Solving** — "Use structured issue management to document, categorize, prioritize, and track problems"; "Document issues thoroughly, then **escalate and notify** the right person"; "Create **corrective and preventive actions** with priority levels, comments, and due dates."
- **Action Tracking** — "Assign and track corrective and preventive actions across departments, ensuring clear responsibilities and deadlines."
- **Continuous Improvement** — "Capture ideas and track continuous improvement projects"; kaizen culture.
- **Visual Management** — "Build custom SFM dashboards to track KPI, monitor management processes, and make data-driven decisions"; "track **key metrics like Safety, Quality, Cost, Delivery, and People**" (SQCDP); "Gain insight into your **team's management behaviors** and support leadership development."

Goal statements (three value props): visibility on frontline operations and performance metrics; standardize management practices on the shop floor; structure problem-solving and accelerate issue resolution ("Shift from reactive firefighting to proactive management").

Customer evidence: Safran Cabin ("structure the flow of information... structure our Gemba Walks"), TOMRA ("evaluate issues and track corrective actions on the floor"), Siemens Haguenau ("What was once handwritten on paper or sent via email is now structured. Every department now knows what's been resolved and what hasn't"), Hason Steel ("structure the cascade of information between the different levels of management").

Imagery: "Two men review a **SQCDP board** in a factory" — the paper board is the explicit before-state of the digitized practice.

Scope: serves "Industrial and Manufacturing" AND "Healthcare and Nursing Homes" — the practice is portable beyond factories.

What is NOT present anywhere in the product framing: production-order execution, machine state/connectivity, OEE computation (OEE appears only inside a customer testimonial), as-built records, routings/BOMs, schedules generated in-product.

### iObeya — Digital Obeya Platform (evidence layer A)

Positioning: "Digital Obeya Platform™ for Operational Excellence at Scale". The Obeya: "a 'big room' where strategy comes to life... It began as a physical space in Lean practices, and today physical and digital rooms blend together." "The Obeya has evolved from **paper walls** to a connected digital space."

Lean Manufacturing use case (the shop-floor-facing one): "Digitize your **SQCDP system** to give every shift and site real-time visibility, **faster problem-solving**, and **one connected rhythm of performance**." And: "Through **Visual Management**, goals and KPIs become visible so everyone stays aligned, reacts fast, and **improves daily**. This shared understanding builds trust, accelerates decisions and powers a **Daily Management System** that drives Lean success **across every tier**."

Structural elements: Network of Obeya Rooms ("digital spaces that mirror your organizational structure... expand seamlessly to hundreds or thousands of rooms"); Obeya Control Tower™ (live KPIs); "work like paper" board experience.

Customer review evidence (independent of marketing): "I like the possibility of **escalation and deescalation of actions**... The **hierarchical structure can be nicely rebuilt** with this tool and **all meetings can be held in iObeya**" (Performance Engineer); "monitoring KPIs, identifying gaps through visual management, and **formalizing and tracking actions**" (CI Project Manager); "an industrial company... we have Lean, Agile, **Shop floor** and Project Management in our DNA" (industrial customer).

Data posture: integrations page names Power BI (QCD), TrakSYS (an MES), Poka, SAP — production data is **consumed from neighboring systems**, not produced by machine connectivity at the center.

Scope: manufacturing, engineering, "financial services, and government" (FAQ); "Whether you're digitizing SQCDP boards, aligning portfolios, or scaling Agile delivery..." — SFM practice is one use case of a broader visual OpEx platform.

What is NOT present: order execution, machine-state management, as-built records.

### L2L — Shop Floor Execution (evidence layer A; boundary pole)

Positioning: "Your shop floor, but running the same way every shift. **Every abnormality caught, every response standardized.**" Three pillars: close the execution gap (plan vs floor); make the right way the only way (standard work to the frontline); catch and fix problems fast.

Features: shift priorities ("the most important priorities for each shift at a glance"); **real-time dispatch** ("Automatically assign and track tasks based on machine alerts"); **abnormality management** ("Give operators a seamless way to report machine, quality, or safety hiccups. These alerts are instantly routed and tracked through to resolution"); visual work instructions & SOPs at the point of work; digital checklists; root cause analysis + "permanent corrective actions"; best-practice sharing (Yokoten); downtime/OEE dashboards; notifications; integrations.

Self-definition (FAQ, verbatim): "What is shop floor execution software? A digital system that **translates shift plans into standardized, trackable actions for frontline workers**... You could see it as a **combination of MES + connected worker + CMMS**." "Does L2L replace our ERP? No. L2L complements ERP by handling the '**last mile' of execution on the floor**... pulls plans down from the ERP and pushes real-time results back up."

Reading: this is the **execution/dispatch** family — operator work queues, machine-alert-driven tasks, function-routed abnormalities (maintenance work orders). The management-routine structure (tiered meetings, SQCDP boards, leader routines) is absent from the module's own framing. The prior FOM pass correctly placed L2L in FOM's sample.

### ShopVue MES (CAI Software) (evidence layer A; boundary pole)

Positioning: "ShopVue is a Manufacturing Execution System (MES)... trusted by manufacturers for nearly 30 years... to make **shop floor management** simpler, smoother, and more efficient." — "shop floor management" appears as a **benefit phrase**, the product self-labels MES.

Features: Shop Activity & Labor (barcode-scanned travelers, direct/indirect labor, quantities per operation, scrap reason codes, WIP status continuously updated in ERP); Time & Attendance; **Paperless Factory Dispatch** ("Operators can see a sequenced list of Orders, Lots, or Serials to work on... When the Operator completes the operation, ShopVue automatically dispatches the Order to the next step in routing"); Direct Machine Interface (OPC UA polling, OEE/Utilization/Efficiency); Production Traceability (lot/serial genealogy); Digital Instructions (sub-operations, sign-offs); Analytics (OTD, OLE, OEE, WIP).

Reading: the classic **shop-floor-control/MES** structure — order dispatch against routings, labor and quantity reporting, as-built genealogy. No tiered meetings, no SQCDP board routine, no escalation-of-issues machinery as the center. Corroborates the MES pass's "market label noise" note: shop-floor language attaches to MES products.

### Tulip — "Shop floor management" support doc (evidence layer A; label-only usage)

The page titled "Shop floor management" documents **administering the shop floor's connected estate**: Stations ("digital representations of physical workspaces"), Interfaces (display devices running the Tulip Player), Machines, Edge devices, Vision, and per-workspace numeric limits (e.g., 10,000 stations per workspace — vendor detail, kept here only). It is a system-building/administration surface, not a daily-management practice.

Reading: vendor-specific page naming — evidence of label polysemy, not Type structure. (The FOM pass already used Tulip's operator-app and shop-floor tour docs for the FOM sample.)

---

## Cross-product Comparison

| Dimension | Tervene | iObeya | L2L (execution) | ShopVue (MES) | Tulip (label-only) |
|---|---|---|---|---|---|
| SQCDP-class performance boards | ✓ ("dashboards to track KPIs — Safety, Quality, Cost, Delivery, People"; SQCDP imagery) | ✓ ("Digitize your SQCDP system"; QCD via Power BI) | dashboards (downtime/OEE) — analysis, not the reviewed board routine | KPI analytics (OEE/OTD/WIP) | — |
| Tiered recurring meetings | ✓ explicit (Tier 1/2/3, huddles, agendas) | ✓ explicit (tiered Obeya rooms, "all meetings can be held in iObeya", "across every tier") | — | — | — |
| Issue capture → escalation → actions to closure | ✓ explicit (document/categorize/prioritize; escalate & notify; CAPA with owners and due dates) | ✓ explicit (escalation/deescalation of actions; formalizing and tracking actions) | ✓ (abnormality routing, resolution tracking — to **functions**) | limited (Call/Response, MRB) | — |
| Leader routines (LSW/gemba/audits) | ✓ deep (LSW, gemba walks, rounds, 5S, LPAs) | ✓ via room routines/boards (meeting-led) | — | — | — |
| Order execution at operation grain | — | — | ✓ (task dispatch, machine-alert tasks) | ✓ (dispatch list, routing steps) | — |
| Machine state / connectivity | — | — | ✓ (machine alerts) | ✓ (OPC UA DMI) | ✓ (as platform substrate) |
| As-built record / genealogy | — | — | — | ✓ | — |
| Self-label | "Shop Floor Management System (SFM)" software | Obeya / Operational Excellence / Daily Management System | "shop floor execution" (MES + connected worker + CMMS) | MES | (page name only) |

**Cross-product commonality (evidence layer B):**

- **SQCDP-class visual performance boards + tiered recurring meetings + issue-to-action escalation** appear together in both management-side products (Tervene, iObeya) — this trio is the stable center of the software family that actually carries the "Shop Floor Management" label as a named system.
- The **execution/dispatch** structure (work queues, machine-alert tasks, function-routed abnormalities) belongs to the products that *avoid* the "shop floor management" self-label (L2L: "shop floor execution"; ShopVue: MES) — the market itself splits the label.
- Both management-side products are **data consumers** from production systems (integrations to MES/ERP/BI named by iObeya; KPI boards fed by entry/integration at Tervene), not producers of machine state or as-built records.
- Both management-side products bind the routine to **management behavior** (Tervene: "gain insight into your team's management behaviors"; iObeya: rooms mirroring organizational structure) — the managed subject is the management system of the floor, not the machines or the orders.

**Canonical inference (evidence layer C):** The Type can be modeled as the **shop floor's daily management system**: a managed performance picture (boards), a recurring tiered review rhythm, and an issue→escalation→action loop — jointly held. This is deliberately more abstract than any vendor's module list and matches every seam the sibling passes pre-drew.

## L0 / L1 / L2 / L3 Abstraction

### L0 — Defining Invariant (minimal; three jointly-held structures)

1. **The floor's performance picture as managed board content** — the shop floor's key performance indicators (SQCDP-class: safety, quality, cost, delivery, people; vocabulary varies) held on a persistent visual board surface that the management team reviews. Not a computed analytics engine — a managed, review-facing picture. Remove → a KPI dashboard / monitoring tool (OEE platform territory).
2. **The recurring tiered management rhythm** — structured, recurring meetings/huddles organized by management level (team/department/site — "Tier 1/2/3" at Tervene, tiered Obeya rooms at iObeya) in which the boards are reviewed, priorities aligned, and decisions made at the right level. Remove → generic meeting scheduling / a static plan.
3. **The issue-to-action escalation loop** — problems surfaced on the floor (from walks, checks, audits, meetings) are documented, escalated to the management level that can resolve them, converted into assigned actions with owners and deadlines, and tracked to closure. Remove → a passive dashboard or a bare meeting tool.

Jointly-held load-bearing analysis:

- 1 alone = KPI dashboard (monitoring)
- 2 alone = meeting scheduler
- 3 alone = generic task/issue tracker (CAPA tooling)
- 1+2 without 3 = performance review theater — boards reviewed with no consequence machinery
- 1+3 without 2 = an issue tracker with KPI tiles and no management routine
- 2+3 without 1 = generic work management (meetings + tasks), no floor binding

Domain binding: the picture, the rhythm, and the issues belong to a **shop floor / production front line** — remove the domain binding and only generic work-management remains.

### L1 — Common Mature Structure (present in mature products, not definitional)

- Leader standard work / standardized manager routines (daily/weekly/monthly cadences, reminders, adherence)
- Gemba walks and structured manager walkthroughs with checklists and photo capture
- Audits, rounds, 5S, layered process audits with corrective-action triggers
- Shift handovers as structured information exchange
- Structured problem-solving methods (categorization, prioritization, CAPA-style actions)
- Continuous improvement / idea / kaizen tracking
- Management-process analytics (action closure, meeting adherence, issue trends)
- Mobile capture (phones/tablets at the gemba)
- Multi-site rollup and standardization across plants
- Integrations feeding board content from production systems (MES/ERP/BI)

### L2 — Variant / Optional Structure

- Domain extension beyond manufacturing (Tervene: healthcare and nursing homes; iObeya: financial services, government) — the routine is domain-portable
- Board vocabulary (SQCDP / SQDCME / QCDSM-class variants; tier counts and naming differ by organization)
- Product philosophy axis: routine/form-first (Tervene) vs visual-canvas-first (iObeya)
- Scale axis: site-level daily management vs enterprise OpEx room networks
- Cloud SaaS deployment; language localization for multi-site rollups

### L3 — Vendor-specific (research notes only)

- Tervene: solution taxonomy (LSW / DMS / Visual Management / Gemba Walk app / meetings-communication pages), "DMS 2.0" naming, implementation/coaching services packaging
- iObeya: Obeya Control Tower™, room-based licensing, "work like paper", per-room scaling story
- L2L: Dispatch/abnormality module naming, Execution AI, Yokoten feature naming, FAQ self-composition ("MES + connected worker + CMMS")
- ShopVue: module names (Shop Activity & Labor, Paperless Factory Dispatch, Direct Machine Interface), OPC UA polling cadence
- Tulip: station/interface/machine administration limits (10,000 stations per workspace etc.)

## Vendor-specific / Rejected Findings

- **"Shop Floor Management = shop-floor execution/dispatch of production work"** — REJECTED as the defining center. The products that do this self-label "shop floor execution" (L2L) or "MES" (ShopVue); their defining structures (order execution, as-built, function-routed abnormalities) are already owned by the MES and FOM Types. The overlap is label noise, documented as such.
- **"Shop Floor Management = station/device administration"** — REJECTED (Tulip's page naming is a vendor-specific sense).
- **"SFM requires machine connectivity / OEE computation"** — REJECTED: neither management-side product centers connectivity or computes effectiveness; OEE appears as board content or customer-testimonial language.
- **"SFM is only a methodology, with no software structure of its own"** — REJECTED: the software family carries a distinct object model (boards, tiers, issues, actions, routines) that generic task/meeting tools lack.
- **"SFM = andon"** — REJECTED as an equation: andon/event-response is FOM/MES-family territory per the sibling passes; SFM's escalation runs through **management tiers**, not function dispatch queues. Where an SFM routine triggers function response, that is the interface to FOM-class machinery, not SFM's defining structure.
- Vendor marketing metrics (30% performance boost, 35% decision acceleration, 50% meeting-time reduction, 96% issue resolution) — excluded from the Type definition; they are customer-outcome claims, not structural facts.

## Boundary Findings

1. **vs Manufacturing Execution System / MES** — RATIFIED from this side (discharges the MES pass's forward flag). MES = released production orders executed at operation/step grain + execution bound to the defined process + the as-built unit/lot record. SFM = the floor's daily management loop; no order execution, no genealogy, no process enforcement. Fresh seam evidence: the execution-dispatch products themselves avoid the SFM label (L2L: "combination of MES + connected worker + CMMS"; ShopVue: "MES... make shop floor management simpler" — benefit phrasing over an MES core). A product can hold an as-built record with no tiered routine (MES); a product can hold the routine with no as-built record (Tervene, iObeya).
2. **vs Factory Operations Management** — RATIFIED (discharges the FOM pass's joint-review flag, using that pass's own pre-drawn seam). FOM = live production-operations picture (machine/line/order state) + event-and-response to functions + operational performance record. SFM = the management routine over the floor: the boards are **reviewed content** rather than a live operations state; escalation runs **up management tiers** rather than out to response functions; the managed subject is the management system (behaviors, routines, actions) rather than the running operation. FOM-class systems are natural data sources for SFM boards (iObeya integrates TrakSYS/Power BI/Poka; Tervene boards consume KPIs). The event-and-response loop is shared territory exactly as the FOM pass recorded — the increments on each side are the differentiators.
3. **vs Production Planning / APS** — CONFIRMED from this side (discharges the production-planning pass's forward flag). The plan pipeline (requirements explosion → firmed orders → release, or finite-capacity scheduling) is upstream; SFM consumes "today's plan/targets" as board content. No schedule generation, no order placement machinery, no capacity model in the SFM core. Matches that pass's row: "production planning feeds the floor its schedule but does not manage the floor's running state."
4. **vs Manufacturing ERP** — CONFIRMED (discharges the manufacturing-erp pass's execution-recording flag). No business-grain recording: SFM actions are management items (issues, corrective/preventive actions, improvement actions), not inventory issues, capacity entries, or WIP postings. The ERP's shop-floor recording (journals, tablets, kiosks) is execution-side machinery, adjacent but different.
5. **vs OEE Management Platform** — held consistent with that pass's row ("visual/issue management at the point of work; can exist with no computed effectiveness score"): OEE platforms center the effectiveness measure + loss attribution + improvement loop; SFM centers the routine. An OEE score can appear on an SFM board as content; the SFM routine can exist with no computed score.
6. **vs APS** — schedule generation across the horizon vs day-of management (matches the APS pass's row "day-of work execution, reporting and visual management on the floor; the APS owns the schedule across the horizon above it").
7. **vs generic work management (Task Management Application, Work Management Platform, Digital Whiteboard)** — the floor-performance binding (SQCDP-class board content, tier structure, gemba/audit routines, shop-floor domain) is the differentiator. iObeya is visually canvas-like and could be mistaken for a whiteboard; its center is the tiered management system (rooms mirroring the organization, escalation semantics, SQCDP), not freeform collaboration. Keep-both; no directory change. This is the SFM↔generic-tooling seam and is the leaf's main exposure to re-classification pressure — recorded here for the taxonomy owner.
8. **Label-noise note for the taxonomy pass** — the phrase "shop floor" is used by at least three neighboring families: "shop floor execution" (L2L, FOM family), "shop floor management" as MES benefit copy (ShopVue), and "Shop floor management" as a station-administration page name (Tulip). The **named-practice** market ("Shop Floor Management System (SFM)") — where the exact leaf label is the product's own category name — is the daily-management family documented here.

## Uncertainties

- **Sample breadth on the management side**: two in-type products reached (Tervene, iObeya). The third natural candidate (Factory Operating System) was unreachable (transport error ×2); other candidates in this niche are small or marketing-heavy with weak documentation. Cross-product claims rest on two independent confirmations; calibrated wording used accordingly.
- **Execution-side small-shop pole** (Katana Shop Floor App) unreachable (404 ×2, help-center transport error ×1) — the execution boundary rests on L2L + ShopVue, both enterprise/mid-market; a small-shop execution pole might blur differently, unverified.
- **Whether any SFM product ships its own live machine-state layer** — none observed in-sample; the data-consumer posture (integrations) is documented at iObeya and implied at Tervene, but a connectivity-equipped SFM product may exist. Held as uncertainty, not asserted either way.
- **Tier-depth conventions** — "Tier 1/2/3" named at Tervene; deeper/wider tier structures likely at enterprise scale (iObeya's "hundreds or thousands of rooms") but no universal standard asserted.
- **iObeya's SFM depth** — evidence from home page, Lean Manufacturing use-case copy, FAQ, and customer reviews; the dedicated use-case page and help center were not fetched this pass, so board-level capability detail stays class-level.

## Historical / Market-Sample Check (§24 test)

Question: would older, regional, platform-native, or differently positioned products still fit the L0?

- **The paper-era practice**: a wall-mounted SQCDP/SQDC board + daily tier meetings (team huddle → department → site) + issues written on cards, escalated by moving them up the board, actions with owners and dates tracked on the same board; leader standard work as printed checklists; gemba walks as a scheduled routine. All three L0 legs are satisfied with paper and meetings — no cloud, no apps, no integrations. The products' own framing confirms this ancestry: iObeya — "The Obeya has evolved from paper walls"; Tervene's SFM imagery shows a physical SQCDP board being reviewed; the Siemens Haguenau customer quote — "What was once handwritten on paper or sent via email is now structured."
- **Pre-lean regional practice** (foreman's daily round + shift-handover book + problem lists reviewed with plant management): satisfies the loop + rhythm legs; the performance picture can be chalk/mark-on-glass production counts. Fits at class level.
- **The execution/MES lineage** (MRP-II shop floor control: dispatch lists, labor reporting) — deliberately NOT part of this Type; it belongs to MES/FOM. The historical check confirms the split: the paper ancestors of *that* lineage (dispatch boards, job travelers) are a different practice from the management-board practice.
- **Non-manufacturing front lines** (Tervene healthcare/nursing homes; iObeya non-manufacturing FAQ): the routine transfers; the leaf stays shop-floor-centered with extension as variant.

Historical check: **passed** — the L0 is not over-fit to the current cloud/mobile implementation.

## Final Synthesis

A **Shop Floor Management** application is the shop floor's **daily management system** — software that holds the floor's performance picture as managed board content (key indicators such as safety, quality, cost, delivery, and people), structures the recurring **tiered meeting rhythm** in which that picture is reviewed level by level, and runs the **issue-to-action loop**: problems surfaced on the floor are documented, escalated to the management level that can resolve them, converted into assigned actions with owners and deadlines, and tracked to closure. Around this core, mature products standardize the managers' own work (leader standard work, gemba walks, audits, shift handovers), run structured problem-solving and continuous improvement, and measure the management process itself; they consume floor data from production systems rather than producing execution records. The defining core is the management routine, not the machines, not the orders, and not the plan.

The market's "shop floor" vocabulary is split: the **execution/dispatch** family self-labels "shop floor execution" or "MES" (Factory Operations Management / MES territory), while the **daily-management** family carries "Shop Floor Management (SFM)" as its own category name. This pass ratifies all four sibling seams on that basis and records the SFM↔generic-work-management seam as the leaf's main classification pressure point.
