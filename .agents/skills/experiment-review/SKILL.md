---
name: experiment-review
description: Review a pilot or experiment for a clear hypothesis, metrics, comparison, sampling, guardrails and decision rules. Use for experiment design or outcome reviews rather than generic document review.
---

# Experiment review

Read the experiment and linked measurement definitions. Distinguish a prospective design review from an evaluation of actual results; assess only evidence available for that mode.

Check:
- The hypothesis connects an intervention and population to an observable outcome. Identify concurrent changes that could confound attribution.
- The primary metric defines numerator, denominator, unit of analysis, eligibility, exclusions, observation window and data source. Distinguish relative improvement from percentage-point change.
- Baseline and comparison use compatible definitions. Assignment and analysis units are explicit. Check spillovers, shared participants, selection bias and seasonality; observational comparisons warrant weaker causal conclusions than random assignment.
- Cohorts are defined before analysis, including how low exposure or other targeting is measured. Do not silently change membership based on post-treatment behavior.
- Duration, minimum usable sample, sample rationale and review date are set or assigned for validation. Do not invent power, significance or universal sample sizes. Explain what replay or a small operational check can establish.
- Instrumentation captures required events and timestamps. For Dispatch, do not equate send with confirmed display, quiet phones with delivery failure, or assumed history scores with production measurements.
- Guardrails define thresholds, measurement windows, monitoring responsibility and pause/rollback actions. Expansion, failure and inconclusive-result rules are explicit.

Return a concise assessment and table of **Pass / Needs clarification / Missing**, evidence references and smallest fixes. Use Needs clarification for ambiguous, contradictory or unverified claims and Missing for absent requirements. Explain justified inapplicable checks. For results, report coverage and uncertainty alongside observed changes; avoid causal claims the design cannot support. Identify decisions that must wait for evidence.

Review only unless edits are requested. Clarify definitions and label assumptions without inventing baselines, targets, sample requirements, approvals or results. Do not launch experiments or alter source data.
