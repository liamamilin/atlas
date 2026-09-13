# Research Notes — Climbing Gym Management

## Research Goal

Understand what software for managing a climbing gym (bouldering and/or rope climbing facility) actually is: which objects it manages, which workflows it runs, which structures are climbing-specific rather than generic fitness-business management, and where its boundary lies against generic Gym Management System and against climber-side climbing apps.

## Initial Boundary

Working hypothesis before research:

- Climbing Gym Management = operator-side business system for a climbing facility: members/memberships, front-desk check-in, waivers, classes/programs, retail, billing.
- Expected climbing-specific structures: routesetting/wall management (routes, boulder problems, grades, setters, set/strip cycles), belay/lead certification tracking, competition/league management, waiver-heavy onboarding.
- Nearest neighbors: Gym Management System, Fitness Membership Management, Fitness Class Booking, Sports Facility Management, Recreation Center Management (all in DIRECTORY §28 Sports, Fitness & Recreation); also climber-side route-logging apps (KAYA app, TopLogger consumer side) which are NOT this Type.
- Risk: the leaf could collapse into Gym Management System if no climbing-specific structure is definitional.

## Research Questions

1. What objects does the system manage (member, membership plan, visit/check-in, waiver, certification, route/problem, wall/area, class, competition, retail item)?
2. How is the routesetting lifecycle modeled, and is it part of the management system or a companion product?
3. How do memberships/passes work (recurring dues, punch cards, day passes, prepaid, corporate)?
4. How do waivers and certifications gate or annotate entry?
5. What are the main interfaces (front desk, back office, kiosk, member app/portal)?
6. What rules matter (waiver on file, certification status, balance due, membership status at check-in; billing decline lifecycle)?
7. Where is the boundary vs generic gym management and vs climber-side apps?

## Representative Products

Selected for market position + philosophy spread + documentation quality:

1. **Rock Gym Pro (RGP)** — the dominant climbing-gym-specific business management product (US-centric; also marketed to gun clubs, wake parks, skate parks). Philosophy: member-management-first. Deep Tier-1 help center accessible.
2. **KAYA (KAYA Gym)** — climber-side community app with a gym-facing routesetting/engagement/competition platform. Philosophy: wall-and-community-first. Official product pages accessible.
3. **GymMaster** — generic all-in-one gym management system (used by gyms across 110+ countries; representative of the non-climbing-specific pole that climbing gyms sometimes adopt). Official product site accessible.

Attempted but unreachable (see Sources): Vertical Softworks, Stökt, TopLogger, RhinoFit, Grifit, Climbing Business Journal industry article.

## Sources

Research date: **2026-09-07**

### Rock Gym Pro (Tier 1 help center + Tier 2 product site)

- Home: https://rockgympro.com/ (fetched)
- Help Center home: https://support.rockgympro.com/hc/en-us (fetched — full section tree)
- Customizable Proficiency Levels / Belay Certifications: https://support.rockgympro.com/hc/en-us/articles/360056601832-Customizable-Proficiency-Levels-Belay-Certifications (fetched)
- Check-ins and Check-outs: https://support.rockgympro.com/hc/en-us/articles/360056602972--Check-ins-and-Check-outs (fetched)
- RGP Membership Billing Lifecycle: https://support.rockgympro.com/hc/en-us/articles/360056602412-RGP-Membership-Billing-Lifecycle (fetched)
- Customer Information Displayed at Check In and POS: https://support.rockgympro.com/hc/en-us/articles/360056601792-Customer-Information-Displayed-at-Check-In-and-POS (fetched — image-only article; screenshots not readable, no text claims drawn from it)

### KAYA (Tier 2 official product pages)

- Home: https://kayaclimb.com/ (fetched)
- Gyms / KAYA Gym: https://kayaclimb.com/forgyms (fetched — feature lists, FAQ, pricing posture)

### GymMaster (Tier 2 official product site)

- Home: https://www.gymmaster.com/ (fetched — feature pages linked but not individually fetched)

### Source-access Limitations

- **Vertical Softworks** (verticalsoftworks.com / www) — transport error ×2. Abandoned per retry rule.
- **Stökt** (stokt.io, stokt.com) — empty responses ×2. Abandoned.
- **TopLogger** (toplogger.nu, /en, support.toplogger.nu, app.toplogger.nu) — JS-only SPA shell + transport error. Abandoned.
- **RhinoFit** (rhinofit.ca) — bot-verification interstitial ×2. Abandoned.
- **Grifit** (grifit.io) — transport error. Abandoned.
- **Climbing Business Journal** "Apps for Routesetting Management" — HTTP 403. Abandoned.

Consequence: the climbing-specific business-management pole beyond RGP is under-sampled, and the routesetting-companion pole is evidenced by KAYA Gym only (TopLogger/Stökt named as market context from KAYA's own competitive reference, not independently verified). All cross-product claims below are restricted to the three sampled products; market-landscape statements are marked as such.

## Product A — Rock Gym Pro (RGP)

### Key observations (evidence layer A = directly observed unless noted)

**Positioning (Tier 2):** "An All-in-One Member Management Software for High-Volume Facilities … tailored for climbing gyms, gun clubs, fitness & recreation, and similar high-traffic facilities." Feature pillars on the official site: Integrated Digital Waivers, Member Management, Point-of-Sale, Check-In, Online Booking & Calendars, Reporting & Analytics. Marketing stats (claims, not independently verified): 25M+ unique users, 100M+ check-ins, $2B+ transactions.

**Module map (Tier 1 help-center section tree):**

- Initial Set Up / Deployment: RGP Cloud client OR locally hosted/installed version (MySQL on premise); front-desk and back-office hardware requirements; receipt printer + cash drawer setup; webcam support.
- Staff Management: staff roles and permissions, access levels, employee PINs, time clock, job types.
- Customer Management: customer records (view/edit window, custom attributes, tags, bulk actions); account statuses with start/end dates (freeze, terminate); Memberships and Punch Cards (EFT billing details, future dues, entity/corporate memberships, prepaid); Online Membership Change Request Form (freeze/unfreeze/cancel/update payment, submitted from the gym's website); Daily Auto-Tagging Rules; **Customizable Proficiency Levels / Belay Certifications**; Youth Program Groups (program products, youth team dues added to memberships, freezing youth participants).
- Waivers: RGP-native digital waiver forms (design, multiple forms, waiver station/kiosk deployment, iPad/website URLs) + Smartwaiver integration; document management (document types, classification barcodes, scanning paper documents, bulk import); waiver-expiry email triggers.
- Checking In: check-in kiosk (online kiosk setup/overview), check-in via barcode key tags / mobile / manual lookup; check-out feature; kiosk operating modes (check-in only / check-out only / combined toggle with re-scan lockout); customer information and notices/statuses displayed at check-in and POS; check-in history per customer; checking in through POS.
- Calendar and Booking System: offerings, events, schedule building, reservation time slots, resources (party room, facility hours), instructors, waitlists, custom questions per offering/booking, deposits/balances to POS, cancellations/restorations, no-show balance voiding, website widgets (booking, occupancy), gift cards, promotional codes.
- Online Memberships and Punch Passes: selling memberships/punch passes online (website widgets, kiosk), enrollment/one-time fees, specials.
- Payment Processing / Billing: integrated gateways (RGP Stripe Custom, OpenEdge/XWeb, ACHWorks); POS transactions (discounts, returns, adjustments, gift cards, quick buttons); Billing lifecycle (see below); automated billing (Cloud only); decline minimizer (auto card updater).
- Reports: grid reports, custom reports, custom SQL, charting, customer queries (constraint-based, e.g. filter by proficiency/belay level), mobile/web dashboard, insurance-renewal reports, contact-tracing report.
- Multigym: multi-location management, archived/placeholder customer records, multigym documents.
- Email: transactional email system (requires external SendGrid account), email actions, email queue.
- API: documented REST API.

**Belay certifications / proficiencies (Tier 1, direct):** gym defines its own proficiency labels (e.g., belay certification) in settings; proficiencies attach to customer profiles; if at least one proficiency is configured, check-in and POS display a warning box when the customer lacks an assigned proficiency; renaming propagates; used proficiencies cannot be deleted; bulk assign/clear via customer queries filtered on "Policies – Proficiency / Belay Levels" + tags + actions. Wording is "proficiency levels / belay certifications" — the mechanism is generic proficiency tracking, climbing-cert being the canonical use.

**Check-in / check-out (Tier 1, direct):** kiosk modes for check-in only, check-out only, or both (toggle by repeated barcode scan, with a short re-scan lockout — 30 seconds in current version, product-specific detail); scanning shows customer details "with the same notices/statuses as when they check in"; manual check-out also exists; check-in window exposes check-in history, invoices/payments, and documents for the customer.

**Billing lifecycle (Tier 1, direct):** requires a third-party payment gateway; monthly cycle = before billing (process membership-change requests, resolve "members with warnings") → day of billing (Post Dues = create invoices + advance billing date; or one-click "Billing Launch"; or scheduled Automated Billing on Cloud) → after (retry declined cards days later, add late fees, terminate & reverse dues for long-declined members). Declined members receive transactional email with a link to update payment info. The documented example decline email states "members MUST pay past due balances prior to climbing" and a termination-after-N-days policy — note: these are template examples with placeholder values, not verified product defaults.

**What was NOT found:** no help-center section and no article referencing routesetting, walls, routes, boulder problems, grades, or setters in any of the fetched RGP surfaces. Absence observed only within the fetched sections; stated as "no routesetting capability found in the researched documentation," not as an absolute claim.

## Product B — KAYA / KAYA Gym

### Key observations

**Positioning (Tier 2):** KAYA is "The Climber's App" — consumer side: digital guidebooks (outdoor), beta videos, ascent logging/statistics, social features (follow gyms/areas, fist-bumps, comments). The gym-facing side, "KAYA Gym", is pitched as: "ENGAGE YOUR COMMUNITY, RUN COMPETITIONS, and MANAGE YOUR ROUTESETTING."

**Routesetting management (Tier 2, direct):**

- Create daily sets + climbs; assign grade, color, and setter "with just a few taps"; add movement-style and climb-characteristic tags, set photos, beta videos.
- Interactive gym map with filters/toggles for exploring setting and customer data.
- Distribution targets (grade distribution to hit when setting) and setting rotation targets (which wall area is due for turnover).
- Setter productivity metrics; time-based reporting (daily/weekly/monthly); CSV export.
- Setting quality metrics: star ratings and community grading (climber feedback on perceived difficulty).
- New Set Notifications pushed to climbers following the gym.

**Member engagement (Tier 2, direct):** gym news feed; gym info surfaced in the app (membership rates, day pass info, waiver linking); climbing-trend analytics; "digital comment card" via climber feedback; community stats (monthly active users, climber ability distribution, ascent demographics by grade).

**Competitions / leagues (Tier 2, direct):** event platform for on-the-wall challenges: solo or team formats, categories with auto-placement, attempts deduction, multi-week league scoring intervals, custom point values, "auto-bump sandbag detection", digital live leaderboards replacing paper scorecards, external/restricted registration links.

**Scope boundaries (Tier 2, direct):** KAYA Gym does not process memberships/billing — the app *displays* gym info (rates, day pass info, waiver links) but the commercial transaction layer is not part of the pitch; FAQ confirms no routesetting-only package (routesetting is bundled with engagement/competition); pricing is per location, single tier (specific numbers are vendor claims, research notes only). Stats claimed: 4K+ routesetters, 750K+ boulders set, 220K+ routes set, 300+ gyms (vendor claims).

**Market context (from KAYA's page, not independently verified):** KAYA cites Climbing Business Journal's Grip List "favorite routesetting app" awards (2022–2025) and a CBJ article on "Apps for Routesetting Management in 2022" — evidence that routesetting software is recognized as its own product category in the climbing industry.

## Product C — GymMaster (generic pole)

### Key observations

**Positioning (Tier 2):** "Easy to use Gym Management Software … all-in-1"; flagship differentiator is built-in 24/7 bluetooth door access control ("no third party"). Feature set: 24/7 access control, integrated billing, POS & stock control, member management, online booking (classes, PT sessions, pools, saunas), online signups/website integration, member app (book, check in, profile, workouts, visitation), automation & marketing/retention tools, lead management & sales funnel, tailgating detection, reporting APIs.

**Climbing relevance:** nothing climbing-specific appears on the fetched surface — no walls, routes, grades, belay, waivers-as-flagship. GymMaster represents the generic fitness-business pole that some climbing gyms adopt; its core loop (member + billing + access + booking + POS) is the same business spine RGP implements.

**Use as comparison anchor:** confirms that the member/billing/check-in/booking/POS core is NOT climbing-specific; whatever makes Climbing Gym Management its own Type must live in the structures around that core.

## Cross-product Comparison

| Structure | RGP (climbing-specific business) | KAYA Gym (wall & community) | GymMaster (generic) | Assessment |
|---|---|---|---|---|
| Customer/member records with statuses | ✔ (core) | ✖ (displays gym info only) | ✔ (core) | shared business core |
| Entry entitlements: memberships, punch passes, day passes | ✔ (EFT, prepaid, punch, entity/corporate) | ✖ (displays rates) | ✔ (membership plans) | shared business core |
| Check-in / visit recording | ✔ (kiosk, barcode, manual; check-out too) | ✖ | ✔ (member app check-in, 24/7 door access) | shared business core |
| Recurring billing + decline handling | ✔ (full lifecycle) | ✖ | ✔ (integrated billing) | shared business core |
| Retail POS + inventory | ✔ | ✖ | ✔ | shared business core |
| Class/program booking + resources + instructors | ✔ | ✖ (events only) | ✔ | shared business core |
| Waiver management | ✔ (flagship feature; kiosk stations; expiry triggers) | partial (waiver *linking* displayed in app) | not surfaced as flagship | strong in climbing-specific pole; near-universal in industry |
| Proficiency / belay certifications on customer + check-in warning | ✔ (direct) | ✖ | ✖ | climbing-segment structure (rope gyms); not in generic pole |
| Wall/route management (routes/problems, grades, colors, setters, set/strip, rotation) | ✖ (not found in researched docs) | ✔ (flagship) | ✖ | climbing-defining structure; lives in a separate product pole |
| Setter productivity / setting analytics | ✖ | ✔ (flagship) | ✖ | same |
| Competitions/leagues with digital scoring | ✖ (events/booking only) | ✔ (flagship) | ✖ | climbing-segment structure |
| Climber community engagement (logging, new-set notifications, feedback) | ✖ | ✔ (flagship) | ✖ | climbing-segment structure |
| Youth programs/teams with program dues | ✔ | ✖ | ✖ (not surfaced) | vertical-program structure |
| 24/7 unstaffed access control | ✖ (key tags at staffed desk) | ✖ | ✔ (built-in hardware) | segment/deployment variant |
| Marketing automation / lead funnel | ✖ (email system only) | ✖ | ✔ | generic-pole capability |
| Multigym / multi-location | ✔ | ✔ (per-location pricing) | not surfaced | scale variant |

**Reading of the comparison:** the market is polarized into two complementary poles —

- **Business-management pole** (RGP; generic products like GymMaster serve the same loop): members, entitlements, check-in, billing, POS, programs.
- **Wall-and-community pole** (KAYA Gym; TopLogger/Stökt named in market context): routesetting lifecycle, setting analytics, competitions, climber engagement.

No researched product covers both poles. Mature climbing gyms commonly run one product from each pole (KAYA's own marketing addresses gyms that clearly run other systems for membership/billing).

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

An operator-side system of record for a climbing facility's business, built on:

1. **Identified visitors holding entry entitlements** — people records with a standing that defines on what basis they may enter (membership, prepaid period, punch card, day pass).
2. **Check-in that validates and records entry** — the daily operational loop; the person's standing (entitlement, waiver on file, certification flags, balance) is surfaced to staff/kiosk at the moment of entry.
3. **Money resolution** — recurring dues and pass sales collected against the entitlement (with retail sales as the standard companion transaction).

The climbing-specific safety posture is part of the visitor's standing, not a separate module: a **waiver on file** (the legal foundation of participation in a high-inherent-risk activity) and **proficiency/certification flags** (e.g., belay certification — applicable where the facility's format requires it) are recorded on the person and surfaced at check-in.

Historical check (§24-style): 1990s–2000s climbing gym software/paper systems already ran on member records + punch cards + waiver-on-file flags + belay-check flags at the desk; the L0 therefore does not depend on cloud deployment, kiosks, apps, or routesetting software. Bouldering-only facilities satisfy the L0 with the certification element vacuous ("where applicable").

### L1 — Common Mature Structure

- **Digital waiver management** — waiver forms, kiosk/waiver stations, guardian/minor handling, expiry and re-sign triggers, searchable document archive (RGP flagship; KAYA links waivers; industry-wide practice).
- **Proficiency/belay certification tracking** — custom proficiency labels on customer profiles, warnings at check-in/POS, bulk management (RGP direct).
- **Class/program scheduling and booking** — offerings, events, resources, instructors, waitlists, online booking widgets (RGP; GymMaster).
- **Youth programs/teams** with program-specific dues and enrollment (RGP direct).
- **Retail POS + inventory** — pro shop, gear, snacks; packaged products; gift cards (RGP; GymMaster).
- **Member self-service** — online accounts, membership change requests (freeze/cancel/payment update), member mobile app (RGP; GymMaster).
- **Reporting/analytics** — check-ins, revenue, membership trends, occupancy, insurance-renewal reporting (RGP; GymMaster).
- **Staff management** — roles/permissions, time clock (RGP; GymMaster).
- **Wall/route management (routesetting layer)** — walls/areas as structured space; routes/boulder problems as dated, grade- and color-tagged, setter-attributed objects with set/strip turnover; rotation and grade-distribution targets; setter productivity analytics; climber-facing route info and feedback (KAYA Gym direct; TopLogger/Stökt as named market context). Standard for modern climbing gyms, but frequently delivered by a **companion product** rather than the management system itself.
- **Competitions/leagues** — event formats with digital scoring and leaderboards (KAYA direct; RGP covers only generic event booking).

### L2 — Variant / Optional Structure

- Facility format: bouldering-only vs rope+autobelay vs hybrid (drives whether belay/lead certifications exist at all).
- Product-stack posture: single business system + separate routesetting tool (common) vs whatever bundling a vendor offers.
- Deployment: cloud vs locally hosted (RGP ships both); hardware-dependent front desk (printers, drawers, webcams) vs software-only.
- Payment stack: integrated gateways vs external billing providers; ACH/card mix; decline-minimization services.
- 24/7 unstaffed access (door hardware, tailgating detection) — generic-pole capability some climbing gyms adopt.
- Entitlement mix: EFT vs prepaid vs punch cards vs corporate/entity memberships.
- Access-control hardware integration (barcode key tags, bluetooth readers).
- Regionalization: localized receipts/language, country-specific best practices (RGP documents UK practices, optional French receipts).
- Institutional segments: university/outdoor-program walls, non-profit pricing (KAYA FAQ).
- Adjacent-facility reuse: the same software class also serves gun clubs, wake parks, skate parks (RGP positioning) — evidence that the business core is facility-class-generic while the climbing structures are the differentiator.

### L3 — Vendor-specific (research notes only)

- RGP: Smartwaiver integration; SendGrid dependency for transactional email; "Billing Launch" one-click billing; "Decline Minimizer"; 30-second kiosk re-scan lockout; peach-colored change-request banner; cloud seat types/roles; Zout income account; QuickBooks integration; webcam capture at check-in; Groupon promotion setup; Facebook Pixel/custom-audience exports; "Members With Warnings" queue; example decline-email template values (5-day late fee, 14-day termination — template placeholders, not verified defaults).
- KAYA: Grip List award claims; per-location pricing figures; usage stats (750K+ boulders, 220K+ routes, 4K+ setters); "auto-bump sandbag detection"; KAYA PRO consumer tiers; onboarding-portal process; university/non-profit one-time fee.
- GymMaster: built-in bluetooth door hardware; tailgating detection; Deloitte/SoftwareAdvice award claims; 110+ countries / 180k weekly users claims.

## Vendor-specific Findings

See L3 above. The most consequential vendor fact for the Type model: **RGP — the leading climbing-gym-specific product — shows no routesetting capability in its researched documentation**, while **KAYA Gym — a leading routesetting product — shows no membership/billing/check-in capability**. The Type is therefore realized in the market as a two-product stack more often than as a single system.

## Boundary Findings

- **vs Gym Management System:** the business core (members, entitlements, check-in, billing, POS, booking) is shared — GymMaster proves a generic product can serve the core. The climbing leaf's independent identity rests on (a) the safety-posture records (waiver-on-file, proficiency/certification flags) as first-class check-in surfaces, (b) the wall/routesetting layer, and (c) a dedicated vendor market selling to climbing gyms. This is a segment-sibling relationship (same relationship Gym Management System has to Martial Arts School Management / Swim School Management / Gymnastics Club Management). Flagged in STATUS Boundary Issues for consistent treatment across the sibling leaves.
- **vs Fitness Class Booking:** booking is one capability inside the management system (offerings/events/resources), not the Type.
- **vs Sports Facility Management:** facility management is about the physical plant/operations; climbing gym management is about the commercial relationship with visitors. The wall appears here as commercial-programmatic inventory (routesetting), not as building/facility infrastructure.
- **vs Digital Waiver Management (§26 leaf):** waivers are a defining capability of this Type but a standalone waiver product serves many industries; the management system binds waivers to membership, check-in, and billing.
- **vs climber-side logging apps (KAYA app consumer side, TopLogger consumer side):** different user (climber vs operator) and different core object (personal ascent log vs business records). KAYA Gym is the operator-side slice of a climber app — a boundary case showing the two markets touch.
- **vs Event/Competition Management:** comps/leagues are a module (KAYA) or generic events (RGP), not the Type's center.
- **"去掉什么就变成另一个 Type" 判据:** remove the wall/routesetting layer and the safety-posture records → generic Gym Management System. Remove the business core (members/billing/check-in) → a routesetting/community tool (KAYA-Gym-like), which is the wall pole, not the management Type. Both removals are observed in real products — this is why the Type document must present the core and the climbing-specific layers as distinct tiers.

## Uncertainties

1. Vertical Softworks, Stökt, TopLogger, RhinoFit, Grifit unreachable — the climbing-specific business pole beyond RGP is under-sampled; claims like "all climbing-specific products do X" are avoided.
2. Whether RGP has any routesetting capability at all is unknown (not found in fetched docs; absence asserted only over fetched surfaces).
3. Exact check-in enforcement (hard block vs warning) is not directly evidenced; RGP shows warnings/notices and a sample email stating past-due members must not climb — enforcement posture likely configurable; stated with qualification.
4. KAYA Gym's exact relationship with gym membership systems (integrations? none?) is not documented on fetched pages.
5. Market-share and landscape claims (TopLogger/Stökt positions) rest on KAYA's competitive references and general market knowledge, not independent Tier-1 verification.

## Final Synthesis

Climbing Gym Management is the operator-side business system for a climbing facility. Its defining core is the visitor loop: identified people with entry entitlements, check-in that validates and records entry against the person's standing (entitlement + waiver on file + certification flags + balance), and money resolution (dues, passes, retail). Around that core, mature products add the structures the climbing industry demands: digital waivers as a flagship workflow, proficiency/belay certifications surfaced at the front desk, programs and youth teams, retail, reporting, and staff management. The most climbing-distinctive structure — the wall as managed inventory (routesetting lifecycle with grades, setters, rotation, and climber feedback) — is standard for modern gyms but is frequently delivered by a companion product (routesetting/community platforms) rather than by the management system itself; the market is polarized into a business-management pole and a wall-and-community pole, and gyms commonly run one of each. The Type shares its business core with generic Gym Management System; its independent identity rests on the climbing-specific safety posture, the wall layer, and a dedicated vendor market.
