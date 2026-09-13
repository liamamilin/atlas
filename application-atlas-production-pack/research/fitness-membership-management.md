# Research Notes — Fitness Membership Management

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (update-v1)

## Research Goal

Understand what "Fitness Membership Management" software actually is in the market: the operator-side system for running the membership relationship of a fitness business — member records, membership plans, recurring dues, the membership lifecycle (join / freeze / renew / cancel / lapse), and the connection between standing and access/usage — as distinct from class booking, from full gym/studio business suites, and from generic (association-type) membership systems.

## Initial Boundary

Hypothesis at start:

- The core is the **membership as a managed relationship**: member of record + plan + dues cycle + standing state.
- Neighbors to keep separate:
  - **Fitness Class Booking** (processed) — booking loop; memberships appear there only as the entitlement a booking consumes. Its doc already describes this leaf as "capability slice of the broader suite — owns the membership/billing relationship."
  - **Gym Management System / Fitness Studio Management** (unprocessed siblings) — broader business systems (staff, POS, payroll, retail, access ops). Membership is one pillar there.
  - **Membership Management System (§25) / Membership Billing / Member Portal / Member Benefits Management** (unprocessed) — the generic membership family; need a center-of-gravity seam.
  - **Climbing Gym Management** (processed) — climbing-facility business system; EFT membership + check-in appear there as facility entitlement machinery.
  - **Fan Membership Platform** (processed) — fan-side dues to a creator; different counterparty.
  - **Subscription Billing Platform / Recurring Commerce Management** — money machinery without the fitness membership semantics.
  - **Corporate Wellness Platform** (processed) — employer-side program; different operator seat.
- Risk: this leaf could be judged a mere vertical variant of Membership Management System. Precedent: congregation-membership-management was confirmed as keep-both with a center-of-gravity seam. Expected outcome here: keep-both, seam = fitness entitlement semantics (facility access + class/PT usage + freeze culture + check-in conventions) on the same dues/lifecycle skeleton.

## Research Questions

1. What objects does the system keep: member, plan, held membership, payment, check-in? How do they relate?
2. What plan shapes exist (recurring EFT/monthly, prepaid term, class packs, day/trial passes)? What terms attach (commitment periods, joining fees, usage limits, access windows)?
3. What is the membership lifecycle and which events are first-class (signup, trial, activation, hold/freeze, renewal, cancellation, lapse, win-back)?
4. How does dues billing work (recurring charges, payment methods, failed-payment recovery, dunning, debt handling)?
5. How is standing converted into access/use (check-in scans, door access, balance thresholds blocking entry, pack/concession counting)?
6. What does the member self-service surface do (buy/renew, update payment, freeze request, book)?
7. What reporting does the operator run the business on (membership counts, MRR/revenue, visitation, retention)?
8. Where does this Type end and Gym Management System / Fitness Studio Management / class booking / generic membership systems begin?

## Representative Products

Selected for market coverage + documentation depth + different product philosophy + different customer level:

| Product | Vendor / origin | Segment | Philosophy | Evidence level |
|---|---|---|---|---|
| TeamUp | UK, independent | boutique studios/gyms | booking-led product with a deep membership engine | Tier-1 official help centre (deep) |
| GymMaster | Treshna Enterprises, NZ | small–mid gyms, 24/7 access niche | membership + native door access + flexible billing partners | Tier-2 official product pages (rich) |
| Zen Planner | Daxko, US | mid-market martial arts / functional fitness / boutique | all-in-one suite with membership+billing as flagship pillar | Tier-2 official product pages |
| PerfectGym | Sport Alliance GmbH, EU/global | enterprise chains & franchises | enterprise suite; financial services incl. debt collection | Tier-2 official product pages |
| LegitFit | Ireland | SMB gyms/studios | all-in-one with explicit "Memberships Management" pillar | Tier-2 official product pages |

Also considered: Wodify (CrossFit-affiliate niche) — www.wodify.com returned HTTP 403 on 2026-09-08; abandoned after one attempt per network rule; no claims rest on it. Glofox was observed in the fitness-class-booking pass at product-page level; not re-sampled here.

## Sources

- Zen Planner — root: https://zenplanner.com/ ; product: https://zenplanner.com/product/ (fetched 2026-09-08)
- GymMaster — https://www.gymmaster.com/membership-management/ ; https://www.gymmaster.com/billing-management/ ; https://www.gymmaster.com/gym-access-control/ ; root https://gymmaster.com/ (fetched 2026-09-08)
- TeamUp Help Centre — https://support.goteamup.com/ ; collection "For Business Owners, Admins, Instructors": https://support.goteamup.com/en/collections/9210299-for-business-owners-admins-instructors ; collection "Memberships": https://support.goteamup.com/en/collections/9210400-memberships ; article "Membership Holds & Payment Rescheduling": https://support.goteamup.com/en/articles/14038967-membership-holds-payment-rescheduling ; article "Cancelling a Membership on Behalf of Your Customer": https://support.goteamup.com/en/articles/9327443-cancelling-a-membership-on-behalf-of-your-customer (fetched 2026-09-08)
- PerfectGym — root: https://www.perfectgym.com/ ; Financial Services: https://www.perfectgym.com/en/solutions/gym-payments (fetched 2026-09-08)
- LegitFit — root: https://www.legitfit.com/ ; Memberships Management: https://www.legitfit.com/features-legitfit/memberships-management (fetched 2026-09-08)

Sourcing limitation: only TeamUp provided article-level operational documentation from this environment. The other four products were observed at official product-page level (Tier-2), which confirms positioning and capability presence but not precise operational rules. Consequently all precise numeric parameters, default values, and state-name ladders observed at TeamUp are kept in these notes as product-specific evidence and are NOT generalized in the application document.

## Product A — TeamUp (Tier-1, help centre)

### Key observations (evidence layer A)

**Membership types.** The system distinguishes three membership families: recurring plans (auto-renewing, billed per cycle), prepaid plans (paid up front for a term), and packs (class packs / credit bundles with a use count). Memberships carry usage limits; where several limit kinds exist, the proration logic resolves them in priority order (billing-cycle limit > yearly limit > monthly limit > weekly limit) — product-specific detail.

**Purchase & assignment.** Customers purchase memberships themselves (customer site) or staff add one on the customer's behalf (with start-date changes and upgrades). Joining fees can be enabled per plan. Multiple memberships valid for the same event can coexist on one profile.

**Membership detail page** carries tabs such as Upcoming Payments, Skipped Payments, and Usage — the held membership is the working object, not just a row in a list.

**Holds (freeze).** Putting a membership on hold: billing paused (payments in the hold window skipped), class access suspended, existing bookings inside the hold automatically cancelled, recurring reservations preserved and restored after the hold. On reactivation the system generates a prorated payment (time-based for unlimited memberships; usage-based for limited ones); credits are issued when the member overpaid. Holds may be open-ended (no end date; useful for injury) or fixed. "Extend expiration dates" option: packs/prepaid extended by the hold days; recurring plans' expiration and commitment period extended by the billing periods spanned. Bulk hold tool exists; all holds reportable ("All Membership Holds" report with status active/upcoming/ended and payment calculation: no payment / credit owed to customer / credit due to customer).

**Cancellation.** Staff cancel on behalf with three expiry options: today, end of billing period, specific date. No proration on cancellation — billing dates falling before the expiry are charged in full. An "outstanding payment void" option waives a pending payment (irreversible). Commitment periods are enforced: cancelling before commitment end moves expiry to the commitment end and billing continues until then. Cancellation policy is configured on the payment plan: customer self-cancel with no notice, with a minimum notice period, or contact-the-business-to-cancel. Past (ended) memberships remain visible on the profile.

**Billing machinery.** Payment processors (card via Stripe, direct debit via GoCardless); payment statuses with required actions; distinct failure behavior for recurring vs non-recurring payments; account credit applied to recurring membership payments; offline payments with an overdue threshold that can block the membership from being used. Payment methods can be added per membership; billing date changeable per member or business-wide; upcoming payments downloadable.

**Customer lifecycle statuses.** Customers classified as New / Active / Slipping Away (criteria set by the business) / Inactive (no active membership + no attendance for a defined period) — status-driven retention workflow. Reports: Memberships (filter by status, group by plan), membership purchase/cancel counts per period, average customer lifespan, average lifetime value, all membership holds.

**Usage.** Remaining uses on membership/pack; staff can record a class usage against a pack manually; pack-running-low notifications; check-ins set up and managed; attendance feeds "who's missing / not showing up" reporting.

**Adjacent machinery** (suite context): CRM lifecycle pipeline (lead → member stages, Kanban, stage automations), forms/waivers/policies incl. expiring forms, family member profiles on one account, referrals, POS, communication automation (membership purchase notifications, hold-end emails etc.).

## Product B — GymMaster (Tier-2, product pages)

### Key observations

- "Member Management" is a headline pillar: online signups & waivers; a sales funnel that converts gym leads into paying members; customizable member profiles (member details, acquisition channel, memberships and billing records, visitation, booking habits, communications, measurements, purchases); member self-service portal.
- **Plan configurability**: "ultra configurable memberships" — combine visit rights, booking-type rights, and access restrictions; "control who can visit and when, what classes and services they can use, or set limits for these." Trial, promo & concession passes as separate club-pass types. Access-hour tiers per plan: standard hours, off-peak, full 24/7; group/area restrictions (e.g. women-only areas).
- **Billing**: automated recurring payments via a choice of PCI-compliant billing partners (Ezypay, Ezidebit, GoCardless, Stripe, Payrix, Braintree, Square, Paystack, Bluefin, Paychoice, Fiserv listed); partial vs full integration; choose billing day and frequency; up-front / weekly / monthly / annual billing; failed payments trigger automatic reminders and recollection attempts; configurable failed-payment fees; payment plans to settle historic debts; offline CSV export billing for merchant banks; member online payments and renewal registration.
- **Standing → access**: "flag bad debtors to block access to your facility"; balance thresholds ("balance barriers") that deny entry when a member owes beyond a set amount; expired memberships instantly applied to member cards; concession visits automatically counted against the membership; members arriving for a class automatically checked into the session; all visits logged; staff-device alerts when a flagged member checks in.
- **Access control** (native hardware): RFID keytags/fobs, RFID+Bluetooth door readers, phone-as-key via member app; GateKeeper controller linked to the membership database; tailgating detection with camera evidence.
- Communications: bulk or automated email/SMS/push to leads, members, at-risk-of-cancelling members, and historic members. Reporting: preset + custom reports, business KPIs. FAQ mentions debt collection handled alongside memberships and billing. "3m+ memberships managed" claim (marketing figure — not used as evidence of capability).

## Product C — Zen Planner (Tier-2, product pages)

### Key observations

- Suite (Daxko) for martial arts schools, functional fitness, boutique studios. "Membership Management" is the flagship capability: "from registration and billing to tailored communication and self-service."
- **Membership and class package builder** named as a core feature; **contracts and waivers**: "Build customized contracts and waivers for specific membership categories" — contract documents bound to membership categories.
- **Automated billing**: "get paid on time every month with automated billing"; integrated payment processing; "revenue protection" capability and a Revenue Recovery service (failed-payment recovery positioned as a paid add-on service — vendor-specific packaging).
- **Member self-service**: members check in, reserve class spots, resolve alerts, pay bills, purchase retail on their own; Kiosk Mode check-in; Staff App check-in; member mobile app.
- **Attendance tracking**: attendance history visible to members; automated absentee emails after absence periods; milestone recognition (anniversaries, class-count milestones).
- Vertical flavor: skill and belt tracking for martial arts (rank progression attached to members); workout tracking via SugarWOD integration.
- Also in suite: retail/POS, staff time clock and payroll, reporting & dashboards, marketing/lead tools (Engage), branded app. PerfectGym-style breadth confirms membership is one pillar of a business suite.

## Product D — PerfectGym (Tier-2, product pages)

### Key observations

- Enterprise pole: "mid-sized and enterprise-level fitness businesses… regional and international fitness chains and franchises, as well as public and private leisure operators"; multi-location centralized control.
- **Financial Services** pillar: automated recurring billing (weekly/monthly/annual/customized schedules); payment methods incl. credit cards, cash, bank transfers, direct debits, online and at reception; multiple currencies and localized payment methods for international operations.
- **Debt Collection module**: "automate debt collection stages", member overdue payments with due dates and collection stages, debtor grouping by criteria such as debt level, current status, debt amount, previously completed debt collection steps, days past due; reminders and penalties. (Enterprise depth of the dunning loop.)
- Other pillars: Club Management (facility, class & staff scheduling, reporting), Sales & Marketing (lead management), Member Engagement (self-service tools, personalized communication, loyalty program), open platform integrations (ClassPass, Wellhub, EGYM, Technogym, Stripe, GoCardless etc.).
- Membership-specific plan machinery was not documented at page level (only payments/engagement); evidence for plan config rests on the suite positioning.

## Product E — LegitFit (Tier-2, product pages)

### Key observations

- All-in-one for gyms/studios (gyms, yoga, pilates, CrossFit, SGPT/PT, leisure centres, multi-location). "Memberships Management" is a named feature pillar: "Flexible packages, auto-renew memberships, roaming options, and recurring plans."
- **Plan shapes**: recurring memberships; auto-renew packages; class passes (single-class to multi-class, discounted bundles, unlimited monthly); PAYG or credit-based; gift packages (buy a membership for someone else); joining fees shown as plan attributes; plan card shows price, duration, session allowance (e.g. 4 sessions per week over 4 weeks), joining fee, count of active payments, and a for-sale toggle.
- **Freeze**: "Freeze Periods — set the start and end date once, and billing pauses and resumes automatically"; "Bulk Freeze Memberships" for closures (holidays/renovations), pausing memberships in bulk with member notification.
- **Roaming memberships** for multi-site operators (member's plan usable across locations).
- **Compliance**: signed terms & conditions documents stored against clients (membership agreements, liability waivers, policy updates).
- **Sales surface**: coupons/discount codes (new-client, referral, seasonal), public links for memberships/packages/events, embedded signups.
- **Money view**: MRR / gross volume / net volume trend cards; "Active Memberships Charts" (active membership counts over time, retention/drop-off trends).
- **Check-in**: QR check-in via app; turnstile integration listed in integrations.
- Payments: integrated payments, online and offline processing (incl. cash logged), custom fees, discounts; payment-method icons incl. card, cash, cheque, Apple/Google Pay.

## Cross-product Comparison

| Structure / capability | TeamUp | GymMaster | Zen Planner | PerfectGym | LegitFit | Assessment |
|---|---|---|---|---|---|---|
| Member/customer records (identified person, profile, history) | A | A | A | A | A | Core |
| Operator-defined membership plans (price + billing frequency + terms) | A | A | A | A (suite-level) | A | Core |
| Held membership = member × plan instance, the working record | A | A | A | B | A | Core |
| Recurring dues billing (automated charges) | A | A | A | A | A | Core |
| Standing state lifecycle (active / frozen / ended; renewals; lapses) | A | A | A | B | A | Core |
| Hold / freeze as a first-class lifecycle event | A | A (implied by change requests in climbing sibling pass) | — | — | A | Common |
| Class packs / usage-count memberships | A | A (concession/visit passes) | A (class packages) | B | A | Common |
| Check-in / usage recording | A | A | A | B | A | Common |
| Door access control (hardware) | — | A (native) | — | B | B (turnstile integration) | Common variant |
| Standing→access gating (balance thresholds, expired → denied) | A (offline overdue → block membership) | A | — | B | — | Common |
| Failed-payment recovery (reminders, retries, fees) | A | A | A (revenue recovery) | A (debt collection module) | — | Common |
| Commitment/contract terms | A | A (implied by plans) | A (contracts per category) | B | A (T&C docs) | Common |
| Joining fees | A | B | — | — | A | Common |
| Trials / promo / concession passes | A (free credit offers) | A | A (free trial funnels) | B | A (coupons) | Common |
| Member self-service (portal/app: buy, renew, payment method, bookings) | A | A | A | A (self-service tools) | A | Common |
| Lifecycle/retention communications (renewal, at-risk, win-back, absent) | A | A | A | A | A | Common |
| Sales funnel / lead management | A (CRM pipeline) | A | A (Engage) | A | A (lead nurture) | Common (suite territory) |
| Family/household accounts | A | — | — | — | — | Optional |
| Multi-location / roaming | B | A | A | A (enterprise core) | A | Common variant |
| Debt collection as distinct module | — | B | B (revenue recovery service) | A | — | Variant |
| Rank/belt tracking (martial arts) | — | — | A | — | — | Vendor/vertical-specific |
| Workout tracking integration | — | A (workouts in app) | A (SugarWOD) | B (Technogym/Strava integrations) | A (exercise programming) | Optional |
| Retail/POS, payroll | A (POS) | A | A | A | A (payroll per-session rates) | Suite territory, not this Type's core |
| Loyalty program | — | — | — | A | — | Optional |

Legend: A = directly observed in this pass (official source, specific product); B = cross-product commonality / suite-level page-level evidence.

## Canonical Model (L0/L1/L2/L3)

### L0 — Defining Invariant

The Type is the fitness business's system of record for the membership relationship. Three structures held jointly:

1. **The member of record** — a persistent, individually identified person enrolled with the fitness business, carrying their membership standing and history (acquisition source, agreements, payments, usage). Remove → a class-booking customer list or anonymous pass sales.
2. **The held membership** — an operator-defined plan (dues amount, billing frequency, term, usage/access terms) instantiated for one member as a standing, renewable entitlement to the facility and its services. The plan catalog and the per-member instance are distinct objects; the instance is the working record staff act on. Remove → event registration or one-off transactions.
3. **The governed dues-and-standing cycle** — recurring dues charged against the held membership on a cycle, managed through a standing state (active; frozen/suspended; renewed/ended by cancellation or lapse), where money events (charges, failed payments, refunds/credits) and lifecycle events (join, hold, cancel, expire) convert into whether the entitlement is currently exercisable. Remove → a static member register (no dues management) or a pure billing engine (no membership standing).

Jointly-held is load-bearing: member + plan without dues/state = CRM contacts with a price list. Dues + state without membership-as-entitlement = subscription billing. Entitlement state without dues = attendance/visit tracking.

### L1 — Common Mature Structure

- Plan-shape breadth: recurring EFT/monthly/annual, prepaid term plans, class packs / credit bundles, day and trial passes; joining fees; discounts/coupons.
- Check-in and usage recording (scan/QR/keytag/kiosk at the door; concession counts; attendance feeding retention views).
- Member self-service portal/app: sign up, purchase/renew, update payment method, request freeze/cancel, book sessions.
- Failed-payment recovery: reminders, retry/recollection, configurable failed-payment fees; overdue balances gating access or blocking the membership.
- Renewal/expiry machinery: auto-renew, expiry notices, rejoin/reactivation.
- Lifecycle communications: renewal reminders, win-back/at-risk campaigns, absent-member outreach, milestone recognition.
- Membership reporting: active counts, revenue/MRR, attendance/visitation, retention/lifespan, holds.
- Agreements capture: digital contracts/waivers/terms stored against the member (paper-era analog: signed cards).
- Family/household accounts (several products), member photos/measurements.
- Sales funnel/lead management feeding membership signup (suite territory, near-universal in market).

### L2 — Variant / Optional Structure

- Native door-access hardware vs third-party/turnstile integration vs no hardware (front-desk-only businesses).
- Access-hour tiers per plan (standard / off-peak / 24/7) and area restrictions.
- Debt collection as a distinct module (enterprise pole) vs reminder-and-retry (SMB pole) vs outsourced recovery service.
- Multi-location, roaming/franchise memberships, centralized chain control.
- Debt settlement plans for historic balances; offline/manual billing rails (bank CSV, cash/cheque logging).
- Regional billing rails (direct debit schemes, localized payment methods, multi-currency).
- Vertical seasoning: martial-arts rank/belt tracking, workout tracking, community feeds, loyalty programs.
- Corporate/institutional membership shapes (leisure centres) — observed at suite positioning level only.
- Compliance depth: e-signature waivers, expiring forms, minor/guardian handling (from sibling passes).

### L3 — Vendor-specific (research notes only)

- TeamUp: hold proration with limit-priority order (billing cycle > yearly > monthly > weekly); expiry options at cancellation (today / end of billing period / specific date); void-outstanding-payment option; "extend expiration dates" hold option (days for packs, billing periods for recurring incl. commitment extension); All Membership Holds report widgets; customer statuses New/Active/Slipping Away/Inactive with business-defined criteria; skippable/unskippable upcoming payments; offline-payment overdue threshold blocking membership use.
- GymMaster: GateKeeper controller; tailgating detection with camera evidence; "balance barriers"; concession auto-count on entry; class auto check-in on door entry; 24/7 unstaffed operation posture.
- Zen Planner: Kiosk Mode; Revenue Recovery service (Daxko); SugarWOD integration; skill/belt tracking.
- PerfectGym: Debt Collection module debtor-grouping criteria (debt level, status, amount, completed steps, days past due); ISO 27001/PCI claims.
- LegitFit: bulk freeze for closures; roaming memberships; MRR/gross/net volume cards; public links; Lia AI assistant.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- Paper-era gym: membership card + front-desk ledger; monthly dues collected in person or by bank draft; freeze granted verbally and noted; cancellation by notice. Member of record ✓ (ledger line/card), held membership ✓ (card = plan instance with dues terms), dues-and-standing cycle ✓ (dues collected, standing tracked, expired = no access). Fits without apps, portals, door hardware, or card rails — so none of those belong in L0.
- 1990s–2000s club software with barcode scan + bank-draft billing house (the draft-processing lineage that survives in the market's billing-services corner): fits — dues cycle and standing state were the heart even when access control was a mag-stripe card.
- Regional differences (SEPA direct debit vs ACH vs cash-based markets) affect only the payment rail — L2.
- Conclusion: the L0 above is era-neutral and region-neutral. The modern additions (self-service, access hardware, dunning automation, MRR analytics) stay in L1/L2.

## Vendor-specific Findings

See L3 above; none promoted to the application document.

## Boundary Findings

- **vs Fitness Class Booking** (processed): the booking loop owns schedule/roster/spot economy; memberships appear there only as the entitlement a booking consumes. Here the membership/dues relationship is the object; class booking is absent entirely from this Type's core. The two meet at "entitlement resolution" and "check-in."
- **vs Gym Management System / Fitness Studio Management** (both unprocessed): those leaves center the whole business (staff, scheduling, POS/retail, payroll, access operations). Membership is one pillar there. The seam is center of gravity: strip scheduling/staff/POS and this Type still stands; strip the membership engine and a studio suite still doesn't run.
- **vs Membership Management System (§25, unprocessed) / Membership Billing / Member Portal / Member Benefits Management**: same dues/lifecycle skeleton; the fitness leaf's discriminator is the entitlement semantics (facility access + class/PT usage + freeze culture + check-in conventions) and the operator seat (fitness business owner/staff). Flag for joint review with the §25 pass.
- **vs Subscription Billing Platform / Recurring Commerce Management**: those are money machinery over goods/any subscriptions; here the object of record is a person's standing entitlement to a physical facility and its services, with usage/check-in semantics money platforms lack.
- **vs Fan Membership Platform** (processed): different counterparty (creator vs fitness business) and different fulfillment (digital output vs facility/service access).
- **vs Corporate Wellness Platform** (processed): employer-sponsored program participation vs consumer membership sold by the fitness operator.
- **vs Climbing Gym Management** (processed): that leaf centers the climbing facility's business incl. wall/route inventory; membership/check-in machinery there is the facility-flavored instance of this Type's core.
- **Remove-test:** remove dues/billing → attendance/visit tracker. Remove standing state → plain member CRM. Remove membership-as-entitlement (keep money only) → subscription billing. Remove fitness entitlement semantics (facility/service access, freeze, check-in) while keeping dues+state → generic Membership Management System.

## Uncertainties

- Zen Planner's help centre sits behind a Salesforce community (help.daxko.com) that was not fetchable in this environment; its operational depth (plan builder fields, hold rules) is unverified — its capability claims are page-level only.
- PerfectGym plan-configuration depth not directly documented at page level; financial/debt-collection evidence is strong but membership-plan machinery is inferred from suite positioning (marked B in the comparison).
- GymMaster's member-side freeze/cancel flows are documented in product FAQ/marketing (member portal, online change requests) and via the climbing sibling pass's vendor help (RGP is a different product); treat GymMaster self-service specifics as page-level evidence.
- Whether "debt collection" is definitional for enterprise pole or purchasable module — treated as L2 either way.
- Corporate/institutional membership shapes (leisure centres, employer-paid) are weakly evidenced here (suite positioning only).

## Final Synthesis

Fitness Membership Management is the operator-side system of record for the membership relationship of a fitness business. Its defining core is the triad member-of-record + held membership (member × operator-defined plan = standing renewable entitlement to the facility and its services) + the governed dues-and-standing cycle that converts money and lifecycle events into whether that entitlement is currently exercisable. Everything the market commonly bundles around it — plan-shape breadth, check-in/access hardware, self-service apps, dunning, retention automation, sales funnels, multi-location — is standard mature structure or variant structure, not definition. The Type sits between Fitness Class Booking (which consumes memberships as entitlements) and Gym Management / Studio Management suites (which contain it as one pillar), and shares a dues/lifecycle skeleton with generic membership systems while being distinguished by fitness entitlement semantics and the fitness-operator seat.
