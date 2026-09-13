# Research Notes — Lead Management Platform

## Research Goal

Understand what a Lead Management Platform (§07 Sales, Customer & Revenue) actually is as an Application Type: what a lead is as a managed object, what the lead lifecycle looks like, what qualification and conversion mean operationally, what distribution/working machinery exists, how the Type is packaged in the market (standalone vs CRM module), and where its boundaries sit against the neighboring Types that share its vocabulary — CRM, Sales Pipeline Management, Opportunity Management, Lead Capture Platform, Lead Generation Platform, Marketing Automation Platform, Sales Engagement Platform, Event Lead Retrieval, Territory Management.

This pass also discharges joint-review flags carried by: lead-capture-platform (§06, 2026-09-07), lead-generation-platform (§06, 2026-09-07), customer-relationship-management-crm (§07, 2026-09-08), marketing-automation-platform (§06, 2026-09-08), sales-pipeline-management (§07, 2026-09-07), opportunity-management (§07, processed), account-management-crm (§07, 2026-09-07), sales-engagement-platform / outreach-sequencing-platform (§07, processed), event-lead-retrieval (§26, 2026-09-07), territory-management (§07, processed).

## Initial Boundary

**Hypothesis (pre-research):** Lead Management Platform = the downstream lifecycle owner of the lead: the system of record for a transient prospect population from intake to disposition (qualification → conversion/disqualification), with routing/assignment and follow-up machinery. Nearest neighbors: CRM (full relationship system of record), Sales Pipeline Management (deal-only slice), Lead Capture (intake mechanism ending at handoff), Lead Generation (supply side ending at delivery), Marketing Automation (nurture execution).

**Known prior-pass positions to ratify:**
- capture pass: "management = downstream lifecycle ownership (qualification/scoring/routing/nurture)"
- generation pass: "management = downstream lifecycle ownership"; marketplace FAQ names the buyer's "lead management system" as the receiving system
- CRM pass: "lead management centers the transient pre-qualification population; CRM holds the full prospect→customer relationship of record, with lead handling as one intake mechanism"; CRM lead-object deliberately NOT definitional (dedicated lead object vs lifecycle-stage vs lead-inbox implementations all documented)
- MAP pass: "lead lifecycle/routing record vs nurture execution producing scoring→handoff as program outcomes"
- sales-pipeline pass: "Leads are unqualified prospects worked for fit and interest; the deal is the qualified commercial unit. The conversion act (lead → deal) is the designed seam; lead qualification and disqualification machinery belongs to the lead side." One sampled product gives leads their own pipeline with a disqualified outcome (Pipedrive LeadBooster).
- opportunity-management pass: "upstream transient pre-qualification population vs the qualified commercial unit; the conversion act (lead→opportunity) is the designed seam"
- account-management-crm pass: "works a transient prospect population toward conversion; the account here is durable across the whole relationship"
- sales-engagement / outreach-sequencing passes: "Lead management spans capture-to-qualification; the platform is the touch-execution instrument within that span, not the qualification record itself"
- event-lead-retrieval pass: "Lead Management Platform / CRM = downstream systems of record for pipeline and relationships; lead retrieval ends at delivering the captured point-of-contact record"
- territory-management pass: "Routing distributes incoming leads in real time using rules that consume the territory structure; it does not maintain the standing coverage structure"

## Research Questions

1. What is a lead as an object? What does the record carry? Is the lead a distinct record class or a stage on a person record?
2. What is the lead lifecycle? What states exist? What does qualification mean operationally?
3. What happens at conversion? What is created, what is transferred, is it reversible?
4. What distribution/assignment machinery exists? Is per-lead ownership mandatory?
5. What working machinery exists (tasks, cadences, response-time discipline)?
6. How do leads enter (sources)? Is multi-source aggregation definitional?
7. Where does scoring sit — definitional or common?
8. How is the Type packaged — standalone products vs CRM modules?
9. Where are the boundaries vs CRM / pipeline / capture / generation / MAP / engagement?

## Representative Products

Selected for market representation, documentation quality, product-philosophy diversity, and customer-tier spread:

1. **Zoho CRM (lead management)** — the classic modular CRM realization; the most complete lead-object documentation (lead status picklist, convert machinery, field mapping). Enterprise/SMB modular pole.
2. **Freshsales (Freshworks)** — SMB CRM with strong lead-management positioning; documented conversion semantics and AI scoring. SMB pole.
3. **Follow Up Boss** — real-estate vertical team lead-management platform; person-record-with-stages implementation; documented Lead Flow routing, Ponds, first-to-claim. Vertical team pole.
4. **LeadSimple** — standalone process-driven lead management for property management/home services; speed-to-lead machinery documented in detail. SMB standalone process pole.
5. **LeadSquared** — high-volume multi-vertical (education admissions, financial services, healthcare, automotive) lead management platform; self-named "Lead Management System" product with a definitional FAQ. High-volume vertical pole.

Structural cross-check: **Frappe CRM** (open-source CRM) documentation used as a sixth structural data point (open-source pole) — deal/lead conversion semantics.

## Sources

| Product | Source | Tier | Date |
|---|---|---|---|
| Zoho CRM | Lead Management product page — https://www.zoho.com/crm/lead-management.html | 2 | 2026-09-10 |
| Zoho CRM | Lead Nurturing product page — https://www.zoho.com/crm/lead-management/lead-nurturing.html | 2 | 2026-09-10 |
| Zoho CRM | Help KB "Converting Leads" — https://help.zoho.com/portal/en/kb/crm/sales-force-automation/leads/articles/convert-leads | 1 | 2026-09-10 |
| Zoho CRM | Help KB "FAQs: Leads Management" — https://help.zoho.com/portal/en/kb/crm/faqs/sales-force-automation/lead-management/articles/faqs-on-leads-management | 1 | 2026-09-10 |
| Zoho CRM | API docs "Convert Lead" v8 — https://www.zoho.com/crm/developer/docs/api/v8/convert-lead.html | 1 | 2026-09-10 |
| Freshsales | Support "How to convert qualified leads" — https://support.freshsales.io/support/solutions/articles/217477-how-to-convert-qualified-leads | 1 | 2026-09-10 |
| Freshsales | Support "How to use contacts" — https://support.freshsales.io/support/solutions/articles/217734-how-to-use-contacts | 1 | 2026-09-10 |
| Freshsales | Support Leads folder — https://support.freshsales.io/support/solutions/160485 | 1 | 2026-09-10 |
| Freshsales | Features page (auto-assignment, Freddy scoring/dedup) — https://freshworks.com/crm/features | 2 | 2026-09-10 |
| Follow Up Boss | Help Center root + Contacts & Lead Profiles category — https://help.followupboss.com/ | 1 | 2026-09-10 |
| Follow Up Boss | "People Overview" — https://help.followupboss.com/hc/en-us/articles/360018115954-People-Overview | 1 | 2026-09-10 |
| Follow Up Boss | "Lead Flow Overview" — https://help.followupboss.com/hc/en-us/articles/360014570494-Lead-Flow-Overview | 1 | 2026-09-10 |
| Follow Up Boss | "Lead Ponds Overview" — https://help.followupboss.com/hc/en-us/articles/360048829034-Lead-Ponds-Overview | 1 | 2026-09-10 |
| Follow Up Boss | Help-center search results (stages, lead routing) | 1 | 2026-09-10 |
| LeadSimple | Homepage — https://www.leadsimple.com/ | 2 | 2026-09-10 |
| LeadSimple | CRM product page — https://www.leadsimple.com/property-management/crm | 2 | 2026-09-10 |
| LeadSquared | Homepage — https://www.leadsquared.com/ | 2 | 2026-09-10 |
| LeadSquared | "Lead Management System" product page — https://www.leadsquared.com/lead-management-system/ | 2 | 2026-09-10 |
| Frappe CRM | Developer docs (lead/deal) — https://docs.frappe.io/crm/deal.md | 1 | 2026-09-10 |
| Prior passes | STATUS.md Boundary Issues entries (lead-capture, lead-generation, CRM, MAP, sales-pipeline, opportunity-management, account-management-crm, sales-engagement, outreach-sequencing, event-lead-retrieval, territory-management) | — | 2026-09-07/08 |

**Source-access limitations:**
- LeadSquared support KB (support.leadsquared.com) unreachable (transport error ×1; abandoned per network rules) — LeadSquared evidence is product-page-level (Tier 2), not help-article-level. Assertion strength reduced accordingly.
- LeadSimple help center (help.leadsimple.com) unreachable (transport error ×1; abandoned) — LeadSimple evidence is product-page-level (Tier 2).
- Zoho help KB articles were reached via search-result excerpts (full-page fetch of the KB article itself not performed); the conversion semantics are corroborated across three independent Zoho surfaces (help KB, API docs, product pages) and match the Freshsales Tier-1 documentation, so the cross-product claim is Layer B.
- No pricing/plan-tier details used; no numeric limits stated.

## Product Observations

### Zoho CRM — lead management (evidence layer A for product-specific, B in aggregate)

- **Lead definition (Tier 1 KB):** "A lead is a prospective customer interested in purchasing your organization's products or services. During the follow-up process, when you reach a certain stage, like a business opportunity with the lead… it can be converted to an account, contact, and deal." Open Leads vs Converted Leads are named list views.
- **Lead record:** one person + one company on one record (Company field mandatory for account creation on conversion); carries Lead Source (attribution), Lead Status (customizable picklist, "industry standard" defaults), Rating, contact + company fields.
- **Conversion (Tier 1 KB + API docs):** Convert action creates Account (if Company name present) + Contact, optionally a Deal; field mapping transfers lead data; **"A lead cannot be reverted once converted"**; converted lead moves to Converted Leads view (copy retained); merge-with-existing account/contact options; duplicate-prevention via Lead Conversion Options API (match existing records before conversion); permission-gated ("Convert Leads permission in profile").
- **Distribution (Tier 2):** assignment by criteria to users/roles/groups, round-robin, AI matching; **assignment limits** ("Set limits on the number of leads they can be assigned and how excess leads should be handled").
- **Scoring (Tier 2):** manual models (engagement, demographic data) or AI (Zia).
- **Capture (Tier 2):** webforms, spreadsheet import, card scanner app, social, live chat; dedup ("Prevent, remove, or merge duplicates"), enrichment, data preparation.
- **Nurture (Tier 2):** Cadences — automated branching follow-up sequences over email/calls/meetings/quotes.
- **Consent (Tier 2):** double opt-in, consent tracking, GDPR/HIPAA compliance surfaces.

### Freshsales (evidence layer A)

- **Conversion semantics (Tier 1):** "When a lead has shown genuine interest in your product, you qualify the lead by converting it to a contact with an account and a deal." On conversion: Contact created by default; Account created if Account name populated (not mandatory); Deal created if Deal name & value populated (not mandatory); **"The Status field takes the value as Qualified lead automatically"**; **"the lead is converted to a contact and ceases to exist under Leads"**; email-match dedup against existing contacts; field mapping incl. custom-field mapping; deal placed into a chosen pipeline at conversion.
- **Traditional process framing (Tier 1):** "If you've a traditional sales process (leads, contacts, accounts and deals), then you can convert your qualified leads to contacts."
- **Lead module (Tier 1 folder):** "How to use leads", "How to automatically add leads", "lead score to prioritize leads", Freddy duplicate detection for leads/contacts.
- **Auto-assignment (Tier 2):** "automatically assigns leads to salespeople across territories, based on lead-routing rules."
- **Scoring (Tier 2):** Freddy AI contact/lead scoring from historical data.

### Follow Up Boss (evidence layer A)

- **Object model (Tier 1):** the People screen is "the central place to see every contact you have access to"; leads are person records carrying a **stage** (custom stages configurable in Admin; stage changes drive automations; named stages include Lead, Nurture, Active, Closed, Lost, Trash). No separate lead object — the lead is a stage on the person record. Deal Tracking is a separate object with its own pipelines/stages.
- **Lead Flow (Tier 1):** "the command center for new web leads to make sure leads are assigned to the correct agents/lenders and the specified action plan automatically runs to initiate communication. Automate everything to increase speed to lead." Per-source setup: assigned agent or group, lender, action plan (drip campaign). Advanced rules: assignment by tags, price, city, state, zip, MLS number, phone number. Lead Flow Delay: hold routing up to a few minutes to aggregate multiple events for the same lead before routing (e.g., wait for a phone number). Direct-to-user routing by lead providers; lead email address as an intake channel.
- **Ponds (Tier 1):** shared unassigned pools — "group those leads into opportunities for your team to actively grab and work"; pond has a "Pond Lead" agent of record; members claim leads from the pond; permissions per role; pond leads excluded from the default People totals. **Confirms per-lead ownership is NOT mandatory — an unassigned shared pool is a first-class state.**
- **First to Claim / Instant Response (Tier 1 section titles):** claim-based assignment and immediate-response machinery exist as named features.
- **Working machinery (Tier 1):** Tasks (quick follow-up tasks, recurring), Call Lists ("rapidly call through leads"), Smart Lists, filters (stage, last communication), mass actions (stage/source/assignment), Lead Deduplication, Merge Contacts, Change Log on lead profile, export gated to owner/admin.
- **Reporting (Tier 1 category):** Reporting & Leaderboard; agent goal reports.

### LeadSimple (evidence layer A for product-specific claims, Tier 2 product pages)

- **Positioning:** "Lead capture, speed-to-lead routing, guided playbooks, and revenue forecasting — a sales CRM built for how property management companies grow." CRM is "the growth layer of the LeadSimple platform"; sits on top of property-management software (AppFolio/Buildium/Rentvine) with two-way sync; won deals trigger an onboarding Process.
- **Speed-to-lead machinery (Tier 2, detailed):** centralized lead capture (portals, web forms, inboxes, call leads sync into one CRM — "nothing lives in a personal inbox"); lead auto-assignment rules per pipeline (by source, market, or round-robin) "the second it lands"; instant follow-up (intro text + email on capture, call task on the rep's queue); **SLA escalation** ("If a lead sits untouched past your SLA, it escalates to a manager automatically"); median speed-to-lead reported as a headline metric.
- **Funnel (Tier 2):** New lead → Contacted → Qualified → Proposal → Won, with counts and conversion per stage; source ROI (deals/win rate/fees won per source); time-in-stage reporting; pipeline-weighted forecasting.
- **Playbooks/cadences (Tier 2):** stage-based playbooks (tasks, scripts, templates per stage), automated cadences incl. "90-day nurtures", shared template library.
- **AI (Tier 2):** AI scoring/qualification ("reads each inquiry, scores it, extracts doors, property type, market"), AI voice agent answering after-hours new-lead calls, answer drafting.

### LeadSquared (evidence layer A for product-specific claims, Tier 2 product pages)

- **Self-definition (Tier 2 FAQ):** "Is lead management part of CRM? Yes — lead management is the part of CRM that happens before a prospect becomes a customer. It covers everything from first inquiry to qualification: capturing leads, scoring them, assigning them to the right rep, and nurturing them until they're ready to buy. A CRM manages the full customer relationship; lead management is what keeps that relationship organized in its earliest, most fragile stage."
- **Leads vs deals (Tier 2 FAQ):** "Leads are potential customers who have shown some interest but haven't yet engaged in a formal sales conversation… Once a lead is qualified and shows clear intent, it becomes a deal. Deals are specific sales opportunities tracked through the sales pipeline."
- **Lead Management System page (Tier 2):** capture from all sources ("website, Meta, Google, channel partners, referrals, and even AI search engines… onto one platform with zero leakage"; online/offline/aggregators); quality & engagement scoring with auto-qualification; **Distribution Engine** ("weighs the rep's availability, current workload, expertise, and performance, and assigns the record instantly. It tracks the SLA on every record it assigns, and the moment one is at risk, it reassigns it to the next best available rep"); lead profiles (contact details, location, source, requirements, funnel stage, full interaction history); lead-account mapping by email domain; multiple industry-shaped pipelines ("Financial services teams track applicants through KYC and underwriting. Education teams move students from inquiry to counseling to enrollment…"); leads inbox ("a central place in your CRM where all new inquiries land… decide which ones are worth pursuing right away"); deal rotting (time limits per stage, flag cold records); nurture lists + omnichannel; sales notifications (task assignment, follow-up reminders, stage changes, overdue alerts); role-based access (SDR/BDR/manager), time-boxed lead access, lead transfer between reps.
- **Positioning:** "Built for lead management, not adapted for it"; high-volume consumer-facing verticals (education admissions, lending, healthcare, automotive dealers).

### Frappe CRM (structural cross-check, evidence layer A)

- **Deal/lead semantics (Tier 1 docs):** "A deal is a qualified opportunity you're actively working to close. It usually starts as a lead. Once you've figured out there's real potential, you convert it into a deal and start tracking it through your pipeline." On conversion: "the contact from the lead becomes the primary contact automatically… all the communication history – emails, calls, comments, moves over to the deal. Nothing gets lost." Lead list and deal list are parallel structures; deal status pipeline configurable.

## Cross-product Comparison

| Structure | Zoho | Freshsales | FUB | LeadSimple | LeadSquared | Frappe | Verdict |
|---|---|---|---|---|---|---|---|
| Lead as distinct pre-customer population | dedicated Lead module | dedicated Lead module | person record + lead stages | Leads workspace + pipelines | lead profiles + leads inbox | lead list | **Core (implementation varies)** |
| Source attribution on the lead | Lead Source field | Source field | lead source (flow-level) | source per lead (Referral/Website/Ads) | source + capture channel | — | **Core (context)** |
| Qualification as managed judgment | Lead Status picklist + convert decision | convert = qualify; status auto "Qualified lead" | stage progression (Lead→…→Active) | Qualified stage in funnel | auto-qualify by score | "figured out there's real potential" | **Core** |
| Conversion act → downstream records | convert → account+contact+deal, irreversible | convert → contact+account+deal, lead ceases to exist | stage move (lead→contact continuum) + separate deals | Won → onboarding trigger → PM sync | lead→deal/opportunity mapping | lead→deal, history carries over | **Core (the designed seam)** |
| Disqualification / recycling | custom Lead Status values (e.g. Closed) | lead remains unconverted | Lost/Trash stages | funnel attrition visible | unqualified leads stay in nurture | — | **Core (named outcome)** |
| Assignment/routing | round-robin, criteria, roles/groups, limits | auto-assignment rules across territories | Lead Flow per-source rules, advanced rules, groups | auto-assignment by source/market/round-robin | Distribution Engine (skill/availability/location/performance/workload) | assignment field | **Common (manual assignment satisfies)** |
| Unassigned shared pool | — | — | Ponds (claim-based) | — | leads inbox (triage) | — | Common (shows ownership not mandatory) |
| Speed-to-lead / SLA | — | — | Instant Response; Lead Flow delay | SLA escalation; speed-to-lead metric | SLA tracking + auto-reassignment | — | Common |
| Scoring | manual + AI (Zia) | Freddy AI lead score | — (not central) | AI score per lead | quality & engagement scoring, auto-qualify | — | Common |
| Follow-up tasks/cadences | Cadences | tasks/appointments | Tasks, Call Lists, Action Plans | playbooks, cadences, call queues | reminders, notifications, nurture lists | tasks | Common |
| Duplicate detection/merge | prevent/remove/merge | email-match at convert; Freddy dedup | Lead Deduplication, Merge Contacts | — (sync dedup "no duplicates found") | "avoid duplicate lead creation" | — | Common |
| Multi-source capture | webforms/import/scanner/social | web library/import/phone | 350+ lead providers, lead email | portals/web forms/inboxes/calls | all sources incl. aggregators | import | Common (capture itself = §06) |
| Population reporting | pipeline/funnel analytics | conversion reports | Reporting & Leaderboard | funnel, source ROI, time-in-stage, forecast | 100+ reports, stage analysis | — | Common |
| Post-conversion records in-product | full CRM | full CRM | deals + long-term contact | onboarding Process + PM sync | accounts + opportunities | deals | Optional/bundled (CRM capability) |
| Vertical pipelines | configurable | configurable | real-estate stages | property-management shaped | industry pipelines (KYC, admissions) | configurable | Variant |

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The lead population of record.** Persistent identified records for prospective buyers in the pre-customer stage — people/organizations who have expressed interest or been identified as prospects — held as a distinct managed working population pending disposition, each carrying contact identity and source/interest context. The population is transient by design: its members are expected to leave it (by conversion or disqualification) rather than accumulate as permanent records. Implementation varies across products: a dedicated lead module (Zoho, Freshsales), a person record with lead stages (Follow Up Boss), a leads inbox/pool (LeadSquared, Pipedrive LeadBooster per the sales-pipeline pass). Remove → a generic contact database or inquiry log with no distinct pre-customer population.

2. **The qualification-and-disposition lifecycle.** Each lead moves through managed states from intake toward a recorded disposition. Qualification is the defining judgment — deciding whether the prospect is sales-ready — expressed as status/stage progression. The lifecycle terminates in named outcomes: **conversion** (the lead's data transfers into the downstream relationship/deal records — contact, account, deal — the designed seam with CRM and pipeline Types; in the classic lead-object implementations the conversion is irreversible and the lead record leaves the lead population) or **disqualification/recycling** (unqualified, lost, nurture). Remove → an inquiry register with no managed disposition.

3. **The distribution-and-working machinery.** Incoming leads are assigned to owners — manually or by rules (round-robin, criteria, territory, workload) — and worked with tracked follow-up (tasks, reminders, activity history, response-time discipline), so the population advances toward disposition rather than aging unworked. Team-scale is the design center: the machinery exists because multiple sellers share one lead flow. Per-lead ownership is not mandatory (FUB Ponds: shared claim-based pools are first-class), but assignment-and-working as a managed discipline is. Remove → a generic task tracker; without it the population is a register nobody works.

**Jointly-held load-bearing:**
- 1 alone = inquiry log / contact segment (no disposition)
- 2 alone = empty lifecycle over nothing
- 3 without 1+2 = generic task queue
- 1+2 without 3 = a lead register nobody works (spreadsheet of inquiries with statuses)
- 1+3 without 2 = routing/follow-up over contacts with no qualification semantics
- 2+3 without 1 = lifecycle machinery over anonymous inquiries

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Rule-based routing engines: round-robin, criteria/territory matching, workload/availability weighting, SLA tracking with auto-reassignment (Zoho, Freshsales, FUB, LeadSimple, LeadSquared)
- Lead scoring: manual rule models and AI/predictive scoring (Zoho Zia, Freshsales Freddy, LeadSquared, LeadSimple)
- Speed-to-lead automation: instant response (auto text/email on capture), first-to-claim, SLA escalation to managers (FUB, LeadSimple, LeadSquared)
- Multi-source capture aggregation: web forms, ads, portals, aggregators, calls, imports into one population (all sampled)
- Duplicate detection and merge (all sampled)
- Follow-up task machinery: tasks, reminders, call lists, overdue alerts (all sampled)
- Cadences/nurture coordination: drip sequences, nurture lists, long-horizon nurtures (Zoho, FUB, LeadSimple, LeadSquared)
- Population-level monitoring: funnel/conversion by stage, source ROI, response-time metrics, time-in-stage, deal-rotting flags (all sampled)
- Lead-account mapping / company grouping (Zoho company field, LeadSquared email-domain mapping)
- Consent/privacy machinery (Zoho double opt-in; LeadSquared compliance posture)
- Role-based access and lead transfer between reps (LeadSquared, FUB permissions)

### L2 — Variant / Optional Structure

- Packaging: standalone lead-management platform (FUB, LeadSimple, LeadSquared LMS) vs lead module inside a CRM (Zoho, Freshsales, Frappe) — the dominant market packaging is the CRM module
- Object realization: dedicated lead object vs person-record-with-stages vs leads inbox/pool
- Vertical pipelines: education admissions (inquiry→counseling→enrollment), lending (KYC/underwriting), healthcare (patient inquiry→appointment), automotive (inquiry→test drive→delivery), real estate (FUB stages)
- Field-force/mobile lead management (LeadSquared mobile CRM, offline day plans)
- AI voice/chat agents handling first contact and qualification (LeadSquared Invorto, LeadSimple AI voice agent) — current-market layer
- Post-conversion depth: full CRM records in-product (Zoho/Freshsales) vs handoff to external systems (LeadSimple → PM software; FUB deals)
- Unassigned shared pools with claim mechanics (FUB Ponds; Pipedrive Lead Pool per prior pass)

### L3 — Vendor-specific (Research Notes only)

- FUB "Ponds" naming and Pond Lead agent semantics; "First to Claim"; Lead Flow Delay (beta, up to 5 minutes)
- Zoho "Zia" AI assistant; "Cadences"; Convert Leads profile permission; "My Converted Leads" view
- Freshsales "Freddy" AI; plan names (Sprout/Blossom/Garden/Estate/Forest)
- LeadSquared "Distribution Engine", "Invorto" voice bot, "Lumen"/"Siera" AI/reporting, "Converse"; INR pricing
- LeadSimple "BDM" (business development manager) role framing; doors/fees vocabulary; PM-software sync set

## Historical / Market-Sample Check (§24)

**Paper-era analog:** the sales manager's inquiry card file — inquiry cards (from ads, trade shows, phone calls) collected in a central register, distributed to salespeople with follow-up dates, status dividers (new / contacted / qualified / lost), and conversion = opening a customer file for the qualified prospect. This satisfies all three L0 legs — lead population of record, qualification-and-disposition lifecycle, distribution-and-working machinery — with zero software, no scoring, no routing engine, no multi-source capture machinery. **Historical check passed.**

**Early-web analog:** form-to-email into a shared inbox, manually triaged and assigned, tracked in a spreadsheet with status columns — legs 1+2 with minimal leg 3. In-type.

**Anti-overfit confirmations:**
- Scoring is NOT definitional: the paper-era and early-web forms satisfy the core without any scoring; even in-sample, FUB's center of gravity is routing/follow-up rather than scoring.
- Rule-based routing engines are NOT definitional: manual per-source assignment (FUB basic setup) and shared unassigned pools (FUB Ponds) satisfy the core.
- Multi-source capture machinery is NOT definitional: single-source intake (one web form) remains in-type; the capture machinery itself belongs to Lead Capture Platform (§06).
- The dedicated lead object is NOT definitional: person-record-with-stages (FUB) and leads-inbox (LeadSquared) realizations documented — matching the CRM pass's finding that lead-object is an implementation variable.
- Irreversibility of conversion is NOT definitional as stated: it is documented for the classic lead-object implementations (Zoho "cannot be reverted", Freshsales "ceases to exist under Leads"), but FUB's stage continuum has no such hard boundary. The canonical statement is "the lead leaves the lead population at disposition", with irreversibility as a common implementation property of the dedicated-lead-object form.

## Vendor-specific Findings

See L3 above. None promoted to the canonical core.

## Boundary Findings

**Removal tests ("去掉什么就变成另一个 Type"):**

| Remove | Becomes |
|---|---|
| the transient pre-customer population binding (keep full relationship records + deals) | Customer Relationship Management / CRM |
| the qualification lifecycle (keep only the deal after qualification) | Sales Pipeline Management / Opportunity Management |
| the lifecycle ownership after intake (keep only capture point → record → handoff) | Lead Capture Platform (§06) |
| the lifecycle ownership (keep only the platform-operated demand surface + delivery) | Lead Generation Platform (§06) |
| the lifecycle record (keep only nurture/cadence execution producing scoring→handoff as program outcomes) | Marketing Automation Platform (§06) |
| the qualification record (keep only touch execution: sequences, dialing) | Sales Engagement Platform / Outreach Sequencing (§07) |
| the standing lifecycle (keep only show-floor badge-keyed capture + delivery) | Event Lead Retrieval (§26) |
| the lead population (keep only the standing coverage structure that routing consumes) | Territory Management (§07) |
| the population's transience (keep durable customer-organization stewardship) | Account Management CRM (§07) |

**Seam dispositions (discharging carried flags):**

1. **vs CRM (§07)** — RATIFIED keep-both, center-of-gravity seam. LeadSquared's own FAQ states the seam from the vendor side: "lead management is the part of CRM that happens before a prospect becomes a customer… A CRM manages the full customer relationship; lead management is what keeps that relationship organized in its earliest, most fragile stage." The CRM pass's structural seam ("transient prospect population vs full relationship system of record") is confirmed from this side with direct evidence. The same products carry both (Zoho/Freshsales lead modules; FUB self-describes as usable "as your CRM") — packaging overlap, not identity. CRM's lead-object-not-definitional finding is mirrored here: the lead population is definitional for THIS Type while being an implementation variable for CRM.
2. **vs Sales Pipeline Management / Opportunity Management (§07)** — RATIFIED keep-both. Lead = unqualified prospect worked for fit and interest; deal/opportunity = the qualified commercial unit. The conversion act (lead → deal/opportunity) is the designed seam; qualification and disqualification machinery belongs to the lead side (confirmed: Freshsales conversion creates the deal; Zoho conversion optionally creates the deal; Frappe "a deal… usually starts as a lead").
3. **vs Lead Capture Platform (§06)** — RATIFIED keep-both. Capture = designed prompts at the business's own touchpoints converting traffic into attributed records, ending at handoff; management = the lifecycle after intake (qualification, scoring, routing, working, conversion). The capture pass's discriminator is confirmed; the generation pass's note that the marketplace FAQ names the buyer's "lead management system" as the receiving system is consistent.
4. **vs Lead Generation Platform (§06)** — RATIFIED keep-both. Generation = platform-operated demand surface supplying lead records, ending at delivery; management = downstream lifecycle ownership. LeadSquared's capture-from-aggregators feature shows the supply→management handoff inside one suite (bundling, not identity).
5. **vs Marketing Automation Platform (§06)** — RATIFIED keep-both. MAP = nurture execution producing scoring→MQL→handoff as program outcomes; lead management = the lead's lifecycle/routing record of ownership. In-suite the MAP produces the scored handoff; the lead management layer receives and owns the record thereafter. LeadSquared bundles both (Marketing Suite + LMS) — packaging.
6. **vs Sales Engagement Platform / Outreach Sequencing (§07)** — CONFIRMED from this side. The engagement platform is the touch-execution instrument within the capture-to-qualification span; the qualification record and lifecycle ownership remain here. LeadSquared's built-in dialer/sequences are bundled execution inside a lead-management-centered product.
7. **vs Event Lead Retrieval (§26)** — CONFIRMED keep-both. Retrieval is badge-keyed show-floor capture ending at delivery into "Lead Management Platform / CRM" — the downstream destination named by that pass is this Type.
8. **vs Territory Management (§07)** — CONFIRMED. Routing rules consume the territory structure; territory management holds the standing coverage structure. Freshsales "auto-assignment… across territories, based on lead-routing rules" shows the consumption direction.
9. **vs Account Management CRM (§07)** — CONFIRMED. Transient prospect population worked toward conversion vs durable customer-organization record stewarded across the whole relationship.

**Taxonomy tension recorded (not a directory change):** the market label "lead management" is heavily CRM-module-dominated — searching the category surfaces mostly CRM lead modules (Zoho, Freshsales, HubSpot, Salesforce) rather than standalone products; standalone poles exist (FUB, LeadSimple, LeadSquared's LMS product). The leaf is defined by the lead-lifecycle-of-record structure, which both packagings realize. This mirrors the account-management-crm precedent (keep-both on center of gravity). Additionally, "lead management platform" is traded by routing-only tools (instant lead routing + meeting booking) — a capability slice within this Type's distribution leg, not the whole Type.

## Uncertainties

- LeadSquared and LeadSimple evidence is product-page-level (Tier 2); their help-center operational details (exact stage vocabularies, rule mechanics) are unverified. Claims about these two products are kept at positioning/feature level.
- Zoho help KB articles were verified via search excerpts corroborated across three Zoho surfaces; full-page fetch not performed.
- Pipedrive LeadBooster's lead pool/inbox semantics are carried from the sales-pipeline and opportunity-management passes (their Tier-1 evidence), not re-fetched here.
- Whether a pure routing-only product (instant distribution + scheduling, no lifecycle record) should be a separate leaf is left open — recorded as a possible future boundary question; no directory change made.
- The exact prevalence of "unassigned shared pool" as a first-class structure across the wider market is unverified (documented in FUB Ponds and Pipedrive; not evidenced in Zoho/Freshsales docs fetched).

## Final Synthesis

A Lead Management Platform is the selling organization's system of record for its **pre-customer prospect population**: the lead lifecycle from intake to disposition. Its world is built from three jointly-held structures: the lead population of record (persistent identified prospect records carrying contact identity and source/interest context, held as a distinct working population pending disposition — realized as a dedicated lead module, person-record stages, or a leads inbox), the qualification-and-disposition lifecycle (managed states from intake toward recorded outcomes — qualification as the defining judgment, conversion transferring the lead into contact/account/deal records as the designed seam with CRM and pipeline machinery, disqualification/recycling as the named alternative), and the distribution-and-working machinery (assignment/routing to owners — manual or rule-based — plus tracked follow-up work and response-time discipline so the population advances rather than ages). Everything else widely associated with lead management — scoring, routing engines, speed-to-lead automation, multi-source capture, cadences, duplicate handling, funnel analytics, AI qualification — is mature-but-not-definitional. The paper-era inquiry card file satisfies the core. The center of gravity (the transient pre-qualification population as the managed object) separates it from CRM (full relationship of record), Sales Pipeline/Opportunity Management (the qualified deal), Lead Capture (intake ending at handoff), Lead Generation (supply ending at delivery), Marketing Automation (nurture execution), and Sales Engagement (touch execution).
