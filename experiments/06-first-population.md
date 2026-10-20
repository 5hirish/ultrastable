---
id: "06"
title: "First population"
status: planned
weeks: 4
hypothesis: "Three variants of one screen, generated against the jobs manifest and run behind flags, produce a winner selected on job completion."
metric: "Job completion difference between variants, with confidence interval"
kill_signal: "No variant beats control after 2 weeks, or traffic too low to detect a 10% relative change"
decision: null
---

# 06. First population

## Hypothesis

Three variants of one screen, generated against the jobs manifest and run behind flags, produce a winner selected on job completion.

## Metric

Job completion difference between variants, with confidence interval

## Kill signal

No variant beats control after 2 weeks, or traffic too low to detect a 10% relative change

## Method

1. Pick one screen tied to the weakest job.
2. Generate 3 variants with the mutator; pass all through replay tests and synthetic users.
3. Run as an OpenFeature or PostHog experiment.
4. Record the result in the ledger and compare with a single-PR approach.

## Output

A documented selection run and the first evidence on populations versus single PRs.

## Results

Not started.

## Decision

Pending: continue, adjust or kill.
