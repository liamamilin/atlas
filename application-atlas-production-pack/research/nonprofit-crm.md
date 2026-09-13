# Research Notes — Nonprofit CRM

## Research Goal

Understand what a "Nonprofit CRM" really is as an Application Type: what objects it manages, what its defining structure is (vs. adjacent Types), how the term maps onto the real market, and how the sample's products realize it across customer tiers and product philosophies.

This pass also carries three inherited flags to discharge:

1. **From the donor-management-system pass (§25, processed 2026-09-07)**: term collision — the market calls donor databases "nonprofit CRMs"; candidate outcomes were "donor management as the donor-centered sibling of Nonprofit CRM (parallel to church-giving vs ChMS) or consolidation view"; this pass was asked to claim the nonprofit usage of "CRM" and record the shared family shape.
2. **From the constituent-relationship-management pass (§24, processed)**: "constituent relationship management" is the standard term in both government software and nonprofit/advancement software; the government pass scoped its leaf to government and recommended that this pass explicitly claim the nonprofit usage of the term and record the shared family shape (person-centric records + interactions + engagement workflow) with the relationship-semantics seam (service vs giving).
3. **From the customer-relationship-management-crm pass (§07, processed 2026-09-08)**: family note — the CRM family shape (person-centric records + interaction history + progression toward outcomes) is instantiated by domain Types; nonprofit-crm expected to claim the nonprofit usage per the constituent-relationship-management pass's recommendation.

## Initial Boundary

Hypothesis at start:

- Core use: a nonprofit/mission-driven organization manages its relationships with the people who support and participate in its mission — donors, members, volunteers, event participants, prospects — in one shared organizational database.
- Primary users: fundraising/development staff, membership and volunteer coordinators, communications staff, executive directors.
- Nearest neighbors (dense seam, §25 is heavily subdivided): Donor Management System, Nonprofit Management Platform, Online Donation Platform, Fundraising Management Platform, Volunteer Management System, Membership/Association Management, Nonprofit Case Management, Church Management System; plus the two cross-reference Types: generic CRM (§07) and Constituent Relationship Management (§24, government).
- Likely key question: is "Nonprofit CRM" just a market label for donor management software, or a genuinely broader structure?

## Research Questions

1. What is the central record? What population does it cover (donors only, or donors + members + volunteers + participants + served people)?
2. What accumulates on the record (gifts, interactions, participation)? Is the giving record definitional or the dominant act class of the current realization?
3. What relationship work does the product drive from the record (segmentation → outreach → cultivation → acknowledgment)?
4. What distinguishes this from generic sales CRM — is there a deal/pipeline, and what plays its role?
5. What is the workflow lifecycle (import/migrate → record → segment → communicate → acknowledge → report)?
6. Which capabilities are common mature structure vs. optional/variant (case, grants, advocacy, online giving, CMS/website integration)?
7. How do the market's self-labels ("CRM", "donor management", "constituent relationship management") map to the structures?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Self-label | Evidence level |
|---|---|---|---|
| CiviCRM | open-source full constituent suite | "constituent relationship management (CRM) system built by and for nonprofit organizations and NGOs" | Tier-1 (official user guide, 2 pages fetched) |
| Bloomerang | donor-retention-focused SaaS platform | "Nonprofit Software for Fundraising, CRM & Volunteers"; FAQ equates "donor management (CRM)" | Tier-1 (official site + FAQ) |
| Little Green Light | small-org value SaaS | "all-in-one donor management software" (constituent vocabulary throughout) | Tier-1 (official site + features page) |
| Neon CRM | mid-market all-in-one SaaS suite | "nonprofit CRM" (market anchor only) | UNREACHABLE this pass (403 + transport error) |
| Salesforce Nonprofit Cloud / NPSP | enterprise CRM-platform-adapted | market anchor only | UNREACHABLE this pass (404; matches prior Salesforce 403 findings) |

## Sources

- https://civicrm.org/ — CiviCRM home (positioning, feature index, stats) — fetched 2026-09-08
- https://docs.civicrm.org/user/en/latest/ — CiviCRM User Guide index — fetched 2026-09-08
- https://docs.civicrm.org/user/en/latest/introduction/what-is-civicrm/ — "What is CiviCRM?" — fetched 2026-09-08
- https://bloomerang.co/ — Bloomerang home + FAQ — fetched 2026-09-08
- https://www.littlegreenlight.com/ — LGL home (positioning, pricing by constituent count, region restriction) — fetched 2026-09-08
- https://www.littlegreenlight.com/features/ — LGL features page — fetched 2026-09-08
- Neon CRM (neoncrm.com + help.neoncrm.com) — FAILED (403, transport error ×1) — abandoned per retry rule
- Salesforce (salesforce.com/nonprofits/) — FAILED (404; consistent with prior passes' Salesforce 403s) — abandoned

## Product Observations

### CiviCRM (open-source constituent suite) — Evidence layer A

- Self-definition (What is CiviCRM?): "a powerful, web-based constituent relationship management (CRM) system built by and for nonprofit organizations and NGO's". Home page: "Open source constituent relationship management for non-profits, NGOs and advocacy organizations"; "more than 14,000 non-profits" use it; aggregate stats: 189M contacts, 116M donations, 24M event participants managed across sites.
- Explicitly distinguishes itself from an address book: "CiviCRM is more than just an address book" — the docs' own analogy: an address book that records every interaction, lets you ask "What were my interactions with X?", target messages to specific groups, observe reactions, and adjust the next interaction.
- **Simplest setup** (docs' own words): record basic contact info; define relationships between contacts; send emails; keep a record of interactions with contacts. This is the docs' own minimal core — contacts + relationships + activities + communication.
- **Components** (modular): CiviContribute (contributions, contribution pages/forms, offline fundraising, manual entry, receipts & thank-you letters, soft credits, accounting integration, payment processors, pledges), CiviEvent (events, online/manual registration, participant tracking), CiviMember (memberships, levels/price sets, renewals, cancelling/expiring), CiviCampaign (campaigns, surveys, GOTV voter tracking, petitions), CiviCase (case management), CiviGrant (grant management), CiviMail (mass mailings, scheduled reminders, A/B testing, tokens/mail-merge), SMS, postal mail.
- Data organization: Contacts; Groups and tags; Smart groups (dynamic segments); Activities; Relationships; Custom fields; Profiles; Deduping and Merging; Undelete. Searching: SearchKit with saved search displays; CiviReport reporting.
- Multi-user: "web-based, which means it can be accessed by many users at the same time from different locations"; permissions and access control chapter; change logging.
- Website integration: works with a CMS (Backdrop, Drupal, Joomla, WordPress); "Visitors to your website can carry out many activities on their own, such as renewing their membership, signing up for events, requesting email updates, and donating money".
- Sector vocabulary: communications, community engagement, activism, outreach, donor management — all named as goals. Mission-support language, zero sales/deal vocabulary.

### Bloomerang (donor-retention SaaS platform) — Evidence layer A

- Positioning: "Nonprofit Software for Fundraising, CRM & Volunteers"; title copy: "Bloomerang's fundraising tools and CRM help you acquire and manage donors and volunteers effectively."
- FAQ: "Bloomerang is a nonprofit software platform that combines fundraising tools, donor management (CRM), and volunteer engagement into one unified system to help organizations grow their impact." — **the product equates "CRM" with "donor management" and bundles volunteers**.
- Product lines: Bloomerang Fundraising ("Raise more"), Bloomerang CRM ("Engage more. Keep donors close to the cause with meaningful outreach at the right time. Increase retention, major gifts, and all-around impact."), Bloomerang Volunteer ("Recruit more... recruit, organize, and engage volunteers").
- Data framing: "Get a 360-degree understanding of donors, prospects, and volunteers"; customer quote: "donors, volunteers, and fundraising—into one unified platform... a single place where we can see the full picture of engagement... better steward our supporters."
- Philosophy pole: donor retention ("2.5X first-time donor retention" claim), growth of supporter base, gift size.
- Audience: "built for nonprofits of all sizes" (local orgs to United Way / Habitat / Boys & Girls Club).
- Includes online payment acceptance breadth (cards, ACH, wallets) inside the platform.

### Little Green Light (small-org value SaaS) — Evidence layer A

- Positioning: "Donor Management Software for Nonprofits"; "all-in-one donor management software"; "Illuminating Data. Advancing Nonprofits." — does NOT self-label CRM; uses **constituent** vocabulary pervasively ("manage 1,000 or 100,000 constituents"; pricing tiers by constituent record count).
- Constituent Management feature: "Manage all your organization's supporters (donors, volunteers, members) in one place" — **even the donor-labeled pole defines the record base as donors + volunteers + members**.
- Essential features: Import & Export Data (migration as first-class); Customizable Dashboard (alerts, real-time fundraising totals); Constituent Management; List Creation & Management ("Search and save information into easy-to-use lists for mailings, reports, and more"); Contact Management ("Track all communications (mailings, emails, meetings) and manage calendar of tasks"); Built-In & Custom Reporting; Donor/Fundraising Management ("Store all gifts and track all fundraising efforts"); Acknowledgments/Receipts ("Quickly produce thank you's right inside"); Built-In Integrations (email marketing, accounting, prospect research); Generate Customized Mailings (mail-merge letters, labels, envelopes, tracked who received them); online donation collection synced to records.
- Advanced features: Constituent Coding (tags/groupings); Major Gifts ("Steward prospects by setting and managing a series of tasks"); Event Tracking (invitees, attendees, donations); Document Storage on constituent records; Data Segmentation ("send personalized solicitations and mailings"); Scheduled Reports; Data Maintenance ("Manage duplicates, perform bulk updates and edits"); Volunteer Management ("Manage volunteer interests and hours served by task"); Membership Management ("Easily manage active and lapsed members, their levels, and renewal dates"); Grant Proposals ("Track grant requests; manage set of tasks from ask to completion"); Alumni Management (class lists, class year); Data Analysis ("increased giving opportunities, new donor prospects"); Account Customization (custom fields, hide system fields).
- Migration framed as a 3-step first-class workflow (prep → upload & map → review & save).
- Region variant: service refused to organizations in EU/UK/Switzerland (banner).
- Integrations: Stripe, PayPal, QuickBooks, Zapier, Constant Contact, Mailchimp.

### Neon CRM / Salesforce Nonprofit Cloud — no first-hand evidence this pass

- Both unreachable (Neon: 403 + transport error; Salesforce: 404). Recorded as market anchors only: Neon is widely positioned as a mid-market all-in-one nonprofit CRM; Salesforce Nonprofit Cloud/NPSP is the enterprise CRM-platform-adapted pole (the generic-CRM pass, which also could not reach Salesforce help, documented the generic CRM structure structurally). **No precise claims from these two are made in this pass.**

## Cross-product Comparison

| Structure | CiviCRM | Bloomerang | LGL | Evidence |
|---|---|---|---|---|
| Constituent records covering donors + members + volunteers (+ prospects/participants) | contacts (189M managed); relationships; groups | "donors, prospects, and volunteers"; "donor management (CRM)" | "supporters (donors, volunteers, members) in one place" | A×3 |
| Cumulative relationship history on the record | "keep a record of your interactions"; activities; contributions | "full picture of engagement" | "Track all communications"; gifts stored; hours; events | A×3 |
| Segmentation → outreach → record loop | groups/tags/smart groups; CiviMail; mail-merge; scheduled reminders | "meaningful outreach at the right time" | lists; segmentation; tracked mail-merge; tasks | A×3 |
| Gift/contribution recording + acknowledgment | CiviContribute; receipts & thank-yous; soft credits | Fundraising line; payments in-platform | "Store all gifts"; Acknowledgments/Receipts | A×3 |
| Membership tracking (levels, renewals, lapse) | CiviMember | not directly observed this pass | "active and lapsed members, their levels, and renewal dates" | A×2 |
| Volunteer tracking | via components/extensions (not in fetched core pages) | Bloomerang Volunteer product line | "volunteer interests and hours served by task" | A×2 |
| Event participation tracking | CiviEvent (24M participants stat) | not directly observed | Event Tracking (invitees, attendees) | A×2 |
| Major-gift cultivation as task series | — (not in fetched pages) | "Increase retention, major gifts" | "Steward prospects by setting and managing a series of tasks" | A×2 |
| Dedupe/merge discipline | Deduping and Merging | not directly observed | Data Maintenance ("manage duplicates") | A×2 |
| Import/migration as first-class workflow | importing/exporting chapters | — (not directly observed) | 3-step migration; import/export essential | A×2 |
| Online donation capture writing back to records | CMS integration; contribution pages | payment acceptance in-platform | LGL Forms + Stripe/PayPal sync | A×3 |
| Reporting/dashboards, scheduled | CiviReport; dashlets | insights framing | Built-In & Custom Reporting; Scheduled Reports; dashboard | A×3 |
| Email-marketing/accounting/prospect-research integrations | CiviMail; accounting integration | — (not directly observed) | named essential feature + integrations | A×2 |
| Case / grants / advocacy machinery | CiviCase, CiviGrant, CiviCampaign/petitions (components) | — | Grant Proposals (received side) | A×2 (aspirational breadth = the suite pole) |
| Deal/pipeline object as organizing center | ABSENT (no sales vocabulary) | ABSENT | ABSENT | A×3 — the shared negative |
| Self-hosted vs SaaS deployment | self-hosted/hosted partners | SaaS | SaaS | A×3 (as variant) |

### Key synthesis observations

1. **The record base is broader than donors in every product's own words** — even the two products that market themselves as donor management define the managed population as "donors, prospects, and volunteers" (Bloomerang) / "supporters (donors, volunteers, members)" (LGL) / contacts of every kind (CiviCRM). The "Nonprofit CRM = donor database" reading understates what the products actually structure.
2. **No deal/pipeline.** The CRM-family "managed commercial progression" leg is absent across the sample; its role is played by support acts (gifts, memberships, volunteer commitments, participation) and by stewardship work (acknowledgment, cultivation task series). This is the load-bearing difference from generic CRM.
3. **Giving is the dominant act class** (contributions are the biggest machinery in all products; CiviCRM's own stats: 116M donations vs 24M event participants) but not the only in-type act class.
4. **The stewardship loop is the workflow center**: segment (groups/lists/tags) → communicate (mail-merge, email, postal) → record (activities, tracked sends, acknowledgments) → cultivate (task series) → review (reports). All three products articulate this loop in their own vocabulary.
5. **Terminology mapping is messy and itself evidence**: CiviCRM claims the full term "constituent relationship management"; Bloomerang equates "CRM" with "donor management"; LGL avoids "CRM" entirely while carrying constituent vocabulary. The market label "nonprofit CRM" is applied to the whole spectrum.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

The nonprofit/mission-driven organization's shared system of record for its supporter relationships. Jointly-held structures:

1. **Constituent records of record** — persistent, individually identified records for the people (and organizations/households) the organization engages as supporters of its mission — donors, members, volunteers, event participants, prospects — held as shared organizational records, not a personal address book.
2. **Cumulative relationship history attached to each record** — support acts and interactions (gifts, communications, participation) accumulating over time on the record — the organization's memory of each relationship, surviving staff turnover. Act classes follow the organization's engagement programs; giving is the dominant class in current market realizations but not the definitional one (historical check: paper-era supporter card files + gift ledgers satisfy the core).
3. **Relationship work driven from the record** — segment the supporter base (groups/lists/saved searches) → act on segments (outreach, acknowledgment, cultivation) → record outcomes back on the records. The record is worked, not just stored.
4. **Mission-support semantics** — the relationship being worked is support of the organization's mission (giving, membership, volunteering, participation, advocacy), not a commercial sale; no deal/pipeline object as the organizing center.

Load-bearing test: (1) alone = contact directory/mailing list; (2) alone = activity/gift ledger; (3) without 1+2 = outreach tool with no memory; 1+2 without 3 = passive archive (the spreadsheet pre-history); 1+3 without 2 = list with no relationship memory; without (4) = generic sales CRM (deals) or government service CRM.

### L1 — Common Mature Structure

- gift/contribution machinery as the dominant act class (entry + online capture writing back + acknowledgment/receipts)
- segmentation machinery (groups, tags, saved/dynamic lists)
- communications with tracking (email, mail-merge letters/labels, tracked sends)
- fundraising campaign/appeal coding and reporting
- event participation tracking
- volunteer interest/hours tracking
- membership tracking (levels, renewals, lapsed)
- major-gift cultivation as task series/moves
- reporting/dashboards, scheduled reports
- dedupe/merge + bulk data maintenance; import/export/migration as first-class
- custom fields/account customization; households and inter-constituent relationships
- integrations: email marketing, accounting, payment processors, prospect research
- multi-user web access with permissions (universal in the current sample, but implementation-era: a one-person paper office still fits L0)

### L2 — Variant / Optional Structure

- case management component (service-delivery organizations) — CiviCase
- grant tracking (received — LGL grant proposals; granted — CiviGrant)
- advocacy machinery (campaigns, petitions, GOTV) — advocacy orgs
- online donation pages / peer-to-peer fundraising / website-CMS self-serve integration
- alumni/advancement orientation (schools)
- deployment: self-hosted open source vs SaaS; hosted-partner ecosystems
- regional availability (LGL refuses EU/UK/CH)
- pricing models (by constituent count, unlimited users, platform bundles)
- household-level giving attribution / soft credits (CiviCRM soft credits A-evidenced; household handling A-evidenced at LGL)

### L3 — Vendor-specific (research notes only)

- CiviCRM component names (CiviContribute/CiviEvent/CiviMember/CiviMail/CiviCase/CiviGrant/CiviCampaign), SearchKit, Spark hosting, aggregate stats, CMS integrations (Drupal/WordPress/Joomla/Backdrop)
- Bloomerang retention marketing claims (2.5X first-time donor retention, 37% gift size), "Giving Platform" naming, product trio naming, pricing figures
- LGL pricing tiers and prepay discounts, 30-day trial, 3-step migration branding
- Neon/Salesforce specifics — unreachable, nothing recorded

## Vendor-specific Findings

See L3. One cross-cutting note: Bloomerang's self-equation of "CRM" = "donor management" is a positioning fact about that vendor, not a definition of the Type; CiviCRM's "constituent relationship management" self-description is the sector's full-term claim.

## Boundary Findings

1. **vs Donor Management System (§25 sibling, processed 2026-09-07)** — DISCHARGES that pass's flag. Verdict: **keep-both, donor management as the donor-centered specialization, Nonprofit CRM as the broader Type that claims the sector's CRM term.** The two L0s share the family shape; donor management's L0 additionally requires the attributed gift record + cumulative giving history as definitional content (the money engine as the center), while Nonprofit CRM's L0 holds the constituent relationship machinery with act classes open (gifts dominant). Market evidence for the collision is first-hand: Bloomerang FAQ = "donor management (CRM)"; LGL = donor-management label with constituent breadth; CiviCRM = constituent relationship management label with component breadth. The market label "nonprofit CRM" is applied across this whole spectrum; the Type documented here is the fuller sense the term also names. Overlap is heavy and real — the same products realize both — so this is a center-of-gravity seam, not an object-level line.
2. **vs Constituent Relationship Management (§24, government, processed)** — claims the term from the nonprofit side as that pass recommended. Shared family shape: person-centric records + interaction history + engagement workflow. Seam = relationship semantics: mission support (giving/membership/volunteering/participation) vs public service delivery by an agency. Keep-both.
3. **vs Customer Relationship Management / CRM (§07, processed 2026-09-08)** — keep-both as the nonprofit domain instantiation of the CRM family shape; consistent with that pass's family note. One load-bearing leg transformed: managed commercial progression (deals/opportunities toward closed-won/lost) → mission-support acts + stewardship. Removing leg 4 from either side collapses into the other's territory (deals appear → generic CRM; support-act semantics with no commercial progression → this Type).
4. **vs Membership Management System / Association Management System (§25 siblings)** — membership lifecycle (join/renew/benefits/chapters) is the center there; membership appears in Nonprofit CRM as one act class on the constituent record (LGL membership features; CiviMember). For member-centric orgs where the membership program IS the relationship, the sibling Types fit better. Keep separate; expect overlap at membership-heavy nonprofits.
5. **vs Volunteer Management System (§25 sibling)** — volunteer scheduling/engagement machinery is the center there; volunteers appear in Nonprofit CRM as a supporter class with interests/hours recorded (LGL, Bloomerang product line). Keep separate.
6. **vs Nonprofit Case Management (§25 sibling, processed 2026-09-08)** — the casework episode (client under an organization-defined program, accountable caseworker, closure) is the center there; served clients appear in Nonprofit CRM at most as a constituent class (CiviCase is an optional component, not the core). Consistent with that pass's boundary (donor CRM/contact database as the negative case for casework).
7. **vs Online Donation Platform / Fundraising Management Platform (§25 siblings, per donor pass)** — donor-facing collection flow vs organization-side record system; online giving pages here exist as capture surfaces writing back into the record system.
8. **vs Nonprofit Management Platform (§25 sibling)** — the broader umbrella suite (accounting, programs, events, etc.); Nonprofit CRM is the relationship spine that umbrella platforms include. This leaf is the relationship-centric Type.
9. **vs Church Management System / ChMS (§25 sibling)** — congregational variant of the same family with parish-life semantics (members, pastoral care, worship); the general nonprofit Type does not require congregational objects. Church products straddle; boundary = center of gravity.
10. **Below-Type boundary**: a pure contact/mailing-list tool (import + list + send, no support-act recording) fails leg 2+3 and is below the Type.

### "Remove one thing" tests

- Remove constituent breadth (keep only donors + gifts) → Donor Management System.
- Remove support semantics, add deals/pipeline → generic CRM.
- Remove relationship work (segment/outreach/cultivate) → passive supporter archive / spreadsheet pre-history.
- Remove the shared organizational record (personal use) → personal address book / contact manager, not a nonprofit CRM.
- Remove history accumulation → outreach list with no memory.

## Historical / Market-Sample Check (§24)

- Paper-era charity office: supporter card file (persons, households, organizations) + gift ledger with attributed gifts + correspondence log + acknowledgment letters + membership rolls with renewals + committee/volunteer rosters + mailing lists — satisfies all four L0 legs at analog level. The definition names no cloud, email, online donations, dashboards, or any modern machinery.
- Spreadsheet era (Excel donor lists + mail-merge in a word processor) satisfies legs 1–2 and partially 3; the products' own marketing ("consolidate your spreadsheets" — LGL) names this as the pre-history the Type digitized.
- No era-, region-, or vendor-specific pattern is baked into L0: deployment (SaaS/self-hosted), channel set (email/postal/SMS), act-class mix, and regional availability are all held at L2.

## Uncertainties

1. Neon CRM and Salesforce Nonprofit Cloud/NPSP could not be verified first-hand (403/404). The five-pole market picture therefore rests on three directly evidenced products + the prior generic-CRM pass's structural Salesforce evidence. Claims in the final document are calibrated accordingly; no precise Neon/Salesforce facts are stated.
2. Whether the market would ever produce a "nonprofit CRM" with NO gift recording at all is untested — every sampled product carries contribution machinery. Gifts are held as the dominant act class (L1) rather than L0 precisely because of this uncertainty; if later evidence shows gifts are universal AND definitional, the L0/L1 boundary with donor management may need re-examination (would push toward alias with donor-management-system).
3. Household/soft-credit machinery is A-evidenced for CiviCRM (soft credits) and LGL (household handling blog) but not directly observed at Bloomerang this pass; held at L2.
4. Volunteer-hours tracking at CiviCRM sits in extensions (not fetched core pages) — breadth claim for volunteers rests on LGL + Bloomerang (A×2).

## Final Synthesis

A Nonprofit CRM is the mission-driven organization's shared system of record for its supporter relationships: identified constituent records covering everyone the organization engages (donors, members, volunteers, participants, prospects), cumulative relationship history accumulated on those records, relationship work (segment → reach out → acknowledge → cultivate) driven from and recorded back onto the records, with the relationship being support of the mission rather than a commercial sale. The CRM family shape (records + history + progression + shared work) is instantiated with support-act semantics replacing the deal pipeline. In the current market the term "nonprofit CRM" is most often applied to donor/fundraising-centric systems (the dominant realization), but the products themselves — across every sampled pole — structure a supporter base broader than donors, which is the sense of the term this Type claims. Donor Management System is the donor-centered specialization; Constituent Relationship Management (government) shares the family shape with service-delivery semantics; generic CRM (§07) shares the family shape with commercial-progression semantics.
