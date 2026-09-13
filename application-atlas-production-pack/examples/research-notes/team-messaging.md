# Research Notes — Team Messaging Application

## Research Goal

Identify the stable product structure of a workplace-oriented Team Messaging Application without importing bundled project-management, document, meeting, or AI modules into the canonical core.

## Initial Boundary

Target:

> Team Messaging Application

Nearest confusing types:

- Instant Messaging Application
- Community Chat Platform
- Video Conferencing Application
- Project Management Application

Working hypothesis:

> Team Messaging is distinguished by persistent organizational conversation spaces, searchable shared history, and membership/access tied to a workplace/team context.

## Research Questions

- What is the top-level organizational container?
- How are conversations organized?
- What distinguishes a channel from a direct conversation?
- How is message context preserved?
- How are membership and visibility controlled?
- What lifecycle does a conversation space have?
- Which modern suite features are merely bundled rather than defining?

## Representative Products

| Product | Why selected |
|---|---|
| Slack | archetypal channel-centered workplace messaging product |
| Microsoft Teams | major enterprise alternative with team/channel/chat and richer enterprise access modes |

Mattermost is a useful additional market reference, but the primary evidence set used here is Slack + Microsoft Teams.

## Sources

Research date: 2026-09-05

### Slack

- What is a channel?  
  https://slack.com/help/articles/360017938993-What-is-a-channel
- How to use Slack: your quick start guide  
  https://slack.com/help/articles/360059928654-How-to-use-Slack--your-quick-start-guide.
- Use threads to organize discussions  
  https://slack.com/help/articles/115000769927-Use-threads-to-organize-discussions
- Getting started for workspace creators  
  https://slack.com/help/articles/217626298-Getting-started-for-workspace-creators

### Microsoft Teams

- Create a standard, private, or shared channel in Microsoft Teams  
  https://support.microsoft.com/en-US/teams/teams-channels/create-a-standard-private-or-shared-channel-in-microsoft-teams

## Product Observations

### Slack

Observed model:

```text
Workspace
├── Channels
│   └── Messages
│       └── Threads
└── Direct Messages
```

Important observations:

- workspace provides organizational context
- channels organize persistent conversation around a purpose
- direct messages provide private/small-group conversation
- threads preserve sub-conversation context
- channel access can be public/private within workspace rules
- channels can be archived
- files/resources can be attached to conversation

### Microsoft Teams

Observed model:

```text
Team
├── Channels
└── Chats
```

Important observations:

- channel is organized around a topic/project/department
- standard/private/shared channel modes create different membership/visibility semantics
- chat exists alongside channel conversation
- enterprise/external collaboration modifies access but does not change the basic conversation model

## Cross-product Comparison

| Finding | Slack | Teams | Canonical decision |
|---|---|---|---|
| organizational container | Workspace | Team | Core |
| persistent channel | yes | yes | Core |
| direct/private conversation | yes | yes | Core |
| message history | yes | yes | Core |
| membership/access model | yes | yes | Core |
| restricted channel type | private | private/shared variants | Common |
| thread/contextual replies | explicit | implementation differs | Common |
| file/resource sharing | yes | yes in product family | Common |
| meetings | bundled | bundled | Optional / adjacent |
| task/project tooling | bundled/extensions | bundled/integrated | Optional / adjacent |

## Canonical Model

```text
Organization / Workspace
│
├── Membership
│
├── Channel
│   ├── Message
│   │   └── contextual reply / thread
│   └── shared history/resources
│
└── Direct Conversation
    └── Message
```

Core property:

> conversation is persistent and discoverable inside an organizational collaboration context.

## Vendor-specific / Rejected Findings

Not part of the canonical Team Messaging core:

- Slack Canvas
- Slack Lists
- Slack AI/agents
- Microsoft 365 document suite integration
- video-meeting feature depth

## Boundary Findings

### vs Instant Messaging

Instant messaging may center on personal contacts and private conversations.

Team Messaging adds:

- organizational container
- persistent shared channels
- team membership/access semantics
- shared workplace context

### vs Community Chat

The structures can look similar, but Team Messaging is primarily organized around work/organization collaboration rather than open/semi-open community participation.

### vs Video Conferencing

Synchronous meeting is primary in video conferencing; persistent textual conversation context is primary here.

## Uncertainties

- threading behavior varies materially across products and should remain Common rather than defining
- external collaboration models differ and should be treated as access variants

## Final Synthesis

Canonical Team Messaging:

```text
persistent organizational conversation
=
workspace/team
+ members/access
+ channels
+ direct conversations
+ messages/history
```
