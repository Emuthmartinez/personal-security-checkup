# Personal security checkup

A calm guide for ordinary people and their agents. Start with what is happening today, take one useful step, and stop with a clear place to resume. You do not need to understand security jargon or finish a long checklist.

If money is moving without your permission, you lost account access, or your phone was stolen, start with [urgent help](guides/incidents.md). Use the bank's official app or a known number to contact it now.

## Start

Give your agent this prompt after loading the skill:

> Help me with a personal security checkup, one small step at a time. First check whether anything urgent is happening and how much time I have. Explain why each step matters, what you can do, what needs me, and how we will know it worked. Keep secrets and account identifiers out of chat. Let me stop and resume. Ask before saving private notes or setting reminders.

The agent starts with urgent triage, recovery and main email. It asks about countries and devices as needed, then helps with phone, money, devices and country protections. Each short session ends with **done / needs you / not checked**, with the evidence behind “done.” There is no security score or promise that accounts are safe.

## Load the skill

For an agent that supports skill folders, copy this folder into that agent's documented skills directory. Keep `SKILL.md`, `countries/`, `guides/` and `examples/` together. Skill installation differs by agent; check its current instructions. Loading the skill grants no account access or recurring monitoring.

For an ordinary chat assistant, paste [SKILL.md](SKILL.md) first. When it requests a linked guide or country module, paste that file too. If it cannot load the needed guidance or verify an official source, it should explain the gap and pause that step.

## What you control

You sign in and enter passwords, codes, PINs and identity details directly in official apps, out of the agent's view. The agent researches, explains and keeps only the minimal private progress notes you approve. It asks before any change. Recovery comes before changes that could lock you out.

Keep real trackers, inventories and evidence outside this public repository, issues and pull requests. Use generic labels in chat. Even private chat may be retained by its provider. The examples here are fictional. [Privacy and evidence rules](guides/private-tracker.md) explain what a useful record can contain.

## Guides

| Guide | Use it for |
| --- | --- |
| [Core skill](SKILL.md) | The agent's order, boundaries and one-action response format |
| [Urgent help](guides/incidents.md) | Account takeover, lost phone, money fraud, identity misuse |
| [Recurring checkups](guides/recurring.md) | Optional reminders, realistic cadence, setup/readback tests and manual fallback |
| [Synthetic conversations](examples/conversations.md) | First use, getting stuck, takeover and a routine review |
| [US](countries/us.md), [US abroad](countries/us-person-abroad.md), [Argentina](countries/argentina.md), [other countries](countries/other.md) | Local protections and official support routes |
| [Sources](guides/sources.md) | Verified claims and things to recheck |

The skill does not install reminders or continuously watch accounts. Recurring setup must be consented to, read back from the scheduler and tested. Manual calendar reminders work when agent scheduling is unavailable.

## Contribute and check

Read [AGENTS.md](AGENTS.md). Use synthetic data only. Prefer fewer useful actions over a longer checklist. Link current official sources, state limitations, and preserve recovery paths. Guidance is not legal, tax or financial advice.

Run the offline checks with `python3 -m unittest discover -s tests -v`. They validate packaged local links and skill metadata. They do not audit accounts, install reminders or prove real-world security.

MIT license. See [LICENSE](LICENSE).
