---
id: "02"
title: "Ledger v0"
status: planned
weeks: 2
hypothesis: "Logging every change (human or agent) with a predicted impact, then measuring it after 7 days, is cheap enough to keep doing and produces usable history."
metric: "Entries with a measured outcome; time spent per entry"
kill_signal: "Logging takes more than 5 minutes per change, or fewer than half of entries get measured"
decision: null
---

# 02. Ledger v0

## Hypothesis

Logging every change (human or agent) with a predicted impact, then measuring it after 7 days, is cheap enough to keep doing and produces usable history.

## Metric

Entries with a measured outcome; time spent per entry

## Kill signal

Logging takes more than 5 minutes per change, or fewer than half of entries get measured

## Method

1. Create `ledger/` in the testbed repo with one YAML file per change, using `spec/ledger.schema.json`.
2. Require a ledger entry in every PR description template.
3. After 7 days, fill in `measured` from the job metrics.

## Output

10 entries with measured outcomes, and the prediction error for each.

## Results

Not started.

## Decision

Pending: continue, adjust or kill.
