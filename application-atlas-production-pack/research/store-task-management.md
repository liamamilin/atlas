# Research Notes — Store Task Management

## Research Goal

Understand the task-layer slice of retail/multi-unit store operations: products whose center is creating, targeting, executing, and tracking store work items (tasks, checklists) between a directing side (HQ / field leadership / store management) and the store workforce. Produce a vendor-neutral Application Document that also completes the joint review with the two processed §05.11 siblings (retail-store-management-system, store-operations-platform).

## Initial Boundary

- Hypothesis: this leaf is the **task-only slice** of the frontline-execution family ratified in the joint review recorded by both sibling passes: work items are directed to store staff and completion is tracked, without a fused first-class directed-communication layer and without the platform's multi-layer coordination surface.
- Nearest neighbors: Store Operations Platform (§05.11 sibling), Retail Store Management System (§05.11 sibling), Task Management Application (§03.06), Retail Merchandising Platform (§05.13), Employee Scheduling / Time & Attendance (§09), Commercial Kitchen Management (§26 — boundary note from that pass), Retail Loss Prevention (§05.25), audit/checklist-only tools.
- Alias risk (recorded by both siblings): market labels drift between "store operations", "task management", and "execution"; some task-first products have grown communication modules.
- Prior passes to treat as counterparty: research/store-operations-platform.md §Boundary Findings (proposed seam: single-layer task tool vs multi-layer coordination platform); research/retail-store-management-system.md §Boundary Findings (record-base vs activity seam).

## Research Questions

1. What is a "task" in these products — one-off, recurring, checklist-packaged? What other work-item classes exist?
2. How are tasks created and targeted (by whom, to what)?
3. How is completion recorded and verified (mark-done, timestamps, evidence)?
4. What does the directing side see (tracking, roll-up, exceptions, reports)?
5. Where does communication sit — absent, a module, or fused into the task surface? (The seam question.)
6. Which capabilities are standard around the core (reminders, corrective actions, audit trail, reports)?
7. What distinguishes this Type from generic task management, from the store operations platform, and from audit-only tools?

## Representative Products

| Product | Tier / positioning | Why selected |
|---|---|---|
| Crunchtime Ops Execution (formerly Zenput) | multi-unit restaurant & convenience-store operations execution; enterprise/multi-brand; suite pillar that "can stand alone" | HQ-driven task automation pole; AI photo validation; franchise hierarchies |
| Bindy | task management + audits for retail & hospitality networks; SMB–mid; self-described "Retail Task Management" | audit-anchored compliance pole; explicit multi-unit field hierarchy; modular platform |
| Jolt / SmartSense Operate (Jolt Lists) | checklist-first digital task management for deskless teams; SMB; restaurants/retail/grocery/convenience | recurring-checklist pole; evidence-gated completion; communication rides on lists |
| Zebra Workcloud Task Management (Reflexis heritage) | enterprise retail task management archetype | market-context anchor only — documentation unreachable (see Sources); no claims from it |
| MeazureUp (Ladle) | audit/site-assessment-first tool | boundary specimen: audits without a directed task loop as center |

Selection spans different philosophies (HQ-automation vs audit-anchored vs checklist-first), industries (restaurant/c-store vs retail/hospitality vs restaurant/retail hybrid), and customer tiers (enterprise multi-brand franchise vs SMB–mid network vs SMB single/multi-site).

## Sources

Research date: **2026-09-08**. All evidence below is from official vendor product pages (Tier 2); no Tier-1 help-center article was fetched this pass.

- Crunchtime — Ops Execution overview: https://www.crunchtime.com/operations-execution ; Restaurant Task Management: https://www.crunchtime.com/ops-execution/task-management (fetched 2026-09-08)
- Bindy — homepage: https://www.bindy.com ; Task Management: https://www.bindy.com/products/task-management/ (fetched 2026-09-08)
- Jolt — homepage: https://www.joltup.com (redirects into jolt.com / SmartSense); SmartSense Operate (digital checklists & task management): https://www.jolt.com/products/task-management-lists/ → served as https://www.smartsense.co (Operate page) (fetched 2026-09-08)
- MeazureUp — Ladle portfolio page: https://ladle.com (fetched 2026-09-08)
- Zebra — https://www.zebra.com/us/en/products/software/workcloud/task-management.html — **transport error** (1 attempt this pass; zebra.com failed ×2 and reflexisinc.com ×1 in the sibling store-operations-platform pass). Abandoned per retry discipline; the enterprise retail-native archetype has no primary evidence across both passes.

Sourcing limitation shared with the sibling pass: Zebra Workcloud / Reflexis unreachable. Assertions about that archetype are avoided; the enterprise pole is evidenced indirectly by the sampled products' positioning (multi-brand franchise hierarchies, above-store leadership views).

## Product Observations

### Crunchtime Ops Execution (formerly Zenput) — evidence layer A

- Positioning: "Operations Execution — equip teams with operational tasks and audits"; task management page titled "Restaurant Task Management"; FAQ: "top-ranked software platform for multiunit restaurants and convenience stores", used in "100,000+ locations"; customers incl. Domino's, Chipotle, Five Guys; supports multibrand franchise hierarchies. (A)
- Task creation/packaging: "Build checklists, projects, and rollouts once and deploy them everywhere. Assign by role, shift, or site to eliminate the manual coordination." Recurring daily operational tasks: "line checks and opening checklists to audits and food safety processes." (A)
- Reminders: "Alerts remind teams when tasks are due so work doesn't slip through the cracks, even during the busiest shifts." (A)
- Completion visibility: "Above-store teams can see what work is being done without stepping foot in a store. Track which tasks were done on time (or not) and identify whether tasks weren't completed correctly." (A)
- Verification: "AI photo verification and completion tracking metrics give field leaders proof that critical tasks were completed correctly, not just marked done"; AI flags blurry/wrong-subject/non-compliant photos. (A)
- Follow-up loop: "Set up automated triggers to identify issues and use follow-up actions to fix them" — corrective-action machinery. (A)
- Records: "comprehensive report of the work that's been done in that location as well as the audits" selectable by date for third-party regulators (health department). (A)
- Suite context: Ops Execution is one pillar of the Crunchtime suite (Inventory, Labor & Scheduling, Kitchen, Guest, Intelligence, L&D); "solutions can stand alone"; task data flows to Insights/Data Streaming analytics. (A)
- Classification: in-type. Task loop is the center; communication is not a marketed pillar of this product line.

### Bindy — evidence layer A

- Positioning: "Bindy is a cloud AI-powered Audits, Tasks and Communication app, purpose-built for retail and hospitality networks. Inspect your sites, verify brand standards, and send tasks." Platform modules: Audits, Task Management, Communication, Ticket Tracking, Project Management. Marketed externally as "Retail Task Management" (FeaturedCustomers badge). (A)
- Work-item classes: Tasks, Information requests, Data collection — tasks usable "on their own or with Projects and Tickets." (A)
- Targeting: "Send tasks to sites and users in seconds. Target recipients individually or by role, and tag. Set priority and due date." Bulk assignment. (A)
- Verification: "Verify with photos, request attachments, and link tasks"; photos, videos, signatures, timestamps, geotags; "full audit trail shows what was done, by whom, where and when." (A)
- Tracking: "Real-time tracking by task, project, and recipient. View aggregate and individual completion and verification photos. Know exactly who has or hasn't done what, where and when." Reminders: "Automatic app notifications and email reminders. Tasks are featured on the dashboard and in the calendar." (A)
- Hierarchy: "Purpose-built for multi-unit networks... region and site-based field hierarchy. Every location and every management layer have the access and visibility they need... no risk of over-sharing." Site affiliation, roles, permissions, confidential sharing. (A)
- Corrective actions: "Assign and track corrective actions" (from audits); "Identify issues, repeat defects, and root causes." (A)
- Industries: multi-unit retail, restaurants, convenience, hotels, pharmacies, CPG, facilities, construction, parking. (A)
- Classification: in-type at the center (tasks), but packaged as a five-module platform. Communication is a separate module — the task module page never fuses comms into the task loop. Center-of-gravity reading: bought for inspections→tasks→completion tracking.

### Jolt / SmartSense Operate (Jolt Lists) — evidence layer A

- Positioning: "Digital task management & checklists for deskless teams... ensuring compliance from the front-of-house to the back office"; Jolt brand page: "We combine powerful task management and IoT technology"; "Jolt Lists — streamline operations with a task management tool with built in accountability features." 16M+ monthly tasks completed on SmartSense. (A)
- Accountability: "Assign tasks, track progress in real-time, and get instant notifications for missed items"; "every task is assigned and tracked... It's clear who is responsible for what." (A)
- Standardization: "Standardize your operations across all locations. From opening procedures to cleaning schedules, guarantee that every task meets your brand's high standards" — SOP-driven recurring checklists. (A)
- Compliance trail: "Every completed task is time-stamped and logged, creating a verifiable and irrefutable digital record of compliance"; "audit-ready records"; centralized documentation for auditors/inspectors/corporate QA. (A)
- Evidence gating (product-specific packaging): "Operate requires users to submit specific forms of evidence—such as photos, notes, signatures, or geo-verified QR code scans—before a corrective action can be marked as complete." (A)
- Exception machinery: "Exception reporting... automatically identifies missed, failed, or late tasks"; corrective actions: "If a task is missed or an issue is found (e.g., a temperature reading is out of range), the system can be configured to send instant alerts, prompting immediate corrective action." (A)
- Sensor coupling (vertical variant): automated temperature logs from SmartSense Monitor fill list items; HACCP time-as-a-control / cool-down monitoring; proactive equipment-maintenance checklists. (A)
- Embedded knowledge/training: information library reachable inside lists ("training videos and SOPs directly within the lists"). (A)
- Communication rides on the task surface: "Communicate key information, daily updates, and announcements directly through lists" — no separate first-class communication module claimed on this product line. (A)
- Adjacent modules: Employee Scheduling, Time Clock, Labeling, Sensors — separate products. (A)
- Industries: restaurants, car washes, hotels, retail, grocery, convenience, healthcare, K-12. (A)
- Classification: in-type; the checklist-first pole; also evidence for the seam (communication as a feature of the task layer).

### Zebra Workcloud Task Management — no evidence (unreachable)

- Documentation unreachable (zebra.com transport errors ×1 this pass; ×2 in the sibling pass; reflexisinc.com ×1). Market context only: an enterprise retail suite packaging task management (Reflexis heritage) alongside separately packaged communication and scheduling products — consistent with task management being a separable layer, but **no product-specific claims are made from it in either pass**.

### MeazureUp (Ladle) — boundary specimen — evidence layer A

- "MeazureUp makes site audits effortless with a mobile-friendly solution that helps multi-location brands improve accountability, track performance, and ensure every location meets brand standards. Streamline audits and daily checklists." Part of the Ladle portfolio (with ComplianceMate food-safety checklists and Storewise pricing). (A)
- Classification: audit/site-assessment-first; the directed work-item loop is not the center (checklists and audits are assessment instruments). Kept as the boundary toward audit/checklist-only tools.

## Cross-product Comparison

| Dimension | Crunchtime Ops Execution | Bindy | Jolt / SmartSense Operate |
|---|---|---|---|
| Location-organized population with directing side | Yes — store teams, field leaders, above-store teams; franchise hierarchies | Yes — region/site field hierarchy; management layers with scoped visibility | Yes — locations with managers overseeing; brand/enterprise dashboard |
| Directed work items | Checklists, projects, rollouts; assign by role, shift, or site; recurring daily tasks | Tasks, information requests, data collection; individual/role/tag targeting; bulk assign | Recurring lists/checklists (opening procedures, cleaning schedules) + assigned tasks |
| Due timing | Due-time alerts | Priority + due date + reminders | Time-stamped lists; notifications for missed items |
| Completion record | Completion tracking metrics; on-time tracking | Real-time per task/project/recipient; audit trail (who/where/when) | Time-stamped completion logs; user productivity reports |
| Verification evidence | AI photo validation | Photos, attachments, videos, signatures, geotags | Photos/notes/signatures/QR scans required for corrective-action completion |
| Overdue/exception machinery | Alerts; automated triggers → follow-up actions | Reminders; dashboard/calendar placement | Exception reporting (missed/failed/late); corrective-action alerts |
| Roll-up to directing side | Above-store visibility; regulator-ready dated reports | Aggregate + individual completion; 28 built-in reports | Cloud dashboard "every location's performance in one place" |
| Communication | Not a marketed pillar of this line | Separate module (Communication) | Rides on lists ("communicate... directly through lists") |
| Audits | In-product audits | Dedicated module (core positioning) | Via checklists/corrective actions |
| Knowledge/training | Separate L&D suite pillar | (Not sampled in depth) | Information library embedded in lists |
| Scheduling/time | Separate Labor pillar | Not claimed | Separate products (Schedule, Time Clock) |
| Sensor/IoT coupling | Temp monitoring / labels (sister products) | Not claimed | Automated temperature logs into lists; HACCP |
| Customer tier | Enterprise/multi-brand franchise | SMB–mid networks | SMB (single & small chains) |
| Industry span | Restaurants, c-stores | Retail, hospitality (broad) | Restaurants, retail/grocery, c-store, hotels, car wash, healthcare |

### Cross-product readings (evidence layer B unless noted)

- **The directed-work loop is the common core**: a directing side creates work items; items are targeted to locations/roles/people; staff execute and mark done; completion (who/when/what, on-time or late) is tracked and visible upward. Present in all three sampled products with nearly identical vocabulary ("who has or hasn't done what, where and when"). (B)
- **Checklists are the dominant packaging of recurring store work**: opening/closing/line-check/cleaning routines built once and deployed to many locations (Crunchtime "build once, deploy everywhere"; Jolt SOP checklists; Bindy "hundreds of templates and checklists"). (B)
- **Attributable, time-stamped completion records are the norm** — the products sell "irrefutable digital records" vs paper. (B)
- **Verification evidence (photos/signatures/attachments) is near-universal in mature products**, but its strictness varies (Bindy optional verification; Jolt evidence-gating for corrective actions; Crunchtime AI validation). Common-mature, not definitional. (B)
- **Exception machinery (reminders, missed/late identification, corrective actions) is common**, packaged differently per product. (B)
- **Communication is NOT fused as a first-class co-equal layer in any sampled product**: absent from Crunchtime's task line; a separate module in Bindy; riding on lists in Jolt. This is the load-bearing seam evidence vs the store-operations-platform Type (where directed communication is a founding, first-class flow). (B)
- **Task management is packaged both standalone and as a suite module**: Crunchtime "solutions can stand alone"; Bindy Task Management is one of five modules; Jolt Lists is a named product line; Zebra Workcloud packages task management as a separately marketed product (market context only). (B; Zebra market context)
- **The audit layer is adjacent and variably packaged**: dedicated module (Bindy), in-product audits (Crunchtime), corrective-action machinery (Jolt), audit-only products exist (MeazureUp) — audits feed tasks (corrective actions) rather than defining the Type. (B)
- **Scheduling/knowledge/learning appear as adjacent modules or sister pillars, not as the center** — consistent with the sibling pass's reading. (B)
- **Food-safety vertical coupling** (temperature probes/sensors filling list items, HACCP) is a strong variant concentrated in foodservice/c-store. (B)
- **Industry span**: retail is the leaf's center of gravity, but the sampled structure is identical across restaurants, convenience, grocery, hospitality — industry is packaging. (B)

## Canonical Model

### Level 0 — Defining Invariant

The smallest structure without which the product stops being a store task management application. Three jointly-held structures:

1. **The store/site-organized workforce as the served population, with a directing side above the executing side.** Work is organized around physical locations and the staff in them; HQ / field leadership / store management directs, store staff execute. One or many locations; the two-sided structure is the invariant, fleet size is not. *(Remove → generic task management with no store structure.)*
2. **Directed work items targeted to that population.** Tasks (commonly grouped as recurring checklists) created by the directing side — or locally by store managers — targeted by location/role/person, carrying due timing, which staff see and execute. *(Remove → a staff directory / org chart; nothing is directed.)*
3. **The completion record and its upward tracking.** Each item's execution state — done or not, by whom, when, on time or late — is recorded at the item level, attributable, and visible to the directing side per location (commonly aggregated across locations). *(Remove → one-way distribution: a memo plus a task pad with no follow-up.)*

Jointly-held is load-bearing:

- 1 alone → staff directory / org chart
- 2 + 3 without 1 → generic task tracker (§03.06 territory)
- 2 without 3 → distribution without control
- 1 + 3 without 2 → reporting shell with no directed work

Consistency note (joint review): this is exactly the sibling platform's decomposition — its structures 2 + 4 minus its structure 3 (first-class directed operational communication). The seam is ratified from this side.

### Level 1 — Common Mature Structure

Present across the sample; expected in the market but not definitional:

- **Recurring checklists / SOP deployment** — build routines once, deploy to all locations; daily opening/closing/line-check/cleaning lists. (B)
- **Targeting engine** — assign by location, role, person, shift, tag; bulk assignment. (B)
- **Priority and due dates** with **automatic reminders/notifications**. (B)
- **Verification evidence** — photos, attachments, signatures, timestamps, geotags; in some products evidence gates completion (product-specific packaging). (B)
- **Exception machinery** — missed/failed/late identification, exception reports, alerts, corrective actions and follow-up tasks. (B)
- **Manager and above-store visibility** — real-time tracking, dashboards, completion-rate and on-time reporting, drill-down by location; audit-ready records for inspectors/regulators. (B)
- **Attributable audit trail** — who did what, where and when, time-stamped. (B)
- **Mobile staff surface + web console** — tablets/phones at the store; dashboard for managers/HQ. (B)
- **Templates library** — pre-built checklist/form templates to start from. (B)

### Level 2 — Variant / Optional Structure

- **Industry packaging** — retail stores canonical (leaf position), but the same structure serves restaurants, convenience, grocery, hotels, car washes, healthcare; industry is packaging, not core.
- **Center-of-gravity poles** — recurring-checklist-first (Jolt pole) vs freeform directed-task-first (Bindy/Crunchtime pole) vs HQ-rollout-automation-first (Crunchtime pole).
- **Audit/inspection layer** — dedicated module, in-product audits, or corrective-actions-only; audit-first products without a task loop are boundary tools (MeazureUp specimen).
- **Food-safety sensor coupling** — temperature probes/sensors auto-filling list items, HACCP workflows, labeling integrations (foodservice/c-store vertical).
- **Franchise/multi-brand hierarchies** — scoped visibility for corporate vs franchisee; multibrand support (product-specific depth in the enterprise pole).
- **Suite-module vs standalone packaging**; adjacent modules sold alongside (scheduling, time clock, communication, knowledge/training, analytics warehouses).
- **Communication features** — absent, riding on the task surface, or a separate module; NOT a fused co-equal directed-communication layer (that is the platform Type).
- **Knowledge/training embedding** — SOPs/training videos reachable inside lists (one sampled product) vs separate learning products.
- **AI assistance (current generation)** — photo validation, auto-flagged non-compliance, insights; current-gen layer, not definitional.

### Level 3 — Vendor-specific Structure (kept out of the final document)

- Crunchtime: "Ops Execution" pillar naming, Zenput→Crunchtime rebrand, AI photo-intelligence flagging, Data Streaming/Insights analytics products, named customer counts (100,000+ locations), "rollouts" terminology.
- Bindy: five-module platform naming (Audits/Task Management/Communication/Ticket Tracking/Project Management), "information requests" and "data collection" as named work-item classes, usage-based pricing, 140 brands/21 countries claim, weather-tagging, check-in/check-out geolocation, "Ask Bindy" AI onboarding, 28 built-in reports.
- Jolt/SmartSense: "Jolt Lists" / SmartSense "Operate" naming, evidence-gated corrective actions (photos/notes/signatures/geo-verified QR scans before completion), 16M+ monthly tasks claim, sensor/label/time-clock product lines, Digi International ownership, Customer Success Manager onboarding model.
- MeazureUp/Ladle: AuditApp trial funnel, portfolio structure with ComplianceMate/Storewise.

## Vendor-specific Findings (structural value, kept in notes)

- Crunchtime's "solutions can stand alone" is direct market evidence that the task layer is independently purchasable — supporting the layer-slice reading of this Type. (A)
- Bindy's five-module split (tasks / communication / audits / tickets / projects as separately named modules) mirrors the layer decomposition used in the joint review: the task layer is separable from the communication layer even inside one product. (A)
- Jolt's "communicate... directly through lists" shows the no-platform pattern: communication piggybacks on work items instead of being an independent directed flow. (A)
- Crunchtime's and Bindy's franchise-hierarchy visibility controls ("no risk of over-sharing", "right amount of visibility to corporate and field teams") evidence that multi-party hierarchy visibility is a real design constraint of the Type. (A)

## Boundary Findings

1. **vs Store Operations Platform (§05.11 sibling, processed 2026-09-08) — JOINT REVIEW COMPLETED from this side.** The sibling's proposed seam — single-layer task tool (work-item half: assign/execute/track) vs multi-layer coordination platform (tasks + directed communication, commonly audits/scheduling/knowledge, over one staff-facing surface) — is **CONFIRMED, with a center-of-gravity refinement**. Evidence from this side: (a) in all three sampled task-layer products, directed communication is absent, a separate module, or rides on the task surface — never a fused first-class co-equal flow; (b) the products are bought for the task loop; the directing side's primary lens is completion/compliance of defined work items; (c) the market itself packages the task layer as separable (suite pillars that "stand alone", separately named modules). Refinement: because task-first products can grow communication modules, the binary "layer present/absent" test can misclassify mature products near the seam; classification should ask what the product is bought for and which layer is the founding, center surface (task loop vs coordination fabric). A product that adds a first-class directed-communication flow and a fused day-surface (tasks + comms + schedule) has drifted into the platform Type. Alias risk stands (market label drift), cross-references required in both documents.
2. **vs Retail Store Management System (§05.11 sibling, processed 2026-09-07).** Record-base vs activity seam, already ratified by both sibling passes: the management system is the commerce-operations record base (offering/stock/staff/cash/sales behind the register); store task management directs and tracks workforce activity. Different record bases; coexist in one retail stack. No conflict from this side.
3. **vs Task Management Application (§03.06).** Generic task tracking serves any team/project context; store task management is structured by store/site hierarchy, targets a store workforce, and carries a compliance/standardization lens (brand standards, SOPs, regulator-ready records). Remove the store/location population structure → generic task management.
4. **vs Retail Merchandising Platform (§05.13).** Merchandising decides what stores should display and stock (planograms, assortments); task management executes and verifies the associated in-store work (setup tasks, photo verification). Field-execution data capture (sibling pass's GoSpotCheck specimen; MeazureUp audits) sits at this seam: capture about execution vs direction of work.
5. **vs Employee Scheduling / Workforce Management (§09).** Scheduling-led products center labor forecasting, shifts, time & attendance for their own sake; here the schedule (when present) is an adjacent module that makes task targeting shift-aware ("assign by role, shift, or site"). Jolt/SmartSense and Crunchtime both package scheduling as separate products.
6. **vs Commercial Kitchen Management (§26; boundary note from that pass).** That pass recorded: store task management is "checklist execution without recipes/production". Confirmed: checklist-first tools share the execution surface, but kitchen management centers the food-production knowledge loop (recipes → prep plans → production); task management has no production object model.
7. **vs Retail Loss Prevention (§05.25).** LP audits and exception follow-ups appear inside task/audit layers (Bindy lists loss prevention as a solution); the LP Type centers shrink/fraud programs. Task management is the execution substrate LP programs may ride on.
8. **vs audit/site-assessment tools (MeazureUp specimen).** Audit-first products center the assessment instrument (scored site visits, brand-standard audits); task management centers the directed work-item loop. Audits generate corrective actions which may become tasks — the audit instrument is not the task loop. Under the store-operations joint-review structure, an audit-only tool lacks the directed task half.
9. **vs Construction Field Management / Punch List (§17) and other industry task-loop products.** The same directed-work loop exists in construction, facilities, field service; the store leaf is scoped to retail/multi-unit location operations. Bindy already lists construction as an industry — the cross-industry drift zone is real; industry-scoped products with different object models (punch lists, RFIs, submittals) are different Types, while same-structure products are industry packaging.

### "Remove what, and it becomes another Type?" summary

- Remove the store/location population structure → generic task management (§03.06).
- Add a fused first-class directed-communication layer + coordinated day-surface → store operations platform (sibling Type).
- Move the center to commerce records (offering/stock/sales) → retail store management system.
- Move the center to the assessment instrument → audit/site-assessment tool.
- Move the center to labor scheduling/time → employee scheduling / WFM.
- Move the center to recipes/production → commercial kitchen management.
- Move the center to what stores display/stock → retail merchandising platform.

## Historical / Market-Sample Check (§24 discipline)

- **Paper-era chain retail** satisfies the core: HQ directive sheets and planogram memos translated into store task pads and daily job lists (directed work items targeted to locations), manager sign-off and initialing of completed jobs (attributable completion record), district-manager visit reports and completion sheets mailed/collected weekly (upward tracking). No software, mobile, cloud, or photo evidence required. ✓
- **Restaurant checklist heritage**: printed opening/closing/line-check lists with initials and time-in/time-out columns — same structure, centuries older than software. ✓
- **Pre-smartphone software era**: store-level task lists on back-office PCs, printed daily for the shift — directed work items + completion tracking without mobile apps. ✓
- **Regional products** (e.g., European/Japanese chain store-execution tools): same structure expected; not directly sampled; no definition element depends on region-specific machinery. ✓ (qualified)

The definition therefore does not depend on: mobile apps, cloud delivery, AI, photo verification, sensors/IoT, audits, scheduling, communication features, or any specific evidence-gating mechanism — all are common implementations, not invariants.

## Uncertainties

1. **Zebra Workcloud / Reflexis unreachable** (shared limitation with the sibling pass) — the enterprise retail-native task-management archetype has no primary evidence across both passes; no claims made from it; the enterprise pole is evidenced indirectly (Crunchtime/Bindy franchise-hierarchy features).
2. **Standalone vs module market share** — the sample shows both packagings; no assertion about which dominates the market.
3. **Seam fuzziness** — task-first products adding communication modules (drift toward the platform) mean the boundary is center-of-gravity, not binary absence; recorded as a refinement, not a contradiction, of the sibling's proposed seam.
4. **Retail center of gravity** — the leaf name says "store"; the sampled market skews restaurant/c-store-heavy; the structure is identical, but the retail-only referent (Zebra Workcloud Task Management) could not be directly verified.
5. **Bindy's "information requests" / "data collection" work-item classes** — product-specific packaging of directed requests; whether other products formally separate these classes was not verified.
6. **Tier-1 help-center evidence** — no help-center article was fetched this pass; all observations are product-page level (Tier 2). Precise operational parameters (limits, defaults, exact state names) are avoided in the final document.

## Final Synthesis

A **Store Task Management** application is the task-layer slice of store (multi-unit location) operations: a directing side — HQ, field leadership, store management — creates targeted work items (recurring checklists and one-off tasks) for the workforce of specific store locations; staff see, execute, and mark them done, commonly with attributable, time-stamped records and often with verification evidence; and completion state rolls back up so the directing side can see who has and hasn't done what, where and when — with reminders, exceptions, and corrective actions keeping the loop closed. Its defining core is three jointly-held structures: the location-organized two-sided workforce, directed work items targeted into that population, and the tracked completion record. Around that core, mature products add recurring SOP deployment, targeting engines, priority/due machinery, evidence capture, exception/reporting layers, and templates. The Type is distinct from the store operations platform (no fused first-class directed-communication layer; the task loop, not multi-layer coordination, is what the product is bought for), from the retail store management system (activity layer vs commerce record base), from generic task management (store/site structure and compliance lens), from audit-only tools (the directed work-item loop, not the assessment instrument, is the center), and from scheduling/WFM (shift-awareness is adjacent, not central). The same structure packages across industries (retail canonical; restaurants, convenience, grocery, hospitality identical) and across delivery forms (standalone products, suite pillars, separately marketed modules).
