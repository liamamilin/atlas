# Research Notes — Tenant / Resident Portal

Leaf: Tenant / Resident Portal (DIRECTORY §17 Construction, Real Estate & Facilities)
Slug: tenant-resident-portal
Research date: 2026-09-10
Methodology: WORKFLOW v1.1 / WRITING_GUIDE v1.1

## Research Goal

Understand the Application Type "Tenant / Resident Portal" from real products: what the resident-facing self-service surface consists of, who holds accounts and what anchors them, what residents actually read and do, how actions write back into the property operator's systems, how the operator governs the surface, and where the boundary sits against the operator-side property systems (property management, rent collection, maintenance, association management) and against the atlas's other portal Types.

## Initial Boundary

- §17 places this leaf beside Residential Property Management, Commercial Property Management, Rent Collection Platform, Property Maintenance Management, HOA / Community Association Management, Rental Application Platform, Amenity Booking Platform, Package & Mailroom Management, Building Access & Visitor Management, Short-term Rental Management, Student Housing Management, Affordable Housing Management.
- Prior passes pre-hung seams this pass must discharge:
  1. **residential-property-management** (2026-09-09): "tenant-resident-portal (resident-facing delivery surface vs operator-side system of record — all five sampled products ship a resident surface as standard capability, not the center)". Forward flag.
  2. **property-maintenance-management** (2026-09-09): "the portal is the resident-facing surface (requests/status/payments), this Type is the operator-side system the portal feeds".
  3. **rent-collection-platform** (2026-09-09): "pre-hung surface-vs-money-machinery seam for the unprocessed tenant-resident-portal sibling".
  4. **member-portal** (2026-09-08): the atlas has a `<relationship>-portal` family (mortgage-borrower-portal, tenant-resident-portal, customer-portal, employee-service-portal) sharing the member-portal self-service grammar with different standing anchors — no consolidation proposed; this pass canonizes the occupancy-relationship member of that family.
  5. **amenity-booking-platform** research observed: "ResidentPortal is Entrata's resident-facing portal within a large multifamily PM suite (OXP operations platform + RXP resident experience platform)" — portal as the resident-side surface of a suite.
- Vocabulary hazard: the market says "tenant portal", "resident portal", "resident services portal", "resident center", "online portal", "homeowner portal" — same surface, different operator segments. RentCafe's own FAQ distinguishes "applicant portals" (prospect-side) from "resident services portals" (current-resident side).

## Research Questions

1. What exactly does the resident-facing surface expose? Which tabs/pages/objects?
2. What can a resident DO (view vs change), and what does each action write back to?
3. What anchors access — how is the account provisioned, and what relationship does it bind to (lease? unit? ownership? application)?
4. Who else holds accounts — roommates, board members, prospects, owners?
5. How does the operator govern the surface (feature toggles, per-property overrides, payment methods/fees, role visibility)?
6. Where does the money sit — what does the portal do vs the operator-side collection machinery?
7. Where does the request sit — what does the portal do vs the operator-side maintenance machinery?
8. How do rental (tenant) and association (owner/resident) poles differ on the same surface?
9. Where are the seams: vs RPM (system of record), vs rent collection (money machinery), vs property maintenance (work machinery), vs HOA/CAM (governance spine), vs rental application (prospect side), vs amenity booking / package / access (hosted capabilities), vs customer/member portals (grammar family)?

## Representative Products

| Product | Market position | Why sampled | Evidence tier reached |
|---|---|---|---|
| Buildium — Resident Center (RealPage) | SMB/mid-market residential PM suite (rentals + associations); portal included in every account | suite-included portal pole; rental AND association-owner populations in one portal; strongest documented governance layering | Tier-1 help center content (captured via search-engine rendering; direct fetch SPA-blocked — limitation recorded) |
| AppFolio — Online Portal | SMB/mid-market PM suite (rentals + HOAs); portal branded "Online Portal" | suite-included portal pole with a full public resident-facing help page; explicit "service they can choose to offer" governance language | Tier-1 (official help page fetched in full) |
| Entrata — ResidentPortal | enterprise multifamily; portal as the resident-facing product of the suite (OXP staff side + RXP resident side) | enterprise branded resident-experience pole; property-configurability stated verbatim; official resident guide PDF | Tier-2 product page (fetched) + official resident guide PDF + official app-store listings |
| Yardi — RentCafe Resident Portal | enterprise multifamily; branded resident portal of Yardi Voyager suite | second enterprise pole; registration-code provisioning; leaseholder-gated features; roommate split payments | Tier-2 (product page + official resident-guide PDFs via search capture; yardi.com/rentcafe.com 403 — limitation recorded) |
| TownSq (CINC partner) / CINC Connect | HOA / community association pole; resident engagement + payments platform | association pole; third-party platform "chosen by your HOA or management company"; board/manager request routing; role-based surfaces | Tier-2 (FAQ + product pages fetched; press release) |

Coverage: two SMB/mid-market suite portals (Buildium, AppFolio), two enterprise multifamily branded portals (Entrata, Yardi), one association-pole platform (TownSq/CINC). Different philosophies: portal-as-included-suite-surface vs portal-as-branded-resident-experience-product vs portal-as-third-party-engagement-platform.

## Sources

Tier-1 (official operational documentation):

- AppFolio — "Resident Portal Overview" help page (fetched in full): https://www.appfolio.com/help/online-portal
- Buildium Help Center — "Resident Center", "How to Submit a Maintenance Request", "Getting Started with ePay", "How can a tenant update or delete a scheduled payment set-up?", "Troubleshooting: Resident cannot pay online", "Resident Center Resources" (content captured via search-engine rendering of help.buildium.com; direct fetch returns a Salesforce SPA error — limitation recorded): https://help.buildium.com/hc/s/article/Resident-Center etc.
- Buildium — Resident Center Help Center (resident-facing): https://www.residentcenter.com/resident-center-help/
- Entrata — official ResidentPortal resident guide PDF (ResidentPay — Resident Experience): https://medialibrary.entrata.com/media_library/2146/547ca42411f46427.pdf
- Entrata — ResidentPortal app listings (official): https://apps.apple.com/us/app/resident-portal-mobile/id443831139 ; https://play.google.com/store/apps/details?id=com.psi.residentportal
- Yardi — RentCafe Resident Portal User Guide + Features Guide PDFs (official, Yardi CDN; captured via search rendering): https://cdngeneral.rentcafe.com/dmslivecafe/3/62511/Master_RENTCafe_Resident_Portal.pdf ; https://cdngeneral.rentcafe.com/dmslivecafe/3/450446/3_450446_4315856.pdf
- Yardi — RentCafe Resident App Guide (official resources site): https://resources.yardi.com/documents/yardi-breeze-rentcafe-resident-app-user-guide/
- Yardi — RentCafe Resident app listing (official): https://apps.apple.com/us/app/rentcafe-resident/id541403633
- TownSq — FAQ (fetched in full): https://www.townsq.io/resources/faq
- CINC — "CINC Launches CINC Connect" press release: https://cincsystems.com/news/cinc-launches-cinc-connect ; management/accounting product page: https://cincsystems.com/management-accounting

Tier-2 (official product pages):

- Entrata — ResidentPortal product page (fetched in full): https://www.entrata.com/products/residentportal
- Yardi — RentCafe Resident Portal product page (captured via search rendering; direct fetch 403): https://www.yardi.com/product/rentcafe-resident-portal/
- TownSq — Community Homeowner App page: https://www.townsq.io/solutions/community-features/community-homeowner-app ; Online Payments page: https://www.townsq.io/solutions/community-features/online-payments ; site root: https://www.townsq.io/
- AppFolio — Login page naming the Resident Portal: https://www.appfolio.com/login

Unreachable / abandoned (per source-access rules):

- help.buildium.com direct fetch → Salesforce SPA "CSS Error" (matches the residential-property-management pass's recorded SPA limitation). Content held via search-engine rendering of the official articles; no claim rests on anything beyond that rendered text.
- yardi.com and rentcafe.com → 403 (matches prior passes' Yardi 403 records). RentCafe evidence held at search-rendered official page + official CDN-hosted PDFs + official app-store listing strength.
- Entrata operational help center not attempted after product page + official PDF + app-store evidence proved sufficient.

## Product Observations

### Buildium — Resident Center (Tier-1 via search-rendered official help articles)

- Placement: "Every Buildium account comes with Resident Center, a free portal for residents to do things like view their financial transactions, submit maintenance requests, and make payments online." Population: "tenants and association owners" — rental and association poles in one portal. [A]
- Contents: payment history page; messages/requests tab; contact directory; community discussions; for associations, an option allowing board members to run certain reports. [A]
- Access provisioning: "A valid email is required in order to give a resident access to Resident Center." The manager invites residents (Resident Center Settings → Users tab → "Not invited" list → welcome email → "Invitation pending" until first login). [A]
- Governance: "Resident Center settings allow fine-tuned control over what your tenants and association owners see when they log into their resident site. These settings can be overridden for an individual property." Logo upload; payments toggle; announcements with optional email copy. [A]
- Payments (ePay) enablement is layered: account-level ePay application → property-level enablement → lease-level enablement; troubleshooting article walks account → property → lease → tenant checks. Payment methods EFT/eCheck and credit/debit; ePay fees configurable, including who pays the card processing fee; "Block Partial ePayments" is an optional manager setting. [A]
- Resident payment actions: one-time payments, scheduled future payments, autopay; residents edit/delete their scheduled payments; managers can act on behalf via "Sign in as user". [A]
- Requests: "Maintenance request" vs "General inquiry" types; category, subject, description, attachments, "scheduling entry permissions"; track open requests from Home dashboard or Requests page; closed history; message the manager on a request. [A]
- Extras: renters insurance purchase inside the portal (powered by MSI); Rent Reporting to credit bureaus; security-deposit visibility ("check in on their security deposit"); documents access; lease details; communication preferences. [A]
- Lifecycle continuity: "Resident Center is the central location where you will manage your new home—all the way from application to move-in, and beyond. Once you submit your application and are approved, your Resident Center account will give you access to your communication preferences, lease details, and payment history." Feature availability is manager-dependent: "Based on the property manager… you may also have access to some additional features… like online rent payments, maintenance requests, purchasing renters insurance, and even automatically reporting on-time rent payments." [A]
- Mobile: responsive web + Resident Center mobile app (iOS/Android). [A]

### AppFolio — Online Portal (Tier-1, fetched in full)

- Placement: "The Online Portal is an easy, fast, and secure way to pay charges online, view payment history, and submit maintenance requests." Populations: residents of rental properties AND homeowners of associations ("Pay rent or dues"; homeowners "submit architectural requests and view association-related events"). [A]
- Activation: "You'll receive an Online Portal Activation email or text message from your property management company… to establish a strong password." Password reset only works "if there is an active existing account." 2FA via authenticator app optional. [A]
- Governance (verbatim, three separate features): payments — "this is a service they can choose to offer their tenants"; maintenance — "this feature may not be enabled for their account"; notice to vacate — "Your property manager can choose whether or not you can give notice through the Online Portal." [A]
- Payments: one-time ("Pay Now") and autopay ("Set Up Autopay"); methods eCheck (bank withdrawal) and credit/debit (incl. Apple Pay); saved payment methods; pay-in-full vs editable amount — "If online payments are required to be made in full, the payment amount will not be editable" (operator configuration); Balance Due vs Full Balance (incl. unposted recurring bills); transaction fee displayed before submit; payment history via "View full account ledger". [A]
- Autopay management: delete, skip a month, edit amount, edit method, maximum-limit field on pay-in-full autopay; "you cannot delete/skip/edit payments created by your roommates" — household sharing semantics. [A]
- Money boundary: "Can I get a printed receipt? Please contact your property manager"; "I made a payment online by mistake… contact your bank or credit card provider"; "Please contact your property manager if you have any questions about the transactions displayed"; "Your property manager cannot see any of the payment information you have saved." [A]
- Cash pole: PaySlip with barcode for cash payments at retail locations (certified-funds regime); fees and limits stated. [A]
- Lease lifecycle: electronic lease signing in the portal (initial/signature lines, Sign and Accept); lease renewal offers appear on Home with e-signing; electronic-signature profile management. [A]
- Requests: Maintenance tab → Request Maintenance; description, photos, "permission to enter with their key", preferred time slots ("select 3 or more time slots"); status ranges "received → technician contacted → technician scheduled → completed"; "Check Status" shows a communication timeline. [A]
- Documents & insurance: Shared Documents tab (email-notified); lease under Property Details; Insurance tab — upload proof of renters insurance (provider, policy number, expiration, file) or purchase a policy if enabled; Liability-to-Landlord notice. [A]
- Account: contact info, vehicle info, login email, password, language (Spanish), payment reminders (email/push); account deletion only via the property manager; multiple units — "View Another Unit", each unit activated separately; combining portals is manager-only. [A]

### Entrata — ResidentPortal (Tier-2 product page + official resident guide PDF + app listings)

- Placement: resident-facing product of the Entrata suite — OXP (Operations Experience Platform, staff side) vs RXP (Resident Experience Platform: ResidentPortal, ResidentPay, Renters Insurance, Insurance Verification, Deposit Alternative, Rent Reporting, rewards). "Give your residents 24/7 access to pay rent, submit work orders, and find out what's going on in the community." [A2]
- Write-back: "Payments and work orders submitted online are immediately posted to your accounting or maintenance system." [A2]
- Governance: "Much of the ResidentPortal app is configurable by the property in which you live. Property settings include, but are not limited to, payment methods, payment days, full balance payment requirements, or maintenance request availability." (official app-store listing) [A]
- Enrollment (official resident guide PDF): resident self-enrolls from the property website (name, email, password, birthdate); "You may receive one of two error messages if the information does not match: No account found — …your information not matching the information entered in Entrata… contact property management to verify your information has been entered correctly in the management software." Account anchored in operator records. [A]
- Payments (guide): one-time and auto payments (monthly amount, bill day, begin/end months, "When I cancel… or until the lease is no longer current"); method-specific convenience fees; Visa max-limit with phone authorization; payment posts "in real time on Entrata and in third-party property management software (if integrated), and it will update the ledger simultaneously"; payment history "will show payment receipts as well as payments made by roommates so residents can distinguish where payments are coming from"; returned payment deletes stored billing/recurring info; charity donation add-on to rent payment. [A]
- App features (official listings): one-time pay, recurring payments, One-Tap Pay, RentNotify push reminders, contact property with after-hours routing, maintenance requests with photos, inspections (move-in/maintenance) from mobile, reserve amenities, Touch/Face ID, submit Notice to Vacate, view estimated move-out charges. [A]
- Product page: resident CRM framing (surveys, events, newsletters); login messages/alerts; electronic documents review; community wall (buy/sell, maintenance requests, coordinate activities); dashboard screenshot shows balance due + make payment, quick links, alerts (late rent, package pickup, amenity booking). [A2]

### Yardi — RentCafe Resident Portal (Tier-2 via search-rendered official pages/PDFs + app listing)

- Placement: "RentCafe Resident Portal gives residents one connected place to manage payments, maintenance, renewals and more… a mobile-first digital platform that gives residents one place to manage everything about their home, including rent payments, maintenance requests, move-in tasks, lease renewals, renter essentials and loyalty rewards." [A2]
- Write-back: "All payments post automatically to your ledger in Voyager, eliminating manual processing." "RentCafe Resident Portal connects directly with Voyager to keep payments, work orders, move-ins and renewals in sync with real-time data." [A2]
- Provisioning (official resident guide PDF): "Enter your email address used during your application process and your registration code" — staff-issued registration code binds the account to the application/lease record. [A]
- Occupancy gating (client-deployed official guide): "Only leaseholders have access to all RentCafe Resident Portal features" — payments, work orders, amenity reservations, form signing, deposit payments, lease documents, community updates, bulletin board, authorized guests, absence notification; "To add a leaseholder to your current lease, please contact your Resident Services Team." [A]
- Payments: one-time and recurring; methods bank account / credit card / debit card; autopay with lease-renewal adjustment note ("When you renew your lease, you will need to adjust your monthly amount"); "Splitting Auto-Payments Between Roommates" documented; per-community configuration — "Currently, payments must be made in full" (that community's setting); zero-cost ACH, Apple Pay/Google Pay, flexible rent options (product page). [A]
- Requests: submit with photos and voice memos; Request History; track progress; "If the property has Maintenance Requests enabled…" (app guide) — feature enablement per property; client guide notes terminology alternates "Work Order"/"Maintenance Request" with the same meaning. [A]
- Renewal: "Sign and complete your lease renewal directly in the app"; renewal offers appear in the portal with e-sign (product page). [A]
- Community layer: amenity reservations, package tracking, bulletin board, community updates (app listing: "options vary based on each community"). [A]
- AI layer: Chat IQ assistant for balance/lease/community questions and AI-guided request description (product page). [A2]
- Applicant vs resident: RentCafe FAQ — "Many communities on RentCafe.com offer applicant portals and resident services portals." [A2]

### TownSq / CINC — association pole (Tier-2, FAQ + product pages fetched)

- Self-description: "TownSq is a third-party communication and payment platform chosen by your HOA or management company." [A]
- Provisioning: "Your management company will send you an email invitation with your login details" OR self-register with "Sign up with an account number" (property ZIP + account number → confirm details → create password); "Don't have your account details? Contact your management company." Account anchored in the management company's records. [A]
- Payments: one-time, recurring/autopay, manage payment methods, pay open balance, custom amounts; statements in-app; fees stated ($2.95 + 3.5% credit card; $2.95 eCheck; "may vary by community association"; check/direct-debit without fees arranged via the management company). [A]
- Money boundary: "TownSq is a third-party app and cannot process refunds or waive fees" — refunds and late-fee waivers are management-company acts; billing questions and mailing-address updates route to the management company. [A]
- Requests: "log into your TownSq account and contact your community manager or board members directly through the Requests tab"; architectural requests from any device; maintenance requests; request submissions and direct messaging. [A]
- Community layer: open forums, surveys, event registration, legally binding ballots/voting, documents, amenity bookings, budgets visibility, package tracking, local home-service deals; multiple-property account switching (account picker). [A2]
- CINC Connect (CINC's own resident surface): "branded web and mobile experiences for boards and residents within the CINC platform"; "Native integration with CINC's community association management platform"; role-based — "Boards and residents see the information appropriate to their role"; residents "submit requests and see status"; boards "review and decide when the workflow calls for them"; financial information "based on their role and permissions"; work orders/violations/architectural workflows; amenity reservations, surveys/polls/voting, package tracking, news feeds/group chat; tiered packaging (Essential/Lifestyle/Premium: e-voting, parking, pet registries, e-signatures, access management). [A2]

## Cross-product Comparison

| Structure | Buildium | AppFolio | Entrata | Yardi RentCafe | TownSq/CINC | Evidence |
|---|---|---|---|---|---|---|
| Account anchored in operator records, bound to occupancy | email + resident record; manager invitation | activation email/text from PM company; per-unit activation | enrollment must match Entrata records ("No account found → contact property management") | registration code + application email; leaseholder gating | invitation from management company OR account-number + ZIP self-registration | 5/5 |
| Balance/ledger read (own charges + payments) | payment history; financial transactions | account ledger view | balance due + payment history (incl. roommate payments) | statements; payments post to Voyager ledger | statements; open balance | 5/5 |
| One-time + recurring/autopay payments with saved methods | ePay (EFT/card); scheduled + autopay; edit/delete | Pay Now + autopay; delete/skip/edit; max-limit | one-time + auto payments; method fees | one-time + recurring; roommate split | one-time + autopay + methods | 5/5 |
| Fees displayed; money policy stays with operator | ePay fees configurable; who-pays-fee setting | fee shown before submit; receipts via PM | convenience fees per method | per-community full-balance rule | fees vary by association; refunds/waivers = management company | 5/5 |
| Maintenance/service request submission + status tracking | maintenance request vs general inquiry; attachments; open/closed history | photos; entry permission; time slots; received→scheduled→completed | work orders with photos | photos + voice memos; request history | Requests tab to manager/board; status | 5/5 |
| Documents (lease, statements, community docs) | documents access; lease details | shared documents; lease under Property Details | electronic documents in portal | lease documents; forms | essential documents | 5/5 |
| Announcements/communication from operator | announcements + email copy | email notifications of shared docs | login messages/alerts; newsletters | community updates and notices | news feeds; notifications preferences | 5/5 |
| Profile/contact self-maintenance | contact info; communication preferences | contact info, vehicle, language, reminders, 2FA | profile via enrollment/account | profile update | profile + notification preferences | 5/5 |
| Operator-governed feature availability | settings + per-property overrides; ePay 3-level enablement | payments/maintenance/notice each "can choose to offer" | "configurable by the property… payment methods, payment days, full balance… maintenance request availability" | "options vary based on each community"; "if the property has Maintenance Requests enabled" | "chosen by your HOA or management company"; fees vary by association | 5/5 |
| Mobile app companion | Resident Center app | Online Portal app | ResidentPortal app | RentCafe Resident app | TownSq app | 5/5 |
| Lease/renewal e-signature in portal | lease details view (signing not evidenced) | full e-sign lease + renewal offers | renewals/transfers tools (4.0) | renewal e-sign in app | e-signatures (CINC Lifestyle tier) | 3/5 explicit |
| Roommate/household semantics | (not directly evidenced) | cannot edit/delete roommates' payments | history shows roommate payments | split auto-payments between roommates | (not evidenced) | 3/5 |
| Association surfaces (dues, architectural, board) | association owners; board members run reports | dues; architectural requests; association events | (multifamily focus) | (client-dependent) | assessments; architectural requests; board role surfaces; voting | 3/5 explicit |
| Community engagement layer | community discussions | (not evidenced) | community wall (buy/sell) | bulletin board | forums, surveys, events, ballots, deals | 4/5 |
| Amenity booking hosted in portal | (not evidenced) | (not evidenced) | reserve amenities (app) | reserve amenities (app) | amenity bookings | 3/5 |
| Package notifications | (not evidenced) | (not evidenced) | package pickup alert | package tracking | package tracking | 3/5 |
| Insurance upload/purchase | purchase renters insurance | upload proof / purchase if enabled | RXP insurance products | (not evidenced) | (not evidenced) | 3/5 |
| Notice to vacate / move-out | (not evidenced) | Request Notice to Vacate (if enabled) | Notice to Vacate + move-out charges | (not evidenced) | (not evidenced) | 2/5 |
| Cash-payment network (PaySlip) | (not evidenced) | PaySlip barcode at retail | (not evidenced) | (not evidenced) | check/direct-debit alternatives via manager | 1/5 |
| AI assistant | (not evidenced) | (not evidenced) | (not evidenced this pass) | Chat IQ | TownSq AI reply drafting | 2/5 |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (jointly held; remove any leg and the Type collapses)

1. **Occupancy-anchored authenticated access to the property operator's records.** The resident signs in with an account that lives in the operator's systems and is bound to their occupancy — the lease/tenancy for a rental household, the ownership/residence record for an association household. The occupancy relationship is the axis that structures what the portal shows and allows (unit scope, leaseholder gating, per-property configuration). Accounts are provisioned by the operator or self-registered by matching against operator records. Remove → a public property website or a login wall with nothing behind it.
2. **Self-service over the resident's own occupancy.** Through the surface the resident both reads their own state (balance and ledger, lease and documents, request status, announcements) and changes it with effect in the operator's records: pay rent/assessments and manage autopay, submit maintenance requests and general inquiries, sign leases/renewals where offered, give notice where enabled, update contact details, upload insurance proof. These are actions that would otherwise be phone calls or office visits. Remove → a brochure site or a static document archive (nothing to act on).
3. **Operator-governed surface.** The property operator decides what the portal exposes and allows: which features are enabled at all (payments, maintenance requests, notice to vacate are each documented as operator choices), which payment methods and fee structures apply, whether payments must be made in full, what appears per property/community, and who sees what by role (resident vs roommate vs board member). The portal is the operator's surface onto its records, not a fixed generic account shell. Remove → a generic account center (customer-portal grammar) with no property-operator artifact.

Load-bearing tests:
- 1+3 without 2 = an announcements-only resident site / gated brochure (the pre-self-service web era).
- 1+2 without 3 = a generic account center; loses the operator artifact (drifts to customer-portal territory).
- 2+3 without 1 = a public payment form / open request form with no resident identity (checkout territory).
- Single legs: 1 alone = login wall; 2 alone = payment checkout; 3 alone = marketing website.

### L1 — Common Mature Structure (market-defining expectation, not definitional)

- Balance/ledger visibility (charges, payments, payment history; roommate attribution) — 5/5.
- One-time + recurring/autopay payments with saved payment methods and fees displayed before submit — 5/5.
- Maintenance/service request submission with photos/attachments and status tracking — 5/5.
- Documents center (lease, statements, community documents; email-notified shared documents) — 5/5.
- Announcements/communication from the operator — 5/5.
- Profile/contact self-maintenance with notification preferences — 5/5.
- Companion mobile app — 5/5.
- Dashboard/home surfacing balance due, open requests, alerts — 4/5 explicit.
- Lease/renewal e-signature in the portal — 3/5 explicit (common and growing).
- Roommate/household payment semantics — 3/5.

### L2 — Variant / Optional Structure

- Population pole: rental tenants (rent, lease lifecycle, renewals) ↔ association owners/residents (assessments/dues, architectural requests, board surfaces, voting, violations visibility). Same surface grammar; different charge and request vocabularies.
- Packaging: portal included in a PM suite (Buildium, AppFolio) ↔ branded resident-experience product of an enterprise suite (Entrata ResidentPortal, Yardi RentCafe) ↔ third-party engagement/payments platform chosen by the operator (TownSq, CINC Connect).
- Hosted capabilities: amenity booking, package tracking, visitor/guest management, access management — present in some products as portal tabs; the machinery belongs to neighboring Types.
- Embedded renter services: renters insurance purchase/verification, deposit alternatives, rent reporting to credit bureaus, flexible rent, rewards/loyalty.
- Move-out and lifecycle edges: notice to vacate, estimated move-out charges, move-in tasks; application-to-move-in continuity (drift toward Rental Application Platform).
- Cash-access pole: PaySlip/barcode cash networks for unbanked residents (AppFolio).
- AI layer: assistants answering balance/lease questions, drafting request descriptions, drafting operator replies (RentCafe Chat IQ, TownSq AI) — era-current.
- Segment flavors: student housing (enrollment-cycle), affordable/compliance contexts (certification/recertification self-service observed in the affordable-housing pass), commercial tenant portals (service-request-centric; not deeply sampled).

### L3 — Vendor-specific (research notes only; excluded from final document)

- Buildium: "Resident Center" naming; ePay three-level enablement (account → property → lease); "Sign in as user"; board-member report running; community discussions; MSI-powered insurance; Rent Reporting; Resident Center/ePay reminder emails; "Block Partial ePayments".
- AppFolio: "Online Portal" naming; Authy-based 2FA; certified-funds PaySlip cash network (retail locations, per-transaction fees, per-location limits); bank-statement descriptors ("AF*…"); Spanish language toggle; vehicle info on profile; per-card-brand acceptance rules; eCheck max amounts with fraud-protection limits.
- Entrata: ResidentPortal/ResidentPay/RXP/OXP naming; One-Tap Pay; RentNotify; Pay by Voice; community wall classifieds; charity donation add-on; Visa phone-authorization flow; enrollment error messages ("No account found"); residentportal.com; RealPage-ecosystem integrations.
- Yardi: RentCafe/Chat IQ naming; registration-code provisioning; Voyager ledger posting; rewards/loyalty; flexible rent; bulletin board; "Work Order"/"Maintenance Request" terminology alternation (documented in a client guide); leaseholder-only feature gating (client-deployed guide); Yardi Breeze app guide.
- TownSq/CINC: TownSq Community/Business/Resale Solutions naming; account-number + ZIP self-registration; specific fee schedule; CINC Connect tiers (Essential/Lifestyle/Premium); Cephai+ AI; ONR acquisition; legally binding e-ballots; TownSq's origin as a CINC integration partner.

## Historical / Market-Sample Check

- Early-2000s property-manager website with a resident login — view balance, pay by ACH, submit a request form that emails the office — satisfies all three L0 legs with no mobile app, no autopay, no documents center, no community layer. ✓
- Paper-era analog: the rent book / mailed dues invoice + check by mail + phoning in a repair + architectural request form at the office. The resident acts on their occupancy but through staff-mediated channels; the self-service surface does not exist. Correct failure (pre-history the portal digitized).
- Regional check: UK social-housing "Digital Essentials" packages include resident portals (observed [A] in the affordable-housing-management pass) — same structure under a different regulatory regime; nothing in the core is US-specific. ✓
- Segment check: the association pole (TownSq/CINC) satisfies the same three legs with assessment/architectural vocabulary; the rental pole satisfies them with rent/lease vocabulary. One Type, two populations. ✓
- The definition names no specific technology (no "app", no payment rail), no fee structure, no tab set, no status vocabulary. ✓

## Vendor-specific Findings

See L3 above. Additional notes:

- AppFolio's help page is resident-facing (written to the renter), which is itself evidence of the portal being a mass-market consumer surface, not an operator tool.
- Buildium's troubleshooting article confirms the enablement chain is operator-side configuration, not resident choice: a resident who cannot pay online is told the manager must enable ePay at account/property/lease level.
- TownSq's FAQ is explicit that the platform sits beside the management company: registration data comes from the management company's records; refunds and fee waivers are management-company acts. This is the cleanest verbatim statement of the surface-vs-operator seam.
- Entrata's guide shows the enrollment match against operator records — the portal account cannot be created from nothing; it must correspond to a person the operator already has on file.

## Boundary Findings

1. **vs Residential Property Management (§17)** — DISCHARGES the RPM pass's forward flag as KEEP-BOTH. RPM is the operator-side system of record (managed stock, tenancies, rent cycles, turnover, accounting); the portal is the resident-facing self-service surface onto those records. Removal tests: strip the resident-facing surface from an RPM suite → RPM remains the operator system; strip the operator-side machinery (portfolio, ledger, leasing, work orders) → the portal surface remains but has nothing of its own to keep. All five RPM-sampled products ship a resident surface as a standard capability; the portal also exists as a named market category (ResidentPortal, RentCafe Resident Portal, Resident Center, Online Portal, TownSq), so the resident-side seat deserves its own leaf.
2. **vs Rent Collection Platform (§17)** — DISCHARGES the pre-hung surface-vs-money seam as KEEP-BOTH. The portal hosts the payment UX (methods, autopay, fee display, ledger view); the money machinery (charge creation, late-fee rules, arrears handling, refunds, deposit accounting) lives in the operator-side systems. Evidence: TownSq "cannot process refunds or waive fees"; AppFolio routes receipts and transaction questions to the property manager; Buildium's ePay enablement is operator configuration. A payments-heavy portal (TownSq self-describes as "communication and payment platform") is still the surface — the machinery behind it is not the portal's.
3. **vs Property Maintenance Management (§17)** — DISCHARGES the seam as KEEP-BOTH. Requests originate in the portal (submission, photos, entry permission, time preferences, status visibility); the work-item lifecycle (triage, assignment, scheduling, vendor dispatch, completion, cost) is operator-side. The portal shows the status timeline; it does not run the work.
4. **vs HOA / Community Association Management (§17)** — the association governance/accounting spine (assessments levied, boards, violations, payables) vs the resident/board-facing surface. CINC Connect is explicitly the resident surface "within the CINC platform" with role-based visibility; board members are portal users with elevated roles, but board work (approvals, payables workflows) executes in the management system. KEEP-BOTH.
5. **vs Rental Application Platform (§17)** — prospect-side machinery (applications, screening, lease generation) vs current-resident self-service. Overlap: portals increasingly carry application-to-move-in continuity (Buildium "from application to move-in, and beyond"; RentCafe registration uses the application email; Entrata ships a separate ProspectPortal) and lease e-signing. The application/screening machinery remains the other Type; the portal's anchor is the approved occupancy.
6. **vs Amenity Booking Platform (§17)** — booking machinery (amenity inventory, rules, reservation lifecycle) vs the portal hosting a booking tab (Entrata app, RentCafe app, TownSq, CINC). A portal without amenities remains a portal; an amenity platform can run standalone. KEEP-BOTH per that pass's framing.
7. **vs Package & Mailroom Management / Building Access & Visitor Management (§17)** — those Types own the operational machinery; the portal hosts notifications (package alerts), guest adds, and access-related tabs as capabilities.
8. **vs Customer Portal (§07) / Member Portal (§25) / Employee Service Portal / Mortgage Borrower Portal** — the atlas's `<relationship>-portal` family: same self-service grammar (relationship-anchored access + self-service on one's own relationship + operator-governed surface), different standing anchors (commercial customer/order; organizational membership; employment; mortgage; here: occupancy of a unit in an operator's portfolio). No consolidation (per the member-portal pass's note); the family framing is recorded in each leaf's Related Types.
9. **Vocabulary blur (recorded, no directory change)** — "applicant portal" (prospect-side, RentCafe FAQ distinguishes it), "owner portal" (owner-accounting surface of PM suites — a different counterparty seat), and short-term-rental guest portals (transient stays) are adjacent surfaces, not this leaf.

## Type-status Verdict

Tenant / Resident Portal stands as a separate Application Type: the resident is a distinct primary user with distinct jobs; the market names the surface as a category across segments (suite-included, branded enterprise product, third-party platform); and the atlas's portal family expects an occupancy-anchored member. It is a resident-side surface Type whose value is the seam it maintains against the operator-side systems (property management, rent collection, maintenance, association management) — the same structural position the Member Portal pass canonized for membership.

## Uncertainties

- Buildium help center is SPA-inaccessible from this environment; article content was captured via search-engine rendering of the official help center (verbatim but not directly fetched). Claims are held at that strength; no Buildium-specific numeric detail is asserted.
- Yardi surfaces (yardi.com, rentcafe.com) return 403 from this environment; RentCafe evidence rests on search-rendered official pages, official CDN-hosted resident-guide PDFs, and official app-store listings. Client-deployed guide details (leaseholder gating, full-balance rule) are realizations of per-community configuration, not product defaults.
- Entrata operational help center not attempted; Entrata claims rest on the product page, official resident guide PDF, and official app-store listings.
- Non-US products not directly sampled this pass; UK resident-portal evidence is cross-domain corroboration from the affordable-housing pass.
- Exact fee schedules, payment limits, status vocabularies, and feature defaults vary by product AND by per-property configuration; no universal values are asserted anywhere in the final document.
- Commercial (office/retail) tenant portals were not sampled; they are recorded as an adjacent flavor (service-request-centric) without claims.

## Final Synthesis

A Tenant / Resident Portal is the resident-facing self-service surface of a property operation. Its defining structure is small and jointly-held: resident accounts anchored in the property operator's records and bound to an occupancy (lease/tenancy or ownership/residence) as the axis of access; self-service over the resident's own occupancy — reading balance/ledger, lease documents, request status and announcements, and acting on it (pay rent or assessments, manage autopay, submit and track service requests, sign leases/renewals, give notice, update contact details, upload insurance) with every action writing back into the operator's records; and operator-governed configuration of the surface — which features exist at all, which payment methods and fee rules apply, what appears per property or community, and who sees what by role. Around that core, mature products add the same recognizable layer: balance/ledger visibility with roommate attribution, one-time and autopay payments with saved methods and displayed fees, maintenance-request submission with photos and status timelines, document centers, announcements, profile and notification preferences, and companion mobile apps. Variants extend the Type by population (rental tenants vs association owners), packaging (suite-included vs branded resident-experience product vs third-party engagement platform), hosted capabilities (amenities, packages, guests, access), embedded renter services (insurance, rent reporting, flexible rent), lifecycle edges (application-to-move-in continuity, notice to vacate), and era-current layers (AI assistants). The Type's boundaries hold against the operator-side systems the portal feeds (property management, rent collection, maintenance, association management), the prospect-side application machinery, the hosted-capability Types (amenities, packages, access), and the atlas's other relationship-portal Types (customer, member, employee, borrower) that share the self-service grammar over different standing anchors.
