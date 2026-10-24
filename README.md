# Personal security checkup

An agent skill that walks one person, step by step, through securing their digital life: password manager, email, two-step login, phone number, phones, computers, home Wi-Fi, money alerts, breaches, family emergency access, scam habits, and a short monthly check.

The core is country-neutral. Country-specific steps (credit bureaus, tax agency, national ID, carrier rules, fraud reporting) live in modules the agent loads based on where you live and which countries you have ties to.

| File | What it covers |
| --- | --- |
| `SKILL.md` | The core checkup flow and ground rules |
| `countries/us.md` | Living in the US: credit freezes, IRS IP PIN, SSA, carrier locks, FTC reporting |
| `countries/us-person-abroad.md` | US SSN holders living outside the US |
| `countries/argentina.md` | Argentina: BCRA Central de Deudores, Veraz, ARCA Clave Fiscal and Token, Mi Argentina, carriers and \*910, WhatsApp takeover, banks and wallets, No Llame, fraud reporting |
| `countries/other.md` | Template for any other country: what to look up and where |

## Ground rules the agent follows
- Never asks you to type a password, code, PIN, ID number, or card number into the chat. You type those directly into the official site or app.
- Only sends you to official sites and apps.
- Checks and reports before changing anything, and only changes things after you say yes.

## Install

**Agents that support skills** (Claude Code, Cursor, and others that read `SKILL.md` folders): copy the whole folder, including `countries/`, into the agent's skills directory, for example:

```bash
git clone https://github.com/Emuthmartinez/personal-security-checkup.git
cp -r personal-security-checkup ~/.claude/skills/        # Claude Code
# or your agent's own skills folder
```

**Agents without skills support** (any chat assistant): paste the contents of `SKILL.md` into the chat, then paste the country file(s) that apply to you (for example `countries/argentina.md` and `countries/us-person-abroad.md`), then send the kickoff prompt below.

## Kickoff prompt

> Run my personal security checkup. First ask where I live and which other countries I have ID, tax, or bank ties to, and load the matching country modules. Then ask what devices and accounts I have, make me a tracker, and walk me through it one step at a time, most important first. Never ask me to type a password, code, PIN, or ID number into this chat. Check before you change anything, and set up a short monthly check when we're done.

## Notes
- Country facts were checked on official sources in October 2026. Rules and app menus change; the agent is told to trust the official site when it differs.
- This is security guidance, not legal, tax, or financial advice.
- Contributions of new country modules are welcome. Follow `countries/other.md` and link official sources.

## License
MIT. See `LICENSE`.
