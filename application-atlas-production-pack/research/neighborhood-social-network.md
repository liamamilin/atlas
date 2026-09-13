# Research Notes — Neighborhood Social Network

Research date: 2026-09-08

## Research Goal

Understand the canonical structure of the Neighborhood Social Network Application Type: how locality enters the product (membership gate vs content scoping vs both), what the "neighborhood" object is and who defines it, how verification works, what identity posture prevails, what content objects and roles exist, and where the boundary lies with the §01.05 siblings (General Social Network, Interest-based, Microblogging, Professional, Photo-centric, Short-form Video, Friend Discovery, Social Profile Network) and with adjacent Types (Community Platform, Classifieds/Marketplace, Resident/HOA Portal, Civic Engagement Platform, Local News).

This pass is a sibling pass under the §01.05 family boundary framework ratified by the `general-social-network` and `microblogging-platform` passes: the family discriminator is **the organizing key of the core consumption/distribution loop**, and the neighborhood sibling's key was pre-registered as **verified locality**. This pass ratifies that assignment from the neighborhood side.

## Initial Boundary

- Core hypothesis: a social network where membership is gated by verified residence in a geographic area, the local area (neighborhood) is the container of the core loop, and the content loop is practical local-life exchange between co-residents, with local institutions (businesses, public agencies, organizations) participating as constrained guests.
- Likely confusions: General Social Network (same surface vocabulary), Community Platform / Online Forum (containers, but topic-keyed and open), Classifieds Platform / Local Service Marketplace (commerce-heavy neighbors products), Tenant/Resident Portal & HOA management (§17, operator-side residential systems), Civic Engagement Platform (§24, government-side), Local News / News Aggregator (Nextdoor bundles news), Friend Discovery (meeting neighbors as a use case).
- Known prior signals: `general-social-network` ("membership gated by verified locality → neighborhood"; assign by center of gravity, not feature presence), `microblogging-platform` and `interest-based-social-network` ("verified locality becomes the membership key → neighborhood").

## Research Questions

1. How does locality enter the loop — is it a membership gate, a content scoping mechanism, or both? What exactly is verified?
2. What is the neighborhood object — how is it demarcated, who creates/maintains it, how granular is it, and how does membership attach to it?
3. What identity posture do products enforce (real name, address on file, display rules)?
4. What content objects circulate (recommendations, help, items, safety, events, civic discussion), and what is the interaction loop (posts, replies, private messages)?
5. What is the social graph — automatic co-residency vs self-curated follows? Is there a follow graph at all?
6. What roles exist (member, volunteer moderator, business, agency, organization) and what are their rights — especially: can institutions read neighbor conversations?
7. What monetization postures exist and do they change the core?
8. Where are the removal-test boundaries to every neighboring Type?
9. Does the definition survive older / regional / differently-positioned products (historical/market-sample check)?

## Representative Products

Selected for market representativeness across geography, product philosophy, business model, and era; operational-document accessibility was the binding constraint (see Sources).

Directly researched (evidence layer A):

1. **Nextdoor** — the global canonical product (US-origin, 11 countries per its own about page); ad-funded, marketplace- and institution-heavy. Official about page, neighborhood directory, corporate blog (product updates, self-promotion policy), and public-agency page fetched. Help center unreachable (see Source-access Limitation).
2. **nebenan.de** — Germany's largest neighborhood platform per its own FAQ (founded 2015, 15,000+ neighborhoods); social-startup posture, real-name + address verification, ad-light funding mix. Root page and FAQ page fetched (rich). Help center unreachable.
3. **Hoplr** — Belgium/Netherlands (founded 2014); public-sector-funded, ad-free, privacy-first posture; explicit address-based access control. Root landing and About page fetched (rich). Help center unreachable.
4. **Karrot / Danggeun (당근)** — Korea's hyperlocal super-app (founded 2015 as a secondhand direct-trade service; 40M+ cumulative signups, 20M+ MAU per its own about page); commerce-first with a community feed riding on verified locality. Corporate about + service pages fetched (Korean). Consumer app surface unreachable (403).
5. **LocalCircles** — India; "social media for communities, governance and urban daily life"; locality is used to *suggest* circles rather than gate a neighborhood feed — retained as a boundary case, not a core sample.

Market anchors commonly cited for this Type but **not directly researched** this pass (official surfaces unreachable — see Source-access Limitation): Front Porch Forum (US regional email-list era), E-Democracy neighborhood forums (1990s era), Streetbank (UK). None of their operational details are used as evidence anywhere in these notes; they are named only as market context and flagged as an uncertainty.

## Sources

Tier 1 / Tier 2 (fetched successfully, 2026-09-08):

- Nextdoor — About: https://about.nextdoor.com/ (positioning: "essential neighborhood network for 110 million verified neighbors across 350,000 neighborhoods"; section taxonomy News / Alerts / Ask / For Sale & Free / Events and Groups; participant classes neighbors / businesses / publishers / public agencies; scale claims).
- Nextdoor — Neighborhood directory: https://nextdoor.com/find-neighborhood (public state-by-state directory of neighborhoods; "Discover your neighborhood").
- Nextdoor — Product updates blog: https://blog.nextdoor.com/whats-new-on-nextdoor-product-updates-2 (core feed/conversation improvements; Ask AI over "nearly fifteen years of trusted conversations between verified neighbors"; Post Insights; Events rebuild; journalist accounts; Faves; Opportunity Alerts routing "high-intent service requests from verified neighbors" to businesses).
- Nextdoor — Self-promotion policy update: https://blog.nextdoor.com/self-promotion-update (personal account = "you as a neighbor" vs Business Page; main feed described as "a recommendation for a great plumber, a heads-up about a road closure, a post about a neighborhood lemonade stand"; flagging reduces reach rather than deleting; Groups admins set their own promotion rules).
- Nextdoor — Public Agencies: https://about.nextdoor.com/public-agency (free agency pages; geo-targeting to neighborhoods/wards/flood zones/jurisdiction; polls; **"neighbors cannot start conversations with you"**; **agency staff cannot see conversations residents are having**; employment verification + work email + GIS boundary files for service areas; free page vs Ads comparison).
- nebenan.de — Root: https://nebenan.de/ (marketplace, neighborhood help, events, meeting people; posts attributed to named neighborhoods; "Nur mit echtem Namen + Adresse" — address verification at signup so everyone in the neighborhood actually lives there; abbreviated name display; street visibility toggle; post visibility "nur in der direkten Nachbarschaft oder auch in deiner Umgebung").
- nebenan.de — FAQ: https://nebenan.de/ueber-uns/fragen (real name + address signup → **automatic assignment to your neighborhood**; read/write posts, find/offer help, marketplace, meet people nearby; 15,000+ neighborhoods; founded 2015, Good Hood GmbH, Burda majority since 2020; funding: voluntary user contributions + ads from local businesses/nonprofits/cities + labeled ads; real names → positive tone rationale; 3 golden rules).
- Hoplr — Root: https://www.hoplr.com/ (onboarding form: "Fill in your home address" street+number+postal code+city → "Find my neighbourhood"; "Every neighbourhood is closed. Hoplr neighbourhoods are geographically demarcated. Your profile is only visible to members of your neighbourhood network"; use cases: group chats, introductions, neighbour list, recommendations, borrow/give away, activities + neighbourhood calendar, babysitter, alerts from city/municipality, participation projects; **"Local authorities cannot view conversations going on in the neighbourhood, but they can post messages concerning it"**; moderator/founder testimonials; 800,000 households BE/NL, 2,500 active neighbourhoods).
- Hoplr — About: https://www.hoplr.com/about (founded 2014 Belgium; "free and closed social network"; **"Access is based on address and only members have access to the neighbourhood messages"**; public-sector licenses via paying service dashboard; only non-commercial external parties allowed; use-case list incl. borrow ladder/drill, roadworks discussion, yard sale, block party, calendar, notifications, projects).
- Karrot — About: https://about.daangn.com/ ("동네를 여는 문, 당근" — the door to the neighborhood; secondhand direct trade with nearby neighbors as the start, building an unprecedented local life community; neighbors share real neighborhood stories; store owners hear neighbors' voices; trade/gatherings/promotion/payments connected; 40M+ signups, 20M+ MAU, 3 countries).
- Karrot — Service: https://about.daangn.com/service/ (중고거래 secondhand trade with **동네인증 [neighborhood verification]** and 매너온도 [manner temperature] reputation; 커뮤니티 community — share neighborhood news, meet like-minded people, connect with same-apartment residents; 동네가게 neighborhood stores with coupons and neighbor reviews; business profiles/brand profiles/ads targetable to 읍·면·동 [administrative units]; jobs, cars, realty, pay).
- LocalCircles — Root: https://www.localcircles.com/ ("Social Media for Communities, Governance and Urban Daily Life"; signup asks apartment/complex/landmark "Knowing you and your locality enables us to suggest circles"; circles + entities model).

Unreachable / abandoned per network rules (1–4 fetch failures each; not substituted from memory):

- Nextdoor help center — help.nextdoor.com/s/ and help.nextdoor.com/ (transport errors); nextdoor.com/neighborhood_guidelines (transport error ×2); nextdoor.com/member_agreement (transport error); nextdoor.com root and /choose_address (JS shells, no content).
- Hoplr help center — help.hoplr.com/hc/en-us (timeout, then transport error).
- nebenan.de help center — hilfe.nebenan.de/hc/de (transport error ×2).
- Karrot consumer app surface — www.daangn.com (HTTP 403).
- Front Porch Forum — frontporchforum.com root, /about, /faq (empty responses ×4).
- E-Democracy — e-democracy.org, www.e-democracy.org (transport errors ×2).
- Streetbank — www.streetbank.com (empty response).

## Product Observations

### Nextdoor (evidence layer A)

- **Positioning**: "the essential neighborhood network for 110 million verified neighbors across 350,000 neighborhoods" — verification and the neighborhood unit are in the first sentence of the official about page. "1 in 3 U.S. households rely on Nextdoor" (vendor claim, not repeated in final document).
- **Onboarding**: get-started URL is `/choose_address` — address selection is the entry act; neighborhoods are publicly browsable via a state-by-state "Discover your neighborhood" directory (`/find-neighborhood`).
- **Section taxonomy** (about page): News (stories from vetted local publishers into the feed), Alerts (real-time safety alerts, "in partnership with local public agencies like fire departments"), Ask (AI answers "drawing on nearly fifteen years of trusted conversations between verified neighbors", pointing to "a conversation already happening, a trusted local business, another neighbor, or a Group"), For Sale & Free (marketplace "built on trust and powered by community"), Events and Groups.
- **Participant classes**: neighbors (verified), local businesses (claimed pages — "5+ million claimed business pages"), local news publishers (4,000+), public agencies (6,000+), local journalists (500+ journalist accounts).
- **Feed posture**: "the main feed feels like your neighborhood: a recommendation for a great plumber, a heads-up about a road closure, a post about a neighborhood lemonade stand." Personal account = "you as a neighbor"; business promotion must move to a Business Page (with reviews, Faves, searchability). Flagging reduces distribution rather than deleting ("It stays up exactly as you posted it… fewer neighbors will see it").
- **Institution layer rights**: public-agency pages are free; staff initiate and close conversations, "neighbors cannot start conversations with you"; agency staff **cannot see conversations residents are having** ("Nextdoor is designed to facilitate connections between neighbors… allowing for private conversations between neighbors"); targeting by custom GIS polygons (wards, flood zones, jurisdiction); employment verification and work-email vetting for agency staff; department name displayed above staff profile name.
- **Monetization**: ads (Ads Manager machinery), Opportunity Alerts (paid routing of neighbor service requests to businesses), Faves (recommendation/award program). None of this is described as changing the neighbor loop.

### nebenan.de (evidence layer A)

- **Positioning**: "Deutschlands größte Nachbarschaftsplattform" — millions of people "in mehr als 15.000 Nachbarschaften"; they "tauschen sich aus, helfen einander und gestalten ihr Miteinander – online und im echten Leben" (exchange, help each other, shape their life together — online and in real life).
- **Onboarding**: "Du meldest dich mit deinem echten Namen und deiner Adresse an und wirst **automatisch deiner Nachbarschaft zugeordnet**" — real name + address signup, automatic assignment to the neighborhood. Address verification exists "Um sicherzustellen, dass alle Nutzer:innen in deiner nebenan.de-Nachbarschaft **vor Ort wohnen**" (to ensure everyone in your neighborhood actually lives there).
- **Identity display**: real name required at signup but displayed abbreviated (first name + last-name initial); street visibility within the neighborhood is a user toggle. Rationale given: real names → more respectful, trust-based interaction.
- **Content loop**: read/write posts, find or offer help, use the marketplace, meet people nearby. Homepage post examples attributed to named neighborhoods (Altstadtviertel: childcare search; Nikolaivorstadt: found key; Kastanienallee: courtyard festival; Südvorstadt: cooking together) — the neighborhood is the attribution frame of ordinary posts.
- **Audience scoping**: per-post setting — visible "nur in der direkten Nachbarschaft oder auch in deiner Umgebung" (only the direct neighborhood, or also the surrounding area).
- **Institution layer**: local businesses and nonprofits get free base profiles; funding = voluntary user contributions + ads from local businesses/nonprofits/cities + clearly labeled paid ads. Founded 2015 as a social startup (Good Hood GmbH, Berlin; Hubert Burda Media majority since 2020); adjacent charitable foundation.
- **Tone governance**: "3 goldene Regeln" (be nice, be honest, be helpful); vendor-reported tone statistics (not repeated in final document).

### Hoplr (evidence layer A)

- **Positioning**: "The social network for your neighbourhood"; Belgian, founded 2014; "Hoplr shifts the focus from the individual to the local community."
- **Access control**: "Hoplr offers neighbours a **free and closed social network**… Hoplr neighbourhoods are **geographically demarcated**. **Access is based on address** and only members have access to the neighbourhood messages." Onboarding form literally asks street + number + postal code + city → "Find my neighbourhood".
- **Content loop**: talk to neighbours; share and borrow items; ask for help; neighbourhood alerts and activities; group chats (building, running, block party); introduce yourself; profile with hobbies/pets/profession/interests; consult the list of your neighbours; recommendations (plumber, babysitter); give away items; group purchases; organise activities (cleanup, game night, walk, yard sale) with a neighbourhood calendar; discuss traffic problems and roadworks.
- **Institution layer**: local governments and utility companies buy a paying service dashboard for "neighbourhood-oriented communication and citizen participation"; they post roadworks/nuisance/security messages into neighborhoods but **"cannot view conversations going on in the neighbourhood"**; only external parties "that bring non-commercial value to citizens" are allowed. Ad-free consumer posture; GDPR-first positioning.
- **Roles**: testimonials from neighborhood "moderators" and "founders" — volunteer neighborhood-level roles exist.
- **Scale (vendor-claimed)**: 800,000 households, 2,500 active neighbourhoods, Belgium + Netherlands.

### Karrot / Danggeun (evidence layer A)

- **Positioning**: "동네를 여는 문" (the door that opens the neighborhood); "근처 이웃과의 중고 직거래를 시작으로, 전에 없던 지역 생활 커뮤니티를 만들어 나가고 있어요" — starting from secondhand direct trade with nearby neighbors, building a local-life community; neighbors share "진짜 우리 동네 이야기" (real our-neighborhood stories); store owners hear neighbors' voices up close.
- **Locality verification**: 중고거래 (secondhand trade) explicitly ships **동네인증** (neighborhood verification) plus 매너온도 (manner temperature — a reputation score) and ML post analysis for safe trading.
- **Community**: "이웃과 자연스레 동네 소식을 나누고, 취향이 비슷한 사람들과 모이고, 같은 아파트 주민들과 더 가까워질 수 있어요" — share neighborhood news with neighbors, gather with like-minded people, get closer to same-apartment residents; "동네 안에서 이웃을 연결" (connecting neighbors within the neighborhood).
- **Institution layer**: 동네가게 (neighborhood stores) — store news, coupons, neighbor reviews; business/brand profiles; ads targetable down to 읍·면·동 (town/village/dong administrative units).
- **Super-app extensions**: jobs (알바), used cars, realty (with lived-experience review maps), payments (당근페이 — "금융 생활" grounded in the neighborhood), neighborhood-walking campaigns. Scale: 40M+ cumulative signups, 20M+ MAU (vendor-claimed, Jan 2025), operations in 3 countries.

### LocalCircles (evidence layer A — boundary case)

- **Positioning**: "Social Media for Communities, Governance and Urban Daily Life."
- **Locality's role**: signup asks for apartment/complex name or nearby landmark — "Knowing you and your locality enables us to **suggest circles** that are useful and engaged in making your locality a better place to live in." Locality *suggests* membership in circles; it does not gate a geographically demarcated neighborhood feed. The organizing structure is the circle (topic/community container), not the residential area. Retained as evidence for the boundary against Community Platform / Civic Engagement, not as a core sample.

## Cross-product Comparison

| Structure | Nextdoor | nebenan.de | Hoplr | Karrot | LocalCircles | Layer |
|---|---|---|---|---|---|---|
| Address/residence-based membership | ✓ ("verified neighbors"; /choose_address) | ✓ (real name + address, verification "vor Ort wohnen") | ✓ ("Access is based on address"; closed network) | ✓ (동네인증) | locality suggests circles only | A, 4/4 core |
| Geographically demarcated neighborhood container | ✓ (350,000 neighborhoods; public directory) | ✓ (automatic assignment; 15,000+ neighborhoods) | ✓ ("geographically demarcated") | ✓ (동네; ads to 읍·면·동) | ✗ (circles instead) | A, 4/4 core |
| Neighborhood as default audience / attribution frame | ✓ ("main feed feels like your neighborhood") | ✓ (posts attributed to named neighborhoods) | ✓ (profile visible only to neighborhood members) | ✓ (동네 소식 neighborhood news) | ✗ | A, 4/4 core |
| Resident-attributed practical local-life posts | ✓ (plumber rec, road closure, lemonade stand) | ✓ (childcare, found key, festival, cooking) | ✓ (borrow, help, roadworks, yard sale) | ✓ (동네 소식, same-apartment ties) | (circle posts) | A, 4/4 core |
| Real-identity posture | ✓ ("verified neighbors"; personal account = "you as a neighbor") | ✓ (real name required, abbreviated display) | ✓ (profile with real attributes; closed network) | ✓ (동네인증; manner temperature) | (name+locality at signup) | A, 4/4 core |
| Item exchange (sell/free/borrow) | ✓ (For Sale & Free) | ✓ (Marktplatz) | ✓ (borrow/give away, group purchases) | ✓ (중고거래 — the founding service) | — | A, 4/4 core |
| Recommendations / local business discovery | ✓ (Ask, Faves, business pages) | ✓ (Empfehlungen; Gewerbe profiles) | ✓ (plumber/babysitter recommendations) | ✓ (동네가게 + reviews) | — | A, 4/4 core |
| Events / gatherings | ✓ (Events, Groups) | ✓ (event posts) | ✓ (activities + neighbourhood calendar) | ✓ (모임 meetups) | — | A, 4/4 core |
| Private messaging between members | ✓ ("private conversations between neighbors") | ✓ (Nachrichten) | ✓ (private conversations, group chats) | ✓ (chat in trade flow) | — | A, 4/4 core |
| Nearby-neighborhood reach extension | ✓ (agency targeting beyond single neighborhood; jurisdiction-wide) | ✓ (per-post "direkte Nachbarschaft oder auch Umgebung") | (neighbour-scoped; municipality posts) | ✓ (targeting granularity) | — | A, 2/4 direct + 2 implied |
| Institution layer with constrained rights | ✓ (agencies cannot read neighbor conversations; businesses on pages) | ✓ (business/nonprofit/city profiles + labeled ads) | ✓ (governments post, cannot read; non-commercial only) | ✓ (store profiles, coupons) | — | A, 4/4 core |
| Volunteer neighborhood roles | (Groups admins) | (implied) | ✓ (moderators, founders in testimonials) | — | — | A, thin |
| Safety/alerts surface | ✓ (Alerts with public agencies) | — | ✓ (neighbourhood alerts) | (ML post analysis for trade safety) | — | A, 3/4 |
| Local news integration | ✓ (publishers, journalist accounts — deep) | — | — | — | — | A, product-specific |
| Reputation mechanics | — | — | — | ✓ (매너온도 manner temperature) | — | A, product-specific |
| AI answer surface | ✓ (Ask) | — | — | — | — | A, era-current |
| Monetization | ads + paid lead routing + awards | voluntary contributions + local/labeled ads | public-sector licenses (ad-free) | commerce super-app + ads | (governance programs) | A, all different |

Reading: the jointly-held structures (4/4 core sample) are the address-verified membership, the demarcated neighborhood container as default audience, resident-attributed practical exchange, real-identity posture, and the constrained institution layer. Everything else varies — including the business model, which differs in all four core samples without any of them ceasing to be neighborhood networks.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures. If any one is removed, the product stops being recognizable as a Neighborhood Social Network:

1. **Verified-locality membership** — membership is established through a real-world residence claim (an address) that the product verifies, and the member's standing in the network derives from where they live. Remove the gate → a social network anyone can join from anywhere (General SNS / Community Platform).
2. **The neighborhood as the container and default audience** — a geographically demarcated local area holds the membership; content is scoped to it (with controlled extension to surrounding areas); the neighborhood is the attribution frame of ordinary posts. Remove the container → topic-keyed community or person-graph feed.
3. **Resident-to-resident practical exchange as the content loop** — the currency of the network is posts between resident-members about local practical life (recommendations, help, items, safety, events, local issues), attributed to identified residents, with persistent history and private channels. Remove the exchange → a resident directory or local bulletin board; remove the resident-to-resident direction → a local news/information service.

Jointly-held is load-bearing: 1 alone = a verified-address directory; 2 without 1 = an open local topic forum; 3 without 1+2 = a general social network with a location interest.

### L1 — Common Mature Structure

Present across the sampled market; makes the Type practical but does not define it:

- **Resident profile** — real-name posture (display often abbreviated), street-visibility toggles, personal attributes (hobbies, pets, profession).
- **Practical post taxonomy** — recommendations and asks, help offered/sought, item exchange (sell / free / borrow), safety alerts and lost-and-found, events, local civic discussion.
- **Replies and private messaging** between members; group chats.
- **Nearby reach extension** — per-post or per-surface scoping beyond the immediate neighborhood (surrounding neighborhoods, city, jurisdiction).
- **Constrained institution layer** — business pages, public-agency pages, nonprofit/organization pages that post into localities but cannot read neighbor conversations (directly documented in two products, structurally present in all four).
- **Moderation machinery** — community guidelines, tone rules, volunteer moderator/admin roles, flagging that reduces distribution.
- **Events and groups** — calendar surfaces, member-formed interest/activity groups inside the locality.
- **Mobile apps + web** sharing one identity; notifications.

### L2 — Variant / Optional Structure

- **Verification method** — how an address is proven varies by product and region (not stated precisely anywhere in the fetched evidence; deliberately left abstract).
- **Neighborhood container definition** — system-drawn geographies, member-founded neighborhoods (Hoplr founders), administrative units (Karrot 읍·면·동), public directories (Nextdoor).
- **Business model** — ads + paid lead routing (Nextdoor), public-sector licensing (Hoplr), voluntary contributions + local labeled ads (Nebenan), commerce super-app (Karrot). All four differ; none changes the core.
- **Marketplace depth** — full commerce verticals (Karrot: cars, realty, jobs, payments) vs listings (Nextdoor, Nebenan) vs borrow/give (Hoplr).
- **Local news integration** — publisher and journalist programs (Nextdoor, deep; absent elsewhere in sample).
- **Civic participation tooling** — municipality projects and polls (Hoplr, Nextdoor agencies); governance-focused circles (LocalCircles — boundary case).
- **Reputation mechanics** — trade-manner scores (Karrot).
- **AI answer surfaces** — neighborhood Q&A over accumulated conversations (Nextdoor Ask; era-current).

### L3 — Vendor-specific (research notes only; not in final document)

- Nextdoor: Faves awards program and voting campaigns; Opportunity Alerts (paid routing, "100,000+ alerts per week" claim); journalist accounts and publisher program; Post Insights; self-promotion policy specifics (casual offers up to once a month, nonprofit posts up to once a week, flag-then-review flow); agency qualification rules (fully-staffed top-level departments only; no elected officials/committees); GIS boundary-file onboarding; Ads Manager machinery; "1 in 3 U.S. households" claim.
- Hoplr: services.hoplr.com government dashboard; Intigriti responsible-disclosure; ICTRecht privacy certification; World Summit Awards; exact BE/NL household counts.
- nebenan.de: Stiftung (charitable foundation) structure; Burda ownership; "3 golden rules"; vendor-reported tone/report statistics (40% / 4% — claims, not repeated); 15,000+ neighborhoods claim.
- Karrot: 매너온도 scoring; 동네걷기 (neighborhood walking); 당근페이; 알바/중고차/부동산 verticals; Toss merchant partnership (2026 press release); 40M/20M scale claims.
- LocalCircles: circle/entity taxonomy; government engagement programs; media "featured in" wall.

## Rejected Findings

- "A Neighborhood Social Network requires a specific verification method (postcard / credit card / phone)" — REJECTED as definitional: no method was directly evidenced this pass; the invariant is that residence is verified, not how.
- "The neighborhood must be a system-drawn map polygon" — REJECTED: member-founded neighborhoods (Hoplr) and administrative-unit anchoring (Karrot) satisfy the Type; demarcation mechanism is a variant.
- "Real-name display is definitional" — REJECTED as stated: the load-bearing structure is verified locality; Nebenan itself requires real names but displays them abbreviated, showing the display layer is implementation. Real-identity posture is held at L1 as a strong common norm.
- "Marketplace/classifieds are part of the definition" — REJECTED: item exchange is universal in the sample but Hoplr's borrow/give form and Karrot's commerce-first form are structurally different realizations; a neighbors-only help/alert network (email-list era class) would satisfy the core without any marketplace.
- "Local institutions (businesses/agencies) are part of the definition" — REJECTED as L0: the institution layer is universal in the current sample (4/4) but the resident-to-resident loop stands without it; institutions are guests with constrained rights, not the organizing structure.
- "The Type is just a General SNS restricted to a zip code" — REJECTED: the organizing key differs structurally — membership is address-gated and the default audience is co-residency, not a self-curated graph; content is practical local-life exchange, not untyped personal updates.
- "Neighborhood networks are civic/government platforms" — REJECTED: agencies participate as constrained guests; the resident loop, not the government program, is the spine (Hoplr and Nextdoor both document the one-way privacy wall).

## Boundary Findings

The §01.05 family framework is **ratified from this side**: the neighborhood sibling's organizing key is **verified locality** — stated as the family test: *residence, verified against a real address, keys both membership and the default audience, and the demarcated local area is the container of the loop.*

Removal tests against neighbors:

| Neighbor Type | Relationship | Removal test (what removed → becomes that Type) |
|---|---|---|
| General Social Network (§01.05) | family sibling, sharpest | remove the address gate and the neighborhood container; let members self-curate their graph and post untyped updates → General SNS |
| Interest-based Social Network (§01.05) | organizing-key sibling | swap the locality domain for an interest domain (identity becomes an interest record, content domain-anchored) → interest-based |
| Microblogging Platform (§01.05) | tie-semantics sibling | ties become public broadcast subscriptions, posts general/untyped, discovery-first → microblogging |
| Professional Social Network (§01.05) | audience sibling | career/professional context keys identity and sharing → professional |
| Photo-centric / Short-form Video (§01.05) | content-type siblings | the medium becomes the organizing key → those Types |
| Friend Discovery Application (§01.05) | formation-loop sibling | forming new relationships becomes the primary loop; here meeting neighbors is a byproduct of the exchange loop |
| Social Profile Network (§01.05) | substrate sibling | remove the exchange loop → profiles + resident directory |
| Community Platform / Online Forum / Q&A (§01.06) | container siblings | containers become topic-keyed and membership open (anyone interested joins) → community Types; LocalCircles-class products sit on this seam (locality suggests circles; circles organize) |
| Classifieds Platform / Service Marketplace (§05) | commerce sibling | the transaction becomes the unit of record and the neighbor loop serves it → marketplace; Karrot-class products straddle and are assigned by center of gravity (verified-locality community loop remains the spine) |
| Tenant/Resident Portal, HOA/Community Association Management (§17) | operator-side residential systems | the property/association operator runs the system, membership follows tenancy/ownership of a specific property, and the operator's business processes (dues, maintenance, bookings) are the core → residential management Types; here membership follows residence in a demarcated area and the peer exchange is the core |
| Civic Engagement Platform, 311 (§24) | government-side | the government operates the surface for constituent engagement and service requests → civic Types; here agencies are guests posting into a resident-owned loop |
| Local News Application / News Aggregator (§02.04) | information sibling | editorial news consumption is the product; here news is a bundled capability feeding the neighbor loop (Nextdoor's News section) |
| Instant Messaging Application (§01.01) | conversation sibling | private addressed conversation is the product; here DMs are a side channel of the neighborhood loop |
| Review Platform (§02.10) | object overlap | the review of record for purchase decisions is the product; here recommendations are neighbor posts, and business reviews attach to pages inside the network |

Straddle zones recorded honestly: commerce-heavy hyperlocal products (Karrot) and civic-circle products (LocalCircles) sit at the Type's edges; both are assigned by center of gravity per the family framework.

## Uncertainties

1. **Nextdoor's operational help documentation was unreachable this pass** (help center, guidelines page, member agreement all failed). The Nextdoor model rests on the official about page, the public neighborhood directory, and three corporate blog posts (product updates, self-promotion policy, public agencies) — all official but not help-center-grade operational detail. Verification methods, exact neighborhood granularity rules, and lead/moderator program details are therefore NOT stated anywhere in this pass's outputs.
2. **Hoplr and nebenan.de help centers were unreachable**; their models rest on landing + about/FAQ pages (official, rich on structure and rules, thin on step-by-step mechanics).
3. **Karrot's consumer app surface was unreachable (403)**; its model rests on the corporate about/service pages (Korean). Community-feed mechanics (posting rules, feed structure) are inferred only as far as those pages state.
4. **The email-list / pre-smartphone era sample (Front Porch Forum, E-Democracy, Streetbank) could not be fetched.** The historical check is therefore reasoned, not sourced: the L0 requires no app, no feed ordering, no marketplace, no AI — an address-scoped member list exchanging practical neighborhood messages satisfies all three L0 structures. This is recorded as canonical inference with a sampling limitation, not as observed fact.
5. The balance between neighborhood-scoped-only and city-scoped products in the wider market was not measurable; nearby-reach extension is documented directly in two products and implied in two more.
6. Prevalence of volunteer moderator programs across the market is unknown (thin evidence: Hoplr testimonials, Nextdoor Groups admins).
7. All scale figures in this file are vendor claims and are not repeated in the final document.

## Final Synthesis

The Neighborhood Social Network is a social network organized by **verified locality**: residents join by verifying where they live, are placed into a geographically demarcated neighborhood that forms their default audience and the attribution frame of their posts, and exchange practical local-life content with co-residents — recommendations, help, items, safety, events, local issues — while local institutions (businesses, public agencies, organizations) participate as constrained guests who can post into localities but cannot read neighbor conversations. The defining core is exactly the three jointly-held L0 structures above. Resident profiles, the practical post taxonomy, replies and DMs, nearby reach extension, the institution layer, moderation, events and groups are common mature structure; verification method, container demarcation, business model, marketplace depth, news integration, civic tooling, reputation mechanics, and AI surfaces are variants. The Type is assigned by the organizing key of the core loop: verified residence in a demarcated local area — not a self-curated person graph (General SNS), not an interest domain (interest-based), not broadcast subscriptions (microblogging), not an audience context (professional), not a content type (photo/short-form), not topic containers (community Types), not a transaction (marketplace), and not an operator's property business (residential management Types).
