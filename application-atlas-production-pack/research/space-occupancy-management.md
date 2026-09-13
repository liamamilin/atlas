# Research Notes — Space & Occupancy Management (§17)

Research date: 2026-09-09
Slug: space-occupancy-management

## Research Goal

Determine whether the §17 leaf **Space & Occupancy Management** denotes an Application Type distinct from the already-processed §10 sibling **Space Management Platform**, or whether the market uses the two phrases for one and the same product population (alias). Produce this leaf's own record either way, and resolve the alias suspicion pre-hung by the space-management-platform pass (2026-09-08): *"the market treats the phrases as the same domain. Strong likelihood the two directory leaves denote one Type → Taxonomy note recorded; both leaves kept, alias suspected."*

## Initial Boundary

Hypothesis entering research — "occupancy" could add to a space-inventory core in three ways:

1. **Occupancy as managed state** — who/what is assigned to each space (people, organizations, departments), maintained as records. If this is all, the leaf is the same Type as Space Management Platform (whose core leg 3 is "allocation & occupancy state per space — who sits where").
2. **Occupancy as forward planning** — occupancy planning: forecasting headcount, scenario/stack planning for future space needs.
3. **Occupancy as measurement** — sensor/badge/WiFi-derived utilization of spaces.

If (2) or (3) formed a distinct product population centered on them (without the inventory/allocation record), the leaf could be an independent Type. If (1) dominates, alias.

Nearest types (directory): Space Management Platform (§10, processed), IWMS (§17, processed), Facility Management System (§17, processed), Workplace Management Platform (§10, processed), Office Operations Platform (§10, processed), Building Management System (§17, processed), Amenity Booking Platform (§17, processed), Coworking/Flexible Workspace Management (§17, processed), Hotel PMS (§26), Lease Administration (§17).
Non-directory boundary pole: occupancy sensing / occupancy-analytics products (VergeSense, Density class).

Pre-hung flags on this leaf: space-management-platform pass → alias suspected (discharged this pass); IWMS pass → "vs Space Management Platform / Space & Occupancy Management (§10/§17): space is a domain inside the IWMS; standalone space platforms exist. Keep both."

## Research Questions

1. What do vendors that use the exact phrase "space & occupancy management" actually sell under that phrase?
2. In their product architecture, what does "occupancy" denote — assignment state, planning, or measurement?
3. Is there a market population whose center is occupancy measurement WITHOUT a space-inventory/allocation record of record? Do those products self-describe as "management"?
4. Does the sampled population's core structure differ from the space-management-platform pass's four jointly-held legs?
5. Historical check: does pre-digital and pre-modern practice of space & occupancy management satisfy the same core?

## Representative Products

Selected for: use of the exact phrase, market representativeness, documentation depth, different product philosophies (suite module vs pure-play) and customer segments (enterprise/government/higher-ed vs mid-market corporate).

| Product | Kind | Segment | Why sampled |
|---|---|---|---|
| IBM TRIRIGA | IWMS suite (space & occupancy as domain) | enterprise, government | exact phrase "space and occupancy"; best Tier-1 operational docs |
| Archibus (Eptura) | IWMS/CAFM suite (Space domain) | enterprise, higher-ed, government | official help docs use the exact phrase "space and occupancy management" |
| FM:Systems FM:Interact | mid-market IWMS/CAFM suite | corporate, higher-ed, healthcare | product pages title space management as "visibility into space and occupancy"; exact-phrase anchor |
| OfficeSpace | pure-play workplace/space management | mid-market/enterprise corporate | modern pure-play pole; Tier-2 evidence (help docs unreachable, also for the sibling pass) |
| SpaceIQ (SiQ, now Eptura) | pure-play space management | enterprise corporate | pure-play pole; consolidated category history (Archibus+SpaceIQ+Serraview→Eptura) |
| VergeSense | occupancy sensing/analytics (boundary pole, not the Type) | enterprise corporate | tests whether "occupancy" alone forms a distinct measurement-centered Type |

## Sources

All accessed 2026-09-09 unless noted.

**IBM TRIRIGA (Tier 1)**
- IBM TRIRIGA Space and Move Management User Guide (PDF, v11.6): https://www.ibm.com/docs/en/SSFCZ3_11.6/pdf/pdf_tri_space_move_mng.pdf
- IBM TRIRIGA docs — "Planning facilities, spaces, and moves": https://www.ibm.com/docs/en/tririga/11.6.0?topic=planning-facilities-spaces-moves
- IBM TRIRIGA docs — "Managing spaces and moves": https://www.ibm.com/docs/en/tririga/11.5.0?topic=moves-managing-spaces
- IBM TRIRIGA docs — "Occupancy Rate (%) metric": https://www.ibm.com/docs/en/tririga/11.5.0?topic=metrics-occupancy-rate-metric
- State of Arizona GAO — TRIRIGA Space Management manual (agency operational procedure): https://gao.az.gov/sites/default/files/2022-05/TRIRIGA%20Space%20Management%20V2_0.pdf

**Archibus / Eptura (Tier 1)**
- Archibus help — Space Inventory: https://help.archibus.com/user_en/Subsystems/webc/Content/sp_results/space_inv_web.htm
- Archibus help — Space Domain: https://help.archibus.com/user_en/Content/sp_results/space_business_functions.htm
- Archibus help — Space module (Archibus SaaS): https://help.archibus.com/user_en/Subsystems/webc/Content/sp_results/space_module.htm
- Archibus help (mirror) — Workspace Transactions tables: https://archibus.tn.gov/archibus_help/user/Subsystems/webc/Content/web_user/space/concepts/understanding_transactions.htm
- Archibus products: https://archibus.com/products , https://archibus.com/products/space-management
- University of Queensland — Archibus Space Management Manual (customer operational doc): https://coo.uq.edu.au/files/28309/Archibus%20Space%20Management%20Manual.pdf

**FM:Systems (Tier 2 — official product pages/blog)**
- Space Management: https://fmsystems.com/products/workplace-management-solutions/space-management
- Strategic Scenario Planning: https://fmsystems.com/products/workplace-management-solutions/strategic-scenario-planning
- Blog — Best Practices for Space Management: https://fmsystems.com/blog/introducing-the-best-practices-for-space-management
- FM:Interact 8.4 announcement (PRNewswire, 2015): https://www.prnewswire.com/news-releases/fmsystems-announces-the-availability-of-fminteract-version-84-with-room-scheduling-and-powerful-new-space-management-tools-300025867.html
- FM:Interact 7.0 (FMLink, 2006): https://www.fmlink.com/fmsystems-introduces-updated-version-of-fminteract-which-analyzes-facilities-in-real-time

**OfficeSpace (Tier 2 — official product pages; help center unreachable in both this and the sibling pass)**
- Space Management: https://www.officespacesoftware.com/solutions/space-management , https://www.officespacesoftware.com/lp/space-management-062025
- Scenario Planning: https://www.officespacesoftware.com/features/scenario-planning
- Studio (floor plan editor): https://www.officespacesoftware.com/features/officespace-studio

**SpaceIQ (Tier 2/3)**
- SpaceIQ → Eptura transition page: http://spaceiq.com/
- TechnologyEvaluation.com SpaceIQ features list: https://www.technologyevaluation.com/features-list/spaceiq-54119

**VergeSense (boundary pole, Tier 2 — official product pages)**
- Occupancy Intelligence Platform: https://www.vergesense.com/occupancy-intelligence , https://www.vergesense.com/products/occupancy-intelligence/analytics

**Sourcing limitations**
- OfficeSpace and SpaceIQ official help/knowledge centers were not reachable in this pass (and were recorded unreachable — Salesforce render / transport errors — in the sibling space-management-platform pass). Evidence for both is product-page tier; assertions about them are calibrated accordingly.
- No precise numeric claims (percentages, sqft thresholds, counts) are asserted from marketing pages; one vendor-cited "up to 30%" utilization claim and sensor "95% accuracy" claim are recorded here as vendor marketing figures only, not used in the Type document.
- The alias determination does not depend on the Tier-2 products: it is carried by Tier-1 evidence (TRIRIGA, Archibus) plus the exact-phrase anchor (FM:Systems, Archibus docs).

## Product Observations

### IBM TRIRIGA (evidence layer A — official operational docs)

- The space management feature: "maintain space plans and track space utilization data in buildings and structures... manage people and assets that are in the space, and coordinate property transactions." (A)
- Process flows: create organizations → **assign space allocations** (spaces allocated to organizations) → **people assignment** ("assigning people to spaces in TRIRIGA... creating the people records, assigning people to the spaces, and **updating the occupancy**"). (A)
- Space occupancy policy: settings "define the space occupancy policy for your organization... whether to manage occupancy allocations for spaces based on the organization of the people assigned"; "the **space occupancy allocation** gives companies the flexibility to set different organizations for occupancy and financial responsibility for the space"; explicit doc figure contrasts "**space occupancy allocations versus space chargeback allocations**". (A)
- Space record carries an **Occupancy Status** (example: "Occupied") on its Allocation tab. (A)
- Roles: **space manager** ("tracking the allocations, assignments, and utilization of the spaces within a facility as determined by space use agreements") and **space planner** ("monitoring the costs and utilization of the spaces at the strategic portfolio level"). (A)
- Space use agreements, space associations (allocate a space/area to one or more organizations; assign a person or asset to one or more spaces), space audits, space utilization tracking. (A)
- Strategic Facility Planning: planning environment + portfolio plans; "in the space plan, you can build and compare different scenarios". Dynamic Space Planning (DSP) app: scenarios to "rearrange organization allocations, rearrange personnel seat assignments, and designate spaces as reservable or dedicated", then "automatically update active space details to match the scenario". (A)
- **Occupancy Rate (%)** is a shipped benchmarking metric. (A)
- Move management: move requests → assign person and assets to new location → "the assignment ensures that the occupancy information for the affected locations is up-to-date". (A)
- Customer-operations corroboration (Arizona GAO manual): space planner evaluates spaces for occupancy and chargeback assignments via walkthroughs; occupying vs chargeback department can differ; vacant rooms can remain chargeable; allocation records generated on activation. (A)
- Customer corroboration (CFTC PIA): TRIRIGA "primarily used to monitor building and workspace occupancy"; floorplans show staff name, division indicator, space information. (A)

### Archibus / Eptura (evidence layer A — official help docs)

- Exact phrase: "**The Space module provides four areas of space and occupancy management**": (1) workspace transaction-based space inventory, (2) workplace chargeback, (3) Space Planning, (4) occupancy/moves content. (A)
- Space Inventory application: facility managers "develop basic underlying facility information"; floor plans drawn in CAD with "gross areas, vertical penetration areas, service areas, and departmental areas"; the **Space Console** is "a multi-faceted tool for managing your space **and occupancy**"; reports include "**Space and Occupancy Analysis reports**". (A)
- Inventory as prerequisite: "An accurate space inventory, particularly developed to the room level, is **the backbone** of an automated facility management system and is a **prerequisite** for many of the Archibus applications" (Corrective Maintenance, Reservations, Service Desk, Condition Assessment all require it). (A)
- **Occupancy application**: "Once you develop a space inventory, manage how it is occupied. Enter your employees and teams and produce **occupancy plans, employee headcounts**, and inventories of employees by site and building. Determine **employee-to-seat ratios and occupancy rates**." (A)
- **Personnel & Occupancy** application: "reduces vacancy rates... place employees according to standards, resulting in uniform and fair employee placement that adheres to corporate policies." (A)
- **Space Chargeback**: "internally bill departments for the space that they occupy as well as their share of the floor's or building's common space." (A)
- **Space Planning**: "develop space requirements, work with **stack plans** to experiment with different allocations of space, and compare the different scenarios." (A)
- Workspace transactions: room/employee/workspace transaction tables hold **occupancy count, primary division/department, category, type**; linked to employee moves and department claims; a division/department may "own" the room and "be charged for their assigned rooms whenever the room is either vacant or occupied". (A)
- Field tools: **Space & Occupancy Survey** mobile app (survey the occupancy inventory, record discrepancies); Space Book app. (A)
- Customer-operations corroboration (UQ manual): Space Inventory + Occupancy modules; org-unit allocation levels 1–5, capacity, occupancy use, occupancy audit info; "Where is My Desk / Where is My Team" self-service; space allocation changes "can only be done and recorded through the Space Manager". (A)

### FM:Systems FM:Interact (evidence layer A/B — official product pages + dated announcements)

- Space management product page: "complete **visibility into space and occupancy**"; "the management of your space inventory includes **tracking and maintaining your space allocation and occupancy information — identifying who sits where**, understanding how much types of space your organization has, how it is categorized, how it's being used, and **projecting and forecasting how much real estate you will need**". (A for FM:Systems' own positioning)
- Suite scope (official pages/PR): space management, strategic scenario planning, room scheduling/space reservation, move management, lease & property, asset management, facility maintenance, sustainability. (A)
- Scenario planning module: "visualize what your space and occupancy might look like years into the future"; interactive **stacking and blocking**; planning criteria by department/division; check out floors in CAD and convert to scenario drawings. (A)
- Own blog: "Space is at the heart of facility management... the **foundation for occupancy management** as well as move management, strategic planning, room reservations, facility maintenance, real estate management and more."; FM list: total area, capacity, occupant count, **occupancy rate, vacancy rate**, planned density, space assignment by occupant, vacant seats, space assignment by department. (A)
- Company lineage: founded 1984 "with the vision of creating a flexible, comprehensive **office space management system**"; describes itself as IWMS/CAFM. (A)
- CAD integration, floor-plan viewing (FMx5 viewer, DWF, A360/BIM viewing) throughout its history (2006–2015 releases). (A)

### OfficeSpace (evidence layer B/C — Tier-2 product pages, third-party listing)

- Interactive floor plans "to track **occupancy, seating assignments, and usage trends** in real time"; teams seated "according to department needs". (B)
- MAC streamlining: "Automate team relocations, adjust seating assignments"; HRIS integration "so new hires are automatically added to the move queue". (B)
- Utilization: heatmaps, utilization dashboards, occupancy stats; "predictive planning signals". (B)
- Scenario planning: multiple floor/LOB scenarios; block & stack; "supply, demand, and allocation at the building stack level"; merge approved scenarios into live plans. (B)
- Third-party listing (Capterra): "Differentiating capabilities include **occupancy management**, move management, and utilization reporting." Customer quote: "we previously managed our **occupancy planning and record keeping** on AutoCAD drawing files." (B/C)

### SpaceIQ / SiQ (evidence layer B/C — Tier-2/3)

- Post-consolidation positioning (now Eptura): SIQ environment to "view workspace usage, **update floorplans, plan office moves**". (B)
- Feature synthesis (TEC): "Space and Move Management — track detailed workspace info like **occupancy rates** and manage office moves"; Space Planning & Optimization module fully supported (floor plan creation, space utilization analysis, space inventory management). (C)
- Category consolidation: Archibus + SpaceIQ + Serraview under Eptura — consistent with the sibling pass's market note. (B)

### VergeSense (boundary pole — evidence layer A for its own positioning)

- Self-description: "**Occupancy Intelligence** Platform" — "badge, WiFi, room booking, video conferencing, and sensor data all in one platform"; workflow "Connect → Unify → Plan"; analytics on person count, active/passive occupancy, utilization by space type; "Predictive Planning" forecasts demand and models scenarios. (A)
- No space-inventory/allocation record of record is claimed anywhere on its pages: no people-to-space assignment records, no org allocations, no move/MAC management, no chargeback. Its output "feeds" planning; it does not maintain who-is-assigned-where. (A — by absence in its own product descriptions)
- It explicitly positions itself as a measurement/decision layer on top of the workplace stack ("integrate with the rest of the workplace tech stack"). (A)

## Cross-product Comparison

| Dimension | TRIRIGA | Archibus | FM:Systems | OfficeSpace | SpaceIQ | VergeSense (pole) |
|---|---|---|---|---|---|---|
| Space inventory of record (rooms/spaces, areas, types) | ✓ (space records, classifications) | ✓ (Space Inventory; "backbone/prerequisite") | ✓ (space inventory management) | ✓ (floor plans as data) | ✓ (space inventory mgmt) | ✗ |
| Floor-plan-anchored spatial representation | ✓ (CAD integration, drawings, Drawing Manager) | ✓ (CAD-linked records; Space Console) | ✓ (FMx5 viewer, CAD/BIM viewing) | ✓ (Studio editor, 3D) | ✓ (floorplans central) | (floor-plan context for analytics only) |
| Person-grain occupancy assignment (who sits where) | ✓ (people assignment → updates occupancy) | ✓ (Occupancy app; headcounts; employee-to-seat ratios) | ✓ ("identifying who sits where") | ✓ (seating assignments) | ✓ (workspace info) | ✗ |
| Org-grain allocation (department/organization occupies space) | ✓ (space allocations to organizations; occupancy vs chargeback allocations) | ✓ (departmental areas; org-unit allocation; workspace transactions) | ✓ (space allocation; assignment by department) | ✓ (department layouts; LOB allocation) | ✓ (neighborhoods/teams) | ✗ |
| Recorded space-changing operations (moves/MAC, reallocations) | ✓ (move mgmt updates occupancy; audits) | ✓ (workspace transactions; moves; survey apps) | ✓ (move management module) | ✓ (MAC automation, move queue) | ✓ (office move planning) | ✗ |
| Occupancy planning (scenarios, stack/block, forecast) | ✓ (SFP, DSP scenarios) | ✓ (Space Planning, stack plans) | ✓ (Strategic Scenario Planning) | ✓ (scenario planning, block & stack) | ✓ (stack planning) | ~ (predictive planning forecasts only) |
| Occupancy/utilization analytics & metrics | ✓ (Occupancy Rate metric, utilization) | ✓ (occupancy rates, Space & Occupancy Analysis reports) | ✓ (occupancy/vacancy rates, dashboards) | ✓ (utilization heatmaps) | ✓ (utilization reports) | ✓ (core — measurement is the product) |
| Chargeback | ✓ (chargeback allocations) | ✓ (Space Chargeback app) | ✓ (chargebacks named) | ~ (cost analysis surfaces) | — | ✗ |
| Employee self-service location surface | ✓ (reservable designation; self-service move requests) | ✓ (Where is My Desk/Team; Workplace portal) | ✓ (Space Reservation module; workplace hoteling) | ✓ (desk/room booking suite) | ✓ (booking stack) | ✗ |
| Sensor/badge measurement integration | — | — | ~ (workplace survey app) | ~ (integrations incl. sensors) | ~ | ✓ (the product itself) |
| Core = inventory + occupancy state + recorded changes | **yes** | **yes** (exact phrase owner) | **yes** | **yes** | **yes** | **no** |

Read: the five management-side products share one structure; the measurement pole lacks that structure and self-describes differently ("occupancy intelligence", not "occupancy management").

## Canonical Abstraction

### L0 — Defining Invariant

The same jointly-held four-leg structure the sibling pass derived for the §10 Space Management Platform population, independently re-derived here from occupancy-language evidence:

1. **The space inventory of record** — the organization's occupiable spaces as persistent individually identified records (site→building→floor→space grain; types, areas, capacities). Remove → drawing tool / room list / real-estate listing.
2. **Plan-anchored spatial representation** — the inventory bound to building/floor plans (native editors, CAD-linked drawings, or BIM) through which space is browsed, edited, and reported. Remove → generic facilities database or CAD viewer.
3. **Occupancy state per space** — the managed org↔space and person↔space map: allocated to a department/organization, assigned to a person, shared/team space, bookable, vacant — "who sits where", at both organization grain and person grain. Remove → floor-plan viewer or space registry.
4. **Recorded space-changing operations** — seat assignments, moves/MAC, department reallocations, surveys/audits recorded as state changes so occupancy stays current and history is reconstructable. Remove → static snapshot.

Jointly-held load-bearing (same failure modes as sibling): inventory+plan without occupancy = CAD viewer; occupancy+ops without inventory = booking tool; inventory+occupancy without recorded ops = space registry.

The "occupancy" half of the leaf name denotes legs 3–4 in vendor usage (TRIRIGA: people assignment "updating the occupancy"; Archibus: the Occupancy application managing "how it is occupied"), NOT the measurement sense.

### L1 — Common Mature Structure

- Occupancy planning: scenario building, block & stack planning, headcount forecasting, scenario-to-execution promotion (4/5 management-side products ship it as a named module).
- Occupancy/utilization analytics & reporting: occupancy rate, vacancy rate, density, headcounts, utilization trends (5/5).
- Chargeback (charging departments/organizations for occupied space incl. shared-space share) (3/5 explicitly, deeper in org-grain segments).
- Employee-facing location surfaces: "where is my desk/team", search people/rooms on floor plans (4/5).
- Field survey/audit tooling for inventory & occupancy accuracy (TRIRIGA space audits, Archibus survey apps, FM:Systems Workplace Survey).
- Space standards/classifications and placement policies governing assignment.
- HRIS/directory integrations feeding people records into occupancy.

### L2 — Variant / Optional

- Real-estate measurement regime specifics (BOMA-class rentable/usable computations, area standards) — segment/regime packaging.
- Hybrid/free-address realization: booking-forward occupancy with sensors/badges feeding measured occupancy (era-current).
- Deployment: on-prem (government-authorized) vs cloud/SaaS.
- Segment regimes: higher-ed/government space classification & chargeback programs vs corporate hybrid workplace.
- Native floor-plan editor vs CAD bi-directional integration vs BIM linkage; 3D walkthroughs.
- Suite-module vs pure-play packaging.

### L3 — Vendor-specific (research notes only)

- TRIRIGA: Dynamic Space Planning app; occupancy-allocation policy flags (use people's primary organization; global vs building level); space use agreements; move policy/cost estimation; Occupancy Rate metric definition.
- Archibus: workspace-transaction schema (rmpct) with occupancy roll-ups; InferRoomDepartment parameter; Essentials SaaS module limits; Space Console; Space & Occupancy Survey mobile app.
- FM:Systems: FMx5 floor plan viewer; Workplace Survey Application; "workplace strategy as a service".
- OfficeSpace: AI agents (Space Planning/WEX/Insights/Facilities), Studio 3D/AI rendering, 35-day implementation claim, BOMA-aligned "Studio" space math.
- SpaceIQ/Eptura: consolidation packaging (Archibus+SpaceIQ+Serraview); SIQ login environment.
- VergeSense: Meridian platform, Large Spatial Model, passive-occupancy detection, Infinity sensors, 250M+ sqft dataset claims, "95% accuracy" marketing figure.

## Vendor-specific Findings / Rejected Findings

**Rejected as definitional:**
1. *"Occupancy = sensor-based measurement"* — the sensing pole exists (VergeSense class) but self-describes as "occupancy intelligence/analytics", holds no allocation record, and integrates INTO management systems. Measurement is an L1/L2 input, not the Type's center.
2. *"Occupancy planning is the core"* — planning is 4/5 common (L1); the record-keeping legs (inventory + occupancy state + recorded changes) exist in all five and are the prerequisite for planning.
3. *"Chargeback is definitional"* — org-grain segments lean on it, pure-play corporate poles de-emphasize it; L1.
4. *"Hybrid-work booking/check-in machinery is the core"* — era-current (L2).
5. *"AI agents / 3D / digital-twin"* — era-current, single-vendor poles (L3).
6. *"Occupancy requires workspace-transaction data structures"* — Archibus-specific schema realization (L3); TRIRIGA realizes the same concept with allocation records.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (remove-test) |
|---|---|---|
| **Space Management Platform (§10)** | **same population — alias** | Market uses the phrases interchangeably: Archibus's own docs call its Space module "four areas of space and occupancy management"; FM:Systems titles space management "complete visibility into space and occupancy"; Capterra lists OfficeSpace's differentiators as "occupancy management, move management". No product found that satisfies "space & occupancy management" but not the space-management core, or vice versa. Both directory leaves kept; this record written from the occupancy articulation. |
| IWMS (§17) | module ⊂ suite | Space & occupancy is one domain inside the integrated real-estate/facility suite (TRIRIGA, Archibus, FM:Interact all sell it as a module); IWMS's differentiator is the multi-domain span + shared estate spine. |
| Facility Management System (§17) | adjacent | FMS's center is keeping the estate operating (maintenance/service work loop); here the center is the space/occupancy record. FMS products *consume* the space inventory ("prerequisite" per Archibus docs). |
| Workplace Management Platform / Office Operations Platform (§10) | adjacent | Those center the employee-facing reservation/coordination surface + workplace-team operations loop (booking, requests, communications); here the center is the managed space inventory and its occupancy record. Pure booking suites fail this Type's legs 1+3+4. |
| Building Management System (§17) | different layer | BMS controls plant (equipment, sensors, setpoints); this Type records places and the people/organizations occupying them. |
| Amenity Booking Platform (§17) | adjacent | Time-bound reservations of shared amenities vs the persistent allocation/occupancy record; booking is one state a space can carry here, not the center. |
| Coworking / Flexible Workspace Management (§17) | opposite side | Operator-side revenue business (memberships, bookable/allocatable units for sale) vs occupier-organization-side internal record. |
| Hotel PMS (§26) | different domain | Transient guest stays with folio/payment vs durable organizational allocation of the occupier's own space. |
| Lease Administration (§17) | adjacent | Lease obligations/financials vs the space record itself; lease admin reads space context, not vice versa. |
| Occupancy sensing / analytics (NOT a directory leaf; VergeSense/Density class) | upstream measurement layer | Measurement feeds the Type (L2 input); it holds no inventory, no assignments, no moves, no chargeback. If a "management" claim appears here, it is analytics-on-workplace-stack, not this Type. |
| Architecture Design / CAD (§16) | different stage | Authoring construction documents vs operating the occupied-space record. |

## Historical / Market-Sample Check

- Pre-digital practice: institutional space inventories with occupancy registers — universities and government agencies tracking rooms, departmental allocation, and chargeback on paper floor plans and ledgers; corporate facilities departments keeping "who sits where" against annotated plans. This satisfies all four L0 legs at analog level (inventory register + plans + occupancy assignments + recorded changes through move paperwork). ✓
- CAFM/CAD era: FM:Systems founded 1984 explicitly as an "office space management system"; TRIRIGA's own docs (© 2011–2024) describe the same four legs with era machinery only (CAD integration, web forms). ✓
- Era-current machinery (sensors, badge/WiFi feeds, hybrid booking, AI agents, 3D/digital twin, cloud vs on-prem) is consistently L1/L2/L3 — the core stands without it. ✓
- The phrase itself: "space and occupancy" is long-established vendor vocabulary (TRIRIGA manuals, Archibus help, FM:Systems pages across ≥ a decade), denoting the same domain throughout. ✓

## Uncertainties

1. Whether any product exists that manages occupancy assignments with NO spatial representation at all — none found in sample; such a product would also fail the sibling's leg 2. Held as an open empirical question, not affecting the determination.
2. OfficeSpace/SpaceIQ official help centers unreachable (this pass and sibling pass) — their contribution to the core determination is corroborative only; Tier-1 anchors (TRIRIGA, Archibus) carry the exact-phrase evidence.
3. The sensing pole's full behavior is known from marketing pages only; the boundary claim (no record of record) is "by absence in its own positioning" — reasonably strong but not doc-grade.
4. Relative market weight of pure-play vs suite-module packaging is not asserted (no reliable numeric evidence).
5. Precise metric definitions (occupancy rate formulas, area standards) vary by product/regime; deliberately not canonicalized.

## Final Synthesis

**ALIAS RESOLVED with Space Management Platform** (§10 sibling, processed 2026-09-08; that pass's pre-hung alias suspicion DISCHARGED from this side). The §17 leaf **Space & Occupancy Management** denotes the same product population as the §10 Space Management Platform: the occupier organization's system of record for its physical space inventory and the occupancy state of every space, kept current by recorded space-changing operations. Vendor evidence is direct: Archibus's official documentation describes its Space module as "four areas of **space and occupancy management**"; FM:Systems titles its space management product "complete visibility into **space and occupancy**"; TRIRIGA's space-management documentation defines the feature as maintaining space plans while "updating the **occupancy**" through people assignments and organization allocations; the pure-play poles (OfficeSpace, SpaceIQ) present the identical feature set under the "space management" name, with third-party listings naming "occupancy management" among their differentiators. No product was found that satisfies one phrase and not the other.

Both directory leaves are kept; each documented from its own lens (this record emphasizes the occupancy articulation: occupancy state at person and organization grain, occupancy planning, occupancy analytics). The IWMS pass's keep-both note (space as suite domain vs standalone platforms) is unaffected. No directory change.
