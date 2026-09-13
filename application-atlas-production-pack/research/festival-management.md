# Research Notes — Festival Management

## Research Goal

Understand what "Festival Management" is as an Application Type: what objects festival-specific software manages, how the festival production loop works, whether the festival substrate is a distinct Type or a segment variant of Event Management Platform, and where the boundaries lie against the sibling event-family leaves (ticketing, agenda, credential/badge, cashless, artist booking, volunteer management, convention/exhibition, attraction).

## Initial Boundary

- Working hypothesis entering research: festival management is organizer-side software for producing festivals — multi-day, multi-part public events (music, film, arts, food, cultural) — centered on the festival's program and its participant ecosystem rather than on a single occasion's registration flow.
- Nearest neighbors suspected: Event Management Platform (generic event lifecycle — the sharpest seam), Event Ticketing Platform, Event Agenda Management, Event Credential / Badge Management (prior pass flagged a security-led accreditation pole involving festivals), Artist Booking Platform, Volunteer Management System, Cashless Venue Platform, Convention / Exhibition Management, Attraction Management System.
- Key taxonomy question inherited from the Event Management Platform pass: that pass documented "festival" as a segment sibling "documented as their own Types when their substrate changes the model". This pass must determine whether the substrate changes the model.
- Prior passes' characterization to verify: cashless-venue-platform research wrote "festival management's object is the event program (lineup, scheduling, production)"; convention-exhibition-management research wrote "festivals organize stages/lineups/ticketing for audiences".

## Research Questions

1. What objects does dedicated festival software manage? (festival/edition, program parts, venues/stages, participants, entitlements, hospitality, publications)
2. Who are the managed populations — audience only, or a wider participant ecosystem?
3. How does the working loop run across the festival year (intake → selection → programming → entitlements → onsite → closeout → next edition)?
4. Do different festival genres (film vs music vs theatre/book) share one model or diverge into different Types?
5. Is audience ticketing definitional, or can festival management exist without it?
6. What are the boundaries vs Event Management Platform, Event Ticketing, Event Agenda Management, Event Credential/Badge Management, Artist Booking, VMS, Cashless Venue, Convention/Exhibition, Attraction Management?
7. Historical check: would paper-era and earlier-generation festival production (wall schedules, spreadsheet accreditation, paper entry forms, laminate passes) still fit the definition?

## Representative Products

| Product | Pole | Segment / customers | Evidence layer |
|---|---|---|---|
| Eventival | Full festival production suite (central database + production office) | 100+ film festivals in ~50 countries; expanding to theatre festivals, book fairs, film schools, awards | A — official positioning pages + features page (detailed) |
| Eventree | Site operations & accreditation suite (crew/artist-facing) | UK festivals, tours, events ("UK industry standard for accreditation, advancing and operations"); Citizen Ticket | A — official homepage with full module descriptions + pricing |
| Eventive | Box office & audience platform (ticketing/passes/film guide/streaming) | 1,000 film festivals, 49 countries (incl. Sundance, Cannes, Telluride); arthouse cinemas | A — official product pages + help-center structure |
| Festhome | Submissions & selection slice | 6,236 festivals (vendor claim), 223,000 films selected; global film festivals | A — official filmmaker + festival-organizer pages |

Boundary neighbors consulted (already-processed sibling research, not re-sampled): Rosterfy (VMS, official site fetched this pass), Eventbrite/Cvent/EventsAir/Whova/Splash (event-management-platform pass), Event Ticketing Platform pass, Event Agenda Management pass, Event Credential/Badge Management pass, Cashless Venue Platform pass, Artist Booking Platform pass, Convention/Exhibition Management pass.

## Sources

Fetched 2026-09-07:

- Eventival — https://eventival.com , https://eventival.com/film-festivals/ , https://eventival.com/features/
- Eventree — https://www.eventree.co.uk
- Eventive — https://eventive.org , https://eventive.org/film-festivals , https://help.eventive.org
- Festhome — https://festhome.com , https://festivals.festhome.com
- Rosterfy (boundary check) — https://www.rosterfy.com

Unreachable this pass (recorded as sourcing limitation):

- Festival Pro (festivalpro.com) — direct fetch timed out ×2, Web Archive transport error ×1. Abandoned per network rules. Festival Pro is a known dedicated music/arts festival management suite; its absence means the music-festival full-suite pole (lineup + vendor + camping machinery) is NOT directly documented.
- FestKit (festkit.com) — transport error ×1. Abandoned.
- The Ticket Fairy (theticketfairy.com) — HTTP 403 ×1. Abandoned.
- Festival Genius (festivalgenius.com) — site has pivoted to a blog; no product documentation.
- InitLive (initlive.com) — now redirects to Bloomerang (nonprofit fundraising/CRM); no longer a festival-operations product.

## Product Observations

### Eventival (Layer A — official positioning + features pages)

Positioning: "Platform for Creative Organizations"; "born in the world of film festivals"; predecessor DataKal built at Karlovy Vary International Film Festival; 100+ film festivals in nearly 50 countries use it "as their central database and a toolbox … as well as a CRM and communication tool". Expanding into theatre festivals and performing arts, book fairs & literary festivals, film schools, awards, professional communities.

Scope statement (film-festivals page): "Film festivals combine an extraordinary range of activities: film submissions, selection, accreditation, guest hospitality, travel, scheduling, industry meetings, publications, websites, communications and much more. Bringing all of these workflows together in a single connected platform…"

Object model (features page):

- **Five interconnected database modules**: persons, companies, films, events, projects — each with predefined + custom fields, interlinked ("who does or did what and when"). The database is "your main data resource" year-round and per event.
- **Submissions**: unlimited customisable online submission forms (films, projects, plays, performances, photos), published on the festival website, entries flow directly into the film database; submission-fee payments via ~20 payment gateways; fee discount codes; can be combined with other submission platforms (preselect there, import selected films).
- **Reviews & selection**: core programmers review in Back Office; external screeners review in Visitor Page; Film Selection interface with comments, recommendations, adjustable ratings; selection status + program section assignment; mass mailing informs submitters of results.
- **Filmmaker collaboration**: selected filmmakers get access to provide catalogue entries, press kits, film-copy technical information through an online interface.
- **Film logistics**: digital/non-digital copies, technical details, movement tracking, logistics sheets, per-film fees.
- **Programming**: drag & drop schedule creation — explicitly described as digitizing the wall practice ("All festivals usually do this on the wall first, printing stickers with the film names and placing them in rows and lines that represent venues, dates and times"); warnings for time collisions and format conflicts; special screening categories (press, private); Q&A/intro sessions linked to people (moderators, translators, directors); short-film packages programmed as a whole.
- **Publications**: catalogue/brochure data proofed, translated, locked in a dedicated section; exported to physical publications, website, mobile app, ticketing systems, VOD platforms.
- **Accreditation & passes**: participant, guest, press, volunteer and staff accreditation; online registration and payment on Visitor Page; automatic confirmations and invoices; badge layouts with photos, names, access levels; print-state tracking (assigned/paid/printed/issued); QR/barcodes scanned at venues for attendance statistics.
- **Hospitality**: invitations with merge fields and personalized attachments (itineraries, invoices); RSVP online; international travel details; local transfer schedules with driver assignment; hotel/room capacity, rooming lists, vouchers; personalized guest schedules generated from invitations + screenings + meetings + travel + hotel.
- **Master schedule**: screenings, Q&As, press conferences, masterclasses, workshops, parties; double-booking warnings; venue colors; many export shapes.
- **Communications**: mass mailing tool (newsletters, press releases, invitations) with merge fields and personalized attachments; Mailchimp/SendGrid/Mailjet integrations; Topol email builder.
- **Volunteers**: recruitment forms, selection communication, staff accreditation, accommodation, travel, schedules.
- **Team coordination**: Notepad (notes on database items, tagging colleagues), task assignment with checklists/deadlines/reminders, project templates cloned across editions.
- **Press relations**: media database, accreditation requests, interview requests, itineraries.
- **Who Is Here**: participant directory with search/filter/contact; guests schedule meetings pre-event.
- **Year-round**: calendar of events/activities; membership management; donor/sponsor relations.
- **Multi-language**: Visitor Page in 15+ languages.
- **Sync**: publish schedule/film data to website, mobile app, ticketing system, VOD; Cinando (Cannes Marché) import.
- **Access control**: badge/QR scanning at venues; attendance statistics.

### Eventree (Layer A — official homepage, full module descriptions + pricing)

Positioning: "The UK industry standard for accreditation, advancing and operations at festivals, tours and other events"; developed over 10 years with UK events; operated by Citizen Ticket (Edinburgh). Value claim: "save thousands of admin hours … year after year".

Modules (homepage "How does it work?"):

- **Accreditation**: "No more emailing spreadsheets for contractors and tour managers to complete"; add/upload contacts, give them a set of passes to choose from, let them self-manage accreditation; organizer modifies and approves requests; team members emailed unique QR codes to collect passes on arrival.
- **Advancing**: "tell Eventree what you need from each person or company and it will take care of collating that information"; automatically sorted and routed to the right team member ("artist liaison receives all the riders").
- **Catering**: teams submit catering requests via dashboard; organizer approves; food collected with a pass issued via Eventree; usage logged to spot no-shows.
- **Forms**: recruit staff and volunteers, gather information from contractors and tour managers; submissions linked to profiles.
- **Document management**: collect documents (e.g. public liability insurance), automatic chasing of missing/expired documents, notifications on new uploads.
- **Health & safety**: online inductions attached to profiles; "nobody can get into site without completing one" — induction taken on phone, QR code presented at admission.
- **Passes and wristbands**: issue tracking; check-in scan shows exactly what to issue; pre-sorting views (e.g. tour-bus envelopes).
- **ID checks**: photo ID collection, on-arrival verification, background checks beforehand.
- **Integrations**: Google Drive document sync, form submissions into spreadsheets, "whatever you're currently using there's a high chance Eventree already knows how to talk to it".
- **Pricing**: per event, per year — Standard £1,750 / Pro £3,000 / Max £4,500 + VAT; tier caps on admin users (5/20/unlimited), passes issued (1,500/20,000/unlimited), forms received; paid-for passes, catering, linked wristbands/passes, passouts only in higher tiers.
- **Staffing service**: pay-as-you-go trained accreditation staff.
- Notably ABSENT from the homepage: audience ticketing, lineup/schedule programming, camping, vendor management. Eventree manages the festival's working population and site access, not the artistic program or audience sales.

### Eventive (Layer A — official product pages + help-center structure)

Positioning: "The seamless platform for independent cinema"; "ticketing, pass management, audience data, year-round member relations, digital promotions, streaming, online film guides, and balloting into a single intelligent platform". Clients: Sundance, Cannes, Telluride, Fantastic Fest, CPH:DOX, Sheffield DocFest, etc. Vendor claims: 1,000 festivals, 49 countries, 10M tickets issued.

Film-festival offering (film-festivals page):

- **Ticketing**: passes, single tickets, rush line, pay-what-you-can; "unifies ticketing levels, management, logistics and scanning"; box office on desktop/mobile/iPad; Eventive Scanner / Terminal hardware; ticket and pass printing; item sales (merch, concessions).
- **Film guide**: "an interactive film guide that also sells tickets" — "fully responsive, genre-segmented, and searchable film guide"; festival website functioning on desktop and mobile; one-click ticket reservations.
- **Passes & benefits**: "infinite combination of pass rules to automatically apply benefits, no discount codes required"; custom-branded passes with names, affiliations, QR codes.
- **Audience data**: insights, analytics, CRM integrations (Mailchimp, Salesforce, Eventival, Zapier, Google Analytics); donor/member/sponsor engagement.
- **Virtual**: VOD, live-streaming, chat; Eventive TV app; hybrid festivals.
- **Balloting**: generate, collect, tabulate app & paper audience ballots (awards).
- **Memberships & year-round programming**: "Eventive doesn't stop when the festival ends" — year-round member relations, automated membership benefits.
- **Reserved seating**: seat maps available.
- Help-center collections (Tier 1 structure): Getting Started; Events & Tickets; Eventive Virtual; Customizing Your Eventive Site; Box Office; Films; Passes; Memberships & Year-Round Programming; Discounts; Balloting; Item Sales; Reporting & Analytics; Financials & Payments; Integrations; People; Reserved Seating; Hardware & Equipment; Eventive for Attendees.
- Pricing: 5% + 99c per paid item; no fees on free tickets, donations, cash/check sales.
- Explicit integration with Eventival (film-festival management suite) — the two products interlock: Eventival manages production/people, Eventive sells admission.

### Festhome (Layer A — official filmmaker + festival-organizer pages)

Positioning: film-festival submission platform ("Submit to the best festivals"); two-sided: filmmakers submit, festival organizers manage selection. Vendor claims: 6,236 festivals, 76% of last year's most successful films, 223,000 films selected, 2,200 fraudulent festivals detected and rejected.

Organizer-side features (festivals.festhome.com):

- Selection process management: selection notification to all submitters, selection statuses, mass mailing.
- Screening Room: watch entries in streaming quality.
- Statistics on submissions; film data views.
- Entry-fee management: Festhome handles accounting and remits entry fees monthly.
- Export: Excel/CSV, database export, "synchronised with Eventival".
- Juror/curator accounts: free accounts for festival members; assign all or specific films/sections; vote or tag.
- Non-exclusive: festivals can use other submission platforms alongside.
- Free of charge for partner festivals; multilingual; handles projection files up to 20 GB.
- Festhome TV: VoD platform for online festivals.

Festhome is a **slice product**: it owns the submissions/selection office only — no program scheduling, no accreditation, no hospitality, no admission. It interlocks with Eventival (sync) the way Eventive does.

### Rosterfy (Layer A — boundary check only)

Volunteer Management Software: recruit & onboard, train & induct, advanced scheduling, reward & retain, insights; volunteer app; built for organizations managing 100+ volunteers; used by SXSW (2,000 volunteers, 500k+ attendees), sports federations, cities, nonprofits. **Not festival management**: no festival occasion, no program, no admission machinery — pure workforce management. Festivals appear as one customer segment among many. Confirms that volunteer coordination inside festival management is one participant category, while dedicated VMS is its own Type.

## Cross-product Comparison

| Structure | Eventival | Eventree | Eventive | Festhome |
|---|---|---|---|---|
| Festival/edition as organizing container | Yes — database spans year-round + editions; queries/exports cloned across editions | Yes — licensed per event per year; "year after year" | Yes — events + year-round programming/memberships | Yes — festival editions with calls/deadlines |
| Participant records beyond the audience | Yes — persons/companies modules: filmmakers, guests, press, volunteers, staff, industry | Yes — contacts: artists, crew, contractors, tour managers, staff, volunteers | Yes — People collection: audience, passholders, members, donors, sponsors | Yes — submitters/filmmakers |
| Access entitlements (passes/accreditation/tickets) | Yes — accreditation types, badges with access levels, QR scanning | Yes — core: passes/wristbands, approval workflow, check-in issuance | Yes — core: tickets/passes with rules, QR scanning | No (submissions only) |
| Program/schedule management | Yes — drag & drop programming, collision warnings, master schedule | No (not on homepage) | Yes — screenings, film guide, schedule browsing | Partial — selection into sections, no schedule |
| Submissions & selection intake | Yes — custom forms, fees, reviews, statuses | Partial — forms for staff/volunteers/contractors (not artistic submissions) | No | Yes — core |
| Publications (catalogue/guide/website sync) | Yes — proofed/translated/locked, exported to web/app/ticketing | No | Yes — film guide/website | No |
| Hospitality & logistics (travel/accommodation/catering) | Yes — travel, transfers, hotels, itineraries | Yes — catering requests, meal passes | No | No |
| Communications (mass mail) | Yes — newsletters, press releases, merge fields | Yes — implied via forms/notifications (emailing QR codes) | Yes — engagement messages, CRM integrations | Yes — selection notifications |
| Audience admission & box office | Partial — syncs to external ticketing; badge scanning for attendance | No | Yes — core | No |
| Edition continuity | Yes — clone queries/templates across editions | Yes — annual per-event licensing, repeat clients | Yes — year-round memberships | Yes — recurring calls |
| Team coordination | Yes — Notepad, tasks, roles | Yes — admin users, routing to team members | Yes — unified dashboard, staff | Yes — juror accounts |
| Reporting/analytics | Yes | Partial (usage logging) | Yes | Yes (submission statistics) |

Reading of the comparison:

- The **shared spine** across all four: a festival/edition container + identified participant records with roles + (for all but the submissions slice) access entitlements.
- The **program** is present in the film-pole products (Eventival, Eventive) but absent from Eventree — the UK festival-operations standard manages the people and site access, not the lineup. Program management is therefore common but NOT definitional.
- **Audience ticketing** is present in Eventive, delegated outward by Eventival, and absent from Eventree. Not definitional.
- **Submissions/selection** is the film-genre intake machinery (Eventival, Festhome); Eventree's equivalent intake is advancing/forms for crew and contractors. The generalizable structure is *structured intake from participants before the event*, not submissions per se.
- **Hospitality** (travel/hotels/catering) appears in both the film pole (Eventival) and the music pole (Eventree catering) — participant logistics is a shared theme, shaped by genre.
- Each product owns a different "office" of the festival: Eventival = central production office & database; Eventree = site operations & accreditation office; Eventive = box office & audience platform; Festhome = submissions office. The Type is realized as a family of office-shaped products around one shared spine.

## Canonical Model

### L0 — Defining Invariant (minimal, jointly held)

Three structures held jointly:

1. **The festival as a composite occasion of record.** An organizer-defined, dated, public event that spans multiple days and is composed of many program parts across multiple venues/stages, recurring across editions; the container to which every record attaches. Remove it → generic single-event tool or CRM.
2. **The participant ecosystem as managed records.** The festival's people — performers/filmmakers and their parties, staff and volunteers, contractors/vendors, press, guests, and the audience — held as identified records with roles, statuses, and festival-specific attributes, worked over time. Remove it → pure schedule or pure ticketing tool.
3. **Access entitlements issued against those records.** Passes, accreditations, tickets, wristbands — entitlements that define who may enter which spaces and program parts, with issuance and check-in tracked. Remove it → a planning/database tool without gates.

Jointly-held is load-bearing: 1+2 without 3 = a participant CRM; 1+3 without 2 = anonymous ticketing; 2+3 without 1 = generic credentialing/badging (the Event Credential/Badge Management sibling).

### L1 — Common Mature Structure

- **Program/schedule management** — program parts placed across venues/days/times with conflict detection, published outward to websites/apps/ticketing (Eventival, Eventive; absent from Eventree).
- **Structured participant intake** — submissions (film genre), advancing/forms (music genre), volunteer calls; information routed to the right team members.
- **Publications** — catalogue/film guide data prepared, proofed, exported to web/app/print/ticketing.
- **Hospitality & logistics** — travel, transfers, accommodation, itineraries, catering for participants.
- **Communications** — mass mail with merge fields, notifications, press releases.
- **Edition continuity** — data, templates, and relationships carried across editions; year-round operation.
- **Team coordination** — roles, tasks, notes, admin users.
- **Reporting/analytics** — submissions, attendance, sales, usage.

### L2 — Variant / Optional Structure

- **Genre substrate**: film (submissions/jury/screenings/guest hospitality), music & tours (advancing/catering/site access), theatre, book fairs & literary festivals, food & cultural festivals.
- **Which production office the product owns**: central production database (Eventival) / site operations & accreditation (Eventree) / box office & audience (Eventive) / submissions office (Festhome).
- **Audience-facing vs crew-facing**: some products sell admission (Eventive), others never touch audience sales (Eventree).
- **Virtual/streaming layer** (Eventive Virtual), **year-round memberships** (Eventive), **awards/balloting** (Eventive, Eventival voting).
- **Pricing shape**: per-event annual licensing (Eventree) vs SaaS per-transaction (Eventive) vs free-for-festivals (Festhome).
- **Paid-for passes, passouts, linked wristbands** (Eventree higher tiers).

### L3 — Vendor-specific (research notes only)

- Eventival: five-module database (persons/companies/films/events/projects), Cinando import, Notepad, Visitor Page (15+ languages), DataKal heritage, ~20 payment gateways, Who Is Here meeting scheduler.
- Eventree: per-event annual tiers with caps (admin users/passes/forms), pay-as-you-go accreditation staff, passouts, linked wristbands, ID checks with background checks.
- Eventive: balloting (app & paper), Eventive TV app, Configurator, 5% + 99c pricing, rush line, pay-what-you-can.
- Festhome: fraud detection (2,200 fraudulent festivals rejected), free-for-partner-festivals model, monthly entry-fee remittance, Festhome TV, 20 GB projection files.

## Vendor-specific Findings

See L3. Additionally: Eventival's features page contains the research's best historical anchor — it explicitly describes the pre-software practice the programming tool replaces ("All festivals usually do this on the wall first, printing stickers with the film names and placing them in rows and lines that represent venues, dates and times"). Eventree's homepage similarly anchors against "emailing spreadsheets for contractors and tour managers to complete".

## Boundary Findings

1. **vs Event Management Platform (sharpest seam).** Event Management's center: event record + registration surface + registrant (audience) population + organizer management of the registration lifecycle. Festival Management's center: the composite occasion + the multi-category participant ecosystem + entitlements. Discriminators: (a) managed population — audience registrants vs the whole production ecosystem (performers/filmmakers, crew, volunteers, vendors, press, guests, audience); (b) occasion shape — a single happening vs a composite, recurring, multi-part occasion; (c) center of gravity — the registration flow vs production coordination (intake, selection, entitlements, hospitality). Generic event platforms can run festival ticketing and even simple agendas; festival-specific products are built around the ecosystem and entitlement logic (Eventree has no audience registration at all, yet is unmistakably festival software). This ratifies the event-management-platform pass's note that festival is "documented as their own Types when their substrate changes the model" — the substrate does change the model. Keep both Types.
2. **vs Event Ticketing Platform.** Ticketing is one capability of festival management (and often delegated to a sibling product — Eventival ↔ Eventive integration). Eventree proves festival management exists without audience ticketing. Conversely, a ticketing platform has no participant ecosystem, submissions, or hospitality.
3. **vs Event Agenda Management.** The program/schedule is one structure inside festival management (and absent from Eventree). Agenda Management's center is the program record and its published renderings; festival management's center is the occasion + ecosystem the program serves.
4. **vs Event Credential / Badge Management.** Accreditation inside festival management is embedded in the participant lifecycle — entitlement requests tie to advancing, documents, inductions, catering, hospitality (Eventree, Eventival). The badge/credential sibling centers on the credential artifact and its issuance/check-in. Cross-references that pass's flagged "security-led accreditation pole" (sports/festivals/venues, zone-based entitlement matrices): festival accreditation as observed here is participant-lifecycle-wide, not zone-matrix-centric; the two poles are related but distinct. Joint review recommended when that pole is processed.
5. **vs Artist Booking Platform.** Booking platforms transact engagements between artists and buyers (festivals are one buyer type). Festival management coordinates the artists already booked *inside the production* — advancing (riders, documents), accreditation, catering, hospitality. Sequential, not the same Type.
6. **vs Cashless Venue Platform.** Refines that pass's characterization ("festival management's object is the event program"): the observed object set is the occasion + participant ecosystem + entitlements; the program is common-but-not-universal. Cashless platforms own credentials-as-wallets and transactions; festival management owns the production relationship.
7. **vs Volunteer Management System (Rosterfy).** Volunteers are one participant category inside festival management (recruitment forms, accreditation, scheduling). A VMS is workforce-generic across industries with no festival occasion, program, or admission. Keep both; festival volunteer coordination is an overlap zone.
8. **vs Convention / Exhibition Management.** Exhibitions organize exhibitors/booths for a marketplace; festivals organize a program and audience (plus production ecosystem). Different core objects; both are large produced events.
9. **vs Attraction Management System / Theme Park Management.** Attractions are venue-side operations (the venue is the asset); festivals are organizer-side productions (the occasion is the asset, the site is temporary). Different operator.
10. **Variant-vs-Type check on genre poles.** Film, music, theatre, and book-festival realizations share the L0 spine; genre machinery (submissions/jury vs advancing/catering) sits at L2. No genre pole requires splitting into a separate Type. The film-festival submissions slice (Festhome) is a slice, not a separate Type — analogous to Event Registration Platform's relationship to Event Management Platform.

## Uncertainties

1. **Music-festival full-suite machinery not directly documented.** Festival Pro and FestKit (the known dedicated music/arts festival suites) were unreachable this pass. Vendor management (food/craft vendors), camping/accommodation fields, and site-plan machinery are widely associated with music festivals but were NOT observed in any sampled product. They are deliberately NOT claimed as standard capabilities in the final document.
2. **Film pole over-weighted** (3 of 4 samples). Mitigated by Eventree (music/tour production pole) and by the cross-pole spine being consistent; genre machinery is kept at variant level.
3. **Exact state names, limits, and defaults** (e.g. accreditation statuses, pass-tier caps) are product-specific and kept in these notes, not asserted in the final document.
4. **The security-led accreditation pole** (zone-based entitlement matrices for sports/festivals/venues) remains unverified from the event-credential-badge-management pass; this pass's festival accreditation evidence (participant-lifecycle-wide) does not confirm or deny that pole.

## Historical / Market-Sample Check

- **Paper-era practice**: wall-sticker scheduling (explicitly described by Eventival as what programming software replaces), spreadsheet-and-email accreditation (explicitly described by Eventree as what it replaces), paper entry forms and mailed screeners (the practice Festhome's domain digitizes), laminate passes and gate lists. The L0 structures — a composite occasion, a participant ecosystem, entitlements governing entry — all existed in paper form. The definition does not depend on digital ticketing, RFID, apps, or streaming.
- **Earlier-generation software**: Eventival's predecessor DataKal (built at Karlovy Vary IFF) shows festival database software predating the current platform generation.
- **Regional breadth**: Czech/Prague-based Eventival (global film festivals), UK Eventree (UK festivals/tours), US Eventive (North American film festivals), Spanish Festhome (global). No single region's implementation defines the Type.
- Conclusion: the definition passes the historical check; nothing in L0 assumes the current mobile/RFID/SaaS era.

## Final Synthesis

Festival Management is the organizer-side production-management Type for festivals: software that holds the festival as a composite, recurring occasion of record, manages the festival's participant ecosystem (performers/filmmakers and their parties, staff/volunteers, contractors, press, guests, audience) as identified records with roles, and issues and tracks the access entitlements (passes, accreditation, tickets, wristbands) that govern who enters which spaces and program parts. Around that spine, mature products commonly add program/schedule management, structured participant intake (submissions or advancing), publications, hospitality and logistics, communications, edition continuity, team coordination, and reporting. The market realizes the Type as a family of office-shaped products — central production database, site operations & accreditation, box office & audience platform, submissions office — that interlock (Eventival ↔ Eventive ↔ Festhome sync) rather than as one monolith. The festival substrate (multi-category participant ecosystem + composite recurring occasion + entitlement logic) is different enough from the generic event substrate (registration flow + attendee population) to stand as its own Type; the sharpest boundary is with Event Management Platform, and the most important internal nuance is that neither audience ticketing nor program scheduling is definitional — the participant ecosystem and its entitlements are.
