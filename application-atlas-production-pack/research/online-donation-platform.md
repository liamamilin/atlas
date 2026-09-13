# Research Notes — Online Donation Platform

Research date: 2026-09-08
Slug: online-donation-platform
Directory leaf: Online Donation Platform (§25 Nonprofit, Membership & Religious Organizations)

## Research Goal

Understand what an Online Donation Platform actually is as an Application Type: what objects exist inside it (donations/gifts, donation forms, designations, recurring plans, receipts, payouts, donor records), who uses it (donors vs organization staff), how a gift moves from a website/app into the organization's hands, which rules govern receipting/money/settlement, and how the Type differs from its four closest §25 siblings (Donor Management System, Fundraising Management Platform, Peer-to-peer Fundraising Platform, Nonprofit Crowdfunding Platform), from Church Giving Platform, and from generic payment/checkout infrastructure.

## Sibling-pass obligations (processed before this pass)

Four processed siblings left flags that this pass must discharge or keep standing:

- **donor-management-system** (processed 2026-09-07, flag 1): vs online-donation-platform — discriminators adopted: system-of-record side (org-side constituency database vs donor-facing collection flow) and center (constituency stewardship vs campaign machinery). Joint review requested when this leaf is processed → discharge this pass.
- **church-giving-platform** (processed 2026-09-07): probable vertical-specialization pair; Givelify serves both markets from one product; church variant carries a distinct object layer (member-database-linked giver attribution, congregational funds vocabulary, year-end giving statements as first-class deliverable, ChMS integration fabric). Candidate outcomes: two Types or consolidation view → joint review discharge this pass.
- **nonprofit-crowdfunding-platform** (processed 2026-09-08, forward flag): family grid — who runs the fundraiser (org vs supporters) × record center (transaction vs campaign vs program); pre-recorded removal tests both directions ("strip campaigns+crowd machinery → donation platform remains; strip standing transaction capability → crowdfunding remains"); keep-both recommended → discharge this pass.
- **nonprofit-crm** (processed 2026-09-08): forward note adopting donor-pass discriminators for this leaf → adopt, note discharged.

Still unprocessed siblings (flags stand): fundraising-management-platform (its pass appears interrupted — no research doc, no STATUS entry), peer-to-peer-fundraising-platform.

## Initial Boundary

Working hypothesis before research:

- Core use: a nonprofit (or church, or similar organization) accepts charitable donations online through forms/pages/buttons it controls, with the platform recording gifts, issuing receipts, settling money to the organization, and giving the org a console over the whole flow.
- Likely users: donors (public-facing side) + development/finance staff (org console).
- Nearest confusion risks: Donor Management System (org-side record), Crowdfunding/P2P (campaign containers), Fundraising Management (program machinery), Church Giving Platform (congregational variant), Payment Gateway/Checkout Platform (generic money movement), Event Registration (tickets vs gifts), Membership Billing (dues vs gifts).
- Unknowns: money-flow models (platform-processed vs BYO processor); whether the org console is definitional or merely universal; how designations/funds are modeled; receipting regimes.

## Research Questions

1. What is the donor-facing giving flow end-to-end, and on which surfaces does it start (embedded form, hosted page, button/snippet, app, text, QR)?
2. What objects exist: donation/gift, donation form/page, designation/fund, recurring plan, payment, receipt, payout/deposit, donor record?
3. What does the organization-side console actually do (create forms, view gifts, receipts, payouts, reporting, donor lookup)?
4. How does money move — platform as processor of record, or bring-your-own gateway?
5. How are recurring gifts modeled and managed (upsell, self-service portal, retries, migration)?
6. How are designations/restricted causes modeled?
7. What receipting/tax-document machinery exists (immediate receipts, year-end statements, regional regimes such as US deductibility / UK Gift Aid)?
8. What fee machinery exists (platform fees, processing fees, donor-covers-fees)?
9. How much donor record does the platform keep, and how does it connect to CRMs/accounting?
10. Where does this Type end vs campaign machinery (crowdfunding/P2P), org-side record systems (DMS), the congregational variant, and generic payment infrastructure?

## Representative Products

Selected for market representativeness, documentation reachability, distinct product philosophies, and different customer tiers:

1. **Fundraise Up** — enterprise pole; "donation checkout" optimization philosophy; installs as a snippet on the org's existing website; large nonprofits (UNICEF USA, Salvation Army UK, Canadian Red Cross per its own pages).
2. **Bloomerang Fundraising (formerly Qgiv)** — mid-market suite pole; donation forms as one product line inside a giving platform (events, text, P2P, auctions, CRM, reporting); also the recorded straddling pole from the crowdfunding pass.
3. **Givelify** — consumer-app-first pole; mobile giving app with a donor-side discovery marketplace; explicitly serves both "Churches & Nonprofits"; the bridge sample for the church-giving joint review.
4. **Raisely** — lightweight/modern pole (AU-origin, multi-region); embed-or-share donation forms; bring-your-own Stripe/PayPal money flow; part of a nonprofit operations suite (Velora: Aplos + Raisely + Keela).

Attempted and abandoned (source-access limitation): **Donorbox** (403 ×2), **GiveWP** (givewp.com 403, docs.givewp.com 403), **Givebutter** (403) — the same three products the crowdfunding pass could not reach; **help.qgiv.com** (transport error), **support.fundraiseup.com** (transport error). Consequence: the self-hosted-WordPress pole and the free/fee-optional all-in-one pole are under-sampled; no claims in this pass rest on those vendors. Evidence below is product-page level (Tier 2) for all four sampled products; help-center-level operational claims are avoided.

## Sources

- Fundraise Up — https://fundraiseup.com/ (home), https://fundraiseup.com/features/checkout/ — fetched 2026-09-08.
- Bloomerang Fundraising (formerly Qgiv) — https://www.qgiv.com/ (home), https://www.qgiv.com/donation-forms — fetched 2026-09-08.
- Givelify — https://www.givelify.com/ (home), https://www.givelify.com/organizations/solutions/giving/, https://www.givelify.com/organizations/solutions/donor-management/ — fetched 2026-09-08.
- Raisely — https://raisely.com/ (home), https://raisely.com/online-giving — fetched 2026-09-08.
- Cross-referenced processed sibling research: research/donor-management-system.md, research/church-giving-platform.md, research/nonprofit-crowdfunding-platform.md (STATUS entries 2026-09-07/08).
- Sibling-pass recorded limitations reused: nonprofit-crowdfunding-platform pass ("Classy/GoFundMe Pro, Givebutter, Donorbox unreachable").

## Product A — Fundraise Up

### Key observations (evidence layer A = directly observed on official pages)

- Self-description (schema.org + page copy): "Fundraise Up is a donation platform that helps nonprofits increase online revenue with AI-optimized donor experiences, advanced payment options, and deep analytics." The vendor labels the category "donation platform" and "the nonprofit digital fundraising platform for online giving."
- **Checkout** = an optimized donation form that "installs as a simple snippet on your existing website, so donors can give without being redirected to a third-party page"; brandable (logo, copy, images, videos, impact descriptions, designations, custom questions, tribute fields).
- **Elements** = "pre-built UI components" for websites (the embed surface layer).
- Feature blurbs (product-page level, each A): **Designations** — "Categorize, code, and track donations"; **Tributes** — "Celebrate loved ones with dedicated donation"; **Donors cover fee** — "Get donors to cover your transaction fees at checkout"; **Impact descriptions** — donor-visible outcome per suggested gift; **Custom questions** — post-conversion gathering; **Address validation**; **White label** — "Zero-out vendor mentions in your donor experience"; **Abandoned donations** — "Recover abandoned donors with contact capture"; **Crypto donations** — "Accept crypto as easily as you accept credit cards."
- **Recurring giving**: recurring upsells surfaced "at key moments during and after the donation, so donors can opt in with one tap. Once they subscribe, they can manage their own plan, payment method, receipts, and preferences through the **Donor Portal**." Case-study quote evidences recurring-plan migration as a routine operation ("We migrated 6,000 recurring donations to Fundraise Up").
- **Payments**: cards, digital wallets, bank transfers (ACH US, SEPA, Bacs, BECS, Canadian PADs, iDEAL|Wero), PayPal, Venmo, crypto; "20+ global payment options", "135+ currencies", "23 languages supported"; **Gift Aid** posture evidenced by UK case study ("74% of donors claimed Gift Aid") — claim-capable UK posture, not help-doc verified.
- **Integrations**: "Push 100+ fundraising and marketing datapoints to 10+ native integrations" — Salesforce (incl. NPSP), Bloomerang, Virtuous, Raiser's Edge, DonorPerfect, NEON, Kindful, HubSpot, plus Zapier/Omatic and a REST API for "custom real-time syncing workflows". The platform is positioned as a capture layer feeding org-side systems.
- **P2P fundraising exists as a module** ("Turn more high-intent supporters into successful fundraisers") — suite overlap, not the center.
- Security/fraud/compliance/scalability pages (GivingTuesday/Dec 31 peak framing); enterprise support standard.
- Fee posture: pricing schema "No setup fees, no contracts… 80% of donors cover fees automatically" (marketing figure — recorded, not asserted).

## Product B — Bloomerang Fundraising (formerly Qgiv)

### Key observations

- Rebrand fact: "Qgiv is now Bloomerang Fundraising! The same trusted fundraising tools are now part of the Bloomerang Giving Platform." Product line: **Donation Forms**, Event Management, Text Fundraising ("Donors initiate a gift via text before visiting a mobile form to complete their donation"), Peer-to-Peer, Auctions, **Donor Management | CRM**, Data/Reports/Statistics, Integrations.
- **Donation Forms product page** (the Type's center within this suite): "Online donation forms… make the giving experience quick and simple."
  - **Mobile-first forms** ("donation forms designed to wow supporters").
  - **Monthly-giving encouragement** ("encouraging monthly giving—transforming every gift into long-term support").
  - **Intelligent donor conversion** — "one-click donations, smart suggestions, **abandoned gift recovery**, and **flexible giving plans**".
  - **Donor portals** — "Give donors control with a custom, self-service portal where they can **manage recurring gifts and download receipts and tax documents** in minutes." (Direct evidence: receipts + tax documents as donor-facing deliverables.)
  - **Communication tools** — automated "personalized acknowledgments, appeals, and reminders" (acknowledgment machinery on the platform).
  - **Reporting tools** — "customize, automate, and send reports".
- Suite context confirms the family grid: the standing donation-forms capability sits alongside campaign machinery (events, P2P, auctions) and org-side machinery (CRM, reporting) as separate product lines — packaging evidence that these are adjacent centers, not one blob.

## Product C — Givelify

### Key observations

- Positioning: "Best app to give and collect online donations for your church or nonprofit" — **explicit dual market** (churches + nonprofits), matching the church-giving pass's bridging observation.
- Two-sided structure: a **donor-facing giving app** ("Find a Cause" — searchable discovery over "more than 80,000 organizations"; ~2M donors claimed) plus an **organization side** (Sign Up, console at analytics.givelify.com).
- **Giving solution page**: "The app built for giving"; **three-tap giving experience**; 24/7 giving "on your website. On social media. Even in person" (Givelithon = in-person giving event); "get those gifts the **next business day**" (payout-timing claim — product-specific, not generalized).
- Org features: "Show gratitude with personal thank-you notes to givers"; "**Raise funds for specific causes, goals, and projects**" (designation-like causes); Analytics Studio — "track each donation with built-in donation management tools. Break your data down… Daily, monthly, by donor."
- **Donor-management solution page**: "Church & Nonprofit Donor Management System… More than record-keeping." Reconciliation breadth: "However you reconcile your finances, we support you. **QuickBooks. Church management systems. Even manually.**" Tax-time: "Our financial reporting makes it effortless to collect your donation records at tax time… **We even send donation reports to your donors** so that you don't have to." (Platform-generated donor giving reports — evidence that donor-side tax documentation sits on the platform.)
- Distinct philosophy: the giving capability is delivered primarily through a consumer app + discovery marketplace, with website/social/embedding as additional surfaces — versus form-embed products.

## Product D — Raisely

### Key observations

- Positioning: "fundraising platform for charities and nonprofits… all for free"; features: Peer-to-Peer, Supporter Management, Ticketed Events, **Donation Pages & Appeals**, DIY Fundraising, **Regular Giving**, **Online Giving & Donation Forms**, AI Solutions, Integrations, Messages.
- **Online Giving page** (operational detail):
  - "3-step donation form… looks good on any device" (mobile-first).
  - Two deploy surfaces: "**Embed on your website** — copy-paste an embed code" or "**Share it as a donation page** — a Raisely link… on a customised landing page."
  - **One-click wallets** — PayPal, Google Pay, Apple Pay.
  - **Recurring**: "Accept **weekly, monthly, or yearly** donations. Save time with **automatic emails and payment retries**."
  - **Matched giving** — "single or multiple matched giving periods on your campaign."
  - **Money flow (BYO processor pole)**: "Get payments directly to your bank — Your donation goes straight to **your own Stripe or PayPal account**, who will charge a small fee per transaction." Direct evidence that the platform does not have to be the processor of record; the gift capture/record layer is the product.
  - "Secure payments in **130+ currencies**"; multilingual campaigns.
- Suite context: built-in CRM ("Easy Donor Management… Built-in CRM"), "instantly sync your donors to one of many non-profit CRMs"; region pages AU/NZ/US/UK/CA/IE/SG/HK; Velora suite (Aplos fund accounting + Raisely + Keela CRM) — donation capture inside a nonprofit-operations portfolio.

## Cross-product Comparison

| Structure | Fundraise Up | Bloomerang Fundraising (Qgiv) | Givelify | Raisely | Strength |
|---|---|---|---|---|---|
| Standing donor-facing give surface (evergreen, org-controlled) | Checkout snippet + Elements on org site | Donation Forms product line | App + website/social surfaces, 24/7 | Embed code + hosted donation page | **B — all four** |
| Donation recorded as a gift from an identified donor, settled to the organization | implied by "donation platform" + integrations ("datapoints" incl. donation data) | donation forms → CRM/reports | "track each donation"; deposits to org | "payments directly to your bank" | **B — all four** |
| Org-side console operating the give capability | platform managed on org's behalf + integrations; brand config | form creation + reporting + CRM | Analytics Studio; signup console | admin (admin.raisely.com) + page builder | **B — all four** |
| Suggested/ask amounts on the form | AI-suggested ask amounts | "smart suggestions" | preset amounts (three-tap flow) | tuned form | **B — all four** (mechanism varies) |
| Recurring giving as a managed plan | upsell at/after checkout; Donor Portal self-manage; plan migration | monthly-giving encouragement; flexible giving plans; donor portal self-manage | (not directly observed on fetched pages) | weekly/monthly/yearly; retries; automatic emails | **B — three of four**; treat as standard |
| Donor self-service portal (manage plan/receipts) | Donor Portal (explicit) | Donor portal (explicit: manage recurring, download receipts & tax documents) | donor app serves the same function from donor side | (not observed) | **B — two explicit**; concept standard |
| Receipts / tax documents | receipts in Donor Portal; UK Gift Aid posture | "download receipts and tax documents" | platform sends donation reports to donors; tax-time records | (not observed) | **B — three of four**; treat as standard |
| Designations / causes / funds | Designations: "categorize, code, and track" | (implied via CRM coding; not explicit on fetched page) | "raise funds for specific causes, goals, and projects" | campaigns/appeals as purposes | **B — moderate** |
| Cover-the-fees option | explicit feature; case-study percentages | (not observed) | (not observed; "no hidden fees" is org-side pricing) | (not observed) | **A single-product in sample** + family cross-pass support (church pass); keep moderate |
| Abandoned-gift recovery | explicit (contact capture) | explicit ("abandoned gift recovery") | — | — | **B — two of four** |
| Tribute / memorial gifts | explicit | — | — | — | A single-product; optional |
| Matched giving | — | — | — | explicit (multiple matched periods) | A single-product; optional |
| Org reporting/dashboards | analytics positioning | "Data, Reports, & Statistics" | Analytics Studio | reporting + supporter management | **B — all four** |
| CRM/accounting handoff | native CRM integrations + REST API | CRM product line + integrations | QuickBooks / ChMS / manual reconciliation | built-in CRM + sync to CRMs; Velora suite | **B — all four** |
| Mobile-first donor experience | mobile-first checkout | mobile-first forms | app-native (three-tap) | mobile-first 3-step form | **B — all four** |
| Wallets (Apple/Google Pay etc.) | 20+ methods incl. wallets | one-click donations | app payments | PayPal/Google Pay/Apple Pay | **B — all four** |
| Money flow: platform-processed | yes (platform handles payments) | yes | yes | **no — BYO Stripe/PayPal** | Variant, both poles evidenced |
| Channel variants (text, in-person, app) | (snippet web only observed) | Text Fundraising | app + in-person Givelithon | (web) | Variant |
| Donor discovery marketplace | no | no | **yes — Find a Cause** | no | Variant (single-product) |
| Campaign/P2P machinery as module | P2P module | P2P + events + auctions | causes/goals (light) | P2P + appeals + ticketed events | **B — module pattern across sample** |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (smallest stable structure)

Three jointly-held structures. Remove any one and the product stops being recognizable as an Online Donation Platform:

1. **The standing donor-facing give capability.** A persistent, organization-controlled capture surface — a donation form, page, button/snippet, or app entry — through which anyone can give to the organization at any time, without needing a campaign container to exist. It is evergreen by default.
   - Remove → campaign machinery (crowdfunding/P2P) or a commerce checkout; the "always-on give front door" is what makes it a donation capability rather than a campaign or a product sale.
2. **The gift as the transaction of record.** Every capture event is recorded as a charitable **gift** made by an identified (or explicitly anonymous) **donor**: an amount, a frequency (one-time or on a schedule), commonly a chosen designation, and a payment — held on the platform and settled to the organization's own money destination.
   - Remove → a generic payment processor or form builder moving money with no gift semantics, no donor attribution, no settlement-to-organization posture.
3. **The organization-side giving console.** The organization operates the give capability *through the platform*: it creates and configures capture surfaces (amounts, designations, branding, receipt behavior), and it manages the resulting gift stream — donation records, receipts/tax documentation, payouts/deposits, a light donor surface, and reporting.
   - Remove → an unmanaged embeddable payment widget (a "donate button" with no platform-held record or console) — the entry tier below the Type, not the platform itself.

Jointly-held load-bearing: 1+2 without 3 = a bare donate button / payment link; 1+3 without 2 = a form/page generator that never holds the gifts; 2+3 without 1 = a donor database or back-office settlement tool (Donor Management System territory), with no donor-facing give flow.

### L1 — Common Mature Structure (very common, not definitional)

- Donor records kept by the platform (light) with sync/export into CRMs and accounting (the dominant integration pattern).
- Receipts and tax documentation (immediate receipts; donor-accessible tax documents; year-end giving reports; regional regimes).
- Recurring giving plans: opt-in at checkout (often via upsell), donor self-service management, payment retries.
- Suggested/ask amounts and impact descriptions.
- Designations: org-defined funds/causes/designees the donor can choose.
- Donor-covers-fees option at checkout.
- Abandoned-gift recovery (contact capture + reminders).
- Org-side reporting/dashboards (by gift, donor, period, designation).
- Mobile-first donor experience; digital-wallet payments.
- Security, fraud protection, compliance posture; peak-load framing (giving days).

### L2 — Variant / Optional Structure

- **Money-flow model**: platform-processed (Fundraise Up, Bloomerang Fundraising, Givelify) vs bring-your-own processor (Raisely → org's own Stripe/PayPal). Both poles are market-real; the platform need not be the processor of record.
- **Capture-surface realization**: embedded snippet/form vs hosted page vs consumer giving app vs text-to-give vs in-person/QR/kiosk; white-labeling depth.
- **Donor-side discovery marketplace**: one sampled product makes finding organizations a donor-facing feature (Givelify); most products have no discovery layer (donors arrive from the org's own channels).
- **Regional/regulatory regimes**: US deductibility receipts, UK Gift Aid claims, CA/AU postures; multi-currency/multilingual breadth.
- **Non-cash gifts**: crypto, bank-transfer rails, donor-advised/noncash methods (depth varies).
- **Tribute/honor-memorial gifts; matched-giving windows; custom questions; address validation.**
- **Suite modules around the core**: peer-to-peer, events/ticketing, auctions, campaigns — packaged as adjacent product lines, not the donation core.
- **Business model**: %/flat fees, free-platform fee-optional postures (era-typical).

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Fundraise Up: Elements component library; Gift Cart; Reminder Element; AI ask-amounts/optimization claims ("3× more donors complete checkout", "30% higher gift size" — marketing figures); "80% of donors cover fees automatically" (pricing schema); 135+ currencies / 23 languages; UNICEF/Red Cross/Salvation Army case metrics.
- Bloomerang Fundraising: Qgiv→Bloomerang rebrand and "Giving Platform" packaging; Auctions module; GivingTuesday guide funnel; G2 badge wall.
- Givelify: "three-tap giving"; Givelithon (in-person giving event); Analytics Studio free positioning; "$1 billion given in 2023", "$3,960 a year per giver", "1,200 donations each hour" (marketing stats); "next business day" payout claim; 80,000+ organizations / ~2M donors marketplace framing.
- Raisely: Velora suite membership (Aplos + Raisely + Keela); B-Corp/ethical-screen positioning; "3-step" form framing; region-specific country pages; ABN footer detail.

### Rejected findings (not promoted)

- **Rejected: "online donation platform = payment processing for nonprofits."** Raisely evidences the opposite pole (org's own Stripe/PayPal holds the money); what all four hold is the gift capture/record/console layer. Consistent with the donor-management pass ("money-movement mechanics are not the Type's center") and the church pass ("a processor moves money but holds no giver credit, funds, or statements").
- **Rejected: "donor management is part of the definition."** Every sampled product ships *some* donor surface, but it is a light capture-side record feeding outward (integrations to real DMS/CRMs); the constituency-database center belongs to donor-management-system. Givelify's "Donor management" solution and Bloomerang's CRM line are suite modules.
- **Rejected: "recurring giving is definitional."** Near-universal in mature products but a one-time-only capture platform would still be recognizable; recurring is the strongest L1 item, not L0.
- **Rejected: "designation/funds is definitional."** Common (FU explicit; Givelify causes) but not universal in the sample (not explicit on Qgiv/Raisely fetched pages); L1.
- **Rejected: "campaigns are part of the donation core."** Campaign/P2P machinery appears as *modules* across the sample; the standing evergreen give capability is the center. Matches the crowdfunding pass's removal tests.
- **Rejected: precise operational claims** (fee percentages, payout schedules, receipt timing, currency counts) — observed only as single-product marketing figures; kept L3, not asserted in the final document.

## Boundary Findings

1. **vs Donor Management System (§25, processed — DISCHARGES its joint-review flag 1).** Seam confirmed from this side: the donation platform's center is the **donor-facing collection flow** (give surface → gift of record → settlement → receipt); the DMS's center is the **org-side constituency database** (constituent → history → cultivation). Donation platforms keep a *light* donor record and hand gifts outward (FU native integrations; Raisely sync; Givelify QuickBooks/ChMS handoff); donor-management products ship donation forms *writing back* (donor pass). Both directions embed a slice of the other; the system-of-record side and the primary user separate them. **Verdict: keep both Types.**
2. **vs Nonprofit Crowdfunding Platform (§25, processed — DISCHARGES its forward flag).** Removal tests re-run from this side: strip campaigns + crowd machinery from any sampled product → a standing donation platform remains (FU with P2P module removed is still fully itself; Raisely's donation form pole); strip the standing transaction capability → crowdfunding remains (campaign-only platforms per the sibling pass). Center: transaction-of-record (gift) vs campaign-of-record (public container). Most crowdfunding platforms ship standing donation forms (suite overlap, per sibling evidence); most donation platforms ship campaign/P2P modules (this pass's evidence). **Verdict: keep both Types; family-grid discriminators stand.**
3. **vs Church Giving Platform (§25, processed — DISCHARGES its joint-review flag).** Shared skeleton confirmed from this side (gift records, designations/causes, recurring, receipts/reports, donor-covered fees family-wide). Givelify re-confirms the bridge: one product, two marketed use cases ("Church & Nonprofit"), ChMS/QuickBooks reconciliation, platform-sent donor reports. The church Type's distinct object layer (member-database-linked giver attribution, congregational funds vocabulary, year-end statements as a first-class deliverable, ChMS-integration fabric) stands as recorded by that pass. **Verdict: keep two Types — the congregational specialization (church-giving-platform) vs the generic Type (this leaf); church giving is the vertical-specialization pole, not an alias.**
4. **vs Fundraising Management Platform (§25, UNPROCESSED — flag stands).** Adopting the donor-pass discriminators: this Type is the donor-facing standing give capability (transaction center); fundraising management is org-side program machinery (campaigns, appeals, events, performance) across the fundraising program. Suite vendors package both (Bloomerang Fundraising: Donation Forms vs Data/Reports; Raisely: Online Giving vs Supporter Management/Appeals). Joint review when that leaf is processed.
5. **vs Peer-to-peer Fundraising Platform (§25, UNPROCESSED — flag stands).** Here the *organization* runs the give capability and donors give to it; supporter-run pages appear only as optional modules that roll up to the org (FU P2P feature; Raisely P2P/DIY). Page-owner = supporter vs organization. Joint review when that leaf is processed.
6. **vs Payment Gateway / Checkout Platform (§08/§05).** Generic money movement knows nothing of gift semantics (designation, tribute, recurring giving plans, cover-the-fees, receipts/tax documents) or of the org-operated giving console with settlement-to-organization reporting. White-label (FU) shows the donor experience may look like the org's site while the platform still holds the gift layer. Distinct Types.
7. **vs Nonprofit CRM / Nonprofit Management Platform (§25, processed).** The umbrella-suite pass itself located "donor-facing capture" in the online-donation/crowdfunding family; nonprofit-crm's forward note adopted the donor-pass discriminators. Donation capture is the donor-facing module feeding the relationship spine. Held.
8. **vs Event Registration / Ticketing (§26, sibling family).** Registration sells attendance (purchase semantics; capacity/seating); donation platforms record gifts. Ticketed events appear as suite modules (Raisely Ticketed Events; Bloomerang Event Management) and donation upsells at registration are a bridge feature, not fusion.
9. **vs Membership Billing / Membership Management (§25).** Dues are owed by right of membership (receivable, renewal obligation); gifts are voluntary with no receivable semantics — adopted from the church and donor passes. Held.
10. **vs Personal/consumer crowdfunding (no leaf).** Beneficiary (organization-for-cause vs individual) + money destination (org account vs personal) + gift-with-charitable-receipt semantics — adopted from the crowdfunding pass. When consumer platforms serve nonprofits, they cross into this family.
11. **Channel variants are not separate Types.** Text-to-give (Bloomerang), in-person/app giving (Givelify Givelithon), kiosk/QR — all are surfaces of the same standing give capability.

## §24 Historical / Market-Sample Check

- **Analog donation-mail routine (paper era)**: a charity's letterhead donation coupon/reply envelope, always available with every appeal (standing give capability); gifts logged by the treasurer in the gift ledger with donor name, amount, date, purpose, and receipt issued from the receipt book (gift of record + attribution); the treasurer's desk with ledger, receipt book, and bank deposit slip (the org-side console). Satisfies all three L0 legs at analog level. ✓
- **Church offering-envelope system** (the church pass's own analog): standing giving channels + attributed gift records + receipts/statements — same function in the congregational specialization. ✓
- **First-generation "Donate button" era (early-2000s web)**: a payment processor's donate button + email receipt + manual spreadsheet. Satisfies legs 1–2 in a thin form and leaves leg 3 to manual tools — the entry tier below the platform Type. Mature products folded the console into the platform; the definition keeps the console because the recognizable *platform* product shape always carries it, while bare buttons remain processors. The definition names no specific implementation (no snippet, no app, no Stripe, no AI). ✓
- Era-bound machinery correctly excluded from L0: AI ask amounts, wallet payments, abandoned-gift recovery, crypto, discovery marketplaces, fee-optional business models, GivingTuesday framing.

## Uncertainties

1. **Reachable sample is Tier-2 only** (product pages). Help-center-level operational detail was unreachable for all four products (Donorbox/GiveWP/Givebutter/Classy blocked across two passes; help.qgiv.com and support.fundraiseup.com transport errors). Precise operational facts (fee levels, payout cycles, receipt timing, plan limits) are therefore **not asserted** anywhere in this pass; the final document deliberately avoids them.
2. **Cover-the-fees** is explicitly evidenced in one sampled product (FU) plus family-wide cross-pass support (church-giving pass listed donor-covered fees as shared skeleton). Held at "common" with moderate wording, not definitional.
3. **Designation depth** varies (FU codes gifts; Givelify raises for causes; Qgiv/Raisely implied via CRM/campaign coding); the object model of designation↔fund↔account reconciliation was not directly documentable and is kept conceptual.
4. **Givelify's record model** (funds, statements structure) is product-page level only (its help center was not fetched in either the church pass or this pass); claims about it kept coarse.
5. **UK Gift Aid** posture rests on FU case-study framing, not help docs; regional regimes kept at variant level with light wording.
6. **Recurring-plan object model** (schedule, retries, dunning, migration) observed as capability language, not mechanics; no precise claims.
7. The free/fee-optional pole (Givebutter/Donorbox class) and the self-hosted-WordPress pole (GiveWP) are **absent from the direct sample**; statements about them are absent from the final document rather than inferred from memory.

## Final Synthesis

An **Online Donation Platform** is the donor-facing, standing give-capability of charitable giving: the organization operates, through the platform, an always-on capture surface (form, page, snippet, app) on which anyone can make a charitable gift — an amount, one-time or scheduled, optionally designated to a cause — the platform records each gift as an attributable transaction of record settled to the organization, issues the receipt/tax documentation, and gives the organization a console over the whole stream (gift records, receipts, payouts, light donor records, reporting) with handoffs to CRM and accounting. The defining core is small (standing give capability + gift of record + org-side console) and survives the historical check: the paper-era donation coupon + treasurer's ledger satisfies it. Everything else — recurring plans, cover-the-fees, designations, tributes, abandoned-gift recovery, wallets, crypto, discovery marketplaces, campaign/P2P modules, AI optimization — is mature common structure or variant. The Type's center is the transaction; its siblings own the campaign (crowdfunding), the supporter-run page (P2P), the program machinery (fundraising management), the constituency database (donor management), and the congregational specialization (church giving).
