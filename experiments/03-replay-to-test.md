---
id: "03"
title: "Replay to test"
status: planned
weeks: 3
hypothesis: "The top 20 sessions per job can be turned into scrubbed Playwright tests that catch real regressions."
metric: "Share of planted regressions caught; flaky test rate"
kill_signal: "Fewer than 3 of 5 planted regressions caught, or flaky rate above 10%"
decision: null
---

# 03. Replay to test

## Hypothesis

The top 20 sessions per job can be turned into scrubbed Playwright tests that catch real regressions.

## Metric

Share of planted regressions caught; flaky test rate

## Kill signal

Fewer than 3 of 5 planted regressions caught, or flaky rate above 10%

## Method

1. Export successful sessions per job from PostHog replay.
2. Scrub personal data (emails, names, free text) and replace with canary values.
3. Generate Playwright tests with an agent; review and fix by hand.
4. Plant 5 regressions on a branch and run the suite.

## Output

A replay-derived test suite in CI and a write-up of the conversion method.

## Results

Not started.

## Decision

Pending: continue, adjust or kill.
