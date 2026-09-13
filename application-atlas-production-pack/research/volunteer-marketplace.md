# Research Notes — Volunteer Marketplace

Research date: 2026-09-09
Leaf: Volunteer Marketplace (DIRECTORY.md §25 Nonprofit, Membership & Religious Organizations)
Slug: volunteer-marketplace

## Research Goal

Understand the "Volunteer Marketplace" Application Type from real products: what the venue is, who participates, what objects exist inside it, how the two sides (volunteers seeking opportunities, organizations seeking volunteers) meet, what the venue operator does versus what the posting organization does, and where the boundary lies against the already-processed sibling Volunteer Management System (§25) and the umbrella Service Marketplace (§05.02).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a two-sided venue operated for many independent organizations to publish volunteer opportunities and for many individual volunteers to discover and respond to them. The venue operator is distinct from the posting organizations.
- Nearest neighbors: Volunteer Management System (one organization's program system of record — already processed 2026-09-09, left a forward flag for this pass), Service Marketplace (§05.02 umbrella — already recorded volunteer as a domain-structured sibling), Job Board (paid work), Listings Platform / Directory (static listing surfaces), Nonprofit Event Management (event-shaped opportunities).
- Known unknowns at start: whether "marketplace" products are a distinct category or just a deployment shape of volunteer management software; whether exchange-based (work-for-lodging) and booking-based (volunteer travel) platforms belong in-type; how the Rosterfy "Volunteer Passports" blur point resolves.

## Research Questions

1. What is the unit of supply on the venue? (opportunity listing — what fields, what lifecycle)
2. Who may post? (organization admission, eligibility rules, approval)
3. How do volunteers discover? (search/filter dimensions, account requirements)
4. How does the response/connection work? (venue-hosted application vs external handoff; what happens after)
5. What does the venue operator govern vs what does the posting organization own? (screening, communication, selection)
6. How is the venue monetized? (org-side fees, membership, licensing, API)
7. How does inventory leave the venue? (embeds, widgets, API syndication)
8. Where is the VMS/marketplace seam, and does the Rosterfy Volunteer Passports blur point collapse the two Types?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| Idealist (incl. VolunteerMatch) | independent venue operator; consumer + nonprofit marketplace; the merged successor of the archetypal US volunteer marketplace | marketplace-native pole; deep Tier-1 help documentation |
| Rosterfy (Volunteer Passports) | enterprise volunteer management software deployed as an institution-hosted community venue (city/government as connector) | the blur point flagged by the volunteer-management-system pass |
| TeamKinetic | UK volunteer management platform whose customer set includes volunteer centres and city councils hosting shared community portals | institution-hosted venue substrate; UK/regional pole |

Products attempted and abandoned per the source-access rule (failures recorded in Sources): Catchafire (skills-based project marketplace), Volunteer World (volunteer-travel booking marketplace), Workaway / HelpX (exchange-based host marketplaces), Golden, JustServe, Volunteer.gov. These poles are therefore NOT evidenced from official documentation this pass; claims about them are degraded to "market forms exist" without operational detail.

## Sources

### Reached (Layer A evidence)

- Idealist / VolunteerMatch (merged early 2025; volunteermatch.org now redirects to idealist.org):
  - https://www.volunteermatch.org/help (redirects to Idealist; confirms merger)
  - https://www.idealist.org/ (homepage: search across Jobs / Internships / Volunteer Opportunities / Events / Organizations; "Post a Free Volunteer Opportunity"; "100,000+ unique ways to volunteer"; "more than 200,000 organizations"; radius presets; popular searches "Board member", "Data analyst")
  - https://www.idealist.org/en/help (Help Desk index: Searching / Posting / Account & User Settings / Email Alerts / Report A Problem / Using Idealist / community guidelines)
  - https://www.idealist.org/en/help/how-do-i-post-a-volunteer-opportunity (organization-side posting flow, application requirements, contacts, applicant statuses, expiry/renew/hide)
  - https://www.idealist.org/en/help/welcome-to-idealist-volunteermatch-frequently-asked-questions (connections, applicant tracking, notification preferences, membership renew cadence, export)
  - https://www.idealist.org/en/help/how-do-i-search-for-volunteer-opportunities-on-idealist (volunteer-side search, filters, saved searches, email alerts, how-to-apply modes)
  - https://www.idealist.org/en/open-network-api (Open Network API: listings syndication + Apply API; CSR platforms, government agencies, startups; partner logos incl. Blackbaud, Benevity, Bonterra, Percent Pledge)
- Rosterfy:
  - https://www.rosterfy.com/ (self-labels "volunteer management software"; platform modules; industries; "built for organisations managing 100 or more volunteers")
  - https://www.rosterfy.com/solutions/volunteer-passport/ (Volunteer Passports: government as connector; community groups publish opportunities; central hub to discover and apply; screening/compliance; public opportunities page embed; QR check-in)
- TeamKinetic:
  - https://www.teamkinetic.co.uk/ (volunteer management software; customer types include "Volunteer centre or volunteer support organisation", local councils; testimonial on sharing volunteers and opportunities across a partnership)

### Attempted, failed, abandoned (source-access limitation)

- help.volunteermatch.org — transport error (×1) → superseded by the Idealist redirect
- support.catchafire.org/hc/en-us — 404; catchafire.org/faq/ — 404; help.catchafire.com — transport error → abandoned (3 failures)
- volunteerworld.com/en/help — 404; volunteerworld.com/en/how-it-works — 404 → abandoned (2 failures)
- workaway.info/en/help — 404; /en/helpdesk.html — 404; /en/ — 404 → abandoned (3 failures)
- helpx.net — 403 → abandoned
- golden.org — timeout (×2) → abandoned
- justserve.org — JS shell only ("Loading...") → unusable, abandoned
- volunteer.gov — Salesforce error page → abandoned

Consequence (evidence rule): the skills-project, booking/travel, and exchange poles are recorded as market forms with NO operational evidence this pass. No precise claims are made about them anywhere in the outputs. The final document's variant section mentions them only as forms whose documentation was not reachable.

### Family evidence (from the processed sibling pass)

- research/volunteer-management-system.md (2026-09-09): public-facing opportunity directory / landing pages / embeds observed across 5/5 sampled VMS products (Volgistics Opportunity Directory, VolunteerHub landing pages + embeds, Better Impact "post opportunities to your website", portal opportunities, Rosterfy Volunteer Passports) — Layer A for those products; publicness held as operator posture, NOT definitional for VMS. Forward flag to this pass recorded there.

## Product Observations

### Idealist (incl. VolunteerMatch) — independent venue operator (Layer A)

Merger fact: VolunteerMatch merged with Idealist in early 2025; volunteermatch.org now serves an Idealist-branded page ("VolunteerMatch is now part of Idealist"). The venue is described as "the world's largest volunteer recruitment network" connecting "more than 200,000 organizations" with "millions of people". Homepage search spans Jobs / Internships / Volunteer Opportunities / Events / Organizations — a multi-listing social-impact venue, not volunteering-only.

Organization side (from "How do I post a volunteer opportunity?"):
- Posting requires representing an organization with an approved profile and administrator access. Organization profiles are admission-gated by the venue.
- Eligibility rule: organizations in for-profit categories (Businesses, Consultants, Recruiters) cannot post volunteer opportunities. Nonprofits, social-impact corporations, and community groups are the stated posting population.
- Posting flow: log in → organization Workspace (Dashboard) → "+Create New Listing" → "Volunteer Opportunity" listing type → form with time commitment, description, location.
- Apply-mode choice: the organization decides whether applicants apply directly through Idealist ("Allow volunteers to submit interest directly through Idealist") or through an external contact method (organization's own website or email).
- Venue-hosted application minimum: First Name, Last Name, email. Optional "Screening Questions & Materials": short text questions, PDF (cover letter), URL (portfolio), checkboxes, multiple choice, phone number — each with a Required toggle.
- Contacts: a named contact per listing receives instant email notifications when a volunteer expresses interest; contacts ≠ administrators; administrators manage the account.
- Applicant tracker: per-listing applicant list; per-applicant notes; status pipeline with venue-defined states: New Inquiry → Screening → Waiting For Response → Under Consideration → Resulted In Volunteering / Didn't Work Out.
- Communication: status changes are NOT auto-notified to candidates; the organization sends bulk messages per status bucket ("Contact All"); a candidate can be contacted only once per status type.
- Export: zip of per-candidate application documents or CSV summary.
- Listing freshness: volunteer listings expire automatically 6 months after posted date; Renew updates the posted date, pushes the listing to the top of search results, and re-circulates it through email alerts; manual Hide; optional auto-hide after an end date. Renew cadence differs by plan (members every 7 days, non-members every 45 days) — plan-specific, vendor detail.
- Monetization: posting volunteer opportunities is free; an Idealist Annual Membership unlocks a cross-listing "View All Volunteers" dashboard and faster renewals. (Freemium org-side.)

Volunteer side (from "How do I search for volunteer opportunities on Idealist?"):
- Search without an account is possible; an account enables applying through Idealist, email alerts, and a profile.
- Search dimensions: keyword (phrase quotes supported), sort Best Match / Newest, Recency filter, Date filter (when the opportunity takes place), Location Type (On-site / Hybrid / Remote), Location, Radius (adjustable only with a city-level location), Cause Areas (multi-select), Skills (multi-select). "Done in a Day" opportunity class exists as a filter.
- Saved searches with custom names; optional email alerts on new matches; alerts also exist for followed organizations and listings.
- "How to Apply" section of each listing carries the organization's chosen apply mode.
- Events can be RSVP'd as a sibling object type.

Venue governance (Help Desk index): community guidelines; "Report A Problem" (safety tips, reporting malicious behavior or inappropriate content); bug reporting; help desk. Safety reporting is a first-class venue surface.

Inventory syndication (Open Network API page):
- "Idealist has the largest and most up-to-date database of volunteering opportunities in the world… 100,000 up-to-date volunteering opportunities posted directly by 250,000 organizations." (Vendor-stated figures vary across pages — 200,000 vs 250,000 organizations; treat as marketing-scale, not precise facts.)
- Open Network API: Listings API (display listings inside third-party platforms, filterable by location, cause area, skill, eligibility) + Apply API (applications flow back). Target segments: corporate CSR & employee engagement platforms, government agencies (SNAP and Medicaid work/community-service compliance), community platforms and startups. Partners may display Idealist listings "alongside opportunities from other sources".
- Partner/consumer logos include CSR and employee-engagement platforms (Blackbaud, Benevity, Bonterra, Percent Pledge, Groundswell, Submittable) and corporate brands.

### Rosterfy — enterprise VMS deployed as an institution-hosted venue (Layer A)

Self-positioning: "Rosterfy's volunteer management software"; "built for organisations managing 100 or more volunteers"; platform modules: Recruit & Onboard, Train & Induct, Advanced Scheduling, Reward & Retain, Insights & Impact, Volunteer App, AI agent. Industries: nonprofits, cities & government, major events, sporting federations, hospitals, universities, emergency services, corporate volunteering.

Volunteer Passports (the flagged blur point) — from the dedicated page:
- Pitch: "Simplify community volunteering with one trusted space to connect, contribute, and keep track of impact." Four steps: "1. Invite community groups to publish volunteer opportunities 2. Provide a central hub for the community to discover and apply 3. Streamline volunteer onboarding 4. Enable seamless check-in with Volunteer Passport QR codes."
- Stakeholder framing: Government organisations (the connector) create "a central volunteer ecosystem where volunteers can discover opportunities and organisations can access engaged, compliant volunteers, eliminating silos and duplication"; community & volunteer organisations "promote your volunteering opportunities to screened, engaged and qualified volunteers within your community"; volunteers get "a single, connected platform where they can discover opportunities and connect with organisations".
- "Empower community organisations to publish opportunities directly to your marketplace."
- "Position your organisation as the trusted hub… a single source of truth for community volunteering."
- Venue-run readiness: integrated background checks and Working With Children Check (WWCC) validation; automated progression based on completed actions; expiring-credential alerts; shift applications paused until renewals complete.
- Public opportunities page: embeddable on the operator's website; volunteers "search via location, availability and skills".
- Tiered admin & permissions across the operator's internal teams and the participating community organizations ("the interface is intentionally simple… showing only what's relevant to them").
- "Old way" contrast: "Organisations relying on job boards to post volunteer opportunities… Volunteers are required to register and complete onboarding multiple times across different organisations."
- Case studies: city-wide programs (Bradford City of Culture; City of Parramatta Bushcare) — the operator is a city government; the venue aggregates community groups.

Interpretation: Rosterfy sells management software to one operator; the Volunteer Passports deployment turns that operator into a venue host over many community organizations. The marketplace structure (multi-org publishing + volunteer discovery + apply) is present, but as a deployment shape of VMS machinery with an institutional connector, not as a standalone venue product.

### TeamKinetic — UK VMS with volunteer-centre / council shared portals (Layer A, homepage only)

- Self-positioning: "volunteer management software for managing, recruiting, events, and rotas"; modules Mobilise (recruitment/onboarding), Manage, Measure, Motivate; mobile app; free Community edition (unlimited volunteers, 1 admin, 3 live opportunities).
- Customer-type picker includes "Volunteer centre or volunteer support organisation" and "Local council or governmental" — the UK volunteer-centre model: an umbrella body hosts a shared portal where many local organizations recruit.
- Testimonial evidence of cross-organization sharing: a gallery states it "means in the future we could look at sharing our volunteers and opportunities across the partnership through TeamKinetic"; another cites matching volunteers to support requests with "over 3,000 tasks completed".
- Interpretation: same pattern as Rosterfy — management machinery hosting multi-organization venues, here at the volunteer-centre / council tier. Homepage is marketing-grade; operational detail not documented this pass.

## Cross-product Comparison

| Structure | Idealist (venue-native) | Rosterfy Volunteer Passports (institution-hosted) | TeamKinetic (council/centre portals) | Evidence |
|---|---|---|---|---|
| Operator distinct from posting organizations | Yes — venue operator vs 200k+ orgs | Yes — government connector vs community groups | Yes — centre/council vs local orgs | A×3 |
| Many independent organizations publish into one shared venue | Yes (free listings, approved profiles) | Yes ("invite community groups to publish… directly to your marketplace") | Yes (partnership sharing; centre portals) | A×3 |
| Volunteer opportunity listing as unit of supply | Yes (listing type with time commitment, description, location) | Yes (opportunities published by groups) | Yes (opportunities/tasks) | A×3 |
| Volunteer-side discovery across the whole venue | Yes (keyword/cause/skills/location/radius/date/remote filters; sort) | Yes (search by location, availability, skills) | Yes (portal search; homepage-level evidence) | A×3 (TeamKinetic weaker) |
| Response/connection routed to the posting organization | Yes (venue-hosted interest/application OR external handoff — org's choice) | Yes (central hub to "discover and apply"; orgs receive screened volunteers) | Yes (implied by recruitment/onboarding loop) | A×2 + B |
| Connector tracking after response | Yes (status pipeline, notes, contact-all, export) | Yes (onboarding progression, compliance states) | Yes (management loop) | A×2 + B |
| Venue-run screening/compliance | No — org-side (application materials only) | Yes — venue-run (background checks, WWCC, credential expiry) | Partial (inbuilt criminal checks advertised) | Variant axis |
| Listing freshness lifecycle | Yes (auto-expiry, renew, hide) | Not documented on fetched pages | Not documented | Product-specific |
| Saved searches + email alerts | Yes | Not documented | Not documented | Product-specific |
| Inventory syndication (embed/widget/API) | Yes (Open Network API, search widget, engagement pages) | Yes (public opportunities page embed) | Not documented | A×2 |
| Monetization | Org-side freemium (membership) + API licensing | Venue licensing to institutions | SaaS tiers incl. free community edition | Variant axis |
| Nonprofit-only posting | No — community groups also post; for-profit businesses excluded from volunteer listings | No — community groups, government context | No — councils, sports bodies, charities | Variant axis |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Volunteer Marketplace is an operated venue where many independent organizations publish volunteer opportunities into one shared searchable space, and individual volunteers discover and respond to those opportunities, with the connection routed to the posting organization.

Four jointly-held structures:

1. **The shared multi-organization venue** — an operator (distinct from the posting organizations) runs one venue into which many independent organizations publish. Remove → a single organization's recruitment page / program tool = Volunteer Management System territory.
2. **The volunteer opportunity as the listed object** — published listings describing unpaid help an organization seeks (what/when/where, cause, skills, time commitment, how to apply). Remove → generic listing venue / paid job board.
3. **Volunteer-side discovery across organizations** — search/browse across the whole venue (cause, location, skills, availability), not within one program. Remove → a posting archive nobody shops; a static directory.
4. **The response connection routed to the posting organization** — the volunteer expresses interest / applies / signs up to a specific opportunity and the response reaches that organization to take the relationship forward (venue-hosted intake or external handoff). Remove → content surface with no pairing loop.

Jointly-held load-bearing checks:
- 1 alone = generic classifieds/listing venue (no volunteer semantics)
- 2 alone = one unpaid-work ad (no venue)
- 3 alone = search over nothing
- 4 alone = a contact form
- 1+2 without 3+4 = a posted directory nobody searches or answers (Listings Platform territory)
- 2+3+4 without 1 = one organization's opportunity page (VMS recruitment channel)
- 1+3+4 without 2 = a generic two-sided marketplace (Service Marketplace umbrella) — the unpaid-contribution semantics is the domain binding

Historical / market-sample check (§24): the paper-era volunteer bureau / volunteer centre satisfies the core with no web machinery — the bureau (operator) keeps a registry of many agencies' needs (multi-organization opportunity registry), volunteers consult the printed directory or a staff member (discovery), and the bureau refers the volunteer to an agency (routed connection). The web marketplace form is itself long-lived (Idealist founded 1995 as Action Without Borders; VolunteerMatch 1998). The definition does not depend on any modern implementation (APIs, alerts, profiles, compliance engines).

### L1 — Common Mature Structure (not definitional)

- Organization profiles with admission/approval (venue gate on who may post)
- Structured listing content: description, time commitment, location, cause area, skills
- Multi-dimensional volunteer search (keyword, cause, location/radius, skills, date, remote/onsite) with sorting
- Venue-hosted response intake with minimum identity fields and optional screening questions/materials
- Connector tracking (statuses, notes, exports) and organization-side notifications
- Listing freshness lifecycle (expiry / renewal / hide)
- Saved searches + email alerts
- Volunteer profiles
- Organization dashboards with role separation (administrators vs named contacts)
- Public embeddable opportunity pages / search widgets
- Community guidelines + safety/problem reporting
- Reporting for organizations

### L2 — Variant / Optional Structure

- Operator posture: independent venue operator (venue IS the product) vs institution-hosted venue (city government, volunteer centre, federation operates the venue on management-software substrate)
- Readiness gating location: posting organization screens (application materials, external process) vs venue-run centralized screening/compliance (background checks, working-with-children checks, credential expiry)
- Apply mode: venue-hosted application vs external handoff (org's website/email) — per-listing choice in the sampled venue-native product
- Monetization: free-to-post with org-side membership upsell; venue licensing to institutions; API licensing; (booking/fee-based travel programs — market form, unevidenced this pass)
- Inventory syndication: embeds, widgets, Listings/Apply APIs into CSR platforms, government benefit systems, community platforms
- Venue scope: volunteering-only vs multi-listing social-impact venue (jobs + internships + events + organizations)
- Audience variants: corporate employee volunteering consuming venue inventory; government work-requirement community-service access
- Opportunity shape: ongoing roles vs one-off events/RSVPs vs "done in a day" micro-tasks
- Skills-based project matching and travel/exchange-based programs: market forms recorded, official documentation not reachable this pass — no operational claims made

### L3 — Vendor-specific (research notes only)

- Idealist applicant status labels (New Inquiry / Screening / Waiting For Response / Under Consideration / Resulted In Volunteering / Didn't Work Out); once-per-status contact rule; 6-month auto-expiry; 7-day (member) vs 45-day (non-member) renew cadence; "Workspaces" account model; owner/administrator/contact role split; zip/CSV export shapes; "Done in a Day" filter; Best Match/Newest sort; radius presets (5–100 miles / Entire Country); radius adjustable only with city-level location; Annual Membership "View All Volunteers" dashboard; VolunteerMatch brand retained on the API product ("Volunteer Match, powered by Idealist").
- Rosterfy: Passport QR check-in; WWCC validation; shift-application pausing on expired credentials; tiered permissions across internal teams and community organizations; white-label app; ISO/SOC2 posture; "built for organisations managing 100 or more volunteers".
- TeamKinetic: Community edition limits (unlimited volunteers, 1 admin, 3 live opportunities); Tempo Time Credits / OpenBadge recognition; DBS checks (UK) in higher tiers; white-labelled enterprise app.

## Vendor-specific Findings

See L3. None of these enter the canonical model. The Idealist status pipeline is generalized in the final document as "connector tracking with venue-defined statuses" — the existence of a tracked pipeline is cross-product (Idealist, Rosterfy onboarding progression), the specific labels are not.

## Rejected Findings

- "Volunteer marketplace = nonprofit-only posting" — REJECTED. The venue-native sample explicitly admits community groups and (for other listing types) social-impact corporations, while excluding for-profit businesses from volunteer listings specifically. The invariant is "organization seeking unpaid contribution", not legal nonprofit status.
- "Volunteer marketplace = free for volunteers" — REJECTED as definitional. Free-to-search is observed in the venue-native sample (product-specific); other market forms (travel/exchange) are commonly fee- or membership-based, but this pass has no official evidence either way. Held as variant, not invariant.
- "Public opportunity directories are definitional for volunteer software" — already REJECTED by the VMS pass for that Type (private programs in-type). For the marketplace Type the shared venue IS the product, so publicness is inherent to the venue posture — but the marketplace leaf must not claim that VMS products are defined by publicness. The seam is the operator's center of gravity, not the directory feature.
- "Marketplace = VMS module" — REJECTED as a collapse. The venue-native pole (Idealist) is a standalone venue product with no single-organization program system of record at its center; the institution-hosted pole reuses VMS machinery but the venue is the deployment. Keep-both with the center-of-gravity seam.
- "Application pipelines with fixed statuses are definitional" — REJECTED. Status vocabularies are vendor-specific; only the existence of tracked connections is cross-product.
- "Marketplace inventory syndication is definitional" — REJECTED. Observed in 2/3 sampled products (embed + API); held as common/optional, not invariant.

## Boundary Findings

### vs Volunteer Management System (§25 sibling, processed 2026-09-09) — JOINT REVIEW DISCHARGED

- VMS: one organization's program system of record — its volunteer database, its opportunities, intake→placement, service record. The organization is the operator.
- Marketplace: the shared venue itself — many organizations as posting participants, volunteers as the seeker-side population, the venue operator as a third party. The organization is a participant, not the venue owner.
- Shared surface: the public opportunity directory. In VMS it is a recruitment channel of one program (documented 5/5 in the VMS pass); in the marketplace it is the venue itself. Same surface, different center of gravity.
- Blur point resolution (Rosterfy Volunteer Passports): a VMS product deployed AS a community venue by an institutional connector (city government). This proves venue-shaped operation is achievable within VMS machinery — it does not collapse the Types, because the venue-native pole (Idealist) has no VMS center at all. Verdict: keep-both RATIFIED; seam = the product's center of gravity (program system of record vs shared venue), with "institution-hosted venue" recorded as a marketplace deployment variant realized on VMS substrate.
- Remove-X discriminators: from the marketplace, remove the multi-organization shared venue (keep one org's program) → VMS. From the VMS, remove the single-organization program center (keep the shared venue) → marketplace.

### vs Service Marketplace (§05.02, processed 2026-09-07)

- That pass already documented the generic venue as umbrella Type over domain-structured siblings, explicitly listing "volunteer §25" among them, with the boundary held on domain structuring. This pass confirms from the volunteer side: the domain binding is the unpaid-contribution opportunity + mission/community posting population + volunteer identity. Keep-both consistent with the babysitting/beauty precedents.

### vs Job Board

- A job board's listed object is paid employment; the response loop targets hiring. The volunteer marketplace's listed object is an unpaid-contribution opportunity; the response loop targets the organization's volunteer program. Adjacency is real (Idealist spans both listing types in one venue; Rosterfy's "old way" contrast calls job boards the wrong tool for volunteer posting) but the objects, populations, and semantics differ. Multi-listing venues that span both are a venue-scope variant, not a Type collapse.

### vs Listings Platform / Directory (§02.11)

- A directory/listings platform is a static listing surface; the marketplace requires the two-sided response loop (discovery → routed connection). Remove the response loop → directory territory.

### vs Nonprofit Event Management (§25 sibling)

- Opportunities can be event-shaped (RSVPs exist as a sibling object in the venue-native sample), but the venue's persistent object is the organization's opportunity listing and the volunteer connection, not a dated event occasion. Event-shaped listings are an opportunity-shape variant.

### vs Community Platform / Member Community (§25 siblings)

- No participatory member spaces; the venue is a two-sided pairing surface. Community features (guidelines, reporting) exist as governance, not as the product center.

### vs Online Donation Platform / Fundraising (§25 siblings)

- Money vs time. The marketplace's unit of exchange is contributed time/skills, not donations. (Fee-based travel programs would blur this — unevidenced this pass, held as uncertainty.)

## Uncertainties

1. Skills-based project matching (Catchafire-class), volunteer-travel booking (Volunteer World-class), and exchange-based host marketplaces (Workaway-class) could not be evidenced from official documentation this pass (all fetch attempts failed). Their existence as market forms is common knowledge, but NO operational claims about them are made in the outputs. If a future pass reaches them, re-check: (a) whether booking/payment makes the travel pole a different Type (tour-marketplace territory), (b) whether peer-host (non-organization) publishers break the "organization" leg of L0.
2. TeamKinetic evidence is homepage-grade (marketing). The volunteer-centre shared-portal pattern is corroborated by Rosterfy's institutional deployments, but TeamKinetic's operational venue mechanics are not documented.
3. Whether venue-run screening (Rosterfy-style) or org-run screening (Idealist-style) is market-dominant is unknown; held as a variant axis.
4. Vendor-stated network sizes vary across the venue-native product's own pages (200,000 vs 250,000 organizations); no precise scale figures are asserted in the final document.
5. Fee-based listing promotion exists ("Expand your reach by promoting your volunteer listing" help article title observed in the Help Desk index) but was not fetched; monetization depth is held at variant level.

## Final Synthesis

The Volunteer Marketplace is the seeker-side counterpart to the Volunteer Management System: where the VMS is one organization's program system of record, the marketplace is the shared venue across many organizations. Its defining core is deliberately small — an operated multi-organization venue, the volunteer opportunity listing as unit of supply, volunteer-side discovery across the venue, and the response connection routed to the posting organization. Everything else commonly seen (profiles, alerts, screening engines, syndication APIs, membership tiers, compliance machinery) is mature structure or variant, not definition. The Type holds two operator postures: the independent venue (the venue is the product) and the institution-hosted venue (an umbrella institution operates the venue on management-software substrate). The Rosterfy Volunteer Passports blur point resolves as the latter posture and does not collapse the Type boundary with VMS. The Type is the volunteer-domain sibling of the Service Marketplace umbrella, consistent with that pass's recorded precedent.
