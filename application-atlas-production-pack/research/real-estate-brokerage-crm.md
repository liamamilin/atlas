# Research Notes — Real Estate Brokerage CRM (§17 Construction, Real Estate & Facilities)

Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

## Research Goal

Understand the real-estate brokerage's own CRM as an Application Type: the software a brokerage, team, or agency uses to hold its client/prospect relationships, work them as buyers and sellers of property, and carry them through the brokerage's pipeline to closed transactions — and to separate this Type from the neighboring §17 leaves (Property Listing Platform, Property Showing Platform, Real Estate Transaction Management) and from the generic §07 CRM family.

## Initial Boundary (hypothesis before research)

- Core use: manage leads/clients (buyers, sellers, landlords, tenants-as-applicants) and the deals that come from them.
- Users: agents, team leads, ISAs (inside sales agents), brokers/owners, admins.
- Nearest neighbors: generic CRM (§07), Property Listing Platform (§17), Property Showing Platform (§17), Real Estate Transaction Management (§17), Lead Generation/Lead Management (§06), Account Management CRM (§07).
- Likely confusion #1: "CRM that has listings" vs the public listing venue.
- Likely confusion #2: showing/appointment scheduling vs the client relationship + pipeline record.
- Unknowns: whether the listing/property record is definitional or variant; how regional markets (UK applicant-vendor model vs US MLS/IDX model) affect the core; where transaction management stops being packaging.

## Research Questions

1. What are the core objects? (contact, lead, buyer/seller role, property/listing, deal/transaction, activity, pipeline stage)
2. How do leads enter, and how are they routed to agents?
3. What does the pipeline look like, and what object carries the stage (contact vs separate deal)?
4. What is the property's role in the model — inbound data (MLS/IDX), outbound listing origin (portal feeds), or both?
5. What distinguishes the brokerage/team structure (ISA, team lead, broker) from generic CRM roles?
6. Where does transaction management / post-contract work live — in the CRM or a sibling Type?
7. Which capabilities are definitional vs common vs optional vs vendor-specific?
8. Does the definition survive the historical/regional check (older, non-US, non-MLS products)?

## Representative Products

| Product | Market role | Why sampled |
|---|---|---|
| Follow Up Boss (US, part of Zillow group) | Team/agent sales-focused real estate CRM ("open system" pole) | Deep Tier-1 help center; canonical stage vocabulary; lead-routing machinery |
| BoldTrail / Inside Real Estate (kvCORE + BoomTown + Brokermint merged) | Brokerage all-in-one front-office platform pole | Ecosystem structure (Smart CRM + IDX websites + Lead Engine + BackOffice) |
| Wise Agent (US, independent) | Small/independent agent classic CRM with embedded transaction checklists | Agent-tier pole; property lists + transactions inside the CRM |
| BoomTown (US, Inside Real Estate) | Lead-generation-driven team platform | Lead gen + predictive CRM + ISA routing evidence |
| Reapit (UK) | UK estate-agency platform pole (Sales CRM / Lettings CRM / PM) | Regional check: applicant–vendor–property record triad, portal-push listing origin, AML compliance |
| Top Producer (US/Canada, Constellation1) | Veteran all-in-one CRM (decades-old lineage) | Historical anchor; MLS Property Insights; Market Snapshot; HouseValues seller leads |

Selection satisfies: market representation, documentation completeness, different product philosophies (open CRM vs all-in-one vs agency platform), different customer tiers (solo agent → team → brokerage → multi-branch agency).

## Sources

Tier-1 (official operational documentation):
- Follow Up Boss Help Center — help.followupboss.com
  - "Getting Started: Owners & Admins" (article 1500008524262)
  - "Changing a Lead Stage" (article 360012456793) — full default stage table
  - "Lead Flow Overview" (article 360014570494)
- (Others' help centers not fetched this pass; see Source-access Limitation.)

Tier-2 (official product pages):
- Wise Agent — wiseagent.com (home; /features/transaction-management.asp)
- BoomTown — boomtownroi.com (home; /features/predictive-crm)
- Reapit — reapit.com (root; /platform/sales-crm incl. FAQ)
- BoldTrail — boldtrail.com (root; product architecture), insiderealestate.com (root; /solution/)
- Top Producer — topproducer.com (root)

Source-access Limitation:
- reapit.com/gb/agents-and-agencies/agency-crm 404'd (recovered via root + /platform/sales-crm).
- insiderealestate.com/boldtrail 404'd (recovered via /solution/ and boldtrail.com).
- Reapit support portal (reapitsupport.refined.site), Top Producer support (support.topproducer.com), and BoldTrail help (help.insiderealestate.com) not accessed — behind support portals / not fetched. Reapit/BoldTrail/Top Producer assertions are therefore held at product-page strength; no Tier-1 operational detail claimed for them.
- No help-center article for BoomTown fetched (intercom.help/boomtown/en listed but not fetched) — BoomTown at product-page strength.
- Follow Up Boss is the only product with deep Tier-1 evidence; used as the vocabulary anchor, cross-checked at the structure level against the others.

## Product Observations

### Follow Up Boss (evidence layer A — help center)

- Getting Started (Owners & Admins): the setup sequence is the type's anatomy: 1) invite your team (team management); 2) link Zillow profile (lead-source integration); 3) import existing contacts (CSV) and "organize everyone by stage"; 4) sync new leads — inbox lead processing via Google/Microsoft 365, direct lead-source and IDX integrations, website pixel for tracking + call/text capture, and "set up lead distribution for web sources on the Lead Flow"; 5) automate follow-up — Smart Lists to find "the people you need to follow up with and when", Action Plans assigned per lead source to "instantly text and email your new leads"; 6) daily workflow; mobile apps.
- Stage table ("Changing a Lead Stage"): stages track "who a contact is to you right now". Default definitions: Lead ("Not spoken to yet", default stage for new people) → Attempted Contact → Spoke with Customer → Appointment Set → Met with Customer → Showing Homes → Listing Agreement ("A listing agreement is in place for you to list your seller's home") → Active Listing ("A client who has their home on the market and available for showings") → Submitting Offers → Under Contract ("Offer accepted") → Nurture / Rejected / Closed ("Closed deal or post-closing") / Trash. One pipeline serves BOTH sides: buyer flow (Appointment → Met → Showing Homes → Submitting Offers → Under Contract) and seller flow (Listing Agreement → Active Listing → Under Contract). Tags (Buyer, Seller, Renter) group contacts "on top of stages". Stages are customizable per team; Action Plans can update stages automatically; automations can key off stage changes.
- Lead Flow: "the command center for new web leads to make sure leads are assigned to the correct agents/lenders and the specified action plan automatically runs to initiate communication. Automate everything to increase speed to lead." Per-lead-source config: assigned agent or group, lender, action plan. Advanced routing rules by tags, price, city, state, zip code, MLS number, phone number. Related: Lead Ponds, First to Claim, groups, instant response.
- Roles: owners/admins vs "agent or lender on a team"; product pages for Solo Agents / Team Leaders / ISAs / Admins / Large Teams — the ISA (inside sales agent) is a first-class role.
- Compare page: positions itself as "Open System vs All-In-Ones" — the CRM-centric pole vs bundled platforms.
- Lead sources: "we accept leads from that source" list of lead providers (Zillow etc.); inbox processing converts email inquiries into contacts.

### Wise Agent (evidence layer A/Tier-2 — product pages)

- Home: "all-in-one real estate CRM built for agents, teams, and brokerages. It brings lead management, follow-up, transactions, and marketing together in one simple platform." Features: Lead Generation (website visitor identification, IDX websites, landing pages, digital ads feeding "directly into your CRM"), Lead Pipelines ("track and work leads as they move through your pipeline"), Contact Summaries ("contact details, notes, and full activity history in one place"), Bulk Emailing, Texting ("logged to each contact automatically"), Drip Campaigns, Lead Rules and Distribution ("Route, assign, and respond to new leads instantly"), Team Features ("shared calendars & leads, lead assignment, distribution and tracking, team-member-based permissions"), Transaction Checklists, Transaction Portals ("clients... view real-time progress"), Commission Reporting, checklist triggers, AI writing assistant. Trusted-by list = franchise brokerages (Century21, Sotheby's, Coldwell Banker, Keller Williams, RE/MAX, eXp...).
- Transaction page: buyer/seller/rental checklist templates; task assignment to team members; automated triggers; client portals; **Property Lists** — "Store, access, and manage all your property info, connected to transactions and reports. MLS Integrations: quickly import listings and link them to your transactions"; "link contacts to specific listings"; commission reporting connected to contacts/checklists/transactions.
- Structure: property records exist inside the CRM (MLS-imported or manual), linked to contacts and to transactions; the transaction checklist is embedded, not a separate product.

### BoomTown (evidence layer A/Tier-2 — product pages)

- Home: "Expert lead generation, IDX websites, intelligent CRM, lead management services... flexible packages" (Launch/Core/Grow/Advance + btPRO); Success Assurance = vendor-run "team of Lead Concierges to monitor your entire database for meaningful lead behaviors and engage them at the right time".
- Predictive CRM page: "monitor customer relationships, manage lead generation, and close deals in one, integrated solution."
  - Lead distribution: "Send leads to the right agents — round robin or agent-on-duty... or send them directly to an ISA before distributing them among your agents."
  - Actionable insights: "Lead activity is tracked within the real estate CRM system to give you predictive insights on top opportunities"; Hot Sheet with MLS Updates ("Keep tabs on hot listings and get every update right in your CRM"); Best-Fit Leads ("Match your best listings with the most fitting and interested homebuyers"); Opportunity Wall.
  - Lists/segmentation: "Tag and segment leads based on location, price point, haven't yet called, etc."
  - Action plans: "automated emails, texts, and scheduled to-do's."
  - Pipeline: "Full-Circle Pipeline Management — follow your transaction lifecycles from start to finish"; My Deals dashboard ("view open opportunities, check status of pending deals, track ROI of closed transactions"); Transaction Management Integrations ("seamless handoff between the real estate agent and transaction coordinator").

### BoldTrail / Inside Real Estate (evidence layer A/Tier-2 — product pages)

- Inside Real Estate = merged kvCORE + BoomTown + Brokermint brands; BoldTrail = "complete tech ecosystem"; 400k+ users claim.
- BoldTrail Platform (front office): IDX Websites, Lead Engine, Smart CRM, Marketing Autopilot, Transaction Integration, Business Analytics, Integrated AI. Framing verbs: Generate / Promote / Connect / Transact / Operate / Analyze / Recruit / Report / Retain.
- BoldTrail BackOffice (ex-Brokermint): agent billings, agent onboarding, accounting, commission management, reporting — the brokerage back office is a separate product integrated with the front office.
- BoldTrail Recruit: agent recruitment/retention (recruiting dashboard, transaction heat map) — recruiting agents is a brokerage-level workflow adjacent to client CRM.
- Solutions tiers: For Agents / For Teams / For Brokers / For Enterprise (brands/franchises).
- Support/help center exists (help.insiderealestate.com) but not fetched — product-page strength only.

### Reapit (evidence layer A/Tier-2 — product pages, UK pole)

- Platform: Sales CRM, Lettings CRM, Bookings, Property Management, Client Accounts, DataWarehouse, Integrations, Reapit Go (mobile). "Unite sales, lettings and property management on one platform." 25+ years; 15k+ branches; per-user pricing; migration 5–12 weeks (vendor-stated).
- Sales CRM page: "Generate leads, turn appraisals into instructions" (UK vocabulary: appraisal = listing valuation visit, instruction = won listing mandate); "track tasks, view messages and appointments, and progress sales, all on one customisable dashboard"; compliance: "built-in checks and robust AML processes"; FAQ: "fields on property records to ensure the right details are stored before you push properties onto portals" + "checklist workflows before, during, and after each sale" + "intuitive chain management functionality".
- Three record types named explicitly:
  - **Applicant Record** — "from marketing consent and key requirements to offers and applicant status... match applicants with suitable properties within your property portfolio."
  - **Property Record** — "from property attributes and marketing consent to property status and key contact details... match properties to applicants."
  - **Vendor Record** — "from marketing consent and ID Checks for properties to vendor status and referrals... letter templates."
- Bookings: "Turn portal leads into quality viewings... let renters book viewings straight into your diary."
- AI: "matching applicants instantly, listing properties faster, automating communications and payments."
- FAQ: "one record of truth for every single client or property"; full audit trail of client interactions; "find vendors, match buyers and progress sales."
- Regional significance: the property record lives IN the agency CRM (no MLS dependency), applicant matching is native, listings push OUT to portals — the mirror image of the US pattern where listing data flows IN from MLS/IDX.

### Top Producer (evidence layer A/Tier-2 — product pages; historical anchor)

- "All-in-one business management platform... meaningful relationships, simplify your day-to-day"; solutions for agents and for teams & brokers; 150+ lead sources synced.
- HouseValues seller leads "with validated contact data and complete property details, delivered right into your CRM."
- MLS Market Snapshot: "branded MLS market reports and real-time alerts for new listings, price changes and sold properties... for all stages of the client lifecycle."
- Dynamic Workflows + Tasks; Lead Response plans applied automatically to incoming leads; Follow Up Coach ("tells me who to call on a specific day").
- Transaction Management: "reminders, expertly created templates, and a timeline that shows you exactly what stage you and your clients are at. With the added MLS integration you can quickly pull relevant listing data with just one click."
- **MLS Property Insights**: "label and take notes on their properties of interest. Property Insights... automatically populating listing data and status (for sale, sold, price change)."
- 360° Contact View + Social Insights; Smart farming (AI-predicted likely sellers).

## Cross-product Comparison

| Structure | FUB | Wise Agent | BoomTown | BoldTrail | Reapit | Top Producer | Verdict |
|---|---|---|---|---|---|---|---|
| Persistent contact/person records as the brokerage's shared database | ✓ (import, team invite) | ✓ ("contact summaries", shared leads) | ✓ ("monitor customer relationships") | ✓ (Smart CRM) | ✓ (applicant/vendor records; "one record of truth") | ✓ (360° contact view) | Core (all 6) |
| Buyer/seller (applicant/vendor) role framing of the relationship | ✓ (stages have both buyer & seller legs; Buyer/Seller tags) | ✓ (buyer/seller/rental checklists) | ✓ (buyers + listings) | ✓ (CRM + listing + transaction objects) | ✓✓ (applicant + vendor record types named) | ✓ (seller leads; buyers) | Core (all 6; two realizations) |
| Property context bound to the relationship | ✓ (MLS number as routing rule; Zillow/IDX integration) | ✓ (Property Lists linked to contacts & transactions; MLS import) | ✓ (Hot Sheet with MLS updates; Best-Fit Leads matching listings↔buyers) | ✓ (IDX sites, listing objects, transaction integration) | ✓✓ (Property Record as first-class; applicant↔property matching; portal push) | ✓✓ (MLS Property Insights on contacts' properties of interest; Market Snapshot) | Core (all 6; direction varies) |
| Pipeline/stages over the client relationship | ✓✓ (full stage vocabulary; stage-per-contact) | ✓ (lead pipelines) | ✓ (My Deals, open opportunities) | ✓ (CRM + transaction stages) | ✓ (applicant status, offers; sales progression; chain mgmt) | ✓ (transaction timeline stages; workflow plans) | Core (all 6; carrier object varies) |
| Multi-channel lead intake (portals, IDX sites, ads, referrals, past clients) | ✓ (lead providers, inbox processing, pixel) | ✓ (visitor ID, landing pages, ads) | ✓ (lead generation services) | ✓ (Lead Engine) | ✓ (portal leads via Bookings) | ✓ (150+ sources, HouseValues) | Standard |
| Lead routing/distribution to agents | ✓✓ (Lead Flow: round-robin-class groups, ponds, first-to-claim, rules incl. MLS number) | ✓ (lead rules & distribution) | ✓ (round robin / agent-on-duty / ISA-first) | ✓ (team routing in platform) | ✓ (branch/team structure) | ✓ (FiveStreet lead routing product line) | Standard (deep in team-tier products; trivial in solo) |
| Automated follow-up (action plans / drip / workflows) | ✓✓ (Action Plans per lead source) | ✓ (drip campaigns, checklist triggers) | ✓ (action plans, to-dos) | ✓ (Marketing Autopilot) | ✓ (automated communications) | ✓ (Lead Response plans, dynamic workflows) | Standard |
| Calling/texting/email on the record | ✓ (built-in call/text/email) | ✓ (texting auto-logged) | ✓ (Mojo dialer integration, etc.) | ✓ (platform comms) | ✓ (messages; letter templates) | ✓ (email & SMS) | Standard |
| Embedded transaction/checklist layer | ✗ (integrations; "open system" positioning) | ✓ (checklists, portals) | ✓ (transaction mgmt integrations) | ✓ (Transaction Integration; BackOffice separate) | ✓ (checklist workflows before/during/after sale; chain mgmt) | ✓ (transaction timeline, templates) | Common (5/6 in-product to some depth; packaging varies) |
| Agent performance reporting / brokerage oversight | ✓ (Reporting & Leaderboard category) | ✓ (broker tools, commission reporting) | ✓ (ROI tracking, dashboards) | ✓ (Business Analytics, Vitals) | ✓ (reporting, MI reports, audit trail) | ✓ (activity calendar, reports) | Standard |
| Property/listing data authority external (MLS-class) | ✓ (MLS/IDX/Zillow feeds in) | ✓ (MLS import) | ✓ (MLS updates) | ✓ (IDX/MLS) | ✗ (property records native; portals OUT) | ✓ (MLS integration) | Variant (US=market-data-in; UK=records-native+portal-out) |
| Compliance machinery | ◐ (texting registration documented) | ◐ | ◐ | ◐ | ✓✓ (AML, ID checks, marketing consent, audit) | ◐ | Variant (regional/segment depth) |
| Vendor-run human services on the database | ✗ | ✗ | ✓✓ (Success Assurance lead concierges) | ✓ (marketplace add-ons) | ✗ | ✗ | Vendor-specific |

## Canonical Model (synthesis)

Three jointly-held structures. Removal test applied to each:

### L0 — Defining Invariant (minimal)

1. **The brokerage's client population of record** — persistent identified person/household records (contacts) held as the brokerage's shared working database, not personal address books: each person carries the role(s) they play in the brokerage's business — new lead, buyer/applicant, seller/vendor, landlord/landlord-applicant, past client — is owned by an agent while remaining office-visible, and accumulates the relationship's interaction history (calls, texts, emails, notes, meetings, showings). Remove → personal contact manager / generic address book; the brokerage loses its collective memory.

2. **The property-anchored relationship** — every working relationship is bound to property context: a seller to the property they want listed (their own), a buyer/applicant to their requirements and the matched/saved/tracked properties, both to offers on specific properties. The property — not an abstract product — is the deal's subject matter, and property data is a first-class part of the CRM (fed in from the market's listing databases, or held natively and pushed out to listing venues). Remove → generic CRM: the record no longer says what the business is transacting.

3. **The brokerage pipeline over client relationships** — working clients advance through the brokerage's own stage vocabulary from lead toward closed transaction (new lead → contacted → appointment → shown/matched → listing agreement / offers → under contract → closed; with nurture/past-client states alongside), under agent ownership with brokerage-level visibility, routing, and accountability. Remove → a lead inbox or a static property contact file; the commercial motion is gone.

Jointly-held is load-bearing:
- 1 alone = address book / personal contact software
- 2 without 1 = a listing/property database (the venue's inventory, not a relationship system)
- 3 without 1+2 = generic sales-pipeline software
- 1+3 without 2 = generic CRM (§07 territory)
- 1+2 without 3 = property-flavored contact file with no commercial motion
- 2+3 without 1 = a deal board over anonymous leads

### L1 — Common Mature Structure (standard capabilities)

- Multi-channel lead intake: portal/marketplace inquiries (Zillow-class, portals in UK/AU), IDX/agency websites, landing pages, digital ads, website-visitor identification, open-house sign-in, referrals, past-client and sphere generation; email-inbox processing that turns inquiries into contacts.
- Lead routing & distribution: per-source rules, round-robin/first-to-claim/agent-on-duty, ponds/teams, ISA-first routing, advanced rules on tags/price/area/property identifiers.
- Automated follow-up: action plans / drip campaigns (email/text sequences, to-dos) assigned by source or stage; smart lists / saved segments ("who to follow up with and when"); predictive/activity-based prioritization.
- Native communication: calling, texting (auto-logged), email (auto-logged), templates.
- Property-data integration: market listing database (MLS-class) feeds for listing data, status changes, hot-sheet updates; buyer-side search/matching (saved searches, best-fit matching); market reports/alerts to clients.
- Appointment/showing coordination at activity level (appointments set, showings logged, viewings in the diary).
- Transaction/checklist layer: post-contract checklists (buyer/seller/rental templates), task assignment, client-facing progress portals, timeline stages — depth varies (see Boundaries).
- Team & brokerage machinery: agents, ISAs, team leads, brokers/admins; shared calendars/leads; permissions; lead assignment/distribution; reporting, leaderboards, dashboards; commission reporting (agent-side).
- Mobile apps; duplicate management; import/migration; integrations marketplace.

### L2 — Variant / Optional Structure

- Packaging poles: pure CRM ("open system", integrates out) ↔ all-in-one front office (IDX sites + lead engine + CRM + marketing) ↔ whole-agency platform (UK: sales CRM + lettings + property management + client accounts; US enterprise: + back office commissions/accounting + agent recruitment).
- Property-data direction: US-style — listing authority external (MLS), CRM consumes (MLS import, IDX search, property insights); UK/AU-style — property records native in the agency CRM and pushed out to portals (fields/compliance required before portal push). Both satisfy L0 leg 2; direction is regional/market-structure variant.
- Carrier of progression: stage-per-contact (contact carries the stage; tags carry role) vs separate deal/transaction objects (My Deals, transaction records) vs applicant-status model (UK). All three realizations observed.
- Segment/tier: solo agent (routing trivial) → team (ISA + routing + accountability) → brokerage/enterprise (multi-branch, brands, recruit + back office).
- Regional machinery: US MLS/IDX/Clear-Cooperation-style market structure vs UK vendor-instruction/appraisal vocabulary, portal feeds, AML/ID checks, chain management, lettings/PM modules; texting-compliance registration (US A2P-class) vs UK consent/AML.
- Business model: per-seat subscription; bundled lead-generation services; vendor-run human services (concierge teams) as add-ons.

### L3 — Vendor-specific (research notes only)

- Follow Up Boss: "Smart Lists", "Lead Ponds", "First to Claim", "Action Plans", "Lead Flow" admin page, agent-owned lead duplication, Zillow two-way integration (Zillow group ownership).
- BoomTown: "Success Assurance" (vendor-run Lead Concierges monitoring the database), "Opportunity Wall", "Best-Fit Leads", "Hot Sheet", "HomeSearch Now", package tiers Launch/Core/Grow/Advance/btPRO.
- BoldTrail: "Smart CRM", "Marketing Autopilot", "Lead Engine", "Vitals" performance dashboard, "PropertyBoost", "Leads360", BackOffice (ex-Brokermint) commission/accounting, Recruit (ex-AmpStats agent recruitment).
- Reapit: "Reapit Go", "Bookings", "Client Accounts", "DataWarehouse", "Power Organiser", AppMarket, Ascend release; "appraisal → instruction" vocabulary.
- Wise Agent: "WiseSocial", checklist triggers, referral trees, 2,500-email/day bulk sending.
- Top Producer: "Market Snapshot", "HouseValues", "AI Author", "Smart Targeting", "Follow Up Coach", "FiveStreet" lead routing, 360° Contact View.

## Evidence → Assertion Calibration

- Layer A (direct, official): all observations above are from official vendor surfaces. FUB at help-center depth; others at product-page depth.
- Layer B (cross-product): the L0 legs and the L1 standard list are supported across all/most sampled products (table above).
- Layer C (canonical): the three-leg defining core is the abstraction surviving boundary reasoning; stage names, module names, and packaging differ per product and are not asserted as uniform.
- Precision rule: no numeric limits, time windows, or default settings are claimed beyond what sources state (e.g., Wise Agent's own "2,500 emails per day" is vendor-stated and stays in notes; FUB stage definitions quoted verbatim).

## Historical / Market-Sample Check (§24)

- Paper-era brokerage: client card files held at the office (shared, agent-assigned, buyer/seller/wants recorded), listing boards/card indexes of the agency's own instructions, and an office deal ledger/pipeline — satisfies all three legs with no software. The core does not require MLS, IDX, portals, apps, or automation.
- Veteran software generation: Top Producer (decades-old lineage, still marketed) and Reapit (25+ years, vendor-stated) fit the core; their current marketing is modern but the record/pipeline/matching structure is old.
- Regional: UK applicant–vendor–property model (no MLS dependency), US MLS-consumer model, and franchise/team models all fit. A non-MLS market product (Reapit) proves the MLS feed is implementation, not invariant; the property anchoring itself is the invariant.
- Phone-first/IDX-first patterns of current US products are era-current implementations (L1/L2), not definition.

## Boundary Findings

1. **vs Property Listing Platform (§17, processed 2026-09-09)** — RATIFIED from this side (discharges that pass's forward note "listing-origin seam... ratify at that pass"). The listing platform is the pooled PUBLIC venue of expiring property offers with location-organized discovery, market-state lifecycle, and interest routing; the brokerage CRM is the AGENCY-side system of record for clients and their property-anchored relationships. Listing-origin seam confirmed with this pass's evidence: the agency CRM commonly acts as a listing SOURCE — Reapit FAQ documents property-record fields required "before you push properties onto portals" (records authored in-CRM, pushed out); the US sample shows the mirror flow (MLS import into the CRM; Wise Agent "quickly import listings and link them to your transactions"; Top Agent/FUB/BoomTown MLS/IDX feeds; FUB routes leads by MLS number). Removal test both directions: remove the pooled public venue → the brokerage CRM stands intact (clients, pipeline, property context remain); remove the client/pipeline record → what remains is listing inventory/discovery, i.e., the venue's territory. The REA (AU uploader-feed) evidence cited by the sibling pass was not independently fetched this pass; ratification rests on Reapit/Wise Agent/Top Producer evidence, consistent with the sibling's seam. Note: the US CRM's inbound MLS consumption does NOT contradict the seam — the seam is about who holds the relationship record and where listing records originate for publication, not about data direction.
2. **vs Property Showing Platform (§17, processed 2026-09-09)** — RATIFIED from this side (discharges that pass's forward note "buyer identity appears in showing platforms only as showing participants... ratify the listing-origin + activity-vs-deal seams"). Showing/appointment machinery appears inside brokerage CRMs at ACTIVITY level: FUB stages "Appointment Set"/"Showing Homes" and invitation emails for appointments; Reapit Bookings books viewings "straight into your diary"; BoomTown tracks lead activity. But the showing SCHEDULE's system of record (per-listing rulebook, listing-side gate, access arrangements, feedback loop) is the sibling Type's record; in the CRM the showing is one activity on the client's timeline and one pipeline stage. The CRM's record is the client relationship and its progression — the deal pipeline is not the showing platform's record, exactly as the sibling held. Keep-both on the venue (listing platform) / schedule (showing platform) / relationship+pipeline (brokerage CRM) three-way split.
3. **vs Real Estate Transaction Management (§17, unprocessed)** — the post-contract transaction file (checklists, documents, deadlines, compliance) is a distinct record system; sampled CRMs embed checklist/timeline layers to varying depth (Wise Agent/Top Producer in-product; BoomTown via integrations; BoldTrail via Transaction Integration with separate BackOffice; FUB deliberately "open", integrating out). Held: embedded transaction capability = packaging/common, the transaction's own system of record = sibling Type. Flag for that pass: the brokerage CRM's pipeline stages (Under Contract, Closed) reference the transaction without owning its file.
4. **vs Customer Relationship Management / CRM (§07, processed 2026-09-08)** — family relationship confirmed per that pass's note ("the CRM family shape... is instantiated by domain Types... real-estate-brokerage-crm"). Same four-leg family shape (relationship records, interaction history, progression, shared working) but the domain Type adds the property-anchored invariant (family leg 2's "commercial progression" becomes property-bound) and the brokerage organization shape (agent ownership, ISA routing, branch/team hierarchy, franchise tiers). Keep-both; generic CRM pass already treats domain CRMs as separate directory Types.
5. **vs Lead Management Platform / Lead Generation (§06)** — lead capture/generation products create and sell leads; the brokerage CRM is where leads land, are routed, and become clients. All-in-one platforms bundle lead-gen engines (BoomTown, BoldTrail Lead Engine, Top Producer HouseValues) — bundling, not identity: remove the generation machinery and the CRM legs remain.
6. **vs Account Management CRM (§07)** — past-client/referral nurture is a strong secondary use (FUB recipe "Generate business from your past clients"; Reapit vendor referrals; Top Producer repeat-and-referral focus) but the center of gravity is acquisition-to-close. The past-client database lives in the same record as the acquisition motion.
7. **vs Real Estate Development Management / Real Estate Investment Management (§17)** — different operators (developers, investors) with different objects (projects, assets, funds); a brokerage CRM serves fee-earning agents transacting on other people's properties.
8. **vs Marketing Automation / Email Marketing (§06)** — drip campaigns and market reports are embedded standard capabilities, not the defining center; remove them and the Type stands.
9. **vs Contact Center / Sales Dialer (§07)** — calling is embedded; dialers are integrations (BoomTown+Mojo).

## Uncertainties

- Exact default stage vocabularies beyond FUB are unverified at Tier-1 (FUB's table quoted verbatim; others' stage names only partially visible: "applicant status", "transaction timeline"). Final document therefore describes stages conceptually with FUB's as a documented example-free pattern (no vendor names in the final doc).
- Depth of embedded transaction management per product varies and was only partially observable (product-page depth). Not claimed as uniform.
- Whether the seller-side listing record is authored in-CRM vs consumed from MLS is variant (documented both ways); proportion in market unknown — not asserted.
- BoomTown help center, Reapit support portal, BoldTrail help, Top Producer support not accessed; any operational detail (limits, defaults, states) withheld.
- Open-house sign-in tools: adjacent (FUB website pixel mentions call/text capture; open-house sign-in not directly evidenced this pass) — noted, unasserted.
- The generic-CRM pass listed this leaf under "domain CRMs" pending this research; consistency confirmed.

## Final Synthesis

A Real Estate Brokerage CRM is the brokerage's shared system of record for its client relationships, whose defining core is three jointly-held structures: (1) the brokerage's client/prospect population — persistent person/household records in buyer/seller/applicant/vendor/past-client roles, agent-owned, office-shared, accumulating interaction history; (2) the property-anchored binding — each working relationship bound to property context (a seller's own property/listing, a buyer's requirements and matched/tracked properties, offers), with property data flowing in from the market's listing databases or held natively and pushed out to listing venues; (3) the brokerage pipeline — clients advancing through the brokerage's stage vocabulary from lead to closed transaction under agent ownership with brokerage-level routing and accountability. Standard capabilities cluster around lead intake and routing, automated follow-up, property-data integration, activity-level appointment/showing coordination, embedded transaction checklists, team/brokerage reporting, and mobile work. Regional realizations differ structurally (US market-data-in vs UK records-native-and-portal-out) but satisfy the same core; the paper-era brokerage satisfies it with card files and a deal ledger.
