---
name: release-readiness
description: Review a release plan before a pilot, launch or rollout decision for ownership, dependencies, validation, monitoring and rollback. Use for launch-readiness reviews rather than ordinary brief proofreading.
---

# Release readiness

Read the release brief and linked spec, validation results and rollout plan available in the project. Identify the intended launch stage. Distinguish planned checks from completed evidence. If the release artifact is unclear, locate likely project files and ask only if the choice remains ambiguous.

Check:
- An accountable owner, decision-maker, intended users, problem, scope and exclusions are explicit. Timing is labeled as proposed or committed.
- Dependencies have owners and a resolution path before launch. For Dispatch, consider eligibility, ranking state, offer timing and the availability update Supply consumes when affected.
- The changed experience has relevant handler/responder validation and engineering checks. A clickable concept or planned test does not establish validation or production behavior.
- Metrics, measurement sources, baseline, guardrails and review points are defined. Necessary telemetry works before exposure begins.
- Rollout specifies initial cohort, exposure stages, monitoring owner and cadence, expansion criteria and decision authority.
- Pause and rollback triggers, operators, state restoration and verification are covered. A feature flag alone is not evidence of a tested rollback.
- Support preparation and user communication are covered when the change affects expectations or workflows.

Return an advisory assessment for the requested stage and a concise table: check, **Pass / Needs clarification / Missing**, evidence with file/section references, and smallest corrective action. Use Needs clarification for ambiguous, contradictory or unverified claims; Missing for absent requirements. Prioritize launch blockers. Mark an inapplicable check as Pass with a reason rather than forcing unnecessary process.

Do not declare the release approved, operate a rollout or contact anyone. Review only unless edits are requested. When fixing a plan, update authorized project files, label unconfirmed choices as proposals and leave actual validation and approvals pending. Do not invent completed checks, owners, dates, rollout percentages or results.
