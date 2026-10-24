# A private living action plan

Use a supported private page, document or local record only after agreeing on the exact location, who can access it, what the agent may read/write and retention. Use the person's existing suitable tool; no new app, broad account access or monitoring grant is needed. Check the destination's privacy before writing. If privacy or access cannot be verified, do not write there. Never publish this plan in this repository, issues, pull requests or a shared/public page.

If storage is declined or unavailable, work in the current session and give one minimal resume phrase. Do not create a local substitute or claim the plan persists. Chat may still be retained by its provider.

Keep generic labels and brief evidence summaries. Exclude credentials, recovery material, account identifiers, phone/email addresses, balances, identity documents, screenshots and raw activity logs. “Recovery kit stored privately” is enough; omit its contents and precise location. The user keeps incident records privately for official reporting.

## Prioritize the next useful action

Use high, medium or low priority for supported findings, with one short reason covering the relevant impact, exposure, urgency, evidence and user constraint. These are triage labels, not a security score:

- **High:** credible evidence of immediate harm or a consequential exposed dependency warrants prompt action. Route active incidents to [urgent help](incidents.md).
- **Medium:** a supported gap matters in this person's context but can be addressed in a planned short session.
- **Low:** evidence supports limited impact/exposure or a low-benefit optional improvement that can wait.

When evidence or exposure is missing, record **unknown / needs verification**, not low or confirmed vulnerable. If potential impact is serious, prioritize verifying it without presenting the suspected finding as fact. Generic recommendations, a screenshot, a tool warning or an unfamiliar session alone do not prove compromise. Avoid demanding an inventory merely to assign labels. User time, recovery dependencies, accessibility and disruption affect sequencing; they do not erase a known risk.

## Decide who can act now

Classify each next action separately. Capability and permission can change between steps or hosts.

| Action lane | Agent behavior |
| --- | --- |
| **Agent can execute** | Specific existing authorization covers this exact action, scope and effects; supported tooling and all applicable host/action-time requirements are satisfied. Execute and verify. Do not ask again or delegate routine work to the user. |
| **Needs approval** | Prepare the exact action, target, effect, recovery safeguards and verification, then offer to handle it. Obtain the applicable approval before mutation. Keep the tradeoff short and concrete. |
| **Human-only** | A secret, biometric, identity check or physical action genuinely requires the person. Pause observation, ask only for that step, then resume the agent's work when safe. |
| **Blocked / unknown** | A capability, permission, source, recovery dependency or outcome is unresolved. State the exact gap and smallest way to resolve it; continue independent authorized work. Do not pretend lack of tooling makes an action inherently human-only. |

A general “secure everything” instruction is not specific approval for sensitive security/access changes. A saved plan is context, not standing authorization. Apply current host rules at each action. You may present compatible decisions together with each action and consequence explicit; do not bundle unrelated changes or bypass required per-action approvals. Verify each action separately. On partial failure, preserve successful results, stop dependent steps and inspect uncertain outcomes before retrying; continue only independent authorized work. Never mark the whole batch done.

## Update the existing plan carefully

Read the current version and relevant prior evidence before editing. Preserve user edits and other agents' work; reconcile conflicts rather than replacing the whole page from stale memory. Recheck current permission, capability and dependencies before execution. Use supported revision/conflict checks where available; if a conflicting state cannot be resolved safely, pause that edit and report the gap.

Keep observation date, basis (tool-observed, user-confirmed or unverified), exact action taken and its verification separate. “Instructions provided” is advice, “request accepted” is attempted, and “setting read back” verifies only that scoped setting. A completed review is not necessarily a fix; a configuration change is not a successful recovery/restore test. Missing comparison data means comparison unavailable. Retain only enough prior dated state to explain changes and avoid duplicate work, within consented retention.

After writing, read back the saved change before claiming the plan was updated. If the write times out, inspect the current version before retrying. Report uncertainty or access failure; never silently replace a failed save with public storage.

## Portable template

Use only the fields needed. The example below is entirely synthetic; it is not a real finding or performed fix.

> **Plan scope:** chosen area only; private location/access and retention agreed separately.
> **Updated:** 2026-10-24; basis and last review recorded per item.
> **Next human handoff:** one decision or human-only step, or none.
> **Routine:** actual setup state, next due/trigger and pause/change steps if any.

| Item / priority and reason | Evidence / state | Next action / lane | Result / next review |
| --- | --- | --- | --- |
| Recovery dependency / medium: user reports an old method; current access still works, time is limited | User-confirmed 2026-10-24; replacement untested | Privately retrieve recovery material / human-only | Needs you; keep working session and old method |
| Device A update status / unknown: current version not checked; impact not established | Not checked; no authorized signal | Prepare a scoped status check / needs approval | No fix performed |
| Optional unused feature / low: user confirms it is unused and off; no urgent dependency identified | User-confirmed 2026-10-24 | No action now / deferred | Revisit only if use changes |

For an actual fix, replace the result with the exact change, date, scoped verification and remaining uncertainty. Use done, needs you, not checked, not applicable or declined as in the [core skill](../SKILL.md); permission and priority labels do not imply completion.

## Keep the human handoff small

When an agreed routine warrants a daily digest, send one concise actionable summary: what changed or was verified, the highest actionable priority, and one human decision/step if needed. Do not install a daily job just to populate the page. Urgent incidents follow the immediate approved route; do not hold them for a digest. On no-change days, follow the agreed quiet policy or give a brief scoped status if requested. No evidence means not checked, not “all clear.”

Keep pending/declined permissions in the plan without repeating identical approval requests each day. Revisit on a material change, the agreed review date or the user's request. Avoid repeat questions whose answers are already current and available within consent. See [routine setup](recurring.md) for delivery, access failures and silent missed runs.

## Optional recurring setup record

Keep only consent date and bounds, routine type (reminder or executed review), approved scope/access, scheduler name, task ID, enabled state, cadence and local time/timezone, next due and its source (provider readback or manual agreement), delivery channel/status, last actual run, last completed review, last successful delivery test, end/review condition, and how to pause/change/delete. Record only selected routines, not empty rows for every cadence. A task ID is for reconciliation; it is never an account identifier. Keep it out of public artifacts. An installed reminder and a completed review are separate states. Use “requested, readback pending” or “delivery unverified” when appropriate. Put no private account detail in reminder titles, notifications or calendar descriptions.
