# Optional recurring checkups

A skill file cannot wake itself up, inspect accounts or deliver alerts. A calendar reminder can prompt the person; an agent task can run only within its installed tools and approved scope. Neither proves a review happened. Use provider security/fraud alerts for urgent events; do not wait for the next checkup.

## Agree on a small plan

Ask whether the person wants reminders at all. Offer a monthly 10-minute review as a starting point, or a cadence they prefer. These are practical defaults, not official requirements:

| When | Small review |
| --- | --- |
| Monthly | Ask about unexpected alerts, access problems or changed devices/numbers. User reviews important account alerts/statements and pending updates. Choose one unfinished priority. |
| Every three months, if useful | Rotate main email recovery, sessions/forwarding, password-manager warnings and one backup restore test. Do not repeat a complete inventory every month. |
| Yearly | Review recovery dependencies, supported devices, country protections and emergency contacts. Recheck changing country rules. Retrieve a new IRS IP PIN when applicable. |
| After a change | Revisit affected recovery after a new phone/number, move, lost device, changed email or provider breach notice. Confirm an alert in the official app. |

Offer a near-term follow-up for a blocked priority only if the user wants it. Agree on timezone, local day/time, destination, what may be checked, what needs the user, access limits, retention and pause/delete method. Do not create monitoring access, paid subscriptions or new connectors as part of reminder setup. If needed tools or approvals are absent, use the manual route.

## Portable setup checklist

Use the scheduler's supported UI/API or help. Never invent a product command. Before creation, inspect existing reminders for this purpose with consent so you can update rather than duplicate them. Avoid reading unrelated calendar content.

1. Show the exact proposed reminder/task, recurrence, timezone and notification destination. Ask for approval if not already given. Use a neutral title such as “Personal check-in.” Keep account names and private details out of notifications.
2. For a calendar/reminder app, create a recurring monthly entry at the approved local time; its body can say “Open the private progress note and choose one next step.” This prompts the user and does not run an audit. For a scheduler that supports iCalendar, the recurrence component can be `RRULE:FREQ=MONTHLY;BYMONTHDAY=1`; use the approved day, a future `DTSTART` with the user's IANA timezone and the product's format. Prefer days 1–28 to avoid skipped months. For a task scheduler, use the prompt below within the approved scope. If timezone/DST handling is unsupported or ambiguous, show the limitation and use a calendar reminder or manual fallback.
3. Read the saved task back from the scheduler. Confirm enabled state, task ID, recurrence, timezone, next run and destination against approval. Configuration text or a successful create call alone is insufficient. If creation has an uncertain outcome, inspect before retrying; do not create duplicates.
4. With consent, create a harmless one-time delivery test using the same channel and a neutral message, at the earliest supported time or with a supported run-now feature. A temporary test may notify immediately; say so first. Verify scheduler run/delivery status and have the user confirm receipt. A run request alone does not prove delivery. Remove temporary tests after readback; verify they were removed.
5. Read back the recurring task again after testing; ensure its real next run remains correct. Explain how to pause and resume it. A separate pause/resume test is optional: perform it only when supported and specifically approved, verify readback and restore only the approved enabled state. Otherwise record that it was not tested; do not delete an existing real task merely to test deletion. Record minimal setup metadata privately with permission.
6. Report the exact state: **installed and delivery tested**, **saved but delivery unverified**, **setup failed**, or **manual only**. Say whether any test or pending task remains. Never call a future review “completed” based on installation. If a task was created but failed delivery, disable it with authorization or report its exact remaining state; do not silently leave duplicate jobs.

Declining the delivery test is fine: label delivery unverified. A manual fallback is always available: the user adds a neutral calendar reminder themselves, confirms the saved recurrence/timezone/next event, and checks that notifications arrive. If reminders are unavailable, agree a date or habit (“first weekend of the month”) and provide the resume prompt. Say plainly that nothing was installed. No background checking occurs while waiting.

## Safe task prompt

Copy only after tailoring to the approved scope. Do not place a private tracker path in a shared task.

> Run one short personal security check-in within the user's approved scope. First ask whether anything urgent happened; route urgent trouble to official recovery help. If the user is unavailable, report that the review needs them and stop; do not infer account state. Use only the minimal private progress note the user authorized. Compare dated observations within that scope; distinguish observed, user reported, stale and unknown. Give one prioritized next action and a short done / needs you / not checked summary. Do not sign in, read messages, change settings, send reports, grant access or spend money without exact authorization. Keep secrets, account identifiers and private evidence out of output and notifications. Never mark an unperformed review complete.

## Compare changes and keep notifications quiet

Compare the same scope with a dated baseline. A newly unknown session, recovery change or missed update is a prompt to verify, not automatic proof of takeover. No baseline, missing access or a failed run means **not checked**, not “no change.” Explain the gap and one recovery step. Do not repeatedly scrape accounts or submit identifiers to breach services.

Keep the approved scheduled reminder. For additional agent-generated findings, notify only about a new actionable change, an urgent verified issue, a due user action, or a failed/stale review needing attention. Group routine items into the next digest. Deduplicate by generic item, state and observation date; do not repeat an unchanged warning at every run. Agree when to remind about an overdue action. If a run starts and detects expired account/connector access, report that scoped review as not checked and give a reconnection/manual step; do not expand access or reconnect without approval. A task that never starts or crashes before reporting cannot send its own failure notification. Use and verify native scheduler failure/missed-run notifications if available and approved; otherwise disclose that these failures may go unnoticed and agree on a manual last-run check. Report detected failures neutrally and group repeated unchanged failures into the agreed digest; silence must never be described as a clean review. Do not suppress the bank's or provider's own security alerts.

Allow pause, reschedule and deletion without guilt. On revocation, stop reading the private note and remove/disable only the task the user specifies; verify provider readback. A deleted reminder does not erase provider-retained chat or notes: explain how the user can remove those separately if requested.
