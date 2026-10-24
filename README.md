# Personal security checkup

A step-by-step security checkup for you and your AI assistant. Start with one useful action, know what needs your attention, and build a routine you can keep up with.

The guide helps you protect access to email and other important accounts, check phone and device protections, plan recovery, and find the right local help. You can start with five minutes and stop with a clear place to resume.

**Something happening now?** If money is moving without your permission, an account is taken over, or your phone is missing, start with [urgent help](guides/incidents.md). For money at risk, contact the bank or payment provider through its official app or a known number immediately.

## Start with your agent

1. Give your agent this repository and ask it to read [SKILL.md](SKILL.md). It should load the linked guides when needed. If it cannot read repository files, paste or attach the skill and the guides it requests.
2. Send the prompt below. The agent should first check for urgent trouble, then help with one step you have time for.
3. Before you finish, choose a useful follow-up: a supported reminder or review, a manual routine, or a clear decision to defer or decline.

> Help me with a personal security checkup, one small step at a time. First check whether anything urgent is happening and how much time I have. Explain why each step matters, what you can do, what needs me, and how we will know it worked. Keep secrets and account details out of chat. Help me set up a small ongoing routine that fits my needs and your actual tools. Ask before saving notes, changing settings or creating tasks. Let me stop and resume.

If your agent supports installable skill folders, follow that agent's current installation instructions and keep the repository's guides and examples with `SKILL.md`. Agents differ in how they load files, browse official sources and schedule tasks; this guide does not add those capabilities.

## What a session looks like

The agent checks for urgent problems first, then helps preserve recovery access and protect your main email. It owns research, preparation and supported actions you specifically authorize, so you handle only the choices and private steps that need you. It asks about other accounts and devices only as needed.

A fictional first action:

> **Next:** check your main email's recovery options, about three minutes.
>
> **Why:** this email may help you get back into other accounts.
>
> **I can:** find your provider's official instructions and explain them.
>
> **You do:** open the account's security settings yourself and check whether the recovery methods are yours and still accessible. Keep their values private.
>
> **Check:** tell me only “I can use them,” “one is old,” or “not sure.”
>
> **Stop here:** if you cannot use them, pause changes and take the official recovery route.

A short session ends with something like:

> **Done:** email recovery checked today, confirmed by you.
>
> **Needs you:** find your recovery kit privately before changing login methods.
>
> **Not checked:** phone and bank alerts.
>
> **Resume:** “Continue at email login protection.”
>
> **Routine:** deferred; nothing is scheduled.

“Done” names the specific action and its evidence. An unchecked item stays visible. You never need to finish a whole checklist to make progress. See [more fictional conversations](examples/conversations.md), including getting stuck and recovering from a takeover.

With your consent, the agent can keep a [private living action plan](guides/private-tracker.md) in a supported page, document or local record. It separates priorities, unknowns, permissions and dated verified results, then brings you one useful next action. You can use the checkup without saving anything.

## Local guidance when you need it

The agent researches current official guidance for the next action wherever you live. Your residence, the country of an account and the issuer of an identity document may differ. It asks only for the country context that matters, never your ID number or a document copy.

Local protections and reporting routes change. The agent checks the responsible authority, who the guidance applies to, and whether newer rules replace it. If it cannot verify a route, it says so and can continue with useful general steps. The [local-research guide](guides/jurisdictions.md) replaces maintained country checklists; it is not a promise of complete coverage in every country.

## Build a routine that fits

The agent helps you choose what is worth repeating. These are options, not five required tasks:

| When | What it might look like |
| --- | --- |
| Daily | Existing provider alerts, or an approved check of an available signal that only notifies you when action is needed |
| Weekly | One unfinished priority, with follow-ups ending when it is resolved |
| Monthly | A short review of one area, such as recovery, important alerts, updates or a backup restore |
| Yearly | A review tied to a real renewal or recovery need; skip it if there is no reason |
| After a change | Revisit affected protections after a new phone, a move, lost access or an unexpected alert |

The agent checks what it can schedule and access, agrees the scope, time, timezone and destination with you, and creates only supported tasks you approve. It checks the saved details and tests delivery with your consent where possible. You get the actual setup status, next due date and a way to pause or change it.

A reminder prompts you; a review checks only what the agent can access with permission. Neither proves an account issue was fixed. Daily routines never mean daily password resets or full audits. Without scheduling support, the agent helps you choose a calendar reminder or manual habit and makes clear that no agent routine is running. You can defer or decline. [Routine setup details](guides/recurring.md) cover missed runs, duplicate prevention and quiet notifications.

## You stay in control

- Enter passwords, codes, PINs and identity details directly in official apps while the agent is not observing. Keep enrollment QR codes, recovery material and screenshots containing secrets out of chat.
- The agent explains consequential changes and obtains the required action-specific approval; it reuses valid specific authorization when host rules allow. Recovery comes before changes that could lock you out; a checkup is not permission to wipe devices, close accounts or remove recovery methods.
- Save only the minimal progress note you want, somewhere private outside this public repository. Keep real account inventories and evidence out of issues, pull requests and examples. Chat may also be retained by its provider. See [private progress notes](guides/private-tracker.md).
- A skill file does not monitor accounts or install reminders by itself. Tool access, saved tasks, delivery and completed reviews need separate evidence. There is no security score or guarantee of safety.

This is guidance, not legal, tax or financial advice. The [source notes](guides/sources.md) describe what was checked and what needs fresh verification.

## Contribute

Read [AGENTS.md](AGENTS.md). Use fictional data only. Prefer one useful next action over a longer checklist, and support technical claims with current official sources.

Run `python3 -m unittest discover -s tests -v` for offline link and skill-metadata checks. The [behavior scenarios](tests/scenarios.md) support further review. These checks do not audit real accounts or prove that a scheduler or agent will behave correctly.

[MIT license](LICENSE).
