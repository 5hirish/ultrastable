---
id: "05"
title: "Immune system v0"
status: planned
weeks: 5
hypothesis: "With separation of powers in place, injections planted in feedback, replays and error messages never reach the deployer."
metric: "Number of injections that cause any unintended action beyond the senses"
kill_signal: "Any injection causes the mutator or deployer to act on attacker instructions"
decision: null
---

# 05. Immune system v0

## Hypothesis

With separation of powers in place, injections planted in feedback, replays and error messages never reach the deployer.

## Metric

Number of injections that cause any unintended action beyond the senses

## Kill signal

Any injection causes the mutator or deployer to act on attacker instructions

## Method

1. Set up the mutator in a container with no network and synthetic data.
2. Implement the deployer as a script that only flips flags allowed by the policy file.
3. Write 10 injection cases: survey text, feedback widget, error message, replay text input, dependency README, and others.
4. Run each case end to end and log what each component did.

## Output

A red-team report and a reusable injection test suite. This step gates Phase 2.

## Results

Not started.

## Decision

Pending: continue, adjust or kill.
