# Research Notes — Association Management System / AMS

## Research Goal

Understand what an Association Management System (AMS) actually is as an Application Type: its core objects, the membership lifecycle it manages, how dues/renewals work, what belongs to the Type vs what is bundled suite capability, and how it differs from adjacent Types (Membership Management System, Member Portal, CRM, Nonprofit CRM, Association Event Management).

## Initial Boundary

Initial hypothesis: an AMS is the staff-operated system of record for a membership organization — a registry of people/organizations, membership records with types/levels and time-bounded status, and a recurring dues/renewal cycle, with events/communications/community run off that registry.

Adjacent leaves in the same directory section (§25) that must be distinguished:

- Membership Management System (separate leaf — possible alias/segment split)
- Member Portal, Membership Billing, Member Benefits Management, Member Directory
- Chapter Management Platform, Committee / Board Management
- Association Event Management (flagged for joint review in STATUS.md)
- Member Community Platform, Association Job Board, Certification Management, Continuing Education Management
- Nonprofit CRM / Donor Management System (§25), CRM (§07), Church Management System (§25), HOA / Community Association Management (§17)

## Research Questions

1. What is the central object model — what is a "member" vs a "contact"?
2. How is a membership structured (types/levels, dues, terms)?
3. What is the membership lifecycle (application → approval → active → renewal → lapse)?
4. How does the renewal cycle work mechanically (notices, invoices, recurring payments, status transitions)?
5. What does the member do directly (self-service) vs what does staff do?
6. Which capabilities are defining vs bundled suite modules (events, community, learning, job boards, chapters, donations)?
7. Is there a structural difference between "AMS" and "Membership Management Software/System"?
8. How do organizational (company) memberships and chapters/AMCs fit?
9. What roles exist (staff, chapter admins, members, executives)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Tier / Philosophy | Why selected |
|---|---|---|---|
| Wild Apricot | Personify | SMB / self-serve all-in-one (clubs, small associations, chambers) | Market-leading small-org tool; feature pages rich |
| YourMembership | Momentive Software | Mid-market "all-in-one AMS" for small-staff associations | Long-established AMS; AMC audience |
| Glue Up | Glue Up | International cloud all-in-one (associations, chambers, nonprofits) | Explicit member-lifecycle description; chapter management; multi-currency |
| Fonteva | Fonteva | Enterprise, Salesforce-native AMS | Platform-native architecture philosophy; large associations/societies |

iMIS (Advanced Solutions International) — the classic enterprise AMS — was intended as a fifth sample but its documentation hosts were unreachable (see Sources / limitations). Enterprise-side evidence rests on Fonteva.

## Sources

Fetched 2026-09-06:

- Wild Apricot — https://www.wildapricot.com/features , https://www.wildapricot.com/features/membership-management-software (Tier 2, product/feature pages)
- YourMembership — https://www.yourmembership.com/ (Tier 2, product page)
- Glue Up — https://www.glueup.com/ , https://www.glueup.com/features/membership-management (Tier 2, product/feature pages incl. FAQ)
- Fonteva — https://fonteva.com/ , https://fonteva.com/membership-software/ (Tier 2, product/feature pages incl. FAQ)

Unreachable (recorded limitations):

- help.wildapricot.com / gethelp.wildapricot.com — JS-rendered SPA, returned no content (2 attempts)
- docs.imis.com — transport error; help.imis.com — transport error; www.imis.com — 403 (abandoned per network rules)
- support.yourmembership.com — transport error; help.yourmembership.com — transport error; features subpage — 403

Consequence: no Tier-1 operational help-center articles were reachable for any sampled product. All evidence below is Layer A (directly observed on official product pages) but marketing-tier; operational precision (exact status vocabularies, numeric limits, default grace periods) is deliberately not asserted. No model-memory filling of such details.

## Product Observations

### Wild Apricot (Personify) — SMB all-in-one

Key observations (Layer A, official feature pages):

- Positions as "all-in-one membership management software"; audiences: associations, nonprofits, chambers, clubs, charities, chapters.
- **Member database**: cloud member database; search/filter/update records in real time; track member activity and membership trends; import from spreadsheet; customizable fields.
- **Membership levels**: renewal policy can "limit self-renewals for specific members or membership levels" — implies levels as a first-class configuration.
- **Automated dues & renewals**: automatic renewal reminders and invoicing; recurring payments ("members never miss a payment and can remain in good standing"); "automatically update membership status depending on member activities during their renewal period"; configurable renewal policy and renewal notice timelines.
- **Member directory**: searchable, customizable; public record or members-only; self-updates by members.
- **Website builder with member-only spaces**: access to member-only pages configurable by member level or group; per-level landing pages after login.
- **Custom forms**: submissions stored directly in the member database.
- **Email & communications**: templates, automation/scheduling, open/click tracking per member.
- **CRM tools**: engagement history — renewals, event attendance, payments, communications — in one database; segment/filter for outreach.
- **Reporting**: real-time membership stats including renewals, **lapsed members**, retention rates; event registration/attendance/revenue; export to Excel/QuickBooks.
- **Mobile apps**: admin app (add contacts, **approve members**, track payments, check-ins) + member app (directories, event registration, profile management).
- **Payments**: online payment processing; invoices and receipts auto-generated. Online store module.
- Add-ons: registration tech, text messaging, community ("CommUnity"), job board.
- Pricing by contact tiers (database size), all plans include core feature set.

### YourMembership (Momentive Software) — mid-market AMS

Key observations (Layer A, official product page):

- Positions explicitly as "all-in-one **AMS**" for small to mid-size associations; audiences: nonprofits, **association management companies (AMCs)**, professional associations.
- Module set: member management ("the industry's best AMS for small to mid-sized organizations"), online community, job board, website design, learning management, event management, data analytics.
- Longevity claim: 25+ years serving member-based organizations; "25 million members interact with YourMembership".
- Customer testimonial (evidence of dues complexity as a core concern): "I have a complicated dues system so [YM] makes it so much simpler… The database is my lifeline."
- Member-centric marketing theme ("member experience", "member engagement and revenue", "non-dues revenue").

### Glue Up — international cloud all-in-one

Key observations (Layer A, official product/feature pages + FAQ):

- Modules: CRM, Memberships, Events, Email Campaigns, Community, Finance & Invoicing, CPD & CPE Credits, Tasks, Surveys, Website, Chapter Management, AI Copilot; member app ("My Glue") + staff "Manager" app.
- Explicit **member lifecycle** framing: "from first application to renewal, event participation, email engagement, payments, and reporting."
- **Centralized member database**: contact details, membership levels, engagement history, event activity, payment records, communication preferences in one online database.
- **Digital member applications**: online application forms; define membership types; collect payments; apply discounts; **route applications for review**; "move approved applicants into your member database automatically."
- **Renewal & dues tracking**: renewal reminders; dues collection; recurring payments; discounts; **membership status updates**; renewal activity reporting; **auto-billing** ("automatically charge the due amount from the member's card or send invoices when the due date is reached").
- **Member self-service**: members update profiles, renew memberships, pay invoices, register for events, access directories.
- **Membership directory**: multiple directories; organization controls what each shows; public or member-facing.
- **Members-only pages** gated by member levels or groups; digital membership cards; coupons; multiple currencies & tax support; trial memberships (short-term memberships with flexible pricing).
- **Chapter management**: multiple chapters in one system; granular permissions; consolidated membership data; automated chapter rebate payments (2026 update).
- Serves associations, chambers of commerce, nonprofits, conference organizers, corporations; FAQ describes itself as both "membership management software" and "association management software".

### Fonteva — enterprise, Salesforce-native AMS

Key observations (Layer A, official product/feature pages + FAQ):

- Positions as "Salesforce AMS" / association management software **built on the Salesforce CRM**; "Member CRM" is a named feature. FAQ: "Do I need to integrate a separate CRM? No… everything… lives on a single platform."
- Feature set: Member CRM; engagement scoring & badging; **customizable member join & renew workflows**; member directories & online community; event & conference management; form & questionnaire builder; native payments; reports & dashboards.
- **Self-service portal**: profile updates, purchases, activity; "join, renew, and manage memberships with fewer steps."
- **Unified data & analytics**: membership, engagement, transactions in one system; lifecycle analytics; role-based access to reporting.
- **Native payments**: cards, ACH, wallets, BNPL; multicurrency/multilingual; reconciliation with automated matching and exception handling.
- Flexible data model options; SaaS + Salesforce platform license; scalable without changing systems.
- Audiences: trade associations, professional societies, AMCs, customer user groups, membership organizations, fraternities & sororities.
- AI: Salesforce Einstein (renewal-risk prediction), Agentforce agents.

## Cross-product Comparison

| Structure / capability | Wild Apricot | YourMembership | Glue Up | Fonteva | Reading |
|---|---|---|---|---|---|
| Central member/contact database | ✓ | ✓ ("database is my lifeline") | ✓ | ✓ (Member CRM) | Universal |
| Membership types / levels with dues | ✓ (levels) | ✓ (complicated dues) | ✓ (unlimited types/levels) | ✓ (member types) | Universal |
| Join/application workflow | ✓ (admin approves) | implied | ✓ (form → review → auto-move to database) | ✓ (customizable join workflows) | Common |
| Dues invoicing & payment collection | ✓ | ✓ | ✓ (auto-billing) | ✓ (native payments) | Universal |
| Renewal automation (reminders, recurring, status updates) | ✓ | ✓ | ✓ | ✓ | Universal |
| Membership status lifecycle (active / renewal window / lapsed) | ✓ (lapsed members, auto status) | implied | ✓ (status changes) | ✓ (renewal risk) | Common (vocabularies unverified) |
| Member self-service portal | ✓ (member app + member pages) | ✓ (community/portal) | ✓ (My Glue) | ✓ (portal) | Universal |
| Member directory | ✓ | implied | ✓ | ✓ | Universal |
| Events registration | ✓ | ✓ | ✓ | ✓ | Universal (bundled) |
| Segmented email/communications | ✓ | ✓ | ✓ | ✓ (via Salesforce) | Universal (bundled) |
| Reporting (membership/renewal/retention/revenue) | ✓ | ✓ (data analytics) | ✓ | ✓ | Universal |
| Website / member-only content | ✓ | ✓ (design services) | ✓ | ✓ (communities) | Common (bundled) |
| Online community / discussion | add-on | ✓ | ✓ | ✓ | Common (bundled) |
| Chapters / sections | audience | — (AMC audience) | ✓ (module + rebates) | — (AMC audience) | Common, depth varies |
| Learning / CE / certification | — | ✓ (LMS) | ✓ (CPD/CPE) | via ecosystem | Optional |
| Job board | add-on | ✓ | — | — | Optional |
| Donations / fundraising | audience (charities) | — | ✓ (2026 donor mgmt) | — | Optional |
| Engagement scoring | ✓ (tracking) | — | ✓ (analytics) | ✓ (scoring & badging) | Common, depth varies |
| eCommerce / store | ✓ | — | — | ✓ | Optional |
| Multi-currency / tax | — | — | ✓ | ✓ | Variant (international) |
| Platform architecture | standalone SaaS | standalone SaaS suite | standalone SaaS suite | CRM-platform-native | Variant |

## Canonical Model (abstraction)

### L0 — Defining Invariant

```text
Constituent registry (identified people and/or organizations as managed records)
└── Membership record: a constituent held under a defined membership type/level
    with a time-bounded status (member in good standing ↔ lapsed/expired)
    └── Dues obligation & renewal cycle attached to the membership term
        (join → renew → renewed / lapsed), settled through recorded payments
        └── Staff-operated system of record: association staff maintain the
            registry, the lifecycle, and the financial relationship
```

Four properties. Remove any one and the Type dissolves:

- Remove the registry → it is just billing or a mailing tool.
- Remove the membership record (type/level + term + status) → it is a generic CRM contact database.
- Remove the dues/renewal cycle → it is a contact database or community platform; the recurring term-based relationship is what makes "membership" the organizing spine.
- Remove the staff-side system of record → it is a member portal (the member-facing surface only).

§24 historical check: a 1990s society running a FileMaker/Access membership tracker (registry + membership records + dues tracking) fits this definition; a modern lightweight membership-billing tool fits; a chamber's card-file era predates software but the same structure applies. The definition does not depend on portals, websites, events, or cloud delivery — all of those are era/segment additions.

### L1 — Common Mature Structure

Present in essentially all mature modern products; expected by the market but not definitional:

- Membership types/levels with distinct dues rates and benefit eligibility
- Online join/application with review/approval routing into the registry
- Renewal automation: notices, invoices, recurring/auto-billing, status transitions, lapse handling
- Member self-service portal (profile, dues payment, renewal, receipts, event registration)
- Member directory (public and/or members-only, field-level control)
- Event registration with member pricing, run off the same registry
- Segmented email/communications driven by membership attributes
- Payments/invoicing (multi-currency and tax handling in international products)
- Reporting: membership counts, renewals, retention, revenue
- Member-only content/pages gated by level and status
- Engagement history/activity tracking across events, payments, communications

### L2 — Variant / Optional Structure

- Organizational/company memberships with designated representatives (trade associations, chambers)
- Chapter/section/branch structures with delegated administration (incl. chapter dues splits/rebates)
- Committees, boards, elections, governance records
- Certification / continuing-education / CPD tracking; bundled LMS
- Online community / discussion; job boards
- Donations/fundraising (nonprofit overlap); sponsorship
- eCommerce / online store
- Bundled website builder / CMS
- Mobile apps (admin-side and member-side)
- Engagement scoring / badging / renewal-risk prediction
- Vertical shapes: professional societies, trade associations, chambers of commerce, alumni, fraternities/sororities, clubs, customer user groups
- Association management companies (AMCs) running many client associations in one system
- Architecture: standalone SaaS suite vs CRM-platform-native (Salesforce)
- Regional: multi-currency, tax handling, privacy regimes

### L3 — Vendor-specific (research notes only)

- Wild Apricot: contact-tier pricing, 60-day trial, add-on names (CommUnity, Registration Tech), Personify Payments
- Glue Up: My Glue / Manager apps, AI Copilot, reward points replacing repeat payments, chapter rebate automation, trial memberships, NVIDIA/ASAE partnerships
- Fonteva: Einstein renewal-risk prediction, Agentforce agents, Klarna BNPL, configurable surcharges, AppExchange positioning, per-user annual licensing
- YourMembership: Momentive Software suite packaging, design services, mobile event app

## Vendor-specific Findings

See L3. None of these entered the canonical model. Notably, "engagement scoring" appears in three products at different depths (tracking → analytics → scored/badged) — treated as L1/L2 gradient, not core.

## Boundary Findings

1. **Membership Management System (separate directory leaf)** — probable alias/segment split, not a structural boundary. The same products carry both labels: Glue Up markets "association management software" and "membership management software" interchangeably; Wild Apricot self-labels "membership management software" while serving associations; Fonteva self-labels both "Salesforce AMS" and "membership management software". Market usage convention: "AMS" leans toward staff-run association suites (often larger orgs, AMC context); "membership management software" leans toward lighter tools for clubs/small orgs. Structurally the core model is identical. → Flag for taxonomy review; do not silently merge.
2. **Association Event Management (flagged joint review)** — confirmed split: all four sampled AMS products bundle event registration, but event-operations depth (agendas, speakers, exhibitors, badges, lead retrieval) belongs to the event Type. The AMS owns the registry and membership lifecycle; event management consumes the registry. Remove events and an AMS remains; remove the registry and event tooling cannot price members or recognize members. Boundary = capability split inside one market, consistent with the earlier note in STATUS.md.
3. **Member Portal (separate leaf)** — the member-facing surface only. AMS products include a portal as one surface of the system; the portal leaf is the member-side Type. Remove the staff-side registry/lifecycle and only the portal remains.
4. **CRM (§07)** — an AMS is a vertical CRM for membership organizations ("Member CRM" is explicit in Fonteva and Wild Apricot marketing). The structural difference: the organizing spine is the time-bounded membership + dues/renewal cycle, not a sales pipeline. Remove the membership term/dues machinery → generic CRM.
5. **Nonprofit CRM / Donor Management (§25)** — donor-centric (donations as the recurring relationship) vs member-centric (dues as the recurring relationship). Overlap is real (Glue Up added donor management; Wild Apricot serves charities); boundary is which recurring relationship is the system's spine.
6. **Membership Billing (separate leaf)** — the dues/invoicing capability alone. AMS = registry + lifecycle + billing + operations.
7. **Church Management System (ChMS, §25)** — structurally similar (people records, giving, groups) but a distinct market with its own leaf; adjacent, not the same Type.
8. **HOA / Community Association Management (§17)** — property/assessment-centric (units, owners, assessments) rather than membership-centric; adjacent.
9. **Chapter Management Platform (separate leaf)** — chapter structures are a common AMS capability (Glue Up module; Wild Apricot/YM/Fonteva AMC/chapter audiences); the standalone leaf covers deep multi-chapter operations. AMS treats chapters as one structural variant.

## Uncertainties

- iMIS (classic enterprise AMS) could not be verified; enterprise-architecture claims rest on Fonteva alone. The L0/L1 model is not believed to depend on iMIS specifics, but enterprise legacy patterns (on-prem heritage, deep customization) are under-evidenced.
- Exact membership status vocabularies (e.g., precise status sets like "pending renewal") were not verifiable from help documentation (SPA/403). The document therefore speaks of status lifecycle generically (applied → active → renewal window → renewed/lapsed) without asserting vendor status names.
- Whether an approval gate on joining is universal: directly evidenced in Glue Up and Wild Apricot, implied in Fonteva ("customizable join workflows"). Treated as common, not defining.
- The AMS vs MMS market distinction is inferred from product self-labeling; no independent definitional source was consulted (Tier-3 sources not needed given product evidence).
- Renewal mechanics details (grace periods, notice counts, proration rules) vary and were not verifiable at help-doc precision; kept qualitative.

## Final Synthesis

An AMS is the staff-operated system of record for a membership organization. Its world is built from a constituent registry (people and organizations), membership records that bind a constituent to a membership type/level with a time-bounded status, and a recurring dues/renewal cycle that keeps that status alive. Around this spine, mature products bundle the operations a membership organization runs off the registry: joining with approval, renewal automation, member self-service, directories, events, segmented communications, payments, and reporting. Deeper capabilities (chapters, committees, certification/CE, communities, job boards, donations, eCommerce) are common but optional suite extensions whose depth belongs to sibling Types. The AMS label and the membership-management label describe the same structure at different market tiers; the true structural neighbors differ in what they remove (portal: staff side; CRM: membership term/dues; event management: the registry; billing: everything but the financial cycle).
