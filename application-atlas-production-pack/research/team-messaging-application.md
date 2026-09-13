# Research Notes — Team Messaging Application

## Research Goal

Understand the Application Type "Team Messaging Application" (DIRECTORY 01.01 Messaging & Chat) from real products: what the organizational container is, how conversation spaces inside it are structured, how membership and access are governed, how conversation is kept as shared memory, and where the Type's boundaries lie.

This leaf carries prior joint-review flags from processed siblings that this pass must discharge from the team-messaging side:

- `chat-room-application` (2026-09-06): "team messaging = org-roster membership and org identity behind room-shaped channels" — held one-sided, joint review pending.
- `group-messaging-application` (2026-09-07): team-messaging side of the place/roster seam open; also noted "org-provided group containers" as a drift surface relevant here.
- `community-chat-platform` (2026-09-07): boundary vs Team Messaging (org roster vs self-service join) — joint review recommended once Team Messaging processed.
- `instant-messaging-application` (2026-09-05): recorded the seam (organizational identity + persistent channels vs personal identity + personal threads) for this pass to confirm.

Additional prior constraints from related passes: `collaborative-workspace` (conversations vs persistent content), `business-messaging-application` (internal audience vs external customers), `clinical-communication-platform` (joinable workspace channel vs directory/assignment-based container), `employee-communication-platform` / `internal-communication-application` (peer-to-peer conversation vs org→workforce broadcast).

A prior-generation example pair (`examples/research-notes/team-messaging.md`, `examples/application-docs/team-messaging.md`, 2026-09-05, Slack + Microsoft Teams) exists as prior art. This pass re-researched independently with a wider, philosophy-diverse sample and the v1.1 evidence rules; conclusions refine, not copy, the example.

## Initial Boundary

Target:

> Team Messaging Application

Working hypothesis (to verify, not to assume):

> Conversation in this Type lives in persistent spaces (channels) inside a governed organizational container (workspace/team/organization), with membership tied to the organization rather than to a personal contact graph, and with history retained as shared organizational memory.

Nearest confusing Types:

- Instant Messaging Application (personal identity, person-addressed threads)
- Group Messaging Application (member-defined private group, personal reachability)
- Chat Room Application (addressable place, self-service/stranger join, no org container)
- Community Chat Platform (community container, interest-based self-service join, strangers expected)
- Collaborative Workspace / Team Workspace Platform (persistent authored content, not conversations)
- Video Conferencing / Conference Calling (live synchronous meeting primary)
- Business Messaging / Customer Support Chat (external audience)
- Employee Communication Platform / Internal Communication Application (org→workforce broadcast, not peer conversation)

## Research Questions

1. What is the top-level container, and how many levels does it have (workspace vs team vs organization)?
2. What is a channel: how is it created, named, governed, and how does it relate to the container?
3. Where does membership come from (org roster, invitation, provisioning) and what non-member roles exist (guests, external participants)?
4. What conversation objects exist: messages, threads/topics, direct/group messages — and which are defining vs common?
5. What visibility/access semantics do channels have (public/private/shared/web-public; discover-join vs invite-only; history visibility on join)?
6. What lifecycle does a channel have (create → active → archive)? What happens to history?
7. What notification/read-state machinery is structural?
8. What governance surfaces exist (roles, policies, retention, admin)?
9. Which bundled capabilities (calls, files, docs, tasks, AI, integrations) are Common vs Optional vs vendor-specific — what must NOT enter the definition?
10. Boundary tests: remove the org container → ?; remove purpose-organized persistent spaces → ?; remove shared persistent history → ?; make join open to strangers → ?
11. Historical check: would older/team-server-era products (Campfire-generation room chats, IRC team servers) still fit the definition?
12. Discharge the four sibling flags with direct evidence.

## Representative Products

| Product | Why selected | Philosophy / tier |
|---|---|---|
| Slack | archetypal channel-first team messaging; market anchor | flat workspace of channels; SaaS, freemium → enterprise |
| Microsoft Teams | largest suite-embedded enterprise deployment | two-level team → channel hierarchy inside a productivity suite |
| Mattermost | open-source / self-hosted / sovereign pole (defense, critical infrastructure) | workspace → teams → channels; ChatOps orientation |
| Zulip | topic-first conversation model; open source; cloud + self-host | challenges the "channels + per-message threads" shape |

The sample spans: channel-first vs topic-first conversation models; flat vs two-level container hierarchies; SaaS vs self-hosted deployment; freemium vs enterprise/mission-critical customer tiers.

## Sources

Research date: 2026-09-09. All Tier-1 (official product documentation / help center).

### Slack (help center)

- What is a channel? — https://slack.com/help/articles/360017938993-What-is-a-channel
- Join a channel — https://slack.com/help/articles/205239967-Join-a-channel
- Getting started for workspace creators — https://slack.com/help/articles/217626298-Getting-started-for-workspace-creators

### Microsoft Teams (Microsoft Learn, admin documentation)

- Overview of teams and channels in Microsoft Teams — https://learn.microsoft.com/en-us/microsoftteams/teams-channels-overview

### Zulip (help center)

- Introduction to channels — https://zulip.com/help/introduction-to-channels
- Channel permissions — https://zulip.com/help/channel-permissions
- Introduction to topics — https://zulip.com/help/introduction-to-topics

### Mattermost (documentation)

- Mattermost Documentation index (Channels module overview) — https://docs.mattermost.com/
- Channel types — https://docs.mattermost.com/end-user-guide/collaborate/channel-types.html

Access notes:

- Two initial Mattermost doc URLs 404'd / returned empty (docs restructure); resolved via the docs index. Mattermost evidence is drawn from the index page and the Channel types page.
- A targeted Teams end-user chat-article URL 404'd; Teams direct-chat surface is supported only indirectly for this pass (see Uncertainties). No Teams-specific chat claims are made beyond structural commonality with the other three products.

## Product Observations

### Slack

Evidence layer: A (directly observed, Tier 1).

Model observed:

```text
Workspace
├── Members (invited; roles: Primary Owner, admins, members, guests)
├── Channels (public / private)
│   ├── Message stream (persistent)
│   └── Threads
└── Direct messages (1:1 and group DMs)
```

Key observations:

- "In Slack, work is organized into dedicated spaces called channels. Channels bring order and clarity, and you can create them for any project or team." Channels are the primary organizing object; the workspace creator guide recommends channels for announcements, major projects, and social purposes.
- Public channels: "Members (but not guests) in your workspace can find, view, and join public channels" — self-service join inside the workspace; messages/files in public channels appear in search results for other members.
- Private channels: "People must be added to private channels by someone who's already a member" — invitation-based; search results restricted to channel members. Public↔private conversion exists.
- The `#general` channel: every workspace has one; members are automatically added and unable to leave; it "cannot be archived, deleted, or converted to private" — a product-specific default-space policy.
- Channel lifecycle: "Archive channels when they're no longer needed." Topic/description fields exist for channels.
- Workspace container: "A Slack workspace is a single place for your team, and anyone else you collaborate with, to get work done." The creator invites coworkers; roles include Primary Owner and Workspace Admins. External collaboration via Slack Connect ("work securely with people from other organizations in the same channel").
- DMs: "In Slack, conversations happen in channels and direct messages (DMs). DMs are better-suited for one-off conversations, and channels are where the majority of work will take place." — the product's own framing of channels as primary, DMs as side surface.
- Threads exist to organize discussions ("To help keep discussions organized, use threads").
- Vendor extras observed in nav/help (not part of the Type): channel templates, Slack Connect, Canvas, Lists, Huddles, Clips, Workflow Builder, Slack AI/agents, Enterprise Key Management, temporary channel joining ("Just for today / 48 hours / 1 week").

### Microsoft Teams

Evidence layer: A (directly observed, Tier 1 admin docs).

Model observed:

```text
Organization (Microsoft 365)
├── Team (private or org-public; owners / members; guests / external participants per policy)
│   ├── Channels (standard / private / shared)
│   │   ├── Conversations (posts; moderation possible)
│   │   └── Files (SharePoint-backed)
│   └── Team settings (member permissions, @mentions, moderation)
└── Chats (person/group; adjacent surface)
```

Key observations:

- "Teams are collections of people, content, and tools surrounding different projects and outcomes within an organization." Teams can be private (invited users) or public ("anyone within the organization can join (up to 10,000 members)"). Org-wide teams exist for ≤10,000-user orgs.
- "Conversations, files, and notes across team channels are only visible to members of the team." — container-level visibility default.
- "Channels are dedicated sections within a team to keep conversations organized by specific topics, projects, disciplines—whatever works for your team." Three channel types: standard (open to all team members), private (selected team members), shared ("selected people both inside and outside the team") — with a detailed feature matrix distinguishing them (e.g., guests in standard/private but not shared; external B2B participants in shared only; moderation in standard only).
- Membership: "Team owners can invite anyone at your organization to join their team. Depending on your organization's settings people from outside of your organization can be added to your teams as guests or as external participants in shared channels." Teams can be created from existing Microsoft 365 groups with membership synced — org-roster coupling.
- Roles: Team owner / Team member; channel-level moderators (start posts, control replies) — a two-layer governance (team roles + per-channel moderation).
- Governance: team settings control members' ability to create channels, @mention team/channel, etc.; Teams administrators set system-wide policy; "all users have permissions to create a team" by default but this is modifiable.
- Implementation detail observed (not canonical): channel files stored in SharePoint; creating a team or private/shared channel auto-creates a SharePoint site.

### Zulip

Evidence layer: A (directly observed, Tier 1).

Model observed:

```text
Organization
├── Users (roles; guests as a restricted role; SAML/SCIM provisioning; invite-based joining)
├── Channels (public / private / web-public; subscribe model)
│   └── Topics (first-class named sub-conversations)
│       └── Messages
└── Direct messages (1:1 and group; restrictable by org)
```

Key observations:

- "Channels organize conversations based on who needs to see them. For example, it's common to have a channel for each team in an organization. Because Zulip further organizes messages into conversations labeled with topics, there is generally no need to create dedicated channels for specific projects." — channels organize *who*, topics organize *what*.
- Subscribe model: "Subscribing to a channel makes conversations in that channel appear in your inbox, recent conversations, combined feed and left sidebar… you'll receive @-mention notifications only in channels you're subscribed to." — membership-in-space is a per-user subscription state, distinct from org membership.
- Channel permission classes (Tier 1): **private** ("joining and viewing messages requires being invited"; per-channel choice whether new subscribers see prior history — **shared vs protected history**), **public** ("open to everyone in your organization other than guests"; non-guests can see channel info, subscribe/unsubscribe themselves, and see all messages whether or not subscribed), **web-public** ("anyone on the Internet can see messages without creating an account"; posting still requires an account).
- Per-channel permissions exist in three classes: subscription permissions (who can administer/subscribe/subscribe others/unsubscribe), messaging permissions (who can send, who can start topics, whether topics are required), moderation permissions (move messages, resolve topics, delete messages). Org-level: restrict channel creation, restrict subscribing others. "Any permission, including whether a channel is private, public, or web-public, can be modified after the channel is created."
- Private-channel governance nuance: organization administrators who are not subscribed "cannot gain access to its content" — metadata vs content access separated.
- Guests: "Guest users can't see public (or private) channels, unless they have been specifically subscribed to the channel."
- Topics: "Zulip is designed around conversations that are labeled with topics"; "Lots of conversations can happen in the same channel at the same time, each in its own topic." Topics can be renamed, resolved, moved, deleted; orgs can require topics. On threads: "Topics in Zulip fill the role of threads in other chat apps… each thread is labeled with a topic."
- DMs exist ("Starting a new direct message") and are org-restrictable ("Restrict direct messages").
- Org container: create an organization, join a Zulip organization (invite), SAML/SCIM, user roles, guest users, message retention policy, archive a channel.
- Boundary-relevant: Zulip organizations have an **organization type** axis that includes open **communities** (a "Communities directory" exists), plus a "Community moderation toolkit" for "open organizations" — the same container structure serves the community pole (drift surface, see Boundary Findings).

### Mattermost

Evidence layer: A (directly observed, Tier 1).

Model observed:

```text
Workspace / system (self-hosted instance; system roles)
├── Teams (org subdivisions; team members; roles)
│   ├── Public channels (open to everyone on the team)
│   ├── Private channels (selected team members)
│   └── Archived channels (read-only)
├── Direct message channels (2 people, cross-team unless disabled)
├── Group message channels (3–7 people)
└── Bundled modules: Playbooks, Boards, Calls, Agents
```

Key observations:

- "Channels are used to organize conversations across different topics. The channels you're a member of display in the left pane."
- Five channel types: **Public** ("open to everyone on a team", globe icon; new team members automatically added to the **Town Square** channel — product-specific default space), **Private** ("for sensitive topics… only visible to selected team members"; members can leave; management restrictions configurable by plan), **Direct message** ("conversations between 2 people. Only members of the conversation can see direct messages"; cross-team DMs allowed unless system admin disables), **Group message** ("conversations between 3 to 7 people"; convertible to a private channel from v9.1), **Archived** ("deactivated… read-only to prevent new messages from being sent and preserve channel history"; access to archived channels can be admin-disabled).
- Hierarchy: channels live inside **teams** ("open to everyone on a team"; "people on other teams"); docs also cover "Teams, groups, and roles" and workspace-level invites ("Invite people to your workspace") — so container depth is instance → team → channel, with DMs/group messages cross-cutting teams.
- Messaging module framing: "Mattermost Channels enables secure, real-time and asynchronous communication… Public and private channels, direct messages, and threaded conversations for structured operational coordination." Role-based access control, audit logs, configurable notifications (alerts, keyword triggers, muting), pinning/bookmarks/search, ChatOps (slash commands, bots, webhooks).
- Deployment/positioning (the sample's pole): self-hosted sovereign platform for "defense, intelligence, security, and critical infrastructure"; air-gapped/DDIL operation; STIG/FIPS-class compliance posture. Bundled adjacent modules: Playbooks (workflow automation), Boards (Kanban), Calls (audio/screenshare in channels and DMs), Agents (AI) — suite packaging on top of the messaging core.
- Governance: read-only broadcast channels (Enterprise); channel management restricted to system/channel admins (paid plans); any member can manage private-channel membership in the free Team Edition — permission depth is a variant axis.

## Cross-product Comparison

| Finding | Slack | Teams | Zulip | Mattermost | Canonical decision |
|---|---|---|---|---|---|
| Organizational container whose membership is governed | Workspace (invite; roles; guests) | Team (owners invite org members; guests/external per policy; M365 group sync) | Organization (invite; SAML/SCIM; roles; guests) | Instance + Teams (system roles; workspace invites) | **Core** — universal in sample |
| Persistent named conversation space organized by purpose | Channel ("for any project or team") | Channel ("dedicated sections within a team… topics, projects, disciplines") | Channel ("based on who needs to see them… channel for each team") | Channel ("organize conversations across different topics") | **Core** — universal |
| Channel exists independent of its participants (created as a space, participants change over time) | yes (create → join/invite over time) | yes (created within team; standard open to all members) | yes (subscribe model; content visible to non-subscribed members in public channels) | yes (public channels open to team; members join/leave) | **Core** (Layer C abstraction from A-evidence) |
| Shared persistent sender-attributed message stream, searchable | yes | yes | yes | yes (pin/bookmark/search emphasized) | **Core** — universal |
| Container-level membership ≠ space-level participation | browse/join public channels; private by invitation | standard vs private vs shared channel membership | explicit subscribe/unsubscribe model | join/leave channels; DM/group messages separate | **Core** — universal (the two-level access model) |
| Public/private access modes on spaces | public / private | standard / private / shared | public / private / web-public | public / private (+read-only broadcast) | Core (at least a private-vs-broader distinction); exact mode set = variant |
| Default all-members space (auto-join, announcement-oriented) | #general (cannot archive/delete/convert) | org-wide team option | default channels for new users; "General chat" channels | Town Square (auto-added) | Common (all four have it; shapes differ → not definitional) |
| Person-to-person / small-group direct conversation as side surface | DMs ("one-off conversations") | chats (indirect evidence this pass) | direct messages (org-restrictable) | direct + group message channel types | Common — universal in sample, but side surface; not defining |
| Sub-conversation organization | threads (per-message) | posts/conversations (channel-structured) | topics (first-class, named) | threads | Common — realization varies radically |
| Unread/mention/notification machinery | yes (keyword notifications, DND) | yes (@team/@channel mention settings; moderation) | yes (mention notifications only in subscribed channels; per-channel/per-topic levels) | yes (keyword triggers, muting, badges) | Common |
| Channel lifecycle: active → archived (read-only, history kept) | archive supported | not explicitly fetched this pass | archive a channel | archived type; read-only; history preserved | Common (direct in 3 of 4; Teams treated as common via product structure, low-weight) |
| Roles & governance surfaces | Primary Owner/admins/members/guests | owners/members/moderators; admin-center policies | org roles; channel admins; per-channel permission classes | system roles; team roles; channel admin depth by plan | Common |
| Guests / external participation | guests; Slack Connect (cross-org channels) | guests; shared channels with external participants | guest users (restricted) | (not examined this pass) | Common (external access posture = variant) |
| File/link sharing in spaces | yes | yes (SharePoint-backed) | yes (share and upload files) | yes | Common |
| Search over history | yes | yes (not re-fetched) | yes | yes ("advanced search") | Common |
| Integrations/bots/webhooks/slash commands | apps/marketplace; workflow builder | apps (tabs, connectors, bots) | bots & integrations | slash commands/bots/webhooks (ChatOps) | Common |
| Voice/video calls inside the container | Huddles; calls | (suite) | start a call (external provider configurable) | Calls module (1:1/group audio in channels/DMs) | Optional/Common-side; never definitional |
| Bundled non-conversation modules | Canvas/Lists/Workflow/AI | full M365 suite coupling | polls/to-do lists (light) | Playbooks/Boards/Agents | Optional — packaging, not Type |
| Self-service join of spaces by members | yes (public channels) | yes (public teams, org-scope) | yes (public channels; see-all even unsubscribed) | yes (public channels) | Common behavior inside the org boundary — key for boundary flags |
| Open-to-strangers spaces | no | no | web-public (view-only, opt-in, org-configured) | no | Variant pole (Zulip) — marks the community boundary |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures. Removing any one changes the Type:

1. **Governed organizational membership container.** A persistent container (workspace / team / organization / instance) whose population is admitted and governed by the organization — invitation, domain or directory provisioning, admin policy — with members carrying organization-scoped identity, plus restricted non-member roles (guests). Remove it → open self-join conversation places for strangers → Chat Room / Community Chat territory.
2. **Persistent purpose-organized conversation spaces inside the container.** Named spaces (channels) created around topics, projects, teams, or organizational units; they exist before and independent of any specific participant set, persist over time, and carry their own visibility/access rules. Remove it (spaces become participant-defined groups) → Group Messaging; remove the purpose-organization (one undifferentiated flood) → bare chat room; remove persistence → ephemeral sync/meeting tool.
3. **Shared message stream as organizational memory.** Conversation in a space is a single sender-attributed stream retained as history — readable by the space's members over time, including members who join after the conversation happened — and discoverable (search) as the organization's memory. Remove it → live/ephemeral communication, not team messaging.

Joint load-bearing checks (Layer C):

- 1 alone = a governed roster with no conversation spaces (identity/deployment surface, not messaging Type).
- 2 without 1 = room-shaped chat without organizational population (Chat Room / Community Chat).
- 3 without 2 = person-addressed message archive (IM).
- 1+2 without 3 = spaces with no memory (ephemeral rooms).
- 1+3 without 2 = personal threads among org members (IM on an org account).

### L1 — Common Mature Structure (expected in the market, not definitional)

- Person-to-person and small-group direct conversations as a side surface (every sampled product; Mattermost even types them as channels, but they are participant-defined lightweight objects — Mattermost's own "convert group message to private channel" operation marks the seam).
- Sub-conversation organization: threads (Slack, Mattermost), posts/conversations (Teams), first-class topics (Zulip).
- Two-level access model: container membership vs space participation (join/subscribe/invite; public vs private spaces).
- Default all-members / announcement space auto-provisioned for new members (#general / Town Square / org-wide team / default channels).
- Unread state, mentions (users, groups, spaces), per-space notification levels, keyword triggers, muting, presence/status.
- Roles: owner/admin/member (+moderator, +guest); per-space admin surfaces.
- Channel lifecycle: create → active → archive (read-only, history preserved); rename/describe/purpose fields.
- Message mechanics: edit/delete (policy-governed), reactions, formatting, pinning/bookmarking, forwarding/moving.
- File/link sharing in spaces; search over history (messages, files, people, spaces).
- External collaboration posture: guests; cross-organization shared spaces (Slack Connect, Teams shared channels).
- Integrations: bots, webhooks, slash commands, app platforms.
- Voice/video calls in space context.

### L2 — Variant / Optional Structure

- Container shape: flat workspace of channels (Slack) vs two-level team → channel (Teams, Mattermost) vs org + folders (Zulip) vs multi-workspace enterprise grids (Slack Enterprise-class). Depth varies; the container itself is invariant.
- Space access mode set: public/private (all), shared (Teams), web-public read-only (Zulip), read-only broadcast (Mattermost Enterprise). Mode vocabulary is product vocabulary.
- History-visibility policy on joining a private space (Zulip shared vs protected history; others commonly full-history).
- Deployment: SaaS, self-hosted, sovereign/air-gapped (Mattermost pole), open source (Mattermost, Zulip).
- Organization type: company/team pole vs open community pole (Zulip organization types incl. communities directory) — same structures, different population posture; the community pole is the drift vector toward Community Chat Platform.
- Suite bundling: docs, tasks/boards, meetings, AI assistants packaged around the messaging core — packaging, not Type.
- Topic-required / structured posting regimes (Zulip require-topics; Teams channel moderation).
- Retention/compliance machinery depth (retention policies, audit exports, e-discovery posture) — depth varies by customer segment.

### L3 — Vendor-specific (research notes only; not in final document)

- Slack: #general un-archivable/un-deletable/un-convertible; temporary channel joining; Canvas/Lists/Huddles/Clips; channel templates; Slack Atlas; Enterprise Key Management; Workflow Builder.
- Teams: standard/private/shared channel triple with a feature matrix (guests allowed in standard/private but not shared; moderation only in standard; dedicated SharePoint site for private/shared); org-wide team; M365 group sync; SharePoint-backed files; Planner/tabs/connectors.
- Mattermost: Town Square; group message 3–7 person range; DM DND/off-hours warning (v10); group-message→private-channel conversion (v9.1); archived-private distinct icon (v11.5); read-only broadcast channels; Playbooks/Boards/Calls/Agents modules.
- Zulip: topics first-class with rename/resolve/move/delete; per-channel "who can start topics"/"topics required"; web-public via "public access option"; email-in to channels; read receipts; private-channel metadata-vs-content governance split (admins see metadata, not content).

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the three-leg L0?

- **Room-chat generation (Campfire-era, mid-2000s):** company account (governed membership), rooms created per project/team (persistent purpose spaces), transcript retained (shared memory). Fits all three legs with no threads, no reactions, no DMs-as-first-class, no notifications depth — confirming those are L1, not L0. (Held as conceptual lineage from documented product history; not re-fetched this pass — low-weight, directionally strong.)
- **IRC team-server deployments:** channels persistent and purpose-organized, but the server population is self-service and pseudonymous with no org governance — fails leg 1 → correctly classified as Chat Room pole, not Team Messaging. This failure case validates leg 1 as load-bearing.
- **Carrier group SMS / mailing lists:** participant-defined, person-addressed — fail leg 2 → Group Messaging / list territory.
- **Suite-embedded and regional products** (e.g., current East-Asian enterprise messaging suites): same container/channel/memory structures under different names; no sampled evidence contradicts the three legs.

Conclusion: the definition is not over-fit to the Slack-shaped present. The one deliberate abstraction vs the naive market image: "channel" is canonically a *persistent purpose-organized space inside a governed container*, not "Slack-style flat public/private channel list"; and self-join of public spaces by members is Common behavior *inside* the org boundary, not a boundary violation.

## Vendor-specific / Rejected Findings

Rejected from the canonical core (with reasons):

- **Threads as per-message reply trees** — Zulip implements the same job with first-class topics; Teams with channel-structured posts. The job (organized sub-conversation) is Common; the per-message mechanism is one realization. (Also matches the example pass's uncertainty.)
- **DMs as defining** — present in all four products but as a side surface; the Type's center of gravity is the shared space (Slack's own docs frame DMs as "one-off"). Placed L1.
- **File storage backends** (SharePoint coupling in Teams) — implementation detail.
- **Default general/announcement space** — universal in sample but policy shapes differ (channel vs team vs default-channel-list); Common, not defining.
- **Bundled work modules** (Lists/Canvas/Playbooks/Boards/Agents/polls) — Optional packaging; multiple vendors prove they are add-ons around a stable messaging core.
- **Numeric limits** (Teams 10,000-member org-public teams; Mattermost group-message 3–7; org-wide ≤10,000) — vendor facts, L3/research-notes only.
- **AI features** — current-era packaging; excluded from definition.

## Boundary Findings

### vs Instant Messaging Application — CONFIRMED (discharges IM-side note)

The conversation's primary object is the persistent named space inside an organizational container, not the person-addressed thread bound to a personal reachability graph. Identity is organization-scoped membership; the population is the org roster plus governed guests, not a personal contact graph. DMs exist here but as a side surface (L1) — the mirror image of group chat in IM. Remove the org container and purpose spaces → an IM-like product; add them to an IM → this Type.

### vs Group Messaging Application — CONFIRMED (discharges the group-messaging flag's team-messaging side)

Channels are created as spaces around purposes and pre-date their participants; membership in a channel flows from the container and its access rules (open-to-team, subscribe, admin-added), not from a member-defined invitation graph over personal contacts. The group objects that DO exist inside team messaging (DM/group messages) are participant-defined lightweight conversations, and the products themselves mark the seam (Mattermost converts a "group message" into a "private channel" when it needs persistence/space semantics). The group-messaging pass's "org-provided group containers" drift note is confirmed from this side: when group membership derives from the organization (class groups, department groups), the structure lives on this side of the seam.

### vs Chat Room Application — CONFIRMED (discharges the chat-room flag's team-messaging side)

The chat-room leaf's proposed discriminator — "org-roster membership and org identity behind room-shaped channels" — is confirmed with direct evidence, with one refinement: **self-service join is not the discriminator.** Slack: "All members (but not guests) can browse and join public channels in their workspace"; Zulip: non-guests "subscribe themselves" to public channels. Join mechanics inside the Type are room-like. What makes it Team Messaging: (a) the population eligible to join is pre-defined by governed org membership (employees/invited collaborators/guests), not open strangers; (b) spaces live inside an organizational container with org-scoped identity, roles, and policy; (c) no public directory of stranger-rooms — discovery ends at the container boundary. Remove the governed container → Chat Room.

### vs Community Chat Platform — CONFIRMED with a refinement (discharges the community-chat flag's team-messaging side)

The org-roster vs self-service-join seam holds **at the container level**, not the channel level: apply the test to "who is the population and who governs admission to it", not to individual join buttons. Team messaging: org-defined population (employment/invitation), container closed to outsiders by default, governance by org roles. Community chat: interest-defined population, self-service join to the community, strangers expected, volunteer governance. Drift surfaces documented in-sample: Zulip's **web-public channels** (Internet-readable without account — a read-only leak outward; posting still requires org membership) and Zulip's **organization type = open community** (same container structure serving a community population, with a Communities directory). The structures migrate; the population/governance test decides the Type. When open join, stranger co-presence, and community governance become primary, the product has drifted to Community Chat Platform.

### vs Collaborative Workspace / Team Workspace Platform

The space's primary content is the message stream; workspaces' primary content is persistent authored items (pages/databases) organized in containers. Bundling runs both directions (Teams couples M365 docs; Mattermost ships Boards; Slack ships Canvas/Lists) but is packaging. Remove conversations as the primary object → workspace territory.

### vs Video Conferencing / Conference Calling

Synchronous live meeting is the primary object there; here the persistent textual conversation space is primary and calls are an in-space capability (L1). Remove persistent spaces → meeting tool.

### vs Business Messaging / Customer-to-Business Messaging / Customer Support Chat

Population: internal members + governed guests here; external customers there. Remove the external individual → Team Messaging (as that pass recorded).

### vs Employee Communication Platform / Internal Communication Application

Direction: peer-to-peer multi-party conversation in spaces here; org→workforce authored broadcast/targeting there. A chat surface inside a comms platform is a secondary feature, not the Type.

### vs Clinical Communication Platform

Container here = governed org membership + joinable/assignable spaces; clinical platform = staff directory/assignment + patient/encounter-thread anchoring with escalation rules (as that pass recorded). Org-channel structure alone → Team Messaging.

## Uncertainties

- **Teams chat surface:** the end-user chat article was unreachable this pass (404); Teams person-to-person chat is supported indirectly (product structure, doc metadata) and by Layer-B commonality across the other three products. No Teams-specific chat claims are made in the final document.
- **Channel archive in Teams:** not directly re-fetched this pass; treated as Common via product structure at reduced weight.
- **Historical generation (Campfire-era, IRC):** argued as conceptual lineage from documented product history, not from fresh Tier-1 fetches — claims kept coarse.
- **Exact permission depths** (who can create channels, who can invite, retention defaults) vary per product and plan; deliberately kept out of the final document.
- **Guest/external access in Mattermost** was not examined this pass; external-participation findings rest on Slack/Teams/Zulip (3 of 4).

## Final Synthesis

A Team Messaging Application is defined by three jointly-held structures:

```text
Governed organizational membership container
  (workspace / team / organization: org-admitted members + guests, org-scoped identity, org policy)
└── Persistent purpose-organized conversation spaces
    (named channels around topics/projects/teams; exist before and independent of participants;
     own visibility/access rules; public-private-class access modes)
    └── Shared message stream as organizational memory
        (sender-attributed, persistent, searchable; readable by later members)
```

The Type's organizing principle: **conversation belongs to the space, and the space belongs to the organization** — in deliberate contrast with IM (conversation belongs to the person) and chat rooms/community chat (the place or community belongs to whoever joins it).

Standard capabilities layered on the core: direct conversations, threads/topics, the two-level access model (container membership vs space participation), default announcement spaces, notification machinery, roles, channel lifecycle (archive), message mechanics, file sharing, search, integrations, calls, guests/external collaboration.

Variants: container depth (flat workspace vs team→channel), access-mode sets, deployment (SaaS/self-hosted/air-gapped), organization type (company pole vs open-community pole), suite bundling, topic regimes.

Everything else the market packages onto these products — document/task/meeting/AI modules — is bundling around a stable conversation core, not part of the definition.
