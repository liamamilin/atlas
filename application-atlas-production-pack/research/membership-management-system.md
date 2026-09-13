# Research Notes — Membership Management System

## Research Goal

Understand what a "Membership Management System" (market label: "membership management software") actually is as an Application Type: its core objects, the membership lifecycle it manages, how dues/renewals work, and — the central question this pass must resolve — whether it is structurally distinct from the already-processed Association Management System / AMS or an alias/segment-split of the same Type.

## Prior Flags This Pass Must Resolve (from STATUS.md)

1. **association-management-system-ams (§25, processed)** — flagged: same products carry both labels (Wild Apricot self-labels "membership management software" while serving associations; Glue Up uses both interchangeably; Fonteva self-labels both); "AMS/MMS split is a market-tier labeling convention… not a structural boundary; probable Alias/segment-split — flagged for joint review when Membership Management System is processed." → This pass must adopt, refine, or contest.
2. **membership-billing (§25, processed)** — forward note: the AMS pass's "lightweight membership-billing shape" low-end note implies a registry-first L0 for MMS; seam = revenue-loop-first (billing) vs registry-first (MMS: member records/types/lifecycle as the center, dues as one settlement leg). → This pass must adopt or contest explicitly.
3. **congregation-membership-management (§25, processed)** — probable domain-sibling pair: generic membership centers dues/renewals/benefits/self-governed member bodies vs congregation status/households/pastoral records with no dues machinery. → Joint review this pass.
4. **fitness-membership-management (§28, processed)** — vertical-vs-generic pair: same dues/lifecycle skeleton; discriminator expected to be entitlement semantics (facility access, freeze/hold, check-in conventions) and operator seat (fitness business vs membership organization). → Joint review this pass.
5. **member-benefits-management (§25, processed)** — benefits management consumes the membership standing that MMS owns (eligibility dependency). Keep-both recommended. → Confirm or contest.
6. Watch items: member-portal (member-facing surface), member-directory (directory as one output of the roll).

## Initial Boundary

Initial hypothesis: a Membership Management System is the organization-operated system of record for a membership base — a registry of members, membership records under defined types/levels with time-bounded status, and a recurring dues/renewal cycle, with self-service, directories, communications, and events run off the registry.

Adjacent leaves that must be distinguished:

- Association Management System / AMS (§25, processed — the alias question)
- Membership Billing (§25, processed), Member Portal (§25), Member Benefits Management (§25, processed), Member Directory (§25)
- Congregation Membership Management (§25, processed), Church Management System (§25), Nonprofit CRM / Donor Management (§25)
- Fitness Membership Management (§28, processed), HOA / Community Association Management (§17)
- CRM (§07), Subscription Billing Platform (§08, unprocessed)

## Research Questions

1. What is the central object model — what is a "member record" and what does it carry?
2. How are membership types/levels structured (dues, terms, billing modes, eligibility)?
3. What is the membership lifecycle (join/application → approval → active → renewal → expired/lapsed/cancelled)? What status vocabularies exist?
4. How does the renewal cycle work mechanically (reminders, auto-charge, invoices, status transitions, lapse handling)?
5. What does the member do directly (self-service) vs what does the organization's side do?
6. Which capabilities are defining vs bundled (directories, events, communications, cards, community, website)?
7. **Alias question:** do MMS-labeled products differ structurally from AMS-labeled products, or is the difference packaging/segment?
8. How do organizational/group/family memberships fit?
9. Where does the dues machinery end and Membership Billing begin (registry-first vs revenue-loop-first)?
10. Does the definition survive the historical check (paper-era membership secretary)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Tier / Philosophy | Why selected |
|---|---|---|
| Wild Apricot (Personify) | SMB all-in-one; the market's defining "membership management software" label (clubs, associations, chambers, nonprofits) | Label archetype; feature pages rich; cross-pass reuse with the AMS pass justified for the alias verdict |
| Raklet | Community/creator-flavored all-in-one (freemium, community-first) | Different philosophy; markets ONE product under membership/association/club/alumni labels — direct alias evidence |
| Join It | Lightweight minimal-core SaaS, Stripe-coupled, integration-first | Leanest core; **Tier-1 help center reachable** (status model, renewal mechanics) |
| Glue Up | Suite tier (associations/chambers, international) | Binds the suite tier to the MMS label; feature page + FAQ fetched this pass |
| MembershipWorks | Website-plugin architecture (WordPress/Squarespace/Wix-native) | Architecture variant; chamber/association audience |

ClubExpress (club/association modules) was intended as a sixth sample but its domain was unreachable (root 403, help timeout — abandoned per network rules).

## Sources

Fetched 2026-09-08 (Layer A unless noted):

- Wild Apricot — https://www.wildapricot.com/features/membership-management-software (Tier 2, feature page + FAQ)
- Raklet — https://www.raklet.com/ (Tier 2; the fetched root renders the membership-management-software solution page) + https://help.raklet.com/en/ (Tier 1, help-center index: module structure — Membership 33 articles incl. plans/application forms; Payments & Billing 18; Directory; Events; Social Network; Job Board; Reports; API)
- Join It — https://www.joinit.org/ (Tier 2, root + FAQ) + https://support.joinit.com/en/ (Tier 1, help-center index) + two Tier-1 articles: "Tracking the Status of Members" (support.joinit.com/en/articles/990121) and "How Member Renewals work" (support.joinit.com/en/articles/4665349)
- Glue Up — https://www.glueup.com/features/membership-management (Tier 2, feature page + FAQ)
- MembershipWorks — https://membershipworks.com/ (Tier 2, root)

Unreachable (recorded limitations):

- ClubExpress — root 403; help.clubexpress.com timeout (2 attempts total, abandoned)
- Wild Apricot help center (gethelp.wildapricot.com) — known JS-gated from the AMS pass; not re-attempted this pass
- iMIS-class enterprise AMS billing-module depth — unverified first-hand (inherited limitation from AMS and membership-billing passes)

Consequence: evidence is mixed Tier-1 (Join It help articles, Raklet help structure) and Tier-2 (official product/feature pages). Operational precision asserted only where directly documented (Join It status set and renewal mechanics). Everything else stays at documented-existence level. No model-memory filling.

## Product Observations

### Wild Apricot (Personify) — SMB all-in-one (MMS label archetype)

Key observations (official feature page + FAQ, this pass):

- Self-labels: "all-in-one membership management system", "Member Management Software". Audiences: associations, nonprofits, chambers, clubs, charities, chapters. 15,000+ organizations.
- FAQ defines the category: "a digital platform that helps organizations manage members, automate renewals, process payments, track engagement, and communicate at scale"; used by "professional associations, trade organizations, chambers of commerce, nonprofits, clubs, alumni groups, and community-based organizations."
- **Member database**: cloud member database; search/filter/update in real time; import from spreadsheet; customizable fields.
- **Automated dues & renewals**: automatic renewal reminders and invoicing; recurring payments ("members never miss a payment and can remain in good standing"); "automatically update membership status depending on member activities during their renewal period"; renewal policy configuration; "limit self-renewals for specific members or membership levels".
- **Member directory**: searchable, customizable; public or members-only; member self-updates.
- **Member-only website/portal**: access to member-only pages configurable by member level or group; per-level landing pages after login.
- **Membership CRM**: engagement history (renewals, event attendance, payments, communications); segmentation/filtering.
- **Reporting**: renewals, **lapsed members**, retention rates; event registration/attendance/revenue; export (Excel/QuickBooks).
- **Mobile apps**: admin app (add contacts, **approve members**, track payments, check-ins) + member app (directories, event registration, profile management).
- Custom forms stored directly in the member database; email automation with per-member tracking.

### Raklet — community/creator-flavored all-in-one

Key observations (official site + help-center index):

- **One product, four solution labels**: "Membership Management Software", "Community Engagement Software", "Association Management Software", "Club Management Software" (plus alumni/HOA/event verticals) — the same platform sold under every adjacent label. Direct first-hand alias evidence.
- Positioning: "All-in-one membership and community management platform… Sell memberships, automate renewals and reminders and offer benefits."
- **Membership plans**: "Once you create your membership plans and **approve the paid applications**, you don't need to check the amount monthly as we automate the process" — application approval workflow + automatic recurring card charging.
- **Automated reminders & renewals**: past-due emails, precise renewal dates, automatic renewals.
- **Contacts vs members**: contacts can be non-members (event attendees); member profiles with self-service updates.
- **Digital membership cards**: "track your members' status for events, gym or club check-ins"; mobile wallets.
- **Directories**: filtered member lists published as pages.
- Modules: CRM, community (discussion boards, posts, DMs), job boards, email campaigns, SMS/push, events (tickets, RSVPs, check-in), engagement reports, website/portal builder with custom domain.
- FREE plan available (free tier exists — free/comped memberships are a plan shape, the dues machinery remains).
- Help-center module structure (Tier 1): Membership (33 articles — set up plans, application forms), Contacts (25), Messages (22), Events (18), Payments & Billing (18), Social Network (19), Directory, Job Board, Reports, API (membership plans).

### Join It — lightweight minimal-core SaaS

Key observations (official site + FAQ + Tier-1 help articles):

- Positioning: "Membership Management Software with Digital Cards… Built for clubs, associations, nonprofits, and communities. Manage members, collect recurring payments, accept event registrations, and issue digital membership cards—all in one simple system." 4,000+ organizations, 40+ countries.
- Member journey framing: "from organizing member records and issuing **proof of membership** to collecting payments, supporting member self-service and keeping your community engaged."
- **Member database**: profiles, memberships, payments, notes, activity; custom fields; membership and payment status in one place.
- **Status model (Tier 1, "Tracking the Status of Members")** — "the Status field associated with memberships… organize, segment, and manage your members throughout their lifecycle":
  - **Prospective** — shown interest, not yet joined; manually assignable
  - **Pending** — "applications awaiting approval / awaiting payment / any custom review or onboarding step"
  - **Active** — fully active, current member
  - **Expired** — "automatically assigned when a membership reaches the end of its term without renewal"
  - **Cancelled** — intentionally cancelled
  - Statuses enable "a workflow for processing new members (e.g., approvals, onboarding, welcome emails)"; status names fixed in this product (product-specific).
- **Renewal mechanics (Tier 1, "How Member Renewals work")**:
  - Two term models: **rolling renewals** vs **fixed expiration dates** (membership types with a common cycle date)
  - Reminders: manual one-off or automated, configurable offsets before expiration, multiple reminders schedulable; **Inactive Notices** trigger on expiry or cancellation for re-engagement
  - Renewal checkout prefilled (details, waivers, payment); confirmation email; member-portal self-renewal; members can **switch membership types during renewal**
- **Membership types (Tier-1 collection "Managing Your Membership Types")**: create/edit types; renewal settings per type; auto re-billing vs one-time billing; term length for auto re-billing; fixed expiration dates; age restrictions; introductory pricing; **check-in limits per membership type**; membership IDs; custom fields incl. file upload and digital signatures; displaying membership benefits.
- **Group memberships (Tier-1 collection)**: group vs individual types; **couples membership**; "Organizations/Businesses as Members, instead of Memberships for Individuals"; group renewals; transferring memberships out of groups.
- **Payments (Tier-1 Finances collection)**: Stripe processing; auto re-billing; failed-payment notifications and handling; offline/external payment recording; refunds; credits; invoices for dues; tax on dues; multi-currency; donations on top of dues; Gift Aid.
- **Automated email taxonomy (Tier 1)**: membership confirmation on join (Type A) and on renew (Type B); renewal reminders; payment confirmations; failed-payment notifications; inactive notices on expiry (Type A) and on cancellation (Type B).
- **Digital cards & check-in (Tier-1 collection)**: Apple/Google Wallet cards with QR showing up-to-date membership status; member check-in and attendance tracking; kiosk mode.
- **Benefits**: displaying membership benefits per type; "Offering Partner-Validated Membership Benefits (Third-Party Redemption)" use case; membership validation via Zapier; benefit redemption on Eventbrite.
- Member directory (with opt-out); member portal (posts, events, directory, self-service); event registration with member pricing; chapter-based organizations guide; migration (CSV import incl. membership types and statuses; import existing Stripe subscriptions).
- Segment stretch: "Business & Services — Run loyalty, passes, and subscriptions for brands people visit" — consumer-facing memberships (loyalty/passes) sold by non-membership businesses. Same core, different operator seat.
- Integrations: Mailchimp/Constant Contact/Klaviyo ("Every new, renewed or **lapsed member** lands in the right list"), QuickBooks/Xero, Eventbrite, Zapier, webhooks, REST API.

### Glue Up — suite tier

Key observations (official membership-management feature page + FAQ, this pass):

- Headline: "AI-Powered Membership Management Software for Modern Associations & Chambers… for associations, chambers, nonprofits, and member-based organizations." 5,000+ member-based organizations.
- FAQ self-definition: "Glue Up is a membership management software… It helps organizations, particularly professional associations, chambers of commerce, and nonprofits, simplify and automate their member application and renewal processes, maintain an updated member database, and offer members exclusive content." — both labels on one page.
- **Member lifecycle framing**: "from first application to renewal, event participation, email engagement, payments, and reporting."
- **Centralized member database**: contact details, membership levels, engagement history, event activity, payment records, communication preferences.
- **Applications**: online application forms; "Unlimited Membership Types"; collect payments; apply discounts; **route applications for review**; "move approved applicants into your member database automatically."
- **Renewals & dues**: renewal reminders, dues collection, recurring payments, discounts, "update membership status", renewal-activity reporting; FAQ: **auto-billing** "automatically charge the due amount from the member's card or send invoices when the due date is reached"; failed-payment notifications; multi-currency and tax.
- **Member self-service (My Glue)**: update profiles, renew, pay invoices, register for events, access directories; staff Manager app.
- Members-only pages gated by member levels/groups; membership directories (org controls what each shows); digital membership cards; coupons; trial memberships; committee management; chapter management (FAQ: multiple chapters, granular permissions; automated chapter rebate payments).
- Community (groups, direct chat, business cards), events (member-only pricing), email campaigns segmented by membership type/renewal status/chapter/committee, reporting (status, renewal trends, payment history).
- FAQ: "What is Membership Management Software? A simple, intuitive, and automated system that helps manage your community or organization's membership database. It scales with you as your community grows."

### MembershipWorks — website-plugin architecture

Key observations (official root page):

- "All-in-one membership software": membership management, member directory, event calendar & registrations, online payments (member billing), donations/shopping cart/web forms, job boards, announcement boards, classified ads, members-only content.
- **Architecture variant**: plugin into an existing website (WordPress, Squarespace, Weebly, Wix, Duda, Without Code, HTML5) rather than a bundled site builder.
- Designed-for statement: "Chambers of Commerce, Professional Associations, Trade Associations, Industry Associations, Networking Groups, Societies, Non-profits and other membership groups."
- Testimonial evidence: association profiles with member self-control; event sign-up and payment via Stripe integration; membership reports.

## Cross-product Comparison

| Structure / capability | Wild Apricot | Raklet | Join It | Glue Up | MembershipWorks | Reading |
|---|---|---|---|---|---|---|
| Central member database (identified people/orgs) | ✓ | ✓ (contacts ⊇ members) | ✓ | ✓ | ✓ | Universal |
| Membership types/levels with dues | ✓ (levels, self-renewal limits) | ✓ (plans) | ✓ (types: auto re-bill vs one-time, term, age gates) | ✓ (unlimited types) | ✓ | Universal |
| Join/application with approval routing | ✓ (admin approves) | ✓ (approve paid applications) | ✓ (Pending status for approval) | ✓ (route for review → auto-move) | implied | Common-to-universal |
| Time-bounded membership + status lifecycle | ✓ (auto status updates, lapsed in reporting) | ✓ (status on cards) | ✓ (Prospective/Pending/Active/Expired/Cancelled, Tier-1) | ✓ (status changes) | ✓ | Universal (vocabularies vary) |
| Renewal automation (reminders, invoices, recurring charge) | ✓ | ✓ | ✓ (Tier-1: rolling vs fixed dates, offsets, inactive notices) | ✓ (auto-billing) | ✓ (member billing) | Universal |
| Payment collection & money records | ✓ (payments processing) | ✓ (card auto-charge) | ✓ (Tier-1: Stripe, refunds, credits, offline, tax) | ✓ (auto-billing, multi-currency) | ✓ (Stripe) | Universal |
| Member self-service (portal/app: profile, renew, pay) | ✓ | ✓ | ✓ (Tier-1: portal renewal, card update, cancel) | ✓ (My Glue) | ✓ (profiles) | Universal |
| Member directory (public/members-only, controlled) | ✓ | ✓ | ✓ (opt-out) | ✓ (multiple, controlled) | ✓ | Universal |
| Member-only content / benefit gating by level & status | ✓ | ✓ (members-only content) | ✓ (benefits display, partner redemption, check-in limits) | ✓ (members-only pages) | ✓ (members-only website) | Universal |
| Digital membership cards as proof of membership | ✓ (check-ins in app) | ✓ | ✓ (Tier-1: wallet cards, QR status) | ✓ | — | Common |
| Events with member pricing | ✓ | ✓ | ✓ | ✓ | ✓ | Universal (bundled) |
| Segmented communications driven by membership data | ✓ | ✓ | ✓ (Tier-1 email taxonomy on lifecycle events) | ✓ | implied | Universal |
| Reporting (renewals, lapsed/churn, revenue) | ✓ | ✓ (engagement) | ✓ (renewals, churn) | ✓ | ✓ | Universal |
| Community/discussion surfaces | add-on | ✓ (boards, DMs) | portal posts/directory messaging | ✓ (groups, chat) | — | Common (bundled) |
| Group/org/family membership units | levels-level | — | ✓ (Tier-1: groups, couples, businesses) | levels-level | — | Common (depth varies) |
| Chapters | audience | — | guide | ✓ (module + rebates) | — | Common, depth varies |
| Donations | audience | ✓ (fundraising module) | ✓ (on top of dues) | ✓ | ✓ | Common (bundled) |
| Job boards / classifieds | add-on | ✓ | — | — | ✓ | Optional |
| Website builder / members-only website | ✓ | ✓ | portal + widgets | ✓ | ✓ (plugin into existing site) | Common; architecture variant |
| Free/comped membership plans | — | ✓ (free plan tier) | ✓ (one-time/free types supported) | trial memberships | — | Variant |
| Consumer-membership stretch (loyalty/passes for businesses) | — | gyms/HOA verticals | ✓ (Business & Services) | corporations (events-led) | — | Variant (operator-seat stretch) |
| Architecture | standalone SaaS suite | standalone SaaS + branded apps | lean SaaS, Stripe-coupled, API/webhooks | standalone SaaS suite | website-plugin | Variant |

**Population shape:** the MMS-labeled market realizes ONE Type in poles — lean self-serve core (Join It), freemium community-flavored suite (Raklet), SMB all-in-one archetype (Wild Apricot), international association/chamber suite (Glue Up), website-plugin architecture (MembershipWorks). All share the same spine: member database → membership type/level → time-bounded membership record → renewal/dues cycle → self-service + benefits + directory + communications + events around it.

## Alias Question — AMS vs MMS (the central verdict)

First-hand evidence this pass:

1. **Raklet sells one product under four labels** — "Membership Management Software", "Association Management Software", "Club Management Software", "Alumni Engagement Software" (plus HOA/event verticals). Same module set behind each.
2. **Glue Up's membership-management feature page** addresses "Modern Associations & Chambers", self-defines as "membership management software", and the same vendor site carries an "association management software" solution page. Both labels, one product.
3. **Wild Apricot** — the MMS label archetype — serves associations/chapters as headline audiences (cross-confirmed with the AMS pass's first-hand fetch).
4. **Join It** (MMS-labeled) publishes an "Association Management" guide and serves professional associations as a primary community; its core (types, statuses, renewals, dues) is the same structure the AMS pass documented for AMS-labeled products (Fonteva/YourMembership/Glue Up/Wild Apricot).
5. **MembershipWorks** (membership software label) is designed for chambers and professional/trade associations.

Verdict: **probable Alias (segment-split), not a structural boundary.** The AMS pass's prediction is confirmed by this pass's independent first-hand evidence. The market convention: "membership management software/system" is the *generic* label (any membership-based organization: clubs, chambers, communities, nonprofits, associations; skewing smaller/leaner), while "AMS" is the *association-operations suite* label (association-flavored packaging: chapters, committees, CE/governance depth; skewing mid/large organizations). Structurally the core is identical — same four-part spine. Per workflow rules this pass does not merge the directory; both documents stand, cross-referenced, and alias consolidation is recommended to the taxonomy owner.

Registry-first adoption: this pass **adopts** the membership-billing pass's forward note — the MMS L0 is registry-first (member records/types/lifecycle as the center, dues as one settled leg of the lifecycle), which cleanly separates it from the revenue-loop-first Membership Billing L0.

## Canonical Model (abstraction)

### L0 — Defining Invariant

```text
Member registry (identified people and/or organizations as managed records)
└── Membership record: a member held under a defined membership type/level
    with a time-bounded status (join-side pending states; active ↔ expired/lapsed/cancelled)
    └── Renewal/term cycle with dues attached to the term
        (join/application → renewal → renewed or expired/lapsed), settlements recorded
        └── Organization-operated system of record: the organization's own
            administrators maintain the registry and the lifecycle;
            members act on their own records through self-service
```

Four structures held jointly. Remove any one and the Type dissolves:

- Remove the member registry → dues billing with member-shaped customers (Membership Billing territory) or a mailing list.
- Remove the membership record (type/level + term + status) → a generic CRM contact database.
- Remove the renewal/dues cycle → a directory/community platform or a dues-free roll (the congregation-roll shape, which the directory treats as its own sibling).
- Remove the organization-operated system of record → only a member portal remains (the member-facing surface Type).

§24 historical check: the paper-era membership secretary's kit — a membership card file/ledger (registry), cards noting membership type and paid-through date (membership record with term and status), renewal notices with dues collection each cycle (renewal/dues cycle), maintained by the club/chamber/association secretary or a volunteer board (organization-operated records) — satisfies all four structures. Union dues books with stamps and card-file chambers fit the same shape. The definition therefore names no portal, no website, no cards-in-wallets, no cloud, no payment rail — those are era/segment additions. ✔

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Membership types/levels with distinct dues rates, terms, and benefit eligibility; eligibility rules (age restrictions in one product) and introductory/trial pricing
- Online join/application forms with optional approval routing into the registry; prospective/pending intake states
- Renewal automation: renewal notices/reminders, renewal policies, self-renewal permissions, invoices, auto-charge of stored payment methods, status transitions on payment/expiry, lapse/inactive notices for re-engagement
- Payment machinery: online processing, one-time and recurring dues, offline payment recording, refunds/credits, taxes, multi-currency (international products)
- Member self-service portal/app: profile, renew, pay, receipts, event registration, directory access, cancel/type-switch at renewal
- Member directory: public and/or members-only, organization-controlled fields, opt-outs
- Member-only content/benefits gated by level and standing; digital membership cards as proof of membership (wallet cards/QR), check-in/attendance
- Events (free/paid, member pricing, check-in) run off the same registry
- Segmented communications driven by membership attributes and lifecycle events
- Reporting: membership counts, renewals, retention/churn, revenue; exports (Excel/QuickBooks-class accounting)
- Data operations: import/migration (with types and statuses), dedup/merge, bulk updates, custom fields

### L2 — Variant / Optional Structure

- Membership-unit variants: individual, couples/family groups, organizations/businesses as members with representatives
- Chapter/branch structures with delegated administration; committee management
- Community surfaces (discussion boards, member-to-member messaging), job boards, classifieds
- Donations/fundraising (nonprofit overlap); eCommerce/store
- Bundled website builder vs plugin-into-existing-site architecture vs portal-only
- Free/comped/trial membership plans within a dues-capable engine
- Consumer-membership stretch: loyalty/passes/subscriptions operated by non-membership businesses (gyms, venues, consumer brands)
- Vertical seasoning per operator seat: chambers, professional/trade associations, clubs (hobby/sports/car/alumni), charities, HOAs, coworking, museums
- Platform architecture: standalone SaaS, suite module, CRM-platform-native, website plugin
- Regional: payment rails, tax handling, privacy regimes, multi-language

### L3 — Vendor-specific Detail (research notes only)

- Wild Apricot: contact-tier pricing, 60-day trial, onboarding coaches, add-on names (CommUnity, Registration Tech, Personify Payments), admin/member app split
- Raklet: branded mobile apps, reward points replacing repeat payments, free plan tier, discovery-call sales motion
- Join It: fixed five-status vocabulary (not customizable, product-specific), Stripe-coupled billing, gift memberships, kiosk check-in mode, check-in limits per membership type, membership-pricing calculator, "Copy for LLM" help affordances
- Glue Up: My Glue / Manager apps, AI Copilot, chapter rebate automation, trial memberships, CPD/CPE credit module
- MembershipWorks: multi-CMS plugin architecture (WordPress/Squarespace/Weebly/Wix/Duda/Without Code/HTML5), developer listing marketplace

## Rejected Findings

- "MMS is a distinct, structurally-lighter Type than AMS": rejected — every attempted discriminator (leaner tier, lighter dues machinery, less governance depth) is a packaging/segment gradient, not a structural difference; the same products carry both labels and the sampled MMS cores match the AMS pass's documented structure exactly.
- "Free/comped memberships break the dues-cycle leg": rejected — free plans are plan shapes inside a dues-capable engine (Raklet free tier, Join It one-time/free types); the machinery is present and standard.
- "Digital membership cards / check-in are definitional": rejected — absent from MembershipWorks' core page; paper-era cards were physical, not digital; proof-of-membership is the conceptual slot, its implementation varies.
- "Consumer loyalty/passes (Business & Services pole) make this a different Type": rejected as a variant — same member registry + membership record + renewal machinery; only the operator seat differs (watch-item for consumer-membership leaves if the taxonomy grows there).
- Single-product behaviors (Join It's fixed status names, check-in limits; Raklet reward points; Glue Up chapter rebates) not promoted.

## Boundary Findings

| Neighbor | Judgment | "Remove what → becomes the other Type" |
|---|---|---|
| **AMS** (§25, processed) | **Probable Alias / segment-split — RESOLVES the AMS pass flag.** Same four-part core, same products carrying both labels (Raklet 4 labels; Glue Up both; Wild Apricot MMS label + association audiences). Market convention: MMS label = generic/leaner tier; AMS label = association-suite packaging. Both documents stand, cross-referenced; consolidation recommended to taxonomy owner. | Remove the association-suite packaging (chapters/committees/CE depth) from an AMS → still this Type; add association-operations packaging → sold as AMS. No structural removal separates them. |
| **Membership Billing** (§25, processed) | Adopted seam (registry-first vs revenue-loop-first). Keep-both. | Remove the registry/lifecycle breadth and center the dues/revenue machinery → Membership Billing. |
| **Fitness Membership Management** (§28, processed) | Keep-both confirmed. Same dues/lifecycle skeleton; discriminator = entitlement semantics (facility access, freeze/hold culture, check-in conventions) + operator seat (fitness business vs membership organization). | Remove the fitness entitlement semantics while keeping dues+state → this Type. |
| **Congregation Membership Management** (§25, processed) | Keep-both confirmed (domain-sibling pair). Generic membership is dues-bearing with renewal machinery for self-governed member bodies; the congregation roll centers people/households/status with no dues machinery. | Remove the dues/renewal machinery and re-domain to pastoral records/households → congregation roll. |
| **Member Benefits Management** (§25, processed) | Keep-both confirmed. Benefits management consumes the standing this Type owns (eligibility dependency); dedicated benefit platforms anchor member identity externally. | Remove benefit-program depth, keep standing → this Type. |
| **Member Portal** (§25) | Complementary surface. | Remove the organization-side registry/lifecycle; keep only the member-facing self-service → Member Portal. |
| **Member Directory** (§25) | Capability slice — the directory is one output of the registry. | Remove the lifecycle/dues machinery; keep the published member list → Member Directory. |
| **CRM** (§07) | Vertical CRM with a time-bounded membership spine. | Remove the membership term/dues machinery → generic CRM. |
| **Member Community Platform** (§25) | Interaction-first vs registry-first. | Make discussion/community the center and the registry incidental → community platform. |
| **Nonprofit CRM / Donor Management** (§25) | Donations vs dues as the recurring relationship. | Make donations the recurring relationship spine → donor management. |
| **Subscription Billing Platform** (§08, unprocessed) | Flag stands: dues-for-belonging (standing is the "fulfillment", gated by payment) vs vendor-billed product/service subscriptions. Joint review when that leaf is processed. | Remove the organizational belonging + standing coupling → generic subscription billing. |
| **HOA / Community Association Management** (§17) | Property/assessment-centric (units, owners, assessments). | Make units/assessments the spine → HOA management. |

## Uncertainties

- Join It's five-status vocabulary is one product's model (Tier-1 verified there, fixed names product-specific); other products' exact status sets were observed only at documented-existence level (Wild Apricot "automatically update membership status", Glue Up "update membership status", "lapsed members" reporting). The canonical lifecycle is therefore stated generically.
- Approval-on-join universality: directly evidenced in 4/5 (Wild Apricot, Raklet, Join It, Glue Up); implied in MembershipWorks. Treated as common, not defining.
- Enterprise/legacy MMS-class deployments (iMIS-class systems run as "membership systems") remain unverified first-hand (inherited limitation); the enterprise association pole is covered by the AMS pass's Fonteva evidence.
- ClubExpress (club/association module tier) unreachable — its segment is otherwise covered by Wild Apricot/Raklet/Join It club verticals.
- Chapter/committee/governance depth varies widely between the lean and suite poles; the document treats these as common-optional, with depth belonging to sibling Types.

## Final Synthesis

A Membership Management System is the organization-operated system of record for a membership base. Its world is: a member registry (identified people and organizations) → membership records binding a member to a defined type/level with a time-bounded status → a renewal/term cycle with dues attached to the term, settled through recorded payments → all operated by the organization's own administrators, with members acting on their own records through self-service. Around this spine, mature products run the operations a membership organization performs off its registry: joining with approval, renewal automation, benefit gating and member-only content, directories, proof-of-membership cards, events, segmented communications, and reporting. The market realizes one Type in poles — lean self-serve core, freemium community-flavored suite, SMB all-in-one, association/chamber suite, website-plugin architecture — and the "membership management" label is the generic form of the same structure the market also sells as "association management software"; the two labels segment packaging and customer tier, not structure.
