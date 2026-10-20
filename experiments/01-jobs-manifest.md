---
id: "01"
title: "Jobs manifest v0"
status: planned
weeks: 2
hypothesis: "3 to 5 hand-written jobs with success events and guardrails can be computed daily from PostHog data and match what the owner believes the app is for."
metric: "Daily completion rate per job, computed automatically"
kill_signal: "The owner disagrees with more than one job definition after a week of data, or a job cannot be measured with existing events"
decision: null
---

# 01. Jobs manifest v0

## Hypothesis

3 to 5 hand-written jobs with success events and guardrails can be computed daily from PostHog data and match what the owner believes the app is for.

## Metric

Daily completion rate per job, computed automatically

## Kill signal

The owner disagrees with more than one job definition after a week of data, or a job cannot be measured with existing events

## Method

1. Write `ultrastable.jobs.yaml` in the testbed repo using `spec/jobs.schema.json`.
2. Add any missing success events to the app.
3. Build one PostHog insight or SQL query per job; check numbers by hand against 10 sessions per job.
4. Validate the file with `tools/validate.py`.

## Output

A validated jobs manifest and a daily per-job completion view.

## Results

Not started.

## Decision

Pending: continue, adjust or kill.
