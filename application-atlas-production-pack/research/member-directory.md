# Research Notes — Member Directory

## Research Goal

Determine what a Member Directory application is when researched from real products: what objects exist inside it, who populates and who consumes it, how lookup and publication work, what role the organization's membership plays, and whether this §25 leaf is a structurally independent Application Type or a domain-scoped instance of Directory Application (§02.11).

This pass also carries three pre-hung flags to discharge:
1. directory-application (§02.11, processed) — "most plausibly a domain-scoped instance of Directory Application… no member-directory product was reachable… joint review recommended".
2. member-community-platform (§25, processed) — removal test recorded: "strip participation → directory remains; strip directory → community remains (degraded)"; keep-both expected, awaiting ratification.
3. congregation-membership-management (§25, processed) — watch-item: "the directory is one output of the roll… watch-item for capability-slice consolidation".

## Initial Boundary

Working hypothesis at start of pass:

- A Member Directory is a roster of an organization's members (people and/or member organizations) held as structured profiles and organized so that specific members can be found and reached.
- Primary users: membership organization staff (administer) and members (look up each other, maintain their own entries); public-facing postures expose member businesses to outsiders.
- Nearest neighbors: Directory Application (§02.11), Listings Platform (§02.11), Member Community Platform, Member Portal, Membership Management System / AMS (§25), Congregation Membership Management (§25), Social Profile Network (§01.05), CRM (§07).
- Obvious unknowns: does the market realize this as a standalone product category (decisive for Type vs capability-slice)? Is visibility governance definitional or merely common? Is the membership anchoring structural or just an "entity class" choice?

## Research Questions

1. What objects exist? (member record vs profile entry, families/households, companies with staff lists, groups/committees as directory scopes, categories, photos/galleries)
2. Where does the population come from — manual entry, join flow, import, or derived from the membership database?
3. Who maintains records — org staff only, members themselves, or moderated member submissions?
4. How does lookup work — search, filters/facets, category browse, map, alphabetical?
5. What visibility rules exist — public vs members-only, field-level display, per-member opt-out, email protection?
6. What is membership's role — do status/approval/standing gate inclusion, ordering, or prominence?
7. What outputs exist — web, app, print/PDF, exports?
8. What is adjacent but NOT part of it — dues, events, forums, job boards?
9. Standalone vs module packaging — is there a dedicated-product market?
10. Type decision vs Directory Application: alias (segment instance) or keep-both?

## Representative Products

Selected to span product philosophy, customer segment, and packaging (market representation + documentation completeness + different poles):

| Product | Pole | Packaging | Docs reached |
|---|---|---|---|
| Instant Church Directory | congregation photo directory; print heritage; standalone | dedicated product (subscription) | Tier-2 product + features pages (help center exists, not fetched) |
| MembershipWorks | all-in-one membership software with named Member Directory feature | SaaS/plugin for WordPress/Squarespace/Wix etc. | Tier-2 product + feature pages |
| Brilliant Directories | directory-website platform with membership machinery | directory-builder SaaS | Tier-1 KB (Search Members Overview; add-on tree) |
| Novi AMS | chamber/association AMS with directory module | AMS suite module | Tier-1 KB (Guide to Member Directory; Privacy cheat sheet; custom-field article; collection tree) |

Deliberately excluded after failures (see Sources): Wild Apricot (help + feature pages 404 ×2), Almabase (transport error). GrowthZone/ChamberMaster not attempted (recorded JS-rendered in sibling passes).

## Sources

Research date: 2026-09-08. All fetched this pass unless noted.

- Instant Church Directory — https://www.instantchurchdirectory.com/ (home); https://www.instantchurchdirectory.com/church-directory-features (features)
- MembershipWorks — https://membershipworks.com/ (home); https://membershipworks.com/member-directory/ (feature page)
- Brilliant Directories — https://support.brilliantdirectories.com/support/solutions (KB tree); https://support.brilliantdirectories.com/support/solutions/articles/12000045147-my-members-search-members-overview (Tier-1); Hidden Member Profiles add-on folder (article list + summary)
- Novi AMS — https://help.noviams.com/ (KB home); Member Directory collection https://help.noviams.com/collections/5740287562-member-directory (19 article titles); https://help.noviams.com/articles/6957821970-a-guide-to-the-member-directory (Tier-1, full text); https://help.noviams.com/articles/5302661912-cheat-sheet-member-directory-privacy-and-data-protection (Tier-1, full text); https://help.noviams.com/articles/2120182893-add-remove-or-rearrange-custom-field-values-on-directory-profile-pages (Tier-1, full text)

Source-access limitations:

- Wild Apricot: gethelp.wildapricot.com 404; wildapricot.com/features/member-directory 404 — abandoned after 2 failures per network rule. The vendor most often cited for field-level directory controls is therefore NOT directly evidenced this pass.
- Almabase (alumni pole): help.almabase.com transport error — alumni-variant assertions rest on market structure, not direct observation.
- ICD help center (help.instantchurchdirectory.com) linked but not fetched; ICD claims below are Tier-2.
- No precise numeric limits (message caps, listing counts, search behavior internals) asserted in the final document beyond what vendors state directly.

## Product Observations

### Instant Church Directory (pole: congregation photo directory, standalone)

Evidence layer: A (official product/feature pages).

- The entire product IS the directory: "online membership directory program… maintain up-to-date member contact information"; no dues, events, or forums anywhere in the feature set.
- Records: Families and Individuals as separate record classes; photos (headshots/family), addresses, email addresses, phone numbers, birthdays, anniversaries, and "membership status" listed among the form fields; customizable "Family Label" so non-church organizations can reuse the terminology; staff pages; activity pages; cover; custom PDF pages (maps, history, ads).
- Roles: administrator (account holder), up to 3 editors/volunteers (standard; unlimited on premium), members (viewers via free mobile apps / online members' website).
- Member identity/access: members sign in "using their email address listed in the directory and a secure sign-in link we send to their verified email inbox" — the directory's own email field is the identity key.
- Subject participation with moderation: members "submit updates to your information listed in the church directory… for approval from your directory administrator"; admins "approve or reject members' submission requests… if something is questionable, simply reject it"; editors receive submission-notification emails; members can also upload their own photos for approval.
- Lookup and reach: "search for a family or member and then email, call, text, or launch a map with directions — right from your device"; new members "automatically placed in alphabetical order"; birthdays/anniversaries compiled by month.
- Groups → sub-directories: "add individuals or families to a group, and then print a member directory just for that group… as many groups and sub-directories as you want".
- Outputs: printable PDF in 8.5×11 or booklet size, color/BW, page ordering, larger-font options for elderly members; mobile apps (work "even offline"); online members' website.
- Data movement: CSV import (with field mapping, photo attachment, undo) and CSV export "to create envelopes or mailing labels".
- Privacy posture: dedicated security page; "never use or sell your church data".

### MembershipWorks (pole: all-in-one membership plugin, SMB orgs)

Evidence layer: A (official feature page; home page for packaging).

- Member Directory is one named feature among membership/event/billing features — module realization of the Type.
- Member profile template: "visual & interactive" profiles; drag-and-drop customization of tabs and boxes.
- Access control: "Give access to member profiles for just members, or provide incremental access based on membership levels or labels" — audience/visibility tied to membership tiers.
- Lookup: keyword search engine that "deliver[s] relevant search results… by recognizing related words and ranking search results using keywords and phrases in member profiles"; geo search by location and distance; faceted search by labels or any specified field including custom fields; "stacked with keyword and geo search".
- Map: interactive map with search/zoom, popup previews clicking through to profiles; members can list multiple locations and contacts, "every location is displayed on the map and included in geo search".
- Contact protection: "member's email addresses are not displayed in their directory profile. Our messaging system provides a way for legitimate visitors to contact your members without first revealing the member's email addresses" (explicit CAN-SPAM compliance reference).
- Member-side commerce attached to the entry: member deals created and managed by members through their account; member recommendations/testimonials ("thumbs up" or detailed testimonials).
- Vendor testimonial (weak evidence, used only as corroboration): "the power of the profiles and the control our members have over them".

### Brilliant Directories (pole: directory-website platform with membership)

Evidence layer: A (Tier-1 KB article body + add-on folder titles/summaries).

- Admin-side member registry: "My Members → Search Members… provides access to member records, filtering tools, bulk management actions"; results table with sort options: name A–Z / Z–A, system ID, "Sort Newest First — most recently joined members shown first" / "Oldest First — earliest joined", revenue, credits — join date is a first-class record attribute.
- Member record operations: add manually via admin ("without requiring the member to [sign up]"), CSV import (template + guidelines), CSV export (add-on gated; includes emails/phones), bulk actions, quick edit, login-as-member, password reset, verified status indicator ("How to Verify a Listing"), internal notes, geocoding ("assigning latitude and longitude coordinates to member listings based on their address data" so they "become searchable by location").
- Membership coupling: Hidden Member Profiles add-on — "Address privacy concerns by hiding the profiles of specific membership levels on the website. The admin can also incentivize member upgrades by…" (membership-level-driven visibility + upgrade incentive); spam mitigation article about "free sign-up option for a public listing or profile" — implies open/public listing postures exist and must be governed.
- Entry-side interaction machinery around the directory: Member Leads, Lead Module FAQ, Member Reviews, Reply to Member Reviews, Click to Call Member, Private Member Chat, Member Profile Analytics, Member Profile Badges, Multi-Location Listing, Claimable Business Listings, Members-Only Content, Feature Members on Homepage.
- Positioning (home/support titles): "Brilliant Directories Documentation" — the product's own frame is directory websites whose members hold accounts.

### Novi AMS (pole: chamber/association AMS with directory module)

Evidence layer: A (Tier-1 KB full texts ×3 + 19-article collection titles).

- The directory is a configured object derived from the membership database: "Create multiple directories based on groups and/or committees like all members, new members, specific member types, or even directories built from custom fields"; each directory has "its own unique URL and customizable settings, independent from others".
- Population flows from membership: "updates to the Group (like adding new members) automatically flow through to the Directory, keeping everything current without extra work"; "Groups can only include member records that have been approved. Pending members cannot be displayed in a directory."
- Standing shapes the listing: final sort always groups "Featured members before non-featured… Members with benefits (status: current, grace, or inheriting) before those without… Dues-paying members before beneficiaries… Inheriting members"; profiles may display "Member Since Date" or "Original Join Date".
- Visibility governance: per-directory "Visibility" setting — "Public… all general website visitors will be able to see the members within this directory" or "limit visibility to Specific Groups… so only those logged-in members of the specific group can view the directory"; public directories can separately "show (or not show) the contact info of listed members".
- Per-member consent overrides: member-record settings "Hide on Website" / "Hide Contact Information on Website" / "Hide Address on Website" — "overrule any member type, global, or specific event settings"; the admin "can also decide whether members can update their directory preferences themselves"; "Members who opted in to Hide Contact Info… will remain hidden regardless of the directory settings."
- Profile surfaces: preview card ("Member Profile Badge": name always required, logo/headshot, phone, address with city/state-only option, email "or a secure contact form, if you prefer not to show emails directly", website/social links, member type from "Display Name for Directories") → full Member Profile Page (contact info, organization overview/professional bio, directory gallery with photos/videos, custom fields, contacts/related members list, primary contact, live social feeds, member-since fields).
- Profile composition is configuration: custom fields marked visible to Members can be added, removed, and rearranged per directory in a Profile Pages settings list; fields only render when the member has a value.
- Lookup: search by "company names, individual names, keywords"; custom-field filters and group/committee filters; combinable; Category View ("alphabetized list by category, each with its own unique URL" — example: Areas of Expertise for finding supplier members); Map View (geocoded shipping address, city/state/zip/county/country filters, search-near-address, use-current-location, hidden-address members excluded from map, paged results, list↔map toggle).
- Contact protection: Member Directory Contact Form (article notes a message limit), "Email Addresses Behind reCAPTCHA in Public Member Directories", "Deep Dive: Data Harvesting & Website Scraping".
- Monetization/prominence: Featured Directory Listings ("double as an advertising opportunity"; per-field display differences between featured and basic profiles; "Automate Featured Directory Listings with Optional Dues Rules"); member-to-member discounts as related machinery.
- Distinct search surfaces: "Difference Between Backend Members List Search & Frontend Directory Search" — admin registry search and public/member directory search are separate surfaces over the same records.
- Subject self-service: "Members can easily update their personal and company profiles within their Member Compass [member portal], ensuring their directory listing is complete, accurate."

## Cross-product Comparison

| Dimension | ICD | MembershipWorks | Brilliant Directories | Novi AMS |
|---|---|---|---|---|
| Population source | org-maintained roster (families + individuals), CSV import | membership database (join flow) | member accounts (admin-added or sign-up), CSV import | derived from groups/committees over member database |
| Record classes | families + individuals + staff | members (orgs/individuals), multi-location/contact | member listings (business/person), related records | companies + people, contacts/related members, beneficiaries |
| Standing attributes on records | membership status field | membership levels/labels gate access | join date, verified status, membership plan | approval status, benefit status (current/grace/inheriting), dues-paying vs beneficiary, join dates |
| Lookup | alphabetical order, search, groups | keyword + geo + faceted search, map | filters, geocoded location search, sorting | search + custom-field/group filters, category view, map view, sort rules |
| Audience postures | members (closed, app/website sign-in) | members-only or tiered access | public listing sites common, members-only content | public vs specific-groups per directory; contact-info toggle |
| Visibility governance | admin approval of member submissions; security posture | levels/labels access control; email hidden, relayed | hidden-by-membership-level add-on; free-plan spam governance | per-directory visibility + per-member hide overrides + field-level display (featured vs basic) |
| Subject participation | submit own updates/photos → approval | members manage profiles and deals | members manage their listings (claimable listings, login-as) | members update profiles via member portal; opt-out preferences |
| Contact/reach payload | direct: email/call/text/map from entry | relayed messaging (email never displayed), map | click-to-call, private chat, lead routing, reviews | direct display or secure contact form; reCAPTCHA; map directions |
| Outputs | print PDF/booklet, apps, members' website | website directory surfaces | directory websites (SEO-oriented) | web list/map/category, unique URLs |
| Prominence/monetization | none observed (ads via custom pages) | member deals, testimonials | featured members, upgrade incentives | featured listings, dues rules, member-to-member offers |
| Packaging | standalone product | module of membership suite | whole product = directory+membership sites | module of AMS (admin registry is the record system) |

Cross-product commonalities (Layer B):

1. Every product's population is the organization's own membership — a closed roster bound by belonging (congregation, association, chamber), not the open world.
2. Every product holds standing structured profiles per member: identity (name/photo/logo), reach attributes (contact/address/web), descriptive attributes (type/category/custom fields), and standing markers (status/type/join date).
3. Every product organizes retrieval: search and/or filter/browse structures over those attributes (alphabetical, keyword, faceted, category, map).
4. Every product has organization-governed publication: the org decides which members appear and what shows to which audience; per-member opt-out/consent machinery appears in all four in some form (moderated submissions, tiered access, hide-by-level, hide-on-website overrides).
5. Membership machinery is structurally adjacent in all four: status/level gates inclusion, visibility, or prominence; join dates appear as record attributes; approval-gated inclusion appears (Novi explicit; ICD moderation; BD admin-added/claimable).
6. Member self-maintenance of their own entry appears in all four (ICD moderated submissions; MW member-managed profiles/deals; BD member accounts/claimable; Novi portal updates + preference setting).
7. Contact-with-the-member is the payload: direct display, click-to-contact, relayed forms, or messaging — with email-protection patterns (hide + relay, reCAPTCHA) in the public-posture products.

Distinctive to subsets (held out of the defining core): print/PDF output (ICD only in sample; heritage form), map views (MW, Novi, BD-geocoding), featured/monetized prominence (MW/BD/Novi), deals/reviews/leads (MW/BD), messaging/chat between members (BD), scrapers/spam defenses (BD/Novi), AI assistants (BD).

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures:

1. **Membership-anchored population.** The directory's population is the organization's own members — people and/or member organizations — held as a roster whose inclusion is governed by the organization's membership records (approval, standing, type), not by open self-listing into an unbounded catalog and not by third-party curation of the outside world. Remove → a membership roll/registry (Congregation Membership Management / AMS territory) or a generic people/entity catalog (Directory Application).
2. **Standing member profiles built for lookup and reach.** Each member carries a persistent structured profile — identity (name, photo/emblem), reach attributes (contact, address, web), descriptive attributes (member type, category, custom fields), standing markers (status, type, join date) — and the directory organizes retrieval over these attributes (search, filter, category browse, alphabetical or mapped order) so specific members can be found and reached. Remove → a mailing list, an org chart note, or a raw export; the "directory" is gone.
3. **Organization-governed publication.** The organization decides which members appear, which attributes appear, and to which audience (public vs members-only), with per-member consent/opt-out as the common modern realization. Remove → an ungoverned data dump or an uncontrolled listing board; the org's directory as a deliberate publication act is gone.

Jointly-held is load-bearing:
- 1 alone = membership roll/registry (no lookup surface) — sibling Types' territory.
- 2 without 1 = generic Directory Application (operator-curated entities of any class).
- 3 without 1+2 = privacy policy with nothing to publish.
- 1+2 without 3 = roster dump; 1+3 without 2 = a gated list with no retrieval organization; 2+3 without 1 = a people-search over the open world (Whitepages territory).

### L1 — Common Mature Structure

- Member self-service maintenance of the entry (direct editing, or moderated submission→approval, or portal-based profile updates; preference/consent self-setting).
- Dual audience postures over the same records: members-only benefit directories and public-facing directories ("find a member business").
- Search + faceted/custom-field filters + category views; alphabetical and map-based organizations.
- Contact-relay forms and email protection for public postures; direct click-to-contact for member postures.
- Groups/committees/chapters as directory scopes → multiple sub-directories per organization.
- Photos/logos and profile galleries; member type/category display; join/since dates.
- Print/PDF companion output and CSV import/export (mailing labels).
- Admin roles around the directory (administrator, editors/volunteers, approval queues).
- Verification markers; featured/promoted listings as non-dues revenue.

### L2 — Variant / Optional Structure

- Audience posture as configuration: fully closed (congregations), tiered by membership level (access increments), deliberately public (chambers, "find a professional").
- Record-class emphasis: family/household units (congregations) vs organizations with staff/beneficiary lists (chambers/associations) vs individuals (alumni).
- Identity substrate for member access: email listed in the directory + secure link, app registration, member-portal sign-on / SSO.
- Monetization models: featured listings with dues rules, upgrade incentives, member deals, advertising custom pages.
- Packaging: standalone product vs module of membership suite/AMS vs plugin for existing websites.
- Data-protection postures: reCAPTCHA, scraping guidance, CAN-SPAM-compliant relays.
- Photo-directory emphasis vs business-directory emphasis.

### L3 — Vendor-specific Structure (research notes only)

- ICD: 3 editors standard/unlimited premium; booklet sizes; birthday/anniversary pages; import undo; "Family Label" customization; app offline mode.
- MembershipWorks: drag-and-drop profile template builder; keyword-ranking search engine claims; CAN-SPAM naming.
- Brilliant Directories: BD Butler AI queries; smart lists; credits/revenue sorting; specific add-on catalog names; login-as-member.
- Novi: random-hourly-reshuffle sort; benefit-inheritance "family tree" display rules; Member Compass; "Display Name for Directories" field; per-directory header/footer content regions; message-limit contact form.

## Historical / Market-Sample Check (§24 analog form)

- Printed congregational photo directory (mid-20th-century pattern, still common): roster of member families, photos, addresses/phones, alphabetical/grouped order for lookup, office-maintained, unlisted-by-request and staff-only listings as governance. Satisfies all three L0 legs at analog level. Subject self-service absent → correctly L1, not definitional.
- Annual association member directory / "buyer's guide" (printed, category-organized, advertising-supported): members listed by category with contact info; inclusion required membership; publication choices made by the association. Satisfies legs 1–3 with public posture.
- Alumni directories (printed): roster of graduates with class years and contact info, ordered for lookup. Satisfies with an alumni-anchored population.
- Conclusion: the Type is not defined by any digital-only feature. Maps, relays, apps, featured listings, reCAPTCHA, self-service portals are all standard-but-not-definitional. The membership anchoring, structured lookup, and publication governance are the stable spine across print and digital eras.

## Boundary Findings

### vs Directory Application (§02.11) — FLAG DISCHARGED (joint review verdict: KEEP-BOTH)

The lookup machinery is genuinely inherited: standing entries + attribute profiles + retrieval organization are shared structure, exactly as the directory-application pass predicted ("domain-scoped instance"). But this pass found load-bearing structure beyond the entity-class choice:

1. Population provenance is structurally different: entries exist **because of a membership relationship** with the operating organization — inclusion is gated by that organization's membership machinery (approval, standing, type), updates flow from it (Novi: group updates "automatically flow through"), and lapse removes standing. A generic directory's entries are operator-curated entities with no belonging semantics.
2. The record's subject is usually a participant: members hold credentials, maintain their own entries, and hold consent rights over their own data (all four products). Generic directory entries describe third parties who may never touch the system.
3. Publication is membership-aware: audience gating (public vs members-only), standing-driven prominence (Novi's dues/benefits ordering; BD's hide-by-level upgrade incentives; MW's level-based access), consent overrides (Novi per-member settings).

Removal tests both ways: strip the membership anchoring (operator-curated open-world entities) → Directory Application; strip lookup organization (keep roster + governance) → membership roll with outputs, not a directory. Verdict: keep-both — this leaf is the membership-anchored realization carrying the governance/participation structures; a consolidation pass could record it as a named segment of Directory Application, but the dedicated-product market (ICD; BD's membership mode) justifies keeping the leaf. (Written to STATUS Boundary Issues as a discharge.)

### vs Listings Platform (§02.11)

Consistent with the directory-application pass's record-temporality seam: a member directory entry is a standing record of a member; a listing is a current offer that expires or is consummated. Member "deals/offers" attached to entries (MW/Novi/BD) are adjacent machinery, not the record.

### vs Member Community Platform (§25) — FLAG DISCHARGED (ratified)

Removal tests recorded by that pass confirmed here: strip participatory spaces → the directory remains as a complete product (ICD has no participation surface at all); strip the directory → community remains but degraded (community pass: "profiles + directory" is a standard capability there). Keep-both: interaction container vs roster lookup surface.

### vs Member Portal (§25, unprocessed) — new joint-review note

The portal is the member's self-service surface (account, payments, preferences); the directory is the org's roster lookup surface. They meet at profile self-maintenance: Novi explicitly updates directory listings "within their Member Compass". Flag for the member-portal pass: expected keep-both with the profile-editing overlap documented.

### vs Membership Management System / AMS (§25, processed as AMS)

Registry/dues/renewals system of record vs the member-lookup/publication surface. The AMS pass lists member-directory as L1 (standard capability) — consistent: module realization is the dominant packaging, and this leaf documents the directory surface as realized both inside suites and by dedicated products. Keep-both.

### vs Congregation Membership Management (§25, processed) — watch-item discharged

"The directory is one output of the roll" (that pass). The roll system holds people/status and produces directories; this Type covers the directory surface as the product center — including standalone directory products that never hold dues/participation machinery (ICD). Capability-slice consolidation not warranted; keep-both.

### vs Social Profile Network (§01.05)

Consistent with the directory-application pass seam: profile networks center on self-authored presentation, follow graphs, and feeds; the member directory centers on the organization's roster and lookup. A member profile here has no follower semantics; prominence comes from standing/feature settings, not from the graph.

### vs CRM (§07) / Contact Discovery (§07)

Directory records are not relationship or workflow records; no deals/activities/owners. Population is the org's own members, not the market — opposite provenance from contact-discovery/enrichment platforms.

### vs People-search directories (Whitepages-class, covered by Directory Application)

The seam is population provenance, not "people vs businesses": Whitepages is a people directory over the open world; a member directory is a governed roster of the org's own people/orgs.

## Uncertainties

- Wild Apricot — the market's most-cited example of field-level directory visibility controls — was unreachable; the field-level visibility claim rests on MW (levels/labels), Novi (per-field featured/basic + per-member overrides), BD (hide-by-level). Wording kept at "mature products commonly provide…".
- Alumni-directory variant (Almabase unreachable) asserted from market structure only; no product-level claims.
- Community-embedded directories (Higher Logic-class) corroborated only via the member-community-platform pass's records, not fetched this pass.
- The exact prevalence of moderated vs unmoderated member self-editing is unknown; both forms are directly evidenced (ICD moderated; Novi direct portal editing with admin-set preference rights).
- Chapter/multi-level org directory hierarchies not directly evidenced this pass (chapter-management-platform pass touched the seam only).
- No precise numeric or default-value claims asserted (message limits, editor counts, reshuffle intervals are L3 product facts).

## Final Synthesis

A Member Directory is the membership organization's governed lookup surface over its own people: a roster whose population is anchored in the organization's membership records, held as standing member profiles with identity, reach, descriptive, and standing attributes, organized for retrieval, and published under the organization's control — which members appear, what shows, and to which audience, with the members themselves participating in maintaining and consenting to their own entries.

The directory structure (entries + lookup) is inherited from the general Directory Application structure; what makes this leaf stand is the membership anchoring of the population plus the governance and participation machinery wrapped around it, realized by both dedicated products and modules inside membership suites/AMSs.
