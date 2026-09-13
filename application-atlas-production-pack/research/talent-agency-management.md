# Research Notes — Talent Agency Management

Date: 2026-09-09
Slug: talent-agency-management
Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Artist Booking Platform, Casting Platform, Audition Management, Record Label Management, Music Promotion Platform)

Carries a **joint-review obligation** recorded by the artist-booking-platform pass (2026-09-08): "agency-side booking suites and agency management systems overlap on roster/offers/contracts/settlements; structural test = booking transaction (artist × date × terms × lifecycle) as center vs artist career/agency operations as center — a marketplace booking platform needs no career-management objects at all; probable partial-overlap gradient, flagged for joint review when Talent Agency Management is processed." Discharged in Boundary Findings #1.

## Research Goal

Understand what "Talent Agency Management" actually is as an Application Type: what object the system centers on (the represented client vs the booking vs the role), what its users do daily, what lifecycle its core records carry, where the agency's money enters the system, and where the Type begins/ends relative to Artist Booking Platform, Casting Platform, Audition Management, Staffing Agency Management System, and Record Label Management.

## Initial Boundary

Initial hypothesis (to be tested, not assumed): the software a talent/creative agency (actors, models, voice artists, writers, directors, comedians, musicians) runs its business on — a roster of represented clients, a pipeline of opportunities matched to that roster (submissions, offers, holds), a diary/availability layer, contracts and deals, and commission-based money (client earnings, agency commission, client statements/payments). Nearest confusions:

- Artist Booking Platform (booking transaction as center) — sibling, flagged
- Casting Platform (two-sided market) — the agency is a participant in it, not its operator
- Audition Management (production-side selection) — agency observes, does not run
- Staffing Agency Management System (§09) — naming collision, different business (workforce supply vs career representation)
- Record Label Management — different asset of record (recordings vs people)

## Research Questions

1. What is the central record — the client, the engagement, or the opportunity?
2. How do opportunities enter the agency (breakdowns, inbound offers, enquiries) and how are they matched to clients?
3. What pipeline states do agency systems track (submission, availability check, audition/tape, recall, pencil/hold, offer, job, contract)?
4. How does the agency's money work: commission rates, payruns, client statements, agency receivables — and is the money loop definitional?
5. How is availability/diary handled, and is it part of the core or a common addition?
6. What does the talent themselves get (portal, accounts) vs what is agent-only?
7. Do booking-agency systems (music touring) form a separate Type or a segment flavor of this one?
8. What does intake (applications for representation) look like — is roster-building part of the system?

## Representative Products

Selection logic: cover the two dominant operating segments of the market — acting/creative/voice representation (UK pole) and live-music booking agencies (US/global pole) — plus the casting-ecosystem context that agency systems integrate with. Geographic spread: UK + US. Evidence layers marked A (directly observed on official source) / B (cross-product commonality).

| Product | Segment | Geography | Status |
|---|---|---|---|
| Tagmin | acting / creative / voice / supporting-artist agencies | UK (used in EU/US/AU/NZ) | Fetched — homepage, feature list, About |
| Prism (For Agencies) | music booking & touring agencies | US | Fetched — homepage + agency solution page |
| Gigwell | music booking agencies | US/ES | Fetched — homepage |
| Talent Systems (Spotlight family) | casting ecosystem incl. representative workflow | global | Fetched — homepage (context; same family as Tagmin) |

Examined and **rejected** (Product Mismatch): TalentDesk.io — a buyer-side freelancer/vendor management platform (external workforce management), not agency-side career representation; belongs to Contingent Workforce Management territory.

## Sources

- Tagmin — https://www.tagmin.com/ (homepage: features list, TagTools, About, pricing model). Fetched 2026-09-09.
- Talent Systems — https://talentsystems.com/ (homepage: four audiences incl. "Talent Representatives"). Fetched 2026-09-09.
- Prism — https://prism.fm/ and https://prism.fm/why-prism-for-agencies/. Fetched 2026-09-09.
- Gigwell — https://gigwell.com/ (homepage: Productivity Suite, Contract Builder, FlexPay, Tour IQ, Ticket Counts Pro). Fetched 2026-09-09.
- Cross-referenced: research/artist-booking-platform.md (Gigwell observation, 2026-09-08); applications/casting-platform.md, applications/audition-management.md, applications/record-label-management.md (boundary calibration); STATUS.md staffing-agency-management-system entry (2026-09-08).

Source-access limitations (recorded per evidence rules):
- https://www.tagmin.co.uk/faq/ timed out twice — abandoned; Tagmin evidence limited to homepage.
- bookingware.com / www.bookingware.com (model-agency software) — transport errors twice; abandoned. Model-agency pole unverified.
- bandpencil.co.uk — www transport error, bare domain 403; abandoned.
- backonstage.io — transport error; abandoned.
- showscape.com — transport error; abandoned.
- No vendor help-center articles were reachable for any sampled product. All product observations are from official marketing/product pages (Tier 2). Deep operational rules (payrun frequencies, exact state names, commission defaults) are therefore asserted at reduced strength.

## Product Observations

### Tagmin (UK acting/creative/voice/supporting-artist agencies) — Layer A

From tagmin.com homepage (official):

- Self-positioning: "The leading agency software for talent agents"; "Tagmin provides solutions for talent agents. Tools designed to save time and money by streamlining your workflow and linking your world — your talent and contacts — and the projects that connect them."
- Testimonials from dozens of named UK agencies across acting, voiceover, and personal management (PMA / CPMA / AYPA members cited); "90% of PMA Artists' Agents, 85% of CPMA, 95% of AYPA members" claimed.
- **Full feature list** (homepage, verbatim): Applications for representation · Client Availability · Filters & Searches · Project tracking · Submissions · Availability Checks · Scripts · Auditions, Tapes & Meetings · Recalls · Pencils · Offers · Jobs · Contracts · Invoices · Payments · Reports · Contacts · Mail · Texts · Website syncing · Tasks.
- **Talent have their own accounts**: "Tagmin accounts for each of the talent you represent" — client-facing access is first-class.
- **TagRep**: "streamlines how performers apply to your agency for representation… process those applications… ensure all applicants get a response" — roster intake machinery.
- **TagTools family** (add-on modules): TagTapes (convert/compress/organise tapes), TagVoice (voiceover-specific tools), TagProjects (track projects in pre-production), TagTexts (message talent from desktop), TagWeb ("updates all the client info on your website"), TagExtras (supporting-artist-specific tools).
- **#YesNo**: free tool for casting directors to notify all involved when a role is cast — the vendor operates on both sides of the industry's workflow.
- **Money evidence**: "Invoices · Payments · Reports" in core feature list; testimonial "A payrun that could take two days is now taking just two hours!" (Gielgud Management) — payrun machinery confirmed.
- **Ecosystem**: integrates with Spotlight (the UK casting platform); Tagmin is now part of Spotlight / Talent Systems family; German-language version exists (tagmin.de).
- Pricing: per-user licensing with discounted additional users and "Lite" accounts (limited access days/year).
- Segments evidenced: acting, voiceover (TagVoice), supporting artists (TagExtras) — the same core system with segment add-ons.

### Prism (For Agencies) (US music booking/touring agencies) — Layer A

From prism.fm homepage + /why-prism-for-agencies/ (official):

- Self-positioning: "Booking Agency Software Built for Live Music"; agency page titled "Talent Agency Software".
- **Roster + commission**: "Manage Your Artists… add new artists to your roster, **set or edit commission percentages**, view upcoming events, and manage files like W-9s and riders, all in one convenient location."
- **Calendar**: "monitor the entire booking process for your whole roster… filter by agent or artist" — diary/availability over the roster with per-agent and per-artist views.
- **Deal Tracker / Deal & Payment Tracker**: "keep up with all contracts, offers and bookings"; "keeps you informed and in control of your contracts and payments ensuring that nothing falls through the cracks."
- **Contracts**: generate contracts with templates; "dial in every financial element, including deals, ticket scaling, merch rates."
- **Payments**: track deposits & payments per show; chase late payments (Mail Merge bulk email by role/event); "artist payouts and commissions, from estimates and forecasts to actuals" in real-time financial reporting.
- **Reporting**: performance by agent, artist, genre, tour; historical data to inform future tour routing.
- **Itineraries**: custom versions for artist teams (managers, publicists) with or without financials.
- **Contact Book**: agency contacts with roles, related artists and events.
- **Connected Show**: import venue/promoter offers (Prism runs both sides — venue/promoter product and agency product).
- Segment-flavored extras: box-office data insights (Insights), settlements (show accounting).

### Gigwell (US/ES music booking agencies) — Layer A (+ cross-ref to sibling research)

From gigwell.com homepage (official):

- Self-positioning: "The First End-to-End Booking Management Platform for Artists… centralized booking solutions for artists, agents and venues to streamline contracts, track online payments, manage artist advancing & monitor real-time revenue goals."
- **Productivity Suite**: "negotiate contracts, manage artist logistics, collect online payments & monitor real-time revenue goals."
- **Contract Builder**: "one-click contract builder empowers your agents to customize and send contracts, artist riders and travel docs in minutes."
- **FlexPay** (online payments): "automating deposit reminders and offering your clients multiple payment options."
- **Tour IQ**: venue/festival database, availability tool, "venue radius clauses and capacity restrictions" — discovery machinery for filling tour dates.
- **Ticket Counts Pro**: automated ticket-count collection, market-pace reports, sales analytics.
- Testimonials: contracts/deposits workflow was formerly a dedicated staff role at one agency; on-time deposits improved at another.
- Sibling research (artist-booking-platform.md, 2026-09-08) additionally documented: offers, holds ("multiple holds per date"), settlements, advancing, itineraries, radius clauses.

### Talent Systems (ecosystem context; parent of Tagmin and Spotlight) — Layer A

From talentsystems.com homepage (official):

- Four audiences: performers, casting directors, **talent representatives** ("Manage your roster clients' profiles and submit them to thousands of projects posted by the world's most prolific casting directors"), studios/filmmakers.
- Portfolio: Casting Networks, Spotlight, Tagmin, Cast It Talent, Casting Frontier, Staff Me Up — the representative workflow ("roster clients' profiles and submit them") is sold as one of the ecosystem's four legs.
- Confirms: the agency-side system is structurally coupled to (but distinct from) the casting platform — the platform publishes roles; the agency manages its own roster and submits into the platform.

## Cross-product Comparison

| Structure | Tagmin (acting) | Prism (booking agency) | Gigwell (booking agency) | Evidence |
|---|---|---|---|---|
| Roster of represented clients as persistent records | ✔ "your talent" + client accounts | ✔ "Manage Your Artists… roster" | ✔ artists at the center of booking suite | B |
| Client profile with media/materials | ✔ tapes, scripts, website sync | ✔ files (W-9s, riders) | ✔ artist profile/logistics | B |
| Opportunity pipeline matched to roster | ✔ submissions, availability checks, projects | ✔ offers, Connected Show imports | ✔ offers, Tour IQ discovery | B |
| Availability / diary / holds over roster | ✔ Client Availability, Availability Checks, Pencils | ✔ calendar filtered by agent/artist | ✔ availability tool, booking dates | B |
| Pipeline states toward booked work | ✔ auditions/tapes/meetings, recalls, pencils, offers, jobs | ✔ deal tracker: contracts, offers, bookings | ✔ negotiate contracts; holds (sibling obs.) | B |
| Contracts / deal terms as records | ✔ Contracts | ✔ contract templates, financial elements | ✔ Contract Builder, riders | B |
| Agency earnings against client work (commission) | ✔ payrun testimonial + Invoices/Payments/Reports | ✔ "set or edit commission percentages… artist payouts and commissions, estimates to actuals" | implied (booking revenue goals; deposits/payments) | B (A on 2 poles) |
| Money settled between agency and client | ✔ payrun, invoices, payments | ✔ artist payouts | ✔ artist-side payments (sibling obs.) | B |
| Communication with clients & industry | ✔ Mail, Texts | ✔ Mail Merge, Contact Book | ✔ (contact/chase flows) | B |
| Intake / applications for representation | ✔ TagRep | — (not observed) | — | A (single product) |
| Reporting by agent/client/engagement | ✔ Reports | ✔ by agent/artist/genre/tour | ✔ analytics | B |
| Segment-specific machinery | tape processing, VO tools, extras tools (L3 modules) | itineraries, settlements, ticket scaling, routing | radius clauses, ticket counts, advancing | A per product |
| Casting-platform integration | ✔ Spotlight | — | — | A (single product) |

Reading: all three primary poles independently carry roster + pipeline + availability/holds + contracts + money. The acting pole expresses the pipeline as submissions→auditions→pencils→offers→jobs; the booking pole expresses it as offers→holds→contracts→settlements. Same spine, different vocabulary — consistent with the industry's own usage ("pencil" is UK/US theatre-film vocabulary; "hold" is live-music vocabulary).

## Canonical Model

### L0 — Defining Invariant

The agency-side business system of record for representing creative talent. Three jointly-held structures; remove any one and the product stops being recognizable as talent agency management:

1. **The agency's roster of represented clients.** Persistent, individually identified records for the people (and in some segments acts/brands) the agency represents — the agency's asset of record. Each client carries their professional profile: identifying details, appearance/category attributes, media (photos, reels, tapes, scripts, files), and representation status (active, invited, lapsed). The client is a managed record, not the operator; agents operate on behalf of clients.
   - remove → a generic contact/CRM database (people exist but are not represented careers).

2. **The opportunity pipeline matched against the roster.** Professional opportunities flow in from outside — casting breakdowns, inbound offers, event enquiries, direct approaches — and the agency matches them to suitable, available clients and pursues them as tracked pipeline items, through pursuit states (submitted, auditioning/taping, recalled, held/pencilled, offered, negotiating) to booked work. Availability and diary state are the matching substrate: an opportunity is matched to who is free and suitable.
   - remove → a static roster nobody works from, or a submissions tool over unanchored people (casting-platform territory).

3. **The representation money loop.** Booked work converts into the client's earnings, from which the agency's earnings are derived (commission on client work in the dominant model; the configurability of rates is implementation detail), and money is settled between agency and client — invoices and payments tracked to the agency, payruns/statements computed for clients.
   - remove → a pipeline tool with no economics (a submission desk), or bare invoicing disconnected from represented work.

Jointly-held load-bearing:
- 1 alone = client/CRM database
- 2 without 1 = submission/offer machinery over unanchored people
- 3 without 1+2 = commission calculator over nothing
- 1+2 without 3 = opportunity tracker with no economics
- 1+3 without 2 = client accounts with statements but no pipeline (bookkeeping + contacts)
- 2+3 without 1 = a deal/booking system for anonymous parties

### L1 — Common Mature Structure

Present in most mature products; not definitional:

- intake/applications for representation (roster-building pipeline; A on Tagmin only — held common-with-caution)
- client profiles with media management (tape/reel processing, headshots)
- industry contact book (casting directors, producers, promoters, buyers)
- communication tooling (mail/merge, texts) toward clients and industry
- contracts generated from templates, e-sign/attachment of deal terms
- per-client and per-agent diary/calendar views; conflict awareness
- agency reporting (by agent, client, engagement type, revenue)
- client-facing accounts/portal (talent see their diary, jobs, materials)
- tasks/admin tracking around jobs
- website syncing of client information

### L2 — Variant / Optional Structure

- **Segment flavor** — the pipeline's vocabulary and machinery specialize per segment: acting/creative (submissions → auditions/tapes → recalls → pencils → offers → jobs), live music/touring (offers → holds → contracts → settlements → itineraries → routing → ticket counts), voiceover (democarts/tape specs), supporting artists (bulk extras booking). The L0 spine is identical; the state vocabulary and attached machinery differ.
- **Ecosystem integration substrate** — casting-platform integration (Spotlight) on the acting pole; venue/festival discovery databases (Tour IQ) on the booking pole; none/standalone for smaller agencies.
- **Touring depth** — radius clauses, ticket scaling, settlements, advancing: deep on the booking pole, absent on the acting pole (variant, not core).
- **Client portal depth** — from full accounts to none.
- **Regulatory posture** — jurisdictions regulate agency commission and contracting to varying degrees; products reflect this through configurable commission structures and contract templates (configurability observed: Prism; the regulatory specifics were not researched — see Uncertainties).
- **Business-manager flavor** — some representation firms take on broader financial management of clients' affairs (beyond commission on agency-sourced work); software depth for this varies.

### L3 — Vendor-specific (research notes only)

- Tagmin: TagTapes, TagVoice, TagExtras, TagProjects, TagTexts, TagWeb, TagRep (module), #YesNo (free cross-side tool), Lite-user licensing.
- Prism: Connected Show (offer import from venue side), Mail Merge, Insights (shared box-office data), Deal & Payment Tracker naming.
- Gigwell: FlexPay, Tour IQ, Ticket Counts Pro, Eco-Rider content marketing.

## Boundary Findings

1. **vs Artist Booking Platform (sibling leaf; joint-review flag DISCHARGED — keep both, RATIFIED).** The artist-booking-platform pass hypothesized a partial-overlap gradient with the structural test "booking transaction as center vs artist career/agency operations as center." This pass confirms the seam and sharpens it:
   - **Unit of record**: the booking platform's record is the booking transaction (artist × dated performance occasion × terms), and its buyer side is a first-class system population (talent buyers, venues, promoters with their own surfaces and products). The agency system's record is the **represented client within one agency's business**; buyers/casting are external counterparties held as contacts, not as a system population.
   - **Scope of work types**: the agency pipeline spans many revenue types around a client's career (auditions, commercials, theatre/TV jobs, tours, appearances, endorsements); the booking platform centers one transaction shape (dated live appearance).
   - **Career-management objects**: the agency system carries objects with no booking analog — representation status, intake/applications for representation, client availability as an ongoing profile attribute, commission structure per client, payruns/statements. The booking platform can operate with none of these (the sibling pass's own observation: "a booking platform can exist with no career-management object at all").
   - **The gradient is real and the market exhibits it**: music booking agencies instantiate agency systems whose center of gravity sits close to the booking transaction (Gigwell self-labels "booking management platform"; Prism sells venue-side and agency-side as one connected market). The seam is center-of-gravity, not a wall: a booking-heavy agency product and a career-focused agency product can converge on roster + offers + contracts + money. **Ratification: keep both Types**, with the test above as the discriminator; the booking platform pass's "agency-mediated suite" operating model already documents this convergence from its side. Search-term pollution noted: Prism markets its agency product as "Talent Agency Software" while being booking-centered — beware name-based linking in future passes.
2. **vs Casting Platform**: the casting platform is a shared two-sided market (productions publish roles; many agencies and performers submit into it). The agency system is one organization's private system of record over its own roster, which *consumes* casting platforms — Tagmin's Spotlight integration and Talent Systems' representative workflow both evidence this coupling. Remove the shared market (publisher-controlled visibility, many unrelated productions) and the agency system still stands; remove the roster/money spine and a casting platform still stands. Distinct Types.
3. **vs Audition Management**: audition management runs the selection process on the production side (roles → candidacies → auditions → evaluation → casting decision). The agency tracks its own clients' auditions/tapes/recalls as pipeline states but never runs the selection. Distinct.
4. **vs Staffing Agency Management System (§09)**: naming collision, different business. The staffing agency's clients are organizations buying workforce capacity; the unit of demand is the client-owned job order; money is pay/bill spread or placement fee on supplying workers. The talent agency's "buyers" book *specific individuals*; the money is the agency's earnings on the client's own work. Staffing = supply of interchangeable labor; talent = representation of particular careers. Distinct Types; the parallelism (roster + pipeline + placement) is real but the commercial object differs.
5. **vs Record Label Management**: the label's asset of record is the controlled recording catalog with contractual deal structure and settlement loop over exploitation income. The agency's asset of record is the person and their flow of engagements. A label signs *works*; an agency represents *people*. Distinct Types (both carry a "deal + money" spine over different assets).
6. **vs generic CRM**: a configured CRM can approximate roster + pipeline (1 + partial 2) for a small agency. What it lacks is the representation-specific money loop (commission against client earnings, payruns/statements), the availability/holds state machinery, and the industry integration substrate. The Type is a vertical business system of record, and the market's own framing ("ditch the spreadsheets") confirms the spreadsheet/CRM baseline it replaces.
7. **vs Talent Sourcing / Recruiting (§09)**: recruiting markets employment to candidates as a hiring funnel owned by the employer; representation markets a client's professional services as an ongoing commercial relationship owned by the agency. Brief distinction recorded; not a live confusion in the market.

## Uncertainties

- **Model-agency software pole unverified**: bookingware.com (model agency booking systems) unreachable; whether model-agency systems (options lists, comp cards, usage rates) instantiate this L0 unchanged or carry a distinct "options book" state model is unconfirmed. The acting + music poles span the two segments with the strongest evidence; model segment claims are held at "expected variant" strength only.
- **Payrun mechanics**: the payrun (commission run) is evidenced by Tagmin testimonial + feature list and Prism's "artist payouts and commissions, from estimates and forecasts to actuals"; exact frequencies, statement formats, and reconciliation behavior were not observed (no help-center access). Asserted only as "the system computes and settles agency vs client money."
- **Whether intake is definitional**: roster intake (applications for representation) observed on one product (TagRep). Held L1; a stable-roster agency without intake machinery still satisfies the L0.
- **Regulatory specifics**: jurisdiction-specific rules on agency commission/licensing were not researched; only configurability of commission was observed. No regulatory claims made in the final document.
- **Talent Systems family bias**: Tagmin and Spotlight share a parent (Talent Systems), so the acting-pole integration evidence comes from one corporate family; no independent acting-agency product was reachable to cross-check integration depth (others failed transport).
- **Influence/creator talent management** (digital creators, influencer agencies): likely a growing segment of this Type (roster + brand deals + commission) but no product was fetched; recorded as a probable variant with no direct evidence.

## Final Synthesis

Talent Agency Management is the agency-side business system of record for representing creative talent. Its defining core is three jointly-held structures: a persistent roster of represented clients (each a managed career record with profile and media, not an operator account); an opportunity pipeline that ingests external opportunities and matches them against the roster's availability and suitability, pursuing each through pursuit states to booked work; and the representation money loop that derives the agency's earnings from the client's booked work and settles money between agency and client (commission-based in the dominant model). Around this spine, mature products add intake, media/materials management, contact books, communication tooling, contract templates, diaries with holds, reporting, and client portals — and specialize the pipeline's vocabulary and machinery per segment (acting's submissions-and-pencils vs live music's offers-and-settlements). The market's closest confusion — agency-side booking suites vs booking platforms — resolves on the unit of record (represented client vs booking transaction) and on whether buyer-side parties are a system population or external contacts; both Types are kept.
