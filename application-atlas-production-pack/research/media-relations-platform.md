# Research Notes — Media Relations Platform

Research date: **2026-09-08**

## Research Goal

Understand what a Media Relations Platform actually is as an Application Type: what objects exist inside it, what workflow a PR/communications team runs through it, and — because this leaf carries a joint-review flag from the public-relations-management-platform pass — whether it is a distinct Type (the relationship-and-pitching slice) or a consolidation view of Public Relations Management Platform. Also hold the seam recorded by the media-monitoring-platform pass (journalist-database/outreach modules inside monitoring suites).

## Initial Boundary

- Under DIRECTORY §06 Marketing, Advertising & Growth, PR cluster. Siblings: Public Relations Management Platform (processed 2026-09-06), Press Release Distribution Platform (processed 2026-09-06), Media Monitoring Platform (processed 2026-09-08), Social Listening Platform (processed), Social Media Management Platform (unprocessed).
- **Carried joint-review flag (from public-relations-management-platform pass):** "closest boundary pair in the PR cluster — both center media relationship records and pitch/outreach sending, and market vocabulary straddles (Meltwater sells its 'Media Relations' capability inside the full intelligence suite; Agility's all-in-one platform lives on a /media-relations solution page; Prezly self-describes as a 'PR CRM') — boundary held in that pass on scope of the loop: media relations = the relationship-and-pitching slice (database + lists + pitches), PR management = that slice plus organized campaigns, coverage capture, and reporting across the whole PR function; candidate outcomes are two Types by scope (slice vs whole function) or a consolidation view."
- **Carried flag (from media-monitoring-platform pass):** "journalist-database/outreach modules inside monitoring suites (Cision Journalist Outreach; Meltwater Media Relations) are that Type's subject matter; monitoring itself has no outreach."
- Working hypothesis before research: the journalist-relationship and pitching system — media contact records + discovery + media lists + personalized tracked pitches + per-contact relationship memory. The question is whether that slice is a definable Type.
- Likely confusions: PR Management (whole function), Media Monitoring (listening, no outreach), Press Release Distribution (gated network broadcast), Email Marketing (same send shape, different audience), CRM (structural analogy), Sales Engagement/Outreach Sequencing (same machinery, sales audience), journalist-source request marketplaces (journalist-initiated), plain media directories (database without sending).

## Research Questions

1. What are the core objects (journalist/contact record, media list, pitch, engagement events, relationship history) and how do they relate?
2. How does discovery work (vendor-maintained database vs customer-built contacts; search/filter dimensions; AI matching)?
3. How do media lists work (creation, saving, sharing, segmentation, import/enrich)?
4. How is pitching done (1:1 vs bulk, personalization, templates, AI drafting, scheduling/follow-ups, own-domain sending)?
5. How is engagement tracked (opens/clicks/replies/bounces; per-contact responsiveness)?
6. What relationship memory is kept per contact (CRM-style history, interaction log, duplicate-pitch avoidance)?
7. **Joint-review discriminator:** do these products include organized campaigns, coverage capture, and function-wide reporting as first-class structures — or is the pitch/relationship loop the organizing frame?
8. What roles/collaboration machinery exists (shared lists, tasks, agency access)?
9. What is the suite posture — standalone vs named module/capability inside a suite?
10. Would older/regional practice (rolodex + typed pitches + follow-up notes; printed media directories) still fit the definition?

## Representative Products

| Product | Pole / philosophy | Evidence quality |
|---|---|---|
| Meltwater (Media Relations capability + Media Database product) | suite capability sold under the leaf's own name; intelligence-first | A/B — official capability page + product page fetched (Tier 2) |
| Cision (CisionOne Journalist Outreach) | suite module; incumbent database | A/B — official module page fetched (Tier 2) |
| Prowly (now Semrush AI PR Toolkit) | self-serve AI toolkit; database + outreach | A/B — official page fetched (Tier 2) |
| Roxhill Media | UK regional database-first specialist | A/B — official database + list-building pages fetched (Tier 2) |
| JustReachOut | pitch-first self-serve; no proprietary-database claim | A/B — official homepage + tool page fetched (Tier 2) |
| Muck Rack | journalist-database-first (market's most prominent "media relations" brand) | ✗ — 403 on muckrack.com ×2 (prior pass) + help.muckrack.com ×1 (this pass); abandoned per network rule; market context only |
| Prezly | PR-CRM framing, customer-built contacts | cross-reference — Tier-1 help-center evidence documented in the public-relations-management-platform pass research notes |

Sampling rationale: suite capability sold under the leaf's own name (Meltwater) + incumbent suite module (Cision) + self-serve toolkit (Prowly/Semrush) + regional database specialist (Roxhill) + pitch-first thin pole (JustReachOut), plus the PR pass's Tier-1 Prezly evidence as cross-reference. Six product philosophies across enterprise/mid-market/self-serve tiers and US/UK geographies. Muck Rack's absence weakens the database-first pole's direct evidence; mitigated by Roxhill (database-first with documented tool structure) and the module pages.

## Sources

- Cision — https://www.cision.com/journalist-outreach/ (retrieved 2026-09-08)
- Meltwater — https://www.meltwater.com/en/capabilities/media-relations ; https://www.meltwater.com/en/products/media-database (retrieved 2026-09-08); https://www.meltwater.com/en/products/media-relations → 404
- Prowly / Semrush — https://www.prowly.com/media-database (retrieved 2026-09-08; page fronts the Semrush AI PR Toolkit)
- Roxhill — https://roxhillmedia.com/ ; https://roxhillmedia.com/media-database/ ; https://roxhillmedia.com/media-database/list-building-tool/ (retrieved 2026-09-08)
- JustReachOut — https://justreachout.io/ ; https://justreachout.io/tools/journalist-outreach-tool (retrieved 2026-09-08)
- Muck Rack — https://help.muckrack.com/ → 403 (this pass); muckrack.com root + /pr-software → 403 ×2 (prior pass). Abandoned; market context only.
- Cross-referenced sibling research notes: research/public-relations-management-platform.md (Prezly Tier-1 evidence; Cision/Meltwater/Onclusive/Agility/Prowly suite-level observations); research/media-monitoring-platform.md; research/press-release-distribution-platform.md

## Product Observations

### Meltwater — Media Relations capability + Media Database product

Evidence: official capability page (/en/capabilities/media-relations) + product page (/en/products/media-database).

Key observations:

- The vendor sells **"Media Relations" as a named capability** with its own page, product tour, and FAQ — the market's own use of the leaf's name. FAQ: "A traditional media database helps you find contacts. Meltwater provides a complete media relations platform, including AI-powered journalist discovery, outreach tracking, monitoring integration, and executive reporting."
- **Capability-page workflow (vendor's own six steps):** Discover the right journalists (AI-powered search using your pitch/key messages) → Build smarter media lists (labels, filters, contact update alerts) → Send personalized outreach (personalized or mass emails directly from the platform) → Track engagement & coverage (opens/clicks; secured coverage; visibility gaps) → Measure PR impact (share of voice, campaign momentum, outreach→earned-media outcomes) → Report to leadership (executive-ready dashboards).
- **Relationship-management tab:** "Go beyond static contact lists with refreshed journalist profiles, outreach history, and better context for every interaction" — unified journalist profiles, outreach history in one place, beat/role change alerts, **avoid duplicate pitching**.
- **In-house control tab:** own contacts and results, govern shared access, multi-user permissions so agencies can collaborate while the customer maintains governance/ownership.
- **Media database product page:** continuously updated journalist profiles (vendor claims: AI crawlers + 90+ analysts; critical changes within 24–48 hours; ~7–8% bounce rate; 800,000+ contacts; Dow Jones/WSJ exclusive content) — all vendor-stated figures, kept out of canonical claims.
- Discovery: natural-language search ("tech journalists covering AI regulation"), filters by beat/location/outlet/recent coverage; "analyzes what journalists are writing about and recommends the most relevant contacts"; AI-assisted list building and pitch suggestions.
- Outreach: email outreach with engagement tracking; FAQ: "track individual open rates, clicks, and bounce types directly within the Outreach workflow"; "CRM-style relationship history and tracking"; sending "from your own domain" for deliverability; import and enrich existing media lists; integrated press release distribution; GDPR-compliant posture (opt-in data practices, opt-out handling).
- Feature list names: advanced journalist search with filters for beat/outlet/geography; AI-assisted list building and journalist recommendations; real-time contact enrichment and profile updates; coverage insights including recent articles and social activity; media list management and collaboration tools; email outreach with engagement tracking; bounce/open/click performance analytics; CRM-style relationship history and tracking; import and enrich existing media lists; integrated press release distribution.
- Positioning against "database-only tools": "Unlike database-only tools, Meltwater combines media intelligence, monitoring, and analytics in one platform" — the vendor itself names the database-only pole as a distinct (lesser) category.

### Cision — CisionOne Journalist Outreach module

Evidence: official module page (same page as fetched in the PR pass; re-confirmed 2026-09-08).

Key observations:

- Sold as a **named module** ("Journalist Outreach") beside Media Monitoring, Instant Insights & Reporting, Social Listening & Management inside CisionOne — the monitoring pass's flag confirmed: the media-relations slice is packaged as its own module.
- "Craft more powerful pitches and enhance your media coverage with the industry's most accurate, comprehensive media database and AI-powered outreach tool."
- Database: "human-curated database of verified journalists and media outlets" (vendor figure: 500,000+ media profiles across 225 countries/territories — vendor claim).
- Find: "powerful search tools, advanced filters, and insights into the topics journalists are covering."
- Send: "branded media releases with our intuitive email builder and pre-saved templates, AI-powered recommendations to craft high-impact pitches."
- Measure: "Track engagement with your media releases to understand which stories and outreach methods resonate most with your target journalists. Combined with your earned media coverage, see how a media release drove story pickup."
- Team alignment: "centralizing all journalist interactions in one convenient place. Build and share media lists, capture important phone and email conversations, assign tasks to the right team members, and when the time is right, generate reports."
- Media Brief: free weekly roundup of journalist moves/editorial shifts (vendor community layer).

### Prowly (now Semrush AI PR Toolkit)

Evidence: official page (prowly.com/media-database now fronts the Semrush product; rebrand observed in PR pass, re-confirmed).

Key observations:

- Modules: **AI-Cited Media Database** (outlets that shape LLM responses; journalist profiles; audience/traffic data; AI search/keywords/filters), **Email Outreach and Analytics** (AI-drafted emails and press releases; engagement tracking; **scheduled follow-ups based on recipient behavior**; "automatically track which pitches earned media mentions"), Media Monitoring, Strategic Intelligence & Benchmarking.
- FAQ anticipates customer-owned contacts: "What if I already have press contacts?" — import supported (self-serve posture).
- The automatic pitch→mention tracking is direct evidence of outreach→coverage linkage in a self-serve product.

### Roxhill Media

Evidence: official homepage, media-database page, list-building page (Tier 2, operationally detailed).

Key observations:

- UK regional database-first specialist: "Media intelligence you can trust. One login. Multiple solutions." Products: Media Database, Media Monitoring, Spokespeople, Bespoke Insights. The **media database is the lead product**.
- Database figures (vendor claims): 6,781,235 tagged articles; 40k+ outlets; 250k+ journalists.
- Discovery: "Search by topic, sector, keyword and company in seconds, and create a target list of journalists waiting to hear your story. This gives you added insight to ensure legitimate interest, and keep you GDPR-compliant."
- Journalist profiles: "personal bios, social feeds, and pitching preferences" — live social feeds inside the profile; "always visit journalists' profiles to look over their topic coverage, and ensure that your communications align with their interests."
- **List building (documented workflow):** "Simply name your list, search for relevant journalists, and add them to your list." Daily data updates; "automated alerts to your inbox when a contact changes roles"; "Avoid bouncebacks."
- **GDPR machinery:** "company-wide GDPR view. Contacts that have opted out of receiving communications from you and your colleagues will appear as GDPR Rejected across all your shared lists."
- Sending: "creating personalised emails that look and feel tailored to your recipients, and distributing your press releases" — list-based distribution (not a PRD-style gated network).
- Alerts: "instant customisable alerts… never miss a journalist move or promotion" (vendor figure: 50+ moves updated per day); alerts for article headlines, social posts, media requests.
- Trend analysis ("Pinpoint"): track keyword mentions across sources to "pitch at the perfect time."
- PR opportunities directory: "search slots from over 200 outlets" (vendor figure).
- Community/events layer: journalist Q&As, speed-pitching events, pitching guides — distinctive relationship-ecosystem posture.
- Client testimonial evidence of the workflow: "Being able to have all your agency's key journalists and media on hand allows us to work more productively"; "build stronger, more targeted relationships with the right journalists."

### JustReachOut

Evidence: official homepage + journalist-outreach tool page (Tier 2; homepage partially truncated by base64 noise — tool page clean).

Key observations:

- Pitch-first self-serve posture: "Find and pitch relevant journalists faster than ever before"; "You should be pitching journalists yourself" (DIY-PR framing, anti-agency).
- Tool page: "Easily find the journalists writing about your niche"; "in depth journalist contact info"; **"See how responsive each journalist is to pitches"** (per-contact responsiveness indicator); "Let AI craft the pitch email in seconds"; "Schedule automatic followups"; "Build relationships that last for future press features."
- How-It-Works footer: Targeted Lists of Journalists → PR Outreach Guidance → Pitch Analytics.
- Tool suite: Journalist Outreach, Pitch Requests (journalist-initiated requests), Podcast Outreach, Broken Link Building, Guest Post Outreach — outreach extensions beyond press pitching (SEO-adjacent).
- No proprietary-database scale claims on fetched pages; no campaign/coverage/reporting apparatus evidenced — the closest observed shape to the pure relationship/pitch slice.

### Muck Rack (unreachable)

403 on three attempts across two passes (root, /pr-software, help subdomain). Known in the market as a journalist-database-first PR platform (media database + pitches + monitoring + reports). No claims drawn from it; retained as market context only.

### Cross-reference — Prezly (from the public-relations-management-platform pass, Tier-1 help center)

- "PR CRM" framing: contacts (journalists, influencers, stakeholders) with "details, preferences, and consent status"; Pitches (1:1 personalized emails, templates, open/click tracking); "full history of every email sent, every story opened, and every piece of coverage earned. All tied directly to your contact records."
- No proprietary journalist database — contacts customer-built/imported; paid "curated list building service" offered instead.
- Prezly also ships Campaigns (mass emails), Coverage log, Newsrooms, reporting — i.e., it satisfies the PR Management L0; its relationship-first emphasis is the pole that pass documented.

## Cross-product Comparison

| Dimension | Meltwater | Cision | Prowly/Semrush | Roxhill | JustReachOut | Prezly (cross-ref) | Layer |
|---|---|---|---|---|---|---|---|
| Media contact records as managed objects (journalists/outlets with beats/topics/channels) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Core |
| Vendor-maintained discoverable journalist database (search/filter by beat, topic, location, outlet, recent coverage) | ✓ | ✓ | ✓ | ✓ | ✓ (journalist search; no scale claims) | ✗ (customer-built; service offered) | Common |
| AI recommendations / matching (contacts for your story) | ✓ | ✓ | ✓ | ✗ (not evidenced) | ✓ (AI-crafted pitches; find journalists) | partial | Common |
| Saved/shareable media lists; segmentation | ✓ | ✓ ("build and share media lists") | ✓ | ✓ (name→search→add; shared lists) | ✓ ("targeted lists") | ✓ (tags/views/filters) | Core |
| Import/enrich customer-owned contact lists | ✓ | (not evidenced on page) | ✓ (FAQ) | (not evidenced) | (not evidenced) | ✓ | Common |
| Pitch/outreach sending from the platform (personalized; templates; AI drafting) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (Pitches) | Core |
| Engagement tracking per send/contact (opens/clicks/replies/bounces) | ✓ (FAQ explicit) | ✓ | ✓ | ✓ (distribution analytics) | ✓ (responsiveness; pitch analytics) | ✓ | Core |
| Per-contact relationship history (CRM-style; outreach history; interaction log) | ✓ ("CRM-style relationship history"; "avoid duplicate pitching") | ✓ ("centralizing all journalist interactions"; capture conversations) | ✓ (implied by tracking) | partial (profiles/preferences; opt-out state) | ✓ (responsiveness per journalist) | ✓ (activity feed) | Common |
| Follow-up machinery (scheduled/behavior-triggered) | (not evidenced) | (not evidenced) | ✓ (scheduled follow-ups based on recipient behavior) | (not evidenced) | ✓ (automatic followups) | (not evidenced) | Common |
| Own-domain sending / deliverability | ✓ | (not evidenced) | (not evidenced) | (not evidenced) | (not evidenced) | ✓ (from PR pass) | Common |
| Consent/GDPR machinery (opt-out state, company-wide views, legitimate interest) | ✓ | (claimed) | (not evidenced) | ✓ (GDPR Rejected across shared lists) | (not evidenced) | ✓ (consent status; enforced unsubscribe) | Common |
| Journalist-move / role-change alerts | ✓ | ✓ (Media Brief) | (not evidenced) | ✓ (role-change alerts; 50+/day claim) | (not evidenced) | ✗ | Common |
| Pitch→coverage linkage (which pitches earned mentions) | ✓ | ✓ (release→pickup) | ✓ (automatic) | (via monitoring products) | (not evidenced) | ✓ (coverage tied to contacts) | Common |
| Organized campaigns as first-class container | ✓ (suite) | ✓ (suite) | ✓ (campaign dashboard) | ✗ (not evidenced) | ✗ (not evidenced) | ✓ (Campaigns) | PR-Management marker, not this Type's core |
| Automated media monitoring engine | ✓ (suite) | ✓ (suite module) | ✓ | ✓ (separate product) | ✗ | ✗ (integrations) | Suite extension |
| Function-wide reporting (SOV, sentiment, executive/white-label) | ✓ (suite) | ✓ (suite) | ✓ (benchmarking) | ✓ (bespoke insights) | ✗ | ✓ | Suite extension |
| Press-release distribution | ✓ (integrated feature) | ✓ (PR Newswire, separate product) | ✗ | ✓ (list-based distribution tool) | ✗ | ✗ | Variant |
| Outreach extensions (podcast, guest-post, link-building, journalist requests) | ✗ | ✗ | ✗ | ✓ (requests/opportunities directory) | ✓ (tool suite) | ✗ | Variant |
| Community/events layer (journalist Q&As, speed pitching) | ✗ | ✓ (Media Brief newsletter) | ✗ | ✓ (events program) | ✗ (training videos) | ✗ | Variant |
| Agency/multi-user governance | ✓ (FAQ explicit) | ✓ | (self-serve) | ✓ (agency testimonials) | ✗ | ✓ (roles) | Common |
| Commercial model | enterprise | enterprise | self-serve | quote/demo | self-serve + trial | self-serve + plans | Variant |

## Canonical Model (abstraction)

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a media relations platform:

```text
Media contact records (journalists / outlets / influencers as managed objects)
└── Media list building (selecting and grouping contacts into saved, shareable outreach lists)
    └── Tracked pitch sending (personalized outbound pitches to selected contacts,
        engagement recorded per send and per contact)
```

Three properties:

1. **Media contact records** — the platform holds journalists/outlets/influencers as first-class managed records carrying PR-relevant attributes (outlet/role, topics/beat, contact channels). Without this it is a generic email tool.
2. **Media list building** — contacts are selected and grouped into reusable, shareable outreach lists (per story/announcement), rather than one-off address entry. Without this it is an address book with a send button.
3. **Tracked pitch sending** — the platform is the sending surface for personalized pitches to selected media contacts and records how each send and each contact engaged. Without this it is a media database (directory); without tracking it is a mail-merge blaster.

Removal tests: remove contact records → email marketing (customer audiences); remove list building → plain contact manager; remove sending → media database/directory; remove tracking → mail-merge sender (thin pole, below the Type).

**Joint-review discriminator:** the L0 deliberately excludes organized campaigns, coverage capture, and function-wide reporting. Those are the additions that turn the slice into a Public Relations Management Platform (that pass's L0 legs 2 and 4). A product whose organizing frame is the journalist relationship and the pitch loop is a Media Relations Platform even if it lacks campaigns/coverage/reporting; a product that adds those as first-class structures is a PR Management Platform (which necessarily contains a media-relations capability).

### L1 — Common Mature Structure

Very common in mature modern products, not required to recognize the Type:

- vendor-maintained, continuously enriched journalist database (search/filter by beat, topic, location, outlet, recent coverage; AI recommendations of contacts for a story; role-change/move alerts)
- per-contact relationship history (CRM-style activity log: outreach history, engagement, notes, captured conversations; responsiveness indicators; duplicate-pitch avoidance)
- personalization at scale (merge fields, templates, AI-drafted pitches)
- follow-up machinery (scheduled or behavior-triggered follow-ups)
- own-domain sending / deliverability management
- import and enrichment of customer-owned contact lists
- consent/GDPR machinery (opt-out state on contacts, company-wide consent views, legitimate-interest evidence, unsubscribe enforcement)
- pitch→coverage linkage (which pitches/releases earned media mentions)
- team collaboration (shared lists, task assignment, roles, agency access with governance)
- outreach performance reporting
- journalist-request/opportunity visibility (media requests, forward-opportunity directories)

### L2 — Variant / Optional Structure

- **Database philosophy:** vendor-maintained proprietary database (dominant) vs customer-built/imported contacts with enrichment services (Prezly pole; JustReachOut's search-without-scale-claims posture).
- **Packaging:** standalone product vs named module/capability inside a monitoring/intelligence suite (Cision Journalist Outreach, Meltwater Media Relations) vs full PR suite with media-relations center of gravity vs pitch-first self-serve tool.
- **Regional depth:** national/regional media-market databases and language coverage (Roxhill UK; regional agencies persist).
- **Outreach extensions:** podcast outreach, guest-post/broken-link outreach (SEO-adjacent), journalist-request matching (request marketplaces are a different direction — journalist-initiated).
- **Distribution adjacency:** list-based press-release distribution tools (Roxhill, Meltwater integrated feature) vs the gated-network PRD Type.
- **Community/events layer:** journalist Q&As, speed-pitching events, curated move newsletters.
- **AI depth:** AI drafting, AI matching, AI-cited outlet discovery (current-cycle emphasis).
- **Commercial model:** enterprise contracts + onboarding vs self-serve plans/trials.

### L3 — Vendor-specific (Research Notes only)

- Meltwater: Mira AI; vendor figures (800,000+ contacts, 24–48h critical updates, ~7–8% bounce, 90+ analysts, 27,000+ customers); Dow Jones/WSJ exclusive content; six-step capability-page workflow; "database-only tools" competitive framing.
- Cision: CisionOne module names; Media Brief weekly roundup; vendor figures (500,000+ profiles, 225 countries); PR Newswire as separate product line.
- Prowly/Semrush: "AI-Cited Media Database" concept; automatic pitch→mention tracking; Semrush rebrand; FAQ list.
- Roxhill: Pinpoint trend tool; PR opportunities directory (200+ outlets claim); vendor figures (250k+ journalists, 40k+ outlets, 6.7M tagged articles, 50+ moves/day); "GDPR Rejected" shared-list state; events/speed-pitching program; ISO 27001 badge.
- JustReachOut: tool-suite naming (Journalist Outreach / Pitch Requests / Podcast Outreach / Broken Link Building / Guest Post Outreach); per-journalist responsiveness indicator; DIY-PR positioning; ChatRank.ai sibling product.
- Prezly (from PR pass): composer mechanics, tracking-toggle immutability, coverage provider integrations (Talkwalker, Auxipress, Belga).

## Vendor-specific / Rejected Findings

- All database-size, update-latency, bounce-rate, and move-volume figures — vendor marketing claims; excluded from the canonical document.
- "AI-cited outlets / LLM visibility" — current-cycle L2 emphasis; the stable structure underneath (database enrichment + discovery) is already covered.
- Meltwater's six-step workflow as a canonical workflow — vendor's own packaging; the canonical loop is abstracted from cross-product comparison, not adopted verbatim.
- JustReachOut's responsiveness scoring mechanics — single-product; generalized only as "responsiveness indicators" (L1).
- Roxhill's "GDPR Rejected" state name — product UI vocabulary; generalized as "opt-out state visible across shared lists."
- "Media relations = the whole PR function" — rejected: the market label straddles (suites sell "media relations" over broad bundles), but the sampled module/capability pages consistently center the contact→list→pitch→relationship loop; the whole-function reading belongs to PR Management.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (removal test) |
|---|---|---|
| Public Relations Management Platform | **closest sibling; joint review discharged this pass** | Media Relations' organizing frame is the journalist relationship and the pitch loop (contacts → lists → tracked pitches → relationship memory). PR Management adds organized campaigns, coverage capture, and function-wide reporting as first-class structures around that slice. Remove campaigns/coverage/reporting → Media Relations. Add them as the organizing frame → PR Management. The L0s are nested; both product shapes exist (whole-function platforms and relationship/pitch-centered products and suite modules). **Keep-both RATIFIED as two Types by scope.** |
| Media Monitoring Platform | complementary slice | Monitoring listens and measures after publication; no contacts, no outreach, no relationship records. The journalist-database/outreach modules inside monitoring suites (Cision Journalist Outreach, Meltwater Media Relations) are this Type's subject matter packaged as suite modules — confirming the monitoring pass's flag from this side. Remove contacts/outreach → Media Monitoring. |
| Press Release Distribution Platform | adjacent, list overlap | PRD's unit is one authored release broadcast through a platform-operated gated network with a per-release distribution record. Media Relations' unit is the per-journalist relationship and pitch. List-based distribution tools inside media-relations products (Roxhill, Meltwater) are an adjacency, not the gated network. Remove the relationship/pitch loop, keep gated network broadcast → PRD. |
| Email Marketing Platform | same send+track shape, different world | Opted-in customer audiences and promotional content vs media contacts and pitches; no media-list semantics (beats/outlets), no relationship stewardship frame. |
| CRM (generic) | structural analogy | Contact records + history + activity is CRM-shaped; the audience (journalists), the list semantics (media lists over a media universe), and the outbound unit (pitches) are media-specific. Vendors themselves say "CRM-style" — the analogy is acknowledged, the Type is distinct. |
| Sales Engagement / Outreach Sequencing Platform | machinery analogy | Same personalization/sequencing/tracking machinery aimed at sales prospects and deals; media relations aims at journalists and earned coverage. Different audience object and outcome object. |
| Journalist-source matching platforms (request marketplaces) | direction reversed | There, journalists post requests and sources respond; here the PR side initiates pitches to chosen journalists. Request feeds appear inside media-relations products as an alert/opportunity surface (L1), not the core direction. |
| Media Database / Directory Application | slice below the Type | A database without sending is a directory; the tracked-send leg is what makes it a relations platform. Meltwater's own marketing names "database-only tools" as the lesser category. |
| Social Media Management Platform | adjacent, sometimes bundled | Publishing/engaging on social channels is the primary job there; media relations centers journalist email pitching. |

## Historical / Market-Sample Check

- **Rolodex/card-file era:** contact cards carrying outlet, beat, phone, and handwritten notes (the relationship memory); pulled card stacks per story (the media list); typed/mailed pitch letters with logged follow-ups (the tracked send in analog form). All three L0 legs hold without software. ✓
- **Printed media-directory era:** published journalist directories + mail-merged releases to pulled lists — records + lists + sends; tracking thinner (response logs where kept). ✓ (noted as the thin pole)
- **Regional check:** national/regional media databases (UK Roxhill in sample; European/Nordic/Asian databases per the PR pass) — same shape with regional depth. ✓
- **Modern AI-era check:** AI drafting/matching/AI-cited discovery are current-generation L1/L2 structures on the same L0; the Type is fully recognizable without them. ✓

Conclusion: the definition is not over-fitted to the modern AI-suite implementation; the card-file practice satisfies the same three-part core.

## Uncertainties

1. **Muck Rack unreachable** (403 ×3 cumulative across two passes). The market's most prominent database-first brand is documented as market context only; no claims drawn. The database-first pole rests on Roxhill's documented tool structure and the module pages.
2. **Evidence tier:** no Tier-1 help-center documentation fetched this pass (Meltwater/Cision help centers were JS-gated in prior passes; not re-attempted per network rule). All direct evidence is Tier-2 official product/capability pages, plus the PR pass's Tier-1 Prezly notes as cross-reference. No precise operational rules (limits, defaults, state machines) are asserted anywhere; all scale/latency figures are vendor claims kept in these notes.
3. **JustReachOut depth:** whether it offers coverage tracking beyond pitch analytics is not evidenced from fetched pages; treated as the pitch-first thin pole with no coverage claims.
4. **Roxhill distribution mechanics:** the distribution tool is list-based (share with selected journalists); whether any gated-network semantics exist is not evidenced — held as adjacency, not PRD overlap.
5. **Suite-label straddle:** Meltwater's "Media Relations" capability page includes coverage/SOV/executive reporting — the label stretches over the suite bundle. The Type seam is held on the organizing frame (pitch/relationship loop vs campaign/coverage/report frame), consistent with how the monitoring/listening straddle was resolved; recorded in STATUS.md as the joint-review outcome.
6. **Prowly/Semrush deeper docs** now live under Semrush and were not fetched; Prowly used as the self-serve anchor on the fetched page only.

## Final Synthesis

A Media Relations Platform is the communications team's system for finding, reaching, and building working relationships with journalists. Its defining core is three jointly-held structures: media contact records (journalists/outlets/influencers held as managed records with outlet/role, beats/topics, contact channels); media list building (selecting and grouping contacts into saved, shareable outreach lists per story); and tracked pitch sending (personalized pitches sent from the platform to selected contacts, with engagement recorded per send and per contact). Around this core, mature products add: continuously enriched vendor-maintained journalist databases with AI matching and role-change alerts; per-contact CRM-style relationship history with duplicate-pitch avoidance; personalization at scale with AI drafting and follow-up scheduling; own-domain deliverability; consent/GDPR machinery; pitch→coverage linkage; team collaboration with agency governance; and outreach performance reporting. The market realizes the Type as standalone database-first products (with regional depth), named modules/capabilities inside monitoring and intelligence suites, full PR suites with a media-relations center of gravity, and pitch-first self-serve tools. The joint review with Public Relations Management Platform is resolved as two Types by scope: the media-relations slice (this Type) vs the whole-function loop (campaigns + coverage + reporting around the slice); the L0s are nested, both product shapes exist, and removal tests hold in both directions. Other boundaries: vs Media Monitoring (no contacts/outreach), vs Press Release Distribution (gated network broadcast vs per-journalist pitches), vs Email Marketing (customer audiences), vs CRM/Sales Engagement (structural analogies with different audiences and outcomes), vs journalist-request marketplaces (direction reversed), vs plain media directories (no sending).
