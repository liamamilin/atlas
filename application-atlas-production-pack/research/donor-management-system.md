# Research Notes — Donor Management System

Research date: **2026-09-07**

## Research Goal

Understand what a Donor Management System actually is as an Application Type: what objects exist inside it, who uses it, how work flows through it, which rules shape behavior, and where its boundaries lie against neighboring nonprofit/philanthropy Types (Online Donation Platform, Fundraising Management Platform, Nonprofit CRM, Church Giving Platform, Beneficiary Management, University Advancement Platform, Membership Management, Nonprofit Fund Accounting, commercial CRM).

## Initial Boundary Hypothesis

- Core use: nonprofit organizations record donors and their gifts, and manage ongoing relationships (stewardship, cultivation, communication) with the people and organizations that support or might support them.
- Primary users: development / advancement / fundraising staff; database administrators; executive directors; volunteers in small organizations.
- Nearest neighbors: donation collection platforms (donor-facing), fundraising campaign platforms (event/campaign machinery), nonprofit CRMs (broader constituent base), church giving platforms (congregational variant), beneficiary management (money-in vs services-out).
- Main unknowns at start: how gifts vs pledges vs recurring giving are modeled; how acknowledgment/receipting works; how households/relationships/soft credits are modeled; how segmentation and communications attach to the record; whether payment processing is owned or delegated.

## Research Questions

1. What is the central record? What does it hold? Who/what can it represent (individuals, organizations, households, foundations)?
2. What is a gift record? What types exist (one-time, pledge, recurring, in-kind, stock, matching, tribute, grant)? What coding structures attach to it (campaign / fund / appeal / event)?
3. How does the acknowledgment cycle work (receipts, thank-you letters, year-end statements)? How is acknowledgment state tracked?
4. How is credit modeled beyond the payer (soft credits, household giving, spouse/partner, donor-advised funds, memorials/honoraries)?
5. How does segmentation work (queries, saved searches, lists, smart groups) and how do communications flow from it (mail merge, email, letters)?
6. What relationship-cultivation machinery exists (activity tracking, contact reports, tasks, goals, lifecycles)?
7. What reporting is standard (giving history, campaign progress, constituent vs fundraising views, retention signals)?
8. Where do online donation forms and payment processing sit (owned vs integrated vs delegated)?
9. What data-hygiene machinery exists (duplicate detection, merge/unmerge, deceased handling, address updates)?
10. How do the neighbors differ, and what single removal turns this Type into another?

## Representative Products

Selection rationale: market coverage across customer tiers and product philosophies; documentation completeness; deliberately different origins (SMB SaaS, mid-market heritage vendor, platform-suite vendor, market-leading enterprise product, open-source suite).

| Product | Vendor | Tier / philosophy | Evidence level |
|---|---|---|---|
| Little Green Light (LGL) | Little Green Light LLC | SMB/mid-market, donor-management-first SaaS, US-market, transparent pricing | **A — direct** (official knowledge base: KB home, Fundraising category, Gift entry article, Acknowledgments category, Constituents category) |
| CiviCRM | CiviCRM LLC / community | Open-source constituent relationship suite; donor management (CiviContribute) is one component of a broader CRM | **A — direct** (official user guide: contributions chapter incl. key concepts, soft credits, receipts/thank-you letters; relationships chapter) |
| Bloomerang | Bloomerang | Mid-market "Giving Platform" (CRM + Fundraising + Volunteer); donor-retention-centric positioning | **B — positioning** (official root site + Bloomerang CRM product page; help center unreachable) |
| DonorPerfect | SofterWare | Long-heritage (40+ years) mid-market fundraising system with donor CRM center | **B — positioning** (official product page + FAQ; knowledge base is a Salesforce community, not fetched) |
| Raiser's Edge NXT | Blackbaud | Enterprise market leader; the historical category standard | **anchor only** — all documentation attempts failed (see Sources); no operational claims made |

Attempted and abandoned: Neon One (neonone.com 403); Blackbaud docs (docs.blackbaud.com JS shell; webfiles.blackbaud.com 404; kb.blackbaud.com JS shell; blackbaud.com/products 404). Per network rules these were dropped after repeated failures; Raiser's Edge NXT is retained as a market anchor with product-page-level evidence only.

## Sources

- Little Green Light — root site: https://www.littlegreenlight.com/ ; Knowledge Base home: https://help.littlegreenlight.com/ ; Constituents category: https://help.littlegreenlight.com/category/64-constituents ; Fundraising (Gifts & Pledges) category: https://help.littlegreenlight.com/category/96-fundraising-gifts-pledges ; Gift entry article: https://help.littlegreenlight.com/article/99-gift-entry ; Acknowledgments category: https://help.littlegreenlight.com/category/262-acknowledgments
- CiviCRM — User guide home: https://docs.civicrm.org/user/en/latest/ ; Key concepts and configurations: https://docs.civicrm.org/user/en/latest/contributions/key-concepts-and-configurations/ ; Soft credits: https://docs.civicrm.org/user/en/latest/contributions/soft-credits/ ; Manual receipts and thank-you letters: https://docs.civicrm.org/user/en/latest/contributions/manual-receipts-and-thank-yous/ ; Relationships: https://docs.civicrm.org/user/en/latest/organising-your-data/relationships/
- Bloomerang — root: https://www.bloomerang.co/ ; CRM product page: https://bloomerang.com/crm
- DonorPerfect — product page + FAQ: https://www.donorperfect.com/fundraising-software/
- Blackbaud — https://docs.blackbaud.com/ , https://kb.blackbaud.com/ , https://webfiles.blackbaud.com/ , https://www.blackbaud.com/products/raiser-edge-nxt (all failed; anchor only)

Related processed Atlas leaves consulted for boundary consistency: church-giving-platform (Boundary Findings + Related Types), beneficiary-management, alumni-management/university-advancement flags, constituent-relationship-management flag.

---

## Product Observations

### Little Green Light (evidence layer A — official help center)

**Constituents** (KB category "Constituents — Households, relationships, merging, deceased constituents, duplicates, memberships"; article titles):

- Constituent record is the central object: overview; what information can be stored; adding; deleting; importing; name information; **giving summary**; **constituent activity**; constituent categories; merging and **unmerging** records; **households**; relationships between constituents; relationships between employees and organizations; **managing data for deceased constituents**; bulk editing; **tracking memberships**; school-specific data; **options for recording anonymous donations**.
- Pricing model based on number of constituent records (tiers by record count) — the constituent population is the product's unit of scale (marketing fact; noted only).

**Fundraising (Gifts & Pledges)** (KB category + Gift entry article):

- Gift entry flow: **select constituent** (search or auto from Constituent Details page) → **amount** (the only required field) → optional **deposited amount** (separable from gift amount, e.g. when a transaction fee was subtracted) → **gift type** — a *fixed* set: **Gift, Other Income, Pledge, In Kind** ("Other Income" explicitly for non-tax-deductible income) → **gift category** (customizable list) → **payment type** (customizable: check, cash, credit card, stock…) → **gift date + deposit date** (gift date = date the donation was made; deposit date = date processed; defaults documented) → **campaign, fund, appeal, and/or event coding** (each assignable per gift; account-level defaults configurable) → **acknowledgment template** assignment at entry → optional **related gifts** (soft credits, matching gifts) → **related tasks** → optional team-member **email notification** on entry.
- **In-kind gifts**: separate gift type; no payment type or deposit date; optional **tax-deductible amount** (with cautionary guidance: only with verified third-party appraisal or documented fair market value); optional **quantity** (documented in pounds) that can merge into year-end tax letters via merge fields.
- **Bulk gift entry** (multiple constituents at once); bulk gift editing; **cloning** gifts (for repeated same-amount gifts; preserves everything except acknowledgment template); "use values for next gift" / "use same constituent for next gift" data-entry accelerators.
- **Split gifts** (dedicated article).
- **Pledge entry** (dedicated article; pledges are a gift type with installments — "gift, pledge, and goal details" review article).
- **Fundraising goals** for major gifts or grants (goal objects tracked against).
- **Matching gifts** (dedicated article); **soft credits** (dedicated article: "Gifts given by a spouse/partner, Donor Advised Funds, Family Foundations").
- **Tributes** (own KB category: record, acknowledge, import tributes, accept via LGL form).
- **Gift batches** (dedicated article).
- **Stewards** ("Working with stewards" article).
- Gifts of **securities (stocks)** entry article.
- **QCD recording** (qualified charitable distribution from an IRA owner) — product-specific guidance: gift attributed to the donor not the custodian; set deductible amount to $0; special acknowledgment (research notes only — regional US tax concept).
- **Import** of gifts and constituents (Flex Importer; data dictionary).

**Acknowledgments** (KB category):

- Print and **email acknowledgment** templates; templates assigned to gifts at entry; **generate and send** acknowledgment letters; final step: **mark mailing "Sent"**; **"Unacknowledged Gifts" dashboard alert**; acknowledgment preferences/settings; **receipt numbers for Canadian customers**; FAQ; merge fields; **tribute gifts** acknowledgment; **split gifts** acknowledgment.

**Year-End Tax Receipts/Annual Statements** — own KB category (mail or email).

**Searches, lists, reports, mailings, email:**

- Constituent Searches & Lists: basic/complex searches, **saved searches**, **building lists**.
- Reports: building and customizing, **scheduling**, **constituent vs. fundraising** reports, smart fields.
- Mailings: **mail-merge letters, envelopes, labels** for reminders/solicitations.
- Emailing directly from LGL (own category).
- LGL Forms: **donation forms** with payments (Stripe/PayPal integrations shown), event registration forms, volunteer-hour forms; data flows into LGL.

**Activity** (KB category): **tasks, contact reports, volunteering, notes, and documents**.

**Integrations**: Mailchimp, Constant Contact, PayPal, QuickBooks, Zapier (and others). US-market focus (explicitly not offered to EU/UK organizations).

### CiviCRM (evidence layer A — official user guide)

**Contacts & relationships** (Organising your data):

- Contact types: individuals, organizations, **households** (household as its own contact type with members linked by relationship; "Head of Household" vs "Household Member of" documented with cautions).
- **Relationships**: typed, **bidirectional** (Label A→B and B→A, e.g. "Grandparent of"/"Grandchild of"), with **start/end dates**, description, notes, **permissions** (view/update of the related contact via relationship), enabled flag; custom relationship types creatable; custom fields attachable to relationships; **employee↔employer** relationship auto-created from the Current Employer field (with dedupe checks before creating a new organization contact).

**Constituency organization**: groups and tags; **smart groups** (saved-query-driven membership); activities; custom fields; **deduping and merging** (dedup rules exist per contact type; unsupervised vs supervised rules); profiles; undelete.

**CiviContribute (contributions = gifts):**

- Each contribution must be assigned a **financial type** (defaults: donation, member dues, event fee, campaign contribution; user-definable — e.g. one per appeal). Financial types link to **financial accounts** based on the organization's chart of accounts; saving a contribution records the appropriate **double-entry debits/credits** for export to accounting software (accounting codes per account). (This depth is a CiviCRM design choice — see vendor-specific.)
- **Payment processors** configured to connect online payments; **payment methods** (credit card, cash, check, debit card, EFT defaults, editable); accepted credit cards.
- **Contribution statuses**: Completed; **Pending (Pay Later)** (entered, payment not received, e.g. paper/electronic check); **Pending (Incomplete)** (sent to processor, response unresolved); **Failed**; plus In Progress / Overdue / Partially Paid used by partial-payment and recurring features. Status labels editable; adding new statuses discouraged (interferes with accounting validation).
- **Contribution pages** (online fundraising pages on the website) and contribution forms; **personal campaign pages** (supporter-led pages, donations soft-credited to the page owner); premiums (gift incentives); widgets.
- **Manual entry** of contributions; **offline fundraising**; **finding and viewing contributions** (Find Contributions search); **importing** contributions.

**Receipts & thank-you letters** (dedicated guide section):

- Online contributions: **automatic email receipt** when configured; manual send/re-send by editing the contribution (**"Send Receipt?"** tick) or batch: select contributions from search → **Receipts — print or email** → email or PDF; **receipt dates are recorded/updated** on the contribution by default; "Do not email/Do not mail" contact preferences honored (with an override option).
- **Thank-you letters**: run from contribution search results; choose to **update thank-you dates and/or receipt dates**; print/email options (PDFs only; emails where possible + PDFs for non-emailable; emails + PDFs for all); **group contributions by contact** (one letter covering multiple gifts — used for **end-of-fiscal-year giving statements/tax receipts**; aggregate amount token available via Smarty); letter templates with **tokens/mail merge**; a "Print/Merge Document" **activity is created for each letter** (letters leave a trace on the activity record).

**Soft credits** (dedicated guide section):

- Assign credit for a donation to people who are **not the donor**; **soft credit types** (reserved: In Honor of, In Memory of, Solicited, Personal Campaign Page, Gift; custom types e.g. Donor Advised Funds, scholarships, family bequests); **partial crediting** (a single $1,500 contribution split as three $500 soft credits to different people); credit **without double counting** (the donor is credited; the solicitor/honoree carry soft credits); **honoree profiles** created via contribution pages with dedupe checks; reporting columns for soft credits.

**Pledges** (CiviPledge): pledge campaigns with scheduled payments, reminders, reports.

**Reporting**: CiviReport; contribution detail reports with soft-credit columns; **accounting integration** (export of financial transactions).

**Scope note for boundaries**: CiviCRM ships events (CiviEvent), membership (CiviMember), campaigns, grant management, case management (CiviCase), surveys/petitions — i.e., a full constituent suite in which donor management is one component. This matters for the Nonprofit CRM boundary.

### Bloomerang (evidence layer B — official product pages; help center unreachable)

- Positioning: "Giving Platform" combining **Fundraising**, **CRM** (donor management), and **Volunteer** management; "built by fundraisers, for fundraisers"; nonprofit customers from local organizations to national names.
- Bloomerang CRM (product page): **360-degree constituent profile** ("one profile"); **constituent timeline** ("every donation, interaction, and engagement in one timeline"); **giving insights** ("who's loyal — and ready to give"; blends activity and giving potential; retention/major-gift signal framing); **dynamic donor groups** (automatic segmentation feeding tailored messages); **automated donor outreach** (journeys "from first gift to lasting loyalty"); **AI-powered email campaigns** with templates; dashboards (giving trends, campaign results, donor growth); data hygiene (duplicate prevention; **nightly NCOA address updates** — vendor-specific detail).
- Payments: platform supports cards, ACH, PayPal, Apple/Google Pay, Venmo, Tap to Pay (product-page FAQ).
- FAQ self-definition: "A nonprofit CRM is software that centralizes donor and constituent data and interactions to guide fundraising, communications, and engagement."

### DonorPerfect (evidence layer B — official product page + FAQ; Salesforce-hosted knowledge base not fetched)

- "Unified donor database: track giving history, donor outreach, and engagement results in one place"; **"Custom nonprofit CRM" — tailor fields, screens, reports, and daily workflows**; **relationship tracking** ("connections between donors, families, organizations, volunteers, and advocates"); **role-based permissions** ("protect sensitive donor data, and train volunteers").
- **Automation**: automatic **receipts and thank-yous** after every gift; **monthly giving programs** with automatic processing; triggered emails/alerts based on donor activity; **assign donor outreach and track deadlines across your team**; automated donor journeys from gift and behavior data.
- **Data management**: duplicate detection; **automatic address updates**; global updates; **credit card updater** (prevents failed recurring donations).
- **Online**: conversion-optimized **donation forms synced with the data**; integrated payment gateway; mobile and text giving; crowdfunding; events and ticketing; email and direct-mail campaigns; **grants and pledges**; monthly giving.
- **Insights**: identify high-value donors; **segment by behavior, giving history, engagement**; personalize across email/direct mail; **track donor lifecycle progress "from first impressions to major gifts"**; retention and lifetime-value framing; AI coaching assistant ("Tivy" — vendor-specific).
- **Integrations**: QuickBooks (accounting), Constant Contact (email; bundled), DonorSearch (prospect research), matching-gifts database; volunteer management module; mobile app.
- **FAQ (market self-definition — important boundary evidence)**: "A nonprofit CRM focuses on managing donor relationships and supporter data, while fundraising software helps organizations run campaigns, process donations, and track fundraising performance. Many modern platforms, including DonorPerfect, combine both capabilities into one system."
- 40+ years heritage claim; scale claim (hundreds to hundreds of thousands of donors).

### Raiser's Edge NXT (anchor only — no operational claims)

- Retained as the enterprise market anchor and the historical reference point for the category (desktop-era Raiser's Edge → cloud NXT). Documentation unreachable in this pass; nothing asserted about its internals.

---

## Cross-product Comparison

| Dimension | LGL | CiviCRM | Bloomerang | DonorPerfect |
|---|---|---|---|---|
| Central record | Constituent (person/org) with giving summary + activity | Contact (individual / organization / household) | 360° constituent profile + timeline | Donor record, customizable screens |
| Gift record | Gift entry: amount required; type (Gift / Other Income / Pledge / In Kind); category; payment type; gift date + deposit date | Contribution: amount; financial type; status (Completed / Pending (Pay Later) / Pending (Incomplete) / Failed / …) | Donations on timeline (detail at help-center level not observed) | Gifts incl. grants and pledges; receipts/thank-yous automated |
| Coding structures | Campaign / fund / appeal / event per gift; account-level defaults | Financial type per contribution; campaign objects; (fund/appeal via financial types or custom data) | Campaign results on dashboards | Campaigns across giving channels |
| Acknowledgment | Template assigned at entry; print + email; "mark Sent"; unacknowledged-gifts alert; year-end statements category | Auto receipt; batch print/email receipts; receipt dates recorded; thank-you letters with grouping = year-end statements; activity logged per letter | (positioning: engagement/stewardship) | Automatic receipts and thank-yous after every gift |
| Soft credit / attribution beyond payer | Related gifts: soft credits, matching gifts; split gifts; anonymous options; tribute gifts | Soft credit types (In Honor/Memory, Solicited, PCP); partial crediting; honoree profiles; no double counting | (not observed at this evidence level) | Matching-gifts integration; relationship tracking |
| Segmentation | Searches, saved searches, lists | Smart groups (saved queries) + SearchKit | Dynamic donor groups | Segment by behavior/giving/engagement |
| Communications | Mail merge letters/envelopes/labels; email from product | CiviMail, SMS, postal mail, tokens/mail merge | Automated outreach journeys; AI email campaigns | Email (Constant Contact), direct mail |
| Cultivation machinery | Contact reports, tasks, notes, documents; fundraising goals for major gifts/grants; stewards | Activities; case management (suite); campaigns | Giving insights (loyalty/ready-to-give); engagement signals | Outreach assignments + deadlines; donor lifecycle tracking |
| Relationships/households | Households; relationships; employee–organization; deceased handling; merge/unmerge | Typed bidirectional relationships with dates/permissions; households as contact type | Timeline of interactions | Relationship tracking (families, organizations) |
| Reporting | Constituent vs fundraising reports; scheduled | CiviReport; contribution reports; soft-credit columns | Dashboards: giving trends, campaign results, donor growth | Custom nonprofit reporting/analytics |
| Data hygiene | Merge/unmerge; duplicates category; import | Dedup rules; deduping & merging | Duplicate prevention; NCOA address updates | Duplicate detection; address updater; card updater; global updates |
| Online giving | LGL Forms (donation/event/volunteer forms) with payment processing | Contribution pages + payment processors + personal campaign pages | Fundraising product incl. donation forms | Integrated donation forms + gateway; text/mobile; crowdfunding |
| Money ownership | Payment processing via integrations (Stripe/PayPal); deposit amount field | Payment processors configured by org | Platform accepts payments (rails listed) | Integrated payment gateway (vendor services) |
| Integration | QuickBooks, Mailchimp, Constant Contact, Zapier | Accounting export via financial accounts | (suite-internal) | QuickBooks, Constant Contact, DonorSearch, matching gifts |
| Permissions | Team members; notifications | Role-based permissions (incl. financial-type permissions) | (enterprise tier implied) | Role-based permissions explicit |
| Scope posture | Donor management first; forms/events/volunteering as adjacent features | Full constituent suite (events/membership/case/grants) with contributions as one component | Platform: CRM + Fundraising + Volunteer | Fundraising system with donor-CRM center + events/volunteers/marketing modules |

Stable commonalities across all sampled products (B-level): constituent/record as center; gift attributed to the record; cumulative giving history on the record; coding of gifts; acknowledgment/receipt machinery; segmentation of the constituency; communications generated from the database; relationship/household modeling; cultivation activity on the record; reporting on both money and people; duplicate/data hygiene; import/export; integration outward (accounting, email marketing).

## Canonical Model (working)

```text
Constituent (standing record: person / organization / household;
             includes prospects who have not yet given)
└── Gift (recorded contribution attributed to the constituent:
        amount · date · method · coding)
    └── Cumulative giving history (rolls up onto the constituent)
└── Relationship activity (interactions, notes, tasks, acknowledgments,
    communications — recorded on and driven from the record)
└── Segment (selection over the constituency for outreach and reporting)
```

## Abstraction Hierarchy

### L0 — Defining Invariant (candidate)

1. **Constituent record** — a standing, identified record for a person or organization the organization relates to philanthropically; it exists before and after any single gift and covers **prospects and non-donors as well as donors** (this is what makes it a *management* system rather than a payment record).
2. **Gift record attributed to a constituent** — a recorded contribution (at minimum amount + date; method/type) credited to a specific constituent record.
3. **Cumulative giving history** — the gift stream accumulates on the constituent as a queryable history (giving summary / timeline).
4. **Recorded relationship work** — interactions with the constituent (acknowledgments, notes, contact reports, tasks, communications) are recorded on and driven from the record; the system actively supports outreach to selected constituents (segmentation feeding communication).

Remove (1) → you have a payment/ledger system. Remove (2)–(3) → you have a generic contact manager / CRM shell without the philanthropic money record. Remove (4) → you have a donation platform with giver credit (the church-giving pass explicitly calls that surface *not* donor management: "the giving platform's donor surface is limited to giving history, payment methods, and statements"). All four together are the minimal recognizable core.

Historical check: a paper donor card file + gift ledger + typed acknowledgment letters + sorted mailing lists satisfies all four (records, attribution, history, cultivation work) — the core survives without cloud, automation, or even software-era segmentation tooling. Desktop-era donor databases (Raiser's Edge heritage, DonorPerfect's 40-year lineage) satisfy it trivially. The L0 is era-neutral.

### L1 — Common Mature Structure

- **Acknowledgment machinery** — per-gift receipts, thank-you letters (print + email), templates with merge fields, acknowledgment state tracked per gift (unacknowledged alerts; "mark sent"), **year-end statements/tax receipts** (grouped, date-ranged, conservative content).
- **Coding structures** — gifts coded to campaign / fund / appeal / event (or financial-type equivalents); account-level defaults; coding is the backbone of reporting.
- **Segmentation & selection** — searches, saved searches/smart groups, list building; the population is worked in groups, not just one-by-one.
- **Communications from the database** — mail-merge letters, envelopes/labels, email to segments; opt-out/contact-preference handling (CiviCRM "Do not email/Do not mail").
- **Households & relationships** — household records, typed relationships between people and organizations, employee–employer links.
- **Gift-type breadth** — pledges (with installments), recurring/monthly giving, in-kind, securities/stock, matching gifts, tribute/memorial gifts, grants.
- **Soft credits & credit splitting** — crediting non-payers (spouse/partner, DAF, solicitor, honoree) without double counting; split gifts.
- **Anonymous-gift handling** — recording gifts without public attribution.
- **Deceased-constituent handling** — a distinct lifecycle discipline in the record.
- **Duplicate discipline** — dedupe rules, merge/unmerge; data hygiene (address updates, card updaters).
- **Import/export** — bulk data migration is a first-class workflow (constituents and gifts).
- **Reporting** — constituent-level and fundraising-level reports; campaign progress; giving trends; retention/lifecycle signals (wording varies by product).
- **Dashboards** — role surfaces for giving trends, campaign results, unacknowledged-gift alerts.
- **Online donation forms** — forms that write gifts back into the database (owned or integrated).
- **Integration spine** — accounting (QuickBooks-class), email marketing (Mailchimp/Constant Contact-class), payment processors, prospect research, matching-gift databases.
- **Role-based permissions** — sensitivity of donor financial data; restricted entry roles.
- **Tasks/reminders** — cultivation next-steps attached to constituents and gifts.

### L2 — Variant / Optional Structure

- **Payment processing posture** — integrated native gateway vs processor integrations vs delegated processing; deposit-amount vs gift-amount separation.
- **Suite breadth** — standalone donor database vs platform suites adding volunteers, events, membership, marketing, AI (drift direction toward Nonprofit CRM at the far end).
- **Moves-management depth** — major-gift portfolios, goals, lifecycles, prospect research integration, wealth/ratings data (prospect-research integrations observed as integrations, not core).
- **Deployment & business model** — cloud SaaS by constituent tier; open-source self-hosted; desktop heritage; pricing by record count vs seats vs modules.
- **Regional variants** — receipting rules (Canadian receipt numbers; US deductibility/QCD; EU/UK market availability differences — LGL explicitly does not serve EU/UK).
- **AI assistance** — drafting, coaching, insights (era-typical; several vendors).
- **Volunteer / membership / event data in the same record** — common but belongs to neighboring Types when it becomes the center.

### L3 — Vendor-specific (research notes only)

- LGL: fixed gift-type set (Gift / Other Income / Pledge / In Kind); gift categories vs types split; "Use values for next gift"; clone-gifts setting; in-kind quantity in pounds with `[[gifts.YEAR.in_kind_qty_total]]` merge fields; QCD guidance (deductible $0, custodian-as-delivery-mechanism); "unacknowledged gifts" dashboard alert; stewards article; constituent-count pricing tiers; EU/UK non-availability; Help Scout-based KB.
- CiviCRM: financial types ↔ financial accounts double-entry machinery (chart-of-accounts-linked, accounting-code export); contribution status vocabulary (Pending (Pay Later) / Pending (Incomplete) / Failed / In Progress / Overdue / Partially Paid); reserved soft-credit types (In Honor of, In Memory of, Solicited, Personal Campaign Page, Gift); Smarty tokens (`{$contribution_aggregate}`); Print/Merge activity per letter; Head-of-Household caution; CiviContribute/CiviMail/CiviEvent/CiviMember/CiviCase/CiviGrant component naming; optional-features statuses "not recommended to add".
- Bloomerang: nightly NCOA address updates; "generosity signals"; Giving Platform packaging (Fundraising $/CRM $/Volunteer $ split pricing — marketing numbers, not asserted in final doc); retention-first marketing stats (2.5x first-time donor retention etc. — marketing claims, not evidence).
- DonorPerfect: Constant Contact bundling; Tivy AI coach; "25% revenue growth in first year" marketing claim; 40-years heritage; 75,000-users claim; Salesforce-community knowledge base.
- Raiser's Edge NXT: nothing (unreachable).

## Vendor-specific vs Rejected Findings

- **Rejected: "donor management = online donation forms."** Forms are ubiquitous but two sampled products treat processing as integration rather than core, and the historical form is a reply envelope. Forms are L1.
- **Rejected: "donor management = payment processing."** DonorPerfect/Bloomerang integrate processing; LGL delegates to Stripe/PayPal; CiviCRM configures external processors. Money-movement mechanics are not the Type's center (consistent with the church-giving pass: "a processor moves money but holds no giver credit, funds, or statements").
- **Rejected: "nonprofit CRM = donor management."** CiviCRM self-labels a CRM yet contains donor management as one component (CiviContribute) alongside membership/events/case/grants. Bloomerang/DonorPerfect self-label CRM while centering donors. The label is used loosely in the market; the object base differs (see Boundary Findings).
- **Rejected: double-entry financial recording as definitional.** CiviCRM records debits/credits per contribution; LGL instead exposes a deposit-amount field and a lump-sum QuickBooks report; DonorPerfect hands off via integrations. The accounting bridge is common, the machinery is vendor-specific.
- **Rejected: precise acknowledgment timing/defaults** (e.g. "receipts within X days") — not evidenced; not asserted.

## Boundary Findings

1. **vs Online Donation Platform (§25 sibling, unprocessed).** Collection surface vs relationship system of record. A donation platform's center is the donor-facing giving flow (form → payment → receipt → gift record); a donor management system's center is the org-side constituency database (constituent → history → cultivation). Many donor-management products *include* forms, and many donation platforms *include* a light donor surface — the seam is which side is the system of record and who the primary user is. **Joint-review flag** (echoes the church-giving pass flag; recommend joint review when online-donation-platform is processed).
2. **vs Fundraising Management Platform (§25 sibling, unprocessed).** DonorPerfect's own FAQ separates "managing donor relationships and supporter data" (CRM) from "running campaigns, processing donations, tracking performance" (fundraising software) — market-internal evidence of the seam — while noting modern products combine both. Campaign machinery (events, peer-to-peer, crowdfunding, ticketing) vs constituency stewardship. **Joint-review flag.**
3. **vs Nonprofit CRM (§25 sibling, unprocessed).** Term collision: the market calls donor databases "nonprofit CRMs" (Bloomerang CRM, DonorPerfect "custom nonprofit CRM"), while a fuller Nonprofit CRM extends the constituent base to members, volunteers, clients, and program participants (CiviCRM's component breadth is the structural tell). Candidate outcomes: donor management as the donor-centered sibling of Nonprofit CRM (parallel to church-giving vs ChMS), or consolidation view. The constituent-relationship-management pass already flagged the nonprofit usage of "CRM" for this pass to claim. **Joint-review flag.**
4. **vs Church Giving Platform (§25, processed).** Boundary already drawn from that side and confirmed here: the giving platform's donor surface is "limited to giving history, payment methods, and statements"; donor management adds cultivation, segmentation, and communications across the constituency. A church *can* run a donor management product on top of its giving platform (or a ChMS with contributions can pair with one). Held.
5. **vs Beneficiary Management (§25, processed).** Mirror structures: registry of people + recorded transactions + activity + reporting. Seam = direction of value: money/service flowing **in from** constituents (donor) vs services flowing **out to** beneficiaries. The beneficiary pass itself framed donor software as the counterpart. Held.
6. **vs University Advancement Platform (§23, processed).** Advancement = donor management core + alumni/engagement layer + prospect/proposal machinery over the advancement constituency (alumni, parents, friends), often suite-packaged. A generic DMS core applies inside advancement; the alumni-management pass flagged the seam from its side. Held — advancement is the higher-ed-specialized superset, not a duplicate of this leaf.
7. **vs Membership Management System / AMS (§25).** Dues are owed by right of membership (invoiced, receivable, renewals-as-obligation); gifts are voluntary. Membership modules may live inside donor databases (LGL "tracking memberships" article exists) without changing the Type. Held (same argument the church pass used vs Membership Billing).
8. **vs Nonprofit Fund Accounting (§25).** Relationship/gift-intent records vs books. The bridge is a handoff (ledger codes, lump-sum reports, accounting exports). Fund accounting keeps double-entry ledgers with restricted funds; donor management records intent-level gifts. Held (consistent with fund-administration pass note that nonprofit-fund-accounting is GL-shaped).
9. **vs CRM (§07 commercial).** Commercial CRM centers on a revenue pipeline over accounts/deals owned by sellers; donor management centers on philanthropic support and stewardship over constituents, with gifts (not deals) as the money object and no sales-pipeline stage machinery as defining structure. Held (parallel to the constituent-relationship-management pass's service-vs-giving seam).
10. **vs Email Marketing Platform (§06).** Communications exist *in service of* the constituent record here; the mailing list is derived from segmentation, and the standard realization is integration (Mailchimp/Constant Contact) rather than the product being a mailing platform. Held.
11. **Removal tests.** Remove the constituency cultivation half (segments, communications, activity) → Online/Church Donation Platform. Remove the gift money record → generic CRM/constituent manager (Nonprofit CRM pole). Remove the org-side stance (donor becomes the primary user) → donor-facing giving platform. Remove double-entry books → you still have donor management (books belong to Fund Accounting). Remove campaign/event machinery → still donor management (that machinery belongs to Fundraising Management Platform).

## Uncertainties

- **Raiser's Edge NXT internals unverified.** The enterprise pole's operational model (prospect portfolios, moves management, gift batch workflows at enterprise depth) is not evidenced in this pass; the final document deliberately avoids enterprise-specific workflow claims.
- **Moves management as a named structure** was not directly observed in fetched documentation (only lifecycle/major-gift framing at positioning level: DonorPerfect "first impressions to major gifts", LGL "fundraising goals for major gifts or grants", Bloomerang "who's loyal and ready to give"). Treated as L2 with hedged wording, not as a named canonical structure.
- **Retention metric vocabularies** (industry terms like LYBUNT/SYBUNT) were not observed in fetched official docs; not asserted.
- **Nonprofit CRM and Fundraising Management Platform leaves are unprocessed**; boundary positions here are one-sided and flagged for joint review.
- **EU/international donor-management practice** is under-sampled (LGL US-only; CiviCRM international but donor-specific receipting rules not fetched in depth; DonorPerfect has Canada/Australia variants noted in nav). Regional receipting kept at variant level with light wording.
- **Bloomerang/DonorPerfect evidence is product-page level**; help-center-level operational detail for those two products is not behind the claims made here (claims kept to what the pages state or to cross-product B-level commonalities).

## Final Synthesis

A Donor Management System is the nonprofit's organization-side system of record for philanthropic support: a standing constituency of identified people and organizations (donors, prospects, households, organizations), the gifts attributed to them, and the relationship work — acknowledgment, communication, cultivation — conducted over that constituency and recorded on it. Its defining core is four-part and deliberately small (constituent record; attributed gift; cumulative giving history; recorded/driven relationship work including segmentation-fed outreach). Everything else the market associates with it — receipts and thank-you letters, year-end statements, coding structures, soft credits and tributes, households, recurring and pledge machinery, mail merge and email, online forms, dashboards, integrations, data hygiene — is standard capability of mature products rather than definition. The Type sits between collection platforms (which move and record money but do not manage relationships) and nonprofit suites (which widen the constituent base to members/volunteers/clients), and mirrors beneficiary management as the money-in counterpart of services-out.
