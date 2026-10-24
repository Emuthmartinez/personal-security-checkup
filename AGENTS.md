# Contributing to personal-security-checkup

Read `README.md`, `SKILL.md`, relevant `guides/` and any affected compatibility redirects before edits. This is a portable guidance skill, not an account-audit service. Keep the first interaction and short session output small. Jurisdiction research and maintenance detail load only as needed. Do not restore maintained country playbooks; agents verify current local routes at use time.

- Use isolated branches/checkouts and inspect open issues, pull requests and local ownership before changing shared work. Preserve active owners.
- Use synthetic examples only. No personal inventories, account identifiers, credentials, recovery material, screenshots or raw evidence in commits, fixtures, issues or PRs. Personal progress belongs in a user-approved private location outside this repository. Ignore rules are a guardrail, not a guarantee; inspect the diff.
- Prioritize incident triage and recovery before changes that can lock someone out. Make user versus agent actions explicit. Never equate attempted configuration or user intent with verified completion.
- Verify technical and country claims against current primary sources. Record reusable technical claims and source-method lessons in `guides/sources.md`; keep individual jurisdiction research in consented private notes. Check for superseding rules. A reachable official page can be obsolete. Avoid fixed menu paths, eligibility thresholds and contact numbers unless necessary and verified.
- No security scores, guarantees, automatic account closure, hidden access grants or claims of verified scheduling without readback, or verified delivery without a delivery test. Preserve consent, manual fallback and “not checked” states.
- Local verification: `python3 -m unittest discover -s tests -v`, `git diff --check`, and the synthetic scenarios in `tests/scenarios.md`. No real account audits, sign-ins, settings changes, message sends or persistent scheduled jobs as tests. Explain which provider tests remain unperformed.
- Do not push, publish, merge or enable services without separate user authorization.
