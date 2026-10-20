---
id: "00"
title: "Baseline: PostHog plus Self-driving"
status: planned
weeks: 2
hypothesis: "PostHog Self-driving alone, left untouched for two weeks, gives a stable baseline for job completion, error rate and PR merge rate."
metric: "Job completion rate per job (once step 1 exists), errors per 1k sessions, share of Self-driving PRs merged unmodified"
kill_signal: "Baseline numbers move more than 20% week to week with no changes shipped, which means the testbed is too noisy"
decision: null
---

# 00. Baseline: PostHog plus Self-driving

## Hypothesis

PostHog Self-driving alone, left untouched for two weeks, gives a stable baseline for job completion, error rate and PR merge rate.

## Metric

Job completion rate per job (once step 1 exists), errors per 1k sessions, share of Self-driving PRs merged unmodified

## Kill signal

Baseline numbers move more than 20% week to week with no changes shipped, which means the testbed is too noisy

## Method

1. Install PostHog with session replay, error tracking and surveys on the testbed.
2. Run `npx @posthog/wizard@latest self-driving` and enable signal sources.
3. Ship no product changes for two weeks except Self-driving PRs, each logged.
4. Record weekly: sessions, errors per 1k sessions, reports raised, PRs opened, PRs merged unmodified, PRs rejected.

## Output

A baseline table in this file, and the testbed decision in ADR 0004 accepted.

## Results

Not started.

## Decision

Pending: continue, adjust or kill.
