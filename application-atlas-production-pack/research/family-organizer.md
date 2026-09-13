# Research Notes — Family Organizer

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a **Family Organizer** application actually is by studying real products: what the shared container is, what time and "stuff" structures it manages, how household members relate to them, which loops connect the structures, and where the boundary lies against neighboring Types (Family Location/Safety, Family Care Coordination, Household Chore Application, shared/team calendars, task apps, family messaging, Home Management).

## Initial Boundary

Directory location: §29 Home, Family, Personal & Local Services. Siblings: Home Management Application, Household Chore Application, Family Location / Safety Application, Family Care Coordination, Parenting / Baby Tracking Application, plus work-side calendar/task Types in §03.

Initial hypothesis: a shared, whole-household application for coordinating everyday family life — shared calendar, shared lists, chores, sometimes meals, messaging, photos. Nearest confusions:
- a shared calendar alone (TimeTree-style) — one surface, not an organizer
- a chore-only app (Household Chore Application leaf)
- a family locator (center of gravity = people's location)
- a care-coordination circle (center of gravity = one care recipient)
- a generic task/list app with a family workspace (container is a generic workspace, not household semantics)

## Research Questions

1. What is the household container — account, circle, device profile set? Who joins, how, with what roles?
2. Is the shared family calendar definitional or merely common? What are its member/event semantics?
3. What "stuff" structures exist (shopping lists, to-dos, chores/tasks) and how does member assignment work?
4. How do the structures interconnect (recipes → lists, meals → calendar, chores → rewards)?
5. What surfaces do users face (mobile, web, hardware display, print, widgets)?
6. What notification/reminder model keeps the household in sync?
7. What access/permission models exist (full-access vs roles vs child accounts)?
8. Where are the exact boundaries vs the six neighboring Types listed above?

## Representative Products

Selection logic: market representativeness + documentation completeness + different product philosophies + different customer levels/poles.

| Product | Philosophy / pole | Status |
|---|---|---|
| Cozi | classic software family organizer; calendar+lists first; free-with-ads + subscription; long market history | Researched (official FAQ + feature pages) |
| FamilyWall | full-featured "family organizer + private family network"; freemium + Premium; roles and multi-circle | Researched (official site + official knowledge base) |
| Skylight Calendar | ambient hardware pole: wall touchscreen family hub + companion app; chores/rewards emphasis; hardware + subscription | Researched (official product page + official help center) |
| OurHome | chore/reward-centric free app | WebFetch failed twice → abandoned per network rule; excluded |
| Picniic | freemium all-in-one | WebFetch failed once → abandoned; excluded |
| Maple | modern "household OS" generation | Site reachable but product is sunsetting (acquired, data deletion Dec 31 2026); excluded as non-current representative; sunset page used only to note generational vocabulary ("mental load", "everyone can share in it") |

## Sources

All fetched 2026-09-07 (Tier 1 official operational documentation unless noted):

- Cozi — https://www.cozi.com/ (root), https://www.cozi.com/feature-overview/ (Tier 2), https://www.cozi.com/faq/ (Tier 1 FAQ)
- FamilyWall — https://www.familywall.com/ (root, Tier 2), https://support.familywall.com/ (official Freshdesk KB), About FamilyWall article (47001013681), How can I create a family? (47001013687), Invite a member without email / Child account (47001239550), Getting started category (47000476352)
- Skylight — https://www.skylightframe.com/calendar/ (Tier 2 product page + FAQ), https://skylight.zendesk.com/hc/en-us (official help center), Calendar category (36091345815963), Tasks section (35335533724315) incl. "What Are Tasks?" (35335515611803), Profiles section (31521940984603)
- Maple — https://growmaple.com/ (sunset notice only)

Evidence layers used below: **A** = directly observed in one product's official docs; **B** = observed across multiple products; **C** = canonical inference from cross-product comparison and boundary reasoning.

## Product A — Cozi

### Key observations (evidence layer A unless noted)

- **Positioning**: "the #1 family organizer app"; "must-have family calendar organizer for families"; helps "coordinate and communicate schedules and activities, track grocery lists, manage to-do lists, plan ahead for dinner, and keep the whole family on the same page."
- **Container = one fully shared family account**: up to 12 people; each member signs in with their own email + **one shared password**; every included member has **full access** to view/add/edit/delete **all** account data; the FAQ explicitly states no restricted-access option exists.
- **Shared family calendar**: color-coded per family member; events show name + color dot; multi-person events show multiple dots; an "All" designation exists; recurring events; day/week/month/agenda views; reminders per attendee (free: 1 per attendee; Gold: up to 3 — plan detail, L3); daily/weekly agenda emails; change notifications when events are created/edited (Gold).
- **Only attendees receive reminders** — a structural rule tying notifications to event membership.
- **Lists**: Shopping lists (automatically shared with the whole account; auto-sync; print; email/text a list; sections/categories; Shopping Mode in Gold) and To-do lists (as many as wanted; sections; premade list library: packing, school supplies, routines).
- **Chores**: a Chores feature in mobile apps auto-creates one chore list per family member; supports daily and weekly recurrence; members can pin their own list.
- **Meals**: Recipe Box (add by URL or manual); ingredients → shopping list in one tap; meal planner (planning breakfast/lunch/dinner/snacks) writes meals onto the family calendar "so the whole family knows what's for dinner"; planner highlights busy days.
- **Sync**: read-only iCal feed integration with Google/Outlook/Apple Calendar; incoming refresh ~hourly (precision kept in notes); outbound feed immediate.
- **Notifications**: device notifications and/or email; per-person delivery configuration; a member must have a valid delivery method to be a reminder recipient.
- **Model/pricing**: free version ad-supported; Gold subscription (price and features recorded in L3 notes); one subscription covers the whole account.
- **No chat, no photos, no location, no budget** in Cozi's feature set (absence observed across root + feature overview + FAQ).

## Product B — FamilyWall

### Key observations (evidence layer A)

- **Positioning**: "Happy Family Organization… helping families with their daily organization and communication"; "YOUR FAMILY ORGANIZER… the whole family is on the same page"; marketed as family dashboard + private network.
- **Container = the "Family" / "Circle"**: created by signing up (creator becomes Founder); members join via invitation; **child accounts** can be created **without email** (name + credentials handed to the child); **roles exist**: Founder and administrators vs simple members — administrators can change/delete other members' content; members without email are simple members by default and "can only change or delete the content they publish"; rights are managed in the "My Family" settings; **additional circles** can be created (extended family, friends, neighbors — "Multi Groups").
- **Shared family calendar**: color-coded; view an individual's schedule or the whole family; add/edit appointments everyone sees; reminders; calendar import (Outlook/Google) is Premium; subscribe to public/shared calendar by URL (Premium); add events by forwarding an email (KB article exists).
- **Shopping lists**: shared with the whole family; offline browsing at the store; items added by others visible.
- **To-do lists**: **private or shared**; **assign to-dos to selected family members**; track progress; chore checklists for kids; as many lists as wanted (packing, camp list, emergency supplies).
- **Family messaging**: post a message to family members; thread view; notifications; audio/video messaging Premium.
- **Family gallery**: share photos/videos privately (L2 social layer).
- **Important contacts / Family Directory**: any member can add contacts (babysitter, grandparents).
- **Family locator** (Premium): map of kids; each member controls with whom they share location; "Family Places" (home/work/school) with arrival/departure notifications — the L2 drift layer toward Family Location/Safety.
- **Premium extras**: budget/finance tracker, meal planner (week's meals; recipes → grocery list), timetables, 25 GB storage (L3 detail).
- **Platforms**: iOS/iPad/Android/Web; free core with Premium subscription.

## Product C — Skylight Calendar

### Key observations (evidence layer A unless noted)

- **Positioning/form factor**: a **wall/counter touchscreen hardware display** ("all-in-one family hub… 1 million+ families") + companion mobile/desktop app; explicitly a **shared household hub** under one roof; "multiple households can also share the same information across two or more devices with Device Linking" (all-or-nothing data sharing between devices — L3).
- **Household container = profiles on the device**: "people profiles" per family member with colors; multiple external calendars (Google/Apple/Outlook/Yahoo/Cozi/Readdle/public links) can be **linked to one profile**; hashtag (#) profiles exist (shared groupings, e.g. #family — semantic inferred from name; detail L3); Parental Lock secures settings.
- **Shared calendar is the center of the device**: auto-synced schedules; color-coded profiles; day/week/month views; weather at event time/location; countdowns to birthdays/vacations/holidays.
- **Tasks = Chores + Routines** (official distinction): **Routines** are task sets occurring around the same time of day, repeating daily (e.g., "Brush Teeth"); **Chores** are tasks at chosen times, repeatable or one-off ("Clean the garage"); per-profile assignment ("Profiles Are Missing When Creating Tasks" implies tasks require profiles); Chore Chart view; **star/reward system** (Calendar Plus) — "Add stars to Chores to motivate kids… earning rewards."
- **Custom lists**: create/edit/color-code checklists (grocery list created by default) on device or app; transfer lists to other apps (AnyList).
- **Meal planning** (Plus): plan a week's meals; save favorites; meal plan displayed on the calendar.
- **Import**: "Sidekick" turns emails, paper schedules, PDFs into calendar events (Plus).
- **Photo screensaver** (Plus) — ambient photo layer.
- **Deliberate absence of communication layer**: no social media or internet access on device; no family chat (absence observed — the display is a passive/shared household surface; the companion app is for management).
- **Model/pricing**: hardware purchase + free core features (tasks, lists, profiles, parental lock) + Plus subscription (meal planning, rewards, import, screensaver, animations).
- Marketing vocabulary across testimonials/FAQ: "mental load", "second brain", "get on the same page", "kids have never been so motivated by a chore chart" (B-level signal of category framing, not operational evidence).

## Excluded / Unreachable products

- **OurHome** (ourhomeapp.com): transport errors twice → abandoned per network rule. Intended as the gamified-chore pole. The chore/reward pole is instead covered by Skylight (chores/routines/stars/rewards) and Cozi (per-member chore lists with recurrence).
- **Picniic**: transport error → abandoned.
- **Maple**: reachable but sunsetting (acquired; accounts/data close Dec 31, 2026). Not used as operational evidence; its farewell page confirms the generational framing ("mental load at home… family life works better when everyone can share in it") consistent with Skylight's vocabulary.

## Cross-product Comparison

| Structure | Cozi | FamilyWall | Skylight Calendar |
|---|---|---|---|
| Household container | one shared account, up to 12, full access for all; shared password | Family/Circle with Founder + admin + simple member roles; child accounts without email; additional circles | device profile set (people profiles); device linking spans households; parental lock |
| Shared family calendar | central; color-coded per member; multi-person + "All" events; recurring; reminders per attendee; agenda emails | central; color-coded; individual or whole-family view; reminders; import/URL subscribe (Premium) | central; auto-synced external calendars; profiles with colors; day/week/month; event-time weather |
| Shared lists | shopping (auto-shared) + to-do (many, sections, library) | shopping + to-do (private or shared, assignable, progress) | custom lists (grocery default), color-coded, device+app |
| Chores / tasks | per-member chore lists; daily/weekly recurrence | chore checklists for kids; assignment; progress tracking | Tasks = Chores + Routines; per-profile; chore chart; stars/rewards (Plus) |
| Meal planning | recipe box; ingredients→list; meals→calendar; busy-day hints | meal planner (Premium); recipes→grocery | meal planning (Plus); meals on calendar |
| Family messaging | none (notifications/agenda emails only) | messenger with threads (+audio/video Premium) | none (no internet/chat on device) |
| Photos / gallery | none | private family gallery | photo screensaver (Plus) |
| Location | none | family locator + places (Premium) | none |
| Budget | none | budget tracker (Premium) | none |
| External calendar sync | read-only iCal both directions | import + URL subscribe (Premium) | primary ingestion mechanism (multi-provider) |
| Notifications | device + email; per-attendee; change notices (Gold) | reminders; message notifications; place arrivals | reminders & alerts |
| Surfaces | web + iOS + Android; print; email/text a list | iOS/Android/Web | hardware display + companion app + web cloud |
| Business model | free w/ads + subscription | freemium + Premium | hardware + free core + subscription |

### Stability reading

- Present in **all three**: household container of named members; shared color-coded family calendar with per-member visibility; shared lists; chores/tasks with member assignment and recurrence; meal planning; reminders/notifications; multi-device access. → strong B-level commonality.
- Present in **some**: messaging (FamilyWall only), photos (FamilyWall, Skylight-Plus), location (FamilyWall only), budget (FamilyWall only), rewards/gamification (Skylight), print/paper handoff (Cozi). → L2.
- Absent in some mature products entirely (chat, location, photos): must NOT be definitional.

## L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a Family Organizer:

1. **The household circle as the shared container** — a persistent, private space whose members are the known people of one family/household, joined by invitation or household setup, all operating on the same shared picture. Remove → personal organizer or a generic shared workspace.
2. **The shared household calendar** — the household's schedule of record: events belonging to identified members, visible across the circle, color-coded by member. Remove → a shared-list/chore app (Household Chore Application), not an organizer.
3. **The shared household items layer** — shared lists and/or household tasks/chores carrying the household's outstanding work and wants, visible to the circle and assignable to members. Remove → a bare shared calendar, not an organizer.

The three coexist **in one place as one household-wide picture** — that conjunction is what "organizer" means; each structure alone is a different, narrower Type.

Checked against implementation variants: the container may be a full-shared account (full access, no roles), a role-based circle, or a device profile set — the invariant is the named-member household sharing one picture, not any specific account/role machinery.

## L1 — Common Mature Structure

Very common across the researched sample; expected in current products; not definitional:

- member profiles with color coding (identity inside the circle)
- reminders and household-wide notifications (event reminders, daily/weekly agenda digests, change notifications)
- meal planning / recipes, with the ingredient→shopping-list and meal→calendar flows
- chore/task recurrence (repeats, routines)
- external-calendar sync/import (households already keep calendars elsewhere)
- real-time cross-device sync of lists and events
- child/kid representation in the container (child accounts, per-kid chore lists, kid-facing profiles)
- web + mobile multi-platform access; printing/paper handoff surfaces

## L2 — Variant / Optional Structure

Depends on product philosophy, segment, era:

- family messaging/chat layer (present in the "private family network" pole; absent in calendar-first and hardware poles)
- photo/video sharing layer (gallery or ambient screensaver)
- location/safety layer (locator, places, arrival alerts) — drift boundary to Family Location / Safety Application
- care layer (medication lists, care needs) — drift boundary to Family Care Coordination
- budget/finance module
- rewards/gamification for children (stars, points)
- multi-circle / extended-family groups beyond the co-resident household
- access-control philosophy: fully-shared account vs admin/member roles vs parental locks
- business model: ads+subscription vs freemium+premium vs hardware+subscription
- form factor: app/web vs ambient household hardware display

## L3 — Vendor-specific (research notes only)

- Cozi: 12-member account cap; one shared password for the account; explicit no-restricted-access design; Gold $39/yr; up to 3 reminders/attendee in Gold vs 1 in free; free-tier event entry limited to next 30 days in Agenda view; Shopping Mode; premade list library; hourly incoming iCal refresh; 2-week account-deletion grace.
- FamilyWall: Premium gating specifics (import, locator, budget, meal planner, timetables, 25 GB, audio/video messaging); child-account credential flow (credentials emailed to creator); event creation by forwarding email; Freshdesk KB structure; "circle" terminology.
- Skylight: device sizes (10"/15"/27"); Calendar Max wall-only; device linking all-or-nothing; Sidekick (email/PDF → events); Disney Mode; AnyList list transfer; #hashtag profiles; event-time weather; parental-lock reset flow; WiFi-required hardware.

## Historical / Market-Sample Check

Pre-digital and platform-native anchors tested against the L0:

- **Kitchen wall calendar + fridge shopping list + wall chore chart + family bulletin board**: household circle ✓ (the family), shared calendar ✓, shared lists/chores ✓, one shared picture ✓ — satisfies L0 with zero software. Notifications, apps, photos, messaging, rewards are correctly NOT definitional.
- **Platform-native shared calendar (e.g., a shared calendar inside a device ecosystem)**: has the calendar layer but not the household items layer or household semantics → correctly NOT a Family Organizer; confirms that the conjunction (not the calendar alone) is the invariant.
- **Paper-era family command centers and 2000s family websites** (shared calendar page + lists): satisfy the core without any modern machinery.
- Conclusion: L0 does not over-fit the current app-era implementation; the historical check passes.

## Boundary Findings

1. **vs Family Location / Safety Application** — same household, different center of gravity: organizer centers the household's schedule/stuff; safety Type centers the map of people and the response purpose. Discriminator: "could the application function with zero location sharing?" Yes → organizer. FamilyWall carries a locator as a Premium L2 layer — bundling exists; center of gravity decides. (Consistent with the recorded family-location-safety-application boundary row.)
2. **vs Family Care Coordination** — organizer centers the *household* (everyone's calendar, chores, shopping); care coordination centers *one person who needs care* with a helper circle deliberately crossing household boundaries and an express-and-claim needs loop. Removing the care-recipient-centered container leaves a family organizer. (Consistent with the recorded family-care-coordination boundary row.)
3. **vs Household Chore Application (§29 sibling)** — chore-only products (chore charts, cleaning schedules, gamified chores without a household calendar hub) belong to the chore leaf; the chore chart inside a full household hub is a standard capability of this Type. Discriminator: presence of the shared household calendar as a co-equal defining layer.
4. **vs Calendar Application / Shared Team Calendar (§03.08)** — generic calendars lack the household circle semantics and the items layer; §03.08 Types are work-context. A shared family calendar alone is one layer of this Type, not the whole.
5. **vs To-do List / Task Management (§03.06)** — generic task apps have workspace/project containers and work-task semantics; here tasks are household chores/wants inside a family circle. A family workspace inside a generic task tool is a usage pattern, not this Type's product category.
6. **vs Group / Family messaging (§01.01)** — chat-first products define communication as the object; in organizers, messaging (when present) is an auxiliary L2 layer (absent entirely in two of three sampled products).
7. **vs Home Management Application (§29 sibling)** — home management centers the *premises* (inventory, maintenance, bills of the home); the organizer centers the *people* of the household. Bundling exists in the market; center of gravity decides.
8. **vs Parenting / Baby Tracking** — child-log-first (feedings, sleep) with parents as sole operators; no whole-household schedule/items hub.

## Uncertainties

- The chore-reward pole (OurHome-style) could not be studied from official docs (fetch failures); the pole is covered indirectly via Skylight's chores/stars/rewards and Cozi's per-member chore lists. If a later pass studies chore-gamified organizers, expect no change to L0 (the container+calendar+items conjunction holds), but reward mechanics could be promoted from L2-with-strong-evidence to firmly-common L1.
- Older regional family-portal products (2000s web "family site" genre) were reasoned about structurally (calendar + lists pages) but not fetched; the historical check for them rests on category knowledge, marked as C-level inference.
- Exact membership caps, plan gates, and hardware behaviors are product-specific (kept in L3 notes); market-wide norms for caps were not researched.
- Skylight "#hashtag profiles" semantics were inferred from the article title, not read in full — treat as unverified detail (excluded from the final document).

## Final Synthesis

A Family Organizer is the household's shared coordination hub: a private, invitation-gated space for the known members of one family, presenting **one shared picture of household life** built on two co-equal layers — the household's shared calendar (who is where, when) and the household's shared items (shopping, to-dos, chores, meals) — with member assignment, recurrence, and notifications keeping the circle in sync. Communication, photos, location, budget, rewards, and AI are optional enrichments; the conjunction of household circle + calendar + items, visible family-wide, is the defining core. The Type sits deliberately between four drift boundaries: care coordination (care-recipient-centered), family location/safety (people-map-centered), chore apps (chore-only), and shared calendars (calendar-only).
