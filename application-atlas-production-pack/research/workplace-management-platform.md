# Research Notes — Workplace Management Platform

## Research Goal

Understand what the market sells under the label "Workplace Management Platform": which products carry this label, what capability bundle sits at its center, whether the label names the same market territory as the already-documented Office Operations Platform (§10 sibling, processed 2026-09-08 with a pre-hung joint-review flag naming this leaf), or a defensibly different Type, and where the label's edges drift (booking-led products below the Type; IWMS-suite usage above it).

## Initial Boundary

Hypothesis before research: the leaf sits in §10 Enterprise Operations & Administration adjacent to "Office Operations Platform" (processed same day), "Space Management Platform" (processed), "Facility Management System" (processed), and "Integrated Workplace Management System / IWMS" (unprocessed). The office-operations pass recorded: "the market uses 'workplace management platform' (Envoy, OfficeRnD), 'workplace operations platform' (Robin), 'office management software' (Robin heritage; Eden persona), and 'workplace experience applications' (Gartner category cited by Robin) near-interchangeably for the same capability cluster (booking + visitors + requests + deliveries + comms + analytics)" — joint review pre-hung on this pass.

Expected confusions:

- vs Office Operations Platform (processed sibling): probable near-alias; this pass must resolve the joint review with removal tests.
- vs Space Management Platform: space inventory, allocation, moves, floor-plan planning discipline.
- vs Facility Management System: estate-anchored maintenance work orders.
- vs IWMS: suite packaging integrating space + facility + real estate; some vendors use "workplace management" for exactly this (label drift to verify).
- vs Resource Calendar / desk & room booking: booking-only thin pole.
- vs Enterprise Request Management, Building Access & Visitor Management, Coworking / Flexible Workspace Management, Employee Portal / Intranet.

## Research Questions

1. Which vendors self-label "workplace management platform" (or close variants), and what capability bundle do they ship at the center?
2. Does the label-side population satisfy the office-operations-platform defining core (operated office of record + employee-facing reservation surface + office-team service loop)? Leg-by-leg, per product.
3. Does the label carry any additional invariant not already in the sibling's core — or is it the same Type under a second name?
4. How do booking-led products (thin pole) and suite vendors (umbrella pole) use the label, and what does that drift imply for the definition?
5. Historical check: would pre-hybrid-era deployments and the paper-era office toolkit satisfy the definition? Would older IWMS-style "workplace management" usage fit or fail?
6. Where are the seams vs Space Management, FMS, IWMS, Resource Calendar, ERM, Visitor Management, Coworking Management?

## Representative Products

Selected for market representation, label fidelity, documentation depth, different product philosophies, and different customer tiers:

| Product | Self-positioning (verbatim) | Philosophy | Tier | Evidence depth |
|---|---|---|---|---|
| Envoy | "Unite people, spaces, and communications on one workplace management platform—built for modern security and compliance" | security/compliance-first platform + modules | enterprise | dedicated platform page + FAQ (this pass); help-center evidence carried from the office-operations pass (same date) |
| OfficeRnD | nav: "Workplace Management — Robust Platform for Modern Workplaces"; "hybrid workplace management solution" | calendar-native, "app-less" employee experience | mid-market | product page + dedicated Helpdesk page (this pass, both) |
| Robin | homepage title: "A New Era of Workplace Management"; "the leading workplace operations platform" | operations-unification for workplace/facilities/IT teams | mid-market/enterprise | homepage this pass (help center previously unreachable — sibling pass, 2 timeouts) |
| Skedda | page title: "Workplace Management Software"; subtitle: "the world's leading space booking and scheduling software" | booking-led pure-play (thin-pole test) | SMB/mid-market | homepage this pass |
| Eptura (Condeco) | "Condeco has been rebranded to Eptura Engage. The #1 bookings solution… book rooms and desks… for your global corporate offices" | enterprise suite umbrella (Engage/Workplace/Visitor/Asset apps) | enterprise/global | Condeco migration page this pass |
| FM:Systems | "Integrated Workplace Management Software"; "FM:Systems' complete Workplace Management Platform" | IWMS-suite usage of the label (boundary data point, not a sample member) | enterprise | homepage this pass |

Deliberately not sampled: Eden, OfficeSpace (sampled by the sibling/space passes), pure visitor-management vendors (Building Access & Visitor Management territory), room-display devices (Resource Calendar territory), coworking operators' software (OfficeRnD Flex noted as boundary data point from the same vendor).

## Sources

All fetched 2026-09-08 (this pass):

- Envoy — homepage: https://envoy.com/ ; dedicated platform page with FAQ: https://envoy.com/workplace-management-platform
- Envoy help center (Tier-1; fetched in the office-operations-platform pass, same date): https://envoy.help/en/ — Workplace Ticketing collection ("Report workplace issues from the Envoy mobile app, integrated with ServiceNow, Jira and more")
- OfficeRnD — product page: https://www.officernd.com/hybrid-workplace-management-software/ ; Helpdesk module page: https://www.officernd.com/hybrid-work-software/helpdesk-management-software/
- Robin — homepage: https://robinpowered.com/ (help center https://support.robinpowered.com/hc/en-us timed out twice in the sibling pass; not retried per network rules)
- Skedda — homepage: https://www.skedda.com/
- Eptura/Condeco — Condeco migration page: https://www.condecosoftware.com/
- FM:Systems — homepage: https://fmsystems.com/ (boundary data point only)
- Sibling context (no fetch): applications/office-operations-platform.md, research/office-operations-platform.md, applications/space-management-platform.md, applications/facility-management-system.md

## Product A — Envoy

### Key observations (evidence layer A unless noted)

- Homepage: "Unite people, spaces, and communications on one workplace management platform—built for modern security and compliance." Meta description: "Trusted visitor management, workplace management, and emergency management."
- Dedicated platform page: "Envoy unifies visitors, spaces, and communications into one enterprise-ready workplace management platform and ecosystem—so teams can operate securely, stay compliant, and scale with confidence." Structured-data self-description: "an enterprise workplace management platform that unifies visitor management, space booking, communications, and operational analytics."
- Vendor's own FAQ definition of the domain: "What is workplace management software? Workplace management software helps organizations coordinate people, spaces, and onsite operations. It brings together tools for visitor access, space booking, communications, analytics, and compliance in one system."
- Packaging: platform tiers (Premium: dashboard, core integrations Slack/Teams/calendars, basic analytics, maps with image upload + POIs, SCIM/SSO, SMS, mobile app for admins and employees; Enterprise adds presence signals "HRIS, MDM, WiFi, ACS, SSO, Geo", advanced analytics, custom admin roles, event log). "*Platform must be purchased with at least one module (Reservations, Emergency Notifications, Screens, or Deliveries)". FAQ: "Do I need the platform to use Envoy products? Yes."
- Modules: Visitor management ("secure, compliant pre-registration, screening, and check-in"), Resource booking ("real-time room, desk, and parking management"), Mailroom management ("accurate digital delivery records and automated notifications"), Critical event management, Digital signage, Workplace analytics ("occupancy, utilization, and presence insights powered by passive data signals").
- Employee-facing actions (leg 2): "Instantly reserve rooms, desks, or parking directly via the Envoy mobile app, calendar invites, or the interactive live map"; "Empower teams to navigate the workplace effortlessly—from locating coworkers to finding the right space"; "Book a space, find a teammate, reserve parking, and check in with ease."
- Operated-place record (leg 1): maps, rooms, desks, parking as bookable inventory; "Whether you manage one location or dozens."
- Service loop (leg 3): from the Envoy help center Workplace Ticketing collection (evidence carried from the sibling pass, same date): "Report workplace issues from the Envoy mobile app, integrated with ServiceNow, Jira and more."
- Compliance emphasis: "Mitigate risk and uphold compliance with regulations like ITAR, CMMC, EAR, OFAC, and C-TPAT"; "audit-ready records"; personas: security, facilities, enterprise IT, HR, C-suite, employees. Integrations: access control (Avigilon, Brivo, LenelS2, Genetec, Honeywell), identity (Okta, Entra), calendars, Teams/Slack, ServiceNow, DocuSign.
- Reading: Envoy carries all three legs; the label's center is people + spaces + communications on an operated workplace, with security/compliance as its differentiating posture.

## Product B — OfficeRnD

### Key observations (evidence layer A)

- Navigation label: "Workplace Management — Robust Platform for Modern Workplaces" — the literal leaf label. Product pitch: "Build Thriving Global Teams with Hybrid Work Software… an all-in-one hybrid workplace solution… book desks and spaces with ease, manage meeting rooms and collaborate."
- Modules: Desks (desk booking), Meetings (room scheduling), Parking, Helpdesk ("Simplify workplace issue reporting and requests"), Experience (collaborative scheduling), Visitor Hub ("Delight guests and streamline delivery management"); plus Booking policies ("custom policies for your team's office days"), Workplace analytics, Presence tracking ("track employees' presence with check-ins"), Space management ("enable hot desking or office hoteling practices").
- Employee loop (leg 2): "Seamlessly book your preferred spaces… with our intuitive and user-friendly interactive floor plan"; "Navigate through interactive office maps / Filter to find the right space and resources / Make bookings private or recurring / Save time by booking in bulk for the entire team"; "See who's in each day / Get suggestions for best onsite days / Plan a weekly hybrid schedule / Send and receive invites."
- Service loop (leg 3) — direct fetch of the dedicated Helpdesk page: "Give employees a quick and easy way to report workplace issues, submit requests, and follow their progress, all from the OfficeRnD Workplace app." Mechanics: report "broken equipment, maintenance problems, IT issues, or workplace feedback" from web portal or mobile app; custom request categories; employee-selected severity; two-way ticket communication; complete issue history; automatic routing ("custom categories and choose who should be notified… Requests go directly to the people responsible… without manual forwarding"); "Different routing rules for every location"; named responders per category; internal admin priority distinct from employee severity; clear ticket statuses; automatic closure of inactive pending tickets; CSV export; "identify recurring problems, high-maintenance locations"; "Helpdesk is built into the same platform used for desks, rooms, parking, visitors, announcements, and employee feedback"; "One platform instead of another standalone tool."
- Operated-place record (leg 1): desks/rooms/parking per location; per-location helpdesk configuration; multi-location support.
- Posture: "App-less experience — No new apps or tabs needed for Microsoft and Google organizations" (Teams, Outlook, M365, Google Calendar, Slack).
- G2 positioning: Leader badges for Desk Booking, Meeting Room Booking Systems, Space Management, Hybrid Enablement.
- Boundary data point from same vendor: OfficeRnD Flex (coworking management: members, bookings, billing, e-commerce, AI demand capture) is a separate product line for workspace operators — operator-side vs occupant-organization-side seam inside one vendor.
- Industries: higher education, healthcare, tech, financial services.

## Product C — Robin

### Key observations (evidence layer A; product-page level)

- Homepage title: "A New Era of Workplace Management". Platform claim: "Double the effectiveness of the office in half the time with the leading workplace operations platform"; "Bring booking, operations, and space planning together in one platform built to take the work out of running your workplace."
- Modules: Resource booking ("Book desks, rooms, lockers, parking and more with AI"), Space management ("Collaboratively plan, edit and execute office updates"), Meeting management ("Reduce conflicts, right-size meetings and handle requests"), Workplace analytics, Visitor management ("fast check-ins, badges, and host notifications… Track deliveries and notify recipients when packages arrive"), Employee experience ("Share announcements, gather feedback and plan office events"), Room displays, Wayfinding, Access control, Microsoft/Google integrations.
- Personas (all three legs visible): Workplace managers — "Orchestrate team days… Set in-office policies, see what's working… Get a real-time 360° view of the workplace: See who's in, how spaces are used and capture feedback"; Facilities — "Manage resources, deliveries and services all in one place… Plan, share and execute office moves, transitions and layout adjustments"; IT — "Track requests in one place: Capture tech and AV tickets, automatically route them to the right team and keep requesters in the loop" and "Connect systems, reduce tickets."
- Employee-facing actions: "Use AI to book desks and spaces and bring people together"; "Book resources in the apps they already use – Teams, Slack, Outlook, mobile and more."
- Market-category evidence: "Robin Named a Leader in Gartner's Magic Quadrant [for Workplace Experience Applications]" (inaugural MQ).
- Reading: Robin carries all three legs; "workplace management" and "workplace operations" used as synonyms on one page (title vs platform claim).

## Product D — Skedda (thin-pole test)

### Key observations (evidence layer A)

- Page title self-labels "Workplace Management Software"; subtitle and footer: "the world's leading space booking and scheduling software"; badge claim "#1 Space Management Solution." "One platform to book space and manage operations, backed by the data to justify every square foot."
- Capabilities: self-serve booking for desks, rooms, and resources; automated booking rules ("Approvals, quotas, priority windows, and check-in rules control when, where, and how people book, and release seats that go unused"); interactive maps; neighborhoods; custom roles/permissions; Wi-Fi-based occupancy detection ("shows who's in"); utilization insights ("Workplace Intelligence": desk and room usage, peak hours, booking patterns).
- Visitor management: "Seamless visitor check-in and check-out, with admin notifications"; "QR code self-check-in"; "Package and delivery logging."
- Integrations: two-way Microsoft 365/Google sync, native Teams and Slack apps, Zoom links; SSO (Okta/Entra/Google/JumpCloud/OneLogin), SCIM; SOC 2 Type II.
- Use cases extend beyond offices: labs, parking, universities, community spaces, music studios, sports facilities, consulting rooms — space booking as the invariant, office as one market.
- **No service-request/ticketing machinery observed on the fetched page** — absence on fetched pages only, not asserted as product absence. A customer quote frames ticket reduction as an outcome of booking self-service ("The fact that we don't get phone calls and tickets proves how easy it is") — tickets here are booking questions, not a workplace service loop.
- Reading: Skedda satisfies legs 1+2 and fails leg 3 on fetched evidence — a booking suite borrowing the "workplace management" label for SEO reach. Confirms the label is used loosely below the Type.

## Product E — Eptura / Condeco (umbrella-pole test)

### Key observations (evidence layer A)

- Condeco's site is a migration page: "Condeco's website has been migrated to eptura.com. Condeco has been rebranded to Eptura Engage. The #1 bookings solution is now Eptura Engage. Connect your teams, book rooms and desks, and managing catering requests for your global corporate offices."
- Eptura platform structure (nav): Platform ("How enterprises run the physical world"; "Intelligent Workplace — Connect people and workplaces"; "Integrated Operations — Asset and operational uptime"; "IWMS for complex environments — FedRAMP Authorized"); Platform Apps: **Asset** ("Facility maintenance and asset management"), **Engage** ("Workplace experience and hybrid work"), **Workplace** ("Workplace operations and space management"), **Visitor** ("Building security and visitor experience"); Specialized: Archibus ("FedRAMP Authorized and on-premise IWMS"), Serraview ("Portfolio and real estate management").
- "Eptura is a Leader in Gartner® Magic Quadrant™ for Workplace Experience Applications."
- Reading: at suite vendors, "workplace" is an umbrella spanning bookings (Engage), operations + space (Workplace app), security (Visitor), and maintenance/assets (Asset) — i.e., the label stretches across several sibling Types. The office-operations slice (Engage + Visitor + service handling) is one part of the umbrella.

## Boundary data point — FM:Systems (label drift, historical/enterprise usage)

- Self-labels: "Integrated Workplace Management Software"; "FM:Systems' complete Workplace Management Platform"; "An integrated space and facility management platform to create exceptional workplace experiences, improve portfolio performance, drive building efficiencies, support workplace mandates and enhance well-being."
- Product families: OpenBlue Workplace (Space Management, Move Management, Strategic Planning, Real Estate & Lease, Project Management); Facility Operations (Facility Management, Facility Maintenance, Asset Management, Work Order Ticketing, Preventative Maintenance, Sustainability); OpenBlue Employee (Workplace Experience: Desk Booking, Interactive Floorplans, Room Scheduling, Catering & Workplace Services, Panels & Kiosks, Visitor Management); OpenBlue Insights (Portfolio/Utilization/Booking/Sensor Analytics). Part of Johnson Controls.
- Reading: in the IWMS tradition, "workplace management" names the integrated space + facility + real-estate platform of record — the same words as the current workplace-experience cluster, a different (suite) center of gravity. The directory already holds a separate IWMS leaf, so this is recorded as label drift, not a second Type for this leaf. Note the pattern: even here, the workplace-experience slice (desk booking, floor plans, room scheduling, catering, visitors) appears as one product family among four — the operational core recurs inside the suite.

## Cross-product Comparison

| Capability | Envoy | OfficeRnD | Robin | Skedda | Eptura/Condeco | Reading |
|---|---|---|---|---|---|---|
| Self-labels "workplace management" | ✓ dedicated page + FAQ | ✓ nav label | ✓ page title + "operations platform" synonym | ✓ page title (alongside "space booking") | umbrella app "Workplace"; Engage = bookings | label spans the cluster and its edges |
| Operated workplace of record: locations + bookable resources | ✓ (maps, rooms, desks, parking) | ✓ (desks, rooms, parking per location) | ✓ (desks, rooms, lockers, parking) | ✓ (desks, rooms, resources; also labs/parking) | ✓ (rooms, desks, catering; per "global corporate offices") | Universal |
| Employee-facing reservation & coordination surface | ✓ (mobile app, calendar invites, live map; "find a teammate") | ✓ (floor plan, bulk/recurring/private booking, who's-in, suggested days, invites) | ✓ (Teams/Slack/Outlook/mobile, AI booking, who's-in) | ✓ (self-serve booking, map, neighborhoods, who's-in) | ✓ (book rooms and desks) | Universal; surface varies (native app ↔ app-less) |
| Presence / who's-in | ✓ (presence signals HRIS/MDM/WiFi/ACS/Geo on Enterprise) | ✓ (presence tracking with check-ins) | ✓ ("see who's in") | ✓ (Wi-Fi-based occupancy detection) | not observed on fetched pages | Common |
| Service loop: requests routed to teams | ✓ (Workplace Ticketing — help-center evidence, sibling pass) | ✓ (Helpdesk: categories, named responders, per-location routing, statuses) | ✓ (tech & AV tickets auto-routed, requesters kept in loop) | **not observed** (booking questions framed as the tickets it eliminates) | service handling not observed on fetched page; sibling app "Asset" carries work orders | 3/5 label-side products show it directly; its absence defines the thin pole |
| Visitor management | ✓ (core module) | ✓ (Visitor Hub) | ✓ (module) | ✓ (QR check-in, delivery logging) | ✓ (Visitor app: "building security and visitor experience") | Universal in sample — but module-gated at Envoy |
| Mail & deliveries | ✓ (Mailroom module) | ✓ (Visitor Hub: delivery management) | ✓ (under visitor mgmt) | ✓ (package and delivery logging) | not observed | Common |
| Announcements / employee comms | ✓ (in "people, spaces, and communications"; signage) | ✓ (announcements, feedback) | ✓ (Employee experience module) | not observed | not observed | Common |
| Occupancy / utilization analytics | ✓ (Workplace analytics) | ✓ (Workplace analytics) | ✓ (Workplace analytics) | ✓ (Workplace Intelligence) | ✓ (Insights family at sibling level) | Universal |
| Calendar/collab-suite integration | ✓ | ✓ (defining "app-less" posture) | ✓ | ✓ (two-way sync, native Teams/Slack) | ✓ (Microsoft partnership page) | Universal |
| Space planning / moves | partial (map drafts, space planning with insights — sibling-pass evidence) | ✓ (space management: hot desking/hoteling) | ✓ (named Space management module; "execute office moves") | not observed | ✓ (Workplace app: "space management"; Serraview: portfolio/RE) | Common; deep planning = Space Management seam |
| Facility maintenance / assets | not observed | not observed | not observed | not observed | ✓ (Asset app; Archibus IWMS) | Umbrella drift only — not part of the label's center |
| Emergency / critical events | ✓ (CEM module) | not observed | not observed | not observed | not observed | Optional (Envoy pole) |
| AI assistance | not observed on fetched pages | not observed | ✓ ("with AI", AI insights) | not observed | "Eptura AI" | Optional, era-current |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures — independently derived on this pass, and matching the office-operations pass's operational center:

1. **The operated workplace of record** — the organization's own workplace location(s) held as managed records carrying their shared workplace resources (meeting rooms universally; desks, parking, and other resources commonly) as bookable inventory. Remove → a booking backend with no operated workplace, or space-inventory territory.
2. **The employee-facing reservation and coordination surface** — employees directly discover availability, reserve shared resources, see who is in, and coordinate onsite time through the platform (web, mobile, calendar, and chat surfaces). Remove → back-office facilities tooling; the employee stops being a user.
3. **The workplace team's operations loop** — employee-reported needs (issues, requests) and workplace services (deliveries, communications) are captured through the platform, routed to the teams that run the workplace (workplace/office/facilities/IT), and tracked with the requester kept informed. Remove → a pure booking suite (the Skedda/Engage thin pole).

Jointly-held is load-bearing:

- 1 alone = space inventory / booking machinery (Space Management or Resource Calendar territory)
- 1+2 without 3 = booking suite (Skedda pole) — booking software that borrows the label without being the Type
- 3 without 1+2 = generic internal ticketing (Enterprise Request Management territory)
- 1+3 without 2 = facilities back-office (FMS/ERM drift)
- 2+3 without 1 = unanchored point tools

Historical check (§24): pre-hybrid-era deployments (rooms + visitors + requests with fixed seating — the Condeco/Engage heritage shape) satisfy all three legs without desks, presence, or hybrid machinery. The paper-era office toolkit (reception visitor log, room-booking binder, mailroom ledger, requisition book, announcement board) satisfies all three legs at analog level. The IWMS-era usage of the label (FM:Systems) satisfies the legs only in its workplace-experience slice (desk booking + floor plans + room scheduling + catering + visitors); its space/facility/real-estate modules belong to sibling Types — so the definition names no suite packaging. Therefore desks, presence signals, hybrid policies, and analytics are NOT in the invariant; they are the current era's emphasis, consistent with the sibling pass's historical check.

### L1 — Common Mature Structure

Present across the sample, expected in mature products, not definitional:

- Visitor management pipeline (invites/pre-registration → host notification → check-in → badge → record; delivery logging commonly packaged with it)
- Mail & deliveries (log, notify, track pick-up)
- Announcements / employee communications (push/email/chat; signage)
- Presence & attendance (who's in, check-ins, external signals where offered)
- Occupancy & utilization analytics (bookings + check-ins + signals → dashboards)
- Calendar and collaboration-suite integration (Google/Microsoft, Teams, Slack) as both data source and booking surface
- Booking policies (office-day policies, quotas, approval and release rules)
- Floor-plan/map visualization of spaces and resources
- Multi-location administration (per-location categories, responders, policies)
- Room displays / digital signage (common, often module-level)
- Access-control integration (badge systems)

### L2 — Variant / Optional Structure

- Parking management; lockers and other resource classes
- Health & safety screening (era- and region-dependent)
- Emergency / critical-event management (Envoy CEM pole)
- Deep space planning and move management (Robin Space management module; FM:Systems Move Management; Eptura Workplace app) — the Space Management seam
- Catering and workplace services (OfficeRnD meeting services; Eptura Engage catering; FM:Systems Catering & Workplace Services)
- All-department internal ticketing vs workplace-scoped requests (sibling-pass variant, unchanged)
- Non-office space booking (Skedda: labs, universities, community spaces, studios) — the booking invariant generalized beyond offices
- Wayfinding; AI booking/coordination assistance (era-current)
- Deployment posture: standalone app vs embedded calendar/chat surfaces ("app-less")

### L3 — Vendor-specific (research notes only)

- Envoy: platform-tier + module packaging ("Platform must be purchased with at least one module"); presence-signal source list (HRIS/MDM/WiFi/ACS/SSO/Geo); CEM/Response with threat intelligence; compliance-regulation framing (ITAR, CMMC, EAR, OFAC, C-TPAT); integration catalog; Schema.org self-description.
- Robin: "Workplace Operations" framing; $9M workplace-friction report; AI-driven booking and space recommendations; Gartner MQ Workplace Experience Applications leader claim; persona pages.
- OfficeRnD: "app-less" headline posture; per-location helpdesk routing rules; automatic closure of inactive pending tickets; sibling product OfficeRnD Flex for coworking operators; G2 badge claims.
- Skedda: 8,000 customers / 28 countries / 3M active users claims; dedicated-specialist onboarding ("live in days, not months"); non-office use-case catalog; G2 "#1 Space Management" claims.
- Eptura: Condeco→Engage rebrand; four-app platform naming (Engage/Workplace/Visitor/Asset); Archibus and Serraview specialized products; FedRAMP positioning; Gartner MQ leader claim.
- FM:Systems: OpenBlue product-family naming; Johnson Controls ownership; 3B+ sq ft managed and other trust metrics.

## Vendor-specific Findings

See L3. Additionally: the same vendors stretch the label in both directions — Envoy extends into critical-event management (emergency-management territory) as a module; Eptura's "Workplace" app reaches into space management; FM:Systems uses the label for the whole IWMS. Module presence under a "workplace management" banner does not promote a capability into this Type's core.

## Rejected Findings

- **"Workplace management platform = IWMS"** — rejected as the definition. The IWMS usage (FM:Systems; Eptura's "IWMS for complex environments") is a real but older/suite-side usage of the same words; the directory holds a separate IWMS leaf. Recorded as label drift.
- **"The label names a broader Type than office operations"** — rejected. The additional areas under the label at suite vendors (space management, facility maintenance, real estate, assets) belong to sibling Types; the label's center of gravity — verified by its FAQ definitions (Envoy) and module structure (OfficeRnD, Robin) — is the same capability cluster the office-operations pass defined.
- **"Booking-led products define the floor of this Type"** — rejected. Skedda and the Condeco/Engage heritage satisfy only legs 1+2; they are the thin pole below the Type (booking suites), even though they borrow the label.
- **"Desk booking / hybrid machinery is definitional"** — rejected (historical check: pre-hybrid and paper-era shapes satisfy; Condeco heritage is rooms-first).
- **"Visitor management is definitional"** — rejected (5/5 sample presence, but Envoy sells it as a separate module on a required platform; a product without visitors remains recognizably this Type). Held as the strongest standard capability, matching the sibling pass.
- **"Emergency management is definitional"** — rejected (single-vendor pole; module-level).

## Boundary Findings

- **vs Office Operations Platform (§10 sibling, processed 2026-09-08) — JOINT REVIEW RESOLVED: near-alias, consolidation recommended.** The label-side population (Envoy, OfficeRnD, Robin) independently satisfies the sibling's defining core leg-by-leg: operated office of record (maps/rooms/desks/parking per location), employee-facing reservation surface (app + calendar + chat + map booking, who's-in), service loop (Envoy Workplace Ticketing; OfficeRnD Helpdesk with named responders and per-location routing; Robin tech/AV ticket routing). No additional invariant appears on the label side that the sibling's core lacks. Removal tests both directions: strip the service loop from Envoy/OfficeRnD/Robin → a booking suite remains (Skedda/Engage shape), not a new Type; add the label's edge content (space planning, facility maintenance, real estate) → the product drifts into Space Management/FMS/IWMS territory, not a bigger version of this Type. The two leaves name the SAME market territory — "workplace management platform" from the market-label angle, "office operations platform" from the operational angle; the same vendors use both phrases as synonyms on single pages (Robin: title "workplace management" vs claim "workplace operations platform"; Envoy FAQ defines "workplace management software" as the cluster). Recommendation: consolidate into one Type at a taxonomy pass; until then both documents stand and cross-reference, with the sibling's operational phrasing as the canonical center and this document carrying the label-side evidence and edge-drift record.
- **vs Space Management Platform (processed)**: keep-both. Space management centers the standing space inventory, allocation state, and recorded space-changing operations (assignments, moves, re-allocations). This Type centers running daily services around the occupied workplace. Robin ships "Space management" and Eptura a "Workplace [operations and space management]" app as named components — supporting the seam.
- **vs Facility Management System (processed)**: keep-both. FMS holds the estate and place-anchored maintenance work (work orders, PM, assets, costs); this Type's requests are workplace-service needs routed to workplace/IT/facilities teams without estate/asset/PM machinery. Confirmed again at Eptura: maintenance/assets live in a separate "Asset" app.
- **vs Integrated Workplace Management System / IWMS (§17, unprocessed)**: label-drift boundary. Suite vendors (FM:Systems; Eptura's Archibus line) use "workplace management" for the integrated space + facility + real-estate platform of record. This leaf's center is the operational/experience cluster, not the suite. Flag for the IWMS pass: the two leaves must be separated by the suite-of-record criterion (integrated multi-domain modules: real estate/lease, capital planning, facility maintenance), not by the word "workplace".
- **vs Resource Calendar / desk & room booking (§03.08–03.09)**: booking-only products (Skedda; Engage heritage) are the thin pole below this Type; the service loop (and commonly visitors/deliveries/comms) is the discriminator. Skedda's use of the label shows the market's naming does not respect this seam — the definition must.
- **vs Enterprise Request Management (processed)**: ERM is department-generic internal request fulfillment; this Type's service loop is anchored to the operated workplace. All-department ticketing products straddle (sibling-pass variant, unchanged).
- **vs Building Access & Visitor Management (§17)**: visitor management as building-security/access layer vs visitors as one workplace service among several. Envoy straddles (security-first posture, access-control depth, CEM) — held as variant posture, matching the sibling pass.
- **vs Coworking / Flexible Workspace Management (§17)**: operator-side commercial business (memberships, billing, member CRM) vs occupant-organization-side operations. Confirmed inside one vendor: OfficeRnD Flex vs OfficeRnD Workplace.
- **vs Employee Portal / Intranet (§10)**: org-wide information/services surfaces vs workplace-scoped operations and communication.

## Uncertainties

- Help centers were not fetched this pass: Envoy's help-center service-loop evidence is carried from the sibling pass (fetched same date); Robin's help center timed out in the sibling pass (not retried per network rules); Skedda, Eptura, and FM:Systems are documented at product-page level. Accordingly no precise numeric limits, default settings, time windows, or plan-gated feature details are asserted anywhere.
- Skedda's missing service loop is an absence-on-fetched-pages finding, not an asserted product absence; Skedda may ship request machinery elsewhere. The thin-pole verdict for Skedda rests on what its own homepage presents as the product.
- Eptura's "Workplace" app and Engage's service-handling depth were not documentable beyond the migration page (product-page 404 for the workplace app URL; one fetch attempt only). The umbrella reading rests on the app descriptions on the migration page.
- Regional/European label usage (CAFM tradition) not sampled; the IWMS label-drift finding may be broader than the two US-suite data points.
- The final consolidation of the two §10 leaves is a taxonomy-owner decision; this pass records the recommendation and the evidence but does not modify the directory.

## Final Synthesis

The Workplace Management Platform is the market-label name for the same Application Type the office-operations pass documented from the operational angle: the workplace team's operating system for the organization's workplace as a served place. Its defining core is three jointly-held structures — the operated workplace of record (locations + bookable shared resources), the employee-facing reservation and coordination surface (employees directly book, see who's in, coordinate onsite time), and the workplace team's operations loop (requests and services routed to the teams that run the workplace and tracked to resolution). Mature products standardly add the visitor pipeline, mail/deliveries, announcements, presence and occupancy analytics, calendar-suite integration, booking policies, and multi-location administration; optionally parking, health screening, emergency management, deep space planning, catering, and AI assistance. The label is used loosely at both edges — booking-led products below the Type borrow it, and IWMS suites stretch it across space, facility, and real-estate modules — which is itself evidence that the Type must be defined by its operational core rather than by the words vendors attach to it. Joint review with the office-operations-platform leaf is resolved as near-alias: consolidation recommended, both documents standing until a taxonomy pass merges them.
