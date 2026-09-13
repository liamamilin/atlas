# Research Notes — Shared Team Calendar

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what a "Shared Team Calendar" is as a directory leaf (§03.08 Calendar family): what the market ships under and around the concept, what the defining structure of a calendar shared with a group of people is, who holds which roles, how sharing and permission machinery actually works across dedicated products and calendar suites, and where the Type's boundary sits.

Two pre-hung flags frame this pass:

1. **calendar-application pass (2026-09-06)** flagged the §03.08 siblings as "audience/object variants of the same defining structure (shared team calendar = the Type's sharing+permission machinery pointed at an organization; resource calendar = a calendar owned by a bookable resource…)" and called for joint review when this leaf is processed.
2. **resource-calendar pass (2026-09-08)** discharged that flag, determined Resource Calendar an object/subject variant of Calendar Application, and recommended "the same treatment expected for sibling shared-team-calendar — its pass should confirm the triad framing (calendar / shared team / resource)".

This pass must decide with evidence: independent Type, calendar-family variant, or capability — and confirm or refute the triad framing.

---

## Initial Boundary

Working hypothesis at step 1:

- **What it is:** a calendar maintained as the shared schedule of record for a defined group of people (team, organization, department, family): multiple members consult it, and — within permission tiers — add and change its entries. The events are of common concern to the group (meetings, deadlines, shifts of note, holidays, launches, vacations).
- **Who uses it:** a calendar administrator/owner who creates the calendar and governs access; editors who maintain events; ordinary members who read it (and sometimes add); occasionally external parties who consume read-only feeds.
- **Nearest neighbors:** Calendar Application (parent structure), Resource Calendar (sibling §03.08 leaf, processed 2026-09-08), Meeting Scheduling Application, Team Messaging Application, Family Organizer, Employee Scheduling Platform, Project Management.
- **Likely confusion #1:** suite-native *group* calendars (a Microsoft 365 group's calendar) — is the group calendar a product in its own right or the calendar's sharing machinery realized through a group container?
- **Likely confusion #2:** public events calendars (published/embedded) — publication of a team calendar is a distribution surface, not the Type itself.
- **Unknowns at start:** is explicit permission tiering definitional or common? Does a dedicated standalone product category exist (unlike resource calendar)? How do link-based (no-account) access models fit? Is event-ownership tracking ("modify my own events") common?

---

## Research Questions

1. What is the object of record — one shared schedule? multiple named calendars inside it? who owns it?
2. Who are the members and what roles/permission tiers exist (view / edit / add / manage)?
3. How do members gain access (accounts, invitations, links, directory groups)?
4. What goes on the calendar, and who puts it there? Is event authorship tracked ("my events")?
5. How do members consume it (web, mobile, subscription feeds, embedding, suite clients)?
6. What change-visibility machinery exists (notifications, agendas, update emails)?
7. Which parts are invariant vs common vs variant across dedicated products and suite-native realizations?
8. Where is the seam vs Calendar Application (parent), Resource Calendar (sibling), Meeting Scheduling, Team Messaging, Family Organizer, Employee Scheduling?
9. Historical check: would a paper team wall calendar, a whiteboard planner, or 2000s-era group schedules still fit the definition?

---

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different layers of the stack:

| Product | Form | Why sampled |
|---|---|---|
| **Teamup Calendar** | dedicated standalone shared-calendar product (web-first, link/account access) | the clearest archetype of "shared calendar" sold as a product; deepest Tier-1 KB (permission levels, access modes, feeds) |
| **TimeTree** | mobile-first consumer shared calendar | the consumer/social pole: group-based shared calendars with communication around events; help center unreachable (see Sources) |
| **Microsoft Outlook / Microsoft 365 shared & group calendars** | suite-native sharing inside a calendar service | the enterprise realization: per-person permission tiers, delegate management, and group calendars as a byproduct of group membership |
| **Apple Calendar (shared calendars)** | platform-native sharing | carried Tier-1 evidence from the calendar-application pass (iCloud calendar sharing, publish/subscribe) |
| **Google Calendar (shared calendars)** | suite-native, second ecosystem | market anchor; official docs unreachable (same wall as two prior passes) |

Sample spans: dedicated product vs suite-native vs platform-native; enterprise vs consumer; account-based vs link-based access. Teamup and TimeTree answer the "standalone product category" question affirmatively — a structural difference from the resource-calendar case.

---

## Sources

**Fetched successfully this pass (Tier 1 unless noted):**

- Teamup — "Customizable shared calendar for business" (product site): https://www.teamup.com/
- Teamup — "Access Permission Levels" (KB): https://calendar.teamup.com/kb/what-are-access-permissions/
- Teamup — "User Account Access vs Calendar Links" (KB): https://calendar.teamup.com/kb/how-to-choose-between-account-access-or-calendar-links/
- Teamup — "Sync with iCalendar Feeds" (KB, reached via blog redirect): https://calendar.teamup.com/kb/what-are-icalendar-feeds (fetched as https://blog.teamup.com/what-are-icalendar-feeds)
- Microsoft — "About shared mailboxes, shared folders, and shared calendars in Outlook": https://support.microsoft.com/en-us/outlook/sharing/about-shared-mailboxes-shared-folders-and-shared-calendars-in-outlook
- Microsoft — "Microsoft 365 Groups and Microsoft Teams" (Microsoft Learn): https://learn.microsoft.com/en-us/microsoftteams/office-365-groups
- Microsoft — Outlook help & learning hub (Sharing & delegate topic structure): https://support.microsoft.com/en-us/outlook/

**Unreachable (abandoned per network rules):**

- Google Calendar sharing documentation (support.google.com/calendar/answer/37095) — timeout; the calendar-application pass (2× timeout) and resource-calendar pass (2× timeout) recorded the same wall. Google is held as a market anchor only; no Google-specific claims are made.
- TimeTree Help Pages (support.timetreeapp.com/hc and article URL) — timeout + transport error ×2. TimeTree evidence is product-page strength (Tier 2) and is kept at capability level.
- Teamup KB article "What are access permissions" — failed once (transport error), succeeded on retry; all cited Teamup KB content was retrieved successfully on the retry attempt.

**Carried corpus evidence (from sibling passes' documents/notes, Tier 1 in the original pass):**

- calendar-application.md — Apple Calendar: share iCloud calendars (edit or view-only); publish read-only to a web address others subscribe to; non-creators of an event can only change their own acceptance status. Outlook Calendar: permissions granted by the calendar owner (view-only vs create/edit on shared calendars); Delegate Access; group schedules; share/subscribe.
- resource-calendar.md — sibling determination and triad framing.
- family-organizer.md — "Calendar Application / Shared Team Calendar — single-layer neighbor: a shared calendar alone, typically in a work context, without the household circle or the items layer."

---

## Product Observations

### Teamup Calendar (dedicated standalone product) — Tier 1

Evidence layer A (directly observed in official docs).

**Positioning**
- "The only customizable calendar for business… helps businesses organize schedules, resources and teams"; "a shared calendar keeps everyone on the same page"; use cases: field crews, operations, event planning, education, sports, nonprofits; "effortless to share on any device, platform, or across organizations." [A]

**Object structure**
- A Teamup calendar contains **sub-calendars** — named, color-coded event containers (referenced throughout the KB: permissions assigned "for each individual sub-calendar", feeds "with selected sub-calendars combined into one feed"). [A]
- Events carry rich content: images, files, links, notes, **time-stamped event comments**, **signups**; custom event fields; "each event is a hub of connected information." [A]

**Roles and permissions (the "9 levels of access control")**
- A **calendar administrator** configures the calendar and assigns permissions "for users and links"; only administrators can add users, create groups, manage feeds and settings. [A]
- Eight user permission levels + administration access: **Modify** (view/create/modify/delete), **Read-only**, **Read-only, no details** (titles shown as "Reserved", date/time and calendar names visible, other details hidden), **Add-only** (add but not modify existing; own events editable briefly in the same browser session ~30 min), **Add-only, no details**, **Modify my events** (add and modify own events; view but not modify others'), **Modify my events, no details**, **Not Shared** (no access). [A]
- Permissions are assigned per user **and per sub-calendar**: "assign one access permission level for all sub-calendars, or assign different permission levels for each individual sub-calendar." [A]
- "Sensitive event details can stay hidden from read-only users." [A]

**Access modes**
- **Account-based access**: users added by the administrator, tied to verified email; calendar dashboard listing all accessible calendars; one login across devices via mobile apps; event reminders; **change notifications** configurable per user; **daily agenda** email subscription; admin can revoke per-user access without affecting others; admin can create **groups** with a set permission level and add users to it. [A]
- **Shareable link access**: no login required; "anyone who has the link can access"; recommended with read-only / read-only-no-details permission for public or large-group sharing; links not tied to individuals (former-employee risk documented by the vendor itself). [A]
- Account-based is "the default choice and provides the most secure and convenient option"; links are for non-confidential public/group access. [A]

**Distribution and interop**
- **Outbound iCalendar feeds**: one-way, read-only sync of Teamup events into Google/Apple/Outlook or another Teamup calendar; administrators can build a custom feed from selected sub-calendars. **Inbound feeds**: other calendars subscribe-able as read-only sub-calendars; administrator-only operation; periodic refresh (refresh interval configurable). [A]
- Embedded calendars on websites, customizable via link parameters; shareable standalone event pages. [A]
- Microsoft Teams integration, Zapier, REST API, SSO (Azure AD/Entra OIDC + SCIM provisioning). [A]
- 12 calendar views (Timeline, Scheduler, Tiles, Table, year frames, etc.). [A]

### TimeTree (mobile-first consumer shared calendar) — Tier 2 (product site; help center unreachable)

- Positioning: "An app for easy calendar sharing and communication"; "All your plans, Together in one calendar." [A-T2]
- **Group-based calendar sharing**: "Easily share schedules with any group. Create a calendar, send an invite, and you're done. Family, hobbies, school; keep every group in sync with as many calendars as you need." [A-T2]
- **Multiple shared calendars with filters**: "From your own plans to family schedules and events you care about. Use filters to see everything together, or switch between calendars whenever you want." [A-T2]
- Communication around events is core positioning ("calendar sharing and communication"); Premium adds file attachments, vertical view, pinned/prioritized events, ad-free. [A-T2]
- Governance artifacts on the site: "Shared Calendar Guidelines", a separate **Public Calendar** business offering with its own acceptable-use policy and store. [A-T2]
- Operational depth (roles, permission tiers, change notifications) **not verified** — help center unreachable. Claims kept at capability level.

### Microsoft Outlook / Microsoft 365 (suite-native) — Tier 1

**Shared calendars (directly observed)**
- "Shared calendars are limited to the calendar folder within your mailbox. You can choose to share your calendar with one person or multiple people. Permissions can differ between people you're sharing your calendar with and also depends on the account you're using." [A]
- Sharing works with **work/school and personal accounts**; "in most cases, you can select the calendar you want to share and assign permissions from within Outlook"; no admin setup required. [A]
- Dedicated article tracks for **view-only sharing** and for **edit and delegation permissions**; delegate privilege "goes beyond edit privileges and is what allows someone to send or respond to mail or calendar items on your behalf." [A]
- A dedicated topic "Receive notifications from a shared calendar" exists in the sharing family (title-level evidence). [A]
- A **shared mailbox** (admin-provisioned) "provides group or individual access to the entire mailbox… including mailbox content such as folders, calendars, and contacts" — the admin-managed route to a team-owned calendar. [A]

**Group calendars (M365 Groups, directly observed)**
- "Microsoft 365 Groups is the cross-application membership service… a group is an object in Microsoft Entra ID with a list of members and a coupling to related workloads including a SharePoint team site, shared Exchange mailbox, Planner, and OneNote notebook." The group's shared mailbox carries the group calendar; visibility of the group mailbox in Outlook varies by creation surface (hidden by default for Teams-created teams, controllable via Set-UnifiedGroup). [A]

**Carried from the calendar-application pass (Tier 1 there)**
- Owner-granted permissions: "Depending on the permissions granted by the owner of a calendar, you can simply view another person's calendar, or create appointments on shared calendars"; **Delegate Access** (manage the manager's calendar on their behalf); group schedules; send/subscribe to Internet Calendars; view shared calendars side-by-side or overlaid. [carried A]

### Apple Calendar (platform-native) — carried Tier 1 (calendar-application pass)

- Share iCloud calendars with **edit or view-only** access; share CalDAV calendars/accounts with same-service coworkers; **publish read-only** to a web address others subscribe to; event non-creators can only change their own acceptance status. [carried A]

### Google Calendar — NOT REACHED

- Official docs unreachable this pass (timeout ×1, abandoned) and in both prior passes (timeouts ×2 each). **No Google-specific operational claims are made.** Retained as a market anchor only.

---

## Cross-product Comparison

| Dimension | Teamup (dedicated) | TimeTree (mobile-first) | Outlook / M365 (suite) | Apple (platform-native, carried) |
|---|---|---|---|---|
| Object of record | one Teamup calendar containing named sub-calendars | multiple named shared calendars, filterable together | a shared calendar folder (per-person sharing) or a group's calendar (group container) | a shared iCloud/CalDAV calendar |
| Who it serves | teams, operations, orgs (work-first) | families, hobbies, school groups (consumer-first) | colleagues, org units, groups | individuals + families/coworkers |
| Roles | calendar administrator + 8 permission levels per user × per sub-calendar | invite-based members; operational roles unverified | owner grants per-person permissions; view-only / edit / delegate tracks | sharer grants edit or view-only |
| Joining | admin adds users (accounts) or distributes links (no login) | "create a calendar, send an invite" | share from within the calendar app; group membership via group object | share from device; publish URL |
| Event authorship | tracked ("modify my events"; add-only tiers) | unverified | editors/delegates; non-owners edit per granted permission | non-creators limited to their own RSVP |
| Change visibility | user-configurable change notifications; daily agenda email | unverified | notifications from shared calendars (topic-level) | subscribe sync |
| Read-only consumption | read-only links, embedded calendars, outbound iCal feeds, event pages | members + presumably viewers (unverified) | view-only sharing article track | view-only share; read-only publish/subscribe |
| Cross-suite interop | inbound/outbound iCal feeds (read-only, admin-managed) | app-internal | suite-native; open shared calendars side-by-side/overlay; subscribe | CalDAV; publish/subscribe |
| Beyond events | comments, signups, custom fields, files, event pages | communication around events positioned as core; premium attachments | delegates act on behalf; shared mailbox bundles mail+calendar | RSVP/invitations machinery |

### What repeats across the sample (layer B)

1. **One shared schedule of record** for the group — not separate private calendars stitched together by invitations; every consumer reads the same store. [B — all four evidence-bearing products]
2. **A defined member audience with controlled access**: sharing is directed at specific people (or a group object), and visibility/edit participation is tiered. [B]
3. **An administering role** — whoever creates/owns the calendar governs who sees and changes what (Teamup administrator; Outlook owner; Apple sharer; group owners). [B]
4. **Permission tiers spanning at least view-only vs edit** (Teamup 8 levels; Outlook view/edit/delegate; Apple edit/view-only). [B, strong]
5. **Multiple named calendars inside one shared space** (Teamup sub-calendars; TimeTree "as many calendars as you need"; Outlook/Apple multiple calendars — carried). [B, moderate]
6. **Read-only subscription/distribution** of the shared calendar to other apps/surfaces (iCal feeds, publish/subscribe, embedding). [B]
7. **Change-visibility machinery** (notifications, agenda emails) — present where documented (Teamup full; Outlook topic-level). [B, moderate]
8. **Richer coordination content on events** — comments, attachments, signups (Teamup; TimeTree attachments). [B, moderate]

### What differs (philosophy, not Type)

- **Access model**: Teamup makes link-based (no-account) access a first-class mode; suites assume accounts and directory membership; TimeTree assumes app accounts and invites.
- **Container philosophy**: dedicated products sell the shared calendar itself as the product; suites realize sharing through calendar-folder permissions or group objects; platform-native through OS accounts.
- **Audience**: work/operations first (Teamup), consumer groups first (TimeTree), organizational first (suite).
- **Surrounding machinery**: views/embedding/custom fields (Teamup); communication-around-events (TimeTree); delegation and mailbox bundling (Outlook).

---

## Canonical Model

### L0 — Defining Invariant (minimal)

```text
Defined group of people (bounded, identifiable audience)
└── One shared schedule of record: persistent, time-anchored events
    of common concern to the group, on a calendar grid
    └── Controlled multi-person access (who may view / who may change)
```

Three jointly-held properties:

1. **A persistent schedule of time-anchored events of common concern to the group** — the calendar-Application core, but the events belong to the group's shared life (what the team is doing), not to one person's private planning. Remove the shared-group subject → Calendar Application (personal planning).
2. **A defined group as the audience** — a bounded, identifiable set of members (a team, department, organization, family), not the anonymous public. Remove the defined group → a published events/publicity calendar, which is a distribution surface, not a shared team calendar.
3. **Controlled multi-person access** — more than one person consumes the same schedule, and who can view and who can add/change is governed (an owner/administrator grants at least view vs edit participation). Remove the access control and multi-person consumption → an ordinary personal calendar.

Joint-bearing tests:

- 1 alone = an events feed / publicity calendar with no group around it.
- 2 without 1+3 = a member roster — nothing calendrical.
- 3 without 1 = document sharing with permissions, no schedule.
- 1+3 without 2 = a personal calendar with an assistant/delegate (Calendar Application's delegation territory) or a published read-only feed (distribution).
- 1+2 without 3 = a wall calendar anyone may alter — recognizably "a shared calendar" informally, but the managed form that software products realize always carries access control; keep 3 as jointly-held with the note that its *minimum* form (view vs change) is small.

L0 is deliberately smaller than any shipped product: no permission-level counts, no sub-calendars, no feeds, no notifications, no accounts, no links, no comments, no embedding, no recurrence/alerts machinery named. §24 check below passes.

### L1 — Common Mature Structure (standard capabilities)

- **Administrator/owner role and member management** — who is in, who is out, at what level; groups of members managed collectively (Teamup groups; Outlook owner/delegate; group membership objects). [A: Teamup, Outlook; B]
- **Permission tiers beyond view/edit** — at the deep pole: add-only, modify-own-events, read-only-without-details (Teamup); at the common pole: view vs edit vs delegate (Outlook; Apple edit/view-only). [A ×2; B]
- **Multiple named calendars within one shared space**, typically color-coded, with per-calendar permissions or visibility. [A: Teamup; A-T2: TimeTree; carried A: Outlook/Apple]
- **Read-only distribution surfaces** — subscription feeds to other calendar apps, published/embedded web views. [A: Teamup; carried A: Apple/Outlook]
- **Change notifications and digests** — alerting members when the shared schedule changes; daily agenda emails. [A: Teamup; A-topic: Outlook]
- **Rich event content for coordination** — attachments, comments, signups, custom fields, event pages. [A: Teamup; A-T2: TimeTree]
- **Recurrence, reminders/alerts, day/week/month views** — inherited calendar-standard capabilities. [carried A]
- **Mobile and web access to the same shared record.** [B]

### L2 — Variant / Optional Structure

- **Link-based (no-account) access** as a first-class sharing mode, with its security trade-offs (Teamup; also published/embedded calendars generally). [A: Teamup]
- **Organization-directory integration** — SSO/SCIM provisioning of calendar users; group membership objects doubling as calendar access. [A: Teamup SSO; A: M365 Groups]
- **Suite bundling** — the shared group calendar arriving as part of a group/membership container with mailbox/site/notebook (M365 Groups), or as a shared mailbox's calendar. [A]
- **Cross-suite sync bridges** — inbound/outbound iCal feeds making the shared calendar interoperate with foreign calendar services (one-way, read-only in the observed sample). [A: Teamup]
- **Event-level interaction** — comments, signups/RSVP-style participation on shared events; communication around events as a headline feature. [A: Teamup; A-T2: TimeTree]
- **Household/family positioning** — the same structure pointed at a family rather than a work team (TimeTree; Apple family sharing carried; boundary with Family Organizer documented by that pass). [B]
- **Public publishing/embedding** of the group's schedule to wider audiences. [A: Teamup]
- **Alternative visual organizations** — timeline/scheduler/table views, resource-availability layouts. [A: Teamup]

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Teamup: the specific 8+1 permission-level ladder and names; per-sub-calendar × per-user permission matrix; add-only's ~30-minute same-session edit window; "Reserved" title masking in no-details modes; calendar dashboard; daily agenda subscription; link-parameter customization; 12 named views; SSO/SCIM details; API; pricing-tier user counts; administrator-link concept.
- Microsoft: shared-mailbox vs shared-calendar vs shared-folder taxonomy; send-on-behalf vs send-as; HiddenFromExchangeClientsEnabled group-mailbox visibility toggle; group-membership propagation delays (≈2h chat / up to 24h Teams) — operational, not calendar-structural; delegate quick-start guides.
- TimeTree: premium pricing figures; Public Calendar business offering and store; shared-calendar guidelines document.
- Apple (carried): iCloud publishing model specifics; floating time zones.

---

## Vendor-specific Findings

- **Link-based access without accounts** is Teamup's signature mode. Suites distribute via accounts/directory membership and publish via URLs; the *concept* (credentialed access vs credentialed-less link access) generalizes, the mechanism is product-specific. Kept as a variant example.
- **Event-ownership tracking** ("modify my events") is documented explicitly only in Teamup; other products constrain non-owners via granted permissions instead. Concept (authorship-aware edit rights) common; mechanism product-specific.
- **The 9-level permission ladder** is Teamup's realization; the generalizable finding is the *spectrum* (view-only … full edit … administration), not the count.
- **Group-calendar-as-byproduct-of-group-object** is the Microsoft-suite realization; TimeTree/Teamup make calendars primary and groups derivative. Container direction is a variant axis.

---

## Rejected Findings (anti-overfit)

1. **"Nine permission levels" / granular tiers as definitional** — rejected. The invariant is controlled access (view vs change); the deep ladder is one product's engineering. A two-tier edit/view-only share (Apple, Outlook) is unmistakably the same Type.
2. **"Link-based no-account sharing" as definitional** — rejected. It is one access realization; suites and platform-native products share through accounts and directory groups.
3. **"Sub-calendars inside one shared calendar" as definitional** — rejected as structure detail. Multiple named calendars are common (and appear in the parent Type too), but a single-calendar shared space (TimeTree per-group calendar) fits equally.
4. **"Work/organizational use only"** — rejected. TimeTree (family/hobbies/school) and family calendar sharing sit squarely in the same structure; "team" in the leaf name is the organizational pole of an audience spectrum.
5. **"Notifications/agendas/digests" as definitional** — rejected. Change-visibility machinery is common where documented but a bare shared calendar functions without it.
6. **"Cloud/web product"** — rejected. Platform-native sharing (Apple) and suite sharing realize the same structure; the historical check includes paper artifacts.
7. **"A standalone product category exists, therefore independent Type"** — rejected as inference. Dedicated products exist (unlike the resource-calendar case), but their defining structure is the Calendar Application's, with the sharing machinery aimed at a group; no new core object beyond the calendar's appears. The leaf is best held as a variant leaf of the calendar family (consistent with both sibling passes), with the dedicated-product nuance recorded for the taxonomy pass.

---

## Boundary Findings

1. **vs Calendar Application (§03.08 parent)** — the same calendar core (time-anchored events, persistent grid, user-managed) with the audience shifted from the private self to a defined group, which pulls sharing/permission machinery from L1-adjacent nice-to-have into the load-bearing core. **Triad framing CONFIRMED from this side**: Calendar Application = the structure itself; Shared Team Calendar = the sharing/permission machinery pointed at an organization's people; Resource Calendar = the calendar owned by a bookable thing, consumed as free/busy. Remove-tests: strip the group audience + access control → Calendar Application; the calendar-application document already lists this Type as its "audience variant".
2. **vs Resource Calendar (§03.08 sibling, processed)** — people vs thing. A shared team calendar holds the group's events of common concern; a resource calendar holds claims on a resource and is consumed as an availability record. Overlap zone: Teamup calendars used for room/equipment booking (its own user stories) show the shared-calendar machinery being *applied* to resource scheduling — the audience is still the group; the resource-calendar's subject (the room) is absent unless the calendar is owned by the thing. Sibling determination (variant of Calendar Application) confirmed; the two siblings are parallel variants, not a nesting.
3. **vs Meeting Scheduling Application (§03.09)** — negotiating a time across people (availability collection, polls, booking links) vs maintaining the group's persistent schedule record. Scheduling machinery may fill the shared calendar; the record, not the negotiation, is the center of gravity here.
4. **vs Team Messaging Application** — teams often live in a messaging product with an embedded/shared calendar surface. The messaging Type's center is conversation (channels, threads); the calendar is a surface over the schedule. When the group's schedule of record becomes the primary object with member-managed events, the product is in this leaf; when conversation is the object, it is messaging.
5. **vs Family Organizer (processed)** — a family-shared calendar alone is the single-layer neighbor of that Type; the family organizer adds the household circle and the items layer (lists, meals, chores). A household variant of the shared calendar is inside this leaf's audience spectrum; the full organizer product is a different Type. Consistent with that pass's Related-Types row.
6. **vs Employee Scheduling Platform (§09, processed)** — shifts as labor records under wage/qualification/coverage rules vs events of common concern under calendar semantics. Shift publishing may produce a team-calendar surface; the labor-record machinery is the other Type's core.
7. **vs Project Management / Work Management (§03.07)** — task-derived timelines and roadmaps vs the event record on a calendar grid. Deadline events may land on the shared calendar; task objects do not.
8. **vs Event Management Platform (§26)** — the group's internal schedule vs the production of events (registration, attendees, agenda, ticketing). Public publishing of a team calendar is distribution, not event production.
9. **vs Appointment Scheduling Application (§03.09)** — customer-facing booking of provider time vs internal group schedule.
10. **Determination for the taxonomy record** — the leaf is an **audience variant of the Calendar Application Type**, confirming the triad framing proposed by the calendar-application pass and recommended by the resource-calendar pass. One nuance for the taxonomy pass, in fairness: unlike the resource-calendar case, a genuine standalone product category exists here (Teamup, TimeTree) — "shared calendar" is sold as a product, which gives the variant more market visibility than its sibling. The structure analysis nonetheless keeps it inside the calendar family: no core object exists in these products that the Calendar Application's model lacks; what differs is which machinery is load-bearing. No directory change made from this side.

---

## Historical / Market-Sample Check

- **Paper-era practice**: the team wall calendar or whiteboard planner in an office/kitchen — a schedule of events of common concern (holidays, launches, training days, leave), visible to the group, maintained by whoever holds the pen under an understood "who may write here" rule. Satisfies all three L0 legs with zero software machinery. [C]
- **2000s suite lineage**: Exchange group schedules, SharePoint team calendars, shared folder calendars — permission-governed shared schedules inside mail-centric suites; the modern Outlook article is the direct descendant. [carried A]
- **Platform-native lineage**: Apple iCloud family/work sharing and publish/subscribe — same structure without enterprise machinery. [carried A]
- **Regional/consumer lineage**: mobile-first group calendars in consumer markets (TimeTree's origin market included family/school use) — same structure, no enterprise wrapper. [A-T2]
- The definition names no accounts, links, cloud, feeds, notifications, sub-calendars, permission counts, or views — all era/market machinery. Historical check **passed**.

---

## Uncertainties

1. **TimeTree's operational depth** — help center unreachable (timeout + transport error ×2). Member roles, permission tiers, notification behavior unverified; held at product-page (capability) strength. If a later pass fetches TimeTree's help pages, the L1/L2 lists should be re-verified.
2. **Google Calendar sharing mechanics** — unreachable in three passes (this pass ×1 timeout; prior passes ×2 each). Held as market anchor only; no Google-specific claims anywhere. Google's real-world dominance means the sample under-represents the largest suite; the multi-product B-layer claims rest on the three reachable products plus carried evidence.
3. **Event-ownership tracking outside Teamup** — "modify my events"-style rights documented only in Teamup; other products may offer equivalents under different names (unverified). Kept as a deep-pole capability, not generalized.
4. **Standalone-category boundary** — no systematic market scan was done to enumerate all dedicated shared-calendar products; the claim "a standalone product category exists" rests on two well-documented products (Teamup, TimeTree) plus the general market, and is framed for the taxonomy pass rather than asserted exhaustively.
5. **Bidirectional cross-suite sync** — observed feeds were one-way read-only (Teamup, Apple publish/subscribe, Outlook subscribe); whether mature products commonly offer two-way write-through sync of shared calendars across foreign suites was not verified this pass and is not claimed.

---

## Final Synthesis

A Shared Team Calendar is **the group's schedule of record**: a persistent calendar of time-anchored events of common concern to a defined group of people, consumed by its members and — within permission tiers granted by an administrator/owner — maintained by them. The defining core is three jointly-held structures (group audience + one shared schedule + controlled multi-person access). Everything else mature products carry — role ladders, sub-calendars, feeds and embedding, notifications and digests, comments/signups/attachments, link-based access, SSO, suite/group bundling, family positioning, alternative views — is standard capability or variant structure, not definition.

**Determination for the taxonomy record:** the leaf is an **audience variant of the Calendar Application Type** — the calendar's sharing/permission machinery pointed at an organization's people — confirming the triad framing (calendar → shared team → resource) proposed by the calendar-application pass and endorsed by the resource-calendar pass. A genuine standalone product category exists (Teamup, TimeTree), unlike the resource-calendar case; this is recorded as a taxonomy nuance, not a reclassification. The document is written in full as the variant's own record, cross-referencing both siblings and the parent Type. No directory change made from this side.
