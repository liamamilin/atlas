# Research Notes — Church Giving Platform

Research date: 2026-09-07

## Research Goal

Understand what a Church Giving Platform actually is as an Application Type: what objects exist inside it (gifts, givers, funds), how money moves from congregation members to the church, how the church administers the resulting contribution records, and where the boundary lies against generic online donation platforms, church management systems (ChMS), payment processors, and donor management systems.

## Initial Boundary (hypothesis before research)

- Core guess: a church-side system for collecting monetary contributions from congregation members and recording them as attributed, fund-designated gifts, with year-end statements and ChMS integration.
- Likely confusions:
  - Online Donation Platform (generic nonprofit) — is this just a vertical variant?
  - Church Management System — many ChMS products contain a contributions module; where is the seam?
  - Payment Processing Platform — modern vendors emphasize owning the payment rails.
  - Donor Management System — vendors market "donor management" as part of giving.
- Unknowns: exact donation record model; fund semantics; statement/receipt mechanics; offline (cash/check) handling; recurring lifecycle; anonymous giving; regional tax regimes.

## Research Questions

1. What is the unit of record (gift/donation)? What fields does it carry?
2. What is a fund, and how does designation work (including multi-fund gifts)?
3. Through which channels do givers give (web, app, text, kiosk, NFC, QR, in-person)?
4. How does recurring giving work (setup, self-serve management, failure handling)?
5. How are offline gifts (cash, checks) recorded and by whom (roles, batches, commit)?
6. How do receipts and year-end statements work, including regional tax regimes?
7. How are gifts attributed to givers (donor profiles, matching, joint donors, anonymous)?
8. What church-side administration exists (reporting, refunds, reassignment, permissions)?
9. How does the platform connect to ChMS people records and to accounting?
10. What distinguishes this Type from a generic Online Donation Platform?

## Representative Products

Selected for market representation, documentation quality, and different product philosophies / customer tiers:

| Product | Philosophy / tier | Evidence quality |
|---|---|---|
| Planning Center Giving | Giving as a module of a ChMS suite; record-keeping first; strong public help center | Tier-1 help articles (7 fetched) + Tier-2 product page |
| Tithe.ly | Giving-first suite for small/mid churches; free giving + paid suite | Tier-1 help articles (3 fetched) + Tier-2 site |
| Pushpay | Enterprise, mobile-first, large churches; owns payment processing | Tier-2 product pages (2 fetched); help center not fetched |
| Givelify | Donor-side app; multi-organization discovery; serves churches + nonprofits | Tier-2 pages (2 fetched); support center not fetched |
| Vanco | Legacy faith-payments heritage (20+ years); online giving + integrations | Tier-2 site (root fetched) |
| ParishSOFT | Historical/regional anchor: Catholic parish/diocese ChMS; separate Offering (record) vs Giving (collect) modules | Tier-2 site (root fetched) |

## Sources

Fetched 2026-09-07:

- Planning Center — product page: https://www.planningcenter.com/giving
- Planning Center Help (Tier 1):
  - Import donation history: https://help.planningcenter.com/en/154395-import-donation-history.html
  - Create and manage funds: https://help.planningcenter.com/en/138385-create-and-manage-funds.html
  - Batches: https://help.planningcenter.com/en/138386-batches.html
  - Anonymous donors and loose cash: https://help.planningcenter.com/en/138373-anonymous-donors-and-loose-cash.html
  - Donor numbers: https://help.planningcenter.com/en/138370-donor-numbers.html
  - Create and share donor statements: https://help.planningcenter.com/en/138407-create-and-share-donor-statements.html
  - Recurring donations: https://help.planningcenter.com/en/138387-recurring-donations.html
- Tithe.ly — site: https://tithe.ly/ ; support center root + Donors category (Tier 1):
  - How to Use Multi-Fund Giving: https://support.tithe.ly/hc/en-us/articles/36920990013079
  - Donation Receipts and Tax Receipts For Donors: https://support.tithe.ly/hc/en-us/articles/30922189182871
- Pushpay — https://www.pushpay.com/ and https://pushpay.com/product/church-giving/
- Givelify — https://www.givelify.com/ and https://www.givelify.com/organizations/solutions/giving/
- Vanco — https://www.vancopayments.com/
- ParishSOFT — https://www.parishsoft.com/

Source-access limitations:

- docs.planningcenter.com (developer docs host) failed twice (transport error) → abandoned; help.planningcenter.com worked and was used instead.
- subsplash.com timed out twice → abandoned; Subsplash Giving excluded from the sample (no claims made about it).
- vancopayments.com/church-giving returned 404; root site used (weaker evidence for Vanco — positioning only).
- Pushpay and Givelify help centers were not fetched; their observations are Tier-2 (marketing/product pages) and are marked accordingly.
- No numeric limits, fees, or defaults from memory; all precise figures below come from fetched pages and are kept in these notes (most do not appear in the final document).

## Product Observations

### Planning Center Giving (evidence layer A — official help center)

**Positioning (Tier 2):** "Online church donation software"; "Tithes, offerings, & reporting"; giving "inside your church database, not siloed" — syncs with People (free ChMS database). Donor surface is Church Center (app/web). Pricing: subscription tiers by donations/month + processing fees (Stripe-powered); donor-covered fees optional (US only); guests can give without logging in.

**Donation record (Tier 1, import article):** required fields = amount, received date, fund, payment method (cash/check/card/ach), donor first + last name; optional = middle/suffix, email, phone, address, donor number, check number/date, campus, memo (donor intent, visible to donor in Church Center), admin notes (internal only), labels, fees, card type/brand/last4. Giving "was designed to handle tax-deductible donations only"; tracks some non-deductible types (QCD, DAF) with separate payment sources; in-kind donations tracked but not importable.

**Funds (Tier 1):** "Funds are used to track the intent of a donor's donation." Every donation must map to a fund. Default fund (created at setup; suggested for the discretionary fund; cannot be closed). Visibility: Listed (in donor dropdown) / Direct link (only via fund URL or Text2Give) / Unpublished (admin-only designation). Open vs closed funds; seasonal funds closed and reopened; renaming is logged; delete only with no history; ledger code for general-ledger mapping; fund descriptions visible to donors; recurring donations continue into closed/unpublished funds until changed; donor permission requested before reassigning designated gifts. "Giving is designed to handle donations only" — sales/payments/reimbursements belong elsewhere; links IRS Tax Guide for Churches.

**Batches / offline recording (Tier 1):** batches track physical donations (cash, checks), external payment sources, and imports. Roles: counters can create/enter; only administrators/bookkeepers can commit. Batch groups (e.g., per Sunday service); batch defaults (fund, received date, payment source, method). Manual entry with donor matching against People (create-new-person fallback); joint donors (join two people to one giving record); split donation across funds (⊕); received date = the date the donor receives credit (year-end caution); check reader hardware (MICR; bill-pay caveat). Commit semantics: in-progress donations are invisible to donors, excluded from statements, automations don't fire, marked "Uncommitted", changes not logged; after commit they become fully qualified donations, receipts send, changes are logged in system logs. Deleting a committed batch is logged.

**Anonymous / loose cash (Tier 1):** anonymous donor record for loose cash/unidentified checks; anonymous gifts appear in reports via an "anonymous" stamp, not on the People page; online giving cannot be anonymous (name + email required).

**Donor numbers (Tier 1):** optional feature for organizations that "use numbers to identify donors, like using numbered envelopes"; assign per donor, search by #number, export CSV. (Explicit continuity with the envelope-number offertory tradition.)

**Statements (Tier 1):** donor statements list successful donations over a date range "which helps them file their taxes"; exclude failed, refunded, and in-progress donations; cover letter with variables; deliverability report (missing email/address); email and/or print; joint donors share a statement; donors self-serve all statements on Church Center; statement immutable once emailed. Regional formats: US (itemized with fund subtotals + tax disclaimer), Canada (CRA official receipt: receipt number, replaced-receipt number, treasurer signature, address rules; total-only), Australia, New Zealand (IRD option). Non-deductible (DAF/QCD) include/exclude; pledge campaign progress optionally shown.

**Recurring (Tier 1):** donor- or admin-created; frequencies weekly/biweekly/monthly/twice-monthly patterns; split across funds; statuses Active / On hold indefinitely / On hold until; failures (insufficient funds, invalid card, removed method, bank rejection) notify donor + subscribed admins; no auto-retry of the failed date — next scheduled occurrence proceeds; donor can fix/hold/delete or recover via one-time gift; if a donor profile is marked deceased, recurring donations are set to On Hold; donor emailed when admin edits.

**Other (Tier 2 + FAQ):** reports by donor/fund/campus/pledge/payout; recurring-donation forecasting; automatic card updates; in-kind tracking (vehicles, furniture, services); embed form, QR codes, NFC tags (Links app); text-to-give; CSV exports + public API (no QuickBooks integration); four permission levels; multi-campus via campus attribute (not separate funds); pledge campaigns with goals/progress.

### Tithe.ly (evidence layer A for donor-side articles; layer B elsewhere)

**Positioning (Tier 2):** "#1 Church Software Platform"; Giving free (transaction fees only) with paid suite (ChMS, apps, sites, service planning); "I AM A CHURCH / I AM A GIVER" split entry. Giving features: online form, mobile app, text giving, kiosk, NFC tap discs, pledge campaigns, insights dashboard, recurring, Cover the Fees™, end-of-year tax statements; available in English, Spanish, French, Japanese, Chinese. People database "syncs directly with your giving data."

**Donor account (Tier 1 category):** donors create a personal donor account (app or desktop); giving history in app; can select a different church on the giving form (one donor account gives to multiple churches); giving reminders; duplicate donor accounts are a known failure mode (identity matching matters).

**Multi-fund giving (Tier 1):** donor can split one transaction across up to 5 funds; one-time only (recurring per fund requires separate setups); processed as a single charge (bank statement shows total) but tracked as separate per-fund line items; admin can refund a specific fund portion; multi-fund gifts flagged with an icon in Transactions.

**Receipts (Tier 1):** automatic per-gift receipts contain date of gift, organization name, amount, fund/designation, gift ID. Annual tax receipts are issued by the church/organization, not the platform; donor statement errors are resolved with the church, not support. Canadian note: email receipts may not serve as official tax receipts under Canadian tax law.

**Donor-side flows (Tier 1 article list):** QuickGive™ in-app; make a donation (app/desktop); create/update recurring gifts; turn one-time gift into recurring; pledge toward a pledge campaign; 3D Secure verification; text giving guide.

### Pushpay (evidence layer B — official product pages only)

**Positioning:** "church engagement platform"; Giving product page: "standalone church giving software"; claims 14,000+ churches, 7 of 10 largest US churches (marketing claims, kept as claims).

**Channels:** mobile app, online/web (embedded giving), text giving, kiosk, tap-to-give (NFC via partner), branded QR codes and pre-configured giving links.

**Payment methods:** credit/debit, ACH, Apple Pay, Google Pay, stock and crypto (via partner); "cash, check, and non-cash donations can also be managed within Pushpay for a complete donor management experience" — i.e., offline gifts are recorded, not processed.

**Structures observed:** recurring gifts; future-dated gifts; campaigns and pledges; multi-site management; multi-language (Spanish web giving); giving statements "for tax purposes"; donor sign-in ("personal account for giving, recurring gifts, and managing payment details"); AI Q&A over giving data; failed-payment recovery / card-updater suite (Everygift® — vendor-branded); 80+ integrations incl. ChMS and accounting; direct payment processing ("we own the giving infrastructure").

### Givelify (evidence layer B — official product pages only)

**Positioning:** donor-side giving app; "more than 80,000 organizations"; donors discover organizations ("Find a Cause"); serves both "Places of worship" and "Nonprofits" — the same product spans the church and generic-nonprofit markets.

**Structures observed:** three-tap giving flow; giving 24/7 from app/web/social/in-person; raise funds "for specific causes, goals, and projects" (designation analog); personal thank-you notes to givers; in-person giving events ("Givelithon" — vendor-branded); next-business-day deposits; organization-side analytics studio, donor management, integrations; bookkeeping "built around your actual needs."

### Vanco (evidence layer B — official site root only)

**Positioning:** payments/donation processing for faith organizations and nonprofits; "20+ years serving churches"; 25,000+ organizations; 60+ integrations with church tools (incl. ChMS). Faith software list: online giving, mobile church app, live streaming, donor communication, reporting dashboards, text-to-give, events, mobile card reader, ChMS integrations. Legacy heritage: long-standing electronic giving / direct-debit provider for congregations.

### ParishSOFT (evidence layer B — official site root; historical/regional anchor)

**Positioning:** Catholic parish & diocese ChMS "built by Catholics for Catholics"; suite includes Families/census, Faith Formation, Accounting, Tuition, Websites, Mobile App, etc.

**Key structural observation:** the suite separates **Offering** ("track giving and pledges with superb reporting") from **Giving** ("easy online and recurring donation options for parishioners"). I.e., in the Catholic parish heritage, contribution *recording* (offertory/envelope side) and online *collection* are distinct modules. This confirms that the record half of the Type has a long history independent of online payment, and that the record half overlaps the ChMS contribution module.

## Cross-product Comparison

| Structure | Planning Center | Tithe.ly | Pushpay | Givelify | Vanco | ParishSOFT |
|---|---|---|---|---|---|---|
| Gift as recorded unit (amount/date/method) | A: yes (field list) | A: yes (receipts, history) | B: yes ("track every contribution") | B: yes | B: yes | B: yes (Offering) |
| Giver attribution (donor profiles) | A: yes (People-matched profiles, joint donors, anonymous) | A: yes (donor accounts; duplicates issue) | B: yes (donor sign-in) | B: yes (donor accounts) | B: yes | B: yes (Families link) |
| Anonymous giving | A: yes (offline only; online requires name+email) | not observed | not observed | not observed | not observed | not observed |
| Funds / designation | A: yes (rich: default/listed/direct/unpublished, open/closed, ledger code) | A: yes (multi-fund ≤5, per-fund refund) | B: yes (campaigns/funds) | B: yes (causes/goals/projects) | B: yes | B: yes (Offering funds) |
| Online giving form/page | A: yes (Church Center, embed, direct links) | A/B: yes | B: yes | B: yes (app-first) | B: yes | B: yes |
| Mobile app giving | A: yes (Church Center app) | A/B: yes | B: yes | B: yes (primary) | B: yes | B: yes (mobile app) |
| Text giving | A: yes (Text2Give + fund shortcuts) | B: yes | B: yes | not observed | B: yes | not observed |
| Kiosk / in-person hardware | A: check reader; NFC tags (Links) | B: kiosk, NFC tap discs | B: kiosk, tap-to-give | B: in-person events | B: mobile card reader | not observed |
| Recurring giving | A: yes (statuses, failure handling, deceased→hold) | A/B: yes (one-time→recurring conversion) | B: yes (+ future-dated) | not observed | B: yes | B: yes |
| Pledge campaigns | A: yes (goals/progress on statements) | A/B: yes (donor-side pledging) | B: yes | B: causes/goals | not observed | B: yes (Offering pledges) |
| Statements / receipts | A: yes (per-gift receipts; year-end; US/CRA/AU/NZ formats) | A: yes (receipt fields; church issues annual) | B: yes ("for tax purposes") | not observed | not observed | B: yes (reporting) |
| Offline recording (cash/check) | A: yes (batches, counters, commit, check reader) | not observed (manual entry implied by FAQ re: Venmo/PayPal) | B: yes ("managed within") | not observed | not observed | B: yes (Offering) |
| ChMS people-record integration | A: native (same suite, People) | B: native (People product) | B: integrations (80+) | B: integrations | B: integrations (60+) | B: native (same suite) |
| Accounting export/integration | A: CSV export; ledger codes; no QuickBooks | not observed | B: integrations | B: bookkeeping | B: integrations | B: Accounting module |
| Multi-campus | A: yes (campus attribute) | not observed | B: yes (multi-site) | not observed | not observed | B: diocese/parish structure |
| Donor-covered fees | A: yes (US only) | B: yes (Cover the Fees™) | not observed | not observed | not observed | not observed |
| Donor discovery across orgs | no (church-owned channels) | partial (donor account spans churches) | no | yes (core philosophy) | no | no |
| Non-church (generic nonprofit) use | no (church-focused) | church-focused | church (+ Catholic parishes) | yes (explicit) | yes (explicit) | no (Catholic only) |

## Abstraction Levels

### L0 — Defining Invariant

A Church Giving Platform is the church-side system through which monetary contributions are given and recorded. Minimal structures, all required:

1. **Gift record** — each contribution is recorded as a discrete gift: amount, date received, payment method/channel.
2. **Giver attribution** — gifts are creditable to givers (identified persons, or an explicit anonymous record for unattributable gifts).
3. **Fund designation** — gifts are designated to church-defined funds (purposes), including a default/general fund; designation records the donor's intent.
4. **Church-side administration** — the church (not the giver alone) administers the giving process: manages funds and giver records, reviews/corrects gifts, and issues receipts/statements to givers.

The platform is the channel through which gifts reach the church *and* the system of record for what was given. Remove the record half → it is a payment processor. Remove the channel half and the church-administration half → it is a spreadsheet. Remove giver attribution + funds + administration → it is a generic checkout.

§24 historical check: envelope-based offertory recording (donor numbers, ParishSOFT Offering) satisfies this definition with a purely physical channel — gifts recorded per giver per fund, statements issued, church-administered. Online payment is NOT definitional. ✓

### L1 — Common Mature Structure

- Online giving form/page (branded, embeddable, shareable links/QR)
- Mobile app giving (church app or donor app)
- Text-to-give
- Payment methods: card, ACH/bank transfer, digital wallets; donor-covered fees option
- Recurring giving: schedules, donor self-serve management, failure notification, card-updater assistance
- Giver self-serve account: giving history, saved payment methods, statements
- Guest giving without an account
- Per-gift receipts + year-end giving statements (tax purpose)
- Pledge campaigns tied to funds, with progress tracking
- Reporting: by fund, donor, campus, payment type, time period; deposit/payout views
- Offline gift recording: cash/check entry, batching with commit semantics, check scanning/reading
- ChMS people-record integration (native or via integrations)
- Accounting export/integration (CSV or API)
- Multi-campus support
- Staff roles/permissions (at minimum: full admin vs restricted entry roles)
- Refunds (full and partial)

### L2 — Variant / Optional Structure

- Stock / crypto giving; in-kind non-cash gift tracking
- Donor-discovery marketplace pole (donor app that spans organizations) vs church-owned-channels pole
- Suite membership: standalone giving vs ChMS module vs engagement-platform module
- Regional tax-receipt regimes (US itemized vs CRA official receipt vs IRD) and multi-language giving
- Denominational packaging (Catholic parish/diocese structures; sacrament-adjacent modules)
- AI insights / generosity analytics / donor engagement messaging
- Future-dated gifts, giving reminders, thank-you notes
- Kiosk/NFC hardware programs
- Pricing shapes: free + processing fees, subscription tiers, enterprise contracts
- Donor numbers (envelope-number heritage) as an optional feature

### L3 — Vendor-specific (research notes only)

- Pushpay: Everygift® (Assured Payments, Failed Payment Recovery, Recurring Suggestion), ChurchStaq/ParishStaq suites, VisitorTap, "6-second giving", direct processing as ISO of KeyBank.
- Tithe.ly: QuickGive™, Cover the Fees™, Tap Discs, All Access bundle, multi-fund ≤5 limit, single-charge multi-fund processing.
- Planning Center: Church Center donor surface, Links/NFC app, batch groups, four permission levels, Stripe-powered processing, subscription-by-donation-volume pricing, "Giving is designed to handle donations only" posture.
- Givelify: Givelithon, Analytics Studio, Bravo stories, three-tap flow.
- Vanco: egiving suite naming, 25,000+ churches claim.
- ParishSOFT: Offering vs Giving module split, diocesan compliance, Ministry Brands ownership.

## Vendor-specific / Rejected Findings

Rejected from the canonical model (with reasons):

- **"Owning the payment rails" is definitional** — rejected. Pushpay markets direct processing; Planning Center explicitly runs on Stripe. Channel ownership is a vendor strategy, not the Type.
- **Multi-fund split limit (5)** — product-specific (Tithe.ly). The *ability* to split across funds is cross-product; the limit is not.
- **Donor numbers / envelope numbers** — optional feature (Planning Center), heritage continuity, not definitional.
- **Donor discovery marketplace** — one product's philosophy (Givelify); the church-owned-channel pole is at least as dominant.
- **"Giving grows X% with product Y"** — vendor marketing claims; kept as claims, excluded from the model.
- **Specific fee percentages / subscription prices** — observed but plan/region-specific; excluded from the final document.
- **Deceased-donor auto-hold rule** — observed in one product (Planning Center); treated as an example of pastoral-data sensitivity, not a universal rule (noted as product-specific in the final doc if mentioned).

## Boundary Findings

1. **vs Online Donation Platform (generic nonprofit).** The closest sibling. Shared: gift records, designations, recurring, receipts, donor-covered fees. Distinct in the church Type: giver attribution is anchored in the congregation's people records (member-linked giving), funds vocabulary is congregational (general/missions/building/benevolence), year-end giving statements are a first-class deliverable, ChMS integration is standard, and the vendor ecosystem is church-specific. Givelify literally serves both markets with one product — evidence that the boundary is a specialization seam, not a hard wall. Judgment: keep as a separate Type (distinct object model + distinct market), but flag the variant relationship.
2. **vs Church Management System (ChMS).** ChMS owns people/membership/ministry life; the giving platform owns collection channels + contribution records + money movement. Overlap: ChMS contribution modules (ParishSOFT Offering; Planning Center Giving is itself a ChMS-suite module). Seam test: if the product's center of gravity is parish life (groups, classes, check-in, pastoral care) it is ChMS even with a contributions module; if the center is the giving process itself, it is this Type. The two meet at the giver record.
3. **vs Payment Processing Platform.** A processor moves money and knows nothing of funds, giver credit, or statements. The giving platform's gift record (attribution + designation + statement) is the difference. Vertical integration (Pushpay) blurs the market position, not the Type.
4. **vs Donor Management System / Nonprofit CRM.** DMS manages relationships and cultivation across campaigns and communications; the giving platform's donor surface is narrower (giving history, payment methods, statements). Vendors drift into DMS (Pushpay "Donor Development", Givelify "Donor management") — adjacent expansion, not the core.
5. **vs Nonprofit Fund Accounting.** Fund accounting keeps the books (restricted funds, ledgers); the giving platform records intent-level gifts and hands summaries to accounting (ledger codes, CSV export). Planning Center's "donations only" posture documents the seam from inside.
6. **vs Membership Billing.** Membership dues are owed by right of membership (invoiced, billable); gifts are voluntary with no receivable semantics. ParishSOFT's separate Tuition module (invoicing) vs Offering/Giving confirms the split.

## Uncertainties

- Pushpay and Givelify help centers were not fetched; their internal record models (e.g., how funds and statements are structured) are inferred from product pages only (Tier 2). Assertions about them are kept coarse.
- Subsplash Giving was dropped (timeouts); no claims.
- Vanco evidence is root-site only; its current feature depth (e.g., statements, batching) is unverified.
- Whether "annual statements issued by the church, not the platform" is universal (observed explicitly in Tithe.ly; Planning Center's statements are generated by the church admin within the platform — functionally equivalent, but the responsibility framing differs).
- Regional tax regimes beyond US/CA/AU/NZ (e.g., UK Gift Aid) were not researched; the final document treats tax-statement formats as region-dependent without enumerating regimes beyond the sampled ones.
- Kiosk hardware depth (SecureGive-style dedicated kiosk vendors) not sampled; kiosk treated as a channel variant only.

## Final Synthesis

The Church Giving Platform is the congregational specialization of the donation-collection Type: a church-administered system that operates giving channels (online form, app, text, kiosk, in-person recording) and records every gift as an attributable, fund-designated entry in the church's contribution record, from which receipts, year-end statements, and reports flow, and which connects to the church's people records (ChMS) and books (accounting). Its defining core is small — gift record + giver attribution + fund designation + church-side administration — and survives the historical check: envelope-based offertory recording satisfies it without any online payment. Everything else (channels, recurring, pledges, regional tax formats, discovery marketplaces, AI) is mature common structure or variant.
