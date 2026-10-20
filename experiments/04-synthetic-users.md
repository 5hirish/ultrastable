---
id: "04"
title: "Synthetic users v0"
status: planned
weeks: 4
hypothesis: "Agent personas attempting the jobs on staging predict the direction of real outcomes for past changes in the ledger."
metric: "Agreement between synthetic and real outcome direction on 2 to 3 past changes"
kill_signal: "Direction wrong on most past changes, or results unstable across reruns"
decision: null
---

# 04. Synthetic users v0

## Hypothesis

Agent personas attempting the jobs on staging predict the direction of real outcomes for past changes in the ledger.

## Metric

Agreement between synthetic and real outcome direction on 2 to 3 past changes

## Kill signal

Direction wrong on most past changes, or results unstable across reruns

## Method

1. Build 3 to 5 personas from replay patterns (new user, power user, mobile user, struggling user).
2. Check out the version before and after each chosen ledger change on staging.
3. Run each persona on each job 10 times per version; record completion and time.
4. Compare with the measured impact in the ledger.

## Output

A go or no-go on synthetic users as a pre-release fitness signal. This step gates Phase 2.

## Results

Not started.

## Decision

Pending: continue, adjust or kill.
