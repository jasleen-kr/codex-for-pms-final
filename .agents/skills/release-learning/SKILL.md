---
name: release-learning
description: Review post-release evidence against original goals and guardrails, then propose lessons and owned follow-up work. Use for release retrospectives and pilot outcomes rather than pre-launch readiness checks.
---

# Release learning

Read the original plan and available release notes, metrics, incidents, research and support evidence. Establish actual release date, exposure, shipped changes and observation window. If results are unavailable, assess gaps and propose a review structure rather than inventing a retrospective.

Compare:
- Intended outcome, baseline, target and guardrails with observed results using consistent definitions, cohorts and periods.
- Overall outcomes with distribution across affected users and dependencies. Separate adoption, implementation correctness and user benefit.
- Quantitative trends with support and research. Reports describe reported experiences, not automatically independent customers or verified incidents.
- Expected behavior with surprises, unresolved defects and missing instrumentation. Separate association from causation, especially when multiple changes shipped together.

For this course, label replayed scores, modeled rankings and prototype interactions as simulations. Account for partial coverage, release-day treatment, zero-activity rows and elapsed-time denominators where relevant.

Return a concise assessment of whether goals and guardrails were met, missed or remain inconclusive. Include a table of review areas rated **Pass / Needs clarification / Missing**, with evidence references and smallest corrections: these rate evidence coverage, not release success. Needs clarification means ambiguous, contradictory or unverified evidence; Missing means absent evidence. Explain justified inapplicable checks.

List useful follow-ups with action, proposed owner or unassigned status, rationale, success evidence and proposed review trigger. Separate confirmed decisions from recommendations. Explain roadmap implications as proposals to continue, adjust, stop or investigate; Product confirms commitment changes.

Review only unless a saved report or edits are requested. Save requested outputs inside the project. Do not invent agreement, completed follow-ups, dates or outcomes. Do not send messages or change production systems.
