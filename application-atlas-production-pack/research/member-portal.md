# Research Notes — Member Portal

Leaf: Member Portal (DIRECTORY §25 Nonprofit, Membership & Religious Organizations)
Slug: member-portal
Research date: 2026-09-08
Methodology: WORKFLOW v1.1 / WRITING_GUIDE v1.1

## Research Goal

Understand the Application Type "Member Portal" from real products: what the member-facing self-service surface consists of, what members actually do in it, what gates access, how membership standing shapes the surface, how the organization governs it, and where its boundaries lie against the AMS/Membership Management System family, Member Community Platform, Member Directory, Member Benefits Management, gated-content "membership site" tools, and the generic Customer Portal.

## Initial Boundary

- Section 25 places this leaf beside Association Management System / AMS, Membership Management System, Membership Billing, Member Benefits Management, Member Directory, Member Community Platform — all processed or flagged.
- Prior passes pre-hung flags that this pass must discharge:
  1. AMS pass: "Member Portal (separate leaf) — the member-facing surface only. AMS products include a portal as one surface of the system; the portal leaf is the member-side Type. Remove the staff-side registry/lifecycle and only the portal remains." (research/association-management-system-ams.md)
  2. member-community-platform pass: "NEW FLAG for unprocessed §25 siblings: member-portal (member's self-service surface vs peer-to-peer participation; overlap on profile/self-service elements — keep-both expected, ratify from that side)."
  3. member-directory pass: "NEW JOINT REVIEW FLAG for member-portal … the two Types meet at member profile self-maintenance — Novi documents members updating their directory listings 'within their Member Compass' … expected keep-both (portal = the member's self-service account/benefit surface vs directory = the org-facing roster lookup/publication surface), to be ratified from the member-portal pass."
  4. member-benefits-management pass: "watch member-portal (benefits presentation surface)."
- Adjacent portal Types elsewhere in the atlas: mortgage-borrower-portal (§08), tenant-resident-portal (§17), customer-portal (§07), employee-service-portal (§10) — the atlas has a <relationship>-portal family; Member Portal is the membership-relationship member of that family.
- Vocabulary hazard: "member portal" is also used by credit unions (= Online Banking Portal), health plans (a capability inside Health Plan Administration System — observed in that pass's source capture), and golf/club systems (a nav module — observed in research/golf-course-management.md [A]). The word "member" names different counterparty relationships in each.

## Research Questions

1. What exactly do member-facing "portal" surfaces expose? Which tabs/pages/fields?
2. What can a member DO (view vs change) through the portal, and what does each action write back to?
3. What gates access — login, membership status, member type, role (company contacts)? What happens to lapsed/suspended members?
4. Where is the account layer's boundary — do non-members have portal accounts?
5. How does the organization govern/configure the portal (settings, per-type content, field locks, disabling self-service)?
6. How does the portal sit relative to the org's website (embedded area vs app vs standalone)?
7. Where is the seam vs the AMS (staff-side), vs Member Community (peer participation), vs Member Directory (roster lookup), vs gated-content membership-site tools?

## Representative Products

| Product | Market position | Why sampled | Evidence tier reached |
|---|---|---|---|
| Wild Apricot (Personify) | small-staff associations/nonprofits/clubs/chambers; portal = logged-in members' area of the org's own Wild Apricot site + member mobile app | portal explicitly headlined ("Member Portal"); strongest operational docs; member-side seat is the product's marketing center | Tier-1 help articles (4 full articles) + Tier-2 feature page |
| Novi AMS | small/mid associations and chambers (US); portal = "Member Compass" on the association's Novi-built site | the portal has a dedicated KB collection and a flagship self-service-hub article; individual-member AND organization-member (company/family-tree) populations documented | Tier-1 (flagship article full text) |
| GrowthZone AMS / ChamberMaster | mid associations + chambers; product family (GrowthZone AMS, ChamberMaster, MemberSuite, MemberZone) | org-member (chamber business membership) pole; portal named on product pages | Tier-2 only (help center login-walled — limitation recorded) |
| Glue Up | global all-in-one association suite (multi-region) | suite-posture pole; portal = member self-service through "My Glue" web+app | Tier-2 (product pages) |
| MemberSpace | contrast pole — "membership site" tool adding gated content/memberships to any website | boundary anchor: content gating without an organization's member records | Tier-2 product page |
| Cobot (cross-domain anchor) | coworking management — named "member portal (manage plan, bookings, payments)" and per-location Members Portal | shows the same member-side surface recurring in another membership business | [A] captured in research/coworking-flexible-workspace-management.md |
| Club-management systems (cross-domain anchor) | "Member Portal" as a named nav module beside Member Management, POS, tee sheet | same recurrence in club market | [A] captured in research/golf-course-management.md |

## Sources

Tier-1 (official help/knowledge base, directly observed):

- Wild Apricot Help Center (Elevio KB; full article text embedded as JSON-LD in page HTML):
  - "Member access to their profile" — https://gethelp.wildapricot.com/en/articles/161-member-access-to-their-profile
  - "Member access to renewal and level changes" — https://gethelp.wildapricot.com/en/articles/162-member-access-to-renewal-and-level-changes
  - "Member access to invoices and payments" — https://gethelp.wildapricot.com/en/articles/163-member-access-to-invoices-and-payments
  - "Can a lapsed member see member-only pages or ticket types?" — https://gethelp.wildapricot.com/en/articles/1768-can-a-lapsed-member-see-member-only-pages-or-ticket-types
  - "Why are non-member contacts able to log in" — https://gethelp.wildapricot.com/en/articles/1756-why-are-non-member-contacts-able-to-log-in
  - "Can a suspended member log in restore their membership" — https://gethelp.wildapricot.com/en/articles/1765-can-a-suspended-member-log-in-restore-their-membership
- Novi AMS Knowledge Base (Pylon KB):
  - Collection "Member Signup & Member Compass" — https://help.noviams.com/collections/4666526414-member-signup-%26-member-compass
  - "Navigating the Member Compass: Novi's Self-Service Hub" — https://help.noviams.com/articles/8026345875-navigating-the-member-compass-novi-s-self-service-hub
  - Sub-collection "Member Compass" — https://help.noviams.com/collections/4212766500-member-compass

Tier-2 (official product pages):

- Wild Apricot — Membership Management feature page: https://www.wildapricot.com/features/membership-management-software
- GrowthZone — ChamberMaster product page: https://www.growthzone.com/chambermaster ; GrowthZone AMS page: https://www.growthzone.com/growthzone-ams ; site root: https://www.growthzone.com/
- Glue Up — Membership Management page: https://www.glueup.com/membership-management-software ; My Glue App page: https://www.glueup.com/features/glue-up-app ; site root: https://www.glueup.com/
- MemberSpace — https://www.memberspace.com/

Unreachable / abandoned (per source-access rules):

- Novi: www.noviams.com/novi-support (404), support.noviams.com (transport error) → resolved via help.noviams.com.
- GrowthZone: support.chambermaster.com (transport error), help.growthzone.com (JUNO event-platform help center, not AMS), support.growthzoneapp.com (product login wall) → GrowthZone claims restricted to product-page level; no operational detail asserted.
- Glue Up: /member-portal path 404; member-facing detail drawn from product pages only.
- r.jina.ai rendering proxy for Wild Apricot help (timed out once) → abandoned; full article text obtained directly from page-embedded JSON-LD instead.

## Product Observations

### Wild Apricot (Tier-1 [A] + Tier-2 [A2])

Portal placement: the portal is the members' logged-in area of the organization's own Wild Apricot website ("Build a Branded Website & Member Portal – No Coding Required"; members-only spaces; "Set a landing page for where members land after logging in and even customize it for each membership level"; per-page access controlled "which member levels or groups are given access to each page"). [A2]

Account and profile surface (article 161): "Members can access their profiles by logging in"; after login a profile link appears (name / profile icon / "View profile"). "My profile" area comprises:

- Edit profile (member edits and saves; non-member contacts can also edit their profiles; admin customizes the page under Website > System pages > Contact profile > Edit). [A]
- Privacy settings — member chooses per-field visibility: everyone / members only / hidden; "If a lock icon appears beside a field, the admin has locked the privacy settings for that field, and members cannot change their individual privacy setting." [A]
- Member photo albums inside the profile. [A]
- Event registrations tab — "view all their current and past event registrations"; cancel a registration if the admin setting allows; "Canceling a paid registration within My profile will automatically void the registration invoice and generate a credit in the registrant's account." [A]
- Invoices and payments tab — "view payment history and make payments on invoices." [A]
- Donations tab — one-time and recurring donations; "Users can select Stop next to a recurring donation." [A]
- "My directory profile" — preview how the public profile displays to others based on privacy settings. [A]

Renewal self-service (article 162): "WildApricot allows your members to manage several aspects of their own memberships, including membership renewal, automatic dues payments, and membership level changes."

- Renew from the renewal-notice email link or inside the profile; renewals may also run automatically (automatic renewal payments). [A]
- Renewal-window policy: "When a member is limited to renewing only one period ahead or only a certain number of days or months ahead, a notice … will appear in place of a membership renewal link until the renewal window has begun." [A]
- On login, a corner message surfaces unpaid invoices, incomplete registrations, outstanding balances → opens the profile to confirm/cancel renewal and pay. [A]
- Member can "Cancel renewal and void invoice" for an initiated-but-unpaid renewal; can stop automatic renewal payments from the profile. [A]
- The help-center TOC names an admin capability "Disabling the ability for members to manage their own renewals" — self-renewal is admin-governable; the feature page also says "limit self-renewals for specific members or membership levels." [A]
- Membership level change by the member is a documented flow (with proration questions in the FAQ corpus). [A]

Financial self-service (article 163): "WildApricot offers several self-service functions for members and other contacts, including viewing their financial history and paying for one or more invoices online." Open/partially paid invoices appear at the top; multiple invoices can be paid at once; account credits can be applied; invoices are generated by transactions, event registration, membership application/renewal; join + event registration can be combined into one payment. [A]

Standing gating (article 1768): "A lapsed member is not allowed to view member-only pages, register using member-only ticket types, complete polls, add comments to blog pages, or post or reply to forum topics. As well, they do not receive automatic renewal notices, poll announcements, or appear in member directories." [A]

Account layer beyond members (articles 1756/1765): "Non-member contacts are sent login information if they register for an event, make a donation, or purchase a product … They need to be able to log in so that they can view or cancel registrations, view or pay outstanding invoices, manage recurring donations, and update their email and privacy settings." "A suspended member can still log into your site, but as a non-member contact … A suspended member cannot restore their membership, but they can apply for membership like anyone else." [A]

Member mobile app (feature page + article corpus): members browse directories, register for events, manage profiles; admins use the same app for approvals/check-in. [A2]

### Novi AMS (Tier-1 [A])

Naming and placement: "The Member Compass is your members' profile and guide to their information within your association." It lives on the association's own Novi-built website at /member-compass (direct-link convention documented per tab and per field). "An individual must first create a user account. Once they are logged in, they will be able to see and access their profile information, membership status, transaction history, ecommerce orders, event registrations, and more." "Non-members with a login still have their own Member Compass but cannot access members-only information." [A]

Tabs (documented with direct links): Dashboard, Pay Balance, Account History, My Events, Continuing Education, My Orders, My Involvement, Profile, Login & Password, Payment Methods, Company/Companies, People, Reports. [A]

- Dashboard: "a customized message from you, their membership status, any outstanding invoices, upcoming events, and featured blog categories." Membership status "will display differently if the logged-in individual has their own membership, inherits benefits from their company's membership, or simply has a user account"; inherited status includes company name + company member type. "Member Since" display (term start / original join date / not displayed) is an Association Setting. [A]
- Pay Balance: open transactions billed to self or to a company in the "family tree"; choose Full Balance / Overdue Balance / Specific Invoices; optional dues items reviewable per invoice; saved card payment; Auto-Pay opt-in at payment and opt-out in Payment Methods; partial payments when the association enables them ("balance stays open until fully paid"). [A]
- Account History: transaction/invoice list with details, pay, bulk print; sorting by balance/billed-party/date/due/status/total. [A]
- My Events: Upcoming (add to calendar; Join button for private webinar links from shortly before start) and Past (Attended/Not-Attended status when recorded); "Edit Registration" to update attendee details; company-privileged users see related people's registrations via "Show Related Registrations." [A]
- Continuing Education: credits awarded for attendance + manually added; downloadable CE report; "This section only appears if your association awards credits." [A]
- My Orders: ecommerce orders, fulfillment status, tracking, subscriptions. [A]
- My Involvement: committee participation history (future/current/historical terms, public role), shown only for committees the org marks "Visible in the Member Compass" / "public role." [A]
- Profile: edit contact info and custom fields; "To maintain data integrity, individuals must contact the association to request a change to their name, title (prefix), and/or suffix"; parent-company change is a per-association setting. [A]
- Login & Password: view contact email vs login email; change login email/password (current password required). [A]
- Payment Methods: add/update/delete saved cards; manage membership auto-pay status. [A]
- Company/Companies + People (company-privileged only): edit company info (company name is admin-only); add/remove people from the company list (removal detaches parent company but does not delete the record); assign open seats for seat-based memberships; grant management access; removal of Primary/Billing Contacts is blocked in the portal ("reach out to the association"). Settings gate the People tab entirely — "For trade associations with company members, we recommend that this setting is turned ON … For a society with individual members, you may want this turned OFF." [A]
- Reports: org-shared custom reports surfaced to non-admin users (print to PDF / export to Excel); tab appears only with reports access. [A]

Visibility rule: "Logged-in individuals may see different tabs in their Member Compass, based on their membership status, engagement, and whether or not they have management access to their company's account." [A]

Membership creation/renewal from the Compass: expired/lapsed renewal; grace-period renewal; current member self-renew when auto-renewal is off and self-renewal-before-expiration is allowed; non-member/prospect with login joining individual membership; company membership via primary/billing contact of a non-member/prospect company. [A]

Org content into the portal: dedicated articles "Maximize the Member Compass with Content and Direct Links" and "Adding Specific Member Type Content to the Member Compass Dashboard" — the org authors dashboard content per member type. [A] (collection titles)

### GrowthZone AMS / ChamberMaster (Tier-2 [A2] — operational docs unreachable)

- ChamberMaster product page: "From automated renewal reminders to self-service member portals, ChamberMaster makes retention easier…"; billing tools "handle invoicing, payment processing, and automatic reminders"; "Give your members enhanced directory profiles with business categories, ability to post special offers with Hot Deals, job postings, and multi-location listings. Members can update their own profiles anytime, and changes appear instantly on your website." [A2]
- GrowthZone AMS product page: "…all while giving members the ability to self-serve through their membership portal." [A2]
- Site root confirms product family (GrowthZone AMS / ChamberMaster / MemberSuite / MemberZone) and market (associations + chambers). [A2]
- No operational (Tier-1) claims made from this product; portal shape inferred only at the level the product pages state.

### Glue Up (Tier-2 [A2])

- Membership page: "Member Self-Service — Let members update profiles, renew memberships, pay invoices, register for events, access directories, and manage their experience through My Glue." FAQ: "…provides self-service options to members allowing them to renew their membership, update their contact information, register for events and pay dues from their computer or mobile device." [A2]
- My Glue app page: "Renewal Management / Upcoming Events & Community / Membership Directory / Newsletters & Notifications"; "an all-in-one app that lets them get the most of their memberships from palm of their hand"; event session documents & presentations. [A2]
- Suite context: CRM, Events, Email, Community, Memberships, Finance & Invoicing, CPD/CPE, Chapters, Websites as modules; My Glue is the member-facing app of the suite. [A2]

### MemberSpace (Tier-2 [A2] — boundary pole)

- Self-description: "Membership Site Software … Using your existing website — offer communities, courses, and premium content"; install via code snippet on any website (Squarespace/Wix/WordPress/Webflow/Notion…); "Create spaces for members … Offer whatever membership pricing you want and manage everything from one simple dashboard." Members pay the site owner for access to gated content/courses/community. [A2]
- Structural contrast: no organization-side membership record semantics (no dues invoices ledger the member settles, no org-managed standing/renewal of organizational status, no staff-side registry) — the "membership" is a content-access subscription on the site owner's terms.

### Cross-domain anchors (from prior passes, [A] there)

- Cobot (coworking): "member portal (manage plan, bookings, payments)"; per-location "Members Portal" (research/coworking-flexible-workspace-management.md).
- Club management: "Member Portal" as a named navigation module (research/golf-course-management.md).
- Fitness membership management: member self-service portal/app classified as standard-not-definitional for that Type; gym-management-system final doc: "Membership Billing / Member Portal | narrower / companion | the money machinery alone, or the member-side window onto these records; neither keeps the register nor runs the door."

## Cross-product Comparison

| Structure | Wild Apricot | Novi | GrowthZone/ChamberMaster | Glue Up | Evidence |
|---|---|---|---|---|---|
| Login-anchored portal on/attached to the org's own web presence | yes — logged-in area of org's Wild Apricot site; per-level landing page | yes — /member-compass on the association's Novi site; per-tab/per-field links | asserted ("self-service member portals") | asserted + My Glue app | 2/2 Tier-1 confirm; 2/2 Tier-2 assert |
| Membership standing displayed and status-differentiated | profile + status; lapsed loses member-only reach | Dashboard shows status (own vs inherited vs account-only) | asserted renewal/retention framing | asserted ("renew memberships") | 2/2 Tier-1; consistent |
| Self-service dues/invoices/payment methods | invoices+payments tab; multi-invoice pay; credits; stop recurring donations; stop auto-pay | Pay Balance; Account History; saved cards; auto-pay opt-in/out; partial pay (setting) | invoicing/payments asserted | "pay invoices … pay dues" | 2/2 Tier-1; 2/2 assert |
| Renewal self-service under org policy | renew in profile/email; renewal window notices; cancel renewal+void invoice; admin can disable self-renewal; limit per level | lapsed/grace/self-renew flows documented; requires-login scenarios enumerated | "automated renewal reminders" | "renewal management" | 2/2 Tier-1; 2/2 assert |
| Profile self-maintenance with org-locked fields | privacy per field (admin-locked fields); admin customizes edit page | name/title/suffix admin-mediated; parent-company change per-association setting; company name admin-only | "Members can update their own profiles anytime" | "update profiles" | 2/2 Tier-1; 2/2 assert |
| Event registration self-service | view/cancel registrations (policy-gated; cancel voids invoice → credit) | My Events upcoming/past; edit registration; related-company view | events in suite | "register for events" | 2/2 Tier-1; 2/2 assert |
| Member-only content spaces | member-only pages/ticket types/forums/blogs gated by status | "members-only information" gate; dashboard content per member type | directory profiles + Hot Deals | "access directories"; community in suite | 2/2 Tier-1; consistent |
| Org configuration of the surface | system-page customization; admin-locked privacy; disable self-renewal; per-level landing | Association Settings (member-since display, people management on/off, parent-company change); committee visibility flags; per-type dashboard content; report sharing | product-page posture | suite admin configures modules | 2/2 Tier-1 explicit; strong |
| Account layer beyond members | non-member contacts log in after transactions; suspended member = non-member contact view | non-members with accounts have a Compass without members-only info | not stated | not stated | 2/2 Tier-1 |
| Organization-member (company) delegation | not evidenced | Company/Companies + People tabs; primary/billing contact; management access; seat-based memberships; family tree | chamber business-membership market; self-serve directory listings | not evidenced | 1/2 Tier-1 explicit + market context — treat company-delegation depth as common for org-member orgs, not universal |
| CE credits surface | not evidenced | Continuing Education tab + downloadable report (if org awards credits) | GZ Learn add-on exists | CPD/CPE module exists | 1/2 Tier-1; common capability, optional |
| Branded mobile member app | yes (member app) | mobile-friendly site emphasized | not evidenced | yes (My Glue) | 2/4 — common, not definitional |
| Committee/involvement history | not evidenced | My Involvement (org-visibility flags) | not evidenced | not evidenced | 1/4 — optional |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (jointly held; remove any leg and the Type collapses)

1. **Member-anchored authenticated access to the organization's own systems.** The member signs in with an account tied to the organization's member records; the membership relationship — its standing, type, and whether held directly or inherited — is the primary axis structuring who is recognized, what is visible, and what may be done. The account layer commonly extends beyond members (contacts with transaction relationships also hold accounts) but standing still differentiates reach. Remove → public website / member bulletin (no gate, no axis).
2. **Member self-service over the member's own relationship.** Through the surface the member directly views their own state (standing, financial records, registrations, involvement) and performs consequential actions — renew and pay dues, settle or manage invoices, update profile information, manage payment methods and registrations — that take effect in the organization's records rather than being staff work requested by email/phone. Remove → static gated content area / document archive (nothing to act on).
3. **Organization-governed configuration of the surface.** The organization decides what the portal exposes — which pages/tabs/fields and content appear, for which member types and statuses — and can govern or withdraw individual self-service actions (disable self-renewal, lock fields, require staff-mediated changes, gate cancellation, share or withhold reports). The portal is the organization's surface onto its records, not a fixed product shell and not the member's private app. Remove → generic fixed account center (customer-portal territory) or an ungoverned site area.

Load-bearing tests:
- 1+3 without 2 = member-bulletin / gated content area (MemberSpace pole, the pre-history of "member area").
- 1+2 without 3 = fixed generic account center (loses the membership-org artifact; drifts to customer-portal territory).
- 2+3 without 1 = staff-side forms/processes with no authenticated member seat (the paper pre-history).
- Single legs: 1 alone = login wall; 2 alone = transaction checkout; 3 alone = org website.

### L1 — Common Mature Structure (market-defining expectation, not definitional)

- Dues/invoice self-service (view, pay, payment methods, credits, auto-pay opt-in/out) — 4/4.
- Renewal self-service bounded by org policy (windows, per-level limits, disable switches, grace semantics) — 4/4.
- Profile self-maintenance with governance (some fields org-locked / staff-mediated) — 4/4.
- Event registration history/management — 4/4 (depth varies).
- Dashboard/home surfacing standing + outstanding items + org content — 3/4 explicit.
- Member-only content spaces and directory access/self-update attached to the portal — 3/4.
- Branded member mobile app or mobile-first access — 2/4 explicit; market-defining expectation.
- Self-service landing of join/renew funnels (account-first scenarios for non-members/prospects/lapsed) — 2/2 Tier-1.

### L2 — Variant / Optional Structure

- Surface form: logged-in area of the org's own website (Wild Apricot, Novi) ↔ dedicated branded mobile app (Wild Apricot app, My Glue) ↔ standalone portal site; direct-link conventions (/member-compass).
- Population shape: individual members ↔ organization members (chamber business membership: primary/billing contacts, management access, seat-based dues, people management, family tree) — depth of delegation varies; societies may deliberately disable people self-management.
- Suite position: portal as surface of an AMS/MMS suite (all sampled) vs portal-first packaging; community forums/LMS/CE modules attached or separate.
- Content depth: gated pages, resource libraries, forums, per-member-type dashboard content, org-shared reports.
- Presentation extras: CE credit histories, involvement/committee histories, member-since display, e-commerce order histories.
- Regional/deployment: white-labeling, SSO federation, multi-chapter scoping (not deeply evidenced this pass — weak claims only).

### L3 — Vendor-specific (research notes only; excluded from final document)

- Wild Apricot: "My profile" tab naming; member photo albums; "Cancel renewal and void invoice" phrasing; Elevio help center; PSSF servicing fee; per-level landing pages; mobile-app admin/member split.
- Novi: "Member Compass" naming and /member-compass path; family-tree vocabulary; Full/Overdue/Specific-Invoices balance picker; webinar Join-button timing (15 minutes); CECs private-to-individual rule; "trade association ON / society OFF" people-setting recommendation; Pylon KB.
- GrowthZone: product-family naming (GrowthZone AMS / ChamberMaster / MemberSuite / MemberZone); GZ Pay merchant portal (a different, staff-side portal — do not conflate); JUNO help-center split.
- Glue Up: "My Glue" naming; reward points program; NVIDIA/AI marketing framing.
- MemberSpace: snippet install model; platform list; $350M marketing claim.

## Historical / Market-Sample Check

- Early-2000s association website with a member login area — renew via online form, update contact details, download receipts, view members-only documents — satisfies all three L0 legs with no mobile app, no auto-pay, no per-type content, no community. ✓
- Paper-era analog: the member-services counter + mailed renewal invoice + "update your details" form + printed member card. The member acts on their own relationship, but through staff-mediated paper — this is the pre-history the portal digitized; the self-service leg fails at analog level (the routine exists but the self-service surface does not). Correct failure.
- BBS-era/dial-up member areas with profile editing and dues tracking: satisfy (thin ancestor). ✓
- Club/coworking/fitness membership businesses run member portals on the same structure (cross-domain anchors), so the definition is not §25-association-specific. ✓
- The definition names no specific technology (no "app", no CMS, no SSO), no specific status vocabulary (current/lapsed/grace named as examples only), and no specific tab set. ✓

## Boundary Findings

1. **vs Association Management System / Membership Management System (§25)** — DISCHARGES the AMS pass's pre-hung framing. The AMS is the staff-side system of record (registry, lifecycle, billing machinery, communications); the portal is the member-side self-service surface onto those records. Removal test both directions: from the portal, remove the staff-side seat → portal remains a portal; from the AMS, remove the member-side surface → AMS remains the registry. Products bundle both; the leaf documents the member-side Type. KEEP-BOTH ratified from this side.
2. **vs Member Community Platform (§25)** — RATIFIES that pass's flag as keep-both. Portal = member↔organization self-service (member acts on their own relationship; org publishes content); community = peer-to-peer participatory spaces (members create the content; discussion threads canonical). Overlap zone: profile self-service and org-published content exist in both. Removal tests: strip participatory spaces from a community → portal-like self-service shell remains; strip transactional self-service from a portal → gated content area remains (not a community). No sampled portal requires member-authored discussion; no sampled community requires dues settlement as its center.
3. **vs Member Directory (§25)** — RATIFIES that pass's flag as keep-both. Directory = the organization-facing governed lookup surface over the roster; portal = the member's own self-service surface. They meet at profile self-maintenance: Wild Apricot "My directory profile" preview + privacy settings; Novi directory visibility via profile; ChamberMaster "Members can update their own profiles anytime, and changes appear instantly on your website." Directory visibility preferences are commonly edited through the portal, but the lookup/publication machinery is the directory's object, not the portal's. Strip self-service account actions from a portal → directory still stands; strip the roster lookup → portal still stands.
4. **vs Member Benefits Management (§25)** — DISCHARGES the watch-item. Benefits programs may present inside the portal and may use portal login as their verify-and-redeem mechanism (the benefits pass itself recorded "member login, org sign-on" as program-issued mechanics), but the benefit offering catalog, eligibility scope, and redemption mechanics are not the portal's defining core: a portal without a benefit program remains a portal; a benefits program can run without owning a portal (standalone deep links documented in that pass). KEEP-BOTH.
5. **vs gated-content "membership site" tools (MemberSpace pole)** — content-gated member areas without org-record write-back and membership-standing semantics are a different Type (monetized gated content on the site owner's terms). Remove L0-2 (self-service over an organizational relationship) → the artifact collapses into this pole. The word "member" is shared; the counterparty relationship is not.
6. **vs Customer Portal (§07)** — same surface shape (account, invoices, payment methods, history). The discriminator is the anchoring relationship: commercial customer/order relationship vs organizational membership (dues, standing, renewal, inherited benefits, involvement). The customer-portal pass independently reached the same family framing (portals named by relationship).
7. **vs Employee Service Portal / Employee Portal (§09/§10)** — structural sibling over the employment relationship; same self-service grammar, different standing semantics and record owners. Named for the taxonomy's portal family.
8. **Vocabulary blur (recorded, no directory change)** — "member portal" is also the market term for credit-union online banking surfaces and health-plan member surfaces; both belong to other Types (Online Banking Portal; Health Plan Administration System's member capability). Club/coworking/fitness systems embed member portals as modules — those passes correctly held the portal as a non-definitional standard capability for their operator-side Types; this leaf canonizes the member-side surface itself.

## Type-status Verdict

Member Portal stands as a separate Application Type: the member is a distinct primary user with distinct jobs, the market names the surface as a category (Wild Apricot headline feature; ChamberMaster "self-service member portals"; GrowthZone "membership portal"), and the atlas already contains a <relationship>-portal family (borrower, tenant, exhibitor, customer, employee). It is a member-side surface Type, deliberately narrow, whose value is the seam it maintains against the staff-side AMS and the participatory community.

## Uncertainties

- GrowthZone/ChamberMaster operational depth (portal tab structure, renewal-window mechanics, company delegation) unverified — help center login-walled; only product-page claims held, so no GrowthZone-specific behavior is asserted anywhere.
- Glue Up portal detail limited to product pages; whether My Glue includes invoice-level payment flows (vs marketing summary) unverified at Tier-1.
- Non-English/regional products (e.g., European association suites) not sampled; SSO/white-label depth recorded as weak L2 only.
- Whether any standalone "portal-only" product (a portal sold without an AMS behind it) exists as a meaningful market population: not found this pass; the market realization observed is portal-as-surface-of-a-suite plus the portal-first *positioning* of Wild Apricot. The Type is defined by the member-side seat, not by packaging.
- Wild Apricot article 162's "Disabling the ability for members to manage their own renewals" was observed as a TOC heading (admin capability), not read in full — the existence of the capability is held [A], its mechanics are not asserted.
